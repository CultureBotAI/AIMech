# Contrastive learning, information estimation and regularization — 2026-10-11T08:46:32Z

Added five concepts; AIMech now contains 208 native DRAFT records.

| Record | Scope |
| --- | --- |
| [AIMech:ContrastivePredictiveCoding](../../data/curated/ContrastivePredictiveCoding.yaml) | A representation-learning procedure that encodes observations, summarizes preceding representations as context, and jointly trains these components to distinguish future representations from sampled alternatives using InfoNCE. |
| [AIMech:VirtualAdversarialTraining](../../data/curated/VirtualAdversarialTraining.yaml) | A prediction-smoothing regularization procedure that trains a model to preserve its current output distribution under approximately worst-case small input perturbations, constructing those perturbations without using target labels. |
| [AIMech:RegularizedInformationMaximization](../../data/curated/RegularizedInformationMaximization.yaml) | A discriminative clustering framework that fits conditional class probabilities by maximizing empirical input–assignment mutual information penalized by classifier complexity, with linear and kernel softmax configurations. |
| [AIMech:MutualInformationNeuralEstimation](../../data/curated/MutualInformationNeuralEstimation.yaml) | A mutual-information estimation procedure that trains a neural statistics function to maximize a Donsker–Varadhan objective contrasting joint samples with product-of-marginals samples, using stochastic optimization and an optional moving-average denominator for gradient estimation. |
| [AIMech:InfoNCE](../../data/curated/InfoNCE.yaml) | A contrastive log-softmax objective that identifies a joint positive among sampled candidates and, under independent marginal-negative sampling, gives an expectation-level lower bound on mutual information. |

CPC is a representation-learning procedure; InfoNCE is its separable contrastive objective. VAT smooths local predictions, RIM clusters by regularized information, and MINE estimates dependence. CPC, RIM and InfoNCE have qualified AIO related matches; VAT and MINE have explicit snapshot-bounded no-match assessments.

The primary methods, MINE supplementary proofs, Poole’s information-bound analysis and three pinned VAT source files support the records. Expected information bounds are distinguished from finite estimates and optimization guarantees. Only declared passages were read; no model or benchmark was run.

Adversarial author self-review corrected VAT source locators and loss-weight placement in [issue43](https://github.com/CultureBotAI/AIMech/issues/43). It also clarified the MINE gradient target and expanded the RIM equation locator. Original values, hashes and correction time are preserved in the JSON ledger.

NT-Xent, graph clustering components, additional variational bounds and older leads remain pending. Discovery remains active.
