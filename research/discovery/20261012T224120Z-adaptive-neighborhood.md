# Adaptive-neighborhood sparse-spectrum regression

Added [Two-stage adaptive-neighborhood sparse-spectrum regression](../../data/curated/TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.yaml) as a DRAFT native algorithm with an explicit related AIO regression mapping.

The fully read Tan preprint specifies two local fits: Euclidean neighbors first, followed by full-training-set reselection using squared posterior-mean inverse-lengthscales. [Exact finite arithmetic](adaptive-neighborhood-boundaries.py) distinguishes this from posterior-second-moment weighting; no fitting or benchmark was run.

The 735-entry main frontier retains 485 pending and 56 partly addressed cohorts. The [structured report](20261012T224120Z-adaptive-neighborhood.json) preserves source limitations, title-only leads and the separate unresolved NCVMP fitting cohort.
