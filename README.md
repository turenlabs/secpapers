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
**2208 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-03**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 510 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 546 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 343 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 514 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 481 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 656 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 270 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1038 |
| [Other LLM Security](papers.md#other-llm-security) | 143 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-03 | **Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents**<br>Nivya Talokar, Ayush K Tarun, Murari Mandal, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.16346) / [PDF](https://arxiv.org/pdf/2602.16346) |
| 2026-11-03 | **MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Content**<br>Minjae Seo, Wonwoo Choi, Geonwoo Han, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.22061) / [PDF](https://arxiv.org/pdf/2608.22061) |
| 2026-11-03 | **Residual Attribute Leakage Is an Interface: Auditing Privacy Evaluation After Text De-identification**<br>Tuan Thanh Duong, Joongmin Shin, Jeongho Yoon, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.04941) / [PDF](https://arxiv.org/pdf/2611.04941) |
| 2026-11-03 | **Extracting System Prompt of LLM Services in Complex (Agentic) Settings: Hierarchical Optimization and Reliable Evaluation Metrics**<br>Shuaidong Li, Chenhao Lin, Xinshan Yang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.04803) / [PDF](https://arxiv.org/pdf/2611.04803) |
| 2026-11-03 | **ChatGPT as a Surveillance Assistant? An Exploratory Case Study of AI-Assisted Surveillance Risks**<br>Ayana Hussain, Nicholas Vincent | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.40890) / [PDF](https://arxiv.org/pdf/2610.40890) |
| 2026-11-03 | **Cyber-JEV: Matched Contrastive Fine-Tuning of Language Models for Fast Source-Code Vulnerability Triage**<br>Zhuyi Zhao, Shengjie Yuan, Shengyu Wang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.02957) / [PDF](https://arxiv.org/pdf/2611.02957) |
| 2026-11-03 | **Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees**<br>Hui Xuan Tan, Stefanos Chaliasos, Alastair F. Donaldson | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.04701) / [PDF](https://arxiv.org/pdf/2611.04701) |
| 2026-11-03 | **Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning**<br>Yao Wang, Zehua Ma, Weiming Zhang, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.04673) / [PDF](https://arxiv.org/pdf/2611.04673) |
| 2026-11-03 | **Perseus: A Full-Stack System for Homomorphic Model Inference**<br>Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.04488) / [PDF](https://arxiv.org/pdf/2611.04488) |
| 2026-11-03 | **Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code**<br>Yitong Zhang, Shiteng Lu, Jia Li | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.11817) / [PDF](https://arxiv.org/pdf/2606.11817) |
| 2026-11-03 | **TxBench: A Benchmark of Attack Transactions and Evidence-Backed Negatives on Seven EVM Chains**<br>Tamer Abdelaziz, karim Ali | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.04411) / [PDF](https://arxiv.org/pdf/2611.04411) |
| 2026-11-03 | **Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents**<br>Ilan Zendel, Matan Levy, Stav Cohen, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.04393) / [PDF](https://arxiv.org/pdf/2611.04393) |
| 2026-11-03 | **CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion**<br>Li Zheng, Simin Chen | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.04356) / [PDF](https://arxiv.org/pdf/2611.04356) |
| 2026-11-03 | **Alignment Dynamics in LLM Fine-Tuning**<br>Yuhan Huang, Huanran Chen, Yinpeng Dong | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2605.18309) / [PDF](https://arxiv.org/pdf/2605.18309) |
| 2026-11-02 | **Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems**<br>Shravya Kanchi | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.04086) / [PDF](https://arxiv.org/pdf/2611.04086) |
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
