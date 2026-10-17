# Literature Discovery Report: Mixture-Approximation Node-Splitting Conflict Diagnostic

- **Report ID**: `20261017T085200Z-mixture-node-splitting-conflict`
- **Created At**: `2026-10-17T08:52:00Z`
- **Curated Concept**: `AIMech:MixtureApproximationNodeSplittingDiagnostic` (`data/curated/MixtureApproximationNodeSplittingDiagnostic.yaml`, SHA-256 `28fef075fcf205209c1ea251fc3d23aa34529d2f34b0087f18eb6d5690750952`)
- **Verification Script**: `research/discovery/mixture-node-splitting-boundaries.py` (SHA-256 `13fa366f8762fcaf0d34513077b597618ca6db28b94291ce7b4190c95493bca7`)

## Primary Sources Inspected

1. **Yang, Nott, & Presanis (2026)** — *Conflict Diagnostics for Directed Acyclic Graphical Models with Application to Infectious Disease Modelling*, `arXiv:2511.02977v2` (DOI `https://doi.org/10.48550/arXiv.2511.02977`). Complete 52-page PDF read (`sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d`).
2. **Presanis, Ohlssen, Spiegelhalter, & De Angelis (2013)** — *Conflict Diagnostics in Directed Acyclic Graphical Models, with Applications in Evidence Synthesis*, *Statistical Science* 28(3):376–397, `arXiv:1310.0628v1` (DOI `https://doi.org/10.1214/13-STS426`). Complete 22-page PDF read (`sha256: 9cff5092b47d7ba20f9ae654b6ea63bd4fdf75ea8ccfdb663427ccab36f3d3a0`).

## Candidate Decisions

- **`AIMech:MixtureApproximationNodeSplittingDiagnostic`** (`ADD_CURATED`): Bayesian DAG node-splitting conflict diagnostic (Algorithm 2, Section 3.2, p. 20) that approximates parent-side and child-side split posteriors of a duplicated separator block by Gaussian mixtures while propagating shared parent-parameter uncertainty, forms the closed-form convolved Gaussian mixture density of their difference, and evaluates the density-level tail probability at zero without nonparametric kernel density estimation.

## Constructed Mathematical Verification Summary

```json
{
  "limits": "Constructed analytic Gaussian mixture convolution and deterministic quadrature checks only; no EM fitting, MCMC sampling, or real-data epidemic model execution.",
  "multimodal_mixture_vs_single_gaussian": {
    "mixture_density_at_mode": 0.19947114,
    "mixture_density_at_zero": 0.00443185,
    "mixture_density_level_p": 0.00289893,
    "single_gaussian_mahalanobis_p": 1.0
  },
  "shared_nuisance_pairing_boundary": {
    "p_paired": 0.04550026,
    "p_unpaired": 0.37109337,
    "var_paired": 1.0,
    "var_unpaired": 5.0,
    "variance_inflation_ratio": 5.0
  }
}
```
