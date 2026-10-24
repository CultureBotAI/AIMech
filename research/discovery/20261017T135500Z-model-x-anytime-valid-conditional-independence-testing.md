# Literature Discovery Report: Model-X Anytime-Valid Conditional Independence Testing via E-Processes

- **Report ID**: `20261017T135500Z-model-x-anytime-valid-conditional-independence-testing`
- **Created At**: `2026-10-17T13:55:00Z`
- **Curated Concept**: `AIMech:ModelXAnytimeValidConditionalIndependenceTesting` (`data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml`, SHA-256 `00eba6063c717bd325de163ab10f91b16f906630f6e81a4b04d61f7fa698445e`)
- **Verification Script**: `research/discovery/model-x-anytime-valid-conditional-independence-testing-boundaries.py` (SHA-256 `545fe37b8a23e0d4e620ced865d70eb33118c5de17b9bc8bbdcbd193aa794fbf`)

## Primary Sources Inspected

1. **Grünwald, Henzi, & Lardy (2024)** — *Anytime-Valid Tests of Conditional Independence Under Model-X*, *Journal of the American Statistical Association* 119(546):1554–1565, `DOI:10.1080/01621459.2023.2205607`, `arXiv:2209.12637v2`. Complete full-text HTML conversion read (`sha256: 2a68c4355f736174f431b7610664b603bb0210fdfeb010de3ba0461ea9ee8b16`), Crossref metadata (`sha256: 8efce92ca7a71b0526bbc4370bb510433bd1de67a6ec01e4818ca3cd563083ba`), and arXiv abstract (`sha256: 2ffb4cdf23e82030c267f75ccd5bee104b88a42099cf4bb84adb6934bb1c4131`).
2. **Shaer, Maman, & Romano (2023)** — *Model-X Sequential Testing for Conditional Independence via Testing by Betting*, *NeurIPS* 36, `arXiv:2210.00354v3`. Abstract read (`sha256: 397b2ffe9dac56cd2303888dd2bfdf0b34cca3994404cf80ef8f7b709d84b8d3`).

## Candidate Decisions

- **`AIMech:ModelXAnytimeValidConditionalIndependenceTesting`** (`ADD_CURATED`): Sequential Model-X conditional independence testing framework (Grünwald, Henzi, & Lardy 2024; Shaer, Maman, & Romano 2023) using exact or Monte Carlo plus-one normalized conditional e-variables and conditional GRO likelihood ratios.

## Constructed Mathematical Verification Summary

```json
{
  "claim1_exact_and_mc_conditional_e_statistic": {
    "exact_e_cond_expectation": 1.0,
    "mc_naive_cond_expectation": 1.239524,
    "mc_plus_one_cond_expectation": 1.0,
    "mc_plus_one_max_bound": 2.333333,
    "null_anytime_rejection_rate_m2": 0.034
  },
  "claim2_gro_conditional_mutual_information_and_kl_regret": {
    "cmi_i_x_y_given_z": 0.12312,
    "gro_expected_log_growth": 0.12312,
    "max_e_gro_vs_likelihood_ratio_diff": 4e-16,
    "plugin_expected_log_growth": 0.096722,
    "prop4_exact_decomposition_diff": 0.0,
    "prop4_kl_lower_bound": 0.092637
  },
  "claim3_tv_robustness_under_model_x_misspecification": {
    "null_reject_prob_under_hat_q": 0.0,
    "null_reject_prob_under_true_q": 0.0,
    "product_tv_distance": 0.057797,
    "theorem6_upper_bound_alpha_plus_tv": 0.157797
  },
  "claim4_sequential_logistic_e_crt_and_truncation": {
    "alt_anytime_power": 1.0,
    "alt_mean_per_step_log_growth": 0.083661,
    "null_anytime_type1_error": 0.025,
    "single_step_e_truncated_eps005": 0.1,
    "single_step_e_untruncated_eps0": 1.9e-13
  }
}
```
