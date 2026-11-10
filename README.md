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
**2305 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-09**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 541 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 571 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 360 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 534 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 503 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 675 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 276 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1072 |
| [Other LLM Security](papers.md#other-llm-security) | 150 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-09 | **Suppression Is Not Erasure: Mechanistic Analysis and Reactivation Boundaries of Subspace Projection for LoRA Backdoor Defense**<br>Junsheng Fu, Shuangshuang Gao | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.12807) / [PDF](https://arxiv.org/pdf/2611.12807) |
| 2026-11-09 | **The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort**<br>Aleksandr Churilov | Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2605.17062) / [PDF](https://arxiv.org/pdf/2605.17062) |
| 2026-11-09 | **LLM Watermarking as Big Data Provenance: A Deployment-Oriented Systematization**<br>Huy Phan, Kieu Dang, Ojaswi Dulal, et al. | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2607.10103) / [PDF](https://arxiv.org/pdf/2607.10103) |
| 2026-11-09 | **Text2NGAC: a multi-LLM pipeline for NGAC policy extraction with mutation-based verification**<br>Ayesha Habib, Huixiang Zhang, Dan Zhu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.12572) / [PDF](https://arxiv.org/pdf/2611.12572) |
| 2026-11-09 | **Diffusion LLMs are Natural Adversaries for any LLM**<br>David Lüdke, Tom Wollschläger, Paul Ungermann, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2511.00203) / [PDF](https://arxiv.org/pdf/2511.00203) |
| 2026-11-09 | **Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks**<br>Dario Pasquini, Reworr, Giuseppe Ateniese, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2611.12386) / [PDF](https://arxiv.org/pdf/2611.12386) |
| 2026-11-09 | **MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study**<br>Farooq Shaikh, Biagio Montaruli | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.03555) / [PDF](https://arxiv.org/pdf/2611.03555) |
| 2026-11-09 | **SNAPRAG: Cost-Efficient Knowledge Extraction Attack on RAG Systems via Adversarial Perturbations**<br>Melih Coşğun, Mehmet Emre Gürsoy, Alptekin Küpçü, et al. | Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2611.12241) / [PDF](https://arxiv.org/pdf/2611.12241) |
| 2026-11-09 | **Latent-space Attacks for Refusal Evasion in Language Models**<br>Giorgio Piras, Raffaele Mura, Fabio Brau, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Adversarial ML, Poisoning &amp; Backdoors | [abstract](https://arxiv.org/abs/2605.21706) / [PDF](https://arxiv.org/pdf/2605.21706) |
| 2026-11-09 | **OrigaMI: An LLM Serving System with First-Class Interpretability Apps**<br>Michael Blum, Mark Silberstein, Yaniv David | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2607.22595) / [PDF](https://arxiv.org/pdf/2607.22595) |
| 2026-11-09 | **StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills**<br>Jingfen Qiao, Rui Li, Shuaiqun Pan, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.12155) / [PDF](https://arxiv.org/pdf/2611.12155) |
| 2026-11-09 | **Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots**<br>Mark Vero, Fabian Kaczmarczyck, Ivan Petrov, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.29963) / [PDF](https://arxiv.org/pdf/2605.29963) |
| 2026-11-09 | **Harness Matters: Measuring and Dissecting Security Resilience in Web Agents**<br>Xinyi Wu, Jiagui Chen, JiaYi Dong, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.11971) / [PDF](https://arxiv.org/pdf/2611.11971) |
| 2026-11-09 | **Alignment Dynamics in LLM Fine-Tuning**<br>Yuhan Huang, Huanran Chen, Yinpeng Dong | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2605.18309) / [PDF](https://arxiv.org/pdf/2605.18309) |
| 2026-11-09 | **Spectral Unlearning: Transformer Structure-Preserving Updates for Language Models**<br>Sung Il Choi, Junhao Cai, Dohun Kim, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2611.11902) / [PDF](https://arxiv.org/pdf/2611.11902) |
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
