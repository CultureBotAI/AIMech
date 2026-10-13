# Stochastic nonconjugate GLMM variational inference

Added [the finite-population stochastic GLMM procedure](../../data/curated/StochasticNonconjugateGLMMVariationalInference.yaml) as a DRAFT algorithm with a related AIO random-effects mapping. The record follows the simultaneous natural-gradient derivation and retains the appendix’s complete covariance target. Source pseudocode and sampling discrepancies are explicit.

[Finite arithmetic](stochastic-glmm-boundaries.py) checks fixed-state minibatch weighting, natural-parameter mixing and the local-covariance correction. Both primary papers were read in full; no local optimization, author code or model fitting was run.

The [structured report](20261013T001117Z-stochastic-nonconjugate-glmm-inference.json) retains 484 pending and 57 partly addressed main-frontier cohorts. Message-conflict diagnostics and further source inventories remain pending.

Author review clarified that both papers contain the malformed normal-weight display. The normalized construction is specifically the 2013 Appendix B on PDF pages19–20. The expectation itself is unchanged; https://github.com/CultureBotAI/AIMech/issues/218 tracks the correction and successor review.
