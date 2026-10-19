# Discovery Report: Round 338 — Gradient Descent Avoidance of Strict Saddle Points via Stable Manifold Theorem

- **Timestamp**: `2026-10-19T07:00:00Z`
- **Selected Concept**: `AIMech:GradientDescentAvoidanceOfStrictSaddlePointsViaStableManifoldTheorem` (*Gradient Descent Avoidance of Strict Saddle Points via Stable Manifold Theorem*)
- **Record Path**: `data/curated/GradientDescentAvoidanceOfStrictSaddlePointsViaStableManifoldTheorem.yaml`
- **Primary Source**: Jason D. Lee, Max Simchowitz, Michael I. Jordan, Benjamin Recht — *Gradient Descent Converges to Minimizers* (`https://proceedings.mlr.press/v49/lee16.html`).

## Identity & Boundary Resolution

Distinct from Perturbed Gradient Descent for Escaping Saddle Points in Hessian-Lipschitz Optimization (`AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization`), which modifies gradient descent by injecting uniform ball perturbations to achieve polynomial tilde{O}(1/epsilon^2) worst-case runtime, whereas Lee et al. (2016) analyze unmodified deterministic gradient descent with random initialization via the diffeomorphic Center-Stable Manifold Theorem. Also captures the explicit 2D degenerate-saddle counterexample f(x,y) = x^2/2 + y^4/4 - y^3/3 where an open plot of initial conditions (0,1) x (-2,0) converges to a non-strict saddle point.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 338 Stable Manifold GD (Lee et al. 2016): prox_inv_err=1.11e-16, min_det_dg=0.2688, escaped=40/40, nondeg_err=1.11e-16, deg_sublinear_err=0.1085
```
