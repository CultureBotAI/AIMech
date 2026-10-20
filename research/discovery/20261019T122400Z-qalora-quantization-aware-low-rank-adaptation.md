# Discovery Report: Round 661 — Quantization-Aware Low-Rank Adaptation (QA-LoRA)

- **Timestamp**: `2026-10-19T12:24:00Z`
- **Selected Concept**: `AIMech:QaloraQuantizationAwareLowRankAdaptation` (*Quantization-Aware Low-Rank Adaptation (QA-LoRA)*)
- **Record Path**: `data/curated/QaloraQuantizationAwareLowRankAdaptation.yaml`
- **Primary Source**: Yuhui Xu, Lingxi Xie, Xiaotao Gu, Xin Chen, Heng Chang, Hengheng Zhang, Zhengsu Chen, Xiaopeng Zhang, Qi Tian — *QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models* (`https://dblp.org/rec/conf/iclr/XuXGCCZ0T24.html`).

## Identity & Boundary Resolution

Distinct from QLoRA (Dettmers et al., 2023; AIMech:QloraQuantizedLowRankAdaptation) and LoftQ (Li et al., 2024; AIMech:LoftqLoraFineTuningAwareQuantization), which use unconstrained D_in x D_int adapter matrices A that cannot be merged into column-wise or group-wise N-bit quantized weights without either converting the merged matrix back to FP16 or applying lossy post-training quantization (PTQ).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 661 QA-LoRA (Xu et al. 2024): max_merge_err=1.78e-15 << ptq_err=0.3171, adapter_params=96<192
```
