# Discovery Report: Round 708 — HyperGrid (Grid-wise Decomposable Hyper Projections for Multi-Task Transformers)

- **Timestamp**: `2026-10-19T13:11:00Z`
- **Selected Concept**: `AIMech:HyperGridDecomposableGridwiseHyperProjection` (*HyperGrid (Grid-wise Decomposable Hyper Projections for Multi-Task Transformers)*)
- **Record Path**: `data/curated/HyperGridDecomposableGridwiseHyperProjection.yaml`
- **Primary Source**: Yi Tay, Zhe Zhao, Dara Bahri, Donald Metzler, Da-Cheng Juan — *HyperGrid: Efficient Multi-Task Transformers with Grid-wise Decomposable Hyper Projections* (`https://dblp.org/search/publ/api?q=HyperGrid+Transformers+Towards+A+Single+Model&format=xml`).

## Identity & Boundary Resolution

Introduced by Yi Tay, Zhe Zhao, Dara Bahri, Donald Metzler, and Da-Cheng Juan (ICLR 2021, arXiv:2007.05891). Distinct from post-FFN adapter hypernetworks such as HyperFormer (Karimi Mahabadi et al., ACL 2021; AIMech Round 703) and self-attention prompt hypernetworks such as HyperPrompt (He et al., ICML 2022; AIMech Round 706), as well as post-ReLU Output Gating (Section 7.3, Eq. 7): HyperGrid gates the pre-existing second FFN weight matrix W_i in R^{d_m x d_f} in 2D grid regions with negligible parameter overhead (d_m d_r + d_c in the LG variant). All four HyperGrid composition variants (L, L^2, LG, and GL) are covered within this single record.

## Constructed Boundary & Regime Verification

```text
[PASS] HyperGrid boundaries verified: cost_lg=24704 < cost_gl=393248 < cost_l2=417792, max_res_err=1.11e-16, gating_diff=0.1346
```
