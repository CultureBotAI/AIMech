# Discovery Report: Uniformly Valid Post-Model-Selection Confidence Intervals via Consistent Variance Overestimation (Round 213)

- **Report ID**: `20261017T174500Z-uniformly-valid-post-model-selection-confidence-intervals`
- **Created At**: `2026-10-17T17:45:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:UniformlyValidPostModelSelectionConfidenceIntervals` (`data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml`)
- **Verification Script**: `research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py` (SHA-256: `307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486`)

## Summary of Primary Sources Inspected

1. **Bachoc, Preinerstorfer, & Steinberger (2020)**, *Uniformly valid confidence intervals post-model-selection*, *The Annals of Statistics*, 48(1):440–463 (`DOI:10.1214/19-AOS1815`, `arXiv:1611.01043v4`).
   - Read all 70 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/e8f5af049ece013f.pdf`, `828184` bytes, SHA-256 `8cfe880631d099338a706a63a8ca5e194d4c0dd0f6aa71fb6c8b4f75a741974f`), Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3065/content.md`, `4692` bytes, SHA-256 `811c958acffdc11ae9fac8c19ee8ea237a1cdefb961040eccf80dfc3a86a782c`), and arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3100/content.md`, `6170` bytes, SHA-256 `60d4499beb32921901fec796f2f9976c21ef87de64d9e103697ab499c3269004`).

## Constructed Boundary & Regime Verification

```json
{
  "concept_id": "AIMech:UniformlyValidPostModelSelectionConfidenceIntervals",
  "regime_1_proposition_2_7_overestimation": {
    "mean_variance_ratio_well_specified": 0.99856,
    "mean_variance_ratio_misspecified": 1.64697,
    "theoretical_misspecified_limit_1_plus_dn": 1.64,
    "proposition_2_7_verified": true
  },
  "regime_2_homoskedastic_adaptation_and_impossibility": {
    "prop_3_4_misspecified_var_ratio": 3.272727,
    "prop_3_4_correct_var_ratio": 1.0,
    "thm_3_3_k_individual_xi": 1.959964,
    "thm_3_2_k_simultaneous_gamma": 2.236477,
    "prop_3_5_unconditional_var": 1.02,
    "prop_3_5_conditional_var": 1.0,
    "homoskedastic_regime_verified": true
  },
  "regime_3_heteroskedastic_eicker_and_lemma_2_9": {
    "q_naive": 1.644854,
    "b_alpha_min_k_p_k": 2.397949,
    "b_alpha_k_k": 2.63407,
    "significance_hunting_naive_coverage": 0.8275,
    "significance_hunting_posi_hlm_coverage": 0.9762,
    "heteroskedastic_eicker_verified": true
  },
  "regime_4_binary_regression_and_canonical_link": {
    "canonical_link_max_score_diff_error": 2.220446049250313e-16,
    "canonical_link_max_second_derivative": -0.045177,
    "b_alpha_canonical_logistic_p3_k12": 2.397949,
    "b_alpha_general_link_k12_k12": 2.63407,
    "binary_regression_canonical_reduction_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py (SHA-256 307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486): (1) Regime 1 (Proposition 2.7 consistent overestimation): verified well-specified mean variance ratio 0.99856 ~= 1.0 and misspecified ratio 1.64697 ~= 1 + d_n = 1.64. (2) Regime 2 (Homoskedastic adaptation & impossibility): verified Proposition 3.4 misspecified ratio 3.272727 vs. well-specified ratio 1.0, Theorem 3.3 K(corr(Xi_n)) = 1.959964 < Theorem 3.2 K(corr(Gamma_n)) = 2.236477, and Proposition 3.5 impossibility mixture unconditional variance 1.02 vs. conditional 1.0. (3) Regime 3 (Heteroskedastic Eicker & Lemma 2.9): verified q_naive = 1.644854 < B_alpha(min(k, p), k) = 2.397949 < B_alpha(k, k) = 2.63407, and under significance hunting naive coverage collapses to 0.8275 while CI^hlm achieves 0.9762. (4) Regime 4 (Binary regression & canonical link): verified canonical logistic identity phi_dot_1 - phi_dot_2 === 1 to machine precision (2.220446049250313e-16), negative definiteness of the log-likelihood Hessian (-0.045177 < 0), and rank reduction from B_alpha(12, 12) = 2.63407 to B_alpha(3, 12) = 2.397949.
