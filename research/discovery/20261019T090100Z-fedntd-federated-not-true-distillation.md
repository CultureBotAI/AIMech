# Discovery Report: Round 458 — FedNTD (Federated Not-True Distillation for Global Knowledge Preservation)

- **Timestamp**: `2026-10-19T09:01:00Z`
- **Selected Concept**: `AIMech:FedNtdNotTrueDistillationForFederatedLearning` (*FedNTD (Federated Not-True Distillation for Global Knowledge Preservation)*)
- **Record Path**: `data/curated/FedNtdNotTrueDistillationForFederatedLearning.yaml`
- **Primary Source**: Gihun Lee, Minchan Jeong, Yongjin Shin, Sangmin Bae, Se-Young Yun — *Preservation of the Global Knowledge by Not-True Distillation in Federated Learning* (`https://arxiv.org/abs/2106.03097`).

## Identity & Boundary Resolution

Distinct from FedLSD (Federated Local Self-Distillation) and full-logit client-side knowledge distillation methods that distill all C logits including the ground-truth class y, which couples the distillation gradient with in-local class adaptation L_KL^true and degrades new local knowledge acquisition under severe non-IID skew; and distinct from server-side ensemble distillation methods such as FedDF (AIMech:FedDfEnsembleKnowledgeDistillationForFederatedModelFusion, Lin et al. 2020) and FedGEN (AIMech:FedGenDataFreeKnowledgeDistillationForHeterogeneousFederatedLearning, Zhu et al. 2021), as FedNTD operates purely during client local training without proxy datasets or generative models.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 458 FedNTD verified: Lambda(0)=1.8250->Lambda(1.5)=1.0516, dL_NTD/dz_y=0.0e+00, Prop2_diff=3.47e-18
```
