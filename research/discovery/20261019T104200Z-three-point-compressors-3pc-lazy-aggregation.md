# Discovery Report: Round 559 — 3PC Three Point Compressors for Communication-Efficient Distributed Training

- **Timestamp**: `2026-10-19T10:42:00Z`
- **Selected Concept**: `AIMech:ThreePointCompressorsForCommunicationEfficientDistributedTraining` (*3PC Three Point Compressors for Communication-Efficient Distributed Training*)
- **Record Path**: `data/curated/ThreePointCompressorsForCommunicationEfficientDistributedTraining.yaml`
- **Primary Source**: Peter Richtarik, Igor Sokolov, Ilyas Fatkhullin, Elnur Gasanov, Zhize Li, Eduard Gorbunov — *3PC: Three Point Compressors for Communication-Efficient Distributed Training and a Better Theory for Lazy Aggregation* (`https://openalex.org/W4221138265`).

## Identity & Boundary Resolution

Introduced by Peter Richtarik, Igor Sokolov, Ilyas Fatkhullin, Elnur Gasanov, Zhize Li, and Eduard Gorbunov (ICML 2022, PMLR Vol. 162, pp. 18596-18648; arXiv:2202.00998). Distinct from EF21 (Richtarik, Sokolov, & Fatkhullin, NeurIPS 2021; Round 380), which is a single special case of 3PC without lazy trigger thresholds; and distinct from standalone Lazily Aggregated Gradient (LAG, Chen et al., NeurIPS 2018), which uses a multi-step weighted history condition without contractive compression or the single-step 3PC Lyapunov inequality.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 559 3PC/CLAG verified: dist_sq 6.9100 -> 2.494e-20, skipped=144/720, A_clag=0.1835, B_clag=3.6330
```
