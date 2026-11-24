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
**2491 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-22**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 581 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 602 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 395 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 583 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 545 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 726 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 300 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1150 |
| [Other LLM Security](papers.md#other-llm-security) | 159 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-22 | **FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems**<br>Fanxiao Li, Jiaying Wu, Tingchao Fu, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.11514) / [PDF](https://arxiv.org/pdf/2605.11514) |
| 2026-11-22 | **Persistent Jailbreak Backdoor Attack**<br>Haichuan Zhang, Xinyu Sun, Shih-Chieh Dai, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.29217) / [PDF](https://arxiv.org/pdf/2611.29217) |
| 2026-11-22 | **Ziv Meets Sumcheck: Zero-Knowledge Proofs of Floating-Point LLM Inference**<br>Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.29188) / [PDF](https://arxiv.org/pdf/2611.29188) |
| 2026-11-21 | **To See is Not to Learn: Protecting Multimodal Data from Unauthorized Fine-Tuning of Large Vision-Language Models**<br>Chengshuai Zhao, Zhen Tan, Dawei Li, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2605.14291) / [PDF](https://arxiv.org/pdf/2605.14291) |
| 2026-11-21 | **Operational Assurance for LLM-Based Systems under Governance Opacity**<br>Pedro Pinacho-Davidson | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.28834) / [PDF](https://arxiv.org/pdf/2611.28834) |
| 2026-11-21 | **When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design**<br>Mingjie Bao, Yu Dai, Guangke Chen, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.28823) / [PDF](https://arxiv.org/pdf/2611.28823) |
| 2026-11-21 | **Synthetic EHR Generators Should Be Audited Like LLMs**<br>Inigo Stibbe, Padmanabhan Ramnarayan, A. Aldo Faisal | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.28804) / [PDF](https://arxiv.org/pdf/2611.28804) |
| 2026-11-21 | **LLM-Based Website Classification for Targeted Web Measurements**<br>Simone Bozzolan, Stefano Calzavara, Lorenzo Cazzaro | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.08101) / [PDF](https://arxiv.org/pdf/2510.08101) |
| 2026-11-21 | **Distillation Defenses Easily Break After Reinforcement Learning**<br>Shidan Javaheri, Alexander Panfilov, Oliver Britton, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35699) / [PDF](https://arxiv.org/pdf/2609.35699) |
| 2026-11-21 | **Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub**<br>Gabi Nakibly, Zvika Babo | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.28763) / [PDF](https://arxiv.org/pdf/2611.28763) |
| 2026-11-21 | **Physical regime changes expose formula misuse in large language models**<br>Maohao Ran, Yanting Zhang, Chendong Ma, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.28669) / [PDF](https://arxiv.org/pdf/2611.28669) |
| 2026-11-21 | **Mitigating Backdoors in Masked Diffusion Language Models**<br>Chengzhong Wang, Lang Lin, Shengfang Zhai, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.28640) / [PDF](https://arxiv.org/pdf/2611.28640) |
| 2026-11-21 | **Right Verdict, Right Reason? An Execution-Grounded Study of Whether LLM Vulnerability Detectors Understand Vulnerabilities**<br>Leizhen Zhang, Sheng Chen | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.28584) / [PDF](https://arxiv.org/pdf/2611.28584) |
| 2026-11-21 | **Beyond Unit Tests: Path-Aware Rubric-Guided LLM Autograding of Notebooks**<br>Salman Hajizada, Mohammed Yusuf Ansari, Gianni Di Caro | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.28565) / [PDF](https://arxiv.org/pdf/2611.28565) |
| 2026-11-21 | **Weight-Space Backdoors in Open-Weight LLMs: Cross-Architecture Attacks and Blind Model Forensics**<br>Mohammed Tanveer | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.28543) / [PDF](https://arxiv.org/pdf/2611.28543) |
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
