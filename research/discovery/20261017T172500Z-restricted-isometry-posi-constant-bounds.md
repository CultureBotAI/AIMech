# Discovery Report: Round 211 (`AIMech:RestrictedIsometryPostSelectionInferenceConstantBounds`)

- **Report ID**: `20261017T172500Z-restricted-isometry-posi-constant-bounds`
- **Created At**: `2026-10-17T17:25:00Z`
- **Corpus State**: `442` AIO records, `605 -> 606` curated records
- **Stopping Status**: `CONTINUE_DISCOVERY`

## 1. Candidate Curated in Round 211

### `AIMech:RestrictedIsometryPostSelectionInferenceConstantBounds` — Restricted isometry post-selection inference (PoSI) constant upper and lower bounds
- **Concept Kind**: `mathematical_method`
- **Record Path**: `data/curated/RestrictedIsometryPostSelectionInferenceConstantBounds.yaml` (SHA-256 `317e5e5fb341d3f207d90f7a9571f612a4f6115ce5c057a6ade1055f931f4b73`)
- **Primary Sources Inspected in Full Text**:
  1. François Bachoc, Gilles Blanchard, & Pierre Neuvial (2018), *On the post selection inference constant under restricted isometry properties*, *Electronic Journal of Statistics* 12(2):3736–3757 (`arXiv:1804.07566v2` full-text 22-page PDF, SHA-256 `c703312f4db92644aeb50fa0fc55b377de0386920bba1cbdba0a6eadc8a4a090`, `308563` bytes; `DOI:10.1214/18-EJS1490`).
  2. Crossref bibliographic record (`https://api.crossref.org/works/10.1214/18-EJS1490`, SHA-256 `6983055f26d21f1f9622d49c0447357c975da594f66f2e86a37dd6d39405b643`).
  3. arXiv abstract record (`https://arxiv.org/abs/1804.07566`, SHA-256 `86886d722b4e8751c11c4339717c9531702523ab11382800bd860a1a874d1b7e`).

## 2. Constructed Boundary & Numerical Verification

Executed `python3 research/discovery/restricted-isometry-posi-constant-bounds-boundaries.py` (SHA-256 `ddb5c03dffeb5b06b49c0032e04629ef49e8c42c7f3913e388dfdeb8c41ac5fb`):
- **Section 2 Invariance & Gaussian Concentration**:
  - Verified Lemma 2.2 scale invariance ($\max \|w_X - w_Z\|_\infty = 1e-15$), Lemma 2.4 sparse cardinality bound, and Lemma A.3 finite-$r$ quantile bound.
- **Section 3 Theorem 3.3 & Figure 2 Bounds ($p = 1000, s = 15, \delta = 0.03, \alpha = 0.05$)**:
  - Verified $U_{\mathrm{orth}} = 3.898949 < U_{\mathrm{RIP}} = 4.740587 < \tilde{U}_{\mathrm{RIP}} = 5.430915 < \overline{U}_{\mathrm{RIP}} = 7.45679 \ll U_{\mathrm{sparse}} = 13.406862$.
- **Section 4 Block-Equicorrelated Lower Bound ($p = 10, k = 9, s = 4, c = 0.25$)**:
  - Verified Lemma 4.1 exact RIP constant $\delta(Z^{(c, k)}, s) = 0.4330127019 = c\sqrt{s - 1}$, Equation (18) inverse identity error `0.0`, and $\|w_{M, p} - z_{M, p}\| = 0.4440995 \le 2\delta c(\delta) = 1.82844677$.
