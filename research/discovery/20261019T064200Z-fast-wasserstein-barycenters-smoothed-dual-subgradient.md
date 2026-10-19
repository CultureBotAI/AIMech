# Discovery Report: Round 325 — Fast Wasserstein Barycenters and Smoothed Dual Subgradient Descent

- **Timestamp**: `2026-10-19T06:42:00Z`
- **Selected Concept**: `AIMech:FastWassersteinBarycentersAndSmoothedDualSubgradientDescent` (*Fast Wasserstein Barycenters and Smoothed Dual Subgradient Descent*)
- **Record Path**: `data/curated/FastWassersteinBarycentersAndSmoothedDualSubgradientDescent.yaml`
- **Primary Source**: Marco Cuturi, Arnaud Doucet — *Fast Computation of Wasserstein Barycenters* (`https://proceedings.mlr.press/v32/cuturi14.html`).

## Identity & Boundary Resolution

Distinct from pairwise Sinkhorn distance evaluation (`AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport`) and from Iterative Bregman Projections (`AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport`). Specifically captures the Cuturi & Doucet (2014) primal-dual entropic smoothing of Wasserstein barycenters (Propositions 1 and 2, Equations 6-10), the Algorithm 3 Sinkhorn primal-dual gradient extractor, the Algorithm 1 entropic mirror descent simplex optimizer for fixed-support weights, and the Equation 8 / Algorithm 2 alternating Newton step for free-support atom locations under squared Euclidean ground cost.

## Constructed Boundary & Regime Verification

```text
{"concept": "FastWassersteinBarycentersAndSmoothedDualSubgradientDescent", "euclidean_mean_midpoint_mass": 0.01, "free_support_newton_locations": [0.0, 2.0], "marginal_feasibility_err": 1.915134717478395e-15, "prop2_dual_tangent_grad_err": 1e-09, "status": "VERIFIED", "wasserstein_barycenter_midpoint_mass": 0.845502}
```
