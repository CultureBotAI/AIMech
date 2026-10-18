# Literature Discovery Report: Adaptive Data-Driven Optimal P-Value Weighting

- **Report ID**: `20261017T145500Z-adaptive-data-driven-optimal-p-value-weighting`
- **Created At**: `2026-10-17T14:55:00Z`
- **Curated Concept**: `AIMech:AdaptiveDataDrivenOptimalPValueWeighting` (`data/curated/AdaptiveDataDrivenOptimalPValueWeighting.yaml`, SHA-256 `87961708f5770edc0a05f6048c36f9d50507a48e453db008ec06cf37d9ecb32b`)
- **Verification Script**: `research/discovery/adaptive-data-driven-optimal-p-value-weighting-boundaries.py` (SHA-256 `f1d278cc2731b192fdfd3d00352cbee849761fe5c38973a92c5baca38509ec42`)

## Primary Sources Inspected

1. **Durand (2019)** — *Adaptive p-value weighting with power optimality*, *Electronic Journal of Statistics* 13(2):3336–3385, `DOI:10.1214/19-EJS1578`, `arXiv:1710.01094v2`. Complete full-text HTML conversion read (`sha256: a6eddfe1e0a9ea8136d1088cc6b9da218426d0cd9ed7a3a4db3fc0ffdf3543ca`), Crossref metadata (`sha256: 792010392cd70a1ef92b7c10fe3326f5eda717498e7a608e2da973fd17475e65`), and arXiv abstract (`sha256: ee606b72127354a287093bc8d42cbe265c0d615640bbf6d9d392f8be377526a9`).

## Candidate Decisions

- **`AIMech:AdaptiveDataDrivenOptimalPValueWeighting`** (`ADD_CURATED`): Multi-Weighted Benjamini-Hochberg (MWBH), Adaptive Data-Driven Optimal Weighting (ADDOW / ADDOW-tilde) with Grenander least-concave-majorant CDF estimation over the null-proportion-weighted budget `K_hat`, and F-fold cross-weighted `crADDOW` (Durand 2019).

## Constructed Mathematical Verification Summary

```json
{
  "all_checks_passed": true,
  "claim1_mwbh_addow_fixed_point_and_lcm_concavity": {
    "max_fixed_point_error": 0.0,
    "max_gaddow_concavity_violation": 5.811e-05,
    "max_lcm_concavity_violation": 0.0,
    "max_monotonicity_violation": 0.0,
    "mismatches_addow_vs_wbh_terminal": 0,
    "mismatches_lemma_a5_step_up": 0,
    "trials": 40
  },
  "claim2_asymptotic_power_optimality_and_me_equivalence": {
    "asymp_fdr_ce": 0.05,
    "asymp_fdr_me_C1_15": 0.043478,
    "asymp_power_abh": 0.127344,
    "asymp_power_addow_ce": 0.131404,
    "asymp_power_bh": 0.117761,
    "asymp_power_hzz": 0.130514,
    "asymp_power_ihw": 0.119278,
    "asymp_power_pro1": 0.131199,
    "asymp_power_pro2": 0.131404,
    "expected_alpha_over_C1_15": 0.043478,
    "max_budget_saturation_error": 0.0,
    "max_weight_diff_G_vs_P_under_ME": 0.0
  },
  "claim3_remark3_1_section6_4_ihw_suboptimality_counterexample": {
    "asymp_fdr_addow_ce": 0.7,
    "asymp_fdr_bh_pi0_alpha": 0.539,
    "asymp_fdr_ihw": 0.566215,
    "asymp_power_addow_ce": 0.229168,
    "asymp_power_bh": 0.216218,
    "asymp_power_ihw": 0.20932,
    "mc_fdr_addow_ce": 0.69793,
    "mc_fdr_bh": 0.5335,
    "mc_fdr_ihw": 0.56447,
    "mc_power_addow_ce": 0.23123,
    "mc_power_bh": 0.21713,
    "mc_power_ihw": 0.21465,
    "w_addow_ce_group1_group2": [
      1.86593,
      1.29499
    ],
    "w_ihw_group1_group2": [
      0.51401,
      1.054
    ]
  },
  "claim4_section7_cross_addow_stabilization_and_theorem7_1": {
    "fdr_addow_weak_signal": 0.09417,
    "fdr_craddow_strong_signal": 0.04632,
    "fdr_craddow_weak_signal": 0.048,
    "fdr_reduction_weak_signal": 0.04617,
    "pow_addow_strong_signal": 0.16854,
    "pow_bh_strong_signal": 0.14437,
    "pow_craddow_strong_signal": 0.15817,
    "tpr_addow_strong_signal": 0.67417,
    "tpr_bh_strong_signal": 0.5775,
    "tpr_craddow_strong_signal": 0.63267
  },
  "concept_id": "AIMech:AdaptiveDataDrivenOptimalPValueWeighting",
  "primary_source": {
    "arxiv": "1710.01094v2",
    "authors": "Guillermo Durand",
    "doi": "10.1214/19-EJS1578",
    "title": "Adaptive p-value weighting with power optimality",
    "venue": "Electronic Journal of Statistics 13(2):3336-3385",
    "year": 2019
  }
}
```
