# Discovery Report: Round 253 — Loss-Specific Optimal Singular Value Shrinkage for Low-Rank Matrix Denoising

- **Timestamp**: `2026-10-19T01:12:00Z`
- **Selected Concept**: `AIMech:LossSpecificOptimalSingularValueShrinkageForMatrixDenoising` (*Loss-Specific Optimal Singular Value Shrinkage for Low-Rank Matrix Denoising*)
- **Record Path**: `data/curated/LossSpecificOptimalSingularValueShrinkageForMatrixDenoising.yaml`
- **Primary Source**: Matan Gavish and David L. Donoho (2017), *Optimal Shrinkage of Singular Values*, *IEEE Transactions on Information Theory* 63(4):2137-2152 (`arXiv:1405.7511v3`, `DOI:10.1109/TIT.2017.2653801`).

## Identity & Boundary Resolution

`AIMech:LossSpecificOptimalSingularValueShrinkageForMatrixDenoising` was checked against all 442 pinned AIO concepts and 647 maintained AIMech concepts:

1. **`AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree`**: Restricts estimation to hard truncation $y \mathbf{1}(y \ge \tau_*)$ under Frobenius MSE (worst-case AMSE $3r$), whereas Gavish & Donoho (2017) derive loss-specific continuous and discontinuous singular value shrinkers across Frobenius (worst-case AMSE $2r$), nuclear, operator, and Schatten-$p$ norm losses.
2. **`AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices`**: Shrinks symmetric sample covariance eigenvalues toward $1$ using a single QR basis $W_n$, whereas Gavish & Donoho (2017) shrink rectangular singular values toward $0$ using separate left and right Gram-Schmidt bases $W_n, \tilde{W}_n$ with distinct left/right cosines $c(x) \ne \tilde{c}(x)$.

## Constructed Boundary & Regime Verification

```text
Gavish & Donoho (2017) optimal singular value shrinkage verified: MSE optimal shrinker=3.041 (asymp=3.224) < hard=4.099 < TSVD=4.099 < soft=5.623.
```

Verified analytically and via Monte Carlo: (1) exact forward/inverse rectangular singular value bijection y(x) = sqrt((x + 1/x)(x + beta/x)) and x(y) above 1 + sqrt(beta); (2) exact identity eta_fro^*(y) = x(y) c(x(y)) tilde_c(x(y)) = (1/y) sqrt((y^2 - beta - 1)^2 - 4 beta), nuclear-norm bulk neighborhood threshold x_0 > beta^{1/4} where c(x_0) tilde_c(x_0) = s(x_0) tilde_s(x_0) (x_0 = sqrt(2), y_0 = 3/sqrt(2) ~= 2.1213 at beta = 1), and exact 2x2 reciprocal-quadratic operator-norm minimizer z_1(x, beta) x(y) <= x(y); (3) strict ordering 0 <= eta_nuc^* <= eta_{S_1.5}^* <= eta_fro^* <= eta_{S_4}^* <= eta_op^*; and (4) finite-sample Monte Carlo (n=60, m=45, beta=0.75, r=2) confirming Frobenius MSE 3.041 (asymptotic 3.224) < hard thresholding 4.099 < soft thresholding 5.623.
