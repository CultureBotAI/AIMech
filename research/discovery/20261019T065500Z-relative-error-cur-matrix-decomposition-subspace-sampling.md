# Discovery Report: Round 332 — Relative-Error CUR Matrix Decomposition via Subspace Leverage Sampling

- **Timestamp**: `2026-10-19T06:55:00Z`
- **Selected Concept**: `AIMech:RelativeErrorCURMatrixDecompositionViaSubspaceLeverageSampling` (*Relative-Error CUR Matrix Decomposition via Subspace Leverage Sampling*)
- **Record Path**: `data/curated/RelativeErrorCURMatrixDecompositionViaSubspaceLeverageSampling.yaml`
- **Primary Source**: Petros Drineas, Michael W. Mahoney, S. Muthukrishnan — *Relative-Error CUR Matrix Decompositions* (`https://doi.org/10.1137/07070471X`).

## Identity & Boundary Resolution

Distinct from Nyström Gram Matrix Low-Rank Approximation with Diagonal Sampling (`AIMech:NystromGramMatrixLowRankApproximationWithDiagonalSampling`), which applies only to symmetric positive semidefinite Gram matrices G and achieves additive error bounds proportional to sum_i G_{ii}^2, and from Principal Component Analysis (`AIO:PrincipalComponentAnalysis`), which represents A_k in dense orthogonal eigenbases that destroy sparsity and interpretability of original rows and columns. Specifically captures the Drineas-Mahoney-Muthukrishnan (2008) subspace leverage sampling probabilities p_j = (1/k)||(V_{A,k})_{(j)}||_2^2, the Lemma 1 pseudoinverse reduction to generalized l_2 regression, and the relative-error CX (Theorem 1) and CUR (Theorem 2) algorithms.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 332 Relative-Error CUR Matrix Decomposition: prob_sum_err=0.00e+00, lemma1_eq27_err=2.70e-16, lemma1_eq26_err=1.11e-16, cx_rel_err=0.5300, cur_rel_err=0.7809, naive_colnorm_rel_err=21.20, exact_rank_k_err=6.04e-15
```
