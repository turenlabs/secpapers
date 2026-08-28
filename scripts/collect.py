#!/usr/bin/env python3
"""Collect LLM security papers from arXiv and render repository outputs."""

from __future__ import annotations

import argparse
import csv
import html
import http.client
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
OPEN_SEARCH = "{http://a9.com/-/spec/opensearch/1.1/}"
USER_AGENT = "secpapers/1.0 (+https://github.com/turenlabs/secpapers)"
MAX_FEED_BYTES = 8 * 1024 * 1024
MAX_RETRY_DELAY_SECONDS = 60
ALLOWED_ARXIV_HOSTS = {"arxiv.org", "export.arxiv.org"}
ARXIV_ID = re.compile(r"(?:\d{4}\.\d{4,5}|[a-z][a-z0-9.-]*/\d{7})", re.IGNORECASE)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "config" / "topics.json",
        help="collection and taxonomy configuration",
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=ROOT / "data" / "papers.json",
        help="canonical JSON dataset",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        help="override the configured number of recent API results",
    )
    parser.add_argument(
        "--offline-feed",
        type=Path,
        help="parse an Atom fixture instead of contacting arXiv",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="regenerate outputs from existing JSON without network access",
    )
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    existing = load_papers(args.data)

    if args.render_only:
        papers = merge_papers(existing, [], config)
    else:
        max_results = args.max_results or config["max_results"]
        if max_results < 1:
            parser.error("--max-results must be greater than zero")
        fetched = (
            parse_feed(args.offline_feed.read_bytes())
            if args.offline_feed
            else fetch_papers(config, max_results)
        )
        if not fetched:
            raise RuntimeError("arXiv returned no papers; refusing to replace outputs")
        papers = merge_papers(existing, fetched, config)

    write_outputs(papers, config, args.data)
    print(f"SecPapers catalog contains {len(papers)} papers")


def fetch_papers(config: dict, max_results: int) -> list[dict]:
    papers = []
    batch_size = min(config["batch_size"], max_results)

    for start in range(0, max_results, batch_size):
        if start:
            time.sleep(config["request_delay_seconds"])
        query = urllib.parse.urlencode(
            {
                "search_query": config["query"],
                "start": start,
                "max_results": min(batch_size, max_results - start),
                "sortBy": "lastUpdatedDate",
                "sortOrder": "descending",
            }
        )
        request = urllib.request.Request(
            f"{config['api_url']}?{query}", headers={"User-Agent": USER_AGENT}
        )
        page = fetch_with_retries(request, config["request_delay_seconds"])
        papers.extend(page)
        if len(page) < min(batch_size, max_results - start):
            break

    return papers


def fetch_with_retries(request: urllib.request.Request, delay: float) -> list[dict]:
    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                validate_response_url(response.geturl())
                payload = response.read(MAX_FEED_BYTES + 1)
                if len(payload) > MAX_FEED_BYTES:
                    raise RuntimeError(
                        f"arXiv response exceeds {MAX_FEED_BYTES} byte limit"
                    )
                return parse_feed(payload)
        except urllib.error.HTTPError as error:
            if error.code != 429 and error.code < 500:
                raise RuntimeError(f"arXiv request failed with HTTP {error.code}") from error
            last_error = error
            if attempt < 2:
                retry_after = error.headers.get("Retry-After") if error.headers else None
                time.sleep(
                    min(float(retry_after), MAX_RETRY_DELAY_SECONDS)
                    if retry_after and retry_after.isdigit()
                    else delay * (attempt + 1)
                )
        except (
            urllib.error.URLError,
            TimeoutError,
            ConnectionError,
            http.client.HTTPException,
            ET.ParseError,
        ) as error:
            last_error = error
            if attempt < 2:
                time.sleep(delay * (attempt + 1))

    raise RuntimeError(f"failed to fetch arXiv after 3 attempts: {last_error}") from last_error


def validate_response_url(value: str) -> None:
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_ARXIV_HOSTS:
        raise RuntimeError(f"arXiv redirected to untrusted URL: {value}")


