import csv
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.collect import (
    enrich_paper,
    merge_papers,
    parse_feed,
    render_catalog,
    render_csv,
    replace_section,
)


ROOT = Path(__file__).resolve().parents[1]


class CollectorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(
            (ROOT / "config" / "topics.json").read_text(encoding="utf-8")
        )
        cls.feed = parse_feed((ROOT / "tests" / "fixtures" / "arxiv-feed.xml").read_bytes())

    def test_parses_atom_metadata_and_preserves_legacy_ids(self):
        modern, legacy = self.feed

        self.assertEqual(modern["id"], "2608.01234")
        self.assertEqual(modern["version"], 2)
        self.assertEqual(modern["primary_category"], "cs.CR")
        self.assertEqual(modern["authors"], ["Ada Researcher", "Sam Security"])
        self.assertEqual(modern["doi"], "10.1000/example")
        self.assertEqual(legacy["id"], "cs/0601001")

    def test_relevance_and_multi_topic_classification(self):
        paper = enrich_paper(self.feed[0], self.config)

        self.assertIsNotNone(paper)
        self.assertGreaterEqual(paper["relevance_score"], 4)
        self.assertIn("prompt-security", paper["topics"])
        self.assertIn("agent-security", paper["topics"])
        self.assertIn("evaluation", paper["topics"])

    def test_rejects_paper_without_security_signal(self):
        paper = dict(self.feed[1])
        paper["abstract"] = "This survey explains large language model scaling laws."

        self.assertIsNone(enrich_paper(paper, self.config))

    def test_rejects_incidental_weak_security_term(self):
        paper = dict(self.feed[1])
        paper["title"] = "Optimizing Scientific Code with Large Language Models"
        paper["abstract"] = "The open-source implementation preserves data privacy."

        self.assertIsNone(enrich_paper(paper, self.config))

    def test_rejects_non_security_use_of_vulnerability(self):
        paper = dict(self.feed[1])
        paper["title"] = "Discovering Cancer Vulnerabilities with AI Agents"
        paper["abstract"] = "Large language models identify treatment targets."

        self.assertIsNone(enrich_paper(paper, self.config))

    def test_rejects_unscoped_arxiv_category(self):
        paper = dict(self.feed[0], categories=["cs.CY"], primary_category="cs.CY")

        self.assertIsNone(enrich_paper(paper, self.config))

    def test_merge_keeps_newest_revision(self):
        old = dict(self.feed[0], version=1, updated="2026-08-19T10:00:00Z")
        papers = merge_papers([old], [self.feed[0]], self.config)

        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["version"], 2)
        self.assertEqual(papers[0]["updated"], "2026-08-20T10:00:00Z")

    def test_merge_prefers_version_over_anomalous_timestamp(self):
        higher_version = dict(self.feed[0], version=3, updated="2026-08-18T10:00:00Z")
        papers = merge_papers([self.feed[0], higher_version, self.feed[0]], [], self.config)

        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["version"], 3)

    def test_renderers_are_deterministic_and_escape_markdown(self):
        paper = enrich_paper(self.feed[0], self.config)
        paper["title"] = "Prompt [Injection] | An *LLM* <Security> Study"

        catalog = render_catalog([paper], self.config)
        csv_output = render_csv([paper])

        self.assertIn(
            "Prompt \\[Injection\\] \\| An \\*LLM\\* &lt;Security&gt; Study",
            catalog,
        )
        self.assertEqual(catalog, render_catalog([paper], self.config))
        self.assertEqual(csv_output, render_csv([paper]))
        rows = list(csv.DictReader(io.StringIO(csv_output)))
        self.assertEqual(
            rows[0]["title"], "Prompt [Injection] | An *LLM* <Security> Study"
        )

    def test_csv_neutralizes_spreadsheet_formulas(self):
        paper = enrich_paper(self.feed[0], self.config)
        paper["title"] = '=HYPERLINK("https://example.com")'
        paper["authors"] = ["@malicious"]

        row = list(csv.DictReader(io.StringIO(render_csv([paper]))))[0]

        self.assertTrue(row["title"].startswith("'="))
        self.assertTrue(row["authors"].startswith("'@"))

    def test_readme_marker_replacement_requires_one_pair(self):
        document = "before\n<!-- SECPAPERS:X:START -->\nold\n<!-- SECPAPERS:X:END -->\nafter\n"
        updated = replace_section(document, "X", "new")

        self.assertIn("START -->\nnew\n<!--", updated)
        with self.assertRaises(ValueError):
            replace_section("missing markers", "X", "new")

    def test_fixture_can_drive_an_offline_dataset(self):
        papers = merge_papers([], self.feed, self.config)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "papers.json"
            path.write_text(json.dumps({"schema_version": 1, "papers": papers}))
            restored = json.loads(path.read_text())

        self.assertEqual(len(restored["papers"]), 1)
        self.assertEqual(restored["papers"][0]["id"], "2608.01234")


if __name__ == "__main__":
    unittest.main()
