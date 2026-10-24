# Discovery Report: Round 637 — EKFAC (Eigenvalue-Corrected Kronecker Factorization)

- **Timestamp**: `2026-10-19T12:00:00Z`
- **Selected Concept**: `AIMech:EKFACEigenvalueCorrectedKroneckerFactorizationNaturalGradient` (*EKFAC (Eigenvalue-Corrected Kronecker Factorization)*)
- **Record Path**: `data/curated/EKFACEigenvalueCorrectedKroneckerFactorizationNaturalGradient.yaml`
- **Primary Source**: Thomas George, César Laurent, Xavier Bouthillier, Nicolas Ballas, Pascal Vincent — *Fast Approximate Natural Gradient Descent in a Kronecker-factored Eigenbasis* (`https://dblp.org/rec/conf/nips/GeorgeLBBV18`).

## Identity & Boundary Resolution

Distinct from K-FAC (AIMech:KFacKroneckerFactoredApproximateCurvature), which approximates each layer's Fisher block as G_KFAC = A (x) B = (U_A (x) U_B)(S_A (x) S_B)(U_A (x) U_B)^T with eigenvalues restricted to the Kronecker product S_A (x) S_B; EKFAC keeps the Kronecker-Factored Eigenbasis U_A (x) U_B but replaces S_A (x) S_B with the unconstrained diagonal second-moment matrix S* in KFE coordinates, provably achieving ||G - G_EKFAC||_F <= ||G - G_KFAC||_F and enabling cheap per-iteration updates of S* without recomputing the eigendecomposition.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 637 EKFAC verified: ||G-G_EKFAC||_F=3.7313 < ||G-G_KFAC||_F=3.7479, lemma1_err=8.88e-16, kron_vec_err=0.00e+00
```
