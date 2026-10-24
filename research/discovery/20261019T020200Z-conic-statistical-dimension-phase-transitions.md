# Discovery Report: Round 257 — Conic Statistical Dimension, Intrinsic Volume Concentration, and Approximate Kinematic Phase Transitions in Random Convex Programs

- **Timestamp**: `2026-10-19T02:02:00Z`
- **Selected Concept**: `AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions` (*Conic Statistical Dimension, Intrinsic Volume Concentration, and Approximate Kinematic Phase Transitions in Random Convex Programs*)
- **Record Path**: `data/curated/ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions.yaml`
- **Primary Source**: Dennis Amelunxen, Martin Lotz, Michael B. McCoy, and Joel A. Tropp (2014), *Living on the edge: phase transitions in convex programs with random data*, *Information and Inference: A Journal of the IMA* 3(3):224-294 (`DOI:10.1093/imaiai/iau005`, `arXiv:1303.6672v2`).

## Identity & Boundary Resolution

`AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions` was checked against all 442 pinned AIO concepts and 651 maintained AIMech concepts:

1. **`AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems`**: Proves one-sided Gaussian recovery sufficiency bounds via Gordon's inequality, whereas Amelunxen et al. (2014) establish conic intrinsic-volume concentration around the statistical dimension $\delta(C)$, the two-sided Approximate Kinematic Formula, universal phase transitions for linear inverse problems, convex demixing, and random cone programs, and the nonasymptotic Theorem 4.3 error bound for the subdifferential recipe.
2. **`AIMech:MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding`**: Characterizes matrix denoising risk under SVST, whereas Amelunxen et al. (2014) establish the conic kinematic phase transition theory and Schatten 1-norm descent-cone statistical dimension.

## Constructed Boundary & Regime Verification

```text
Amelunxen et al. (2014) statistical dimension verified: Gauss-Bonnet err=0.00e+00, Crofton(d=101,m=35,50,66)=(0.9991,0.5000,0.0009), l1 psi(0.2)=0.5111 (tau*=0.8616, err_bd=0.0089), permutahedron(d=100) delta=94.8126.
```

Verified in pure Python: (1) for the nonnegative orthant R_+^{100}, conic intrinsic volumes v_k = 2^{-100} C(100, k) satisfy Gauss-Bonnet sum_{even} v_k = 1/2 to 0.00e+00, intrinsic and metric statistical dimension delta(R_+^{100}) = 50.0, half-tail interlacing 2 h_k >= t_k >= 2 h_{k+1}, and Theorem 6.1 concentration bounds; (2) for d=101, the exact Crofton probability 2 h_{m+1}(R_+^{101}) drops from 0.9991 at m=35 through 0.5000 at m=50.5 to 0.0009 at m=66; (3) the l_1 subdifferential recipe (Eqs. 4.4-4.6) at rho=0.2 (d=500, s=100) gives psi(0.2)=0.5111 with tau*=0.8616 and Theorem 4.3 error bound 0.0089; and (4) the Weyl chamber A_{d-1} generating polynomial confirms delta(C_A) = H_d and the d=100 permutahedron threshold d - H_{100} = 94.8126 (matching Figure 9.1).
