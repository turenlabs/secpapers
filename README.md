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
**2018 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-22**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 462 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 493 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 315 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 485 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 444 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 599 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 250 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 957 |
| [Other LLM Security](papers.md#other-llm-security) | 131 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-22 | **Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure**<br>Pellegrino Casoria, Simon Pietro Romano | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.31573) / [PDF](https://arxiv.org/pdf/2610.31573) |
| 2026-10-22 | **AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack**<br>Justin Tan, Miao Li, Ding Zhao | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.31404) / [PDF](https://arxiv.org/pdf/2610.31404) |
| 2026-10-22 | **Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory**<br>Masahiro Kaneko, Hiromi Arai, Timothy Baldwin | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.28315) / [PDF](https://arxiv.org/pdf/2610.28315) |
| 2026-10-22 | **Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models**<br>Jinwei Gan, Zifeng Cheng, Zhiwei Jiang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.31331) / [PDF](https://arxiv.org/pdf/2610.31331) |
| 2026-10-22 | **Network topology shapes consensus and vulnerability in LLM populations**<br>Roberto Passaro, Ariel Flint, Romualdo Pastor-Satorras, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.31165) / [PDF](https://arxiv.org/pdf/2610.31165) |
| 2026-10-22 | **Poisoning-Based Backdoors Are Not Cryptographic**<br>Masahiro Kaneko | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.28045) / [PDF](https://arxiv.org/pdf/2610.28045) |
| 2026-10-22 | **WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing**<br>Mingjie Li, Yukun Jiang, Yicong Tan, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.31152) / [PDF](https://arxiv.org/pdf/2610.31152) |
| 2026-10-22 | **SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence**<br>Yifan Wang, Dongliang Xu, Xiaoyong Li, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.31000) / [PDF](https://arxiv.org/pdf/2610.31000) |
| 2026-10-22 | **ReDence: A Hybrid Agentic and Decision-Model Framework for Rapid, Evidence-Grounded Detection of Modern Social Engineering Scams**<br>Jaishnoor Kaur, Josef Horáček, Ian Waskom, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.30963) / [PDF](https://arxiv.org/pdf/2610.30963) |
| 2026-10-22 | **Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks**<br>Rohan Menon, Chih-Hong Cheng | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.26589) / [PDF](https://arxiv.org/pdf/2610.26589) |
| 2026-10-22 | **The Price of Safety: Benign-Case Utility and Token Overhead of Memory-Poisoning Defenses in LLM Agents**<br>Pritom Bhowmik | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.22818) / [PDF](https://arxiv.org/pdf/2609.22818) |
| 2026-10-22 | **Amplifying Latency and Cost of LLM Inference via Rowhammer Attack**<br>Mrityunjay Shukla, Shubham Roy, Biswabandan Panda | Other LLM Security | [abstract](https://arxiv.org/abs/2610.30798) / [PDF](https://arxiv.org/pdf/2610.30798) |
| 2026-10-22 | **AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes**<br>Jie Ying, Xutao Zhang, Ningyuan Chen, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.30738) / [PDF](https://arxiv.org/pdf/2610.30738) |
| 2026-10-22 | **MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking**<br>Yizhou Zhao, Zhiwei Steven Wu, Adam Block | Other LLM Security | [abstract](https://arxiv.org/abs/2512.04044) / [PDF](https://arxiv.org/pdf/2512.04044) |
| 2026-10-22 | **Model-intrinsic, Weight-level, and Training-free Spectral Fingerprinting for Large Language Models**<br>Yanan He, Yanli Chen, Ling Xiong, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.30626) / [PDF](https://arxiv.org/pdf/2610.30626) |
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