def parse_feed(payload: bytes) -> list[dict]:
    if len(payload) > MAX_FEED_BYTES:
        raise ValueError(f"Atom feed exceeds {MAX_FEED_BYTES} byte limit")
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("Atom feed contains a forbidden DTD or entity declaration")
    root = ET.fromstring(payload)
    return [parse_entry(entry) for entry in root.findall(f"{ATOM}entry")]


def parse_entry(entry: ET.Element) -> dict:
    raw_id = required_text(entry, f"{ATOM}id")
    parsed_id = urllib.parse.urlparse(raw_id)
    if (
        parsed_id.scheme not in {"http", "https"}
        or parsed_id.hostname not in ALLOWED_ARXIV_HOSTS
        or not parsed_id.path.startswith("/abs/")
        or parsed_id.query
        or parsed_id.fragment
    ):
        raise ValueError(f"arXiv entry has an invalid identifier URL: {raw_id}")
    versioned_id = parsed_id.path.removeprefix("/abs/")
    version_match = re.fullmatch(rf"({ARXIV_ID.pattern})v(\d+)", versioned_id, re.IGNORECASE)
    if version_match is None:
        raise ValueError(f"arXiv entry has an invalid identifier: {versioned_id}")
    paper_id = version_match.group(1)
    categories = [item.attrib["term"] for item in entry.findall(f"{ATOM}category")]
    if not categories:
        raise ValueError(f"arXiv entry {paper_id} has no categories")
    primary = entry.find(f"{ARXIV}primary_category")

    return {
        "id": paper_id,
        "version": int(version_match.group(2)),
        "title": clean_text(required_text(entry, f"{ATOM}title")),
        "authors": [
            clean_text(required_text(author, f"{ATOM}name"))
            for author in entry.findall(f"{ATOM}author")
        ],
        "abstract": clean_text(required_text(entry, f"{ATOM}summary")),
        "categories": sorted(set(categories)),
        "primary_category": primary.attrib["term"] if primary is not None else categories[0],
        "published": required_text(entry, f"{ATOM}published"),
        "updated": required_text(entry, f"{ATOM}updated"),
        "url": f"https://arxiv.org/abs/{paper_id}",
        "pdf_url": f"https://arxiv.org/pdf/{paper_id}",
        "doi": optional_text(entry, f"{ARXIV}doi"),
        "journal_ref": optional_text(entry, f"{ARXIV}journal_ref"),
        "comment": optional_text(entry, f"{ARXIV}comment"),
    }


def required_text(element: ET.Element, path: str) -> str:
    child = element.find(path)
    if child is None or child.text is None:
        raise ValueError(f"arXiv entry is missing required field {path}")
    return child.text.strip()


def optional_text(element: ET.Element, path: str) -> str | None:
    child = element.find(path)
    if child is None or child.text is None:
        return None
    return clean_text(child.text)


def clean_text(value: str) -> str:
    return " ".join(value.split())


def load_papers(path: Path) -> list[dict]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or not isinstance(payload.get("papers"), list):
        raise ValueError(f"unsupported dataset shape in {path}")
    return payload["papers"]


def merge_papers(existing: list[dict], fetched: list[dict], config: dict) -> list[dict]:
    by_id = {}
    for paper in [*existing, *fetched]:
        current = by_id.get(paper["id"])
        if current is None or paper_revision_key(paper) > paper_revision_key(current):
            by_id[paper["id"]] = paper

    enriched = [enrich_paper(paper, config) for paper in by_id.values()]
    return sorted(
        [paper for paper in enriched if paper is not None],
        key=paper_sort_key,
        reverse=True,
    )


def paper_sort_key(paper: dict) -> tuple[str, str, int, str]:
    return (
        paper["updated"],
        paper["published"],
        paper.get("version", 1),
        paper["id"],
    )


def paper_revision_key(paper: dict) -> tuple[int, str]:
    return (paper.get("version", 1), paper["updated"])


