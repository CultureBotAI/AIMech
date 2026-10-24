# Discovery Report: Round 473 — FedPer (Federated Learning with Personalization Layers)

- **Timestamp**: `2026-10-19T09:16:00Z`
- **Selected Concept**: `AIMech:FedPerFederatedLearningWithPersonalizationLayers` (*FedPer (Federated Learning with Personalization Layers)*)
- **Record Path**: `data/curated/FedPerFederatedLearningWithPersonalizationLayers.yaml`
- **Primary Source**: Manoj Ghuhan Arivazhagan, Vinay Aggarwal, Aaditya Kumar Singh, Sunav Choudhary — *Federated Learning with Personalization Layers* (`https://arxiv.org/abs/1912.00818`).

## Identity & Boundary Resolution

Distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which alternates separate inner head-only optimization epochs and representation-only optimization steps within each round rather than jointly updating (W_{B,j}, W_{P_j}) simultaneously via coupled SGD steps (Algorithm 1, Line 5); and distinct from FedBABU (AIMech:FedBabuFederatedLearningWithOnlyBodyAggregationAndBodyUpdate, Oh et al. 2022), which freezes a shared random head (alpha_h = 0) during federated representation training.

## Constructed Boundary & Regime Verification

```text
[PASS] FedPer boundary verification passed: L_PR(FedPer)=3.1949e-05 << L_PR(FedAvg)=0.6500
```
