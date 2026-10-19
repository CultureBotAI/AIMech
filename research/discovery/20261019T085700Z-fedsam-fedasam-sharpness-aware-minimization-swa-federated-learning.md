# Discovery Report: Round 454 — FedSAM and FedASAM (Sharpness-Aware Minimization and Server Stochastic Weight Averaging for Federated Learning)

- **Timestamp**: `2026-10-19T08:57:00Z`
- **Selected Concept**: `AIMech:FedSamAndFedAsamSharpnessAwareMinimizationAndStochasticWeightAveragingForFederatedLearning` (*FedSAM and FedASAM (Sharpness-Aware Minimization and Server Stochastic Weight Averaging for Federated Learning)*)
- **Record Path**: `data/curated/FedSamAndFedAsamSharpnessAwareMinimizationAndStochasticWeightAveragingForFederatedLearning.yaml`
- **Primary Source**: Debora Caldarola, Barbara Caputo, Marco Ciccone — *Improving Generalization in Federated Learning by Seeking Flat Minima* (`https://doi.org/10.1007/978-3-031-20050-2_38`).

## Identity & Boundary Resolution

Distinct from centralized SAM (AIMech:SharpnessAwareMinimization, Foret et al. 2021) and centralized SWA (AIMech:StochasticWeightAveraging, Izmailov et al. 2018), which operate on a single centralized model without cross-client parameter averaging or heterogeneous client drift; and distinct from FedSpeed (AIMech:FedSpeedProxCorrectionAndGradientPerturbationForFederatedLearning, Sun et al. 2023), which combines a local proximal regularizer and prox-correction momentum variable g^hat_i^t with unnormalized extra-gradient perturbation rather than scale-invariant ASAM and server-side cyclic SWA.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 454 FedSAM/FedASAM verified: g_flat=-0.8556<g_sharp=-0.4227, sam_flat=-0.6881<<sam_sharp=-0.0427
```
