# Graph linkage and contrastive loss — 2026-10-11T09:17:17Z

Added four native DRAFT records; AIMech now contains218 maintained concepts.

| Record | Scope |
| --- | --- |
| [AIMech:GraphDegreeLinkage](../../data/curated/GraphDegreeLinkage.yaml) | An agglomerative clustering algorithm that merges the pair with greatest symmetric graph-degree affinity, formed by summing products of cluster-normalized incoming and outgoing edge weights on a fixed directed nearest-neighbor graph. |
| [AIMech:AcceleratedGraphDegreeLinkage](../../data/curated/AcceleratedGraphDegreeLinkage.yaml) | An approximate graph degree linkage algorithm that selects merges from maintained cluster-neighbor sets and updates those sets locally instead of searching every current cluster pair. |
| [AIMech:PathIntegralClustering](../../data/curated/PathIntegralClustering.yaml) | An agglomerative clustering algorithm that merges clusters with the greatest increase in their size-normalized sums of discounted random-walk paths when paths are allowed through the proposed union. |
| [AIMech:NTXentLoss](../../data/curated/NTXentLoss.yaml) | A contrastive cross-entropy objective that uses cosine-normalized, temperature-scaled similarities to identify a paired positive representation among nonself candidates, including that positive in the denominator. |

GDL uses all-pair degree-product linkage; AGDL restricts candidate search. Path integral clustering uses conditional discounted-path increments with the original cluster normalizations. NT-Xent specializes the contrastive categorical loss and is distinct from the complete SimCLR procedure.

The [JULE correction](../../data/curated/JointUnsupervisedLearning.yaml) addresses [issue48](https://github.com/CultureBotAI/AIMech/issues/48): an unrelated IMSAT qualifier was removed from its clustering-task rationale. Initial validation also caught and removed a redundant NT-Xent spelling alias.

Mappings retain algorithm-to-task and objective-to-approach scope. Review remains author self-review; no benchmark was reproduced.

Power iteration clustering, Zell, CHAMELEON, contrastive-loss references and older unresolved leads remain in the JSON frontier. Discovery is ongoing.

[Issue49](https://github.com/CultureBotAI/AIMech/issues/49) added the primary InfoNCE derivation as directly cited context for NT-Xent’s sampling caveat. The qualification is curator inference; it does not rule out alternative bounds.
