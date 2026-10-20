# Discovery Report: Round 784 — TK Transformer-Kernel Neural Re-Ranking Model

- **Timestamp**: `2026-10-19T14:27:00Z`
- **Selected Concept**: `AIMech:TKTransformerKernelModelForReRanking` (*TK Transformer-Kernel Neural Re-Ranking Model*)
- **Record Path**: `data/curated/TKTransformerKernelModelForReRanking.yaml`
- **Primary Source**: Sebastian Hofstätter, Markus Zlabinger, Allan Hanbury — *Interpretable & Time-Budget-Constrained Contextualization for Re-Ranking* (`https://arxiv.org/bibtex/2002.01854`).

## Identity & Boundary Resolution

Distinct from CEDR-KNRM (AIMech:CEDRContextualizedEmbeddingsForDocumentRanking), which jointly encodes concatenated query-document pairs through 12-layer BERT and pools across L layer-wise similarity matrices with only log-normalized KNRM kernels plus BERT's [CLS] vector; and distinct from standard KNRM and Conv-KNRM, which use uncontextualized word embeddings or fixed-width local CNN n-gram filters without global sequence-wide self-attention or parallel document-length-normalized kernel pooling.

## Constructed Boundary & Regime Verification

```text
[PASS] TK boundaries verified: s_pos=0.6375 (slog=0.6020, slen=0.6908) > s_neg=-6.9331 (slog=-11.6206, slen=0.0981)
```
