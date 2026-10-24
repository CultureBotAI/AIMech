# Literature Discovery Report: Projected Hotelling T-Squared Divide-and-Combine Confidence Region

- **Report ID**: `20261017T105000Z-projected-hotelling-t2-divide-and-combine`
- **Created At**: `2026-10-17T10:50:00Z`
- **Curated Concept**: `AIMech:ProjectedHotellingT2DivideAndCombineConfidenceRegion` (`data/curated/ProjectedHotellingT2DivideAndCombineConfidenceRegion.yaml`, SHA-256 `e90c5c9448b52371dbe720d48eebd14211970a06202b343e255f35248e7101f0`)
- **Verification Script**: `research/discovery/projected-hotelling-t2-divide-and-combine-boundaries.py` (SHA-256 `c7088a2983726ad8a61ef831944d7072e4e000b433fb5686ecfcdf4bc616a793`)

## Primary Sources Inspected

1. **Liu, Meng, & Pillai (2025)** — *Half-Cauchy Combination Method for Versatile Divide-and-Combine Confidence Regions*, `arXiv:2501.01065v1` (DOI `https://doi.org/10.48550/arXiv.2501.01065`). Complete full-text HTML conversion read (`sha256: 2fe912b58a74ff5008a52f8f319cef872ffe8f0510fbadb94f14d7cbe265f6e3`).
2. **Fang, Chang, Park, & Tseng (2023)** — *Heavy-tailed distribution for combining dependent p-values with asymptotic robustness*, `arXiv:2103.12967` (*Statistica Sinica* 33, 1115–1142, DOI `https://doi.org/10.5705/ss.202021.0078`). Complete full-text HTML conversion read (`sha256: 432b18ec119b33e5b3cd66b32bb71015a243bb7dd28362cf7c9557f0e78a8402`).

## Candidate Decisions

- **`AIMech:ProjectedHotellingT2DivideAndCombineConfidenceRegion`** (`ADD_CURATED`): Multivariate divide-and-combine confidence region methodology (Liu, Meng, & Pillai 2025) that projects parameter vector $\boldsymbol{\theta} \in \mathbb{R}^d$ into $m$ lower-dimensional subspaces $\boldsymbol{P}_j \boldsymbol{\theta} \in \mathbb{R}^{d_j}$, calibrates sub-study quadratic forms via Hotelling's $T^2(d_j, k_j)$, and inverts the Half-Cauchy combination test to produce guaranteed convex, compact confidence regions when $k_j \ge d_j + 1$ without global $d \times d$ covariance inversion.

## Constructed Mathematical Verification Summary

```json
{
  "conflict_diagnostic_and_stopping_time_downweighting": {
    "downweighted_min_T": 6.005673,
    "downweighted_region_non_empty": true,
    "equal_weight_min_T": 10.804618,
    "equal_weight_region_empty": true,
    "inequality_3_7_lower_bound": 1.333333,
    "stopping_iterations_tau": 3
  },
  "example1_cct_vs_hcct": {
    "alpha": 0.05,
    "cct_connected_components": 3,
    "critical_value": 6.313752,
    "hcct_connected_components": 1,
    "hcct_interval": [
      -0.067904,
      0.067904
    ],
    "hcct_min_at_zero": 2.901421
  },
  "high_dim_small_n_divide_and_combine": {
    "classical_hotelling_t2_applicable": false,
    "d": 6,
    "degrees_of_freedom_k_j": 3,
    "global_sample_cov_max_rank": 3,
    "midpoint_convexity_slack": 1.036215,
    "n": 4,
    "num_projections_m": 3,
    "sub_covariance_determinants": [
      9.826e-05,
      1.997e-05,
      2.413e-05
    ],
    "subspace_dim_d_j": 2,
    "theorem_3_2_condition_k_ge_d_plus_1": true,
    "unit_contrast_directional_radius_95": 0.533575
  }
}
```
