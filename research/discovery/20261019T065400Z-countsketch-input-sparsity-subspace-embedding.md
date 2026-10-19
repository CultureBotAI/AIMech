# Discovery Report: Round 331 — CountSketch Input-Sparsity Subspace Embedding and Regression

- **Timestamp**: `2026-10-19T06:54:00Z`
- **Selected Concept**: `AIMech:CountSketchInputSparsitySubspaceEmbeddingAndRegression` (*CountSketch Input-Sparsity Subspace Embedding and Regression*)
- **Record Path**: `data/curated/CountSketchInputSparsitySubspaceEmbeddingAndRegression.yaml`
- **Primary Source**: Kenneth L. Clarkson, David P. Woodruff — *Low Rank Approximation and Regression in Input Sparsity Time* (`https://doi.org/10.1145/2488608.2488620`).

## Identity & Boundary Resolution

Distinct from Subsampled Randomized Hadamard Transform Subspace Embedding (`AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding`), which requires O(n d log t) dense Walsh-Hadamard butterfly operations regardless of matrix sparsity, and from Frequent Directions Deterministic Streaming Matrix Sketching (`AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching`), which uses O(n d l) deterministic SVD shrinkage. Specifically captures the Clarkson-Woodruff single-nonzero-per-column CountSketch matrix S = Phi D, the heavy/light leverage row decomposition (Lemma 2.5), and the O(nnz(A)) input-sparsity time algorithms for subspace embedding, least-squares regression, and rank-k approximation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 331 CountSketch Input-Sparsity Subspace Embedding: exp_frob_err=3.55e-15, heavy_isometry_err=0.00e+00, collision_preserved_ratio=0.00, rel_res_ratio=1.0324, precond_iter_err=7.54e-13
```
