# Literature Discovery Report: Simultaneous Pathwise False Discovery Proportion Bounds

- **Report ID**: `20261017T141500Z-simultaneous-pathwise-false-discovery-proportion-bounds`
- **Created At**: `2026-10-17T14:15:00Z`
- **Curated Concept**: `AIMech:SimultaneousPathwiseFalseDiscoveryProportionBounds` (`data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml`, SHA-256 `4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de`)
- **Verification Script**: `research/discovery/simultaneous-pathwise-false-discovery-proportion-bounds-boundaries.py` (SHA-256 `b4f6273c45f9dcb44f79bcf7bc052cb797e4b023ccb4abde527ecdd328438c77`)

## Primary Sources Inspected

1. **Katsevich & Ramdas (2020)** — *Simultaneous high-probability bounds on the false discovery proportion in structured, regression, and online settings*, *The Annals of Statistics* 48(6):3465–3487, `DOI:10.1214/19-AOS1938`, `arXiv:1803.06790v5`. Complete full-text HTML conversion read (`sha256: b636ac1329528fa685c8d178398956826d9f3aa85206cc2ad9b24cd38dc234b7`), Crossref metadata (`sha256: 1a675bc830c88194d805a099b2bba29feaf62becd3a0ebfbc1e94b3c1bdde309`), and arXiv abstract (`sha256: 84e6c38e4fb79aec2eebe8489d5aa3152b258aa28b07bf3705b742d8417abc51`).

## Candidate Decisions

- **`AIMech:SimultaneousPathwiseFalseDiscoveryProportionBounds`** (`ADD_CURATED`): Simultaneous finite-sample high-probability upper bounds on the false discovery proportion across sorted, interactive, knockoff, and online rejection paths with closed-testing interpolation (Katsevich & Ramdas 2020).

## Constructed Mathematical Verification Summary

```json
{
  "claim1_sorted_path_and_poisson_lemma": {
    "alpha_cutoff_at_x_1_5": 0.318532,
    "c_sort_alpha_0_10": 1.927324,
    "mc_global_null_violation_rate": 0.056667,
    "mc_unadjusted_violation_rate": 1.0,
    "v_bar_dkw_intermediate": 66.0,
    "v_bar_robbins_intermediate": 125.0,
    "v_bar_sort_intermediate": 26.0
  },
  "claim2_lemma1_and_knockoff_simultaneous_fdp": {
    "c_backward_alpha_0_05": 20.0,
    "c_knockoff_alpha_0_05": 4.485775,
    "mc_knockoff_simultaneous_violation_rate": 0.006,
    "sm_factor_case1": 1.0,
    "sm_factor_case2": 1.0,
    "sm_factor_case3": 1.0
  },
  "claim3_interactive_path_power_and_coverage": {
    "avg_discoveries_interactive_fdp_0_20": 32.335,
    "avg_discoveries_sorted_fdp_0_20": 24.8425,
    "interactive_violation_rate": 0.0225
  },
  "claim4_online_posthoc_and_correlation_boundary": {
    "correlated_rho_0_90_q90_max_ratio": 11.333333,
    "correlated_rho_0_90_violation_rate": 0.23,
    "online_adaptive_violation_rate": 0.001,
    "online_simple_violation_rate": 0.001
  }
}
```
