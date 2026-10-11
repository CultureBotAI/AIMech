# Mixture, real-valued and document density models — 2026-10-11T17:49:48Z

Added three native DRAFT records, bringing the maintained collection to 352.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:MixtureDensityNetwork](../../data/curated/MixtureDensityNetwork.yaml) | A neural conditional-density architecture whose input-dependent outputs parameterize the mixing weights and component distributions of a finite mixture over target variables. |
| [AIMech:RealValuedNeuralAutoregressiveDensityEstimator](../../data/curated/RealValuedNeuralAutoregressiveDensityEstimator.yaml) | A fully visible neural autoregressive density architecture for real-valued vectors that shares input-to-hidden parameters across ordered scalar conditional mixture-density models. |
| [AIMech:DocumentNADE](../../data/curated/DocumentNADE.yaml) | A neural autoregressive document model that predicts successive words from shared additive embeddings of the preceding words, using normalized word conditionals and a deterministic document representation. |

Mixture density networks map broadly to ArtificialNeuralNetwork; RNADE and Document NADE map broadly to BayesianNetwork. Document NADE also has a related mapping to the AIO topic-model context. The records distinguish conditional density from a point prediction, deterministic hidden features from latent variables, and ordered sequence probabilities from symmetrized or count probabilities.

The [finite examples](density-document-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 195 pending inspection leads.
