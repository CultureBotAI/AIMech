# Discovery Report: Round 410 — FedSplit (Operator Splitting for Fast Federated Optimization)

- **Timestamp**: `2026-10-19T08:13:00Z`
- **Selected Concept**: `AIMech:FedSplitOperatorSplittingForFastFederatedOptimization` (*FedSplit (Operator Splitting for Fast Federated Optimization)*)
- **Record Path**: `data/curated/FedSplitOperatorSplittingForFastFederatedOptimization.yaml`
- **Primary Source**: Reese Pathak, Martin J. Wainwright — *FedSplit: An algorithmic framework for fast federated optimization* (`https://proceedings.neurips.cc/paper/2020/hash/4ebd440d99504722d80de606ea8507da-Abstract.html`).

## Identity & Boundary Resolution

Distinct from FedAvg / multi-step FedGD(s, e) and FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization), whose deterministic fixed points fail to satisfy sum_{j=1}^m nabla f_j(x^*) = 0 when client objectives are heterogeneous (Propositions 1 and 2), from FedDyn (AIMech:FedDynFederatedLearningBasedOnDynamicRegularization, which maintains a server dual-like state h^t for partial client participation using ADMM-like linear penalties), and from FedPD (AIMech:FedPdFederatedPrimalDualOptimizationWithAdaptivityToNonIidData, which targets non-convex primal-dual augmented Lagrangian consensus with randomized communication skipping).

## Constructed Boundary & Regime Verification

```text
[PASS] FedSplit boundaries verified: x*=2.071429, FedGD(e=2)_err=0.2967, FedProx_err=0.5942, FedSplit_err=0.00e+00, rho=0.5000
```
