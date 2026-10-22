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
**1998 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-21**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 459 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 487 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 313 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 482 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 442 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 595 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 243 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 948 |
| [Other LLM Security](papers.md#other-llm-security) | 128 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-21 | **Closing the Sim-to-Real Gap: An Evaluation Framework for Autonomous Cyber Defense Configuration of Commercial EDR**<br>Kerri Prinos, Lilianne Brush | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.08168) / [PDF](https://arxiv.org/pdf/2606.08168) |
| 2026-10-21 | **Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs**<br>Prakhar Ganesh, Yash More, Marco Romanelli, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.29925) / [PDF](https://arxiv.org/pdf/2610.29925) |
| 2026-10-21 | **Exploring Post-Training Alignment of Small Language Models for Biomedical Data-to-Text Generation: A Case Study of Medication Leaflet**<br>Xi Yang, Guodong Liu, Chuqin Li, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.13430) / [PDF](https://arxiv.org/pdf/2607.13430) |
| 2026-10-21 | **Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations**<br>Frank Breitinger, Jan Gruber, Christopher Hargreaves, et al. | Prompt Injection &amp; Jailbreaks, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.29747) / [PDF](https://arxiv.org/pdf/2610.29747) |
| 2026-10-21 | **Output Vector Editing for Memorization Mitigation in Large Language Models**<br>Ahmad Dawar Hakimi, Kaiwei Lei, Isabelle Augenstein, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2606.18767) / [PDF](https://arxiv.org/pdf/2606.18767) |
| 2026-10-21 | **VertMark: A Unified Training-Free Robust Watermarking Framework for Vertical Domain Pre-trained Language Models**<br>Xin Cheng, Cong Kong, Zhaoxia Yin, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2605.02557) / [PDF](https://arxiv.org/pdf/2605.02557) |
| 2026-10-21 | **SUDP: Secret-Use Delegation Protocol for Agentic Systems**<br>Xiaohang Yu, Hejia Geng, Xinmeng Zeng, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2604.24920) / [PDF](https://arxiv.org/pdf/2604.24920) |
| 2026-10-21 | **Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities**<br>Gadi Evron | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.29379) / [PDF](https://arxiv.org/pdf/2610.29379) |
| 2026-10-21 | **Quality-Diversity Red-Teaming: Automated Generation of High-Quality and Diverse Attackers for Large Language Models**<br>Ren-Jian Wang, Ke Xue, Zeyu Qin, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2506.07121) / [PDF](https://arxiv.org/pdf/2506.07121) |
| 2026-10-21 | **Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment**<br>Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.27548) / [PDF](https://arxiv.org/pdf/2610.27548) |
| 2026-10-21 | **Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics**<br>Hongyu Li, Xinlong Huang, Zhan Yu, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.29225) / [PDF](https://arxiv.org/pdf/2610.29225) |
| 2026-10-21 | **Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models**<br>Yejin Lee, Ungsik Kim, Yo-Sub Han | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.13043) / [PDF](https://arxiv.org/pdf/2605.13043) |
| 2026-10-21 | **A Unified Evaluation Framework of Physical Adversarial Robustness in the Edge VLM Era**<br>Eric Liang, Alan Luo, Kaiwen Yuan | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.29196) / [PDF](https://arxiv.org/pdf/2610.29196) |
| 2026-10-21 | **Correlated Failures of AI Approval Monitors**<br>Luca Zanolini | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.29178) / [PDF](https://arxiv.org/pdf/2610.29178) |
| 2026-10-21 | **SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders**<br>Evan Caville, Spencer Kayser, Siamak Layeghy, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.21951) / [PDF](https://arxiv.org/pdf/2607.21951) |
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
