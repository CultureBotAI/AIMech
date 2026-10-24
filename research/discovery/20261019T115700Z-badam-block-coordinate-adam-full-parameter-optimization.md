# Discovery Report: Round 634 — BAdam (Block Coordinate Descent with Adam's Update Rule)

- **Timestamp**: `2026-10-19T11:57:00Z`
- **Selected Concept**: `AIMech:BAdamBlockCoordinateAdamFullParameterOptimization` (*BAdam (Block Coordinate Descent with Adam's Update Rule)*)
- **Record Path**: `data/curated/BAdamBlockCoordinateAdamFullParameterOptimization.yaml`
- **Primary Source**: Qijun Luo, Hengxu Yu, Xiao Li — *BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models* (`https://dblp.org/rec/conf/nips/LuoYL24`).

## Identity & Boundary Resolution

Distinct from parameter-efficient fine-tuning methods such as LoRA (AIMech:LowRankAdaptation, Hu et al. 2021), which restrict weight updates to low-rank adapter subspaces rather than learning full-rank perturbations across all model parameters. Distinct from LOMO (AIMech:LOMOLowMemoryOptimization, Lv et al. 2023), which performs stateless on-the-fly FP16 SGD updates during backpropagation without Adam moments or gradient accumulation, and from GaLore (AIMech:GaLoreGradientLowRankProjection, Zhao et al. 2024), which projects gradients of all layers into SVD subspaces simultaneously rather than performing block coordinate Adam updates with per-block state clearing.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 634 BAdam verified: mem=20.0GB_vs_144.0GB, ubp=52800_vs_102400 (ratio=0.5156), eff_rank=36, descent=-6.5824e-03<=-9.3161e-05
```
