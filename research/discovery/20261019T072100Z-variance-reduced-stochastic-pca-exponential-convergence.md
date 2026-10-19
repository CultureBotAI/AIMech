# Discovery Report: Round 358 — Variance-Reduced Stochastic PCA and SVD with Exponential Convergence (VR-PCA)

- **Timestamp**: `2026-10-19T07:21:00Z`
- **Selected Concept**: `AIMech:VarianceReducedStochasticPCAWithExponentialConvergence` (*Variance-Reduced Stochastic PCA and SVD with Exponential Convergence (VR-PCA)*)
- **Record Path**: `data/curated/VarianceReducedStochasticPCAWithExponentialConvergence.yaml`
- **Primary Source**: Ohad Shamir — *A Stochastic PCA and SVD Algorithm with an Exponential Convergence Rate* (`https://proceedings.mlr.press/v37/shamir15.html`).

## Identity & Boundary Resolution

Distinct from generic PrincipalComponentAnalysis (AIO:PrincipalComponentAnalysis) and DimensionalityReduction (AIO:DimensionalityReduction), which do not specify SVRG-style variance-reduced stochastic power updates on the unit sphere. Distinct from AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm (Round 357), which is a single-pass streaming Oja algorithm with decaying step size eta_t = O(1/t) and sub-exponential O(1/n) convergence rate due to non-vanishing stochastic update variance. Also distinct from AIMech:ShiftAndInvertPreconditioningForFasterEigenvectorComputation (Round 354), which applies SVRG to solve shifted linear systems (lambda I - A)x = b rather than directly iterating normalized variance-reduced power steps on the non-convex unit-sphere Rayleigh quotient.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 358 VR-PCA (Shamir 2015): fast_diff=3.33e-16, b0=0.6331->b_vr=2.22e-16<<b_oja=7.3890e-02, var_first=7.707e-04->var_last=0.000e+00 (s1=0.8888)
```
