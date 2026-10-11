# Mean-field learning and context-sensitive sequence models — 2026-10-11T20:34:41Z

Added three native DRAFT concepts, bringing the maintained collection to388.

| Record | Definition |
| --- | --- |
| [AIMech:MeanFieldBoltzmannLearning](../../data/curated/MeanFieldBoltzmannLearning.yaml) | A deterministic approximation to Boltzmann-machine parameter learning that substitutes mean-field phase statistics for stochastic equilibrium correlations in the positive-minus-negative weight update. |
| [AIMech:ContextSensitiveEmissionHiddenMarkovModel](../../data/curated/ContextSensitiveEmissionHiddenMarkovModel.yaml) | A hidden-state sequence-model family with a first-order Markov prior whose observation distributions depend jointly on hidden states at multiple temporal positions, introducing context beyond the contemporaneous hidden state. |
| [AIMech:HiddenMarkovModelWithAuxiliaryMemory](../../data/curated/HiddenMarkovModelWithAuxiliaryMemory.yaml) | A hidden-state symbol-sequence model family in which paired states write emitted symbols to auxiliary memory and later read them to condition emissions and memory-dependent state transitions. |

Adaptive local experts substantially overlaps the existing MDN and HME records. Its alternative objectives and parameterization differences are retained in the JSON disposition; no duplicate ID or unconditional synonym was added.

The [finite examples](mean-field-context-boundaries.py) check phase-bound differences, contextual-emission normalization and indexing, and stack/queue memory constraints. The ledger preserves five PDF reading scopes, separate author/journal versions, ignored-inclusive identity searches and AIO mapping rationales.

Adversarial author self-review is required. Discovery remains active with212 pending inspection leads and carried unresolved dispositions.
