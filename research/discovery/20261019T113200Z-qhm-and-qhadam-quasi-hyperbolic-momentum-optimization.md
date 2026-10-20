# Discovery Report: Round 609 — Quasi-Hyperbolic Momentum (QHM) and Quasi-Hyperbolic Adam (QHAdam) Optimization

- **Timestamp**: `2026-10-19T11:32:00Z`
- **Selected Concept**: `AIMech:QhmAndQhAdamQuasiHyperbolicMomentumAndAdaptiveOptimization` (*Quasi-Hyperbolic Momentum (QHM) and Quasi-Hyperbolic Adam (QHAdam) Optimization*)
- **Record Path**: `data/curated/QhmAndQhAdamQuasiHyperbolicMomentumAndAdaptiveOptimization.yaml`
- **Primary Source**: Jerry Ma, Denis Yarats — *Quasi-hyperbolic momentum and Adam for deep learning* (`https://dblp.org/rec/conf/iclr/MaY19`).

## Identity & Boundary Resolution

Distinct from standard Polyak momentum and Nesterov's Accelerated Gradient (NAG), which tightly couple the momentum buffer's exponential discount factor beta to the current gradient's weight (recovered as special cases of QHM at nu = 1 and nu = beta, respectively); distinct from Aggregated Momentum (AggMo, Lucas et al., 2018), which maintains K >= 2 separate momentum buffers rather than a single momentum buffer interpolated with the current gradient; and distinct from vanilla Adam (Kingma & Ba, 2015) and NAdam (Dozat, 2016), which correspond to QHAdam at (nu_1, nu_2) = (1, 1) and (modulo bias correction) (nu_1, nu_2) = (beta_1, 1) without second-moment immediate discounting nu_2 < 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 609 QHM/QHAdam verified: unrolled_err=4.44e-16, cov_err=0.00e+00, snv_err=5.55e-16, pid_err=6.66e-16, acc_err=6.11e-16, xi_nag_gap=2.3604>0, f1_err=0.00e+00, adam_bound=7.2703>kb=3.1623, nmt_bound_ratio=0.6303<1
```
