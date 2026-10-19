# Discovery Report: Round 326 — Entropic Gromov-Wasserstein Discrepancy and Barycenter Averaging

- **Timestamp**: `2026-10-19T06:44:00Z`
- **Selected Concept**: `AIMech:EntropicGromovWassersteinDiscrepancyAndBarycenterAveraging` (*Entropic Gromov-Wasserstein Discrepancy and Barycenter Averaging*)
- **Record Path**: `data/curated/EntropicGromovWassersteinDiscrepancyAndBarycenterAveraging.yaml`
- **Primary Source**: Gabriel Peyré, Marco Cuturi, Justin Solomon — *Gromov-Wasserstein Averaging of Kernel and Distance Matrices* (`https://proceedings.mlr.press/v48/peyre16.html`).

## Identity & Boundary Resolution

Distinct from standard linear Wasserstein optimal transport (`AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport`) and linear Wasserstein barycenters (`AIMech:FastWassersteinBarycentersAndSmoothedDualSubgradientDescent`), which require a cross-domain ground cost matrix M_{ij} between points in a shared ambient space. Specifically captures the Peyré, Cuturi, and Solomon (2016) entropic regularization of Mémoli's Gromov-Wasserstein discrepancy (Equations 2-4), the Proposition 1 O(N^2 M + N M^2) separable-loss factorization, the Proposition 2 / Algorithm 1 iterative Sinkhorn solver, and the Propositions 3-5 / Algorithm 2 closed-form L_2 and KL relational barycenter updates.

## Constructed Boundary & Regime Verification

```text
{"concept": "EntropicGromovWassersteinDiscrepancyAndBarycenterAveraging", "prop1_kl_contraction_err": 1.3877787807814457e-16, "prop1_l2_contraction_err": 5.551115123125783e-17, "prop2_isometric_perm_alignment_err": 0.0, "prop4_psd_barycenter_det": 1.147391, "prop5_cond_psd_quadratic_form": 0.977431, "status": "VERIFIED"}
```
