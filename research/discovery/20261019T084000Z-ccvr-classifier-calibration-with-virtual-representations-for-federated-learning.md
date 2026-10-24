# Discovery Report: Round 437 — CCVR (Classifier Calibration with Virtual Representations for Federated Learning)

- **Timestamp**: `2026-10-19T08:40:00Z`
- **Selected Concept**: `AIMech:CcvrClassifierCalibrationWithVirtualRepresentationsForFederatedLearning` (*CCVR (Classifier Calibration with Virtual Representations for Federated Learning)*)
- **Record Path**: `data/curated/CcvrClassifierCalibrationWithVirtualRepresentationsForFederatedLearning.yaml`
- **Primary Source**: Mi Luo, Fei Chen, Dapeng Hu, Yifan Zhang, Jian Liang, Jiashi Feng — *No Fear of Heterogeneity: Classifier Calibration for Federated Learning with Non-IID Data* (`https://proceedings.neurips.cc/paper/2021/hash/2f2b265625d76a6704b08093c652fd79-Abstract.html`).

## Identity & Boundary Resolution

Distinct from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, Collins et al. 2021), which learns client-specific personalized heads locally during alternating minimization rather than calibrating a single global classifier on the server via exact federated Gaussian mixture covariance reconstruction, and from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which requires an external unlabeled proxy dataset on the server for logit knowledge distillation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 437 CCVR (Luo et al. 2021): exact_mu_err=1.30e-16, exact_cov_err=1.60e-15, scalars_per_class=15
```
