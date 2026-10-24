# Discovery Report: Round 424 — FedBABU (Federated Averaging with Body Aggregation and Body Update)

- **Timestamp**: `2026-10-19T08:27:00Z`
- **Selected Concept**: `AIMech:FedBabuFederatedAveragingWithBodyAggregationAndBodyUpdate` (*FedBABU (Federated Averaging with Body Aggregation and Body Update)*)
- **Record Path**: `data/curated/FedBabuFederatedAveragingWithBodyAggregationAndBodyUpdate.yaml`
- **Primary Source**: Jaehoon Oh, SangMook Kim, Se-Young Yun — *FedBABU: Toward Enhanced Representation for Federated Image Classification* (`https://openreview.net/forum?id=HuaYQfggn5u`).

## Identity & Boundary Resolution

Distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which actively updates each client's local linear head theta_{i,cls} via local gradient steps before updating the shared body in every round, whereas FedBABU keeps a single shared random orthogonal head completely frozen (alpha_cls = 0) during federated representation learning so all clients share identical fixed class decision boundaries.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 424 FedBABU (Oh et al. 2022): orthogonal_head_dot=0.0, margin_fedbabu=5.8679 > margin_fedavg=4.4917
```
