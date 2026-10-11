# Population and density methods — 2026-10-11T11:08:01Z

Added three native DRAFT concepts, bringing the maintained collection to 253.

| Record | Defining procedure |
| --- | --- |
| [AIMech:PopulationBasedTraining](../../data/curated/PopulationBasedTraining.yaml) | A population-based neural-network training procedure that interleaves parameter updates with performance-guided copying of partially trained models and exploration of hyperparameters, producing training trajectories with changing hyperparameter settings. |
| [AIMech:TreeStructuredParzenEstimator](../../data/curated/TreeStructuredParzenEstimator.yaml) | A sequential hyperparameter optimization method that separates observations by a loss quantile, fits tree-structured densities for the better and remaining configurations, and proposes evaluations using their density ratio as an expected-improvement ranking. |
| [AIMech:BayesianDataAugmentation](../../data/curated/BayesianDataAugmentation.yaml) | Tran et al.’s supervised deep-learning procedure that treats synthetic labeled examples as latent data, repeatedly samples them from an evolving learned model and updates model parameters through a generalized Monte Carlo expectation-maximization formulation. |

The records distinguish weight inheritance and schedule search, two-density configuration ranking, and iterative generation of labeled training examples. The Bayesian augmentation record preserves the gap between sampled-objective improvement and practical convergence guarantees.

An [original finite calculation](population-density-boundaries.py) checks density-ratio scaling, expectation and normalization boundaries. The JSON ledger records exact sources, reading scopes, ignored-inclusive identity searches, AIO mappings and inherited/new leads.

Review is adversarial author self-review. Discovery remains active; expected improvement and Smart Augmentation still need separate inspection.
