# Literature Discovery Report: Covariate-Powered Cross-Weighted Multiple Testing

- **Report ID**: `20261017T144500Z-covariate-powered-cross-weighted-multiple-testing`
- **Created At**: `2026-10-17T14:45:00Z`
- **Curated Concept**: `AIMech:CovariatePoweredCrossWeightedMultipleTesting` (`data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml`, SHA-256 `84d7094933c475533243366de9802790a89da87fb149ceffcb6ff304eacd3cf9`)
- **Verification Script**: `research/discovery/covariate-powered-cross-weighted-multiple-testing-boundaries.py` (SHA-256 `1d1be938e747200cda54c07cec039d6bd6c38c3881c99aca95c7fe396bcc035e`)

## Primary Sources Inspected

1. **Ignatiadis & Huber (2021)** — *Covariate powered cross-weighted multiple testing*, *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 83(4):720–751, `DOI:10.1111/rssb.12411`, `arXiv:1701.05179v7`. Complete full-text HTML conversion read (`sha256: 601c70dd0ebaa83c002b3882400ac8da8514ae8a54bf8a1c3a205c87d3080271`), Crossref metadata (`sha256: 3375754909898a3e6a4661ebd98b49507e8a988a4680c4d4d101299b749b4b45`), and arXiv abstract (`sha256: 2c863b983bbb6aed7033dcf5b5bb109495f4ca455cf91458933f3ce93ed816fd`).

## Candidate Decisions

- **`AIMech:CovariatePoweredCrossWeightedMultipleTesting`** (`ADD_CURATED`): K-fold cross-weighted multiple testing (IHW) with honest out-of-fold weight learning, tau-censoring, block-dependent fold partitioning, and Grenander least-concave-majorant convex weight optimization (Ignatiadis & Huber 2021).

## Constructed Mathematical Verification Summary

```json
{
  "claim1_honest_tau_censored_fdr_and_counterexamples": {
    "fdr_ihw_bh_alt": 0.0385,
    "fdr_ihw_gbh_global_null_G25": 0.065,
    "fdr_ihw_storey_alt": 0.0859,
    "fdr_naive_gbh_global_null_G25": 0.2533,
    "power_ihw_bh_no_storey": 0.8148,
    "power_ihw_storey": 0.8891,
    "power_unweighted_bh": 0.7487,
    "s13_exact_uncensored_honest_fdr": 0.216,
    "s13_mc_tau_censored_honest_fdr": 0.2023,
    "s13_mc_uncensored_honest_fdr": 0.212
  },
  "claim2_asymptotic_proposition1_and_corollary2": {
    "prop1a_naive_spec7_fdr": 0.7674,
    "prop1b_ihw_spec7_uncensored_fdr": 0.1331,
    "prop1c_gbh_power": 0.3978,
    "prop1c_ihw_gbh_uncensored_fdr": 0.0789,
    "prop1c_ihw_gbh_uncensored_power": 0.3954,
    "prop1c_ihw_vs_oracle_power_gap": 0.00522,
    "prop1c_oracle_power": 0.4006
  },
  "claim3_block_dependence_theorems3_4_and_examples1_2": {
    "example1_dishonest_wby_fdr": 1.0,
    "example1_honest_ihw_by_fdr": 0.012,
    "example2_adapt_by_exact_fdr_lower_bound": 0.2925,
    "example2_adapt_by_mc_fdr": 0.2938,
    "thm3_ihw_kbonf_kfwer": 0.016,
    "thm3_ihw_kbonf_power": 0.8829,
    "thm3_unweighted_kbonf_power": 0.7881,
    "thm4_ihw_by_fdr": 0.0083,
    "thm4_ihw_by_power": 0.8709,
    "thm4_unweighted_by_power": 0.7551
  },
  "claim4_grenander_kkt_and_breaking_adapt_regimes": {
    "adapt_min_rejections_at_alpha_0_05": 20,
    "fdr_ihw_grenander_sparse_superuniform": 0.0454,
    "grenander_max_concavity_slope_violation": 0.0,
    "power_adapt_sparse_superuniform": 0.0,
    "power_ihw_grenander_sparse_superuniform": 0.8375,
    "power_unweighted_bh_sparse_superuniform": 0.7672,
    "sparse_m1_true_signals": 12
  }
}
```
