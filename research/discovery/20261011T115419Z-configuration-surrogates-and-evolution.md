# Configuration surrogates and evolution — 2026-10-11T11:54:19Z

Added three native DRAFT concepts, bringing the maintained collection to 265.

| Record | Defining procedure |
| --- | --- |
| [AIMech:SequentialModelBasedAlgorithmConfiguration](../../data/curated/SequentialModelBasedAlgorithmConfiguration.yaml) | A sequential algorithm-configuration procedure that uses random-forest performance models to propose parameter settings and compares candidate settings with an incumbent through adaptive evaluations on shared problem instances and random seeds. |
| [AIMech:FABOLAS](../../data/curated/FABOLAS.yaml) | A Bayesian hyperparameter optimization algorithm that jointly chooses a model configuration and training-data subset size using surrogate models of loss and evaluation cost, directing evaluations toward information about the best configuration on the full dataset. |
| [AIMech:DEHB](../../data/curated/DEHB.yaml) | A hyperparameter optimization algorithm that combines Hyperband resource schedules with differential-evolution populations at different resource levels, using promising lower-resource configurations to guide proposals evaluated and selected at higher resource levels. |

The records preserve original SMAC’s scope, distinguish FABOLAS paper and implementation conventions, and separate DEHB’s synchronous halving stages from asynchronous population updates across overlapping brackets. Source ambiguities and unverified performance claims remain explicit.

An [original finite calculation](configuration-surrogate-boundaries.py) examines cost aggregation, resource units and source conventions. The JSON ledger records primary-source hashes, actual reading scopes, identity searches, AIO mapping assessments and the remaining discovery frontier.

Review is adversarial author self-review. Discovery remains active.
