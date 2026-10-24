# Discovery Report: Round 209 (`AIMech:ForestStructuredDKWPostHocConfidenceBounds`)

- **Report ID**: `20261017T170500Z-forest-structured-dkw-post-hoc-confidence-bounds`
- **Created At**: `2026-10-17T17:05:00Z`
- **Corpus State**: `442` AIO records, `603 -> 604` curated records
- **Stopping Status**: `CONTINUE_DISCOVERY`

## 1. Candidate Curated in Round 209

### `AIMech:ForestStructuredDKWPostHocConfidenceBounds` — Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds
- **Concept Kind**: `mathematical_method`
- **Record Path**: `data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml` (SHA-256 `9bae8e3738defe08500250ea05b7669885f8434e0ac0413058d9c332be8fa29f`)
- **Primary Sources Inspected in Full Text**:
  1. Guillermo Durand, Gilles Blanchard, Pierre Neuvial, & Etienne Roquain (2020), *Post hoc false positive control for structured hypotheses* (arXiv title: *Post hoc false positive control for spatially structured hypotheses*), *Scandinavian Journal of Statistics* 47(4):1114–1148 (`arXiv:1807.01470v2` full-text 24-page PDF, SHA-256 `c8e024a9c369dc010ef3f7af754267fc07dad921a2525ab3ed717e3cee077e9b`, `713481` bytes; `DOI:10.1111/sjos.12453`).
  2. Crossref bibliographic record (`https://api.crossref.org/works/10.1111/sjos.12453`, SHA-256 `ab88eb06001fb7ea657c92970f067c9b65236a97503b85893e8df9de5a9b37e5`).
  3. arXiv abstract record (`https://arxiv.org/abs/1807.01470`, SHA-256 `7bcfe7da684a82ac7adbd6b06f3d36b582472ea7714bc0486cb14b1456f1f0a5`).

## 2. Constructed Boundary & Numerical Verification

Executed `python3 research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py` (SHA-256 `33e506cbe878afedd9ef5e25ea394b6b744fe7bb06f6cc10f516135b5c1cf852`):
- **Section 2.3 & Section 3 Forest Interpolation & Algorithm 1**:
  - **Example 2.2 non-forest gap (p. 4)**: $V^*_{\mathfrak{R}}(S) = 1 < \widetilde{V}_{\mathfrak{R}}(S) = 2 = \overline{V}_{\mathfrak{R}}(S) = 2$.
  - **Example 3.2/3.4 & Theorem 3.6 / Algorithm 1 (pp. 5–8, 22–24)**: Node depths `[1, 2, 2, 2, 3, 3, 3, 1, 2]`, `8` atomic partition blocks via Algorithm 2, $d = 5$, and $\mathrm{Algorithm\_1}(\mathfrak{R}, S) = \widetilde{V}_{\mathfrak{R}}(S) = \widetilde{V}^d_{\mathfrak{R}}(S) = 13 < \overline{V}_{\mathfrak{R}}(S) = 15$, plus exact equality $V^*_{\mathfrak{R}}(S) = \mathrm{Algorithm\_1}(\mathfrak{R}, S) = \widetilde{V}^d_{\mathfrak{R}}(S)$ across all `256` subsets of an 8-element forest.
- **Section 4.1 Local DKW-Massart Calibration & Remark 4.3 / Lemma A.1**:
  - $\zeta_k(X) \le \zeta^{GW}_k(X)$ verified across all `3000` region-trials (strict improvement on `965` region-trials), empirical JER `0.025` (tree) and `0.035` (partition) $\le \alpha = 0.05$.
- **Section 4.2 Figure 6 & Section 5.3 Hybrid Bound**:
  - Equation (23) Figure 6 ratio upper bounds: $\mu = 2.0$: `0.492103`, $\mu = 4.0$: `0.798229`.
  - Hybrid bound $V^{0.02}_{\mathrm{hybrid}}(0.05, S_k)$: at $k = 10$, $V_{\mathrm{Simes}} = 0 < V_{\mathrm{tree}} = 10 \implies V_{\mathrm{hybrid}} = 0$; at $k = 200$, $V_{\mathrm{tree}} = 71 < V_{\mathrm{Simes}} = 145 \implies V_{\mathrm{hybrid}} = 71$.
