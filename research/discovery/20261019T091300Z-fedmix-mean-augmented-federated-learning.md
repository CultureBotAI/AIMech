# Discovery Report: Round 470 — FedMix (Approximation of Mixup under Mean Augmented Federated Learning)

- **Timestamp**: `2026-10-19T09:13:00Z`
- **Selected Concept**: `AIMech:FedMixApproximationOfMixupUnderMeanAugmentedFederatedLearning` (*FedMix (Approximation of Mixup under Mean Augmented Federated Learning)*)
- **Record Path**: `data/curated/FedMixApproximationOfMixupUnderMeanAugmentedFederatedLearning.yaml`
- **Primary Source**: Tehrim Yoon, Sumin Shin, Sung Ju Hwang, Eunho Yang — *FedMix: Approximation of Mixup under Mean Augmented Federated Learning* (`https://arxiv.org/abs/2107.00233`).

## Identity & Boundary Resolution

Distinct from standard Mixup (AIMech:MixupVicinalRiskMinimizationByConvexSampleInterpolation, Zhang et al. 2018), which requires direct access to raw sample pairs (x_i, y_i) and (x_j, y_j); and distinct from NaiveMix within MAFL (Equation 1), which directly evaluates f((1 - lambda) x_i + lambda x_bar_j) on averaged inputs without the input-Jacobian correction term lambda (partial ell / partial x) . x_bar_j derived in Proposition 1.

## Constructed Boundary & Regime Verification

```text
[PASS] FedMix boundary verification passed: Eq5_diff=0.00e+00, O(lam^2)_ratios=(4.21, 4.11), |FedMix-NaiveMix|=1.0608e-03
```
