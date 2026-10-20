# Discovery Report: Round 607 — Apollo (Adaptive Parameter-wise Diagonal Quasi-Newton Optimizer)

- **Timestamp**: `2026-10-19T11:30:00Z`
- **Selected Concept**: `AIMech:ApolloAdaptiveParameterWiseDiagonalQuasiNewtonOptimization` (*Apollo (Adaptive Parameter-wise Diagonal Quasi-Newton Optimizer)*)
- **Record Path**: `data/curated/ApolloAdaptiveParameterWiseDiagonalQuasiNewtonOptimization.yaml`
- **Primary Source**: Xuezhe Ma — *Apollo: An Adaptive Parameter-wise Diagonal Quasi-Newton Method for Nonconvex Stochastic Optimization* (`https://dblp.org/rec/journals/corr/abs-2009-13586`).

## Identity & Boundary Resolution

Distinct from L-BFGS, SdLBFGS (Wang et al. 2017), AdaHessian (AIMech:AdaHessianAdaptiveSecondOrderOptimizer), and Sophia (AIMech:SophiaSecondOrderClippedStochasticOptimization): Apollo requires zero Hessian-vector products or multi-step secant history buffers; instead it solves the minimum-Frobenius-norm diagonal update min_B ||B - B_t||_F subject to the parameter-wise weak secant equation s_t^T B_{t+1} s_t = s_t^T y_t (Eqs. 6-7), applies stepsize bias correction y'_t = eta_t y_t so B_{t+1} is invariant to eta_t (Eq. 8), and enforces positive definiteness via elementwise rectified absolute values max(|B_{t+1}|, sigma) (Eq. 11).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 607 Apollo verified: secant_err=0.00e+00, frob_gain=7.9768e-02>0, eq8_err=4.44e-16, thm1_th_err=5.55e-14, thm1_B_err=2.06e-13, scale_inv_err=1.25e-15
```
