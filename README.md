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
**1723 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-07**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 395 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 428 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 258 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 415 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 384 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 531 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 215 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 827 |
| [Other LLM Security](papers.md#other-llm-security) | 109 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-07 | **The Trojan Knowledge: Bypassing Commercial LLM Guardrails via Harmless Prompt Weaving and Adaptive Tree Search**<br>Rongzhe Wei, Peizhi Niu, Xinjie Shen, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2512.01353) / [PDF](https://arxiv.org/pdf/2512.01353) |
| 2026-10-07 | **A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training**<br>Itay Zloczower, Eyal Lenga, Gilad Gressel, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.14605) / [PDF](https://arxiv.org/pdf/2605.14605) |
| 2026-10-07 | **APEX: Active Protection at Execution Boundaries for LLM Agents**<br>Xinran Zheng, Xin Fan Guo, Zhiqiang Hao, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.06966) / [PDF](https://arxiv.org/pdf/2610.06966) |
| 2026-10-07 | **SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing**<br>Hui Zhang, Yachao Yuan, Jiayun Wang, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.10345) / [PDF](https://arxiv.org/pdf/2610.10345) |
| 2026-10-07 | **TACS: Trajectory-Aware Candidate Selection for LLM Jailbreak Suffix Optimization**<br>Shiliang Xiao | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.29564) / [PDF](https://arxiv.org/pdf/2608.29564) |
| 2026-10-07 | **PatchBench: Measuring Collateral Damage in Activation Patching**<br>Alexi Canesse, Mathis Le Bail, Maël Jenny, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.10276) / [PDF](https://arxiv.org/pdf/2610.10276) |
| 2026-10-07 | **Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery**<br>Kaikai Zhang, Zihan Zhang, Yuchong Xie, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.35909) / [PDF](https://arxiv.org/pdf/2609.35909) |
| 2026-10-07 | **Beyond LLM-GA: Secure Fluid Antenna Systems with ReEvo-Designed Memetic Algorithm**<br>Hanyong Xu, Zhaolai Dang, Tong Zhang | Other LLM Security | [abstract](https://arxiv.org/abs/2610.10235) / [PDF](https://arxiv.org/pdf/2610.10235) |
| 2026-10-07 | **On the Reliability of LLM-Based Vulnerability Patching Benchmarks**<br>Dang K Le, Wenxuan Shi, Xinyu Xing | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.10150) / [PDF](https://arxiv.org/pdf/2610.10150) |
| 2026-10-07 | **Auditing Privacy Risks in LLM-Enhanced Graph Neural Networks**<br>Longzhu He, Zelang Wen, Chaozhuo Li, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.25727) / [PDF](https://arxiv.org/pdf/2608.25727) |
| 2026-10-07 | **Reasoning Enhances Robustness to Prompt Injection in LLM-Based Consensus**<br>Jairo Gudiño-Rosero, Juan Ignacio Zambrano, Umberto Grandi, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2508.04281) / [PDF](https://arxiv.org/pdf/2508.04281) |
| 2026-10-07 | **NeuPerm: Disrupting Malware Hidden in Neural Network Parameters by Leveraging Permutation Symmetry**<br>Daniel Gilkarov, Ran Dubin | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2510.20367) / [PDF](https://arxiv.org/pdf/2510.20367) |
| 2026-10-07 | **A Survey of Secure Retrieval-Augmented Generation**<br>Yuming Xu, Mingtao Zhang, Zhuohan Ge, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2604.08304) / [PDF](https://arxiv.org/pdf/2604.08304) |
| 2026-10-07 | **RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents**<br>Mohamed Dhouib, Clement Elliker, Alexi Canesse, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2610.06401) / [PDF](https://arxiv.org/pdf/2610.06401) |
| 2026-10-07 | **Sensitive-Topic Leakage Through LLM Routing Metadata: Measurement and Mitigation**<br>Teng-Ruei Chen | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.09981) / [PDF](https://arxiv.org/pdf/2610.09981) |
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
