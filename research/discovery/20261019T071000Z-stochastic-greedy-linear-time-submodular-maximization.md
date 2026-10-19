# Discovery Report: Round 348 — Stochastic-Greedy Linear-Time Monotone Submodular Maximization

- **Timestamp**: `2026-10-19T07:10:00Z`
- **Selected Concept**: `AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization` (*Stochastic-Greedy Linear-Time Monotone Submodular Maximization*)
- **Record Path**: `data/curated/StochasticGreedyLinearTimeMonotoneSubmodularMaximization.yaml`
- **Primary Source**: Baharan Mirzasoleiman, Ashwinkumar Badanidiyuru, Amin Karbasi, Jan Vondrak, Andreas Krause — *Lazier Than Lazy Greedy* (`https://doi.org/10.1609/aaai.v29i1.9486`).

## Identity & Boundary Resolution

Distinct from K-Determinantal Point Processes for Fixed-Size Subset Selection (`AIMech:KDeterminantalPointProcessesForFixedSizeSubsetSelection`), which samples fixed-size subsets with probability proportional to principal minor determinants det(L_Y) using elementary symmetric polynomials rather than maximizing general monotone submodular set functions, and from classical Greedy (Nemhauser, Wolsey, & Fisher 1978) or Lazy-Greedy (Minoux 1978), whose oracle complexity scales with k as O(n k). Specifically captures the per-step random candidate sub-sampling s = (n/k) log(1/epsilon) (Algorithm 1), the concavity-based overlap probability bound Pr[R cap (A^* \ A) != empty] >= (1 - epsilon)|A^* \ A|/k (Lemma 2), the cardinality-independent O(n log(1/epsilon)) complexity and (1 - 1/e - epsilon) approximation guarantee (Theorem 1), and its combination with lazy upper-bound evaluations.

## Constructed Boundary & Regime Verification

```text
[PASS] Stochastic-Greedy boundaries verified: mean_SG=143.73>=theo=86.78 (OPT=180.0), evals=114<std_evals=345, nonmono_sum=0.0<gap=1.0
```
