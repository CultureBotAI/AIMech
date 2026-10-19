# Discovery Report: Operator-Norm Consistent Estimation of Beta-Sparse Covariance Matrices (Round 245)

- **Report ID**: `20261018T234500Z-beta-sparse-covariance-hard-thresholding`
- **Created At**: `2026-10-18T23:45:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:OperatorNormConsistentEstimationOfBetaSparseCovarianceMatrices` (`data/curated/OperatorNormConsistentEstimationOfBetaSparseCovarianceMatrices.yaml`)
- **Verification Script**: `research/discovery/beta-sparse-covariance-hard-thresholding-boundaries.py` (SHA-256: `a539821edc349632fd60e9151e097616aa831b8f67552b0a37276c5c4784c54e`)

## Summary of Primary Sources Inspected

1. **Noureddine El Karoui (2008)**, *Operator norm consistent estimation of large-dimensional sparse covariance matrices*, *The Annals of Statistics* 36(6):2717-2756 (`arXiv:0901.3220v1`, `DOI:10.1214/07-AOS559`).
   - Read all 42 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/9dbdb9e1642b4923.pdf`, `470262` bytes, SHA-256 `c8948201a88c0d9f85b7f8f601aef86e53bcaf436cadcfabe6d0721000aa4fee`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4134/content.md`, `6083` bytes, SHA-256 `ac79f9d1147845d5f32a8ff8b527289441c0d42590676fa31d3cc2a9c1854c53`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4135/content.md`, `3543` bytes, SHA-256 `ad8569a5d5fa21ebef71167490a65f80c19bd8d1d991b4468c9c41219a69b339`).

## Constructed Boundary & Regime Verification

```text
El Karoui (2008) beta-sparsity verified: E1_spec=1.9747 vs E2_spec=1.4422; permuted 0-sparse err_thresh=0.5849 < err_sample=1.3424; 1/2-sparse oracle sq_err=0.2466 (theory=0.2514).
```

Executed pure-Python verification in research/discovery/beta-sparse-covariance-hard-thresholding-boundaries.py (SHA-256 a539821edc349632fd60e9151e097616aa831b8f67552b0a37276c5c4784c54e): verified (1) the Section 2 motivating example (pp. 2720-2722) showing that the arrowhead matrix E_1 (beta = 1/2) and tridiagonal matrix E_2 (beta = 0) share the exact same number of nonzero entries (3p - 2) and entry values (1/sqrt(p)) yet have distinct spectral norms (1.9747 vs 1.4422 at p = 20) and closed-walk counts phi_p(4) = trace(A_p^4) (970 vs 358); (2) permutation invariance of trace(A_p^k) (Section 2.2), non-closure of beta-sparsity under multiplication (Fact 2, E_1^2 has p^2 = 400 nonzeros), and Hadamard modulus operator-norm monotonicity |||M||| <= ||| |M|_Had ||| (Lemma A.2); (3) Theorem 2 & Section 3.2 operator-norm reduction on a randomly permuted 0-sparse Toeplitz covariance matrix (hard thresholding spectral error 0.5849 vs sample covariance error 1.3424); and (4) the Section 3.3 sharp phase transition at beta = 1/2, confirming that even the oracle support estimator on the 1/2-sparse arrowhead matrix has squared operator-norm error 0.2466 matching the theoretical limit (p - 1 + sum_{i>=2} alpha_i^2)/(n - 1) = 0.2514 > 0.
