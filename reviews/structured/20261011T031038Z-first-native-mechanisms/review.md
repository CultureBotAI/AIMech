# Scientific self-review of the first 36 native concept definitions and mechanisms

- Review: 20261011T031038Z-first-native-mechanisms
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T03:10:38Z
- Finished UTC: 2026-10-11T03:10:38Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 36 selected maintained records have supported narrow definitions/mechanisms, explicit AIO relationships and honest draft provenance. No unresolved curation finding remains within this scope. This does not certify empirical performance, exhaust discovery or endorse upstream hierarchy boundaries.

## Scope And Provenance

Definition, identity, mechanism citation and AIO mapping direction for the first 36 maintained concepts.

Selection: Select exactly the 36 paths in the inspected first-native-cohort manifest; all selected records reviewed without sampling.
Coverage: full; 36 reviewed / 36 in the declared population.
Source: working_tree at Git base 945bd67d190e867ac379f8d4ebbc6d4ddec152a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AdaBoost | data/curated/AdaBoost.yaml | maintained | AdaBoost |
| AIMech:Apriori | data/curated/Apriori.yaml | maintained | Apriori |
| AIMech:BIRCH | data/curated/BIRCH.yaml | maintained | BIRCH |
| AIMech:Bagging | data/curated/Bagging.yaml | maintained | Bagging |
| AIMech:Boosting | data/curated/Boosting.yaml | maintained | Boosting |
| AIMech:C45 | data/curated/C45.yaml | maintained | C4.5 |
| AIMech:CART | data/curated/CART.yaml | maintained | CART |
| AIMech:DBSCAN | data/curated/DBSCAN.yaml | maintained | DBSCAN |
| AIMech:DirectPreferenceOptimization | data/curated/DirectPreferenceOptimization.yaml | maintained | Direct preference optimization |
| AIMech:Eclat | data/curated/Eclat.yaml | maintained | Eclat |
| AIMech:ElasticNet | data/curated/ElasticNet.yaml | maintained | Elastic net |
| AIMech:ExpectationMaximization | data/curated/ExpectationMaximization.yaml | maintained | Expectation maximization |
| AIMech:FlashAttention | data/curated/FlashAttention.yaml | maintained | FlashAttention |
| AIMech:GaussianProcessRegression | data/curated/GaussianProcessRegression.yaml | maintained | Gaussian process regression |
| AIMech:GeneticAlgorithm | data/curated/GeneticAlgorithm.yaml | maintained | Genetic algorithm |
| AIMech:GloVe | data/curated/GloVe.yaml | maintained | GloVe |
| AIMech:GradientBoosting | data/curated/GradientBoosting.yaml | maintained | Gradient boosting machine |
| AIMech:HDBSCAN | data/curated/HDBSCAN.yaml | maintained | HDBSCAN |
| AIMech:HiddenMarkovModel | data/curated/HiddenMarkovModel.yaml | maintained | Hidden Markov model |
| AIMech:ID3 | data/curated/ID3.yaml | maintained | ID3 |
| AIMech:KMeans | data/curated/KMeans.yaml | maintained | k-means |
| AIMech:LeastAngleRegression | data/curated/LeastAngleRegression.yaml | maintained | Least-angle regression |
| AIMech:LinearDiscriminantAnalysis | data/curated/LinearDiscriminantAnalysis.yaml | maintained | Linear discriminant analysis |
| AIMech:LoRA | data/curated/LoRA.yaml | maintained | Low-rank adaptation |
| AIMech:Mamba | data/curated/Mamba.yaml | maintained | Mamba sequence architecture |
| AIMech:MarkovDecisionProcess | data/curated/MarkovDecisionProcess.yaml | maintained | Markov decision process |
| AIMech:MarkovRandomField | data/curated/MarkovRandomField.yaml | maintained | Markov random field |
| AIMech:MeanShift | data/curated/MeanShift.yaml | maintained | Mean shift |
| AIMech:NaiveBayes | data/curated/NaiveBayes.yaml | maintained | Naive Bayes |
| AIMech:OPTICS | data/curated/OPTICS.yaml | maintained | OPTICS |
| AIMech:PartialLeastSquaresRegression | data/curated/PartialLeastSquaresRegression.yaml | maintained | Partial least squares regression |
| AIMech:PartiallyObservableMarkovDecisionProcess | data/curated/PartiallyObservableMarkovDecisionProcess.yaml | maintained | Partially observable Markov decision process |
| AIMech:QuadraticDiscriminantAnalysis | data/curated/QuadraticDiscriminantAnalysis.yaml | maintained | Quadratic discriminant analysis |
| AIMech:Stacking | data/curated/Stacking.yaml | maintained | Stacking |
| AIMech:StochasticGradientDescent | data/curated/StochasticGradientDescent.yaml | maintained | Stochastic gradient descent |
| AIMech:VotingClassifier | data/curated/VotingClassifier.yaml | maintained | Voting classifier |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | Checked 442 record(s); 0 failed. |
| python -m aimech validate-curated | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | Checked 36 curated concept record(s); 0 error(s). |
| python -m aimech seed --check | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-history --base HEAD | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | Checked 5 history record(s); 0 error(s). |
| python scripts/record_review.py check | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 1,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class |
| Repository code and schema quality gate | passed | True | AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier | 209 tests passed, 3 skipped; 442 AIO records reproduced; 36 native records passed; history and review checks passed. |

## Scientific And Domain Assessments

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:AdaBoost.

Boosting that reweights training observations according to prior prediction errors. EnsembleLearning does not specify sequential sample reweighting by prediction error.

The cited method passage supports the maintained claim scope. EnsembleLearning does not specify sequential sample reweighting by prediction error. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Apriori.

Frequent-itemset mining using breadth-first candidate enumeration and support-based pruning. AssociationRuleLearning does not identify breadth-first frequent-itemset mining. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed.

The cited method passage supports the maintained claim scope. AssociationRuleLearning does not identify breadth-first frequent-itemset mining. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:BIRCH.

Clustering that compresses observations into a clustering-feature tree for subsequent grouping. Clustering does not specify the clustering-feature tree and incremental compression procedure.

The cited method passage supports the maintained claim scope. Clustering does not specify the clustering-feature tree and incremental compression procedure. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Bagging.

Ensemble learning that aggregates predictors trained on bootstrap samples. EnsembleLearning does not require bootstrap samples; bagging is distinct from generic ensembles and sampling without replacement.

The cited method passage supports the maintained claim scope. EnsembleLearning does not require bootstrap samples; bagging is distinct from generic ensembles and sampling without replacement. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Boosting.

Ensemble learning that sequentially adds learners to improve an existing predictor. EnsembleLearning does not require sequential error/loss-directed combination of learners.

The cited method passage supports the maintained claim scope. EnsembleLearning does not require sequential error/loss-directed combination of learners. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:C45.

Decision-tree induction extending ID3 with tests on continuous-valued features. DecisionTree does not identify this extension of ID3 handling continuous features.

The cited method passage supports the maintained claim scope. DecisionTree does not identify this extension of ID3 handling continuous features. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:CART.

Decision-tree induction using binary recursive partitioning for classification or regression. DecisionTree denotes a broad tree-based model/category and does not identify this binary tree-induction procedure.

The cited method passage supports the maintained claim scope. DecisionTree denotes a broad tree-based model/category and does not identify this binary tree-induction procedure. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:DBSCAN.

Density-based clustering that connects dense neighborhoods and identifies unsupported observations as noise. Clustering does not specify core points, density connectivity or noise handling.

The cited method passage supports the maintained claim scope. Clustering does not specify core points, density connectivity or noise handling. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:DirectPreferenceOptimization.

Preference-based policy fitting using a classification objective on policy-to-reference probability ratios for preferred and dispreferred responses. A training algorithm, not an instruction-tuned language-model instance or a synonym for all reinforcement learning from human feedback.

The cited method passage supports the maintained claim scope. DPO is a policy-fitting procedure. The target discusses training strategies but uses a preprocessing genus, so a subclass claim is withheld. DPO is motivated by preference-based language-model alignment but its derived training objective does not require the separate RL optimization loop described for conventional RLHF. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Eclat.

Frequent-itemset mining using depth-first enumeration and transaction-set intersections. AssociationRuleLearning does not identify depth-first transaction-set intersection. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed.

The cited method passage supports the maintained claim scope. AssociationRuleLearning does not identify depth-first transaction-set intersection. Mining itemsets and generating association rules are distinct tasks; an intermediate parent may be needed. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:ElasticNet.

Linear regression regularized by a combination of L1 and L2 penalties. RegressionAnalysis does not require mixed L1/L2 penalties; existing Lasso and Ridge concepts cover the separate penalty types.

The cited method passage supports the maintained claim scope. RegressionAnalysis does not require mixed L1/L2 penalties; existing Lasso and Ridge concepts cover the separate penalty types. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:ExpectationMaximization.

Parameter estimation alternating expected complete-data log-likelihood evaluation and its maximization. MachineLearningTask does not identify the alternating expected-log-likelihood and maximization estimation procedure.

The cited method passage supports the maintained claim scope. MachineLearningTask does not identify the alternating expected-log-likelihood and maximization estimation procedure. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:FlashAttention.

An exact attention computation algorithm using tiling and recomputation to reduce transfers between GPU memory levels. The original dense exact-attention algorithm, not a distinct trained model, a generic attention layer, or its separately described block-sparse approximation.

The cited method passage supports the maintained claim scope. FlashAttention changes how attention is computed and stored, while this AIO target denotes a layer implementing attention. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:GaussianProcessRegression.

Probabilistic regression conditioning a Gaussian-process prior on observed training data. RegressionAnalysis does not specify conditioning a Gaussian-process prior.

The cited method passage supports the maintained claim scope. RegressionAnalysis does not specify conditioning a Gaussian-process prior. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:GeneticAlgorithm.

Evolutionary optimization using fitness-based selection and genetic variation of candidate solutions. MachineLearningTask does not specify evolutionary fitness selection, recombination and mutation; genetic optimization is not necessarily learning from data.

The cited method passage supports the maintained claim scope. MachineLearningTask does not specify evolutionary fitness selection, recombination and mutation; genetic optimization is not necessarily learning from data. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:GloVe.

Word-vector learning from global word co-occurrence statistics. The existing word2vec concepts use different training objectives. RepresentationLearning is defined as a deep neural network in this pin, so using it as a parent would need an upstream abstraction correction.

