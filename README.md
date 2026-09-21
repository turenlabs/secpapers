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
**1298 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-18**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 278 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 323 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 207 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 302 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 284 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 413 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 164 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 613 |
| [Other LLM Security](papers.md#other-llm-security) | 92 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-18 | **SRAF: Stealthy and Robust Adversarial Fingerprint for Copyright Verification of Large Language Models**<br>Zhebo Wang, Zhenhua Xu, Maike Li, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2505.06304) / [PDF](https://arxiv.org/pdf/2505.06304) |
| 2026-09-18 | **Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing**<br>Weizhe Wang, Yitong Zhang, Yao Zhang, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.07344) / [PDF](https://arxiv.org/pdf/2609.07344) |
| 2026-09-18 | **CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation**<br>Jiale Luo, Eric Han | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.21793) / [PDF](https://arxiv.org/pdf/2609.21793) |
| 2026-09-18 | **CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents**<br>Tao Huang, Guosen Wu, Guolong Zheng, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.21686) / [PDF](https://arxiv.org/pdf/2609.21686) |
| 2026-09-18 | **ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions**<br>Guosen Wu, Huizhen Huang, Guoxiong Long, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.18864) / [PDF](https://arxiv.org/pdf/2609.18864) |
| 2026-09-18 | **Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems**<br>Pedro Pereira, Eva Maia, Isabel Praça | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.21573) / [PDF](https://arxiv.org/pdf/2609.21573) |
| 2026-09-18 | **Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel**<br>Jiaji He, Yi Shi, Junfeng Cai, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.21569) / [PDF](https://arxiv.org/pdf/2609.21569) |
| 2026-09-18 | **ServeGuard: Verifiable, Bounded-Residual Confinement of Operator-Invisible Channels Without Revealing the Certified Read Factor**<br>Dominik Dahlem, Rui Vieira | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.21515) / [PDF](https://arxiv.org/pdf/2609.21515) |
| 2026-09-18 | **HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference**<br>Byeongseo Min, Yongwoo Lee, Young-Sik Kim, et al. | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.21484) / [PDF](https://arxiv.org/pdf/2609.21484) |
| 2026-09-18 | **Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision-Language Models**<br>Yining Wang, Xi Li, Mi Zhang, et al. | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.21363) / [PDF](https://arxiv.org/pdf/2609.21363) |
| 2026-09-18 | **CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices**<br>Wenquan Zhou, An Wang, Jing Liang, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.21344) / [PDF](https://arxiv.org/pdf/2609.21344) |
| 2026-09-18 | **Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees**<br>Shuo Huang, Gholamreza Haffari, Xingliang Yuan, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.21340) / [PDF](https://arxiv.org/pdf/2609.21340) |
| 2026-09-18 | **QuanText: Protecting Dataset-Level Secrets in Textual Data Sharing**<br>Shuaiqi Wang, Zinan Lin, Giulia Fanti | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.17995) / [PDF](https://arxiv.org/pdf/2609.17995) |
| 2026-09-18 | **PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs**<br>Rushabh Vipulkumar Patel, Dipo Dunsin, Mohammed Almaiah, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.18120) / [PDF](https://arxiv.org/pdf/2609.18120) |
| 2026-09-17 | **NetInspector: Measuring and Improving LLM Capabilities for Reliable Intent-Based Networking Policy Generation**<br>Yuxuan Zhang, Hongxin Hu, Guofei Gu | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.21103) / [PDF](https://arxiv.org/pdf/2609.21103) |
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
