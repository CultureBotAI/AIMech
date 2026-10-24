# Discovery Report: Round 324 — Sinkhorn Distances and Entropic Regularized Optimal Transport

- **Timestamp**: `2026-10-19T06:40:00Z`
- **Selected Concept**: `AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport` (*Sinkhorn Distances and Entropic Regularized Optimal Transport*)
- **Record Path**: `data/curated/SinkhornDistancesAndEntropicRegularizedOptimalTransport.yaml`
- **Primary Source**: Marco Cuturi — *Sinkhorn Distances: Lightspeed Computation of Optimal Transport* (`https://papers.nips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html`).

## Identity & Boundary Resolution

Distinct from 1-Wasserstein discriminator critic maximization in Wasserstein GANs (AIMech:WassersteinGANAndKantorovichRubinsteinDualityCritic) and from classical combinatorial auction / network-simplex linear programming solvers. Specifically captures Cuturi's (2013) Primal-Sinkhorn entropy ball constraint U_alpha(r, c) (Definition 1 and Equation 1), the Dual-Sinkhorn entropic Lagrangian d_M^lambda(r, c) = <P^lambda, M> (Equation 2), the metric symmetry and triangle-inequality proof via conditional gluing of transport plans and strong data-processing inequality I(X; Z) <= min(I(X; Y), I(Y; Z)) (Theorem 1 and Lemma 1), the Gibbs kernel diagonal scaling characterization P^lambda = diag(u) exp(-lambda M) diag(v) (Lemma 2), and the vectorized Sinkhorn-Knopp algorithm (Algorithm 1).

## Constructed Boundary & Regime Verification

```text
{"concept": "SinkhornDistancesAndEntropicRegularizedOptimalTransport", "cost_trajectory_vs_lambda": [0.931449, 0.808138, 0.80002, 0.8], "entropy_trajectory_vs_lambda": [1.897269, 1.77826, 1.758002, 1.75789], "kl_glued_xz": 0.155965, "kl_mutual_info_xy": 0.402584, "marginal_feasibility_err": 1.6653345369377348e-15, "non_coincidence_self_distance": 0.160602, "status": "VERIFIED"}
```