The cited method passage supports the maintained claim scope. The existing word2vec concepts use different training objectives. RepresentationLearning is defined as a deep neural network in this pin, so using it as a parent would need an upstream abstraction correction. Mapping is local curation, not an upstream subclass assertion. The existing word2vec concepts use different training objectives. RepresentationLearning is defined as a deep neural network in this pin, so using it as a parent would need an upstream abstraction correction. Mapping is local curation, not an upstream subclass assertion. The existing word2vec concepts use different training objectives. RepresentationLearning is defined as a deep neural network in this pin, so using it as a parent would need an upstream abstraction correction. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:GradientBoosting.

Boosting that adds predictors fitted to negative loss-function gradients. EnsembleLearning does not specify stagewise fitting to negative loss gradients.

The cited method passage supports the maintained claim scope. EnsembleLearning does not specify stagewise fitting to negative loss gradients. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:HDBSCAN.

Hierarchical density-based clustering that selects clusters across density scales. HierarchicalClustering does not specify density scales and cluster-stability selection.

The cited method passage supports the maintained claim scope. HierarchicalClustering does not specify density scales and cluster-stability selection. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:HiddenMarkovModel.

A sequence model whose hidden Markov states generate observations through state-dependent emission distributions. ProbabilisticGraphicalModel does not specify Markov hidden states and observation emissions.

The cited method passage supports the maintained claim scope. ProbabilisticGraphicalModel does not specify Markov hidden states and observation emissions. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:ID3.

Decision-tree induction that selects categorical attributes by information gain. DecisionTree does not identify information-gain-based categorical tree induction.

The cited method passage supports the maintained claim scope. DecisionTree does not identify information-gain-based categorical tree induction. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:KMeans.

Clustering that partitions observations around centroids by minimizing within-cluster squared distances. The Clustering task does not specify the centroid/squared-distance objective of this algorithm.

The cited method passage supports the maintained claim scope. The Clustering task does not specify the centroid/squared-distance objective of this algorithm. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:LeastAngleRegression.

Regression that advances along directions equiangular to predictors most correlated with the residual. RegressionAnalysis does not specify the equiangular active-predictor fitting path; distinguish this algorithm from the resulting regression model.

The cited method passage supports the maintained claim scope. RegressionAnalysis does not specify the equiangular active-predictor fitting path; distinguish this algorithm from the resulting regression model. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:LinearDiscriminantAnalysis.

Gaussian discriminant classification sharing one covariance matrix across classes. Classification does not specify Gaussian class models with shared covariance; distinguish the classifier from its dimension-reduction use.

The cited method passage supports the maintained claim scope. Classification does not specify Gaussian class models with shared covariance; distinguish the classifier from its dimension-reduction use. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:LoRA.

A parameter-efficient adaptation method that freezes pretrained weights and learns additive low-rank matrix updates. A method for adapting model parameters, not a pretrained checkpoint or the LoRA software package. AIO:TransferLearning is a broader task description and does not specify this weight-update factorization.

The cited method passage supports the maintained claim scope. LoRA implements an adaptation procedure; the AIO target denotes the general transfer-learning task rather than this factorization algorithm. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Mamba.

A neural sequence architecture built from repeated blocks containing input-dependent selective state-space transformations. The original Mamba architecture, not its trained checkpoints, all state-space models, or Mamba-2. Existing AIO recurrent and deep-network categories do not specify selective state-space blocks.

The cited method passage supports the maintained claim scope. Repeated learned blocks form a multilayer neural network; the target is broader than this specific architecture. Selective state updates use a temporal recurrence, but this mapping does not equate all recurrent networks with Mamba. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:MarkovDecisionProcess.

A sequential decision model with states, actions, Markov transitions, and rewards. Model does not require controlled Markov transitions and reward-based sequential decisions.

The cited method passage supports the maintained claim scope. Model does not require controlled Markov transitions and reward-based sequential decisions. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:MarkovRandomField.

An undirected graphical probability model associating potential functions with variable groups. ProbabilisticGraphicalModel covers broader directed and undirected dependencies; this candidate specifically uses an undirected graph.

The cited method passage supports the maintained claim scope. ProbabilisticGraphicalModel covers broader directed and undirected dependencies; this candidate specifically uses an undirected graph. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:MeanShift.

Mode-seeking clustering that moves candidate centers toward local density maxima. Clustering does not specify iterative mode seeking in a kernel density estimate.

The cited method passage supports the maintained claim scope. Clustering does not specify iterative mode seeking in a kernel density estimate. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:NaiveBayes.

Probabilistic classification assuming feature independence conditional on the class. Classification does not specify conditional feature independence or a probabilistic generative classifier.

The cited method passage supports the maintained claim scope. Classification does not specify conditional feature independence or a probabilistic generative classifier. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:OPTICS.

Density-based clustering analysis that orders observations using reachability across neighborhood scales. Clustering does not specify a reachability ordering across neighborhood scales; OPTICS is not identical to one flat partition.

The cited method passage supports the maintained claim scope. Clustering does not specify a reachability ordering across neighborhood scales; OPTICS is not identical to one flat partition. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:PartialLeastSquaresRegression.

Regression using latent components chosen to capture predictor-response covariance. RegressionAnalysis does not identify covariance-based latent predictor/response components.

The cited method passage supports the maintained claim scope. RegressionAnalysis does not identify covariance-based latent predictor/response components. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:PartiallyObservableMarkovDecisionProcess.

A Markov decision model in which observations provide incomplete information about the current state. Model does not require state uncertainty, actions, transition probabilities, observations and rewards.

The cited method passage supports the maintained claim scope. Model does not require state uncertainty, actions, transition probabilities, observations and rewards. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:QuadraticDiscriminantAnalysis.

Gaussian discriminant classification with class-specific covariance matrices. Classification does not specify Gaussian class models with class-specific covariance.

The cited method passage supports the maintained claim scope. Classification does not specify Gaussian class models with class-specific covariance. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:Stacking.

Ensemble learning that trains a final estimator on base-estimator predictions. EnsembleLearning does not require a learned final estimator on base-estimator predictions.

The cited method passage supports the maintained claim scope. EnsembleLearning does not require a learned final estimator on base-estimator predictions. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:StochasticGradientDescent.

Optimization using gradients estimated from sampled training observations. TrainingStrategy does not identify a stochastic optimization algorithm, and its preprocessing genus requires upstream clarification.

The cited method passage supports the maintained claim scope. TrainingStrategy does not identify a stochastic optimization algorithm, and its preprocessing genus requires upstream clarification. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

### Definition, method identity and inspected mechanism support

evidence: supported. Targets: AIMech:VotingClassifier.

A classifier combining base predictions through class votes or aggregated class probabilities. EnsembleLearning does not specify class voting or aggregation of class probabilities.

