# Discovery Report: Round 294 — Convex and Nonconvex Optimization Bridging for Robust PCA under Noise, Outliers, and Missing Data

- **Timestamp**: `2026-10-19T05:40:00Z`
- **Selected Concept**: `AIMech:ConvexAndNonconvexBridgingForRobustPCAUnderNoiseOutliersAndMissingData` (*Convex and Nonconvex Optimization Bridging for Robust PCA under Noise, Outliers, and Missing Data*)
- **Record Path**: `data/curated/ConvexAndNonconvexBridgingForRobustPCAUnderNoiseOutliersAndMissingData.yaml`
- **Primary Source**: Yuxin Chen, Jianqing Fan, Cong Ma, Yuling Yan — *Bridging Convex and Nonconvex Optimization in Robust PCA: Noise, Outliers, and Missing Data* (`https://doi.org/10.1214/21-AOS2066`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 688 maintained AIMech concepts. Distinct from `AIMech:DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification` (Chen, Fan, Ma, & Yan 2019, which studies outlier-free matrix completion with $\boldsymbol{S}^\star = \boldsymbol{0}$) and from `AIMech:ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis` (Ma, Wang, Chi, & Chen 2020, which analyzes unregularized nonconvex algorithms in noiseless/Gaussian models without bridging to the global optimality and rank-$r$ exactness of convex nuclear-norm plus $\ell_1$-penalized Robust PCA).

## Constructed Boundary & Regime Verification

```text
{
  "matrix_dim_n": 14,
  "lambda_reg": 1.2,
  "tau_reg": 0.35,
  "dual_certificate_residual_perp_eigenvalue": 0.63318,
  "kkt_stationarity_grad_norm": 0.0,
  "convex_nonconvex_bridge_frob_distance": 0.0,
  "entrywise_linf_error": 0.14601,
  "frobenius_error": 1.42333,
  "exact_outlier_support_recovered": true
}
```
