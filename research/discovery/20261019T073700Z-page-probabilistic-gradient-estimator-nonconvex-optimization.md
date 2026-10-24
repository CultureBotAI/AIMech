# Discovery Report: Round 374 — PAGE (Probabilistic Gradient Estimator) for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:37:00Z`
- **Selected Concept**: `AIMech:PageProbabilisticGradientEstimatorForNonconvexOptimization` (*PAGE (Probabilistic Gradient Estimator) for Non-Convex Optimization*)
- **Record Path**: `data/curated/PageProbabilisticGradientEstimatorForNonconvexOptimization.yaml`
- **Primary Source**: Zhize Li, Hongyan Bao, Xiangliang Zhang, Peter Richtarik — *PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization* (`https://proceedings.mlr.press/v139/li21a.html`).

## Identity & Boundary Resolution

Distinct from double-loop recursive gradient methods SARAH (Nguyen et al. 2017, AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization), SPIDER (Fang et al. 2018, AIMech:SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization), and SpiderBoost (Wang et al. 2019, Round 376), which reset the gradient estimator at deterministic epoch boundaries mod(k, q) = 0; from L-SVRG / Loopless Katyusha (Kovalev et al. 2020, AIMech:LooplessSVRGAndLooplessKatyushaStochasticOptimization, which uses a loopless coin flip to update an anchor point w^t in the SVRG control-variate estimator nabla f_i(x^t) - nabla f_i(w^t) + nabla f(w^t) rather than switching between a fresh minibatch gradient and a recursive path-integrated step); and from STORM (Cutkosky & Orabona 2019, AIMech:StormStochasticRecursiveMomentumForNonconvexOptimization, which blends both terms at every step via deterministic weight a_t rather than a probabilistic two-branch estimator with unequal minibatch sizes b and b').

## Constructed Boundary & Regime Verification

```text
[PASS] Round 374 PAGE (Li et al. 2021): lemma3_exact=0.054279 <= ub=0.064107, eta_factor=0.50, grad_per_iter=198.02 < 200, cost_page=7930792.1 < cost_svrg=18576355.3 < cost_gd=400000000.0, pl_contraction=0.8750
```
