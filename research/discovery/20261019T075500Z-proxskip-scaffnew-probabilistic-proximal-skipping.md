# Discovery Report: Round 392 — ProxSkip and Scaffnew Probabilistic Proximal Skipping for Accelerated Local Gradient Descent

- **Timestamp**: `2026-10-19T07:55:00Z`
- **Selected Concept**: `AIMech:ProxSkipAndScaffnewProbabilisticProximalSkippingForAcceleratedLocalGradientDescent` (*ProxSkip and Scaffnew Probabilistic Proximal Skipping for Accelerated Local Gradient Descent*)
- **Record Path**: `data/curated/ProxSkipAndScaffnewProbabilisticProximalSkippingForAcceleratedLocalGradientDescent.yaml`
- **Primary Source**: Konstantin Mishchenko, Grigory Malinovsky, Sebastian Stich, Peter Richtarik — *ProxSkip: Yes! Local Gradient Steps Provably Lead to Communication Acceleration! Finally!* (`https://doi.org/10.48550/arXiv.2202.09357`).

## Identity & Boundary Resolution

Distinct from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which uses deterministic K-step local schedules and requires O(kappa log(1/eps)) communication rounds under arbitrary heterogeneity) and from FedProx (AIMech:FedProxProximalFederatedOptimization, which adds a static proximal penalty (mu/2)||w - w^t||^2 without control variates or O(sqrt(kappa)) communication acceleration). Scaffnew is the exact consensus-splitting specialization of ProxSkip where psi is the indicator of x_1 = ... = x_n and prox_{(gamma/p) psi} reduces to exact model averaging across clients.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 392 ProxSkip/Scaffnew verified: scaff_err=1.926e-34, h_err=6.360e-30, lgd_err=6.702e-02, comm_rounds=233/600
```
