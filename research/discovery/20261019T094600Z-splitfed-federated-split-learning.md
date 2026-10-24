# Discovery Report: Round 503 — SplitFed Learning

- **Timestamp**: `2026-10-19T09:46:00Z`
- **Selected Concept**: `AIMech:SplitFedFederatedAndSplitLearningHybridArchitecture` (*SplitFed Learning*)
- **Record Path**: `data/curated/SplitFedFederatedAndSplitLearningHybridArchitecture.yaml`
- **Primary Source**: Chandra Thapa, M. A. P. Chamikara, Seyit Camtepe, Lichao Sun — *SplitFed: When Federated Learning Meets Split Learning* (`https://doi.org/10.1609/aaai.v36i8.20825`).

## Identity & Boundary Resolution

Distinct from standard Federated Learning (AIMech:FederatedAveraging), where each client trains and communicates the entire un-split model W, and from sequential Split Learning (Gupta & Raskar, 2018; Vepakomma et al., 2018), where clients train the client-side sub-network in a relay fashion one client at a time without parallel FedServer client-side aggregation. Distinct from FedGKT (AIMech:FedGktGroupKnowledgeTransferForEdgeFederatedLearning; He et al., NeurIPS 2020), which uses alternating bi-directional KL-divergence knowledge distillation between compact edge feature extractors and a server classifier rather than exact cut-layer activation/gradient backpropagation coupled with FedAvg of client-side sub-networks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 503 SplitFed (Thapa et al., AAAI 2022): time_SFLV2=2.306 < time_SFLV1=2.406 < time_SL=6.128, comm_SFL=4.13e+07 < comm_FL=4.00e+08, split-FedAvg exact match=(w_C=1.117200, w_S=-0.675800)
```
