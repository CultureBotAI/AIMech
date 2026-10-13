# Real-time recurrent learning

Added [Real-time recurrent learning](../../data/curated/RealTimeRecurrentLearning.yaml) as a DRAFT native algorithm with an explicit AIO mapping assessment.

The complete Williams/Zipser1989 manuscript supports forward state sensitivities and their use for recurrent weight updates. Fixed-weight exact gradients are distinguished from online weight drift; target substitution changes derivative paths. Tensor size, nonlocality and source-limited small-network demonstrations remain explicit.

[Constructed checks](rtrl-boundaries.py) illustrate mathematical boundaries without author-code execution or fitting. The [structured report](20261013T061904Z-real-time-recurrent-learning.json) resolves the prior nested lead and retains ongoing discovery.
