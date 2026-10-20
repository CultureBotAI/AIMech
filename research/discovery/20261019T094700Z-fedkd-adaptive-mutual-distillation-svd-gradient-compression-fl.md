# Discovery Report: Round 504 — FedKD: Communication-Efficient Federated Learning via Knowledge Distillation

- **Timestamp**: `2026-10-19T09:47:00Z`
- **Selected Concept**: `AIMech:FedKdCommunicationEfficientFederatedLearningViaKnowledgeDistillation` (*FedKD: Communication-Efficient Federated Learning via Knowledge Distillation*)
- **Record Path**: `data/curated/FedKdCommunicationEfficientFederatedLearningViaKnowledgeDistillation.yaml`
- **Primary Source**: Chuhan Wu, Fangzhao Wu, Lingjuan Lyu, Yongfeng Huang, Xing Xie — *FedKD: Communication Efficient Federated Learning via Knowledge Distillation* (`https://doi.org/10.1038/s41467-022-29763-x`).

## Identity & Boundary Resolution

Distinct from proxy-dataset federated ensemble distillation methods such as FedMD (AIMech:FedMdHeterogeneousFederatedLearningViaPublicDatasetModelDistillation; Li & Wang, 2019) and FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning; Lin et al., NeurIPS 2020), which require a shared or unlabeled public dataset to exchange or ensemble logits; FedKD requires no shared dataset and instead exchanges SVD-factorized gradients of a compact local student model that mutually distills with each client's private large teacher model. Distinct from FedGKT (AIMech:FedGktGroupKnowledgeTransferForEdgeFederatedLearning; He et al., 2020), which offloads a large classifier to the server and exchanges intermediate feature maps and logits.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 504 FedKD (Wu et al., Nat. Commun. 2022): w_early=0.3338 -> w_late=3.7330, K(t=0)=4 (T=0.95) -> K(t=1)=7 (T=0.98), compression_ratio=5.88x
```
