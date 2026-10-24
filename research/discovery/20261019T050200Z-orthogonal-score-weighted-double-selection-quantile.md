# Discovery Report: Round 275 — Orthogonal Score and Weighted Double-Selection Post-Selection Inference in High-Dimensional Quantile Regression

- **Timestamp**: `2026-10-19T05:02:00Z`
- **Selected Concept**: `AIMech:OrthogonalScoreAndWeightedDoubleSelectionPostSelectionInferenceInHighDimensionalQuantileRegression` (*Orthogonal Score and Weighted Double-Selection Post-Selection Inference in High-Dimensional Quantile Regression*)
- **Record Path**: `data/curated/OrthogonalScoreAndWeightedDoubleSelectionPostSelectionInferenceInHighDimensionalQuantileRegression.yaml`
- **Primary Source**: Alexandre Belloni, Victor Chernozhukov, and Kengo Kato (2019), *Valid Post-Selection Inference in High-Dimensional Approximately Sparse Quantile Regression Models*, *Journal of the American Statistical Association* 114(526):749–768 (`DOI:10.1080/01621459.2018.1442339`, `arXiv:1312.7186v4`).

## Identity & Boundary Resolution

`AIMech:OrthogonalScoreAndWeightedDoubleSelectionPostSelectionInferenceInHighDimensionalQuantileRegression` was checked against all 442 pinned AIO concepts and 669 maintained AIMech concepts:

1. **`AIMech:L1PenalizedAndPostPenalizedQuantileRegressionProcessInHighDimensionalSparseModels`**: Single-equation $\ell_1$-QR process estimation rates vs. Neyman-orthogonal score and $\widehat{f}_i$-weighted double-selection quantile inference without beta-min conditions.
2. **`AIMech:PostDoubleSelectionInferenceForHighDimensionalTreatmentEffects`**: Unweighted least-squares double selection for conditional means vs. conditional-density-weighted auxiliary Lasso and weighted quantile refitting.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:OrthogonalScoreAndWeightedDoubleSelectionPostSelectionInferenceInHighDimensionalQuantileRegression",
  "source": "Belloni, Chernozhukov, & Kato (2019), JASA 114(526):749-768, arXiv:1312.7186v4",
  "results": {
    "neyman_orthogonality_and_density_estimation": {
      "gateaux_derivative_beta_weighted": -1.2915928533131522e-17,
      "gateaux_derivative_beta_unweighted_without_f_ratio": -0.072016,
      "asymptotic_variance_minimax_weighted": 2.38363,
      "asymptotic_variance_unweighted": 3.436865,
      "efficiency_gain_ratio": 1.441862,
      "density_estimator_bias_h005": {
        "f_true": 0.21,
        "f_hat_eq215_order2": 0.20851879,
        "f_hat_eq216_printed_3_4": 0.17989233,
        "f_hat_eq216_corrected_2_3_order4": 0.21010203,
        "abs_err_eq215": 0.00148121,
        "abs_err_eq216_corrected": 0.00010203,
        "error_reduction_factor": 14.52
      }
    },
    "algorithms_2_1_and_2_2_verification": {
      "n": 300,
      "p": 40,
      "lambda_lasso": 175.3937,
      "lambda_tau": 43.8484,
      "S_y_selected": [
        0
      ],
      "S_d_selected": [
        0,
        1,
        2,
        3,
        4,
        5
      ],
      "T_check_union": [
        0,
        1,
        2,
        3,
        4,
        5
      ],
      "alpha_true": 0.5,
      "alpha_naive_post_selection": 0.70639,
      "alpha_weighted_double_selection": 0.365247,
      "alpha_orthogonal_score": 0.364747,
      "sqrt_n_os_ds_diff": 0.00866,
      "sigma_1n": 1.412116,
      "sigma_3n": 1.412116,
      "ci_95_orthogonal_score": [
        0.204954,
        0.52454
      ],
      "os_covers_true_alpha": true
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across two regimes: (1) Under heteroscedastic conditional quantile errors, the density-weighted instrument v_i = f_i (d_i - x_i' theta_tau) achieves exact Neyman orthogonality |E[f_i v_i x_i]| = 1.29e-17 and lowers asymptotic variance from 3.4369 (unweighted) to 2.3836 (1.44x efficiency gain), while Taylor verification of Eq. (2.16) at h = 0.05 confirms that the printed coefficient 3/4 converges to (6/7)*f_true = 0.1799 whereas the corrected Richardson coefficient 2/3 achieves f_hat = 0.210102 vs. f_true = 0.210000 (14.52x smaller error than second-order Eq. 2.15); and (2) on an approximately sparse median regression design (n = 300, p = 40, true alpha = 0.5) without beta-min separation, Naive Post-Selection suffers omitted-variable bias (alpha_naive = 0.7064), whereas Weighted Double Selection (alpha_DS = 0.3652) and Orthogonal Score (alpha_OS = 0.3647) satisfy Theorem 1 first-order equivalence sqrt(n)|alpha_OS - alpha_DS| = 0.00866 << 0.15 with 95% confidence interval [0.2050, 0.5245] covering alpha_true = 0.5.
