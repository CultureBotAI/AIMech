# Multimodal harmonium boundaries — 2026-10-12T01:14:39Z

Added three native DRAFT model families, bringing the maintained collection to 447.

| Record | Defining structure |
| --- | --- |
| [RAP](../../data/curated/RateAdaptingPoissonModel.yaml) | Poisson counts with bounded binomial hidden variables |
| [FoH](../../data/curated/FamilyOfHarmonium.yaml) | Separately normalized class-specific multimodal harmoniums |
| [HH](../../data/curated/HierarchicalHarmonium.yaml) | Shared latent topics coupled to binary labels |

All 29 primary PDF pages were visually read. [Finite calculations](multimodal-harmonium-boundaries.py) check 96 RAP conditional probabilities, normalization and gradients, class-normalizer ranking reversal, and binary versus one-hot label support. No author implementation or benchmark ran.

The original unbounded Poisson/Gaussian dual-wing specialization is deferred: integrating its hidden variables yields divergent quadratic count tails. Binary observations do not repair its model support.

Ten new provisional cohorts leave329 pending leads and other unresolved dispositions; discovery continues.
