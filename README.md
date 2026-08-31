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
**959 papers** across **4 publication years**. Latest arXiv metadata update: **2026-08-28**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 212 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 241 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 142 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 224 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 215 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 316 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 120 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 453 |
| [Other LLM Security](papers.md#other-llm-security) | 68 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-08-28 | **Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration and External Control**<br>Jun Wen Leong | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.28502) / [PDF](https://arxiv.org/pdf/2608.28502) |
| 2026-08-28 | **SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces**<br>Chang Jin, An Wang, Zeming Wei, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.12015) / [PDF](https://arxiv.org/pdf/2605.12015) |
| 2026-08-28 | **LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment**<br>Jingjing Nie, Jiawei Guo, Krishna Meda, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2608.28490) / [PDF](https://arxiv.org/pdf/2608.28490) |
| 2026-08-28 | **ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent**<br>Sriram Selvam, Anneswa Ghosh | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.26403) / [PDF](https://arxiv.org/pdf/2606.26403) |
| 2026-08-28 | **LongPIBench: A Long-Context Benchmark for Prompt Injection**<br>Yupei Liu, Yuqi Jia, Neil Zhenqiang Gong, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.28411) / [PDF](https://arxiv.org/pdf/2608.28411) |
| 2026-08-28 | **When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning**<br>Mingyuan Huang, Zimo Ji, Yifan Mo, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.28400) / [PDF](https://arxiv.org/pdf/2608.28400) |
| 2026-08-28 | **BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence**<br>Changze Li, Yutong Cheng, Tsania Camila Finnisa, et al. | Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.28394) / [PDF](https://arxiv.org/pdf/2608.28394) |
| 2026-08-28 | **CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents**<br>Jaewon Jung, Haizhong Zheng, Hongsun Jang, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.28389) / [PDF](https://arxiv.org/pdf/2608.28389) |
| 2026-08-28 | **Progressive Behavioral Drift through Compression Valleys in Large Language Models**<br>Zhiyuan Xu, Stanislav Abaimov, Joseph Gardiner, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2511.17194) / [PDF](https://arxiv.org/pdf/2511.17194) |
| 2026-08-28 | **Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation**<br>Rujin Liang, Zhongpu Chen, Yuhao Lei, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2608.20756) / [PDF](https://arxiv.org/pdf/2608.20756) |
| 2026-08-28 | **Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers**<br>Abrar Alotaibi, Muhammad Shahid Jabbar, Sadam Al-Azani, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2608.28327) / [PDF](https://arxiv.org/pdf/2608.28327) |
| 2026-08-28 | **Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors**<br>Joshua Penman | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2608.23873) / [PDF](https://arxiv.org/pdf/2608.23873) |
| 2026-08-28 | **TagZilla: Automated Owner and Abuse Type Tagging for Indicators of Compromise in Threat Reports**<br>Gibran Gomez, Juan Caballero | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2608.28124) / [PDF](https://arxiv.org/pdf/2608.28124) |
| 2026-08-28 | **Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents**<br>Chenhao Wu, Haoxuan Jia, Yang Liu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.27141) / [PDF](https://arxiv.org/pdf/2608.27141) |
| 2026-08-28 | **Agentao: A Policy-Governed Runtime Harness for Embeddable Tool-Using LLM Agents**<br>Bo Jin, Qiang Jiao, Xin Tong | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.13574) / [PDF](https://arxiv.org/pdf/2608.13574) |
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
