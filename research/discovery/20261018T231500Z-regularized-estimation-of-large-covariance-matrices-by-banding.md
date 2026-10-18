# Discovery Report: Regularized Covariance Estimation by Banding (Round 242)

- **Report ID**: `20261018T231500Z-regularized-estimation-of-large-covariance-matrices-by-banding`
- **Created At**: `2026-10-18T23:15:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:RegularizedCovarianceEstimationByBanding` (`data/curated/RegularizedCovarianceEstimationByBanding.yaml`)
- **Verification Script**: `research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py` (SHA-256: `f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0`)

## Summary of Primary Sources Inspected

1. **Peter J. Bickel and Elizaveta Levina (2008)**, *Regularized estimation of large covariance matrices*, *The Annals of Statistics* 36(1):199-227 (`arXiv:0803.1909v1`, `DOI:10.1214/009053607000000758`).
   - Read all 30 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/6b8eb5f3ab67a1ab.pdf`, `436962` bytes, SHA-256 `2ca5cccd7bbd0845e95ce36c89cb3e9746b32a7335fc06935fd417ecbcb5aba3`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4081/content.md`, `6001` bytes, SHA-256 `bd09cffdd7a97113786cdb1f083d9fdb43515981b978ccfe7df1786feebf9d3e`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4071/content.md`, `4461` bytes, SHA-256 `6dfcedbb21fb25632d304f11a39a5fc222f9e3a7dd7080e82711804635dda3d5`).

## Constructed Boundary & Regime Verification

```text
All Bickel & Levina (2008a) boundary and mechanism assertions passed.
```

Executed pure-Python verification in research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py (SHA-256 f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0): verified (1) in the p > n regime (p=18, n=12) where the sample covariance S is singular, modified Cholesky k-predecessor regression banding (k=2 < n) produces a strictly lower-triangular 2-banded factor A_tilde_2, positive residual variances D_tilde_2, and a symmetric positive-definite 2-banded precision estimator Sigma_tilde_{2,18}^{-1} = (I - A_tilde_2)^T D_tilde_2^{-1} (I - A_tilde_2) whose inverse Sigma_tilde_{2,18} is unbanded and distinct from B_2(S) (Section 2.2, Eqs. 2-4); (2) symmetric operator-norm inequality ||M||_2 <= ||M||_{(1,1)} (Eq. A2), monotone banding bias decay, and operator/l1 norm reductions of B_2(S) and Sigma_tilde_{1,24} relative to unregularized S (Theorems 1 & 3); (3) construction of a positive-definite 4x4 covariance matrix M whose 1-banded version B_1(M) is indefinite (min eigenvalue < -0.2) whereas Schur-product tapering R_sigma(M) = M * R_sigma with triangular and exponential positive-definite tapers preserves strict positive definiteness (Section 3.3, Theorem 2); and (4) random-split resampling risk minimization (Section 5, Eqs. 24-25) recovering the exact oracle bandwidth k_hat = k_0 = 1 on an MA(1) process (Section 6.1, Example 1).
