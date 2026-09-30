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
**1507 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-29**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 341 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 379 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 235 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 351 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 326 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 467 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 186 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 723 |
| [Other LLM Security](papers.md#other-llm-security) | 100 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-29 | **Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation**<br>Yixuan Liu | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.33401) / [PDF](https://arxiv.org/pdf/2609.33401) |
| 2026-09-29 | **Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment**<br>Haotian Deng, Wenbin Xing, Gang Xu, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.37837) / [PDF](https://arxiv.org/pdf/2609.37837) |
| 2026-09-29 | **TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking**<br>Churui Zeng, Kedong Xiu, Weiwei Qi, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2605.30883) / [PDF](https://arxiv.org/pdf/2605.30883) |
| 2026-09-29 | **Selective Channel Restoration for Backdoored Vision-Language Models**<br>Shuming Liu, Zhifang Zhang, Suqin Yuan, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.37759) / [PDF](https://arxiv.org/pdf/2609.37759) |
| 2026-09-29 | **Where Do LLMs Decide to Break the Rules? Mechanistic Localization of Prompt Injection Compliance**<br>Rui Wen, Jiayang Liu, Zeyu Yang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.37737) / [PDF](https://arxiv.org/pdf/2609.37737) |
| 2026-09-29 | **Reasoning Hijacking: The Fragility of Reasoning Alignment in Large Language Models**<br>Yuansen Liu, Yixuan Tang, Anthony Kum Hoe Tung | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2601.10294) / [PDF](https://arxiv.org/pdf/2601.10294) |
| 2026-09-29 | **BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models**<br>Jiaqi Xue, Mengxin Zheng, Yebowen Hu, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2406.00083) / [PDF](https://arxiv.org/pdf/2406.00083) |
| 2026-09-29 | **Concealing LLM-Based Multi-Agent Topology via Phantom Structure Injection**<br>Longzhu He, Zelang Wen, Xinfeng Li, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.37567) / [PDF](https://arxiv.org/pdf/2609.37567) |
| 2026-09-29 | **Confidence-Guided Protocol IR for LLM-Aided Security Protocol Modeling**<br>Siqi Li, Yufan Cai, Hongshu Wang, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.37396) / [PDF](https://arxiv.org/pdf/2609.37396) |
| 2026-09-29 | **Backdoor Mitigation in Decentralized LLM Fine-Tuning**<br>Sayan Biswas, Jade Garcia Bourrée, Rachid Guerraoui, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.37367) / [PDF](https://arxiv.org/pdf/2609.37367) |
| 2026-09-29 | **Beyond Semantic Narrowing: Robust and Efficient LLM Watermarking with Hamming Neighborhoods**<br>Zewen Sun, Tongyang Zhao, Liyao Xiang, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.37218) / [PDF](https://arxiv.org/pdf/2609.37218) |
| 2026-09-29 | **ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents**<br>Yanjie Li, Xiangyu He, Xuelong Dai, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2609.37196) / [PDF](https://arxiv.org/pdf/2609.37196) |
| 2026-09-29 | **actr: aligning thoughts and responses for multilingual safety in reasoning llms**<br>Xianhui Zhang, Jian Yu, Chengyu Xie, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.37054) / [PDF](https://arxiv.org/pdf/2609.37054) |
| 2026-09-29 | **Controlled Decoding Attacks on Black-Box LLMs**<br>Jesson Wang, Shawn Li, Wei Yang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.36956) / [PDF](https://arxiv.org/pdf/2609.36956) |
| 2026-09-29 | **Practical Secrets Extraction against Black-box LLMs**<br>Shiqian Zhao, Siwei Jiang, Xinfeng Li, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.36941) / [PDF](https://arxiv.org/pdf/2609.36941) |
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
