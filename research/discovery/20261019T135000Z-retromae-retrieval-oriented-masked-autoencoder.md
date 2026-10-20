# Discovery Report: Round 747 — RetroMAE (Retrieval-Oriented Masked Auto-Encoder Pre-Training)

- **Timestamp**: `2026-10-19T13:50:00Z`
- **Selected Concept**: `AIMech:RetroMAERetrievalOrientedMaskedAutoEncoder` (*RetroMAE (Retrieval-Oriented Masked Auto-Encoder Pre-Training)*)
- **Record Path**: `data/curated/RetroMAERetrievalOrientedMaskedAutoEncoder.yaml`
- **Primary Source**: Shitao Xiao, Zheng Liu, Yingxia Shao, Zhao Cao — *RetroMAE: Pre-Training Retrieval-oriented Language Models Via Masked Auto-Encoder* (`https://dblp.org/search/publ/api?q=RetroMAE+Pre-Training+Retrieval-oriented+Language+Models+Xiao&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Xiao, Liu, Shao, and Cao (EMNLP 2022, pp. 538-548, arXiv:2205.12035). Distinguished from standard BERT Masked Language Modeling (15% single-mask token prediction without a sentence-embedding bottleneck), from Condenser/coCondenser (Gao & Callan, 2021, 2022) which concatenate the [CLS] state with intermediate encoder hidden states under a single mask, and from SEED (Lu et al., 2021) or TSDAE (Wang et al., 2021) which rely on autoregressive prefix decoding rather than asymmetric dual-mask MLM with two-stream position-specific attention.

## Constructed Boundary & Regime Verification

```text
RetroMAE boundary verification passed: {'diff_norm': 17.2766, 'tokens_reconstructed': 6}
```
