# Discovery Report: Round 644 — K-BFGS and K-BFGS(L) (Kronecker-Factored Quasi-Newton Optimization)

- **Timestamp**: `2026-10-19T12:07:00Z`
- **Selected Concept**: `AIMech:KBfgsKroneckerFactoredQuasiNewtonOptimization` (*K-BFGS and K-BFGS(L) (Kronecker-Factored Quasi-Newton Optimization)*)
- **Record Path**: `data/curated/KBfgsKroneckerFactoredQuasiNewtonOptimization.yaml`
- **Primary Source**: Donald Goldfarb, Yi Ren, Achraf Bahamou — *Practical Quasi-Newton Methods for Training Deep Neural Networks* (`https://dblp.org/rec/conf/nips/GoldfarbRB20`).

## Identity & Boundary Resolution

Distinct from K-FAC (AIMech:KfacKroneckerFactoredApproximateCurvature), which approximates the Fisher information matrix using outer products of backpropagated predictive-distribution gradients and requires explicit O(d_i^3 + d_o^3) matrix inversions every T steps; K-BFGS and K-BFGS(L) approximate the true layerwise Hessian inverse via secant updates on pre-activation changes s_g^l = E[h_l^+ - h_l] and gradient changes y_g^l = E[g_l^+ - g_l] and require only O(d_i^2 + d_o^2) matrix-vector and matrix-matrix multiplications. Distinct from standard L-BFGS (AIMech:LimitedMemoryBfgsOptimization), which operates on the unfactored n-dimensional parameter vector rather than layerwise Kronecker factors.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 644 K-BFGS verified: thm1_diff=1.11e-16, s_raw^T y_raw=-3.100->st^T yt=0.4205>=mu2*||st||^2=0.0484, kron_err=1.78e-15
```
