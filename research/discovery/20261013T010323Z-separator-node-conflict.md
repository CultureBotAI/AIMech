# Separator-node conflict diagnostic

Added [the general separator-node diagnostic](../../data/curated/SeparatorNodeConflictDiagnostic.yaml) as a DRAFT algorithm with related AIO Bayesian-network context. It makes the evidence partition, reference priors, nuisance dependence and choice of conflict score explicit.

[Constructed score checks](separator-conflict-boundaries.py) show that symmetric unimodal radial and density-level scores can differ, and that nonlinear separator scales can change density scoring while preserving signed comparisons. These are not reproductions of source experiments.

The [structured report](20261013T010323Z-separator-node-conflict.json) retains the discovery frontier, the full reading of a later multiple-testing paper, and five additional source leads. Discovery remains incomplete.
