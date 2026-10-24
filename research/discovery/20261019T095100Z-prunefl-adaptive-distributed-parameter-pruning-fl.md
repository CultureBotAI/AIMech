# Discovery Report: Round 508 — PruneFL: Adaptive and Distributed Parameter Pruning for Federated Learning

- **Timestamp**: `2026-10-19T09:51:00Z`
- **Selected Concept**: `AIMech:PruneFlAdaptiveDistributedParameterPruningForFederatedLearning` (*PruneFL: Adaptive and Distributed Parameter Pruning for Federated Learning*)
- **Record Path**: `data/curated/PruneFlAdaptiveDistributedParameterPruningForFederatedLearning.yaml`
- **Primary Source**: Yuang Jiang, Shiqiang Wang, Victor Valls, Bong Jun Ko, Wei-Han Lee, Kin K. Leung, Leandros Tassiulas — *Model Pruning Enables Efficient Federated Learning on Edge Devices* (`https://doi.org/10.1109/tnnls.2022.3166101`).

## Identity & Boundary Resolution

Distinct from personalized sparse federated learning methods such as DisPFL (AIMech:DisPflDecentralizedSparseTrainingForPersonalizedFederatedLearning; Dai et al., ICML 2022), which maintain client-specific fixed-density masks over a decentralized peer-to-peer graph rather than dynamically resizing a shared global model mask M_k via an exact greedy optimizer of the risk-reduction-per-unit-time ratio Gamma(M). Distinct from static post-training or lottery-ticket initialization pruning (Frankle & Carbin, 2019), which fixes a predetermined target sparsity ratio and requires rewinding weights to initialization rather than adaptively shrinking and regrowing the active parameter set during ongoing federated optimization.

## Constructed Boundary & Regime Verification

```text
PruneFL boundary verification passed: {'optimal_subset_size': 4, 'optimal_gamma': 1.442424, 'stage2_subset_size': 5, 'stage2_gamma': 3.060811}
```
