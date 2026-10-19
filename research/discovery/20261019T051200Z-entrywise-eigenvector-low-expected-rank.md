# Discovery Report: Round 280 — Entrywise First-Order Eigenvector Approximation and Leave-One-Out Perturbation Analysis for Low-Expected-Rank Random Matrices

- **Timestamp**: `2026-10-19T05:12:00Z`
- **Selected Concept**: `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` (*Entrywise First-Order Eigenvector Approximation and Leave-One-Out Perturbation Analysis for Low-Expected-Rank Random Matrices*)
- **Record Path**: `data/curated/EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices.yaml`
- **Primary Source**: Emmanuel Abbe, Jianqing Fan, Kaizheng Wang, and Yiqiao Zhong (2020), *Entrywise Eigenvector Analysis of Random Matrices with Low Expected Rank*, *The Annals of Statistics* 48(3):1452–1474 (`DOI:10.1214/19-AOS1854`, `arXiv:1709.09565v2`).

## Identity & Boundary Resolution

`AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` was checked against all 442 pinned AIO concepts and 674 maintained AIMech concepts:

1. **`AIMech:LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation`**: Deterministic $\ell_\infty$ perturbation in terms of $\|\mathbf{E}\|_\infty$ vs. probabilistic first-order linear entrywise approximation $\mathbf{u}_k \approx \mathbf{A}\mathbf{u}_k^* / \lambda_k^*$ via leave-one-out row decoupling.
2. **`AIMech:SCORESpectralClusteringOnRatiosOfEigenvectorsForDegreeCorrectedBlockModels`**: Eigenvector-ratio degree normalization for DCBMs vs. leave-one-out entrywise eigenvector perturbation theory and exact recovery at the information-theoretic threshold.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices",
  "source": "Abbe, Fan, Wang, & Zhong (2020), Annals of Statistics 48(3):1452-1474, arXiv:1709.09565v2",
  "results": {
    "first_order_and_leave_one_out": {
      "n": 48,
      "lambda_star": 14.0,
      "lambda_hat": 14.07781,
      "err_direct_inf": 0.039419,
      "err_first_order_inf": 0.005274,
      "first_order_improvement_ratio": 7.4737,
      "loo_l2_diff": 0.131239,
      "loo_non_m_linf": 0.008222,
      "row_m_decouple_abs_err": 0.000699
    },
    "sbm_exact_recovery_and_theorem_3_3": {
      "thm33_a": 1.85,
      "thm33_b": 0.45,
      "thm33_eta": 2.5845,
      "thm33_scaled_linf_lower_bound": 2.093803,
      "sbm_n": 56,
      "sbm_lambda2_star": 11.76,
      "sbm_lambda2_hat": 12.06,
      "scaled_direct_inf_err": 0.592753,
      "scaled_first_order_inf_err": 0.300571,
      "min_signed_scaled_u2": 0.407247,
      "exact_recovery_achieved": true
    },
    "rank_r_polar_sign_alignment": {
      "n": 40,
      "r": 2,
      "lambda1_star": 12.0,
      "lambda2_star": 11.75,
      "err_column_sign_only_2_to_inf": 0.083343,
      "err_polar_aligned_vs_ustar_2_to_inf": 0.061687,
      "err_polar_aligned_vs_first_order_2_to_inf": 0.009132
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across three constructed experiments: (1) for a rank-1 low-expected-rank random matrix A in R^{48 x 48} (lambda_1^* = 14.0), the first-order entrywise residual ||u_1 - A u_1^* / lambda_1^*||_inf = 0.005274 is 7.47x smaller than the direct deviation ||u_1 - u_1^*||_inf = 0.039419, and the leave-one-out auxiliary eigenvector u_1^{(0)} matches u_1 on non-removed coordinates to 0.008222 and decouples the row-0 noise projection to 0.000699; (2) for Theorem 3.3's two-block SBM parameters (a = 1.85, b = 0.45), Newton's method gives eta = 2.5845 and the asymptotic lower bound a(eta - 1)/(a - b) = 2.0938 > 1, while on an n = 56 SBM realization the first-order residual sqrt(n)||u_2 - A u_2^* / lambda_2^*||_inf = 0.3006 is nearly half of sqrt(n)||u_2 - u_2^*||_inf = 0.5928 and vanilla sgn(u_2) achieves 100% exact community recovery (min signed scaled coordinate 0.4072 > 0); and (3) for a rank-2 matrix with close eigenvalues (12.0 and 11.75), polar-factor alignment U sgn(H) reduces the 2-to-infinity error against the first-order approximation A U^* (Lambda^*)^{-1} to 0.009132 vs. 0.061687 against U^* and 0.083343 for column-sign-only alignment.
