# Discovery Report: Round 298 — Truncated Amplitude Flow and Orthogonality-Promoting Initialization for Random Quadratic Equations

- **Timestamp**: `2026-10-19T05:48:00Z`
- **Selected Concept**: `AIMech:TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations` (*Truncated Amplitude Flow and Orthogonality-Promoting Initialization for Random Quadratic Equations*)
- **Record Path**: `data/curated/TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations.yaml`
- **Primary Source**: Gang Wang, Georgios B. Giannakis, Yonina C. Eldar — *Solving Systems of Random Quadratic Equations via Truncated Amplitude Flow* (`https://doi.org/10.1109/TIT.2017.2756858`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 692 maintained AIMech concepts. Distinct from `AIMech:WirtingerFlowPhaseRetrievalAndSpectralInitialization` (Candès, Li, & Soltanolkotabi 2015) and `AIMech:TruncatedWirtingerFlowAndTruncatedSpectralInitializationForQuadraticSystems` (Chen & Candès 2017), which minimize smooth fourth-order intensity-based or Poisson losses using fourth-moment spectral initialization and discard large-residual measurements, whereas Truncated Amplitude Flow minimizes the nonsmooth second-order amplitude loss $\frac{1}{2m}\sum_i(\psi_i - |\boldsymbol{a}_i^\top\boldsymbol{z}|)^2$ using magnitude-free spherical covariance initialization $\overline{\boldsymbol{Y}}_0$ and truncates small-$|\boldsymbol{a}_i^\top\boldsymbol{z}_t|/\psi_i$ watershed measurements that carry corrupted signs.

## Constructed Boundary & Regime Verification

```text
{"concept": "TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations", "dimension_n": 12, "lemma1_lhs_subspace_dist_sq": 0.485342, "lemma1_rhs_quadratic_form_ratio": 0.964672, "measurements_m": 48, "orthogonality_promoting_init_rel_err": 0.697415, "status": "VERIFIED", "taf_final_rel_err": 1.3070268198670348e-15, "wrong_sign_measurements_kept_after_truncation": 8, "wrong_sign_measurements_total_at_init": 8}
```
