# Classical ML concept proposals

Assessed 2026-10-11T02:45:28Z against AIO `397851c547d1c4d8f06ef184f63c1d40bc86937a`.

These are local upstream-term proposals, not generated AIMech records. All 36 candidates from [AIO issue 167](https://github.com/berkeleybop/artificial-intelligence-ontology/issues/167) are retained: 32 proposed terms, three deferred candidates, and one existing alias requiring scope review. New AIO IDs are unresolved. No upstream submission has been made.

The released ontology, committed template and live source sheet each contain the same 442 accepted class IDs already present in AIMech. The maintained owner is the AIO source Google Sheet exported to `src/ontology/aio-src.csv`, as verified in the pinned `src/ontology/aio.Makefile`. Parent suggestions below are provisional inferences, not asserted ontology changes.

Duplicate searches included ignored and hidden files in both AIMech checkouts and normalized labels plus scoped synonyms over all 442 named classes. Text hits are not class matches; absence of a spelling does not establish a distinct concept. Comparisons below therefore retain overlap and abstraction concerns.

## Candidate ledger

| Candidate | Disposition | Nearest AIO concepts | Proposed definition | Evidence |
| --- | --- | --- | --- | --- |
| k-means | propose_upstream_term | AIO:Clustering | Clustering that partitions observations around centroids by minimizing within-cluster squared distances. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#k-means) |
| DBSCAN | propose_upstream_term | AIO:Clustering | Density-based clustering that connects dense neighborhoods and identifies unsupported observations as noise. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#dbscan) |
| HDBSCAN | propose_upstream_term | AIO:HierarchicalClustering | Hierarchical density-based clustering that selects clusters across density scales. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#hdbscan) |
| OPTICS | propose_upstream_term | AIO:Clustering | Density-based clustering analysis that orders observations using reachability across neighborhood scales. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#optics) |
| BIRCH | propose_upstream_term | AIO:Clustering | Clustering that compresses observations into a clustering-feature tree for subsequent grouping. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#birch) |
| Mean shift | propose_upstream_term | AIO:Clustering | Mode-seeking clustering that moves candidate centers toward local density maxima. | [Method source](https://scikit-learn.org/1.8/modules/clustering.html#mean-shift) |
| AdaBoost | propose_upstream_term | AIO:EnsembleLearning | Boosting that reweights training observations according to prior prediction errors. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#adaboost) |
| Gradient boosting machine | propose_upstream_term | AIO:EnsembleLearning | Boosting that adds predictors fitted to negative loss-function gradients. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#mathematical-formulation) |
| XGBoost | defer_software_method_boundary | AIO:EnsembleLearning | A tree-boosting system with sparsity-aware learning and weighted quantile sketches. | [Method source](https://arxiv.org/abs/1603.02754v3) |
| LightGBM | defer_software_method_boundary | AIO:EnsembleLearning | A gradient-boosted tree implementation introducing gradient-based sampling and exclusive feature bundling. | [Method source](https://proceedings.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html) |
| Bagging | propose_upstream_term | AIO:EnsembleLearning | Ensemble learning that aggregates predictors trained on bootstrap samples. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#bagging-meta-estimator) |
| Boosting | propose_upstream_term | AIO:EnsembleLearning | Ensemble learning that sequentially adds learners to improve an existing predictor. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#gradient-boosted-trees) |
| Stacking | propose_upstream_term | AIO:EnsembleLearning | Ensemble learning that trains a final estimator on base-estimator predictions. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#stacked-generalization) |
| Voting classifier | propose_upstream_term | AIO:EnsembleLearning | A classifier combining base predictions through class votes or aggregated class probabilities. | [Method source](https://scikit-learn.org/1.8/modules/ensemble.html#voting-classifier) |
| Naive Bayes | propose_upstream_term | AIO:Classification | Probabilistic classification assuming feature independence conditional on the class. | [Method source](https://scikit-learn.org/1.8/modules/naive_bayes.html#naive-bayes) |
| Linear discriminant analysis | propose_upstream_term | AIO:Classification | Gaussian discriminant classification sharing one covariance matrix across classes. | [Method source](https://scikit-learn.org/1.8/modules/lda_qda.html#lda) |
| Quadratic discriminant analysis | propose_upstream_term | AIO:Classification | Gaussian discriminant classification with class-specific covariance matrices. | [Method source](https://scikit-learn.org/1.8/modules/lda_qda.html#qda) |
| CART | propose_upstream_term | AIO:DecisionTree | Decision-tree induction using binary recursive partitioning for classification or regression. | [Method source](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart) |
| C4.5 | propose_upstream_term | AIO:DecisionTree | Decision-tree induction extending ID3 with tests on continuous-valued features. | [Method source](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart) |
| ID3 | propose_upstream_term | AIO:DecisionTree | Decision-tree induction that selects categorical attributes by information gain. | [Method source](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart) |
| Hidden Markov model | propose_upstream_term | AIO:ProbabilisticGraphicalModel | A sequence model whose hidden Markov states generate observations through state-dependent emission distributions. | [Method source](https://hmmlearn.readthedocs.io/en/0.3.3/tutorial.html) |
| Markov decision process | propose_upstream_term | AIO:Model | A sequential decision model with states, actions, Markov transitions, and rewards. | [Method source](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=3) |
| Partially observable Markov decision process | propose_upstream_term | AIO:Model | A Markov decision model in which observations provide incomplete information about the current state. | [Method source](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=7) |
| Markov random field | propose_upstream_term | AIO:ProbabilisticGraphicalModel | An undirected graphical probability model associating potential functions with variable groups. | [Method source](https://pgmpy.org/api/generated/undirected/pgmpy.models.DiscreteMarkovNetwork.html) |
| Multilayer perceptron | covered_alias_requires_scope_review | AIO:DeepFeedForwardNetwork | A feed-forward neural model with one or more nonlinear hidden layers. | [Method source](https://scikit-learn.org/1.8/modules/neural_networks_supervised.html#multi-layer-perceptron) |
| Expectation maximization | propose_upstream_term | AIO:MachineLearningTask | Parameter estimation alternating expected complete-data log-likelihood evaluation and its maximization. | [Method source](https://people.ece.uw.edu/bilmes/p/mypubs/bilmes1997-em.pdf#page=4) |
| Genetic algorithm | propose_upstream_term | AIO:MachineLearningTask | Evolutionary optimization using fitness-based selection and genetic variation of candidate solutions. | [Method source](https://deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple) |
| Stochastic gradient descent | propose_upstream_term | AIO:TrainingStrategy | Optimization using gradients estimated from sampled training observations. | [Method source](https://scikit-learn.org/1.8/modules/sgd.html#id5) |
| Elastic net | propose_upstream_term | AIO:RegressionAnalysis | Linear regression regularized by a combination of L1 and L2 penalties. | [Method source](https://scikit-learn.org/1.8/modules/linear_model.html#elastic-net) |
| Least-angle regression | propose_upstream_term | AIO:RegressionAnalysis | Regression that advances along directions equiangular to predictors most correlated with the residual. | [Method source](https://scikit-learn.org/1.8/modules/linear_model.html#least-angle-regression) |
| Ordinary least squares | defer_overlap_review | AIO:LeastsquaresAnalysis, AIO:LinearRegression | Linear parameter estimation minimizing the unweighted sum of squared residuals. | [Method source](https://scikit-learn.org/1.8/modules/linear_model.html#ordinary-least-squares) |
| Partial least squares regression | propose_upstream_term | AIO:RegressionAnalysis | Regression using latent components chosen to capture predictor-response covariance. | [Method source](https://scikit-learn.org/1.8/modules/cross_decomposition.html#cross-decomposition) |
| Gaussian process regression | propose_upstream_term | AIO:RegressionAnalysis | Probabilistic regression conditioning a Gaussian-process prior on observed training data. | [Method source](https://scikit-learn.org/1.8/modules/gaussian_process.html#gaussian-process-regression-gpr) |
| GloVe | propose_upstream_term | AIO:RepresentationLearning, AIO:word2vecCBOW, AIO:word2vecSkipGram | Word-vector learning from global word co-occurrence statistics. | [Method source](https://nlp.stanford.edu/projects/glove/) |
| Apriori | propose_upstream_term | AIO:AssociationRuleLearning | Frequent-itemset mining using breadth-first candidate enumeration and support-based pruning. | [Method source](https://borgelt.net/apriori.html) |
| Eclat | propose_upstream_term | AIO:AssociationRuleLearning | Frequent-itemset mining using depth-first enumeration and transaction-set intersections. | [Method source](https://borgelt.net/eclat.html) |

## Identity, placement and evidence locators

### k-means

The Clustering task does not specify the centroid/squared-distance objective of this algorithm.

Parent proposal: AIO:Clustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #k-means](https://scikit-learn.org/1.8/modules/clustering.html#k-means). Supports the narrow identity/method description, not general performance.

### DBSCAN

Clustering does not specify core points, density connectivity or noise handling.

Parent proposal: AIO:Clustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #dbscan](https://scikit-learn.org/1.8/modules/clustering.html#dbscan). Supports the narrow identity/method description, not general performance.

### HDBSCAN

HierarchicalClustering does not specify density scales and cluster-stability selection.

Parent proposal: AIO:HierarchicalClustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #hdbscan](https://scikit-learn.org/1.8/modules/clustering.html#hdbscan). Supports the narrow identity/method description, not general performance.

### OPTICS

Clustering does not specify a reachability ordering across neighborhood scales; OPTICS is not identical to one flat partition.

Parent proposal: AIO:Clustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #optics](https://scikit-learn.org/1.8/modules/clustering.html#optics). Supports the narrow identity/method description, not general performance.

### BIRCH

Clustering does not specify the clustering-feature tree and incremental compression procedure.

Parent proposal: AIO:Clustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #birch](https://scikit-learn.org/1.8/modules/clustering.html#birch). Supports the narrow identity/method description, not general performance.

### Mean shift

Clustering does not specify iterative mode seeking in a kernel density estimate.

Parent proposal: AIO:Clustering. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #mean-shift](https://scikit-learn.org/1.8/modules/clustering.html#mean-shift). Supports the narrow identity/method description, not general performance.

### AdaBoost

EnsembleLearning does not specify sequential sample reweighting by prediction error.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #adaboost](https://scikit-learn.org/1.8/modules/ensemble.html#adaboost). Supports the narrow identity/method description, not general performance.

### Gradient boosting machine

EnsembleLearning does not specify stagewise fitting to negative loss gradients.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. The inspected implementation is gradient tree boosting; the generic GBM scope needs the original functional-gradient formulation.

Evidence: [User Guide, section #mathematical-formulation](https://scikit-learn.org/1.8/modules/ensemble.html#mathematical-formulation). Supports the narrow identity/method description, not general performance.

### XGBoost

EnsembleLearning is a method category; this name also identifies a software implementation, requiring representation review.

Parent proposal: unresolved. The cited work describes a software system or implementation. Separate its method contribution from a software-instance record before proposing an AIConcept.

Evidence: [Chen and Guestrin (2016), arXiv:1603.02754v3, abstract: system identity, sparsity-aware learning and weighted quantile sketch](https://arxiv.org/abs/1603.02754v3). Supports the narrow identity/method description, not general performance.

### LightGBM

EnsembleLearning is a method category; this name also identifies a software implementation, requiring representation review.

Parent proposal: unresolved. The cited work describes a software system or implementation. Separate its method contribution from a software-instance record before proposing an AIConcept.

Evidence: [Ke et al. (NeurIPS 2017), abstract: GOSS and EFB in a gradient-boosted decision-tree implementation](https://proceedings.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html). Supports the narrow identity/method description, not general performance.

### Bagging

EnsembleLearning does not require bootstrap samples; bagging is distinct from generic ensembles and sampling without replacement.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #bagging-meta-estimator](https://scikit-learn.org/1.8/modules/ensemble.html#bagging-meta-estimator). Supports the narrow identity/method description, not general performance.

### Boosting

EnsembleLearning does not require sequential error/loss-directed combination of learners.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #gradient-boosted-trees](https://scikit-learn.org/1.8/modules/ensemble.html#gradient-boosted-trees). Supports the narrow identity/method description, not general performance.

### Stacking

EnsembleLearning does not require a learned final estimator on base-estimator predictions.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #stacked-generalization](https://scikit-learn.org/1.8/modules/ensemble.html#stacked-generalization). Supports the narrow identity/method description, not general performance.

### Voting classifier

EnsembleLearning does not specify class voting or aggregation of class probabilities.

Parent proposal: AIO:EnsembleLearning. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #voting-classifier](https://scikit-learn.org/1.8/modules/ensemble.html#voting-classifier). Supports the narrow identity/method description, not general performance.

### Naive Bayes

Classification does not specify conditional feature independence or a probabilistic generative classifier.

Parent proposal: AIO:Classification. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #naive-bayes](https://scikit-learn.org/1.8/modules/naive_bayes.html#naive-bayes). Supports the narrow identity/method description, not general performance.

### Linear discriminant analysis

Classification does not specify Gaussian class models with shared covariance; distinguish the classifier from its dimension-reduction use.

Parent proposal: AIO:Classification. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #lda](https://scikit-learn.org/1.8/modules/lda_qda.html#lda). Supports the narrow identity/method description, not general performance.

### Quadratic discriminant analysis

Classification does not specify Gaussian class models with class-specific covariance.

Parent proposal: AIO:Classification. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #qda](https://scikit-learn.org/1.8/modules/lda_qda.html#qda). Supports the narrow identity/method description, not general performance.

### CART

DecisionTree denotes a broad tree-based model/category and does not identify this binary tree-induction procedure.

Parent proposal: AIO:DecisionTree. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart). Supports the narrow identity/method description, not general performance.

### C4.5

DecisionTree does not identify this extension of ID3 handling continuous features.

Parent proposal: AIO:DecisionTree. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart). Supports the narrow identity/method description, not general performance.

### ID3

DecisionTree does not identify information-gain-based categorical tree induction.

Parent proposal: AIO:DecisionTree. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart](https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart). Supports the narrow identity/method description, not general performance.

### Hidden Markov model

ProbabilisticGraphicalModel does not specify Markov hidden states and observation emissions.

Parent proposal: AIO:ProbabilisticGraphicalModel. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [hmmlearn 0.3.3 tutorial, opening HMM generative-process definition and parameter list](https://hmmlearn.readthedocs.io/en/0.3.3/tutorial.html). Supports the narrow identity/method description, not general performance.

### Markov decision process

Model does not require controlled Markov transitions and reward-based sequential decisions.

Parent proposal: AIO:Model. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [Kaelbling, Littman and Cassandra (1998), section 2.1, printed pp. 101–102 / PDF pp. 3–4: states, actions, transitions and rewards](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=3). Supports the narrow identity/method description, not general performance.

### Partially observable Markov decision process

Model does not require state uncertainty, actions, transition probabilities, observations and rewards.

Parent proposal: AIO:Model. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [Kaelbling, Littman and Cassandra (1998), section 3.1, printed p. 105 / PDF p. 7: POMDP tuple and observation model](https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=7). Supports the narrow identity/method description, not general performance.

### Markov random field

ProbabilisticGraphicalModel covers broader directed and undirected dependencies; this candidate specifically uses an undirected graph.

Parent proposal: AIO:ProbabilisticGraphicalModel. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. The pgmpy URL is unversioned; preserve access time and recheck its API description before upstream adoption.

Evidence: [DiscreteMarkovNetwork class description and add_factors documentation; undirected graph and factor potentials](https://pgmpy.org/api/generated/undirected/pgmpy.models.DiscreteMarkovNetwork.html). Supports the narrow identity/method description, not general performance.

### Multilayer perceptron

An existing exact MLP synonym already resolves to DeepFeedForwardNetwork. Do not add a duplicate solely because the expanded synonym has a spelling error. Scope of shallow versus deep networks remains unresolved.

Parent proposal: unresolved. MLP is already an exact synonym of AIO:DeepFeedForwardNetwork. Its expanded synonym is misspelled Multilayer Perceptoron; inspect depth scope before proposing a separate identity.

Evidence: [User Guide, section #multi-layer-perceptron](https://scikit-learn.org/1.8/modules/neural_networks_supervised.html#multi-layer-perceptron). Supports the narrow identity/method description, not general performance.

### Expectation maximization

MachineLearningTask does not identify the alternating expected-log-likelihood and maximization estimation procedure.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. These are procedures, not trained model instances; current AIO branch definitions mix abstraction levels.

Evidence: [Bilmes, TR-97-021 (PDF cover dated April 1998), section 2 Basic EM, PDF pp. 3–4: expected log-likelihood Q, E-step and M-step](https://people.ece.uw.edu/bilmes/p/mypubs/bilmes1997-em.pdf#page=4). Supports the narrow identity/method description, not general performance.

### Genetic algorithm

MachineLearningTask does not specify evolutionary fitness selection, recombination and mutation; genetic optimization is not necessarily learning from data.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. These are procedures, not trained model instances; current AIO branch definitions mix abstraction levels.

Evidence: [DEAP algorithms documentation, eaSimple pseudocode: evaluate, select, varAnd, mate and mutate](https://deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple). Supports the narrow identity/method description, not general performance.

### Stochastic gradient descent

TrainingStrategy does not identify a stochastic optimization algorithm, and its preprocessing genus requires upstream clarification.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. These are procedures, not trained model instances; current AIO branch definitions mix abstraction levels.

Evidence: [User Guide, section #id5](https://scikit-learn.org/1.8/modules/sgd.html#id5). Supports the narrow identity/method description, not general performance.

### Elastic net

RegressionAnalysis does not require mixed L1/L2 penalties; existing Lasso and Ridge concepts cover the separate penalty types.

Parent proposal: AIO:RegressionAnalysis. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #elastic-net](https://scikit-learn.org/1.8/modules/linear_model.html#elastic-net). Supports the narrow identity/method description, not general performance.

### Least-angle regression

RegressionAnalysis does not specify the equiangular active-predictor fitting path; distinguish this algorithm from the resulting regression model.

Parent proposal: AIO:RegressionAnalysis. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #least-angle-regression](https://scikit-learn.org/1.8/modules/linear_model.html#least-angle-regression). Supports the narrow identity/method description, not general performance.

### Ordinary least squares

LeastsquaresAnalysis and LinearRegression overlap substantially with this candidate. Decide whether an exact synonym, narrower class or no change is appropriate after upstream scope review.

Parent proposal: unresolved. Compare AIO:LeastsquaresAnalysis and AIO:LinearRegression; do not assume a distinct class solely from absence of the OLS acronym.

Evidence: [User Guide, section #ordinary-least-squares](https://scikit-learn.org/1.8/modules/linear_model.html#ordinary-least-squares). Supports the narrow identity/method description, not general performance.

### Partial least squares regression

RegressionAnalysis does not identify covariance-based latent predictor/response components.

Parent proposal: AIO:RegressionAnalysis. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #cross-decomposition](https://scikit-learn.org/1.8/modules/cross_decomposition.html#cross-decomposition). Supports the narrow identity/method description, not general performance.

### Gaussian process regression

RegressionAnalysis does not specify conditioning a Gaussian-process prior.

Parent proposal: AIO:RegressionAnalysis. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [User Guide, section #gaussian-process-regression-gpr](https://scikit-learn.org/1.8/modules/gaussian_process.html#gaussian-process-regression-gpr). Supports the narrow identity/method description, not general performance.

### GloVe

The existing word2vec concepts use different training objectives. RepresentationLearning is defined as a deep neural network in this pin, so using it as a parent would need an upstream abstraction correction.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance.

Evidence: [Author project page, Introduction: global log-bilinear regression model and word co-occurrence statistics](https://nlp.stanford.edu/projects/glove/). Supports the narrow identity/method description, not general performance.

### Apriori

AssociationRuleLearning does not identify breadth-first frequent-itemset mining. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. Frequent-itemset mining and association-rule induction are different operations; an intermediate parent may be needed.

Evidence: [Author Apriori implementation page, Introduction: breadth-first traversal of the subset lattice and minimum-support test](https://borgelt.net/apriori.html). Supports the narrow identity/method description, not general performance.

### Eclat

AssociationRuleLearning does not identify depth-first transaction-set intersection. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed.

Parent proposal: unresolved. Proposed placement is an inference from the existing AIO hierarchy; maintainers must resolve task, algorithm and model scope before acceptance. Frequent-itemset mining and association-rule induction are different operations; an intermediate parent may be needed.

Evidence: [Author Eclat implementation page, Introduction: depth-first enumeration and intersection of transaction sets](https://borgelt.net/eclat.html). Supports the narrow identity/method description, not general performance.

## Acceptance and handoff

Use the existing issue 167 discussion rather than creating duplicate requests. Upstream maintainers must resolve scope, distinctness, definitions, synonyms and hierarchy in the maintained source; acceptance must produce stable AIO IDs in a reviewed release. Then assess the complete source diff with `aimech-refresh-aio`, regenerate through the supported workflow, and recheck source integrity, schema and exact reproduction. A local proposal alone cannot trigger that migration.

The JSON companion preserves aliases, duplicate matches, precise source locators, access times and hashes for the versioned implementation documents. The separate source assessment records remaining discovery leads and the bounded stopping criterion. Broader literature coverage remains open.
