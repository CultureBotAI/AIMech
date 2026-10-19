# Discovery Report: Round 288 — Rank Centrality Iterative Random-Walk Spectral Ranking from Pairwise Comparisons

- **Timestamp**: `2026-10-19T05:28:00Z`
- **Selected Concept**: `AIMech:RankCentralityIterativeRandomWalkSpectralRankingFromPairwiseComparisons` (*Rank Centrality Iterative Random-Walk Spectral Ranking from Pairwise Comparisons*)
- **Record Path**: `data/curated/RankCentralityIterativeRandomWalkSpectralRankingFromPairwiseComparisons.yaml`
- **Primary Source**: Sahand Negahban, Sewoong Oh, Devavrat Shah — *Rank Centrality: Ranking from Pairwise Comparisons* (`https://doi.org/10.1287/opre.2016.1534`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 682 maintained AIMech concepts. Distinct from `AIMech:TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis` (Chen, Fan, Ma, & Wang 2019, which introduces leave-one-out entrywise $\ell_\infty$ perturbation analysis for top-$K$ identification on Erdős–Rényi graphs, whereas Negahban, Oh, & Shah 2017 formulate the Rank Centrality random-walk algorithm, the Beta$(\varepsilon,\varepsilon)$-regularized transition matrix, the general-graph $L^2(\tilde{\pi})$ Dirichlet-form spectral gap comparison Theorem 1 / Lemma 6, the weighted pairwise ranking loss $D_w(\sigma)$ bound Lemma 1, and the simplex packing minimax lower bound Theorem 3).

## Constructed Boundary & Regime Verification

```text
{
  "n_items": 16,
  "dynamic_range_b": 4.0,
  "d_min": 8.0,
  "d_max": 11.0,
  "population_rc_rel_l2_err": 2.638184852004332e-12,
  "population_mc3_irregular_graph_bias": 0.086575,
  "laplacian_spectral_gap_xi": 0.520681,
  "p_tilde_spectral_gap": 0.173661,
  "eq26_dirichlet_comparison_lower_bound": 0.023667,
  "mean_rel_err_k25": 0.145876,
  "mean_rel_err_k400": 0.032831,
  "lemma1_dw_bound_verified": true
}
```
