# Discovery Report: Round 651 — Weight-Decomposed Low-Rank Adaptation (DoRA)

- **Timestamp**: `2026-10-19T12:14:00Z`
- **Selected Concept**: `AIMech:DoraWeightDecomposedLowRankAdaptation` (*Weight-Decomposed Low-Rank Adaptation (DoRA)*)
- **Record Path**: `data/curated/DoraWeightDecomposedLowRankAdaptation.yaml`
- **Primary Source**: Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang, KT Cheng, Min-Hung Chen — *DoRA: Weight-Decomposed Low-Rank Adaptation* (`https://dblp.org/rec/conf/icml/LiuWY0WCC24.html`).

## Identity & Boundary Resolution

Distinct from standard Low-Rank Adaptation (LoRA, Hu et al., 2022), which updates W' = W_0 + B A directly without column-wise directional normalization ||W_0 + B A||_c or an independent magnitude vector m, causing LoRA to exhibit a positive coupling between magnitude and directional changes that struggles to make fine-grained directional adjustments without simultaneous large magnitude shifts. Also distinct from Weight Normalization (Salimans & Kingma, 2016), which trains full weight matrices V from random initialization rather than freezing W_0 and adapting V via a low-rank increment Delta V = B A.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 651 DoRA boundary and mathematical verification succeeded.
```
