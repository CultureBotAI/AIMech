# Discovery Report: Round 552 — DeTAG Decentralized Stochastic Gradient Tracking with By-Phase Accelerated Gossip

- **Timestamp**: `2026-10-19T10:35:00Z`
- **Selected Concept**: `AIMech:DetagDecentralizedStochasticGradientTrackingWithByPhaseAcceleratedGossip` (*DeTAG Decentralized Stochastic Gradient Tracking with By-Phase Accelerated Gossip*)
- **Record Path**: `data/curated/DetagDecentralizedStochasticGradientTrackingWithByPhaseAcceleratedGossip.yaml`
- **Primary Source**: Yucheng Lu, Christopher De Sa — *Optimal Complexity in Decentralized Training* (`https://dblp.org/rec/conf/icml/LuS21`).

## Identity & Boundary Resolution

Introduced by Yucheng Lu and Christopher De Sa (ICML 2021, PMLR Vol. 139, pp. 7111-7123; arXiv:2006.08085). Distinct from standard Decentralized Stochastic Gradient Tracking (DSGT / GT-DSGD, Pu & Nedic 2020; Zhang & You 2019; Xin et al. 2021), which corresponds to the unaccelerated single-step special case R = 1, eta = 0 and incurs suboptimal O((1 - lambda)^(-3)) spectral-gap dependence; and distinct from RelaySum / RelaySGD (Vogels et al., NeurIPS 2021, Round 549), which routes unattenuated sums over spanning trees rather than running by-phase Chebyshev-accelerated gossip with gradient tracking on arbitrary doubly-stochastic gossip matrices.

## Constructed Boundary & Regime Verification

```text
[PASS] DeTAG boundaries verified: err_ag=4.2248 < err_std=14.1003, detag_max_err=2.33e-04
```
