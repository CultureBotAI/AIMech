# Spatial joint Markov models — 2026-10-11T21:03:31Z

Added three native DRAFT model families, bringing the maintained collection to 394.

| Record | Definition |
| --- | --- |
| [AIMech:HiddenObservedPairMarkovRandomField](../../data/curated/HiddenObservedPairMarkovRandomField.yaml) | A latent-variable spatial-model family in which each site contains a hidden label and an observation, and their joint paired field has a normalized Gibbs factorization on a specified neighborhood graph, without requiring either marginal field to be Markov on that graph. |
| [AIMech:TripletMarkovField](../../data/curated/TripletMarkovField.yaml) | A latent-variable spatial-model family that introduces an auxiliary field so the complete hidden, auxiliary and observed triplet has a normalized Gibbs factorization on a specified neighborhood graph, while its hidden–observed projection need not remain Markov on that graph. |
| [AIMech:PairwiseMarkovTree](../../data/curated/PairwiseMarkovTree.yaml) | A latent-variable tree-model family whose paired hidden and observed states factor into a root distribution and parent-to-child conditional kernels on a fixed rooted tree, without requiring the hidden marginal to be Markov on that tree. |

The [finite examples](spatial-joint-markov-boundaries.py) check joint and projected locality, exact tree messages and Gaussian normalization restrictions. The ledger preserves all28primary PDF pages read, source-version discrepancies, ignored-inclusive identity searches and directional AIO mappings.

Adversarial author self-review is required. Discovery remains active with220pending inspection leads and carried unresolved dispositions.
