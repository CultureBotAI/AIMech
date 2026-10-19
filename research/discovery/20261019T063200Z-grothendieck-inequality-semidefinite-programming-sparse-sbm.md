# Discovery Report: Round 320 — Grothendieck Inequality and Semidefinite Programming for Sparse SBM

- **Timestamp**: `2026-10-19T06:32:00Z`
- **Selected Concept**: `AIMech:GrothendieckInequalityAndSemidefiniteProgrammingForSparseSBM` (*Grothendieck Inequality and Semidefinite Programming for Sparse SBM*)
- **Record Path**: `data/curated/GrothendieckInequalityAndSemidefiniteProgrammingForSparseSBM.yaml`
- **Primary Source**: Olivier Guedon, Roman Vershynin — *Community detection in sparse networks via Grothendieck's inequality* (`https://doi.org/10.1007/s00440-015-0659-z`).

## Identity & Boundary Resolution

Distinct from exact recovery at logarithmic average degree p = a log(n)/n via dual certificate construction (AIMech:StochasticBlockModelExactRecoveryPhaseTransitionAndSemidefiniteProgramming) and Hashimoto non-backtracking spectral clustering (AIMech:NonBacktrackingWalkMatrixAndKestenStigumSpectralRedemption). Specifically captures the Guedon-Vershynin (2016) Grothendieck inequality SDP perturbation principle (Theorem 3.1, Lemma 6.1, Lemma 6.2, and Lemma 7.1) that achieves arbitrary fraction 1 - epsilon community recovery in constant-average-degree sparse networks without degree trimming whenever the signal-to-noise ratio (a - b)^2 / (a + b) >= C epsilon^{-2} (Theorems 1.1-1.4).

## Constructed Boundary & Regime Verification

```text
{"concept": "GrothendieckInequalityAndSemidefiniteProgrammingForSparseSBM", "empirical_max_grothendieck_ratio": 0.186532, "grothendieck_constant_bound": 1.782214, "hub_relative_cut_norm_perturbation": 0.277778, "hub_relative_spectral_perturbation": 0.372678, "lemma62_min_curvature_margin": 0.032, "status": "VERIFIED"}
```
