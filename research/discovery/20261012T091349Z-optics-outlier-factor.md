# OPTICS outlier factor

Added [OPTICS-OF](../../data/curated/OPTICSOutlierFactor.yaml) as a native DRAFT algorithm, bringing the native collection to 513. Its self-inclusive neighborhoods produce different scores from [LOF](../../data/curated/LocalOutlierFactor.yaml), whose earlier unresolved-comparison note is now clarified. Both retain a related UnsupervisedLearning mapping.

Mechanism evidence comes from fully inspected immutable ELKI 0.8.0 source and neighbor contracts. The original 1999 paper was read as parsed text only; its equations and figures were not visually verified. [Exact calculations](optics-outlier-factor-boundaries.py) document the distinct scores, tie behavior and zero-distance limits. No library execution or benchmark result is claimed.

The ledger now includes the LMU publication catalogue and retains 441 pending cohorts, plus other unresolved work. Discovery continues.
