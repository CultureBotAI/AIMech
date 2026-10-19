# Discovery Report: Round 341 — Regularized Nonlinear Acceleration of Fixed-Point Iterations

- **Timestamp**: `2026-10-19T07:03:00Z`
- **Selected Concept**: `AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations` (*Regularized Nonlinear Acceleration of Fixed-Point Iterations*)
- **Record Path**: `data/curated/RegularizedNonlinearAccelerationOfFixedPointIterations.yaml`
- **Primary Source**: Damien Scieur, Alexandre d'Aspremont, Francis Bach — *Regularized Nonlinear Acceleration* (`https://doi.org/10.1007/s10107-018-1319-8`).

## Identity & Boundary Resolution

Distinct from Catalyst Universal Acceleration for First-Order Optimization (`AIMech:CatalystUniversalAccelerationForFirstOrderOptimization`), which modifies the optimization problem inside the loop by adding quadratic proximal terms (kappa/2)||x - y_{k-1}||^2, whereas RNA leaves the inner algorithm's iterate trajectory {x_0, ..., x_{k+1}} completely untouched and extrapolates it post-hoc via regularized residual Gram matrix inversion. Also distinct from Classical Anderson Acceleration / Minimal Polynomial Extrapolation (lambda = 0), which becomes catastrophically unstable under nonlinear perturbations due to exponential condition-number growth of the Krylov matrix R^T R (Section 3.1).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 341 Regularized Nonlinear Acceleration (Scieur, d'Aspremont, & Bach 2016): err_k3=1.0876e+00 <= 1.1234e+01, err_k4_CH=2.01e-10, eq23_err=2.20e-16, prop_a1_err=8.88e-16, norm_c_unreg=7.54 vs norm_c_reg=0.62
```
