# Discovery Report: Round 642 — Tensor Normal Training (TNT Kronecker-Factored Natural Gradient Optimization)

- **Timestamp**: `2026-10-19T12:05:00Z`
- **Selected Concept**: `AIMech:TensorNormalTrainingKroneckerNaturalGradientOptimization` (*Tensor Normal Training (TNT Kronecker-Factored Natural Gradient Optimization)*)
- **Record Path**: `data/curated/TensorNormalTrainingKroneckerNaturalGradientOptimization.yaml`
- **Primary Source**: Yi Ren, Donald Goldfarb — *Tensor Normal Training for Deep Learning Models* (`https://dblp.org/rec/conf/nips/RenG21`).

## Identity & Boundary Resolution

Distinct from Shampoo (AIMech:ShampooPreconditionedStochasticTensorOptimization), which accumulates unnormalized empirical-gradient outer products E[G_{(j)} G_{(j)}^T] on dataset labels without dividing by prod_{l != j} d_l and preconditions via fractional matrix powers L_j^{-1/(2k)} (an upper bound approximating the square root of the empirical Fisher rather than the true Fisher). Distinct from K-FAC (AIMech:KfacKroneckerFactoredApproximateCurvature), which factors layer curvature into forward activation covariance A A^T and backpropagated pre-activation gradient covariance E_F E_F^T and requires architecture-specific derivations and approximations for convolutional and attention layers, whereas TNT operates directly on the parameter gradient tensor G of any layer shape.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 642 TNT verified: err_U1=0.0126, err_U2=0.0133, thm1_max_diff=(0.0187,0.0200), L_init=8.3925->L_TNT=0.004654<<L_SGD=2.9950
```
