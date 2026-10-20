# Discovery Report: Round 477 — FedMAX (Maximum-Entropy Activation Divergence Mitigation in Federated Learning)

- **Timestamp**: `2026-10-19T09:20:00Z`
- **Selected Concept**: `AIMech:FedMaxMaximumEntropyActivationDivergenceMitigationInFederatedLearning` (*FedMAX (Maximum-Entropy Activation Divergence Mitigation in Federated Learning)*)
- **Record Path**: `data/curated/FedMaxMaximumEntropyActivationDivergenceMitigationInFederatedLearning.yaml`
- **Primary Source**: Wei Chen, Kartikeya Bhardwaj, Radu Marculescu — *FedMAX: Mitigating Activation Divergence for Accurate and Communication-Efficient Federated Learning* (`https://arxiv.org/abs/2004.03657`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization, Li et al. 2020), which penalizes Euclidean distance ||w_k - w^t||^2 in weight space rather than regularizing penultimate-layer feature activations; and distinct from FedDecorr (AIMech:FedDecorrFeatureDecorrelationForDimensionalCollapseMitigationInFederatedLearning, Shi et al. 2023), which penalizes the Frobenius norm of off-diagonal entries of the batch feature correlation matrix rather than the Shannon entropy / KL divergence to uniformity of individual softmax-normalized activation vectors sigma(a_i^k).

## Constructed Boundary & Regime Verification

```text
[PASS] FedMAX boundary verification passed: delta_FedAvg=0.7892 -> delta_FedMAX=0.1304, norm_FedMAX=1.611 > norm_L2=0.277
```
