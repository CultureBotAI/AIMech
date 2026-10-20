# Discovery Report: Round 522 — Byzantine-Robust Stochastic Aggregation for Heterogeneous Datasets

- **Timestamp**: `2026-10-19T10:05:00Z`
- **Selected Concept**: `AIMech:RsaByzantineRobustStochasticAggregationForHeterogeneousDatasets` (*Byzantine-Robust Stochastic Aggregation for Heterogeneous Datasets*)
- **Record Path**: `data/curated/RsaByzantineRobustStochasticAggregationForHeterogeneousDatasets.yaml`
- **Primary Source**: Liping Li, Wei Xu, Tianyi Chen, Georgios B. Giannakis, Qing Ling — *RSA: Byzantine-Robust Stochastic Aggregation Methods for Distributed Learning from Heterogeneous Datasets* (`https://dblp.org/rec/conf/aaai/LiXCGL19.json`).

## Identity & Boundary Resolution

Distinct from gradient-averaging or robust gradient-aggregation rules that assume i.i.d. worker gradients (Krum, Bulyan, Trimmed-Mean, Coordinate-Wise Median, Geometric Median / RFA), and distinct from proximal heterogeneous federated optimization without Byzantine robustness (FedProx). Specifically denotes the l_1-norm and l_p-norm Regularized Stochastic Aggregation (RSA) methods of Li, Xu, Chen, Giannakis, & Ling (AAAI 2019, Eqs. 5-11, Proposition 1, Theorems 1-4).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 522 RSA (Li et al. 2019): lambda_0=2.258, benign_opt_gap=0.0284, err_rsa_byz=1.3699 << err_mean_byz=318.7088
```
