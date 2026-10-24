# Discovery Report: Round 807 — FastBERT: Self-Distilling BERT with Adaptive Inference Time

- **Timestamp**: `2026-10-19T14:50:00Z`
- **Selected Concept**: `AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime` (*FastBERT: Self-Distilling BERT with Adaptive Inference Time*)
- **Record Path**: `data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml`
- **Primary Source**: Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Haotang Deng, Qi Ju — *FastBERT: a Self-distilling BERT with Adaptive Inference Time* (`https://arxiv.org/bibtex/2004.02178`).

## Identity & Boundary Resolution

Introduced by Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Haotang Deng, and Qi Ju (ACL 2020, pp. 6035-6044, arXiv:2004.02178, doi:10.18653/v1/2020.acl-main.537). Distinct from cross-model knowledge distillation methods (DistilBERT Round 803, TinyBERT Round 800, MobileBERT Round 804) that execute a fixed number of layers for every input, and from Patience-Based Early Exit (PABEE, Round 808), which jointly trains linear internal classifiers and exits based on cross-layer prediction agreement patience rather than frozen-backbone branch self-distillation and single-layer normalized entropy thresholding.

## Constructed Boundary & Regime Verification

```text
{"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime", "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform": 0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled": 0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08": 2784.0, "layer0_exit_speedup": 11.74, "status": "ok"}
```
