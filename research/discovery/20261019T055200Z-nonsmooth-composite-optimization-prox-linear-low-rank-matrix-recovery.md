# Discovery Report: Round 300 — Nonsmooth Convex-Composite Optimization, Weak Convexity, Sharpness, and Prox-Linear Low-Rank Matrix Recovery

- **Timestamp**: `2026-10-19T05:52:00Z`
- **Selected Concept**: `AIMech:NonsmoothCompositeOptimizationAndProxLinearLowRankMatrixRecovery` (*Nonsmooth Convex-Composite Optimization, Weak Convexity, Sharpness, and Prox-Linear Low-Rank Matrix Recovery*)
- **Record Path**: `data/curated/NonsmoothCompositeOptimizationAndProxLinearLowRankMatrixRecovery.yaml`
- **Primary Source**: Vasileios Charisopoulos, Yudong Chen, Damek Davis, Mateo Diaz, Lijun Ding, Dmitriy Drusvyatskiy — *Low-Rank Matrix Recovery with Composite Optimization: Good Conditioning and Rapid Convergence* (`https://doi.org/10.1007/s10208-020-09490-9`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 694 maintained AIMech concepts. Distinct from `AIMech:TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations` (Wang, Giannakis, & Eldar 2018, which minimizes a smooth-after-truncation squared amplitude loss for rank-1 vectors without outlier robustness or prox-linear quadratic convergence) and from `AIMech:ScaledGradientDescentForIllConditionedLowRankMatrixEstimation` (Tong, Ma, & Chi 2021, which preconditions smooth differentiable losses rather than proving weak convexity and sharpness of nonsmooth $\ell_1$-composite objectives $f(\boldsymbol{X}) = \|\mathcal{A}(\boldsymbol{X}) - \boldsymbol{b}\|_1$).

## Constructed Boundary & Regime Verification

```text
{"concept": "NonsmoothCompositeOptimizationAndProxLinearLowRankMatrixRecovery", "dimension_d": 6, "initial_distance": 0.612372, "measurements_m": 60, "min_empirical_sharpness_ratio": 1.352929, "outlier_fraction_p_fail": 0.25, "polyak_subgradient_final_dist": 7.043024209661601e-14, "prox_linear_error_trajectory": [0.48989794855664, 0.05035997855491, 0.00055443589206, 6.764347e-08, 7.2e-13, 7.2e-13], "status": "VERIFIED", "taylor_model_diff": 0.15803361, "taylor_quad_upper_bound": 0.24845449}
```
