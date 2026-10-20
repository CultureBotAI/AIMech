# Discovery Report: Round 647 — ACProp Momentum-Centered Asynchronous Adaptive Gradient Optimization

- **Timestamp**: `2026-10-19T12:10:00Z`
- **Selected Concept**: `AIMech:ACPropMomentumCenteringAsynchronousAdaptiveGradientOptimization` (*ACProp Momentum-Centered Asynchronous Adaptive Gradient Optimization*)
- **Record Path**: `data/curated/ACPropMomentumCenteringAsynchronousAdaptiveGradientOptimization.yaml`
- **Primary Source**: Juntang Zhuang, Yifan Ding, Tommy Tang, Nicha C. Dvornek, Sekhar Tatikonda, James S. Duncan — *Momentum Centering and Asynchronous Update for Adaptive Gradient Methods* (`https://dblp.org/rec/conf/nips/ZhuangDTDTD21`).

## Identity & Boundary Resolution

Distinct from synchronous uncentered adaptive optimizers (AIMech:Adam, AIMech:RMSProp, AIMech:AMSGrad, AIMech:RAdam), which include g_t^2 inside the step-t denominator v_t; distinct from synchronous centered adaptive optimizers (AIMech:AdaBelief, AIMech:SDProp), which center the second moment via (g_t - m_t)^2 but evaluate s_t synchronously in the step-t denominator; and distinct from asynchronous uncentered optimizers (AIMech:AdaShift), which decorrelate numerator and denominator using uncentered v_{t-n} that decays exponentially to zero during zero-gradient intervals.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 647 ACProp boundary and mathematical verification succeeded.
```
