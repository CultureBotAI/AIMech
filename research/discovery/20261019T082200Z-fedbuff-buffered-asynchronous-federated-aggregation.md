# Discovery Report: Round 419 — FedBuff (Federated Learning with Buffered Asynchronous Aggregation)

- **Timestamp**: `2026-10-19T08:22:00Z`
- **Selected Concept**: `AIMech:FedBuffBufferedAsynchronousFederatedAggregation` (*FedBuff (Federated Learning with Buffered Asynchronous Aggregation)*)
- **Record Path**: `data/curated/FedBuffBufferedAsynchronousFederatedAggregation.yaml`
- **Primary Source**: John Nguyen, Kshitiz Malik, Hongyuan Zhan, Ashkan Yousefpour, Michael Rabbat, Mani Malek, Dzmitry Huba — *Federated Learning with Buffered Asynchronous Aggregation* (`https://proceedings.mlr.press/v151/nguyen22b.html`).

## Identity & Boundary Resolution

Distinct from synchronous Federated Averaging / FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization) and FedOpt (AIMech:FedOptAdaptiveServerOptimizationFedAdagradFedYogiFedAdam), which block each round until the slowest scheduled straggler finishes, and from unbuffered asynchronous FL (FedAsync, K = 1), which updates the global model on every single client arrival and exposes each individual client update without cohort secure aggregation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 419 FedBuff (Nguyen et al. 2022): max_tau(K=1)=24 -> max_tau(K=10)=3, mean_tau(K=1)=9.80 -> mean_tau(K=10)=0.82, lr_norm_invariance_err=0.0
```
