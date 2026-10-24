# Discovery Report: Round 267 — Group Restricted Eigenvalue Oracle Inequalities and Multi-Task Group Lasso Minimax Optimality

- **Timestamp**: `2026-10-19T04:30:00Z`
- **Selected Concept**: `AIMech:GroupRestrictedEigenvalueOracleInequalitiesAndMultiTaskGroupLassoMinimaxOptimality` (*Group Restricted Eigenvalue Oracle Inequalities and Multi-Task Group Lasso Minimax Optimality*)
- **Record Path**: `data/curated/GroupRestrictedEigenvalueOracleInequalitiesAndMultiTaskGroupLassoMinimaxOptimality.yaml`
- **Primary Source**: Karim Lounici, Massimiliano Pontil, Sara van de Geer, and Alexandre B. Tsybakov (2011), *Oracle inequalities and optimal inference under group sparsity*, *The Annals of Statistics* 39(4):2164–2204 (`DOI:10.1214/11-AOS896`, `arXiv:1007.1771v3`).

## Identity & Boundary Resolution

`AIMech:GroupRestrictedEigenvalueOracleInequalitiesAndMultiTaskGroupLassoMinimaxOptimality` was checked against all 442 pinned AIO concepts and 661 maintained AIMech concepts:

1. **`AIMech:GroupLassoBlockCoordinateDescent`**: Covers the Group Lasso optimization formulation and block coordinate descent without the Group Restricted Eigenvalue condition $RE(s, \mathbf{c})$, multi-task $O(\frac{s}{N}(1 + \frac{\log M}{T}))$ minimax optimality, or block-coherence $\ell_{2,\infty}$ support recovery.
2. **`AIMech:BickelRitovTsybakovRestrictedEigenvalueConditionAndLassoDantzigOracleBounds`**: Coordinate-wise $\ell_1$ Restricted Eigenvalue oracle bounds for standard Lasso and Dantzig selector rather than weighted block-$\ell_{2,1}$ cones and multi-task chi-square concentration.

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:GroupRestrictedEigenvalueOracleInequalitiesAndMultiTaskGroupLassoMinimaxOptimality",
  "source": "Lounici, Pontil, van de Geer, & Tsybakov (2011), Ann. Statist. 39(4):2164-2204",
  "multitask_and_kkt": {
    "tasks_grid": [
      1,
      4,
      16
    ],
    "kkt_max_violation": 3e-12,
    "lemma31_max_ratio": 0.788078,
    "gl_per_task_l2_errors": [
      0.170883,
      0.075674,
      0.024521
    ],
    "lasso_per_task_l2_errors": [
      0.160181,
      0.332146,
      0.260801
    ],
    "theoretical_gl_rates": [
      0.045942,
      0.013829,
      0.005801
    ],
    "theoretical_lasso_rates": [
      0.042817,
      0.053648,
      0.064478
    ]
  },
  "block_coherence_and_support_recovery": {
    "block_coherence_theta": 0.0,
    "coherence_threshold_1_over_7s": 0.071429,
    "a0_constant": 1.5,
    "max_group_l2_error": 0.099363,
    "theorem51_bound": 0.135,
    "recovered_support": [
      0,
      1
    ]
  },
  "lemma91_maximal_moment_inequality": {
    "m=1": {
      "lhs": 10.3011,
      "rhs": 32.914,
      "ratio_lhs_over_rhs": 0.312969
    },
    "m=2": {
      "lhs": 111.7663,
      "rhs": 1402.335,
      "ratio_lhs_over_rhs": 0.0797
    },
    "m=4": {
      "lhs": 15236.478,
      "rhs": 4200729.3352,
      "ratio_lhs_over_rhs": 0.003627
    }
  },
  "all_assertions_passed": true
}
```

Verified in pure Python across three regimes: (1) across multi-task dimensions T in {1, 4, 16} (N=24, M=12, s=2), the Group Lasso satisfies Proposition 2.1 KKT conditions to 3e-12, obeys Lemma 3.1's block-l_{2,1} cone bound ||Delta_{S^c}||_{2,1} <= 3 ||Delta_S||_{2,1} (max ratio 0.788078 <= 3.0), and reduces per-task l_2 error monotonically from 0.170883 (T=1) to 0.075674 (T=4) and 0.024521 (T=16), outperforming separate-task LASSO by 10.6x at T=16 (0.024521 vs 0.260801); (2) under Assumption 5.1 block coherence theta = 0.0 <= 1/(7s) = 0.071429 (a_0 = 1.5), the uniform group-l_{2,inf} error 0.099363 is strictly below Theorem 5.1's bound a_0*lambda*sqrt(T) = 0.135, and hard thresholding at a_0*lambda*sqrt(T) recovers the exact group support [0, 1]; and (3) Lemma 9.1's subgaussian maximal moment bound holds across m in {1, 2, 4} (ratios 0.312969, 0.0797, 0.003627 <= 1.0).
