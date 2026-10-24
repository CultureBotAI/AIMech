# Discovery Report: Round 435 — MSDA and SSDA (Multi-Step and Single-Step Dual Accelerated Decentralized Optimization)

- **Timestamp**: `2026-10-19T08:38:00Z`
- **Selected Concept**: `AIMech:MsdaMultiStepDualAcceleratedDecentralizedOptimization` (*MSDA and SSDA (Multi-Step and Single-Step Dual Accelerated Decentralized Optimization)*)
- **Record Path**: `data/curated/MsdaMultiStepDualAcceleratedDecentralizedOptimization.yaml`
- **Primary Source**: Kevin Scaman, Francis Bach, Sebastien Bubeck, Yin Tat Lee, Laurent Massoulie — *Optimal Algorithms for Smooth and Strongly Convex Distributed Optimization in Networks* (`https://proceedings.mlr.press/v70/scaman17a.html`).

## Identity & Boundary Resolution

Distinct from primal-dual consensus algorithms such as EXTRA (AIMech:ExtraExactFirstOrderDecentralizedConsensusOptimization, Shi et al. 2015) and DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic et al. 2017), which evaluate primal gradients nabla f_i(x_i) without Nesterov dual acceleration or Chebyshev polynomial gossip and have non-accelerated O(kappa_l / gamma) dependence on the condition number kappa_l = beta / alpha and spectral gap gamma(W).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 435 MSDA (Scaman et al. 2017): gamma_W=0.1464 -> gamma_PK=0.4531 (1/sqrt(gamma_PK)=1.4856 <= 2), msda_err=1.93e-14
```
