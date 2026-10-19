# Discovery Report: Round 254 — Minimax Risk and Least-Favorable Subspace Characterization of Matrix Denoising by Singular Value Soft Thresholding

- **Timestamp**: `2026-10-19T01:22:00Z`
- **Selected Concept**: `AIMech:MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding` (*Minimax Risk and Least-Favorable Subspace Characterization of Matrix Denoising by Singular Value Soft Thresholding*)
- **Record Path**: `data/curated/MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding.yaml`
- **Primary Source**: David L. Donoho and Matan Gavish (2014), *Minimax risk of matrix denoising by singular value thresholding*, *The Annals of Statistics* 42(6):2413-2440 (`arXiv:1304.2085v4`, `DOI:10.1214/14-AOS1257`).

## Identity & Boundary Resolution

`AIMech:MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding` was checked against all 442 pinned AIO concepts and 648 maintained AIMech concepts:

1. **`AIMech:LossSpecificOptimalSingularValueShrinkageForMatrixDenoising`**: Analyzes fixed-rank $r \ll m_n, n$ loss-specific singular value shrinkers via $2 \times 2$ singular-vector rotation cosines, whereas Donoho & Gavish (2014) prove finite-sample singular-value monotonicity of SVST via SURE and Anderson's theorem and derive the proportional-rank $r_n/m_n \to \rho \in (0, 1)$ minimax risk $\mathcal{M}(\rho, \beta)$ over compressed Marčenko-Pastur laws.
2. **`AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree`**: Analyzes fixed-rank hard truncation at $4/\sqrt{3}$, whereas Donoho & Gavish (2014) analyze proportional-rank soft thresholding $(y_i - \lambda)_+$ and its trigonometric quarter-circle minimax curve.

## Constructed Boundary & Regime Verification

```text
Donoho & Gavish (2014) SVST minimax risk verified: M(0.2, 1|Mat)=0.5717 at Lambda*=0.8677; SV-monotone risk R(mu=0)=0.037 -> R(mu=50)=0.589 (asymp=0.583).
```

Verified analytically and via Monte Carlo: (1) exact agreement between Quarter-Circle closed-form moments Q_0, Q_1, Q_2 (Eqs. 2.17-2.19) and Marcenko-Pastur incomplete moments P_1(x^2; k) (Eq. 2.8); (2) exact agreement between Theorem 5 trigonometric threshold Lambda_* = 2 sin(theta_alpha(rho)), Theorem 7 parametric curve (with the p. 14 Sym formula corrected from 1 - (g - pi/2)/(g + pi/2) to (g - pi/2)/(g + pi/2)), and Theorem 3/4 MP root solver; (3) low-rank slope 2(1 + sqrt(beta) + beta) rho (Theorem 8) and global minimax ratio M(rho, beta) / M^-(rho, beta) <= 2(1 + sqrt(beta)/(1 + beta)) <= 3 (Theorem 9); (4) exact match between central-difference divergence and corrected Lemma 3 SURE formula (fixing the p. 20 typo min(y_i, lambda)*y_j to min(y_i, lambda)*y_i); and (5) Monte Carlo SV-monotonicity R(mu=0)=0.037 < R(mu=0.8)=0.228 < R(mu=2.0)=0.498 < R(mu=50.0)=0.589 converging to the least-favorable subspace risk 0.583 at infinity.
