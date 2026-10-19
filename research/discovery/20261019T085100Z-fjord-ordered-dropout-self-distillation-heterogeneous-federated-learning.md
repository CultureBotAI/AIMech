# Discovery Report: Round 448 — FjORD (Fair and Accurate Federated Learning under Heterogeneous Targets with Ordered Dropout)

- **Timestamp**: `2026-10-19T08:51:00Z`
- **Selected Concept**: `AIMech:FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning` (*FjORD (Fair and Accurate Federated Learning under Heterogeneous Targets with Ordered Dropout)*)
- **Record Path**: `data/curated/FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning.yaml`
- **Primary Source**: Samuel Horvath, Stefanos Laskaridis, Mario Almeida, Ilias Leontiadis, Stylianos I. Venieris, Nicholas D. Lane — *FjORD: Fair and Accurate Federated Learning under heterogeneous targets with Ordered Dropout* (`https://proceedings.neurips.cc/paper/2021/hash/6aed000af86a084f9cb0264161e29dd3-Abstract.html`).

## Identity & Boundary Resolution

Distinct from HeteroFL (AIMech:HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning, Diao et al. 2021), which trains each client only at its single static capability width p_max^i rather than stochastically sampling all prefix widths p <= p_max^i via Ordered Dropout and self-distillation to enforce SVD-ordered representation importance across nested submodels.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 448 FjORD (Horvath et al. 2021): OD_err_b2=4.232 < RD_err_b2=26.315, KL_self_distill=0.1527 < KL_hard_only=0.1584
```
