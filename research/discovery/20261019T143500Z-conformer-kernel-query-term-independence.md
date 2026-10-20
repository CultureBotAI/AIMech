# Discovery Report: Round 792 — Conformer-Kernel with Query Term Independence for Document Retrieval

- **Timestamp**: `2026-10-19T14:35:00Z`
- **Selected Concept**: `AIMech:ConformerKernelWithQueryTermIndependenceForDocumentRetrieval` (*Conformer-Kernel with Query Term Independence for Document Retrieval*)
- **Record Path**: `data/curated/ConformerKernelWithQueryTermIndependenceForDocumentRetrieval.yaml`
- **Primary Source**: Bhaskar Mitra, Sebastian Hofstätter, Hamed Zamani, Nick Craswell — *Conformer-Kernel with Query Term Independence for Document Retrieval* (`https://arxiv.org/bibtex/2007.10434`).

## Identity & Boundary Resolution

Distinct from TK (AIMech:TKTransformerKernelRankingModel, which contextualizes both query and document with quadratic self-attention) and TKL (AIMech:TKLTransformerKernelForLongDocuments, which applies TK over overlapping sliding windows of long documents). Conformer-Kernel replaces quadratic self-attention with separable self-attention (Equations 5-6) inside a parallel Convolution+Transformer (Conformer) block and optionally enforces Query Term Independence (CK with QTI) by combining a learned explicit batch-scaled BM25 sub-model s_{t,d}^{(explicit)} (Equations 9-10) with an implicit Conformer-Kernel sub-model s_{t,d}^{(implicit)} (Equations 11-16) whose non-negative combined scores s_{t,d} = ReLU(alpha * s_{t,d}^{(explicit)} + (1 - alpha) * s_{t,d}^{(implicit)} + b_comb) can be pre-computed offline for top-k vocabulary terms per document.

## Constructed Boundary & Regime Verification

```text
Conformer-Kernel with QTI boundary verification passed:
  Intermediate A shape: (8, 6) vs full (200, 200)
  Explicit BM25 scores: [1.113, 2.1787, 1.3838]
```
