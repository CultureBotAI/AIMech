# Discovery Report: Round 476 — LG-FedAvg (Local Global Federated Averaging)

- **Timestamp**: `2026-10-19T09:19:00Z`
- **Selected Concept**: `AIMech:LgFedAvgLocalGlobalRepresentationsFederatedLearning` (*LG-FedAvg (Local Global Federated Averaging)*)
- **Record Path**: `data/curated/LgFedAvgLocalGlobalRepresentationsFederatedLearning.yaml`
- **Primary Source**: Paul Pu Liang, Terrance Liu, Liu Ziyin, Nicholas B. Allen, Randy P. Auerbach, David Brent, Ruslan Salakhutdinov, Louis-Philippe Morency — *Think Locally, Act Globally: Federated Learning with Local and Global Representations* (`https://arxiv.org/abs/2001.01523`).

## Identity & Boundary Resolution

Distinct from FedPer (AIMech:FedPerFederatedLearningWithPersonalizationLayers, Arivazhagan et al. 2019) and FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which reverse the architectural split by keeping lower feature-extraction layers global (W_B) and top classification heads private on each client; in contrast, LG-FedAvg keeps lower feature-extraction encoders theta_m^l local (allowing modality-specific or adversarially de-biased encoders) and shares only the compact top global classifier theta^g across clients.

## Constructed Boundary & Regime Verification

```text
[PASS] LG-FedAvg boundary verification passed: alpha^*(high_rho)=0.8333 > alpha^*(low_rho)=0.3333, comm_ratio=0.0539
```
