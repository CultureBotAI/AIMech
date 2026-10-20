# Discovery Report: Round 479 — pFedBayes (Personalized Federated Learning via Variational Bayesian Inference)

- **Timestamp**: `2026-10-19T09:22:00Z`
- **Selected Concept**: `AIMech:PFedBayesPersonalizedFederatedLearningViaVariationalBayesianInference` (*pFedBayes (Personalized Federated Learning via Variational Bayesian Inference)*)
- **Record Path**: `data/curated/PFedBayesPersonalizedFederatedLearningViaVariationalBayesianInference.yaml`
- **Primary Source**: Xu Zhang, Yinchuan Li, Wenpeng Li, Kaiyang Guo, Yunfeng Shao — *Personalized Federated Learning via Variational Bayesian Inference* (`https://proceedings.mlr.press/v162/zhang22o.html`).

## Identity & Boundary Resolution

Distinct from pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, T. Dinh et al. 2020), which regularizes deterministic point-estimate weights via an L2 Moreau envelope (zeta/2) ||w_i - w||_2^2 without modeling posterior weight uncertainty sigma_i^2 or optimizing an evidence lower bound; and distinct from FedPA (AIMech:FedPaFederatedPosteriorAveragingViaLocalMcmcAndShrinkageCovariance, Al-Shedivat et al. 2021) and FedBE (AIMech:FedBeFederatedBayesianModelEnsembleViaStochasticWeightAverageDistillation, Chen & Chao 2021), which construct a single global posterior rather than bi-level personalized variational Bayesian posteriors P_{theta_i}(w_i) coupled to a learned global variational prior P_theta(w).

## Constructed Boundary & Regime Verification

```text
[PASS] pFedBayes boundary verification passed: F(w^*)=3.28634, minimax_rate=n^(-2*beta/(2*beta+d))=0.03162
```
