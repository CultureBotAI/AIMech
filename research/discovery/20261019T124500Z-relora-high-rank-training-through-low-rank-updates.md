# Discovery Report: Round 682 — ReLoRA

- **Timestamp**: `2026-10-19T12:45:00Z`
- **Selected Concept**: `AIMech:ReLoRA` (*ReLoRA*)
- **Record Path**: `data/curated/ReLoRA.yaml`
- **Primary Source**: Vladislav Lialin, Sherin Muckatira, Namrata Shivagunde, Anna Rumshisky — *ReLoRA: High-Rank Training Through Low-Rank Updates* (`https://dblp.org/rec/conf/iclr/LialinMSR24.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which trains a single pair of low-rank matrices whose update rank is bounded above by r without restarts or warm-start pre-training), from Chain of LoRA (AIMech:ChainOfLoRA, which fine-tunes already pretrained models via a Frank-Wolfe conditional-gradient chain with step-down rank schedules rather than pre-training transformers with a full-rank warm start, magnitude-pruned partial Adam moment resets, and a jagged cosine learning rate schedule), and from GaLore (AIMech:GaLoreGradientLowRankProjection, which projects full-parameter gradients into low-rank subspaces via SVD rather than parameterizing linear layers with merged-and-reinitialized LoRA adapters). Formulated by Lialin et al. (ICLR 2024, arXiv:2307.05695).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 682 ReLoRA (Lialin et al., ICLR 2024): rank_lora=2 -> rank_relora=8, err_lora=5.4350 -> err_relora=1.8545
```