The cited method passage supports the maintained claim scope. EnsembleLearning does not specify class voting or aggregation of class probabilities. Mapping is local curation, not an upstream subclass assertion. The record remains DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier. Retain these narrow local identities: density/centroid clustering, alternative ensemble constructions, classifier covariance assumptions, tree-induction criteria, hidden-state versus controlled-decision models, estimation/optimization procedures and the modern adaptation/sequence/attention methods have different defining mechanisms or abstraction levels. Boosting and its named algorithms may overlap hierarchically without being equivalent. No AIO ID is replaced or merged.
- defer: AIMech:AdaBoost, AIMech:Apriori, AIMech:BIRCH, AIMech:Bagging, AIMech:Boosting, AIMech:C45, AIMech:CART, AIMech:DBSCAN, AIMech:DirectPreferenceOptimization, AIMech:Eclat, AIMech:ElasticNet, AIMech:ExpectationMaximization, AIMech:FlashAttention, AIMech:GaussianProcessRegression, AIMech:GeneticAlgorithm, AIMech:GloVe, AIMech:GradientBoosting, AIMech:HDBSCAN, AIMech:HiddenMarkovModel, AIMech:ID3, AIMech:KMeans, AIMech:LeastAngleRegression, AIMech:LinearDiscriminantAnalysis, AIMech:LoRA, AIMech:Mamba, AIMech:MarkovDecisionProcess, AIMech:MarkovRandomField, AIMech:MeanShift, AIMech:NaiveBayes, AIMech:OPTICS, AIMech:PartialLeastSquaresRegression, AIMech:PartiallyObservableMarkovDecisionProcess, AIMech:QuadraticDiscriminantAnalysis, AIMech:Stacking, AIMech:StochasticGradientDescent, AIMech:VotingClassifier. A complete local-to-upstream subclass hierarchy and a global lump/split audit remain unresolved. Inspect each upstream branch genus and full neighboring method definitions before replacing related mappings with stronger relations; continue the recorded literature frontier.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mapping-pin | sources/aio/aio.json; Named CLASS labels, definitions and scoped synonyms; all AIO targets listed in the curated mappings | supports | Compared candidate identity and method scope with the actual pinned class definitions. Task/model abstraction mismatches use related mappings; AIO assertions were not edited. |
| bounded-discovery | research/discovery/20261011T030803Z-first-native-cohort.json | supports | The first native cohort records 36 supported additions and a nonempty discovery frontier, with full-text PDF reading and visual-inspection provenance. |
| adaboost-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#adaboost; User Guide, section #adaboost | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Successive weak classifiers fit reweighted observations, increasing attention to samples misclassified by previous rounds. |
| apriori-method-source | https://borgelt.net/apriori.html; Author Apriori implementation page, Introduction: breadth-first traversal of the subset lattice and minimum-support test | supports | Apriori: Frequent Item Set Mining; Apriori 6.31 (2022-11-22) project description. Inspected documentation supports the narrowly stated definition and mechanism. A breadth-first subset-lattice search prunes candidate itemsets that cannot meet minimum support. |
| birch-method-source | https://scikit-learn.org/1.8/modules/clustering.html#birch; User Guide, section #birch | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Clustering features summarize counts, linear sums and squared sums in a tree before optional final clustering. |
| bagging-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#bagging-meta-estimator; User Guide, section #bagging-meta-estimator | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Base estimators are fitted on bootstrap samples and their predictions are aggregated. |
| boosting-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#gradient-boosted-trees; User Guide, section #gradient-boosted-trees | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. The ensemble is built sequentially, with each learner trained in relation to the current ensemble. |
| c45-method-source | https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart; User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart | supports | scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Continuous features can be split into discrete intervals while extending the ID3 tree-induction approach. |
| cart-method-source | https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart; User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart | supports | scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Binary tests recursively partition feature space to build a classification or regression tree. |
| dbscan-method-source | https://scikit-learn.org/1.8/modules/clustering.html#dbscan; User Guide, section #dbscan | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Core observations have sufficiently many neighbors within a radius; density-connected cores form clusters with neighboring border observations. |
| directpreferenceoptimization-original-paper | https://arxiv.org/pdf/2305.18290v3; Section 4, equations 4–7, PDF/printed p. 4 | supports | Direct Preference Optimization: Your Language Model is Secretly a Reward Model; 2305.18290v3. Inspected full_text supports the narrowly stated definition and mechanism. A reward-to-policy reparameterization yields a logistic preference loss that trains the policy without separately fitting an explicit reward model. |
| eclat-method-source | https://borgelt.net/eclat.html; Author Eclat implementation page, Introduction: depth-first enumeration and intersection of transaction sets | supports | Eclat: Frequent Item Set Mining; Eclat 5.24 (2022-11-22) project description. Inspected documentation supports the narrowly stated definition and mechanism. Depth-first itemset enumeration intersects transaction sets to calculate support. |
| elasticnet-method-source | https://scikit-learn.org/1.8/modules/linear_model.html#elastic-net; User Guide, section #elastic-net | supports | scikit-learn User Guide: linear model; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. The fitting objective combines a squared-error term with L1 and squared L2 penalties on coefficients. |
| expectationmaximization-method-source | https://people.ece.uw.edu/bilmes/p/mypubs/bilmes1997-em.pdf#page=4; Bilmes, TR-97-021 (PDF cover dated April 1998), section 2 Basic EM, PDF pp. 3–4: expected log-likelihood Q, E-step and M-step | supports | A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian Mixture and Hidden Markov Models; TR-97-021; PDF cover dated April 1998. Inspected full_text supports the narrowly stated definition and mechanism. The E-step evaluates the expected complete-data log likelihood under current parameters; the M-step maximizes that expected objective. |
| flashattention-original-paper | https://arxiv.org/pdf/2205.14135v2; Sections 3.1–3.2 and Algorithm 1, PDF/printed pp. 4–6 | supports | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness; 2205.14135v2. Inspected full_text supports the narrowly stated definition and mechanism. Blocks of queries, keys and values are processed with running softmax statistics; intermediate attention values can be recomputed during the backward pass. |
| gaussianprocessregression-method-source | https://scikit-learn.org/1.8/modules/gaussian_process.html#gaussian-process-regression-gpr; User Guide, section #gaussian-process-regression-gpr | supports | scikit-learn User Guide: gaussian process; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. A kernel defines a Gaussian-process prior whose conditioning on observations gives a predictive distribution. |
| geneticalgorithm-method-source | https://deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple; DEAP algorithms documentation, eaSimple pseudocode: evaluate, select, varAnd, mate and mutate | supports | DEAP algorithms: eaSimple; DEAP 1.4.1 stable documentation as inspected. Inspected documentation supports the narrowly stated definition and mechanism. Fitness evaluation and selection are combined with crossover and mutation to produce successive populations. |
| glove-method-source | https://aclanthology.org/D14-1162.pdf; Section 3, equations 6–9, printed pp. 1534–1535 / PDF pp. 3–4 | supports | GloVe: Global Vectors for Word Representation; EMNLP 2014, D14-1162. Inspected full_text supports the narrowly stated definition and mechanism. A weighted least-squares objective fits word-vector dot products and biases to logarithms of word co-occurrence counts. |
| gradientboosting-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#mathematical-formulation; User Guide, section #mathematical-formulation | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Each stage fits a learner to negative loss gradients evaluated at the current additive predictor. |
| hdbscan-method-source | https://scikit-learn.org/1.8/modules/clustering.html#hdbscan; User Guide, section #hdbscan | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Mutual-reachability distances produce a density hierarchy from which persistent clusters are selected. |
| hiddenmarkovmodel-method-source | https://hmmlearn.readthedocs.io/en/0.3.3/tutorial.html; hmmlearn 0.3.3 tutorial, opening HMM generative-process definition and parameter list | supports | hmmlearn tutorial; hmmlearn 0.3.3. Inspected documentation supports the narrowly stated definition and mechanism. The current hidden state depends on the previous state, and an observation is generated from the current state emission distribution. |
| id3-method-source | https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart; User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart | supports | scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. At each node an information-gain criterion selects a categorical feature for partitioning the observations. |
| kmeans-method-source | https://scikit-learn.org/1.8/modules/clustering.html#k-means; User Guide, section #k-means | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. The fitting procedure alternates assignment to the nearest centroid and centroid updates from assigned observations. |
| leastangleregression-method-source | https://scikit-learn.org/1.8/modules/linear_model.html#least-angle-regression; User Guide, section #least-angle-regression | supports | scikit-learn User Guide: linear model; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. The coefficient path moves in a direction equiangular to the active predictors until another predictor joins the active set. |
| lineardiscriminantanalysis-method-source | https://scikit-learn.org/1.8/modules/lda_qda.html#lda; User Guide, section #lda | supports | scikit-learn User Guide: lda qda; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Gaussian class-conditional distributions share a covariance matrix, producing linear decision boundaries. |
| lora-original-paper | https://arxiv.org/pdf/2106.09685v2; Section 4.1, equation 3, PDF/printed p. 4; Section 4.2, Practical Benefits and Limitations, PDF/printed p. 5 | supports | LoRA: Low-Rank Adaptation of Large Language Models; 2106.09685v2. Inspected full_text supports the narrowly stated definition and mechanism. An adapted linear transformation uses W0x + BAx, with W0 fixed and the lower-rank factors A and B trainable. |
| mamba-original-paper | https://arxiv.org/pdf/2312.00752v2; Sections 3.2–3.4, Algorithm 2 and Figure 3, PDF/printed pp. 5–8 | supports | Mamba: Linear-Time Sequence Modeling with Selective State Spaces; 2312.00752v2. Inspected full_text supports the narrowly stated definition and mechanism. Input-dependent B, C and time-step parameters control selective state updates; a scan computes the recurrence inside repeated gated blocks. |
| markovdecisionprocess-method-source | https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=3; Kaelbling, Littman and Cassandra (1998), section 2.1, printed pp. 101–102 / PDF pp. 3–4: states, actions, transitions and rewards | supports | Planning and acting in partially observable stochastic domains; Artificial Intelligence 101 (1998), 99–134. Inspected full_text supports the narrowly stated definition and mechanism. Actions condition transitions between states and yield rewards used to define a policy objective. |
| markovrandomfield-method-source | https://raw.githubusercontent.com/pgmpy/pgmpy/1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312/pgmpy/models/DiscreteMarkovNetwork.py; DiscreteMarkovNetwork.py at commit 1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312, class docstring (lines 16–29) and add_factors docstring (lines 109–145) | supports | pgmpy DiscreteMarkovNetwork class and method documentation; 1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312. Inspected documentation supports the narrowly stated definition and mechanism. Undirected graph structure and factors over variable groups represent probabilistic dependencies. |
| meanshift-method-source | https://scikit-learn.org/1.8/modules/clustering.html#mean-shift; User Guide, section #mean-shift | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Candidate centers are iteratively shifted toward local means of observations in their neighborhoods. |
| naivebayes-method-source | https://scikit-learn.org/1.8/modules/naive_bayes.html#naive-bayes; User Guide, section #naive-bayes | supports | scikit-learn User Guide: naive bayes; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Class posterior comparisons use class priors and the product of class-conditional feature likelihoods. |
| optics-method-source | https://scikit-learn.org/1.8/modules/clustering.html#optics; User Guide, section #optics | supports | scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Reachability distances are recorded in an ordering that supports extracting clusters at different density thresholds. |
| partialleastsquaresregression-method-source | https://scikit-learn.org/1.8/modules/cross_decomposition.html#cross-decomposition; User Guide, section #cross-decomposition | supports | scikit-learn User Guide: cross decomposition; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Predictors and responses are projected onto latent components chosen using their cross-covariance. |
| partiallyobservablemarkovdecisionprocess-method-source | https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=7; Kaelbling, Littman and Cassandra (1998), section 3.1, printed p. 105 / PDF p. 7: POMDP tuple and observation model | supports | Planning and acting in partially observable stochastic domains; Artificial Intelligence 101 (1998), 99–134. Inspected full_text supports the narrowly stated definition and mechanism. The model specifies state transitions and an observation distribution conditional on the resulting state and action. |
| quadraticdiscriminantanalysis-method-source | https://scikit-learn.org/1.8/modules/lda_qda.html#qda; User Guide, section #qda | supports | scikit-learn User Guide: lda qda; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Gaussian class-conditional distributions use separate covariance matrices, allowing quadratic decision boundaries. |
| stacking-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#stacked-generalization; User Guide, section #stacked-generalization | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. A final estimator learns from predictions of base estimators; held-out predictions can separate its training from base-estimator fitting. |
| stochasticgradientdescent-method-source | https://scikit-learn.org/1.8/modules/sgd.html#id5; User Guide, section #id5 | supports | scikit-learn User Guide: sgd; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Parameters are updated using an estimated objective gradient computed from sampled training observations. |
| votingclassifier-method-source | https://scikit-learn.org/1.8/modules/ensemble.html#voting-classifier; User Guide, section #voting-classifier | supports | scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation supports the narrowly stated definition and mechanism. Hard voting combines predicted labels; soft voting combines predicted class probabilities. |

## Limits And Additional Notes

- This is scientific self-review of stated identity and method support, not independent peer review or reproduction of experiments.
- Literature inspection occurred during the documented discovery/curation session; the review timestamps record this post-inspection assessment and artifact preparation.
- Official implementation documentation is narrower than a complete historical literature review; the MRF example is discrete and LDA covers its classifier use.
- Source URLs that are access-dated documentation may change; named versions and available byte hashes are preserved, but not every historical website is immutable.
- No performance, universal convergence, biological efficacy or general safety claim is assessed. Native status remains DRAFT.
- The full discovery goal is incomplete: this batch adds 36 concepts and retains known candidate and source leads.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T031038Z-first-native-mechanisms
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of the first 36 native concept definitions and mechanisms
started_at: '2026-10-11T03:10:38Z'
finished_at: '2026-10-11T03:10:38Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent curated these records, inspected the cited evidence
    and prepared this review; independent scientific review is not claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All 36 selected maintained records have supported narrow definitions/mechanisms,
  explicit AIO relationships and honest draft provenance. No unresolved curation finding
  remains within this scope. This does not certify empirical performance, exhaust
  discovery or endorse upstream hierarchy boundaries.
