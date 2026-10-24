# Discovery Report: Model-Robust Nonlinearity-Consistent Sandwich Variance and Ratio of Asymptotic Variances (RAV) Specification Test (Round 214)

- **Report ID**: `20261017T175500Z-model-robust-nonlinearity-sandwich-and-rav-test`
- **Created At**: `2026-10-17T17:55:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest` (`data/curated/ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml`)
- **Verification Script**: `research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py` (SHA-256: `3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49`)

## Summary of Primary Sources Inspected

1. **Buja, Berk, Brown, George, Pitkin, Traskin, Zhao, & Zhang (2019)**, *Models as Approximations I: Consequences Illustrated with Linear Regression*, *Statistical Science*, 34(4):523–544 (`DOI:10.1214/18-STS693`, `arXiv:1404.1578v4`).
   - Read all 43 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/dc997ddb5fa16119.pdf`, `849867` bytes, SHA-256 `11d501663ce1861ce2fd446b367d12360456fe6a1f4d0b8ffef1a49b5674a61d`), Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3124/content.md`, `6236` bytes, SHA-256 `72ef24d405646eeaed1810f783df3afe2bc62ac2fc2d50b082bd873c165ea715`), and arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3123/content.md`, `6643` bytes, SHA-256 `38a840a331cdab71ed15d55946e521ee7bbbdd73a77a5d06f9b6b6aa248e55ca`).

## Constructed Boundary & Regime Verification

```json
{
  "concept_id": "AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest",
  "regime_1_ancillarity_and_decomposition": {
    "nonlinear_slope_p1": 0.0,
    "nonlinear_slope_p2": 2.0,
    "linear_slope_p1": 2.0,
    "linear_slope_p2": 2.0,
    "max_orthogonality_error": 0.0,
    "expected_m2": 0.525,
    "proposition_4_1_verified": true
  },
  "regime_2_estimation_offsets_and_bootstrap_limit": {
    "var_noise_eo": 0.003204,
    "var_approx_eo": 0.013707,
    "var_total_eo": 0.015723,
    "cov_noise_approx_eo": -0.000547,
    "av_sandwich_b1": 1.029159,
    "m_of_n_bootstrap_scaled_var_b1": 1.100014,
    "bootstrap_sandwich_rel_error": 0.068848,
    "offsets_and_bootstrap_limit_verified": true
  },
  "regime_3_adjusted_slopes_and_rav_bounds": {
    "beta1_matrix": 1.768122,
    "beta1_casewise": 1.768122,
    "beta1_pairwise": 1.768122,
    "rav_protective_sigma2": 0.357143,
    "rav_antiprotective_eta2": 2.028571,
    "rav_combined_m2": 1.348668,
    "rav_lower_bound": 0.142857,
    "rav_upper_bound": 2.285714,
    "slopes_and_rav_bounds_verified": true
  },
  "regime_4_rav_specification_test": {
    "gaussian_null_asymptotic_variance": 8.0,
    "gaussian_null_asymptotic_sd": 2.828427,
    "rav_hat_1_misspecified": 3.319706,
    "rav_hat_2_well_behaved": 0.804898,
    "perm_pval_1": 0.0025,
    "perm_pval_2": 0.3775,
    "rav_specification_test_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py (SHA-256 3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49): (1) Regime 1 (Proposition 4.1 & canonical decomposition): verified nonlinear slope shift from 0.0 under P_{X,1} to 2.0 under P_{X,2} vs. linear invariance 2.0 = 2.0, and exact orthogonality error 0.0. (2) Regime 2 (Estimation Offsets & Proposition 8.2 bootstrap limit): verified Var(Noise EO) = 0.003204, Var(Approx EO) = 0.013707, Var(Total EO) = 0.015723, Cov(Noise, Approx) = -0.000547, and M-of-N bootstrap scaled variance 1.100014 matching plug-in sandwich 1.029159 (rel error 0.068848). (3) Regime 3 (Section 10 weighted slopes & Section 11 RAV bounds): verified exact equality of matrix (1.768122), case-wise (1.768122), and pairwise (1.768122) OLS slopes, and Lemma E.2 convex combination RAV[m^2] = 1.348668 from protective RAV[sigma^2] = 0.357143 < 1 and anti-protective RAV[eta^2] = 2.028571 > 1 within sharp bounds [0.142857, 2.285714]. (4) Regime 4 (Section 12 RAV_hat_j test): verified Proposition 12.2 Gaussian null variance = 8.0 (SD = 2.828427) and permutation test detection of nonlinear X_1 (RAV_hat_1 = 3.319706, p = 0.0025) while linear X_2 is unrejected (RAV_hat_2 = 0.804898, p = 0.3775).
