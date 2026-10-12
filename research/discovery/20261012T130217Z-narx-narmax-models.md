# NARX and NARMAX models

Added two DRAFT model families: [NARX](../../data/curated/NonlinearAutoregressiveExogenousModel.yaml) and [NARMAX](../../data/curated/NonlinearAutoregressiveMovingAverageExogenousModel.yaml). AIMech now has 530 native concepts and 442 unchanged AIO records.

The complete 1989 representation paper and OLS companion support the definitions. [Exact calculations](narx-narmax-boundaries.py) preserve the distinction between current and lagged errors, local output branches, coefficient linearity and residual initialization. They also contradict a specific published approximation bound; the records retain that source caveat.

Discovery continues with 468 pending and 47 partly addressed cohorts. Original realization proofs, input-free time-series models, rational/output-affine forms, prediction-error estimation and Volterra/block models remain source leads. The original Documents checkout still needs restored OS access for synchronization.
