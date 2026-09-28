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
**1404 papers** across **4 publication years**. Latest arXiv metadata update: **2026-09-25**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 310 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 356 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 222 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 324 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 302 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 444 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 175 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 670 |
| [Other LLM Security](papers.md#other-llm-security) | 94 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-09-25 | **FragToken: Amplifying LLM Inference Costs through Noncanonical Token Generation**<br>Zihan Wang, Rui Zhang, Xinyuan Qian, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.31552) / [PDF](https://arxiv.org/pdf/2609.31552) |
| 2026-09-25 | **AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents**<br>Weida Liang, Shi Qiu, Zhun Wang, et al. | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.31318) / [PDF](https://arxiv.org/pdf/2609.31318) |
| 2026-09-25 | **Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains**<br>Toqeer Ali Syed, Asadullah Abdullah Khan | Agent &amp; Tool Security, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.31282) / [PDF](https://arxiv.org/pdf/2609.31282) |
| 2026-09-25 | **Deduplication-while-Training: A Resilient Paradigm for Privacy-Preserving Cross-Client Deduplication in Federated Learning**<br>Rongxi Wang, Guanxiong Ha, Chunfu Jia, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2609.31262) / [PDF](https://arxiv.org/pdf/2609.31262) |
| 2026-09-25 | **From ASR to ASP: Evaluating Prompt Attack Vulnerabilities Against Open-Source LLMs**<br>Jiawen Wang, Pritha Gupta, Eyke Hüllermeier, et al. | Prompt Injection &amp; Jailbreaks, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2505.14368) / [PDF](https://arxiv.org/pdf/2505.14368) |
| 2026-09-25 | **AuthGuard-R: Safety-Compliant Mission Hijacking and Dual-Gate Defense for LLM-Controlled Robots**<br>Saidattu Chepuri, Vikas Srivastava | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.31110) / [PDF](https://arxiv.org/pdf/2609.31110) |
| 2026-09-25 | **MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes**<br>Hanzhang Ma, Ali Hariri, Tianxiang Shen, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2609.31039) / [PDF](https://arxiv.org/pdf/2609.31039) |
| 2026-09-25 | **Blind, Not Weak: A Best-of-Suite Safety-Utility Frontier for Recover-and-Reguard Defenses Against Encoded VLM Jailbreaks**<br>Haoyu Zhang, Zhuoxi Wang, Shibo Zheng, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2607.26574) / [PDF](https://arxiv.org/pdf/2607.26574) |
| 2026-09-25 | **The Uncontrolled Variable: Vision-Language Refusal Is Conditioned on the Image-Attachment Interface, and Not Robust to Irrelevant Image Properties**<br>Haoyu Zhang, Yi Feng, Hanwen Liu, et al. | Privacy &amp; Data Leakage, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2609.26174) / [PDF](https://arxiv.org/pdf/2609.26174) |
| 2026-09-25 | **Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis**<br>Thong Bach, Dung Nguyen, Thao Minh Le, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.30841) / [PDF](https://arxiv.org/pdf/2609.30841) |
| 2026-09-25 | **What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs**<br>Xingyu Li, Juefei Pu, Yifan Wu, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2509.22796) / [PDF](https://arxiv.org/pdf/2509.22796) |
| 2026-09-25 | **AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents**<br>Xiaorui Zhang, Zhuoran Cheng, Kailin Liu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.30830) / [PDF](https://arxiv.org/pdf/2609.30830) |
| 2026-09-25 | **Crypto-bound identity-verified capability tokens for coordinating distributed AI agents: A proposal**<br>Srikumar Subramanian, Shubhashis Sengupta | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2609.30824) / [PDF](https://arxiv.org/pdf/2609.30824) |
| 2026-09-25 | **PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations**<br>Luciano Maldonado | Prompt Injection &amp; Jailbreaks, Privacy &amp; Data Leakage, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2609.30094) / [PDF](https://arxiv.org/pdf/2609.30094) |
| 2026-09-25 | **A Large-Scale Empirical Study of Modern Phishing Email Content**<br>Jaehwan Park, Woonghee Lee, Fujiao Ji, et al. | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2609.30683) / [PDF](https://arxiv.org/pdf/2609.30683) |
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
