# Discovery Report: Round 444 — Fed-RoD (Federated Robust Decoupling for Generic and Personalized Learning)

- **Timestamp**: `2026-10-19T08:47:00Z`
- **Selected Concept**: `AIMech:FedRodFederatedRobustDecouplingForGenericAndPersonalizedLearning` (*Fed-RoD (Federated Robust Decoupling for Generic and Personalized Learning)*)
- **Record Path**: `data/curated/FedRodFederatedRobustDecouplingForGenericAndPersonalizedLearning.yaml`
- **Primary Source**: Hong-You Chen, Wei-Lun Chao — *On Bridging Generic and Personalized Federated Learning for Image Classification* (`https://openreview.net/forum?id=I1hQbx10Kxn`).

## Identity & Boundary Resolution

Distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which discards a shared global classifier head and cannot perform zero-shot generic inference on unseen balanced test distributions, and from CCVR (AIMech:CcvrClassifierCalibrationWithVirtualRepresentationsForFederatedLearning, Luo et al. 2021), which calibrates only a generic head post-hoc using uploaded Gaussian feature covariances rather than jointly training a Bayes-optimal balanced generic head and an additive personalized residual head.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 444 Fed-RoD (Chen & Chao 2022): generic_bayes_err=2.78e-17, personalized_bayes_err=1.11e-16, generic_top=0 (0.70) vs client_top=1 (0.667)
```
