# Discovery Report: Round 658 — LoRA-Fine-Tuning-Aware Quantization (LoftQ)

- **Timestamp**: `2026-10-19T12:21:00Z`
- **Selected Concept**: `AIMech:LoftqLoraFineTuningAwareQuantization` (*LoRA-Fine-Tuning-Aware Quantization (LoftQ)*)
- **Record Path**: `data/curated/LoftqLoraFineTuningAwareQuantization.yaml`
- **Primary Source**: Yixiao Li, Yifan Yu, Chen Liang, Pengcheng He, Nikos Karampatziakis, Weizhu Chen, Tuo Zhao — *LoftQ: LoRA-Fine-Tuning-Aware Quantization for Large Language Models* (`https://dblp.org/rec/conf/iclr/Li00KHCZ24.html`).

## Identity & Boundary Resolution

Distinct from QLoRA (Dettmers et al., 2023; AIMech:QloraQuantizedLowRankAdaptation), which quantizes W once without regard to LoRA (Q = q_N(W)) and initializes A B^T = 0 with Gaussian A and zero B, causing severe starting-point discrepancy ||W - Q||_F in the 2-bit to 4-bit regime. Also distinct from PiSSA (Meng et al., 2024; AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation), which performs SVD directly on the full-precision weight W rather than alternating quantization and SVD on the quantization residual W - Q_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 658 LoftQ boundary and mathematical verification succeeded.
```