def enrich_paper(paper: dict, config: dict) -> dict | None:
    if ARXIV_ID.fullmatch(paper["id"]) is None:
        raise ValueError(f"dataset contains an invalid arXiv identifier: {paper['id']}")
    if not set(paper["categories"]).intersection(config["allowed_categories"]):
        return None

    llm_in_title = matching_terms(paper["title"], config["llm_terms"])
    llm_in_abstract = matching_terms(paper["abstract"], config["llm_terms"])
    security_in_title = matching_terms(paper["title"], config["security_terms"])
    security_in_abstract = matching_terms(paper["abstract"], config["security_terms"])

    if not (llm_in_title or llm_in_abstract):
        return None
    if not (security_in_title or security_in_abstract):
        return None

    score = (
        (3 if llm_in_title else 1)
        + (3 if security_in_title else 1)
        + (2 if "cs.CR" in paper["categories"] else 0)
    )
    if score < config["minimum_relevance_score"]:
        return None
    combined = f"{paper['title']} {paper['abstract']}"
    if not (
        (llm_in_title and security_in_title)
        or "cs.CR" in paper["categories"]
        or matching_terms(combined, config["strong_security_terms"])
    ):
        return None

    topics = [
        topic["id"]
        for topic in config["topics"]
        if matching_terms(combined, topic["keywords"])
    ]

    return {
        "id": paper["id"],
        "version": paper.get("version", 1),
        "title": paper["title"],
        "authors": paper["authors"],
        "abstract": paper["abstract"],
        "categories": sorted(set(paper["categories"])),
        "primary_category": paper["primary_category"],
        "published": paper["published"],
        "updated": paper["updated"],
        "url": f"https://arxiv.org/abs/{paper['id']}",
        "pdf_url": f"https://arxiv.org/pdf/{paper['id']}",
        "doi": paper.get("doi"),
        "journal_ref": paper.get("journal_ref"),
        "comment": paper.get("comment"),
        "topics": topics or ["other"],
        "relevance_score": score,
    }


def matching_terms(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if contains_term(text, term)]


def contains_term(text: str, term: str) -> bool:
    pattern = re.escape(term).replace(r"\ ", r"[\s-]+")
    return re.search(rf"(?<!\w){pattern}(?!\w)", text, flags=re.IGNORECASE) is not None


def write_outputs(papers: list[dict], config: dict, data_path: Path) -> None:
    atomic_write(
        data_path,
        json.dumps({"schema_version": 1, "papers": papers}, indent=2, sort_keys=True)
        + "\n",
    )
    atomic_write(ROOT / "data" / "papers.csv", render_csv(papers))
    atomic_write(ROOT / "papers.md", render_catalog(papers, config))

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = replace_section(readme, "STATS", render_stats(papers, config))
    readme = replace_section(readme, "LATEST", render_latest(papers, config))
    atomic_write(readme_path, readme)


