# Discovery Report: Round 354 — Shift-and-Invert Preconditioning for Faster Leading Eigenvector Computation

- **Timestamp**: `2026-10-19T07:17:00Z`
- **Selected Concept**: `AIMech:ShiftAndInvertPreconditioningForFasterEigenvectorComputation` (*Shift-and-Invert Preconditioning for Faster Leading Eigenvector Computation*)
- **Record Path**: `data/curated/ShiftAndInvertPreconditioningForFasterEigenvectorComputation.yaml`
- **Primary Source**: Dan Garber, Elad Hazan, Chi Jin, Sham M. Kakade, Cameron Musco, Praneeth Netrapalli, Aaron Sidford — *Faster Eigenvector Computation via Shift-and-Invert Preconditioning* (`https://proceedings.mlr.press/v48/garber16.html`).

## Identity & Boundary Resolution

Distinct from Randomized Block Krylov Methods for Stronger and Faster Approximate SVD (`AIMech:RandomizedBlockKrylovMethodsForStrongerAndFasterApproximateSVD`), which applies polynomial Krylov subspace iteration with full matrix-matrix multiplications in O(nnz(A) k log(d) / sqrt(epsilon)) time where nnz(A) and 1/sqrt(gap) are multiplied together, whereas Shift-and-Invert Preconditioning with SVRG additively separates nnz(A) from d sr(A) / gap^2 and achieves true log(1/epsilon) linear convergence in both offline and O(d)-memory streaming PCA.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 354 Shift-and-Invert Eigenvector (Garber et al. 2016): inv_gap_ratio=101.0, G(x)=1.8051 -> G(B^-1 x)=0.003869, lemma11_ratio=0.0000 <= 1.0, 5step_sipm_err=0.00e+00 vs pm_err=0.2755
```
