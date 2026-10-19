# Discovery Report: Round 427 — D2 (Decentralized Training over Decentralized Heterogeneous Data)

- **Timestamp**: `2026-10-19T08:30:00Z`
- **Selected Concept**: `AIMech:D2VarianceReducedDecentralizedTrainingOverHeterogeneousData` (*D2 (Decentralized Training over Decentralized Heterogeneous Data)*)
- **Record Path**: `data/curated/D2VarianceReducedDecentralizedTrainingOverHeterogeneousData.yaml`
- **Primary Source**: Hanlin Tang, Xiangru Lian, Ming Yan, Ce Zhang, Ji Liu — *D2: Decentralized Training over Decentralized Data* (`https://proceedings.mlr.press/v80/tang18a.html`).

## Identity & Boundary Resolution

Distinct from centralized federated control-variate methods such as SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning) and FedDyn (AIMech:FedDynDynamicRegularizationForFederatedLearning), which require a central server to aggregate control variates or model states, and from compressed decentralized methods DCD-PSGD/ECD-PSGD (AIMech:DcdPsgdAndEcdPsgdCompressedDecentralizedParallelStochasticGradientDescent) and Choco-SGD (AIMech:ChocoSgdAndChocoGossipDecentralizedCompressedOptimization), whose convergence bounds depend on the inter-worker gradient dissimilarity zeta^2.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 427 D^2 (Tang et al. 2018): |v(-1/3)|=1.0000==1.0 (|v(-0.25)|=0.8090<1<|v(-0.50)|=1.3660), d2_err=5.8e-16 << dpsgd_heterogeneity_err=0.2339
```
