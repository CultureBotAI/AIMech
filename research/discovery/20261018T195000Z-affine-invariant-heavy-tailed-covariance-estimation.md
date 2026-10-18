# Discovery Report: Affine-Invariant Calibrated Covariance Estimation and Heavy-Tailed Ridge Regression (Round 223)

- **Report ID**: `20261018T195000Z-affine-invariant-heavy-tailed-covariance-estimation`
- **Created At**: `2026-10-18T19:50:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression` (`data/curated/AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml`)
- **Verification Script**: `research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py` (SHA-256: `03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416`)

## Summary of Primary Sources Inspected

1. **Dmitrii M. Ostrovskii & Alessandro Rudi (2019)**, *Affine Invariant Covariance Estimation for Heavy-Tailed Distributions*, *Proceedings of the 32nd Conference on Learning Theory (COLT)*, PMLR 99:2531-2550, `arXiv:1902.03086v2`.
   - Read all 20 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/67414044f88161dc.pdf`, `386511` bytes, SHA-256 `65feb9f97b0b40a86339c6a59207072dcfa5debb4a0ab3ce41446a5600fa0e46`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3459/content.md`, `6567` bytes, SHA-256 `6a55c4b48442cddb485274a6cdba50c3bbe5a5dc029164f6b14a90cb50036f4f`), and PMLR metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3440/content.md`, `5205` bytes, SHA-256 `b1a61c2001fe6e95b4d36f18a3ba793f6ed1a457fdb5a3cd09c2e5f73cab2c57`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression",
  "all_passed": true,
  "check_1_lemmas_14_and_6": {
    "passed": true,
    "max_df_halving_ratio": 1.487357,
    "similarity_eigenvalue_range": [
      0.675676,
      1.923077
    ],
    "theoretical_similarity_bounds": [
      0.666667,
      2.0
    ],
    "max_trace_surrogate_diff_ratio": 0.475552
  },
  "check_2_algorithm1_and_lepskii": {
    "passed": true,
    "calibrated_error_alg1": 0.1238,
    "calibrated_error_wei_minsker_uncalibrated": 1.299639,
    "max_relative_diagonal_error_alg1": 0.092035,
    "lepskii_selected_theta": 4.0,
    "calibrated_error_lepskii": 0.157731
  },
  "check_3_theorem13_ridge_decomposition": {
    "passed": true,
    "E3_fixed_design_bias": 0.454459,
    "Eq47_bias_upper_bound": 0.753434,
    "E2_covariance_estimation_term": 0.444905,
    "Eq48_upper_bound": 0.467981
  }
}
```

Executed pure-Python verification in research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py (SHA-256 03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416): verified (1) Lemma 14 dyadic effective-dimension doubling df_{lambda/2}(S) <= 2 df_lambda(S) (max ratio 1.4874 <= 2.0) and Lemma 6 similarity eigenvalue bounds [0.6757, 1.9231] subset [2/3, 2] and trace surrogate control (ratio 0.4756 <= 3.0); (2) Algorithm 1 multi-stage dyadic regularization halving vs. uncalibrated Wei-Minsker clipping on a heavy-tailed Student-t_5 covariance with spectrum {100, 10, 0.1, 0.01} at lambda = 0.01 (calibrated error 0.1238 vs. 1.2996, and Lepskii Algorithm 2 adaptive selection error 0.1577); and (3) Theorem 13 / Appendix D ridge regression excess-risk decomposition.
