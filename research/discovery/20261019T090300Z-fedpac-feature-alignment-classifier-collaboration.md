# Discovery Report: Round 460 — FedPAC (Personalized Federated Learning with Feature Alignment and Classifier Collaboration)

- **Timestamp**: `2026-10-19T09:03:00Z`
- **Selected Concept**: `AIMech:FedPacFeatureAlignmentAndClassifierCollaborationForPersonalizedFederatedLearning` (*FedPAC (Personalized Federated Learning with Feature Alignment and Classifier Collaboration)*)
- **Record Path**: `data/curated/FedPacFeatureAlignmentAndClassifierCollaborationForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Jian Xu, Xinyi Tong, Shao-Lun Huang — *Personalized Federated Learning with Feature Alignment and Classifier Collaboration* (`https://arxiv.org/abs/2306.11867`).

## Identity & Boundary Resolution

Distinct from FedRep (AIMech:FedRepSharedRepresentationPersonalizedFederatedLearning, Collins et al. 2021) and FedPer (AIMech:FedPerFederatedLearningWithPersonalizationLayers), which keep each client's classifier head strictly local without inter-client classifier collaboration or global centroid alignment; and distinct from FedProto (AIMech:FedProtoFederatedPrototypeLearning, Tan et al. 2022), which communicates only class prototypes without aggregating shared feature extractors or solving a bias-variance quadratic program for personalized classifier combinations.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 460 FedPAC verified: alpha_opt=[0.622, 0.328, 0.05, 0.0], R_opt=0.0374 < R_local=0.0596 < R_unif=0.4380
```
