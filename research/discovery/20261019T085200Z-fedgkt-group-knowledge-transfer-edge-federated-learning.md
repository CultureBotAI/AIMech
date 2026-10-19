# Discovery Report: Round 449 — FedGKT (Group Knowledge Transfer for Federated Learning of Large CNNs at the Edge)

- **Timestamp**: `2026-10-19T08:52:00Z`
- **Selected Concept**: `AIMech:FedGktGroupKnowledgeTransferForEdgeFederatedLearning` (*FedGKT (Group Knowledge Transfer for Federated Learning of Large CNNs at the Edge)*)
- **Record Path**: `data/curated/FedGktGroupKnowledgeTransferForEdgeFederatedLearning.yaml`
- **Primary Source**: Chaoyang He, Murali Annavaram, Salman Avestimehr — *Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge* (`https://proceedings.neurips.cc/paper/2020/hash/a1d4c20b182ad7137ab3606f0e3fc8a4-Abstract.html`).

## Identity & Boundary Resolution

Distinct from FedDF (AIMech:FedDfEnsembleDistillationForModelFusionInFederatedLearning, Lin et al. 2020), which transmits full client model weights to the server and performs ensemble distillation on an unlabeled server proxy dataset rather than offloading deep CNN layers to the server via uploaded client hidden feature maps and bidirectional ground-truth + KL distillation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 449 FedGKT (He et al. 2020): edge_params=15<server_params=30, ce_server=0.5979 < ce_gkt_edge=0.9054 < ce_isolated=0.9188
```
