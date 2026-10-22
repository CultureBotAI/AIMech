# Discovery Report: Round 839 — Halko-Martinsson-Tropp Randomized Subspace Iteration and Low-Rank Matrix Decomposition

- **Timestamp**: `2026-10-19T15:22:00Z`
- **Selected Concept**: `AIMech:HalkoMartinssonTroppRandomizedSubspaceIterationAndLowRankMatrixDecomposition` (*Halko-Martinsson-Tropp Randomized Subspace Iteration and Low-Rank Matrix Decomposition*)
- **Record Path**: `data/curated/HalkoMartinssonTroppRandomizedSubspaceIterationAndLowRankMatrixDecomposition.yaml`
- **Primary Source**: Nathan Halko, Per-Gunnar Martinsson, Joel A. Tropp — *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions* (`https://arxiv.org/abs/0909.4061`).

## Identity & Boundary Resolution

No AIO class represents the Halko-Martinsson-Tropp two-stage randomized range finder and QR-stabilized subspace iteration framework; DimensionalityReduction (AIO:DimensionalityReduction) and PrincipalComponentAnalysis (AIO:PrincipalComponentAnalysis) are the closest broad matches covering low-rank spectral and SVD dimensionality reduction.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 839 Halko-Martinsson-Tropp Randomized SVD (2010/2011): emp_frob=0.4969<=bound=0.9037, q_errs=[0.5734, 0.4402, 0.4326, 0.4287], nys=0.4532<dir=0.6575
```
