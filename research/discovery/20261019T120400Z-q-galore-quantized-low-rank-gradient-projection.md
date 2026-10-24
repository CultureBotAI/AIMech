# Discovery Report: Round 641 — Q-GaLore (Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients)

- **Timestamp**: `2026-10-19T12:04:00Z`
- **Selected Concept**: `AIMech:QGaLoreQuantizedLowRankGradientProjection` (*Q-GaLore (Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients)*)
- **Record Path**: `data/curated/QGaLoreQuantizedLowRankGradientProjection.yaml`
- **Primary Source**: Zhenyu Zhang, Ajay Jaiswal, Lu Yin, Shiwei Liu, Jiawei Zhao, Yuandong Tian, Zhangyang Wang — *Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients* (`https://dblp.org/rec/conf/cpal/ZhangJYLZTW25`).

## Identity & Boundary Resolution

Distinct from GaLore (AIMech:GaLoreGradientLowRankProjection), which maintains full BF16/FP16 master weights, stores projection matrices in 16-bit floating point (or 8-bit in Q-GaLore baseline), and recomputes SVD projections at a fixed uniform interval across all layers. Distinct from QLoRA (AIMech:QloraQuantizedLowRankAdaptation), which freezes 4-bit NormalFloat base weights and optimizes only additive low-rank adapter matrices rather than updating the full-rank weight matrix in INT8 via quantized low-rank gradient projections.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 641 Q-GaLore verified: cos_early=0.2525<gamma=0.4<cos_stat=0.9992, SVD_calls=5/50, cos_INT4=0.99947, w_stoch=-2.920(target=-3.0) vs w_det=1.0, mem_save=80.7%
```
