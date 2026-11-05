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
**2229 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-04**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 517 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 549 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 348 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 519 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 486 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 660 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 270 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1044 |
| [Other LLM Security](papers.md#other-llm-security) | 145 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-04 | **Phantoms and Disclosures: A Statistical Framework for Auditing Privacy in Synthetic Data**<br>Kareem Amin, Rudrajit Das, Alessandro Epasto, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2606.16952) / [PDF](https://arxiv.org/pdf/2606.16952) |
| 2026-11-04 | **SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents**<br>Guoqin Xiong, Shengtao Wen, Xiang Chen, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.06682) / [PDF](https://arxiv.org/pdf/2611.06682) |
| 2026-11-04 | **Addition by Subtraction: Toward Mitigating Fragile Safety Alignment in Large Language Models**<br>Hamid Dashtbani, Alexandra Dmitrienko | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.06553) / [PDF](https://arxiv.org/pdf/2611.06553) |
| 2026-11-04 | **Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models**<br>Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39509) / [PDF](https://arxiv.org/pdf/2610.39509) |
| 2026-11-04 | **From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection**<br>Chaomeng Lu, Bert Lagaisse | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.10485) / [PDF](https://arxiv.org/pdf/2512.10485) |
| 2026-11-04 | **Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation**<br>Georgios Feretzakis, Alexandros Papaspyridis | Other LLM Security | [abstract](https://arxiv.org/abs/2611.06498) / [PDF](https://arxiv.org/pdf/2611.06498) |
| 2026-11-04 | **Towards Early Warning of Real-World Vulnerabilities: An Evidence-Aware Decoupled Method for CVSS Vector Prediction Based on Unstructured Disclosures**<br>Jianhong Ma, Wenhao Li, Xixing Li, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.06477) / [PDF](https://arxiv.org/pdf/2611.06477) |
| 2026-11-04 | **LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments**<br>Chiyu Zhang, Lu Zhou, Xiaogang Xu, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.10779) / [PDF](https://arxiv.org/pdf/2605.10779) |
| 2026-11-04 | **DUP: Detection-guided Unlearning for Backdoor Purification in Language Models**<br>Man Hu, Yahui Ding, Yatao Yang, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2508.01647) / [PDF](https://arxiv.org/pdf/2508.01647) |
| 2026-11-04 | **Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs**<br>Man Hu, Xinyi Wu, Zhufeng Suo, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.07697) / [PDF](https://arxiv.org/pdf/2510.07697) |
| 2026-11-04 | **CoRTeC: A Differentially Private Release for Synthetic Tabular Data, Decodable by Any Generator**<br>Calister Nnona | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.06342) / [PDF](https://arxiv.org/pdf/2611.06342) |
| 2026-11-04 | **A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code**<br>Jiongchi Yu, Keke Lian, Junqing Wang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.06294) / [PDF](https://arxiv.org/pdf/2611.06294) |
| 2026-11-04 | **Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks**<br>Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.06257) / [PDF](https://arxiv.org/pdf/2611.06257) |
| 2026-11-04 | **Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives**<br>Soheil Khodayari, Xuenan Zhang, Bhupendra Acharya, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2604.27202) / [PDF](https://arxiv.org/pdf/2604.27202) |
| 2026-11-04 | **Beyond the Landing Page: Website Blocking, Tracker Visibility, and Human Alignment in Automated Web Crawls**<br>A H M Nazmus Sakib, Mahsin Bin Akram, Raveen Wijewickrama, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.06197) / [PDF](https://arxiv.org/pdf/2611.06197) |
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
