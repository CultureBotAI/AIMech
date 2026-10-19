# Discovery Report: Round 372 — SNVRG (Stochastic Nested Variance Reduction) for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:35:00Z`
- **Selected Concept**: `AIMech:SnvrgStochasticNestedVarianceReductionForNonconvexOptimization` (*SNVRG (Stochastic Nested Variance Reduction) for Non-Convex Optimization*)
- **Record Path**: `data/curated/SnvrgStochasticNestedVarianceReductionForNonconvexOptimization.yaml`
- **Primary Source**: Dongruo Zhou, Pan Xu, Quanquan Gu — *Stochastic Nested Variance Reduction for Nonconvex Optimization* (`https://jmlr.org/papers/v21/19-055.html`).

## Identity & Boundary Resolution

Distinct from two-level SVRG (which corresponds to K = 1 in SNVRG and requires O(n^{2/3} * varepsilon^{-2}) or O(varepsilon^{-10/3}) gradient complexity) and distinct from SPIDER (Round 345, Fang et al. 2018), which updates at every step using the immediate predecessor x_{j-1} and requires accuracy-dependent normalized step sizes eta = O(varepsilon / L), whereas SNVRG uses K = O(log n) or O(log(1/varepsilon)) nested reference levels with a large constant step size eta = 1/(6L) and adapts automatically across the full-gradient, Polyak-Lojasiewicz, and non-convex stationary regimes.

## Constructed Boundary & Regime Verification

```text
[PASS] SNVRG boundaries verified: T=B^(1/2), Lemma A.1 & Lemma C.2 hold for K=2,3,4, ref_indices(K=2)=[(0, 0, 0), (0, 0, 1), (0, 2, 2), (0, 2, 3)]
```
