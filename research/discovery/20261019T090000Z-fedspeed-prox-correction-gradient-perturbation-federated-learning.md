# Discovery Report: Round 457 — FedSpeed (Prox-Correction and Extra-Gradient Perturbation for Federated Learning)

- **Timestamp**: `2026-10-19T09:00:00Z`
- **Selected Concept**: `AIMech:FedSpeedProxCorrectionAndGradientPerturbationForFederatedLearning` (*FedSpeed (Prox-Correction and Extra-Gradient Perturbation for Federated Learning)*)
- **Record Path**: `data/curated/FedSpeedProxCorrectionAndGradientPerturbationForFederatedLearning.yaml`
- **Primary Source**: Yan Sun, Li Shen, Tiansheng Huang, Liang Ding, Dacheng Tao — *FedSpeed: Larger Local Interval, Less Communication Round, and Higher Generalization Accuracy* (`https://openreview.net/forum?id=bZjxxYURKT`).

## Identity & Boundary Resolution

Distinct from FedDyn (AIMech:FedDynDynamicRegularizationForFederatedLearning, Acar et al. 2021), whose convergence proof requires each active client to find an exact stationary point of the local dynamic-regularized subproblem in every round and which uses standard single-point gradients rather than an extra-gradient ascent quasi-gradient g~_{i,k}^t and post-processed upload x^hat_i^t = x_{i,K}^t - lambda*g^hat_i^t; and distinct from FedSAM (AIMech:FedSamAndFedAsamSharpnessAwareMinimizationAndStochasticWeightAveragingForFederatedLearning, Caldarola et al. 2022), which lacks the local prox-term, the exponential-decay prox-correction momentum g^hat_i^t, and the O(1/T) large-interval K = O(T) non-convex convergence guarantee.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 457 FedSpeed verified: lemma1_err=3.33e-16, lemma2_err=8.88e-16, err_fedspeed=4.44e-16
```
