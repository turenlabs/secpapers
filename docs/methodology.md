# Collection Methodology

SecPapers is an automated discovery index for research at the intersection of
large language models and security. Its rules are public, deterministic, and
intentionally simple enough to audit in a code review.

## Source

The collector queries the official [arXiv API](https://info.arxiv.org/help/api/)
over HTTPS and parses its Atom feed. It records the canonical paper ID, latest
revision number, title, authors, abstract, arXiv categories, publication and
update times, DOI, journal reference, comment, abstract URL, and PDF URL.

Paper revisions share one canonical record. When a newer revision appears, its
metadata replaces the older revision. Papers outside the current query window
remain in the local dataset and are re-evaluated against the current relevance
and taxonomy rules on every run.

## Discovery query

The API query in [`config/topics.json`](../config/topics.json) has three parts:

1. At least one LLM or language-model phrase.
2. At least one security, privacy, safety, abuse, or cyber-defense phrase.
3. At least one relevant arXiv category: `cs.CR`, `cs.CL`, `cs.AI`, `cs.SE`,
   `cs.LG`, `cs.MA`, or `stat.ML`.

Results are requested by most recently updated date. The scheduled job fetches
the latest 500 matches in 100-record pages and waits three seconds between API
requests. Existing records make this an incremental rolling collection rather
than a 500-paper cap on the repository.

## Relevance filter

The local filter independently requires both an LLM term and a security term.
It assigns:

- 3 points when an LLM term appears in the title, otherwise 1 point when it
  appears in the abstract.
- 3 points when a security term appears in the title, otherwise 1 point when it
  appears in the abstract.
- 2 points when the paper is in arXiv's `cs.CR` category.

A paper needs at least 4 points. It must also have a high-confidence security
signal: both concepts in the title, the `cs.CR` category, or one of the stronger
phrases listed in `strong_security_terms` anywhere in its metadata. This keeps
generic mentions such as "data privacy" in an otherwise unrelated system paper,
or "vulnerability" in a medical paper, from being treated as security research.
Papers where both concepts are only in the abstract remain eligible when the
authors classified the work as cryptography and security.

Matching is case-insensitive, phrase-boundary aware, and treats spaces and
hyphens as equivalent. The resulting score is stored with every record.

## Taxonomy

Accepted papers can have multiple topics. Topic classification is a direct
keyword match against title and abstract; the complete ordered keyword lists
are in `config/topics.json`. Papers that meet the relevance rule but match no
specialized topic are retained as `Other LLM Security`.

Topic labels organize discovery. They are not claims about a paper's primary
contribution and may overlap.

## Determinism

All papers are sorted by update time, publication time, then canonical ID.
Generated files contain no collection timestamp, so a run with unchanged arXiv
metadata produces no Git diff and no empty automated commit. The displayed
"latest metadata update" comes from the newest paper record.

## Limitations

- arXiv does not contain every peer-reviewed security paper.
- Keyword rules can miss unusual terminology and can admit false positives.
- The rolling query discovers newly updated matches; an old paper newly made
  relevant only by a query-rule change may require a larger manual backfill.
- Topic labels are heuristic and do not replace reading the paper.
- Inclusion is not peer-review validation, endorsement, or a safety assessment.

Report false positives or missing papers with the repository's issue forms.
