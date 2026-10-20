# Discovery Report: Round 474 — FedProto (Federated Prototype Learning across Heterogeneous Clients)

- **Timestamp**: `2026-10-19T09:17:00Z`
- **Selected Concept**: `AIMech:FedProtoFederatedPrototypeLearningAcrossHeterogeneousClients` (*FedProto (Federated Prototype Learning across Heterogeneous Clients)*)
- **Record Path**: `data/curated/FedProtoFederatedPrototypeLearningAcrossHeterogeneousClients.yaml`
- **Primary Source**: Yue Tan, Guodong Long, Lu Liu, Tianyi Zhou, Qinghua Lu, Jing Jiang, Chengqi Zhang — *FedProto: Federated Prototype Learning across Heterogeneous Clients* (`https://arxiv.org/abs/2105.00243`).

## Identity & Boundary Resolution

Distinct from FedPer (AIMech:FedPerFederatedLearningWithPersonalizationLayers, Arivazhagan et al. 2019) and FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which exchange and average homogeneous base-layer weight tensors in parameter space; and distinct from FedGen (AIMech:FedGenDataFreeFederatedKnowledgeDistillationViaServerLatentGenerator, Zhu, Hong, & Zhou 2021), which trains a conditional generator on the server from uploaded classifier heads rather than aggregating mean class feature prototypes C_bar^{(j)} across architecturally heterogeneous encoders.

## Constructed Boundary & Regime Verification

```text
[PASS] FedProto boundary verification passed: global_classes=[0, 1, 2], one_round_delta=-0.4792<0, comm_floats=18 vs model_params=64200
```
