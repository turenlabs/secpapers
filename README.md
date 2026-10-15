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
**1856 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-14**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 423 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 457 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 282 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 446 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 409 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 563 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 228 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 888 |
| [Other LLM Security](papers.md#other-llm-security) | 122 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-14 | **Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge**<br>Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.20570) / [PDF](https://arxiv.org/pdf/2610.20570) |
| 2026-10-14 | **From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)**<br>Alicia Colmenero-Fernández | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.20437) / [PDF](https://arxiv.org/pdf/2610.20437) |
| 2026-10-14 | **Same Request, Different Boundary: Evaluating Cybersecurity Assistance across Conversational Contexts**<br>Rui Yang, Yang Hong, Yichao Xu, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.00578) / [PDF](https://arxiv.org/pdf/2609.00578) |
| 2026-10-14 | **An Open-Source End-to-End FHE Implementation for Privacy-Preserving Llama 3 8B Inference**<br>Yuhang Fan, Yusi Chen, Kanyu Ye, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.12378) / [PDF](https://arxiv.org/pdf/2609.12378) |
| 2026-10-14 | **From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence**<br>Jiahong Qian | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.20417) / [PDF](https://arxiv.org/pdf/2610.20417) |
| 2026-10-14 | **Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis**<br>Yinzhen Huang, Jiahe Xie, Yitong Sun, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.20319) / [PDF](https://arxiv.org/pdf/2610.20319) |
| 2026-10-14 | **Towards Efficient Threat Intelligence Instruction Tuning via Quality-Aware and Optimal Transport-Guided Data Selection**<br>Jiyu Tian, Mingchu Li, Xiangwei Chen, et al. | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.20284) / [PDF](https://arxiv.org/pdf/2610.20284) |
| 2026-10-14 | **P2Patch: Exploit-Guided Vulnerability Repair**<br>Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.20245) / [PDF](https://arxiv.org/pdf/2610.20245) |
| 2026-10-14 | **Security Analysis of ChatGPT: Threats and Privacy Risks**<br>Yushan Xiang, Zhongwen Li, Xiaoqi Li | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2508.09426) / [PDF](https://arxiv.org/pdf/2508.09426) |
| 2026-10-14 | **Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety**<br>Ping Wu, Haibo Tong, Feifei Zhao, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.13304) / [PDF](https://arxiv.org/pdf/2608.13304) |
| 2026-10-14 | **GeoCloak: An Agentic Framework for Semantics-Preserving Geolocation Privacy via Peripheral Clue Manipulation**<br>Yixin Wu, Mingjie Li, Yun Shen, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.20055) / [PDF](https://arxiv.org/pdf/2610.20055) |
| 2026-10-14 | **Diagnose Before You Refine: Multi-Dimensional Judge Feedback for Query-Efficient Jailbreak Attacks**<br>Yixin Tan, Chia-Yi Hsu, Jiayang Liu, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.19971) / [PDF](https://arxiv.org/pdf/2610.19971) |
| 2026-10-14 | **Safe-FCL: Continual Risk Awareness and Fine-Grained Safety Aggregation for Federated Continual Learning of LLMs**<br>Shuaijie Ma, Yongkang Hu, Yu Cheng, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.19968) / [PDF](https://arxiv.org/pdf/2610.19968) |
| 2026-10-14 | **SecureClaw: Clawing Back Control of LLM Agents**<br>Yuhan Ma, Stefan Schmid | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2606.09549) / [PDF](https://arxiv.org/pdf/2606.09549) |
| 2026-10-14 | **DarKnight: Retrieval-Guided Agentic Framework for Breaking Dark Web CAPTCHA Gates**<br>Binghui Wu, Yeo Zi Yi, Darren Tan, et al. | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.19830) / [PDF](https://arxiv.org/pdf/2610.19830) |
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
