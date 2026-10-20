# Discovery Report: Round 815 — Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ)

- **Timestamp**: `2026-10-19T14:58:00Z`
- **Selected Concept**: `AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks` (*Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ)*)
- **Record Path**: `data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml`
- **Primary Source**: Pierre Stock, Armand Joulin, Remi Gribonval, Benjamin Graham, Herve Jegou — *And the Bit Goes Down: Revisiting the Quantization of Neural Networks* (`https://arxiv.org/bibtex/1907.05686`).

## Identity & Boundary Resolution

Distinct from classical weight-space Product Quantization (Gong et al., 2014), which minimizes Frobenius weight error ||W - W_hat||_2^2 (Eq. 1) and suffers catastrophic accuracy drift across deep layers, and distinct from Quant-Noise (AIMech:QuantNoiseTrainingWithQuantizationNoiseForExtremeCompression), which applies quantization noise to random weight blocks during training to preserve unbiased gradient flow.

## Constructed Boundary & Regime Verification

```text
iPQ verification passed: act_err_act=0.0558 << act_err_std=13.1130, idx_bytes=16384, cb_bytes=4608
```
