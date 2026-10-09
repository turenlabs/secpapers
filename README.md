<div align="center">

# SecPapers

**A living, searchable catalog of large language model security research.**

[![Update papers](https://github.com/turenlabs/secpapers/actions/workflows/update.yml/badge.svg)](https://github.com/turenlabs/secpapers/actions/workflows/update.yml)
[![CI](https://github.com/turenlabs/secpapers/actions/workflows/ci.yml/badge.svg)](https://github.com/turenlabs/secpapers/actions/workflows/ci.yml)
[![Explore](https://img.shields.io/badge/explore-live%20index-1e7bff.svg)](https://turenlabs.github.io/secpapers/)
[![License: MIT](https://img.shields.io/badge/License-MIT-0f766e.svg)](LICENSE)
[![Data: JSON + CSV](https://img.shields.io/badge/data-JSON%20%2B%20CSV-334155.svg)](data)

[Explore the web index](https://turenlabs.github.io/secpapers/) | [Browse all papers](papers.md) | [Use the dataset](data/papers.json) | [Methodology](docs/methodology.md) | [Suggest a paper](https://github.com/turenlabs/secpapers/issues/new?template=paper.yml)

</div>

SecPapers tracks both sides of LLM security: research that makes language
models safer, and research that applies language models to cybersecurity. It
queries arXiv every day, applies a transparent relevance filter, deduplicates
paper revisions, and regenerates this repository from stable source data.

## At a glance

<!-- SECPAPERS:STATS:START -->
**1750 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-08**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 399 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 432 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 260 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 422 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 386 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 537 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 218 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 842 |
| [Other LLM Security](papers.md#other-llm-security) | 115 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-08 | **ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI**<br>Shihab Ahmed, Md Sajidul Islam Sajid, Teryl Taylor, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.12415) / [PDF](https://arxiv.org/pdf/2610.12415) |
| 2026-10-08 | **Beyond Direct Access: Resource Hijacking in LLM Agents**<br>Puyu Zeng, Mingang Chen, Zheli Liu, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.15108) / [PDF](https://arxiv.org/pdf/2608.15108) |
| 2026-10-08 | **Poster: A Preliminary Study of LLM Distillation Inference**<br>Edward Chen, Yuntao Du | Other LLM Security | [abstract](https://arxiv.org/abs/2610.12137) / [PDF](https://arxiv.org/pdf/2610.12137) |
| 2026-10-08 | **Could LLM Watermark Detection be Public?**<br>Georgios Milis, Tom Sander, Tomáš Souček, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.12106) / [PDF](https://arxiv.org/pdf/2610.12106) |
| 2026-10-08 | **A Security Meta-Model for Retrieval-Augmented Generation Systems**<br>Steve Nouyep, Sébastien Salva, Maxime Puys | Other LLM Security | [abstract](https://arxiv.org/abs/2610.11893) / [PDF](https://arxiv.org/pdf/2610.11893) |
| 2026-10-08 | **SemField: A Simple, Linear, Continuous, yet Robust Semantic Watermark**<br>Varun Gumma, Navonil Majumdar, Soujanya Poria | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.11848) / [PDF](https://arxiv.org/pdf/2610.11848) |
| 2026-10-08 | **Anytime-valid detection of LLM weight exfiltration**<br>Ines Ortega-Fernandez, Mateusz Kowalczyk, Keri Warr | Other LLM Security | [abstract](https://arxiv.org/abs/2610.11843) / [PDF](https://arxiv.org/pdf/2610.11843) |
| 2026-10-08 | **Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation**<br>Haitong Jiang, Chunlin Liu, Sihan Tang, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.11766) / [PDF](https://arxiv.org/pdf/2610.11766) |
| 2026-10-08 | **Evaluating and Improving the Robustness of Large Language Models to Input Sequence Variations**<br>Narek Maloyan | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.02432) / [PDF](https://arxiv.org/pdf/2610.02432) |
| 2026-10-08 | **Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for Language Models**<br>Haoxiang Wang, Da Yu, Huishuai Zhang | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.06213) / [PDF](https://arxiv.org/pdf/2605.06213) |
| 2026-10-08 | **LTBD: Learnable Trust-Boundary Delimiters for Prompt Injection Defense**<br>Luman Zhao, Minghui Xu, Yue Zhang, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.11634) / [PDF](https://arxiv.org/pdf/2610.11634) |
| 2026-10-08 | **Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery**<br>Li Lu, Yanjie Zhao, Hongjie Chen, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.11602) / [PDF](https://arxiv.org/pdf/2610.11602) |
| 2026-10-08 | **Measuring Cultural Alignment Beyond the Average: A Framework for Evaluating Maternal-Health LLM Interactions in Indian Contexts**<br>Umaira Izhar, Gunjan Arora, Pushpendra Singh | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.11586) / [PDF](https://arxiv.org/pdf/2610.11586) |
| 2026-10-08 | **SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation**<br>Varun Kohli, Lee Bing Cheng, Nur Hazim Ghazali, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.11556) / [PDF](https://arxiv.org/pdf/2610.11556) |
| 2026-10-08 | **Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model**<br>Tianyi Wang, Huawei Fan, Yuanchao Shu, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2602.07878) / [PDF](https://arxiv.org/pdf/2602.07878) |
<!-- SECPAPERS:LATEST:END -->

## Scope

Included work must mention an LLM or language-model concept and a concrete
security, safety, privacy, abuse, or cyber-defense concept in its title or
abstract. The taxonomy covers:

- Prompt injection and jailbreaks
- Agent and tool security
- Privacy, memorization, and data leakage
- Model safety, alignment, and misuse
- Adversarial attacks, poisoning, and backdoors
- Vulnerability discovery and secure software
- Malware, phishing, and threat intelligence
- Security evaluation, benchmarks, and red teaming

The catalog is automated discovery, not a quality ranking or endorsement. See
[the methodology](docs/methodology.md) for the query, scoring rules, known
limitations, and correction process.

## How it works

```text
arXiv Atom API
      |
      v
query + pagination -> relevance scoring -> revision deduplication
      |                                          |
      +-------------------> data/papers.json <---+
                                  |
                                  v
            README.md + papers.md + CSV + web index
```

The collector uses only the Python standard library. There is no package
installation step and no runtime dependency lockfile to maintain.

```bash
# Run tests
python3 -m unittest discover -s tests -v

# Fetch recent papers and regenerate every output
python3 scripts/collect.py

# Regenerate Markdown and CSV without network access
python3 scripts/collect.py --render-only
```

Search terms and taxonomy rules live in [`config/topics.json`](config/topics.json).
The canonical record format is documented by
[`data/schema.json`](data/schema.json). Updates run daily at 06:17 UTC and can
also be started manually from the Actions tab.

## Data use

- [`data/papers.json`](data/papers.json) is the canonical, stable dataset.
- [`data/papers.csv`](data/papers.csv) is convenient for spreadsheets and analysis.
- [`papers.md`](papers.md) is the human-readable catalog grouped by topic.
- [`docs/data`](docs/data) contains compact, generated payloads for the
  [SecPapers web index](https://turenlabs.github.io/secpapers/).
- Each record links to the authoritative arXiv abstract and PDF.
- Paper titles, abstracts, and author metadata remain attributable to their
  respective authors and are not relicensed by this repository's MIT license.

## Contributing

False positives, missing papers, taxonomy improvements, and collector fixes are
welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Acknowledgments

Paper metadata is provided by the [arXiv API](https://info.arxiv.org/help/api/).
SecPapers is not affiliated with or endorsed by arXiv. Please cite the original
authors and papers when using this catalog in research.
