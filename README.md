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
**2348 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-12**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 550 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 578 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 370 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 549 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 513 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 686 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 280 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1088 |
| [Other LLM Security](papers.md#other-llm-security) | 155 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-12 | **ANCHOR: Schema-Agnostic Threat Knowledge Graph Construction via Hybrid Ontology Discovery**<br>Seonwoo Kim, Jinwoo Kim, Daegyu Kang, et al. | Privacy &amp; Data Leakage, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2606.01208) / [PDF](https://arxiv.org/pdf/2606.01208) |
| 2026-11-12 | **Conflux: Preventing Privilege Escalation with Principal Contexts and System-Level Evaluation**<br>Raya Buckley, Christian Schroeder de Witt | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.08768) / [PDF](https://arxiv.org/pdf/2611.08768) |
| 2026-11-12 | **Preserve the Vulnerability, Break the Alert: Testing the Robustness of CodeQL Taint Tracking with Natural Rewrites**<br>Zhezhen Cao, Weiyuan Ding, Bowen Xu | Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.17123) / [PDF](https://arxiv.org/pdf/2611.17123) |
| 2026-11-12 | **CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts**<br>Zimo Xu, Wenzhuo Liu, Hideki Nakayama | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.17115) / [PDF](https://arxiv.org/pdf/2611.17115) |
| 2026-11-12 | **Optimal Single-History Tokenization Disambiguation for Provably Secure Linguistic Steganography**<br>Feng Jiang | Other LLM Security | [abstract](https://arxiv.org/abs/2611.17091) / [PDF](https://arxiv.org/pdf/2611.17091) |
| 2026-11-12 | **STEALTH: Steganographic Text Encoding Agnostic to Low-Level Tensor Hardware**<br>William Fleshman | Other LLM Security | [abstract](https://arxiv.org/abs/2611.16928) / [PDF](https://arxiv.org/pdf/2611.16928) |
| 2026-11-12 | **Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents**<br>Yiheng Zhao, Runze Ji, Chenyu Yi, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.16744) / [PDF](https://arxiv.org/pdf/2611.16744) |
| 2026-11-12 | **Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models**<br>Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.39509) / [PDF](https://arxiv.org/pdf/2610.39509) |
| 2026-11-12 | **MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection**<br>Yingbin Jin, Ji'an Wang, HaoYang Chai, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.16693) / [PDF](https://arxiv.org/pdf/2611.16693) |
| 2026-11-12 | **ASAP: Assembly-Source Aligned Pseudocode Refinement For Binary Decompilation**<br>Yujian Zhuang, Dehong Gao, Qichao Zhang, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2610.06900) / [PDF](https://arxiv.org/pdf/2610.06900) |
| 2026-11-12 | **BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems**<br>Leonhard Waibl, Felix Michalak, Hadrien Mariaccia | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.20668) / [PDF](https://arxiv.org/pdf/2606.20668) |
| 2026-11-12 | **Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function**<br>Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse, Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.16369) / [PDF](https://arxiv.org/pdf/2611.16369) |
| 2026-11-12 | **Data-Efficient LLM Safety Alignment Guided by Interpretable Features**<br>Hongyu Li, Zhan Yu, Zhe Zhao, et al. | Agent &amp; Tool Security, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.16183) / [PDF](https://arxiv.org/pdf/2611.16183) |
| 2026-11-12 | **PolicySniff: Inferring Agent Policy States through Shared-GPU Execution**<br>Weimin Fu, Minghao Shao, Zeng Wang, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2611.16158) / [PDF](https://arxiv.org/pdf/2611.16158) |
| 2026-11-12 | **Intent-Aware Protection for AI Agents**<br>Fady Copty, Neta Haiby, Max Braitmaiere, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.16122) / [PDF](https://arxiv.org/pdf/2611.16122) |
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
