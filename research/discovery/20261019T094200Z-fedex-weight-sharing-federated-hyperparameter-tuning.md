# Discovery Report: Round 499 — FedEx Weight-Sharing Exponentiated Gradient for Federated Hyperparameter Tuning

- **Timestamp**: `2026-10-19T09:42:00Z`
- **Selected Concept**: `AIMech:FedExWeightSharingExponentiatedGradientForFederatedHyperparameterTuning` (*FedEx Weight-Sharing Exponentiated Gradient for Federated Hyperparameter Tuning*)
- **Record Path**: `data/curated/FedExWeightSharingExponentiatedGradientForFederatedHyperparameterTuning.yaml`
- **Primary Source**: Mikhail Khodak, Renbo Tu, Tian Li, Liam Li, Maria-Florina Balcan, Virginia Smith, Ameet Talwalkar — *Federated Hyperparameter Tuning: Challenges, Baselines, and Connections to Weight-Sharing* (`https://dblp.org/search/publ/api?q=Federated+Hyperparameter+Tuning+Khodak+Balcan+Talwalkar&format=json`).

## Identity & Boundary Resolution

Distinct from standard Federated Averaging (AIO:FederatedLearning) and Per-FedAvg (AIMech:PerFedAvgModelAgnosticMetaLearningForPersonalizedFederatedLearning), which use fixed client hyperparameters rather than maintaining and updating a categorical distribution D_theta over local training hyperparameters via weight-sharing exponentiated gradient.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 499 FedEx (Khodak et al. 2021): unbiased_grad_err=5.55e-17, theta_opt=0.9999 >> runner_up=0.0001, reg_tau5000=0.5565 < reg_tau50=2.0074
```
