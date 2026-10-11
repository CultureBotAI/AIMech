# Probabilistic inference — 2026-10-11T06:49:09Z

Added six concepts; the native collection now contains 159 DRAFT records.

| Record | Kind |
| --- | --- |
| [AIMech:MetropolisHastings](../../data/curated/MetropolisHastings.yaml) | algorithm |
| [AIMech:BarkerAcceptanceRule](../../data/curated/BarkerAcceptanceRule.yaml) | mathematical_method |
| [AIMech:IndependenceMetropolisHastings](../../data/curated/IndependenceMetropolisHastings.yaml) | algorithm |
| [AIMech:HamiltonianMonteCarlo](../../data/curated/HamiltonianMonteCarlo.yaml) | algorithm |
| [AIMech:OriginalNoUTurnSampler](../../data/curated/OriginalNoUTurnSampler.yaml) | algorithm |
| [AIMech:DualAveragingHamiltonianStepSize](../../data/curated/DualAveragingHamiltonianStepSize.yaml) | algorithm |

Each has a related mapping to AIO Markov Chain, with distinct rationales for samplers, the Barker acceptance rule and step-size warmup. The relation does not assert that a sampling algorithm is a stochastic model or a trained network.

The records separate target invariance from convergence, independent proposals from independent retained draws, and original slice NUTS from later variants. Acceptance and tuning formulas are supported by inspected method passages and rendered equations.

The original 1987 HMC full text was inaccessible through the attempted hosts. Its historical metadata is distinguished from the fully inspected algorithm in the NUTS paper and Neal’s author chapter. All unresolved source leads and earlier frontiers remain open.
