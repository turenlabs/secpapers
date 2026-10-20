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
**1954 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-19**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 451 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 476 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 304 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 468 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 431 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 585 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 238 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 929 |
| [Other LLM Security](papers.md#other-llm-security) | 127 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-19 | **Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams**<br>Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.26781) / [PDF](https://arxiv.org/pdf/2610.26781) |
| 2026-10-19 | **Proof-of-Machine-Learning-Inference: Mining Knowledge, Not Hashes**<br>Wan Ki Wong, Michele Ciampi, Rik Sarkar | Other LLM Security | [abstract](https://arxiv.org/abs/2610.26713) / [PDF](https://arxiv.org/pdf/2610.26713) |
| 2026-10-19 | **The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training**<br>Haonan Huang, Chengkun Cai | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.26655) / [PDF](https://arxiv.org/pdf/2610.26655) |
| 2026-10-19 | **Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates**<br>Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.26595) / [PDF](https://arxiv.org/pdf/2610.26595) |
| 2026-10-19 | **Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks**<br>Rohan Menon, Chih-Hong Cheng | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.26589) / [PDF](https://arxiv.org/pdf/2610.26589) |
| 2026-10-19 | **CoSec: Benchmarking Agent Security in Communities**<br>Hao Chen, Wenhui Dong, Ye Chen, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.34790) / [PDF](https://arxiv.org/pdf/2609.34790) |
| 2026-10-19 | **Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents**<br>Mengxiao Wang, Nitesh Saxena | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.26438) / [PDF](https://arxiv.org/pdf/2610.26438) |
| 2026-10-19 | **QuasiLeak-Bench: Evaluating LLM-Based Privacy Detectors on Policy-Conditioned Quasi-Evidence Group Recovery**<br>Yufan Zhu, Yangfan Jiang, Yang Fei, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.21333) / [PDF](https://arxiv.org/pdf/2610.21333) |
| 2026-10-19 | **Sequential Behavioral Watermarking for LLM Agents**<br>Hyeseon An, Shinwoo Park, Dongsu Kim, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2605.11036) / [PDF](https://arxiv.org/pdf/2605.11036) |
| 2026-10-19 | **LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context**<br>Anastasiia Kucherenko, Francois Brouchoud, Dimitri Percia David, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.26211) / [PDF](https://arxiv.org/pdf/2610.26211) |
| 2026-10-19 | **From GAN-Based Models to GPT-5: A Taxonomy-Guided Study of Human Performance in Detecting Deepfake Face Images**<br>Zhiqing Guo, Lixin Jia, Luning Sun, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23144) / [PDF](https://arxiv.org/pdf/2610.23144) |
| 2026-10-19 | **SpanGuard: Decoupling Instruction Localization from Authorization for Lightweight IPI Defense**<br>Yinxiang Wang, Zehua Ma, Kejiang Chen, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.26013) / [PDF](https://arxiv.org/pdf/2610.26013) |
| 2026-10-19 | **Flipping Minds by Flipping Bits: Decision-Level Cognitive Hijacking of Large Language Models**<br>Yu Yan, Jiahao Chen, Siqi Lu, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2607.25227) / [PDF](https://arxiv.org/pdf/2607.25227) |
| 2026-10-19 | **SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code**<br>Mirza Masfiqur Rahman, MD Ajwad Akil, Imtiaz Karim, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.26001) / [PDF](https://arxiv.org/pdf/2610.26001) |
| 2026-10-19 | **NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents**<br>Jin Han, Mingfeng Xin, Feng Liang, et al. | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.25985) / [PDF](https://arxiv.org/pdf/2610.25985) |
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
