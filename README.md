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
**2432 papers** across **4 publication years**. Latest arXiv metadata update: **2026-11-18**.

| Topic | Papers |
| --- | ---: |
| [Prompt Injection &amp; Jailbreaks](papers.md#prompt-injection--jailbreaks) | 573 |
| [Agent &amp; Tool Security](papers.md#agent--tool-security) | 592 |
| [Privacy &amp; Data Leakage](papers.md#privacy--data-leakage) | 382 |
| [Safety, Alignment &amp; Misuse](papers.md#safety-alignment--misuse) | 572 |
| [Adversarial ML, Poisoning &amp; Backdoors](papers.md#adversarial-ml-poisoning--backdoors) | 535 |
| [Software &amp; Vulnerability Security](papers.md#software--vulnerability-security) | 710 |
| [Malware, Phishing &amp; Cyber Defense](papers.md#malware-phishing--cyber-defense) | 292 |
| [Evaluation, Benchmarks &amp; Red Teaming](papers.md#evaluation-benchmarks--red-teaming) | 1128 |
| [Other LLM Security](papers.md#other-llm-security) | 157 |
<!-- SECPAPERS:STATS:END -->

## Latest papers

<!-- SECPAPERS:LATEST:START -->
| Updated | Paper | Topics | Links |
| --- | --- | --- | --- |
| 2026-11-18 | **Jailbreak Detection on Large Language Models via Contrastive Prototype Structures**<br>Yan Qiu, Yuanyuan Li | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24936) / [PDF](https://arxiv.org/pdf/2611.24936) |
| 2026-11-18 | **LLM-Guided Cyber-Physical Attack Path Identification in Smart Grids**<br>Amr Elshazly, Jesse Roberts, Rachad Atat, et al. | Safety, Alignment &amp; Misuse, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24765) / [PDF](https://arxiv.org/pdf/2611.24765) |
| 2026-11-18 | **Extracting Training Data from Diffusion Language Models via Infilling**<br>Yihan Wang, N. Asokan | Privacy &amp; Data Leakage | [abstract](https://arxiv.org/abs/2605.24173) / [PDF](https://arxiv.org/pdf/2605.24173) |
| 2026-11-18 | **TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization**<br>Matan Ben-Tov, Mahmood Sharif | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2606.23496) / [PDF](https://arxiv.org/pdf/2606.23496) |
| 2026-11-18 | **Language Model Security Modules: Turning LLM Interpretability into Runtime Defense**<br>XiuYu Zhang, Bonan Ruan, Junfeng Fang, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2608.25697) / [PDF](https://arxiv.org/pdf/2608.25697) |
| 2026-11-18 | **Who Is Behind the Harness? Verifying Model Identity in Coding Agents through Behavioral Fingerprinting**<br>Chuyi Wang, Xiaohui Xie, Tongze Wang, et al. | Other LLM Security | [abstract](https://arxiv.org/abs/2609.28559) / [PDF](https://arxiv.org/pdf/2609.28559) |
| 2026-11-18 | **PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents**<br>Lipeng He, Yihan Wang, Jiawen Zhang, et al. | Prompt Injection &amp; Jailbreaks, Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Software &amp; Vulnerability Security, Malware, Phishing &amp; Cyber Defense, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24362) / [PDF](https://arxiv.org/pdf/2611.24362) |
| 2026-11-18 | **AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents**<br>Stavros Damianakis, Konstantinos Psounis | Prompt Injection &amp; Jailbreaks, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24313) / [PDF](https://arxiv.org/pdf/2611.24313) |
| 2026-11-18 | **When Shuffling Fails: Token Recovery from Obfuscated KV Caches**<br>Chengzhi Yi, Xiao Cheng, Wei Song, et al. | Software &amp; Vulnerability Security | [abstract](https://arxiv.org/abs/2611.24276) / [PDF](https://arxiv.org/pdf/2611.24276) |
| 2026-11-18 | **What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents**<br>Haoyang Liu, Yinong Xu, Zhe Lang, et al. | Prompt Injection &amp; Jailbreaks | [abstract](https://arxiv.org/abs/2611.24231) / [PDF](https://arxiv.org/pdf/2611.24231) |
| 2026-11-18 | **Reinforcement Learning with Reference-Based Rewards for Language Model Reasoning and Alignment**<br>Shuai Zhao, Yunqiu Xu, Linchao Zhu, et al. | Safety, Alignment &amp; Misuse | [abstract](https://arxiv.org/abs/2504.09895) / [PDF](https://arxiv.org/pdf/2504.09895) |
| 2026-11-18 | **Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming**<br>Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong, et al. | Agent &amp; Tool Security, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24221) / [PDF](https://arxiv.org/pdf/2611.24221) |
| 2026-11-18 | **Evaluating LIM Trading Agents: A Critical Review of Backtesting Validity and Reporting Practices**<br>Long Xu, Fuyi Wang, Xiaolu Hu, et al. | Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.24133) / [PDF](https://arxiv.org/pdf/2611.24133) |
| 2026-11-18 | **Weighing the Envelope: Component Weight and Arbitration in Envelope-Layer Defenses for a Single LLM Agent**<br>Yuelin Han | Agent &amp; Tool Security, Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.23844) / [PDF](https://arxiv.org/pdf/2611.23844) |
| 2026-11-18 | **Plug-and-Play Multi-Licensee Robust Watermarking for Mixture-of-Experts LLMs**<br>Jianshuo Liu, Kang G. Shin, Haining Wang | Adversarial ML, Poisoning &amp; Backdoors, Evaluation, Benchmarks &amp; Red Teaming | [abstract](https://arxiv.org/abs/2611.23838) / [PDF](https://arxiv.org/pdf/2611.23838) |
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
