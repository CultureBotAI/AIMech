# Literature Discovery Report: Fork-Convex Exchangeability Testing via Universal Safe E-Processes

- **Report ID**: `20261017T140500Z-fork-convex-exchangeability-testing-by-safe-e-processes`
- **Created At**: `2026-10-17T14:05:00Z`
- **Curated Concept**: `AIMech:ForkConvexExchangeabilityTestingBySafeEProcesses` (`data/curated/ForkConvexExchangeabilityTestingBySafeEProcesses.yaml`, SHA-256 `300ea1665bdd8cedfa38746832f1e7d6b85a410eacb4a87ca16eab55ca833370`)
- **Verification Script**: `research/discovery/fork-convex-exchangeability-testing-by-safe-e-processes-boundaries.py` (SHA-256 `5f65c10a5abea1ce5ba60848103e7f9a5160614cb3e3082bfb5a77779069758b`)

## Primary Sources Inspected

1. **Ramdas, Ruf, Larsson, & Koolen (2022)** — *Testing exchangeability: Fork-convexity, supermartingales and e-processes*, *International Journal of Approximate Reasoning* 141:83–109, `DOI:10.1016/j.ijar.2021.06.017`, `arXiv:2102.00630v4`. Complete full-text HTML conversion read (`sha256: c26efcd568aec8916fb5ef6041ab96c3cc4c66b2b8bb5bb6b15df2b65f495c06`), Crossref metadata (`sha256: f95719b0d50d5a65dc01b8b9965dbf91fa34fa0e29597792eea122d7b6ddd400`), and arXiv abstract (`sha256: 59f57aab3f19cb76eca534c71ccb66ca9df7449dca9f54eab3aa52a7c696a7c1`).

## Candidate Decisions

- **`AIMech:ForkConvexExchangeabilityTestingBySafeEProcesses`** (`ADD_CURATED`): Fork-convexity characterization of composite test supermartingales and universal-inference / context-tree safe e-processes for sequential exchangeability testing (Ramdas, Ruf, Larsson, & Koolen 2022).

## Constructed Mathematical Verification Summary

```json
{
  "claim1_fork_convexity_and_nsm_impossibility": {
    "max_fork_martingale_diff": 4e-16,
    "r_t_on_alternating_8": 10.9375,
    "snell_envelope_exceeds_one": 1.0
  },
  "claim2_universal_jeffreys_eprocess_and_safety": {
    "kt_regret_upper_bound": 3.783787,
    "max_kt_regret_minus_bound": -1.457486,
    "max_seq_vs_closed_form_diff": 0.0,
    "sup_tau_expected_r_beta22_exchangeable": 1.0
  },
  "claim3_asymptotic_growth_and_higher_order_mixtures": {
    "alt_empirical_log_growth_rate": 0.678431,
    "alt_theoretical_r_star": 0.693147,
    "cycle_0011_double_mixture_log_growth_rate": 0.665104,
    "cycle_0011_first_order_r_t": 0.002552
  },
  "claim4_empty_cs_stopping_time_and_adjuster": {
    "changepoint_final_adjusted_e_process": 246.022558,
    "changepoint_final_unadjusted_r_t": 0.024891,
    "changepoint_peak_r_t": 31787.24818,
    "empty_cs_vs_r_t_stopping_mismatch": 0.0,
    "shift_tau_intersection": 41.0,
    "shift_tau_r_threshold": 43.0
  }
}
```
