# Literature Discovery Report: Bayes Optimal P-Value Weighting Under a Gaussian Prior on the Effect Sizes

- **Report ID**: `20261017T151000Z-bayes-optimal-p-value-weighting-under-gaussian-prior`
- **Created At**: `2026-10-17T15:10:00Z`
- **Curated Concept**: `AIMech:BayesOptimalPValueWeightingUnderGaussianPrior` (`data/curated/BayesOptimalPValueWeightingUnderGaussianPrior.yaml`, SHA-256 `b41f7ac57487b427d7bb97fb02c2e4408d93c2427f772554459327e665e78056`)
- **Verification Script**: `research/discovery/bayes-optimal-p-value-weighting-under-gaussian-prior-boundaries.py` (SHA-256 `cdb8e8e9e9c99a4a8143a6090b0d80932b358fa93d82ee238a6ebfb5de98dfd1`)

## Primary Sources Inspected

1. **Dobriban, Fortney, Kim, & Owen (2015)** — *Optimal multiple testing under a Gaussian prior on the effect sizes*, *Biometrika* 102(4):753–766, `DOI:10.1093/biomet/asv050`, `arXiv:1504.02935v1`. Complete full-text HTML conversion read (`sha256: 74f78d99ae84e7b018d019c3c8ea1669170a00beb033c2ac1adff3c440078942`), Crossref metadata (`sha256: bb77cf0915e8054cea78b81499250a82d8fe88d34101f77a8e64ae3b357c28b2`), and arXiv abstract (`sha256: 06609ec825323efe4b17a2be6e96c9a5476724d0fcaef93fcb9c619695543ba6`).

## Candidate Decisions

- **`AIMech:BayesOptimalPValueWeightingUnderGaussianPrior`** (`ADD_CURATED`): Bayes optimal p-value weights under uncertain Gaussian effect-size priors `mu_i ~ N(eta_i, sigma_i^2)`, sparse-means two-regime phase transition (Proposition 3.1), exact small-`q` quadratic-root weights and Spjøtvoll convergence (Theorem 3.2, Proposition 3.3), `O(J log J)` jump-discontinuity solver for general `q` (Theorem 3.5, Lemma 9.2), and maximin robustness (Section 4.2).

## Constructed Mathematical Verification Summary

```json
{
  "all_checks_passed": true,
  "concept_id": "AIMech:BayesOptimalPValueWeightingUnderGaussianPrior",
  "proposition_3_1_sparse_means": {
    "hotspot_exceeds_3x": true,
    "hotspot_power_ratio": 3.052,
    "regime1_thresh_gt_q": true,
    "regime2_p_all_on_M": 0.002,
    "regime2_p_star": 0.002999,
    "regime2_strictly_beats_all_on_M": true,
    "regime2_thresh_le_q": true,
    "regime2_w0_positive": 1.001538
  },
  "section_4_2_maximin_and_fwer": {
    "alpha_mc": 0.05,
    "bayes_has_maximin_advantage": true,
    "bayes_weight_on_small_mean": 0.729314,
    "fwer_controlled_under_misspecification": true,
    "fwer_mc_misspecified": 0.0456,
    "min_relative_eff_bayes": 0.857032,
    "min_relative_eff_spj": 0.686113,
    "pfer_mc_misspecified": 0.0468,
    "pow_bayes_sigma0": 0.055004,
    "pow_bayes_sigma1": 0.084652,
    "pow_spj_sigma0": 0.064179,
    "pow_spj_sigma1": 0.058081,
    "pow_unif_sigma0": 0.038991,
    "pow_unif_sigma1": 0.078755,
    "regret_bayes_at_sigma0": 0.009176,
    "regret_spj_at_sigma1": 0.026571,
    "spj_weight_on_small_mean": 0.0
  },
  "theorem_3_2_and_proposition_3_3": {
    "budget_error": 5.329070518200751e-15,
    "cond5_holds": true,
    "converges_to_spjotvoll": true,
    "global_lagrangian_maximum_holds": true,
    "lambda_star": 6.726987,
    "spjotvoll_convergence_max_diffs": {
      "sigma=0.0001": 1.98e-07,
      "sigma=0.01": 0.000114097,
      "sigma=0.1": 0.011526324,
      "sigma=1.0": 0.695122152
    }
  },
  "theorem_3_5_and_symmetry_breaking": {
    "W_star": 8.572377,
    "cond5_fails_for_large_q": true,
    "max_lemma_9_2_root_error": 1.1102230246251565e-16,
    "q_star": 0.375041,
    "q_star_bound": 0.0625,
    "q_star_gap": 0.025041,
    "symmetry_breaking_beats_uniform": true,
    "symmetry_breaking_power": 5.99983,
    "theorem_3_5_bound_holds": true,
    "theoretical_symmetry_limit": 6.0,
    "uniform_power_large_sigma": 5.00013
  }
}
```
