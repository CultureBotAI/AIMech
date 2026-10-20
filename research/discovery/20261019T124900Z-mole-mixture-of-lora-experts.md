# Discovery Report: Round 686 — MoLE (Mixture of LoRA Experts)

- **Timestamp**: `2026-10-19T12:49:00Z`
- **Selected Concept**: `AIMech:MoLEMixtureOfLoRAExperts` (*MoLE (Mixture of LoRA Experts)*)
- **Record Path**: `data/curated/MoLEMixtureOfLoRAExperts.yaml`
- **Primary Source**: Xun Wu, Shaohan Huang, Furu Wei — *Mixture of LoRA Experts* (`https://dblp.org/search/publ/api?q=2404.13628&format=xml`).

## Identity & Boundary Resolution

Distinct from LoraHub (AIMech:LoraHub, which optimizes static scalar weights per LoRA module via gradient-free black-box optimization), from LoRA-Flow (AIMech:LoRAFlow, which computes token-level gates directly from the pre-LoRA hidden state x^l_t without concatenating LoRA expert outputs or optimizing a log-product gating balancing loss), and from LoRAMoE (AIMech:LoRAMoE, which trains LoRA experts from scratch inside FFN blocks with a localized balancing constraint to prevent world knowledge forgetting during SFT rather than composing separately pre-trained frozen LoRAs). Formulated by Wu, Huang, and Wei (ICLR 2024, arXiv:2404.13628).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32 << nla_err=43.80 < unnorm_err=50.70, L_bal(uniform)=3.2958 < L_bal(collapsed)=6.0968
```
