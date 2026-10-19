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
**1912 papers** across **4 publication years**. Latest arXiv metadata update: **2026-10-16**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 437 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 470 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 299 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 453 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 420 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 576 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 235 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 916 |
| [Other LLM Security](papers.md#other-llm-security) | 124 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-10-16 | **HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation**<br>Manohar Vellala, Soumya Banerjee, Sandip Roy, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23685) / [PDF](https://arxiv.org/pdf/2610.23685) |
| 2026-10-16 | **ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics**<br>Xiaohang Yu, Hejia Geng, William Knottenbelt | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23656) / [PDF](https://arxiv.org/pdf/2610.23656) |
| 2026-10-16 | **The Infinite Mutation Engine? Measuring Polymorphism in LLM-Generated Offensive Code**<br>Gabriel Hortea, Mario Varlese, Simon Pietro Romano, et al. | Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2605.03619) / [PDF](https://arxiv.org/pdf/2605.03619) |
| 2026-10-16 | **From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation**<br>Gabriel Hortea, Simon Pietro Romano, Juan Tapiador, et al. | Privacy &amp; Data Leakage, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense | [abstract](https://arxiv.org/abs/2610.23534) / [PDF](https://arxiv.org/pdf/2610.23534) |
| 2026-10-16 | **S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models**<br>Wenda Li, Tongya Zheng, Shunyu Liu, et al. | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23465) / [PDF](https://arxiv.org/pdf/2610.23465) |
| 2026-10-16 | **MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection**<br>Songping Wang, Peiyang Li, Yi Huang, et al. | Prompt Injection &amp; Jailbreaks, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23307) / [PDF](https://arxiv.org/pdf/2610.23307) |
| 2026-10-16 | **Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents**<br>Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2610.23254) / [PDF](https://arxiv.org/pdf/2610.23254) |
| 2026-10-16 | **AgentLoupe: Kernel-Resident Semantic Causal Labels for AI Agent Observability**<br>Yifei Bao, Ting Liu, Yuxin Ren, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2610.23233) / [PDF](https://arxiv.org/pdf/2610.23233) |
| 2026-10-16 | **From GAN-Based Models to GPT-5: A Taxonomy-Guided Study of Human Performance in Detecting Deepfake Face Images**<br>Zhiqing Guo, Lixin Jia, Luning Sun, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23144) / [PDF](https://arxiv.org/pdf/2610.23144) |
| 2026-10-16 | **When Approval Becomes Execution: Authorization-Grounded Workflow Attacks on Tool-Using Agents**<br>Chenggong Shi, Hongmei Mou | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23077) / [PDF](https://arxiv.org/pdf/2610.23077) |
| 2026-10-16 | **VulnSAGE: Adjudicating SAST Reports by Connecting LLM Reasoning to Program Structure**<br>Jinbao Chen, Zixiang Zhou, Yu Zhang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23035) / [PDF](https://arxiv.org/pdf/2610.23035) |
| 2026-10-16 | **ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack**<br>Yuanwei Wu, Lingdong Huang, Yunlong Mao, et al. | Prompt Injection &amp; Jailbreaks, Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.23030) / [PDF](https://arxiv.org/pdf/2610.23030) |
| 2026-10-16 | **Surprise Masking: Private Data Filtering with Model Likelihoods**<br>Riya Tyagi, Sahra Ghalebikesabi, Vinnie Monaco, et al. | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2610.22988) / [PDF](https://arxiv.org/pdf/2610.22988) |
| 2026-10-16 | **SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval**<br>Haoming Li, Dingyi Kang, Xu Hu, et al. | Agent &amp; Tool Security | [abstract](https://arxiv.org/abs/2610.22959) / [PDF](https://arxiv.org/pdf/2610.22959) |
| 2026-10-16 | **When Core-Network Elements Become Reachable: Field-Level Exploitability Analysis in Diameter**<br>Wei Yi, Changlong Han, Xue Zhang, et al. | Software &amp; Vulnerability Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2610.22943) / [PDF](https://arxiv.org/pdf/2610.22943) |
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
