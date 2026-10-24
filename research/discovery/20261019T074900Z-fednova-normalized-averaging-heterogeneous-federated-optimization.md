# Discovery Report: Round 386 — FedNova Normalized Averaging for Heterogeneous Federated Optimization

- **Timestamp**: `2026-10-19T07:49:00Z`
- **Selected Concept**: `AIMech:FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization` (*FedNova Normalized Averaging for Heterogeneous Federated Optimization*)
- **Record Path**: `data/curated/FedNovaNormalizedAveragingForHeterogeneousFederatedOptimization.yaml`
- **Primary Source**: Jianyu Wang, Qinghua Liu, Hao Liang, Gauri Joshi, H. Vincent Poor — *Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization* (`https://proceedings.neurips.cc/paper/2020/hash/564127c03caab942e503ee6f810f54fd-Abstract.html`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalHeteratedOptimization / AIMech:FedProxProximalHeterogeneousFederatedOptimization, which adds a proximal penalty (mu/2)||x - x^{(t,0)}||^2 to local objectives but still suffers from surrogate objective inconsistency w_i proportional to p_i ||a_i||_1 when tau_i varies across clients, as proven in Wang et al. 2020 Section 4.3), from SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which transmits control variate shifts c_i and requires equal local step counts), and from Local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent). No pinned AIO class covers FedNova or objective-inconsistency-eliminating normalized federated averaging.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 386 FedNova (Wang et al. 2020): chi2_pw=1.9167, fa_err=0.5504 (surrogate_diff=6.1568e-04), fednova_errs(sgd=3.55e-03, prox=3.55e-03, mom=6.18e-03)
```
