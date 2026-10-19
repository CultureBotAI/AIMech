# Discovery Report: Round 455 — FedALA (Adaptive Local Aggregation for Personalized Federated Learning)

- **Timestamp**: `2026-10-19T08:58:00Z`
- **Selected Concept**: `AIMech:FedAlaAdaptiveLocalAggregationForPersonalizedFederatedLearning` (*FedALA (Adaptive Local Aggregation for Personalized Federated Learning)*)
- **Record Path**: `data/curated/FedAlaAdaptiveLocalAggregationForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Jianqing Zhang, Yang Hua, Hao Wang, Tao Song, Zhengui Xue, Ruhui Ma, Haibing Guan — *FedALA: Adaptive Local Aggregation for Personalized Federated Learning* (`https://doi.org/10.1609/aaai.v37i9.26330`).

## Identity & Boundary Resolution

Distinct from APFL (Adaptive Personalized Federated Learning, Deng et al. 2020), which mixes a separately trained local model and global model using a single scalar mixing coefficient alpha_i in [0, 1] after or parallel to full-model training; and distinct from FedPer (AIMech:FedPerFederatedLearningWithPersonalizationLayers) and FedRep (AIMech:FedRepSharedRepresentationPersonalizedFederatedLearning, Collins et al. 2021), which hard-code binary layer splits (sigma in {0, 1}) and discard all global information in the personalized head layers rather than learning element-wise [0, 1]-clipped pre-training initialization masks W_i^p.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 455 FedALA verified: loss_fedavg_init=2.6000 -> loss_ala_init=0.020000, W_p=[0.06667050999632229, 0.0]
```
