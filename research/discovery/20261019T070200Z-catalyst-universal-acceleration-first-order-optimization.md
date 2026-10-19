# Discovery Report: Round 340 — Catalyst Universal Acceleration for First-Order Optimization

- **Timestamp**: `2026-10-19T07:02:00Z`
- **Selected Concept**: `AIMech:CatalystUniversalAccelerationForFirstOrderOptimization` (*Catalyst Universal Acceleration for First-Order Optimization*)
- **Record Path**: `data/curated/CatalystUniversalAccelerationForFirstOrderOptimization.yaml`
- **Primary Source**: Hongzhou Lin, Julien Mairal, Zaid Harchaoui — *A Universal Catalyst for First-Order Optimization* (`https://www.jmlr.org/papers/v18/17-748.html`).

## Identity & Boundary Resolution

Distinct from Regularized Nonlinear Acceleration of Fixed-Point Iterations (`AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations`), which extrapolates a post-hoc trajectory of fixed-point iterates via Tikhonov-regularized residual Gram inversion without modifying the inner objective, and from specific inner variance-reduced solvers that require custom algorithm-specific momentum couplings. Specifically captures the Catalyst black-box proximal wrapper G_k(x) = F(x) + (kappa/2)||x - y_{k-1}||^2, the canonical estimate-sequence recurrences (Equations 20-28), warm-start inner-loop complexity bounds (Proposition 3.2), and optimal smoothing parameter selection kappa = O(L / n) for finite-sum optimization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 340 Catalyst Acceleration (Lin, Mairal, & Harchaoui 2015): max_eq27_err=6.66e-16, max_eq28_err=8.08e-16, max_eq26_err=1.67e-16, F_cat=3.9897e-06 << F_unacc=2.5834e-03, F_stall=4.6619e-01
```
