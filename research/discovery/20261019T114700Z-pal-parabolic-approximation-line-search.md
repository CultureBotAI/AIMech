# Discovery Report: Round 624 — Parabolic Approximation Line Search

- **Timestamp**: `2026-10-19T11:47:00Z`
- **Selected Concept**: `AIMech:ParabolicApproximationLineSearch` (*Parabolic Approximation Line Search*)
- **Record Path**: `data/curated/ParabolicApproximationLineSearch.yaml`
- **Primary Source**: Maximus Mutschler, Andreas Zell — *Parabolic Approximation Line Search for DNNs* (`https://dblp.org/rec/conf/nips/MutschlerZ20`).

## Identity & Boundary Resolution

Distinct from backtracking Armijo Stochastic Line Search (SLS, which requires the interpolation condition and checks sufficient decrease via variable numbers of forward passes), from linear loss-approximation step-size schemes (L4, ALIG), and from Gaussian-process Probabilistic Line Search (PLS): PAL uses a deterministic 2-forward-pass, 1-backward-pass 1D parabolic fit along unit-normalized negative-gradient or conjugate-like directions.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 624 PAL verified: interp_err=8.88e-16, curv_err=1.24e-13, orth_angle_err=1.41e-12 deg, case2_s_upd=0.40, loss_beta0=7.30e-02, loss_beta04=1.77e-06<loss_beta0
```
