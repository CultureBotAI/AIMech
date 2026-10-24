# Discovery Report: Round 375 — SCSG (Stochastically Controlled Stochastic Gradient) for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:38:00Z`
- **Selected Concept**: `AIMech:ScsgStochasticallyControlledStochasticGradientForNonconvexOptimization` (*SCSG (Stochastically Controlled Stochastic Gradient) for Non-Convex Optimization*)
- **Record Path**: `data/curated/ScsgStochasticallyControlledStochasticGradientForNonconvexOptimization.yaml`
- **Primary Source**: Lihua Lei, Cheng Ju, Jianbo Chen, Michael I. Jordan — *Non-convex Finite-Sum Optimization Via SCSG Methods* (`https://papers.nips.cc/paper/2017/hash/2eb5657d37f474e4c4cf01e4882b8962-Abstract.html`).

## Identity & Boundary Resolution

Distinct from classical SVRG (Johnson & Zhang 2013; Reddi et al. 2016; Allen-Zhu & Hazan 2016), which computes a full n-sample gradient at every outer epoch (incurring an unavoidable O(n + n^{2/3} / varepsilon_g^2) cost even when n >> varepsilon_g^{-2}) and uses a fixed deterministic epoch length m with uniform random iterate selection; from SAGA (Defazio et al. 2014, AIMech:SagaFastIncrementalGradientMethodWithSupportForNonStronglyConvexCompositeObjectives), which stores O(n*d) gradient tables; and from recursive path-integrated estimators (SARAH, SPIDER, SNVRG, STORM, PAGE), which update the gradient estimate incrementally from x_{t-1} rather than from a geometrically terminated epoch anchor xtilde_{j-1}.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 375 SCSG (Lei et al. 2017): geom_id_err=5.55e-17, wo_repl_var=0.260832 <= 0.358644, B_scsg=1000 << n=1000000, cost_scsg=11000 << cost_sgd=1000000 < cost_svrg=11000000
```
