# Discovery Report: Round 655 — Representation Finetuning (ReFT) and Low-Rank Linear Subspace ReFT (LoReFT)

- **Timestamp**: `2026-10-19T12:18:00Z`
- **Selected Concept**: `AIMech:ReftAndLoreftLowRankLinearSubspaceRepresentationFinetuning` (*Representation Finetuning (ReFT) and Low-Rank Linear Subspace ReFT (LoReFT)*)
- **Record Path**: `data/curated/ReftAndLoreftLowRankLinearSubspaceRepresentationFinetuning.yaml`
- **Primary Source**: Zhengxuan Wu, Aryaman Arora, Zheng Wang, Atticus Geiger, Dan Jurafsky, Christopher D. Manning, Christopher Potts — *ReFT: Representation Finetuning for Language Models* (`https://dblp.org/rec/conf/nips/WuAWGJMP24.html`).

## Identity & Boundary Resolution

Distinct from weight-based PEFT methods such as LoRA (Hu et al., 2022), DoRA (Liu et al., 2024), and VeRA (Kopiczko et al., 2024), which modify weight matrices across all sequence positions and merge updates into weights, whereas ReFT/LoReFT never modifies weights and instead intervenes selectively on hidden representations at specific token positions P (e.g., p prefix and s suffix tokens). Also distinct from RED (Wu et al., 2024a) and (IA)^3 (Liu et al., 2022), which apply element-wise scaling and bias to activations at every token position rather than performing a rank-r orthogonal subspace replacement R^T (W h + b - R h) on a small subset of prompt positions.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 655 ReFT/LoReFT boundary and mathematical verification succeeded.
```
