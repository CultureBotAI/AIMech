# Discovery Report: Round 571 — ProxSkip-VR and ProxSkip-HUB Variance-Reduced Local Training and Regional-Hub Federated Optimization

- **Timestamp**: `2026-10-19T10:54:00Z`
- **Selected Concept**: `AIMech:ProxSkipVrAndProxSkipHubVarianceReducedLocalTrainingAndRegionalHubFederatedOptimization` (*ProxSkip-VR and ProxSkip-HUB Variance-Reduced Local Training and Regional-Hub Federated Optimization*)
- **Record Path**: `data/curated/ProxSkipVrAndProxSkipHubVarianceReducedLocalTrainingAndRegionalHubFederatedOptimization.yaml`
- **Primary Source**: Grigory Malinovsky, Kai Yi, Peter Richtárik — *Variance Reduced ProxSkip: Algorithm, Theory and Application to Federated Learning* (`https://api.openalex.org/works/W7133186255`).

## Identity & Boundary Resolution

Distinct from vanilla ProxSkip and SProxSkip (Mishchenko et al. 2022, which use either full batch gradients nabla f(x_t) at every local step or non-variance-reduced stochastic gradients with C > 0 that only converge to a neighborhood or require O(1/epsilon) complexity), and distinct from non-accelerated variance-reduced local methods such as S-Local-SVRG and Scaffold: ProxSkip-VR couples probabilistic prox skipping with recursive variance-reduced estimators (C = C_tilde = 0), achieving accelerated O(sqrt(L(tau)/mu) log(1/epsilon)) communication complexity while reducing total computation-plus-communication cost whenever the per-sample local computation cost delta exceeds a small threshold.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 571 ProxSkip-VR/HUB verified: cost_ratio(0)=0.7638<1<4.51<4.63, err_x=3.533e-32, err_h=5.136e-33
```
