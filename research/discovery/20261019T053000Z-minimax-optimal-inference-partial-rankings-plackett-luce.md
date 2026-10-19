# Discovery Report: Round 289 — Minimax-Optimal Inference and Rank-Breaking from Plackett-Luce Partial Rankings

- **Timestamp**: `2026-10-19T05:30:00Z`
- **Selected Concept**: `AIMech:MinimaxOptimalInferenceAndRankBreakingFromPlackettLucePartialRankings` (*Minimax-Optimal Inference and Rank-Breaking from Plackett-Luce Partial Rankings*)
- **Record Path**: `data/curated/MinimaxOptimalInferenceAndRankBreakingFromPlackettLucePartialRankings.yaml`
- **Primary Source**: Bruce Hajek, Sewoong Oh, Jiaming Xu — *Minimax-optimal Inference from Partial Rankings* (`https://arxiv.org/abs/1406.5638`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 683 maintained AIMech concepts. Distinct from `AIMech:RankCentralityIterativeRandomWalkSpectralRankingFromPairwiseComparisons` (Negahban, Oh, & Shah 2017, which analyzes spectral random-walk aggregation of pairwise comparisons $k=2$) and from `AIMech:TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis` (Chen, Fan, Ma, & Wang 2019, which analyzes entrywise $\ell_\infty$ top-$K$ recovery from pairwise comparisons rather than $k_j$-way Plackett–Luce partial rankings, Gumbel-utility van Trees oracle lower bounds, and dependent Full Rank-Breaking composite likelihoods).

## Constructed Boundary & Regime Verification

```text
{
  "van_trees_and_gumbel": {
    "p0_integral": 1.0,
    "I_p0_numerical": 9.8696044,
    "pi_squared": 9.8696044,
    "I_gumbel_numerical": 1.0
  },
  "fisher_at_zero_and_claim1": {
    "fisher_at_zero_identity_max_err": 5.551115123125783e-17,
    "claim1_extremal_lambda2": 0.04476686,
    "claim1_formula_lambda2": 0.04476686,
    "claim1_lower_bound_1_over_r_e2b": 0.03364942
  },
  "pl_mle_and_rank_breaking": {
    "m_120": {
      "m": 120,
      "k": 4,
      "oracle_lb_l2": 0.35502,
      "cramer_rao_lb_l2": 0.72532,
      "err_ml_l2": 0.4171,
      "err_fb_l2": 0.44701,
      "err_ib_l2": 0.75908
    },
    "m_600": {
      "m": 600,
      "k": 4,
      "oracle_lb_l2": 0.15877,
      "cramer_rao_lb_l2": 0.32437,
      "err_ml_l2": 0.24309,
      "err_fb_l2": 0.28661,
      "err_ib_l2": 0.45073
    }
  },
  "all_assertions_passed": true
}
```
