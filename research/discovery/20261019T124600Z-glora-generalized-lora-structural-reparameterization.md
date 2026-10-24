# Discovery Report: Round 683 — Generalized LoRA

- **Timestamp**: `2026-10-19T12:46:00Z`
- **Selected Concept**: `AIMech:GLoRA` (*Generalized LoRA*)
- **Record Path**: `data/curated/GLoRA.yaml`
- **Primary Source**: Arnav Chavan, Zhuang Liu, Deepak Gupta, Eric Xing, Zhiqiang Shen — *One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning* (`https://dblp.org/rec/journals/corr/abs-2306-07967.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which tunes only an additive low-rank weight residual B without weight scaling A, layer-wise prompt vector C, or bias scale/shift tensors D and E), from DoRA (AIMech:DoraWeightDecomposedLowRankAdaptation, which normalizes column-wise weight directions and learns a magnitude vector rather than searching heterogeneous support tensor types {LoRA, vector, scalar, none} in a multi-path supernet), and from DyLoRA (AIMech:DyLoRADynamicSearchFreeLowRankAdaptation, which orders ranks within a single LoRA pair via nested dropout rather than searching across five distinct support tensor roles). Formulated by Chavan et al. (arXiv:2306.07967).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 683 GLoRA (Chavan et al., 2023): configs_per_layer=432, max_reparam_err=8.88e-16, deg_err=3.33e-16
```
