# Discovery Report: Round 296 — PhaseLift Convex Semidefinite Programming Matrix-Lifting for Phase Retrieval

- **Timestamp**: `2026-10-19T05:44:00Z`
- **Selected Concept**: `AIMech:PhaseLiftConvexSemidefiniteProgrammingPhaseRetrieval` (*PhaseLift Convex Semidefinite Programming Matrix-Lifting for Phase Retrieval*)
- **Record Path**: `data/curated/PhaseLiftConvexSemidefiniteProgrammingPhaseRetrieval.yaml`
- **Primary Source**: Emmanuel J. Candes, Thomas Strohmer, Vladislav Voroninski — *PhaseLift: Exact and Stable Signal Recovery from Magnitude Measurements via Convex Programming* (`https://doi.org/10.1002/cpa.21432`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 690 maintained AIMech concepts. Distinct from `AIMech:WirtingerFlowPhaseRetrievalAndSpectralInitialization` (Candès, Li, & Soltanolkotabi 2015) and `AIMech:TruncatedWirtingerFlowAndTruncatedSpectralInitializationForQuadraticSystems` (Chen & Candès 2017), which operate directly in the nonconvex vector space $\mathbb{C}^n$ via spectral initialization and Wirtinger gradient descent rather than convex semidefinite matrix lifting $\boldsymbol{X} = \boldsymbol{x}\boldsymbol{x}^* \succeq \boldsymbol{0}$.

## Constructed Boundary & Regime Verification

```text
{
  "rank2_l1_isometry_lemmas": {
    "f_real_at_0": 1.0,
    "f_real_at_1": 1.27323954,
    "min_f_real_on_0_1": 0.941032,
    "min_f_complex_on_0_1": 0.828428,
    "exact_2_sqrt2_minus_1": 0.828427
  },
  "dual_certificate_moments": {
    "S_S_inv_max_err": 0.0
  },
  "phaselift_sdp_recovery": {
    "n": 5,
    "m": 45,
    "matrix_frob_err": 0.0,
    "signal_vec_err": 0.0,
    "top_eigenvalue_ratio": 1.0
  },
  "all_assertions_passed": true
}
```
