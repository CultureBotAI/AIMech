# Discovery Report: Round 514 — GCFL+ (Gradient Sequence Dynamic Time Warping Clustered Federated Graph Classification)

- **Timestamp**: `2026-10-19T09:57:00Z`
- **Selected Concept**: `AIMech:GcflPlusGradientSequenceDynamicTimeWarpingClusteredFederatedGraphClassification` (*GCFL+ (Gradient Sequence Dynamic Time Warping Clustered Federated Graph Classification)*)
- **Record Path**: `data/curated/GcflPlusGradientSequenceDynamicTimeWarpingClusteredFederatedGraphClassification.yaml`
- **Primary Source**: Han Xie, Jing Ma, Li Xiong, Carl Yang — *Federated Graph Classification over Non-IID Graphs* (`https://dblp.org/rec/conf/nips/XieMXY21`).

## Identity & Boundary Resolution

Introduced by Han Xie, Jing Ma, Li Xiong, and Carl Yang in 'Federated Graph Classification over Non-IID Graphs' (NeurIPS 2021, pages 18839-18852; arXiv:2106.13423). Extends vanilla GCFL (Section 4 of the same paper), which bi-partitions client clusters using single-round gradient cosine similarities and is vulnerable to fluctuating GNN gradient norms across rounds; distinct from Euclidean Clustered Federated Learning (CFL, Sattler et al. 2020), which does not track multi-round DTW gradient-norm sequences or analyze GNN Laplacian/feature perturbation bounds; and distinct from FedSage+ (Zhang et al. NeurIPS 2021), which addresses node classification on disjoint subgraphs with missing links.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 514 GCFL+ (Xie et al. 2021): delta_mean=0.0000<0.05, delta_max=0.5161>0.35, DTW_intra=3.30<<DTW_inter=26.62, prop4_1=7.6865e-04<=2.8106e+00
```
