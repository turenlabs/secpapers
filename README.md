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
**2520 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-24**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 588 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 608 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 401 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 589 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 550 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 734 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 302 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1161 |
| [Other LLM Security](papers.md#other-llm-security) | 162 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-24 | **Where Did My Tokens Go? Verifiable Token Billing for LLM Services**<br>Jiayuan Du, Yebo Feng, Lin Zhang, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2611.31806) / [PDF](https://arxiv.org/pdf/2611.31806) |
| 2026-11-24 | **SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?**<br>Asma Farajidizaji, Vyas Raina, Vatsal Raina, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.31791) / [PDF](https://arxiv.org/pdf/2611.31791) |
| 2026-11-24 | **Separating Measurement Failures from Defence Failures in Split Language-Model Privacy**<br>Georgios Politis, Evangelos Pappas | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.31752) / [PDF](https://arxiv.org/pdf/2611.31752) |
| 2026-11-24 | **Mixed-Initiative Mining of Root-Cause Analyses into Audit Priors for C/C++ Vulnerability Hunting**<br>Yuhei Kawakoya, Eitaro Shioji, Yuto Otsuki, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.31744) / [PDF](https://arxiv.org/pdf/2611.31744) |
| 2026-11-23 | **Fail-Closed Alignment for Large Language Models**<br>Zachary Coalson, Sanghyun Hong | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2602.16977) / [PDF](https://arxiv.org/pdf/2602.16977) |
| 2026-11-23 | **Evaluating LLM Security Review Agents with Operationally Sourced Ground Truth**<br>Mudita Khurana, Karim Liman-Tinguiri | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.31606) / [PDF](https://arxiv.org/pdf/2611.31606) |
| 2026-11-23 | **Frequency-Conditioned Privacy Auditing of Fine-Tuned Language Models**<br>Aymen Noor, Ke Lyu, Honglu Jiang | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.31581) / [PDF](https://arxiv.org/pdf/2611.31581) |
| 2026-11-23 | **Aftershock: Yesterday's Linux Kernel Bugs, Tomorrow's Android Exploits**<br>Kareem Shehada, Zhiyun Qian | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.31547) / [PDF](https://arxiv.org/pdf/2611.31547) |
| 2026-11-23 | **ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection**<br>Yi Han, Zhen Sun, Zhijie Deng, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.31424) / [PDF](https://arxiv.org/pdf/2611.31424) |
| 2026-11-23 | **MASCing: Configurable Mixture-of-Experts Behavior via Activation Steering Masks**<br>Jona te Lintelo, Lichao Wu, Marina Krček, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2604.27818) / [PDF](https://arxiv.org/pdf/2604.27818) |
| 2026-11-23 | **FATCAT: Fault Injection Attacks Targeting Chip-level Alignment**<br>Peter Horvath, Ilia Shumailov, Zhuoran Liu, et al. | Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.31129) / [PDF](https://arxiv.org/pdf/2611.31129) |
| 2026-11-23 | **Maverick: Private and Verifiable LLM Inference Made Practical via Matrix-Vector Multiplication Delegation**<br>Ben Merbaum, Mohammad Amin Raeisi, Wenhao Wang, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.10264) / [PDF](https://arxiv.org/pdf/2609.10264) |
| 2026-11-23 | **Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills**<br>Kaixuan Li, Wenbo Guo, Sen Chen, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.30932) / [PDF](https://arxiv.org/pdf/2611.30932) |
| 2026-11-23 | **On-policy distillation as a Backdoor Propagation Channel**<br>Zane Fu, Yanzhao Zheng, Ziting Qin, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.19207) / [PDF](https://arxiv.org/pdf/2611.19207) |
| 2026-11-23 | **As Student Rollouts Continue, Visual Backdoors Keep Growing**<br>Zane Fu, Yanzhao Zheng, Jinze Liu, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.22446) / [PDF](https://arxiv.org/pdf/2611.22446) |
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
