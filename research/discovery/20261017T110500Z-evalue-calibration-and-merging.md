# Literature Discovery Report: E-Value Calibration and Merging

- **Report ID**: `20261017T110500Z-evalue-calibration-and-merging`
- **Created At**: `2026-10-17T11:05:00Z`
- **Curated Concept**: `AIMech:EValueCalibrationAndMerging` (`data/curated/EValueCalibrationAndMerging.yaml`, SHA-256 `f5246f4bae50e562eaa72b28da34d9ab2100831ad5a4e148447754f4debd2107`)
- **Verification Script**: `research/discovery/evalue-calibration-and-merging-boundaries.py` (SHA-256 `6222e8f15cfaddf4f5462c703a1511c323bebc52e72115d6bf6b88b1f2b9b571`)

## Primary Sources Inspected

1. **Vovk & Wang (2021)** — *E-values: Calibration, combination, and applications*, *The Annals of Statistics* 49(3):1736–1754, `arXiv:1912.06116` (DOI `https://doi.org/10.1214/20-AOS2020`). Complete full-text HTML conversion read (`sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda`).
2. **Vovk & Wang (2020)** — *Combining p-values via averaging*, *Biometrika* 107(4):791–808, `arXiv:1212.4966` (DOI `https://doi.org/10.1093/biomet/asaa027`). Complete full-text HTML conversion read (`sha256: 795de89f2d3ab8ce1a5c07046cce1fb85a097610b08ba7ffd661ddeae22a16a3`).

## Candidate Decisions

- **`AIMech:EValueCalibrationAndMerging`** (`ADD_CURATED`): Foundational statistical hypothesis testing and evidence synthesis framework (Vovk & Wang 2021) characterizing admissible $p$-to-$e$ and $e$-to-$p$ calibrators, arithmetic-mean essential domination and the minimal complete class $\lambda + (1-\lambda)M_K$ of symmetric e-merging functions under arbitrary dependence, U-statistic and product se-/ie-merging functions under test supermartingales, and $O(K^2)$ / $O(K)$ closed-testing family-wise valid multiple testing adjustments.

## Constructed Mathematical Verification Summary

```json
{
  "arbitrary_dependence_merging": {
    "arithmetic_mean_M_K": 2.0,
    "scaled_r_mean_values": {
      "r_0_5_square_root": 1.717717,
      "r_1_arithmetic_admissible": 2.0,
      "r_2_quadratic_scaled": 1.433721,
      "r_inf_max_scaled": 1.333333,
      "r_neg1_harmonic": 0.114286
    },
    "test_vector": [
      0.5,
      1.5,
      4.0
    ],
    "theorem_3_2_class_lambda_0_25": 1.75,
    "worst_case_coordinate_expectations": [
      1.0,
      1.0,
      1.0
    ]
  },
  "calibration_verification": {
    "e_to_p_tightness_at_alpha_0_05": 0.05,
    "mixture_calibrator_antiderivative_on_1e8_to_1": 0.945713,
    "mixture_calibrator_exact_integral": 1.0,
    "mixture_calibrator_quadrature_u25": 0.96,
    "power_calibrator_exact_integrals": {
      "kappa_0.25": 1.0,
      "kappa_0.5": 1.0,
      "kappa_0.75": 1.0
    },
    "vs_bound_partial_integral_eps_1e_100": 2.633091,
    "vs_bound_partial_integral_eps_1e_6": 1.598095
  },
  "closed_testing_algorithms": {
    "algorithm_1_adjusted_e_values": [
      0.4,
      0.6,
      0.9,
      2.175,
      4.425
    ],
    "algorithm_1_minimizing_prefix_counts_i": [
      0,
      1,
      2,
      3,
      3
    ],
    "algorithm_1_vs_bruteforce_max_abs_diff": 0.0,
    "algorithm_2_adjusted_e_values": [
      0.32,
      0.32,
      0.48,
      1.92,
      4.8
    ],
    "algorithm_2_vs_bruteforce_max_abs_diff": 0.0,
    "input_e_values": [
      0.4,
      0.8,
      1.5,
      6.0,
      15.0
    ],
    "naive_bonferroni_e_values": [
      0.08,
      0.16,
      0.3,
      1.2,
      3.0
    ]
  },
  "sequential_u_statistic_merging": {
    "sequential_tree_expectations": {
      "U_0": 1.0,
      "U_1": 1.0,
      "U_2": 1.0,
      "U_3_product": 1.0
    },
    "weak_domination_on_1_5_2_0_3_0": {
      "U_1": 2.166667,
      "U_2": 4.5,
      "U_3_product": 9.0
    }
  }
}
```
