# Interpolation and pseudo-labels — 2026-10-11T10:23:37Z

Added four native DRAFT concepts, bringing the maintained collection to 238.

| Record | Defining procedure |
| --- | --- |
| [AIMech:MixUp](../../data/curated/MixUp.yaml) | A training-data interpolation procedure that fits a predictor to convex combinations of example inputs and their corresponding targets using the same random mixing coefficient for both. |
| [AIMech:InterpolationConsistencyTraining](../../data/curated/InterpolationConsistencyTraining.yaml) | A semi-supervised training procedure that encourages a student’s prediction at an interpolated pair of unlabeled inputs to match the same interpolation of predictions from a moving-average teacher, while also fitting labeled examples. |
| [AIMech:FixMatch](../../data/curated/FixMatch.yaml) | A semi-supervised classifier-training procedure that fits labeled examples and trains on strongly augmented unlabeled inputs using hard pseudo-labels retained only when the corresponding weakly augmented prediction reaches a confidence threshold. |
| [AIMech:ReMixMatch](../../data/curated/ReMixMatch.yaml) | A semi-supervised classifier-training procedure that adjusts weak-view guessed labels toward an estimated class prior, sharpens and anchors those soft targets across strong augmentations, and trains with interpolated pairs plus unmixed consistency and rotation-prediction losses. |

The records preserve source differences: ICT’s published pre-step teacher averaging, FixMatch’s inclusive main-paper/code threshold versus the strict supplement notation, and ReMixMatch’s loss normalization and rotation scheduling. Distribution alignment encourages a prior match without enforcing exact class frequencies.

An [original finite calculation](ssl-source-boundaries.py) checks those algebraic boundaries. It does not train a model or reproduce a benchmark.

The JSON ledger preserves failed and successful source retrievals, exact PDF/code versions and reading scope, all inherited candidates and new augmentation/interpolation leads. Scientific review is adversarial author self-review; discovery remains active.
