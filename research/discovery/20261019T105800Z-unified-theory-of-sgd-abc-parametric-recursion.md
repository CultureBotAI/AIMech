# Discovery Report: Round 575 — Unified Parametric Theory of Proximal SGD

- **Timestamp**: `2026-10-19T10:58:00Z`
- **Selected Concept**: `AIMech:UnifiedSgdParametricRecursionTheory` (*Unified Parametric Theory of Proximal SGD*)
- **Record Path**: `data/curated/UnifiedSgdParametricRecursionTheory.yaml`
- **Primary Source**: Eduard Gorbunov, Filip Hanzely, Peter Richtarik — *A Unified Theory of SGD: Variance Reduction, Sampling, Quantization and Coordinate Descent* (`https://proceedings.mlr.press/v108/gorbunov20a.html`).

## Identity & Boundary Resolution

Distinct from individual variance-reduced or quantized stochastic gradient methods (such as SAGA, L-SVRG, SEGA, or DIANA) because it defines the six-parameter (A, B, C, D_1, D_2, rho) meta-assumption (Assumption 4.1) and master Lyapunov contraction theorem (Theorem 4.1) that simultaneously derives existing and new methods (SGD-star, N-SAGA, N-SEGA, Q-SGD-SR) as parameter specializations.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 575 Unified SGD verified: err_sgd_star=2.947e-32, tau_errs=(0.0:3.255e-32, 0.25:1.261e-02, 1.0:2.504e-01)
```
