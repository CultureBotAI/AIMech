# Discovery Report: Round 436 — GT-SAGA and GT-SVRG (Decentralized Variance-Reduced Gradient Tracking)

- **Timestamp**: `2026-10-19T08:39:00Z`
- **Selected Concept**: `AIMech:GtSagaAndGtSvrgDecentralizedVarianceReducedGradientTracking` (*GT-SAGA and GT-SVRG (Decentralized Variance-Reduced Gradient Tracking)*)
- **Record Path**: `data/curated/GtSagaAndGtSvrgDecentralizedVarianceReducedGradientTracking.yaml`
- **Primary Source**: Ran Xin, Usman A. Khan, Soummya Kar — *Variance-Reduced Decentralized Stochastic Optimization With Accelerated Convergence* (`https://doi.org/10.1109/TSP.2020.3031071`).

## Identity & Boundary Resolution

Distinct from DSGT and GSGT (AIMech:DsgtAndGsgtDistributedStochasticGradientTracking, Pu & Nedic 2021), which use unreduced stochastic gradients G_i(x_{i,k}, xi_{i,k}) and suffer an O(alpha sigma^2 / n) steady-state variance neighborhood under constant step size, and from centralized SAGA (AIMech:SagaFastIncrementalGradientMethodWithSupportForNonStronglyConvexCompositeObjectives, Defazio et al. 2014) and SVRG (AIMech:StochasticVarianceReducedGradient, Johnson & Zhang 2013), which operate on a single shared parameter vector without decentralized consensus or inter-node gradient tracking.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 436 GT-SAGA & GT-SVRG (Xin et al. 2020): err_gt_saga=7.55e-15, err_gt_svrg=2.66e-15 << err_no_gt=1.1692
```
