# Discovery Report: Round 696 — AdaptFormer

- **Timestamp**: `2026-10-19T12:59:00Z`
- **Selected Concept**: `AIMech:AdaptFormer` (*AdaptFormer*)
- **Record Path**: `data/curated/AdaptFormer.yaml`
- **Primary Source**: Shoufa Chen, Chongjian Ge, Zhan Tong, Jiangliu Wang, Yibing Song, Jue Wang, Ping Luo — *AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition* (`https://dblp.org/search/publ/api?q=AdaptFormer+Adapting+Vision+Transformers+Chen&format=xml`).

## Identity & Boundary Resolution

Distinct from sequential bottleneck adapters (AIMech:BottleneckAdapter; Houlsby et al., 2019), which insert adapters sequentially after MHSA and/or MLP sub-layers, and from Visual Prompt Tuning (AIMech:VisualPromptTuning), which prepends learnable tokens into the attention sequence (and suffers optimization instability when token counts scale up on video tasks or under hierarchical shifted-window attention in Swin Transformers). Also distinct from SSF (AIMech:SSFScaleAndShiftFeatures), which applies channel-wise linear scale/shift modulation rather than a parallel nonlinear ReLU bottleneck.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 696 AdaptFormer (Chen et al., NeurIPS 2022): init_diff=0.0e+00, layer_params=99136 (1.38% of ViT-B), err_parallel=0.00e+00 << err_sequential=0.0738
```
