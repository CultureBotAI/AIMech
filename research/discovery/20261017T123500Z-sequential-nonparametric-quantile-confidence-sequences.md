# Literature Discovery Report: Sequential Nonparametric Quantile Confidence Sequences

- **Report ID**: `20261017T123500Z-sequential-nonparametric-quantile-confidence-sequences`
- **Created At**: `2026-10-17T12:35:00Z`
- **Curated Concept**: `AIMech:SequentialNonparametricQuantileConfidenceSequences` (`data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml`, SHA-256 `a3d72fae22daf9b8ad6d2049df0f3e79ce5b8ff72bb829ed14b162853030dc11`)
- **Verification Script**: `research/discovery/sequential-nonparametric-quantile-confidence-sequences-boundaries.py` (SHA-256 `2d2bedcb5fe830f3c5444ccbad91b96e034af2ff89e0d42a740066d17ac7b8aa`)

## Primary Sources Inspected

1. **Howard & Ramdas (2022)** — *Sequential estimation of quantiles with applications to A/B testing and best-arm identification*, *Bernoulli* 28(3):1704–1728, `arXiv:1906.09712` (DOI `https://doi.org/10.3150/21-BEJ1388`). Complete full-text HTML conversion read (`sha256: 09a883cff34d29a90f41d1fb175392703bd82f68c23248d45aa1b1a9e79d18b7`).
2. **Howard, Ramdas, McAuliffe, & Sekhon (2021)** — *Time-uniform, nonparametric, nonasymptotic confidence sequences*, *The Annals of Statistics* 49(2):1055–1080, `arXiv:1810.08240` (DOI `https://doi.org/10.1214/20-AOS1991`). Complete full-text HTML conversion read (`sha256: aef352a6e271a2317826f200bf481b2aaf956b978323ee8a2b25b589c2ec1732`).
3. **Waudby-Smith & Ramdas (2024)** — *Estimating means of bounded random variables by betting*, *Journal of the Royal Statistical Society Series B: Statistical Methodology* 86(1):1–27, `arXiv:2010.09686` (DOI `https://doi.org/10.1093/jrsssb/qkad009`). Complete full-text HTML conversion read (`sha256: c41bcb5ff7e35853316a0709b17b18506ef1e4be8252a3a474ed38a4811f2495`).

## Candidate Decisions

- **`AIMech:SequentialNonparametricQuantileConfidenceSequences`** (`ADD_CURATED`): Distribution-free, nonasymptotic sequential quantile and empirical distribution function confidence sequence framework (Howard & Ramdas 2022) combining exact Galois order-statistic inversions, point-mass quantile martingales, stitched sub-gamma and beta-binomial fixed-quantile bounds, stratified dyadic empirical-process finite-LIL chaining, double-stitched log-odds quantile grids, two-sample sequential quantile tests, and QLUCB quantile bandit best-arm identification.

## Constructed Mathematical Verification Summary

```json
{
  "empirical_process_lil_and_lemma10": {
    "cor2_radius_t1000": 0.083344,
    "cor2_to_fixed_dkw_ratio_t1000": 1.940623,
    "dr68_radius_t1000": 0.120129,
    "gamma_sq_A085_C7_eta101": 1.256413,
    "max_lemma10_violation": -2.6e-06,
    "prefactor_at_gamma_sq_125": 1611.9867,
    "szorenyi_radius_t1000": 0.094706
  },
  "fixed_quantile_bounds_and_cauchy_coverage": {
    "cauchy_cs_miscover_rate": 0.0,
    "cauchy_naive_clt_miscover_rate": 0.358,
    "f_bb_p05_t200": 0.061055,
    "f_stitch_p05_t200": 0.070183,
    "f_subg_p05_t200": 0.122514,
    "r_tuned_p05_m32": 0.145,
    "r_tuned_p50_m32": 0.758,
    "tail_tightness_ratio_subg_to_bb": 2.006621
  },
  "galois_inversion_and_martingale": {
    "atom_martingale_mean_abs_err": 1e-16,
    "inversion_mismatches": 0.0,
    "max_cgf_minus_psi_b": -5.63308e-05,
    "max_psi_b_minus_psi_g": -4.2e-09
  },
  "two_sample_and_qlucb": {
    "min_profile_g_minus_true_log_l": -0.142992,
    "qlucb_accuracy": 1.0,
    "qlucb_mean_samples": 121.6,
    "sample_reduction_ratio": 1.3263,
    "uniform_rr_mean_samples": 161.28
  }
}
```
