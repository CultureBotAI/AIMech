# Discovery Report: Diagonal Thresholding and Semidefinite Relaxation Support Recovery for Sparse Principal Components (Round 248)

- **Report ID**: `20261019T002000Z-diagonal-thresholding-sdp-sparse-pca`
- **Created At**: `2026-10-19T00:20:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA` (`data/curated/DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA.yaml`)
- **Verification Script**: `research/discovery/diagonal-thresholding-sdp-sparse-pca-boundaries.py` (SHA-256: `1006ab7a2d0940b60c87433e0bea828d9b6d7f21ae8281fee3971798ecaee77e`)

## Summary of Primary Sources Inspected

1. **Arash A. Amini and Martin J. Wainwright (2009)**, *High-dimensional analysis of semidefinite relaxations for sparse principal components*, *The Annals of Statistics* 37(5B):2877-2921 (`arXiv:0803.4026v2`, `DOI:10.1214/08-AOS664`).
   - Read all 47 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/824024536e9063eb.pdf`, `564851` bytes, SHA-256 `b70136a9cc288520d894e3fc57ef16b04470ba0b2ce3c569c7e560c86e5a3c4a`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4213/content.md`, `6881` bytes, SHA-256 `41a370f2e4140f1739cc8dd41f7579ce0298167f7648a9dedda68d072e7c1980`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4214/content.md`, `4802` bytes, SHA-256 `bcfde02e00f232f6da53cded8bd89170e9a851cedd7b79fe8769c228df30075a`).

## Constructed Boundary & Regime Verification

```text
Amini & Wainwright (2009) SDP & Diagonal Thresholding Sparse PCA verified: Lemma 14 err=2.22e-15, ||hat_z_S - z_S^*||_inf=0.1580 <= 0.2041, max|hat_U_ScS|=0.8961 <= 1, max_x subopt_gap=-3.2872 <= 0 (theta_sdp=5.39, theta_dia=0.90).
```

Executed pure-Python verification in research/discovery/diagonal-thresholding-sdp-sparse-pca-boundaries.py (SHA-256 1006ab7a2d0940b60c87433e0bea828d9b6d7f21ae8281fee3971798ecaee77e): verified (1) Lemma 14 (Section 5, p. 31) and Appendix F Equation (84) (p. 44) exact eigenvalue spectrum and log-determinant formula for the Fano mixture covariance Sigma_M against Cholesky log-determinant computation on the explicitly averaged mixture matrix (error 2.22e-15), plus the mutual information bound I(U; X^n)/n <= beta^2 / (2(1 + beta) k); (2) the three-step primal-dual witness construction (Lemmas 5, 6, 7, and 8, pp. 16-20) on a k-sparse spiked model (p = 36, k = 6, beta = 3.0, rho_n = beta/(2k) = 0.25, n = 110, theta_sdp = 5.39, theta_dia = 0.90), confirming Lemma 6 l_infty error ||hat_z_S - z_S^*||_infty = 0.1580 <= 1/(2 sqrt(k)) = 0.2041 and exact signed support recovery sign(hat_z_S) = sign(z_S^*), Lemma 7 dual block feasibility max|hat_U_{S^c S}| = 0.8961 <= 1 and exact eigenvector annihilation (Delta_{S^c S} - rho_n hat_U_{S^c S}) hat_z_S = 0, and Lemma 5 global SDP optimality across 50 random unit vectors x in S^{p-1} (max suboptimality gap -3.2872 <= 0).
