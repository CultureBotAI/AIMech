# Value learning and ant routing — 2026-10-11T13:47:51Z

Added three native DRAFT concepts, bringing the maintained collection to 298.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:QLearning](../../data/curated/QLearning.yaml) | A model-free reinforcement-learning method that incrementally updates action-value estimates toward an observed reward plus the discounted maximum estimated value of the next state’s actions. |
| [AIMech:AntNet](../../data/curated/AntNet.yaml) | A distributed adaptive routing algorithm in which forward agents sample network paths and backward agents use the measured trip times to update local traffic models and probabilistic routing tables. |
| [AIMech:AntColonyOptimization](../../data/curated/AntColonyOptimization.yaml) | A metaheuristic framework for optimization in which artificial ants construct solutions using local information and communicate indirectly through shared pheromone information that is adapted from their search experience. |

Q-learning updates tabular action values; AntNet learns routing probabilities from measured forward trips; ACO defines the broader framework for artificial-ant search. Convergence assumptions, queue conventions and optional framework components remain explicit.

Q-learning and AntNet have qualified related matches to AIO Reinforcement Learning. ACO has a bounded AIO no-match assessment. The [finite calculations](value-learning-and-ant-routing-boundaries.py) check the update distinctions. The JSON ledger preserves source versions, actual reading scopes, identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.

Review issue [83](https://github.com/CultureBotAI/AIMech/issues/83) corrected AntNet’s hard neighbor-eligibility rule. The restricted-set normalization and zero-queue qualifications remain explicit.
