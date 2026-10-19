# Discovery Report: Round 385 — FedProx Proximal Heterogeneous Federated Optimization with Variable Inexact Local Work

- **Timestamp**: `2026-10-19T07:48:00Z`
- **Selected Concept**: `AIMech:FedProxProximalHeterogeneousFederatedOptimization` (*FedProx Proximal Heterogeneous Federated Optimization with Variable Inexact Local Work*)
- **Record Path**: `data/curated/FedProxProximalHeterogeneousFederatedOptimization.yaml`
- **Primary Source**: Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, Virginia Smith — *Federated Optimization in Heterogeneous Networks* (`https://proceedings.mlsys.org/paper_files/paper/2020/hash/1f5fe83998a09396ebe6477d9475ba0c-Abstract.html`).

## Identity & Boundary Resolution

Distinct from control-variate drift correction (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which requires persistent client state c_i and 2x communication rather than a stateless proximal surrogate), from uniform-epoch periodic local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent, which corresponds to mu = 0 with fixed homogeneous local steps), and from centralized proximal stochastic gradient methods (AIMech:SpiderBoostAndProximalSpiderBoostWithMomentumForNonconvexOptimization). Narrower than AIO:FederatedLearning, which covers general federated learning without specifying proximal local surrogates or gamma_k^t-inexact partial-work aggregation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 385 FedProx Proximal Heterogeneous Federated Optimization boundaries verified.
```
