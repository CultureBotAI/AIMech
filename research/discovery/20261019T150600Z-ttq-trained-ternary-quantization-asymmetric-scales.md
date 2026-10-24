# Discovery Report: Round 823 — TTQ (Trained Ternary Quantization)

- **Timestamp**: `2026-10-19T15:06:00Z`
- **Selected Concept**: `AIMech:TTQTrainedTernaryQuantization` (*TTQ (Trained Ternary Quantization)*)
- **Record Path**: `data/curated/TTQTrainedTernaryQuantization.yaml`
- **Primary Source**: Chenzhuo Zhu, Song Han, Huizi Mao, William J. Dally — *Trained Ternary Quantization* (`https://arxiv.org/bibtex/1612.01064`).

## Identity & Boundary Resolution

Distinct from symmetric Ternary Weight Networks (TWN), which tie positive and negative ternary magnitudes to a single analytical scale W_l with heuristic threshold 0.7 * E(|w|), and distinct from uniform k-bit weight quantizers such as DoReFa-Net (AIMech:DoReFaNetTrainingLowBitwidthConvolutionalNeuralNetworksWithLowBitwidthGradients).

## Constructed Boundary & Regime Verification

```text
{"asymmetric_ttq_mse": 0.005588, "concept": "TTQTrainedTernaryQuantization", "delta_threshold": 0.05, "learned_wn": 2.34, "learned_wp": 0.8582, "sparsity_ratio": 0.3, "symmetric_twn_mse": 0.395817, "verification": "passed"}
```
