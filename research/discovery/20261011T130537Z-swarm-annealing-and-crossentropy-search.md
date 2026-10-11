# Swarm, annealing and cross-entropy search — 2026-10-11T13:05:37Z

Added three native DRAFT concepts, bringing the maintained collection to 288.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:ParticleSwarmOptimization](../../data/curated/ParticleSwarmOptimization.yaml) | A population-based optimization method that moves candidate particles through a search space using retained velocities and stochastic attraction toward remembered personal and shared best positions. |
| [AIMech:SimulatedAnnealing](../../data/curated/SimulatedAnnealing.yaml) | A stochastic optimization procedure that explores candidate configurations with temperature-controlled acceptance of cost-increasing moves and progressively cools that acceptance process to concentrate search on low-cost configurations. |
| [AIMech:CrossEntropyOptimization](../../data/curated/CrossEntropyOptimization.yaml) | A stochastic optimization method that iteratively samples a parameterized search distribution, selects high-performing samples using an adaptive threshold, and refits the distribution by maximum likelihood on those selected samples. |

The records distinguish remembered particle motion, temperature-controlled accept/reject search and elite-sample distribution fitting. Source-specific inertia, proposal symmetry, quantile conventions and finite-run limitations remain explicit.

Simulated annealing has a qualified AIO Markov-chain relation. PSO and cross-entropy optimization have bounded no-match assessments. The [finite calculation](stochastic-optimization-boundaries.py) illustrates the recorded boundaries. The JSON ledger preserves source versions, actual text/OCR/image reading scopes, identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
