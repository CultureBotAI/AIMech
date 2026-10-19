# Discovery Report: Round 344 — SARAH Stochastic Recursive Gradient for Finite-Sum Optimization

- **Timestamp**: `2026-10-19T07:06:00Z`
- **Selected Concept**: `AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization` (*SARAH Stochastic Recursive Gradient for Finite-Sum Optimization*)
- **Record Path**: `data/curated/SARAHStochasticRecursiveGradientForFiniteSumOptimization.yaml`
- **Primary Source**: Lam M. Nguyen, Jie Liu, Katya Scheinberg, Martin Takac — *SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient* (`https://proceedings.mlr.press/v70/nguyen17b.html`).

## Identity & Boundary Resolution

Distinct from SVRG, which uses the conditionally unbiased snapshot difference grad f_{i_t}(w_t) - grad f_{i_t}(w_0) + v_0 whose inner-loop step variance does not vanish as t -> infinity within a single outer loop, from SAG/SAGA, which require O(n d) storage of n past component gradients, and from SPIDER (`AIMech:SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization`), which couples recursive path-integrated differential estimation with normalized gradient descent (stepsize proportional to epsilon / ||v^k||) and negative-curvature search for non-convex first- and second-order stationarity. Specifically captures the SARAH recursive estimator (Equation 2), the exact martingale variance identity (Lemma 2) and convex error bound (Lemma 3), the inner-loop linear contraction of E[||v_t||^2] (Theorems 1a-1b), the outer-loop linear rate sigma_m < alpha_m (Theorem 4 and Remark 1), and the adaptive SARAH+ inner stopping rule ||v_{t-1}||^2 > gamma ||v_0||^2 (Algorithm 2).

## Constructed Boundary & Regime Verification

```text
[PASS] SARAH boundaries verified: Lemma2_var=0.057370==0.057370, inner_v_sarah=1.97e-09 vs inner_v_svrg=0.729, sigma_m=1.302<alpha_m=2.750, SARAH+_g8=1.90e-07<<g1=8.35e-02
```
