# Discovery Report: Round 405 — Iterative Federated Clustering Algorithm (IFCA)

- **Timestamp**: `2026-10-19T08:08:00Z`
- **Selected Concept**: `AIMech:IfcaIterativeFederatedClusteringAlgorithm` (*Iterative Federated Clustering Algorithm (IFCA)*)
- **Record Path**: `data/curated/IfcaIterativeFederatedClusteringAlgorithm.yaml`
- **Primary Source**: Avishek Ghosh, Jichan Chung, Dong Yin, Kannan Ramchandran — *An Efficient Framework for Clustered Federated Learning* (`https://proceedings.neurips.cc/paper/2020/hash/e32cc80bf07915058ce90722ee17bb71-Abstract.html`).

## Identity & Boundary Resolution

Distinct from single-global-model federated optimization (FedAvg, FedProx, SCAFFOLD) and from per-client personalized federated learning such as pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes), Per-FedAvg (AIMech:PerFedAvgModelAgnosticMetaLearningForPersonalizedFederatedLearning), Ditto (AIMech:DittoFairAndRobustPersonalizedFederatedMultiTaskLearning), and FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning), which maintain n distinct client models or heads rather than inferring discrete latent cluster memberships S_1,...,S_k and learning k shared cluster-level models.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 405 IFCA (Ghosh et al. 2020): init_dist=1.1595->final_dist=0.0172, misclass=0.00, fedavg_dist=2.0689
```
