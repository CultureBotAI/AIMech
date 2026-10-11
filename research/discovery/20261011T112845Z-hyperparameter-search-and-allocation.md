# Hyperparameter search and allocation — 2026-10-11T11:28:45Z

Added three native DRAFT concepts, bringing the maintained collection to 259.

| Record | Defining procedure |
| --- | --- |
| [AIMech:RandomSearchHyperparameterOptimization](../../data/curated/RandomSearchHyperparameterOptimization.yaml) | A hyperparameter optimization procedure that draws trial configurations independently from a specified search distribution, evaluates their validation performance, and selects a favorable evaluated configuration without adapting subsequent draws to observed trial scores. |
| [AIMech:Hyperband](../../data/curated/Hyperband.yaml) | A hyperparameter resource-allocation algorithm that runs successive-halving brackets with different initial configuration counts and starting budgets, balancing broad early screening against more conservative evaluation. |
| [AIMech:BOHB](../../data/curated/BOHB.yaml) | A hyperparameter optimization algorithm combining Hyperband resource brackets with model-guided configuration proposals from performance-split multivariate kernel density estimates and a continuing random-sampling component. |

The records distinguish independent sampling, successive-halving brackets, and KDE-guided proposals. Hyperband’s printed table and count formula differ, and BOHB’s equations and pinned implementation have different budget and density-fitting conventions; the ledger preserves these distinctions.

An [original finite calculation](hyperparameter-search-boundaries.py) checks the source boundaries. The JSON ledger records source hashes, actual PDF/code reading scopes, ignored-inclusive identity searches, AIO mappings and pending leads.

Review is adversarial author self-review. Discovery remains active.

Author review corrected a missing outer integer conversion for noninteger reduction factors and connected an uncited allocation-context source. Both findings and their fixes are tracked in [issue68](https://github.com/CultureBotAI/AIMech/issues/68).
