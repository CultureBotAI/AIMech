# Fixed-length counts and topic models — 2026-10-11T23:06:04Z

Added three native DRAFT concepts, bringing the maintained collection to 418.

| Record | Definition |
| --- | --- |
| [AIMech:FixedLengthPoissonMarkovRandomField](../../data/curated/FixedLengthPoissonMarkovRandomField.yaml) | A finite-total count distribution whose probability on nonnegative integer vectors summing to a specified total is proportional to a Poisson factorial base measure times exponentiated linear and symmetric quadratic count potentials. |
| [AIMech:FixedLengthPoissonMRFTopicModel](../../data/curated/FixedLengthPoissonMRFTopicModel.yaml) | A probabilistic topic model that allocates a document total among topics, draws an independent fixed-length Poisson-MRF count vector for each allocated topic total, and sums those latent vectors to produce the observed document counts. |
| [AIMech:AdmixtureOfPoissonMarkovRandomFields](../../data/curated/AdmixtureOfPoissonMarkovRandomFields.yaml) | A probabilistic topic-model family that draws each document from a proper Poisson-MRF base distribution whose canonical unary and interaction parameters are convex combinations of topic parameters under document-specific simplex weights. |

The [original mathematical checks](count-topic-boundaries.py) distinguish finite-total support, token updates, parameter mixing and topic-count composition. All 23 source PDF pages were visually read; specified extracted pages were also inspected.

The ledger preserves ignored-inclusive identity searches, directional AIO mappings, source qualifications and explicit follow-up references. Adversarial author self-review is required. Discovery remains active with 249 pending leads plus other unresolved dispositions.
