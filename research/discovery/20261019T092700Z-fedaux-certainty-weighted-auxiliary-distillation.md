# Discovery Report: Round 484 — FedAUX (Certainty-Weighted Unsupervised Auxiliary Ensemble Distillation for Federated Learning)

- **Timestamp**: `2026-10-19T09:27:00Z`
- **Selected Concept**: `AIMech:FedAuxCertaintyWeightedUnsupervisedAuxiliaryEnsembleDistillationForFederatedLearning` (*FedAUX (Certainty-Weighted Unsupervised Auxiliary Ensemble Distillation for Federated Learning)*)
- **Record Path**: `data/curated/FedAuxCertaintyWeightedUnsupervisedAuxiliaryEnsembleDistillationForFederatedLearning.yaml`
- **Primary Source**: Felix Sattler, Tim Korjakow, Roman Rischke, Wojciech Samek — *FEDAUX: Leveraging Unlabeled Auxiliary Data in Federated Learning* (`https://arxiv.org/abs/2102.02514`).

## Identity & Boundary Resolution

Distinct from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which averages client teacher logits with uniform weights A_mean(x) = softmax((1/|S_t|) sum_{i in S_t} f_i(x)) (Equation 2) and degrades under extreme non-IID domain/label skew where most clients are out-of-distribution on x; and distinct from FedMD (AIMech:FedMdHeterogeneousFederatedLearningViaPublicDatasetModelDistillation, Li & Wang 2019), which requires a labeled public dataset for transfer pretraining and uses unweighted logit averaging without differentially private out-of-distribution certainty scoring.

## Constructed Boundary & Regime Verification

```text
[PASS] FedAUX boundary verification passed: ||w^*-v^*||=0.4153 <= 2.5000, p_mean(class0)=0.413 < 0.5 < p_FedAUX(class0)=0.669
```
