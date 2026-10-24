# Discovery Report: Round 337 — Perturbed Gradient Descent for Escaping Saddle Points in Hessian-Lipschitz Optimization

- **Timestamp**: `2026-10-19T06:59:00Z`
- **Selected Concept**: `AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization` (*Perturbed Gradient Descent for Escaping Saddle Points in Hessian-Lipschitz Optimization*)
- **Record Path**: `data/curated/PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization.yaml`
- **Primary Source**: Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M. Kakade, Michael I. Jordan — *How to Escape Saddle Points Efficiently* (`https://proceedings.mlr.press/v70/jin17a.html`).

## Identity & Boundary Resolution

Distinct from Strict-Saddle Property and Noisy Stochastic Gradient Saddle Escaping for Orthogonal Tensor Decomposition (`AIMech:StrictSaddlePropertyAndNoisyStochasticGradientSaddleEscapingForOrthogonalTensorDecomposition`), which injects noise at every stochastic step with poly(d / epsilon) iteration dependence, and from Gradient Descent Avoidance of Strict Saddle Points via Stable Manifold Theorem (`AIMech:GradientDescentAvoidanceOfStrictSaddlePointsViaStableManifoldTheorem`), which establishes asymptotic measure-zero avoidance without quantitative polynomial iteration bounds. Specifically captures the Jin et al. (2017) thresholded ball-perturbation rule (Algorithm 1), the two-point coupling width bound for the thin-pancake stuck region (Lemmas 14-17), the dimension-free log^4(d)/epsilon^2 rate (Theorem 3), and the global strict-saddle/regularity decomposition for symmetric low-rank matrix factorization (Lemmas 6-7).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 337 Perturbed Gradient Descent (Jin et al. 2017): lemma7_hess_id_err=7.11e-15, rayleigh_zero=-6.6667, f_stuck=8.0000, f_escaped=3.32e-26, max_vol_ratio_over_delta=0.4502
```
