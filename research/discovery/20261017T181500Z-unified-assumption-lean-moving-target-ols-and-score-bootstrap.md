# Discovery Report: Unified Assumption-Lean Moving-Target Linear Regression and Score Bootstrap (Round 216)

- **Report ID**: `20261017T181500Z-unified-assumption-lean-moving-target-ols-and-score-bootstrap`
- **Created At**: `2026-10-17T18:15:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap` (`data/curated/UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap.yaml`)
- **Verification Script**: `research/discovery/unified-assumption-lean-moving-target-ols-and-score-bootstrap-boundaries.py` (SHA-256: `ebff2f845dfa5d8cbc6d84cea6b4ee420ca04277692e7f6cb26274a43790dbda`)

## Summary of Primary Sources Inspected

1. **Kuchibhotla, Brown, & Buja (2018)**, *Model-free Study of Ordinary Least Squares Linear Regression*, `arXiv:1809.10538v1`.
   - Read all 33 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/e38ff11b0d11a1d7.pdf`, `335845` bytes, SHA-256 `0306f48fd372e41aecc1a2dd5a8735353b37ebb2e2ffa973a41a2a0650169383`) and arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3200/content.md`, `5668` bytes, SHA-256 `22614725f856e133d72edfa940df5c36a0d6d0aea1635d97e9db8ce1224ff6d8`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap",
  "regime_1_moving_target_and_score_gap": {
    "average_normal_equation_norm": 0.0,
    "max_individual_score_mean_norm": 4.709895,
    "k_star_minus_k_min_eig": 0.956444,
    "k_star_minus_k_max_eig": 2.05296,
    "true_to_conservative_var_ratio_slope": 0.248294,
    "moving_target_gap_verified": true
  },
  "regime_2_conservative_sandwich_and_anderson_lemma": {
    "mean_k_check_to_k_star_op_diff": 0.420623,
    "empirical_95_coverage_inid": 1.0,
    "conservative_coverage_verified": true
  },
  "regime_3_score_bootstraps_vs_pairs_singularity": {
    "estimated_score_sum_norm": 0.0,
    "pairs_bootstrap_singular_rate": 0.0367,
    "score_bootstrap_singular_rate": 0.0,
    "multiplier_score_bootstrap_cov_rel_err": 0.026098,
    "resampling_score_bootstrap_cov_rel_err": 0.03709,
    "score_bootstraps_verified": true
  },
  "regime_4_deterministic_master_inequality": {
    "realizations_checked": 300,
    "lambda_min_sigma_n": 1.0,
    "min_ratio_eq30": 0.91338,
    "max_ratio_eq30": 1.045037,
    "max_lhs_over_rhs_eq31": 0.499148,
    "theorem_8_1_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/unified-assumption-lean-moving-target-ols-and-score-bootstrap-boundaries.py (SHA-256 ebff2f845dfa5d8cbc6d84cea6b4ee420ca04277692e7f6cb26274a43790dbda): verified (1) Definition 2.1 moving-target average normal equation 1/n sum_{i=1}^n E[X_i(Y_i - X_i^T beta_n)] = 0 vs. non-zero individual score expectations E[X_i(Y_i - X_i^T beta_n)] != 0 and strict Loewner-order gap K_n^* - K_n > 0 under i.n.i.d. nonlinearity; (2) Section 6.1 & Lemma 6.2 asymptotically conservative coverage (100% >= 95%) of Eicker-Huber-White sandwich confidence intervals via Anderson's Lemma; (3) Sections 6.2-6.4 multiplier and m-of-n resampling score bootstraps eliminating pairs-bootstrap Gram matrix singularities (0.0% vs. 3.67%) while matching K_check_n within 2.6%-3.7% relative operator error; and (4) Theorem 8.1 deterministic master inequalities (Equations 30-31) across all 300 realizations satisfying D_{2n}^Sigma <= Lambda_n / 2.
