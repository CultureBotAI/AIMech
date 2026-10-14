# Tempered transitions

Added [the DRAFT native record](../../data/curated/TemperedTransitions.yaml) with an explicit related Markov-process AIO mapping.

Add tempered transitions as a target-preserving up/down Markov kernel, with mutually reversed base kernels, full-path acceptance, canceled normalizers and explicit failures of endpoint-only acceptance or arbitrary nonreversible return scans.

[Finite curator calculations](tempered-boundaries.py) check full-path balance, canceled density scales and invalid endpoint-only or nonreversed-kernel alternatives. The [structured report](20261014T194707Z-tempered-transitions.json) retains source-version boundaries, inspected scope and the incomplete discovery frontier.
