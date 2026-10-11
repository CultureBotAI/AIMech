# Clustering and whitening self-supervision — 2026-10-11T08:16:05Z

Added four concepts; AIMech now contains 199 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:DeepCluster](../../data/curated/DeepCluster.yaml) | A visual representation-learning procedure that alternates clustering current neural features into pseudo-labels and training the feature extractor and a classifier to predict those labels. |
| [AIMech:SeLa](../../data/curated/SeLa.yaml) | A self-supervised representation-learning procedure that alternates neural pseudo-label prediction and dataset-wide self-labelling through an entropy-regularized balanced optimal-transport assignment. |
| [AIMech:WhiteningMSE](../../data/curated/WhiteningMSE.yaml) | A self-supervised representation-learning procedure that differentiably whitens projected image-view embeddings and minimizes the average squared distance between normalized whitened embeddings of views from the same image. |
| [AIMech:InvariantInformationClustering](../../data/curated/InvariantInformationClustering.yaml) | A neural clustering procedure that maximizes mutual information between discrete cluster-assignment variables for paired unlabeled samples, estimating their joint distribution from the network’s soft assignment probabilities. |

All four have qualified AIO self-supervised-task mappings; DeepCluster, SeLa and IIC also relate to unsupervised clustering. No algorithm/task equivalence or upstream ontology change is asserted.

The audit separates k-means pseudo-label training, global balanced transport with hardening, differentiable whitening with positive-view matching, and discrete assignment mutual information. It preserves SeLa paper/code normalization differences, W-MSE covariance conditions, IIC numerical stabilization and DeepCluster’s labeled hyperparameter-selection context.

Four original papers, the W-MSE supplement and nine pinned author code files support the curation. Only declared passages/images were read; no training was run.

DEC, JULE, IMSAT, Deep InfoMax, whitening components, later method variants and the remaining prior frontier need inspection. Discovery remains active.

Adversarial author review corrected a SeLa normalization ambiguity: integrality applies to the count assignment NQ, while Q is probability mass. The structured review records the resolved issue.
