# Discovery Report: Round 360 — Amortized-Filtering and Iterative-Filtering for Optimal Logarithmic-Adaptivity Submodular Maximization

- **Timestamp**: `2026-10-19T07:23:00Z`
- **Selected Concept**: `AIMech:AmortizedFilteringForLogarithmicAdaptivitySubmodularMaximization` (*Amortized-Filtering and Iterative-Filtering for Optimal Logarithmic-Adaptivity Submodular Maximization*)
- **Record Path**: `data/curated/AmortizedFilteringForLogarithmicAdaptivitySubmodularMaximization.yaml`
- **Primary Source**: Eric Balkanski, Aviad Rubinstein, Yaron Singer — *An Exponential Speedup in Parallel Running Time for Submodular Maximization without Loss in Approximation* (`https://api.crossref.org/works/10.1145/3188745.3188752`).

## Identity & Boundary Resolution

Distinct from AIMech:GreeDiTwoStageDistributedSubmodularMaximization (Round 359), which partitions data across MapReduce machines but runs sequential k-round greedy selection on each machine (Omega(k) adaptivity), and from AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization (Round 348), which reduces total oracle evaluations to O(n log(1/epsilon)) across k sequential rounds. Also distinct from AIMech:SieveStreamingAndSieveStreamingPlusPlusForSubmodularMaximization (Round 350), which is a single-pass streaming threshold algorithm achieving 1/2 - epsilon rather than a low-adaptivity parallel algorithm achieving 1 - 1/e - epsilon.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 360 Amortized-Filtering Submodular (Balkanski et al. 2018/2019): |X_0|=10->|X_1|=4<9.09, val_amort=40.00>=thm2_bound=17.28, amort_rounds=3<iter_rounds=4
```
