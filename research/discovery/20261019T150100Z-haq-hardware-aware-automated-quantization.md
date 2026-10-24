# Discovery Report: Round 818 — HAQ (Hardware-Aware Automated Quantization with Mixed Precision)

- **Timestamp**: `2026-10-19T15:01:00Z`
- **Selected Concept**: `AIMech:HAQHardwareAwareAutomatedQuantizationWithMixedPrecision` (*HAQ (Hardware-Aware Automated Quantization with Mixed Precision)*)
- **Record Path**: `data/curated/HAQHardwareAwareAutomatedQuantizationWithMixedPrecision.yaml`
- **Primary Source**: Kuan Wang, Zhijian Liu, Yujun Lin, Ji Lin, Song Han — *HAQ: Hardware-Aware Automated Quantization with Mixed Precision* (`https://arxiv.org/bibtex/1811.08886`).

## Identity & Boundary Resolution

Distinct from uniform fixed-bitwidth quantization (e.g., PACT or 8-bit integer quantization), distinct from Hessian-spectrum mixed-precision quantization such as Q-BERT (AIMech:QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT) which relies on second-order sensitivity without hardware-in-the-loop latency/energy feedback, and distinct from AMC (AIMech:AMCAccelerationAndModelCompressionOnMobileDevicesWithRL) which uses DDPG to search continuous channel/fine-grained pruning sparsity ratios rather than mixed-precision weight and activation bitwidths.

## Constructed Boundary & Regime Verification

```text
HAQ verification passed: bits=(2,5,8), err_8bit=0.000034 < err_2bit=0.4360, final_cost=55.0<=55.0, dw_oi=4.47 << pw_oi=59.17
```
