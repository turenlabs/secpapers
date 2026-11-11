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
**2324 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-10**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 544 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 575 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 364 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 541 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 510 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 681 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 278 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1079 |
| [Other LLM Security](papers.md#other-llm-security) | 152 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-10 | **NICE: A Framework for Declarative and Machine-Checkable Vulnerability Reproduction**<br>Minh-Luân Nguyen, Olivier Levillain, Julien Malka, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.00625) / [PDF](https://arxiv.org/pdf/2606.00625) |
| 2026-11-10 | **Model-Based Authoring of SOC Simulation Exercises for Cybersecurity Education**<br>Felix Härer | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.14227) / [PDF](https://arxiv.org/pdf/2611.14227) |
| 2026-11-10 | **Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces**<br>William Lugoloobi, Samuele Marro, Jabez Magomere, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.14786) / [PDF](https://arxiv.org/pdf/2605.14786) |
| 2026-11-10 | **Rotated Robustness: A Training-Free Defense against Bit-Flip Attacks on Large Language Models**<br>Deng Liu, Song Chen | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2603.16382) / [PDF](https://arxiv.org/pdf/2603.16382) |
| 2026-11-10 | **Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models**<br>Xingqi Wang, Xiaoyuan Yi, Xing Xie, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.13997) / [PDF](https://arxiv.org/pdf/2611.13997) |
| 2026-11-10 | **From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses**<br>Simon Hegelich, Bardh Prenkaj, Habiba Sarhan, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.13960) / [PDF](https://arxiv.org/pdf/2611.13960) |
| 2026-11-10 | **Domain-Invariant and Language-Model-Assisted Acoustic Side-Channel Attacks on Keyboards**<br>Bikrant Bikram Pratap Maurya | Other LLM Security | [abstract](https://arxiv.org/abs/2611.13922) / [PDF](https://arxiv.org/pdf/2611.13922) |
| 2026-11-10 | **BadMoE: Backdooring Mixture-of-Experts LLMs via Routing-Aware Triggers and Task-Underutilized Experts**<br>Qingyue Wang, Qi Pang, Xixun Lin, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2504.18598) / [PDF](https://arxiv.org/pdf/2504.18598) |
| 2026-11-10 | **On Private Knowledge Retrieval and Private Inference for secure multi-agent systems**<br>Vicenç Torra, Maria Bras-Amorós | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.13696) / [PDF](https://arxiv.org/pdf/2611.13696) |
| 2026-11-10 | **BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities**<br>Weifeng Yuan, Zifan Chen, Yucheng Zhang, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.13684) / [PDF](https://arxiv.org/pdf/2611.13684) |
| 2026-11-10 | **Specification-based Security Evaluation of Real-World Agents Tool-Calling under Long-Horizon Context Tasks**<br>Yuchuan Fu, Minghe Wang, Xiaohan Yuan, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2506.15253) / [PDF](https://arxiv.org/pdf/2506.15253) |
| 2026-11-10 | **MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference**<br>Linru Zhang, Xiangning Wang, Jun Jie Sim, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.13641) / [PDF](https://arxiv.org/pdf/2611.13641) |
| 2026-11-10 | **POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling**<br>Haoyi Wu, Yunkai Dang, Wanyu Zhang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.13578) / [PDF](https://arxiv.org/pdf/2611.13578) |
| 2026-11-10 | **TERM: Target-Free Jailbreak Defense via Entropy-Guided Residual Modulation**<br>Yunkai Dang, Wanyu Zhang, Meiyi Zhu, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.13577) / [PDF](https://arxiv.org/pdf/2611.13577) |
| 2026-11-10 | **RoCoMark: Robust Code Watermarking Against LLM-Based Functionality-Preserving Rewriting Attacks**<br>Hongjie Zhang, Xingcheng Li, Hanzhou Wu, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.11399) / [PDF](https://arxiv.org/pdf/2611.11399) |
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
