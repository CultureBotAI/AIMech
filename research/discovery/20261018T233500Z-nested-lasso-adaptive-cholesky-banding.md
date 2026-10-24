# Discovery Report: Nested Lasso Adaptive Banding for Covariance Estimation (Round 244)

- **Report ID**: `20261018T233500Z-nested-lasso-adaptive-cholesky-banding`
- **Created At**: `2026-10-18T23:35:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:NestedLassoAdaptiveBandingForCovarianceEstimation` (`data/curated/NestedLassoAdaptiveBandingForCovarianceEstimation.yaml`)
- **Verification Script**: `research/discovery/nested-lasso-adaptive-cholesky-banding-boundaries.py` (SHA-256: `b593f041305dd466652a8dcf8f21573ceb6a140a3ef16d94868a20bd5f0f4164`)

## Summary of Primary Sources Inspected

1. **Elizaveta Levina, Adam Rothman, and Ji Zhu (2008)**, *Sparse estimation of large covariance matrices via a nested Lasso penalty*, *The Annals of Applied Statistics* 2(1):245-263 (`arXiv:0803.3872v1`, `DOI:10.1214/07-AOAS139`).
   - Read all 21 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/d66271eef9473101.pdf`, `383599` bytes, SHA-256 `91f75cf387d48b0ab26891848fc68a84b6a3a69f3a448b991b33bae13ba30c83`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4121/content.md`, `5812` bytes, SHA-256 `ad16fbce344df6fd5e9a7bd442ab8ffd11b4f468988c2313463503f3317fea68`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4123/content.md`, `4403` bytes, SHA-256 `c66060e857a679ae17d54102a292e050630c9743ee623652933277cba7032fc2`).

## Constructed Boundary & Regime Verification

```text
Nested Lasso adaptive banding verified: KL_nested=0.2664 < KL_band1=0.4977 and KL_sample=0.5541; exact Cholesky decomposition err=2.22e-16.
```

Executed pure-Python verification in research/discovery/nested-lasso-adaptive-cholesky-banding-boundaries.py (SHA-256 b593f041305dd466652a8dcf8f21573ceb6a140a3ef16d94868a20bd5f0f4164): verified (1) the exact modified Cholesky factorization Sigma^{-1} = T^T D^{-1} T and Sigma = T^{-1} D (T^{-1})^T (Eq. 3, max error 2.22e-16) and exact equality between the full matrix Gaussian negative log-likelihood (Eq. 4) and the sum of separable row regression objectives (Eq. 5); (2) the structural fill-in boundary showing that irregular non-contiguous zeros in T (unstructured Cholesky Lasso, Figure 1b) produce fill-in in Sigma^{-1} = T^T D^{-1} T whereas nested Lasso adaptive banding (Figure 1c) preserves exact structural zeros outside the adaptive band envelope; and (3) the alternating residual-variance and local quadratic approximation (LQA) ridge solver for the J_2 nested Lasso penalty (Section 2.2, Eq. 13) on a variable-bandwidth autoregression (Model Sigma_3), confirming that every row satisfies the nested zero-propagation invariant and achieves lower Kullback-Leibler concentration loss (KL = 0.2664) than fixed k=1 banding (KL = 0.4977) and sample precision inversion (KL = 0.5541).
