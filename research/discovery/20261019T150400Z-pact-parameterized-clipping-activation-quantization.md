# Discovery Report: Round 821 — PACT (Parameterized Clipping Activation for Quantized Neural Networks)

- **Timestamp**: `2026-10-19T15:04:00Z`
- **Selected Concept**: `AIMech:PACTParameterizedClippingActivationForQuantizedNeuralNetworks` (*PACT (Parameterized Clipping Activation for Quantized Neural Networks)*)
- **Record Path**: `data/curated/PACTParameterizedClippingActivationForQuantizedNeuralNetworks.yaml`
- **Primary Source**: Jungwook Choi, Zhuo Wang, Swagath Venkataramani, Pierce I-Jen Chuang, Vijayalakshmi Srinivasan, Kailash Gopalakrishnan — *PACT: Parameterized Clipping Activation for Quantized Neural Networks* (`https://arxiv.org/bibtex/1805.06085`).

## Identity & Boundary Resolution

Distinct from fixed-range ReLU clipping (e.g., ReLU6 or fixed [0, 1] clipping in DoReFa-Net, AIMech:DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients) where the clipping bound is a hand-tuned hyperparameter rather than a gradient-learned parameter alpha, and distinct from post-training KL-divergence activation calibration in HAQ (AIMech:HAQHardwareAwareAutomatedQuantizationWithMixedPrecision).

## Constructed Boundary & Regime Verification

```text
{"bitwidth_k": 2, "concept": "PACTParameterizedClippingActivationForQuantizedNeuralNetworks", "eq1_piecewise_identity_verified": true, "learned_pact_alpha": 2.2944, "mse_pact_learned_alpha": 0.025999, "mse_unclipped_max_range": 0.181759, "outlier_max_alpha": 6.5, "verification": "passed"}
```
