# Discovery Report: Round 493 — FedMGDA+ (Multi-Objective Pareto-Stationary Federated Learning with Normalized Multiple Gradient Descent)

- **Timestamp**: `2026-10-19T09:36:00Z`
- **Selected Concept**: `AIMech:FedMgdaPlusMultiObjectiveParetoStationaryFederatedOptimization` (*FedMGDA+ (Multi-Objective Pareto-Stationary Federated Learning with Normalized Multiple Gradient Descent)*)
- **Record Path**: `data/curated/FedMgdaPlusMultiObjectiveParetoStationaryFederatedOptimization.yaml`
- **Primary Source**: Zeou Hu, Kiarash Shaloudegi, Guojun Zhang, Yaoliang Yu — *Federated Learning Meets Multi-Objective Optimization* (`https://arxiv.org/abs/2006.11489`).

## Identity & Boundary Resolution

Distinct from Agnostic Federated Learning (AIMech:AgnosticFederatedLearningMinimaxDistributionallyRobustOptimization, Mohri et al. 2019) and q-Fair Federated Learning (AIMech:QFairFederatedLearningAlphaFairResourceAllocation, Li et al. 2020), which weight client updates by raw loss levels max_{lambda in Lambda} sum_i lambda_i f_i(w) or f_i(w)^q and are vulnerable to malicious clients inflating their loss by an additive constant or multiplicative scalar, whereas FedMGDA+ centers function values (Equation 19) and normalizes client pseudo-gradients g_bar_i = g_i / ||g_i||_2 before solving the epsilon-constrained Frank-Wolfe / minimum-norm quadratic program (Equation 25).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 493 FedMGDA+ (Hu et al. 2022): inner_c2_fedavg=-1.00 < 0 vs FedMGDA+ common descent (0.732 > 0, 0.414 > 0), scaling_attack_err=0.0e+00, prox_avg_err=0.0
```
