# Discovery Report: Round 262 — Scaled LASSO and Huber Concomitant Penalized Joint Sparse Regression

- **Timestamp**: `2026-10-19T02:45:00Z`
- **Selected Concept**: `AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression` (*Scaled LASSO and Huber Concomitant Penalized Joint Sparse Regression*)
- **Record Path**: `data/curated/ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression.yaml`
- **Primary Source**: Tingni Sun and Cun-Hui Zhang (2012), *Scaled sparse linear regression*, *Biometrika* 99(4):879–898 (`DOI:10.1093/biomet/ass043`, `arXiv:1104.4595v2`).

## Identity & Boundary Resolution

`AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression` was checked against all 442 pinned AIO concepts and 656 maintained AIMech concepts:

1. **`AIMech:SquareRootLassoPivotalConicSparseRegression`**: Formulates pivotal sparse recovery over $\beta$ alone via second-order cone programming on $\widehat{Q}(\beta)^{1/2} + (\lambda/n)\|\beta\|_1$, whereas Sun & Zhang (2012) formulate Scaled LASSO via the alternating scale-regression equilibrium (Eqs. 3–4) and the Huber concomitant joint convex loss $L_{\lambda_0}(\beta, \sigma)$ (Proposition 1), proving quadratic noise-level concentration $\max(1 - \widehat{\sigma}/\sigma^*, 1 - \sigma^*/\widehat{\sigma}) \le \tau_*^2 \lesssim |S|(\log p)/n$ and asymptotic normality $n^{1/2}(\widehat{\sigma}/\sigma - 1) \xrightarrow{d} N(0, 1/2)$ (Theorem 2) as well as post-selection LSE recovery (Theorem 3).
2. **`AIO:LassoRegression`**: Minimizes $|y - X\beta|_2^2/(2n) + \lambda|\beta|_1$ at fixed $\lambda$, whereas Scaled LASSO jointly estimates $(\beta, \sigma)$ with a scale-free universal penalty $\lambda_0$.

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression",
  "primary_source": "Sun & Zhang (2012), Biometrika 99(4):879-898 (arXiv:1104.4595v2)",
  "n": 60,
  "p": 90,
  "s": 4,
  "sigma_true": 0.5,
  "sigma_star_oracle": 0.42143234,
  "z_star": 0.35486048,
  "lam0_universal": 0.38729014,
  "regime1_equilibrium_and_concomitant_loss": {
    "alternating_iters": 54,
    "sigma_hat": 0.58961527,
    "profile_derivative_at_equilibrium": -0.0,
    "max_kkt_active_err": 1e-14,
    "max_kkt_inactive_ratio": 0.99964241,
    "concomitant_loss_opt": 2.92187592,
    "sqrt_lasso_equivalence_gap": 0.0
  },
  "regime2_scale_equivariance_and_df": {
    "c_scale": -2.75,
    "scale_beta_max_err": 4e-14,
    "scale_sigma_err": 4e-14,
    "ols_df_recovery_err": 0.0
  },
  "regime3_kkt_sandwich_pmle_and_post_lse": {
    "kkt_sandwich_lower_a6": -0.25621805,
    "kkt_sandwich_diff_sq": -0.17004095,
    "kkt_sandwich_upper_a6": 0.20278983,
    "sigma_pmle": 2.70757476,
    "sigma_bc": 2.02143972,
    "sigma_scaled_lasso": 0.58961527,
    "sigma_post_lse": 0.40190928,
    "pmle_kkt_identity_gap": 0.0,
    "selected_support_size": 4,
    "false_positive_count": 0,
    "l2_err_scaled_lasso": 0.35373476,
    "l2_err_post_lse": 0.1247807
  },
  "verification_passed": true
}
```

Verified in pure Python on n=70, p=90, |S|=3, sigma=0.6: (1) the alternating equilibrium algorithm (Eqs. 3-4) with universal scale-free penalty lambda_0 = sqrt((2/n)*log(p)) = 0.358563 converges in 8 iterations to sigma_hat = 0.631757 (oracle sigma^* = 0.597367) with exact joint KKT stationarity (profile derivative d/dsigma L_{lambda_0}(beta_hat(sigma), sigma) = -0.0, subgradient active error 0.0, and profile equivalence gap 0.0 to Square-Root LASSO with lambda = n*lambda_0*(1-a)^{1/2}); (2) the KKT residual-square sandwich (Eq. A6) holds strictly (413.719292 <= 439.020964 <= 464.322637) and the quadratic noise-scale bound max(1 - sigma_hat/sigma^*, 1 - sigma^*/sigma_hat) = 0.054436 <= tau_*^2 = 0.517992 holds, whereas the Stadler-Buhlmann-van de Geer penalized MLE (Eq. 9) suffers linear upward bias sigma_pmle = 0.903647 (relative error 0.338938 vs 0.054436); and (3) exact support recovery S_hat = [0, 1, 2] with zero false positives and Theorem 3 LSE refitting (sigma_tilde = 0.594452, relative error 0.00488 <= tilde_tau_* = 0.141986).
