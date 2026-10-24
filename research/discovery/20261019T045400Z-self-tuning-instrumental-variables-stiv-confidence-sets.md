# Discovery Report: Round 270 — Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets

- **Timestamp**: `2026-10-19T04:54:00Z`
- **Selected Concept**: `AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets` (*Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets*)
- **Record Path**: `data/curated/SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml`
- **Primary Source**: Eric Gautier and Christiern Rose (2021), *High-Dimensional Instrumental Variables Regression and Confidence Sets*, *The Review of Economic Studies* 88(6):2888–2929 (`DOI:10.1093/restud/rdab002`, `arXiv:1105.2454v7`; originally circulated by Gautier & Tsybakov 2011).

## Identity & Boundary Resolution

`AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets` was checked against all 442 pinned AIO concepts and 664 maintained AIMech concepts:

1. **`AIMech:SquareRootLassoPivotalHighDimensionalSparseRegression`**: Exogenous regression $\mathbb{E}[XU]=0$ vs. endogenous IV conic program with asymmetric $\widehat{\Psi}$ and LP sensitivity confidence intervals.
2. **`AIMech:SelfNormalizedLassoOptimalInstrumentEstimationAndSupNormWeakIdentificationTesting`**: First-stage Lasso optimal instruments for low-dimensional $d$ vs. joint high-dimensional structural parameter + scale conic estimation ($d_X, d_Z \gg n$).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets",
  "source": "Gautier & Rose (2011/2021), Review of Economic Studies 88(6):2888-2929, arXiv:1105.2454v7",
  "pivotal_statistic_and_conic_program": {
    "t_hat_beta_star": 0.037139,
    "r_hat": 0.05,
    "c_param": 19.0,
    "sigma_star": 0.152004,
    "sigma_hat_stiv": 0.149807,
    "sigma_at_beta_hat": 0.149807,
    "zmom_over_r_hat": 0.149807,
    "stiv_obj_at_bhat": 5.621187,
    "stiv_obj_at_bstar": 5.663777
  },
  "cone_and_sensitivity_verification": {
    "cone_lhs_off_support_l1": 0.014116,
    "cone_rhs_bound": 0.414399,
    "psi_delta_inf": 0.011911,
    "eq_a14_rhs": 0.015091,
    "kappa_lower_bound": 0.740733
  },
  "support_recovery_and_bias_correction": {
    "true_support": [
      0,
      1
    ],
    "stiv_support": [
      0,
      1,
      7
    ],
    "thresholded_stiv_support": [
      0,
      1
    ],
    "signs_match": true,
    "stiv_active_l2_error": 0.011179,
    "bc_stiv_active_l2_error": 0.001978
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on an endogenous high-dimensional IV design (n = 120, d_X = 10, d_Z = 14, true sparse beta* = (1.2, -0.9, 0, ..., 0) with strong endogeneity Cov(X_0, U) != 0): (1) at beta*, the pivotal self-normalized statistic t_hat(beta*) = 0.037139 <= r_hat = 0.05 holds (event G), certifying feasibility of (beta*, sigma_hat(beta*)) with STIV objective 5.621187 < 5.663777 at beta* and binding conic equality sigma_hat = sigma_hat(beta_hat) = |D_Z E_n[ZU(beta_hat)]|_inf / r_hat = 0.149807; (2) the standardized estimation error Delta_hat = D_X^{-1}(beta_hat - beta*) satisfies the empirical cone inequality |Delta_hat_{S^c}|_1 = 0.014116 <= |Delta_hat_S|_1 + c*g_hat(Delta_hat) = 0.414399 (Eq. 9) and Eq. (A.14) |Psi_hat Delta_hat|_inf = 0.011911 <= 2*r_hat*sigma_bar + r_hat*(sigma_hat(beta*) - sigma_hat) = 0.015091 with empirical sensitivity lower bound kappa_hat >= 0.740733; and (3) hard-thresholded STIV (Theorem 3.2, Eq. 27) recovers the exact support {0, 1} and signs while one-step BC-STIV (Section 4, Eq. 30) reduces active L2 error by 82.3% from 0.011179 to 0.001978.
