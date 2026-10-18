# Literature Discovery Report: Optimal Multi-Weighted Step-Up Procedure for False Discovery Rate Control

- **Report ID**: `20261017T150500Z-optimal-multi-weighted-step-up-procedure-for-fdr-control`
- **Created At**: `2026-10-17T15:05:00Z`
- **Curated Concept**: `AIMech:OptimalMultiWeightedStepUpProcedureForFDRControl` (`data/curated/OptimalMultiWeightedStepUpProcedureForFDRControl.yaml`, SHA-256 `0ce681bedc7dae26198a31774cb3234dab960c9f788adebd3f28225aae14c1a8`)
- **Verification Script**: `research/discovery/optimal-multi-weighted-step-up-procedure-for-fdr-control-boundaries.py` (SHA-256 `810d1ec102b97f173b750065ed2f004a625206ab99fad1a85674c7bcfa6f2b40`)

## Primary Sources Inspected

1. **Roquain & van de Wiel (2009)** — *Optimal weighting for false discovery rate control*, *Electronic Journal of Statistics* 3:678–711, `DOI:10.1214/09-EJS430`, `arXiv:0807.4081v3`. Complete full-text HTML conversion read (`sha256: 118114d17f1c9900cb2e2c7461777243a70495f634b6aaaa8951df9ac3b1cc38`), Crossref metadata (`sha256: c9bc07d65747b07c0ea7261c54df5111adccc7f7cf13303e94fe9cc745194294`), and arXiv abstract (`sha256: cc884794c5874c17adbfb7903210e1ea1dd0092093543e8b4b6ae33343ffdf5c`).

## Candidate Decisions

- **`AIMech:OptimalMultiWeightedStepUpProcedureForFDRControl`** (`ADD_CURATED`): Multi-weighted step-up `SU(W*)` and step-down `SD(W*)` procedures, Lagrangian optimal weight function `W*(u)` (Proposition 3.2), damped finite-sample FDR control `SU(W_tilde)` and `SD(W_tilde)` (Theorem 4.1), and non-asymptotic and asymptotic oracle power dominance over static weighted linear step-up procedures `LSU(w)` (Theorems 4.2–4.3).

## Constructed Mathematical Verification Summary

```json
{
  "all_checks_passed": true,
  "concept_id": "AIMech:OptimalMultiWeightedStepUpProcedureForFDRControl",
  "lemma_c1_and_theorem_4_1_fdr": {
    "alpha": 0.2,
    "damped_su_controls_fdr": true,
    "exact_su_damped_fdr": 0.160839,
    "exact_su_unmodified_fdr": 0.21,
    "mc_sd_unmodified_fdr": 0.19892,
    "mc_su_damped_fdr": 0.16146,
    "mc_su_unmodified_fdr": 0.20968,
    "step_down_controls_fdr_m2": true,
    "unmodified_su_exceeds_alpha": true
  },
  "proposition_3_2_optimal_weights": {
    "max_budget_error": 8.881784197001252e-16,
    "max_kkt_marginal_spread": 2.1316282072803006e-14,
    "max_perturbed_pow_u025": 0.372535,
    "pow_opt_u025": 0.374161,
    "strict_lagrangian_maximum": true,
    "threshold_monotone": true,
    "w_large_u_max_mu": 0.564465,
    "w_small_u_max_mu": 2.383683
  },
  "section_5_3_misspecification": {
    "fdr_controlled_under_severe_misspecification": true,
    "fdr_high_sigma_350": 0.02943,
    "fdr_low_sigma_020": 0.00027,
    "pow_high_sigma_350": 0.35119,
    "pow_low_sigma_020": 0.70655,
    "power_degrades_under_severe_misspecification": true
  },
  "theorems_4_2_and_4_3_oracle_dominance": {
    "all_fdr_controlled": true,
    "fdr_bh": 0.03729,
    "fdr_sd_damped": 0.00021,
    "fdr_su_damped": 0.00021,
    "fdr_su_star": 0.00021,
    "max_static_pow": 0.68356,
    "multi_weighted_beats_bh": true,
    "pow_bh": 0.51428,
    "pow_sd_damped": 0.67778,
    "pow_su_damped": 0.67072,
    "pow_su_star": 0.68644,
    "sd_damped_beats_su_damped": true,
    "static_pows": {
      "u0=0.02": 0.64494,
      "u0=0.10": 0.68356,
      "u0=0.30": 0.67878,
      "u0=0.60": 0.62361,
      "u0=1.00": 0.56356
    }
  }
}
```
