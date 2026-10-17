# Literature Discovery Report: Half-Cauchy Combination Test

- **Report ID**: `20261017T093500Z-half-cauchy-combination-test`
- **Created At**: `2026-10-17T09:35:00Z`
- **Curated Concept**: `AIMech:HalfCauchyCombinationTest` (`data/curated/HalfCauchyCombinationTest.yaml`, SHA-256 `16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e`)
- **Verification Script**: `research/discovery/half-cauchy-combination-test-boundaries.py` (SHA-256 `0263679759caeb837b0ee68bb7783d0b9566370eee9fa0a28052967a77e73991`)

## Primary Sources Inspected

1. **Liu, Meng, & Pillai (2025)** — *A Heavily Right Strategy for Integrating Dependent Studies in Any Dimension*, `arXiv:2501.01065v1` (DOI `https://doi.org/10.48550/arXiv.2501.01065`). Complete full-text HTML conversion read (`sha256: 2fe912b58a74ff5008a52f8f319cef872ffe8f0510fbadb94f14d7cbe265f6e3`).
2. **Yang, Nott, & Presanis (2026)** — *Detecting Conflicts in Evidence Synthesis Models Using Score Discrepancies*, `arXiv:2511.02977v2` (DOI `https://doi.org/10.48550/arXiv.2511.02977`). Complete 52-page PDF read (`sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d`).

## Candidate Decisions

- **`AIMech:HalfCauchyCombinationTest`** (`ADD_CURATED`): Statistical $p$-value combination method transforming $p_1, \dots, p_m$ into non-negative standard Half-Cauchy variables $\tan((1 - p_j)\pi/2)$, preventing cancellation by large $p$-values near 1, guaranteeing strictly convex confidence regions under Gaussian test inversion, and maintaining asymptotic tail equivalence under pairwise quasi-asymptotic independence or bivariate normal correlations.

## Constructed Mathematical Verification Summary

```json
{
  "example1_confidence_sets": {
    "cct_disconnected_positive_roots": [
      0.1038,
      0.1212,
      0.1277
    ],
    "cct_q95": 6.313752,
    "eq37_inconsistency_lower_bound": 0.795775,
    "hcct_connected_95_interval": [
      -0.1015,
      0.1015
    ],
    "hcct_min_at_zero": 2.901421,
    "hcct_q95": 13.687511
  },
  "landau_domain_of_attraction_shift": {
    "landau_shift_equal_weights": 3.200895,
    "landau_shift_harmonic_weights": 2.612409,
    "m": 100
  },
  "large_p_insensitivity": {
    "T_CCT": -127.326049,
    "T_HCCT": 63.661454,
    "p1": 0.005,
    "p2": 0.999,
    "p_value_CCT": 0.99750009,
    "p_value_HCCT": 0.01024157
  }
}
```
