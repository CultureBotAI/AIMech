# Discovery Report: Round 604 — MARS (Make vAriance Reduction Shine Preconditioned Optimizer Framework)

- **Timestamp**: `2026-10-19T11:27:00Z`
- **Selected Concept**: `AIMech:MarsVarianceReducedPreconditionedGradientOptimization` (*MARS (Make vAriance Reduction Shine Preconditioned Optimizer Framework)*)
- **Record Path**: `data/curated/MarsVarianceReducedPreconditionedGradientOptimization.yaml`
- **Primary Source**: Huizhuo Yuan, Yifeng Liu, Shuang Wu, Xun Zhou, Quanquan Gu — *MARS: Unleashing the Power of Variance Reduction for Training Large Models* (`https://dblp.org/rec/conf/icml/Yuan0WZG25`).

## Identity & Boundary Resolution

Distinct from unpreconditioned STORM (AIMech:StormStochasticRecursiveMomentumForNonconvexOptimization), AdamW, Lion (AIMech:LionEvoSignMomentumOptimizer), and Shampoo (AIMech:ShampooKroneckerFactoredPreconditionedOptimizer): MARS unifies preconditioned adaptive optimization and recursive variance reduction through Proposition 3.2, introducing the control-variate scaling factor gamma_t that continuously interpolates between standard exponential moving average momentum (gamma_t = 0) and full recursive momentum (gamma_t = 1) before applying diagonal, elementwise-sign, or orthogonal-matrix preconditioning H_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 604 MARS verified: lion_err=4.44e-16, muon_err=2.66e-15, cv_gain_err=8.88e-16, mse_ratio=0.2090<1, loss_mars=1.0962e-01<loss_adamw=1.1554e-01
```
