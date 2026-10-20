# Discovery Report: Round 511 — FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations

- **Timestamp**: `2026-10-19T09:54:00Z`
- **Selected Concept**: `AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation` (*FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations*)
- **Record Path**: `data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml`
- **Primary Source**: Ziyao Wang, Zheyu Shen, Yexiao He, Guoheng Sun, Hongyi Wang, Lingjuan Lyu, Ang Li — *FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Low-Rank Adaptations* (`https://dblp.org/rec/conf/nips/WangSHS0LL24`).

## Identity & Boundary Resolution

Distinct from FFA-LoRA (AIMech:FfaLoraFederatedFreezeALowRankAdaptation; Sun et al., ICLR 2024), which eliminates aggregation cross-terms by freezing a homogeneous random projection matrix A_0 across all clients rather than training both A_k and B_k with heterogeneous client ranks r_k and stacking them on the server. Distinct from FedIT (Zhang et al., 2023) and zero-padded heterogeneous LoRA (HetLoRA; Cho et al., 2023), which average A_k and B_k separately and suffer from cross-client product noise (sum_k p_k B_k)(sum_k p_k A_k) != sum_k p_k B_k A_k. Also distinct from centralized memory-efficient low-rank gradient projection (Flora; Hao et al., 2024), which resamples random projection matrices on a single machine rather than stacking multi-client heterogeneous LoRA adapters in federated learning.

## Constructed Boundary & Regime Verification

```text
FLoRA boundary verification passed: {'stacked_rank': 6, 'flora_err': 7.033790317987055e-17, 'fedit_zeropad_err': 0.691864, 'perm_err': 7.033790317987055e-17}
```
