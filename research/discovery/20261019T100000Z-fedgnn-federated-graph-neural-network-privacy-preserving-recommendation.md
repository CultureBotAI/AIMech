# Discovery Report: Round 517 — FedGNN (Federated Graph Neural Network for Privacy-Preserving Recommendation)

- **Timestamp**: `2026-10-19T10:00:00Z`
- **Selected Concept**: `AIMech:FedGnnFederatedGraphNeuralNetworkForPrivacyPreservingRecommendation` (*FedGNN (Federated Graph Neural Network for Privacy-Preserving Recommendation)*)
- **Record Path**: `data/curated/FedGnnFederatedGraphNeuralNetworkForPrivacyPreservingRecommendation.yaml`
- **Primary Source**: Chuhan Wu, Fangzhao Wu, Yang Cao, Yongfeng Huang, Xing Xie — *FedGNN: Federated Graph Neural Network for Privacy-Preserving Recommendation* (`https://dblp.org/rec/journals/corr/abs-2102-04925`).

## Identity & Boundary Resolution

Introduced by Chuhan Wu, Fangzhao Wu, Yang Cao, Yongfeng Huang, and Xing Xie in 'FedGNN: Federated Graph Neural Network for Privacy-Preserving Recommendation' (arXiv:2102.04925, DBLP:journals/corr/abs-2102-04925). Distinct from FCF (Federated Collaborative Filtering, Ammad-ud-din et al. 2019), which models only first-order matrix factorization interactions and exposes interacted item IDs via non-zero item-embedding gradients; and distinct from FedSage+ (Zhang et al. NeurIPS 2021), which trains a local missing-neighbor generator (NeighGen) across multi-node subgraphs rather than expanding user-centric bipartite recommendation graphs via encrypted item matching and pseudo-item LDP gradients.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 517 FedGNN (Wu et al. 2021): pseudo_mean_diff=0.0034, anonymity_deg=10.43, eps_LDP=1.00, matched_neighbors=[1]
```
