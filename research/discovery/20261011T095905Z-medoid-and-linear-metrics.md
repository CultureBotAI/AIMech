# Medoid search and linear metrics — 2026-10-11T09:59:05Z

Added three native DRAFT concepts; AIMech now contains 230 maintained records. BIRCH already exists and was not duplicated.

| Record | Scope |
| --- | --- |
| [AIMech:CLARANSClustering](../../data/curated/CLARANSClustering.yaml) | A randomized medoid-clustering algorithm that searches fixed-size sets of representative observations by accepting improving single swaps and restarting after a budget of unsuccessful neighbor trials. |
| [AIMech:RelevantComponentAnalysis](../../data/curated/RelevantComponentAnalysis.yaml) | A partially supervised linear metric-learning procedure that estimates within-group covariance from positive equivalence constraints and whitens the representation using that covariance. |
| [AIMech:LargeMarginNearestNeighbor](../../data/curated/LargeMarginNearestNeighbor.yaml) | A supervised metric-learning method that fits a positive-semidefinite distance matrix by pulling fixed same-class target neighbors together while penalizing margin violations by differently labeled observations. |

CLARANS uses randomized improving medoid swaps; RCA whitens within-chunklet variation; LMNN fits a fixed-target convex distance-matrix objective. Their AIO mappings retain algorithm, task and representation distinctions.

Original primary methods were inspected. A [finite calculation](metric-source-boundaries.py) checks the removed-medoid contribution, a singular RCA covariance despite a large sample-size count, and the failure of the triangle inequality for squared distance. These are curator checks, not benchmarks or author errata.

The complete JSON ledger preserves query and PDF provenance, the BIRCH reuse decision, all inherited candidates and new medoid/metric-learning leads. Scientific review is an adversarial author self-review; no saturation is claimed.
