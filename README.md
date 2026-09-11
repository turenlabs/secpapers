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
**1189 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-10**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 258 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 291 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 175 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 286 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 259 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 382 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 149 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 560 |
| [Other LLM Security](papers.md#other-llm-security) | 87 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-10 | **BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense**<br>Simona Boboila, Xavier Cadet, Edward Koh, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.11852) / [PDF](https://arxiv.org/pdf/2609.11852) |
| 2026-09-10 | **SpecGuard: Inference-Time Backdoor Detection For Free**<br>Rui Wen, Ahmed Salem, Andrew Paverd, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.11799) / [PDF](https://arxiv.org/pdf/2609.11799) |
| 2026-09-10 | **Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs**<br>Jordi Luque, Fernando López, Aleix Sant | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.11762) / [PDF](https://arxiv.org/pdf/2609.11762) |
| 2026-09-10 | **VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use**<br>Juan S. Santillana | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2608.08477) / [PDF](https://arxiv.org/pdf/2608.08477) |
| 2026-09-10 | **Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation**<br>Junyu Lu, Kaiyuan Liu, Kaichun Wang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.22230) / [PDF](https://arxiv.org/pdf/2608.22230) |
| 2026-09-10 | **Exploring the Role of Security Experience and ChatGPT Usage Strategies on Secure Software Engineering Education**<br>Alessio Ferrari, Minh An Nguyen, Kushal Ramkumar, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.11303) / [PDF](https://arxiv.org/pdf/2609.11303) |
| 2026-09-10 | **Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model**<br>Hyojung Han | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.11291) / [PDF](https://arxiv.org/pdf/2609.11291) |
| 2026-09-10 | **Privacy Auditing with Zero (0) Training Run**<br>Tudor Cebere, Mathieu Even, Linus Bleistein, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.14591) / [PDF](https://arxiv.org/pdf/2605.14591) |
| 2026-09-10 | **ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks**<br>Haozhe Lu, Jiaqi Li, Xinyuan Zhu, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.11082) / [PDF](https://arxiv.org/pdf/2609.11082) |
| 2026-09-10 | **DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks**<br>Rui Cao, Shaojing Fan, Liming Fang, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.11008) / [PDF](https://arxiv.org/pdf/2609.11008) |
| 2026-09-10 | **Demystifying the Privacy-Utility Trade-off in LLM Interactions**<br>Zhenhua Liu, Zhanxu Xie, Junjie Yu, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.10992) / [PDF](https://arxiv.org/pdf/2609.10992) |
| 2026-09-10 | **LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories**<br>Mohammad Farhad, Shuvalaxmi Dass | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.10945) / [PDF](https://arxiv.org/pdf/2609.10945) |
| 2026-09-09 | **DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents**<br>Asif Pinjari, Mithun Paul Saint-Germain | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.10892) / [PDF](https://arxiv.org/pdf/2609.10892) |
| 2026-09-09 | **A2ABreak: Systematic Security Analysis of the A2A Protocol**<br>Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.10871) / [PDF](https://arxiv.org/pdf/2609.10871) |
| 2026-09-09 | **No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers**<br>Zehua Zhang, Jie Hu, Pratham Hegde, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.10854) / [PDF](https://arxiv.org/pdf/2609.10854) |
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
