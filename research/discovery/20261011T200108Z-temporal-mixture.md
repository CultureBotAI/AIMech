# Temporal mixture and energy models — 2026-10-11T20:01:08Z

Added three native DRAFT model families, bringing the maintained collection to382.

| Record | Definition |
| --- | --- |
| [AIMech:HiddenMarkovDecisionTree](../../data/curated/HiddenMarkovDecisionTree.yaml) | A conditional latent sequence-model family that extends a probabilistic hierarchical decision tree by coupling each decision level to the same level at the previous time. |
| [AIMech:MixedMemoryMarkovModel](../../data/curated/MixedMemoryMarkovModel.yaml) | A family of compact temporal probability models whose component transition distributions are convex mixtures of transition tables indexed by a single selected predecessor lag or component. |
| [AIMech:BoltzmannChain](../../data/curated/BoltzmannChain.yaml) | A family of tied-weight undirected Boltzmann sequence models with hidden temporal variables, observed variables and chain-derived connectivity chosen to permit exact elimination. |

HMDT and mixed-memory models have broad Bayesian-network mappings; Boltzmann chains have a broad Boltzmann-machine mapping. Related tree/process mappings preserve abstraction and endpoint distinctions.

The [finite examples](temporal-mixture-boundaries.py) and JSON ledger preserve reading of33PDF pages, identity and mapping checks, mixture restrictions, exact elimination and terminal-conditioned HMM equivalence. Markov mixtures of experts overlap the existing IOHMM family; no duplicate record or exact alias was added.

Adversarial author self-review is required. Discovery remains active with210 pending inspection leads and carried unresolved dispositions.
