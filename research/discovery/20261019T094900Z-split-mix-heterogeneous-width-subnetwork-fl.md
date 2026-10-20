# Discovery Report: Round 506 — Split-Mix Federated Learning

- **Timestamp**: `2026-10-19T09:49:00Z`
- **Selected Concept**: `AIMech:SplitMixHeterogeneousWidthSubnetworkFederatedLearning` (*Split-Mix Federated Learning*)
- **Record Path**: `data/curated/SplitMixHeterogeneousWidthSubnetworkFederatedLearning.yaml`
- **Primary Source**: Junyuan Hong, Haotao Wang, Zhangyang Wang, Jiayu Zhou — *Efficient Split-Mix Federated Learning for On-Demand and In-Situ Customization* (`https://dblp.org/rec/conf/iclr/HongWWZ22`).

## Identity & Boundary Resolution

Distinct from nested width-slimming heterogeneous FL algorithms such as HeteroFL (AIMech:HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning; Diao et al., ICLR 2021) and FjORD (AIMech:FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning; Horvath et al., NeurIPS 2021), which slice nested prefix channel blocks from a single monolithic parameter tensor (causing wider channel blocks to be trained exclusively on wide-budget clients) rather than decomposing the model into M = floor(1/r) modular width-r base sub-networks sampled cyclically across all clients and ensembled on demand at inference time. Distinct from FedRolex (AIMech:FedRolexModelHeterogeneousFederatedLearningWithRollingSubModelExtraction; Alam et al., NeurIPS 2022), which extracts a deterministic rolling channel window from a single global model rather than maintaining M independent width-r base sub-networks with training-free Dual Batch-Normalization mixing.

## Constructed Boundary & Regime Verification

```text
Split-Mix boundary verification passed: {'base_counts': [20, 20, 20, 20], 'mses_by_K_R': [0.10877, 0.07314, 0.03555, 0.0217]}
```
