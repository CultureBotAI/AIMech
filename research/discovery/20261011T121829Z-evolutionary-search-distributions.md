# Evolutionary search distributions — 2026-10-11T12:18:29Z

Added three native DRAFT concepts, bringing the maintained collection to 273.

| Record | Defining procedure |
| --- | --- |
| [AIMech:DifferentialEvolution](../../data/curated/DifferentialEvolution.yaml) | A population-based continuous optimization method that generates trial vectors using scaled differences between population members, combines mutant and target coordinates, and selects replacements through target-trial objective comparisons. |
| [AIMech:CovarianceMatrixAdaptationEvolutionStrategy](../../data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml) | An evolution strategy for continuous optimization that samples a multivariate normal search distribution and adapts its mean, covariance and global step size from ranked offspring and accumulated selected-step paths. |
| [AIMech:NaturalEvolutionStrategies](../../data/curated/NaturalEvolutionStrategies.yaml) | A family of black-box optimization algorithms that adapts a parameterized search distribution using estimates of the natural gradient of expected fitness with respect to the distribution parameters. |

The records distinguish population difference-vector proposals, selected-step covariance adaptation, and Fisher-preconditioned search-distribution updates. Source-specific tie rules, errata and finite-sample limits are retained.

Each concept carries an explicit AIO no-match assessment. The [finite calculation](evolutionary-search-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves queries, source hashes, actual reading scopes, ignored-inclusive identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
