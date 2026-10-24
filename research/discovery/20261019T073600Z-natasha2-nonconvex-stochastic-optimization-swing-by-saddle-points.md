# Discovery Report: Round 373 — Natasha 2 Non-Convex Stochastic Optimization via Swing-by Saddle Points

- **Timestamp**: `2026-10-19T07:36:00Z`
- **Selected Concept**: `AIMech:Natasha2NonconvexStochasticOptimizationViaSwingBySaddlePoints` (*Natasha 2 Non-Convex Stochastic Optimization via Swing-by Saddle Points*)
- **Record Path**: `data/curated/Natasha2NonconvexStochasticOptimizationViaSwingBySaddlePoints.yaml`
- **Primary Source**: Zeyuan Allen-Zhu — *Natasha 2: Faster Non-Convex Optimization Than SGD* (`https://papers.nips.cc/paper/2018/hash/2b64c2f19d868305aa8bbc2d72902cc5-Abstract.html`).

## Identity & Boundary Resolution

Distinct from deterministic accelerated gradient + negative-curvature exploitation (Carmon et al. 2018, AIMech:AcceleratedGradientAndNegativeCurvatureExploitationForNonConvexOptimization, which requires exact gradients and exact Hessian-vector products in O_tilde(varepsilon^{-7/4})), from perturbed SGD/GD (Ge et al. 2015; Jin et al. 2017/2018, which add isotropic balls of noise and require O_tilde(varepsilon^{-4}) in the online stochastic setting), and from pure first-order variance reduction methods (SVRG, SCSG, SPIDER, SNVRG, STORM, which assume first-order L-smoothness or multi-batch variance reduction without alternating Oja negative-curvature steps with proximal retraction sigma = 1.5*delta to convert online second-order smoothness into a faster O_tilde(varepsilon^{-3.25}) first-order stochastic complexity without Hessian-vector oracle calls).

## Constructed Boundary & Regime Verification

```text
[PASS] Natasha 1.5 & Natasha 2 boundaries verified: 2nd-order step decrease=0.002370 == delta^3/(12*L2^2)=0.002370, Lemma 5.5 |grad F(x*)|=0.4000 == 2*sigma*|x*-x_hat|, eps^-3.25=3162277.7 < eps^-10/3=4641588.8 < eps^-4=100000000.0
```
