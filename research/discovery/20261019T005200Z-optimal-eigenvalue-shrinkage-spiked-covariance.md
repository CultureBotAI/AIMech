# Discovery Report: Round 251 — Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices

- **Timestamp**: `2026-10-19T00:52:00Z`
- **Selected Concept**: `AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices` (*Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices*)
- **Record Path**: `data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml`
- **Primary Source**: David L. Donoho, Matan Gavish, and Iain M. Johnstone (2018), *Optimal shrinkage of eigenvalues in the spiked covariance model*, *The Annals of Statistics* 46(4):1742-1778 (`arXiv:1311.0851v3`, `DOI:10.1214/17-AOS1601`).

## Identity & Boundary Resolution

`AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices` was checked against all 442 pinned AIO concepts and 645 maintained AIMech concepts:

1. **`AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation`**: Establishes the forward eigenvalue limit $\lambda(\ell) = \ell + \gamma \ell / (\ell - 1)$ without 2x2 eigenvector-cosine pivot-loss decoupling or optimal eigenvalue shrinkage rules.
2. **`AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition`**: Characterizes the $M^{-2/3} F_k$ and $M^{-1/2} G_k$ fluctuation laws of the largest sample eigenvalue.
3. **`AIMech:RotationallyInvariantNonlinearShrinkageCovarianceEstimation` / `AIMech:QuESTNonlinearShrinkageCovarianceEstimation`**: Address general bulk spectra via Stieltjes transforms rather than closed-form loss-specific spiked covariance shrinkage across 26 pivot and discrepancy losses.

## Constructed Boundary & Regime Verification

```text
Donoho, Gavish, & Johnstone (2018) loss-specific optimal eigenvalue shrinkage verified: Frobenius loss 38.67 -> 7.18 (asymp=6.18); Stein loss 9.69 -> 0.33 (asymp=0.30); MP median sigma^2_hat=2.578 vs 2.500.
```

Verified analytically and via Monte Carlo: (1) exact forward/inverse Baik-Silverstein bijection lambda(ell) = ell + gamma ell / (ell - 1) and ell(lambda) above lambda_+(gamma); (2) nuclear-norm neighborhood bulk shrinkage eta_*^N(ell) = 1 on (ell_+(gamma), 1 + 0.5*(gamma + sqrt(gamma^2 + 8*gamma))] where c^2(ell) <= 1/2; (3) strict ordering 1 < eta_*^{St}(ell) < eta_*^{fre}(ell) < eta_*^F(ell) < eta_*^O(ell) = ell and 2x2 grid-optimality across Frobenius, Stein, Operator, and Nuclear losses; and (4) high-dimensional Wishart simulation (n=120, p=60, gamma=0.5, spikes 5.0 and 3.0) reducing Frobenius squared loss from 38.67 to 7.18 (asymptotic 6.18) and Stein loss from 9.69 to 0.33 (asymptotic 0.30) with Marcenko-Pastur median variance plug-in hat_sigma^2 = 2.578 vs 2.500.
