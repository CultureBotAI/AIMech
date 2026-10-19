# Discovery Report: Round 286 — Asymmetric Low-Rank Matrix Eigenvalue and Linear-Form Eigenvector Perturbation Analysis

- **Timestamp**: `2026-10-19T05:24:00Z`
- **Selected Concept**: `AIMech:AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis` (*Asymmetric Low-Rank Matrix Eigenvalue and Linear-Form Eigenvector Perturbation Analysis*)
- **Record Path**: `data/curated/AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis.yaml`
- **Primary Source**: Yuxin Chen, Chen Cheng, Jianqing Fan — *Asymmetry Helps: Eigenvalue and Eigenvector Analyses of Asymmetrically Perturbed Low-Rank Matrices* (`https://doi.org/10.1214/20-AOS1963`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 680 maintained AIMech concepts. Distinct from `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` (Abbe, Fan, Wang, & Zhong 2020, which analyzes *symmetric* random matrices $H_{ij} = H_{ji}$ via leave-one-out decoupling where the leading eigenvalue suffers $O(n\sigma^2/\lambda^\star)$ upward bias, whereas Chen, Cheng, & Fan 2021 exploit *asymmetry* $H_{ij} \perp H_{ji}$ via combinatorial Neumann-series walk partitions to eliminate the $O(n\sigma^2/\lambda^\star)$ eigenvalue bias without knowing heteroscedastic noise variances) and from `AIMech:LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation` (Fan, Wang, & Zhong 2018, which is deterministic in $\|\mathbf{H}\|_\infty$ for symmetric matrices).

## Constructed Boundary & Regime Verification

```text
{
  "n": 64,
  "lambda_star": 1.0,
  "sigma_base": 0.045,
  "neumann_series_identity_max_err": 6.686262654653774e-12,
  "mean_u_star_H2_u_star_asymmetric": 0.003799,
  "mean_u_star_H2_u_star_symmetric": 0.134921,
  "mean_asym_eigenvalue_err": 0.036197,
  "mean_sym_eigenvalue_err": 0.137407,
  "mean_vanilla_svd_err": 0.136917,
  "mean_entrywise_eigenvector_linf_err": 0.125859,
  "asymmetrized_dilation_singular_value_err": 0.023881,
  "averaged_svd_singular_value_err": 0.03945
}
```
