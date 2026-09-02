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
**1037 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-01**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 230 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 257 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 152 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 253 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 234 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 330 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 127 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 496 |
| [Other LLM Security](papers.md#other-llm-security) | 72 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-01 | **SILK: Closing the Time-of-Check-to-Time-of-Use Gap in RoT-Protected AI Systems**<br>Ruichen Qi, Xinting Jiang, Ema Dimitrova, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2608.26402) / [PDF](https://arxiv.org/pdf/2608.26402) |
| 2026-09-01 | **When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning**<br>Yitong Guo, Xiaoyi Chen, Siyuan Zhang, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.01455) / [PDF](https://arxiv.org/pdf/2609.01455) |
| 2026-09-01 | **VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models**<br>Zhiqi Huang, Vivek Datla, Zhichao Xu, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.01325) / [PDF](https://arxiv.org/pdf/2609.01325) |
| 2026-09-01 | **Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges**<br>Rui Yang, Shuang Huang, Junhua Liu, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.01210) / [PDF](https://arxiv.org/pdf/2609.01210) |
| 2026-09-01 | **Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion**<br>Phong Trinh Duy, Trang Dang Yen, Hung Nguyen-Huu, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.01187) / [PDF](https://arxiv.org/pdf/2609.01187) |
| 2026-09-01 | **Reveree: Diagnosing LLM Reverse-Engineering Agents**<br>Hadjer Benkraouda, Hongyu Cai, Berkay Celik, et al. | Privacy &amp; Data Leakage, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.01185) / [PDF](https://arxiv.org/pdf/2609.01185) |
| 2026-09-01 | **A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing**<br>Saastha Vasan, Hadjer Benkraouda, Jizhou Chen, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.01174) / [PDF](https://arxiv.org/pdf/2609.01174) |
| 2026-09-01 | **CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild**<br>Jian Yang, Haau-Sing Li, Shawn Guo, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2608.23181) / [PDF](https://arxiv.org/pdf/2608.23181) |
| 2026-09-01 | **GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods**<br>Ruixuan Huang, Xunguang Wang, Zongjie Li, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2502.16903) / [PDF](https://arxiv.org/pdf/2502.16903) |
| 2026-09-01 | **Hidden State Poisoning Attacks against Mamba-based Language Models**<br>Alexandre Le Mercier, Chris Develder, Thomas Demeester | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2601.01972) / [PDF](https://arxiv.org/pdf/2601.01972) |
| 2026-09-01 | **HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation**<br>Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.01046) / [PDF](https://arxiv.org/pdf/2609.01046) |
| 2026-09-01 | **Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning**<br>Michele Armillotta, Nicolò Romandini, Rebecca Montanari, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2607.01138) / [PDF](https://arxiv.org/pdf/2607.01138) |
| 2026-09-01 | **AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs**<br>Chou Jin Chua, Sarang Nambiar, Murali Srinivasan, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.01023) / [PDF](https://arxiv.org/pdf/2609.01023) |
| 2026-09-01 | **Using LLMs to Elicit Security Requirements for Service-Oriented Cyber Ranges**<br>Michail Takaronis, Athanasia Kollarou, Georgios Kavallieratos, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.00886) / [PDF](https://arxiv.org/pdf/2609.00886) |
| 2026-09-01 | **Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry**<br>Shengfang Zhai, Leo Marchyok, Yuling Shi, et al. | Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.00873) / [PDF](https://arxiv.org/pdf/2609.00873) |
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
