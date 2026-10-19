# Discovery Report: Round 328 — Nyström Gram Matrix Low-Rank Approximation with Diagonal Sampling

- **Timestamp**: `2026-10-19T06:48:00Z`
- **Selected Concept**: `AIMech:NystromGramMatrixLowRankApproximationWithDiagonalSampling` (*Nyström Gram Matrix Low-Rank Approximation with Diagonal Sampling*)
- **Record Path**: `data/curated/NystromGramMatrixLowRankApproximationWithDiagonalSampling.yaml`
- **Primary Source**: Petros Drineas, Michael W. Mahoney — *On the Nyström Method for Approximating a Gram Matrix for Improved Kernel-Based Learning* (`https://www.jmlr.org/papers/v6/drineas05a.html`).

## Identity & Boundary Resolution

Distinct from classical Principal Component Analysis (`AIO:PrincipalComponentAnalysis`), which requires O(n^3) eigendecomposition of the full n x n Gram matrix G, and from oblivious random projection subspace embeddings (`AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding`). Specifically captures the Drineas & Mahoney (2005) rank-k truncated pseudoinverse Nyström estimator tilde{G}_k = C W_k^+ C^T with diagonal-squared importance sampling p_i propto G_{ii}^2, the Lemma 4 feature-space projection equivalence tilde{G}_k = X^T hat{U}_k hat{U}_k^T X, the Section 5.2 Equation 47 Schur complement identity A - tilde{A} = [[0, 0], [0, A_{22} - A_{21} A_{11}^{-1} A_{12}]], and the Theorem 3 additive spectral and Frobenius error guarantees.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 328 Nystrom Gram matrix low-rank approximation boundary checks succeeded.
```
