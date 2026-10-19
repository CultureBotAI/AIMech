# Discovery Report: Round 438 — Push-Pull and G-Push-Pull Gradient Methods for Distributed Optimization

- **Timestamp**: `2026-10-19T08:41:00Z`
- **Selected Concept**: `AIMech:PushPullAndGPushPullGradientMethodsForDistributedOptimization` (*Push-Pull and G-Push-Pull Gradient Methods for Distributed Optimization*)
- **Record Path**: `data/curated/PushPullAndGPushPullGradientMethodsForDistributedOptimization.yaml`
- **Primary Source**: Shi Pu, Wei Shi, Jinming Xu, Angelia Nedic — *Push-Pull Gradient Methods for Distributed Optimization in Networks* (`https://doi.org/10.1109/TAC.2020.2972824`).

## Identity & Boundary Resolution

Distinct from Push-DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic, Olshevsky, & Shi 2017), which uses only column-stochastic matrices C(k) for both state and tracker updates and requires maintaining and inverting an auxiliary Push-Sum eigenvector estimate V(k) = diag(v(k)) at every step, whereas Push-Pull combines row-stochastic R (pulling states) and column-stochastic C (pushing trackers) to eliminate eigenvector estimation altogether.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 438 Push-Pull (Pu et al. 2021): conservation_err=5.77e-15, err_p2p=4.44e-16, err_leader_only=1.33e-15
```
