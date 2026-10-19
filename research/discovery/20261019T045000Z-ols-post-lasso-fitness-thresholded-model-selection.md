# Discovery Report: Round 268 — OLS Post-Lasso and Fitness-Thresholded Post-Model-Selection Estimation in High-Dimensional Sparse Models

- **Timestamp**: `2026-10-19T04:50:00Z`
- **Selected Concept**: `AIMech:OLSPostLassoAndFitnessThresholdedPostModelSelectionInHighDimensionalSparseModels` (*OLS Post-Lasso and Fitness-Thresholded Post-Model-Selection Estimation in High-Dimensional Sparse Models*)
- **Record Path**: `data/curated/OLSPostLassoAndFitnessThresholdedPostModelSelectionInHighDimensionalSparseModels.yaml`
- **Primary Source**: Alexandre Belloni and Victor Chernozhukov (2013), *Least squares after model selection in high-dimensional sparse models*, *Bernoulli* 19(2):521–547 (`DOI:10.3150/11-BEJ410`, `arXiv:1001.0188v5`).

## Identity & Boundary Resolution

`AIMech:OLSPostLassoAndFitnessThresholdedPostModelSelectionInHighDimensionalSparseModels` was checked against all 442 pinned AIO concepts and 662 maintained AIMech concepts:

1. **`AIMech:L1PenalizedAndPostPenalizedQuantileRegressionProcessInHighDimensionalSparseModels`**: Check-loss quantile regression process rather than least-squares Post-Lasso, Lemma 3 sparse eigenvalue sublinearity $\phi(\ell k) \le \lceil\ell\rceil\phi(k)$, Remark 3.1 Lasso shrinkage lower bounds, and Equation (2.11) fitness thresholding.
2. **`AIMech:PostDoubleSelectionHighDimensionalTreatmentEffectInference`**: Union-of-supports double selection for semiparametric causal treatment effects rather than single-equation OLS Post-Lasso oracle inequalities.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:OLSPostLassoAndFitnessThresholdedPostModelSelectionInHighDimensionalSparseModels",
  "source": "Belloni & Chernozhukov (2013), Bernoulli 19(2):521-547",
  "lemma3_sparse_eigenvalue_sublinearity": {
    "phi_values": {
      "1": 1.0,
      "2": 1.475191,
      "3": 1.709834,
      "4": 1.873682,
      "5": 1.964419,
      "6": 2.026816
    },
    "sublinearity_checks": [
      {
        "k": 1,
        "l": 2,
        "phi_lk": 1.475191,
        "l_times_phi_k": 2.0
      },
      {
        "k": 1,
        "l": 3,
        "phi_lk": 1.709834,
        "l_times_phi_k": 3.0
      },
      {
        "k": 2,
        "l": 2,
        "phi_lk": 1.873682,
        "l_times_phi_k": 2.950382
      },
      {
        "k": 2,
        "l": 3,
        "phi_lk": 2.026816,
        "l_times_phi_k": 4.425573
      },
      {
        "k": 3,
        "l": 2,
        "phi_lk": 2.026816,
        "l_times_phi_k": 3.419668
      }
    ]
  },
  "post_lasso_and_fitness_thresholding": {
    "lasso_support": [
      0,
      1,
      2,
      3
    ],
    "fitness_thresholded_support": [
      0,
      1,
      2
    ],
    "phi_m_hat": 1.319438,
    "remark31_lasso_lower_bound": 0.030868,
    "lasso_pred_error": 0.28324,
    "ols_post_lasso_pred_error": 0.146349,
    "fitness_post_lasso_pred_error": 0.074447,
    "q_hat_lasso": 0.092189,
    "q_hat_post0": 0.060505,
    "q_hat_post_fit": 0.068442,
    "gamma_target": -0.015842,
    "selected_threshold_t_gamma": 1.249326
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across two regimes: (1) on an n=40, p=12 correlated design, exact subset enumeration confirms Lemma 3's sparse eigenvalue sublinearity phi(l*k) <= ceil(l)*phi(k) across all (k, l) pairs (e.g., phi(2) = 1.475191 <= 2*phi(1) = 2.0, phi(6) = 2.026816 <= 3*phi(2) = 4.425573); and (2) on an n=60, p=45 sparse regression instance (s=3, T=[0, 1, 2]) where Lasso selects T_hat = [0, 1, 2, 3] (1 false positive), Remark 3.1's deterministic shrinkage lower bound holds strictly (lasso_pred_error = 0.28324 >= 0.030868), unthresholded OLS Post-Lasso reduces empirical risk Q_hat from 0.092189 to 0.060505 and nearly halves prediction error from 0.28324 to 0.146349, and Equation 2.11 fitness thresholding (t_gamma = 1.249326) prunes the false positive to recover the exact support [0, 1, 2] and reduces prediction error 3.8x over Lasso to 0.074447.
