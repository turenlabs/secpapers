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
**2536 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-24**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 594 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 610 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 403 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 591 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 553 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 743 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 302 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1167 |
| [Other LLM Security](papers.md#other-llm-security) | 163 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-24 | **SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment**<br>Shivank Rajput, Himanshu Singh, A. V. Subramanyam | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.33030) / [PDF](https://arxiv.org/pdf/2611.33030) |
| 2026-11-24 | **PORTA: Systematic Discovery of Vulnerabilities in Identity Brokers**<br>Zixu Zhou, Xiangyu Guo, Ilya Grishchenko, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.33015) / [PDF](https://arxiv.org/pdf/2611.33015) |
| 2026-11-24 | **Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents**<br>Jie Li, Chenxu Niu, Tongyang Wang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.32958) / [PDF](https://arxiv.org/pdf/2611.32958) |
| 2026-11-24 | **"I Do Intend to Deliver": Will LLMs Run a Marketplace Advance-Fee Scam?**<br>Megan Squire | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.32957) / [PDF](https://arxiv.org/pdf/2611.32957) |
| 2026-11-24 | **PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting**<br>Momoko Shiraishi, Yinzhi Cao, Takahiro Shinagawa | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2511.20555) / [PDF](https://arxiv.org/pdf/2511.20555) |
| 2026-11-24 | **VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems**<br>Guowei Guan, Yurong Hao, Jiaming Zhang, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2602.06409) / [PDF](https://arxiv.org/pdf/2602.06409) |
| 2026-11-24 | **C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems**<br>Guowei Guan, Yurong Hao, Jiaming Zhang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.32780) / [PDF](https://arxiv.org/pdf/2611.32780) |
| 2026-11-24 | **ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models**<br>Wonjune Seo, Minkyung Park, Saerom Park | Other LLM Security | [abstract](https://arxiv.org/abs/2611.32755) / [PDF](https://arxiv.org/pdf/2611.32755) |
| 2026-11-24 | **Red-Teaming a Sovereign LLM, Its Reasoning and Its Training Stages**<br>Hatef Otroshi Shahreza | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.32710) / [PDF](https://arxiv.org/pdf/2611.32710) |
| 2026-11-24 | **CAPTA: Identifying LLMs Behind AI Agents**<br>Kailun Yan, Yue Huang, Sisi Duan | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.32686) / [PDF](https://arxiv.org/pdf/2611.32686) |
| 2026-11-24 | **The Missing Compliance Class: LLM Graders That Collapse Jailbreak Success, and a Free Check**<br>Ruqiya Bin Safi | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.24872) / [PDF](https://arxiv.org/pdf/2610.24872) |
| 2026-11-24 | **Privacy Disclosure Control Benchmark (PDC-Bench): How Faithfully Do LLMs Keep Privacy Constraints on In-Context Disclosure Granularity?**<br>Kosuke Fujita, Daiki Nishiyama, Jun Sakuma | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.32610) / [PDF](https://arxiv.org/pdf/2611.32610) |
| 2026-11-24 | **ContextAdapt: Evaluating Contextual Adaptation and Value Alignment in LLMs**<br>Olivia Macmillan-Scott, Mirco Musolesi | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.38260) / [PDF](https://arxiv.org/pdf/2609.38260) |
| 2026-11-24 | **Analyzing Single-Bit Flips on LLMs and Their Backbone-Matched VLMs**<br>Xiaomeng Wang, Martha Larson, Zhuoran Liu, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.32503) / [PDF](https://arxiv.org/pdf/2611.32503) |
| 2026-11-24 | **Merging Cyber Threat Intelligence Through Retrieval-Augmented Generation and Small Language Models for Rich Threat Representation**<br>Nicola Deidda, Leonardo Regano, Alessandro Sanna, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.07280) / [PDF](https://arxiv.org/pdf/2609.07280) |
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
