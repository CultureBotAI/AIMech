# Discovery Report: Round 391 — MARINA Faster Non-Convex Distributed Learning with Compression

- **Timestamp**: `2026-10-19T07:54:00Z`
- **Selected Concept**: `AIMech:MarinaFasterNonconvexDistributedLearningWithCompression` (*MARINA Faster Non-Convex Distributed Learning with Compression*)
- **Record Path**: `data/curated/MarinaFasterNonconvexDistributedLearningWithCompression.yaml`
- **Primary Source**: Eduard Gorbunov, Konstantin P. Burlachenko, Zhize Li, Peter Richtárik — *MARINA: Faster Non-Convex Distributed Learning with Compression* (`https://proceedings.mlr.press/v139/gorbunov21a.html`).

## Identity & Boundary Resolution

Distinct from DIANA (AIMech:DianaDistributedLearningWithCompressedGradientDifferences, which forms an unbiased gradient estimator by compressing g_i^k - h_i^k against stored per-worker shift vectors h_i^k and achieves worse O(omega/n + omega^{2/3}/n^{2/3}) scaling in nonconvex optimization), from EF21 (AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization, which supports biased contractive compressors without uncompressed synchronization rounds c_k = 1, whereas MARINA uses independent unbiased quantizers across workers to obtain a 1/sqrt(n) multi-node variance reduction factor), and from centralized PAGE/SARAH/SPIDER (AIMech:SARAHStochasticRecursiveGradientForFiniteSumOptimization and AIMech:SPIDERStochasticPathIntegratedDifferentialEstimatorForNonConvexOptimization, which do not compress worker-to-server communication). No pinned AIO class covers MARINA.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 391 MARINA (Gorbunov et al. 2021): mc_var=0.5533~=0.5421<=0.7762, end_grad_sq=0.00e+00, end_est_err_sq=0.00e+00
```
