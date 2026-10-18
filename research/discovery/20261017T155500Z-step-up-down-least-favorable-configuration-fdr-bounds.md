# Literature Discovery Report: Step-Up-Down Least Favorable Configuration and Two-Population Steck FDR Bounds

- **Report ID**: `20261017T155500Z-step-up-down-least-favorable-configuration-fdr-bounds`
- **Created At**: `2026-10-17T15:55:00Z`
- **Curated Concept**: `AIMech:StepUpDownLeastFavorableConfigurationFDRBounds` (`data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml`, SHA-256 `364829550c002d6abacfff66a6b7f140112c4985d9e1148925c2e81ea34a0342`)
- **Verification Script**: `research/discovery/step-up-down-least-favorable-configuration-fdr-bounds-boundaries.py` (SHA-256 `bc5c1e73bdf0ad38b5e1c0a9b58781cd7ee995b6cff434bb7aba6dc69f509e17`)

## Primary Sources Inspected

1. **Gilles Blanchard, Thorsten Dickhaus, Etienne Roquain, & Fanny Villers (2014)** — *On least favorable configurations for step-up-down tests*, *Statistica Sinica* 24(1):1–23, `DOI:10.5705/ss.2011.205`, `arXiv:1108.5262v1`. Complete 33-page full-text PDF read (`sha256: 3276246bf48077619f74aa42f44a9707d4dab17309e1fb1377814a3321453bd1`), full-text ar5iv HTML conversion (`sha256: ff44c60469e2615968d6008f77ade067d262e89dd3854daf870f371c727ac4aa`), Crossref metadata (`sha256: b5a8c00ddcee85cd3f63afdadbd4b1313692f2afb9c65184c662c9dfda69580b`), and arXiv abstract (`sha256: 3a141ad1099f65a122b41b04ca60754c794d396a3011dfb77cb10de14fc7a4a2`).

## Candidate Decisions

- **`AIMech:StepUpDownLeastFavorableConfigurationFDRBounds`** (`ADD_CURATED`): Two-population generalized Steck recursion for order statistics from heterogeneous null/alternative populations (Proposition 5.1, Theorem 5.2, Corollary 5.3), exact finite-sample disproof of the Dirac-uniform LFC conjecture for intermediate linear step-up-down procedures `LSUD_lambda` (Proposition 4.1), continuous fixed-point bracketing `U(ell, G)` (Lemma 4.3), and non-asymptotic Dvoretzky–Kiefer–Wolfowitz perturbation upper bounds and `O((1 - zeta_m)^(-1) sqrt((log m)/m))` convergence rates for linear and AORC rejection curves (Theorem 4.4, Corollary 4.5).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:StepUpDownLeastFavorableConfigurationFDRBounds",
  "lemma_4_3_figure_6_bracketing": {
    "k_hat_over_m_lam4": 0.7,
    "k_hat_over_m_lam8": 0.7,
    "u_lam4_lower": 0.4,
    "u_lam4_upper": 0.8,
    "u_lam8_lower": 0.7
  },
  "lemma_b_1_extreme_sd_exceeds_su": {
    "critical_t0": 0.158018,
    "fdr_sd": 0.790285,
    "fdr_su": 0.7,
    "t0": 0.2
  },
  "primary_source": "Blanchard, Dickhaus, Roquain, & Villers (2014), Statistica Sinica 24(1):1-23 (arXiv:1108.5262v1, DOI:10.5705/ss.2011.205)",
  "proposition_4_1_counterexample": {
    "alpha": 0.5,
    "counterexample_lambdas_fm": [
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "counterexample_lambdas_rm": [
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "fm_fdr_dirac_uniform": {
      "1": 0.32985,
      "10": 0.35,
      "2": 0.32985,
      "3": 0.32985,
      "4": 0.32985,
      "5": 0.336128,
      "6": 0.342451,
      "7": 0.346717,
      "8": 0.348944,
      "9": 0.349806
    },
    "fm_fdr_uniform_alt": {
      "1": 0.280884,
      "10": 0.35,
      "2": 0.320328,
      "3": 0.33568,
      "4": 0.342981,
      "5": 0.346685,
      "6": 0.348561,
      "7": 0.349461,
      "8": 0.349844,
      "9": 0.349974
    },
    "m": 10,
    "m0": 7,
    "rm_fdr_dirac_uniform": {
      "1": 0.324164,
      "10": 0.35,
      "2": 0.325755,
      "3": 0.329258,
      "4": 0.33406,
      "5": 0.339161,
      "6": 0.34364,
      "7": 0.34693,
      "8": 0.348897,
      "9": 0.349774
    },
    "rm_fdr_uniform_alt": {
      "1": 0.280884,
      "10": 0.35,
      "2": 0.320328,
      "3": 0.33568,
      "4": 0.342981,
      "5": 0.346685,
      "6": 0.348561,
      "7": 0.349461,
      "8": 0.349844,
      "9": 0.349974
    }
  },
  "theorem_4_4_and_corollary_4_5_rates": {
    "100": {
      "delta_m": 0.172838,
      "fdr_excess_upper_bound_linear": 0.195683,
      "scaled_by_sqrt_log_m_over_m": 0.911863
    },
    "1000": {
      "delta_m": 0.060812,
      "fdr_excess_upper_bound_linear": 0.056525,
      "scaled_by_sqrt_log_m_over_m": 0.680098
    },
    "10000": {
      "delta_m": 0.021661,
      "fdr_excess_upper_bound_linear": 0.019789,
      "scaled_by_sqrt_log_m_over_m": 0.652057
    },
    "100000": {
      "delta_m": 0.007607,
      "fdr_excess_upper_bound_linear": 0.007018,
      "scaled_by_sqrt_log_m_over_m": 0.654045
    }
  }
}
```
