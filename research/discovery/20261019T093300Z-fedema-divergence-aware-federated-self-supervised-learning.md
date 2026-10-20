# Discovery Report: Round 490 — FedEMA (Federated Divergence-Aware Exponential Moving Average Update for Self-Supervised Learning)

- **Timestamp**: `2026-10-19T09:33:00Z`
- **Selected Concept**: `AIMech:FedEmaDivergenceAwareExponentialMovingAverageFederatedSelfSupervisedLearning` (*FedEMA (Federated Divergence-Aware Exponential Moving Average Update for Self-Supervised Learning)*)
- **Record Path**: `data/curated/FedEmaDivergenceAwareExponentialMovingAverageFederatedSelfSupervisedLearning.yaml`
- **Primary Source**: Weiming Zhuang, Yonggang Wen, Shuai Zhang — *Divergence-aware Federated Self-Supervised Learning* (`https://arxiv.org/abs/2204.04385`).

## Identity & Boundary Resolution

Distinct from MOON (AIMech:MoonModelContrastiveFederatedLearning, Li et al. 2021), which adds a supervised model-contrastive representation loss between local and global encoders on labeled client data rather than performing unlabeled Siamese self-supervised learning with L2-divergence-scaled exponential moving average parameter interpolation; and distinct from APFL (AIMech:ApflAdaptivePersonalizedFederatedLearningViaConvexGlobalLocalModelInterpolation, Deng et al. 2020), which learns a gradient-updated mixing scalar alpha_i between separate global and local supervised models rather than dynamically setting the online-network EMA decay rate mu = min(lambda_k ||W_g^r - W_k^{r-1}||_2, 1) from encoder L2 divergence in Siamese self-supervised learning.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 490 FedEMA (Zhuang et al. 2022): mu_cal=0.70 -> mu_later=0.14, err_fedema=0.1848 < err_standalone=0.2450 < err_byol=0.7200
```
