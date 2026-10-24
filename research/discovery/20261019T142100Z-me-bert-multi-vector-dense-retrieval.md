# Discovery Report: Round 778 — ME-BERT Multi-Vector Dense Retrieval

- **Timestamp**: `2026-10-19T14:21:00Z`
- **Selected Concept**: `AIMech:MEBERTMultiVectorDenseRetrieval` (*ME-BERT Multi-Vector Dense Retrieval*)
- **Record Path**: `data/curated/MEBERTMultiVectorDenseRetrieval.yaml`
- **Primary Source**: Yi Luan, Jacob Eisenstein, Kristina Toutanova, Michael Collins — *Sparse, Dense, and Attentional Representations for Text Retrieval* (`https://arxiv.org/bibtex/2005.00181`).

## Identity & Boundary Resolution

Distinct from ColBERT (AIMech:ColBERTContextualizedLateInteraction), which encodes every query token and every document token and sums maximum similarities across all query tokens (requiring multiple MIPS queries per user query plus post-processing rather than a single query vector searched against m fixed vectors per document); and distinct from Poly-encoders (AIMech:PolyEncoderArchitecture), which apply a softmax-weighted attention step over m context codes before computing the final query dot product (preventing direct single-query sublinear MIPS indexing).

## Constructed Boundary & Regime Verification

```text
[PASS] ME-BERT boundaries verified: mu_multi=1.0000 > mu_single=0.2157, k_multi=52.6 < k_single=440.1, best_doc='doc_0' (1.1600)
```
