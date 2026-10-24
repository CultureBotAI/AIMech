# Discovery Report: Round 478 — FedMD (Heterogeneous Federated Learning via Public-Dataset Model Distillation)

- **Timestamp**: `2026-10-19T09:21:00Z`
- **Selected Concept**: `AIMech:FedMdHeterogeneousFederatedLearningViaPublicDatasetModelDistillation` (*FedMD (Heterogeneous Federated Learning via Public-Dataset Model Distillation)*)
- **Record Path**: `data/curated/FedMdHeterogeneousFederatedLearningViaPublicDatasetModelDistillation.yaml`
- **Primary Source**: Daliang Li, Junpu Wang — *FedMD: Heterogenous Federated Learning via Model Distillation* (`https://arxiv.org/abs/1910.03581`).

## Identity & Boundary Resolution

Distinct from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which exchanges model weights and performs ensemble distillation on the server into global prototype architectures rather than communicating only public-dataset logits f_k(x_i^0) and distilling on each client via alternating Digest and Revisit phases; and distinct from FedGKT (AIMech:FedGktGroupKnowledgeTransferForEdgeFederatedLearning, He et al. 2020), which exchanges intermediate feature maps and private-sample logits between small edge encoders and a large server classifier.

## Constructed Boundary & Regime Verification

```text
[PASS] FedMD boundary verification passed: disagreement_init=1.3974 -> disagreement_final=0.0173, het_params=[9, 15, 18], comm_floats=12
```
