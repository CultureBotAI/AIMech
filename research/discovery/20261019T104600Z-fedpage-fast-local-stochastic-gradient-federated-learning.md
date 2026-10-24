# Discovery Report: Round 563 — FedPAGE Probabilistic Local Stochastic Gradient Method for Federated Learning

- **Timestamp**: `2026-10-19T10:46:00Z`
- **Selected Concept**: `AIMech:FedPageProbabilisticLocalGradientMethodForFederatedLearning` (*FedPAGE Probabilistic Local Stochastic Gradient Method for Federated Learning*)
- **Record Path**: `data/curated/FedPageProbabilisticLocalGradientMethodForFederatedLearning.yaml`
- **Primary Source**: Haoyu Zhao, Zhize Li, Peter Richtarik — *FedPAGE: A Fast Local Stochastic Gradient Method for Communication-Efficient Federated Learning* (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2108.04755`).

## Identity & Boundary Resolution

Distinct from single-step centralized PAGE (Li et al., ICML 2021; recovered when K = 1), SCAFFOLD (Karimireddy et al., ICML 2020; which requires O(N^{2/3} L / (S^{2/3} eps^2)) nonconvex and O(N L / (S eps)) convex rounds and maintains per-client states across rounds), and FedAvg / Local-SGD. FedPAGE (Zhao, Li, & Richtarik, 2021, arXiv:2108.04755) is stateless on clients and improves SCAFFOLD's communication complexity by factors N^{1/6} S^{1/3} (nonconvex) and N^{1/4} (convex) for S <= sqrt(N).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 563 FedPAGE verified: geom_sum=6.483<=3K=12, grad_fp=2.220e-16 << grad_fa=1.590e+00
```
