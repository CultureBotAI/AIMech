# Discovery Report: Round 660 — LongLoRA and Shifted Sparse Attention (S^2-Attn)

- **Timestamp**: `2026-10-19T12:23:00Z`
- **Selected Concept**: `AIMech:LongloraAndShiftedSparseAttention` (*LongLoRA and Shifted Sparse Attention (S^2-Attn)*)
- **Record Path**: `data/curated/LongloraAndShiftedSparseAttention.yaml`
- **Primary Source**: Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, Jiaya Jia — *LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models* (`https://dblp.org/rec/conf/iclr/ChenQTL0HJ24.html`).

## Identity & Boundary Resolution

Distinct from standard LoRA (Hu et al., 2022), which freezes embeddings and normalization layers and uses dense O(N^2) self-attention during training—resulting in both high perplexity on extended context windows even at rank r = 256 and quadratic training memory/time growth. Also distinct from sparse-from-scratch Transformer architectures such as Longformer (Beltagy et al., 2020) and BigBird (Zaheer et al., 2020), which permanently alter the attention architecture, whereas S^2-Attn is used only during fine-tuning and preserves unmodified dense full self-attention at inference time.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 660 LongLoRA / S^2-Attn (Chen et al. 2024): attn_pairs_ratio=256/64=4x, unshifted_cross_group_diff=0.00e+00, s2_cross_group_diff=0.3526
```
