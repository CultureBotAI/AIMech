# Discovery Report: Round 761 — ADORE and STAR Hard-Negative Dense Retrieval Training Framework

- **Timestamp**: `2026-10-19T14:04:00Z`
- **Selected Concept**: `AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives` (*ADORE and STAR Hard-Negative Dense Retrieval Training Framework*)
- **Record Path**: `data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml`
- **Primary Source**: Jingtao Zhan, Jiaxin Mao, Yiqun Liu, Jiafeng Guo, Min Zhang, Shaoping Ma — *Optimizing Dense Retrieval Model Training with Hard Negatives* (`https://arxiv.org/bibtex/2104.08051`).

## Identity & Boundary Resolution

Distinct from ANCE (AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning), which periodically re-encodes the entire corpus and rebuilds the ANN index every several thousand steps to refresh static hard negatives without random-negative stabilization or metric-weighted LambdaLoss; and distinct from RocketQA (AIMech:RocketQADenoisedHardNegativeSampling), which uses a cross-encoder teacher to filter static hard negatives rather than online query-side dynamic hard negative retrieval against a fixed document index.

## Constructed Boundary & Regime Verification

```text
[PASS] ADORE & STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783 > L_ADORE(rank3)=0.0976
```
