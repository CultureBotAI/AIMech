# Neural word-probability architectures — 2026-10-11T18:16:19Z

Added three native DRAFT records, bringing the maintained collection to 358.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:HierarchicalProbabilisticNeuralNetworkLanguageModel](../../data/curated/HierarchicalProbabilisticNeuralNetworkLanguageModel.yaml) | A neural next-word architecture that factors word probabilities along a binary vocabulary tree and shares a nonlinear branch predictor conditioned on context-word embeddings and a separate embedding of the current tree node. |
| [AIMech:LogBilinearLanguageModel](../../data/curated/LogBilinearLanguageModel.yaml) | A next-word language architecture that linearly combines position-specific transforms of context-word embeddings and normalizes their bilinear compatibility with candidate-word embeddings over the vocabulary. |
| [AIMech:HierarchicalLogBilinearLanguageModel](../../data/curated/HierarchicalLogBilinearLanguageModel.yaml) | A next-word language architecture that computes one linear context feature vector and uses its dot products with internal-node vectors to assign normalized vocabulary-tree probabilities, summing path probabilities when a word has multiple codes. |

Each architecture broadly maps to AIO AutoregressiveLanguageModel. The records preserve nonlinear node-conditioned features, tied bilinear word embeddings and reusable linear context features with tree outputs as separate constructions.

The [finite examples](language-architectures-boundaries.py) and JSON ledger document actual source reading, identity and mapping checks, transpose and gradient conventions, and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 199 pending inspection leads.
