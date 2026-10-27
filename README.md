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
**2082 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-26**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 472 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 509 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 323 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 497 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 458 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 620 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 256 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 983 |
| [Other LLM Security](papers.md#other-llm-security) | 137 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-26 | **Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models**<br>Amine Lbath, Massih-Reza Amini | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.35829) / [PDF](https://arxiv.org/pdf/2610.35829) |
| 2026-10-26 | **The Straight and Narrow: Do LLMs Possess an Internal Moral Path?**<br>Luoming Hu, Jingjie Zeng, Liang Yang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2601.10307) / [PDF](https://arxiv.org/pdf/2601.10307) |
| 2026-10-26 | **Genotypic Triggers: Exposing Pharmacogenomic Blind Spots via Host-Specific Backdoors in Generative Antimicrobial Peptide Models**<br>Doniyorkhon Obidov, Xiaolong Guo, Yonghui Li, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.06779) / [PDF](https://arxiv.org/pdf/2608.06779) |
| 2026-10-26 | **Unbiased Alignment for Large Language Models with Noisy Preferences**<br>Jialiang Wang, Xianming Liu, Xiong Zhou, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2607.03248) / [PDF](https://arxiv.org/pdf/2607.03248) |
| 2026-10-26 | **Adversary Brains: Hypothesis-Based Logical Signatures for Threat Actor Detection with LLMs**<br>Gadi Evron | Other LLM Security | [abstract](https://arxiv.org/abs/2610.35624) / [PDF](https://arxiv.org/pdf/2610.35624) |
| 2026-10-26 | **LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes**<br>Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.06795) / [PDF](https://arxiv.org/pdf/2608.06795) |
| 2026-10-26 | **Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning**<br>Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.35477) / [PDF](https://arxiv.org/pdf/2610.35477) |
| 2026-10-26 | **Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems**<br>Zihao Zhu, Siwei Lyu, Adel Bibi, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.30383) / [PDF](https://arxiv.org/pdf/2609.30383) |
| 2026-10-26 | **Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security**<br>Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.35451) / [PDF](https://arxiv.org/pdf/2610.35451) |
| 2026-10-26 | **Beyond LLM-GA: Secure Fluid Antenna Systems with ReEvo-Designed Memetic Algorithm**<br>Hanyong Xu, Zhaolai Dang, Tong Zhang | Other LLM Security | [abstract](https://arxiv.org/abs/2610.10235) / [PDF](https://arxiv.org/pdf/2610.10235) |
| 2026-10-26 | **Can Open Be Too Open? On the Security and Trustworthiness of Fully Transparent LLMs**<br>Sheila Zingg, Florian Tramèr, Martin Vechev, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.35199) / [PDF](https://arxiv.org/pdf/2610.35199) |
| 2026-10-26 | **SoK: Timestamps Are Not a Time Model: Rethinking Temporal Reasoning in Host-Based Intrusion Detection**<br>Rene Heinzl, Markus Nissl | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.35151) / [PDF](https://arxiv.org/pdf/2610.35151) |
| 2026-10-26 | **CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems**<br>Yujia Zheng, Tianhao Li, Shangzhi Xu, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.35082) / [PDF](https://arxiv.org/pdf/2610.35082) |
| 2026-10-26 | **Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs**<br>Seunghyun Lee, Dongyoon Han, Sangdoo Yun | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2607.18639) / [PDF](https://arxiv.org/pdf/2607.18639) |
| 2026-10-26 | **A Cross-Modal Prompt Injection Attack against Large Vision-Language Models with Image-Only Perturbation**<br>Hao Yang, Zhuo Ma, Yang Liu, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2605.16090) / [PDF](https://arxiv.org/pdf/2605.16090) |
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
