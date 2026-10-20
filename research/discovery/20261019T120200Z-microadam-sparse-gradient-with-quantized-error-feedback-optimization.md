# Discovery Report: Round 639 — MicroAdam (Sparse-Gradient Adaptive Optimization with Quantized Error Feedback)

- **Timestamp**: `2026-10-19T12:02:00Z`
- **Selected Concept**: `AIMech:MicroAdamSparseGradientWithQuantizedErrorFeedbackOptimization` (*MicroAdam (Sparse-Gradient Adaptive Optimization with Quantized Error Feedback)*)
- **Record Path**: `data/curated/MicroAdamSparseGradientWithQuantizedErrorFeedbackOptimization.yaml`
- **Primary Source**: Ionut-Vlad Modoranu, Mher Safaryan, Grigory Malinovsky, Eldar Kurtic, Thomas Robert, Peter Richtárik, Dan Alistarh — *MicroAdam: Accurate Adaptive Optimization with Low Space Overhead and Provable Convergence* (`https://dblp.org/rec/conf/nips/ModoranuSMK0RA24`).

## Identity & Boundary Resolution

Distinct from 8-bit Adam (AIMech:EightBitOptimizerBlockwiseQuantization), which quantizes dense first- and second-moment vectors m_t, v_t in R^d to 8 bits (2d bytes total); MicroAdam stores a circular window of m = 10 Top-k sparse gradients (k = d/100) plus a 4-bit quantized error-feedback vector e_t (0.5d + 4mk = 0.9d bytes, less than half of 8-bit Adam). Distinct from GaLore (AIMech:GaLoreGradientLowRankProjection), which projects gradients into a low-rank SVD subspace without error feedback.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 639 MicroAdam verified: M_muA=5.65GB < M_AW8=12.55GB (m_max=37.5), omega=0.2240, adamstats_err=1.11e-16, q_omega=0.8818<1, lemma3_bound=141.49
```
