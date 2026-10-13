# INLA group node conflict diagnostic

Added [the group-wise INLA diagnostic](../../data/curated/INLAGroupNodeConflictDiagnostic.yaml) as a DRAFT algorithm with related Bayesian-network context. It compares a group’s latent linear predictors with the remaining data using two INLA fits.

The record distinguishes the intended diagnostic from the pinned software’s posterior-as-prior updating and inconsistent rank thresholds. [Constructed checks](inla-conflict-boundaries.py) illustrate nuisance weighting, covariance pairing and rank conventions; no R-INLA model was executed.

The [structured report](20261013T013528Z-inla-group-node-conflict.json) preserves primary reading, precise source-code locations, identity assessment and pending leads. Discovery remains incomplete.
