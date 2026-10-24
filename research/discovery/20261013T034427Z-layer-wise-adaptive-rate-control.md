# Layer-wise adaptive rate control

Added [LARC](../../data/curated/LayerWiseAdaptiveRateControl.yaml) as a DRAFT algorithm related to AIO TrainingStrategy. The clipping rule caps the effective vanilla-SGD rate using parameter and gradient norms.

The record distinguishes clipping from scaling mode, and gradient preprocessing from a bound on every wrapped optimizer final displacement. Historical decay, zero-norm and configuration policies remain explicit. [Constructed algebra](larc-clipping-boundaries.py) checks these distinctions without training.

The [structured report](20261013T034427Z-layer-wise-adaptive-rate-control.json) preserves pinned NVIDIA method and historical-code reading, ignored-inclusive identity searches, mapping context and outstanding leads. Discovery remains incomplete.
