# Variational sparse-spectrum inference

Added three DRAFT algorithms with explicit related AIO regression mappings:

- [Variational sparse-spectrum Gaussian-process inference](../../data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml) (VSSGP).
- [Factorized variational sparse-spectrum Gaussian-process inference](../../data/curated/FactorizedVariationalSparseSpectrumGaussianProcessInference.yaml) (fVSSGP).
- [Stochastic factorized variational sparse-spectrum Gaussian-process inference](../../data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml) (sfVSSGP).

Their distinct coefficient families and minibatch objectives follow the fully read main paper and supplement. The pinned author code was read without execution; its fixed phases are distinguished from paper phase integration. [Finite arithmetic](vssgp-boundaries.py) checks bound and moment boundaries, not empirical performance.

There are 549 native and 442 unchanged generated records. The main frontier has 486 pending and 56 partly addressed cohorts; discovery remains incomplete. Tan and Hoang source concerns and further leads are preserved in the [structured report](20261012T222135Z-variational-sparse-spectrum.json).

Author review identified a minor notation omission in sfVSSGP. Its minibatch claim now defines the per-observation expected-log-likelihood summand; https://github.com/CultureBotAI/AIMech/issues/206 tracks the correction and successor review.
