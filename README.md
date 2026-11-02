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
**2151 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-30**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 491 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 529 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 336 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 505 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 471 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 640 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 260 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1017 |
| [Other LLM Security](papers.md#other-llm-security) | 140 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-30 | **The Envelope Layer: An Underestimated Surface of LLM Agent Defense**<br>Yuelin Han | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.37415) / [PDF](https://arxiv.org/pdf/2610.37415) |
| 2026-10-30 | **Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products**<br>Tina Rezaei, Suzan Bayhan, Andrea Continella, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.42032) / [PDF](https://arxiv.org/pdf/2610.42032) |
| 2026-10-30 | **SecPO: Principled Adversarial Training for Prompt Injection Security**<br>Sizhe Chen, Yibo Peng, Jaewon Chang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.41998) / [PDF](https://arxiv.org/pdf/2610.41998) |
| 2026-10-30 | **How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces**<br>Donghang Duan, Qingyu Liu, Yifei Liu, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41885) / [PDF](https://arxiv.org/pdf/2610.41885) |
| 2026-10-30 | **What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer**<br>Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41803) / [PDF](https://arxiv.org/pdf/2610.41803) |
| 2026-10-30 | **From Training Exposure to Membership Evidence: A Controlled Study of OLMo 2**<br>Ali Banaei, Muhammad Shahab Shahzad, Gerald Q. Maguire, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41732) / [PDF](https://arxiv.org/pdf/2610.41732) |
| 2026-10-30 | **Simple Features Beat Most AI Control Monitors**<br>Shubhrangshu Debsarkar, Valmik Nahata | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41713) / [PDF](https://arxiv.org/pdf/2610.41713) |
| 2026-10-30 | **Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization**<br>Hangyi Zhao, Bonan Zhang, Fusen Guo, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.34829) / [PDF](https://arxiv.org/pdf/2610.34829) |
| 2026-10-30 | **A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle**<br>Zehao Lin, Xixuan Hao, Renyu Fu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2604.16548) / [PDF](https://arxiv.org/pdf/2604.16548) |
| 2026-10-30 | **When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing**<br>Yixiang Luo, Ziheng Ma, Ke Chang, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41401) / [PDF](https://arxiv.org/pdf/2610.41401) |
| 2026-10-30 | **Enhancing Safety of Large Language Models via Embedding Space Separation**<br>Xu Zhao, Xiting Wang, Weiran Shen | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2603.20206) / [PDF](https://arxiv.org/pdf/2603.20206) |
| 2026-10-30 | **ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents**<br>Yini Huang, Aiwen LU, Zhen Sun, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41272) / [PDF](https://arxiv.org/pdf/2610.41272) |
| 2026-10-30 | **Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs**<br>Yen-Shan Chen, Zhi Rui Tam, Cheng-Kuang Wu, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.01600) / [PDF](https://arxiv.org/pdf/2602.01600) |
| 2026-10-30 | **When AI Investigators Cannot Trust Their Tools: Conflict-Aware Evidence Verification for Cyber Threat Investigation**<br>Yuchen Zhang | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41191) / [PDF](https://arxiv.org/pdf/2610.41191) |
| 2026-10-30 | **AgentShield: Fortifying Web Applications Against AI Agents and Agentic Browsers**<br>Moiz Ali, Nafis Karim, Rownak Islam, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.41181) / [PDF](https://arxiv.org/pdf/2610.41181) |
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
