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
**1258 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-15**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 269 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 313 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 195 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 295 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 277 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 404 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 157 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 595 |
| [Other LLM Security](papers.md#other-llm-security) | 88 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-15 | **CoER: Defending against Adaptive Indirect Prompt Injection via Adversarial Co-Evolution and Refinement**<br>Boyang Zhang, Qingxin Xiao, Lingwei Dang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.07529) / [PDF](https://arxiv.org/pdf/2609.07529) |
| 2026-09-15 | **Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection**<br>Xueying Zeng, Youquan Xian, Yanze Li, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2608.27994) / [PDF](https://arxiv.org/pdf/2608.27994) |
| 2026-09-15 | **Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models**<br>Xinyue Liu, Niloofar Mireshghallah, Jane C. Ginsburg, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2603.20957) / [PDF](https://arxiv.org/pdf/2603.20957) |
| 2026-09-15 | **Plug 'n' Pray: Agentic LLM-based Detection of Potential Log File Exposures in Third-Party Content Management System Plugins**<br>Sebastian Neef | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.17164) / [PDF](https://arxiv.org/pdf/2609.17164) |
| 2026-09-15 | **ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation**<br>Jiangrui Yu, Baosheng Zhang, Liang Kong, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.16915) / [PDF](https://arxiv.org/pdf/2609.16915) |
| 2026-09-15 | **InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation**<br>Jiachang Zhang, Min Chen, Xiao Ren, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.16818) / [PDF](https://arxiv.org/pdf/2609.16818) |
| 2026-09-15 | **Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion**<br>Zhuoang Cai | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.16777) / [PDF](https://arxiv.org/pdf/2609.16777) |
| 2026-09-15 | **Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives**<br>Rahul Dev T Y, Hiran V Nath | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.16694) / [PDF](https://arxiv.org/pdf/2609.16694) |
| 2026-09-15 | **MarkSec: Capability-Aware Evaluation of Adversarial Attacks Against LLM Watermarks**<br>Kairong Li, Zhikun Zhang, Xiao Ren, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.16681) / [PDF](https://arxiv.org/pdf/2609.16681) |
| 2026-09-14 | **Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification**<br>Md Nazmul Hoque, Shaswata Mitra, Subash Neupane, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.16433) / [PDF](https://arxiv.org/pdf/2609.16433) |
| 2026-09-14 | **Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model**<br>Hyojung Han | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.11291) / [PDF](https://arxiv.org/pdf/2609.11291) |
| 2026-09-14 | **Understanding the (In)Security of Vibe-Coded Applications**<br>Junquan Deng, Zhiyu Fan, Ruijie Meng | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.23130) / [PDF](https://arxiv.org/pdf/2606.23130) |
| 2026-09-14 | **Toward Governance-Aware Autonomous GIS: A Narrative Review of Ethical and Privacy Risks in LLM-Enabled GeoAI**<br>Maya Subramanian, Devika Jain | Agent &amp; Tool Security, Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.16232) / [PDF](https://arxiv.org/pdf/2609.16232) |
| 2026-09-14 | **RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic**<br>Mughees Ur Rehman, Aritran Piplai, Murat Kantarcioglu | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.16231) / [PDF](https://arxiv.org/pdf/2609.16231) |
| 2026-09-14 | **Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration**<br>Aashiq Muhamed, Mona T. Diab, Virginia Smith | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.16204) / [PDF](https://arxiv.org/pdf/2609.16204) |
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
