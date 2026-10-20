# Discovery Report: Round 583 — Sophia (Second-Order Clipped Stochastic Optimization)

- **Timestamp**: `2026-10-19T11:06:00Z`
- **Selected Concept**: `AIMech:SophiaSecondOrderClippedStochasticOptimization` (*Sophia (Second-Order Clipped Stochastic Optimization)*)
- **Record Path**: `data/curated/SophiaSecondOrderClippedStochasticOptimization.yaml`
- **Primary Source**: Hong Liu, Zhiyuan Li, David Leo Wright Hall, Percy Liang, Tengyu Ma — *Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training* (`https://dblp.org/search/publ/api?q=Sophia+A+Scalable+Stochastic+Second-order+Optimizer+for+Language+Model&format=json`).

## Identity & Boundary Resolution

Distinct from Adam/AdamW (which precondition by the empirical Fisher diagonal v_t = EMA(g_t odot g_t) computed with true labels y_b rather than model-sampled labels hat{y}_b ~ p(theta, x_b), conflating residual loss magnitude with curvature) and from unclipped diagonal Newton/AdaHessian methods (which can converge to local maxima or saddle points under negative curvature and require every-step Hessian-vector products). Whenever a coordinate's curvature h_{t,[i]} <= 0 or m_{t,[i]} / (gamma h_{t,[i]}) > rho, Sophia automatically falls back to clipped SignGD/Lion-like constant displacement +-eta_t rho on that coordinate.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 583 Sophia verified: err_soph=2.835e-11<<err_sign=2.500e-01, gnb_diff=2.78e-17, kappa_1e6_loss=1.034e-19
```