def atomic_write(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def replace_section(document: str, name: str, content: str) -> str:
    start = f"<!-- SECPAPERS:{name}:START -->"
    end = f"<!-- SECPAPERS:{name}:END -->"
    if document.count(start) != 1 or document.count(end) != 1:
        raise ValueError(f"README must contain exactly one {name} marker pair")
    before, remainder = document.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{content.rstrip()}\n{end}{after}"


def render_stats(papers: list[dict], config: dict) -> str:
    if not papers:
        return "The catalog has not been collected yet. Run `python3 scripts/collect.py`."

    years = {paper["published"][:4] for paper in papers}
    latest = max(paper["updated"] for paper in papers)[:10]
    topic_names = topic_name_map(config)
    rows = []
    for topic in [*config["topics"], {"id": "other", "name": "Other LLM Security"}]:
        count = sum(topic["id"] in paper["topics"] for paper in papers)
        if count:
            rows.append(
                f"| [{markdown_text(topic_names[topic['id']])}]"
                f"(papers.md#{topic_anchor(topic_names[topic['id']])}) | {count} |"
            )

    return "\n".join(
        [
            f"**{len(papers)} papers** across **{len(years)} publication years**. "
            f"Latest arXiv metadata update: **{latest}**.",
            "",
            "| Topic | Papers |",
            "| --- | ---: |",
            *rows,
        ]
    )


def render_latest(papers: list[dict], config: dict) -> str:
    if not papers:
        return "The latest papers will appear here after the first collection."

    names = topic_name_map(config)
    rows = [
        "| Updated | Paper | Topics | Links |",
        "| --- | --- | --- | --- |",
    ]
    for paper in papers[:15]:
        topics = ", ".join(names[topic] for topic in paper["topics"])
        rows.append(
            f"| {paper['updated'][:10]} | **{markdown_text(paper['title'])}**<br>"
            f"{markdown_text(short_authors(paper['authors']))} | {markdown_text(topics)} | "
            f"[abstract]({paper['url']}) / [PDF]({paper['pdf_url']}) |"
        )
    return "\n".join(rows)


def render_catalog(papers: list[dict], config: dict) -> str:
    names = topic_name_map(config)
    topics = [*config["topics"], {"id": "other", "name": names["other"]}]
    lines = [
        "# LLM Security Papers",
        "",
        "This file is generated by `scripts/collect.py`. Do not edit paper rows by hand.",
        "",
        f"**{len(papers)} unique papers.** Papers may appear in more than one topic.",
        "",
        "## Topics",
        "",
    ]

    lines.extend(
        f"- [{topic['name']}](#{topic_anchor(topic['name'])}) "
        f"({sum(topic['id'] in paper['topics'] for paper in papers)})"
        for topic in topics
        if any(topic["id"] in paper["topics"] for paper in papers)
    )

    for topic in topics:
        matching = [paper for paper in papers if topic["id"] in paper["topics"]]
        if not matching:
            continue
        lines.extend(
            [
                "",
                f"## {topic['name']}",
                "",
                "| Updated | Paper | Authors | Categories | Links |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        lines.extend(
            f"| {paper['updated'][:10]} | **{markdown_text(paper['title'])}** | "
            f"{markdown_text(short_authors(paper['authors']))} | "
            f"{markdown_text(', '.join(paper['categories']))} | "
            f"[{paper['id']}]({paper['url']}) / [PDF]({paper['pdf_url']}) |"
            for paper in matching
        )

    lines.extend(["", "---", "", "Source: [arXiv](https://arxiv.org/).", ""])
    return "\n".join(lines)


def render_csv(papers: list[dict]) -> str:
    output = io.StringIO(newline="")
    fields = [
        "id",
        "title",
        "authors",
        "published",
        "updated",
        "topics",
        "categories",
        "url",
        "pdf_url",
        "abstract",
    ]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for paper in papers:
        writer.writerow(
            {
                key: spreadsheet_safe(value)
                for key, value in {
                    "id": paper["id"],
                    "title": paper["title"],
                    "authors": "; ".join(paper["authors"]),
                    "published": paper["published"],
                    "updated": paper["updated"],
                    "topics": "; ".join(paper["topics"]),
                    "categories": "; ".join(paper["categories"]),
                    "url": paper["url"],
                    "pdf_url": paper["pdf_url"],
                    "abstract": paper["abstract"],
                }.items()
            }
        )
    return output.getvalue()


def topic_name_map(config: dict) -> dict[str, str]:
    return {
        **{topic["id"]: topic["name"] for topic in config["topics"]},
        "other": "Other LLM Security",
    }


def topic_anchor(name: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", name.lower()).replace(" ", "-")


def markdown_text(value: str) -> str:
    escaped = html.escape(value.replace("\n", " "), quote=False)
    return re.sub(r"([\\`*_\[\]{}|])", r"\\\1", escaped)


def spreadsheet_safe(value: str) -> str:
    if value.lstrip().startswith(("=", "+", "-", "@", "\t", "\r")):
        return f"'{value}"
    return value


def short_authors(authors: list[str]) -> str:
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{', '.join(authors[:3])}, et al."


if __name__ == "__main__":
    main()
