# Discovery Report: Round 352 — Perturbed Accelerated Gradient Descent with Negative-Curvature Reset for Escaping Saddle Points

- **Timestamp**: `2026-10-19T07:15:00Z`
- **Selected Concept**: `AIMech:PerturbedAcceleratedGradientDescentWithNegativeCurvatureResetForSaddlePointEscape` (*Perturbed Accelerated Gradient Descent with Negative-Curvature Reset for Escaping Saddle Points*)
- **Record Path**: `data/curated/PerturbedAcceleratedGradientDescentWithNegativeCurvatureResetForSaddlePointEscape.yaml`
- **Primary Source**: Chi Jin, Praneeth Netrapalli, Michael I. Jordan — *Accelerated Gradient Descent Escapes Saddle Points Faster than Gradient Descent* (`https://proceedings.mlr.press/v75/jin18a.html`).

## Identity & Boundary Resolution

Distinct from Perturbed Gradient Descent for Escaping Saddle Points in Hessian-Lipschitz Optimization (`AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization`), which uses unaccelerated gradient descent (theta = 1) and requires O~(epsilon^{-2}) iterations rather than O~(epsilon^{-7/4}) via Hamiltonian momentum accumulation and NCE resets, and from Accelerated Gradient and Negative Curvature Exploitation for Non-Convex Optimization (`AIMech:AcceleratedGradientAndNegativeCurvatureExploitationForNonConvexOptimization`), which is a nested-loop algorithm combining Lanczos negative-curvature search with proximal regularized subproblems rather than a single-loop purely gradient-based perturbed AGD method.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 352 Perturbed AGD (Jin et al. 2018): E0=3.6728 < E1_agd=5.0000 (NCE E1=-2.5000), max_lemma4_viol=-1.92e-06, mu1_agd=1.13403 > mu_gd=1.02500, final_x0=0.1517
```
