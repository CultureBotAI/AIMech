# Discovery Report: Marcenko-Pastur Convex Optimization Spectrum Estimation for Large Covariance Matrices (Round 246)

- **Report ID**: `20261018T235200Z-marcenko-pastur-convex-spectrum-estimation`
- **Created At**: `2026-10-18T23:52:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:MarcenkoPasturConvexOptimizationSpectrumEstimation` (`data/curated/MarcenkoPasturConvexOptimizationSpectrumEstimation.yaml`)
- **Verification Script**: `research/discovery/marcenko-pastur-convex-spectrum-estimation-boundaries.py` (SHA-256: `aeb8b0c6c5e9339bc0d40651ff9cc365afab1541b215b3ffd791695edb98fbd9`)

## Summary of Primary Sources Inspected

1. **Noureddine El Karoui (2008)**, *Spectrum estimation for large dimensional covariance matrices using random matrix theory*, *The Annals of Statistics* 36(6):2757-2790 (`arXiv:math/0609418v1`, `DOI:10.1214/07-AOS581`).
   - Read all 25 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/7bc118941f415f85.pdf`, `444397` bytes, SHA-256 `7f1d03deb521d11bfbe54e4425bbcb33d6a2e9b5da19db07e50ce93a008b419b`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4162/content.md`, `6527` bytes, SHA-256 `3373e1f309222a549e7b4bc7056efd5c3283428e2787a8f158f7a092aaed4c9e`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4153/content.md`, `4657` bytes, SHA-256 `9522a6ae66a9a577a9ff804dee6a753a7f3f22f03564892be515406c07999d4f`).

## Constructed Boundary & Regime Verification

```text
El Karoui (2008) Marcenko-Pastur convex spectrum estimation verified: W1_hat=0.2261 < W1_emp=0.4010, Levy_hat=0.1500 < Levy_emp=0.2500, Lemma 1 err=1.24e-16.
```

Executed pure-Python verification in research/discovery/marcenko-pastur-convex-spectrum-estimation-boundaries.py (SHA-256 aeb8b0c6c5e9339bc0d40651ff9cc365afab1541b215b3ffd791695edb98fbd9): verified (1) the exact closed-form roof/tent basis Stieltjes integral formula of Lemma 1 (Section 2.2, p. 7) against 400-node midpoint numerical quadrature in C^+ with maximum error 1.24e-16; (2) the Section 3.1 (Figure 1, p. 13) two-atom population spectrum H = 0.5 delta_{1.0} + 0.5 delta_{2.0} at n = 200, p = 60 (c = 0.3), where the empirical sample eigenvalues spread across [0.415, 3.736] with Wasserstein-1 error 0.4010 and Kolmogorov/Levy CDF error 0.2500; and (3) the Section 2.2 Marcenko-Pastur Stieltjes-transform convex optimization estimator on a complex grid {z_j} in C^+, reducing Wasserstein-1 distance to 0.2261 (< 0.4010), Kolmogorov/Levy distance to 0.1500 (< 0.2500), and concentrating 0.8758 of the estimated spectral mass directly on the true atoms {1.0, 2.0} while accurately preserving the first moment (1.4648 vs sample trace 1.4832).
