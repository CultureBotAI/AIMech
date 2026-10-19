# Discovery Report: Round 349 — Continuous Greedy and Multilinear Extension for Matroid-Constrained Monotone Submodular Maximization

- **Timestamp**: `2026-10-19T07:12:00Z`
- **Selected Concept**: `AIMech:ContinuousGreedyAndMultilinearExtensionForMatroidSubmodularMaximization` (*Continuous Greedy and Multilinear Extension for Matroid-Constrained Monotone Submodular Maximization*)
- **Record Path**: `data/curated/ContinuousGreedyAndMultilinearExtensionForMatroidSubmodularMaximization.yaml`
- **Primary Source**: Gruia Calinescu, Chandra Chekuri, Martin Pal, Jan Vondrak — *Maximizing a Monotone Submodular Function Subject to a Matroid Constraint* (`https://api.crossref.org/works/10.1137/080733991`).

## Identity & Boundary Resolution

Distinct from Stochastic-Greedy Linear-Time Monotone Submodular Maximization (`AIMech:StochasticGreedyLinearTimeMonotoneSubmodularMaximization`), which accelerates discrete greedy under a simple cardinality constraint |S| <= k via random candidate subset sampling of size (n/k) log(1/epsilon) and still suffers a 1/2 approximation barrier on general matroids, and from Away-Step and Pairwise Frank-Wolfe Linear Convergence on Polytopes (`AIMech:AwayStepAndPairwiseFrankWolfeLinearConvergenceOnPolytopes`), which minimizes strongly convex smooth objectives over polytopes rather than maximizing the non-concave multilinear extension F(y) of a monotone submodular set function via upward-monotone direction dominance and pipage rounding.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 349 Continuous Greedy (Calinescu et al. 2011): swap_curv=4.0000 (err=2.43e-08), min_lemma31_gap=1.00e-04, discrete_greedy_ratio=0.5000, cg_ratio=0.9995 >= 1-1/e=0.6321, pipage_expected=3.9980 >= F(y1)=3.9980
```
