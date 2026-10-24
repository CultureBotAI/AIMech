# Discovery Report: Round 513 — FedSage+ (Subgraph Federated Learning with Missing Neighbor Generation)

- **Timestamp**: `2026-10-19T09:56:00Z`
- **Selected Concept**: `AIMech:FedSagePlusSubgraphFederatedLearningWithMissingNeighborGeneration` (*FedSage+ (Subgraph Federated Learning with Missing Neighbor Generation)*)
- **Record Path**: `data/curated/FedSagePlusSubgraphFederatedLearningWithMissingNeighborGeneration.yaml`
- **Primary Source**: Ke Zhang, Carl Yang, Xiaoxiao Li, Lichao Sun, Siu Ming Yiu — *Subgraph Federated Learning with Missing Neighbor Generation* (`https://dblp.org/rec/conf/nips/ZhangYLSY21`).

## Identity & Boundary Resolution

Introduced by Ke Zhang, Carl Yang, Xiaoxiao Li, Lichao Sun, and Siu-Ming Yiu in 'Subgraph Federated Learning with Missing Neighbor Generation' (NeurIPS 2021, pages 6671-6682; arXiv:2106.13430). Distinct from vanilla FedSage (Section 3.2 of the same paper), which applies FedAvg directly to GraphSage on unmended subgraphs without missing neighbor generation; distinct from LocSage+, which trains NeighGen and GraphSage purely locally without cross-subgraph gradient feedback (alpha = 0 in Eq. 6); and distinct from GCFL+ (Xie et al. NeurIPS 2021), which clusters clients for graph-level classification rather than mending cut cross-subgraph edges for node classification.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 513 FedSage+ (Zhang et al. 2021): dGen_smoothL1=0.0487, fGen_L2_gap=0.1493 << local_only_gap=1.6332, GNTK_bound_reduction=2.236x
```
