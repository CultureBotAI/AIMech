# Discovery Report: Round 266 — Self-Normalized Heteroscedastic LASSO Optimal Instrumental Variables and Weak-Identification Sup-Score Inference

- **Timestamp**: `2026-10-19T04:00:00Z`
- **Selected Concept**: `AIMech:SelfNormalizedHeteroscedasticLassoOptimalInstrumentalVariablesAndWeakIdentificationSupScoreInference` (*Self-Normalized Heteroscedastic LASSO Optimal Instrumental Variables and Weak-Identification Sup-Score Inference*)
- **Record Path**: `data/curated/SelfNormalizedHeteroscedasticLassoOptimalInstrumentalVariablesAndWeakIdentificationSupScoreInference.yaml`
- **Primary Source**: Alexandre Belloni, Daniel Chen, Victor Chernozhukov, and Christian Hansen (2012), *Sparse Models and Methods for Optimal Instruments With an Application to Eminent Domain*, *Econometrica* 80(6):2369–2429 (`DOI:10.3982/ECTA9626`, `arXiv:1010.4345v5`).

## Identity & Boundary Resolution

`AIMech:SelfNormalizedHeteroscedasticLassoOptimalInstrumentalVariablesAndWeakIdentificationSupScoreInference` was checked against all 442 pinned AIO concepts and 660 maintained AIMech concepts:

1. **`AIMech:DoubleDebiasedMachineLearningAndNeymanOrthogonalCrossFitting`**: Cross-fitted Neyman-orthogonal scores for black-box ML nuisance learners, whereas Belloni et al. (2012) introduce iterative self-normalized heteroscedastic penalty loadings $\widehat{\gamma}_j = \sqrt{\mathbb{E}_n[f_{ij}^2 \widehat{\zeta}_i^2]}$, Post-LASSO optimal instrument construction, and weak-identification Sup-Score / Inverse LASSO duality.
2. **`AIMech:SquareRootLassoPivotalConicSparseRegression`**: Homoscedastic conic root-MSE scale elimination rather than predictor-specific heteroscedastic self-normalized moderate-deviation loadings.

## Constructed Boundary & Regime Verification

```text
{
  "score_dominated_by_lambda": true,
  "l_load": 0.92957305,
  "u_load": 1.07279695,
  "refinement_improves_loadings": true,
  "lemma8_kkt_identity_err": 0.0,
  "pred_err_PL": 0.13945612,
  "pred_err_L": 0.64558289,
  "pred_err_2sls": 0.75008384,
  "post_lasso_reduces_pred_err": true,
  "post_lasso_beats_naive_2sls_first_stage": true,
  "lemma6_bound_holds": true,
  "iv_err_post_lasso": 0.09455679,
  "t_stat_alpha0": 1.18987948,
  "true_alpha0_in_sup_score_ci": true,
  "true_alpha0_inverse_lasso_zero": true,
  "false_alpha_excluded_from_ci": true,
  "false_alpha_inverse_lasso_nonzero": true,
  "inverse_lasso_equivalence_mismatches": 0
}
```

Verified in pure Python on a heteroscedastic IV model (n=80, p=100, s=3): (1) under heteroscedastic first-stage errors zeta_i with Var(zeta_i | z_i) = (0.35 * (1 + 0.8 * z_{i1}^2))^2, the self-normalized score max_j |sqrt(n) E_n[f_{ij} zeta_i]| / sqrt(E_n[f_{ij}^2 zeta_i^2]) = 2.91208222 is dominated by Phi^{-1}(1 - gamma/(2p)) = 3.48075641 (Lemma 5), and Algorithm A.1's iterative refinement tightens loading validity bounds from [0.9255008, 1.38023007] to [0.92957305, 1.07279695] (Lemma 12); (2) Lemma 8's Post-LASSO KKT orthogonality identity holds to 0.0, and Post-LASSO reduces first-stage prediction error ||D_hat - D||_{2,n} 4.63x relative to LASSO (0.13945612 vs 0.64558289) and 5.38x relative to full p=100 2SLS (0.75008384), recovering the exact support [0, 1, 2] while obeying Lemma 6's restricted cone bound; (3) in the second stage with endogeneity rho=0.65, full 2SLS suffers severe many-instrument bias (|alpha_2SLS - alpha_0| = 0.37124851) whereas Post-LASSO IV achieves |alpha_PL - alpha_0| = 0.09455679 with valid studentized t-statistic 1.18987948 <= 1.96 (Theorem 2); and (4) the weak-identification-robust Sup-Score test and Inverse LASSO (Eqs. 3.17-3.19) agree on 81/81 grid points (0 mismatches), retaining true alpha_0 = 1.5 (S_hat(1.5) = 3.24962259 <= Lambda = 3.82883205, ||beta_IL(1.5)||_1 = 0.0) and rejecting false alpha = 0.2 (S_hat(0.2) = 7.45646529 > Lambda, ||beta_IL(0.2)||_1 = 0.77936919 > 0).
