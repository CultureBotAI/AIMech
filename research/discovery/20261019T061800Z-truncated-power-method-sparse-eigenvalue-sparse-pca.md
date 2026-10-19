# Discovery Report: Round 313 — Truncated Power Method for Sparse Eigenvalue and Sparse PCA

- **Timestamp**: `2026-10-19T06:18:00Z`
- **Selected Concept**: `AIMech:TruncatedPowerMethodForSparseEigenvalueAndSparsePCA` (*Truncated Power Method for Sparse Eigenvalue and Sparse PCA*)
- **Record Path**: `data/curated/TruncatedPowerMethodForSparseEigenvalueAndSparsePCA.yaml`
- **Primary Source**: Xiao-Tong Yuan, Tong Zhang — *Truncated Power Method for Sparse Eigenvalue Problems* (`https://jmlr.org/papers/v14/yuan13a.html`).

## Identity & Boundary Resolution

Distinct from generic AIO:PrincipalComponentAnalysis, AIO:DimensionalityReduction, semidefinite relaxations (DSPCA), diagonal-thresholding and covariance-thresholding sparse PCA (AIMech:CovarianceThresholdingAndReducedRankSemidefiniteRelaxationForSparsePCA), and convex Fantope projection (AIMech:FantopeProjectionAndSelectionForSparsePCA). Specifically captures the Yuan-Zhang (2013) non-convex Truncated Power (TPower) method (Algorithm 1), its two-step optimality certificate x_t = Truncate(A x_t, supp(x_t)) / ||Truncate(A x_t, supp(x_t))||_2 (Proposition 1), its support-truncation perturbation bounds (Lemmas 3-4), and its geometric alignment contraction under sparse condition number control (Theorems 1-2).

## Constructed Boundary & Regime Verification

```text
{"concept": "TruncatedPowerMethodForSparseEigenvalueAndSparsePCA", "lemma3_lhs": 0.948374, "lemma3_rhs": 0.694729, "lemma4_lhs": 0.948374, "lemma4_rhs": 0.872933, "orthogonal_init_alignment": 0.0, "status": "VERIFIED", "tpower_final_alignment": 0.999993, "tpower_final_l2_error": 0.003731, "tpower_init_alignment": 0.707107}
```
