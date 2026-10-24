# Discovery Report: Round 406 — FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)

- **Timestamp**: `2026-10-19T08:09:00Z`
- **Selected Concept**: `AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization` (*FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)*)
- **Record Path**: `data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml`
- **Primary Source**: Xiaoxiao Li, Meirui Jiang, Xiaofei Zhang, Michael Kamp, Qi Dou — *FedBN: Federated Learning on Non-IID Features via Local Batch Normalization* (`https://openreview.net/forum?id=6YEQUn0QICG`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization) and SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning), which synchronize all model layers including Batch Normalization parameters and add proximal or control-variate corrections, and from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, which keeps the top classification head h_i local to address heterogeneous label conditional distributions P_i(y|x) rather than keeping internal Batch Normalization layers local to mitigate feature shift P_i(x)).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366>mu0=0.01559, rate_fedbn=0.5264<rate_fedavg=0.8554, mse_fedbn=1.51e-31<<mse_fedavg_bn=12.7582
```
