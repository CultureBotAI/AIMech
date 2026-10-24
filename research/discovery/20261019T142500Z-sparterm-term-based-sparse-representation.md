# Discovery Report: Round 782 — SparTerm Learning Term-Based Sparse Representation for Fast Text Retrieval

- **Timestamp**: `2026-10-19T14:25:00Z`
- **Selected Concept**: `AIMech:SparTermLearningTermBasedSparseRepresentation` (*SparTerm Learning Term-Based Sparse Representation for Fast Text Retrieval*)
- **Record Path**: `data/curated/SparTermLearningTermBasedSparseRepresentation.yaml`
- **Primary Source**: Yang Bai, Xiaoguang Li, Gang Wang, Chaoliang Zhang, Lifeng Shang, Jun Xu, Zhaowei Wang, Fangshan Wang, Qun Liu — *SparTerm: Learning Term-based Sparse Representation for Fast Text Retrieval* (`https://arxiv.org/bibtex/2010.00768`).

## Identity & Boundary Resolution

Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which eliminates the separate binary gating network G(p) and achieves sparsity by applying log(1 + ReLU(.)) to MLM logits under differentiable FLOPS regularization; and distinct from EPIC (AIMech:EPICExpansionViaPredictionOfImportanceWithContextualization), which produces dense |V|-dimensional document vectors scaled by softplus token weights and a sigmoid [CLS] quality gate without binary gating or inverted-index full-ranking execution.

## Constructed Boundary & Regime Verification

```text
[PASS] SparTerm boundaries verified: score_literal=6.0360 < score_expanded=10.0710 (> score_neg=0.0000), L_rank=0.000042, L_exp=0.1986
```
