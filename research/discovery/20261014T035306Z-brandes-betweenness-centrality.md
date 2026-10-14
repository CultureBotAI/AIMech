# Brandes betweenness centrality computation

Added [the DRAFT native record](../../data/curated/BrandesBetweennessCentrality.yaml) with an explicit AIO no-match assessment.

Add the Brandes exact vertex-betweenness computation as a reusable graph-analysis algorithm, distinguishing its shortest-path dependency accumulation from the centrality index, community edge removal, and random-walk ranking.

[Exact constructed examples](brandes-betweenness-boundaries.py) distinguish shortest-path fractions, endpoint exclusion, undirected halving and length conventions. The [structured report](20261014T035306Z-brandes-betweenness-centrality.json) preserves the incomplete discovery frontier.

Corrected two preliminary research notes under [issue #340](https://github.com/CultureBotAI/AIMech/issues/340): the primary paper prints the correct dependency ratio. The earlier misreading and its initial structured finding are preserved as history.
