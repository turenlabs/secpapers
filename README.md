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
**1169 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-09**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 253 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 286 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 170 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 285 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 255 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 373 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 147 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 555 |
| [Other LLM Security](papers.md#other-llm-security) | 87 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-09 | **Towards Tackling Application Logic Flaws through Autonomous Formal-Logic Modeling and Automated Reasoning**<br>Yiwei Fang, Yichen Liu, Ze Jin, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.10537) / [PDF](https://arxiv.org/pdf/2609.10537) |
| 2026-09-09 | **TrajMark: Ownership Attribution and Segment-Level Tamper Localization for Coding-Agent Trajectories**<br>Bokang Zeng, Zheng Gao, Xiaoyu Li, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.10416) / [PDF](https://arxiv.org/pdf/2609.10416) |
| 2026-09-09 | **Towards Scalable and Cost-Efficient Vulnerability Detection: A Study on Automatic Query Generation**<br>Ivana Clairine Irsan, Ratnadira Widyasari, Huihui Huang, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.10412) / [PDF](https://arxiv.org/pdf/2609.10412) |
| 2026-09-09 | **Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation**<br>Santiago Perez-Acuna, Yod-Samuel Martín, Juan C. Yelmo | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.10316) / [PDF](https://arxiv.org/pdf/2609.10316) |
| 2026-09-09 | **Maverick: Private and Verifiable LLM Inference Made Practical via Matrix-Vector Multiplication Delegation**<br>Ben Merbaum, Mohammad Amin Raeisi, Wenhao Wang, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.10264) / [PDF](https://arxiv.org/pdf/2609.10264) |
| 2026-09-09 | **Active Adaptation, Not Static Defense: Temporal Dynamics of Preventative Steering in Adversarial Fine-Tuning**<br>Jing Guan, Yachao Yang, Zhaoliang Liu, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.10142) / [PDF](https://arxiv.org/pdf/2609.10142) |
| 2026-09-09 | **Chameleon: An Adaptive AI-Driven Honeypot Architecture Using Threat-Calibrated Particle Swarm Optimization and Semantic Deception Rapidly-Exploring Random Trees**<br>Rohit Swami, Tushar Singh, Akash Warde, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.15407) / [PDF](https://arxiv.org/pdf/2608.15407) |
| 2026-09-09 | **Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection**<br>Hanyi Zhou, Chenyang Li, Yuanzhe Pang, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.10117) / [PDF](https://arxiv.org/pdf/2609.10117) |
| 2026-09-09 | **Bounty Hunter: Autonomous, Comprehensive Emulation of Multi-Faceted Adversaries**<br>Louis Hackländer-Jansen, Rafael Uetz, Martin Henze | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2512.15275) / [PDF](https://arxiv.org/pdf/2512.15275) |
| 2026-09-09 | **AutoTrans: AI-Assisted Automatic Translation of Security Assertions for RISC-V Processors**<br>Sharjeel Imtiaz, Uljana Reinsalu, Tara Ghasempouri | Other LLM Security | [abstract](https://arxiv.org/abs/2609.10057) / [PDF](https://arxiv.org/pdf/2609.10057) |
| 2026-09-09 | **Belief-State Engine: Augmenting LLMs for Principled Planning Under Partial Observability**<br>Arnab Chattopadhayay, Debdipta Halder | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.10036) / [PDF](https://arxiv.org/pdf/2609.10036) |
| 2026-09-09 | **HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving**<br>Han Jin | Other LLM Security | [abstract](https://arxiv.org/abs/2609.08306) / [PDF](https://arxiv.org/pdf/2609.08306) |
| 2026-09-09 | **"Tab, Tab, Bug": Security Pitfalls of Next Edit Suggestions in AI-Integrated IDEs**<br>Yunlong Lyu, Yixuan Tang, Peng Chen, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.06759) / [PDF](https://arxiv.org/pdf/2602.06759) |
| 2026-09-09 | **CS-Guard: Benchmarking LLM Guardrails for Code Generation Security**<br>Jinyang Li, Mingyu Guo, Hung X. Nguyen | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.09798) / [PDF](https://arxiv.org/pdf/2609.09798) |
| 2026-09-09 | **Privacy-Preserving Split Learning for Federated LLM Fine-Tuning**<br>Heng Jin, Chaoyu Zhang, Hexuan Yu, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.09794) / [PDF](https://arxiv.org/pdf/2609.09794) |
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
