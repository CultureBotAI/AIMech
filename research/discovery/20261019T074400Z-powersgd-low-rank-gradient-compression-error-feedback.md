# Discovery Report: Round 381 — PowerSGD Low-Rank Subspace Iteration Gradient Compression with Error Feedback

- **Timestamp**: `2026-10-19T07:44:00Z`
- **Selected Concept**: `AIMech:PowerSgdLowRankGradientCompressionWithErrorFeedback` (*PowerSGD Low-Rank Subspace Iteration Gradient Compression with Error Feedback*)
- **Record Path**: `data/curated/PowerSgdLowRankGradientCompressionWithErrorFeedback.yaml`
- **Primary Source**: Thijs Vogels, Sai Praneeth Karimireddy, Martin Jaggi — *PowerSGD: Practical Low-Rank Gradient Compression for Distributed Optimization* (`https://papers.nips.cc/paper/2019/hash/d9fbed9da256e344c1fa46bb46c34c5f-Abstract.html`).

## Identity & Boundary Resolution

Distinct from coordinate-wise sparse or quantized gradient compressors (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression, AIMech:QsgdQuantizedStochasticGradientDescentWithEliasCoding, and AIMech:SignSgdAndMajorityVoteCompressedNonconvexOptimization, which require all_gather or hierarchical re-compression because non-linear sparse/quantized codes are not closed under addition), and from randomized SVD batch matrix sketching (AIMech:RandomizedSingularValueDecompositionViaSubspaceIteration). No pinned AIO class covers PowerSGD or linear all-reduce low-rank gradient compression with error feedback.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 381 PowerSGD Low-Rank Gradient Compression boundaries verified.
```
