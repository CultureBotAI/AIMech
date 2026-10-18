# Literature Discovery Report: Constrained Convex P-Value Weighting in Monotone Likelihood Ratio Families (Princessp)

- **Report ID**: `20261017T151500Z-constrained-convex-p-value-weighting-in-monotone-likelihood-ratio-families`
- **Created At**: `2026-10-17T15:15:00Z`
- **Curated Concept**: `AIMech:ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies` (`data/curated/ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies.yaml`, SHA-256 `97415576de3471717aa4c965626803a592de772077e8fabab033968b49bd05e5`)
- **Verification Script**: `research/discovery/constrained-convex-p-value-weighting-in-monotone-likelihood-ratio-families-boundaries.py` (SHA-256 `1b9be0d07148762e23e11e0dd19da97330a09ed9f22bfc69bc879c7c00b27d76`)

## Primary Sources Inspected

1. **Edgar Dobriban (2018)** — *Weighted mining of massive collections of P-values by convex optimization*, *Information and Inference: A Journal of the IMA* 7(2):251–275, `DOI:10.1093/imaiai/iax013`, `arXiv:1603.05334v2`. Complete full-text HTML conversion read (`sha256: 2cb5aec839dc83af3c17cf19656ce656b33187513af08341990941df259bc513`), Crossref metadata (`sha256: 8c16d847b555d2ce062b4faf587c8f385c834ab95051566fc32d5a9938f071c0`), and arXiv abstract (`sha256: b43dd4a2f163c568fd7e983076b5606f4b5bddec57e8d35f7acf0ddb58e30544`).

## Candidate Decisions

- **`AIMech:ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies`** (`ADD_CURATED`): Constrained convex p-value weighting in monotone likelihood ratio families (Princessp), ROC re-parametrization concavity in one-sided MLR and two-sided canonical exponential families (Propositions 2.1–2.2), closed-form two-sided Gaussian `arccosh` weights (Proposition 2.3), small-`q` monotonicity vs. moderate-`q` non-monotonicity of unconstrained Spjøtvoll weights (Propositions 3.1–3.2), and `O(J)` tridiagonal-plus-rank-1 interior-point Newton solver under order and box constraints (Section 4.2).

## Constructed Mathematical Verification Summary

```json
{
  "all_checks_passed": true,
  "concept_id": "AIMech:ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies",
  "proposition_2_1_mlr_concavity": {
    "bernoulli_step_roc_non_concave": true,
    "crit_val_param_non_concave": true,
    "crit_val_second_deriv_at_minus_3": 0.241971,
    "exp_mlr_strictly_concave": true,
    "gaussian_roc_strictly_concave": true
  },
  "propositions_2_2_and_2_3_two_sided": {
    "budget_error_two_sided": 0.0,
    "lam_star_two_sided": 0.08047,
    "max_kkt_stationarity_error_two_sided": 9.71445146547012e-17,
    "prop_2_2_two_sided_concave": true,
    "prop_2_3_cond_holds": true,
    "w_star_two_sided": [
      0.010861,
      0.356136,
      1.454571,
      1.820731,
      1.357701
    ]
  },
  "propositions_3_1_and_3_2_monotonicity": {
    "monotone_at_small_q": true,
    "non_monotone_at_moderate_q": true,
    "prop_3_2_a_star": 230.464399,
    "prop_3_2_root_error": 2.6645352591003757e-15,
    "q_crit_one_sided": 4e-06,
    "q_moderate": 0.001,
    "q_small": 2e-06,
    "w_spjotvoll_moderate_q": [
      0.0,
      0.04638,
      1.416629,
      2.375011,
      1.16198
    ],
    "w_spjotvoll_small_q": [
      0.0,
      0.0,
      0.003302,
      0.998367,
      3.998331
    ]
  },
  "section_4_2_princessp_log_barrier_and_robustness": {
    "max_diff_from_spjotvoll_at_small_q": 1.9360055256711917e-06,
    "power_on_underestimated_signal_princessp_l05": 0.391248,
    "power_on_underestimated_signal_spjotvoll": 0.0,
    "solver_stats_moderate_q": {
      "bounds_hold": true,
      "budget_error": 2.6645352591003757e-15,
      "initial_kkt_residual": 4.6629367034256575e-15,
      "max_barrier_curvature_h": 12406880721.560608,
      "monotone_holds": true,
      "total_newton_steps": 50
    },
    "total_power_princessp_l05_well_specified": 0.461019,
    "total_power_spjotvoll_well_specified": 0.49574,
    "total_power_uniform_well_specified": 0.387494,
    "w0_princessp_l05_small_q": 0.500012,
    "w0_spjotvoll_small_q": 0.0,
    "w_princessp_moderate_q_bounded": [
      0.250014,
      0.250055,
      1.294849,
      1.602518,
      1.602566
    ]
  }
}
```
