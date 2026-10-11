# Guided-search extensions — 2026-10-11T14:43:22Z

Added three native DRAFT records, bringing the maintained collection to 310.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:GENET](../../data/curated/GENET.yaml) | A connectionist architecture for finite constraint satisfaction that represents variable assignments by active label nodes and alternates input-maximizing assignment updates with increased inhibitory weights on violated constraints when the network stabilizes without a solution. |
| [AIMech:ExtendedGuidedLocalSearch](../../data/curated/ExtendedGuidedLocalSearch.yaml) | The Tsang–Mills–Ford extension of Guided Local Search that combines cost-scaled penalty weighting, aspiration for a new best original-objective solution despite an augmented-objective penalty, and probabilistic random neighborhood moves. |
| [AIMech:GuidedGeneticAlgorithm](../../data/curated/GuidedGeneticAlgorithm.yaml) | The Lau–Tsang genetic-search framework that uses shared adaptive solution-feature penalties both to modify fitness and to construct per-chromosome gene weights that bias crossover and mutation. |

GENET has a broad AIO ArtificialNeuralNetwork mapping. EGLS and GGA have bounded no-match assessments. The GGA record preserves missing zero-weight rules and contradictory optimization signs; EGLS retains its parameters and strict aspiration boundary.

The [finite examples](guided-search-extensions-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 181 pending inspection leads.
