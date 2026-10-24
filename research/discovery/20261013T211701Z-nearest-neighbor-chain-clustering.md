# Nearest-neighbor-chain clustering

Added [Nearest-neighbor-chain clustering](../../data/curated/NearestNeighborChainClustering.yaml) as a DRAFT native algorithm with an explicit AIO mapping assessment.

Add nearest-neighbor-chain clustering as a DRAFT algorithm with related hierarchical and unsupervised clustering mappings. Preserve reducibility plus disjoint-merge commutation, predecessor ties, sorted/relabelled output, matrix complexity and inspected implementation boundaries.

[Constructed checks](nearest-neighbor-chain-clustering-boundaries.py) illustrate mathematical boundaries without author-code execution or fitting. The [structured report](20261013T211701Z-nearest-neighbor-chain-clustering.json) updates the corresponding discovery lead and retains ongoing discovery.

Review correction ([#312](https://github.com/CultureBotAI/AIMech/issues/312)): Figure 4 prints `length(chain) ≤ 3`, consistent with the pinned code. The earlier `<3` reading and alleged three-entry indexing defect were curator errors and are rejected. The calculation now checks the actual guard. The structured report records this correction and explicitly supersedes the preliminary suspicion in the preceding Ward discovery report; historical reports remain unchanged.
