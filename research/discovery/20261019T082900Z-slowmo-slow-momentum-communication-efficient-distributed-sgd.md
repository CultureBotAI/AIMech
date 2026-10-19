# Discovery Report: Round 426 — SlowMo (Slow Momentum for Communication-Efficient Distributed SGD)

- **Timestamp**: `2026-10-19T08:29:00Z`
- **Selected Concept**: `AIMech:SlowMoSlowMomentumForCommunicationEfficientDistributedSgd` (*SlowMo (Slow Momentum for Communication-Efficient Distributed SGD)*)
- **Record Path**: `data/curated/SlowMoSlowMomentumForCommunicationEfficientDistributedSgd.yaml`
- **Primary Source**: Jianyu Wang, Vinayak Tantia, Nicolas Ballas, Michael Rabbat — *SlowMo: Improving Communication-Efficient Distributed SGD with Slow Momentum* (`https://openreview.net/forum?id=SkxJ8REYPH`).

## Identity & Boundary Resolution

Distinct from standard Local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent, Stich 2019), which corresponds to the memoryless special case alpha = 1, beta = 0 without outer slow momentum u_t, and from FedOpt (AIMech:FedOptAdaptiveServerOptimizationFedAdagradFedYogiFedAdam, Reddi et al. 2021), which focuses on adaptive second-moment server preconditioners (FedAdagrad, FedYogi, FedAdam) under partial client participation rather than wrapping decentralized gossip/SGP and local base optimizers with outer Polyak momentum and proving BMUF/Lookahead non-convex convergence.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 426 SlowMo (Wang et al. 2020): aux_recurrence_err=1.0e-15, gamma_eff=0.1000, local_sgd_reduction_err=0.0, lookahead_reduction_err=0.0
```
