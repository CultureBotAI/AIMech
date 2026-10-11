# Hierarchical mixtures and mean-field inference — 2026-10-11T20:16:36Z

Added one native DRAFT model family and two variational inference methods, bringing the maintained collection to 385.

| Record | Definition |
| --- | --- |
| [AIMech:HierarchicalMixtureOfExperts](../../data/curated/HierarchicalMixtureOfExperts.yaml) | A conditional mixture-model family that organizes output experts as leaves of a tree and forms each leaf’s mixture weight by multiplying input-dependent probabilistic gates along its root-to-leaf path. |
| [AIMech:StructuredMeanFieldInference](../../data/curated/StructuredMeanFieldInference.yaml) | A variational inference method that approximates a target distribution with a tractable family retaining selected dependencies, choosing its parameters to reduce the approximation-to-target Kullback–Leibler divergence. |
| [AIMech:FullyFactorizedMeanFieldInference](../../data/curated/FullyFactorizedMeanFieldInference.yaml) | A variational inference method that restricts its approximating distribution to a product of single-variable factors and adjusts those factors to reduce the approximation-to-target Kullback–Leibler divergence. |

HME has a broad Bayesian-network mapping and a related decision-tree mapping. Both inference methods have related graphical-model and Boltzmann-network mappings, preserving the distinction between a method and a model.

The [finite examples](hierarchical-mean-field-boundaries.py) and JSON ledger preserve complete reading of both primary papers, identity checks, variational bounds, retained correlations, auxiliary-link constants and conditional mixture responsibilities. Boltzmann trees remains pending full-text access.

Adversarial author self-review is required. Discovery remains active with 212 pending inspection leads and carried unresolved dispositions.
