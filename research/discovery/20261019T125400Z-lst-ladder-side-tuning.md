# Discovery Report: Round 691 — Ladder Side-Tuning (LST)

- **Timestamp**: `2026-10-19T12:54:00Z`
- **Selected Concept**: `AIMech:LadderSideTuning` (*Ladder Side-Tuning (LST)*)
- **Record Path**: `data/curated/LadderSideTuning.yaml`
- **Primary Source**: Yi-Lin Sung, Jaemin Cho, Mohit Bansal — *LST: Ladder Side-Tuning for Parameter and Memory Efficient Transfer Learning* (`https://dblp.org/search/publ/api?q=2206.06522&format=xml`).

## Identity & Boundary Resolution

Distinct from in-backbone PETL methods such as LoRA (AIMech:LoRA), LoRA-FA (AIMech:LoRAFA), Compacter (AIMech:CompacterLowRankHypercomplexAdapterLayers), and IA3 (AIMech:IA3ActivationRescaling), all of which insert trainable parameters inside the backbone and must cache backbone nonlinearity derivatives {sigma'} for chain-rule backpropagation (capping memory savings at <= 50%), and from vanilla Side-Tuning (which fuses representations only at the final output layer without intermediate gated ladder shortcuts, structural pruning initialization, or side-network layer dropping). Formulated by Sung, Cho, and Bansal (NeurIPS 2022, arXiv:2206.06522).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 691 LST (Sung et al., NeurIPS 2022): mem_ratio(LST)=0.125 < mem_ratio(in-backbone_PETL)>=0.50, kept_rows=[3, 11], side_shape=(2x2)
```
