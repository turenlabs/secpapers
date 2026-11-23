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
**2476 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-20**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 577 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 601 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 391 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 579 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 542 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 723 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 299 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1145 |
| [Other LLM Security](papers.md#other-llm-security) | 159 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-20 | **Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models**<br>Xuyang Liu, Zhiwei Xu, Zirui Li, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.27920) / [PDF](https://arxiv.org/pdf/2611.27920) |
| 2026-11-20 | **Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks**<br>Nathan Nour Houlamy, Mattia Favretto, Earlence Fernandes, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27860) / [PDF](https://arxiv.org/pdf/2611.27860) |
| 2026-11-20 | **BinXSight: Fast Binary Program Summarization via Hierarchical Modular Decomposition**<br>Zhijie Liu, Zhipeng Xue, Zhipeng Gao, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.27816) / [PDF](https://arxiv.org/pdf/2611.27816) |
| 2026-11-20 | **SYSEVOLVE: Safe, Autonomous Attack-Defense Co-evolution for Evolving Cyber Defense**<br>Yuhan Meng, Jiandong Jin, Shaofei Li, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.15012) / [PDF](https://arxiv.org/pdf/2608.15012) |
| 2026-11-20 | **GRAML: Graph-Grounded Reasoning and Multi-Task Learning for LLM-Based Software Vulnerability Detection**<br>Ruohan Li, Miaoqing Tian, Haipeng Qu, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.09605) / [PDF](https://arxiv.org/pdf/2610.09605) |
| 2026-11-20 | **Mjolnir: Finding and Reproducing Vulnerabilities in Root-of-Trust Firmware and RTL with Project-Grounded Agents**<br>Collin MacDonald, Carl Lundin, Stephen Herwig, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27567) / [PDF](https://arxiv.org/pdf/2611.27567) |
| 2026-11-20 | **Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs**<br>Feng Huang, Qiang Huang, Yue Gao, et al. | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.27426) / [PDF](https://arxiv.org/pdf/2611.27426) |
| 2026-11-20 | **TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming**<br>Ahaan Dabholkar, Harshvardhan Patel, Michalis Polychronakis, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27425) / [PDF](https://arxiv.org/pdf/2611.27425) |
| 2026-11-20 | **Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization**<br>Ramneek Agnihotri, Yingte Xu, Hans Vath | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27424) / [PDF](https://arxiv.org/pdf/2611.27424) |
| 2026-11-20 | **Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification**<br>Ali Yousefi, Nikos Komninos, Hafizul Asad | Adversarial ML, Poisoning &amp; Backdoors, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27410) / [PDF](https://arxiv.org/pdf/2611.27410) |
| 2026-11-20 | **Suspected Until Inspected: Neuro-Symbolic Detection of Broken Access Control in Server-Side Web Applications**<br>Chengyao Yang, Zifeng Kang, Dongqi Han, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.27270) / [PDF](https://arxiv.org/pdf/2611.27270) |
| 2026-11-20 | **FUSE: A Modular Framework for Evaluating Dangerous Capabilities of LLMs**<br>Zhengyi Jin, Ru Zhang, Xinbo Liu, et al. | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.02168) / [PDF](https://arxiv.org/pdf/2609.02168) |
| 2026-11-20 | **Learning Adaptive Defense Strategies: Fine-Tuned LLMs for Network Security Games under Network Mobility**<br>Md Abu Sayed, Asif Rahman, Ahmed Ryen, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.27180) / [PDF](https://arxiv.org/pdf/2611.27180) |
| 2026-11-20 | **Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted Data**<br>Linru Zhang, Jun Jie Sim, Xiangning Wang, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.27175) / [PDF](https://arxiv.org/pdf/2611.27175) |
| 2026-11-20 | **Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models**<br>Mark Russinovich | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.17202) / [PDF](https://arxiv.org/pdf/2608.17202) |
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