source:
  git_revision: 945bd67d190e867ac379f8d4ebbc6d4ddec152a9
  state: working_tree
  inputs:
  - path: data/curated/AdaBoost.yaml
    sha256: 3a638260e1acaae439b1daaee4ce515cd7420df5fafa2f34a3df03ce14120105
    role: target
  - path: data/curated/Apriori.yaml
    sha256: ecdb6f7857fe97ae313e2e6c95984852213e1647bc4b4ab81a30e81a989c71a6
    role: target
  - path: data/curated/BIRCH.yaml
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    role: target
  - path: data/curated/Bagging.yaml
    sha256: c7860fed789012e17dd1f696a44dbc71be12fe393fa1dec96a3245940ec86d81
    role: target
  - path: data/curated/Boosting.yaml
    sha256: eedf8d5bf384aa6fc25f823b4fe9847b8b9d26fa0d850acdf2b435296e17a3e0
    role: target
  - path: data/curated/C45.yaml
    sha256: b58efdbb4ec07063fd6e5fd3d0baab4686259af6016c4d718aa82152d3726fbc
    role: target
  - path: data/curated/CART.yaml
    sha256: 7c462535877d208fb47c6e418f7c9bdd0305b51cada89db1388fad19845f0178
    role: target
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: target
  - path: data/curated/DirectPreferenceOptimization.yaml
    sha256: 1c1a5dc9cae9c67e33a00f1e6210d9ddecb8a3bde53cbcd923b579f36238b14f
    role: target
  - path: data/curated/Eclat.yaml
    sha256: 9e293cd6daaa774fde31780d488b42194477c9f4284857697a74f2d34ce46aac
    role: target
  - path: data/curated/ElasticNet.yaml
    sha256: b441d7068b074ed4e86fb51f24130cb3a9fb1eaff86e4fc318e619c21699ce6c
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: target
  - path: data/curated/FlashAttention.yaml
    sha256: 227618e46e070c5d5aa6f78f8587763b3d1bc739b457adcc0621779c5b89930d
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: target
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: target
  - path: data/curated/GloVe.yaml
    sha256: 4a37b142c697215fe20f195a762e8dfbae2727b945c14732b9de8d0a2dfbfd92
    role: target
  - path: data/curated/GradientBoosting.yaml
    sha256: 2e89ee7d292a071d6d4b8aecf81cd57cae84a50a2d167cc69ffee2cebf4dffe5
    role: target
  - path: data/curated/HDBSCAN.yaml
    sha256: 46232d726b6e52f2373481fe18f52e3c9721aee83700311012ad07e3cc2704f3
    role: target
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: target
  - path: data/curated/ID3.yaml
    sha256: 5d0bbbe3eff68ad1b163c763d7b73ea7aa9535851096c5be4ec32b9dc34eab01
    role: target
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: target
  - path: data/curated/LeastAngleRegression.yaml
    sha256: 379431bca38c3bbac6653617a424e692fba98edc1cf7f8d25b388328e5fe7ab5
    role: target
  - path: data/curated/LinearDiscriminantAnalysis.yaml
    sha256: cb194468de3c200a57f1d6338e13b604775ce8a10b5517966459242410752b6a
    role: target
  - path: data/curated/LoRA.yaml
    sha256: 8642959e7dd4ca6630720e78771b6e7b825336c967f0663f125c1a23aee7ae49
    role: target
  - path: data/curated/Mamba.yaml
    sha256: 281525b8bfa665b2e777cdda49450449e8a60ab845911118d8020228b688fb3c
    role: target
  - path: data/curated/MarkovDecisionProcess.yaml
    sha256: 9db1ed4a4b01f70cffafe2bcabe7be214779adacf4d7b31c9348ed5f9f54b907
    role: target
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: target
  - path: data/curated/MeanShift.yaml
    sha256: 3e6868e9d4786ef56fc10af3e1b9e8fd8a3cd15fa8e63d058ba99a3d9567448a
    role: target
  - path: data/curated/NaiveBayes.yaml
    sha256: 99caf757d49a76920b59c60591beeaf1f019ec0d1acb7ae5944ea0f5f7339b61
    role: target
  - path: data/curated/OPTICS.yaml
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    role: target
  - path: data/curated/PartialLeastSquaresRegression.yaml
    sha256: 3d34b3313b0580f1aa7316f588cc38589056e8b58711d1944b346f8a0c394ea4
    role: target
  - path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    sha256: 2930142265ec082e972e8ccd05cff84685d611596a58af2af39c4f7b80a16577
    role: target
  - path: data/curated/QuadraticDiscriminantAnalysis.yaml
    sha256: 31a1b7c08a1bae221d571e26441b4690456524b409a33df84427ff929cb4dd3e
    role: target
  - path: data/curated/Stacking.yaml
    sha256: 5271ce4094a5beec8dc87500e64d9c779ec4aec9bbcb20d0efcc22d26e62706b
    role: target
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: target
  - path: data/curated/VotingClassifier.yaml
    sha256: 648ff71f5b9e964aea0fcab2e0430be345884c9c98c8250f76e1ad9a396903cf
    role: target
  - path: docs/proposals/aio/classical-ml-candidates.json
    sha256: 0a5734828d1e4a752723387c64fed0d0f2982114cb33aa272e30b78cfa6075a9
    role: context
  - path: docs/record-review-profile.md
    sha256: 64ce9def82009730ad5b8de54de48771d3eb299a1da42ce8ab5973a9fcd55add
    role: context
  - path: research/discovery/20261011T030803Z-first-native-cohort.json
    sha256: 5b4c66fe530b2cad8a9c8cafef989a0b34c4ebb78ad790511013787c4a3a9225
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 1efe838d99526a85e5b678a70bad7b796edfcc922e7b912a9d4592da78843bbe
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 529cb70f3fa95580d6197c1581e0b3ad62c17f128d3ed1ba848f54d184f4e312
    role: context
targets:
- target_id: AIMech:AdaBoost
  path: data/curated/AdaBoost.yaml
  label: AdaBoost
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaBoost.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Apriori
  path: data/curated/Apriori.yaml
  label: Apriori
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Apriori.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:BIRCH
  path: data/curated/BIRCH.yaml
  label: BIRCH
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BIRCH.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Bagging
  path: data/curated/Bagging.yaml
  label: Bagging
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Bagging.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Boosting
  path: data/curated/Boosting.yaml
  label: Boosting
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Boosting.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:C45
  path: data/curated/C45.yaml
  label: C4.5
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/C45.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:CART
  path: data/curated/CART.yaml
  label: CART
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CART.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:DBSCAN
  path: data/curated/DBSCAN.yaml
  label: DBSCAN
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DBSCAN.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:DirectPreferenceOptimization
  path: data/curated/DirectPreferenceOptimization.yaml
  label: Direct preference optimization
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DirectPreferenceOptimization.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Eclat
  path: data/curated/Eclat.yaml
  label: Eclat
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Eclat.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:ElasticNet
  path: data/curated/ElasticNet.yaml
  label: Elastic net
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ElasticNet.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:ExpectationMaximization
  path: data/curated/ExpectationMaximization.yaml
  label: Expectation maximization
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExpectationMaximization.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:FlashAttention
  path: data/curated/FlashAttention.yaml
  label: FlashAttention
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FlashAttention.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:GaussianProcessRegression
  path: data/curated/GaussianProcessRegression.yaml
  label: Gaussian process regression
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianProcessRegression.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:GeneticAlgorithm
  path: data/curated/GeneticAlgorithm.yaml
  label: Genetic algorithm
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GeneticAlgorithm.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:GloVe
  path: data/curated/GloVe.yaml
  label: GloVe
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GloVe.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:GradientBoosting
  path: data/curated/GradientBoosting.yaml
  label: Gradient boosting machine
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GradientBoosting.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:HDBSCAN
  path: data/curated/HDBSCAN.yaml
  label: HDBSCAN
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HDBSCAN.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:HiddenMarkovModel
  path: data/curated/HiddenMarkovModel.yaml
  label: Hidden Markov model
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovModel.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:ID3
  path: data/curated/ID3.yaml
  label: ID3
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ID3.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:KMeans
  path: data/curated/KMeans.yaml
  label: k-means
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KMeans.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:LeastAngleRegression
  path: data/curated/LeastAngleRegression.yaml
  label: Least-angle regression
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LeastAngleRegression.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:LinearDiscriminantAnalysis
  path: data/curated/LinearDiscriminantAnalysis.yaml
  label: Linear discriminant analysis
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LinearDiscriminantAnalysis.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:LoRA
  path: data/curated/LoRA.yaml
  label: Low-rank adaptation
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LoRA.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Mamba
  path: data/curated/Mamba.yaml
  label: Mamba sequence architecture
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Mamba.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:MarkovDecisionProcess
  path: data/curated/MarkovDecisionProcess.yaml
  label: Markov decision process
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovDecisionProcess.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:MarkovRandomField
  path: data/curated/MarkovRandomField.yaml
  label: Markov random field
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MarkovRandomField.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:MeanShift
  path: data/curated/MeanShift.yaml
  label: Mean shift
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MeanShift.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:NaiveBayes
  path: data/curated/NaiveBayes.yaml
  label: Naive Bayes
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaiveBayes.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:OPTICS
  path: data/curated/OPTICS.yaml
  label: OPTICS
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OPTICS.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:PartialLeastSquaresRegression
  path: data/curated/PartialLeastSquaresRegression.yaml
  label: Partial least squares regression
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartialLeastSquaresRegression.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:PartiallyObservableMarkovDecisionProcess
  path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
  label: Partially observable Markov decision process
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:QuadraticDiscriminantAnalysis
  path: data/curated/QuadraticDiscriminantAnalysis.yaml
  label: Quadratic discriminant analysis
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/QuadraticDiscriminantAnalysis.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:Stacking
  path: data/curated/Stacking.yaml
  label: Stacking
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Stacking.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:StochasticGradientDescent
  path: data/curated/StochasticGradientDescent.yaml
  label: Stochastic gradient descent
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticGradientDescent.yaml
    role: maintained concept and evidence assertions
- target_id: AIMech:VotingClassifier
  path: data/curated/VotingClassifier.yaml
  label: Voting classifier
  record_class: CuratedAIConcept
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VotingClassifier.yaml
    role: maintained concept and evidence assertions
scope:
  description: Definition, identity, mechanism citation and AIO mapping direction
    for the first 36 maintained concepts.
  selection: Select exactly the 36 paths in the inspected first-native-cohort manifest;
    all selected records reviewed without sampling.
  coverage: full
  population_size: 36
  reviewed_target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  exclusions:
  - target: 442 generated AIO records
    reason: Used as mapping/identity context; their scientific assertions were not
      reviewed in this native-record cohort.
  - target: Uncurated literature leads and benchmark results
    reason: The discovery frontier remains active; no uninspected claim is certified.
checks:
- check_id: check-1
  name: python -m aimech check-source
  status: passed
  required: true
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python -m aimech check-source
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: check-2
  name: python -m aimech validate
  status: passed
  required: true
  summary: Checked 442 record(s); 0 failed.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python -m aimech validate
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: check-3
  name: python -m aimech validate-curated
  status: passed
  required: true
  summary: Checked 36 curated concept record(s); 0 error(s).
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python -m aimech validate-curated
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: check-4
  name: python -m aimech seed --check
  status: passed
  required: true
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python -m aimech seed --check
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: check-5
  name: python -m aimech validate-history --base HEAD
  status: passed
  required: true
  summary: Checked 5 history record(s); 0 error(s).
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python -m aimech validate-history --base HEAD
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: check-6
  name: python scripts/record_review.py check
  status: passed
  required: true
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 1,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class"
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run in the isolated worktree with PYTHONPATH selecting its source package
    and the shared locked environment.
