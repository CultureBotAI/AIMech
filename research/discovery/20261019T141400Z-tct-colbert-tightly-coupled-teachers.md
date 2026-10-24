# Discovery Report: Round 771 — TCT-ColBERT Tightly-Coupled Teachers Knowledge Distillation for Dense Retrieval

- **Timestamp**: `2026-10-19T14:14:00Z`
- **Selected Concept**: `AIMech:TCTColBERTTightlyCoupledTeachersForDenseRetrieval` (*TCT-ColBERT Tightly-Coupled Teachers Knowledge Distillation for Dense Retrieval*)
- **Record Path**: `data/curated/TCTColBERTTightlyCoupledTeachersForDenseRetrieval.yaml`
- **Primary Source**: Sheng-Chieh Lin, Jheng-Hong Yang, Jimmy Lin — *Distilling Dense Representations for Ranking using Tightly-Coupled Teachers* (`https://arxiv.org/bibtex/2010.11386`).

## Identity & Boundary Resolution

Distinct from TAS-B (AIMech:TASBTopicAwareSamplingBalancedMarginDistillation), which distills pairwise score margins from dual ColBERT and cross-encoder teachers over topic-clustered queries rather than temperature-scaled listwise KL divergence over dynamic in-batch subsampled passages from a tightly-coupled ColBERT teacher; distinct from RocketQA (AIMech:RocketQADenoisedHardNegativeSampling) and RocketQAv2 (AIMech:RocketQAv2JointTrainingDensePassageRetrievalAndReranking), which distill from a cross-encoder reranker over per-query candidate lists rather than a late-interaction MaxSim teacher over full O(|B|^2) in-batch query-passage grids; and distinct from ANCE (AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning), which requires periodic asynchronous corpus-wide ANN re-encoding instead of tightly-coupled in-batch teacher distillation.

## Constructed Boundary & Regime Verification

```text
[PASS] TCT-ColBERT boundaries verified: loss_before=0.7749 -> loss_after=0.2635, hybrid_scores={'doc_both': 72.88, 'doc_dense_only': 74.08, 'doc_sparse_only': 73.48}
```
