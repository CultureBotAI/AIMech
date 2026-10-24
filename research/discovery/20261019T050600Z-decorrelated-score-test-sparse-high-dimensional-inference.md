# Discovery Report: Round 277 — Decorrelated Score Function and One-Step Estimator for Sparse High-Dimensional Inference

- **Timestamp**: `2026-10-19T05:06:00Z`
- **Selected Concept**: `AIMech:DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference` (*Decorrelated Score Function and One-Step Estimator for Sparse High-Dimensional Inference*)
- **Record Path**: `data/curated/DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference.yaml`
- **Primary Source**: Yang Ning and Han Liu (2017), *A General Theory of Hypothesis Tests and Confidence Regions for Sparse High Dimensional Models*, *The Annals of Statistics* 45(1):158–195 (`DOI:10.1214/16-AOS1448`, `arXiv:1412.8765v2`).

## Identity & Boundary Resolution

`AIMech:DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference` was checked against all 442 pinned AIO concepts and 671 maintained AIMech concepts:

1. **`AIMech:LowDimensionalProjectionAndDebiasedLassoConfidenceIntervalsForHighDimensionalLinearAndGeneralizedLinearModels`**: Predictor-space nodewise de-biasing vs. general likelihood/M-estimation Hilbert-space score projection $S(\boldsymbol{\theta}, \boldsymbol{\gamma}) = \nabla_{\boldsymbol{\theta}}\ell - \mathbf{w}^{*T}\nabla_{\boldsymbol{\gamma}}\ell$, one-step update, multiplier bootstrap for growing $d_0$, and sandwich misspecification theory.
2. **`AIMech:OrthogonalScoreAndWeightedDoubleSelectionPostSelectionInferenceInHighDimensionalQuantileRegression`**: Density-weighted check-loss quantile orthogonal scores vs. smooth empirical risk / log-likelihood decorrelated score tests and one-step estimators.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:DecorrelatedScoreFunctionAndOneStepEstimatorForSparseHighDimensionalInference",
  "source": "Ning & Liu (2017), Annals of Statistics 45(1):158-195, arXiv:1412.8765v2",
  "hilbert_projection_and_partial_information": {
    "d": 8,
    "rho": 0.6,
    "w_star_first3": [
      0.6,
      0.0,
      -0.0
    ],
    "max_orthogonality_error": 0.0,
    "partial_information_I_theta_given_gamma": 0.64,
    "quadratic_score_variance": 0.64
  },
  "linear_and_glm_decorrelated_score": {
    "n": 180,
    "d": 45,
    "theta_true": 0.5,
    "theta_lasso_biased": 0.328207,
    "theta_onestep_eq29": 0.485094,
    "theta_exact_root": 0.485094,
    "onestep_vs_exact_root_diff": 0.0,
    "naive_score_at_true_theta": -0.033451,
    "decorrelated_score_at_true_theta": 0.011375,
    "ci_95_onestep": [
      0.311485,
      0.658704
    ],
    "covers_true_theta": true,
    "glm_U_hat_under_H0": -0.231145,
    "glm_U_naive_under_H0": -0.678866
  },
  "misspecification_and_multiplier_bootstrap": {
    "n": 200,
    "d0": 4,
    "d1": 26,
    "T_hat_sup_norm": 4.247931,
    "multiplier_bootstrap_c95": 7.070251,
    "bootstrap_accepts_true_H0": true,
    "misspecified_sandwich_variance_coord0": 11.430017,
    "naive_homoscedastic_variance_coord0": 4.108025,
    "variance_ratio_sandwich_to_naive": 2.7824
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across three constructed experiments: (1) for an AR(1)/Toeplitz Fisher information matrix I* (d = 8, rho = 0.6), the score projection direction w* = (I*_{gamma,gamma})^{-1} I*_{gamma,theta} = (0.6, 0, ..., 0)^T achieves exact orthogonality ||I*_{gamma,theta} - I*_{gamma,gamma} w*||_infty = 0.0 and partial Fisher information I*_{theta|gamma} = 1 - rho^2 = 0.64 matching (1, -w^{*T}) I* (1, -w^{*T})^T; (2) in a high-dimensional linear model (n = 180, d = 45, theta* = 0.5) and logistic GLM (Eq. 5.2), the one-step estimator theta_tilde = 0.485094 matches the exact root of S_hat(theta, gamma_hat) = 0 to 0.0 error, removes L1 shrinkage bias (theta_hat = 0.328207) with valid 95% CI [0.311485, 0.658704], and the weighted-Lasso logistic decorrelated score yields U_hat = -0.231145 under H_0; and (3) for a multidimensional null (d_0 = 4, d_1 = 26, n = 200) and heteroscedastic misspecification (z_i^2 variance), the multiplier bootstrap critical value c_95 = 7.070251 properly calibrates T_hat = 4.247931 and the sandwich variance estimator (11.4300) corrects the 2.78x downward bias of the naive homoscedastic variance (4.1080).
