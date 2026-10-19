# Discovery Report: Round 287 — De-biased Noisy Matrix Completion and De-shrunken Low-Rank Factor Uncertainty Quantification

- **Timestamp**: `2026-10-19T05:26:00Z`
- **Selected Concept**: `AIMech:DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification` (*De-biased Noisy Matrix Completion and De-shrunken Low-Rank Factor Uncertainty Quantification*)
- **Record Path**: `data/curated/DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification.yaml`
- **Primary Source**: Yuxin Chen, Jianqing Fan, Cong Ma, Yuling Yan — *Inference and Uncertainty Quantification for Noisy Matrix Completion* (`https://doi.org/10.1073/pnas.1910053116`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 681 maintained AIMech concepts. Distinct from `AIMech:ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis` (Ma, Wang, Chi, & Chen 2020, which analyzes order-wise convergence of unregularized nonconvex gradient descent without de-biasing, distributional normality, or confidence intervals) and from `AIMech:DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference` (Ning & Liu 2017, which de-biases sparse $\ell_1$-penalized M-estimators via score projections rather than rank-$r$ singular value projection $\mathcal{P}_{\text{rank-}r}[\boldsymbol{Z} - p^{-1}\mathcal{P}_\Omega(\boldsymbol{Z}-\boldsymbol{M})]$ and spectral factor de-shrinking $(\boldsymbol{I}_r + \frac{\lambda}{p}(\boldsymbol{X}^\top\boldsymbol{X})^{-1})^{1/2}$).

## Constructed Boundary & Regime Verification

```text
{
  "n": 16,
  "p_obs": 0.75,
  "sigma": 0.04,
  "lambda_reg": 0.221703,
  "eq_d4_deshrinking_identity_max_err": 1.3322676295501878e-15,
  "lemma3_svp_vs_factor_max_rel_diff": 9.8e-05,
  "mean_frob_sq_shrunken": 0.152817,
  "mean_frob_sq_debiased": 0.071964,
  "oracle_2n_r_sigma2_over_p": 0.068267,
  "empirical_95_ci_coverage_debiased": 0.9452,
  "empirical_95_ci_coverage_shrunken_uncorrected": 0.7897,
  "max_plugin_variance_rel_err": 0.2691
}
```
