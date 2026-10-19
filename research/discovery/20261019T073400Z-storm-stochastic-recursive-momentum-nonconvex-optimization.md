# Discovery Report: Round 371 — STORM (Stochastic Recursive Momentum) for Single-Loop Adaptive Variance-Reduced Non-Convex SGD

- **Timestamp**: `2026-10-19T07:34:00Z`
- **Selected Concept**: `AIMech:StormStochasticRecursiveMomentumForNonconvexOptimization` (*STORM (Stochastic Recursive Momentum) for Single-Loop Adaptive Variance-Reduced Non-Convex SGD*)
- **Record Path**: `data/curated/StormStochasticRecursiveMomentumForNonconvexOptimization.yaml`
- **Primary Source**: Ashok Cutkosky, Francesco Orabona — *Momentum-Based Variance Reduction in Non-Convex SGD* (`https://dblp.org/rec/conf/nips/CutkoskyO19.xml`).

## Identity & Boundary Resolution

Distinct from SPIDER (Round 345, Fang et al. 2018) and SARAH (Round 344, Nguyen et al. 2017), which use an unweighted recursive estimator v_t = nabla f(x_t, xi_t) - nabla f(x_{t-1}, xi_t) + v_{t-1} (corresponding to a_t = 0) whose accumulated martingale variance grows linearly with t and requires periodic double-loop restarts with O(sigma^2/varepsilon^2) or O(n) checkpoint mega-batches, whereas STORM multiplies the previous error by (1 - a_t) < 1 with a_t = c * eta_{t-1}^2 to damp accumulated error in a single loop without any mega-batch checkpoints.

## Constructed Boundary & Regime Verification

```text
[PASS] STORM boundaries verified: Lyapunov B_t <= -24*L^2*eta_t*||eps_t||^2 holds for all t, noise variance reduced from 0.3573 to 0.0827 (< 0.25*sigma^2=0.1600)
```
