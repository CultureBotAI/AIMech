# Discovery Report: Round 362 — Parallel Greedy Submodular Maximization in Logarithmic Adaptivity and Nearly-Linear Time via Poly-Logarithmic Batch Filtering

- **Timestamp**: `2026-10-19T07:25:00Z`
- **Selected Concept**: `AIMech:ParallelGreedySubmodularMaximizationInLogarithmicAdaptivityAndNearlyLinearTime` (*Parallel Greedy Submodular Maximization in Logarithmic Adaptivity and Nearly-Linear Time via Poly-Logarithmic Batch Filtering*)
- **Record Path**: `data/curated/ParallelGreedySubmodularMaximizationInLogarithmicAdaptivityAndNearlyLinearTime.yaml`
- **Primary Source**: Alina Ene, Huy L. Nguyen — *Submodular Maximization with Nearly-optimal Approximation and Adaptivity in Nearly-linear Time* (`https://api.crossref.org/works/10.1137/1.9781611975482.18`).

## Identity & Boundary Resolution

Distinct from AIMech:AmortizedFilteringForLogarithmicAdaptivitySubmodularMaximization (Round 360), which requires a polynomial number O(n * (k + log n)^2) of random set samples per adaptive round to concentrate every individual element's marginal gain to within O(OPT/k); Ene and Nguyen (2019) instead sample only poly-logarithmically many random sets m = O((ln n)^2 / epsilon^4) and bound the aggregate loss of OPT deterministically against the empirical batch average avg_i (Claim 9), reducing total oracle queries and running time to nearly-linear O(n poly(log n, 1/epsilon)). Also distinct from AIMech:RandGreeDiRandomizedDistributedSubmodularMaximization (Round 361), which is a two-round MapReduce partitioning algorithm with Omega(k) sequential adaptivity per machine.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 362 Parallel Greedy Submodular (Ene & Nguyen 2019): claim6_gap=1.6156>=0, filtered=8/8, claim9_margin=8.7354>=0, final_ratio=1.0000
```
