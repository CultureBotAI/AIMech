# Halving and grid search — 2026-10-11T11:43:00Z

Added three native DRAFT concepts, bringing the maintained collection to 262.

| Record | Defining procedure |
| --- | --- |
| [AIMech:SuccessiveHalving](../../data/curated/SuccessiveHalving.yaml) | A staged best-candidate selection algorithm that divides a resource budget across elimination rounds, evaluates surviving candidates with comparable within-round effort, removes approximately the poorer-performing half, and allocates more effort per remaining candidate in later rounds. |
| [AIMech:AsynchronousSuccessiveHalving](../../data/curated/AsynchronousSuccessiveHalving.yaml) | An asynchronous resource-allocation algorithm that promotes promising completed hyperparameter trials through increasing resource levels as workers become available and starts new trials when no eligible promotion is available, without waiting for an entire evaluation stage to finish. |
| [AIMech:GridSearchHyperparameterOptimization](../../data/curated/GridSearchHyperparameterOptimization.yaml) | A hyperparameter optimization procedure that evaluates a finite Cartesian product of chosen values for each configuration variable and selects a configuration using its validation performance. |

The records retain the common halving identity while separating stochastic and non-stochastic score and rounding conventions. ASHA’s promotion scan follows the author dissertation, with the conference-paper indentation discrepancy recorded explicitly. General grid search is distinct from the maintained fairness reduction.

An [original finite calculation](halving-and-grid-boundaries.py) checks these boundaries. The JSON ledger retains source hashes, actual reading scopes, identity searches, AIO mapping assessments and remaining candidates.

Review is adversarial author self-review. Discovery remains active.
