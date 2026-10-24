# Discovery Report: Round 329 — Subsampled Randomized Hadamard Transform Subspace Embedding

- **Timestamp**: `2026-10-19T06:50:00Z`
- **Selected Concept**: `AIMech:SubsampledRandomizedHadamardTransformSubspaceEmbedding` (*Subsampled Randomized Hadamard Transform Subspace Embedding*)
- **Record Path**: `data/curated/SubsampledRandomizedHadamardTransformSubspaceEmbedding.yaml`
- **Primary Source**: Joel A. Tropp — *Improved Analysis of the Subsampled Randomized Hadamard Transform* (`https://api.crossref.org/works/10.1142/S1793536911000787`).

## Identity & Boundary Resolution

Distinct from classical Principal Component Analysis (`AIO:PrincipalComponentAnalysis`), data-dependent Nyström column sampling (`AIMech:NystromGramMatrixLowRankApproximationWithDiagonalSampling`), and deterministic streaming Frequent-Directions sketching (`AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching`). Specifically captures the structured operator Phi = sqrt(n/l) R H D and Tropp's (2011) two-lemma decoupling: Lemma 3.3 Rademacher-Hadamard row-norm flattening via convex concentration and Lemma 3.4 / Theorem 3.1 matrix Chernoff singular-value preservation for row sampling without replacement at optimal dimension l = O((k + log n) log k).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 329 Subsampled Randomized Hadamard Transform (SRHT) boundary checks succeeded.
```
