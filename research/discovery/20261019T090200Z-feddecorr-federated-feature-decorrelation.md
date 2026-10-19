# Discovery Report: Round 459 — FedDecorr (Federated Feature Decorrelation Regularization for Mitigating Dimensional Collapse)

- **Timestamp**: `2026-10-19T09:02:00Z`
- **Selected Concept**: `AIMech:FedDecorrFeatureDecorrelationForDimensionalCollapseMitigationInFederatedLearning` (*FedDecorr (Federated Feature Decorrelation Regularization for Mitigating Dimensional Collapse)*)
- **Record Path**: `data/curated/FedDecorrFeatureDecorrelationForDimensionalCollapseMitigationInFederatedLearning.yaml`
- **Primary Source**: Yujun Shi, Jian Liang, Wenqing Zhang, Vincent Y. F. Tan, Song Bai — *Towards Understanding and Mitigating Dimensional Collapse in Heterogeneous Federated Learning* (`https://arxiv.org/abs/2210.00226`).

## Identity & Boundary Resolution

Distinct from self-supervised cross-view invariance and redundancy-reduction losses such as Barlow Twins (AIMech:BarlowTwinsSelfSupervisedLearningViaRedundancyReduction, Zbontar et al. 2021) and VICReg (AIMech:VicRegVarianceInvarianceCovarianceRegularization, Bardes et al. 2022), which operate on paired augmented views in self-supervised pretraining rather than mitigating non-IID client label-skew dimensional collapse (Theorem 1) in supervised federated learning; and distinct from parameter-space proximal or control-variate federated optimizers such as FedProx and SCAFFOLD.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 459 FedDecorr verified: Prop1_diff=5.33e-15, sv_var=10.8228->0.0000, min_sv=0.0032->1.0000
```
