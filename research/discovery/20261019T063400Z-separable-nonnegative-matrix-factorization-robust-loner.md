# Discovery Report: Round 321 — Separable Nonnegative Matrix Factorization and Robust-Loner Recovery

- **Timestamp**: `2026-10-19T06:34:00Z`
- **Selected Concept**: `AIMech:SeparableNonnegativeMatrixFactorizationAndRobustLonerRecovery` (*Separable Nonnegative Matrix Factorization and Robust-Loner Recovery*)
- **Record Path**: `data/curated/SeparableNonnegativeMatrixFactorizationAndRobustLonerRecovery.yaml`
- **Primary Source**: Sanjeev Arora, Rong Ge, Ravindran Kannan, Ankur Moitra — *Computing a Nonnegative Matrix Factorization -- Provably* (`https://doi.org/10.1137/130913869`).

## Identity & Boundary Resolution

Distinct from heuristic multiplicative update rules for NMF (`AIO:NonnegativeMatrixFactorization`) and FastAnchorWords / RecoverL2 word-co-occurrence topic modeling (AIMech:AnchorWordsAndRecoverL2TopicWordMatrixFactorization). Specifically captures the Arora-Ge-Kannan-Moitra (2012/2016) formalization of Separable NMF (Definition 5.1), the exact simplicial 'Loner' LP algorithm (Theorem 5.4 and Claim 5.5), the alpha-robust simplicial condition (Definition 5.6), the noisy Robust-Loners algorithm and error bound 10 epsilon/alpha + 7 epsilon (Theorem 5.7 and Claims 5.8-5.10), and the fixed-inner-dimension exact NMF algebraic decidability algorithm in time (nm)^{O(r^2 2^r)} (Theorem 4.1).

## Constructed Boundary & Regime Verification

```text
{"claim58_max_convex_hull_l1_err": 0.014, "concept": "SeparableNonnegativeMatrixFactorizationAndRobustLonerRecovery", "exact_loner_indices": [0, 1, 2], "noisy_robust_loner_indices": [0, 1, 2], "nonseparable_min_vertex_l1_gap": 0.6, "robust_simplicial_alpha": 1.2, "status": "VERIFIED", "theorem57_upper_bound": 0.153333}
```
