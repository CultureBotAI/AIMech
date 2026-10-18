# Discovery Report: Reference-Family Joint Error Rate Post Hoc Confidence Bounds (`AIMech:ReferenceFamilyJERPostHocConfidenceBounds`)

- **Report ID**: `20261017T165500Z-reference-family-jer-post-hoc-confidence-bounds`
- **Created at**: `2026-10-17T16:55:00Z`
- **Skill**: `aimech-add-record`
- **Scope**: Reference-Family Joint Error Rate Post Hoc Confidence Bounds (Blanchard, Neuvial, & Roquain 2020, *The Annals of Statistics* 48(3):1281–1303, `arXiv:1703.02307v3` / `v2`, `DOI:10.1214/19-AOS1847`).

## 1. Summary of Curated Concept

- **ID**: [`AIMech:ReferenceFamilyJERPostHocConfidenceBounds`](../../data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml)
- **Name**: Reference-family joint error rate post hoc confidence bounds
- **Concept kind**: `mathematical_method`
- **Review status**: `DRAFT`
- **Primary sources**:
  - Gilles Blanchard, Pierre Neuvial, & Etienne Roquain (2020), *Post hoc confidence bounds on false positives using reference families* (*Post hoc inference via joint family-wise error rate control*), *The Annals of Statistics* 48(3):1281–1303 (`arXiv:1703.02307v3`, 29 pages, `739014` bytes, SHA-256 `7711fc4b689e9da4ca76ffdbfeccb130e36699388750c5462eea515c217e76fd`; `arXiv:1703.02307v2`, 34 pages including Appendices A–D, `834710` bytes, SHA-256 `a14025460c2029ca6a87db880df41694deedf2b0bd094484556af0bfed8c47fe`; Crossref `DOI:10.1214/19-AOS1847`, `4473` bytes, SHA-256 `2420271bd9a536d5a923b1a51b43ae3c50cda9466779861d2471559cc1293aac`; arXiv abstract `6156` bytes, SHA-256 `91c73d6251c4e1fe1adbf725bb47621e3bc55c372e4ef49b3d4494d1de0bab65`).

## 2. Constructed Boundary & Numerical Verification

Executed `python3 research/discovery/reference-family-jer-post-hoc-confidence-bounds-boundaries.py` (SHA-256 `ec2e60196e1983f307f7b7d68813a31deb5c5d1b1a3dcbcdd5def3b95ddabf74`):
- **Section 2 & Section 8 Structural Properties**:
  - **Triangle-graph NP-hardness gap (Proposition 2.3 in v3 / Proposition 2.2 in v2)**: $V^*_{\mathfrak{R}}(\{1, 2, 3\}) = 1 < \overline{V}_{\mathfrak{R}}(\{1, 2, 3\}) = 2$.
  - **Self-consistency idempotence (Proposition 2.4 in v3 / Proposition 2.3 in v2)**: $\overline{V}_{\widetilde{\mathfrak{R}}}(R) = \overline{V}_{\mathfrak{R}}(R)$ verified across all `32` subsets.
  - **Nested optimality (Proposition 2.5 in v3 / Proposition 2.4 in v2) & Goeman–Solari (2011) Simes shortcut equivalence (Lemmas 8.1–8.2 in v2)**: $\overline{V}_{\mathfrak{R}}(R) = V^*_{\mathfrak{R}}(R)$ and $\overline{V}_{\mathfrak{R}}(R) = \overline{V}^{GS}_\alpha(R)$ verified across all `64` subsets.
- **Section 4.3 Table 2 Exact Simes Beta Tail Probabilities ($m = 1000, \alpha = 0.05$)**:
  - $k=1$: `0.048772`, $k=2$: `0.0046748`, $k=5$: `6.5525e-06`, $k=10$: `1.6415e-10`, $k=100$: `5.7919e-93`.
- **Sections 5–6 Single-Step and Step-Down $\lambda$-Calibration**:
  - Known Gaussian equicorrelation ($\rho = 0.5, \alpha = 0.2$): $\lambda^L(\alpha, \mathbb{N}_m) = 0.361178 < \lambda^L(\alpha, \mathcal{H}_0) = 0.495548$, empirical JER: Simes `0.085` $<$ single-step `0.135` $\le$ step-down `0.1817` $\le \alpha$.
  - Unknown dependence via sign-flipping ($B = 99, \alpha = 0.2$, Theorem 5.8): single-step JER `0.0333`, step-down JER `0.1667` $\le \alpha$.
