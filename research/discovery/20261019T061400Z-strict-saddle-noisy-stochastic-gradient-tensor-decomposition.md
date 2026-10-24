# Discovery Report: Round 311 — Strict Saddle Property and Noisy Stochastic Gradient Saddle Escaping for Orthogonal Tensor Decomposition

- **Timestamp**: `2026-10-19T06:14:00Z`
- **Selected Concept**: `AIMech:StrictSaddlePropertyAndNoisyStochasticGradientSaddleEscapingForOrthogonalTensorDecomposition` (*Strict Saddle Property and Noisy Stochastic Gradient Saddle Escaping for Orthogonal Tensor Decomposition*)
- **Record Path**: `data/curated/StrictSaddlePropertyAndNoisyStochasticGradientSaddleEscapingForOrthogonalTensorDecomposition.yaml`
- **Primary Source**: Rong Ge, Furong Huang, Chi Jin, Yang Yuan — *Escaping From Saddle Points — Online Stochastic Gradient for Tensor Decomposition* (`https://doi.org/10.48550/arXiv.1503.02101`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 705 maintained AIMech concepts. Distinct from `AIMech:OrthogonalTensorDecompositionAndRobustTensorPowerMethodForLatentVariableModels` (which relies on sequential tensor power iterations and deflation of an explicit empirical $d\times d\times d$ tensor) and `AIMech:NonconvexMatrixCompletionLandscapeWithoutSpuriousLocalMinima` (which analyzes Burer-Monteiro matrix completion rather than the $(\theta,\gamma,\zeta)$-strict saddle framework, Noisy SGD negative-curvature amplification, and deflation-free fourth-order cross-correlation tensor objectives on $\prod_{i=1}^d \mathbb{S}^{d-1}$).

## Constructed Boundary & Regime Verification

```text
{"concept": "StrictSaddlePropertyAndNoisyStochasticGradientSaddleEscapingForOrthogonalTensorDecomposition", "local_min_tangent_quadratic_curvature": 2.0, "noiseless_gd_trapped_obj": 0.5, "noisy_psgd_escaped_final_obj": 1.3910297234477976e-59, "saddle_stationary_grad_norm": 3.14018491736755e-16, "saddle_tangent_quadratic_curvature": -2.0, "status": "VERIFIED"}
```
