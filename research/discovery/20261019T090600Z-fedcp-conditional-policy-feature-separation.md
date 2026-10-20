# Discovery Report: Round 463 — FedCP (Federated Conditional Policy for Sample-Wise Feature Information Separation)

- **Timestamp**: `2026-10-19T09:06:00Z`
- **Selected Concept**: `AIMech:FedCpConditionalPolicyFeatureSeparationForPersonalizedFederatedLearning` (*FedCP (Federated Conditional Policy for Sample-Wise Feature Information Separation)*)
- **Record Path**: `data/curated/FedCpConditionalPolicyFeatureSeparationForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Jianqing Zhang, Yang Hua, Hao Wang, Tao Song, Zhengui Xue, Ruhui Ma, Haibing Guan — *FedCP: Separating Feature Information for Personalized Federated Learning via Conditional Policy* (`https://doi.org/10.1145/3580305.3599345`).

## Identity & Boundary Resolution

Distinct from FedALA (AIMech:FedAlaAdaptiveLocalAggregationForPersonalizedFederatedLearning, Zhang et al. 2023), which learns static client-level parameter initialization weights W_i^p before local training rather than a sample-dependent feature-gating Conditional Policy Network CPN(C_i; Theta_i) with dual global/personalized heads during forward inference; and distinct from FedRep (AIMech:FedRepSharedRepresentationPersonalizedFederatedLearning) and FedRoD (AIMech:FedRodDecoupledGenericAndPersonalizedFederatedLearning, Chen & Chao 2022), which feed the entire unseparated feature vector h_i into both heads without complementary per-dimension feature gating r_i + s_i = 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 463 FedCP verified: max|r+s-1|=0.0e+00, r_i=[0.833, 0.221, 0.465, 0.465], s_i=[0.167, 0.779, 0.535, 0.535], PIR=0.5040, out0=4.782
```
