# Discovery Report: Round 376 — SpiderBoost and Proximal SpiderBoost with Momentum for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:39:00Z`
- **Selected Concept**: `AIMech:SpiderBoostAndProximalSpiderBoostWithMomentumForNonconvexOptimization` (*SpiderBoost and Proximal SpiderBoost with Momentum for Non-Convex Optimization*)
- **Record Path**: `data/curated/SpiderBoostAndProximalSpiderBoostWithMomentumForNonconvexOptimization.yaml`
- **Primary Source**: Zhe Wang, Kaiyi Ji, Yi Zhou, Yingbin Liang, Vahid Tarokh — *SpiderBoost and Momentum: Faster Stochastic Variance Reduction Algorithms* (`https://papers.nips.cc/paper/2019/hash/512c5cad6c37edb98ae91c8a76c3a291-Abstract.html`).

## Identity & Boundary Resolution

Distinct from original SPIDER (Fang et al. 2018, AIMech:SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization), which uses a tiny accuracy-dependent step size eta = O(varepsilon / L) and normalized gradient directions that prevent direct extension to composite proximal mappings prox_{eta*h}; from SARAH (Nguyen et al. 2017, AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization), which uses b = 1 and sub-optimal O(n + n^{2/3}/varepsilon^2) non-convex complexity; and from loopless PAGE (Li et al. 2021, AIMech:PageProbabilisticGradientEstimatorForNonconvexOptimization), which replaces deterministic q-periodic epochs with Bernoulli coin flips for unconstrained smooth problems.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 376 SpiderBoost (Wang et al. 2019): beta_1=0.5000==L/4, stepsize_ratio=1000x, prox_grad_final=7.99e-16, PO=1000000 vs SFO=100010000
```
