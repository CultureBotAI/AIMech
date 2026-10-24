# Discovery Report: Round 422 — Qsparse-local-SGD (Distributed SGD with Quantization, Sparsification, and Local Computations)

- **Timestamp**: `2026-10-19T08:25:00Z`
- **Selected Concept**: `AIMech:QsparseLocalSgdQuantizationSparsificationAndLocalComputation` (*Qsparse-local-SGD (Distributed SGD with Quantization, Sparsification, and Local Computations)*)
- **Record Path**: `data/curated/QsparseLocalSgdQuantizationSparsificationAndLocalComputation.yaml`
- **Primary Source**: Debopam Basu, Deepesh Data, Can Karakus, Suhas Diggavi — *Qsparse-local-SGD: Distributed SGD with Quantization, Sparsification, and Local Computations* (`https://papers.nips.cc/paper/2019/hash/d202ed5b6ef82d9b842d9cf2f73b0a37-Abstract.html`).

## Identity & Boundary Resolution

Distinct from uncompressed Local SGD (AIMech:LocalSgdPeriodicAveragingParallelStochasticGradientDescent, Stich 2019), which performs periodic averaging every H steps without quantization, sparsification, or error memory, and from single-step Sparsified SGD with Error Memory (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression) and QSGD (AIMech:QsgdQuantizedStochasticGradientDescentWithEliasCoding), neither of which composes contractive sparsification with unbiased quantization over multi-step local blocks H > 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 422 Qsparse-local-SGD (Basu et al. 2019): beta=1.5 err_scaled_sq=20.00 < ||x||^2=30.00 < err_unscaled_sq=42.50, H4/H1_mem_ratio=16.0
```