- check_id: full-gate
  name: Repository code and schema quality gate
  status: passed
  required: true
  summary: 209 tests passed, 3 skipped; 442 AIO records reproduced; 36 native records
    passed; history and review checks passed.
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  exit_code: 0
  expected_exit_code: 0
  scope_note: The full gate preceded the final MRF provenance and POMDP wording corrections;
    the current curated data and all mandatory record checks were rerun afterward.
    No code/schema changed between those checks.
evidence:
- evidence_id: mapping-pin
  kind: record_content
  reference: sources/aio/aio.json
  locator: Named CLASS labels, definitions and scoped synonyms; all AIO targets listed
    in the curated mappings
  accessed_at: '2026-10-11T03:10:38Z'
  support: supports
  snapshot_sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
  summary: Compared candidate identity and method scope with the actual pinned class
    definitions. Task/model abstraction mismatches use related mappings; AIO assertions
    were not edited.
- evidence_id: bounded-discovery
  kind: search
  reference: research/discovery/20261011T030803Z-first-native-cohort.json
  accessed_at: '2026-10-11T03:10:38Z'
  support: supports
  summary: The first native cohort records 36 supported additions and a nonempty discovery
    frontier, with full-text PDF reading and visual-inspection provenance.
  search_scope: Original checkout and isolated goal worktree searched with rg --no-ignore
    --hidden; normalized labels and aliases checked against all 442 AIO classes. The
    earlier 32-candidate proposal and modern-method searches are bounded identity
    checks, not exhaustive literature coverage.
- evidence_id: adaboost-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#adaboost
  locator: 'User Guide, section #adaboost'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Successive weak classifiers
    fit reweighted observations, increasing attention to samples misclassified by
    previous rounds.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
- evidence_id: apriori-method-source
  kind: authority
  reference: https://borgelt.net/apriori.html
  locator: 'Author Apriori implementation page, Introduction: breadth-first traversal
    of the subset lattice and minimum-support test'
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: 'Apriori: Frequent Item Set Mining; Apriori 6.31 (2022-11-22) project description.
    Inspected documentation supports the narrowly stated definition and mechanism.
    A breadth-first subset-lattice search prunes candidate itemsets that cannot meet
    minimum support.'
- evidence_id: birch-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#birch
  locator: 'User Guide, section #birch'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Clustering features summarize
    counts, linear sums and squared sums in a tree before optional final clustering.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: bagging-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#bagging-meta-estimator
  locator: 'User Guide, section #bagging-meta-estimator'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Base estimators are fitted
    on bootstrap samples and their predictions are aggregated.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
- evidence_id: boosting-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#gradient-boosted-trees
  locator: 'User Guide, section #gradient-boosted-trees'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. The ensemble is built sequentially,
    with each learner trained in relation to the current ensemble.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
- evidence_id: c45-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart
  locator: 'User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Continuous features can
    be split into discrete intervals while extending the ID3 tree-induction approach.'
  snapshot_sha256: 47f9ba403f4f8ef1311c5fef3fbebd975acfba2cdfacb9e9a5ee981fd6401ebb
- evidence_id: cart-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart
  locator: 'User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Binary tests recursively
    partition feature space to build a classification or regression tree.'
  snapshot_sha256: 47f9ba403f4f8ef1311c5fef3fbebd975acfba2cdfacb9e9a5ee981fd6401ebb
- evidence_id: dbscan-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#dbscan
  locator: 'User Guide, section #dbscan'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Core observations have
    sufficiently many neighbors within a radius; density-connected cores form clusters
    with neighboring border observations.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: directpreferenceoptimization-original-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/2305.18290v3
  locator: Section 4, equations 4–7, PDF/printed p. 4
  accessed_at: '2026-10-11T02:58:44Z'
  support: supports
  summary: 'Direct Preference Optimization: Your Language Model is Secretly a Reward
    Model; 2305.18290v3. Inspected full_text supports the narrowly stated definition
    and mechanism. A reward-to-policy reparameterization yields a logistic preference
    loss that trains the policy without separately fitting an explicit reward model.'
  snapshot_sha256: 92cb3a2b71362acda98a789b03d88688fd33cf5fcf13f81d2b1de30ee7d3b67a
- evidence_id: eclat-method-source
  kind: authority
  reference: https://borgelt.net/eclat.html
  locator: 'Author Eclat implementation page, Introduction: depth-first enumeration
    and intersection of transaction sets'
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: 'Eclat: Frequent Item Set Mining; Eclat 5.24 (2022-11-22) project description.
    Inspected documentation supports the narrowly stated definition and mechanism.
    Depth-first itemset enumeration intersects transaction sets to calculate support.'
- evidence_id: elasticnet-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/linear_model.html#elastic-net
  locator: 'User Guide, section #elastic-net'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: linear model; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. The fitting objective combines
    a squared-error term with L1 and squared L2 penalties on coefficients.'
  snapshot_sha256: 358fa62c5481b2f90974d9ea42895548ffd796ae199fcf99ea43c4b57e65cf9b
- evidence_id: expectationmaximization-method-source
  kind: primary_source
  reference: https://people.ece.uw.edu/bilmes/p/mypubs/bilmes1997-em.pdf#page=4
  locator: 'Bilmes, TR-97-021 (PDF cover dated April 1998), section 2 Basic EM, PDF
    pp. 3–4: expected log-likelihood Q, E-step and M-step'
  accessed_at: '2026-10-11T02:45:28Z'
  support: supports
  summary: A Gentle Tutorial of the EM Algorithm and its Application to Parameter
    Estimation for Gaussian Mixture and Hidden Markov Models; TR-97-021; PDF cover
    dated April 1998. Inspected full_text supports the narrowly stated definition
    and mechanism. The E-step evaluates the expected complete-data log likelihood
    under current parameters; the M-step maximizes that expected objective.
- evidence_id: flashattention-original-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/2205.14135v2
  locator: Sections 3.1–3.2 and Algorithm 1, PDF/printed pp. 4–6
  accessed_at: '2026-10-11T02:58:44Z'
  support: supports
  summary: 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness;
    2205.14135v2. Inspected full_text supports the narrowly stated definition and
    mechanism. Blocks of queries, keys and values are processed with running softmax
    statistics; intermediate attention values can be recomputed during the backward
    pass.'
  snapshot_sha256: ca7f9fda10b90fc05dd291a3accc85e9c1a4a860b99b31928dab03ed3fcb14e4
- evidence_id: gaussianprocessregression-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/gaussian_process.html#gaussian-process-regression-gpr
  locator: 'User Guide, section #gaussian-process-regression-gpr'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: gaussian process; scikit-learn 1.8. Inspected
    documentation supports the narrowly stated definition and mechanism. A kernel
    defines a Gaussian-process prior whose conditioning on observations gives a predictive
    distribution.'
  snapshot_sha256: 326f800aca2d88712eff4742f711c5d73fe275b721ddc26f5ecc679afca2cd1a
- evidence_id: geneticalgorithm-method-source
  kind: authority
  reference: https://deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple
  locator: 'DEAP algorithms documentation, eaSimple pseudocode: evaluate, select,
    varAnd, mate and mutate'
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: 'DEAP algorithms: eaSimple; DEAP 1.4.1 stable documentation as inspected.
    Inspected documentation supports the narrowly stated definition and mechanism.
    Fitness evaluation and selection are combined with crossover and mutation to produce
    successive populations.'
- evidence_id: glove-method-source
  kind: primary_source
  reference: https://aclanthology.org/D14-1162.pdf
  locator: Section 3, equations 6–9, printed pp. 1534–1535 / PDF pp. 3–4
  accessed_at: '2026-10-11T03:00:17Z'
  support: supports
  summary: 'GloVe: Global Vectors for Word Representation; EMNLP 2014, D14-1162. Inspected
    full_text supports the narrowly stated definition and mechanism. A weighted least-squares
    objective fits word-vector dot products and biases to logarithms of word co-occurrence
    counts.'
  snapshot_sha256: 6631a1719122a89b3941d851a55ecf38c55971c36b30ae9c0cec617124056adf
- evidence_id: gradientboosting-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#mathematical-formulation
  locator: 'User Guide, section #mathematical-formulation'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Each stage fits a learner
    to negative loss gradients evaluated at the current additive predictor.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
- evidence_id: hdbscan-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#hdbscan
  locator: 'User Guide, section #hdbscan'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Mutual-reachability distances
    produce a density hierarchy from which persistent clusters are selected.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: hiddenmarkovmodel-method-source
  kind: authority
  reference: https://hmmlearn.readthedocs.io/en/0.3.3/tutorial.html
  locator: hmmlearn 0.3.3 tutorial, opening HMM generative-process definition and
    parameter list
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: hmmlearn tutorial; hmmlearn 0.3.3. Inspected documentation supports the
    narrowly stated definition and mechanism. The current hidden state depends on
    the previous state, and an observation is generated from the current state emission
    distribution.
- evidence_id: id3-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart
  locator: 'User Guide, section #tree-algorithms-id3-c4-5-c5-0-and-cart'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: tree; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. At each node an information-gain
    criterion selects a categorical feature for partitioning the observations.'
  snapshot_sha256: 47f9ba403f4f8ef1311c5fef3fbebd975acfba2cdfacb9e9a5ee981fd6401ebb
- evidence_id: kmeans-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#k-means
  locator: 'User Guide, section #k-means'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. The fitting procedure alternates
    assignment to the nearest centroid and centroid updates from assigned observations.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: leastangleregression-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/linear_model.html#least-angle-regression
  locator: 'User Guide, section #least-angle-regression'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: linear model; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. The coefficient path moves
    in a direction equiangular to the active predictors until another predictor joins
    the active set.'
  snapshot_sha256: 358fa62c5481b2f90974d9ea42895548ffd796ae199fcf99ea43c4b57e65cf9b
- evidence_id: lineardiscriminantanalysis-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/lda_qda.html#lda
  locator: 'User Guide, section #lda'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: lda qda; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Gaussian class-conditional
    distributions share a covariance matrix, producing linear decision boundaries.'
  snapshot_sha256: 367d42c265bff7014504d7e36740716eabd1fbff15c292b995637254485b06e1
