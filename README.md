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
**1538 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-30**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 348 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 384 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 239 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 361 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 333 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 477 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 189 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 734 |
| [Other LLM Security](papers.md#other-llm-security) | 102 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-30 | **Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Five Production LLMs**<br>Haochuan Kevin Wang, Zechen Zhang | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2603.28013) / [PDF](https://arxiv.org/pdf/2603.28013) |
| 2026-09-30 | **Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery**<br>Kaikai Zhang, Zihan Zhang, Yuchong Xie, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35909) / [PDF](https://arxiv.org/pdf/2609.35909) |
| 2026-09-30 | **CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion**<br>Zhen Liang, Hai Huang, Wentao Chen | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.39902) / [PDF](https://arxiv.org/pdf/2609.39902) |
| 2026-09-30 | **BadEngram: Backdoor Attack on Gated Memory Components in LLMs**<br>Ariel Fogel, Omer Hofman, Eilon Cohen, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.13478) / [PDF](https://arxiv.org/pdf/2609.13478) |
| 2026-09-30 | **The Verifiable Action Card: Trustworthy Human-in-the-Loop Control for Secure Autonomous Agents**<br>Hasnain Irshad, Anam Mughees, Neelam Mughees, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.18411) / [PDF](https://arxiv.org/pdf/2609.18411) |
| 2026-09-30 | **COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs**<br>Yi Song, Dongchen Xie, Xiaoyuan Xie, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.39783) / [PDF](https://arxiv.org/pdf/2609.39783) |
| 2026-09-30 | **AgentSnare: Learning to Delay, Divert, and Defuse Autonomous Penetration Agents**<br>Ruoyu Wang, Heng Zhao, Renjie Wu, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2607.26998) / [PDF](https://arxiv.org/pdf/2607.26998) |
| 2026-09-30 | **Using Fine-Tuned LLMs to Identify Indicators of Vulnerability in UK Police Incident Logs**<br>Sam Relins, Daniel Birks | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2607.18446) / [PDF](https://arxiv.org/pdf/2607.18446) |
| 2026-09-30 | **Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs**<br>Yifei Wang, Yida Yang, Tianlin Li, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.20641) / [PDF](https://arxiv.org/pdf/2605.20641) |
| 2026-09-30 | **Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks**<br>Zezhong Wang, Xueyang Tang, Rui Lian, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.39549) / [PDF](https://arxiv.org/pdf/2609.39549) |
| 2026-09-30 | **The Surface You Test Is Not the Surface That Breaks**<br>Syed Nazmus Sakib, Nafiul Haque, Shahrear Bin Amin, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.30454) / [PDF](https://arxiv.org/pdf/2605.30454) |
| 2026-09-30 | **ActionGuard: Tool Call Authorization under Poisoned Skills**<br>Jihun Han, Yejin Jang, Byung Il Kwak, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.39450) / [PDF](https://arxiv.org/pdf/2609.39450) |
| 2026-09-30 | **SEW: Style-Encoded Watermarking of LLM-Generated Code**<br>Soohan Lim, Hyundong Jin, Yo-Sub Han | Other LLM Security | [abstract](https://arxiv.org/abs/2609.39414) / [PDF](https://arxiv.org/pdf/2609.39414) |
| 2026-09-30 | **ACTR: Aligning Thoughts and Responses for Multilingual Safety in Reasoning LLMs**<br>Xianhui Zhang, Jian Yu, Chengyu Xie, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.37054) / [PDF](https://arxiv.org/pdf/2609.37054) |
| 2026-09-30 | **Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents**<br>Wenxin Wu, Lingyong Yan, Lei Sha, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.39352) / [PDF](https://arxiv.org/pdf/2609.39352) |
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
