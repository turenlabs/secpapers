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
**1881 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-15**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 427 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 462 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 293 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 448 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 412 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 570 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 231 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 900 |
| [Other LLM Security](papers.md#other-llm-security) | 123 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-15 | **Private Retrieval Augmented Generation via Random Projection**<br>Dixi Yao, Tahseen Rabbani, Tian Li | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.22297) / [PDF](https://arxiv.org/pdf/2610.22297) |
| 2026-10-15 | **Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs**<br>Md. Robiul Islam Niloy | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01263) / [PDF](https://arxiv.org/pdf/2610.01263) |
| 2026-10-15 | **PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents**<br>Kshitij Mishra, Abhijith Sharma, Nils Lukas, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.22124) / [PDF](https://arxiv.org/pdf/2610.22124) |
| 2026-10-15 | **SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes**<br>Mengxiao Wang, Nitesh Saxena | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.19705) / [PDF](https://arxiv.org/pdf/2609.19705) |
| 2026-10-15 | **Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection**<br>Asif Shahriar, Hongyu Cai, Hadjer Benkraouda, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.30587) / [PDF](https://arxiv.org/pdf/2606.30587) |
| 2026-10-15 | **Encoded but Exposed: Language Embeddings can Reveal More Than They Should in Recommender Systems**<br>Linda Beková, Rodrigo Alves | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.21713) / [PDF](https://arxiv.org/pdf/2610.21713) |
| 2026-10-15 | **From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents**<br>Yiqi Wang, Jiaqi Zhang, Zhangkai Wu, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.04990) / [PDF](https://arxiv.org/pdf/2606.04990) |
| 2026-10-15 | **SecureClaw: Clawing Back Control of LLM Agents**<br>Yuhan Ma, Stefan Schmid | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2606.09549) / [PDF](https://arxiv.org/pdf/2606.09549) |
| 2026-10-15 | **BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition**<br>Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.21565) / [PDF](https://arxiv.org/pdf/2610.21565) |
| 2026-10-15 | **On the Privacy of LLMs: An Ablation Study**<br>Karima Makhlouf, Lamiaa Basyoni, Syed Khaderi, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.02255) / [PDF](https://arxiv.org/pdf/2605.02255) |
| 2026-10-15 | **Poisoning the Neighborhood: A Topology-Aware Topic-Level Attack on Large-Scale HNSW-based RAG Systems**<br>Yufei Chen, Yao Wang, Haibin Zhang | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.21464) / [PDF](https://arxiv.org/pdf/2610.21464) |
| 2026-10-15 | **What Survives Self-Evolution: Provenance Marks in Copied Agent Harnesses**<br>Jieyu Li, Jingya Li, Sheng Li, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.21458) / [PDF](https://arxiv.org/pdf/2610.21458) |
| 2026-10-15 | **Evaluating and Improving Static Application Security Testing Tools for Rust**<br>Huaien Zhang, Zhengjie Zhao, Yu Pei, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.21373) / [PDF](https://arxiv.org/pdf/2610.21373) |
| 2026-10-15 | **QuasiLeak-Bench: Evaluating LLM-Based Privacy Detectors on Policy-Conditioned Quasi-Evidence Group Recovery**<br>Yufan Zhu, Yangfan Jiang, Yang Fei, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.21333) / [PDF](https://arxiv.org/pdf/2610.21333) |
| 2026-10-15 | **Combining LLM and Dynamic Analysis for Universal Testing of Static Application Security Testing Tools**<br>Huaien Zhang, Yu Pei, Hao Chen, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.21309) / [PDF](https://arxiv.org/pdf/2610.21309) |
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
