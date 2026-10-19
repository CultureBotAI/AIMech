# Discovery Report: Round 308 — AltMinSense and AltMinComplete (Alternating Minimization for Low-Rank Matrix Sensing and Completion)

- **Timestamp**: `2026-10-19T06:08:00Z`
- **Selected Concept**: `AIMech:AltMinSenseAndAltMinCompleteAlternatingMinimizationForLowRankMatrixSensingAndCompletion` (*AltMinSense and AltMinComplete (Alternating Minimization for Low-Rank Matrix Sensing and Completion)*)
- **Record Path**: `data/curated/AltMinSenseAndAltMinCompleteAlternatingMinimizationForLowRankMatrixSensingAndCompletion.yaml`
- **Primary Source**: Prateek Jain, Praneeth Netrapalli, Sujay Sanghavi — *Low-rank Matrix Completion using Alternating Minimization* (`https://doi.org/10.1145/2488608.2488693`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 702 maintained AIMech concepts. Distinct from `AIMech:AltMinPhaseAndSparseAltMinPhaseAlternatingMinimizationPhaseRetrieval` (which alternates phase $c = \mathrm{Ph}(A x)$ and least-squares for vector phase retrieval) and `AIMech:NonconvexMatrixCompletionLandscapeWithoutSpuriousLocalMinima` / `AIMech:ProcrustesFlowForLowRankMatrixRecovery` (which analyze smooth gradient descent rather than exact alternating least-squares with QR orthonormalization and perturbed power-method operators $B^{-1}((U^t)^\top U^* B - C)$).

## Constructed Boundary & Regime Verification

```text
{"altminsense_final_frob_err": 1.2863743655007717e-15, "clipped_incoherence_bound": 1.226838, "concept": "AltMinSenseAndAltMinCompleteAlternatingMinimizationForLowRankMatrixSensingAndCompletion", "eq4_perturbed_power_identity_diff": 2.220446049250313e-15, "init_subspace_dist": 0.3137, "orthogonal_init_inner_product": 0.0, "status": "VERIFIED"}
```
