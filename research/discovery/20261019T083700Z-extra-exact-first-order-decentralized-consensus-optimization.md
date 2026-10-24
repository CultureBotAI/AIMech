# Discovery Report: Round 434 — EXTRA (Exact First-Order Algorithm for Decentralized Consensus Optimization)

- **Timestamp**: `2026-10-19T08:37:00Z`
- **Selected Concept**: `AIMech:ExtraExactFirstOrderDecentralizedConsensusOptimization` (*EXTRA (Exact First-Order Algorithm for Decentralized Consensus Optimization)*)
- **Record Path**: `data/curated/ExtraExactFirstOrderDecentralizedConsensusOptimization.yaml`
- **Primary Source**: Wei Shi, Qing Ling, Gang Wu, Wotao Yin — *EXTRA: An Exact First-Order Algorithm for Decentralized Consensus Optimization* (`https://doi.org/10.1137/14096668X`).

## Identity & Boundary Resolution

Distinct from Exact Diffusion (AIMech:ExactDiffusionForDistributedOptimizationAndLearning, Yuan et al. 2019), which applies an adapt-then-combine step psi_i^k = w_i^{k-1} - mu_i nabla J_i(w_i^{k-1}) so that both mixing and gradient differences are premultiplied by A_bar = (I + A)/2 with double the stability range, and from DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic, Olshevsky, & Shi 2017), which communicates an auxiliary gradient tracker y^k at every iteration rather than maintaining single-vector primal consensus differences.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 434 EXTRA (Shi et al. 2015): equiv_err=2.15e-15, extra_err=2.00e-16 << dgd_err=2.8412
```
