# Discovery Report: Round 282 — Procrustean Matrix Decomposition and Two-to-Infinity Norm Singular Subspace Perturbation Bounds

- **Timestamp**: `2026-10-19T05:16:00Z`
- **Selected Concept**: `AIMech:ProcrusteanMatrixDecompositionAndTwoToInfinityNormSingularSubspacePerturbationBounds` (*Procrustean Matrix Decomposition and Two-to-Infinity Norm Singular Subspace Perturbation Bounds*)
- **Record Path**: `data/curated/ProcrusteanMatrixDecompositionAndTwoToInfinityNormSingularSubspacePerturbationBounds.yaml`
- **Primary Source**: Joshua Cape, Minh Tang, and Carey E. Priebe (2019), *The Two-to-Infinity Norm and Singular Subspace Geometry with Applications to High-Dimensional Statistics*, *The Annals of Statistics* 47(5):2405–2439 (`DOI:10.1214/18-AOS1752`, `arXiv:1705.10735v3`).

## Identity & Boundary Resolution

`AIMech:ProcrusteanMatrixDecompositionAndTwoToInfinityNormSingularSubspacePerturbationBounds` was checked against all 442 pinned AIO concepts and 676 maintained AIMech concepts:

1. **`AIMech:LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation`**: Individual eigenvector $\ell_\infty$ perturbation requiring distinct top eigenvalues vs. Procrustes-aligned singular subspace $\|\widehat{\mathbf{U}} - \mathbf{U}\mathbf{W}_U\|_{2\to\infty}$ perturbation via the exact 4-term Procrustean decomposition (Theorem 3.1) valid under degenerate top singular values.
2. **`AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices`**: Probabilistic row-and-column leave-one-out decoupling vs. deterministic 4-term Procrustean decomposition and asymmetric $2\to\infty$ operator-norm geometry (Propositions 2.1 and 6.5, Lemma 6.7).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:ProcrusteanMatrixDecompositionAndTwoToInfinityNormSingularSubspacePerturbationBounds",
  "source": "Cape, Tang, & Priebe (2019), Annals of Statistics 47(5):2405-2439, arXiv:1705.10735v3",
  "results": {
    "norm_geometry": {
      "counterexample_AB_2_to_inf": 2.0,
      "counterexample_A_2inf_times_B_2inf": 1.414214,
      "non_submultiplicative_confirmed": true,
      "prop65_AB_lhs": 6.182631,
      "prop65_AB_rhs": 7.689145,
      "prop65_CA_lhs": 7.319066,
      "prop65_CA_rhs": 18.548052
    },
    "procrustean_decomposition_and_thm42": {
      "p": 24,
      "r": 2,
      "degenerate_top_eigenvalues": [
        12.0,
        12.0
      ],
      "theorem31_max_abs_err": 1.205632815803881e-15,
      "lemma67_half_sin_sq": 0.0001428,
      "lemma67_ut_uhat_minus_w_op2": 0.00014281,
      "lemma67_sin_sq": 0.00028559,
      "unaligned_col1_inf_err": 0.149842,
      "procrustes_aligned_2_to_inf_err": 0.011047,
      "theorem42_upper_bound": 0.34446
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across three constructed experiments: (1) Proposition 2.1's identity ||U||_{2->inf} = sqrt(r/p) sqrt(mu(U)) holds to 0.0 error, the 2x2 counterexample A = [[1,1],[0,0]], B = [[1,0],[1,0]] exhibits non-submultiplicativity ||A B||_{2->inf} = 2.0 > 1.414214 = ||A||_{2->inf} ||B||_{2->inf}, and Proposition 6.5's asymmetric product inequalities ||A B||_{2->inf} = 6.1826 <= 7.6891 and ||C A||_{2->inf} = 7.3191 <= 18.5481 hold strictly; (2) for Theorem 3.1's exact four-term Procrustean decomposition under degenerate top eigenvalues lambda_1 = lambda_2 = 12.0 (p = 16, r = 2), the four-term identity matches U_hat - U W_U to 1.21e-15 and Lemma 6.7's canonical-angle sandwich 0.5 ||sin Theta||_2^2 = 0.0001428 <= ||U^T U_hat - W_U||_2 = 0.00014281 <= 0.00028559 holds; and (3) under repeated eigenvalues lambda_1 = lambda_2 = 12.0 (p = 24, r = 2), unaligned individual eigenvectors suffer O(1) rotation error (0.149842), whereas the Procrustes-aligned subspace error ||U_hat - U W_U||_{2->inf} = 0.011047 is 13.6x smaller and satisfies Theorem 4.2's bound (0.34446).
