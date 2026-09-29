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
**1466 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-28**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 326 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 369 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 231 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 340 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 316 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 456 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 181 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 702 |
| [Other LLM Security](papers.md#other-llm-security) | 98 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-28 | **Distillation Defenses Easily Break After Reinforcement Learning**<br>Shidan Javaheri, Alexander Panfilov, Oliver Britton, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35699) / [PDF](https://arxiv.org/pdf/2609.35699) |
| 2026-09-28 | **WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading**<br>Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.02177) / [PDF](https://arxiv.org/pdf/2609.02177) |
| 2026-09-28 | **Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents**<br>Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.35576) / [PDF](https://arxiv.org/pdf/2609.35576) |
| 2026-09-28 | **INTCC: A Framework for Interactive Confidential Computing**<br>Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.35552) / [PDF](https://arxiv.org/pdf/2609.35552) |
| 2026-09-28 | **LLM-Assisted Automatic Security Proofs for Cryptographic Protocols: How Far Are We?**<br>Tianjian Liu, Shicheng Feng, Jin'ao Shang, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35434) / [PDF](https://arxiv.org/pdf/2609.35434) |
| 2026-09-28 | **Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoor Triggers and Preserves Desired Traits**<br>Kajetan Dymkiewicz, Tim Farrelly, Adam Práda, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.35356) / [PDF](https://arxiv.org/pdf/2609.35356) |
| 2026-09-28 | **Continuous Assurance of Agentic Security Auditors for Software Delivery Decision Gates**<br>Guy Lupo, Nguyen Hung Nguyen, Viet Vo, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35266) / [PDF](https://arxiv.org/pdf/2609.35266) |
| 2026-09-28 | **Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis**<br>Ziyu Lin, Ziting Wang, Xinfeng Li, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2607.10315) / [PDF](https://arxiv.org/pdf/2607.10315) |
| 2026-09-28 | **EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents**<br>Fengzhou Sun, Yuan Zhang, Xintong Yu, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35233) / [PDF](https://arxiv.org/pdf/2609.35233) |
| 2026-09-28 | **TANGO: Watermarking Masked Diffusion Language Models in Token Pairs**<br>Kasra Arabi, Nir Weinberger, Micah Goldblum, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.35224) / [PDF](https://arxiv.org/pdf/2609.35224) |
| 2026-09-28 | **Trajectory-Level Security Debt in LLM Coding Agents**<br>Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35199) / [PDF](https://arxiv.org/pdf/2609.35199) |
| 2026-09-28 | **When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents**<br>Geonwoo Kim, Brent ByungHoon Kang | Other LLM Security | [abstract](https://arxiv.org/abs/2609.35088) / [PDF](https://arxiv.org/pdf/2609.35088) |
| 2026-09-28 | **How LLM Task-Adaptation Reshapes Alignment: A Multi-dimensional Study of Behavioral and Representational Drift**<br>James Elcock, William F. Shen, Xinchi Qiu, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.22676) / [PDF](https://arxiv.org/pdf/2607.22676) |
| 2026-09-28 | **Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models**<br>Qiankun Li, Yuechen Zhang, Bowen Chen, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35002) / [PDF](https://arxiv.org/pdf/2609.35002) |
| 2026-09-28 | **SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents**<br>Yuanjin Zheng, Jingbang Chen | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.21929) / [PDF](https://arxiv.org/pdf/2608.21929) |
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
