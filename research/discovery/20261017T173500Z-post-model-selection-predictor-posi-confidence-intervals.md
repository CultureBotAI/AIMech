# Discovery Report: Round 212 (`AIMech:PostModelSelectionPredictorPoSIConfidenceIntervals`)

- **Report ID**: `20261017T173500Z-post-model-selection-predictor-posi-confidence-intervals`
- **Created At**: `2026-10-17T17:35:00Z`
- **Corpus State**: `442` AIO records, `606 -> 607` curated records
- **Stopping Status**: `CONTINUE_DISCOVERY`

## 1. Candidate Curated in Round 212

### `AIMech:PostModelSelectionPredictorPoSIConfidenceIntervals` — Post-model-selection predictor PoSI confidence intervals under full and active-only covariate observation
- **Concept Kind**: `mathematical_method`
- **Record Path**: `data/curated/PostModelSelectionPredictorPoSIConfidenceIntervals.yaml` (SHA-256 `69249cfe00828610a5f294e4d091b12b54c6c77ac55a139f699d4d59aa625b9a`)
- **Primary Sources Inspected in Full Text**:
  1. François Bachoc, Hannes Leeb, & Benedikt M. Pötscher (2019), *Valid confidence intervals for post-model-selection predictors*, *The Annals of Statistics* 47(3):1475–1504 (`arXiv:1412.4605v3` full-text 56-page PDF, SHA-256 `222cfb10a74f331210a1ce0494e00543f6f8f9ef14bff5205baf1766acc6cca9`, `789744` bytes; `DOI:10.1214/18-AOS1721`).
  2. Crossref bibliographic record (`https://api.crossref.org/works/10.1214/18-AOS1721`, SHA-256 `1b41a05db014e113754d1a60138002d6192d6e9af2b7382200d747b9ade3a9d3`).
  3. arXiv abstract record (`https://arxiv.org/abs/1412.4605`, SHA-256 `5df943653a28d09308512eb466568443defe347842b04442e140f41b3f788304`).

## 2. Constructed Boundary & Numerical Verification

Executed `python3 research/discovery/post-model-selection-predictor-posi-confidence-intervals-boundaries.py` (SHA-256 `3a620af56bf4cbde531923b1fd429db6bbb2130328d38333dda4a6874322bf04`):
- **Regime 1 (Lemma B.4 Exact Union-Bound Geometry on $S^1$)**:
  - Verified pairwise inner products $\langle \bar{s}_{\{1\}}, \bar{s}_{\{2\}} \rangle = -0.5$ and $\langle \bar{s}_{\{1\}}, \bar{s}_{\{1,2\}} \rangle = 0.5$, disjoint spherical caps for $c = 0.90 \ge \sqrt{3}/2$, full circle coverage for $c = 0.85 \le \sqrt{3}/2$, and $F^*_{M, x_0}(0.90) = 0.13860224$ across all $M \in 2^{\{1,2\}}$.
- **Regime 2 (Hierarchy & Anti-Monotonicity for $d = p = 3, r = \infty$)**:
  - Verified $K_{\mathrm{naive}} = 1.959964 < K_1(x_0) = 2.529043 < K_3(x_0[\{1,2\}], \{1,2\}) = 2.600879 < K_3(x_0[\{1\}], \{1\}) = 2.60497 = K_4 = 2.60497 < K_5 = 2.795483$.
- **Regime 3 (Orthogonal-Design $\sqrt{p}$ Scaling vs. Sparse $x_0$ and $K_4/\sqrt{p} \to \sqrt{3}/2$)**:
  - Verified $\xi = 0.636328$ at $b^* = 0.612$ vs. $K_1(e_1, \infty) = 1.959964$, and $K_4(\infty)/\sqrt{p} = 0.866426 \to \sqrt{3}/2 = 0.866025$.
- **Regime 4 (Random-Design Out-of-Sample Target $\beta_M^{(*)}$ vs. In-Sample Target $\beta_M^{(n)}$)**:
  - Verified on correlated Gaussian design ($\rho = 0.6, \beta_{\{1\}}^{(*)} = 1.6$) that fixed-design scale $\sigma$ covers $\beta_{\{1\}}^{(n)}$ at `0.9507` but under-covers $\beta_{\{1\}}^{(*)}$ at `0.6993`, whereas $\hat{\sigma}_{\hat{M}}$ achieves `0.9627`.
