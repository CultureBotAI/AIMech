# Discovery Report: Round 483 — FedPop and FedSOUK (Bayesian Mixed-Effects Population Personalized Federated Learning)

- **Timestamp**: `2026-10-19T09:26:00Z`
- **Selected Concept**: `AIMech:FedPopAndFedSoukBayesianHierarchicalPopulationPersonalizedFederatedLearning` (*FedPop and FedSOUK (Bayesian Mixed-Effects Population Personalized Federated Learning)*)
- **Record Path**: `data/curated/FedPopAndFedSoukBayesianHierarchicalPopulationPersonalizedFederatedLearning.yaml`
- **Primary Source**: Nikita Kotelevskii, Maxime Vono, Alain Durmus, Eric Moulines — *FedPop: A Bayesian Approach for Personalised Federated Learning* (`https://arxiv.org/abs/2206.03611`).

## Identity & Boundary Resolution

Distinct from pFedBayes (AIMech:PFedBayesPersonalizedFederatedLearningViaVariationalBayesianInference, Zhang et al. 2022), which places a full-dimensional diagonal Gaussian variational distribution over all neural network weights (doubling communication cost) rather than a mixed-effects model with deterministic shared representation phi and low-dimensional Langevin-sampled random effects z_i in R^d (d << d_phi); and distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which computes point-estimate local heads z_i without a shared population prior N(z_0, Gamma), empirical Bayes shrinkage on small-sample clients, or posterior uncertainty quantification.

## Constructed Boundary & Regime Verification

```text
[PASS] FedPop/FedSOUK boundary verification passed: mean_small=1.000 (shrunk toward z0=2.0), mean_large=-2.902, z0_est=2.0000==2.0000, contract=0.6250
```
