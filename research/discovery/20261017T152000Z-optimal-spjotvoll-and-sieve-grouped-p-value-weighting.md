# Literature Discovery Report: Optimal Spjøtvoll and Sieve-Grouped P-Value Weighting

- **Report ID**: `20261017T152000Z-optimal-spjotvoll-and-sieve-grouped-p-value-weighting`
- **Created At**: `2026-10-17T15:20:00Z`
- **Curated Concept**: `AIMech:OptimalSpjotvollAndSieveGroupedPValueWeighting` (`data/curated/OptimalSpjotvollAndSieveGroupedPValueWeighting.yaml`, SHA-256 `5bcc259bbbe4758e8fff9ec95e7b7c967e7431c39327bad2b771284bcf9e1841`)
- **Verification Script**: `research/discovery/optimal-spjotvoll-and-sieve-grouped-p-value-weighting-boundaries.py` (SHA-256 `b8cd995e32e5c6e5163a2f12fc3e7271118b406e8ae70ec1517273e5f96b06c2`)

## Primary Sources Inspected

1. **Kathryn Roeder & Larry Wasserman (2009)** — *Genome-Wide Significance Levels and Weighted Hypothesis Testing*, *Statistical Science* 24(4):398–413, `DOI:10.1214/09-STS289`, `arXiv:1010.4637v1`. Complete full-text HTML conversion read (`sha256: a7ac40415cd7649f2933c79f98fcc4e830f5fbf9c9c50602e2505cbb2878ff9f`), Crossref metadata (`sha256: 26d259113110dcfc5f97fb2af1d85cface93638f2d1280b3f180b28d8e7f6523`), and arXiv abstract (`sha256: b3d1954b604c394236efeb63499834c82d7639cd1a0753ce4584678b0eb9a80f`).

## Candidate Decisions

- **`AIMech:OptimalSpjotvollAndSieveGroupedPValueWeighting`** (`ADD_CURATED`): One-parameter Spjøtvoll optimal p-value weights and oracle power (Theorem 3.1, Lemma 3.2), worst-case sparse-weight robustness and `b=0` safe zone (Theorems 3.3–3.4, Lemma 3.5), Kolmogorov-Smirnov discontinuity of optimal weights vs. least-favorable worst-case power at `u_* = sqrt(2 c_*)` (Lemma 3.6, Theorems 3.7–3.8), maximin binary external weights (Theorems 4.1–4.3), and sieve-principle grouped method-of-moments weighting with linear smoothing (Section 5, Equations 12–13).

## Constructed Mathematical Verification Summary

```json
{
  "lemma_3_6_and_theorems_3_7_3_8_ks_discontinuity_vs_power": {
    "expected_ratio_1_over_K_plus_1": 0.000999,
    "ks_distance_gamma": 0.1,
    "min_grid_power_over_u": 0.7529825,
    "rho_tilde_xi": 0.00999001,
    "rho_true": 10.0,
    "thm_3_7_xi_star_threshold": 5.91887833,
    "thm_3_8_c_star": 5.94833415,
    "thm_3_8_u_star": 3.44915472,
    "thm_3_8_worst_case_power": 0.75292715,
    "thm_3_8_xi_test": 4.2,
    "u_lemma_3_6": 0.030529,
    "unweighted_bonferroni_power_at_xi_test": 0.62149445,
    "weight_ratio_tilde_over_true": 0.000999,
    "worst_case_still_beats_bonferroni": true,
    "xi_lemma_3_6": 9.763185
  },
  "theorem_3_1_and_lemma_3_2_oracle_weights": {
    "avg_oracle_power": 0.53897493,
    "avg_unweighted_bonferroni_power": 0.39544288,
    "budget_error": 2.22e-16,
    "c_star": 3.6167495309,
    "max_kkt_stationarity_error": 6.592e-17,
    "max_lemma_3_2_power_identity_error": 3.608e-16,
    "oracle_beats_bonferroni": true
  },
  "theorems_3_4_and_lemma_3_5_sparse_robustness": {
    "B": 4.0,
    "R_B0_above_xi_star": -0.01657252,
    "R_B0_at_half_xi_star": 0.00053768,
    "R_B0_at_lemma_3_5_threshold": 0.00051182,
    "lemma_3_5_mills_ratio_threshold": 1.18817712,
    "safe_zone_positive_at_b_zero": true,
    "xi_star_exact_root": 2.41591146,
    "z_B_alpha_over_m": 4.10747965,
    "z_alpha_over_m": 4.41717341
  },
  "theorems_4_1_4_2_and_section_5_sieve_grouped_weights": {
    "section_5_mom_max_pi_error": 5.551e-17,
    "section_5_mom_max_xi_error": 4.441e-16,
    "section_5_smoothed_group_weights": [
      2.875555,
      0.969733,
      0.104712,
      0.05
    ],
    "section_5_smoothed_null_group_weight_positive": true,
    "thm_4_1_B_star": 9.459504,
    "thm_4_1_max_robustness_R": 0.09446462,
    "thm_4_1_turnaround_B0": 111.65303,
    "thm_4_2_B_maximin": 16.130156,
    "thm_4_2_power_w0": 0.45060625,
    "thm_4_2_power_w1": 0.7,
    "thm_4_2_w0": 0.569311,
    "thm_4_2_w1": 9.183082
  }
}
```
