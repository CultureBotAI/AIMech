# Shared inverse-lengthscale spectral inference

Added [the Tan base inference procedure](../../data/curated/SharedInverseLengthscaleVariationalSparseSpectrumInference.yaml) as a DRAFT algorithm with an explicit related AIO regression mapping. It uses a shared Gaussian inverse-lengthscale factor, full Gaussian coefficients and half-Cauchy-derived scale coordinates.

[Finite calculations](shared-spectrum-boundaries.py) check moment dependence, normalization, coefficient and derivative algebra, and predictive variance. The source notation issues are explicit; the adaptive controller remains pending. No author implementation or fitting loop was run.

The [structured report](20261012T233132Z-shared-spectrum-inference.json) preserves 484 pending and 57 partly addressed main-frontier cohorts. Discovery remains incomplete.
