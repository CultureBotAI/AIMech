# Discovery Report: Round 626 — Stochastic Polyak Step-Size

- **Timestamp**: `2026-10-19T11:49:00Z`
- **Selected Concept**: `AIMech:StochasticPolyakStepSize` (*Stochastic Polyak Step-Size*)
- **Record Path**: `data/curated/StochasticPolyakStepSize.yaml`
- **Primary Source**: Nicolas Loizou, Sharan Vaswani, Issam Hadj Laradji, Simon Lacoste-Julien — *Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence* (`https://dblp.org/rec/conf/aistats/LoizouVLL21`).

## Identity & Boundary Resolution

Distinct from classical deterministic Polyak step-size (Polyak, 1987, which requires full objective evaluations f(x^k), full subgradients g^k, and the global minimum f^*), from ALI-G (Berrada et al., 2020, which adds a denominator regularizer delta > 0 that prevents exact convergence under interpolation), from L4 (Rolinek & Martius, 2018, which estimates f_i^* online using three hyperparameters without convergence guarantees), and from Stochastic Armijo Line Search (SLS, Vaswani et al., 2019, which requires expensive backtracking function evaluations).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 626 SPS verified: eq17_err=5.55e-17, cor32_rat=0.3563<=1, thm31_rat=0.4706<=1, rk_step_err=1.11e-16, w1_logloss_grad_err=5.55e-17, w0_exploss_grad_err=5.55e-17
```
