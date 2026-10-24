# Discovery Report: Round 462 — FedCorr (Multi-Stage Federated Learning for Heterogeneous Label Noise Correction)

- **Timestamp**: `2026-10-19T09:05:00Z`
- **Selected Concept**: `AIMech:FedCorrMultiStageLabelNoiseCorrectionForFederatedLearning` (*FedCorr (Multi-Stage Federated Learning for Heterogeneous Label Noise Correction)*)
- **Record Path**: `data/curated/FedCorrMultiStageLabelNoiseCorrectionForFederatedLearning.yaml`
- **Primary Source**: Jingyi Xu, Zihan Chen, Tony Q. S. Quek, Kai Fong Ernest Chong — *FedCorr: Multi-Stage Federated Learning for Label Noise Correction* (`https://doi.org/10.1109/CVPR52688.2022.00994`).

## Identity & Boundary Resolution

Distinct from centralized noisy-label learning methods such as DivideMix (AIMech:DivideMixLearningWithNoisyLabelsAsSemiSupervisedLearning, Li et al. 2020) and Co-teaching (AIMech:CoTeachingRobustTrainingOfDeepNeuralNetworksWithExtremelyNoisyLabels, Han et al. 2018), which assume a single centralized dataset with homogeneous noise and cannot distinguish clean versus noisy clients or bound non-IID weight divergence across distributed clients; and distinct from Byzantine-robust gradient aggregators (such as Krum or Trimmed Mean), which discard client updates rather than correcting corrupted local sample labels.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 462 FedCorr verified: cum_LID_clean=6.278<cum_LID_noisy=9.950, drift=0.532->0.332, clean_labels=6/20->16/20
```
