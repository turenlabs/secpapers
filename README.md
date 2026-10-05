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
**1599 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-02**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 362 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 401 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 249 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 378 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 350 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 493 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 197 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 769 |
| [Other LLM Security](papers.md#other-llm-security) | 102 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-02 | **Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks**<br>Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03585) / [PDF](https://arxiv.org/pdf/2610.03585) |
| 2026-10-02 | **PrivDev: Mapping Static-Analysis Data Types to DPV**<br>Simon Bernbeck, Ricardo Ramalho, Matheus Amendoeira, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03518) / [PDF](https://arxiv.org/pdf/2610.03518) |
| 2026-10-02 | **Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents**<br>Zhuowen Liu | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03448) / [PDF](https://arxiv.org/pdf/2610.03448) |
| 2026-10-02 | **Understanding Gaps in LLM Pipelines Towards Scalable Fuzzing Harness Generation: An Empirical Study and Enhancement**<br>Kang Yang, Yunhang Zhang, Zichuan Li, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2512.03420) / [PDF](https://arxiv.org/pdf/2512.03420) |
| 2026-10-02 | **Persona Guardrail: A Production-Grade Defense Framework for Agentic Systems**<br>Bijeeta Pal, Sridhar Reddy Maddireddy, Muhaimin Bin Munir, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03434) / [PDF](https://arxiv.org/pdf/2610.03434) |
| 2026-10-02 | **Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis**<br>Jugal Gajjar | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2604.10800) / [PDF](https://arxiv.org/pdf/2604.10800) |
| 2026-10-02 | **CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models**<br>Lin Cui, Vincenzo Scotti, Raffaela Mirandola | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03383) / [PDF](https://arxiv.org/pdf/2610.03383) |
| 2026-10-02 | **Defense-in-Depth at the Perception-Reasoning Interface of LLM-Centric Agentic UAV Swarms**<br>Mohammadhossein Homaei, Yousef Emami, Sajad Homayoun, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.03319) / [PDF](https://arxiv.org/pdf/2610.03319) |
| 2026-10-02 | **EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents**<br>Shiyi Kuang, Xuemei Luo, Kun Liu, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03153) / [PDF](https://arxiv.org/pdf/2610.03153) |
| 2026-10-02 | **The Fragility of Trigger-Tag Mechanisms for Misuse Detection in Open-Weight LLMs**<br>Toluwani Aremu, Manit Baser, Mohan Gurusamy, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03124) / [PDF](https://arxiv.org/pdf/2610.03124) |
| 2026-10-02 | **Suan: Rectifying Direct Preference Safety Alignment in Large Language Models**<br>Oleksandr Cherednichenko, Roman Klypa | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.08634) / [PDF](https://arxiv.org/pdf/2609.08634) |
| 2026-10-02 | **LS-AR: Future-Predictive Latent Steering in Autoregressive LLMs**<br>Anubha Gupta, Eduardo Pignatelli | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.03093) / [PDF](https://arxiv.org/pdf/2610.03093) |
| 2026-10-02 | **Transforming Keystroke Noise to Text: Self-Supervised Acoustic Eavesdropping Attacks on Keyboards**<br>Atsunori Okada, Akira Ito, Rei Ueno, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2607.22094) / [PDF](https://arxiv.org/pdf/2607.22094) |
| 2026-10-02 | **Securing Computer-Use Agents Against Branch Steering Attacks**<br>Giulio Zingrillo, Hanna Foerster, Ilia Shumailov, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.03089) / [PDF](https://arxiv.org/pdf/2610.03089) |
| 2026-10-02 | **Beyond Predefined Sinks: Security-Aware Dependency Analysis for LLM Agents**<br>Hang Cui | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.03014) / [PDF](https://arxiv.org/pdf/2610.03014) |
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
