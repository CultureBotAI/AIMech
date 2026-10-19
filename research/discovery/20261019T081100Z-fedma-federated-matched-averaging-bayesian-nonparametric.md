# Discovery Report: Round 408 — FedMA (Federated Matched Averaging via Layer-Wise Bayesian Nonparametric Matching)

- **Timestamp**: `2026-10-19T08:11:00Z`
- **Selected Concept**: `AIMech:FedMaFederatedMatchedAveragingViaLayerWiseBayesianNonparametricMatching` (*FedMA (Federated Matched Averaging via Layer-Wise Bayesian Nonparametric Matching)*)
- **Record Path**: `data/curated/FedMaFederatedMatchedAveragingViaLayerWiseBayesianNonparametricMatching.yaml`
- **Primary Source**: Hongyi Wang, Mikhail Yurochkin, Yuekai Sun, Dimitris Papailiopoulos, Yasaman Khazaeni — *Federated Learning with Matched Averaging* (`https://openreview.net/forum?id=BkluqlSFDS`).

## Identity & Boundary Resolution

Distinct from coordinate-wise parameter averaging (FedAvg, FedProx) which ignores the permutation invariance of neural network hidden units and averages misaligned neurons, from single-round one-shot Probabilistic Federated Neural Matching (PFNM, which applies only to shallow fully connected networks without layer-wise freezing and retraining), and from FedDF (AIMech:FedDfEnsembleDistillationForRobustModelFusionInFederatedLearning, which fuses models in output logit space using unlabeled server data rather than matching weights layer-by-layer via Hungarian assignment).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 408 FedMA (Wang et al. 2020): perm_inv_err=0.00e+00, mse_fedma=0.00929<<mse_fedavg=43.6464, bbp_min_dist_sq=74.51>eps=1.00
```
