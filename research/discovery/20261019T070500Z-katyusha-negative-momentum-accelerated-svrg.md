# Discovery Report: Round 343 — Katyusha Direct Negative-Momentum Acceleration for Stochastic Variance-Reduced Optimization

- **Timestamp**: `2026-10-19T07:05:00Z`
- **Selected Concept**: `AIMech:KatyushaDirectNegativeMomentumAccelerationForStochasticVarianceReducedOptimization` (*Katyusha Direct Negative-Momentum Acceleration for Stochastic Variance-Reduced Optimization*)
- **Record Path**: `data/curated/KatyushaDirectNegativeMomentumAccelerationForStochasticVarianceReducedOptimization.yaml`
- **Primary Source**: Zeyuan Allen-Zhu — *Katyusha: The First Direct Acceleration of Stochastic Gradient Methods* (`https://jmlr.org/papers/v18/16-410.html`).

## Identity & Boundary Resolution

Distinct from Catalyst Universal Acceleration (`AIMech:CatalystUniversalAccelerationForFirstOrderOptimization`), which wraps a variance-reduced solver inside an inexact proximal-point outer loop and incurs an extra O(log(L/sigma)) factor and only O(sqrt(b)) mini-batch parallel speedup, and from unaccelerated SVRG, SAGA, or SARAH (`AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization`), which have O((n + L/sigma) log(1/epsilon)) linear dependence on the condition number kappa = L/sigma. Specifically captures the three-way iterate coupling x_{k+1} = tau_1 z_k + tau_2 x_tilde^s + (1 - tau_1 - tau_2) y_k with Katyusha negative momentum tau_2, the Lemma 2.4 tight Bregman variance bound cancellation, the direct non-strongly convex variant Katyusha^{ns} (Algorithm 2, Theorem 4.1), the mini-batch non-uniform smoothness variant Katyusha1 (Algorithm 3, Theorem 5.4), and the non-Euclidean Bregman variant Katyusha2 (Section 6, Theorems 6.1-6.2).

## Constructed Boundary & Regime Verification

```text
[PASS] Katyusha boundaries verified: Lemma2.4_var=0.158596<=0.250180, coupling_diff=3.33e-16, err_kat=1.345e-07 vs err_svrg=1.458e-05, b0=8.0 parallel_speedup=4.71x
```
