# Discovery Report: Round 754 — TAS-Balanced Topic-Aware Sampling and Dual-Teacher Margin Distillation

- **Timestamp**: `2026-10-19T13:57:00Z`
- **Selected Concept**: `AIMech:TASBTopicAwareSamplingBalancedMarginDistillation` (*TAS-Balanced Topic-Aware Sampling and Dual-Teacher Margin Distillation*)
- **Record Path**: `data/curated/TASBTopicAwareSamplingBalancedMarginDistillation.yaml`
- **Primary Source**: Sebastian Hofstatter, Sheng-Chieh Lin, Jheng-Hong Yang, Jimmy Lin, Allan Hanbury — *Efficiently Teaching an Effective Dense Retriever with Balanced Topic Aware Sampling* (`https://dblp.org/rec/conf/sigir/HofstatterLYLH21.xml`).

## Identity & Boundary Resolution

Distinct from ANCE (Xiong et al., ICLR 2021, AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning), which requires 8 V100 GPUs to repeatedly re-encode the passage corpus and refresh an ANN index every 10k batches; distinct from RocketQA (Qu et al., NAACL 2021, AIMech:RocketQADenoisedHardNegativeSampling), which requires cross-batch negatives of size 4,000 across 8 V100 GPUs and multi-cycle training; and distinct from single-teacher pairwise Margin-MSE or Tightly-Coupled Teachers (TCT-ColBERT), which use random query batches without topic-aware query clustering or balanced margin bin stratification.

## Constructed Boundary & Regime Verification

```text
Round 754 TAS-Balanced boundary verification passed.
```
