# Discovery Report: Round 333 — Faster Least Squares Approximation via Randomized Hadamard Preconditioning

- **Timestamp**: `2026-10-19T06:56:00Z`
- **Selected Concept**: `AIMech:FasterLeastSquaresApproximationViaRandomizedHadamardPreconditioning` (*Faster Least Squares Approximation via Randomized Hadamard Preconditioning*)
- **Record Path**: `data/curated/FasterLeastSquaresApproximationViaRandomizedHadamardPreconditioning.yaml`
- **Primary Source**: Petros Drineas, Michael W. Mahoney, S. Muthukrishnan, Tamas Sarlos — *Faster Least Squares Approximation* (`https://doi.org/10.1007/s00211-010-0331-6`).

## Identity & Boundary Resolution

Distinct from Subsampled Randomized Hadamard Transform Subspace Embedding (`AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding`), which analyzes only the matrix-Chernoff singular value bounds of Phi V for a fixed orthonormal basis V without the response-residual cross-term condition ||U_A^T X^T X b^perp||_2^2 <= epsilon Z^2 / 2 or parameter recovery bounds ||x_opt - tilde{x}_opt||_2, and from CountSketch Input-Sparsity Subspace Embedding and Regression (`AIMech:CountSketchInputSparsitySubspaceEmbeddingAndRegression`). Specifically captures the Drineas et al. (2011) Randomized Hadamard leverage-flattening Lemma 3, the deterministic two-condition least-squares perturbation framework (Lemmas 1-2, Equations 8-21), and the Algorithm 1 / Algorithm 2 fast least-squares solvers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 333 Faster Least Squares (RHT Preconditioning): max_lev_before=1.000, max_lev_after=0.131, smin_sq_XUA=0.9228, lemma1_norm_eq_err=1.49e-15, pythag_err=4.44e-16, smin_sq_unprecond=0.00e+00
```
