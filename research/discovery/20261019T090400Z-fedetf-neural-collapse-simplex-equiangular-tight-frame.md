# Discovery Report: Round 461 — FedETF (Neural-Collapse-Inspired Federated Learning with Synthetic Fixed Simplex ETF Classifier)

- **Timestamp**: `2026-10-19T09:04:00Z`
- **Selected Concept**: `AIMech:FedEtfNeuralCollapseSimplexEquiangularTightFrameClassifierForFederatedLearning` (*FedETF (Neural-Collapse-Inspired Federated Learning with Synthetic Fixed Simplex ETF Classifier)*)
- **Record Path**: `data/curated/FedEtfNeuralCollapseSimplexEquiangularTightFrameClassifierForFederatedLearning.yaml`
- **Primary Source**: Zexi Li, Xinyi Shang, Rui He, Tao Lin, Chao Wu — *No Fear of Classifier Biases: Neural Collapse Inspired Federated Learning with Synthetic and Fixed Classifier* (`https://doi.org/10.1109/ICCV51070.2023.00490`).

## Identity & Boundary Resolution

Distinct from CCVR (AIMech:CcvrClassifierCalibrationWithVirtualRepresentationsForFederatedLearning, Luo et al. 2021), which trains standard unconstrained classifiers during federated learning and recalibrates the classifier post-hoc using Gaussian virtual features; and distinct from FedBABU (AIMech:FedBabuFederatedLearningWithBodyAggregationAndBodyUpdate, Oh et al. 2022), which freezes a randomly initialized orthogonal or uniform classifier head rather than synthesizing an exact Simplex Equiangular Tight Frame V_ETF with a projection layer, learnable temperature scaling beta, and power-law balanced feature loss.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 461 FedETF verified: v_i^T v_j=-1/4=-0.2500, Eq6_diff=0.0e+00, NC2_mse=6.75e-05, learned_beta=5.126
```
