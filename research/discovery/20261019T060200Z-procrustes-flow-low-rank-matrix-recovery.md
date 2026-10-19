# Discovery Report: Round 305 — Procrustes Flow (Factored Gradient Descent with $U^\top U = V^\top V$ Balancing Regularization) for Low-Rank Matrix Recovery

- **Timestamp**: `2026-10-19T06:02:00Z`
- **Selected Concept**: `AIMech:ProcrustesFlowForLowRankMatrixRecovery` (*Procrustes Flow (Factored Gradient Descent with $U^\top U = V^\top V$ Balancing Regularization) for Low-Rank Matrix Recovery*)
- **Record Path**: `data/curated/ProcrustesFlowForLowRankMatrixRecovery.yaml`
- **Primary Source**: Stephen Tu, Ross Boczar, Max Simchowitz, Mahdi Soltanolkotabi, Benjamin Recht — *Low-rank Solutions of Linear Matrix Equations via Procrustes Flow* (`https://doi.org/10.48550/arXiv.1507.03566`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 699 maintained AIMech concepts. Distinct from `AIMech:ScaledGradientDescentForIllConditionedLowRankMatrixEstimation` (Tong, Ma, & Chi 2021, which replaces Euclidean gradients and the $\|U^\top U - V^\top V\|_F^2$ balancing penalty by right-preconditioned iterates $L_t(Y_t^\top Y_t)^{-1}$ to remove condition-number $\kappa$ slowdown) and `AIMech:NonconvexMatrixCompletionLandscapeWithoutSpuriousLocalMinima` (Ge, Lee, & Ma 2016, which analyzes global saddle-free geometry for matrix completion).

## Constructed Boundary & Regime Verification

```text
{
  "psd_init_procrustes_dist": 0.17141,
  "lemma54_upper_bound_sq": 0.26571,
  "lemma57_regularity_lhs": 0.14261,
  "lemma57_regularity_rhs": 0.07397,
  "psd_final_procrustes_dist": 2.4064224674853886e-07,
  "rect_init_matrix_err": 0.44346,
  "rect_final_matrix_err": 1.6027715155475733e-15,
  "rect_init_factor_imbalance": 2.07383,
  "rect_final_factor_imbalance": 1.241348629070493e-14
}
```
