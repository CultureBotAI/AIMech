# Discovery Report: Round 485 — pFedLA and HeurpFedLA (Layer-Wised Hypernetwork Model Aggregation for Personalized Federated Learning)

- **Timestamp**: `2026-10-19T09:28:00Z`
- **Selected Concept**: `AIMech:PFedLaAndHeurPFedLaLayerWisedHypernetworkModelAggregationForPersonalizedFederatedLearning` (*pFedLA and HeurpFedLA (Layer-Wised Hypernetwork Model Aggregation for Personalized Federated Learning)*)
- **Record Path**: `data/curated/PFedLaAndHeurPFedLaLayerWisedHypernetworkModelAggregationForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Xiaosong Ma, Jie Zhang, Song Guo, Wenchao Xu — *Layer-wised Model Aggregation for Personalized Federated Learning* (`https://arxiv.org/abs/2205.03993`).

## Identity & Boundary Resolution

Distinct from pFedHN (AIMech:PFedHnPersonalizedFederatedHypernetworks, Shamsian et al. 2021), where a single hypernetwork directly generates the target neural network's raw weight tensors theta_i = HN(v_i; psi) rather than generating an N x n cross-client layer-wise convex combination matrix alpha_i = HN_i(v_i; psi_i) to aggregate clients' locally trained layer parameters {theta_j^{ln}}; and distinct from FedFomo (AIMech:FedFomoFirstOrderModelOptimizationForPersonalizedFederatedLearning, Zhang et al. 2021) and FedAMP (AIMech:FedAmpFederatedAttentiveMessagePassingForPersonalizedCrossSiloFederatedLearning, Huang et al. 2021), which compute whole-model scalar aggregation weights using parameter/loss distances rather than hypernetwork-parameterized layer-granular aggregation matrices.

## Constructed Boundary & Regime Verification

```text
[PASS] pFedLA/HeurpFedLA boundary verification passed: err_pFedLA=0.11688 < err_modelwise=0.57365, chain_err=1.075e-09, self_weights=0.500<0.802
```