- evidence_id: lora-original-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/2106.09685v2
  locator: Section 4.1, equation 3, PDF/printed p. 4; Section 4.2, Practical Benefits
    and Limitations, PDF/printed p. 5
  accessed_at: '2026-10-11T02:58:44Z'
  support: supports
  summary: 'LoRA: Low-Rank Adaptation of Large Language Models; 2106.09685v2. Inspected
    full_text supports the narrowly stated definition and mechanism. An adapted linear
    transformation uses W0x + BAx, with W0 fixed and the lower-rank factors A and
    B trainable.'
  snapshot_sha256: e9a0d3128767db616085dc0f4e6e455e672e89af823e8ed1282793682787395a
- evidence_id: mamba-original-paper
  kind: primary_source
  reference: https://arxiv.org/pdf/2312.00752v2
  locator: Sections 3.2–3.4, Algorithm 2 and Figure 3, PDF/printed pp. 5–8
  accessed_at: '2026-10-11T02:58:44Z'
  support: supports
  summary: 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces; 2312.00752v2.
    Inspected full_text supports the narrowly stated definition and mechanism. Input-dependent
    B, C and time-step parameters control selective state updates; a scan computes
    the recurrence inside repeated gated blocks.'
  snapshot_sha256: adf70ed1803c85b1899dec3e21f3af0b124411439e8654b840ea65f7b9f52b2e
- evidence_id: markovdecisionprocess-method-source
  kind: primary_source
  reference: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=3
  locator: 'Kaelbling, Littman and Cassandra (1998), section 2.1, printed pp. 101–102
    / PDF pp. 3–4: states, actions, transitions and rewards'
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: Planning and acting in partially observable stochastic domains; Artificial
    Intelligence 101 (1998), 99–134. Inspected full_text supports the narrowly stated
    definition and mechanism. Actions condition transitions between states and yield
    rewards used to define a policy objective.
- evidence_id: markovrandomfield-method-source
  kind: authority
  reference: https://raw.githubusercontent.com/pgmpy/pgmpy/1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312/pgmpy/models/DiscreteMarkovNetwork.py
  locator: DiscreteMarkovNetwork.py at commit 1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312,
    class docstring (lines 16–29) and add_factors docstring (lines 109–145)
  accessed_at: '2026-10-11T03:03:12Z'
  support: supports
  summary: pgmpy DiscreteMarkovNetwork class and method documentation; 1f6296fc2606eb479f1f1b9fbfdd9c41aa7ad312.
    Inspected documentation supports the narrowly stated definition and mechanism.
    Undirected graph structure and factors over variable groups represent probabilistic
    dependencies.
  snapshot_sha256: 1c71a02efcff7432ef862f134667c785224ae216f052a7c3bc54db466721a99f
- evidence_id: meanshift-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#mean-shift
  locator: 'User Guide, section #mean-shift'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Candidate centers are iteratively
    shifted toward local means of observations in their neighborhoods.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: naivebayes-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/naive_bayes.html#naive-bayes
  locator: 'User Guide, section #naive-bayes'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: naive bayes; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Class posterior comparisons
    use class priors and the product of class-conditional feature likelihoods.'
  snapshot_sha256: a69210ae66552ba1f8fc86126152858eb3796ce93fafa62a4edda5f7f4ea9eed
- evidence_id: optics-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/clustering.html#optics
  locator: 'User Guide, section #optics'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: clustering; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Reachability distances
    are recorded in an ordering that supports extracting clusters at different density
    thresholds.'
  snapshot_sha256: 323e56d3d77e8c185dd1dd0bf7153b85da7019d555562d1edaa741ddbc59e10a
- evidence_id: partialleastsquaresregression-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/cross_decomposition.html#cross-decomposition
  locator: 'User Guide, section #cross-decomposition'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: cross decomposition; scikit-learn 1.8. Inspected
    documentation supports the narrowly stated definition and mechanism. Predictors
    and responses are projected onto latent components chosen using their cross-covariance.'
  snapshot_sha256: d73a2c0457769dc5fd9983452ae253b5cf290c60aeca044e20eb7b15df7f6e3f
- evidence_id: partiallyobservablemarkovdecisionprocess-method-source
  kind: primary_source
  reference: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf#page=7
  locator: 'Kaelbling, Littman and Cassandra (1998), section 3.1, printed p. 105 /
    PDF p. 7: POMDP tuple and observation model'
  accessed_at: '2026-10-11T02:40:02Z'
  support: supports
  summary: Planning and acting in partially observable stochastic domains; Artificial
    Intelligence 101 (1998), 99–134. Inspected full_text supports the narrowly stated
    definition and mechanism. The model specifies state transitions and an observation
    distribution conditional on the resulting state and action.
- evidence_id: quadraticdiscriminantanalysis-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/lda_qda.html#qda
  locator: 'User Guide, section #qda'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: lda qda; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Gaussian class-conditional
    distributions use separate covariance matrices, allowing quadratic decision boundaries.'
  snapshot_sha256: 367d42c265bff7014504d7e36740716eabd1fbff15c292b995637254485b06e1
- evidence_id: stacking-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#stacked-generalization
  locator: 'User Guide, section #stacked-generalization'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. A final estimator learns
    from predictions of base estimators; held-out predictions can separate its training
    from base-estimator fitting.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
- evidence_id: stochasticgradientdescent-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/sgd.html#id5
  locator: 'User Guide, section #id5'
  accessed_at: '2026-10-11T02:37:27Z'
  support: supports
  summary: 'scikit-learn User Guide: sgd; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Parameters are updated
    using an estimated objective gradient computed from sampled training observations.'
  snapshot_sha256: e487031917c5bfcd2590e116395fb4e8b2fbadaca4152bfa33fe52ec9a6f8829
- evidence_id: votingclassifier-method-source
  kind: authority
  reference: https://scikit-learn.org/1.8/modules/ensemble.html#voting-classifier
  locator: 'User Guide, section #voting-classifier'
  accessed_at: '2026-10-11T02:37:26Z'
  support: supports
  summary: 'scikit-learn User Guide: ensemble; scikit-learn 1.8. Inspected documentation
    supports the narrowly stated definition and mechanism. Hard voting combines predicted
    labels; soft voting combines predicted class probabilities.'
  snapshot_sha256: 8014d31b6fc9f14d11cfde8ff3b7db6b77e511ffcc75840cde22d715b758a4b1
assessments:
- assessment_id: adaboost-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:AdaBoost
  evidence_ids:
  - adaboost-method-source
  - mapping-pin
  - bounded-discovery
  summary: Boosting that reweights training observations according to prior prediction
    errors. EnsembleLearning does not specify sequential sample reweighting by prediction
    error.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not specify sequential sample reweighting by prediction error. Mapping is
    local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - adaboost-method-source
- assessment_id: apriori-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Apriori
  evidence_ids:
  - apriori-method-source
  - mapping-pin
  - bounded-discovery
  summary: Frequent-itemset mining using breadth-first candidate enumeration and support-based
    pruning. AssociationRuleLearning does not identify breadth-first frequent-itemset
    mining. Mining itemsets and generating association rules are distinct tasks; an
    intermediate parent may be needed.
  details: The cited method passage supports the maintained claim scope. AssociationRuleLearning
    does not identify breadth-first frequent-itemset mining. Mining itemsets and generating
    association rules are distinct tasks; an intermediate parent may be needed. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - apriori-method-source
- assessment_id: birch-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:BIRCH
  evidence_ids:
  - birch-method-source
  - mapping-pin
  - bounded-discovery
  summary: Clustering that compresses observations into a clustering-feature tree
    for subsequent grouping. Clustering does not specify the clustering-feature tree
    and incremental compression procedure.
  details: The cited method passage supports the maintained claim scope. Clustering
    does not specify the clustering-feature tree and incremental compression procedure.
    Mapping is local curation, not an upstream subclass assertion. The record remains
    DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - birch-method-source
- assessment_id: bagging-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Bagging
  evidence_ids:
  - bagging-method-source
  - mapping-pin
  - bounded-discovery
  summary: Ensemble learning that aggregates predictors trained on bootstrap samples.
    EnsembleLearning does not require bootstrap samples; bagging is distinct from
    generic ensembles and sampling without replacement.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not require bootstrap samples; bagging is distinct from generic ensembles
    and sampling without replacement. Mapping is local curation, not an upstream subclass
    assertion. The record remains DRAFT; related mappings do not assert equivalence
    or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - bagging-method-source
- assessment_id: boosting-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Boosting
  evidence_ids:
  - boosting-method-source
  - mapping-pin
  - bounded-discovery
  summary: Ensemble learning that sequentially adds learners to improve an existing
    predictor. EnsembleLearning does not require sequential error/loss-directed combination
    of learners.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not require sequential error/loss-directed combination of learners. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - boosting-method-source
- assessment_id: c45-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:C45
  evidence_ids:
  - c45-method-source
  - mapping-pin
  - bounded-discovery
  summary: Decision-tree induction extending ID3 with tests on continuous-valued features.
    DecisionTree does not identify this extension of ID3 handling continuous features.
  details: The cited method passage supports the maintained claim scope. DecisionTree
    does not identify this extension of ID3 handling continuous features. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - c45-method-source
- assessment_id: cart-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:CART
  evidence_ids:
  - cart-method-source
  - mapping-pin
  - bounded-discovery
  summary: Decision-tree induction using binary recursive partitioning for classification
    or regression. DecisionTree denotes a broad tree-based model/category and does
    not identify this binary tree-induction procedure.
  details: The cited method passage supports the maintained claim scope. DecisionTree
    denotes a broad tree-based model/category and does not identify this binary tree-induction
    procedure. Mapping is local curation, not an upstream subclass assertion. The
    record remains DRAFT; related mappings do not assert equivalence or an upstream
    subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - cart-method-source
- assessment_id: dbscan-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:DBSCAN
  evidence_ids:
  - dbscan-method-source
  - mapping-pin
  - bounded-discovery
  summary: Density-based clustering that connects dense neighborhoods and identifies
    unsupported observations as noise. Clustering does not specify core points, density
    connectivity or noise handling.
  details: The cited method passage supports the maintained claim scope. Clustering
    does not specify core points, density connectivity or noise handling. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - dbscan-method-source
- assessment_id: directpreferenceoptimization-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:DirectPreferenceOptimization
  evidence_ids:
  - directpreferenceoptimization-original-paper
  - mapping-pin
  - bounded-discovery
  summary: Preference-based policy fitting using a classification objective on policy-to-reference
    probability ratios for preferred and dispreferred responses. A training algorithm,
    not an instruction-tuned language-model instance or a synonym for all reinforcement
    learning from human feedback.
  details: The cited method passage supports the maintained claim scope. DPO is a
    policy-fitting procedure. The target discusses training strategies but uses a
    preprocessing genus, so a subclass claim is withheld. DPO is motivated by preference-based
    language-model alignment but its derived training objective does not require the
    separate RL optimization loop described for conventional RLHF. The record remains
    DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - directpreferenceoptimization-original-paper
