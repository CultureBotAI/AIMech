# Discovery Report: Round 584 — GaLore (Gradient Low-Rank Projection)

- **Timestamp**: `2026-10-19T11:07:00Z`
- **Selected Concept**: `AIMech:GaLoreGradientLowRankProjectionForMemoryEfficientLlmTraining` (*GaLore (Gradient Low-Rank Projection)*)
- **Record Path**: `data/curated/GaLoreGradientLowRankProjectionForMemoryEfficientLlmTraining.yaml`
- **Primary Source**: Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, Yuandong Tian — *GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection* (`https://dblp.org/search/publ/api?q=GaLore+Memory-Efficient+LLM+Training+by+Gradient+Low-Rank+Projection&format=json`).

## Identity & Boundary Resolution

Distinct from Low-Rank Adaptation (LoRA, AIMech:LowRankAdaptation) and ReLoRA, which reparameterize the weight matrix itself as W = W_0 + B A (restricting updates within each phase to a bilinear product B A that alters gradient dynamics and requires mn + 3mr + 3nr memory). GaLore keeps W_t as a single full-rank m x n matrix, never introduces bilinear adaptor factors B A, and reduces optimizer-state memory by projecting the gradient G_t before applying stateful regularizers rho_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 584 GaLore verified: sr_0=1.0045->sr_final=1.000000, err_galore_sq=1.214e-17<<lora_min=5.0, mem=(3407872<4456448<6291456)
```
