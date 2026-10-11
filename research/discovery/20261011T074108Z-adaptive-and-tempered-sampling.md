# Adaptive and tempered sampling — 2026-10-11T07:41:08Z

Added six concepts; AIMech now contains 187 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:AdaptiveMetropolis](../../data/curated/AdaptiveMetropolis.yaml) | A history-adaptive random-walk Metropolis sampler whose Gaussian proposal covariance is estimated from the accumulated retained states, including repetitions after rejected proposals. |
| [AIMech:DelayedRejectionAdaptiveMetropolis](../../data/curated/DelayedRejectionAdaptiveMetropolis.yaml) | An adaptive Metropolis procedure combining history-based Gaussian proposal covariance updates between transitions with corrected delayed-rejection proposal stages within a transition. |
| [AIMech:AdaptiveScalingMetropolis](../../data/curated/AdaptiveScalingMetropolis.yaml) | A random-walk Metropolis algorithm that adapts its proposal scale through stochastic approximation driven by the proposal acceptance probability relative to a chosen target rate. |
| [AIMech:AdaptiveScalingWithinAdaptiveMetropolis](../../data/curated/AdaptiveScalingWithinAdaptiveMetropolis.yaml) | An adaptive Metropolis algorithm that combines acceptance-rate-driven scalar proposal scaling with recursive mean and covariance-shape adaptation from retained samples. |
| [AIMech:ParallelTempering](../../data/curated/ParallelTempering.yaml) | A population Monte Carlo method that combines within-temperature target-preserving updates with corrected exchanges between replicas targeting differently tempered densities. |
| [AIMech:AdaptiveParallelTempering](../../data/curated/AdaptiveParallelTempering.yaml) | A parallel-tempering algorithm that adapts temperature gaps and within-replica random-walk proposal parameters through projected stochastic approximation. |

All six have qualified related mappings to AIO Markov Chain. Adaptive sampled-state history is not asserted to be a homogeneous Markov chain.

The source audit distinguishes covariance from scale adaptation, probabilities from binary acceptances, standard-deviation from variance scaling, and fixed from adaptive temperature ladders. Projection assumptions and source-version differences remain explicit.

AM uses original indexed method text and a later visually inspected primary treatment. DRAM uses pinned author implementation; original-article access remains a follow-up.

Rao-Blackwellized adaptation, simulated tempering, Wang–Landau, particle methods and the broader carried frontier remain open. Six additions do not establish saturation.
