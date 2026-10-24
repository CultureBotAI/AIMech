# Discovery Report: Round 431 — DIGing and Push-DIGing (Distributed Inexact Gradient Tracking Over Time-Varying Graphs)

- **Timestamp**: `2026-10-19T08:34:00Z`
- **Selected Concept**: `AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs` (*DIGing and Push-DIGing (Distributed Inexact Gradient Tracking Over Time-Varying Graphs)*)
- **Record Path**: `data/curated/DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs.yaml`
- **Primary Source**: Angelia Nedic, Alex Olshevsky, Wei Shi — *Achieving Geometric Convergence for Distributed Optimization Over Time-Varying Graphs* (`https://doi.org/10.1137/16M1084316`).

## Identity & Boundary Resolution

Distinct from DSGT and GSGT (AIMech:DsgtAndGsgtDistributedStochasticGradientTracking, Pu & Nedic 2021), which analyze noisy stochastic gradients G(x_k, xi_k) over static expectation-doubly-stochastic graphs, and from Stochastic Gradient Push (AIMech:StochasticGradientPushAndOverlapSgpForDistributedDeepLearning, Assran et al. 2019), which omits the gradient tracker y(k) and achieves sublinear O(1 / sqrt(n K)) convergence rather than global R-linear geometric convergence O(lambda^k) over time-varying directed graphs.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 431 DIGing & Push-DIGing (Nedic, Olshevsky, & Shi 2017): dig_err=2.67e-15, lambda=0.9909, row_stoch_err=2.22e-16, push_dig_err=1.42e-16
```
