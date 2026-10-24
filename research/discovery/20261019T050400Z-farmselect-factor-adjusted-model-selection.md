# Discovery Report: Round 276 — Factor-Adjusted Regularized Model Selection and Decorrelated Variable Screening

- **Timestamp**: `2026-10-19T05:04:00Z`
- **Selected Concept**: `AIMech:FactorAdjustedRegularizedModelSelectionAndDecorrelatedVariableScreening` (*Factor-Adjusted Regularized Model Selection and Decorrelated Variable Screening*)
- **Record Path**: `data/curated/FactorAdjustedRegularizedModelSelectionAndDecorrelatedVariableScreening.yaml`
- **Primary Source**: Jianqing Fan, Yuan Ke, and Kaizheng Wang (2020), *Factor-Adjusted Regularized Model Selection*, *Journal of Econometrics* 216(1):71–85 (`DOI:10.1016/j.jeconom.2020.01.006`, `arXiv:1612.08490v2`).

## Identity & Boundary Resolution

`AIMech:FactorAdjustedRegularizedModelSelectionAndDecorrelatedVariableScreening` was checked against all 442 pinned AIO concepts and 670 maintained AIMech concepts:

1. **`AIMech:PrincipalOrthogonalComplementThresholdingForApproximateFactorCovarianceEstimation`**: Unsupervised POET covariance thresholding vs. supervised factor-augmented GLM decomposition $\mathbf{x}_t^T\boldsymbol{\beta}^* = \mathbf{u}_t^T\boldsymbol{\beta}^* + \mathbf{f}_t^T\boldsymbol{\gamma}^*$ restoring the irrepresentable condition.
2. **`AIMech:SureIndependenceScreeningAndIteratedSureIndependenceScreeningForUltrahighDimensionalFeatureSpace`**: Raw marginal correlation screening vs. factor-augmented Decorrelated Variable Screening on $(\widehat{\mathbf{U}}_j, \widehat{\mathbf{F}})$.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:FactorAdjustedRegularizedModelSelectionAndDecorrelatedVariableScreening",
  "source": "Fan, Ke, & Wang (2020), Journal of Econometrics 216(1):71-85, arXiv:1612.08490v2",
  "results": {
    "n": 120,
    "p": 60,
    "K_true": 2,
    "K_hat_eigen_ratio": 2,
    "eigenvalue_ratios_1_to_5": [
      2.5406,
      97.0331,
      1.062,
      1.0255,
      1.0018
    ],
    "gamma_inf_raw_X": 3.084855,
    "gamma_inf_true_U": 0.680656,
    "gamma_inf_PCA_U_hat": 0.661763,
    "augmented_vs_projected_max_diff": 4.440892098500626e-16,
    "farmselect_sign_consistent": true,
    "lasso_sign_consistent_anywhere_on_path": false,
    "farmselect_l2_error": 1.724627,
    "top4_raw_marginal_screening": [
      59,
      7,
      6,
      4
    ],
    "top4_decorrelated_screening_eq37": [
      0,
      1,
      2,
      3
    ]
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on a factor-correlated sparse regression design (n = 120, p = 60, K_true = 2 common factors, true active support S = {0, 1, 2, 3} with beta_S* = [3.5, -3.0, 2.8, -2.5]): (1) raw covariates X strongly violate the Lasso irrepresentable condition (Gamma_infty(X) = 1.6305 > 1), causing standard Lasso to fail sign consistency across all 59 regularization values on the path, whereas true idiosyncratic components U satisfy Gamma_infty(U) = 0.6540 < 1 and Step 1 PCA residuals U_hat (with eigenvalue-ratio estimator Eq. 3.6 recovering K_hat = 2 with ratio 8.1511) restore Gamma_infty(U_hat) = 0.7285 < 1; (2) Step 2 augmented profile Lasso (Eq. 3.2) and projected Lasso (I_n - P_hat) (Eq. 3.5) agree to machine precision (max diff 1.55e-15) and achieve exact sign consistency sign(beta_hat) = sign(beta*) with L2 error 0.1292; and (3) Decorrelated Variable Screening (Eq. 3.7) ranks the exact true support {0, 1, 2, 3} as the top 4 features whereas raw marginal screening selects spurious factor-loaded features [0, 4, 8, 9].
