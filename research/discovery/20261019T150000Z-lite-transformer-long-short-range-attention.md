# Discovery Report: Round 817 — Lite Transformer with Long-Short Range Attention (LSRA)

- **Timestamp**: `2026-10-19T15:00:00Z`
- **Selected Concept**: `AIMech:LiteTransformerWithLongShortRangeAttention` (*Lite Transformer with Long-Short Range Attention (LSRA)*)
- **Record Path**: `data/curated/LiteTransformerWithLongShortRangeAttention.yaml`
- **Primary Source**: Zhanghao Wu, Zhijian Liu, Ji Lin, Yujun Lin, Song Han — *Lite Transformer with Long-Short Range Attention* (`https://arxiv.org/bibtex/2004.11886`).

## Identity & Boundary Resolution

Distinct from Evolved Transformer (So et al., 2019), which stacks convolution and self-attention layers sequentially rather than in parallel channel-split branches and retains the 1:4 FFN bottleneck, distinct from LightConv (Wu et al., 2019), which replaces self-attention entirely with lightweight convolutions and lacks a global attention branch, and distinct from MobileBERT (AIMech:MobileBERTCompactTaskAgnosticBERTWithBottlenecks), which narrows intra-block channels via linear bottlenecks rather than flattening the FFN and splitting channels across parallel attention and convolution extractors.

## Constructed Boundary & Regime Verification

```text
Lite Transformer LSRA verification passed: ffn_base=62914560 > attn_base=31918080, attn_flat=31918080 > ffn_flat=15728640, lsra_total=14081280 < 0.5*attn_flat=15959040
```
