# Discovery Report: Round 489 — FedRolex (Model-Heterogeneous Federated Learning with Rolling Sub-Model Extraction)

- **Timestamp**: `2026-10-19T09:32:00Z`
- **Selected Concept**: `AIMech:FedRolexModelHeterogeneousFederatedLearningWithRollingSubModelExtraction` (*FedRolex (Model-Heterogeneous Federated Learning with Rolling Sub-Model Extraction)*)
- **Record Path**: `data/curated/FedRolexModelHeterogeneousFederatedLearningWithRollingSubModelExtraction.yaml`
- **Primary Source**: Samiul Alam, Luyang Liu, Ming Yan, Mi Zhang — *FedRolex: Model-Heterogeneous Federated Learning with Rolling Sub-Model Extraction* (`https://arxiv.org/abs/2212.01548`).

## Identity & Boundary Resolution

Distinct from HeteroFL (AIMech:HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning, Diao et al. 2021) and FjORD (AIMech:FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning, Horvath et al. 2021), which use static prefix sub-model extraction S_{n,i}^{(j)} = {0, 1, ..., floor(beta_n K_i) - 1} independent of round j (Equation 6) so that the global server model cannot exceed the largest client model and higher-index parameters are never trained on low-capacity clients' data; and distinct from Federated Dropout (Caldas et al. 2018), which extracts random node subsets each round (Equation 5) and requires O(I log I + I(m-1) log log I) expected rounds rather than m I rounds to update all I sub-models at least m times.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 489 FedRolex (Alam et al. 2022): uniform_node_visits=18 (var=0 vs static_upper=[0, 0, 0, 0]), Lemma1_E[N]=21.74 > I=8, Lemma2_E[N]=34.88 > m*I=16, selective_agg_err=0.0
```
