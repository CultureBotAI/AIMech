# Discovery Report: Round 776 — DeepImpact Learning Passage Impacts for Inverted Indexes

- **Timestamp**: `2026-10-19T14:19:00Z`
- **Selected Concept**: `AIMech:DeepImpactLearningPassageImpactsForInvertedIndexes` (*DeepImpact Learning Passage Impacts for Inverted Indexes*)
- **Record Path**: `data/curated/DeepImpactLearningPassageImpactsForInvertedIndexes.yaml`
- **Primary Source**: Antonio Mallia, Omar Khattab, Torsten Suel, Nicola Tonellotto — *Learning Passage Impacts for Inverted Indexes* (`https://arxiv.org/bibtex/2104.12016`).

## Identity & Boundary Resolution

Distinct from DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval), which trains per-token linear regression against static heuristic ground-truth term recall weights rather than end-to-end pairwise ranking over sum-of-impacts and requires BM25 scoring formulas at query time; and distinct from uniCOIL (AIMech:uniCOILUnifiedContextualizedInvertedList), which operates over WordPiece subword tokens and computes query-time contextualized query term weights rather than query-independent first-occurrence word-level impacts.

## Constructed Boundary & Regime Verification

```text
[PASS] DeepImpact boundaries verified: s_pos=8.755 (quantized=720) > s_neg=0.500 (quantized=42), loss=0.0003
```
