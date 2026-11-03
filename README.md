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
**2189 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-02**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 505 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 541 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 340 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 511 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 479 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 649 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 266 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1032 |
| [Other LLM Security](papers.md#other-llm-security) | 142 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-02 | **VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably**<br>Wei-Lin Chen, Zhepei Wei, Xinyu Zhu, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.03575) / [PDF](https://arxiv.org/pdf/2611.03575) |
| 2026-11-02 | **JailbreakOPT: Iterative Jailbreak Prompt Optimization with Macro-Action**<br>Ge Shi, Jun Yin, Donglin Xie, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.11425) / [PDF](https://arxiv.org/pdf/2606.11425) |
| 2026-11-02 | **MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study**<br>Farooq Shaikh, Biagio Montaruli | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.03555) / [PDF](https://arxiv.org/pdf/2611.03555) |
| 2026-11-02 | **RogueMerge: Robust and Unified Attacks against LLM Model Merging**<br>Jinghuai Zhang, Yetian He, Kunlin Cai, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2606.03344) / [PDF](https://arxiv.org/pdf/2606.03344) |
| 2026-11-02 | **IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning**<br>Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.03431) / [PDF](https://arxiv.org/pdf/2611.03431) |
| 2026-11-02 | **MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems**<br>Mohammad Kachuee, Phu Mon Htut, Sheng Li, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.28397) / [PDF](https://arxiv.org/pdf/2610.28397) |
| 2026-11-02 | **TrafficInstruct: A Multi-Task Network Traffic Dataset and Benchmark for Instruction Tuning**<br>Zhengdao Li, Hui Wen, Zixuan Wan, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.03319) / [PDF](https://arxiv.org/pdf/2611.03319) |
| 2026-11-02 | **Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction**<br>Yiwei Zha, Qingyu Meng, Herbert Bos, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.03223) / [PDF](https://arxiv.org/pdf/2611.03223) |
| 2026-11-02 | **WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference**<br>Zixun Xiong, Gaoyi Wu, Lingfeng Yao, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2603.11132) / [PDF](https://arxiv.org/pdf/2603.11132) |
| 2026-11-02 | **PentestEval: Benchmarking LLM-based Penetration Testing with Modular and Stage-Level Design**<br>Ruozhao Yang, Mingfei Cheng, Gelei Deng, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.14233) / [PDF](https://arxiv.org/pdf/2512.14233) |
| 2026-11-02 | **Cyber-JEV: Matched Contrastive Fine-Tuning of Language Models for Fast Source-Code Vulnerability Triage**<br>Zhuyi Zhao, Shengjie Yuan, Shengyu Wang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.02957) / [PDF](https://arxiv.org/pdf/2611.02957) |
| 2026-11-02 | **Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck**<br>Felix Mächtle, Gautham Sriram, Manjil Neupane, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.02788) / [PDF](https://arxiv.org/pdf/2611.02788) |
| 2026-11-02 | **ATrust: Adaptive Trust Boundary Expansion for Securing LLM Agents**<br>Xu Zhang, Zhichao Lu | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.02741) / [PDF](https://arxiv.org/pdf/2611.02741) |
| 2026-11-02 | **The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants**<br>Bohan Jiang, Dawei Li, Yasin Silva, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.02689) / [PDF](https://arxiv.org/pdf/2611.02689) |
| 2026-11-02 | **AgentTypo: Adaptive Typographic Prompt Injection Attacks against Black-box Multimodal Agents**<br>Yanjie Li, Yiming Cao, Dong Wang, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.04257) / [PDF](https://arxiv.org/pdf/2510.04257) |
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
