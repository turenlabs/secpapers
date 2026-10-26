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
**2034 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-23**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 464 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 495 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 317 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 490 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 447 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 603 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 251 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 965 |
| [Other LLM Security](papers.md#other-llm-security) | 133 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-23 | **From One Query to Many: A Critical Survey of Privacy Accounting in RAG**<br>Zhiyuan Zhang | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.21245) / [PDF](https://arxiv.org/pdf/2610.21245) |
| 2026-10-23 | **Trusting the Tool: Asymmetric Deference of LLM Vulnerability Auditors to Static-Analysis Evidence**<br>ZhiHong Liu, Shuyao Gao | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.32876) / [PDF](https://arxiv.org/pdf/2610.32876) |
| 2026-10-23 | **Constitution-Guided Watermarking**<br>Toluwani Aremu, Samuele Poppi, Nils Lukas | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.09552) / [PDF](https://arxiv.org/pdf/2610.09552) |
| 2026-10-23 | **LocalAlign: Enabling Generalizable Prompt Injection Defense via Generation of Near-Target Adversarial Examples for Alignment Training**<br>Yuyang Gong, Zihao Wang, Jiawei Liu, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2605.01462) / [PDF](https://arxiv.org/pdf/2605.01462) |
| 2026-10-23 | **On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection**<br>Yuyang Gong, Zihao Wang, Jiawei Liu, et al. | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.32531) / [PDF](https://arxiv.org/pdf/2610.32531) |
| 2026-10-23 | **Spend Where It Counts: Dynamic Budget Allocation for Multi-Turn LLM Evaluation**<br>Shai Feldman, Yaniv Romano | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.06605) / [PDF](https://arxiv.org/pdf/2605.06605) |
| 2026-10-23 | **Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models**<br>Jinwei Gan, Zifeng Cheng, Zhiwei Jiang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.31331) / [PDF](https://arxiv.org/pdf/2610.31331) |
| 2026-10-23 | **Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models**<br>Yi Wang, Xiuyuan Qi, Dongqi Han, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.10625) / [PDF](https://arxiv.org/pdf/2610.10625) |
| 2026-10-23 | **DeepAVR: Deep Analysis via Multi-Agent Collaboration for Automated Vulnerability Repair**<br>Woorim Han, Hyunjun Kim, Brian Junekyu Lee, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.32345) / [PDF](https://arxiv.org/pdf/2610.32345) |
| 2026-10-23 | **Injection-Execution Dissociation: A Mechanistic Evaluation of Persistent Memory Attacks and Defenses in Stateful LLM Agents**<br>Jun Wen Leong | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.08442) / [PDF](https://arxiv.org/pdf/2605.08442) |
| 2026-10-23 | **Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools**<br>Shenyuan Guan, Qiaodan Hou, Yanjun Chen, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.09181) / [PDF](https://arxiv.org/pdf/2608.09181) |
| 2026-10-23 | **WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents**<br>Yulin Chen, Tri Cao, Haoran Li, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2604.12284) / [PDF](https://arxiv.org/pdf/2604.12284) |
| 2026-10-23 | **Depth-Dependent Safety Geometry in Vision-Language Models: Layer-Wise Localization and Bidirectional Refusal Control**<br>Muhammad Zeeshan Karamat, Syed Talal Hassan, Christiana Chamon Garcia | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.32182) / [PDF](https://arxiv.org/pdf/2610.32182) |
| 2026-10-23 | **Detecting Insecure Compositions of Clean Agent Skills via Capability-Flow Graph Analysis**<br>Yihao Li, Chuanpu Fu, Yizhou Zhao, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.32155) / [PDF](https://arxiv.org/pdf/2610.32155) |
| 2026-10-23 | **AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents**<br>Gejian Zhao, Hanzhou Wu, Xinpeng Zhang | Other LLM Security | [abstract](https://arxiv.org/abs/2610.32092) / [PDF](https://arxiv.org/pdf/2610.32092) |
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
