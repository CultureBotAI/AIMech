# Discovery Report: Round 439 — FedPara and pFedPara (Low-Rank Hadamard Product Parameterization for Federated Learning)

- **Timestamp**: `2026-10-19T08:42:00Z`
- **Selected Concept**: `AIMech:FedParaAndPFedParaLowRankHadamardProductParameterization` (*FedPara and pFedPara (Low-Rank Hadamard Product Parameterization for Federated Learning)*)
- **Record Path**: `data/curated/FedParaAndPFedParaLowRankHadamardProductParameterization.yaml`
- **Primary Source**: Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh — *FedPara: Low-Rank Hadamard Product for Communication-Efficient Federated Learning* (`https://openreview.net/forum?id=d71n4ftoCBy`).

## Identity & Boundary Resolution

Distinct from PowerSGD (AIMech:PowerSgdLowRankGradientCompressionWithErrorFeedback, Vogels et al. 2019), which compresses full-model gradients via power-iteration low-rank approximations with error feedback rather than reparameterizing the model weights via an unconstrained-rank Hadamard product of low-rank factors, and from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which splits personalization by network depth (shared body vs local head) rather than intra-layer Hadamard decomposition W_1 odot (W_2 + 1).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 439 FedPara & pFedPara (Hyeon-Woo et al. 2022): rank(W1)=4, rank(W2)=4 -> rank(W1 o W2)=16 (full rank) vs equal-budget low-rank=8, params=256
```
