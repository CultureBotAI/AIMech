# Literature Discovery Report: Exact Harmonic Mean P-Value Combination Test

- **Report ID**: `20261017T095800Z-exact-harmonic-mean-pvalue`
- **Created At**: `2026-10-17T09:58:00Z`
- **Curated Concept**: `AIMech:ExactHarmonicMeanPValueTest` (`data/curated/ExactHarmonicMeanPValueTest.yaml`, SHA-256 `e37fe73ff6637f2951762fe4cceca81cd277e7f3d8dafaad63ca150e314a9793`)
- **Verification Script**: `research/discovery/exact-harmonic-mean-pvalue-boundaries.py` (SHA-256 `9a622dc1dc2eb9d6c36fdc7c9076c2bb253092422bf0ff4489f9e1fbf192782a`)

## Primary Sources Inspected

1. **Liu, Meng, & Pillai (2025)** — *A Heavily Right Strategy for Integrating Dependent Studies in Any Dimension*, `arXiv:2501.01065v1` (DOI `https://doi.org/10.48550/arXiv.2501.01065`). Complete full-text HTML conversion read (`sha256: 2fe912b58a74ff5008a52f8f319cef872ffe8f0510fbadb94f14d7cbe265f6e3`).

## Candidate Decisions

- **`AIMech:ExactHarmonicMeanPValueTest`** (`ADD_CURATED`): Statistical $p$-value combination method aggregating $p_1, \dots, p_m$ via weighted reciprocal Pareto(1, 1) variables $T_{\text{HMP}}(\mathbf{p}) = \sum_{j=1}^m w_j / p_j$, evaluating exact finite-$m$ unequal-weight null distributions via Laplace-transform contour integration with second-order exponential integrals and Ramanujan's scaled series (Theorem A.1), transitioning to the unequal-weight Landau limit (Theorem A.2), and yielding strictly convex confidence regions under test inversion (Theorem A.3).

## Constructed Mathematical Verification Summary

```json
{
  "exact_m2_pareto_convolution": {
    "cdf_x5_equal_weights": 0.75605551,
    "cdf_x5_unequal_weights_02_08": 0.7690478,
    "q95_equal_weights": 21.725333,
    "q95_unequal_weights_01_09": 20.731245
  },
  "example1_convex_confidence_interval": {
    "ehmp_connected_95_interval": [
      -0.1012,
      0.1012
    ],
    "ehmp_min_at_zero": 4.732618
  },
  "landau_domain_of_attraction_shift": {
    "landau_shift_equal_weights": 5.027955,
    "landau_shift_harmonic_weights": 4.103562,
    "m": 100
  },
  "large_p_insensitivity": {
    "T_EHMP": 100.500501,
    "p1": 0.005,
    "p2": 0.999,
    "p_value_EHMP": 0.01021248
  }
}
```
