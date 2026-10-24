# Discovery Report: Round 252 — Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising

- **Timestamp**: `2026-10-19T01:02:00Z`
- **Selected Concept**: `AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree` (*Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising*)
- **Record Path**: `data/curated/OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml`
- **Primary Source**: Matan Gavish and David L. Donoho (2014), *The Optimal Hard Threshold for Singular Values is $4/\sqrt{3}$*, *IEEE Transactions on Information Theory* 60(8):5040-5053 (`arXiv:1305.5870v3`, `DOI:10.1109/TIT.2014.2323359`).

## Identity & Boundary Resolution

`AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree` was checked against all 442 pinned AIO concepts and 646 maintained AIMech concepts:

1. **`AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices`**: Shrinks sample covariance eigenvalues toward 1 under 26 covariance losses rather than hard-thresholding rectangular data singular values to 0 at $\lambda_*(\beta)\sqrt{n}\sigma$.
2. **`AIMech:SingularValueThresholdingForMatrixCompletion`**: Uses iterative soft thresholding in Uzawa optimization for matrix completion from partial entries.

## Constructed Boundary & Regime Verification

```text
Gavish & Donoho (2014) optimal singular value hard threshold 4/sqrt(3) verified: tau*=2.3094 (adaptive tau^*=2.2969), MSE SVHT=2.885 (adaptive=2.885) vs TSVD=7.788 and USVT=5.022.
```

Verified analytically and via Monte Carlo: (1) exact reproduction of Table I aspect-ratio optimal thresholds lambda_*(beta) for beta in {0.05, 0.25, 0.50, 0.75, 1.00} with lambda_*(1) = 4/sqrt(3) ~= 2.3094; (2) exact verification of the indifference quartic x_*^4 - (beta + 1) x_*^2 - 3 beta = 0, Table II square-matrix worst-case AMSE constants (SVHT 3r, USVT 4.26r, TSVD 5r), and Theorem 5 nuclear-norm minimax constant sqrt(3); (3) exact reproduction of Table IV unknown-noise coefficients omega(beta) = lambda_*(beta) / sqrt(mu_beta) (omega(1) = 2.8582) via quarter-circle substitution t = u^2 and cubic approximation within 0.02; and (4) finite-sample Monte Carlo (n=60, r=2, low-SNR singular values 1.25 and 1.15) confirming SVHT (MSE=2.885, adaptive=2.885) substantially outperforms oracle-rank TSVD (MSE=7.788) and USVT 2.02 (MSE=5.022).
