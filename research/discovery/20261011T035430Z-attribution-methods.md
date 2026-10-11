# Attribution-method discovery — 2026-10-11T03:54:30Z

Added Integrated Gradients, DeepLIFT, SmoothGrad and layer-wise relevance propagation after inspecting primary methods and rendered equations. The native collection now contains 68 DRAFT records.

| Record | Scope retained |
| --- | --- |
| [AIMech:IntegratedGradients](../../data/curated/IntegratedGradients.yaml) | Straight-path gradient integration differs from a gradient at one input, layer-wise contribution propagation and Shapley averaging across feature orderings. |
| [AIMech:DeepLIFT](../../data/curated/DeepLIFT.yaml) | This record covers the 2017 DeepLIFT method including distinct local rules; it is not identical to gradients, integrated gradients, Deep SHAP or the earlier Rescale-only formulation. |
| [AIMech:SmoothGrad](../../data/curated/SmoothGrad.yaml) | SmoothGrad is an averaging wrapper around a sensitivity-map method, not a new trained network, a training-noise procedure or an exact equivalent of its underlying gradient map. |
| [AIMech:LayerWiseRelevancePropagation](../../data/curated/LayerWiseRelevancePropagation.yaml) | LRP is a family of constrained relevance-propagation constructions, demonstrated for neural networks and kernel-based Bag-of-Words classifiers; it is not a single gradient formula or a classifier-training algorithm. |

Identity searches included ignored and hidden files. Related AIO mappings identify artificial neural networks as directly analyzed systems, without equating methods and architectures.

Baseline dependence, propagation-rule choices, numerical approximation and relevance leakage are preserved. Visual clarity does not establish explanation faithfulness. The JSON companion retains query details, source hashes, exact passages, actual visual inspection and unresolved methods and evaluation evidence, including counterpoints.

Discovery remains active: four new methods were found and both this cohort and earlier cohorts have pending leads.
