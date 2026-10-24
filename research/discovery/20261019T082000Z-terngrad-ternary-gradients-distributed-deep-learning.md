# Discovery Report: Round 417 — TernGrad (Stochastic Ternary Gradient Quantization for Distributed Deep Learning)

- **Timestamp**: `2026-10-19T08:20:00Z`
- **Selected Concept**: `AIMech:TernGradTernaryGradientsForDistributedDeepLearning` (*TernGrad (Stochastic Ternary Gradient Quantization for Distributed Deep Learning)*)
- **Record Path**: `data/curated/TernGradTernaryGradientsForDistributedDeepLearning.yaml`
- **Primary Source**: Wei Wen, Cong Xu, Feng Yan, Chunpeng Wu, Yandan Wang, Yiran Chen, Hai Li — *TernGrad: Ternary Gradients to Reduce Communication in Distributed Deep Learning* (`https://papers.nips.cc/paper/2017/hash/2bf283c05b601f21364d052ca0ec798d-Abstract.html`).

## Identity & Boundary Resolution

Distinct from deterministic sign-based compression SignSGD (AIMech:SignSgdAndMajorityVoteCompressedNonconvexOptimization, Bernstein et al. 2018), which maps coordinates deterministically to {-1, +1} without zero level or unbiased probabilistic rounding, and from multi-level L2-norm quantized SGD QSGD (AIMech:QsgdQuantizedStochasticGradientDescentWithEliasCoding, Alistarh et al. 2017), which normalizes by the Euclidean norm ||g_t||_2 rather than the infinity norm s_t = ||g_t||_infty with layer-wise sigma-clipping.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 417 TernGrad (Wen et al. 2017): max_bias=0.0e+00, var_global=2.8034 == s*||g||_1-||g||_2^2=2.8034, var_layerwise=2.5214 < var_global, var_clipped=1.1812 < var_unclipped=2.5200
```
