# Discovery Report: Round 468 — FedTHE (Test-Time Robust Personalized Federated Learning with Two-Head Ensemble)

- **Timestamp**: `2026-10-19T09:11:00Z`
- **Selected Concept**: `AIMech:FedTheTestTimeHeadEnsembleForPersonalizedFederatedLearning` (*FedTHE (Test-Time Robust Personalized Federated Learning with Two-Head Ensemble)*)
- **Record Path**: `data/curated/FedTheTestTimeHeadEnsembleForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Liangze Jiang, Tao Lin — *Test-Time Robust Personalization for Federated Learning* (`https://openreview.net/forum?id=3a1522662c`).

## Identity & Boundary Resolution

Distinct from FedRoD (AIMech:FedRodBridgingGenericAndPersonalizedFederatedLearning, Chen & Chao 2022), which trains dual generic (balanced softmax) and personalized heads but uses fixed static head selection or addition at test time without per-sample entropy minimization or cosine-similarity feature temperature scaling; and distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which discards the global head and evaluates only a local personalized head that fails on out-of-client shifted test classes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 468 FedTHE verified: ID(1-e*=1.00, lam_s=0.939), OoC(e*=1.00, lam_s=0.065, pred_class=3)
```