- assessment_id: eclat-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Eclat
  evidence_ids:
  - eclat-method-source
  - mapping-pin
  - bounded-discovery
  summary: Frequent-itemset mining using depth-first enumeration and transaction-set
    intersections. AssociationRuleLearning does not identify depth-first transaction-set
    intersection. Mining itemsets and generating association rules are distinct tasks;
    an intermediate parent may be needed.
  details: The cited method passage supports the maintained claim scope. AssociationRuleLearning
    does not identify depth-first transaction-set intersection. Mining itemsets and
    generating association rules are distinct tasks; an intermediate parent may be
    needed. Mapping is local curation, not an upstream subclass assertion. The record
    remains DRAFT; related mappings do not assert equivalence or an upstream subclass
    axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - eclat-method-source
- assessment_id: elasticnet-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:ElasticNet
  evidence_ids:
  - elasticnet-method-source
  - mapping-pin
  - bounded-discovery
  summary: Linear regression regularized by a combination of L1 and L2 penalties.
    RegressionAnalysis does not require mixed L1/L2 penalties; existing Lasso and
    Ridge concepts cover the separate penalty types.
  details: The cited method passage supports the maintained claim scope. RegressionAnalysis
    does not require mixed L1/L2 penalties; existing Lasso and Ridge concepts cover
    the separate penalty types. Mapping is local curation, not an upstream subclass
    assertion. The record remains DRAFT; related mappings do not assert equivalence
    or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - elasticnet-method-source
- assessment_id: expectationmaximization-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:ExpectationMaximization
  evidence_ids:
  - expectationmaximization-method-source
  - mapping-pin
  - bounded-discovery
  summary: Parameter estimation alternating expected complete-data log-likelihood
    evaluation and its maximization. MachineLearningTask does not identify the alternating
    expected-log-likelihood and maximization estimation procedure.
  details: The cited method passage supports the maintained claim scope. MachineLearningTask
    does not identify the alternating expected-log-likelihood and maximization estimation
    procedure. Mapping is local curation, not an upstream subclass assertion. The
    record remains DRAFT; related mappings do not assert equivalence or an upstream
    subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - expectationmaximization-method-source
- assessment_id: flashattention-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:FlashAttention
  evidence_ids:
  - flashattention-original-paper
  - mapping-pin
  - bounded-discovery
  summary: An exact attention computation algorithm using tiling and recomputation
    to reduce transfers between GPU memory levels. The original dense exact-attention
    algorithm, not a distinct trained model, a generic attention layer, or its separately
    described block-sparse approximation.
  details: The cited method passage supports the maintained claim scope. FlashAttention
    changes how attention is computed and stored, while this AIO target denotes a
    layer implementing attention. The record remains DRAFT; related mappings do not
    assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - flashattention-original-paper
- assessment_id: gaussianprocessregression-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessRegression
  evidence_ids:
  - gaussianprocessregression-method-source
  - mapping-pin
  - bounded-discovery
  summary: Probabilistic regression conditioning a Gaussian-process prior on observed
    training data. RegressionAnalysis does not specify conditioning a Gaussian-process
    prior.
  details: The cited method passage supports the maintained claim scope. RegressionAnalysis
    does not specify conditioning a Gaussian-process prior. Mapping is local curation,
    not an upstream subclass assertion. The record remains DRAFT; related mappings
    do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - gaussianprocessregression-method-source
- assessment_id: geneticalgorithm-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:GeneticAlgorithm
  evidence_ids:
  - geneticalgorithm-method-source
  - mapping-pin
  - bounded-discovery
  summary: Evolutionary optimization using fitness-based selection and genetic variation
    of candidate solutions. MachineLearningTask does not specify evolutionary fitness
    selection, recombination and mutation; genetic optimization is not necessarily
    learning from data.
  details: The cited method passage supports the maintained claim scope. MachineLearningTask
    does not specify evolutionary fitness selection, recombination and mutation; genetic
    optimization is not necessarily learning from data. Mapping is local curation,
    not an upstream subclass assertion. The record remains DRAFT; related mappings
    do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - geneticalgorithm-method-source
- assessment_id: glove-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:GloVe
  evidence_ids:
  - glove-method-source
  - mapping-pin
  - bounded-discovery
  summary: Word-vector learning from global word co-occurrence statistics. The existing
    word2vec concepts use different training objectives. RepresentationLearning is
    defined as a deep neural network in this pin, so using it as a parent would need
    an upstream abstraction correction.
  details: The cited method passage supports the maintained claim scope. The existing
    word2vec concepts use different training objectives. RepresentationLearning is
    defined as a deep neural network in this pin, so using it as a parent would need
    an upstream abstraction correction. Mapping is local curation, not an upstream
    subclass assertion. The existing word2vec concepts use different training objectives.
    RepresentationLearning is defined as a deep neural network in this pin, so using
    it as a parent would need an upstream abstraction correction. Mapping is local
    curation, not an upstream subclass assertion. The existing word2vec concepts use
    different training objectives. RepresentationLearning is defined as a deep neural
    network in this pin, so using it as a parent would need an upstream abstraction
    correction. Mapping is local curation, not an upstream subclass assertion. The
    record remains DRAFT; related mappings do not assert equivalence or an upstream
    subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - glove-method-source
- assessment_id: gradientboosting-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:GradientBoosting
  evidence_ids:
  - gradientboosting-method-source
  - mapping-pin
  - bounded-discovery
  summary: Boosting that adds predictors fitted to negative loss-function gradients.
    EnsembleLearning does not specify stagewise fitting to negative loss gradients.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not specify stagewise fitting to negative loss gradients. Mapping is local
    curation, not an upstream subclass assertion. The record remains DRAFT; related
    mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - gradientboosting-method-source
- assessment_id: hdbscan-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:HDBSCAN
  evidence_ids:
  - hdbscan-method-source
  - mapping-pin
  - bounded-discovery
  summary: Hierarchical density-based clustering that selects clusters across density
    scales. HierarchicalClustering does not specify density scales and cluster-stability
    selection.
  details: The cited method passage supports the maintained claim scope. HierarchicalClustering
    does not specify density scales and cluster-stability selection. Mapping is local
    curation, not an upstream subclass assertion. The record remains DRAFT; related
    mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - hdbscan-method-source
- assessment_id: hiddenmarkovmodel-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovModel
  evidence_ids:
  - hiddenmarkovmodel-method-source
  - mapping-pin
  - bounded-discovery
  summary: A sequence model whose hidden Markov states generate observations through
    state-dependent emission distributions. ProbabilisticGraphicalModel does not specify
    Markov hidden states and observation emissions.
  details: The cited method passage supports the maintained claim scope. ProbabilisticGraphicalModel
    does not specify Markov hidden states and observation emissions. Mapping is local
    curation, not an upstream subclass assertion. The record remains DRAFT; related
    mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - hiddenmarkovmodel-method-source
- assessment_id: id3-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:ID3
  evidence_ids:
  - id3-method-source
  - mapping-pin
  - bounded-discovery
  summary: Decision-tree induction that selects categorical attributes by information
    gain. DecisionTree does not identify information-gain-based categorical tree induction.
  details: The cited method passage supports the maintained claim scope. DecisionTree
    does not identify information-gain-based categorical tree induction. Mapping is
    local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - id3-method-source
- assessment_id: kmeans-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:KMeans
  evidence_ids:
  - kmeans-method-source
  - mapping-pin
  - bounded-discovery
  summary: Clustering that partitions observations around centroids by minimizing
    within-cluster squared distances. The Clustering task does not specify the centroid/squared-distance
    objective of this algorithm.
  details: The cited method passage supports the maintained claim scope. The Clustering
    task does not specify the centroid/squared-distance objective of this algorithm.
    Mapping is local curation, not an upstream subclass assertion. The record remains
    DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - kmeans-method-source
- assessment_id: leastangleregression-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:LeastAngleRegression
  evidence_ids:
  - leastangleregression-method-source
  - mapping-pin
  - bounded-discovery
  summary: Regression that advances along directions equiangular to predictors most
    correlated with the residual. RegressionAnalysis does not specify the equiangular
    active-predictor fitting path; distinguish this algorithm from the resulting regression
    model.
  details: The cited method passage supports the maintained claim scope. RegressionAnalysis
    does not specify the equiangular active-predictor fitting path; distinguish this
    algorithm from the resulting regression model. Mapping is local curation, not
    an upstream subclass assertion. The record remains DRAFT; related mappings do
    not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - leastangleregression-method-source
- assessment_id: lineardiscriminantanalysis-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:LinearDiscriminantAnalysis
  evidence_ids:
  - lineardiscriminantanalysis-method-source
  - mapping-pin
  - bounded-discovery
  summary: Gaussian discriminant classification sharing one covariance matrix across
    classes. Classification does not specify Gaussian class models with shared covariance;
    distinguish the classifier from its dimension-reduction use.
  details: The cited method passage supports the maintained claim scope. Classification
    does not specify Gaussian class models with shared covariance; distinguish the
    classifier from its dimension-reduction use. Mapping is local curation, not an
    upstream subclass assertion. The record remains DRAFT; related mappings do not
    assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - lineardiscriminantanalysis-method-source
- assessment_id: lora-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:LoRA
  evidence_ids:
  - lora-original-paper
  - mapping-pin
  - bounded-discovery
  summary: A parameter-efficient adaptation method that freezes pretrained weights
    and learns additive low-rank matrix updates. A method for adapting model parameters,
    not a pretrained checkpoint or the LoRA software package. AIO:TransferLearning
    is a broader task description and does not specify this weight-update factorization.
  details: The cited method passage supports the maintained claim scope. LoRA implements
    an adaptation procedure; the AIO target denotes the general transfer-learning
    task rather than this factorization algorithm. The record remains DRAFT; related
    mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - lora-original-paper
- assessment_id: mamba-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Mamba
  evidence_ids:
  - mamba-original-paper
  - mapping-pin
  - bounded-discovery
  summary: A neural sequence architecture built from repeated blocks containing input-dependent
    selective state-space transformations. The original Mamba architecture, not its
    trained checkpoints, all state-space models, or Mamba-2. Existing AIO recurrent
    and deep-network categories do not specify selective state-space blocks.
  details: The cited method passage supports the maintained claim scope. Repeated
    learned blocks form a multilayer neural network; the target is broader than this
    specific architecture. Selective state updates use a temporal recurrence, but
    this mapping does not equate all recurrent networks with Mamba. The record remains
    DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - mamba-original-paper
