# Discovery Report: Round 775 — uniCOIL Unified Contextualized Inverted List Sparse Retrieval

- **Timestamp**: `2026-10-19T14:18:00Z`
- **Selected Concept**: `AIMech:uniCOILUnifiedContextualizedInvertedList` (*uniCOIL Unified Contextualized Inverted List Sparse Retrieval*)
- **Record Path**: `data/curated/uniCOILUnifiedContextualizedInvertedList.yaml`
- **Primary Source**: Jimmy Lin, Xueguang Ma — *A Few Brief Notes on DeepImpact, COIL, and a Conceptual Framework for Information Retrieval Techniques* (`https://arxiv.org/bibtex/2106.14807`).

## Identity & Boundary Resolution

Distinct from COIL (AIMech:COILContextualizedInvertedList), which stores d = 32 real-valued contextualized token vectors requiring custom vector-inverted-list infrastructure (~40 GB index on MS MARCO) and allows negative weights; distinct from DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval), which trains a regression model on pseudo-ground-truth term frequencies without document expansion or query-term weighting and still relies on BM25's IDF/length-normalization formula; and distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which performs end-to-end MLM-logit vocabulary expansion rather than combining d = 1 COIL scalar impact weighting with external doc2query-T5 expansion.

## Constructed Boundary & Regime Verification

```text
[PASS] uniCOIL boundaries verified: unexpanded=15616 < expanded=47848, hybrid_fused={'doc_pos': 1.7286, 'doc_hard_dense': 1.0, 'doc_neg': 0.1037}
```
