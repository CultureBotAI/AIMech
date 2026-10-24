# Discovery Report: Round 453 — FedLC (Federated Learning via Logits Calibration for Label Distribution Skew)

- **Timestamp**: `2026-10-19T08:56:00Z`
- **Selected Concept**: `AIMech:FedLcLogitsCalibrationForLabelDistributionSkewInFederatedLearning` (*FedLC (Federated Learning via Logits Calibration for Label Distribution Skew)*)
- **Record Path**: `data/curated/FedLcLogitsCalibrationForLabelDistributionSkewInFederatedLearning.yaml`
- **Primary Source**: Jie Zhang, Zhiqi Li, Bo Li, Jie Xu, Shuang Wu, Shouhong Ding, Chao Wu — *Federated Learning with Label Distribution Skew via Logits Calibration* (`https://proceedings.mlr.press/v162/zhang22p.html`).

## Identity & Boundary Resolution

Distinct from centralized Logit Adjustment (AIMech:LogitAdjustmentForLongTailedClassification, Menon et al. 2021), which shifts logits by log pi_y to achieve Fisher consistency for balanced error on a single centralized long-tailed dataset; FedLC derives a client-specific pairwise margin tau * n_y^{-1/4} from the Rademacher-complexity generalization bound across heterogeneous federated clients and proves via Theorem 3 that it enlarges the majority-to-minority gradient ratio D_{j,r} by exp(tau*(n_r^{-1/4} - n_j^{-1/4})) > 1 to prevent local minority-class weight Updates Delta w_r from having negative inner product with minority representations h^{(r)}.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 453 FedLC verified: D_jr_enlargement=2.0883, proj_CE=-4.17<0, proj_FedLC=0.35>0
```