- assessment_id: markovdecisionprocess-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:MarkovDecisionProcess
  evidence_ids:
  - markovdecisionprocess-method-source
  - mapping-pin
  - bounded-discovery
  summary: A sequential decision model with states, actions, Markov transitions, and
    rewards. Model does not require controlled Markov transitions and reward-based
    sequential decisions.
  details: The cited method passage supports the maintained claim scope. Model does
    not require controlled Markov transitions and reward-based sequential decisions.
    Mapping is local curation, not an upstream subclass assertion. The record remains
    DRAFT; related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - markovdecisionprocess-method-source
- assessment_id: markovrandomfield-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:MarkovRandomField
  evidence_ids:
  - markovrandomfield-method-source
  - mapping-pin
  - bounded-discovery
  summary: An undirected graphical probability model associating potential functions
    with variable groups. ProbabilisticGraphicalModel covers broader directed and
    undirected dependencies; this candidate specifically uses an undirected graph.
  details: The cited method passage supports the maintained claim scope. ProbabilisticGraphicalModel
    covers broader directed and undirected dependencies; this candidate specifically
    uses an undirected graph. Mapping is local curation, not an upstream subclass
    assertion. The record remains DRAFT; related mappings do not assert equivalence
    or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - markovrandomfield-method-source
- assessment_id: meanshift-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:MeanShift
  evidence_ids:
  - meanshift-method-source
  - mapping-pin
  - bounded-discovery
  summary: Mode-seeking clustering that moves candidate centers toward local density
    maxima. Clustering does not specify iterative mode seeking in a kernel density
    estimate.
  details: The cited method passage supports the maintained claim scope. Clustering
    does not specify iterative mode seeking in a kernel density estimate. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - meanshift-method-source
- assessment_id: naivebayes-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:NaiveBayes
  evidence_ids:
  - naivebayes-method-source
  - mapping-pin
  - bounded-discovery
  summary: Probabilistic classification assuming feature independence conditional
    on the class. Classification does not specify conditional feature independence
    or a probabilistic generative classifier.
  details: The cited method passage supports the maintained claim scope. Classification
    does not specify conditional feature independence or a probabilistic generative
    classifier. Mapping is local curation, not an upstream subclass assertion. The
    record remains DRAFT; related mappings do not assert equivalence or an upstream
    subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - naivebayes-method-source
- assessment_id: optics-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:OPTICS
  evidence_ids:
  - optics-method-source
  - mapping-pin
  - bounded-discovery
  summary: Density-based clustering analysis that orders observations using reachability
    across neighborhood scales. Clustering does not specify a reachability ordering
    across neighborhood scales; OPTICS is not identical to one flat partition.
  details: The cited method passage supports the maintained claim scope. Clustering
    does not specify a reachability ordering across neighborhood scales; OPTICS is
    not identical to one flat partition. Mapping is local curation, not an upstream
    subclass assertion. The record remains DRAFT; related mappings do not assert equivalence
    or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - optics-method-source
- assessment_id: partialleastsquaresregression-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:PartialLeastSquaresRegression
  evidence_ids:
  - partialleastsquaresregression-method-source
  - mapping-pin
  - bounded-discovery
  summary: Regression using latent components chosen to capture predictor-response
    covariance. RegressionAnalysis does not identify covariance-based latent predictor/response
    components.
  details: The cited method passage supports the maintained claim scope. RegressionAnalysis
    does not identify covariance-based latent predictor/response components. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - partialleastsquaresregression-method-source
- assessment_id: partiallyobservablemarkovdecisionprocess-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:PartiallyObservableMarkovDecisionProcess
  evidence_ids:
  - partiallyobservablemarkovdecisionprocess-method-source
  - mapping-pin
  - bounded-discovery
  summary: A Markov decision model in which observations provide incomplete information
    about the current state. Model does not require state uncertainty, actions, transition
    probabilities, observations and rewards.
  details: The cited method passage supports the maintained claim scope. Model does
    not require state uncertainty, actions, transition probabilities, observations
    and rewards. Mapping is local curation, not an upstream subclass assertion. The
    record remains DRAFT; related mappings do not assert equivalence or an upstream
    subclass axiom.
  dimensions:
  - name: evidence-access
    value: full_text
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - partiallyobservablemarkovdecisionprocess-method-source
- assessment_id: quadraticdiscriminantanalysis-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:QuadraticDiscriminantAnalysis
  evidence_ids:
  - quadraticdiscriminantanalysis-method-source
  - mapping-pin
  - bounded-discovery
  summary: Gaussian discriminant classification with class-specific covariance matrices.
    Classification does not specify Gaussian class models with class-specific covariance.
  details: The cited method passage supports the maintained claim scope. Classification
    does not specify Gaussian class models with class-specific covariance. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - quadraticdiscriminantanalysis-method-source
- assessment_id: stacking-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:Stacking
  evidence_ids:
  - stacking-method-source
  - mapping-pin
  - bounded-discovery
  summary: Ensemble learning that trains a final estimator on base-estimator predictions.
    EnsembleLearning does not require a learned final estimator on base-estimator
    predictions.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not require a learned final estimator on base-estimator predictions. Mapping
    is local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - stacking-method-source
- assessment_id: stochasticgradientdescent-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:StochasticGradientDescent
  evidence_ids:
  - stochasticgradientdescent-method-source
  - mapping-pin
  - bounded-discovery
  summary: Optimization using gradients estimated from sampled training observations.
    TrainingStrategy does not identify a stochastic optimization algorithm, and its
    preprocessing genus requires upstream clarification.
  details: The cited method passage supports the maintained claim scope. TrainingStrategy
    does not identify a stochastic optimization algorithm, and its preprocessing genus
    requires upstream clarification. Mapping is local curation, not an upstream subclass
    assertion. The record remains DRAFT; related mappings do not assert equivalence
    or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - stochasticgradientdescent-method-source
- assessment_id: votingclassifier-support
  area: evidence
  topic: Definition, method identity and inspected mechanism support
  outcome: supported
  target_ids:
  - AIMech:VotingClassifier
  evidence_ids:
  - votingclassifier-method-source
  - mapping-pin
  - bounded-discovery
  summary: A classifier combining base predictions through class votes or aggregated
    class probabilities. EnsembleLearning does not specify class voting or aggregation
    of class probabilities.
  details: The cited method passage supports the maintained claim scope. EnsembleLearning
    does not specify class voting or aggregation of class probabilities. Mapping is
    local curation, not an upstream subclass assertion. The record remains DRAFT;
    related mappings do not assert equivalence or an upstream subclass axiom.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Access level of inspected supporting sources, not a quality score.
    evidence_ids:
    - votingclassifier-method-source
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  evidence_ids:
  - mapping-pin
  - adaboost-method-source
  - apriori-method-source
  - birch-method-source
  - bagging-method-source
  - boosting-method-source
  - c45-method-source
  - cart-method-source
  - dbscan-method-source
  - directpreferenceoptimization-original-paper
  - eclat-method-source
  - elasticnet-method-source
  - expectationmaximization-method-source
  - flashattention-original-paper
  - gaussianprocessregression-method-source
  - geneticalgorithm-method-source
  - glove-method-source
  - gradientboosting-method-source
  - hdbscan-method-source
  - hiddenmarkovmodel-method-source
  - id3-method-source
  - kmeans-method-source
  - leastangleregression-method-source
  - lineardiscriminantanalysis-method-source
  - lora-original-paper
  - mamba-original-paper
  - markovdecisionprocess-method-source
  - markovrandomfield-method-source
  - meanshift-method-source
  - naivebayes-method-source
  - optics-method-source
  - partialleastsquaresregression-method-source
  - partiallyobservablemarkovdecisionprocess-method-source
  - quadraticdiscriminantanalysis-method-source
  - stacking-method-source
  - stochasticgradientdescent-method-source
  - votingclassifier-method-source
  rationale: 'Retain these narrow local identities: density/centroid clustering, alternative
    ensemble constructions, classifier covariance assumptions, tree-induction criteria,
    hidden-state versus controlled-decision models, estimation/optimization procedures
    and the modern adaptation/sequence/attention methods have different defining mechanisms
    or abstraction levels. Boosting and its named algorithms may overlap hierarchically
    without being equivalent. No AIO ID is replaced or merged.'
- action: defer
  target_ids:
  - AIMech:AdaBoost
  - AIMech:Apriori
  - AIMech:BIRCH
  - AIMech:Bagging
  - AIMech:Boosting
  - AIMech:C45
  - AIMech:CART
  - AIMech:DBSCAN
  - AIMech:DirectPreferenceOptimization
  - AIMech:Eclat
  - AIMech:ElasticNet
  - AIMech:ExpectationMaximization
  - AIMech:FlashAttention
  - AIMech:GaussianProcessRegression
  - AIMech:GeneticAlgorithm
  - AIMech:GloVe
  - AIMech:GradientBoosting
  - AIMech:HDBSCAN
  - AIMech:HiddenMarkovModel
  - AIMech:ID3
  - AIMech:KMeans
  - AIMech:LeastAngleRegression
  - AIMech:LinearDiscriminantAnalysis
  - AIMech:LoRA
  - AIMech:Mamba
  - AIMech:MarkovDecisionProcess
  - AIMech:MarkovRandomField
  - AIMech:MeanShift
  - AIMech:NaiveBayes
  - AIMech:OPTICS
  - AIMech:PartialLeastSquaresRegression
  - AIMech:PartiallyObservableMarkovDecisionProcess
  - AIMech:QuadraticDiscriminantAnalysis
  - AIMech:Stacking
  - AIMech:StochasticGradientDescent
  - AIMech:VotingClassifier
  evidence_ids:
  - mapping-pin
  - bounded-discovery
  rationale: A complete local-to-upstream subclass hierarchy and a global lump/split
    audit remain unresolved. Inspect each upstream branch genus and full neighboring
    method definitions before replacing related mappings with stronger relations;
    continue the recorded literature frontier.
limitations:
- This is scientific self-review of stated identity and method support, not independent
  peer review or reproduction of experiments.
- Literature inspection occurred during the documented discovery/curation session;
  the review timestamps record this post-inspection assessment and artifact preparation.
- Official implementation documentation is narrower than a complete historical literature
  review; the MRF example is discrete and LDA covers its classifier use.
- Source URLs that are access-dated documentation may change; named versions and available
  byte hashes are preserved, but not every historical website is immutable.
- No performance, universal convergence, biological efficacy or general safety claim
  is assessed. Native status remains DRAFT.
- 'The full discovery goal is incomplete: this batch adds 36 concepts and retains
  known candidate and source leads.'
tags:
- native-concepts
- mechanism-support
- self-review
- discovery-ongoing
```
