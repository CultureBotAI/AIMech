# Discovery Report: Round 330 — Frequent-Directions Deterministic Streaming Matrix Sketching

- **Timestamp**: `2026-10-19T06:52:00Z`
- **Selected Concept**: `AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching` (*Frequent-Directions Deterministic Streaming Matrix Sketching*)
- **Record Path**: `data/curated/FrequentDirectionsDeterministicStreamingMatrixSketching.yaml`
- **Primary Source**: Edo Liberty — *Simple and Deterministic Matrix Sketching* (`https://api.crossref.org/works/10.1145/2487575.2487623`).

## Identity & Boundary Resolution

Distinct from batch Principal Component Analysis (`AIO:PrincipalComponentAnalysis`), which requires storing A or A^T A in O(n m) or O(m^2) memory, and from randomized oblivious subspace embeddings (`AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding`) or randomized column sampling (`AIMech:NystromGramMatrixLowRankApproximationWithDiagonalSampling`). Specifically captures Liberty's (2013) deterministic SVD singular-value shrinkage rule bar{Sigma} = sqrt(Sigma^2 - I_l delta_i) (Algorithms 1 and 2), its exact reduction to the Misra-Gries / Space-Saving heavy-hitters counter algorithm on orthogonal basis streams (Section 3, Theorem 3.1), and the deterministic Loewner positive semidefinite covariance bound 0 <= A^T A - B^T B <= (2 / l)(||A||_F^2 - ||B||_F^2) I_m (Claims 1-2, Theorems 4.1-4.2).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 330 Frequent-Directions deterministic matrix sketching boundary checks succeeded.
```
