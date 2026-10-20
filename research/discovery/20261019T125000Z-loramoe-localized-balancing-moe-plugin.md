# Discovery Report: Round 687 — LoRAMoE

- **Timestamp**: `2026-10-19T12:50:00Z`
- **Selected Concept**: `AIMech:LoRAMoE` (*LoRAMoE*)
- **Record Path**: `data/curated/LoRAMoE.yaml`
- **Primary Source**: Shihan Dou, Enyu Zhou, Yan Liu, Songyang Gao, Jun Zhao, Wei Shen, Yuhao Zhou, Zhiheng Xi, Xiao Wang, Xiaoran Fan, Shiliang Pu, Jiang Zhu, Rui Zheng, Tao Gui, Qi Zhang, Xuanjing Huang — *LoRAMoE: Alleviate World Knowledge Forgetting in Large Language Models via MoE-Style Plugin* (`https://dblp.org/search/publ/api?q=2312.09979&format=xml`).

## Identity & Boundary Resolution

Distinct from HydraLoRA (AIMech:HydraLoRA, which shares a single down-projection matrix A across multiple up-projection heads B_k without type-partitioned localized balancing), from MoLE (AIMech:MoLEMixtureOfLoRAExperts, which freezes pre-trained LoRAs and gates over their concatenated layer outputs), and from standard sparsely-gated MoE layers (which replace the entire FFN with full-rank experts and apply a single-distribution global coefficient-of-variation balancing loss). Formulated by Dou et al. (ACL 2024, arXiv:2312.09979).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 687 LoRAMoE (Dou et al., ACL 2024): L_lbc(localized)=0.00e+00 < L_lbc(unif)=0.0400 << L_lbc(collapsed)=5.2400
```
