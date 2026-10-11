# Risk and pseudo-targets — 2026-10-11T10:46:13Z

Added four native DRAFT concepts, bringing the maintained collection to 247.

| Record | Defining procedure |
| --- | --- |
| [AIMech:UnsupervisedDataAugmentation](../../data/curated/UnsupervisedDataAugmentation.yaml) | A semi-supervised classifier-training procedure that combines labeled prediction loss with consistency between fixed current-model predictions on original or weakly augmented unlabeled inputs and predictions on strongly augmented versions. |
| [AIMech:PseudoLabel](../../data/curated/PseudoLabel.yaml) | A semi-supervised neural-network training procedure that recomputes hard labels from the model’s most probable class for unlabeled examples and jointly fits observed and generated targets using a scheduled weight on the unlabeled loss. |
| [AIMech:VicinalRiskMinimization](../../data/curated/VicinalRiskMinimization.yaml) | A risk-minimization principle that chooses a predictor from a specified function class by minimizing expected loss under an estimated distribution built from training examples and their neighborhoods. |
| [AIMech:TrainingSignalAnnealing](../../data/curated/TrainingSignalAnnealing.yaml) | A supervised-loss scheduling procedure that temporarily excludes labeled examples already predicted with confidence above an increasing threshold, gradually allowing more labeled training signal during semi-supervised learning. |

The records retain original source conventions: Pseudo-Label’s sigmoid/classwise binary loss, UDA’s paper cross-entropy versus implemented KL, TSA’s labeled-example mask and retained-count denominator, and VRM’s distinction between a point-mass objective and a limit after minimization.

An [original finite calculation](risk-and-target-boundaries.py) checks loss values, mask normalization and schedule endpoints without executing author code or training a model.

The JSON ledger records source access failures and the bounded Pseudo-Label mirror, exact PDF/code versions, reading scope, ignored-inclusive identity searches, mappings and all inherited/new candidates. Review is adversarial author self-review. Discovery remains active.
