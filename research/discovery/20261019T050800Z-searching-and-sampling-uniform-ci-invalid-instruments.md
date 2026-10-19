# Discovery Report: Round 278 — Searching and Sampling Uniform Confidence Intervals for Invalid Instruments

- **Timestamp**: `2026-10-19T05:08:00Z`
- **Selected Concept**: `AIMech:SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments` (*Searching and Sampling Uniform Confidence Intervals for Invalid Instruments*)
- **Record Path**: `data/curated/SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments.yaml`
- **Primary Source**: Zijian Guo (2023), *Causal Inference with Invalid Instruments: Post-selection Problems and a Solution Using Searching and Sampling*, *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 85(3):959–985 (`DOI:10.1093/jrsssb/qkad049`, `arXiv:2104.06911v5`).

## Identity & Boundary Resolution

`AIMech:SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments` was checked against all 442 pinned AIO concepts and 672 maintained AIMech concepts:

1. **`AIMech:TwoStageHardThresholdingWithVotingAndPluralityRuleForInvalidInstruments`**: Pointwise oracle selection $\widehat{\mathcal{V}} = \mathcal{V}^*$ under well-separated invalidity vs. uniform Searching and Sampling CIs robust to locally invalid instruments $0 < |\pi_j^*/\gamma_j^*| < s_j(n)$.
2. **`AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability`**: Majority-rule $\ell_1$ point estimation vs. uniform Searching and Sampling confidence intervals under finite-sample majority and plurality rules.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:SearchingAndSamplingUniformConfidenceIntervalsForInvalidInstruments",
  "source": "Zijian Guo (2023), JRSS Series B 85(3):959-985, DOI:10.1093/jrsssb/qkad049, arXiv:2104.06911v5",
  "results": {
    "n": 800,
    "pz": 10,
    "beta_true": 1.0,
    "tau_locally_invalid": 0.25,
    "separation_level_s_j_n": 0.517092,
    "V_hat_TSHT": [
      0,
      1,
      2,
      3,
      4,
      5
    ],
    "naive_tsht_point_estimate": 1.06919,
    "naive_tsht_ci_95": [
      1.012067,
      1.126313
    ],
    "naive_tsht_covers": false,
    "searching_ci_95": [
      0.801433,
      1.163823
    ],
    "searching_ci_length": 0.36239,
    "searching_ci_covers": true,
    "proposition_1_min_resampling_error": 0.39322,
    "union_bound_z_crit": 2.638257,
    "selected_lambda_shrinkage": 0.231471,
    "non_empty_sampled_proportion": 0.125,
    "sampling_ci_95": [
      0.91015,
      1.073226
    ],
    "sampling_ci_length": 0.163075,
    "sampling_ci_covers": true
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on Setting S2 of Guo (2023, Section 3 Example 1 / Section 7, n = 800, p_z = 10, beta* = 1.0, 4 valid IVs {0,1,2,3}, 2 locally invalid IVs {4,5} with tau = 0.25 < s_j(n) = 0.5171, and 4 strongly invalid IVs {6,7,8,9}): (1) the expanded symmetric-voting initial set V_hat^TSHT (Eq. 34) equals {0, 1, 2, 3, 4, 5}, satisfying Lemma 1's sandwich condition V subset V_hat^TSHT subset V union I(0, s(n)) with |V| = 4 > |V_hat^TSHT|/2 = 3; (2) naive post-selection TSHT point estimation (1.0692) and 95% CI [1.0121, 1.1263] fail to cover beta* = 1.0 due to the unseparated locally invalid IVs {4, 5}; and (3) the Searching CI [0.8014, 1.1638] (length 0.3624) and Sampling CI [0.9102, 1.0732] (length 0.1631, using Remark 2's data-dependent lambda = 0.2315 with 12.5% non-empty resamples) both cover beta* = 1.0 while Sampling cuts CI length by 55.0%.
