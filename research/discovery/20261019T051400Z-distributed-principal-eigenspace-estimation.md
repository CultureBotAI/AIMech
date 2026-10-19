# Discovery Report: Round 281 — Distributed Principal Eigenspace Estimation by Subspace Projection Averaging

- **Timestamp**: `2026-10-19T05:14:00Z`
- **Selected Concept**: `AIMech:DistributedPrincipalEigenspaceEstimationBySubspaceProjectionAveraging` (*Distributed Principal Eigenspace Estimation by Subspace Projection Averaging*)
- **Record Path**: `data/curated/DistributedPrincipalEigenspaceEstimationBySubspaceProjectionAveraging.yaml`
- **Primary Source**: Jianqing Fan, Dong Wang, Kaizheng Wang, and Ziwei Zhu (2019), *Distributed Estimation of Principal Eigenspaces*, *The Annals of Statistics* 47(6):3009–3031 (`DOI:10.1214/18-AOS1713`, `arXiv:1702.06488v4`).

## Identity & Boundary Resolution

`AIMech:DistributedPrincipalEigenspaceEstimationBySubspaceProjectionAveraging` was checked against all 442 pinned AIO concepts and 675 maintained AIMech concepts:

1. **`AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices`**: Single-matrix entrywise $\ell_\infty$ leave-one-out analysis vs. distributed one-shot subspace projection averaging $\widetilde{\boldsymbol{\Sigma}} = m^{-1}\sum_{\ell=1}^m \widehat{\mathbf{V}}_K^{(\ell)}\widehat{\mathbf{V}}_K^{(\ell)T}$ and second-order Frobenius Davis–Kahan bias analysis.
2. **`AIMech:PrincipalOrthogonalComplementThresholdingForApproximateFactorCovarianceEstimation`**: Centralized POET covariance thresholding vs. distributed one-shot principal eigenspace and factor loading estimation.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:DistributedPrincipalEigenspaceEstimationBySubspaceProjectionAveraging",
  "source": "Fan, Wang, Wang, & Zhu (2019), Annals of Statistics 47(6):3009-3031, arXiv:1702.06488v4",
  "results": {
    "algorithm1_and_theorem4": {
      "d": 14,
      "K": 2,
      "m_machines": 12,
      "n_local": 45,
      "N_total": 540,
      "avg_local_subspace_err": 0.341641,
      "distributed_pca_subspace_err": 0.093134,
      "centralized_full_pca_subspace_err": 0.079829,
      "error_reduction_ratio": 3.6683,
      "lemma6_identity_abs_diff": 1.438849039914203e-13
    },
    "lemma2_high_order_davis_kahan": {
      "d": 12,
      "K": 2,
      "eigengap_delta": 7.0,
      "norm_E_op": 0.280638,
      "projection_diff_frob": 0.051218,
      "second_order_residual_frob": 0.00181353,
      "lemma2_theoretical_bound": 0.054553
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across two constructed experiments: (1) across m = 12 machines with local sample size n = 45 (N = 540, d = 14, K = 2), Lemma 5's Frobenius subspace distance identity holds to < 1e-11, Lemma 6's least-squares subspace consensus identity sum_{ell=1}^m rho^2(V_tilde_K, V_hat_K^{(ell)}) = 2m(K - sum_{j=1}^K lambda_j(Sigma_tilde)) holds to 1.44e-13, and Algorithm 1 reduces the average local subspace error 0.341641 by 3.67x to 0.093134, closely matching centralized full-sample PCA (0.079829); and (2) for Lemma 2's deterministic high-order Davis-Kahan expansion (d = 12, K = 2, Delta = 7.0, ||E||_2 = 0.2806), subtracting the first-order linear operator f(E U) U^T + U f(E U)^T reduces the projection perturbation Frobenius norm from 0.051218 to a quadratic residual of 0.001814 (well below Lemma 2's theoretical upper bound 24 sqrt(K) (||E||_2 / Delta)^2 = 0.054553).
