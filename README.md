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
**1007 papers** across **4 publication years**. Latest arXiv metadata update: **2026-08-31**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 225 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 253 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 148 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 243 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 225 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 324 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 122 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 482 |
| [Other LLM Security](papers.md#other-llm-security) | 71 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-08-31 | **BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing**<br>Adrians Skapars, Edoardo Manino | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.31105) / [PDF](https://arxiv.org/pdf/2608.31105) |
| 2026-08-31 | **GradSentry: Gradient Spectral Entropy for Backdoor Sample Filtering in Large Language Model Fine-Tuning**<br>Haodong Zhao, Tianyi Xu, Tianhang Zhao, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.26574) / [PDF](https://arxiv.org/pdf/2605.26574) |
| 2026-08-31 | **Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in Financial Services**<br>Fabrizio Dimino, Bhaskarjit Sarmah, Stefano Pasquali | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2603.10807) / [PDF](https://arxiv.org/pdf/2603.10807) |
| 2026-08-31 | **The Fragility of Jailbreak Robustness Across Operational States**<br>Yuna Park, Hwang Youn Kim, Yujin Kim, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30748) / [PDF](https://arxiv.org/pdf/2608.30748) |
| 2026-08-31 | **Watch your steps: Dormant Adversarial Behaviors that Activate upon LLM Finetuning**<br>Thibaud Gloaguen, Mark Vero, Robin Staab, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2505.16567) / [PDF](https://arxiv.org/pdf/2505.16567) |
| 2026-08-31 | **Learning diverse attacks on large language models for robust red-teaming and safety tuning**<br>Seanie Lee, Minsu Kim, Lynn Cherif, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2405.18540) / [PDF](https://arxiv.org/pdf/2405.18540) |
| 2026-08-31 | **T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search**<br>Hyomin Lee, Sangwoo Park, Yumin Choi, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2603.22341) / [PDF](https://arxiv.org/pdf/2603.22341) |
| 2026-08-31 | **Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models**<br>Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2604.20994) / [PDF](https://arxiv.org/pdf/2604.20994) |
| 2026-08-31 | **ECLIPSE: Self-Evolving Stealthy Prompt Injection Attack against Long-Horizon Agentic Systems**<br>Shiqian Zhao, Yangfan Zhou, Xinfeng Li, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30441) / [PDF](https://arxiv.org/pdf/2608.30441) |
| 2026-08-31 | **EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents**<br>Doyun Kim, Chanwoo Kim, Sugyeong Eo, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30429) / [PDF](https://arxiv.org/pdf/2608.30429) |
| 2026-08-31 | **Why Are LLM Backdoor Defenses Fragmented? A Feature-Level Explanation with Sparse Autoencoders**<br>Yizhe Zeng, Chenxu Niu, Wei Zhang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30403) / [PDF](https://arxiv.org/pdf/2608.30403) |
| 2026-08-31 | **Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems**<br>Lifei Liu, Haoran Yu | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.30387) / [PDF](https://arxiv.org/pdf/2608.30387) |
| 2026-08-31 | **Will the User Ever Know? Covert Indirect Prompt Injection on Tool-Using LLM Agents**<br>Yunseok Lee, Yunji Kim, Woojin Lee | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2608.30362) / [PDF](https://arxiv.org/pdf/2608.30362) |
| 2026-08-31 | **MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks**<br>Tailun Chen, Yu He, Yan Wang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.08289) / [PDF](https://arxiv.org/pdf/2512.08289) |
| 2026-08-31 | **Beyond Token-Level Guidance: Inference-Time Alignment of Specialized LLMs via Cross-Family Representation Steering**<br>Jin Gan, Xin Li, Jun Luo | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2608.30319) / [PDF](https://arxiv.org/pdf/2608.30319) |
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
