# Sequence sampling and diverse beam search — 2026-10-11T16:13:52Z

Added three native DRAFT records, bringing the maintained collection to 331.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:GumbelTopKTrick](../../data/curated/GumbelTopKTrick.yaml) | A categorical sampling construction that adds independent standard Gumbel noise to each category’s log weight and returns the indices of the k largest perturbed values in descending order, producing an ordered sample without replacement under successive renormalization of the remaining weights. |
| [AIMech:StochasticBeamSearch](../../data/curated/StochasticBeamSearch.yaml) | The sequence-sampling algorithm of Kool, van Hoof and Welling that implements Gumbel-Top-k without replacement implicitly on a locally normalized sequence tree by propagating conditional perturbed subtree maxima and retaining the k highest-scoring prefixes at each level. |
| [AIMech:DiverseBeamSearch](../../data/curated/DiverseBeamSearch.yaml) | The inference procedure of Vijayakumar and colleagues that partitions a sequence beam budget into groups and updates each group using model log-probability scores augmented by a weighted dissimilarity to the already-updated earlier groups at the same decoding step. |

Gumbel-Top-k has a bounded AIO no-match assessment. The two decoders have related application mappings to NaturalLanguageProcessing. Exact without-replacement sampling is distinct from soft diversity scoring; finite examples preserve the ordered/inclusion-probability distinction, conditional maxima and separate beam-group boundaries.

The [finite examples](sequence-sampling-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 187 pending inspection leads.
