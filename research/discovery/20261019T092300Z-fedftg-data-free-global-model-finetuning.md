# Discovery Report: Round 480 — FedFTG (Data-Free Global Model Fine-Tuning via Hard Sample Mining Knowledge Distillation)

- **Timestamp**: `2026-10-19T09:23:00Z`
- **Selected Concept**: `AIMech:FedFtgDataFreeGlobalModelFineTuningViaHardSampleMiningKnowledgeDistillation` (*FedFTG (Data-Free Global Model Fine-Tuning via Hard Sample Mining Knowledge Distillation)*)
- **Record Path**: `data/curated/FedFtgDataFreeGlobalModelFineTuningViaHardSampleMiningKnowledgeDistillation.yaml`
- **Primary Source**: Lin Zhang, Li Shen, Liang Ding, Dacheng Tao, Ling-Yu Duan — *Fine-Tuning Global Model via Data-Free Knowledge Distillation for Non-IID Federated Learning* (`https://arxiv.org/abs/2203.09249`).

## Identity & Boundary Resolution

Distinct from FedGen (AIMech:FedGenDataFreeKnowledgeDistillationForHeterogeneousFederatedLearning, Zhu, Hong, & Zhou 2021), which broadcasts a lightweight latent-feature generator to clients to regularize local training rather than adversarially mining hard input-space pseudo-samples x_tilde on the server to fine-tune the global model omega_t via minimax discrepancy maximization (Equation 8); and distinct from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which requires an external unlabeled proxy dataset on the server and uses uniform client logit averaging rather than data-free adversarial generation with class-specific ensemble weights alpha_t^{k,y} (Equation 10).

## Constructed Boundary & Regime Verification

```text
[PASS] FedFTG boundary verification passed: L_dis(collapsed)=1.000 -> L_dis(dispersed)=0.064, L_md_init=0.8674 -> L_md_final=0.0467 (opt=0.0467)
```
