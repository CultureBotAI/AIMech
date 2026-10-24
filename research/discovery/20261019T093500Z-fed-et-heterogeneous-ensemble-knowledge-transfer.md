# Discovery Report: Round 492 — Fed-ET (Heterogeneous Ensemble Knowledge Transfer with Confidence-Weighted Consensus and Diversity Regularization)

- **Timestamp**: `2026-10-19T09:35:00Z`
- **Selected Concept**: `AIMech:FedEtHeterogeneousEnsembleKnowledgeTransferWithWeightedConsensusAndDiversityRegularization` (*Fed-ET (Heterogeneous Ensemble Knowledge Transfer with Confidence-Weighted Consensus and Diversity Regularization)*)
- **Record Path**: `data/curated/FedEtHeterogeneousEnsembleKnowledgeTransferWithWeightedConsensusAndDiversityRegularization.yaml`
- **Primary Source**: Yae Jee Cho, Andre Manoel, Gauri Joshi, Robert Sim, Dimitrios Dimitriadis — *Heterogeneous Ensemble Knowledge Transfer for Training Large Models in Federated Learning* (`https://arxiv.org/abs/2204.12703`).

## Identity & Boundary Resolution

Distinct from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, Lin et al. 2020), which averages client logits with uniform weights without intra-logit variance confidence weighting, dissenting-client diversity KL regularization, or bi-directional representation-layer transfer to a strictly larger server model; and distinct from FedAUX (AIMech:FedAuxCertaintyWeightedUnsupervisedAuxiliaryEnsembleDistillationForFederatedLearning, Sattler et al. 2021), which requires clients to access auxiliary data and train separate logistic-regression out-of-distribution certainty scorers rather than weighting client teachers purely at the server via intra-logit probability variance sigma_s^2(w_k, x) and regularizing with dissenting-client KL divergence.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 492 Fed-ET (Cho et al. 2022): y_s=0 (vs majority=1), S_div=[2, 3, 4, 5], thm1_fedet=0.4723 < thm1_unif=0.5342
```
