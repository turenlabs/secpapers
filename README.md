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
**2551 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-25**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 597 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 616 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 407 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 597 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 555 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 750 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 303 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1174 |
| [Other LLM Security](papers.md#other-llm-security) | 165 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-25 | **A Survey of Security, Privacy, and Ethics of Large Language Models in Telecom**<br>Joy Bose, Srinivas Adyapak | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.34868) / [PDF](https://arxiv.org/pdf/2611.34868) |
| 2026-11-25 | **VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models**<br>Jiaming Luo, Jiacheng Ji, Haoan Jin, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.34819) / [PDF](https://arxiv.org/pdf/2611.34819) |
| 2026-11-25 | **VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents**<br>Yurong Hao, Wen Zhou, Guowei Guan, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.38270) / [PDF](https://arxiv.org/pdf/2609.38270) |
| 2026-11-25 | **IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol**<br>Yunhao Yao, Zhiqiang Wang, Haoran Cheng, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.14166) / [PDF](https://arxiv.org/pdf/2512.14166) |
| 2026-11-25 | **C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems**<br>Guowei Guan, Yurong Hao, Jiaming Zhang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.32780) / [PDF](https://arxiv.org/pdf/2611.32780) |
| 2026-11-25 | **From Models to Services: Systematizing Security Assurance for Model-as-a-Service**<br>Jianming Zhou, Yang Luo, Guangpu Chen, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.34623) / [PDF](https://arxiv.org/pdf/2611.34623) |
| 2026-11-25 | **Know the Design, Pick the Attack: Sentence-Keyed Watermarks for LLMs**<br>Jon Carmona, Jon Irureta, Jon Imaz, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.34505) / [PDF](https://arxiv.org/pdf/2611.34505) |
| 2026-11-25 | **ACTR: Aligning Thoughts and Responses for Multilingual Safety in Reasoning LLMs**<br>Xianhui Zhang, Jian Yu, Chengyu Xie, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.37054) / [PDF](https://arxiv.org/pdf/2609.37054) |
| 2026-11-25 | **AgentLens: Graph-guided Security Auditing for LLM-based Agents**<br>Peizhuo Lv, Tao Chen, Mengya Shi, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.34380) / [PDF](https://arxiv.org/pdf/2611.34380) |
| 2026-11-25 | **Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models**<br>Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39509) / [PDF](https://arxiv.org/pdf/2610.39509) |
| 2026-11-25 | **Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems**<br>Manit Baser, Vyoman Jain, Rachel Yeo Hui Min, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.34278) / [PDF](https://arxiv.org/pdf/2611.34278) |
| 2026-11-25 | **Train-Only-Constrained LM for Synthetic Clinical Trajectories: Leak-Safe Calibration and Auditable Dynamics**<br>Yaser Kord, Moritz Hess | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.34258) / [PDF](https://arxiv.org/pdf/2611.34258) |
| 2026-11-25 | **Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems**<br>Xiaoqing Wang, Keman Huang, Bin Liang, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2511.18467) / [PDF](https://arxiv.org/pdf/2511.18467) |
| 2026-11-25 | **The Detour Is the Danger: Preserving Security During LLM Agent Recovery**<br>Boyang Ma, Jinku Li, Hao Wu, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.33605) / [PDF](https://arxiv.org/pdf/2611.33605) |
| 2026-11-24 | **Benchmarking Open-Ended Vulnerability Discovery in Windows Kernel Binaries**<br>Jongseong Kim, Hwiwon Lee, Dongjun Kim, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.33486) / [PDF](https://arxiv.org/pdf/2611.33486) |
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
