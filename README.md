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
**2457 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-19**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 574 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 598 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 386 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 574 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 538 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 718 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 295 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1136 |
| [Other LLM Security](papers.md#other-llm-security) | 159 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-19 | **SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research**<br>Amine Lbath, Manan Suri, Aurelien Delaitre, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.26601) / [PDF](https://arxiv.org/pdf/2611.26601) |
| 2026-11-19 | **Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)**<br>Mengxiao Wang, Mahbub Alam, Kalyan Nakka, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.26553) / [PDF](https://arxiv.org/pdf/2611.26553) |
| 2026-11-19 | **ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection**<br>Xinhang Ma, Chaowei Xiao, William Yeoh, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2608.27496) / [PDF](https://arxiv.org/pdf/2608.27496) |
| 2026-11-19 | **ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises**<br>Jaime C. Acosta, Anantaa Kotal, Aritran Piplai | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.21579) / [PDF](https://arxiv.org/pdf/2611.21579) |
| 2026-11-19 | **Static Analysis Guidance for Secure LLM Code Generation**<br>Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.26312) / [PDF](https://arxiv.org/pdf/2611.26312) |
| 2026-11-19 | **A Statistical Framework for Training Data Auditing of Large Language Models**<br>Shengjie Niu, Yeheng Ge, Jian Huang | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.26264) / [PDF](https://arxiv.org/pdf/2611.26264) |
| 2026-11-19 | **Evaluating LIM Trading Agents: A Critical Review of Backtesting Validity and Reporting Practices**<br>Long Xu, Fuyi Wang, Xiaolu Hu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24133) / [PDF](https://arxiv.org/pdf/2611.24133) |
| 2026-11-19 | **Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare**<br>Liam Kearns | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2606.28666) / [PDF](https://arxiv.org/pdf/2606.28666) |
| 2026-11-19 | **SCARVA: Interpretable Agentic Reasoning in Software Supply-Chain Analysis**<br>Tim Barsch, Bruno Nogueira, Tobias Wienand, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.26131) / [PDF](https://arxiv.org/pdf/2611.26131) |
| 2026-11-19 | **ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models**<br>Jiawei Xing, Li Wang, Xiangtao Meng, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.26117) / [PDF](https://arxiv.org/pdf/2611.26117) |
| 2026-11-19 | **EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents**<br>Doyun Kim, Chanwoo Kim, Sugyeong Eo, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30429) / [PDF](https://arxiv.org/pdf/2608.30429) |
| 2026-11-19 | **BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving**<br>Qifan Wang, Jeremy Boy, Jonas Sander, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.25945) / [PDF](https://arxiv.org/pdf/2611.25945) |
| 2026-11-19 | **ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing**<br>Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.25809) / [PDF](https://arxiv.org/pdf/2611.25809) |
| 2026-11-19 | **How Reliable Are Explanations of Language Models That Detect Insider Threats?**<br>Suramya R. Angdembay | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.25796) / [PDF](https://arxiv.org/pdf/2611.25796) |
| 2026-11-19 | **On the Reliability of CyberGym Evaluation: Task Material Consistency and Reference-Target Identity**<br>Yule Ding, Hongzhen Wu | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.25790) / [PDF](https://arxiv.org/pdf/2611.25790) |
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
