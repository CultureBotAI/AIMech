# Discovery Report: Round 442 — AD-PSGD (Asynchronous Decentralized Parallel Stochastic Gradient Descent)

- **Timestamp**: `2026-10-19T08:45:00Z`
- **Selected Concept**: `AIMech:AdPsgdAsynchronousDecentralizedParallelStochasticGradientDescent` (*AD-PSGD (Asynchronous Decentralized Parallel Stochastic Gradient Descent)*)
- **Record Path**: `data/curated/AdPsgdAsynchronousDecentralizedParallelStochasticGradientDescent.yaml`
- **Primary Source**: Xiangru Lian, Wei Zhang, Ce Zhang, Ji Liu — *Asynchronous Decentralized Parallel Stochastic Gradient Descent* (`https://proceedings.mlr.press/v80/lian18a.html`).

## Identity & Boundary Resolution

Distinct from synchronous D-PSGD (Lian et al. 2017), which blocks all n workers at a global barrier at every iteration so step time is dictated by the slowest worker max_{i in [n]} t_i, and from centralized Asynchronous Parallel SGD (Hogwild! / Lian et al. 2015), which suffers a central parameter-server communication bottleneck and lacks peer-to-peer doubly stochastic gossip averaging W_k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 442 AD-PSGD (Lian et al. 2018): speedup=4.36x, gossip_cons_err=4.44e-16, mean_err=0.0566, K1_4_staleness=10.0
```
