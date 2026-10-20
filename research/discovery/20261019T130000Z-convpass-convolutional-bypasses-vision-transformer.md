# Discovery Report: Round 697 — Convpass

- **Timestamp**: `2026-10-19T13:00:00Z`
- **Selected Concept**: `AIMech:ConvPass` (*Convpass*)
- **Record Path**: `data/curated/ConvPass.yaml`
- **Primary Source**: Shibo Jie, Zhi-Hong Deng — *Convolutional Bypasses Are Better Vision Transformer Adapters* (`https://dblp.org/search/publ/api?q=Convolutional+Bypasses+Better+Vision+Transformer+Adapters+Jie&format=xml`).

## Identity & Boundary Resolution

Distinct from language-oriented channel-wise MLP adapters such as Bottleneck Adapters (AIMech:BottleneckAdapter) and AdaptFormer (AIMech:AdaptFormer), whose 1x1 linear projections cannot mix information across spatial neighbors without relying on the frozen MHSA block, and from LoRA (AIMech:LowRankAdaptation) and VPT (AIMech:VisualPromptTuning), which lack 2D neighborhood inductive bias.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 697 Convpass (Jie & Deng, 2022): total_params(L=12,d=768,h=8)=327552, 1x1_spatial_diff=0.00e+00, 3x3_contiguous=0.7995 > 3x3_scattered=0.4842
```
