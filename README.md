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
**2127 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-29**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 486 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 520 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 330 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 502 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 466 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 632 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 260 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1002 |
| [Other LLM Security](papers.md#other-llm-security) | 140 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-29 | **The Privacy and Security Risks of Edge LLM Optimization**<br>Mingchen Li, Ren-Yi Huang, Dumindu Samaraweera, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.40543) / [PDF](https://arxiv.org/pdf/2610.40543) |
| 2026-10-29 | **Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training**<br>Qiusi Zhan, Nian Lyu, Stephanie Ding, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.07510) / [PDF](https://arxiv.org/pdf/2610.07510) |
| 2026-10-29 | **WAAA! Web Adversaries Against Web Agents**<br>Sohom Datta, Alex Nahapetyan, William Enck, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.05509) / [PDF](https://arxiv.org/pdf/2605.05509) |
| 2026-10-29 | **Understanding and Mitigating Role Spoofing in LLMs**<br>Ezra Edelman, Benjamin Edelman, Surbhi Goel, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.40396) / [PDF](https://arxiv.org/pdf/2610.40396) |
| 2026-10-29 | **Robust Context-Aware Detection of Malicious Instructions in Text**<br>Buzhao Liu, Xinhang Ma, Yevgeniy Vorobeychik | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.05430) / [PDF](https://arxiv.org/pdf/2608.05430) |
| 2026-10-29 | **Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities**<br>Simin Chen, Yixin He, Suman Jana, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2509.25894) / [PDF](https://arxiv.org/pdf/2509.25894) |
| 2026-10-29 | **InferD: A Honeypot Framework for AI Inference Infrastructure**<br>Hicham Hammouchi, Gabriele Lenzini | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.39807) / [PDF](https://arxiv.org/pdf/2610.39807) |
| 2026-10-29 | **SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection**<br>Doohyun Kim, Donghwa Kang, Mingyu Jun, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.39758) / [PDF](https://arxiv.org/pdf/2610.39758) |
| 2026-10-29 | **zkCraft: Prompt-Guided LLM as a Zero-Shot Mutation Pattern Oracle for TCCT-Powered ZK Fuzzing**<br>Rong Fu, Jia Yee Tan, Ziyu Kong, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.00667) / [PDF](https://arxiv.org/pdf/2602.00667) |
| 2026-10-29 | **Red-Teaming Large Language Models in Low-Resource African Languages: A Case Study of Yoruba and Nigerian Pidgin**<br>Paula Chikaodinaka Anyanwu, Valdini Douglace Lemofouet, Blessing Ngozi Uzor, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39590) / [PDF](https://arxiv.org/pdf/2610.39590) |
| 2026-10-29 | **FuzzAgent: Multi-Agent System for End-to-End Evolutionary Library Fuzzing**<br>Yunlong Lyu, Peng Chen, Fengyi Wu, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2605.14431) / [PDF](https://arxiv.org/pdf/2605.14431) |
| 2026-10-29 | **Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy**<br>Hengyu Wu, Blaise Delattre, Yang Cao | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39532) / [PDF](https://arxiv.org/pdf/2610.39532) |
| 2026-10-29 | **Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems**<br>CheolWon Na, Hao Ni, Lukasz Szpruch, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2608.24069) / [PDF](https://arxiv.org/pdf/2608.24069) |
| 2026-10-29 | **The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems**<br>Youssef Hamdi Zafan Ibrahim, Muhammad Ikram, Mohammed Khalaf Salama | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.18526) / [PDF](https://arxiv.org/pdf/2609.18526) |
| 2026-10-29 | **Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models**<br>Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39509) / [PDF](https://arxiv.org/pdf/2610.39509) |
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
