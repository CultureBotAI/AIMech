# Metric neighbors and representative clustering — 2026-10-11T09:47:08Z

Added four native DRAFT concepts; AIMech now contains227 maintained records.

| Record | Scope |
| --- | --- |
| [AIMech:NeighborhoodComponentsAnalysis](../../data/curated/NeighborhoodComponentsAnalysis.yaml) | A supervised metric-learning algorithm that learns a linear transformation by maximizing the expected number of correctly classified training examples under stochastic leave-one-out neighbor selection. |
| [AIMech:LiftedStructuredEmbeddingLoss](../../data/curated/LiftedStructuredEmbeddingLoss.yaml) | A metric-learning objective that penalizes a positive pair’s Euclidean distance against negative distances incident to either endpoint, using a squared hinge and a hard maximum or its log-sum-exp relaxation. |
| [AIMech:CUREClustering](../../data/curated/CUREClustering.yaml) | An agglomerative clustering procedure that represents each cluster by several scattered points shrunk toward its mean and merges the pair with the smallest distance between their representative points. |
| [AIMech:ROCKClustering](../../data/curated/ROCKClustering.yaml) | An agglomerative clustering procedure that merges clusters using shared-neighbor link counts divided by a cluster-size normalization derived from a neighborhood model. |

NCA learns a supervised linear metric through stochastic neighbor selection. Lifted structured embedding loss contrasts both endpoints of each positive pair and keeps its full-data hard-max and minibatch log-sum-exp scopes separate. CURE uses shrunk representative points; its faster representative-reuse step is qualified. ROCK uses size-normalized shared-neighbor links and may stop before the requested count when links vanish.

[Issue55](https://github.com/CultureBotAI/AIMech/issues/55) corrects the lifted objective’s full-data versus minibatch scope. A [finite neighbor calculation](rock-neighbor-counts.py) reproduces ROCK’s worked counts only when each point is excluded from its own neighborhood. It is not a clustering benchmark.

Original primary PDFs were read, including the scanned ROCK article. The lifted CPU loss file was read at a pinned author commit without execution. Mappings retain task/network and supervision distinctions; all concepts remain DRAFT.

The inherited discovery frontier and new RCA, metric-learning, BIRCH, CLARANS and expanded-ROCK leads remain active. No saturation claim is made.
