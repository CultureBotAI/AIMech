# Discovery Report: Round 411 — FedPD (Federated Primal-Dual Optimization with Adaptivity to Non-IID Data)

- **Timestamp**: `2026-10-19T08:14:00Z`
- **Selected Concept**: `AIMech:FedPdFederatedPrimalDualOptimizationWithAdaptivityToNonIidData` (*FedPD (Federated Primal-Dual Optimization with Adaptivity to Non-IID Data)*)
- **Record Path**: `data/curated/FedPdFederatedPrimalDualOptimizationWithAdaptivityToNonIidData.yaml`
- **Primary Source**: Xinwei Zhang, Mingyi Hong, Sairaj Dhople, Wotao Yin, Yang Liu — *FedPD: A Federated Learning Framework With Adaptivity to Non-IID Data* (`https://doi.org/10.1109/TSP.2021.3115952`).

## Identity & Boundary Resolution

Distinct from FedDyn (AIMech:FedDynFederatedLearningBasedOnDynamicRegularization, which analyzes convex/strongly convex objectives under partial client participation with a server state vector h^t), from FedSplit (AIMech:FedSplitOperatorSplittingForFastFederatedOptimization, which applies Peaceman-Rachford reflection splitting to convex monotone inclusions without randomized communication skipping p), and from Computation-Then-Aggregation (CTA) primal methods such as FedAvg and FedProx, which diverge on unconstrained non-convex objectives with Q > 1 local steps unless inter-client gradient dissimilarity is bounded (Claim 2.2).

## Constructed Boundary & Regime Verification

```text
[PASS] FedPD boundaries verified: FedAvg amp_factor=1.0625 (x_50=21.72), FedPD eta_max=0.3090, consensus_gap=4.44e-16, x0_final=2.066667
```
