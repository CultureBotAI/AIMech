# Discovery Report: Globally Convergent Regularization Homotopy and Nyström Newton Method for Generalized Self-Concordant Losses (Round 224)

- **Report ID**: `20261018T200500Z-globally-convergent-newton-generalized-self-concordant`
- **Created At**: `2026-10-18T20:05:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:GloballyConvergentRegularizationHomotopyAndNystromNewtonForGeneralizedSelfConcordantLosses` (`data/curated/GloballyConvergentRegularizationHomotopyAndNystromNewtonForGeneralizedSelfConcordantLosses.yaml`)
- **Verification Script**: `research/discovery/globally-convergent-newton-generalized-self-concordant-boundaries.py` (SHA-256: `c371e979cc09409b304becd1ed8dd19f016b99e4f292366069ade3a3103c362d`)

## Summary of Primary Sources Inspected

1. **Ulysse Marteau-Ferey, Francis Bach, & Alessandro Rudi (2019)**, *Globally Convergent Newton Methods for Ill-conditioned Generalized Self-concordant Losses*, *Advances in Neural Information Processing Systems* 32 (NeurIPS 2019), `arXiv:1907.01771v2`.
   - Read all 77 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/15b7ec09d0cdc139.pdf`, `1101806` bytes, SHA-256 `f520e8cee313c802dfda6f95e7d8336a34fdb3abcbf508b221c2100edcef1156`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3480/content.md`, `6750` bytes, SHA-256 `ac868ce14413122db2988cdd8d73a2514eff5a25105bd777eac6efc6458ece18`), and NeurIPS 2019 metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3496/content.md`, `10137` bytes, SHA-256 `56c131ef2c2b757d295e13186d75d4556e388b2b4ffd4d92db524d28e0c06eac`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:GloballyConvergentRegularizationHomotopyAndNystromNewtonForGeneralizedSelfConcordantLosses",
  "all_passed": true,
  "check_1_gsc_dikin_and_regimes": {
    "passed": true,
    "max_phi_ratio_err": 1.6e-15,
    "initial_renorm_decrement": 0.120757,
    "dikin_threshold_1_over_7": 0.142857,
    "lemma6_function_equivalence_holds": true,
    "exact_newton_quadratic_convergence_holds": true,
    "relative_anm_linear_convergence_holds": true
  },
  "check_2_homotopy_globalization_scheme": {
    "passed": true,
    "direct_init_renorm_decrement_at_lam": 110.2196,
    "max_renorm_decrement_along_homotopy": 0.138302,
    "phase1_final_renorm_decrement_at_lam": 0.004841,
    "dikin_threshold_1_over_7": 0.142857,
    "phase1_stages_K": 899,
    "theorem1_stage_bound": 3569,
    "phase2_steps_T": 7,
    "final_suboptimality": 0.0,
    "target_eps": 1e-08
  },
  "check_3_pcg_and_nystrom_projection": {
    "passed": true,
    "pcg_tau3_relative_error": 0.000643,
    "pcg_tau3_theoretical_bound": 0.038476,
    "target_rho_1_over_7": 0.142857,
    "projector_capacity_C_P": 3e-06,
    "nu_full_at_projected_point": 0.000669,
    "prop15_upper_bound_3_nuP_plus_s": 0.548732
  }
}
```

Executed pure-Python verification in research/discovery/globally-convergent-newton-generalized-self-concordant-boundaries.py (SHA-256 c371e979cc09409b304becd1ed8dd19f016b99e4f292366069ade3a3103c362d): verified (1) Appendix A.1 Eq. (13) helper identity phi_over(t)/phi_under(t) = e^t (error 1.6e-15), Lemma 6 function-value equivalence inside D_lambda(1/7), Lemma 10 exact Newton quadratic convergence, and Proposition 5 1/7-relative ANM linear convergence; (2) Lemma 3/13 Dikin-ellipsoid inclusion, Proposition 6, and Theorem 1 two-phase regularization homotopy globalization from mu_0 = 7 R ||nabla f(0)|| down to lambda = 1e-4 (maintaining max renormalized decrement 0.138302 <= 1/7 across K = 899 <= 3569 stages and reaching suboptimality <= 1e-8, whereas direct initialization at lambda = 1e-4 has renormalized decrement 110.2196 >> 1/7); and (3) Proposition 12 3-step preconditioned conjugate gradient relative error 0.000643 <= 0.038476 <= 1/7 and Proposition 15 Nyström projector capacity bound.
