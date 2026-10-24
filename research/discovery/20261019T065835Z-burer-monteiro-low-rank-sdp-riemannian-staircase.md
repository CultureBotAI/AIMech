# Discovery Report: Round 336 — Burer-Monteiro Low-Rank Semidefinite Programming and Riemannian Staircase

- **Timestamp**: `2026-10-19T06:58:35Z`
- **Selected Concept**: `AIMech:BurerMonteiroLowRankSemidefiniteProgrammingAndRiemannianStaircase` (*Burer-Monteiro Low-Rank Semidefinite Programming and Riemannian Staircase*)
- **Record Path**: `data/curated/BurerMonteiroLowRankSemidefiniteProgrammingAndRiemannianStaircase.yaml`
- **Primary Source**: Nicolas Boumal, Vladislav Voroninski, Afonso S. Bandeira — *The non-convex Burer-Monteiro approach works on smooth semidefinite programs* (`https://doi.org/10.1002/cpa.21830`).

## Identity & Boundary Resolution

Distinct from Grothendieck Inequality and Semidefinite Programming for Sparse SBM (`AIMech:GrothendieckInequalityAndSemidefiniteProgrammingForSparseSBM`), which analyzes the statistical signal-to-noise recovery threshold of the convex n x n SDP relaxation under Grothendieck's inequality rather than the non-convex rank-p Burer-Monteiro manifold parameterization X = Y Y^T, the Barvinok-Pataki threshold p(p+1)/2 > m, and the Riemannian staircase escape mechanism of Boumal, Voroninski, and Bandeira (2016).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 336 Burer-Monteiro & Riemannian Staircase (Boumal et al. 2016): min_eig_S_low=-2.2361, hess_escape_val=-2.2361, min_eig_S_opt=4.03e-17, primal_obj=-8.090170, duality_gap=0.00e+00
```
