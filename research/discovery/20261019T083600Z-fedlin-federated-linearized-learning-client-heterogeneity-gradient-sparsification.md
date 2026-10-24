# Discovery Report: Round 433 — FedLin (Federated Linearized Learning with Client Heterogeneity and Gradient Sparsification)

- **Timestamp**: `2026-10-19T08:36:00Z`
- **Selected Concept**: `AIMech:FedLinFederatedLinearizedLearningWithClientHeterogeneityAndGradientSparsification` (*FedLin (Federated Linearized Learning with Client Heterogeneity and Gradient Sparsification)*)
- **Record Path**: `data/curated/FedLinFederatedLinearizedLearningWithClientHeterogeneityAndGradientSparsification.yaml`
- **Primary Source**: Aritra Mitra, Rayana H. Jaafar, George J. Pappas, Hamed Hassani — *Linear Convergence in Federated Learning: Tackling Client Heterogeneity and Sparse Gradients* (`https://proceedings.neurips.cc/paper/2021/hash/7a6bda9ad6ffdac035c752743b7e9d0f-Abstract.html`).

## Identity & Boundary Resolution

Distinct from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, Karimireddy et al. 2020), which uses stale control variates c_i from round t-1 that violate the exact single-step fixed-point property at x^* and lacks client- inversely scaled step-sizes eta_i = bar_eta / tau_i for arbitrary systems heterogeneity, and from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization) and FedNova (AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization), which Propositions 1-2 prove converge to distorted surrogate objectives under constant step-sizes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 433 FedLin (Mitra et al. 2021): fedprox_bias=0.2813, fednova_bias=0.5747, fedlin_err=2.53e-16, srv_sparse_err_sq=3.57e-32
```
