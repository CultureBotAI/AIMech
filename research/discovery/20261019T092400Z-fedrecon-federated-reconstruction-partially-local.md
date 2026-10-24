# Discovery Report: Round 481 — FedRecon (Federated Reconstruction for Partially Local Federated Learning)

- **Timestamp**: `2026-10-19T09:24:00Z`
- **Selected Concept**: `AIMech:FedReconFederatedReconstructionForPartiallyLocalFederatedLearning` (*FedRecon (Federated Reconstruction for Partially Local Federated Learning)*)
- **Record Path**: `data/curated/FedReconFederatedReconstructionForPartiallyLocalFederatedLearning.yaml`
- **Primary Source**: Karan Singhal, Hakim Sidahmed, Zachary Garrett, Shanshan Wu, Keith Rush, Sushant Prakash — *Federated Reconstruction: Partially Local Federated Learning* (`https://arxiv.org/abs/2102.03448`).

## Identity & Boundary Resolution

Distinct from stateful partially local methods such as FedPer (AIMech:FedPerFederatedLearningWithPersonalizationLayers, Arivazhagan et al. 2019), FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), and LG-FedAvg (AIMech:LgFedAvgLocalGlobalRepresentationsFederatedLearning, Liang et al. 2020), all of which require clients to persistently store their private parameters across communication rounds and cannot directly evaluate on unseen stateless cross-device clients without a reconstruction step; FedRecon discards local parameters after every round and reconstructs them on the fly via support/query splitting, naturally generalizing to unseen clients at inference time via ReconEval.

## Constructed Boundary & Regime Verification

```text
[PASS] FedRecon boundary verification passed: unseen_ReconEval_MSE(k_r=0)=0.0400 -> unseen_ReconEval_MSE(k_r=10)=1.3486e-26
```
