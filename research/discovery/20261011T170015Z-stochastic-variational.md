# Stochastic activations and black-box variational inference — 2026-10-11T17:00:15Z

Added three native DRAFT records, bringing the maintained collection to 340.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:NoisyRectifier](../../data/curated/NoisyRectifier.yaml) | A stochastic activation that adds zero-mean noise to a preactivation and then applies the positive-part rectifier, producing h=max(0,a+z). |
| [AIMech:StochasticTimesSmoothUnit](../../data/curated/StochasticTimesSmoothUnit.yaml) | A stochastic activation that sets p=sigmoid(a), samples a Bernoulli gate with success probability sqrt(p), and outputs the gate multiplied by sqrt(p). |
| [AIMech:BlackBoxVariationalInference](../../data/curated/BlackBoxVariationalInference.yaml) | A variational-inference procedure that estimates evidence-lower-bound gradients from samples of a tractable variational distribution using its score function and model log joint, with mean-field local signals and score control variates to manage estimator variance. |

The noisy rectifier and STS unit have related component mappings to ReLUFunction and SigmoidFunction respectively. BBVI has a related mapping to ProbabilisticGraphicalModel for its factorization context. The records preserve the distinctions between stochastic outputs and their means, smooth-only and full expected gradients, and fixed versus sample-estimated control variates.

The [finite examples](stochastic-variational-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 186 pending inspection leads.
