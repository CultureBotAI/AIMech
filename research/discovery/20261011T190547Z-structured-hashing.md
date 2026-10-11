# Structured prediction and spectral hashing — 2026-10-11T19:05:47Z

Added three native DRAFT algorithm records, bringing the maintained collection to 370.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:HashCRBM](../../data/curated/HashCRBM.yaml) | A conditional RBM training and prediction method that uses spectral hashing of inputs to retrieve distinct training-output configurations and normalizes the conditional model only over that input-dependent support. |
| [AIMech:CDPercLoss](../../data/curated/CDPercLoss.yaml) | A conditional RBM training algorithm that contrasts the observed output free energy with that of a prediction selected by input-initialized stochastic search, treating the selected prediction as fixed during differentiation. |
| [AIMech:SpectralHashing](../../data/curated/SpectralHashing.yaml) | An unsupervised binary-code learning algorithm that approximates a spectral similarity-preservation objective using a PCA-aligned rectangular data model and zero-thresholded single-coordinate analytic modes. |

HashCRBM and CD-PercLoss relate to the RBM family through their conditional-model training and prediction procedures. Spectral hashing relates to PCA through its coordinate construction. These are algorithm/component associations, not forced subclasses of architectures or tasks.

The [finite examples](structured-hashing-boundaries.py) and JSON ledger document actual source reading, identity and mapping checks, restricted-support normalization, searched-prediction gradients and spectral normalization/coordinate qualifications, and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 201 pending inspection leads.
