# Discovery Report: Round 749 — SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking)

- **Timestamp**: `2026-10-19T13:52:00Z`
- **Selected Concept**: `AIMech:SPLADESparseLexicalAndExpansionModel` (*SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking)*)
- **Record Path**: `data/curated/SPLADESparseLexicalAndExpansionModel.yaml`
- **Primary Source**: Thibault Formal, Benjamin Piwowarski, Stéphane Clinchant — *SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking* (`https://dblp.org/search/publ/api?q=SPLADE+Sparse+Lexical+and+Expansion+Model+Formal&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Formal, Piwowarski, and Clinchant (SIGIR 2021, pp. 2288-2292, arXiv:2107.05720). Distinguished from DeepCT (Dai & Callan, 2019), which re-weights only existing document terms without vocabulary expansion, from doc2query/docTTTTTquery (Nogueira et al., 2019), which perform offline sequence-to-sequence text expansion before BM25 indexing, and from SparTerm (Bai et al., 2020), which uses un-saturated ReLU summation with a fixed pre-trained binary gating mask rather than end-to-end log-saturated FLOPS-regularized training.

## Constructed Boundary & Regime Verification

```text
SPLADE boundary verification passed: {'flops_skewed': 4.0, 'flops_balanced': 1.0}
```
