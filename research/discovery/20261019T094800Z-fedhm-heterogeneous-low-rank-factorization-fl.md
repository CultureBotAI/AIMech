# Discovery Report: Round 505 — FedHM: Efficient Federated Learning for Heterogeneous Models via Low-Rank Factorization

- **Timestamp**: `2026-10-19T09:48:00Z`
- **Selected Concept**: `AIMech:FedHmHeterogeneousFederatedLearningViaLowRankFactorization` (*FedHM: Efficient Federated Learning for Heterogeneous Models via Low-Rank Factorization*)
- **Record Path**: `data/curated/FedHmHeterogeneousFederatedLearningViaLowRankFactorization.yaml`
- **Primary Source**: Dezhong Yao, Wanning Pan, Michael J. O'Neill, Yutong Dai, Yao Wan, Hai Jin, Lichao Sun — *FedHM: Efficient Federated Learning for Heterogeneous Models via Low-rank Factorization* (`https://dblp.org/rec/journals/ai/YaoPSODWZJS25`).

## Identity & Boundary Resolution

Distinct from channel width-slimming heterogeneous FL methods such as HeteroFL (AIMech:HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning; Diao et al., ICLR 2021), FjORD (AIMech:FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning; Horvath et al., NeurIPS 2021), and FedRolex (AIMech:FedRolexModelHeterogeneousFederatedLearningWithRollingSubModelExtraction; Alam et al., NeurIPS 2022), which extract subset channels along width rather than factorizing layers via truncated SVD and recovering full matrices U V^T prior to aggregation. Distinct from FedPara (AIMech:FedParaAndPFedParaLowRankHadamardProductParameterization; Hyeon-Woo et al., ICLR 2022), which parameterizes homogeneous client layers via a Hadamard product of two low-rank matrices (W = (X_1 Y_1^T) odot (X_2 Y_2^T)) without server-side SVD redistributions across heterogeneous client ranks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 505 FedHM (Yao et al., 2021): conv_params(vanilla=589824 -> pufferfish=163840 -> fedhm=98304), alphas(tau=5)=[0.3473, 0.3304, 0.3222]
```
