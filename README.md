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
**2096 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-27**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 477 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 514 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 326 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 499 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 461 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 621 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 257 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 988 |
| [Other LLM Security](papers.md#other-llm-security) | 138 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-27 | **Optimizing Spectral Signature in Code Backdoor Detection**<br>Quoc Hung Le, Thanh Le-Cong, Bach Le, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2510.13992) / [PDF](https://arxiv.org/pdf/2510.13992) |
| 2026-10-27 | **The Envelope Layer: An Underestimated Surface of LLM Agent Defense**<br>Yuelin Han | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.37415) / [PDF](https://arxiv.org/pdf/2610.37415) |
| 2026-10-27 | **Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories**<br>Zirui Ding, Xinxin Fan, Hao Yuan, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.37369) / [PDF](https://arxiv.org/pdf/2610.37369) |
| 2026-10-27 | **DYNASHIELD: A Black-Box Moving Target Defense for LLMs via Dynamic Decoding Customization**<br>Xiaoqun Liu, Weiming Qi, Qiben Yan | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2412.07672) / [PDF](https://arxiv.org/pdf/2412.07672) |
| 2026-10-27 | **When AI Agrees Too Much: Manipulating Automated Code Review via Bias Injection**<br>Georgios Alexopoulos, Nikolaos Alexopoulos, Diomidis Spinellis, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2603.18740) / [PDF](https://arxiv.org/pdf/2603.18740) |
| 2026-10-27 | **Watermark Basins: Black-Box Detection of Distilled LLMs**<br>Hongyan Chang, Hady Elsahar, Tom Sander, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.37266) / [PDF](https://arxiv.org/pdf/2610.37266) |
| 2026-10-27 | **AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset**<br>Amine Lbath, Massih-Reza Amini, Aurelien Delaitre, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2508.20866) / [PDF](https://arxiv.org/pdf/2508.20866) |
| 2026-10-27 | **AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification**<br>Tian Zhang, Yiwei Xu, Juan Wang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2602.22724) / [PDF](https://arxiv.org/pdf/2602.22724) |
| 2026-10-27 | **RHINO: Guided Reasoning for Mapping Network Logs to Adversarial Tactics and Techniques with Large Language Models**<br>Fanchao Meng, Jiaping Gui, Yunbo Li, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2510.14233) / [PDF](https://arxiv.org/pdf/2510.14233) |
| 2026-10-27 | **PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses**<br>Krishna Kanth Nakka, Yujun Wang, Shijie Zhou, et al. | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.36711) / [PDF](https://arxiv.org/pdf/2610.36711) |
| 2026-10-27 | **Measuring Users' Security and Privacy Concerns About Third-Party Community Bots on Discord**<br>Kofi Ampomah, Tu Le | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.36626) / [PDF](https://arxiv.org/pdf/2610.36626) |
| 2026-10-27 | **SoK: Systematizing LLM Prompt Security: Taxonomies, Datasets, and Unified Evaluation of Attacks and Defenses**<br>Hanbin Hong, Shuang Wu, Shuya Feng, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.15476) / [PDF](https://arxiv.org/pdf/2510.15476) |
| 2026-10-27 | **SELF: A Robust Singular Value and Eigenvalue Approach for LLM Fingerprinting**<br>Hanxiu Zhang, Qiang Xu, Yue Zheng | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2512.03620) / [PDF](https://arxiv.org/pdf/2512.03620) |
| 2026-10-27 | **TextCloak: Safeguarding Data from Unauthorized LLM Fine-Tuning via RL-Driven Unlearnable Examples**<br>Chengshuai Zhao, Pingchuan Ma, Dawei Li, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2607.28862) / [PDF](https://arxiv.org/pdf/2607.28862) |
| 2026-10-27 | **What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks**<br>Zihan Chen, Lei Nico Zheng, Di Zhu | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.36422) / [PDF](https://arxiv.org/pdf/2610.36422) |
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
