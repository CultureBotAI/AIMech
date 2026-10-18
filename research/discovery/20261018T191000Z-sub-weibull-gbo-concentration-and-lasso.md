# Discovery Report: Generalized Bernstein-Orlicz Sub-Weibull Concentration and High-Dimensional Misspecified Lasso (Round 218)

- **Report ID**: `20261018T191000Z-sub-weibull-gbo-concentration-and-lasso`
- **Created At**: `2026-10-18T19:10:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso` (`data/curated/GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso.yaml`)
- **Verification Script**: `research/discovery/sub-weibull-gbo-concentration-and-lasso-boundaries.py` (SHA-256: `c47082e9200ab482fa76ded57c303d80fe0b1eb277f7f925d7220043ca693748`)

## Summary of Primary Sources Inspected

1. **Kuchibhotla & Chakrabortty (2022)**, *Moving beyond sub-Gaussianity in high-dimensional statistics: applications in covariance estimation and linear regression*, *Information and Inference: A Journal of the IMA* 11(4):1389–1456, `arXiv:1804.02605v4`, `DOI:10.1093/imaiai/iaac012`.
   - Read all 68 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/5440c541c7835991.pdf`, `954720` bytes, SHA-256 `47098d42e994743cae6a78627a85697478dc18350dc6bc4c9ed3bb1656d14ecc`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3266/content.md`, `7457` bytes, SHA-256 `d410c2530d014a0403653172250e8c8cdbda20f88475ff562f7988e8c015bb62`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3272/content.md`, `7157` bytes, SHA-256 `74ef9f5d18ec5ac0051d26e2fbb84bcf43a33b24391a7cce5441787fa6f790db`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso",
  "regime_1_gbo_and_product_orlicz_norms": {
    "min_phi_over_psi_ratio": 1.357017,
    "max_phi_over_psi_ratio": 2.0,
    "min_inv_ratio": 1.051306,
    "max_inv_ratio": 2.0,
    "product_holder_ratio": 0.913063,
    "proposition_a1_and_d2_verified": true
  },
  "regime_2_joint_vs_marginal_and_maximal_inequality": {
    "q_dim": 64,
    "joint_to_marginal_collinear_ratio": 8.0,
    "expected_sqrt_q": 8.0,
    "gbo_second_order_rate": 1.105241,
    "cck_second_order_rate": 13.794337,
    "joint_vs_marginal_and_remark_3_2_verified": true
  },
  "regime_3_rsc_and_re_sample_complexity_optimization": {
    "k_sparsity": 40,
    "optimal_free_s": 3,
    "penalty_at_s_opt": 0.257321,
    "penalty_at_s_1": 0.297524,
    "penalty_at_s_k": 0.579424,
    "re_free_s_optimization_verified": true
  },
  "regime_4_misspecified_lasso_oracle_inequality": {
    "grad_inf_at_beta0": 0.162479,
    "lambda_n": 0.357454,
    "nu_sc_l1": 0.07,
    "cone_rhs_3_nu_s_plus_4_beta0_sc": 2.991519,
    "lasso_l2_error": 0.548536,
    "equation_e10_cone_and_oracle_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/sub-weibull-gbo-concentration-and-lasso-boundaries.py (SHA-256 c47082e9200ab482fa76ded57c303d80fe0b1eb277f7f925d7220043ca693748): verified (1) Proposition A.1 closed-form Orlicz equivalence ||X||_{Psi_{alpha,L}} <= ||X||_{phi_{alpha,L}} <= 2||X||_{Psi_{alpha,L}} and Proposition D.2 Holder-type product Orlicz inequality; (2) Definitions 2.4-2.5 and Equation 4.1 sqrt(q) divergence of joint vs. marginal sub-Weibull norms under collinearity and Remark 3.2 strict improvement of Theorem 3.4 over Chernozhukov et al. (2017, Lemma E.1); (3) Theorem 4.4 unified Restricted Strong Convexity (RSC) and Section 4.3.1 free-s optimization min_{1<=s<=p}{Xi_{n,s} + k Xi_{n,s}/s} for Restricted Eigenvalue RE(k) sample complexity; and (4) Proposition E.1 deterministic hard-sparsity-free approximate cone condition and l2 oracle bound for misspecified Lasso.
