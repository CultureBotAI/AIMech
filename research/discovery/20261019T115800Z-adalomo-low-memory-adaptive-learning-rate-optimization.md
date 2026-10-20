# Discovery Report: Round 635 — AdaLomo (Low-Memory Optimization with Adaptive Learning Rate)

- **Timestamp**: `2026-10-19T11:58:00Z`
- **Selected Concept**: `AIMech:AdaLomoLowMemoryAdaptiveLearningRateOptimization` (*AdaLomo (Low-Memory Optimization with Adaptive Learning Rate)*)
- **Record Path**: `data/curated/AdaLomoLowMemoryAdaptiveLearningRateOptimization.yaml`
- **Primary Source**: Kai Lv, Hang Yan, Qipeng Guo, Haijun Lv, Xipeng Qiu — *AdaLomo: Low-memory Optimization with Adaptive Learning Rate* (`https://dblp.org/rec/conf/acl/Lv0GLQ24`).

## Identity & Boundary Resolution

Distinct from LOMO (AIMech:LomoFusedBackwardLowMemoryOptimization), which applies naive non-adaptive stochastic gradient descent during the fused backward pass and requires two backward passes whenever global gradient normalization is used; AdaLomo incorporates per-parameter second-moment scaling via row/column moving-average factors (r_{t,i}, c_{t,i}) and normalizes each tensor's update in a single fused backward pass via grouped update normalization. Distinct from Adafactor (AIMech:AdafactorSublinearMemoryAdaptiveOptimization), which materializes full-model gradients before the optimizer step and therefore consumes roughly 2.5x the memory of AdaLomo.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 635 AdaLomo verified: nmf_rank1_err=2.08e-17, state_comp=85.3x, grad_mem_ratio=0.0244, rms_match_err=0.00e+00, f_global=-2.000<f_local=-1.000
```
