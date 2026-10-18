# Literature Discovery Report: Asymptotically Optimal Rejection Curve False Discovery Rate Control and Adjusted Step-Up-Down Testing

- **Report ID**: `20261017T162500Z-asymptotically-optimal-rejection-curve-fdr-control`
- **Created At**: `2026-10-17T16:25:00Z`
- **Curated Concept**: `AIMech:AsymptoticallyOptimalRejectionCurveFDRControl` (`data/curated/AsymptoticallyOptimalRejectionCurveFDRControl.yaml`, SHA-256 `fa6f6a7c44a7f51eaced5de206ddb6679c8bf92489442a4265e6b5c7a6373bf9`)
- **Verification Script**: `research/discovery/asymptotically-optimal-rejection-curve-fdr-control-boundaries.py` (SHA-256 `7044b86e383d07f258fa7ad1acb875a58d7a4fbc9da2ed45282ba3fccf8518f2`)

## Primary Sources Inspected

1. **Helmut Finner, Thorsten Dickhaus, & Markus Roters (2009)** — *On the false discovery rate and an asymptotically optimal rejection curve*, *The Annals of Statistics* 37(2):596–618, `DOI:10.1214/07-AOS569`, `arXiv:0903.5161v1`. Complete 24-page full-text PDF read (`sha256: f93ddc34225fa03697bd0d1e3ab98ca0878de9fcb3e092b0603136b6285725ff`), Crossref metadata (`sha256: f19c0022412bfd1ba3648625a0f537f20e6d47ac08ccc157baec76b90be66093`), and arXiv abstract (`sha256: edcb1378aed6555d8febb02d583c6826304f3e95d9e9d259e13eb7e00d03742f`).

## Candidate Decisions

- **`AIMech:AsymptoticallyOptimalRejectionCurveFDRControl`** (`ADD_CURATED`): Derivation of the Asymptotically Optimal Rejection Curve $f_\alpha(t) = t / (t(1-\alpha) + \alpha)$ and critical values $\alpha_{i:n} = i\alpha / (n - i(1-\alpha))$ from Dirac-uniform configurations (Section 3, Equation (3.1)), regularized step-up-down, tangent/secant linearly adjusted step-up, and truncated step-up procedures (Examples 3.1–3.3), finite-sample FDR upper bounds via conditional rejection-monotonicity (D1)–(D2) and the least isotonic majorant $\overline{q}(x)$ (Theorems 4.1–4.3), Glivenko–Cantelli crossing-point asymptotic FDR theorems and pointwise minimality / asymptotic power optimality of $f_\alpha$ over $\mathcal{M}_1$ (Theorems 5.1–5.5, Corollary 5.1), and finite-sample $\beta_n$-adjusted critical values $\alpha_{i:n}(\beta_n) = i\alpha / (n + \beta_n - i(1-\alpha))$ (Section 6, Equation (6.1)).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:AsymptoticallyOptimalRejectionCurveFDRControl",
  "primary_source": "Finner, Dickhaus, & Roters (2009), Annals of Statistics 37(2):596-618 (arXiv:0903.5161v1, DOI:10.1214/07-AOS569)",
  "section_3_and_figure_1_parameters": {
    "alpha": 0.05,
    "f_alpha_at_kappa_2": 0.94736842,
    "kappa_1_tangent_adjusted": 0.27452375,
    "kappa_2_secant_adjusted": 0.47368421,
    "x_star": 0.5
  },
  "section_5_asymptotic_optimality_comparison": {
    "fdr_aorc": 0.05,
    "fdr_lsu": 0.0125,
    "fdr_truncated_at_zeta_0_08": 0.04166667,
    "r_aorc": 0.78947368,
    "r_lsu": 0.75949367,
    "t_aorc": 0.15789474,
    "t_lsu": 0.03797468,
    "zeta": 0.25,
    "zeta_star_at_kappa_0_5": 0.0952381
  },
  "section_6_eq_6_1_beta_adjustment_verification": {
    "alpha": 0.05,
    "argmax_n0_beta_1_76": 15,
    "max_fdr_beta_1_0_step_up": 0.060123,
    "max_fdr_beta_1_76_step_up": 0.049959,
    "n": 100
  },
  "section_6_figure_2_finite_sample_benchmark": {
    "alpha": 0.05,
    "argmax_n0": 16,
    "fdr_at_n0_11": 0.051489,
    "fdr_at_n0_12": 0.054106,
    "fdr_at_n0_35": 0.051997,
    "fdr_at_n0_36": 0.051914,
    "max_fdr_at_n0_16": 0.058013,
    "n": 100,
    "paper_reported_max_fdr": 0.05801,
    "violating_n0_count": 34,
    "violating_n0_range": [
      11,
      44
    ]
  }
}
```
