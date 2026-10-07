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
**1691 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-06**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 386 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 422 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 257 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 404 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 378 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 521 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 210 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 812 |
| [Other LLM Security](papers.md#other-llm-security) | 105 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-06 | **BARE-AI: Bit-Flip Attack Resilience in AI Hardware through Built-in Performance Monitors**<br>Habibur Rahaman, Swastik Bhattacharya, Sanjay Das, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.08739) / [PDF](https://arxiv.org/pdf/2610.08739) |
| 2026-10-06 | **Secure Speculative Decoding for Large Language Models**<br>Yichi Zhang, Zhiqi Wang, Neil Gong, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.08678) / [PDF](https://arxiv.org/pdf/2610.08678) |
| 2026-10-06 | **Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers**<br>Thiago Sandoval, Ufuk Topcu | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.14089) / [PDF](https://arxiv.org/pdf/2608.14089) |
| 2026-10-06 | **Case-Level Verification in Scanner-LLM Cascades: Overcoming the Alert Aggregation Bottleneck to Expand the FRR-TPR Trade-off Space**<br>Hao Sun, Yibin Yao, Chaohai Xie, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.08406) / [PDF](https://arxiv.org/pdf/2610.08406) |
| 2026-10-06 | **Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis**<br>Mandana Ghadamian, David Mohaisen | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.08405) / [PDF](https://arxiv.org/pdf/2610.08405) |
| 2026-10-06 | **Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution under Analysis Budgets**<br>Mubashar Iqbal, Asifullah Khan, Hifsa Asif, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.04820) / [PDF](https://arxiv.org/pdf/2609.04820) |
| 2026-10-06 | **Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box Vision Language Models for Autonomous Driving**<br>Heyam Bin Jahlan Areej Alhothali Abeer Alhothali | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.08331) / [PDF](https://arxiv.org/pdf/2610.08331) |
| 2026-10-06 | **Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code**<br>Thiago Santos de Moura, Fynn Matuschek, Flavio Toffalini, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2610.08240) / [PDF](https://arxiv.org/pdf/2610.08240) |
| 2026-10-06 | **SpliTEE: Fast and Private LLM Inference by Coupling GPU-Assisted Trusted Execution Environments with Differential Privacy**<br>Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.15039) / [PDF](https://arxiv.org/pdf/2609.15039) |
| 2026-10-06 | **Surviving the Router: Optimizing Skill Injections for Retrieval and Execution**<br>Haneen Najjar, Luca Scionis, Haritz Puerto, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.08098) / [PDF](https://arxiv.org/pdf/2610.08098) |
| 2026-10-06 | **CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection**<br>Sungju Yun, Sijune Hwang, Yeonjoon Lee, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2608.03134) / [PDF](https://arxiv.org/pdf/2608.03134) |
| 2026-10-06 | **ASCENT: First-Order Optimal Fine-Tuning with Recalibration for Safety--Utility Co-Enhancement**<br>Weiwei Qi, Chongyu Wang, Tianhang Zheng, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.08061) / [PDF](https://arxiv.org/pdf/2610.08061) |
| 2026-10-06 | **SIGMA: Self-Improving Alignment Generalization from a Model Spec**<br>Jingyu Zhang, Shruti Palaskar, Daniel Khashabi, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.07935) / [PDF](https://arxiv.org/pdf/2610.07935) |
| 2026-10-06 | **MiniScope: Authorizing Agents with Least-Privilege Permissions**<br>Jinhao Zhu, Xiao Huang, Kevin Tseng, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.11147) / [PDF](https://arxiv.org/pdf/2512.11147) |
| 2026-10-06 | **Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study**<br>Georgios Koutidis, Nikolaos Kekatos, Marina Korgiala-Karyda, et al. | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.07873) / [PDF](https://arxiv.org/pdf/2610.07873) |
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
