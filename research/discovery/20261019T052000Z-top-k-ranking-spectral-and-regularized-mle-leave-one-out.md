# Discovery Report: Round 284 — Top-K Ranking by Spectral Method and Regularized Maximum Likelihood via Leave-One-Out Analysis

- **Timestamp**: `2026-10-19T05:20:00Z`
- **Selected Concept**: `AIMech:TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis` (*Top-K Ranking by Spectral Method and Regularized Maximum Likelihood via Leave-One-Out Analysis*)
- **Record Path**: `data/curated/TopKRankingSpectralAndRegularizedMLEByLeaveOneOutAnalysis.yaml`
- **Primary Source**: Yuxin Chen, Jianqing Fan, Cong Ma, Kaizheng Wang — *Spectral Method and Regularized MLE Are Both Optimal for Top-K Ranking* (`https://doi.org/10.1214/18-AOS1745`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 678 maintained AIMech concepts. Distinct from `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices` (Abbe, Fan, Wang, & Zhong 2020, which analyzes symmetric low-expected-rank matrices rather than asymmetric reversible Markov chain stationary distributions $\boldsymbol{\pi}^T\mathbf{P} = \boldsymbol{\pi}^T$ and $\ell_2$-regularized BTL logistic MLE trajectories) and from `AIMech:RankCentralityIterativeRandomWalkSpectralRankingFromPairwiseComparisons` (Negahban, Oh, & Shah 2017, which bounds only the aggregate Euclidean $\ell_2$ error $\|\boldsymbol{\pi} - \boldsymbol{\pi}^*\|_2 / \|\boldsymbol{\pi}^*\|_2$, suboptimal by a factor of $\Theta(n)$ in sample complexity for top-$K$ identification compared to the entrywise $\ell_\infty$ leave-one-out bounds of Chen, Fan, Ma, & Wang 2019).

## Constructed Boundary & Regime Verification

```text
{
  "n_items": 18,
  "k_top": 5,
  "L_comparisons_per_pair": 400,
  "detailed_balance_max_err": 4.336808689942018e-19,
  "stationarity_max_err": 6.48925357893404e-13,
  "reversible_spectral_gap": 0.12934,
  "thm8_lhs_pi_star_norm": 0.020553,
  "thm8_rhs_bound": 0.042223,
  "spectral_rel_linf_err": 0.051527,
  "spectral_loo_rel_gap": 0.017409,
  "reg_mle_linf_err": 0.052787,
  "reg_mle_loo_gap": 0.015,
  "exact_top_k_recovered_spectral": true,
  "exact_top_k_recovered_reg_mle": true
}
```
