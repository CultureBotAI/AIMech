# Discovery Report: Round 451 — RandProx (Primal-Dual Optimization with Randomized Proximal Updates)

- **Timestamp**: `2026-10-19T08:54:00Z`
- **Selected Concept**: `AIMech:RandProxPrimalDualOptimizationWithRandomizedProximalUpdates` (*RandProx (Primal-Dual Optimization with Randomized Proximal Updates)*)
- **Record Path**: `data/curated/RandProxPrimalDualOptimizationWithRandomizedProximalUpdates.yaml`
- **Primary Source**: Laurent Condat, Peter Richtarik — *RandProx: Primal-Dual Optimization Algorithms with Randomized Proximal Updates* (`https://openreview.net/forum?id=332bf12183`).

## Identity & Boundary Resolution

Distinct from ProxSkip / Scaffnew (AIMech:ProxSkipLocalGradientStepsWithAcceleratedCommunicationSkipping, Mishchenko et al. 2022), which is recovered as the special case of RandProx where g = 0, K = I, h is a single indicator/regularization function, and R^t is a Bernoulli coin flip, whereas RandProx handles a third composite term g(x), arbitrary bounded linear operators K, multi-block separable sum structures h_m(K_m x), and general unbiased stochastic compression/sampling operators R^t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 451 RandProx (Condat & Richtarik 2023): comm_rate=0.280 (p=0.25), psi_ratio=2.29e-32, primal_err=7.81e-16, dual_err=1.37e-15
```
