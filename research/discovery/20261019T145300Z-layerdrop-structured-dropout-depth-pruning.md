# Discovery Report: Round 810 — LayerDrop: Structured Dropout for On-Demand Transformer Depth Reduction

- **Timestamp**: `2026-10-19T14:53:00Z`
- **Selected Concept**: `AIMech:LayerDropStructuredDropoutForTransformerDepthReduction` (*LayerDrop: Structured Dropout for On-Demand Transformer Depth Reduction*)
- **Record Path**: `data/curated/LayerDropStructuredDropoutForTransformerDepthReduction.yaml`
- **Primary Source**: Angela Fan, Edouard Grave, Armand Joulin — *Reducing Transformer Depth on Demand with Structured Dropout* (`https://arxiv.org/bibtex/1909.11556`).

## Identity & Boundary Resolution

Introduced by Angela Fan, Edouard Grave, and Armand Joulin (ICLR 2020, arXiv:1909.11556). Distinct from unstructured weight DropConnect (which zeroes individual weights without reducing inference latency), from Stochastic Depth in ResNets (which uses a linear depth-decay survival schedule purely to accelerate training without inference-time layer pruning), and from distillation-based depth compression methods such as DistilBERT (Round 803) and TinyBERT (Round 800) that must train a separate student model for each target depth.

## Constructed Boundary & Regime Verification

```text
{"concept": "LayerDropStructuredDropoutForTransformerDepthReduction", "optimal_p_for_6_of_12": 0.5, "optimal_p_for_3_of_12": 0.75, "kept_layers_prune_025": [1, 2, 3, 5, 6, 7, 9, 10, 11], "kept_layers_prune_050": [1, 3, 5, 7, 9, 11], "active_layers_48L_p05": 24.0, "status": "ok"}
```
