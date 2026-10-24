# Literature Discovery Report: Sequential Kernelized Independence Testing by Betting

- **Report ID**: `20261017T133500Z-sequential-kernelized-independence-testing-by-betting`
- **Created At**: `2026-10-17T13:35:00Z`
- **Curated Concept**: `AIMech:SequentialKernelizedIndependenceTestingByBetting` (`data/curated/SequentialKernelizedIndependenceTestingByBetting.yaml`, SHA-256 `13d50b1f150eec5c72de7b682597b072d55c89440d57ca0e2585bdf2b2d561d9`)
- **Verification Script**: `research/discovery/sequential-kernelized-independence-testing-by-betting-boundaries.py` (SHA-256 `1011c0595c66b831608d3136f506507a0d185d18c24576ff66eaed218bde12ba`)

## Primary Sources Inspected

1. **Podkopaev, Blobaum, Kasiviswanathan, & Ramdas (2023)** — *Sequential Kernelized Independence Testing*, *Proceedings of the 40th International Conference on Machine Learning (ICML)*, PMLR 202:27957–27993, `arXiv:2212.07383`. Complete full-text HTML conversion read (`sha256: 7c7c96c17f9206e06efde4b3c4338b0cc297d40b6f0037f934523ed7077fbf51`), PMLR record (`sha256: 2efc16eb3712b9ea2ed3532d73a94292582b04339a0a7fa6e2f41fad4c55b0c8`), and arXiv abstract (`sha256: 1206a67911e85351ce8a5edd08ed903f124446590204354a26275565b0e34d47`).

## Candidate Decisions

- **`AIMech:SequentialKernelizedIndependenceTestingByBetting`** (`ADD_CURATED`): Sequential nonparametric independence testing framework (Podkopaev et al. 2023, ICML / PMLR 202:27957–27993) using coordinate-swapped RKHS witness payoffs (HSIC, COCO, KCC) and symmetry-based transformations for unbounded kernels coupled with Online Newton Step coin-betting martingales.

## Constructed Mathematical Verification Summary

```json
{
  "claim1_hsic_swap_payoff_linear_time_norm_and_ons_wealth_growth": {
    "example2_kelly_log_growth": 0.020136,
    "example2_overshoot_log_growth": -0.002447,
    "max_abs_normalized_hsic_payoff": 0.461126,
    "max_linear_vs_quadratic_norm_diff": 2e-15,
    "reduction_2st_mean_samples_to_stop": 180.0,
    "skit_alt_power": 1.0,
    "skit_mean_samples_to_stop": 95.43,
    "skit_null_type1_error": 0.0
  },
  "claim2_time_varying_drift_validity_and_simultaneous_shift_counterexample": {
    "batch_permutation_drifting_null_type1_error": 1.0,
    "example3_simultaneous_shift_expected_payoff": 0.03125,
    "single_marginal_shift_expected_payoff": 0.0,
    "skit_drifting_null_type1_error": 0.0
  },
  "claim3_coco_and_kcc_spectral_skit_and_cholesky_normalization": {
    "cholesky_exact_quad_norm": 3.889458,
    "cholesky_nuclear_upper_bound": 3.925962,
    "coco_nonlinear_alt_power": 1.0,
    "coco_null_type1_error": 0.0,
    "max_abs_coco_payoff": 0.754926
  },
  "claim4_symmetry_based_skit_for_unbounded_kernels": {
    "max_unbounded_linear_kernel_W_t": 635.8096,
    "odd_payoff_alt_power": 1.0,
    "odd_payoff_null_type1": 0.0,
    "pred_payoff_alt_power": 0.9667,
    "pred_payoff_null_type1": 0.0,
    "rank_payoff_alt_power": 1.0,
    "rank_payoff_null_type1": 0.0
  }
}
```
