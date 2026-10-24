# Discovery Report: Round 469 — FedDisco (Federated Learning with Discrepancy-Aware Collaboration)

- **Timestamp**: `2026-10-19T09:12:00Z`
- **Selected Concept**: `AIMech:FedDiscoFederatedLearningWithDiscrepancyAwareCollaboration` (*FedDisco (Federated Learning with Discrepancy-Aware Collaboration)*)
- **Record Path**: `data/curated/FedDiscoFederatedLearningWithDiscrepancyAwareCollaboration.yaml`
- **Primary Source**: Rui Ye, Mingkai Xu, Jianyu Wang, Chenxin Xu, Siheng Chen, Yanfeng Wang — *FedDisco: Federated Learning with Discrepancy-Aware Collaboration* (`https://proceedings.mlr.press/v202/ye23b.html`).

## Identity & Boundary Resolution

Distinct from FedNova (AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization, Wang et al. 2020), which normalizes client updates by their effective number of local SGD steps tau_eff rather than category-distribution discrepancy d_k = ||r_k - u||_2; and distinct from Agnostic Federated Learning (AIMech:AgnosticFederatedLearning, Mohri et al. 2019), which solves a minimax saddle-point problem max_lambda min_w sum_k lambda_k F_k(w) assigning larger weights to high-loss clients rather than down-weighting category-skewed clients via ReLU(n_k - a d_k + b).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 469 FedDisco verified: p_biased=0.1311 < p_unbiased=0.3444, Thm4.5_bound=3.957440->3.944062
```
