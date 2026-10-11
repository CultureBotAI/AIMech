# Contrastive-divergence training — 2026-10-11T19:18:34Z

Added three native DRAFT algorithm records, bringing the maintained collection to 373.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:ContrastiveDivergence](../../data/curated/ContrastiveDivergence.yaml) | A parameter-learning algorithm for energy-based or product-of-experts models that replaces the equilibrium negative-phase expectation by configurations obtained from a short model-invariant Markov chain restarted at observed data, without differentiating through the chain distribution. |
| [AIMech:PersistentContrastiveDivergence](../../data/curated/PersistentContrastiveDivergence.yaml) | A learning algorithm that estimates an energy model’s negative-phase statistics with Markov chains whose states persist across parameter updates, rather than restarting those chains at the current data minibatch. |
| [AIMech:FastPersistentContrastiveDivergence](../../data/curated/FastPersistentContrastiveDivergence.yaml) | A persistent-chain RBM learning algorithm that adds rapidly updated, rapidly decaying auxiliary parameters to the sampling energy while retaining separate regular parameters for the model distribution. |

All three algorithms relate to the RBM model family they train and the Markov transitions supplying negative statistics. These are algorithm/model and algorithm/process associations, not forced subclasses of architectures or tasks.

The [finite examples](contrastive-training-boundaries.py) and JSON ledger document actual source reading, identity and mapping checks, formal-objective versus update distinctions, persistent-chain tracking and fast-overlay/pseudocode qualifications, and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 203 pending inspection leads.
