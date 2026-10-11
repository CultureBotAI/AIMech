# Graph clustering and N-pair losses — 2026-10-11T09:34:40Z

Added five native DRAFT concepts; AIMech now contains223 maintained records.

| Record | Scope |
| --- | --- |
| [AIMech:PowerIterationClustering](../../data/curated/PowerIterationClustering.yaml) | A clustering algorithm that uses an early-stopped power iteration of a normalized similarity matrix to embed observations and then applies k-means to their embedding coordinates. |
| [AIMech:ZetaMerging](../../data/curated/ZetaMerging.yaml) | An agglomerative graph-clustering algorithm that selects the pair with the largest sum of conditional increases in average log-diagonal resolvent popularity. |
| [AIMech:CHAMELEONClustering](../../data/curated/CHAMELEONClustering.yaml) | A graph-clustering procedure that first partitions a sparse neighbor graph into small subclusters and then agglomerates them using interconnectivity and closeness normalized by their internal bisection statistics. |
| [AIMech:MultiClassNPairLoss](../../data/curated/MultiClassNPairLoss.yaml) | A supervised metric-learning objective that averages a joint positive-versus-multiple-negative log-softmax loss across a batch of positive pairs drawn from distinct classes. |
| [AIMech:OneVsOneNPairLoss](../../data/curated/OneVsOneNPairLoss.yaml) | A supervised metric-learning objective that sums separate positive-versus-negative softplus comparisons for each anchor in a batch of positive pairs from distinct classes. |

Power iteration clustering uses a truncated embedding iteration; it is distinct from path integral clustering. Zeta merging is the well-specified agglomerative component of Zell; the full composition remains pending source clarification. CHAMELEON preserves the two-phase graph method and its two documented merge alternatives. N-pair-mc and N-pair-ovo retain different aggregation rules.

Source review found paper/code differences in power-iteration stopping and a false printed Zeta popularity inequality. An original [finite calculation](zeta-popularity-bound.py) checks the latter. The N-pair supplemental link contains another paper and was excluded. CHAMELEON evidence comes from the22page author technical report, not the final journal PDF.

Review issues [51](https://github.com/CultureBotAI/AIMech/issues/51) and [52](https://github.com/CultureBotAI/AIMech/issues/52) address calculation provenance, the overly broad N-pair alias and unsupported symmetry-aggregation wording. The JSON records actual correction times and hashes.

Mappings preserve task/objective scope and supervised-versus-self-supervised distinctions. Review is author self-review; no benchmark was reproduced. The inherited frontier, full Zell and new primary-reference leads keep discovery active.

[Issue53](https://github.com/CultureBotAI/AIMech/issues/53) corrected a spurious Section2.5 citation to the actual Sections2.1–2.4 in the power-iteration paper.
