# Discovery Report: Round 465 — FedAMP (Federated Attentive Message Passing for Personalized Cross-Silo Federated Learning)

- **Timestamp**: `2026-10-19T09:08:00Z`
- **Selected Concept**: `AIMech:FedAmpFederatedAttentiveMessagePassingForPersonalizedCrossSiloFederatedLearning` (*FedAMP (Federated Attentive Message Passing for Personalized Cross-Silo Federated Learning)*)
- **Record Path**: `data/curated/FedAmpFederatedAttentiveMessagePassingForPersonalizedCrossSiloFederatedLearning.yaml`
- **Primary Source**: Yutao Huang, Lingyang Chu, Zirui Zhou, Lanjun Wang, Jiangchuan Liu, Jian Pei, Yong Zhang — *Personalized Cross-Silo Federated Learning on Non-IID Data* (`https://doi.org/10.1609/aaai.v35i9.16960`).

## Identity & Boundary Resolution

Distinct from pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, T. Dinh et al. 2020), which penalizes distance to a single shared global model ||w_i - w||^2 rather than pairwise concave attention functions sum_{i < j} A(||w_i - w_j||^2) producing personalized cloud models u_i^k; and distinct from FedFomo (AIMech:FedFomoFirstOrderModelOptimizationForPersonalizedFederatedLearning, Zhang et al. 2021), which computes weights on the client side using local validation loss evaluations of downloaded peer models rather than server-side attentive message passing.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 465 FedAMP verified: G(W)=5.2885->4.0300, xi_01=0.1237>>xi_02=0.00000, heur_xi_01=0.4975
```
