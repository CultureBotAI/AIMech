# Joint-embedding self-supervision — 2026-10-11T08:05:31Z

Added four concepts; AIMech now contains 195 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:SimSiam](../../data/curated/SimSiam.yaml) | A self-supervised representation-learning procedure that trains a shared encoder and predictor to match the encoder output of another augmented view using symmetric negative cosine similarity with stopped gradients on each target output. |
| [AIMech:SwAV](../../data/curated/SwAV.yaml) | An online self-supervised visual representation-learning procedure that predicts soft prototype assignments of one augmented image view from other views, using entropy-regularized balanced assignment and jointly learned features and prototypes. |
| [AIMech:BarlowTwins](../../data/curated/BarlowTwins.yaml) | A self-supervised representation-learning procedure that trains shared encoder and projection networks to make the cross-correlation of two batches of augmented-view embeddings close to the identity, penalizing diagonal mismatch and off-diagonal correlation. |
| [AIMech:VICReg](../../data/curated/VICReg.yaml) | A self-supervised joint-embedding procedure that combines a paired-view invariance loss with separate per-branch penalties for insufficient coordinate standard deviation and off-diagonal covariance. |

All four relate to the AIO self-supervised learning task. SwAV also relates to unsupervised clustering; neither mapping asserts algorithm/task equivalence.

The audit distinguishes stopped shared-network targets, detached balanced prototype codes, cross-view correlation reduction and separate branch variance/covariance penalties. It preserves VICReg paper/code loss scaling, Barlow Twins normalization conventions, SwAV soft-assignment limitations and SimSiam’s explicitly empirical noncollapse account.

Four original main papers, the SwAV supplement, two pinned author implementations and versioned API documentation support the curation. Only declared passages/images were read; no training was run.

DeepCluster, SeLa, whitening-based methods, visual bag-of-words approaches and the entire remaining prior frontier are pending. Discovery remains active.
