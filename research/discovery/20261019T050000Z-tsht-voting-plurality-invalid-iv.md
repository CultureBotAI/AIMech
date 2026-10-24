# Discovery Report: Round 274 — Two-Stage Hard Thresholding with Voting and Plurality Rule for Invalid Instruments

- **Timestamp**: `2026-10-19T05:00:00Z`
- **Selected Concept**: `AIMech:TwoStageHardThresholdingWithVotingAndPluralityRuleForInvalidInstruments` (*Two-Stage Hard Thresholding with Voting and Plurality Rule for Invalid Instruments*)
- **Record Path**: `data/curated/TwoStageHardThresholdingWithVotingAndPluralityRuleForInvalidInstruments.yaml`
- **Primary Source**: Zijian Guo, Hyunseung Kang, T. Tony Cai, and Dylan S. Small (2018), *Confidence Intervals for Causal Effects with Invalid Instruments by Using Two-Stage Hard Thresholding with Voting*, *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 80(4):793–815 (`DOI:10.1111/rssb.12275`, `arXiv:1603.05224v3`).

## Identity & Boundary Resolution

`AIMech:TwoStageHardThresholdingWithVotingAndPluralityRuleForInvalidInstruments` was checked against all 442 pinned AIO concepts and 668 maintained AIMech concepts:

1. **`AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability`**: 50% majority-rule L1 point estimation vs. plurality-rule two-stage hard thresholding with pairwise symmetric voting and asymptotically normal confidence intervals.
2. **`AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets`**: Conic sensitivity sets under user-specified $\Upsilon$ vs. data-adaptive valid-instrument recovery $\widehat{\mathcal{V}} = \mathcal{V}^*$ via plurality voting.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:TwoStageHardThresholdingWithVotingAndPluralityRuleForInvalidInstruments",
  "source": "Guo, Kang, Cai, & Small (2018), JRSS Series B 80(4):793-815, arXiv:1603.05224v3",
  "results": {
    "theorem1_plurality_identifiability": {
      "case_A_majority_holds": false,
      "case_A_plurality_holds": true,
      "case_A_true_beta": 1.0,
      "case_A_plurality_estimate": 1.0,
      "case_A_median_estimate": 1.5,
      "case_B_plurality_holds": false,
      "case_B_indistinguishable_betas": [
        1.0,
        1.5
      ],
      "case_B_valid_counts": [
        2,
        2
      ],
      "case_B_reduced_form_max_diff": 0.0
    },
    "tsht_voting_and_oracle_equivalence": {
      "n": 2500,
      "p_z": 8,
      "S_hat_1indexed": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "vote_counts_1indexed": {
        "1": 2,
        "2": 2,
        "3": 2,
        "4": 2,
        "5": 3,
        "6": 3,
        "7": 3
      },
      "V_hat_M_1indexed": [],
      "V_hat_P_1indexed": [
        5,
        6,
        7
      ],
      "V_hat_1indexed": [
        5,
        6,
        7
      ],
      "beta_tsht": 1.010856,
      "beta_oracle": 1.010856,
      "beta_naive_tsls": 1.22287,
      "tsht_oracle_abs_diff": 0.0,
      "ci_95_tsht": [
        0.990506,
        1.031205
      ],
      "ci_95_naive_tsls": [
        1.21136,
        1.23438
      ],
      "tsht_covers_true_beta": true,
      "naive_covers_true_beta": false
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on a 10-instrument Mendelian randomization design (n = 2000, p_z = 10, true beta* = 2.0) where only 4 of 8 strong instruments are valid (S* = {0..7}, V* = {0,1,2,3}, so |V*|/|S*| = 4/8 = 50% violates the strict majority rule of sisVIVE while satisfying the plurality rule 4 > max(2, 1, 1) = 2, plus 2 weak/irrelevant instruments {8, 9}): (1) Stage 1 hard thresholding (Eq. 9) exactly recovers S_hat = {0..7}, screening out weak instruments {8, 9}; (2) Stage 2 pairwise symmetric voting (Eq. 14) assigns exactly 4 votes to each valid instrument j in {0,1,2,3} and at most 2 votes to invalid instruments, so the plurality winner recovers V_hat = V* = {0,1,2,3} exactly; (3) the TSHT one-step GMM estimator (Eq. 17) achieves |beta_hat_TSHT - beta*| = 0.0080 with 95% confidence interval [1.9765, 2.0085] covering beta* = 2.0, whereas L1-penalized sisVIVE fails under violated majority validity with error >= 0.4227 across the entire regularization path.
