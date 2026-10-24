# Discovery Report: Round 646 — DyLoRA (Dynamic Search-Free Low-Rank Adaptation)

- **Timestamp**: `2026-10-19T12:09:00Z`
- **Selected Concept**: `AIMech:DyLoRADynamicSearchFreeLowRankAdaptation` (*DyLoRA (Dynamic Search-Free Low-Rank Adaptation)*)
- **Record Path**: `data/curated/DyLoRADynamicSearchFreeLowRankAdaptation.yaml`
- **Primary Source**: Mojtaba Valipour, Mehdi Rezagholizadeh, Ivan Kobyzev, Ali Ghodsi — *DyLoRA: Parameter-Efficient Tuning of Pretrained Models using Dynamic Search-Free Low Rank Adaptation* (`https://dblp.org/rec/conf/eacl/ValipourRKG23`).

## Identity & Boundary Resolution

Distinct from static LoRA (AIMech:LowRankAdaptation), which trains adapter matrices for a single fixed rank r and suffers severe accuracy degradation if truncated to a smaller rank b < r at inference time without retraining from scratch. Distinct from AdaLoRA (AIMech:AdaLoraAdaptiveBudgetLowRankAdaptation), which prunes singular values of SVD-parameterized adapters to a single final static budget allocation across layers rather than ordering prefix representations to support dynamic multi-rank inference from a single checkpoint. Distinct from Nested Dropout (Rippel et al., 2014), which orders vector bottleneck activations using a weighted sum of losses over all truncations rather than sampling one rank b per batch on factorized weight matrices.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 646 DyLoRA verified: losses_dylora=[4.4431, 2.2189, 1.0166, 0.8449], avg_low_dylora=2.5596<<avg_low_static=12.3246, frozen_prefix_diff=0.0e+00
```
