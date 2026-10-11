# Visual self-supervision — 2026-10-11T07:54:20Z

Added four concepts; AIMech now contains 191 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:SimCLR](../../data/curated/SimCLR.yaml) | A self-supervised representation-learning procedure that jointly trains an encoder and a nonlinear projection head by contrasting two augmented views of each image against other images’ views in the same minibatch. |
| [AIMech:MomentumContrast](../../data/curated/MomentumContrast.yaml) | A contrastive representation-learning mechanism that maintains a queue of encoded negative keys and produces new keys with an encoder updated by an exponential moving average of the query encoder. |
| [AIMech:BootstrapYourOwnLatent](../../data/curated/BootstrapYourOwnLatent.yaml) | A self-supervised image representation-learning procedure that trains an online predictor to match a stopped-gradient target projection from another augmented view, while updating the target encoder and projector by exponential moving averages. |
| [AIMech:DINOSelfDistillation](../../data/curated/DINOSelfDistillation.yaml) | A self-supervised representation-learning procedure that matches cross-view student probabilities to centered and sharpened probabilities from a momentum teacher, without a separate prediction head or explicit negative-pair objective. |

All four have qualified related mappings to the AIO self-supervised learning task. SimCLR and MoCo also relate to AIO contrastive learning; the mapping does not assert an algorithm is a network.

The source audit distinguishes current-batch negatives, queued momentum keys, online-only prediction with normalized regression, and centered/sharpened cross-view teacher probabilities. DINO paper/code discrepancies are recorded, and the distinct DINO detector is not an unqualified alias.

Four main papers, the BYOL supplement and pinned DINO code support the records. Only declared passages and images were inspected. No training or benchmark reproduction occurred.

SimSiam, SwAV, DeepCluster, redundancy-reduction methods, Mean Teacher, contrastive objectives and optimizer/variant leads remain pending alongside the entire prior frontier. Discovery remains active.
