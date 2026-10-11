# Score gradients and variational learning — 2026-10-11T16:43:04Z

Added three native DRAFT records, bringing the maintained collection to 337.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:REINFORCE](../../data/curated/REINFORCE.yaml) | A family of stochastic reinforcement-learning update rules that multiply a sampled reward relative to an admissible baseline by the derivative of the log probability of the sampled action or unit output, with a nonnegative learning-rate factor. |
| [AIMech:StraightThroughEstimator](../../data/curated/StraightThroughEstimator.yaml) | A surrogate-gradient rule that keeps a hard threshold or sampled binary output in the forward computation while propagating its downstream derivative backward as though the hard operation were the identity function. |
| [AIMech:NeuralVariationalInferenceAndLearning](../../data/curated/NeuralVariationalInferenceAndLearning.yaml) | A method for jointly training a directed latent-variable model and an amortized stochastic inference network by maximizing a variational log-likelihood bound, using score-function inference gradients with learned baselines and adaptive learning-signal normalization. |

REINFORCE has a related ReinforcementLearning mapping; NVIL has a related BayesianNetwork mapping. The identity straight-through estimator has a bounded AIO no-match assessment. The records distinguish reward-weighted log-probability derivatives, heuristic backward substitution and joint variational training. Source inconsistencies and finite-sample baseline limitations are explicit.

The [finite examples](score-gradient-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 188 pending inspection leads.
