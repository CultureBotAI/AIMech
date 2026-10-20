# Discovery Report: Round 768 — DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval

- **Timestamp**: `2026-10-19T14:11:00Z`
- **Selected Concept**: `AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval` (*DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval*)
- **Record Path**: `data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml`
- **Primary Source**: Zhuyun Dai, Jamie Callan — *Context-Aware Sentence/Passage Term Importance Estimation For First Stage Retrieval* (`https://arxiv.org/bibtex/1910.10687`).

## Identity & Boundary Resolution

Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which projects over the entire MLM vocabulary to perform term expansion and trains end-to-end with contrastive ranking and FLOPS regularization; and distinct from COIL (AIMech:COILContextualizedInvertedList), which stores multi-dimensional contextualized vectors per token in inverted lists rather than scalar integer pseudo-frequencies TF_DeepCT(t, d) compatible with unmodified BM25 and Query Likelihood inverted indexes.

## Constructed Boundary & Regime Verification

```text
[PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00, TF_DeepCT(p1)=78 > TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 > BM25_DeepCT(p2)=4.5833
```
