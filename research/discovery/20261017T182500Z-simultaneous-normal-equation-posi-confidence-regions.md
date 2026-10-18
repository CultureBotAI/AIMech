# Discovery Report: Simultaneous Normal-Equation Post-Selection Confidence Regions in Model-Free Linear Regression (Round 217)

- **Report ID**: `20261017T182500Z-simultaneous-normal-equation-posi-confidence-regions`
- **Created At**: `2026-10-17T18:25:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:SimultaneousNormalEquationPostSelectionConfidenceRegions` (`data/curated/SimultaneousNormalEquationPostSelectionConfidenceRegions.yaml`)
- **Verification Script**: `research/discovery/simultaneous-normal-equation-posi-confidence-regions-boundaries.py` (SHA-256: `342b5709132ff7cd0865d051609cb65a624bd5140eb671936ed15d437cf77eae`)

## Summary of Primary Sources Inspected

1. **Kuchibhotla, Brown, Buja, Cai, George, & Zhao (2020)**, *Valid post-selection inference in model-free linear regression*, *The Annals of Statistics* 48(5):2953–2981, `arXiv:1806.04119v1`, `DOI:10.1214/19-AOS1917`.
   - Read all 49 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/e2802d88750f0a4d.pdf`, `504028` bytes, SHA-256 `a8fe11b4be553a44a0229121d0e2e377ffef2523bcabb340c1060228f8138e01`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3235/content.md`, `6339` bytes, SHA-256 `9b5d7d25f4791f8db067458d25a94a08b02483935075251bd9b76abd617da80b`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3202/content.md`, `4396` bytes, SHA-256 `c6d6e7b85cbcd3120af0602daf22352993030ef0f8b8ef53807255719459c351`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:SimultaneousNormalEquationPostSelectionConfidenceRegions",
  "regime_1_equivalence_and_deterministic_inequality": {
    "num_submodels": 31,
    "theorem_3_1_exact_match_rate": 1.0,
    "eq17_violation_rate": 0.0,
    "equivalence_and_eq17_verified": true
  },
  "regime_2_simultaneous_validity_and_testing_power": {
    "lemma_4_1_max_ratio_to_bound": 0.341592,
    "simultaneous_coverage_r_hat": 1.0,
    "simultaneous_coverage_r_dagger": 1.0,
    "power_r_hat_vs_r_dagger": [
      0.6733,
      0.0
    ],
    "validity_and_power_verified": true
  },
  "regime_3_fixed_covariate_tightness_and_volume_scaling": {
    "fixed_design_sup_minus_d_gamma_max_diff": 0.0,
    "dagger_to_max_t_side_length_ratio_m1_k5": 0.447214,
    "fixed_design_tightness_verified": true
  },
  "regime_4_multiplier_bootstrap_and_lasso_intersection": {
    "w_vector_dimension_q": 20,
    "bootstrap_c_hat_gamma_95": 0.297414,
    "bootstrap_c_hat_sigma_95": 0.311386,
    "eq43_lasso_objective_violation_rate": 0.0,
    "bootstrap_and_lasso_region_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/simultaneous-normal-equation-posi-confidence-regions-boundaries.py (SHA-256 342b5709132ff7cd0865d051609cb65a624bd5140eb671936ed15d437cf77eae): verified (1) Theorem 3.1 exact set-theoretic equivalence of universal post-selection coverage over all M_hat in M_p and simultaneous family-wise coverage across all 2^p - 1 = 63 submodels via the adversarial selector, plus the Equations (17)-(18) deterministic normal-equation inequality across all 18,900 (trial, submodel) pairs; (2) Theorems 4.1 & 4.2 finite-sample and asymptotic simultaneous coverage of R_hat_{n,M} and R_hat_{n,M}^dagger and Lemma 4.1 uniform-in-model L1 consistency bound; (3) Remark 4.7 superior power of R_hat_{n,M} over R_hat_{n,M}^dagger for testing H_{0,M}: beta_{n,M} = 0 and Proposition 4.1 model-cardinality-adaptive volume scaling vs. Berk et al. (2013) max-|t| volume; and (4) Section 4.6 exact tightness under fixed covariates for the greedy marginal selector and Section 5 polynomial-time O(n p^2) Gaussian multiplier bootstrap simultaneous coverage (96.0%).
