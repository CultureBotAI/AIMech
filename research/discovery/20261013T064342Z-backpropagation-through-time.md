# Backpropagation through time

Added [Backpropagation through time](../../data/curated/BackpropagationThroughTime.yaml) as a DRAFT native algorithm with an explicit AIO mapping assessment.

The complete Werbos1990 treatment supports reverse differentiation of finite dynamic trajectories with shared parameters. Direct loss terms, initial-state derivatives, boundary conditions, storage and optimizer scope remain explicit; constructed checks distinguish a complete derivative from a detached-boundary surrogate.

[Constructed checks](bptt-boundaries.py) illustrate mathematical boundaries without author-code execution or fitting. The [structured report](20261013T064342Z-backpropagation-through-time.json) resolves the prior nested lead and retains ongoing discovery.
