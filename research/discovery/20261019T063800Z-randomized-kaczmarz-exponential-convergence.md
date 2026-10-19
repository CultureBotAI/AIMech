# Discovery Report: Round 323 — Randomized Kaczmarz Algorithm with Exponential Convergence

- **Timestamp**: `2026-10-19T06:38:00Z`
- **Selected Concept**: `AIMech:RandomizedKaczmarzAlgorithmWithExponentialConvergence` (*Randomized Kaczmarz Algorithm with Exponential Convergence*)
- **Record Path**: `data/curated/RandomizedKaczmarzAlgorithmWithExponentialConvergence.yaml`
- **Primary Source**: Thomas Strohmer, Roman Vershynin — *A randomized Kaczmarz algorithm with exponential convergence* (`https://doi.org/10.1007/s00041-008-9030-4`).

## Identity & Boundary Resolution

Distinct from finite-sum variance-reduced gradient methods such as SVRG, SAGA, and SDCA, and from deterministic cyclic Kaczmarz / Algebraic Reconstruction Technique (ART). Specifically captures the Strohmer-Vershynin (2009) squared-row-norm sampling distribution p_j = ||a_j||_2^2 / ||A||_F^2 (Algorithm 1, Equation 4), the exact Demmel scaled condition number contraction factor 1 - kappa(A)^{-2} (Theorem 2), the tightness of this rate on circulant/parseval ensembles and high- probability lower bounds (Section 3.2 and Theorem 3), and the invariance to poorly scaled rows demonstrated against uniform row sampling (Section 2.2).

## Constructed Boundary & Regime Verification

```text
{"concept": "RandomizedKaczmarzAlgorithmWithExponentialConvergence", "demmel_scaled_kappa_sq": 252.696009, "one_step_expected_err_sq": 12.938497, "one_step_theorem2_bound": 13.944597, "rownorm_vs_uniform_1step_err": [9.9e-07, 0.99], "section32_tight_trajectory": [0.833333, 0.694444, 0.578704, 0.482253, 0.401878], "status": "VERIFIED", "theorem3_lower_bounds": [0.666667, 0.333333, 0.0, 0.0, 0.0]}
```
