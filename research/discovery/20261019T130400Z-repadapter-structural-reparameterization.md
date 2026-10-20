# Discovery Report: Round 701 — RepAdapter (Structurally Re-parameterized Visual Adapter)

- **Timestamp**: `2026-10-19T13:04:00Z`
- **Selected Concept**: `AIMech:RepAdapter` (*RepAdapter (Structurally Re-parameterized Visual Adapter)*)
- **Record Path**: `data/curated/RepAdapter.yaml`
- **Primary Source**: Gen Luo, Minglang Huang, Yiyi Zhou, Xiaoshuai Sun, Guannan Jiang, Zhiyu Wang, Rongrong Ji — *Towards Efficient Visual Adaption via Structural Re-parameterization* (`https://dblp.org/search/publ/api?q=Towards+Efficient+Visual+Adaption+via+Structural+Re-parameterization&format=xml`).

## Identity & Boundary Resolution

Introduced by Gen Luo, Minglang Huang, Yiyi Zhou, Xiaoshuai Sun, Guannan Jiang, Zhiyu Wang, and Rongrong Ji (2023, arXiv:2302.08106). Distinct from parallel non-linear visual adapters such as AdaptFormer (Chen et al., NeurIPS 2022; AIMech Round 696) and post-FFN non-linear sequential adapters (Houlsby et al., ICML 2019; AIMech Round 677), which cannot be merged into Transformer blocks due to intervening non-linearities, and distinct from SSF (Lian et al., NeurIPS 2022; AIMech Round 692), which applies element-wise affine modulation rather than a dense-to-sparse bottleneck projection. Both full RepAdapter (placed before both MHA and FFN) and the lightweight RepAdapter_attn variant (placed only before MHA) are covered within this single record.

## Constructed Boundary & Regime Verification

```text
[PASS] RepAdapter boundary verification passed: k2_weight_saving=25.0%, max_ada_err=8.88e-16, max_rep_err=6.66e-16, delta_P_infer=0, delta_FLOPs_infer=0
```
