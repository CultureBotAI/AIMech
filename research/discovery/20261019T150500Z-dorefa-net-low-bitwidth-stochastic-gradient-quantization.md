# Discovery Report: Round 822 — DoReFa-Net (Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients)

- **Timestamp**: `2026-10-19T15:05:00Z`
- **Selected Concept**: `AIMech:DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients` (*DoReFa-Net (Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients)*)
- **Record Path**: `data/curated/DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients.yaml`
- **Primary Source**: Shuchang Zhou, Yuxin Wu, Zekun Ni, Xinyu Zhou, He Wen, Yuheng Zou — *DoReFa-Net: Training Low Bitwidth Convolutional Neural Networks with Low Bitwidth Gradients* (`https://arxiv.org/bibtex/1606.06160`).

## Identity & Boundary Resolution

Distinct from PACT (AIMech:PACTParameterizedClippingActivationForQuantizedNeuralNetworks) which learns a parameterized activation clipping bound alpha with full-precision gradients rather than fixed [0, 1] clipping with stochastic low-bitwidth gradient quantization, and distinct from TTQ (AIMech:TTQTrainedTernaryQuantization) which learns asymmetric ternary weight scales {-W_l^n, 0, +W_l^p}.

## Constructed Boundary & Regime Verification

```text
{"bitwise_dot_product_eq3": 24, "concept": "DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients", "deterministic_small_grad_bias": 0.25333, "max_pooling_commutation_eq15_verified": true, "stochastic_small_grad_mean_bias": 0.0125, "verification": "passed"}
```
