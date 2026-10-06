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
**1656 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-05**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 379 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 413 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 255 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 393 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 372 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 513 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 204 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 798 |
| [Other LLM Security](papers.md#other-llm-security) | 105 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-05 | **TranScope: What the Software Hides About LLM Training Data, the Hardware Reveals at Scale, and Accelerators Magnify**<br>Joshua Kalyanapu, Darsh Asher, Kaushal Mhapsekar, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.06848) / [PDF](https://arxiv.org/pdf/2610.06848) |
| 2026-10-05 | **Reward Stealing Attack on Large Language Models**<br>Jiaming Qian, Pengyang Zhou, Jiahe Xu, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.06670) / [PDF](https://arxiv.org/pdf/2610.06670) |
| 2026-10-05 | **Does AI Help Cyber Attackers or Defenders? Evidence from Nonpublic Vulnerabilities and Subsequent Attacks**<br>Tobias Heldt, Matt Turk, Christoph Landolt, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.06584) / [PDF](https://arxiv.org/pdf/2610.06584) |
| 2026-10-05 | **An Evaluation of the Semantic Understanding Capabilities of Large Language Models for Web Attack Payloads**<br>Hao Sun, Yibin Yao, Chaohai Xie, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.06507) / [PDF](https://arxiv.org/pdf/2610.06507) |
| 2026-10-05 | **Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents**<br>Yongxiang Li, Moxin Li, Zhixin Ma, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.28201) / [PDF](https://arxiv.org/pdf/2605.28201) |
| 2026-10-05 | **RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents**<br>Mohamed Dhouib, Clement Elliker, Alexi Canesse, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.06401) / [PDF](https://arxiv.org/pdf/2610.06401) |
| 2026-10-05 | **Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning**<br>Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.06366) / [PDF](https://arxiv.org/pdf/2610.06366) |
| 2026-10-05 | **DP-ES: Differentially Private Evolution Strategies for Prompt Optimization**<br>Ziniu Liu, Aiping Li, Yue Han, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.06236) / [PDF](https://arxiv.org/pdf/2610.06236) |
| 2026-10-05 | **Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection**<br>Takashi Koide, Hiroki Nakano, Daiki Chiba | Prompt Injection &amp; Jailbreaks, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.05484) / [PDF](https://arxiv.org/pdf/2602.05484) |
| 2026-10-05 | **Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair**<br>Wenji Bai, Muhammad Waseem, Zeeshan Rasheed, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.06163) / [PDF](https://arxiv.org/pdf/2610.06163) |
| 2026-10-05 | **Benchmarking Jailbreak Guardrails for Embodied Agents**<br>Xunguang Wang, Qingyue Wang, Yuguang Zhou, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.06122) / [PDF](https://arxiv.org/pdf/2610.06122) |
| 2026-10-05 | **Large Language Models for Agentic NetOps and AIOps: Architectures, Evaluation, and Safety**<br>Muhammad Bilal, Jon Crowcroft, Ruizhi Wang, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.12729) / [PDF](https://arxiv.org/pdf/2605.12729) |
| 2026-10-05 | **Cross-Lingual Transferability of Training Data Extraction Attacks to Recover Memorized PII**<br>Alexandru Nazare, Agnese Profico, Nicolò Vania, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.06093) / [PDF](https://arxiv.org/pdf/2610.06093) |
| 2026-10-05 | **Backdooring Sparse Autoencoders**<br>Enrico Ahlers, Daniel Passon, Tobias Kiecker, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.06049) / [PDF](https://arxiv.org/pdf/2610.06049) |
| 2026-10-05 | **PPFedIT: Towards Privacy-Preserving Federated Instruction Tuning with Few-shot Local Examples**<br>Zhuo Zhang, Jingyuan Zhang, Jintao Huang, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2403.06131) / [PDF](https://arxiv.org/pdf/2403.06131) |
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
