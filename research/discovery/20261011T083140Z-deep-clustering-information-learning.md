# Deep clustering and information-based learning — 2026-10-11T08:31:40Z

Added four concepts; AIMech now contains 203 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:DeepEmbeddedClustering](../../data/curated/DeepEmbeddedClustering.yaml) | A neural clustering procedure that jointly refines an embedding and cluster centers by fitting Student-t soft assignments to periodically refreshed, frequency-normalized squared-assignment targets. |
| [AIMech:JointUnsupervisedLearning](../../data/curated/JointUnsupervisedLearning.yaml) | An image representation and clustering procedure that alternates periods of graph-based agglomerative merging with convolutional-network updates from a cluster-derived weighted triplet objective. |
| [AIMech:InformationMaximizingSelfAugmentedTraining](../../data/curated/InformationMaximizingSelfAugmentedTraining.yaml) | A discrete representation-learning procedure that combines self-augmentation consistency with an information objective, using categorical outputs for clustering or a pairwise approximation for multi-bit hashing. |
| [AIMech:DeepInfoMax](../../data/curated/DeepInfoMax.yaml) | A representation-learning procedure that jointly trains an encoder and a dependence critic on matched versus mismatched global or local-to-global features, optionally regularizing the encoder output toward a chosen prior. |

The records distinguish fixed soft-target refinement, graph agglomeration with neural updates, discrete information with augmentation consistency, and continuous feature dependence critics. AIO links are qualified task associations.

Primary methods, the JULE appendix, the IMSAT supplement and seven versioned source files support the curation. Only declared passages and images were read; no training or benchmark was run.

Adversarial author self-review corrected the ideal-versus-stabilized KL gradient wording in [issue41](https://github.com/CultureBotAI/AIMech/issues/41). Validation also caught and removed a redundant Deep InfoMax alias. The JSON ledger preserves previous values and hashes.

Contrastive predictive coding, regularized information maximization, virtual adversarial training, graph clustering components, MINE and earlier leads remain pending. Discovery remains active.
