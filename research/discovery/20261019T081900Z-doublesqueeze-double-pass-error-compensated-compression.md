# Discovery Report: Round 416 — DoubleSqueeze (Double-Pass Error-Compensated Gradient Compression)

- **Timestamp**: `2026-10-19T08:19:00Z`
- **Selected Concept**: `AIMech:DoubleSqueezeDoublePassErrorCompensatedCompression` (*DoubleSqueeze (Double-Pass Error-Compensated Gradient Compression)*)
- **Record Path**: `data/curated/DoubleSqueezeDoublePassErrorCompensatedCompression.yaml`
- **Primary Source**: Hanlin Tang, Chen Yu, Xiangru Lian, Tong Zhang, Ji Liu — *DoubleSqueeze: Parallel Stochastic Gradient Descent with Double-pass Error-Compensated Compression* (`https://proceedings.mlr.press/v97/tang19d.html`).

## Identity & Boundary Resolution

Distinct from unidirectional error-feedback compression methods such as Sparsified SGD with Error Memory (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression, Stich, Cordonnier, & Jaggi 2018) and EF21 (AIMech:Ef21MarkovCompressorErrorFeedbackForHeterogeneousNonconvexOptimization, Richtárik, Sokolov, & Fatkhullin 2021), which compress only worker-to-server uploads and require uncompressed server-to-worker broadcasts or all-to-all aggregation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 416 DoubleSqueeze (Tang et al. 2019): Lemma 1 exact recurrence verified (err < 1e-12), gamma=1 virtual-iterate drift=0.0, gamma=0 uncompensated drift=0.1017 > 0
```
