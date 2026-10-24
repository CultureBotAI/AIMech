# Discovery Report: Round 299 — Scaled Gradient Descent (ScaledGD) for Ill-Conditioned Low-Rank Matrix and Tensor Estimation

- **Timestamp**: `2026-10-19T05:50:00Z`
- **Selected Concept**: `AIMech:ScaledGradientDescentForIllConditionedLowRankMatrixEstimation` (*Scaled Gradient Descent (ScaledGD) for Ill-Conditioned Low-Rank Matrix and Tensor Estimation*)
- **Record Path**: `data/curated/ScaledGradientDescentForIllConditionedLowRankMatrixEstimation.yaml`
- **Primary Source**: Tian Tong, Cong Ma, Yuejie Chi — *Accelerating Ill-Conditioned Low-Rank Matrix Estimation via Scaled Gradient Descent* (`https://jmlr.org/papers/v22/20-1067.html`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 693 maintained AIMech concepts. Distinct from `AIMech:ImplicitRegularizationInNonconvexStatisticalEstimationByLeaveOneOutTrajectoryAnalysis` (Ma, Wang, Chi, & Chen 2020) and `AIMech:ConvexAndNonconvexBridgingForRobustPCAUnderNoiseOutliersAndMissingData` (Chen, Fan, Ma, & Yan 2021), which analyze unpreconditioned factored gradient descent whose iteration complexity scales linearly or quadratically with the matrix condition number $\kappa = \sigma_1(\boldsymbol{X}_\star)/\sigma_r(\boldsymbol{X}_\star)$ and requires explicit balancing regularizers $\|\boldsymbol{L}^\top\boldsymbol{L} - \boldsymbol{R}^\top\boldsymbol{R}\|_F^2$, whereas ScaledGD uses right Gram-inverse preconditioning $(\boldsymbol{R}_t^\top\boldsymbol{R}_t)^{-1}$ to achieve $\mathrm{GL}(r)$ equivariance and $\kappa$-free contraction without balancing penalties.

## Constructed Boundary & Regime Verification

```text
{"concept": "ScaledGradientDescentForIllConditionedLowRankMatrixEstimation", "condition_number_kappa": 25.0, "equivariance_product_diff": 4.73951517460321e-16, "iterations": 45, "scaled_gd_rel_err_kappa_100": 2.1715182746093956e-16, "scaled_gd_rel_err_kappa_25": 3.6254052353184744e-16, "status": "VERIFIED", "vanilla_gd_rel_err_kappa_25": 0.001449}
```
