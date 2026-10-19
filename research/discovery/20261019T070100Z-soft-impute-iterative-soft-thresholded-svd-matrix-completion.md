# Discovery Report: Round 339 — Soft-Impute Iterative Soft-Thresholded SVD for Large Matrix Completion

- **Timestamp**: `2026-10-19T07:01:00Z`
- **Selected Concept**: `AIMech:SoftImputeIterativeSoftThresholdedSVDForLargeMatrixCompletion` (*Soft-Impute Iterative Soft-Thresholded SVD for Large Matrix Completion*)
- **Record Path**: `data/curated/SoftImputeIterativeSoftThresholdedSVDForLargeMatrixCompletion.yaml`
- **Primary Source**: Rahul Mazumder, Trevor Hastie, Robert Tibshirani — *Spectral Regularization Algorithms for Learning Large Incomplete Matrices* (`https://www.jmlr.org/papers/v11/mazumder10a.html`).

## Identity & Boundary Resolution

Distinct from Singular Value Thresholding Algorithm for Matrix Completion (`AIMech:SingularValueThresholdingAlgorithmForMatrixCompletion`), which solves the equality-constrained Uzawa dual subgradient iteration Y^k = Y^{k-1} + delta_k P_Omega(X - Z^k) on sparse dual matrices rather than the unconstrained majorization-minimization update Z^{k+1} = S_lambda(P_Omega(X) + P_Omega^perp(Z^k)) with sparse-plus-low-rank Lanczos decomposition and warm-started regularization paths. Also distinct from AltMinSense and AltMinComplete Alternating Minimization for Low-Rank Matrix Sensing and Completion (`AIMech:AltMinSenseAndAltMinCompleteAlternatingMinimizationForLowRankMatrixSensingAndCompletion`), which performs non-convex fixed-rank alternating least squares without nuclear-norm soft-thresholding.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 339 Soft-Impute (Mazumder, Hastie, & Tibshirani 2010): lemma6_err=8.88e-16, max_eq13_err=8.88e-16, max_eq22_err=0.00e+00, f_inf=3.528894, final_step_diff=1.91e-20
```
