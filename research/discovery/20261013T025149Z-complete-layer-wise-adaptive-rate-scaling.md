# Complete layer-wise adaptive rate scaling

Added [CLARS](../../data/curated/CompleteLayerWiseAdaptiveRateScaling.yaml) as a DRAFT algorithm related to AIO TrainingStrategy. The published mean-of-individual-norms denominator differs from the LARS norm-of-mean denominator.

The record preserves pseudocode, theorem-condition and implementation boundaries. The inspected author code uses a small-batch approximation, offsets, clipping and other choices that are not silently equated to the published equations. [Constructed algebra](clars-gradient-norm-boundaries.py) checks the distinctions without training.

The [structured report](20261013T025149Z-complete-layer-wise-adaptive-rate-scaling.json) preserves primary and static-code reading, complete ignored-inclusive identity searches, mapping context and outstanding leads. Discovery remains incomplete.
