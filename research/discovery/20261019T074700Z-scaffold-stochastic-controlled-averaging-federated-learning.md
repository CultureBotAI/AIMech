# Discovery Report: Round 384 — SCAFFOLD Stochastic Controlled Averaging for Heterogeneous Federated Learning

- **Timestamp**: `2026-10-19T07:47:00Z`
- **Selected Concept**: `AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning` (*SCAFFOLD Stochastic Controlled Averaging for Heterogeneous Federated Learning*)
- **Record Path**: `data/curated/ScaffoldStochasticControlledAveragingForFederatedLearning.yaml`
- **Primary Source**: Sai Praneeth Karimireddy, Satyen Kale, Mehryar Mohri, Sashank J. Reddi, Sebastian U. Stich, Ananda Theertha Suresh — *SCAFFOLD: Stochastic Controlled Averaging for Federated Learning* (`https://proceedings.mlr.press/v119/karimireddy20a.html`).

## Identity & Boundary Resolution

Distinct from uncorrected periodic local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent, which Theorem II proves suffers an unavoidable Omega(G^2 / (mu^2 * R^2)) client-drift lower bound when K >= 2 under gradient dissimilarity G > 0), from proximal penalty stabilization without control variates (AIMech:FedProxProximalHeterogeneousFederatedOptimization), and from single-machine or every-step compressed variance reduction (AIMech:PageProbabilisticGradientEstimatorForNonconvexOptimization and AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization). Narrower than AIO:FederatedLearning, which covers the general federated learning paradigm without specifying stateful client/server control-variate drift correction.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 384 SCAFFOLD Stochastic Controlled Averaging boundaries verified.
```
