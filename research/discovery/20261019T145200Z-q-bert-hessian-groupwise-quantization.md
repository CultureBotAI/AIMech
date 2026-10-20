# Discovery Report: Round 809 — Q-BERT: Hessian-Based Ultra Low Precision Quantization of BERT

- **Timestamp**: `2026-10-19T14:52:00Z`
- **Selected Concept**: `AIMech:QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT` (*Q-BERT: Hessian-Based Ultra Low Precision Quantization of BERT*)
- **Record Path**: `data/curated/QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT.yaml`
- **Primary Source**: Sheng Shen, Zhen Dong, Jiayu Ye, Linjian Ma, Zhewei Yao, Amir Gholami, Michael W. Mahoney, Kurt Keutzer — *Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT* (`https://arxiv.org/bibtex/1909.05840`).

## Identity & Boundary Resolution

Introduced by Sheng Shen, Zhen Dong, Jiayu Ye, Linjian Ma, Zhewei Yao, Amir Gholami, Michael W. Mahoney, and Kurt Keutzer (AAAI 2020, Vol. 34, No. 05, pp. 8815-8821, arXiv:1909.05840, doi:10.1609/aaai.v34i05.6409). Distinct from mean-only Hessian AWare Quantization (HAWQ) for CNNs — which fails on NLP tasks where middle Transformer layers exhibit high eigenvalue variance across data partitions (e.g., SQuAD layer 7 with var(lambda_7) > 61.6 vs. mean(lambda_7) approx 1.0) — and from layer-wise uniform quantization (DirectQ), which shares a single quantization range across all 3072 output neurons of multi-head self-attention.

## Constructed Boundary & Regime Verification

```text
{"concept": "QBERTHessianBasedUltraLowPrecisionQuantizationOfBERT", "power_iteration_top_eig": 5.0, "omega_squad_layer7": 9.0, "omega_stable_layer": 2.0671, "quant_mse_layerwise_g1": 0.368129, "quant_mse_groupwise_g4": 0.165817, "quant_mse_groupwise_g16": 0.023476, "encoder_compression_ratio": 12.78, "status": "ok"}
```
