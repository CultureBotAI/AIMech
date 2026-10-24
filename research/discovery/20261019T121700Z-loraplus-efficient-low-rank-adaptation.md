# Discovery Report: Round 654 — LoRA+ (Asymmetric Learning Rate Low-Rank Adaptation)

- **Timestamp**: `2026-10-19T12:17:00Z`
- **Selected Concept**: `AIMech:LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates` (*LoRA+ (Asymmetric Learning Rate Low-Rank Adaptation)*)
- **Record Path**: `data/curated/LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates.yaml`
- **Primary Source**: Soufiane Hayou, Nikhil Ghosh, Bin Yu — *LoRA+: Efficient Low Rank Adaptation of Large Models* (`https://dblp.org/rec/conf/icml/HayouG024.html`).

## Identity & Boundary Resolution

Distinct from standard LoRA (Hu et al., 2022), which updates both A and B using the same learning rate eta_A = eta_B = eta and consequently suffers from inefficient feature learning in large-width models (where either delta_t^1 = o(1) or intermediate features explode as width n grows). Also distinct from structural LoRA reparameterizations such as DoRA (Liu et al., 2024) and PiSSA (Meng et al., 2024), which alter the forward-pass weight decomposition or SVD initialization rather than the relative optimizer step sizes eta_B / eta_A.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 654 LoRA+ boundary and mathematical verification succeeded.
```
