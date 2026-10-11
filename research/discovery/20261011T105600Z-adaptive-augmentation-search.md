# Adaptive augmentation search — 2026-10-11T10:56:00Z

Added three native DRAFT concepts, bringing the maintained collection to 250.

| Record | Defining procedure |
| --- | --- |
| [AIMech:FastAutoAugment](../../data/curated/FastAutoAugment.yaml) | An augmentation-policy search procedure that evaluates candidate transformations on held-out training examples using a fixed classifier trained on another split, combines high-scoring policies across splits and uses them for final classifier training. |
| [AIMech:PopulationBasedAugmentation](../../data/curated/PopulationBasedAugmentation.yaml) | An augmentation-schedule learning procedure that jointly trains a population of child classifiers and evolves their augmentation hyperparameters by copying successful members and perturbing their policies over training time. |
| [AIMech:AdaMixUp](../../data/curated/AdaMixUp.yaml) | An adaptive interpolation-training procedure that learns example-dependent mixing-coefficient regions with a policy network and trains a classifier together with an intrusion discriminator intended to separate mixed examples from original data. |

The records distinguish fixed-model policy scoring, population-based schedules and learned interpolation regions. They preserve differences between paper and code in FAA scoring, operation inventories and baseline transforms, and in AdaMixUp loss signs, label conventions and normalization. PBA’s sampled operation count is a cap.

An [original finite calculation](adaptive-augmentation-boundaries.py) checks these mathematical distinctions without executing downloaded implementations.

The JSON ledger contains exact sources, hashes, inspected scopes, ignored-inclusive identity searches, mapping decisions and inherited/new candidates. Review is adversarial author self-review. Discovery remains active.

[Issue63](https://github.com/CultureBotAI/AIMech/issues/63) tracks correction of the draft FAA logged-loss reduction. A shape-aware example separates the actual batch-global score from the incorrectly inferred per-example best-view mean. The initial finding and successor review preserve the audit trail.
