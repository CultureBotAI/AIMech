# Variational message passing

Added [VMP](../../data/curated/VariationalMessagePassing.yaml) as a DRAFT algorithm with a related AIO Bayesian-network mapping. The full original 34-page paper was read. The record separates exact conjugate coordinate updates from auxiliary-bound and sampling extensions and preserves source inconsistencies.

[Finite calculations](vmp-boundaries.py) check message routing, the Gaussian variance term and a stationary saddle. No author implementation or source experiment was run.

The [structured report](20261012T231014Z-variational-message-passing.json) retains 485 pending and 56 partly addressed main-frontier cohorts and additional incompletely assessed source leads.

Author review identified a minor terminology omission. The bound-accounting claim now explicitly names log model evidence, log p(v), consistently with the earlier equation and primary source; https://github.com/CultureBotAI/AIMech/issues/211 tracks the correction and successor review.
