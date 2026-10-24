# Discovery Report: Round 450 — FedAwS (Federated Averaging with Spreadout for Positive-Only Labels)

- **Timestamp**: `2026-10-19T08:53:00Z`
- **Selected Concept**: `AIMech:FedAwsFederatedAveragingWithSpreadoutForPositiveOnlyLabels` (*FedAwS (Federated Averaging with Spreadout for Positive-Only Labels)*)
- **Record Path**: `data/curated/FedAwsFederatedAveragingWithSpreadoutForPositiveOnlyLabels.yaml`
- **Primary Source**: Felix X. Yu, Ankit Singh Rawat, Aditya Krishna Menon, Sanjiv Kumar — *Federated Learning with Only Positive Labels* (`https://proceedings.mlr.press/v119/yu20f.html`).

## Identity & Boundary Resolution

Distinct from standard FedAvg and from FedProto (AIMech:FedProtoFederatedPrototypeLearningAcrossHeterogeneousClients, Tan et al. 2022), which assume each client observes multi-class labeled examples locally so negative classes are separated by client-side cross-entropy rather than learning from positive-only single-class client data via a server-side geometric spreadout regularizer on class embeddings.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 450 FedAwS (Yu et al. 2020): min_sep_fedaws=1.342 >> min_sep_naive=0.080, acc_fedaws=1.000 >> acc_naive=0.192, thm1_ratio=0.070<=1
```
