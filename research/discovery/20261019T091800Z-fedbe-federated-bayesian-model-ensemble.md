# Discovery Report: Round 475 — FedBE (Federated Bayesian Model Ensemble via Stochastic Weight Average Distillation)

- **Timestamp**: `2026-10-19T09:18:00Z`
- **Selected Concept**: `AIMech:FedBeFederatedBayesianModelEnsembleViaStochasticWeightAverageDistillation` (*FedBE (Federated Bayesian Model Ensemble via Stochastic Weight Average Distillation)*)
- **Record Path**: `data/curated/FedBeFederatedBayesianModelEnsembleViaStochasticWeightAverageDistillation.yaml`
- **Primary Source**: Hong-You Chen, Wei-Lun Chao — *FedBE: Making Bayesian Model Ensemble Applicable to Federated Learning* (`https://arxiv.org/abs/2009.01974`).

## Identity & Boundary Resolution

Distinct from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which distills only the direct average of client logits without fitting a Gaussian or Dirichlet global parameter posterior p(w | D), sampling additional higher-quality global models w^{(m)} ~ p(w | D), or applying cyclical Stochastic Weight Averaging (SWA) during server distillation; and distinct from FedPA (AIMech:FedPaFederatedPosteriorAveragingViaLocalMcmcAndShrinkageCovariance, Al-Shedivat et al. 2021), which estimates local client posteriors via MCMC and shrinkage covariance on clients rather than server-side Bayesian ensemble distillation.

## Constructed Boundary & Regime Verification

```text
[PASS] FedBE boundary verification passed: |p_ens-p_fedavg|=3.7692e-03, KD_loss_init=0.64316 -> KD_loss_SWA=0.63516
```
