# Discovery Report: Round 712 — Projected Attention Layers

- **Timestamp**: `2026-10-19T13:15:00Z`
- **Selected Concept**: `AIMech:PALsProjectedAttentionLayers` (*Projected Attention Layers*)
- **Record Path**: `data/curated/PALsProjectedAttentionLayers.yaml`
- **Primary Source**: Asa Cooper Stickland, Iain Murray — *BERT and PALs: Projected Attention Layers for Efficient Adaptation in Multi-Task Learning* (`https://dblp.org/search/publ/api?q=BERT+and+PALs+Projected+Attention+Layers+for+Efficient+Adaptation&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Asa Cooper Stickland and Iain Murray (ICML 2019, PMLR 97:5986-5995, arXiv:1902.02671) as Projected Attention Layers (PALs). Distinct from Houlsby bottleneck adapters and AdapterFusion (AIMech:AdapterFusion), which insert serial feed-forward down/up-projection modules within each layer; from AdaptFormer (AIMech:AdaptFormer), which places parallel bottleneck MLP branches alongside FFN sublayers in Vision Transformers; and from HyperFormer (AIMech:HyperFormerSharedHypernetworkAdapter), which generates serial adapter weights via a shared task-conditioned hypernetwork.

## Constructed Boundary & Regime Verification

```text
[PASS] PALs boundaries verified: params_pal=1811520 (d_s=204 vs 84), diff_active=0.9593, anneal_ratio=156.8->2.7483
```
