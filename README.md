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
**1978 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-20**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 453 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 483 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 309 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 477 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 438 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 589 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 239 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 937 |
| [Other LLM Security](papers.md#other-llm-security) | 128 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-20 | **A Digital Twin to Improve Cyber-Social Impact**<br>Vita Santa Barletta, Danilo Caivano, Gabriel Cellammare, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.28430) / [PDF](https://arxiv.org/pdf/2610.28430) |
| 2026-10-20 | **After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents**<br>Zhiyue Xu, Xukai Wang, Zhiyuan Huang, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.28425) / [PDF](https://arxiv.org/pdf/2610.28425) |
| 2026-10-20 | **MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems**<br>Mohammad Kachuee, Phu Mon Htut, Sheng Li, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.28397) / [PDF](https://arxiv.org/pdf/2610.28397) |
| 2026-10-20 | **Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG**<br>Abhishek Rai | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.28364) / [PDF](https://arxiv.org/pdf/2610.28364) |
| 2026-10-20 | **Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory**<br>Masahiro Kaneko, Hiromi Arai, Timothy Baldwin | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.28315) / [PDF](https://arxiv.org/pdf/2610.28315) |
| 2026-10-20 | **Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection**<br>Kieu Dang, Phung Lai, NhatHai Phan, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2605.23175) / [PDF](https://arxiv.org/pdf/2605.23175) |
| 2026-10-20 | **Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift**<br>Zhihua Wei, Qiang Li, Jian Ruan, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2603.17372) / [PDF](https://arxiv.org/pdf/2603.17372) |
| 2026-10-20 | **Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation**<br>Shayan Ali Hassan, Zaeem Mohtashim Khan, Tao Ni, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.08062) / [PDF](https://arxiv.org/pdf/2602.08062) |
| 2026-10-20 | **ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents**<br>Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.28093) / [PDF](https://arxiv.org/pdf/2610.28093) |
| 2026-10-20 | **Contextual Candour: Role-Aware Graduated Disclosure for LLMs over Mixed-Sensitivity Contexts**<br>Devansh Srivastav, David Pape, Samira Abedini, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.28067) / [PDF](https://arxiv.org/pdf/2610.28067) |
| 2026-10-20 | **Poisoning-Based Backdoors Are Not Cryptographic**<br>Masahiro Kaneko | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.28045) / [PDF](https://arxiv.org/pdf/2610.28045) |
| 2026-10-20 | **SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval**<br>Haoming Li, Dingyi Kang, Xu Hu, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.22959) / [PDF](https://arxiv.org/pdf/2610.22959) |
| 2026-10-20 | **A Unified Attack Framework against Statistical Generative Watermarks for Large Language Models**<br>Romina Omidi, Nima Naderloui, Yuan Hong, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.27653) / [PDF](https://arxiv.org/pdf/2610.27653) |
| 2026-10-20 | **The Show-Up Attack: When Subagents Win Over Their Supervisor**<br>Maosen Zhang, Jianshuo Dong, Yutong Zhang, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.27574) / [PDF](https://arxiv.org/pdf/2610.27574) |
| 2026-10-20 | **Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment**<br>Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.27548) / [PDF](https://arxiv.org/pdf/2610.27548) |
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
