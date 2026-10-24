# Literature Discovery Report: Sequential Score-Discrepancy Conflict Diagnostic

- **Report ID**: `20261017T084600Z-sequential-score-conflict`
- **Created At**: `2026-10-17T08:46:00Z`
- **Curated Concept**: `AIMech:SequentialScoreDiscrepancyConflictDiagnostic` (`data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml`, SHA-256 `14d75f7ce1e21b32cf87cad76dc462d8ac60cf68d1fff58c12e6ba115c001871`)
- **Verification Script**: `research/discovery/sequential-score-conflict-boundaries.py` (SHA-256 `20f6156c7e7ce5e2bd37e6ee24c490bf45b9755005b3177e967045c0d8c386e7`)

## Primary Sources Inspected

1. **Yang, Nott, & Presanis (2026)** — *Conflict Diagnostics for Directed Acyclic Graphical Models with Application to Infectious Disease Modelling*, `arXiv:2511.02977v2` (DOI `https://doi.org/10.48550/arXiv.2511.02977`). Complete 52-page PDF read (`sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d`).
2. **Presanis, Ohlssen, Spiegelhalter, & De Angelis (2013)** — *Conflict Diagnostics in Directed Acyclic Graphical Models, with Applications in Evidence Synthesis*, *Statistical Science* 28(3):376–397, `arXiv:1310.0628v1` (DOI `https://doi.org/10.1214/13-STS426`). Complete 22-page PDF read (`sha256: 9cff5092b47d7ba20f9ae654b6ea63bd4fdf75ea8ccfdb663427ccab36f3d3a0`).

## Candidate Decisions

- **`AIMech:SequentialScoreDiscrepancyConflictDiagnostic`** (`ADD_CURATED`): Two-stage parent-to-child Bayesian DAG node-conflict diagnostic (Algorithm 1, Section 3.1, p. 16) that propagates parent-submodel posterior draws to define conditional priors for a separator block, evaluates conditional prior-expansion Fisher score discrepancies on the child submodel (with explicit single-draw vs. exact-expectation variance scaling per Appendix D.2, p. 43), and combines the dependent conditional $p$-values via order-statistic bounds or the Half-Cauchy Combination Test.
- **Mixture-approximation node-splitting conflict diagnostic (Yang, Nott, & Presanis, 2026, Section 3.2, Algorithm 2)** (`DEFER_NEXT_IN_COHORT`): Queued for dedicated curation in Round 169 as `AIMech:MixtureApproximationNodeSplittingDiagnostic`.

## Constructed Mathematical Verification Summary

```json
{
  "dependent_pvalue_combinations": {
    "comonotonic_hcct_p": 0.04,
    "comonotonic_min_order_p": 0.4,
    "comonotonic_u": 0.04,
    "heterogeneous_hcct_p": 0.00936006,
    "heterogeneous_hcct_t": 68.00956456,
    "heterogeneous_min_order_p": 0.01,
    "null_boundary_hcct_p": 0.7195622
  },
  "limits": "Constructed analytic two-stage normal DAG and closed-form p-value combination checks only; no MCMC, real-data epidemic model fit, or empirical repeated-data calibration simulation.",
  "single_draw_vs_exact_score_scaling": {
    "cond_var_single_given_y_obs": 1.25,
    "expected_cond_var": 0.375,
    "s_exact_obs": 0.875,
    "var_s_exact": 0.125,
    "var_s_single_marginal": 0.5,
    "variance_inflation_ratio": 4.0
  }
}
```
