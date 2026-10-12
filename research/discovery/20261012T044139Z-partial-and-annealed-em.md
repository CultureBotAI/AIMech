# Partial and annealed EM — 2026-10-12T04:41:39Z

Added four native DRAFT algorithms, bringing the maintained collection to 480.

| Record | Scope |
| --- | --- |
| [Generalized Expectation Maximization](../../data/curated/GeneralizedExpectationMaximization.yaml) | Exact-current-E, partial-Q improvement |
| [Incremental Expectation Maximization](../../data/curated/IncrementalExpectationMaximization.yaml) | Selected-case posterior cache refresh |
| [Sparse Expectation Maximization](../../data/curated/SparseExpectationMaximization.yaml) | Frozen outside mass with plausible-set updates |
| [Deterministic Annealing Expectation Maximization](../../data/curated/DeterministicAnnealingExpectationMaximization.yaml) | Warm-started deterministic cooling to inverse temperature one |

All 26 pages containing the three primary sources were visually read. Definitions preserve the differences between expected-objective ascent, cached-bound ascent and observed likelihood. The published incremental-EM correction and annealing source discrepancies remain explicit. [Finite calculations](partial-and-annealed-em-boundaries.py) check these boundaries.

DAEM shares fixed-temperature updates with tempered EM; its separate record denotes the named outer cooling procedure. Related AIO task mappings assert no upstream subclass relation.

Two provisional cohorts leave 405 pending frontier entries and other unresolved dispositions. Discovery continues.
