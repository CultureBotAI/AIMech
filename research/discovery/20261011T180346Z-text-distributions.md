# Document models and hierarchical word probabilities — 2026-10-11T18:03:46Z

Added three native DRAFT records, bringing the maintained collection to 355.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:ReplicatedSoftmax](../../data/curated/ReplicatedSoftmax.yaml) | An undirected document model with binary hidden units and a length-dependent set of categorical word units that share visible-to-hidden weights, with hidden biases scaled by document length. |
| [AIMech:SparseAdditiveGenerativeModel](../../data/curated/SparseAdditiveGenerativeModel.yaml) | A generative model family for categorical text data that forms word probabilities by normalizing a background log-frequency vector plus sparse component deviations, allowing multiple generative facets to combine additively in log space. |
| [AIMech:HierarchicalSoftmax](../../data/curated/HierarchicalSoftmax.yaml) | A neural categorical-output component that assigns a probability to each vocabulary leaf by multiplying normalized branch probabilities along its path through a word tree. |

Replicated Softmax broadly maps to RestrictedBoltzmannMachine; it and SAGE have related mappings to the topic-model task context. Hierarchical softmax broadly maps to OutputLayer. The records separate latent-state document models, additive log-frequency deviations, and tree output probabilities.

The [finite examples](text-distributions-boundaries.py) and JSON ledger document actual reading, identity and mapping checks, source-equation qualifications and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 197 pending inspection leads.
