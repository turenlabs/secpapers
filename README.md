<div align="center">

# SecPapers

**A living, searchable catalog of large language model security research.**

[![Update papers](https://github.com/turenlabs/secpapers/actions/workflows/update.yml/badge.svg)](https://github.com/turenlabs/secpapers/actions/workflows/update.yml)
[![CI](https://github.com/turenlabs/secpapers/actions/workflows/ci.yml/badge.svg)](https://github.com/turenlabs/secpapers/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-0f766e.svg)](LICENSE)
[![Data: JSON + CSV](https://img.shields.io/badge/data-JSON%20%2B%20CSV-334155.svg)](data)

[Browse all papers](papers.md) | [Use the dataset](data/papers.json) | [Methodology](docs/methodology.md) | [Suggest a paper](https://github.com/turenlabs/secpapers/issues/new?template=paper.yml)

</div>

SecPapers tracks both sides of LLM security: research that makes language
models safer, and research that applies language models to cybersecurity. It
queries arXiv every day, applies a transparent relevance filter, deduplicates
paper revisions, and regenerates this repository from stable source data.

## At a glance

<!-- SECPAPERS:STATS:START -->
**934 papers** across **4 publication years**. Latest arXiv metadata update: **2026-08-27**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 205 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 235 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 137 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 219 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 211 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 309 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 117 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 442 |
| [Other LLM Security](papers.md#other-llm-security) | 65 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-08-27 | **RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution**<br>Junjie Zhang, Hui Liu, Kecheng Chen, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.27439) / [PDF](https://arxiv.org/pdf/2608.27439) |
| 2026-08-27 | **When Context Gets Root: Privilege Escalation in LLM Harnesses**<br>Xingbang He, Yuanwei Chen, Yi Qian, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2608.27299) / [PDF](https://arxiv.org/pdf/2608.27299) |
| 2026-08-27 | **SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control**<br>Dylan Girrens, Guangjing Wang | Other LLM Security | [abstract](https://arxiv.org/abs/2608.27234) / [PDF](https://arxiv.org/pdf/2608.27234) |
| 2026-08-27 | **Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot**<br>Yuyang Dai, Yushun Dong | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2606.15810) / [PDF](https://arxiv.org/pdf/2606.15810) |
| 2026-08-27 | **X-WAD: eXplainable Web Anomaly Detection**<br>Matteo Bitussi, Roberto Doriguzzi-Corin | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.27172) / [PDF](https://arxiv.org/pdf/2608.27172) |
| 2026-08-27 | **Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents**<br>Chenhao Wu, Haoxuan Jia, Yang Liu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.27141) / [PDF](https://arxiv.org/pdf/2608.27141) |
| 2026-08-27 | **LAAF: A Layered Accountability Architecture Framework for LLM Applications**<br>Prachi Chaturvedi, Shahnawaz Ahmad, Ehsan Nowroozi, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.27102) / [PDF](https://arxiv.org/pdf/2608.27102) |
| 2026-08-27 | **The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents**<br>Md Habibur Rahman, Jaeho Kim | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.27092) / [PDF](https://arxiv.org/pdf/2608.27092) |
| 2026-08-27 | **MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration**<br>Miseon Yu, Jaehoon Choi, Younghan Lee, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2608.25457) / [PDF](https://arxiv.org/pdf/2608.25457) |
| 2026-08-27 | **PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?**<br>Yitian Zhou, Jingyu Zheng, Qiliang Jiang, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.26882) / [PDF](https://arxiv.org/pdf/2608.26882) |
| 2026-08-27 | **PPE-Bench: A Benchmark for Evaluating MLLM Unlearning under Private-Public Entanglement**<br>Xianren Zhang, Delvin Ce Zhang, Dongwon Lee, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.02897) / [PDF](https://arxiv.org/pdf/2607.02897) |
| 2026-08-27 | **KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference**<br>Yuhao Liu, Yingnan Zhou, Weijie Liu, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.26699) / [PDF](https://arxiv.org/pdf/2608.26699) |
| 2026-08-27 | **Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation**<br>Minh Tran, Cuong Dang, Tuc Nguyen, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.24977) / [PDF](https://arxiv.org/pdf/2608.24977) |
| 2026-08-27 | **Beyond Vector Hiding: Breaking and Mitigating Shared-Direction Weight Obfuscation in TEE-Offloaded Large Language Models**<br>Menghui Zhang, Aoying Zheng, Guoxiao Liu, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2608.26651) / [PDF](https://arxiv.org/pdf/2608.26651) |
| 2026-08-27 | **Subspace Alignment for Vision-Language Model Test-time Adaptation**<br>Zhichen Zeng, Wenxuan Bao, Xiao Lin, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2601.08139) / [PDF](https://arxiv.org/pdf/2601.08139) |
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
                   README.md + papers.md + CSV
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
