# Discovery Report: Round 441 — Acc-DNGD (Accelerated Distributed Nesterov Gradient Descent)

- **Timestamp**: `2026-10-19T08:44:00Z`
- **Selected Concept**: `AIMech:AccDngdAcceleratedDistributedNesterovGradientDescent` (*Acc-DNGD (Accelerated Distributed Nesterov Gradient Descent)*)
- **Record Path**: `data/curated/AccDngdAcceleratedDistributedNesterovGradientDescent.yaml`
- **Primary Source**: Guannan Qu, Na Li — *Accelerated Distributed Nesterov Gradient Descent* (`https://doi.org/10.1109/TAC.2019.2937496`).

## Identity & Boundary Resolution

Distinct from unaccelerated Distributed Gradient Tracking / DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic, Olshevsky, & Shi 2017; Qu & Li 2018), whose iteration complexity scales linearly with the condition number O(kappa) on strongly convex problems and O(1/t) on general convex problems, and from Dual Optimal Decentralized Acceleration (Uribe et al. 2020), which requires Fenchel conjugate oracle evaluations rather than purely primal gradient-tracking Nesterov extrapolation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 441 Acc-DNGD (Qu & Li 2020): tracking_err=2.89e-15, err_acc=3.27e-02 << err_gt=1.77e+00, kappa1000_acc_gain=7.20x
```
