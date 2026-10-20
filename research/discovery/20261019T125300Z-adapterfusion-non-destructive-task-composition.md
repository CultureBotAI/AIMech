# Discovery Report: Round 690 — AdapterFusion

- **Timestamp**: `2026-10-19T12:53:00Z`
- **Selected Concept**: `AIMech:AdapterFusion` (*AdapterFusion*)
- **Record Path**: `data/curated/AdapterFusion.yaml`
- **Primary Source**: Jonas Pfeiffer, Aishwarya Kamath, Andreas Ruckle, Kyunghyun Cho, Iryna Gurevych — *AdapterFusion: Non-Destructive Task Composition for Transfer Learning* (`https://dblp.org/search/publ/api?q=2005.00247&format=xml`).

## Identity & Boundary Resolution

Distinct from sequential fine-tuning (which overwrites model parameters and suffers catastrophic forgetting), from joint multi-task adapter training (MT-A, which requires simultaneous access to all datasets and suffers inter-task gradient interference), and from LoRA composition methods such as LoraHub (AIMech:LoraHub) and MoLE (AIMech:MoLEMixtureOfLoRAExperts). Formulated by Pfeiffer, Kamath, Ruckle, Cho, and Gurevych (EACL 2021, pp. 487-503, arXiv:2005.00247).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 690 AdapterFusion (Pfeiffer et al., EACL 2021): s_a[1]=1.00000, s_b[2]=1.00000, forgetting_drift=0.0e+00, fusion_mse=9.52e-11 << single_adapter_mse=16.00
```
