# Discovery Report: Round 259 — Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance

- **Timestamp**: `2026-10-19T02:15:00Z`
- **Selected Concept**: `AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance` (*Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance*)
- **Record Path**: `data/curated/WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml`
- **Primary Source**: Samet Oymak and Babak Hassibi (2016), *Sharp MSE Bounds for Proximal Denoising*, *Foundations of Computational Mathematics* 16(4):965–1029 (`DOI:10.1007/s10208-015-9278-4`, `arXiv:1305.2714v5`).

## Identity & Boundary Resolution

`AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance` was checked against all 442 pinned AIO concepts and 653 maintained AIMech concepts:

1. **`AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions`**: Defines conic intrinsic volumes $v_k(C)$ and statistical dimension $\delta(C)$ for kinematic phase transitions of random cones, whereas Oymak & Hassibi (2016) prove that the worst-case normalized MSE of convex-regularized proximal denoising across all noise levels $\sigma > 0$ is achieved as $\sigma \to 0^+$ and equals $\mathbf{D}(\lambda \partial f(x_0))$.
2. **`AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems`**: Bounds linear inverse sample complexity via squared Gaussian width $w(T_{\mathcal{A}}(x^*) \cap \mathbb{S}^{p-1})^2$, whereas Oymak & Hassibi (2016) analyze proximal and constrained denoising NMSE via $\mathbf{D}(\lambda \partial f(x_0))$, prove tight multiplicative sandwiching ratios $1 + 2/\sqrt{k^3/n}$ and $1 + 2/\sqrt{r^3 d}$, and derive the exact projected LASSO risk $\mathbf{D}/(m - \mathbf{D})$.

## Constructed Boundary & Regime Verification

```text
Oymak & Hassibi (2016) verified: D(lam*partial f)=32.9944, NMSE(sigma=10)=10.0260, sigma->0 err=0.00e+00, Prop6.1 ratios=(l1:1.5060, nuc:1.004472), LASSO(m=60,D=40) eta=2.00, F=58.00.
```

Verified in pure Python: (1) for l_1 soft-thresholding at n=100, k=10, lambda=1.2, and non-zero amplitude x_{0,i}=2.5, the exact analytic finite-sigma NMSE increases monotonically from NMSE(sigma=10)=10.0260 as sigma decreases and converges to D(lambda partial ||x_0||_1) = 32.9944 with error 0.00e+00 at sigma=1e-6, confirming Theorem 1.1 and Lemma 5.1; (2) Proposition 6.1 multiplicative sandwiching ratios evaluate to 1.5060 for l_1 (n=1000, k=25) and 1.004472 for the nuclear norm (d=200, r=10); and (3) Theorem 3.3 / Proposition 7.1 projected LASSO risk eta = D/(m-D) = 2.00 and residual cost F = m - D/(m-D) = 58.00 at m=60, D=40 satisfy exact complementarity and diverge at the phase transition m -> D+.
