# Sigmoid belief and neural autoregressive models — 2026-10-11T17:27:17Z

Added three native DRAFT records, bringing the maintained collection to 346.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:SigmoidBeliefNetwork](../../data/curated/SigmoidBeliefNetwork.yaml) | A directed acyclic probabilistic network of binary variables whose forward conditional probabilities are logistic functions of weighted parent states and a bias. |
| [AIMech:NeuralAutoregressiveDistributionEstimator](../../data/curated/NeuralAutoregressiveDistributionEstimator.yaml) | A fully visible autoregressive density model whose ordered variable conditionals are computed by neural networks that share input-to-hidden parameters and recursively reuse prefix computations. |
| [AIMech:DeepAutoregressiveNetwork](../../data/curated/DeepAutoregressiveNetwork.yaml) | A generative neural architecture that combines directed stochastic hidden layers with autoregressive within-layer conditional dependencies and a separately parameterized recognition network for approximate latent inference. |

SBN and original NADE map to the broader AIO BayesianNetwork class. DARN has a related mapping to that class for its directed generative component, while its maintained identity includes the recognition network. The records distinguish stochastic variables, deterministic hidden activations, exact model generation and approximate inference/training.

The [finite examples](autoregressive-belief-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 190 pending inspection leads.
