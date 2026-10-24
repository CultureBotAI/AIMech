# Discovery Report: Round 456 — FedDC (Federated Learning via Local Drift Decoupling and Correction)

- **Timestamp**: `2026-10-19T08:59:00Z`
- **Selected Concept**: `AIMech:FedDcLocalDriftDecouplingAndCorrectionForNonIidFederatedLearning` (*FedDC (Federated Learning via Local Drift Decoupling and Correction)*)
- **Record Path**: `data/curated/FedDcLocalDriftDecouplingAndCorrectionForNonIidFederatedLearning.yaml`
- **Primary Source**: Liang Gao, Huazhu Fu, Li Li, Yingwen Chen, Ming Xu, Cheng-Zhong Xu — *FedDC: Federated Learning with Non-IID Data via Local Drift Decoupling and Correction* (`https://doi.org/10.1109/CVPR52688.2022.00987`).

## Identity & Boundary Resolution

Distinct from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, Karimireddy et al. 2020), which only applies a linear control-variate gradient correction without decoupling the parameter-level gap w - theta_i via a shifted quadratic penalty (alpha/2)*||theta_i - (w - h_i)||^2 or aggregating theta_i^+ + h_i^+; and distinct from FedDyn (AIMech:FedDynDynamicRegularizationForFederatedLearning, Acar et al. 2021), which combines a linear historic-gradient term and unshifted quadratic (alpha/2)*||theta_i - w||^2 with server dual state h^t without a separate (1/(eta*K))*<theta_i, g_i - g> SCAFFOLD-style gradient-drift inner product.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 456 FedDC verified: err_dc=9.36e-13 << err_prox=0.0638 < err_avg=0.0658
```
