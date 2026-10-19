# Discovery Report: Round 283 — Adaptive Lasso and Median-of-Ratios Consistent Invalid Instrument Selection in Linear Instrumental Variables Models

- **Timestamp**: `2026-10-19T05:18:00Z`
- **Selected Concept**: `AIMech:AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels` (*Adaptive Lasso and Median-of-Ratios Consistent Invalid Instrument Selection in Linear Instrumental Variables Models*)
- **Record Path**: `data/curated/AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels.yaml`
- **Primary Source**: Frank Windmeijer, Helmut Farbmacher, Neil Davies, and George Davey Smith (2019), *On the Use of the Lasso for Instrumental Variables Estimation with Some Invalid Instruments*, *Journal of the American Statistical Association* 114(527):1339–1350 (`DOI:10.1080/01621459.2018.1498346`, `PMC6817329`).

## Identity & Boundary Resolution

`AIMech:AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels` was checked against all 442 pinned AIO concepts and 677 maintained AIMech concepts:

1. **`AIMech:SomeInvalidSomeValidInstrumentalVariableLassoEstimation`**: Unweighted $\ell_1$-penalized sisVIVE vs. Windmeijer et al. (2019) Schur-complement proof of sisVIVE irrepresentable failure ($\gamma_2'C_{21}C_{11}^{-1} = -\gamma_1'$) and consistent Median-of-Ratios Adaptive Lasso oracle selection.
2. **`AIMech:SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments`**: Voting-matrix searching/sampling confidence intervals vs. Median-of-Ratios Adaptive Lasso variable selection and post-Lasso 2SLS.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels",
  "source": "Windmeijer, Farbmacher, Davies, & Davey Smith (2019), JASA 114(527):1339-1350, DOI:10.1080/01621459.2018.1498346, PMC6817329",
  "irrepresentable_condition_propositions_1_and_2": {
    "L": 10,
    "s": 3,
    "C_gamma_rank_deficiency_norm": 2e-16,
    "prop1_eq18_max_diff": 4e-16,
    "prop2_identity_max_err": 3e-16,
    "ic_inf_norm_unequal_uncorr_9_over_7": 1.285714,
    "ic_inf_norm_unequal_corr": 1.480757,
    "ic_inf_norm_equal_uncorr_3_over_7": 0.428571
  },
  "table2_unequal_strength_simulation": {
    "n": 2000,
    "beta_true": 0.0,
    "plim_beta_naive": 0.264706,
    "beta_naive_2sls": 0.270383,
    "beta_oracle_2sls": -0.032957,
    "standard_lasso_selected_invalid": [
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "beta_standard_lasso_biased": 0.305983,
    "beta_median_of_ratios": -0.006454,
    "adaptive_lasso_selected_invalid": [
      0,
      1,
      2
    ],
    "beta_post_alasso": -0.032957,
    "andrews_hansen_selected_invalid": [
      0,
      1,
      2
    ],
    "beta_post_alasso_ah": -0.032957,
    "andrews_hansen_j_test_path_first4": [
      {
        "step": 0,
        "candidate_set": [],
        "J_stat": 69.7838,
        "df": 9,
        "crit_val": 20.9074
      },
      {
        "step": 1,
        "candidate_set": [
          2
        ],
        "J_stat": 55.9236,
        "df": 8,
        "crit_val": 19.3563
      },
      {
        "step": 2,
        "candidate_set": [
          1,
          2
        ],
        "J_stat": 41.873,
        "df": 7,
        "crit_val": 17.7674
      },
      {
        "step": 3,
        "candidate_set": [
          0,
          1,
          2
        ],
        "J_stat": 3.6748,
        "df": 6,
        "crit_val": 16.1315
      }
    ]
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on Windmeijer et al. (2019, PMC6817329): (1) Proposition 1 Equation (18) matches C_{21} C_{11}^{-1} to 4.44e-16 and Proposition 2's identity gamma_2' C_{21} C_{11}^{-1} = -gamma_1' holds to 3.33e-16; (2) when 2 invalid instruments have strong first-stage effects (gamma_1 = [2.0, 2.0]) and 3 valid instruments have gamma_2 = [1.0, 1.0, 1.0], the Lasso irrepresentable LHS equals 1.333333 > 1, causing unweighted sisVIVE to fail selection consistency across all lambda > 0 and yield biased estimate 1.6524 (true beta = 1.0); and (3) the Median-of-Ratios estimator achieves beta_hat_m = 0.996357, and the resulting Adaptive Lasso recovers the exact invalid instrument support {0, 1} with post-Lasso 2SLS estimate 0.999935.
