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
**1571 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-01**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 353 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 391 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 246 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 373 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 343 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 484 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 195 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 754 |
| [Other LLM Security](papers.md#other-llm-security) | 102 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-01 | **KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards**<br>Pengfei Li, Naufal Suryanto, Sicheng Zhang, et al. | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.02206) / [PDF](https://arxiv.org/pdf/2610.02206) |
| 2026-10-01 | **Scalable Delphi: Large Language Models for Structured Risk Estimation**<br>Tobias Lorenz, Mario Fritz | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.08889) / [PDF](https://arxiv.org/pdf/2602.08889) |
| 2026-10-01 | **UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models**<br>Huawei Lin, Yingjie Lao, Tony Geng, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2502.13141) / [PDF](https://arxiv.org/pdf/2502.13141) |
| 2026-10-01 | **From Network Intrusion Detection to Blockchain-Backed Endpoint Detection and Response: Mapping the Landscape of Decentralized Detection-and-Response Architectures**<br>Yahya Shahsavari, Sara Rouhani, Kaiwen Zhang | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01872) / [PDF](https://arxiv.org/pdf/2610.01872) |
| 2026-10-01 | **Walking the Embedding Space: Datastore Extraction from Multimodal RAG**<br>Maria Carmen Jica, Ali Satvaty, Suzan Verberne, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.01871) / [PDF](https://arxiv.org/pdf/2610.01871) |
| 2026-10-01 | **False Prophets: On the Security of World Models in Agentic Systems**<br>Erik Imgrund, Anna Wimbauer, Klim Kireev, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.23147) / [PDF](https://arxiv.org/pdf/2607.23147) |
| 2026-10-01 | **The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching**<br>Alessandro Pegoraro, Daryan Merx, Phillip Rieger, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01768) / [PDF](https://arxiv.org/pdf/2610.01768) |
| 2026-10-01 | **CHILLGuard: Towards Fine-Grained Chinese LLM Safety Guardrail with Scalable Data Construction and Model-aware Preference Alignment**<br>Wenbo Yu, Bohua Wang, Hao Fang, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.15396) / [PDF](https://arxiv.org/pdf/2606.15396) |
| 2026-10-01 | **In Vino Veritas and Vulnerabilities: Examining LLM Safety via Drunk Language Inducement**<br>Anudeex Shetty, Aditya Joshi, Salil S. Kanhere | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2601.22169) / [PDF](https://arxiv.org/pdf/2601.22169) |
| 2026-10-01 | **False Floors: LLM Safety Routing Evaluations Break Under Distribution Shift**<br>Amit Singh Bhatti, Vishal Vaddina | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01535) / [PDF](https://arxiv.org/pdf/2610.01535) |
| 2026-10-01 | **VideoSTF: Stress-Testing Output Repetition in Video Large Language Models**<br>Yuxin Cao, Wei Song, Shangzhi Xu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.10639) / [PDF](https://arxiv.org/pdf/2602.10639) |
| 2026-10-01 | **OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents**<br>Taolin Zhang, Jiuheng Wan, Hanyu Wang, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01508) / [PDF](https://arxiv.org/pdf/2610.01508) |
| 2026-10-01 | **Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoor Triggers and Preserves Desired Traits**<br>Kajetan Dymkiewicz, Tim Farrelly, Adam Prada, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.35356) / [PDF](https://arxiv.org/pdf/2609.35356) |
| 2026-10-01 | **High-quality Data Do not Mean Safe! Poisoning LLMs after Data Selection**<br>Kaiyang Li, Jiahao Chen, Yuwen Pu, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.01367) / [PDF](https://arxiv.org/pdf/2610.01367) |
| 2026-10-01 | **Sleeping Secrets: How Fine-Tuning Reawakens Privacy Risks in Language Models**<br>Jianhong Li, Jiahao Chen, Yuwen Pu, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.01365) / [PDF](https://arxiv.org/pdf/2610.01365) |
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
