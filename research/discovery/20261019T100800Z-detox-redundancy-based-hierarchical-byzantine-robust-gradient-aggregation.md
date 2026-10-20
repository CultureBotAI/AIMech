# Discovery Report: Round 525 — DETOX Redundancy-Based Hierarchical Byzantine-Robust Gradient Aggregation

- **Timestamp**: `2026-10-19T10:08:00Z`
- **Selected Concept**: `AIMech:DetoxRedundancyBasedHierarchicalByzantineRobustGradientAggregation` (*DETOX Redundancy-Based Hierarchical Byzantine-Robust Gradient Aggregation*)
- **Record Path**: `data/curated/DetoxRedundancyBasedHierarchicalByzantineRobustGradientAggregation.yaml`
- **Primary Source**: Shashank Rajput, Hongyi Wang, Zachary Charles, Dimitris Papailiopoulos — *DETOX: A Redundancy-based Framework for Faster and More Robust Gradient Aggregation* (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1907.12205`).

## Identity & Boundary Resolution

Distinct from DRACO (which requires r = 2s + 1 linear redundancy in the number of Byzantine nodes s to achieve exact zero-error gradient recovery without a second-stage statistical robust aggregator) and from standalone robust aggregators (Krum, Multi-Krum, Bulyan, Coordinate-Wise Median, Geometric Median) applied directly to all p ungrouped compute nodes. Specifically denotes the DETOX and HIER-AGGR algorithms of Rajput, Wang, Charles, & Papailiopoulos (NeurIPS 2019, Algorithms 1-2, Theorems 1 & 3, Corollary 2, Lemma 4).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 525 DETOX (Rajput et al. 2019): E[hat_q]_r3=1.4588<=lemma4=2.1600, hat_eps_decay=[0.2, 0.1012, 0.0534, 0.0284], err_detox=0.4726 < err_vanilla_med=0.8530
```
