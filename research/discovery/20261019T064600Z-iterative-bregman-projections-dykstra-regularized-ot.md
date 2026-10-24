# Discovery Report: Round 327 — Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport

- **Timestamp**: `2026-10-19T06:46:00Z`
- **Selected Concept**: `AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport` (*Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport*)
- **Record Path**: `data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml`
- **Primary Source**: Jean-David Benamou, Guillaume Carlier, Marco Cuturi, Luca Nenna, Gabriel Peyré — *Iterative Bregman Projections for Regularized Transportation Problems* (`https://api.crossref.org/works/10.1137/141000439`).

## Identity & Boundary Resolution

Distinct from standard pairwise Sinkhorn matrix scaling (`AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport`) and dual subgradient Wasserstein barycenters (`AIMech:FastWassersteinBarycentersAndSmoothedDualSubgradientDescent`). Specifically captures the Benamou et al. (2015) unified KL Bregman projection formulation over intersections of affine and non-affine convex sets (Section 2, Equations 2-4), the Proposition 2 geometric-mean IBP Wasserstein barycenter algorithm (which eliminates inner Sinkhorn loops and line-search step sizes), and the Bregman-Dykstra algorithm with multiplicative memory variables for partial, capacity-constrained, and martingale transport (Sections 5.1-5.3, Propositions 4-5, Equations 20-26).

## Constructed Boundary & Regime Verification

```text
{"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport", "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15, "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17, "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"}
```
