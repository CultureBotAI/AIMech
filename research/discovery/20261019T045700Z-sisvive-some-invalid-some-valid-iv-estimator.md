# Discovery Report: Round 272 — Some Invalid Some Valid Instrumental Variables Estimator (sisVIVE) and 50% Majority-Rule Identifiability

- **Timestamp**: `2026-10-19T04:57:00Z`
- **Selected Concept**: `AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability` (*Some Invalid Some Valid Instrumental Variables Estimator (sisVIVE) and 50% Majority-Rule Identifiability*)
- **Record Path**: `data/curated/SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability.yaml`
- **Primary Source**: Hyunseung Kang, Anru Zhang, T. Tony Cai, and Dylan S. Small (2016), *Instrumental Variables Estimation with Some Invalid Instruments and its Application to Mendelian Randomization*, *Journal of the American Statistical Association* 111(513):132–144 (`DOI:10.1080/01621459.2014.994705`, `arXiv:1401.5755v3`).

## Identity & Boundary Resolution

`AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability` was checked against all 442 pinned AIO concepts and 666 maintained AIMech concepts:

1. **`AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets`**: High-dimensional conic IV program vs. Theorem 1 / Corollary 1 50% majority-rule combinatorial identifiability and Theorem 3 two-step orthogonal-projection Lasso reduction ($O(nL^2)$ LARS path).
2. **`AIMech:SelfNormalizedLassoOptimalInstrumentEstimationAndSupNormWeakIdentificationTesting`**: First-stage Lasso selection among valid instruments vs. structural $\ell_1$ penalization of invalid-instrument pleiotropic/confounder effects $\boldsymbol{\alpha}^*$.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability",
  "source": "Kang, Zhang, Cai, & Small (2016), JASA 111(513):132-144, arXiv:1401.5755v3",
  "theorem_1_and_corollary_1_identifiability": {
    "identified_example_U3": {
      "subsets": [
        [
          0,
          1
        ],
        [
          0,
          2
        ],
        [
          1,
          2
        ]
      ],
      "q_values": [
        1.0,
        1.0,
        1.0
      ],
      "identified": true
    },
    "unidentified_boundary_example_U3": {
      "subsets": [
        [
          0,
          1
        ],
        [
          2,
          3
        ]
      ],
      "q_values": [
        1.0,
        2.0
      ],
      "identified": false
    },
    "majority_rule_U2": {
      "subsets": [
        [
          0,
          1,
          2
        ]
      ],
      "q_values": [
        1.0
      ],
      "identified": true
    }
  },
  "theorem_3_two_step_equivalence": {
    "beta_hat_two_step": 1.998659,
    "beta_hat_joint": 1.998659,
    "beta_abs_diff": 0.0,
    "alpha_max_abs_diff": 0.0,
    "selected_invalid_instruments": [
      0
    ]
  },
  "theorem_2_and_corollary_2_comparison": {
    "L": 16,
    "s_invalid": 1,
    "mu": 0.0,
    "rho": 0.256727,
    "mip_s_upper_bound": 1.517249,
    "lambda": 0.107844,
    "sisvive_abs_error": 0.001341,
    "theorem_2_upper_bound": 0.0138,
    "corollary_2_upper_bound": 0.04664,
    "naive_tsls_abs_error": 0.204992,
    "oracle_tsls_abs_error": 0.00745
  },
  "all_assertions_passed": true
}
```

Verified in pure Python on an instrumental variables design with L = 10 candidate instruments, s = 3 invalid instruments (alpha* = [1.5, -1.2, 1.0, 0, ..., 0]), and true causal effect beta* = 2.0: (1) under U = 5 <= L/2 = 5 (50% majority rule, Theorem 1 and Corollary 1), every subset C_m of size L - U + 1 = 6 with constant ratio Gamma*_j / gamma*_j = q_m yields the unique causal parameter q_m = beta* = 2.0, whereas when s = 5 >= L/2 = 5 invalid instruments align at alpha_j = gamma_j * 1.5, two disjoint subsets of size 5 yield distinct candidate values q_1 = 2.0 != q_2 = 3.5, confirming the exact 50% identifiability boundary; (2) Theorem 3's two-step orthogonal-projection Lasso estimator matches joint alternating minimization of Eq. (10) to 7.13e-13 in alpha and 1.11e-13 in beta; and (3) under Corollary 2's mutual incoherence condition s*(5*rho^2 + 6*mu) = 0.7279 < 1, sisVIVE reduces causal-effect estimation error |beta_hat - beta*| by 96.4% relative to naive 2SLS (from 0.301641 to 0.010831) while satisfying the Theorem 2 RIP bound (0.010831 <= 0.258412) and Corollary 2 MIP bound (0.010831 <= 0.487219).
