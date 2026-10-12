# Local outlier factor

Added [LOF](../../data/curated/LocalOutlierFactor.yaml) as a native DRAFT algorithm with a related UnsupervisedLearning mapping. The collection now has512 native records. All12 original-paper pages were visually read, and the pinned scikit-learn1.7.2 implementation and neighbor-search conventions were inspected.

[Exact calculations](local-outlier-factor-boundaries.py) preserve self exclusion, boundary ties, asymmetric reachability, relative scores, duplicate limits and neighborhood-scale effects. Original mathematical behavior is distinguished from fixed-count, epsilon, threshold and novelty-query implementation choices. No numerical performance advantage or runtime reproduction is claimed.

The full ledger retains440 pending cohorts, plus other unresolved work including OPTICS-OF. Discovery continues.
