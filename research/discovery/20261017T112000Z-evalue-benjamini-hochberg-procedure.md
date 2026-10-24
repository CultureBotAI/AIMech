# Literature Discovery Report: E-Value Benjamini-Hochberg Procedure

- **Report ID**: `20261017T112000Z-evalue-benjamini-hochberg-procedure`
- **Created At**: `2026-10-17T11:20:00Z`
- **Curated Concept**: `AIMech:EValueBenjaminiHochbergProcedure` (`data/curated/EValueBenjaminiHochbergProcedure.yaml`, SHA-256 `a9553e05b33722aab92042bef82fe67208d2ddb565f7133125bdb2cb79b27057`)
- **Verification Script**: `research/discovery/evalue-benjamini-hochberg-procedure-boundaries.py` (SHA-256 `1d31fa066cc9b75f87cf6456f126c5f4e16d31e65252a9b1708448954dc57934`)

## Primary Sources Inspected

1. **Wang & Ramdas (2022)** — *False discovery rate control with e-values*, *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 84(3):822–852, `arXiv:2009.02824` (DOI `https://doi.org/10.1111/rssb.12489`). Complete full-text HTML conversion read (`sha256: 26bd39717641ca16a7b1bbfc1d1e962853428ad3fbcbf6a82687bfa6536e901c`).
2. **Vovk & Wang (2021)** — *E-values: Calibration, combination, and applications*, *The Annals of Statistics* 49(3):1736–1754, `arXiv:1912.06116` (DOI `https://doi.org/10.1214/20-AOS2020`). Complete full-text HTML conversion read (`sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda`).

## Candidate Decisions

- **`AIMech:EValueBenjaminiHochbergProcedure`** (`ADD_CURATED`): Step-down e-value multiple hypothesis testing procedure (Wang & Ramdas 2022) controlling the false discovery rate (FDR) at level $\alpha K_0 / K$ under arbitrary dependence without any logarithmic Benjamini–Yekutieli penalty, featuring discrete grid-truncation boosting under arbitrary dependence and PRDS, self-consistent post-selection and structured testing, optimality among monotone e-value transforms, and unification of BH and BY via p-to-e calibration.

## Constructed Mathematical Verification Summary

```json
{
  "boosting_examples": {
    "example_2_exact_y_alpha_K100": 0.048703,
    "example_2_power_ad_b": 6.324555,
    "example_3_gaussian_ad_b": {
      "delta_3": 1.373374,
      "delta_4": 1.11197
    },
    "example_5_power_prds_b": 8.944272,
    "example_6_gaussian_prds_b": {
      "delta_3": 7.881002,
      "delta_4": 10.321968
    }
  },
  "example_4_sharpness": {
    "K": 5,
    "K0": 3,
    "alpha": 0.05,
    "exact_fdr": 0.03,
    "null_e_value_expectation": 1.0,
    "theoretical_upper_bound": 0.03
  },
  "optimality_and_calibration": {
    "proposition_4_K": 6,
    "proposition_4_alpha_times_l_K": 0.1225,
    "proposition_4_harmonic_l_K": 2.45,
    "proposition_4_y_psi": 0.1225,
    "theorem_5_ebh_threshold": 60.0,
    "theorem_5_induced_fdr": 0.066667,
    "theorem_5_k0": 2,
    "theorem_5_violating_m_prime": 45.0
  },
  "stepdown_and_postselection": {
    "alpha": 0.05,
    "k_star": 3,
    "post_selection_amended_alpha": 0.04,
    "post_selection_rejected_0based": [
      2,
      3,
      4
    ],
    "post_selection_subset_size": 4,
    "rejected_0based": [
      2,
      3,
      4
    ],
    "t_alpha": 33.333333,
    "test_vector": [
      0.8,
      12.0,
      34.0,
      55.0,
      90.0
    ]
  }
}
```
