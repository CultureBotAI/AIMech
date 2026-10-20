# Discovery Report: Round 488 — KT-pFL (Parameterized Knowledge Transfer for Personalized Federated Learning)

- **Timestamp**: `2026-10-19T09:31:00Z`
- **Selected Concept**: `AIMech:KtPflParameterizedKnowledgeTransferForPersonalizedFederatedLearning` (*KT-pFL (Parameterized Knowledge Transfer for Personalized Federated Learning)*)
- **Record Path**: `data/curated/KtPflParameterizedKnowledgeTransferForPersonalizedFederatedLearning.yaml`
- **Primary Source**: Jie Zhang, Song Guo, Xiaosong Ma, Haozhao Wang, Wencao Xu, Feijie Wu — *Parameterized Knowledge Transfer for Personalized Federated Learning* (`https://arxiv.org/abs/2111.02862`).

## Identity & Boundary Resolution

Distinct from FedMD (AIMech:FedMdHeterogeneousFederatedLearningViaPublicDatasetModelDistillation, Li & Wang 2019) and FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which form a single unweighted global ensemble teacher (1/N) sum_{m=1}^N s(w^m, x_hat) rather than maintaining a client-specific server soft prediction parameterized by a gradient-trained N x N knowledge coefficient matrix c; and distinct from FedFomo (AIMech:FedFomoFirstOrderModelOptimizationForPersonalizedFederatedLearning, Zhang et al. 2021) and FedAMP (AIMech:FedAmpFederatedAttentiveMessagePassingForPersonalizedCrossSiloFederatedLearning, Huang et al. 2021), which require identical model architectures to aggregate raw model parameters in weight space rather than distilling personalized linear combinations of public-data soft predictions across heterogeneous neural architectures.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 488 KT-pFL (Zhang et al. 2021): risk_cluster=-0.000000 < risk_standalone=0.010470 < risk_uniform=0.348561, obj_init=1.1134 -> obj_final=0.0977, intra_c=0.500 > inter_c=0.000
```
