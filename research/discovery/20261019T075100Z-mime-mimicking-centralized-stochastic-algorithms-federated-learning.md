# Discovery Report: Round 388 — Mime Framework for Mimicking Centralized Stochastic Algorithms in Federated Learning

- **Timestamp**: `2026-10-19T07:51:00Z`
- **Selected Concept**: `AIMech:MimeMimickingCentralizedStochasticAlgorithmsInFederatedLearning` (*Mime Framework for Mimicking Centralized Stochastic Algorithms in Federated Learning*)
- **Record Path**: `data/curated/MimeMimickingCentralizedStochasticAlgorithmsInFederatedLearning.yaml`
- **Primary Source**: Sai Praneeth Karimireddy, Martin Jaggi, Satyen Kale, Mehryar Mohri, Sashank J. Reddi, Sebastian U. Stich, Ananda Theertha Suresh — *Mime: Mimicking Centralized Stochastic Algorithms in Federated Learning* (`https://proceedings.neurips.cc/paper/2021/hash/ecbe1ef9a0c869f69725461b9028c196-Abstract.html`).

## Identity & Boundary Resolution

Distinct from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which requires stateful clients to store persistent control variates c_i across rounds and fails when clients are stateless or sampled once), from FedDyn (AIMech:FedDynDynamicRegularizationForFederatedLearning, which also requires stateful client gradient vectors), and from FedNova (AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization, which normalizes local step lengths rather than freezing server optimizer statistics s_{t-1} and applying cross-device SVRG control variates). No pinned AIO class covers Mime or stateless cross-device optimizer mimicking.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 388 Mime (Karimireddy et al. 2021): delta0_drift=8.88e-16, mime_err=8.42e-08 << naive_local_mom_err=0.2216
```
