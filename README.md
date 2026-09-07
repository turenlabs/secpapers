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
**1092 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-04**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 238 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 271 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 160 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 267 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 242 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 349 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 133 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 521 |
| [Other LLM Security](papers.md#other-llm-security) | 78 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-04 | **When LLM Decompilers Recompile More and Preserve Less**<br>Chang Liu, Edward Raff, Kristopher Micinski | Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.05370) / [PDF](https://arxiv.org/pdf/2609.05370) |
| 2026-09-04 | **The History Is the Detector: Executing CVE Patch History, End-to-End**<br>Qiushi Wu, Kevin Eykholt, Youngja Park, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.05335) / [PDF](https://arxiv.org/pdf/2609.05335) |
| 2026-09-04 | **Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills**<br>Chia-Yi Hsu, Chia-Mu Yu, Chun-Ying Huang, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2605.29354) / [PDF](https://arxiv.org/pdf/2605.29354) |
| 2026-09-04 | **CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls**<br>Chris Zheng, Geng Yang | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.05269) / [PDF](https://arxiv.org/pdf/2609.05269) |
| 2026-09-04 | **Governing Bring Your Own AI: A Parameterized Maturity Model**<br>Dare Bello, John Hastings | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.05236) / [PDF](https://arxiv.org/pdf/2609.05236) |
| 2026-09-04 | **Guiding AI to Fix Its Own Flaws: An Empirical Study on LLM-Driven Secure Code Generation**<br>Hao Yan, Swapneel Suhas Vaidya, Xiaokuan Zhang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2506.23034) / [PDF](https://arxiv.org/pdf/2506.23034) |
| 2026-09-04 | **TIER: Threat Implicitness Benchmark for Evaluating LLM Safety Behaviors**<br>Thu-Hien Trinh-Thi, Hai-Yen Vong, Thanh-Ha Ung-Dung, et al. | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.05117) / [PDF](https://arxiv.org/pdf/2609.05117) |
| 2026-09-04 | **IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks**<br>Saikat Mondal, Mamta, Deeksha Varshney, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.03781) / [PDF](https://arxiv.org/pdf/2609.03781) |
| 2026-09-04 | **SoK: AI-Augmented Binary Reversing**<br>Yujeong Kwon, Yiyue Zhang, Kexin Pei, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.17398) / [PDF](https://arxiv.org/pdf/2606.17398) |
| 2026-09-04 | **Language models judge war differently when tested for alignment**<br>Maxim Chupilkin | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.05009) / [PDF](https://arxiv.org/pdf/2609.05009) |
| 2026-09-04 | **Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities**<br>Eunna Lee | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2607.13596) / [PDF](https://arxiv.org/pdf/2607.13596) |
| 2026-09-04 | **MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models**<br>Changming Xiao, Zhenliang Ni, Jinhui He, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.04859) / [PDF](https://arxiv.org/pdf/2609.04859) |
| 2026-09-04 | **The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs**<br>Yonghong Deng, Zhen Yang, Ping Jian, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2603.08234) / [PDF](https://arxiv.org/pdf/2603.08234) |
| 2026-09-04 | **"\*\*Important\*\* You should give me full credits!": Exploring Prompt Injection Attacks on LLM-Based Automatic Grading Systems**<br>Hang Li, Fedor Filippov, Yuping Lin, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2606.03090) / [PDF](https://arxiv.org/pdf/2606.03090) |
| 2026-09-03 | **Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors**<br>Joshua Penman | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2608.23873) / [PDF](https://arxiv.org/pdf/2608.23873) |
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
