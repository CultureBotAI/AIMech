# Discovery Report: Round 295 — HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA

- **Timestamp**: `2026-10-19T05:42:00Z`
- **Selected Concept**: `AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA` (*HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA*)
- **Record Path**: `data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml`
- **Primary Source**: Anru R. Zhang, T. Tony Cai, Yihong Wu — *Heteroskedastic PCA: Algorithm, Optimality, and Applications* (`https://doi.org/10.1214/21-AOS2074`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 689 maintained AIMech concepts. Distinct from `AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData` (Yan, Chen, & Fan 2024, which develops distributional asymptotic normality and $\chi_r^2$ confidence regions for subspace rows and linear forms by building upon the HeteroPCA estimator) and from `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` (Abbe, Fan, Wang, & Zhong 2020, which analyzes un-imputed symmetric random matrices).

## Constructed Boundary & Regime Verification

```text
{
  "lemma4_sharp_factor_2": {
    "p": 10,
    "empirical_ratio": 1.8,
    "exact_2_minus_2_over_p": 1.8
  },
  "lemma1_contraction": {
    "incoherence_I_U": 1.915976,
    "lhs_D_PU_D_A_norm": 0.418701,
    "rhs_bound_I_r_over_p": 0.603291
  },
  "theorem3_and_theorem1_heteropca": {
    "pure_diag_perturbation_t0_err": 0.111015,
    "pure_diag_perturbation_t8_err": 1.2016e-06,
    "heteroskedastic_sample_err_regular_svd": 0.32001,
    "heteroskedastic_sample_err_diag_deletion": 0.13466,
    "heteroskedastic_sample_err_heteropca_T10": 0.05914
  },
  "all_assertions_passed": true
}
```
