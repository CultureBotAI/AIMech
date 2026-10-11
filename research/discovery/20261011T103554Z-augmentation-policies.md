# Augmentation policies — 2026-10-11T10:35:54Z

Added five native DRAFT concepts, bringing the maintained collection to 243.

| Record | Defining procedure |
| --- | --- |
| [AIMech:Cutout](../../data/curated/Cutout.yaml) | A training-image augmentation method that removes information from a randomly located square region by replacing that region with zeros in the normalized input while keeping the original target. |
| [AIMech:AutoAugment](../../data/curated/AutoAugment.yaml) | An automated augmentation-policy search procedure that trains a controller to propose image-transform subpolicies and rewards those proposals using validation accuracy of a child model trained with the proposed augmentation. |
| [AIMech:RandAugment](../../data/curated/RandAugment.yaml) | An image-augmentation procedure that applies a uniformly sampled sequence of operations sharing one magnitude parameter, reducing augmentation selection to tuning the operation count and shared magnitude on the target task. |
| [AIMech:ManifoldMixup](../../data/curated/ManifoldMixup.yaml) | A neural-network training procedure that interpolates paired examples’ representations at a selected network layer and interpolates their labels with the same coefficient, then trains the entire network on the mixed representation-target pairs. |
| [AIMech:CTAugment](../../data/curated/CTAugment.yaml) | An online augmentation-policy adaptation procedure that samples image operations and adjusts their parameter-selection weights using classifier feedback on labeled probe images during training. |

Cutout preserves the original random-center masking convention. AutoAugment searches policies using a child-model validation reward; RandAugment tunes an operation count and shared magnitude; Manifold Mixup trains through mixed hidden representations. CTAugment’s paper and released-code formulas are qualified separately.

An [original finite calculation](augmentation-source-boundaries.py) checks CTAugment feedback scores and interval selection. It does not execute a model or reproduce performance.

The JSON ledger records exact source versions, inspected pages and code, ignored-inclusive identity searches, mappings, all inherited candidates and new leads. Review is adversarial author self-review. The nonempty frontier keeps discovery active.
