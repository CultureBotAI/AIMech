# Discovery Report: Round 689 — SoRA (Sparse Low-Rank Adaptation)

- **Timestamp**: `2026-10-19T12:52:00Z`
- **Selected Concept**: `AIMech:SoRASparseLowRankAdaptation` (*SoRA (Sparse Low-Rank Adaptation)*)
- **Record Path**: `data/curated/SoRASparseLowRankAdaptation.yaml`
- **Primary Source**: Ning Ding, Xingtai Lv, Qiaosen Wang, Yulin Chen, Bowen Zhou, Zhiyuan Liu, Maosong Sun — *Sparse Low-rank Adaptation of Pre-trained Language Models* (`https://dblp.org/search/publ/api?q=2311.11696&format=xml`).

## Identity & Boundary Resolution

Distinct from AdaLoRA (AIMech:AdaLoRAAdaptiveBudgetAllocationForLoRA, which imposes explicit SVD orthogonality penalties R(U, V) = ||U^T U - I_p||_F^2 + ||V^T V - I_q||_F^2 and prunes triplets using heuristic moving-average weight-gradient sensitivity scores), from DyLoRA (AIMech:DyLoRADynamicSearchFreeLowRankAdaptation, which trains prefix sub-ranks via nested-dropout-style random rank sampling without sparse gating), and from RoSA (AIMech:RoSA, which trains a low-rank matrix plus a separate full-dimensional sparse residual matrix W^S). Formulated by Ding, Lv, Wang, Chen, Zhou, Liu, and Sun (EMNLP 2023, arXiv:2311.11696).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 689 SoRA (Ding et al., EMNLP 2023): r_max=6->r_eff=2, max_prune_diff=8.88e-16, g_t=[1.335, 0.0, -1.065, 0.0, 0.0, 0.0]
```
