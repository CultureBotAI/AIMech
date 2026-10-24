# Discovery Report: Round 759 — PAIR Passage-Centric Similarity Relation for Dense Passage Retrieval

- **Timestamp**: `2026-10-19T14:02:00Z`
- **Selected Concept**: `AIMech:PAIRPassageCentricSimilarityRelationForDenseRetrieval` (*PAIR Passage-Centric Similarity Relation for Dense Passage Retrieval*)
- **Record Path**: `data/curated/PAIRPassageCentricSimilarityRelationForDenseRetrieval.yaml`
- **Primary Source**: Ruiyang Ren, Shangwen Lv, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She, Hua Wu, Haifeng Wang, Ji-Rong Wen — *PAIR: Leveraging Passage-Centric Similarity Relation for Improving Dense Passage Retrieval* (`https://arxiv.org/bibtex/2108.06027`).

## Identity & Boundary Resolution

Distinct from DPR (AIMech:DensePassageRetrieval) and RocketQA (AIMech:RocketQADenoisedHardNegativeSampling), which optimize only query-passage similarity f(q, p) without explicitly penalizing passage-passage inner products f(p^+, p^-); and distinct from GPL (AIMech:GPLGenerativePseudoLabelingForDenseRetrieval), which distills cross-encoder query-passage margins on synthetic queries rather than optimizing a passage-centric contrastive repulsion loss L_P.

## Constructed Boundary & Regime Verification

```text
[PASS] PAIR passage-centric similarity boundaries verified: L_P(clustered)=1.9273 > L_P(separated)=0.8203, L_PAIR(clustered)=0.9241 > L_PAIR(separated)=0.3059
```
