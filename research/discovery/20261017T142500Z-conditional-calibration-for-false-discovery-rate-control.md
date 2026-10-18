# Literature Discovery Report: Conditional Calibration for False Discovery Rate Control Under Dependence

- **Report ID**: `20261017T142500Z-conditional-calibration-for-false-discovery-rate-control`
- **Created At**: `2026-10-17T14:25:00Z`
- **Curated Concept**: `AIMech:ConditionalCalibrationForFalseDiscoveryRateControl` (`data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml`, SHA-256 `6167290e8178827ea950c80549426c871ba5e2b6d727b42b4a536d860e097946`)
- **Verification Script**: `research/discovery/conditional-calibration-for-false-discovery-rate-control-boundaries.py` (SHA-256 `b2faa8358e24e389e3f4990eb3335d0ce511a19c1dc4f2c4b38bdd1c0cbec9b2`)

## Primary Sources Inspected

1. **Fithian & Lei (2022)** — *Conditional calibration for false discovery rate control under dependence*, *The Annals of Statistics* 50(6):3091–3118, `DOI:10.1214/21-AOS2137`, `arXiv:2007.10438v1`. Complete full-text HTML conversion read (`sha256: 3d199e8460e412f938c6fadae545d7ac86ddac5ae3c276fb367ed2dd21e283ca`), Crossref metadata (`sha256: 0da632f9a9738883608821f45e1112036619f11fd13df8a1cdef954f03ac6711`), and arXiv abstract (`sha256: d6affd9d3855f47b4e74deccb560adaf52dd327140b3fe4e57bcc2b83f00e0ae`).

## Candidate Decisions

- **`AIMech:ConditionalCalibrationForFalseDiscoveryRateControl`** (`ADD_CURATED`): Conditional threshold calibration and dependency-adjusted Benjamini-Hochberg / Benjamini-Yekutieli (dBH / dBY) procedures for finite-sample FDR control under known or sufficiency-characterized dependence (Fithian & Lei 2022).

## Constructed Mathematical Verification Summary

```json
{
  "claim1_lemma1_and_randomized_pruning_fdr": {
    "fdr_pruned_with_step3": 0.12775,
    "fdr_unpruned_without_step3": 0.22655,
    "lemma1_exact_match_rate": 1.0,
    "pruning_invoked_rate": 0.99825,
    "theoretical_fdr_bound": 0.133333
  },
  "claim2_dbh_dominance_and_safety": {
    "avg_discoveries_bh_pos": 1.641667,
    "avg_discoveries_by_neg": 1.466667,
    "avg_discoveries_dbh_pos": 1.683333,
    "avg_discoveries_dby_neg": 1.741667,
    "fdr_dbh_pos": 0.083333,
    "fdr_dby_neg": 0.075,
    "ind_exact_match_rate": 1.0,
    "neg_dby_dominance_rate": 1.0,
    "neg_dby_safe_rate": 1.0,
    "pos_cprds_dominance_rate": 1.0,
    "pos_cprds_safe_rate": 1.0
  },
  "claim3_knot_homotopy_and_recursive_refinement": {
    "avg_discoveries_iter1": 1.475,
    "avg_discoveries_iter2": 1.4875,
    "g_star_exact_knots": 0.038511,
    "g_star_fine_quadrature": 0.03849,
    "knot_vs_quadrature_abs_error": 2.082e-05,
    "recursive_refinement_monotone_rate": 1.0
  },
  "claim4_composite_null_and_misspecified_sigma_boundary": {
    "g_theta_0_boundary": 0.034368,
    "g_theta_minus_0_5": 0.013472,
    "g_theta_minus_1_0": 0.004235,
    "null0_fdr_contrib_misspecified_sigma": 0.1075,
    "target_per_hypothesis_alpha_over_m": 0.04
  }
}
```
