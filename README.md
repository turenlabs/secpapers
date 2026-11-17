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
**2393 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-16**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 560 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 585 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 378 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 563 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 525 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 698 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 287 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1111 |
| [Other LLM Security](papers.md#other-llm-security) | 156 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-16 | **ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises**<br>Jaime C. Acosta, Anantaa Kotal, Aritran Piplai | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.21579) / [PDF](https://arxiv.org/pdf/2611.21579) |
| 2026-11-16 | **SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection**<br>Woosang Lim, Yeseul Chang, Jaewoo Lee | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.07222) / [PDF](https://arxiv.org/pdf/2611.07222) |
| 2026-11-16 | **RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems**<br>Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos, et al. | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.21480) / [PDF](https://arxiv.org/pdf/2611.21480) |
| 2026-11-16 | **TRIAGE-CPG: A Cross-Model Study of Budgeted Static Malware Triage with Large Language Models**<br>Paul-Andrei Sava, Alexander Küchler, Daniel Kowatsch, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.21331) / [PDF](https://arxiv.org/pdf/2611.21331) |
| 2026-11-16 | **On the Price of Privacy for Language Identification and Generation**<br>Xiaoyu Li, Andi Han, Jiaojiao Jiang, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2604.07238) / [PDF](https://arxiv.org/pdf/2604.07238) |
| 2026-11-16 | **AudioTrace: File-Level Membership Detection for Audio Large Language Models**<br>Guangzhi Sun, Xiao Zhan, Shuai Wang, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.21088) / [PDF](https://arxiv.org/pdf/2611.21088) |
| 2026-11-16 | **Vishing-Tactics-Bench: Forecasting Exploitation Trajectories in Voice Phishing Calls**<br>Jeongmin Lee, Dongmyung Sul, Seung Yun, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.07151) / [PDF](https://arxiv.org/pdf/2609.07151) |
| 2026-11-16 | **A First Look at System One Decision Models for Malware Detection**<br>Pier Mattia Basciano, Giovanni Farina, Salvatore Monteleone | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.20699) / [PDF](https://arxiv.org/pdf/2611.20699) |
| 2026-11-16 | **MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis**<br>Yongkang Xiao, Qiyi Deng, Jing Chen, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.20671) / [PDF](https://arxiv.org/pdf/2611.20671) |
| 2026-11-16 | **Beyond the Patch: Reconstructing an Incomplete-Fix Patch Bypass in LLM Agent Frameworks with Control-Gated, Benign Probes**<br>Chaitanya Garware | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.20514) / [PDF](https://arxiv.org/pdf/2611.20514) |
| 2026-11-16 | **Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment**<br>Koki Itai, Jun Hirako, Hiroaki Yamagiwa | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.20441) / [PDF](https://arxiv.org/pdf/2611.20441) |
| 2026-11-15 | **Clawdrain: Exploiting Tool-Calling Chains for Stealthy Token Exhaustion in OpenClaw Agents**<br>Ben Dong, Zhonghao Guo, Tianyi Lu, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2603.00902) / [PDF](https://arxiv.org/pdf/2603.00902) |
| 2026-11-15 | **Understanding Users' Security, Privacy, and Trust Concerns in Healthcare AI Systems**<br>Tushar Nayan, Mohammed Al Duniawi, Song Fang, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.20223) / [PDF](https://arxiv.org/pdf/2611.20223) |
| 2026-11-15 | **Risk-certified prompt optimization for LLM-as-a-judge guardrails**<br>Hussein Jawad, Alexandre Landeau, Guy Fleury Iradukunda, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.20156) / [PDF](https://arxiv.org/pdf/2611.20156) |
| 2026-11-15 | **RAS: Measuring LLM Safety Through Refusal Alignment**<br>Chang-Chieh Huang, Yan-Lun Chen, Chia-Mu Yu, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.25750) / [PDF](https://arxiv.org/pdf/2606.25750) |
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
