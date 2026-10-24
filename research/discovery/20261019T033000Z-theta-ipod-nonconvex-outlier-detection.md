# Discovery Report: Round 264 — Theta-IPOD Thresholding-Based Iterative Outlier Detection and Mean-Shift Penalized Regression

- **Timestamp**: `2026-10-19T03:30:00Z`
- **Selected Concept**: `AIMech:ThetaIPODThresholdingBasedIterativeOutlierDetectionAndMeanShiftPenalizedRegression` (*Theta-IPOD Thresholding-Based Iterative Outlier Detection and Mean-Shift Penalized Regression*)
- **Record Path**: `data/curated/ThetaIPODThresholdingBasedIterativeOutlierDetectionAndMeanShiftPenalizedRegression.yaml`
- **Primary Source**: Yiyuan She and Art B. Owen (2011), *Outlier Detection Using Nonconvex Penalized Regression*, *Journal of the American Statistical Association* 106(494):626–639 (`DOI:10.1198/jasa.2011.tm10390`, `arXiv:1006.2592v3`).

## Identity & Boundary Resolution

`AIMech:ThetaIPODThresholdingBasedIterativeOutlierDetectionAndMeanShiftPenalizedRegression` was checked against all 442 pinned AIO concepts and 658 maintained AIMech concepts:

1. **`AIMech:ScaledLassoAndHuberConcomitantPenalizedJointSparseRegression`**: Convex concomitant scale estimation for sparse $\beta$, whereas $\Theta$-IPOD introduces observation-level mean-shift parameters $\gamma \in \mathbb{R}^n$ with nonconvex redescending thresholding rules $\Theta(\cdot; \lambda)$ and leverage-adjusted thresholds $\lambda_i = \lambda\sqrt{1-h_i}\hat{\sigma}$.
2. **`AIMech:CorruptedSensingConvexSignalCorruptionDemixingAndSubdifferentialDistanceBounds`**: Convex signal-corruption demixing under subgaussian random designs rather than nonconvex thresholding fixed-point outlier detection and two-stage redescending $M$-estimation.

## Constructed Boundary & Regime Verification

```text
{
  "prop3_1_and_thm4_1": {
    "max_huber_score_err": 1e-13,
    "concomitant_sigma_sq_diff": 0.0,
    "max_alg1_alg2_diff": 0.0,
    "max_descent_violation_p_theta": 0.0,
    "max_descent_violation_l0": 0.0,
    "max_m_score_err": 1e-14
  },
  "high_leverage_and_bic_star": {
    "soft_exact_recovery_count": 0,
    "detected_hard": [
      0,
      1,
      2,
      3,
      4,
      5
    ],
    "true_outliers": [
      0,
      1,
      2,
      3,
      4,
      5
    ],
    "max_diff_from_clean_ols": 0.0,
    "l2_err_hard": 0.01638866,
    "l2_err_ols": 0.5704719,
    "equivariance_err": 0.0
  },
  "high_dim_hard_ridge_ipod": {
    "max_descent_violation": 0.0,
    "selected_beta": [
      0,
      1
    ],
    "selected_gamma": [
      0,
      1
    ]
  }
}
```

Verified in pure Python across six regimes: (1) Proposition 3 equivalence between Soft-IPOD and Huber's M-estimator holds to 1e-13 (||X^T psi_H(y - X*beta_hat; lambda)||_inf = 1e-13) and concomitant scale sigma^2 matches ||r_S||_2^2 / (n - p) to 0.0; (2) Theorem 1 equivalence between alternating Algorithm 1 and H-compressed Algorithm 2 holds to 0.0 with zero objective descent violations under both continuous P_Theta_H and discrete l_0 penalties, and two-stage M-score ||X^T psi_Theta_H(H*gamma_hat + r_0; lambda)||_inf = 1e-14 (Proposition 2); (3) on a leveraged mask design (n=30, p=2, |O|=6) violating Proposition 1's irrepresentable condition (irr_norm = 1.9810926 > 1), Soft-IPOD achieves 0/60 exact support recoveries across all lambda in [0.1, 12.0] and OLS suffers l_2 error 0.5704719, whereas Hard-IPOD with leverage-adjusted thresholds lambda_i = lambda*sqrt(1 - h_i)*sigma recovers the exact outlier set [0, 1, 2, 3, 4, 5], reduces beta l_2 error 34.8x to 0.01638866, and matches clean-subset OLS to 0.0; (4) Proposition 4 regression and scale equivariance holds to 0.0; and (5) in high-dimensional p > n (n=35, p=50) regression with s=2 active predictors and k=2 gross outliers, joint Hybrid Hard-Ridge + Hard TISP (Eq. 6.1) recovers exact supports [0, 1] for both beta and gamma and reduces l_2 error from 0.87123823 to 0.04933417.
