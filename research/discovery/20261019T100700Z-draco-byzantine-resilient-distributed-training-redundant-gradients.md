# Discovery Report: Round 524 — DRACO Byzantine-Resilient Distributed Training via Redundant Gradients

- **Timestamp**: `2026-10-19T10:07:00Z`
- **Selected Concept**: `AIMech:DracoByzantineResilientDistributedTrainingViaRedundantGradients` (*DRACO Byzantine-Resilient Distributed Training via Redundant Gradients*)
- **Record Path**: `data/curated/DracoByzantineResilientDistributedTrainingViaRedundantGradients.yaml`
- **Primary Source**: Lingjiao Chen, Hongyi Wang, Zachary Charles, Dimitris Papailiopoulos — *DRACO: Byzantine-resilient Distributed Training via Redundant Gradients* (`https://proceedings.mlr.press/v80/chen18l.html`).

## Identity & Boundary Resolution

Distinct from approximate statistical robust aggregators (Krum, Bulyan, Coordinate-Wise Median, Trimmed-Mean, Geometric Median) that do not use algorithmic gradient redundancy and do not recover the exact adversary-free gradient sum, and distinct from DETOX (which uses logarithmic or small odd redundancy r to filter most Byzantine nodes via majority vote before applying approximate hierarchical robust aggregation rather than exact coding recovery with r = 2s + 1). Specifically denotes the DRACO framework of Chen, Wang, Charles, & Papailiopoulos (ICML 2018, PMLR 80:903-912, Definitions 1-2, Theorems 1, 2, 5, Lemmas 3-4, Algorithms 1-2).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 524 DRACO (Chen et al. 2018): thm1_tau4_indistinguishable=True, err_rep=8.88e-16, cyclic_detected=[4], err_cyc=2.58e-15
```
