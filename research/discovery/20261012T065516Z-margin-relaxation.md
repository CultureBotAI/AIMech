# Semidefinite and cutting-plane margin methods — 2026-10-12T06:55:16Z

Added three native DRAFT algorithms, bringing the maintained collection to501.

| Record | Defining scope |
| --- | --- |
| [Semidefinite Maximum Margin Clustering](../../data/curated/SemidefiniteMaximumMarginClustering.yaml) | Unlabeled binary label-matrix SDP and soft recovery |
| [Semisupervised Semidefinite Maximum Margin Clustering](../../data/curated/SemisupervisedSemidefiniteMaximumMarginClustering.yaml) | Observed-label constraints added to the binary SDP |
| [Cutting Plane Multiclass Maximum Margin Clustering](../../data/curated/CuttingPlaneMulticlassMaximumMarginClustering.yaml) | Fixed-kernel multiclass working sets and frozen-winner QPs |

All sixteen primary-paper pages were visually read. [Exact checks](margin-relaxation-boundaries.py) distinguish convex relaxations from discrete solutions, matrix balance from rounded counts, and frozen-winner QPs from global convexity. The semisupervised procedure maps to the related general clustering task; the unlabeled procedures map to the related unsupervised task.

The ledger retains425 pending cohorts and other unresolved dispositions. Discovery has not reached saturation.

The initial self-review identified ambiguous transductive-supervision wording ([issue158](https://github.com/CultureBotAI/AIMech/issues/158)). The corrected identity note separates shared labeled/unlabeled inputs from this procedure’s observed-label constraints. The initial review remains immutable; a successor records the verification.
