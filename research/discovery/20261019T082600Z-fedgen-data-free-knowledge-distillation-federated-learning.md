# Discovery Report: Round 423 — FedGen (Data-Free Knowledge Distillation for Heterogeneous Federated Learning)

- **Timestamp**: `2026-10-19T08:26:00Z`
- **Selected Concept**: `AIMech:FedGenDataFreeKnowledgeDistillationForHeterogeneousFederatedLearning` (*FedGen (Data-Free Knowledge Distillation for Heterogeneous Federated Learning)*)
- **Record Path**: `data/curated/FedGenDataFreeKnowledgeDistillationForHeterogeneousFederatedLearning.yaml`
- **Primary Source**: Zhuangdi Zhu, Junyuan Hong, Jiayu Zhou — *Data-Free Knowledge Distillation for Heterogeneous Federated Learning* (`https://proceedings.mlr.press/v139/zhu21b.html`).

## Identity & Boundary Resolution

Distinct from proxy-data ensemble distillation FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which requires an external unlabeled public dataset on the server to query client ensembles in raw input space X, whereas FedGen is strictly data-free and learns a compact conditional generator in the intermediate feature space Z.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 423 FedGen (Zhu et al. 2021): prob_weighted=0.9820 > prob_uniform=0.6225, d_hdh_aug=0.34 < d_hdh_local=0.60, bound_fedgen=1.0081 < bound_baseline=1.4005
```
