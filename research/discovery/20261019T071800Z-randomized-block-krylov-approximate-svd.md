# Discovery Report: Round 355 — Randomized Block Krylov Iteration for Gap-Independent Approximate SVD and Principal Component Analysis

- **Timestamp**: `2026-10-19T07:18:00Z`
- **Selected Concept**: `AIMech:RandomizedBlockKrylovMethodsForApproximateSingularValueDecomposition` (*Randomized Block Krylov Iteration for Gap-Independent Approximate SVD and Principal Component Analysis*)
- **Record Path**: `data/curated/RandomizedBlockKrylovMethodsForApproximateSingularValueDecomposition.yaml`
- **Primary Source**: Cameron Musco, Christopher Musco — *Randomized Block Krylov Methods for Stronger and Faster Approximate Singular Value Decomposition* (`https://dblp.org/rec/conf/nips/MuscoM15.xml`).

## Identity & Boundary Resolution

Distinct from generic PrincipalComponentAnalysis (AIO:PrincipalComponentAnalysis) and DimensionalityReduction (AIO:DimensionalityReduction), which do not specify randomized block Krylov subspace construction or Chebyshev polynomial spectral tail suppression. Distinct from AIMech:CountSketchInputSparsitySubspaceEmbeddingAndRegression (Round 331) and AIMech:RelativeErrorCURMatrixDecompositionViaSubspaceLeverageSampling (Round 332), which are non-iterative input-sparsity sketching and column-row subset selection methods providing Frobenius-norm low-rank approximation rather than gap-independent O(log(d)/sqrt(epsilon)) spectral-norm and per-vector PCA variance bounds. Also distinct from AIMech:ShiftAndInvertPreconditioningForFasterEigenvectorComputation (Round 354), which accelerates top-1 eigenvector computation under an explicit relative eigengap via SVRG linear system solves on (lambda I - A)^{-1} rather than gap-independent rank-k block Krylov subspace projection.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 355 Block Krylov SVD (Musco & Musco 2015): cheb_tail=1.1401e-01<=bound=4.6652e-01, spec_bk=1.00001<spec_sim=1.00063 (opt=1.00000), pv_bk=0.00002<pv_sim=0.07072
```
