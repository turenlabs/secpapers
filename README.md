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
**1061 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-02**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 232 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 264 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 153 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 257 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 238 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 338 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 129 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 506 |
| [Other LLM Security](papers.md#other-llm-security) | 76 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-02 | **The Implications of Linguistic Illegibility for LLM Security**<br>James Mickens | Other LLM Security | [abstract](https://arxiv.org/abs/2609.02852) / [PDF](https://arxiv.org/pdf/2609.02852) |
| 2026-09-02 | **LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation**<br>Xingyu Chen, Rui Wang, Zhaopeng Tu, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.24780) / [PDF](https://arxiv.org/pdf/2607.24780) |
| 2026-09-02 | **SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment**<br>Qinghua Mao, Wanying Qu, Dadi Guo, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.02786) / [PDF](https://arxiv.org/pdf/2609.02786) |
| 2026-09-02 | **CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation**<br>Varun Gadey, Ziad Marey, Alexandra Dmitrienko | Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.02774) / [PDF](https://arxiv.org/pdf/2609.02774) |
| 2026-09-02 | **LLM Watermarking as Big Data Provenance: A Deployment-Oriented Systematization**<br>Huy Phan, Kieu Dang, Ojaswi Dulal, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.10103) / [PDF](https://arxiv.org/pdf/2607.10103) |
| 2026-09-02 | **ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use**<br>Zhiyang Ding, Yang Luo, Guangpu Chen, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.02690) / [PDF](https://arxiv.org/pdf/2609.02690) |
| 2026-09-02 | **Automated Vulnerability Injection in Smart Contracts Using Large Language Models**<br>Luca Migliaccio, Roberto Natella, Naghmeh Ivaki, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2609.02624) / [PDF](https://arxiv.org/pdf/2609.02624) |
| 2026-09-02 | **Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation**<br>Yuxuan Qiao, Dongqin Liu, Hongchang Yang, et al. | Agent &amp; Tool Security, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2512.16310) / [PDF](https://arxiv.org/pdf/2512.16310) |
| 2026-09-02 | **Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation**<br>Junyu Lu, Kaiyuan Liu, Jingyi Kang, et al. | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2608.22230) / [PDF](https://arxiv.org/pdf/2608.22230) |
| 2026-09-02 | **A Finger on the Scale: Covert Policy Steering through Agentic Skills**<br>Jiarui Li, Jiahao Chen, Chunyi Zhou, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2609.02564) / [PDF](https://arxiv.org/pdf/2609.02564) |
| 2026-09-02 | **SpiderSapien: Client-Centric Web Crawler and Security Scanner**<br>Eric Olsson, Benjamin Eriksson, Adam Doupé, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.02532) / [PDF](https://arxiv.org/pdf/2609.02532) |
| 2026-09-02 | **Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue?**<br>Rafael Uetz, Philipp Bönninghausen, Louis Hackländer-Jansen, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.02465) / [PDF](https://arxiv.org/pdf/2609.02465) |
| 2026-09-02 | **Persistent Sparse Autoencoders: Learning Feature-Specific Timescales in Language Model Representations**<br>Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2607.17117) / [PDF](https://arxiv.org/pdf/2607.17117) |
| 2026-09-02 | **Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions**<br>Huihao Jing, Wenbin Hu, Shaojin Chen, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.12406) / [PDF](https://arxiv.org/pdf/2607.12406) |
| 2026-09-02 | **PoC-Gym: Towards More Reliable LLM-Assisted Proof-of-Concept Exploit Generation**<br>Derin Gezgin, Amartya Das, Shinhae Kim, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2602.04165) / [PDF](https://arxiv.org/pdf/2602.04165) |
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
