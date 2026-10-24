# Discovery Report: Round 387 — FedDyn Dynamic Regularization for Federated Learning

- **Timestamp**: `2026-10-19T07:50:00Z`
- **Selected Concept**: `AIMech:FedDynDynamicRegularizationForFederatedLearning` (*FedDyn Dynamic Regularization for Federated Learning*)
- **Record Path**: `data/curated/FedDynDynamicRegularizationForFederatedLearning.yaml`
- **Primary Source**: Durmus Alp Emre Acar, Yue Zhao, Ramon Matas Navarro, Matthew Mattina, Paul N. Whatmough, Venkatesh Saligrama — *Federated Learning Based on Dynamic Regularization* (`https://openreview.net/forum?id=B7v4QMR6Z9w`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization, which penalizes (mu/2)||theta - theta^{t-1}||^2 without the dynamic linear gradient-alignment term -<nabla L_k(theta_k^{t-1}), theta>, so client minimizers do not align with theta* when nabla L_k(theta*) != 0), from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which doubles communication payload by transmitting control variate updates Delta c_i alongside model parameters), and from FedNova (AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization). No pinned AIO class covers FedDyn.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 387 FedDyn (Acar et al. 2021): max_h_inv_err=5.80e-15, partial_part_err=2.22e-15, client_drift=7.40e-15, feddyn_asym_err=1.96e-16 vs fedprox_bias=0.1765
```
