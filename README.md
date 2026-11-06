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
**2247 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-05**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 522 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 554 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 351 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 523 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 490 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 663 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 272 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1052 |
| [Other LLM Security](papers.md#other-llm-security) | 147 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-05 | **The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI**<br>Julian Kunkel, Ali Doosthosseini | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.08428) / [PDF](https://arxiv.org/pdf/2611.08428) |
| 2026-11-05 | **LABBA: LLM-Assisted Behavioral Biometric Authentication**<br>Howard Halim, Eyasu Getahun Chekole, Jianying Zhou | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.08343) / [PDF](https://arxiv.org/pdf/2611.08343) |
| 2026-11-05 | **Decision Models as Retrieval Gates Against Injection and Pollution**<br>Mahdi Ghadamyari, Reza Habibi | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.08325) / [PDF](https://arxiv.org/pdf/2611.08325) |
| 2026-11-05 | **Escalate or Close: How Fast-Tier Models Handle Held-Out Web Attack Families in Two-Tier Triage**<br>Maciej Kisielewicz, Michał Kędziora, Ngoc Thanh Nguyen | Other LLM Security | [abstract](https://arxiv.org/abs/2611.08229) / [PDF](https://arxiv.org/pdf/2611.08229) |
| 2026-11-05 | **KeHoSu: Keyed Homoglyph Substitution for Authenticated Text Provenance over Copy-Paste Channels**<br>Andrei Alexandru Drăghici, Sediola Ruko, Briland Hitaj, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.08046) / [PDF](https://arxiv.org/pdf/2611.08046) |
| 2026-11-05 | **Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models**<br>Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39509) / [PDF](https://arxiv.org/pdf/2610.39509) |
| 2026-11-05 | **ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection**<br>Shuyi Miao, Xinyi Huang, Wangjie Qiu, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.04992) / [PDF](https://arxiv.org/pdf/2610.04992) |
| 2026-11-05 | **Analysis of LLM Vulnerability to GPU Soft Errors: An Instruction-Level Fault Injection Study**<br>Duo Chai, Zizhen Liu, Shuhuai Wang, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2601.19912) / [PDF](https://arxiv.org/pdf/2601.19912) |
| 2026-11-05 | **CANMentor: A Large-Small Model Collaboration Framework for CAN Bus Intrusion Detection**<br>Zhiquan Liu, Haolin Gao, Bo Wu, et al. | Privacy &amp; Data Leakage, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2611.07853) / [PDF](https://arxiv.org/pdf/2611.07853) |
| 2026-11-05 | **An Information Bottleneck for Post-hoc Memorization Mitigation in LLMs**<br>Dina EL Zein, Shashi Kumar, James Henderson | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.07669) / [PDF](https://arxiv.org/pdf/2611.07669) |
| 2026-11-05 | **Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks**<br>Rongting Zhang, Martin Bertran, Sandeep Avula, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.07640) / [PDF](https://arxiv.org/pdf/2611.07640) |
| 2026-11-05 | **Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs**<br>Seunghyun Lee, Dongyoon Han, Sangdoo Yun | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2607.18639) / [PDF](https://arxiv.org/pdf/2607.18639) |
| 2026-11-05 | **A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow**<br>Seungdeok Roh, Seokjun Ryu, Sohee Park, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.07611) / [PDF](https://arxiv.org/pdf/2611.07611) |
| 2026-11-05 | **JailBound: FOL-Guided Jailbreak Evaluation for Exploring LLM Behavioral Boundaries**<br>Fazong Wu, Xin Wang, Ming Yang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.07530) / [PDF](https://arxiv.org/pdf/2611.07530) |
| 2026-11-05 | **MemForm: Benchmarking Memory Formation Poisoning in LLM Agents**<br>Haowen Pan, Pengyang Shao, Yunshan Ma, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.14431) / [PDF](https://arxiv.org/pdf/2610.14431) |
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
