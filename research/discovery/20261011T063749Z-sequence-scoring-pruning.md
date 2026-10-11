# Sequence scoring and pruning — 2026-10-11T06:37:49Z

Added seven concepts; the native collection now contains 153 DRAFT records.

| Record | Kind |
| --- | --- |
| [AIMech:OptimalStoppingBeamDecoding](../../data/curated/OptimalStoppingBeamDecoding.yaml) | algorithm |
| [AIMech:BoundedLengthReward](../../data/curated/BoundedLengthReward.yaml) | mathematical_method |
| [AIMech:PredictedLengthBoundedReward](../../data/curated/PredictedLengthBoundedReward.yaml) | mathematical_method |
| [AIMech:BoundedAdaptiveReward](../../data/curated/BoundedAdaptiveReward.yaml) | mathematical_method |
| [AIMech:BrevityPenaltyNormalization](../../data/curated/BrevityPenaltyNormalization.yaml) | mathematical_method |
| [AIMech:AbsoluteThresholdBeamPruning](../../data/curated/AbsoluteThresholdBeamPruning.yaml) | algorithm |
| [AIMech:PerNodeCandidateBeamPruning](../../data/curated/PerNodeCandidateBeamPruning.yaml) | algorithm |

All seven have justified related mappings to Natural Language Processing. The records distinguish a stopping certificate, four scoring methods, and two local pruning procedures.

A portable [curator calculation](../../research/validation/20261011T063749Z-score-boundary-examples.py) and [actual result](../../research/validation/20261011T063749Z-score-boundary-examples.json) preserve two necessary distinctions: probability ratios differ from ratios of negative log scores, and a predicted length is not automatically an enforced maximum. Neither example is an author-code run or an established erratum.

Relative pruning remains deferred for score-domain clarification. Earlier frontiers and new primary-source leads remain open; discovery continues.
