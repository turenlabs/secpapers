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
**1824 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-13**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 412 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 446 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 277 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 438 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 403 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 556 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 223 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 872 |
| [Other LLM Security](papers.md#other-llm-security) | 121 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-13 | **What Users See Is Not What Models Read: Split-View PDFs in Document-to-LLM Supply Chains**<br>Side Liu, Jiang Ming | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.15020) / [PDF](https://arxiv.org/pdf/2606.15020) |
| 2026-10-13 | **One Skill, Two Masters: Serving Users and Attackers through Skill Injection**<br>Haochang Hao, Dehai Min, Zhifang Zhang, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.07943) / [PDF](https://arxiv.org/pdf/2606.07943) |
| 2026-10-13 | **DPOison-VL: Clean Preference Poisoning in Vision-Language Direct Preference Optimization**<br>Chengtao Jian, Kai Yang | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.18609) / [PDF](https://arxiv.org/pdf/2610.18609) |
| 2026-10-13 | **Secure Speculative Decoding for Large Language Models**<br>Yichi Zhang, Zhiqi Wang, Neil Gong, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.08678) / [PDF](https://arxiv.org/pdf/2610.08678) |
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.18566) / [PDF](https://arxiv.org/pdf/2610.18566) |
| 2026-10-13 | **Towards Safe Autonomy for Computer Use**<br>Dominik Seip, Bartol Markovinović, Matthias Hein | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.18508) / [PDF](https://arxiv.org/pdf/2610.18508) |
| 2026-10-13 | **LLM Alignment--Utility Asymmetry under Semantic-Preserving Transformations**<br>Mohan Li, Chengyu Yu, Francesco Sovrano, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.32717) / [PDF](https://arxiv.org/pdf/2609.32717) |
| 2026-10-13 | **Adaptive Co-Serving LLM Watermarking on Modern Inference Engines**<br>Kieu Dang, Phung Lai, Ching-Yun Ko, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.03955) / [PDF](https://arxiv.org/pdf/2610.03955) |
| 2026-10-13 | **Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents**<br>Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.18457) / [PDF](https://arxiv.org/pdf/2610.18457) |
| 2026-10-13 | **FedGraph: Defending Federated Large Language Model Fine-Tuning Against Backdoor Attacks via Graph-Based Aggregation**<br>Xi Chen, Chunyi Zhou, Rui Zeng, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.18430) / [PDF](https://arxiv.org/pdf/2610.18430) |
| 2026-10-13 | **Pin It on Anyone: Certified Targeted Displacement of Multi-Bit LLM Watermarks Without the Key**<br>Paweł Batorski, Przemysław Spurek, Paul Swoboda | Other LLM Security | [abstract](https://arxiv.org/abs/2610.18359) / [PDF](https://arxiv.org/pdf/2610.18359) |
| 2026-10-13 | **Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees**<br>Wenbin Hu, Huihao Jing, Haochen Shi, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.18326) / [PDF](https://arxiv.org/pdf/2610.18326) |
| 2026-10-13 | **Encrypted Skills Can Become New Security Exploits If AI Agents Know How to Decipher**<br>Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu | Other LLM Security | [abstract](https://arxiv.org/abs/2610.18262) / [PDF](https://arxiv.org/pdf/2610.18262) |
| 2026-10-13 | **TIBlender: Early-Warning Threat Intelligence from Cross-Platform Social Media Evidence**<br>Hiroki Nakano, Takashi Koide, Daiki Chiba | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.04580) / [PDF](https://arxiv.org/pdf/2606.04580) |
| 2026-10-13 | **Surviving the Router: Optimizing Skill Injections for Retrieval and Execution**<br>Haneen Najjar, Luca Scionis, Haritz Puerto, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.08098) / [PDF](https://arxiv.org/pdf/2610.08098) |
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
