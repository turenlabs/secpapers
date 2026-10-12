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
**1764 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-09**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 401 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 437 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 262 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 427 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 391 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 539 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 218 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 849 |
| [Other LLM Security](papers.md#other-llm-security) | 115 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-09 | **X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems**<br>Yeonsung Jung, Zhiyuan Wang, Zifan Wang, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.13886) / [PDF](https://arxiv.org/pdf/2610.13886) |
| 2026-10-09 | **LLMail-Inject: A Dataset from a Realistic Adaptive Prompt Injection Challenge**<br>Sahar Abdelnabi, Aideen Fay, Ahmed Salem, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2506.09956) / [PDF](https://arxiv.org/pdf/2506.09956) |
| 2026-10-09 | **ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary**<br>Md Nazmul Islam Ananto, Pierre Prevost-Avenel, Colin Smith, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.13651) / [PDF](https://arxiv.org/pdf/2610.13651) |
| 2026-10-09 | **EviRepair: Evidence-Driven Agents for Reliable Vulnerability Repair**<br>Yilian Shi, Qingyu Liu, Tianyi Zhou, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.13491) / [PDF](https://arxiv.org/pdf/2610.13491) |
| 2026-10-09 | **Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents**<br>Lei Liu, Yunji Liang, Xiaowen Zhang, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.13267) / [PDF](https://arxiv.org/pdf/2610.13267) |
| 2026-10-09 | **AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation**<br>Changyi Li, Pengfei Lu, Xudong Pan, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2603.07427) / [PDF](https://arxiv.org/pdf/2603.07427) |
| 2026-10-09 | **Understanding Verification Vulnerabilities in Cross-chain Bridges: An Empirical Study**<br>Yuying Wang, Yi Guo, Jiachi Chen, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.13170) / [PDF](https://arxiv.org/pdf/2610.13170) |
| 2026-10-09 | **LLM4Trust: Exploring the Capabilities of Large Language Models for Trust Evaluation**<br>Jie Wang, Yanbo Sun, Zheng Yan, et al. | Adversarial ML, Poisoning &amp; Backdoors, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.33521) / [PDF](https://arxiv.org/pdf/2609.33521) |
| 2026-10-09 | **The Alignment Veto: How Safety Training Suppresses Cultural Knowledge in LLMs**<br>Pardis Sadat Zahraei, Gokhan Tur, Dilek Hakkani-Tür, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2510.13154) / [PDF](https://arxiv.org/pdf/2510.13154) |
| 2026-10-08 | **VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails**<br>Duy Nguyen, Lesly Miculicich, Bhavana Dalvi Mishra, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.12813) / [PDF](https://arxiv.org/pdf/2610.12813) |
| 2026-10-08 | **DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models**<br>Drew Rein, Patrick Oathout, Vishal Kumar, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.12758) / [PDF](https://arxiv.org/pdf/2610.12758) |
| 2026-10-08 | **Byzantine-Resilient Federated Large Language Model via Hypergraph Message Passing**<br>Kai Li, Hanlin Cai, Zihao Liu, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.12711) / [PDF](https://arxiv.org/pdf/2610.12711) |
| 2026-10-08 | **First-Order In-Context Shapley: Scalable Data Auditing for LLM Alignment and Evaluation**<br>Yunting Song, Matthew Watson, Moustafa Farid Alzantot, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.22766) / [PDF](https://arxiv.org/pdf/2607.22766) |
| 2026-10-08 | **Cancerous Backdoor Attack: Gradual Activation via Invisible Tokens and A Stage Controller**<br>Tahmid Imtiaz Imu, Emama Nahid, Prodipta Sen Amartya, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.12644) / [PDF](https://arxiv.org/pdf/2610.12644) |
| 2026-10-08 | **ERIS: Enhancing the Privacy-Utility-Scalability Trade-Off in Federated Learning via Federated Shard Aggregation**<br>Dario Fenoglio, Pasquale Polverino, Akash Dhasade, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2602.08617) / [PDF](https://arxiv.org/pdf/2602.08617) |
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
