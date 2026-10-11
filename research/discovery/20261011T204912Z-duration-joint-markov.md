# Explicit durations and joint Markov models — 2026-10-11T20:49:12Z

Added three native DRAFT model families, bringing the maintained collection to 391.

| Record | Definition |
| --- | --- |
| [AIMech:HiddenSemiMarkovModel](../../data/curated/HiddenSemiMarkovModel.yaml) | A latent-state sequence-model family that assigns explicit distributions to state sojourn durations, with state changes governed by an embedded transition process and observations conditioned on the hidden states. |
| [AIMech:PairwiseMarkovChain](../../data/curated/PairwiseMarkovChain.yaml) | A hidden-state sequence-model family in which the joint process of a hidden variable and its corresponding observation is first-order Markov, without requiring either marginal process to be Markov or observations to be conditionally independent given the hidden path. |
| [AIMech:TripletMarkovChain](../../data/curated/TripletMarkovChain.yaml) | A latent-variable sequence-model family that introduces an auxiliary process so that the joint hidden, auxiliary and observed process is first-order Markov, while the hidden–observed pair obtained by marginalizing the auxiliary process need not be Markov. |

The [finite examples](duration-joint-markov-boundaries.py) check duration censoring, joint versus marginal Markov behavior and auxiliary-state marginalization. The ledger preserves all 21 primary PDF pages read, source-version distinctions, ignored-inclusive identity searches and directional AIO mappings.

Adversarial author self-review is required. Discovery remains active with 215 pending inspection leads and carried unresolved dispositions.
