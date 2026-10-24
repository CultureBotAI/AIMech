# Discovery Report: Round 579 — Rennala SGD and Malenia SGD

- **Timestamp**: `2026-10-19T11:02:00Z`
- **Selected Concept**: `AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization` (*Rennala SGD and Malenia SGD*)
- **Record Path**: `data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml`
- **Primary Source**: Alexander Tyurin, Peter Richtarik — *Optimal Time Complexities of Parallel Stochastic Optimization Methods Under a Fixed Computation Model* (`https://dblp.org/search/publ/api?q=Optimal+Time+Complexities+Parallel+Stochastic+Optimization+Tyurin+Richtarik&format=json`).

## Identity & Boundary Resolution

Distinct from classical Asynchronous SGD (which applies delayed gradients hat{nabla} f(x^{k - delta_k}) computed at stale iterates and suffers suboptimal wall-clock complexity when slow stragglers inject large delays) and from synchronous Minibatch SGD (which waits for the slowest worker tau_n at every batch). Rennala SGD and Malenia SGD run workers in an asynchronous loop but strictly filter for current-iterate gradients (k' = k), automatically excluding slow stragglers i > m^* in the homogeneous regime and balancing harmonic sample sizes in the heterogeneous regime.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 579 Rennala & Malenia SGD verified: t_rennala=4.80 < t_async=15.50 << t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39>=1.00
```
