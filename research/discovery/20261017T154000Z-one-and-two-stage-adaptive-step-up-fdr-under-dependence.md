# Literature Discovery Report: One-Stage and Two-Stage Adaptive Step-Up Procedures for False Discovery Rate Control under Independence and Dependence

- **Report ID**: `20261017T154000Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence`
- **Created At**: `2026-10-17T15:40:00Z`
- **Curated Concept**: `AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence` (`data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml`, SHA-256 `651276db83f388cdf782125e0ac769bacdb09ce89e63ebf1e9378b3a0d36d91f`)
- **Verification Script**: `research/discovery/one-and-two-stage-adaptive-step-up-fdr-under-dependence-boundaries.py` (SHA-256 `2f6a3346c39be738333ae9b9ec214ced7192718d3ecb781afbfcb9997117f1b1`)

## Primary Sources Inspected

1. **Gilles Blanchard & Etienne Roquain (2009)** — *Adaptive False Discovery Rate Control under Independence and Dependence*, *Journal of Machine Learning Research* 10:2837–2871, `arXiv:0707.0536v3`. Complete full-text HTML conversion read (`sha256: aacce975911525720fafd136396a274f0b7afcbd9fc579bf5430478f5a791cd3`) and arXiv abstract (`sha256: 3670e39f2766195b8e4bdc30d402e063944b1d2e1fc1c588fcdcf46247ebd90e`).

## Candidate Decisions

- **`AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence`** (`ADD_CURATED`): One-stage piecewise inverse-volume step-up procedure `BR-1S-lambda` and Gaussian signal threshold `mu*` (Theorem 3.1, Lemma 2), unified coordinate-wise non-increasing self-consistent plug-in theorem and two-stage `BR-2S-lambda` dominance over `BKY06-lambda` (Theorem 3.2, Corollary 1), exact comonotonic maximal-dependence FDR formulas and `lambda = alpha` tuning robustness (Proposition 1), and two-stage FWER+FDR and Markov-inequality `F_kappa` FDR+FDR adaptive step-up procedures under PRDS and arbitrary dependence (Lemma 3, Theorems 4.1–4.2).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence",
  "primary_source": "Blanchard & Roquain (2009), Journal of Machine Learning Research 10:2837-2871 (arXiv:0707.0536v3)",
  "section_3_1_br_1s_and_lemma_2": {
    "alpha": 0.05,
    "asymptotic_lsu_rej_prop_mu_1_2": 0.008,
    "asymptotic_lsu_rej_prop_mu_2_0": 0.184,
    "br_1s_alpha_thresholds_first5": [
      0.00475,
      0.010556,
      0.017813,
      0.027143,
      0.039583
    ],
    "lemma_2_mu_star_pi0_05_alpha_005": 1.511105,
    "lsu_thresholds_first5": [
      0.005,
      0.01,
      0.015,
      0.02,
      0.025
    ],
    "m": 10,
    "max_fdr_br_1s_alpha": 0.04649744
  },
  "section_3_2_plug_in_hierarchy": {
    "G1_storey": 1.6,
    "G3_bky06": 1.142857,
    "G4_br2s": 1.333333,
    "alpha": 0.05,
    "first_stage_r0_br1s_count": 5,
    "first_stage_r0_lsu_count": 4,
    "lambda": 0.05,
    "m": 10,
    "max_ratio_E_G1_times_pi0": 1.0,
    "second_stage_rejections": {
      "BKY06_alpha": 2,
      "BR_2S_alpha": 3,
      "LSU": 1,
      "Storey_alpha": 4
    }
  },
  "section_3_3_maximal_dependence": {
    "alpha": 0.05,
    "fdr_bky06_alpha": 0.05,
    "fdr_br_1s_alpha": 0.05,
    "fdr_br_2s_alpha": 0.05,
    "fdr_quant_k0_opt": 0.05,
    "fdr_quant_median": 0.083333,
    "fdr_storey_1_2": 0.5,
    "fdr_storey_alpha": 0.05,
    "lambda_1": 0.045455,
    "lambda_2": 0.5,
    "m": 20
  },
  "section_4_dependence_theorems_4_1_and_4_2": {
    "crossover_proportion_F2_inv_2": 0.625,
    "kappa": 2.0,
    "low_pi0_example_m20_m0_2": {
      "f2_factor": 3.414214,
      "r0_holm_count": 15,
      "r0_lsu_alpha_over_4_count": 15,
      "rejections_non_adaptive_lsu": 15,
      "rejections_theorem_4_1": 18,
      "rejections_theorem_4_2": 18
    },
    "markov_factor_exact_equality_checked": true
  }
}
```
