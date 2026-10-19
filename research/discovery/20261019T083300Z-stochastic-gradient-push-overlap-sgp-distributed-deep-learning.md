# Discovery Report: Round 430 — Stochastic Gradient Push and Overlap SGP (SGP and tau-OSGP for Distributed Deep Learning)

- **Timestamp**: `2026-10-19T08:33:00Z`
- **Selected Concept**: `AIMech:StochasticGradientPushAndOverlapSgpForDistributedDeepLearning` (*Stochastic Gradient Push and Overlap SGP (SGP and tau-OSGP for Distributed Deep Learning)*)
- **Record Path**: `data/curated/StochasticGradientPushAndOverlapSgpForDistributedDeepLearning.yaml`
- **Primary Source**: Mahmoud Assran, Nicolas Loizou, Nicolas Ballas, Michael Rabbat — *Stochastic Gradient Push for Distributed Deep Learning* (`https://proceedings.mlr.press/v97/assran19a.html`).

## Identity & Boundary Resolution

Distinct from Push-DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic, Olshevsky, & Shi 2017), which tracks exact gradient differences via an additional d-dimensional state vector y_i(k) for strongly convex objectives, whereas SGP and tau-OSGP transmit only a single scalar PushSum weight w_i^{(k)} alongside x_i^{(k)} and establish smooth non-convex O(1 / sqrt(n K)) linear speedup and exact log_2(n)-step consensus over time-varying directed exponential graphs.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 430 SGP & Overlap-SGP (Assran et al. 2019): exp_graph_err=0.00e+00, sgp_err=0.1089 << naive_skew_err=1.5431, osgp_col_stochastic=1.0
```
