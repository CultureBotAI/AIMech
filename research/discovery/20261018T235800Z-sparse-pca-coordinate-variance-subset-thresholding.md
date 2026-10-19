# Discovery Report: Sparse Principal Components Analysis via Coordinate-Variance Subset Selection and Thresholding (Round 247)

- **Report ID**: `20261018T235800Z-sparse-pca-coordinate-variance-subset-thresholding`
- **Created At**: `2026-10-18T23:58:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding` (`data/curated/SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding.yaml`)
- **Verification Script**: `research/discovery/sparse-pca-coordinate-variance-subset-thresholding-boundaries.py` (SHA-256: `53ed48bc40deaebc2b219eb1ceea9a062bec91ef90cf731f486d448e2e8ac9e4`)

## Summary of Primary Sources Inspected

1. **Iain M. Johnstone and Arthur Yu Lu (2009)**, *On Consistency and Sparsity for Principal Components Analysis in High Dimensions* (*Sparse Principal Components Analysis*), *Journal of the American Statistical Association* 104(486):682-693 (`arXiv:0901.4392v1`, `DOI:10.1198/jasa.2009.0121`).
   - Read all 29 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/f0a7510cd40783eb.pdf`, `514879` bytes, SHA-256 `1d7accf3c72b7fe93635f49f7668176d86e2ecc3976345e8f9a081bbbffe33b4`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4177/content.md`, `6067` bytes, SHA-256 `c75cbca36fa8eda516f87837d8554015add4e99e982e4e6f661a7e93c10a9434`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4178/content.md`, `1702` bytes, SHA-256 `6ec8405176098083edf5d6520b8da79197c16a694e6afba576602503d8ecfe49`).

## Constructed Boundary & Regime Verification

```text
Johnstone & Lu (2009) Sparse PCA verified: dist_spca=0.0662 <= dist_sub=0.0662 < dist_std=0.3432 (|hat_I|=5/180, sigma2_hat=0.9959, b(9)=4.3617, P(FE U FI)=0.0496).
```

Executed pure-Python verification in research/discovery/sparse-pca-coordinate-variance-subset-thresholding-boundaries.py (SHA-256 53ed48bc40deaebc2b219eb1ceea9a062bec91ef90cf731f486d448e2e8ac9e4): verified (1) Appendix A.1 Equation (20) (p. 16) exact rank-2 eigenvalue formula lambda = (tau +- 1)||rho||||u|| and Lemma 1 (p. 16) angular inequality angle(eta, M eta) <= 3 angle(eta, xi) across 25 random trials; (2) Theorem 4 (p. 12) and Appendix A.4 Equation (54) (p. 25) large-deviation exponent b(9) = 4.3617 and total false exclusion/inclusion probability bound P(FE U FI) = 0.0496 < 0.05 at k = 50, p = n = 1000, sqrt(1 + alpha_n) = 1.25; and (3) high-dimensional single-component spiked model (n = 120, p = 180, c = 1.5 > 0) showing classical PCA error sin angle = 0.3432 versus coordinate-variance subset selection (|hat_I| = 5/180, sigma2_hat = 0.9959) + Anderson-variance hard-thresholding Sparse PCA error sin angle = 0.0662.
