# Contributing

SecPapers is generated from arXiv metadata. Contributions should improve the
collector, its transparent selection rules, or the source metadata rather than
editing generated catalog rows by hand.

## Suggest a paper

Open the [paper suggestion form](https://github.com/turenlabs/secpapers/issues/new?template=paper.yml)
with the arXiv URL and a short explanation of why it is in scope. For a missing
topic, include the search terms that would classify it without introducing
obvious unrelated results.

## Change the collector

1. Update `config/topics.json` or `scripts/collect.py`.
2. Add or update a focused test in `tests/`.
3. Run `python3 -m unittest discover -s tests -v`.
4. Run `node --test tests/site.test.mjs`.
5. Run `python3 scripts/collect.py --render-only`.
6. Include generated changes to `README.md`, `papers.md`, `data/`, and
   `docs/data/`.

Do not hand-edit content between `SECPAPERS` markers or in `papers.md`,
`data/papers.json`, or `data/papers.csv`. Those files are deterministic outputs.

## Change the web index

The GitHub Pages site is dependency-free and lives in `docs/`. Serve it locally
with `python3 -m http.server 8765 --directory docs`, then open
`http://localhost:8765`. Keep paper metadata in text-only DOM sinks and retain
the first-party Content Security Policy in `docs/index.html`.

## Selection changes

Changes to LLM terms, security terms, the minimum relevance score, or topic
keywords can add, remove, or reclassify historical records. Explain expected
precision and recall effects in the pull request. Small, auditable term lists
are preferred over opaque classification services.

## Metadata corrections

arXiv is authoritative for titles, authors, abstracts, categories, and revision
dates. Correct upstream metadata on arXiv where possible. SecPapers will adopt
the correction when the revised record appears in a collection window.
