# Discovery Report: Round 285 — Implicit Regularization in Nonconvex Statistical Estimation by Leave-One-Out Trajectory Analysis

- **Timestamp**: `2026-10-19T05:22:00Z`
- **Selected Concept**: `AIMech:ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis` (*Implicit Regularization in Nonconvex Statistical Estimation by Leave-One-Out Trajectory Analysis*)
- **Record Path**: `data/curated/ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis.yaml`
- **Primary Source**: Cong Ma, Kaizheng Wang, Yuejie Chi, Yuxin Chen — *Implicit Regularization in Nonconvex Statistical Estimation: Gradient Descent Converges Linearly for Phase Retrieval, Matrix Completion, and Blind Deconvolution* (`https://doi.org/10.1007/s10208-019-09429-9`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 679 maintained AIMech concepts. Distinct from `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` (Abbe, Fan, Wang, & Zhong 2020, which analyzes static leading eigenvectors of a single symmetric matrix rather than iterative nonconvex gradient descent trajectories $\boldsymbol{x}^{t+1} = \boldsymbol{x}^t - \eta_t\nabla f(\boldsymbol{x}^t)$ across $t \ge 0$) and from `AIMech:TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis` (Chen, Fan, Ma, & Wang 2019, which analyzes strongly convex $\ell_2$-regularized BTL logistic MLE and reversible Markov chains rather than unregularized nonconvex quadratic/quartic phase retrieval, low-rank matrix completion, and bilinear blind deconvolution).

## Constructed Boundary & Regime Verification

```text
{
  "phase_retrieval": {
    "n": 10,
    "m": 90,
    "init_l2_err": 0.427233,
    "final_l2_err": 0.00547304,
    "max_loo_trajectory_gap": 0.001324,
    "max_incoherence_ratio": 1.2969
  },
  "matrix_completion_rank1": {
    "n": 14,
    "p_obs": 0.65,
    "init_l2_err": 0.046465,
    "final_l2_err": 2.036e-05,
    "init_two_to_inf_err": 0.034713,
    "final_two_to_inf_err": 2.021e-05
  }
}
```
