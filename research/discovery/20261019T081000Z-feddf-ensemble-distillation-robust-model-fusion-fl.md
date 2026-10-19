# Discovery Report: Round 407 — FedDF (Ensemble Distillation for Robust Model Fusion in Federated Learning)

- **Timestamp**: `2026-10-19T08:10:00Z`
- **Selected Concept**: `AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning` (*FedDF (Ensemble Distillation for Robust Model Fusion in Federated Learning)*)
- **Record Path**: `data/curated/FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning.yaml`
- **Primary Source**: Tao Lin, Lingjing Kong, Sebastian U. Stich, Martin Jaggi — *Ensemble Distillation for Robust Model Fusion in Federated Learning* (`https://proceedings.neurips.cc/paper/2020/hash/18df51b97ccd68128e994804f3eccc87-Abstract.html`).

## Identity & Boundary Resolution

Distinct from coordinate-wise parameter-averaging schemes such as FedAvg, FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization), FedNova (AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization), and FedOpt (AIMech:FedOptAdaptiveServerOptimizationFedAdagradFedYogiFedAdam), which cannot fuse heterogeneous neural network architectures and suffer functional collapse when averaging heavily drifted non-linear client weights, and from FedMA (AIMech:FedMaFederatedMatchedAveragingViaLayerWiseBayesianNonparametricMatching, which performs layer-wise Hungarian permutation alignment in weight space without unlabeled server-side logit distillation).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 407 FedDF (Lin et al. 2020): kl_feddf=0.00699<<kl_fedavg=1.8643, kl_het_student=0.05593
```
