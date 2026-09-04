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
**1078 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-03**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 236 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 269 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 159 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 264 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 241 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 342 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 130 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 513 |
| [Other LLM Security](papers.md#other-llm-security) | 78 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-03 | **SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center**<br>Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild | Agent &amp; Tool Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.04159) / [PDF](https://arxiv.org/pdf/2609.04159) |
| 2026-09-03 | **Identifying AI Web Scrapers Using Canary Tokens**<br>Steven Seiden, Triss Ren, Caroline Zhang, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2605.13706) / [PDF](https://arxiv.org/pdf/2605.13706) |
| 2026-09-03 | **Representational alignment yields generalizable safety in language models**<br>Lingyu Li, Yan Teng, Yingchun Wang, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.04022) / [PDF](https://arxiv.org/pdf/2609.04022) |
| 2026-09-03 | **Recognition Without Mitigation: Ethical Frameworks in Autonomous Offensive-LLM Agent Research**<br>Andreas Happe, Jürgen Cito | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2506.08693) / [PDF](https://arxiv.org/pdf/2506.08693) |
| 2026-09-03 | **User Perceptions vs. Proxy LLM Judges: Privacy and Helpfulness in LLM Responses to Privacy-Sensitive Scenarios**<br>Xiaoyuan Wu, Roshni Kaushik, Wenkai Li, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2510.20721) / [PDF](https://arxiv.org/pdf/2510.20721) |
| 2026-09-03 | **A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors**<br>Pengxun Li, Litian Zhang, Jianwei Hou, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03884) / [PDF](https://arxiv.org/pdf/2609.03884) |
| 2026-09-03 | **Inferring Hidden User Models from the Behavior of Personalized LLM Agents**<br>Haoyang Li, Yaxin Xiao, Qingqing Ye, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03815) / [PDF](https://arxiv.org/pdf/2609.03815) |
| 2026-09-03 | **IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks**<br>Saikat Mondal, Mamta, Deeksha Varshney, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03781) / [PDF](https://arxiv.org/pdf/2609.03781) |
| 2026-09-03 | **CASCADE: A Component Ablation and Corpus Audit of a Layered Local Defense for MCP-Based Systems**<br>İpek Abasıkeleş Turgut, Edip Gümüş | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2604.17125) / [PDF](https://arxiv.org/pdf/2604.17125) |
| 2026-09-03 | **AlcaTRAz - Anchored Tree-Rule Defense Against Jailbreaks**<br>Jakub Reš, Petr Kaška, Martin Perešíni, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03693) / [PDF](https://arxiv.org/pdf/2609.03693) |
| 2026-09-03 | **Fully Unleashing the Multimodal Attacker: Meta-Adaptive Jailbreaking of Vision-Language Models**<br>Benlei Cui, Shen Pang, Yuke Wang, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2608.27531) / [PDF](https://arxiv.org/pdf/2608.27531) |
| 2026-09-03 | **Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations**<br>Matteo Gioele Collu, Riccardo Conte, Alberto Giaretta, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.28553) / [PDF](https://arxiv.org/pdf/2605.28553) |
| 2026-09-03 | **Sealing the Audit-Runtime Gap for LLM Skills**<br>Tingda Shen, Yebo Feng, Konglin Zhu, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2605.05274) / [PDF](https://arxiv.org/pdf/2605.05274) |
| 2026-09-03 | **AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs**<br>Chua Jin Chou, Sarang Nambiar, Murali Srinivasan, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.01023) / [PDF](https://arxiv.org/pdf/2609.01023) |
| 2026-09-03 | **SpecAlign: Efficient Specification-Grounded Alignment of Large Language Models via Synthetic Data**<br>Wenjie Wang, Yue Huang, Zhengqing Yuan, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2606.16276) / [PDF](https://arxiv.org/pdf/2606.16276) |
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
