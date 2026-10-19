# Discovery Report: Round 382 — Choco-SGD and Choco-Gossip Decentralized Optimization with Compressed Communication

- **Timestamp**: `2026-10-19T07:45:00Z`
- **Selected Concept**: `AIMech:ChocoSgdAndChocoGossipDecentralizedCompressedOptimization` (*Choco-SGD and Choco-Gossip Decentralized Optimization with Compressed Communication*)
- **Record Path**: `data/curated/ChocoSgdAndChocoGossipDecentralizedCompressedOptimization.yaml`
- **Primary Source**: Anastasia Koloskova, Sebastian U. Stich, Martin Jaggi — *Decentralized Stochastic Optimization and Gossip Algorithms with Compressed Communication* (`https://proceedings.mlr.press/v97/koloskova19a.html`).

## Identity & Boundary Resolution

Distinct from centralized/parameter-server error-compensated compression (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression and AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization, which assume a central coordinator or all-to-all aggregation rather than decentralized graph gossip with spectral gap delta), and from uncompressed periodic local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent). No pinned AIO class covers decentralized compressed gossip or Choco-SGD.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 382 Choco-SGD and Choco-Gossip boundaries verified.
```
