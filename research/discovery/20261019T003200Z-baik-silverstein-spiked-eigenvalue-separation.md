# Discovery Report: Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices (Round 249)

- **Report ID**: `20261019T003200Z-baik-silverstein-spiked-eigenvalue-separation`
- **Created At**: `2026-10-19T00:32:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation` (`data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml`)
- **Verification Script**: `research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py` (SHA-256: `1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8`)

## Summary of Primary Sources Inspected

1. **Jinho Baik and Jack W. Silverstein (2006)**, *Eigenvalues of large sample covariance matrices of spiked population models*, *Journal of Multivariate Analysis* 97(6):1382-1408 (`arXiv:math/0408165v1`, `DOI:10.1016/j.jmva.2005.08.003`).
   - Read all 24 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/2487da691b740c6d.pdf`, `293564` bytes, SHA-256 `1eb7d0eb27408acdc9178873a9c47c6a446ffe341f69477ea51c0474d9e2c960`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4232/content.md`, `5366` bytes, SHA-256 `6a6cc776bed2cf882834344652cb4c4be7724b309380488a6e93e90d3d0f08d7`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4233/content.md`, `3288` bytes, SHA-256 `090b2257aed03868d9a574fc0040e5ac7b5c00f8b48603b2409f72de2c5af628`).

## Constructed Boundary & Regime Verification

```text
Baik & Silverstein (2006) spiked covariance eigenvalue separation verified: c=0.5 (s_1=4.154~4.200, s_2=2.693~2.914, s_{p-1}=0.1107~0.0858, s_p=0.0369~0.0365); c=2.0 (s_1=7.166~7.071, s_2=5.123~5.828, s_n=0.2193~0.1716).
```

Executed pure-Python verification in research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py (SHA-256 1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8): verified (1) Theorems 1.1-1.2 critical points and bulk-edge continuity of psi(alpha) = alpha + c alpha / (alpha - 1) at alpha = 1 +- sqrt(c); (2) exact algebraic equivalence between the direct derivative of the Silverstein-Choi companion inverse Stieltjes transform z_p(m) (eq. 3.2) and the rational factorization [f(m) + (1/n) g(m)] / D(m) (eqs. 3.3-3.5), plus the Lemma 3.4 sign condition G_j(-1/alpha_j) = k_j (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p] > 0 iff |alpha_j - 1| > sqrt(c_p) and O(1/n) midpoint cancellation of z_p(m_{j,+/-}^{(n)}); and (3) Monte Carlo non-Gaussian Rademacher sample covariance simulations confirming Theorem 1.1 for c = 0.5 (supercritical upper outlier s_1 = 4.154 ~ 4.200, subcritical collapse s_2 = 2.693 ~ 2.914, lower bulk edge s_{p-1} = 0.1107 ~ 0.0858, supercritical lower outlier s_p = 0.0369 ~ 0.0365) and Theorem 1.2 for c = 2.0 (supercritical upper outlier s_1 = 7.166 ~ 7.071, bulk edge s_2 = 5.123 ~ 5.828, and absorption of small spike alpha_p = 0.05 < 1 with smallest nonzero eigenvalue s_n = 0.2193 ~ (1 - sqrt(2))^2 = 0.1716).
