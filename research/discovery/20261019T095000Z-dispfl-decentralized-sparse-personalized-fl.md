# Discovery Report: Round 507 — DisPFL: Decentralized Sparse Training for Personalized Federated Learning

- **Timestamp**: `2026-10-19T09:50:00Z`
- **Selected Concept**: `AIMech:DisPflDecentralizedSparseTrainingForPersonalizedFederatedLearning` (*DisPFL: Decentralized Sparse Training for Personalized Federated Learning*)
- **Record Path**: `data/curated/DisPflDecentralizedSparseTrainingForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Rong Dai, Li Shen, Fengxiang He, Xinmei Tian, Dacheng Tao — *DispFL: Towards Communication-Efficient Personalized Federated Learning via Decentralized Sparse Training* (`https://dblp.org/rec/conf/icml/DaiSHTT22`).

## Identity & Boundary Resolution

Distinct from centralized sparse FL algorithms such as PruneFL (AIMech:PruneFlAdaptiveDistributedParameterPruningForFederatedLearning; Jiang et al., IEEE TNNLS 2023), which maintains a single shared global pruned mask reconfigured by a central server to minimize global empirical risk rather than personalized per-client ERK masks over a decentralized peer-to-peer topology. Distinct from dense decentralized SGD algorithms such as D-PSGD (Lian et al., 2017) and D^2 (AIMech:D2VarianceReducedDecentralizedTrainingOverHeterogeneousData; Tang et al., ICML 2018), which communicate and average full dense parameter vectors across all nodes rather than performing support-intersection-normalized averaging combined with local magnitude pruning and gradient-magnitude regrowth.

## Constructed Boundary & Regime Verification

```text
DisPFL boundary verification passed: {'erk_densities': [0.5, 0.15, 0.6898], 'w_half': [4.0, 6.0, 0.0, -3.0], 'm_next': [1, 0, 1, 1, 0, 0, 1, 1]}
```
