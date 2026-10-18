# Literature Discovery Report: Exact Step-Up and Step-Down False Discovery Proportion Moment Formulas and Least Favorable Configuration Analysis

- **Report ID**: `20261017T161500Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis`
- **Created At**: `2026-10-17T16:15:00Z`
- **Curated Concept**: `AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis` (`data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml`, SHA-256 `d58e0d5d29e1c28fe4115471e06c8d76d0f66c4265c51c4cf4f33134c4091593`)
- **Verification Script**: `research/discovery/exact-step-up-step-down-fdp-moments-and-lfc-analysis-boundaries.py` (SHA-256 `95c4d9b1902b15d3bf177024d9bc7999edf79656e7084241d1fc87649c7043f1`)

## Primary Sources Inspected

1. **Etienne Roquain & Fanny Villers (2011)** — *Exact calculations for false discovery proportion with application to least favorable configurations*, *The Annals of Statistics* 39(1):584–612, `DOI:10.1214/10-AOS847`, `arXiv:1002.2845v2`. Complete 28-page full-text PDF read (`sha256: 363776dd96ab56cb24dcbee7bd09b88d2809d0b07076554ecad504a55fe1303d`), full-text ar5iv HTML conversion (`sha256: 3e487cf3fae9c8bd51998eeb36fb15ea701384d3a9c8f6c2f422b887e5679b42`), Crossref metadata (`sha256: 80297b7f626cb3769379ba12c3fcf3c85c2d54b247f630e7acf366d3e6278e48`), and arXiv abstract (`sha256: b211939e19d7d28a8f619a5c6c7c1c8dbae95748267bdbc62285e9ad88cb1cd2`).

## Candidate Decisions

- **`AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis`** (`ADD_CURATED`): Conditional binomial distribution of false rejections given total step-up rejections and Stirling-number s-th moment formula for the FDP (Theorem 3.1, Equations (11)–(15)), non-binomial conditional law and exact step-down FDR expansion with Finner–Roters Dirac-uniform LSD formula (Theorem 3.2, Equations (16)–(21)), equicorrelated Gaussian conditioning and negative-correlation counterexample attaining the full Benjamini–Yekutieli bound (Corollaries 3.4–3.5, Proposition 3.6, Equations (25)–(26)), Condition (A) for step-down Dirac-uniform LFCs over concave alternatives (Theorem 4.1, Equation (24)), and exact closed-form minimum and maximum of Var[FDP(LSU)] (Theorem 4.3, Equations (28)–(30)).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis",
  "primary_source": "Roquain & Villers (2011), Annals of Statistics 39(1):584-612 (arXiv:1002.2845v2, DOI:10.1214/10-AOS847)",
  "proposition_3_6_negative_correlation_counterexample": {
    "alpha": 0.05,
    "benjamini_yekutieli_upper_bound": 0.0375,
    "dirac_uniform_fdr": 0.025,
    "fdr_lsu_at_rho_minus_1": 0.0375,
    "m": 2,
    "m0": 1
  },
  "theorem_3_1_moments_verification": {
    "alpha": 0.25,
    "m": 5,
    "moments_1_to_4": {
      "1": {
        "conditional_binomial_eq11": 0.15,
        "stirling_formula_eq13": 0.15
      },
      "2": {
        "conditional_binomial_eq11": 0.1170884792,
        "stirling_formula_eq13": 0.1170884792
      },
      "3": {
        "conditional_binomial_eq11": 0.101398793,
        "stirling_formula_eq13": 0.101398793
      },
      "4": {
        "conditional_binomial_eq11": 0.0934439164,
        "stirling_formula_eq13": 0.0934439164
      }
    },
    "pi0": 0.6,
    "s3_omitting_stirling_factor_3": 0.0875851833,
    "s3_stirling_correction_magnitude": 0.0138136097
  },
  "theorem_3_2_step_down_verification": {
    "lsd_fdr_m6_pi07_alpha02_dirac_eq20": 0.1346047661,
    "lsd_fdr_m6_pi07_alpha02_dirac_eq21": 0.1346047661,
    "lsd_fdr_m6_pi07_alpha02_sqrt": 0.1259581312,
    "lsd_fdr_m6_pi07_alpha02_uniform": 0.1288390608,
    "non_binomial_conditional_l1_gap": 0.12385118
  },
  "theorem_4_1_condition_a_and_su_vs_sd_lfc_split": {
    "eq34_max_discrepancy": 0.03895035,
    "fdr_sd_concave_t_dirac_f1": 0.41564914,
    "fdr_sd_concave_t_uniform_f1": 0.34753598,
    "fdr_su_concave_t_dirac_f1": 0.453016,
    "fdr_su_concave_t_uniform_f1": 0.45956142,
    "q_concave_t_m5": [
      0.11466412,
      0.13277095,
      0.14706628,
      0.16120651,
      0.18
    ],
    "s_lsd_m6_alpha02_recursion_eq34": [
      0.87484276,
      0.94031958,
      0.96827094,
      0.98363858,
      0.99333333,
      1.0
    ],
    "s_lsd_m6_alpha02_true": [
      0.9137931,
      0.95108711,
      0.97138902,
      0.98431953,
      0.99333333,
      1.0
    ]
  },
  "theorem_4_3_fdp_variance_extrema": {
    "small_m6_pi07_alpha02": {
      "sd_max": 0.3469870315,
      "sd_min": 0.2372800877,
      "sd_min_concave": 0.3367491648,
      "var_max_eq30": 0.1204,
      "var_min_concave": 0.1134,
      "var_min_eq29": 0.05630184
    },
    "sparse_m10000_pi099_alpha005": {
      "sd_max": 0.21691,
      "sd_min": 0.021685,
      "sd_min_concave": 0.216852,
      "var_max": 0.04704975,
      "var_min": 0.00047025
    }
  }
}
```
