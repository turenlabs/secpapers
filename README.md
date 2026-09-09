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
**1148 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-08**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 250 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 282 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 165 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 281 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 252 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 367 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 144 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 547 |
| [Other LLM Security](papers.md#other-llm-security) | 85 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-08 | **PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation**<br>Yixuan Liu, Zilong Zhen, Yin Wu, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.09087) / [PDF](https://arxiv.org/pdf/2609.09087) |
| 2026-09-08 | **AGMark: Attention-Guided Dynamic Watermarking for Large Vision-Language Models**<br>Yue Li, Xin Yi, Dongsheng Shi, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2602.09611) / [PDF](https://arxiv.org/pdf/2602.09611) |
| 2026-09-08 | **VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use**<br>Juan S. Santillana | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.08477) / [PDF](https://arxiv.org/pdf/2608.08477) |
| 2026-09-08 | **Measuring the Security of the Evolving Software Supply Chain: a Research Agenda**<br>Sarah Meriem Ourari | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.08810) / [PDF](https://arxiv.org/pdf/2609.08810) |
| 2026-09-08 | **Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports**<br>Akash Prakash, Boubakr Nour, Makan Pourzandi, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.08790) / [PDF](https://arxiv.org/pdf/2609.08790) |
| 2026-09-08 | **Benchmark Scores Are Pipeline-Dependent: A Reliability Audit of Cybersecurity LLM Benchmarks**<br>Aymene Berriche, Cathrine Shalby, Mohannad Alhanahnah, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.08765) / [PDF](https://arxiv.org/pdf/2609.08765) |
| 2026-09-08 | **A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors**<br>Pengxun Li, Litian Zhang, Jianwei Hou, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03884) / [PDF](https://arxiv.org/pdf/2609.03884) |
| 2026-09-08 | **Suan: Rectifying Direct Preference Safety Alignment in Large Language Models**<br>Oleksandr Cherednichenko, Roman Klypa | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.08634) / [PDF](https://arxiv.org/pdf/2609.08634) |
| 2026-09-08 | **Breaking Planner Integrity Boundary: Enviroment State-Text Injection Attack on LLM-Driven Embodied Agents**<br>Jiawei Liu, Jiacheng Guo, Tian Zhang, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2608.16806) / [PDF](https://arxiv.org/pdf/2608.16806) |
| 2026-09-08 | **What You See Is Not What AI Gets: DPAgent-in-the-Middle Defense Against AI-Groomed Deceptive Patterns**<br>Zewei Shi, Ruoxi Sun, Haoyang Li, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2606.06914) / [PDF](https://arxiv.org/pdf/2606.06914) |
| 2026-09-08 | **Structural Jailbreaks Generalize but Do Not Compound: A cross-provider and multilingual study of Involuntary In-Context Learning**<br>Tejasvi C. Addagada | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.08373) / [PDF](https://arxiv.org/pdf/2609.08373) |
| 2026-09-08 | **Do Input-Level Defenses Transfer to Observation-Level Attacks on VideoLLMs?**<br>Bangshuo Zhu, Wei Song, Yuxin Cao, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.08331) / [PDF](https://arxiv.org/pdf/2609.08331) |
| 2026-09-08 | **HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving**<br>Han Jin | Other LLM Security | [abstract](https://arxiv.org/abs/2609.08306) / [PDF](https://arxiv.org/pdf/2609.08306) |
| 2026-09-08 | **ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing**<br>Yi Ting Shen, Kentaroh Toyoda, Alex Leung | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.08256) / [PDF](https://arxiv.org/pdf/2609.08256) |
| 2026-09-08 | **Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts**<br>Yongxi Zhou, Wenbo Ye, Yuanzhe Liu, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.08236) / [PDF](https://arxiv.org/pdf/2609.08236) |
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
