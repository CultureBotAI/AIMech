# Discovery Report: Round 279 — L-Infinity Eigenvector Perturbation Bound and Robust Factor Covariance Estimation

- **Timestamp**: `2026-10-19T05:10:00Z`
- **Selected Concept**: `AIMech:LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation` (*L-Infinity Eigenvector Perturbation Bound and Robust Factor Covariance Estimation*)
- **Record Path**: `data/curated/LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation.yaml`
- **Primary Source**: Jianqing Fan, Weichen Wang, and Yiqiao Zhong (2018), *An $\ell_\infty$ Eigenvector Perturbation Bound and Its Application to Robust Covariance Estimation*, *Journal of Machine Learning Research* 18(207):1–42 (`arXiv:1603.03516v2`, `https://jmlr.org/papers/v18/16-140.html`).

## Identity & Boundary Resolution

`AIMech:LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation` was checked against all 442 pinned AIO concepts and 673 maintained AIMech concepts:

1. **`AIMech:PrincipalOrthogonalComplementThresholdingForApproximateFactorCovarianceEstimation`**: Sample-covariance POET under sub-Gaussian tails vs. deterministic $\ell_\infty$ singular-vector perturbation theory ($O(\|\mathbf{E}\|_\infty / (\gamma_0\sqrt{d}))$) and heavy-tailed Catoni M-estimator and spatial Kendall's tau factor covariance estimation.
2. **`AIMech:AdaptiveThresholdingForHighDimensionalSparseCovarianceMatrixEstimation`**: Direct sparse covariance thresholding vs. low-rank incoherent eigenvector $\ell_\infty$ perturbation and robust factor covariance decomposition.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation",
  "primary_source": "Fan, Wang, & Zhong (2018), JMLR 18(207):1-42 (arXiv:1603.03516v2)",
  "checks": {
    "l_infinity_vs_davis_kahan_delocalization": {
      "d": 36,
      "r": 2,
      "coherence_mu_V": 1.990501,
      "matrix_E_norm_inf": 1.225,
      "v1_err_inf": 0.003861,
      "v1_err_l2": 0.010988,
      "v1_sqrt_d_inf_over_l2": 2.10821,
      "v2_err_inf": 0.005497,
      "v2_err_l2": 0.014962,
      "localized_err_inf_over_l2": 0.999754
    },
    "neumann_series_and_schur_complement": {
      "d": 20,
      "lam": 15.0,
      "lam_tilde": 15.01546909,
      "secular_equation_abs_err": 3.552713678800501e-15,
      "x_star_norm_inf": 0.00373224,
      "neumann_expansion_err_inf": 4.119968255444917e-17
    },
    "robust_factor_covariance_catoni_and_kendall": {
      "n": 140,
      "d": 18,
      "max_entrywise_err_sample": 0.579143,
      "max_entrywise_err_catoni": 0.500981,
      "trace_spatial_kendall": 1.0,
      "v1_inf_err_sample": 0.053541,
      "v1_inf_err_catoni": 0.051998,
      "v1_inf_err_kendall": 0.050827
    }
  },
  "all_passed": true
}
```

Verified in pure Python across three constructed experiments: (1) on an incoherent rank-2 symmetric matrix A in R^{36 x 36} (coherence mu(V) = 1.9905, ||E||_inf = 1.225), the entrywise eigenvector perturbations ||u_tilde_1 - v_1||_inf = 0.003861 and ||u_tilde_2 - v_2||_inf = 0.005497 satisfy sqrt(d) ||u_tilde_1 - v_1||_inf / ||u_tilde_1 - v_1||_2 = 2.1082 (confirming the 1/sqrt(d) delocalization gain over Davis-Kahan), whereas a coherent rank-1 matrix (mu = d) yields ||u_loc - e_1||_inf / ||u_loc - e_1||_2 = 0.9998 (no delocalization gain); (2) in Lemma 5.1 & 5.2's Schur complement decomposition (d = 20), the secular equation lam_tilde = lam + u^T E u + u^T E x^* holds to 3.55e-15 and the 14-term Neumann series matches x^* in l_infinity norm to 4.12e-17; and (3) under heavy-tailed idiosyncratic shocks (n = 140, d = 18, r = 2), both the entrywise Catoni M-estimator (max entrywise error 0.5010 vs. sample 0.5791, v_1 l_inf error 0.0520 vs. sample 0.0535) and the unit-trace spatial Kendall's tau matrix (v_1 l_inf error 0.0508) outperform sample PCA.
