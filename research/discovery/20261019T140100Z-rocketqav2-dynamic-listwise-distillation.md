# Discovery Report: Round 758 — RocketQAv2 Joint Training for Dense Passage Retrieval and Passage Reranking

- **Timestamp**: `2026-10-19T14:01:00Z`
- **Selected Concept**: `AIMech:RocketQAv2JointTrainingDensePassageRetrievalAndReranking` (*RocketQAv2 Joint Training for Dense Passage Retrieval and Passage Reranking*)
- **Record Path**: `data/curated/RocketQAv2JointTrainingDensePassageRetrievalAndReranking.yaml`
- **Primary Source**: Ruiyang Ren, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She, Hua Wu, Haifeng Wang, Ji-Rong Wen — *RocketQAv2: A Joint Training Method for Dense Passage Retrieval and Passage Reranking* (`https://arxiv.org/bibtex/2110.07367`).

## Identity & Boundary Resolution

Distinct from RocketQA (AIMech:RocketQADenoisedHardNegativeSampling), which alternates separate training stages of the retriever and reranker with static pseudo-labels rather than joint synchronous dynamic listwise distillation; distinct from TAS-B (AIMech:TASBTopicAwareSamplingBalancedMarginDistillation), which distills pairwise score margins from static teacher models using topic-clustered batches; and distinct from AR2 (AIMech:AR2AdversarialRetrieverRankerForDenseTextRetrieval), which formulates retriever-ranker training as a minimax adversarial game rather than mutual listwise KL alignment.

## Constructed Boundary & Regime Verification

```text
[PASS] RocketQAv2 boundaries verified: L_kl_init=0.7845 -> L_kl_updated=0.6235, L_ce=0.5589, L_final_init=1.3435
```
