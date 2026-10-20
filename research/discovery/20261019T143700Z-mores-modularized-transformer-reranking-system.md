# Discovery Report: Round 794 — MORES (Modularized Transformer-Based Ranking Framework)

- **Timestamp**: `2026-10-19T14:37:00Z`
- **Selected Concept**: `AIMech:MORESModularizedTransformerBasedRankingFramework` (*MORES (Modularized Transformer-Based Ranking Framework)*)
- **Record Path**: `data/curated/MORESModularizedTransformerBasedRankingFramework.yaml`
- **Primary Source**: Luyu Gao, Zhuyun Dai, Jamie Callan — *Modularized Transfomer-based Ranking Framework* (`https://arxiv.org/bibtex/2004.13313`).

## Identity & Boundary Resolution

Distinct from concatenated cross-encoder BERT rankers (which apply quadratic O((d+q)^2) full self-attention across query and document in every layer), from late-interaction ColBERT (AIMech:ColBERTContextualizedLateInteractionOverBERT, which computes MaxSim dot products without learned Transformer Interaction Blocks), and from DC-BERT (AIMech:DCBERTDecouplingQuestionAndDocumentForEfficientContextualEncoding, which feeds concatenated upper-layer query and document tokens into full (d+q)^2 self-attention layers). MORES restricts online interaction in each Interaction Block strictly to query-to-document cross-attention O(q*d) plus query self-attention O(q^2), leaving D fixed so that per-IB key/value projections D_proj = {D W_k, D W_v} can be pre-computed offline under Reuse-S2.

## Constructed Boundary & Regime Verification

```text
MORES boundary verification passed:
  Max |Reuse-S1 - Reuse-S2| diff: 0.0
  Per-layer online op ratio BERT / Reuse-S2: 32.98x
```
