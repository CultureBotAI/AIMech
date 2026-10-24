# Discovery Report: High-Dimensional Covariance Regularization by Hard Thresholding (Round 238)

- **Report ID**: `20261018T224200Z-covariance-regularization-by-thresholding`
- **Created At**: `2026-10-18T22:42:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:HighDimensionalCovarianceRegularizationByHardThresholding` (`data/curated/HighDimensionalCovarianceRegularizationByHardThresholding.yaml`)
- **Verification Script**: `research/discovery/covariance-regularization-by-thresholding-boundaries.py` (SHA-256: `34c20981c3c88cdf2f6af766990f450007ccbdcb2540616f8010ae5059e7289c`)

## Summary of Primary Sources Inspected

1. **Peter J. Bickel and Elizaveta Levina (2008)**, *Covariance regularization by thresholding*, *The Annals of Statistics* 36(6):2577-2604 (`arXiv:0901.3079v1`, `DOI:10.1214/08-AOS600`).
   - Read all 29 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/6cd31e1ce90225cc.pdf`, `566236` bytes, SHA-256 `048f947d5e8f2813ef84c64b863ea0f481788ff9eb835926c4cec5cf74b81506`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3932/content.md`, `5684` bytes, SHA-256 `6f90d241cd1fe0ab7585d521fee65ea25e7bb07de9e15a4523492081ae6c702b`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3867/content.md`, `4228` bytes, SHA-256 `cce2c7b8df8c389dc6671ca7dbecba1edde113d9ea79e9b1e84efa3e757e5e32`).

## Constructed Boundary & Regime Verification

```text
{"all_passed": true, "bias_bound_eq13": 0.58962273, "checks": {"banding_not_permutation_invariant": true, "bias_bound_eq13_holds": true, "eig_upper_bound_holds": true, "eq14_triangle_decomposition_holds": true, "lambda_min_sigma_positive": true, "pd_preservation_eq4_holds": true, "schur_bound_eq2_holds": true, "sec25_exponent_ordering_holds": true, "thm3_oracle_equivalence_ratio_close_to_1": true, "threshold_permutation_invariant": true}, "eig_upper_bound": 2.40712473, "err_11_ts": 0.11, "err_op_ts": 0.09372771, "exp_banding": 0.25, "exp_thresholding": 0.24, "lambda_max_sigma": 1.46440057, "lambda_min_sigma": 0.67086848, "lambda_min_ts": 0.61894882, "lhs_eq14": 0.10202256, "perm_invariance_diff_ts": 0.0, "perm_noninvariance_diff_b1": 0.51944444, "rhs_eq14": 0.12572714, "thm3_oracle_ratio": 1.0201, "threshold_s": 0.06, "weak_lq_c0_q05": 2.40712473}
```

Executed pure-Python verification in research/discovery/covariance-regularization-by-thresholding-boundaries.py (SHA-256 34c20981c3c88cdf2f6af766990f450007ccbdcb2540616f8010ae5059e7289c): verified (1) Schur/Holder bound ||T_s(Sigma) - Sigma||_{(2,2)} = 0.09372771 <= ||T_s(Sigma) - Sigma||_{(1,1)} = 0.11 (Eq. 2), positive-definiteness preservation lambda_min(T_s(Sigma)) = 0.61894882 >= lambda_min(Sigma) - ||T_s(Sigma) - Sigma||_{(2,2)} = 0.57714077 > 0 (Eq. 4), and exact permutation invariance ||T_s(P Sigma P^T) - P T_s(Sigma) P^T||_{(1,1)} = 0.0 vs banding failure ||B_1(P Sigma P^T) - P B_1(Sigma) P^T||_{(1,1)} = 0.51944444 (Sections 2 & 4); and (2) deterministic weak-l_q bias bound ||T_s(Sigma) - Sigma||_{(1,1)} = 0.11 <= s^{1-q} c_0(p) = 0.58962273 (Eq. 13), triangle decomposition ||T_s(Sigma_hat) - T_s(Sigma)||_{(1,1)} = 0.10202256 <= I + II + III = 0.12572714 (Eq. 14), Section 2.5 exponent ordering (1-q)/2 = 0.24 < alpha/(2(alpha+1)) = 0.25, and Theorem 3 sample-splitting quadratic root bound a_n / r_n = 1.0201 (Eqs. 31-38).
