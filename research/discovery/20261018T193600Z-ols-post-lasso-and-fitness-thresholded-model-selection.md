# Discovery Report: OLS Post-Lasso and Fitness-Thresholded Post-Model Selection Estimation (Round 221)

- **Report ID**: `20261018T193600Z-ols-post-lasso-and-fitness-thresholded-model-selection`
- **Created At**: `2026-10-18T19:36:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:OLSPostLassoAndFitnessThresholdedPostModelSelectionEstimation` (`data/curated/OLSPostLassoAndFitnessThresholdedPostModelSelectionEstimation.yaml`)
- **Verification Script**: `research/discovery/ols-post-lasso-and-fitness-thresholded-model-selection-boundaries.py` (SHA-256: `651b59c8490847a2ad3741043e73389ef4bc0b5b4b4dc9fe0564df6ff2d40fcd`)

## Summary of Primary Sources Inspected

1. **Alexandre Belloni & Victor Chernozhukov (2013)**, *Least squares after model selection in high-dimensional sparse models*, *Bernoulli* 19(2):521-547, `arXiv:1001.0188v5`, `DOI:10.3150/11-BEJ410`.
   - Read all 27 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/78919ef208e97f11.pdf`, `392949` bytes, SHA-256 `3b8ed91d939c20efa9687f9b19920916bea42140615c0560210189bbd7ba1bc5`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3372/content.md`, `7632` bytes, SHA-256 `08b82138c5355b576d24d246d847536b2e0acbaf1f1f71260ad20737b5d734bd`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3373/content.md`, `3891` bytes, SHA-256 `06847f0cbd5e7336f6500836ca980f09699345040de808efa62af02b3a614b19`).

## Constructed Boundary & Regime Verification

```text
{
  "oracle_and_step2_orthogonality_check": {
    "s_oracle": 2,
    "T_supp": [
      0,
      1
    ],
    "c_s": 0.01336,
    "max_corr_on_T": 0.0,
    "max_corr_on_Tc": 0.009916,
    "step2_bound_min_sigma_sqrtn_cs": 0.01336,
    "oracle_step2_ok": true
  },
  "lasso_kkt_lower_bound_and_sublinearity_check": {
    "T_hat_size": 3,
    "m_hat": 1,
    "f_hat_err": 0.073724,
    "kkt_lower_bound": 0.005844,
    "phi_1_2_3_4": [
      2.29953,
      2.886821,
      3.451351,
      4.031139
    ],
    "kkt_lower_ok": true,
    "sublinearity_ok": true
  },
  "ols_post_lasso_and_eq_a7_check": {
    "C_n": 0.0,
    "B_n": 0.000567,
    "eq_a7_rhs": 0.014156,
    "q_tilde_minus_q_0": -0.003661,
    "f_hat_err": 0.073724,
    "f_tilde_0_err": 0.055965,
    "post_lasso_ok": true
  },
  "ols_post_fit_lasso_and_thm7_gamma_t_check": {
    "m_hat": 1,
    "m_tilde_fit": 0,
    "T_fit": [
      0,
      1
    ],
    "gamma_fit": -0.002114,
    "binary_search_steps": 2,
    "max_allowed_steps": 3,
    "avg_err_lasso": 0.069753,
    "avg_err_post_lasso": 0.066228,
    "avg_err_post_fit": 0.059505,
    "gamma_t_actual": 0.007479,
    "gamma_t_bound": 0.007479,
    "fit_lasso_ok": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/ols-post-lasso-and-fitness-thresholded-model-selection-boundaries.py (SHA-256 651b59c8490847a2ad3741043e73389ef4bc0b5b4b4dc9fe0564df6ff2d40fcd): verified (1) Section 2.1 oracle risk minimization program and Proof of Theorem 2 Step 2 residual orthogonality and correlation bounds; (2) Remark 3.1 / Equation (A.1) Lasso KKT prediction-error lower bound and Lemma 3 restricted sparse eigenvalue sublinearity; (3) Theorems 4-5 post-selection fit relation Q_hat(beta_tilde) - Q_hat(beta_0) <= B_n ^ C_n and Equation (A.7) Lasso optimality bound; and (4) Equations (2.9) and (2.14) fitness-thresholded Lasso binary search, exact oracle support recovery, Monte Carlo empirical risk ordering, and Theorem 7 thresholding loss bound gamma_t <= t sqrt(phi(m_t) m_t).
