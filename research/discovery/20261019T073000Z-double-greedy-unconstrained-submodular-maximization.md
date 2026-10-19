# Discovery Report: Round 367 — Double Greedy Algorithm for Unconstrained Non-Monotone Submodular Maximization

- **Timestamp**: `2026-10-19T07:30:00Z`
- **Selected Concept**: `AIMech:DoubleGreedyUnconstrainedSubmodularMaximization` (*Double Greedy Algorithm for Unconstrained Non-Monotone Submodular Maximization*)
- **Record Path**: `data/curated/DoubleGreedyUnconstrainedSubmodularMaximization.yaml`
- **Primary Source**: Niv Buchbinder, Moran Feldman, Joseph (Seffi) Naor, Roy Schwartz — *A Tight Linear Time (1/2)-Approximation for Unconstrained Submodular Maximization* (`https://doi.org/10.1137/130929205`).

## Identity & Boundary Resolution

Distinct from AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization (Round 348) and AIMech:ContinuousGreedyAndMultilinearExtensionForMatroidSubmodularMaximization (Round 349), which require monotone submodular objectives and only grow a single solution from emptyset (failing on non-monotone objectives where elements can have negative marginal contributions to supersets), whereas Double Greedy maintains both a growing lower bound X_i and a shrinking upper bound Y_i to exploit the complement symmetry f_bar(S) = f(N \ S) and achieve the optimal 1/2 approximation for unconstrained non-monotone submodular maximization.

## Constructed Boundary & Regime Verification

```text
[PASS] Double Greedy USM boundaries verified: OPT=5.900, Det=2.000 (ratio=0.3390), Rand=4.4293 (ratio=0.7507 >= 0.5), Multilinear=4.8281 (ratio=0.8183 >= 0.5)
```
