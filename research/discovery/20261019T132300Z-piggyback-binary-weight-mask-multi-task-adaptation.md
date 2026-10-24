# Discovery Report: Round 720 — Piggyback Binary Weight-Mask Multi-Task Adaptation

- **Timestamp**: `2026-10-19T13:23:00Z`
- **Selected Concept**: `AIMech:PiggybackBinaryWeightMaskMultiTaskAdaptation` (*Piggyback Binary Weight-Mask Multi-Task Adaptation*)
- **Record Path**: `data/curated/PiggybackBinaryWeightMaskMultiTaskAdaptation.yaml`
- **Primary Source**: Arun Mallya, Dillon Davis, Svetlana Lazebnik — *Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights* (`https://dblp.org/search/publ/api?q=Piggyback+Adapting+a+Single+Network+to+Multiple+Tasks+Mallya&format=xml`).

## Identity & Boundary Resolution

Distinct from PackNet (Mallya & Lazebnik, CVPR 2018, AIMech:PackNetIterativePruningContinualLearning), which prunes and modifies network weights sequentially and degrades as tasks are added, from Edge-Popup (Ramanujan et al., CVPR 2020, AIMech:EdgePopupUntrainedSubnetworkScoreOptimization) and SupSup (AIMech:SupSupSupermasksInSuperposition), which discover fixed-sparsity top-k% subnetworks in randomly initialized networks without task-specific classification heads, and from Residual Adapters (Rebuffi et al., NeurIPS 2017), which insert additional trainable convolutional filter banks.

## Constructed Boundary & Regime Verification

```text
Piggyback verification passed.
```
