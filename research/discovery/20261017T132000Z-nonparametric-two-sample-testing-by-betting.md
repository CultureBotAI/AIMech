# Literature Discovery Report: Nonparametric Two-Sample Testing by Betting

- **Report ID**: `20261017T132000Z-nonparametric-two-sample-testing-by-betting`
- **Created At**: `2026-10-17T13:20:00Z`
- **Curated Concept**: `AIMech:NonparametricTwoSampleTestingByBetting` (`data/curated/NonparametricTwoSampleTestingByBetting.yaml`, SHA-256 `5c119acd76a48be2ae886b4ebcbcc952d5f4269de14ce3dece35766648d417ac`)
- **Verification Script**: `research/discovery/nonparametric-two-sample-testing-by-betting-boundaries.py` (SHA-256 `710904ef7c5ab90ad551a257c643e39e7a50dcd1b77df7acd620eeb46225d06d`)

## Primary Sources Inspected

1. **Shekhar & Ramdas (2023)** — *Nonparametric Two-Sample Testing by Betting*, *IEEE Transactions on Information Theory* 70(2):1178–1203, `arXiv:2112.09162` (DOI `https://doi.org/10.1109/TIT.2023.3305867`). Complete full-text HTML conversion read (`sha256: 69380bbf6cc3a5ece3ffc898bc31a5c00a277f2a92990f2df50128c2d3b609d6`), Crossref metadata (`sha256: bdb4c6323a40437394bfab1c184b19ecc8dc65661116c7187c40d850c4ec2cf9`), and arXiv abstract (`sha256: 14021274caaf27a2ad1acd1207b9e375846ec092ea3bbabfca267dfd613aa5f1`).

## Candidate Decisions

- **`AIMech:NonparametricTwoSampleTestingByBetting`** (`ADD_CURATED`): Sequential nonparametric two-sample and operator-invariance hypothesis testing framework (Shekhar & Ramdas 2023, IEEE Transactions on Information Theory 70(2):1178–1203) coupling predictable witness learning over Integral Probability Metrics with Online Newton Step coin-betting martingales.

## Constructed Mathematical Verification Summary

```json
{
  "claim1_ons_wealth_lower_bounds_and_variance_adaptivity": {
    "large_variance_log_growth_rate": 0.027052,
    "large_variance_theoretical_lb": 0.014706,
    "max_ons_regret_over_log_n": 0.28249,
    "min_ratio_wealth_to_coarse_exp_lb": 336575370.651454,
    "min_ratio_wealth_to_cutkosky_orabona_tight_lb": 115870.262078,
    "n_steps": 300,
    "small_variance_log_growth_rate": 0.095093,
    "small_variance_theoretical_lb": 0.05
  },
  "claim2_bounded_mean_oga_regret_and_minimax_stopping_time": {
    "alpha": 0.05,
    "bernoulli_mean_stopping_time": 55.27,
    "lemma4_wald_kl_lower_bound": 8.8391,
    "max_ratio_oga_regret_to_3_over_2_sqrt_Mt": 0.521939,
    "mean_stopping_time_delta_0_2": 35.35,
    "mean_stopping_time_delta_0_4": 19.12,
    "null_empirical_type1_error": 0.0,
    "stopping_time_ratio_delta_0_2_to_0_4": 1.849
  },
  "claim3_sequential_kernel_mmd_and_unbounded_sigmoid_test": {
    "kernel_mmd_null_type1_error": 0.0,
    "kernel_mmd_zero_mean_alt_mean_stopping_time": 17.6,
    "kernel_mmd_zero_mean_equal_variance_alt_power": 1.0,
    "odd_sigmoid_symmetry_max_residual": 0.0,
    "unbounded_tanh_linear_kernel_null_type1": 0.05,
    "unbounded_tanh_linear_kernel_power": 1.0
  },
  "claim4_time_varying_streams_and_operator_invariance_tests": {
    "independence_test_swap_operator_null_type1": 0.0,
    "independence_test_swap_operator_power": 1.0,
    "symmetry_test_erm_ks_null_type1": 0.0333,
    "symmetry_test_erm_ks_power": 1.0,
    "time_varying_alternating_alt_power": 1.0,
    "time_varying_drifting_null_type1": 0.0
  }
}
```
