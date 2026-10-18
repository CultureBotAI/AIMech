# Literature Discovery Report: Reverse-Submartingale Confidence Sequences for Convex Divergences and Functionals

- **Report ID**: `20261017T134500Z-reverse-submartingale-convex-divergence-confidence-sequences`
- **Created At**: `2026-10-17T13:45:00Z`
- **Curated Concept**: `AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences` (`data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml`, SHA-256 `7ab66808e86837214be02e6ca9183a7ebd19df51f6c6dbd9ddadfd84a1d81afe`)
- **Verification Script**: `research/discovery/reverse-submartingale-convex-divergence-confidence-sequences-boundaries.py` (SHA-256 `3be3507b60779fcaa44006e746083168f4f2f2c7cfa45571f31f54ea702bcb2b`)

## Primary Sources Inspected

1. **Manole & Ramdas (2023)** — *Martingale Methods for Sequential Estimation of Convex Functionals and Divergences*, *IEEE Transactions on Information Theory* 69(7):4641–4658, `DOI:10.1109/TIT.2023.3250099`, `arXiv:2103.09267v4`. Complete full-text HTML conversion read (`sha256: 473bd824958b260761bdac2383a11e13f12e0f864dad5a097da3de03b9c331fe`), Crossref metadata (`sha256: 2f4bded756bd8507874158acca0883f29751d3f8a6d6a51d45246a916410bc21`), and arXiv abstract (`sha256: 8fb54fe7ac0e37f396fa80bd29283642c1b46b70567b3dac986fb3aea0b53050`).

## Candidate Decisions

- **`AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences`** (`ADD_CURATED`): Exchangeable-filtration reverse-submartingale and partially ordered reverse-submartingale framework (Manole & Ramdas 2023, IEEE TIT 69(7):4641–4658) for time-uniform estimation of convex functionals and two-sample divergences.

## Constructed Mathematical Verification Summary

```json
{
  "claim1_reverse_submartingale_loo_and_ville_inequality": {
    "max_emp_measure_reverse_martingale_diff": 0.0,
    "max_ustat_neg_kernel_loo_diff": 0.0,
    "min_kl_loo_excess": 0.0,
    "min_tv_loo_excess": 0.0,
    "min_vstat_neg_kernel_loo_excess": -0.04,
    "min_vstat_psd_loo_excess": 0.0,
    "ville_empirical_exceed_prob": 0.042,
    "ville_theoretical_upper_bound": 0.2786
  },
  "claim2_two_sample_ks_cs_and_stopping_time_upward_bias": {
    "mean_stopped_plugin_ks": 0.6034,
    "true_ks_distance": 0.25,
    "two_sample_ks_cs_simultaneous_coverage": 1.0,
    "upward_bias_at_stopping_time": 0.3534
  },
  "claim3_discrete_divergences_and_gaussian_smoothing": {
    "discrete_tv_cs_violation_rate": 0.0,
    "smoothed_tv_cs_violation_rate": 0.0,
    "smoothed_tv_mean_at_t10": 0.1016,
    "smoothed_tv_mean_at_t200": 0.0192,
    "unsmoothed_continuous_tv": 1.0
  },
  "claim4_rademacher_loo_and_forward_supermartingale_failure": {
    "forward_supermartingale_asymptotic_width_limit": 1.029653,
    "min_rademacher_loo_excess": 1e-16,
    "reverse_submartingale_kl_bound_at_t500": 0.066883
  }
}
```
