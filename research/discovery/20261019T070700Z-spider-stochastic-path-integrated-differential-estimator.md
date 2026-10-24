# Discovery Report: Round 345 — SPIDER Stochastic Path-Integrated Differential Estimator for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:07:00Z`
- **Selected Concept**: `AIMech:SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization` (*SPIDER Stochastic Path-Integrated Differential Estimator for Non-Convex Optimization*)
- **Record Path**: `data/curated/SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization.yaml`
- **Primary Source**: Cong Fang, Chris Junchi Li, Zhouchen Lin, Tong Zhang — *SPIDER: Near-Optimal Non-Convex Optimization via Stochastic Path-Integrated Differential Estimator* (`https://papers.nips.cc/paper/2018/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html`).

## Identity & Boundary Resolution

Distinct from SARAH (`AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization`), which uses unnormalized gradient descent steps x_{t+1} = x_t - eta v_t with constant stepsize eta = Theta(1/L) for convex/strongly-convex objectives rather than Normalized Gradient Descent stepsizes proportional to epsilon / ||v^k||, and from Perturbed Gradient Descent (`AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization`), which uses full-batch gradients with isotropic ball noise in O(n epsilon^{-2}) evaluations. Specifically captures the general SPIDER martingale integration framework and Pinelis vector-martingale concentration bound (Proposition 1 and Lemma 1), the NGD-coupled SPIDER-SFO algorithm and matching finite-sum lower bound (Algorithm 1, Theorems 1-5), the NEON2-fused second-order stationary point solver SPIDER-SFO+ with mini-step negative-curvature maintenance (Algorithm 2, Theorem 6), and the two-point Gaussian zeroth-order solver SPIDER-SZO (Algorithm 3, Theorem 8).

## Constructed Boundary & Regime Verification

```text
[PASS] SPIDER boundaries verified: Prop1_var=3.122787e-03==3.122787e-03<=5.625000e-02, max_err_sq=2.597e-04<=eps^2=2.500e-03, final_grad=0.0000, spider_cost=1.10e+07<svrg_cost=1.01e+08
```
