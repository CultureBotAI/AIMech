# Discovery Report: Round 261 — Square-Root LASSO Pivotal Second-Order Cone Sparse Regression

- **Timestamp**: `2026-10-19T02:35:00Z`
- **Selected Concept**: `AIMech:SquareRootLassoPivotalConicSparseRegression` (*Square-Root LASSO Pivotal Second-Order Cone Sparse Regression*)
- **Record Path**: `data/curated/SquareRootLassoPivotalConicSparseRegression.yaml`
- **Primary Source**: Alexandre Belloni, Victor Chernozhukov, and Lie Wang (2011), *Square-Root Lasso: Pivotal Recovery of Sparse Signals via Conic Programming*, *Biometrika* 98(4):791–806 (`DOI:10.1093/biomet/asr043`, `arXiv:1009.5689v5`).

## Identity & Boundary Resolution

`AIMech:SquareRootLassoPivotalConicSparseRegression` was checked against all 442 pinned AIO concepts and 655 maintained AIMech concepts:

1. **`AIO:LassoRegression`**: Minimizes $\widehat{Q}(\beta) + \frac{\lambda}{n}\|\beta\|_1$ whose score $2\sigma\mathbb{E}_n(x\epsilon)$ scales linearly with the unknown noise level $\sigma$, whereas Square-Root LASSO minimizes $\widehat{Q}(\beta)^{1/2} + \frac{\lambda}{n}\|\beta\|_1$ with a pivotal self-normalized score $\tilde{S} = \mathbb{E}_n(x\epsilon)/(\mathbb{E}_n(\epsilon^2))^{1/2}$ and a second-order cone programming (SOCP) primal-dual structure.
2. **`AIMech:AdaptiveLassoOracleWeightedL1PenalizedEstimation`**: Reweights $\ell_1$ penalties via initial estimator magnitudes $|\hat{\beta}_{\text{init},j}|^{-\gamma}$ for oracle selection, whereas Square-Root LASSO achieves $\sigma$-free pivotal penalty selection in $p \gg n$ sparse regression.

## Constructed Boundary & Regime Verification

```text
{
  "score_pivotality_and_lemma1": {
    "pivotal_Lambda_across_sigmas": [
      32.643561,
      32.643561,
      32.643561,
      32.643561
    ],
    "non_pivotal_lasso_score_across_sigmas": [
      6.942625,
      69.426252,
      347.131258,
      1735.656289
    ],
    "lemma1_Lambda_1_minus_alpha": 40.118048,
    "lemma1_sqrt_2n_log_2p_over_alpha": 46.442731,
    "lemma1_nu_factor": 1.702783
  },
  "conic_duality_and_theorem1": {
    "lambda_pivotal": 31.751631,
    "primal_socp_objective": 2.67415,
    "dual_socp_objective": 2.67415,
    "conic_duality_gap": 0.0,
    "max_dual_covariate_corr_minus_lambda_over_n": 0.0,
    "delta_T_l1": 0.743452,
    "delta_Tc_l1": 0.0,
    "prediction_norm_error": 0.446067
  }
}
```

Verified in pure Python: (1) across noise standard deviations sigma in {0.1, 1.0, 5.0, 25.0} at n=120, p=200, the Square-Root LASSO maximal score Lambda = n*||tilde_S||_infty is identically 32.643561 (difference < 1e-12), whereas the standard LASSO maximal score scales linearly from 6.942625 to 1735.656289 (250x ratio); (2) Lemma 1 asymptotic penalty base Lambda(0.95) = 40.118048 <= sqrt(2n*log(2p/alpha)) = 46.442731 with finite-sample factor nu = 1.702783; and (3) exact closed-form coordinatewise optimization on n=80, p=40, s=3, sigma=0.5 converges to primal SOCP objective 2.674150 and dual objective 2.674150 with conic duality gap 0.00e+00, dual covariate correlation slack 0.00e+00, zero false positives (||delta_{T^c}||_1 = 0.0 <= c_bar*||delta_T||_1), and prediction norm error ||delta||_{2,n} = 0.446067.
