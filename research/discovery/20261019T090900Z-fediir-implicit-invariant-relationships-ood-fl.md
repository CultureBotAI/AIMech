# Discovery Report: Round 466 — FedIIR (Out-of-Distribution Generalization of Federated Learning via Implicit Invariant Relationships)

- **Timestamp**: `2026-10-19T09:09:00Z`
- **Selected Concept**: `AIMech:FedIirImplicitInvariantRelationshipsForOutOfDistributionFederatedLearning` (*FedIIR (Out-of-Distribution Generalization of Federated Learning via Implicit Invariant Relationships)*)
- **Record Path**: `data/curated/FedIirImplicitInvariantRelationshipsForOutOfDistributionFederatedLearning.yaml`
- **Primary Source**: Yaming Guo, Kai Guo, Xiaofeng Cao, Tieru Wu, Yi Chang — *Out-of-Distribution Generalization of Federated Learning via Implicit Invariant Relationships* (`https://proceedings.mlr.press/v202/guo23b.html`).

## Identity & Boundary Resolution

Distinct from Invariant Risk Minimization (AIMech:InvariantRiskMinimization, Arjovsky et al. 2019), which penalizes per-environment squared gradient norms ||nabla_{w|w=1.0} R^e(w o Phi)||^2 rather than inter-client classifier gradient variance ||nabla_omega R_c(theta) - nabla_omega R(theta)||^2 with server-side EMA tracking; and distinct from FedSR (AIMech:FedSrSimpleAndEffectiveDomainGeneralizationForFederatedLearning, Nguyen et al. 2022), which enforces conditional mutual information and L2-norm representation regularizers rather than classifier-gradient alignment.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 466 FedIIR verified: phi_erm=[1.0, 0.4], phi_iir=[1.0, 0.039] (theo=0.0400), OOD_risk=0.9400->0.5358
```
