# Discovery Report: Round 487 — MOCHA (Systems-Aware Primal-Dual Federated Multi-Task Learning)

- **Timestamp**: `2026-10-19T09:30:00Z`
- **Selected Concept**: `AIMech:MochaSystemsAwarePrimalDualFederatedMultiTaskLearning` (*MOCHA (Systems-Aware Primal-Dual Federated Multi-Task Learning)*)
- **Record Path**: `data/curated/MochaSystemsAwarePrimalDualFederatedMultiTaskLearning.yaml`
- **Primary Source**: Virginia Smith, Chao-Kai Chiang, Maziar Sanjabi, Ameet Talwalkar — *Federated Multi-Task Learning* (`https://arxiv.org/abs/1705.10467`).

## Identity & Boundary Resolution

Distinct from CoCoA (Jaggi et al. 2014; Ma et al. 2015), which solves single-model distributed ERM under a uniform fixed accuracy parameter theta across all workers and rounds without tolerating dropped nodes (theta_t^h = 1) or alternating multi-task relationship matrix updates Omega; and distinct from Ditto (AIMech:DittoFairAndRobustPersonalizedFederatedMultiTaskLearning, Li et al. 2021) and FedU (AIMech:FedUAndDFedULaplacianRegularizedFederatedMultiTaskLearning, Dinh et al. 2022), which operate in the primal parameter space to support nonconvex neural networks rather than solving dual block-quadratic subproblems G_t^{sigma'} with conjugate losses l_t^* and learned task-covariance matrices Omega.

## Constructed Boundary & Regime Verification

```text
[PASS] MOCHA boundary verification passed: sigma'=1.50, Theta_bar=0.55 < 1, dual_subopt=4.441e-16
```
