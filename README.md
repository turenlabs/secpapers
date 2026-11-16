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
**2365 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-13**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 552 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 581 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 372 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 554 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 518 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 691 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 283 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1095 |
| [Other LLM Security](papers.md#other-llm-security) | 157 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-13 | **CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving**<br>Yuhang Wang, Jingxin Yang, Chuheng Wei, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.18442) / [PDF](https://arxiv.org/pdf/2611.18442) |
| 2026-11-13 | **PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review**<br>Hua Yang, Aditya Bhardwaj, Shidong Pan, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.18293) / [PDF](https://arxiv.org/pdf/2611.18293) |
| 2026-11-13 | **REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming**<br>Nicolas Koller, Andreas U. Schmidt | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.07738) / [PDF](https://arxiv.org/pdf/2607.07738) |
| 2026-11-13 | **Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory**<br>Yulliwas Ameur, Billal Mokhtari, Samia Bouzefrane | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.18133) / [PDF](https://arxiv.org/pdf/2611.18133) |
| 2026-11-13 | **HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities**<br>Xiaoxue Ren, Penghao Jiang, Kaixin Li, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.12200) / [PDF](https://arxiv.org/pdf/2510.12200) |
| 2026-11-13 | **Training Language Model Agents to Find Vulnerabilities with CTF-Dojo**<br>Terry Yue Zhuo, Dingmin Wang, Hantian Ding, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2508.18370) / [PDF](https://arxiv.org/pdf/2508.18370) |
| 2026-11-13 | **Cyber-Zero: Training Cybersecurity Agents without Runtime**<br>Terry Yue Zhuo, Dingmin Wang, Hantian Ding, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2508.00910) / [PDF](https://arxiv.org/pdf/2508.00910) |
| 2026-11-13 | **Astraios: Parameter-Efficient Instruction Tuning Code Large Language Models**<br>Terry Yue Zhuo, Armel Zebaze, Nitchakarn Suppattarachai, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2401.00788) / [PDF](https://arxiv.org/pdf/2401.00788) |
| 2026-11-13 | **On Robustness of Prompt-based Semantic Parsing with Large Pre-trained Language Model: An Empirical Study on Codex**<br>Terry Yue Zhuo, Zhuang Li, Yujin Huang, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2301.12868) / [PDF](https://arxiv.org/pdf/2301.12868) |
| 2026-11-13 | **Identifying and Mitigating API Misuse in Large Language Models**<br>Terry Yue Zhuo, Junda He, Jiamou Sun, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2503.22821) / [PDF](https://arxiv.org/pdf/2503.22821) |
| 2026-11-13 | **Condensing Law of Security Information**<br>Qi Tan, Tianyu Cui, Qi Li, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.17918) / [PDF](https://arxiv.org/pdf/2611.17918) |
| 2026-11-13 | **Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners**<br>Stephen Obadinma, Xiaodan Zhu | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.17910) / [PDF](https://arxiv.org/pdf/2611.17910) |
| 2026-11-13 | **RuralShield: Super Intelligence-Assisted Security Triage and Serverless Infrastructure for Resource-Constrained Healthcare**<br>Mohammad Arman Ullah, Asif Ahmed | Other LLM Security | [abstract](https://arxiv.org/abs/2611.17887) / [PDF](https://arxiv.org/pdf/2611.17887) |
| 2026-11-13 | **LLMs are Vulnerable to Malicious Requests with Indistinguishable Intent**<br>Wenzhuo Xu, Zonghao Ying, Deyue Zhang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.17818) / [PDF](https://arxiv.org/pdf/2611.17818) |
| 2026-11-13 | **Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems**<br>Krishna Mohan Guda Nagavenkata Srinivasa, Satya Phanindra Kalaga, Karthik Guda Vishnu | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.29142) / [PDF](https://arxiv.org/pdf/2606.29142) |
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
