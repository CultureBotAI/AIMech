# Discovery Report: Round 314 — Iterative Hard Thresholding for Compressed Sensing

- **Timestamp**: `2026-10-19T06:20:00Z`
- **Selected Concept**: `AIMech:IterativeHardThresholdingForCompressedSensing` (*Iterative Hard Thresholding for Compressed Sensing*)
- **Record Path**: `data/curated/IterativeHardThresholdingForCompressedSensing.yaml`
- **Primary Source**: Thomas Blumensath, Mike E. Davies — *Iterative hard thresholding for compressed sensing* (`https://doi.org/10.1016/j.acha.2009.04.002`).

## Identity & Boundary Resolution

Distinct from convex l1 Basis Pursuit / Lasso (AIO:LassoRegression), greedy Orthogonal Matching Pursuit (AIMech:OrthogonalMatchingPursuitTroppGilbertSignalRecovery), and two-stage least-squares pursuit methods (CoSaMP and Subspace Pursuit). Specifically captures the Blumensath-Davies (2009) Iterative Hard Thresholding update x^{[n+1]} = H_s(x^{[n]} + Phi^T(y - Phi x^{[n]})) (Equation 1.5), its RIP contraction analysis on evolving 3s-sparse unions B^n = Gamma^{x,s} union Gamma^n union Gamma^{n+1} (Theorem 4 and Corollary 1), and its residual-based finite-termination criterion (Lemma 5 and Theorem 5).

## Constructed Boundary & Regime Verification

```text
{"concept": "IterativeHardThresholdingForCompressedSensing", "corollary1_bound_5e": 0.177012, "lemma5_stopping_bound": 0.112528, "noise_l2_norm": 0.035402, "noiseless_final_l2_err": 0.0, "noisy_final_l2_err": 0.008577, "status": "VERIFIED", "undersampled_dense_err": 4.8983}
```
