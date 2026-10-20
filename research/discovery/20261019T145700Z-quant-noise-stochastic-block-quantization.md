# Discovery Report: Round 814 — Quant-Noise (Training with Quantization Noise for Extreme Model Compression)

- **Timestamp**: `2026-10-19T14:57:00Z`
- **Selected Concept**: `AIMech:QuantNoiseTrainingWithQuantizationNoiseForExtremeCompression` (*Quant-Noise (Training with Quantization Noise for Extreme Model Compression)*)
- **Record Path**: `data/curated/QuantNoiseTrainingWithQuantizationNoiseForExtremeCompression.yaml`
- **Primary Source**: Angela Fan, Pierre Stock, Benjamin Graham, Edouard Grave, Remi Gribonval, Herve Jegou, Armand Joulin — *Training with Quantization Noise for Extreme Model Compression* (`https://arxiv.org/bibtex/2004.07320`).

## Identity & Boundary Resolution

Distinct from standard Quantization-Aware Training (QAT) with the Straight-Through Estimator (STE), which quantizes 100% of weights on every forward pass and suffers severe gradient bias under extreme compression (int4 or Product Quantization), distinct from Q-BERT (AIMech:QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT), which uses Hessian-spectrum mixed-precision scalar allocation, and distinct from LayerDrop (AIMech:LayerDropStructuredDropoutForTransformerDepthReduction), which drops entire Transformer layers rather than applying quantizer distortion to random subvector weight blocks.

## Constructed Boundary & Regime Verification

```text
Quant-Noise verification passed: clean_grads_p50=2/4, pq_bits=612352, fp32_bits=18874368, compression_ratio=30.82x
```
