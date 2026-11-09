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
**2265 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-06**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 525 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 558 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 355 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 525 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 494 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 669 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 274 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1056 |
| [Other LLM Security](papers.md#other-llm-security) | 148 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-06 | **GuardrailAgent: An Agentic Framework for Jailbreak Defense**<br>Tianze Chang, Junjie Chu, Yixin Wu, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.09734) / [PDF](https://arxiv.org/pdf/2611.09734) |
| 2026-11-06 | **MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory**<br>David H. Yang, Blake Bullwinkel, Amanda Minnich, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.09721) / [PDF](https://arxiv.org/pdf/2611.09721) |
| 2026-11-06 | **XekRung Technical Report**<br>Jiutian Zeng, Junjie Li, Chengwei Dai, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.00072) / [PDF](https://arxiv.org/pdf/2605.00072) |
| 2026-11-06 | **Towards the Worst-case Robustness of Large Language Models**<br>Huanran Chen, Zeming Wei, Yao Huang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2501.19040) / [PDF](https://arxiv.org/pdf/2501.19040) |
| 2026-11-06 | **PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization**<br>Murat Bilgehan Ertan, Xiaochen Zhu, Phuong Ha Nguyen, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2605.06505) / [PDF](https://arxiv.org/pdf/2605.06505) |
| 2026-11-06 | **Analyzing Code Provenance in LLMs for Programming Education**<br>Subhankar Maity, Faiza Belbachir, Omar Boucelma, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.09177) / [PDF](https://arxiv.org/pdf/2611.09177) |
| 2026-11-06 | **Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use**<br>Chuxue Cao, Jingru Zeng, Boqin Yin, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.09113) / [PDF](https://arxiv.org/pdf/2611.09113) |
| 2026-11-06 | **Beyond a Single Commit: Anchor-Guided Reconstruction of Multi-Commit Patches**<br>Jialiang Dong, Willy Susilo, Xu Gai, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.09026) / [PDF](https://arxiv.org/pdf/2611.09026) |
| 2026-11-06 | **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs**<br>Md Tanvirul Alam, Aritran Piplai, Ionut Cardei, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2602.00513) / [PDF](https://arxiv.org/pdf/2602.00513) |
| 2026-11-06 | **Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks**<br>Mark Heimann, Katherine Taylor, Bruno Jacob | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.08834) / [PDF](https://arxiv.org/pdf/2611.08834) |
| 2026-11-05 | **SCDBench: A Benchmark for LLM-Based Smart Contract Decompilers**<br>Kaihua Qin, Dawn Song, Arthur Gervais | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.29059) / [PDF](https://arxiv.org/pdf/2605.29059) |
| 2026-11-05 | **Exposing the Illusion of Erasure in Knowledge Editing for LLMs**<br>Advik Raj Basani, Anshuman Chhabra | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.23276) / [PDF](https://arxiv.org/pdf/2606.23276) |
| 2026-11-05 | **Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents**<br>Behzad Ousat, Nikita Turkmen, Lalchandra Rampersaud, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2607.18659) / [PDF](https://arxiv.org/pdf/2607.18659) |
| 2026-11-05 | **Conflux: Preventing Privilege Escalation with Principal Contexts and System-Level Evaluation**<br>Raya Buckley, Christian Schroeder de Witt | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.08768) / [PDF](https://arxiv.org/pdf/2611.08768) |
| 2026-11-05 | **Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate**<br>Liting Huang, Huizhi Liang, Yi Lei, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.08756) / [PDF](https://arxiv.org/pdf/2611.08756) |
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
