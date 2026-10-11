# Latent and nonlinear word models — 2026-10-11T18:27:34Z

Added three native DRAFT records, bringing the maintained collection to 361.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:FactoredRestrictedBoltzmannMachineLanguageModel](../../data/curated/FactoredRestrictedBoltzmannMachineLanguageModel.yaml) | A conditional neural word model that factorizes position-specific word-to-hidden weights through a shared word-embedding matrix and couples the next categorical word to binary hidden units in a context-conditioned restricted Boltzmann machine. |
| [AIMech:TemporalFactoredRestrictedBoltzmannMachineLanguageModel](../../data/curated/TemporalFactoredRestrictedBoltzmannMachineLanguageModel.yaml) | A sequential extension of the factored RBM language model that directs information from the preceding binary hidden state into the current hidden bias, propagating context beyond the explicit word window. |
| [AIMech:NeuralProbabilisticLanguageModel](../../data/curated/NeuralProbabilisticLanguageModel.yaml) | A neural finite-context language architecture that jointly learns a shared word-embedding lookup and a nonlinear predictor of the next-word distribution using concatenated context embeddings and a vocabulary softmax. |

Each architecture broadly maps to AIO AutoregressiveLanguageModel. FRBM records also relate to RestrictedBoltzmannMachine through their current word–hidden interaction. Exact conditional normalization, approximate temporal filtering and deterministic nonlinear prediction remain distinct.

The [finite examples](neural-word-models-boundaries.py) and JSON ledger document actual source reading, identity and mapping checks, source bias signs, exact versus approximate normalization and gradient conventions, and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 198 pending inspection leads.
