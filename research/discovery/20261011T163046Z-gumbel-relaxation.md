# Gumbel relaxations and ancestral sampling — 2026-10-11T16:30:46Z

Added three native DRAFT records, bringing the maintained collection to 334.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:GumbelSoftmaxRelaxation](../../data/curated/GumbelSoftmaxRelaxation.yaml) | A continuous relaxation of a finite categorical random variable obtained by applying softmax to independent Gumbel-perturbed log weights divided by a positive temperature, producing a differentiable random vector in the simplex interior. |
| [AIMech:StraightThroughGumbelSoftmax](../../data/curated/StraightThroughGumbelSoftmax.yaml) | A surrogate-gradient estimator that uses a hard one-hot argmax of a Gumbel-Softmax sample in the forward computation and substitutes the corresponding continuous softmax relaxation’s derivative in the backward computation. |
| [AIMech:AncestralGumbelTopKSampling](../../data/curated/AncestralGumbelTopKSampling.yaml) | An exact without-replacement sampler for finite discrete Bayesian-network configurations that propagates conditional Gumbel subtree maxima through a bounded priority frontier, with a configurable number of parallel expansions and parent-respecting variable selection. |

The relaxation and straight-through estimator have related component mappings to SoftmaxFunction; the ancestral sampler has a related input-model mapping to BayesianNetwork. Concrete and Gumbel-Softmax share a distribution, while straight-through differentiation changes the backward rule. Finite examples expose estimator bias and the distinction between parallel rounds and total work.

The [finite examples](gumbel-relaxation-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 187 pending inspection leads.
