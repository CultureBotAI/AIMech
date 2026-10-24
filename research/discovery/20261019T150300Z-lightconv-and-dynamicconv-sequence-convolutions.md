# Discovery Report: Round 820 — Lightweight and Dynamic Convolutions (LightConv and DynamicConv)

- **Timestamp**: `2026-10-19T15:03:00Z`
- **Selected Concept**: `AIMech:PayLessAttentionWithLightweightAndDynamicConvolutions` (*Lightweight and Dynamic Convolutions (LightConv and DynamicConv)*)
- **Record Path**: `data/curated/PayLessAttentionWithLightweightAndDynamicConvolutions.yaml`
- **Primary Source**: Felix Wu, Angela Fan, Alexei Baevski, Yann N. Dauphin, Michael Auli — *Pay Less Attention with Lightweight and Dynamic Convolutions* (`https://arxiv.org/bibtex/1901.10430`).

## Identity & Boundary Resolution

Distinct from standard 1D or depthwise separable convolutions (Kaiser et al., 2018), which neither tie weights across d/H channel groups nor apply temporal softmax normalization or per-timestep kernel prediction, and distinct from Lite Transformer (AIMech:LiteTransformerWithLongShortRangeAttention), which combines a self-attention global branch and a convolution local branch in parallel rather than replacing self-attention across all encoder and decoder layers.

## Constructed Boundary & Regime Verification

```text
LightConv/DynamicConv verification passed: params=(7340032, 7168, 112), ker_dc_1=[0.24, 0.324, 0.437] != ker_dc_2=[0.454, 0.32, 0.226]
```
