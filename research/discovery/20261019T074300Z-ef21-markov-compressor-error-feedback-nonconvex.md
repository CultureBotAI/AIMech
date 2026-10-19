# Discovery Report: Round 380 — EF21 Markov-Compressor Error Feedback for Heterogeneous Nonconvex Distributed Optimization

- **Timestamp**: `2026-10-19T07:43:00Z`
- **Selected Concept**: `AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization` (*EF21 Markov-Compressor Error Feedback for Heterogeneous Nonconvex Distributed Optimization*)
- **Record Path**: `data/curated/Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization.yaml`
- **Primary Source**: Peter Richtarik, Igor Sokolov, Ilyas Fatkhullin — *EF21: A New, Simpler, Theoretically Better, and Practically Faster Error Feedback* (`https://proceedings.neurips.cc/paper/2021/hash/231141b34c82aa95e48810a9d1b33a79-Abstract.html`).

## Identity & Boundary Resolution

Distinct from classical error-compensated SGD (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression, which compresses step-scaled gradients plus residual memory m_t + eta_t * g_t, requires bounded gradient norms, and suffers an O(1/alpha^2) dependence in heterogeneous distributed settings), from unbiased stochastic quantization (AIMech:QsgdQuantizedStochasticGradientDescentWithEliasCoding), and from uncompressed variance-reduced nonconvex optimizers (AIMech:PageProbabilisticGradientEstimatorForNonconvexOptimization). No pinned AIO class covers EF21 or Markov gradient-difference error feedback.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 380 EF21 Markov Compressor Error Feedback boundaries verified.
```
