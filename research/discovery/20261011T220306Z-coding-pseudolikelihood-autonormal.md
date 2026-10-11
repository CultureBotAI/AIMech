# Coding likelihood, pseudolikelihood and auto-normal fields — 2026-10-11T22:03:06Z

Added three native DRAFT concepts, bringing the maintained collection to 403.

| Record | Definition |
| --- | --- |
| [AIMech:MaximumPseudolikelihoodEstimation](../../data/curated/MaximumPseudolikelihoodEstimation.yaml) | A parameter-estimation method that maximizes the product of a specified model’s sitewise full conditional probabilities or densities evaluated at the observed configuration. |
| [AIMech:MaximumCodingLikelihoodEstimation](../../data/curated/MaximumCodingLikelihoodEstimation.yaml) | A conditional parameter-estimation method that selects mutually non-neighboring sites in a Markov field and maximizes their joint conditional likelihood, which factors into sitewise full conditionals given the remaining observed sites. |
| [AIMech:AutoNormalMarkovRandomField](../../data/curated/AutoNormalMarkovRandomField.yaml) | A proper finite Gaussian Markov-field model specified by linear full-conditional means and positive, value-independent site conditional variances, with compatibility enforced by a symmetric positive-definite joint precision matrix. |

The [finite examples](coding-pseudolikelihood-autonormal-boundaries.py) check conditional likelihoods, objective maximizers, weighted Gaussian compatibility and properness. The ledger records all 64 PDF pages read, source-version and asymptotic limitations, extraction retries, ignored-inclusive identity searches and directional AIO mappings.

Adversarial author self-review is required. Discovery remains active with 236 pending inspection leads and carried unresolved dispositions.
