# Scientific self-review of CLARANS, RCA and LMNN

- Review: 20261011T100207Z-medoid-and-linear-metrics
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T09:59:36Z
- Finished UTC: 2026-10-11T10:02:07Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three distinct primary-source-backed DRAFT concepts and their related AIO mappings. Source ambiguities and invalid generalizations are qualified with finite examples. No actionable finding remains within this three-record scope.

## Scope And Provenance

All fields of the three added maintained medoid/linear-metric algorithms.

Selection: Exact three added IDs in the discovery report; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 696ccb475d6023f54ffefd6b66b640baf920fb9c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CLARANSClustering | data/curated/CLARANSClustering.yaml | maintained | CLARANS clustering |
| AIMech:RelevantComponentAnalysis | data/curated/RelevantComponentAnalysis.yaml | maintained | Relevant component analysis |
| AIMech:LargeMarginNearestNeighbor | data/curated/LargeMarginNearestNeighbor.yaml | maintained | Large margin nearest neighbor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CLARANSClustering, AIMech:RelevantComponentAnalysis, AIMech:LargeMarginNearestNeighbor | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 72.46s (0:01:12)<br>Checked 442 record(s); 0 failed.<br>Checked 230 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 50 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 47,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CLARANSClustering, AIMech:RelevantComponentAnalysis, AIMech:LargeMarginNearestNeighbor | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite source-convention calculations | passed | True | AIMech:CLARANSClustering, AIMech:RelevantComponentAnalysis, AIMech:LargeMarginNearestNeighbor | {"clarans": {"observations": [0, 6, 10, 11], "old_medoids": [0, 10], "new_medoids": [6, 10], "old_cost": 5, "new_cost": 7, "per_point_changes": {"0": 6, "6": -4, "10": 0, "11": 0}, "complete_change": 2, "change_over_only_old_nonmedoids": -4, "interpretation": "Omitting the removed medoid reverses the sign of this swap's cost change."}, "rca": {"chunklets": [[[0, 0], [1, 0], [2, 0]], [[10, 0], [11, 0], [12, 0]]], "dimension": 2, "within_chunklet_covariance": [["2/3", "0"], ["0", "0"]], "sum_chunklet_size_minus_one": 4, "actual_rank": 1, "determinant": "0", "interpretation": "The sample-size count can exceed dimension while the covariance is singular."}, "squared_distance": {"points": [0, 1, 2], "squared_direct": 4, "sum_squared_segments": 2, "interpretation": "Squared Euclidean distance need not satisfy the metric triangle inequality."}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, evidence and mapping

evidence: supported. Targets: AIMech:CLARANSClustering.

CLARANS searches the graph of all k-object medoid sets. It samples possible swaps at each state rather than confining all medoids to a fixed subsample as CLARA does, and differs from PAM’s exhaustive best-swap search. Medoids are actual observations, unlike k-means centroids. The record covers the original 1994 clustering method, not its SD/NSD spatial data-mining wrappers or the expanded 2002 polygon-handling methods. No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record and excluded it from additions. Full-checkout word-delimited fixed-string searches included ignored and hidden files, with 79 worktree and 79 main-checkout matching lines; these concern BIRCH identity/proposal/review context and discovery leads. Ten exact AIO CLASS nodes with scoped synonyms and outgoing edges, and nine neighboring native records, were inspected.

For n observations, supplied dissimilarities and 1&lt;=k&lt;n, represent a search state by k selected observations M. Assign each observation to a nearest medoid and define F(M)=sum_(x in X)min_(m in M)d(x,m), over all n observations. A neighboring state replaces one selected medoid with one unselected observation, giving k(n-k) possible neighbors. Begin a run at an arbitrary state. Sample a random neighbor; if its total cost is strictly lower, accept it and reset the unsuccessful-trial counter. Otherwise increment that counter. After maxneighbor unsuccessful trials at the current state, compare its cost with the best completed run and restart until numlocal runs have finished. Return the lowest-cost retained state. Swaps are judged by the full objective difference, including the observation whose medoid role is removed. Curator calculation: with observations {0,6,10,11}, absolute distance and medoids {0,10}, swapping 0 for 6 increases the full cost from 5 to 7. Summing changes only over the old nonmedoids gives -4 and misses the removed medoid’s contribution +6. This demonstrates why the full graph-state objective, not that restricted sum, must govern acceptance. The exact calculation is saved in research/discovery/metric-source-boundaries.py. Limitations: A sampled unsuccessful-trial budget does not certify a local minimum over all possible swaps or a global optimum. The paper’s quoted local-minimum terminology is a stopping heuristic. The original pseudocode specifies a random neighbor but does not state a sampling-without-replacement rule or a particular probability law. This record does not add one, and it does not treat the trial counter as a count of distinct neighbors. Section 2.1 describes cost contributions for currently nonselected objects before Equation (5). Interpreting that literally as excluding every current medoid can omit the removed medoid’s new assignment cost. The full-objective definition in Section 3.1 is retained; an original finite calculation demonstrates the omission, not an author-issued erratum or executed implementation. The requested k, dissimilarity, initialization, trial budget and restart count affect the result. The paper’s experimental numlocal=2 and maxneighbor=max(250, 1.25% of k(n-k)) are experimental choices, not guarantees or identity requirements. No runtime or quality advantage is asserted.

### Identity, definition, mechanism, evidence and mapping

evidence: supported. Targets: AIMech:RelevantComponentAnalysis.

RCA forms chunklets from observations known to share a class without requiring their class names. Different chunklets need not represent different classes. It estimates variation within chunklets, unlike whitening by total covariance, and it does not optimize NCA’s stochastic neighbor reward. The maintained LDA record is a Gaussian classifier, not RCA or the optional constraints-based Fisher projection. This record describes batch RCA; online adaptation and optional dimensionality-reduction procedures are qualified extensions. No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record and excluded it from additions. Full-checkout word-delimited fixed-string searches included ignored and hidden files, with 79 worktree and 79 main-checkout matching lines; these concern BIRCH identity/proposal/review context and discovery leads. Ten exact AIO CLASS nodes with scoped synonyms and outgoing edges, and nine neighboring native records, were inspected.

Take the transitive closure of positive same-class constraints to obtain chunklets C_j with means m_j. Let N be the total number of observations in the chunklets, as clarified in Section 5, and compute Chat=(1/N)sum_j sum_(x in C_j)(x-m_j)(x-m_j)^T. When Chat is positive definite on the represented space, use the symmetric whitening transform W=Chat^(-1/2) on the original feature vectors. Equivalently, compare vectors with squared distance (x-y)^T Chat^(-1)(x-y). Large within-chunklet variance directions receive less weight. The method uses positive constraints without requiring explicit class labels or negative constraints. The paper permits an optional reduction before whitening and describes a constraints-based Fisher discriminant projection; nonsingularity must hold in the retained space. Curator calculation: two chunklets {(0,0),(1,0),(2,0)} and {(10,0),(11,0),(12,0)} have within-chunklet covariance diag(2/3,0), of rank 1. The count sum_j(&#124;C_j&#124;-1)=4 exceeds the ambient dimension 2 while the covariance is singular. This disproves treating the sample-size count as a general exact rank or invertibility certificate. The exact calculation is saved in research/discovery/metric-source-boundaries.py. Limitations: The inverse and inverse square root require a nonsingular covariance on the represented space. Few, singleton or geometrically redundant chunklets may give a singular estimate. This record does not invent a universal pseudoinverse or regularization fallback. Algorithm 2 calls sum_j(&#124;C_j&#124;-1) the covariance rank. In general it is a sample-size upper bound, not the actual rank; collinearity can leave the covariance singular even when that count exceeds the feature dimension. The preceding prose’s rank-greater-than-dimension condition is not a feasible matrix-rank requirement. The source heuristic is not copied as an invertibility guarantee. Whitening can amplify low-variance noise, and erroneous equivalence constraints can contaminate entire chunklets through transitive closure. Small within-group variance is not itself evidence of relevance to a downstream task. The paper’s likelihood and information-optimality results have stated modeling assumptions; this record claims neither universal classification improvement nor unconditional statistical optimality. Optional cFLD, online RCA and their implementation details require separate scope assessments. No model was trained.

### Identity, definition, mechanism, evidence and mapping

evidence: supported. Targets: AIMech:LargeMarginNearestNeighbor.

The core single-metric LMNN formulation fixes directed target-neighbor assignments before fitting and uses a convex objective in a positive-semidefinite matrix. It is not NCA’s stochastic classification objective, a generic triplet loss, or a deep embedding network. Iteratively reassigning targets, learning local metrics, kernelization and rank constraints are distinct extensions; their behavior is not inferred from the core convex program. The energy-based prediction rule in Section 3.5 is separate from ordinary k-nearest-neighbor voting. No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record and excluded it from additions. Full-checkout word-delimited fixed-string searches included ignored and hidden files, with 79 worktree and 79 main-checkout matching lines; these concern BIRCH identity/proposal/review context and discovery leads. Ten exact AIO CLASS nodes with scoped synonyms and outgoing edges, and nine neighboring native records, were inspected.

For labeled vectors choose k other same-class target neighbors T_i for each training point, usually using Euclidean distance before fitting; these directed sets remain fixed in the core method. Let d_M(i,j)=(x_i-x_j)^T M(x_i-x_j), with M positive semidefinite. Minimize (1-mu)sum_i sum_(j in T_i)d_M(i,j)+mu sum_i sum_(j in T_i)sum_(l:y_l!=y_i)max(0,1+d_M(i,j)-d_M(i,l)), with mu in [0,1]. The pull term concerns target neighbors, not all same-class pairs, and the hinge is not squared. Introducing nonnegative slack variables for the margin violations yields a semidefinite program. After learning, factor M=L^T L and use the learned distances for k-nearest-neighbor classification. The matrix-variable objective is convex for fixed target sets; optimizing directly in L is not generally convex. Curator calculation: for one-dimensional points 0,1,2 and M=1, d_M(0,2)=4 exceeds d_M(0,1)+d_M(1,2)=2. The squared expression used for training therefore need not satisfy a metric triangle inequality. The exact calculation is saved in research/discovery/metric-source-boundaries.py. Limitations: Each point needs enough other same-class observations for its chosen target count. Target selection, labels, weighting, feature scale and the solver affect the learned representation; training margins do not certify held-out accuracy. The source uses metric terminology for quadratic distances. The displayed d_M is a squared distance and does not itself generally satisfy the triangle inequality; its square root is a pseudometric when M is positive semidefinite and may collapse distinct points if M is rank deficient. Convexity applies to the fixed-target optimization over M, not to arbitrary factorized, rank-constrained or target-reassignment extensions. Convexity also does not imply a unique optimum, perfect training separation or a certified result from every numerical solver. The endpoints of the stated weight interval can remove one training term; mu=0 permits the collapsed M=0 solution. The paper’s unit margin is a scale convention. No benchmark, special-purpose solver implementation or extension was reproduced.

### State graph, first-improvement swaps and source accounting ambiguity

consistency: supported. Targets: AIMech:CLARANSClustering.

Retain the full graph-state cost and sampled-search stopping convention.

The graph consists of k-subsets of actual observations, connected by a single medoid/nonmedoid swap. The algorithm accepts the first sampled strict improvement and resets its failure counter; it is not PAM best-swap selection or CLARA restriction to a fixed sample. The declared stopping budget does not certify a true neighborhood minimum. Source wording before Equation5 concerns nonselected observations; a literal restriction to those points can miss the removed medoid cost. The record uses Section3.1’s all-object objective and clearly labels the counterexample as curator analysis. Sampling without replacement, exact probability law, tie handling and global-optimum guarantees are not invented.

### Chunklet covariance, normalization and singularity

consistency: supported. Targets: AIMech:RelevantComponentAnalysis.

Retain batch whitening from positive equivalence constraints with actual matrix-domain limits.

Chunklets are positive-constraint connected components and need not identify mutually distinct classes. Within-chunklet centering differs from total covariance; the normalization N is the number of points in chunklets, clarified in Section5. The symmetric inverse square root requires a positive-definite covariance on the represented space. The sample-size count in Algorithm2 is only an upper bound on rank; the original finite collinear example verifies the limitation. No pseudoinverse fallback or unconditional Gaussian optimality is supplied. Optional cFLD and online RCA are separate scope questions, not equivalences to the existing Gaussian LDA classifier.

### Fixed directed targets, convex matrix program and squared-distance terminology

consistency: supported. Targets: AIMech:LargeMarginNearestNeighbor.

Retain the core single-matrix LMNN procedure with fixed-target convexity only.

The loss sums squared distances to selected same-class targets and unsquared unit-margin hinges over differently labeled observations, with complementary weights1-mu andmu. Directed target sets are fixed; convexity concerns the PSD matrixM, not unrestricted factor optimization or rank constraints. The squared distance itself is not a metric triangle-inequality distance, while its square root is a PSD-induced pseudometric. Slack feasibility is not guaranteed perfect separation, and numerical solvers are not automatically certified. The ordinary kNN application and Section3.5 energy classifier remain distinct.

### Algorithm/task and supervision boundaries

grounding: supported. Targets: AIMech:CLARANSClustering, AIMech:RelevantComponentAnalysis, AIMech:LargeMarginNearestNeighbor.

Related mappings preserve the inspected abstraction and supervision differences.

CLARANS relates to the UnsupervisedClustering task. RCA relates to feature transformation and nearest-neighbor classification while preserving its positive-equivalence side-information and batch-whitening scope. LMNN relates to nearest-neighbor classification and supervised learning tasks. AIO MetricLearning is specifically a deep neural network; neither linear algorithm is asserted as that class. Optional reduction does not make these concepts identical to PCA or unsupervised DimensionalityReduction. All positive mappings are related associations, not AIO equivalence or is-a claims.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:CLARANSClustering, AIMech:RelevantComponentAnalysis, AIMech:LargeMarginNearestNeighbor. CLARANS searches medoid sets, RCA whitens within positive-equivalence groups and LMNN learns a fixed-target margin matrix. They have distinct inputs, objectives and update procedures. They do not duplicate BIRCH, Gaussian LDA/QDA, NCA, lifted loss or the inspected clustering methods. No AIO class rewrite, identity merge or DRAFT promotion follows.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T095905Z-medoid-and-linear-metrics.json | supports | All 442 AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases were normalized and compared. BIRCH matched AIMech:BIRCH and was excluded; the other three identities did not match. Complete ignored/hidden-inclusive searches of both checkouts returned 79 lines each, covering the existing BIRCH identity, proposals/reviews and discovery context. Ten exact AIO nodes and nine neighboring native records were inspected. A broader pinned-node name/synonym search for medoid, discriminant, relevant component, large margin, CLARANS and BIRCH yielded no class identity; native LDA/QDA were inspected as Gaussian classifier neighbors. |
| mapping | sources/aio/aio.json; Ten exact CLASS nodes, definitions, all scoped synonyms and outgoing edges; source_analysis.aio_mapping_inspection | supports | CLARANS relates to the UnsupervisedClustering task. RCA relates to feature transformation and nearest-neighbor classification while preserving its positive-equivalence side-information and batch-whitening scope. LMNN relates to nearest-neighbor classification and supervised learning tasks. AIO MetricLearning is specifically a deep neural network; neither linear algorithm is asserted as that class. Optional reduction does not make these concepts identical to PCA or unsupervised DimensionalityReduction. All positive mappings are related associations, not AIO equivalence or is-a claims. |
| neighbors | research/discovery/20261011T095905Z-medoid-and-linear-metrics.json; source_analysis.aio_mapping_inspection.native_neighbors and already_present | supports | Nine maintained neighbors were compared: BIRCH, KMeans, CUREClustering, ROCKClustering, NeighborhoodComponentsAnalysis, LiftedStructuredEmbeddingLoss, LocallyLinearEmbedding, LinearDiscriminantAnalysis and QuadraticDiscriminantAnalysis. BIRCH was reused by identity rather than duplicated. The LDA/QDA records describe Gaussian classifiers, not the metric-learning algorithms or Fisher projection. |
| finite-calculations | research/discovery/metric-source-boundaries.py; calculate(): full versus restricted swap cost, exact covariance, squared distances | supports | Original finite arithmetic executed: the CLARANS example has old cost5, new cost7, full delta+2 versus old-nonmedoid-only delta-4; RCA’s covariance is diag(2/3,0), rank1 despite sample-size count4 and dimension2; squared distance from0 to2 is4 versus two squared segments summing to2. These delimit source interpretations, not implementation accuracy or benchmark performance. |
| claransclustering-source | https://www.vldb.org/conf/1994/P144.PDF; Sections 3.1–3.2, PDF pp. 4–5 (printed 147–148), graph objective and Algorithm CLARANS; Section 2.1, PDF p. 3 (printed 146), cost cases and Equation (5) | supports | Efficient and Effective Clustering Methods for Spatial Data Mining. VLDB 1994, pp. 144–155; 12-page original proceedings PDF. Text pages actually read: []; image pages actually read: [1, 3, 4, 5]. A randomized medoid-clustering algorithm that searches fixed-size sets of representative observations by accepting improving single swaps and restarting after a budget of unsuccessful neighbor trials. |
| relevantcomponentanalysis-source | https://www.jmlr.org/papers/volume6/bar-hillel05a/bar-hillel05a.pdf; Section 2, Algorithm 1 and Equation (1), PDF pp. 4–6 (printed 940–942); Section 5, PDF p. 10, definition of N; Section 6 and Algorithm 2, PDF pp. 10–12 (printed 946–948), dimensionality and rank qualifications | supports | Learning a Mahalanobis Metric from Equivalence Constraints. Journal of Machine Learning Research 6 (2005), pp. 937–965; 29-page expanded primary paper. Text pages actually read: [1, 6]; image pages actually read: [2, 4, 5, 10, 11, 12]. A partially supervised linear metric-learning procedure that estimates within-group covariance from positive equivalence constraints and whitens the representation using that covariance. |
| largemarginnearestneighbor-source | https://www.jmlr.org/papers/volume10/weinberger09a/weinberger09a.pdf; Section 2.1, PDF pp. 3–4 (printed 209–210), squared-distance parameterization; Sections 3.1–3.4, PDF pp. 9–15 (printed 215–221), Equations (10)–(14) and boxed semidefinite program; Section 3.5 for prediction-rule distinction | supports | Distance Metric Learning for Large Margin Nearest Neighbor Classification. Journal of Machine Learning Research 10 (2009), pp. 207–244; 38-page expanded primary paper. Text pages actually read: [1]; image pages actually read: [3, 4, 9, 10, 11, 12, 13, 14, 15]. A supervised metric-learning method that fits a positive-semidefinite distance matrix by pulling fixed same-class target neighbors together while penalizing margin violations by differently labeled observations. |

## Limits And Additional Notes

- Adversarial author self-review only; all three new records remain DRAFT.
- The declared source pages were inspected, not the entire29page RCA or38page LMNN paper. The1994 CLARANS version is not conflated with its expanded2002 article.
- Finite arithmetic qualifies cost accounting, rank and metric terminology. It is not an author erratum, algorithm execution or performance validation.
- The BIRCH identity match caused reuse, not an addition; its original abstract was read without claiming an all-fields review of the older native record.
- No new actionable repository defect was found after these qualifications; no review issue was manufactured. Prior immutable review bundles remain unchanged.
- Three positive additions and an unresolved frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T100207Z-medoid-and-linear-metrics
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of CLARANS, RCA and LMNN
started_at: '2026-10-11T09:59:36Z'
finished_at: '2026-10-11T10:02:07Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent compared all three current YAML records
    against original method pages, exact AIO nodes and nine native neighbors, and
    checked source conventions with finite arithmetic. This adversarial author review
    is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three distinct primary-source-backed DRAFT concepts and their related
  AIO mappings. Source ambiguities and invalid generalizations are qualified with
  finite examples. No actionable finding remains within this three-record scope.
source:
  git_revision: 696ccb475d6023f54ffefd6b66b640baf920fb9c
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/FeatureExtraction.yaml
    sha256: d153b8bbe04e9abb7f1ec13e6219dbcd329235ac58bb9229d4a1f416216c07ef
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/KnearestNeighborAlgorithm.yaml
    sha256: cdb4ab16dea60d54981c94dd2474ac427ffd0e35b728b6356e12cecf87b7a5c0
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/BIRCH.yaml
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    role: context
  - path: data/curated/CLARANSClustering.yaml
    sha256: 79f58a8839bf69a36304f21e1eb5ec94fb0ae829a08839a0f4e3d7de74428e16
    role: target
  - path: data/curated/CUREClustering.yaml
    sha256: ab437b2bd33b77ed821e8695bc15ba90de4fc216d4cafff09da7e48060d42cba
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: target
  - path: data/curated/LiftedStructuredEmbeddingLoss.yaml
    sha256: fbfa4bf9e8910269a90d0f4e866c2f9b8cf7be7512302e1a0debb21154838764
    role: context
  - path: data/curated/LinearDiscriminantAnalysis.yaml
    sha256: cb194468de3c200a57f1d6338e13b604775ce8a10b5517966459242410752b6a
    role: context
  - path: data/curated/LocallyLinearEmbedding.yaml
    sha256: 621f5e3eb78c5d7ae59dbdc639ed778e52e1845e63e9dbff1922d02220e8e55d
    role: context
  - path: data/curated/NeighborhoodComponentsAnalysis.yaml
    sha256: 9aa5fa5229196181f23e7ba5910dba00623a60e558b97233e6cefc1f0fbbd577
    role: context
  - path: data/curated/QuadraticDiscriminantAnalysis.yaml
    sha256: 31a1b7c08a1bae221d571e26441b4690456524b409a33df84427ff929cb4dd3e
    role: context
  - path: data/curated/ROCKClustering.yaml
    sha256: 5be4a00f39b229a245cd86e01d80e2b39cf2f09bb26487d7b911ca9d95625bec
    role: context
  - path: data/curated/RelevantComponentAnalysis.yaml
    sha256: b90fe3dd50da413f6f66c6ea26ecd2eb937b2aec43b4c1eb1f4635dc4609094f
    role: target
  - path: research/discovery/20261011T095905Z-medoid-and-linear-metrics.json
    sha256: 26ad28405fae0a06061c39641271b8fe9c16070a9ab8999577ffae08ed12a2d4
    role: context
  - path: research/discovery/metric-source-boundaries.py
    sha256: 36961d983c5c08464bb4b6cec7e48ba29a169a57416a34ac27a1dfcbb35893a5
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:CLARANSClustering
  path: data/curated/CLARANSClustering.yaml
  label: CLARANS clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CLARANSClustering.yaml
    role: maintained
- target_id: AIMech:RelevantComponentAnalysis
  path: data/curated/RelevantComponentAnalysis.yaml
  label: Relevant component analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RelevantComponentAnalysis.yaml
    role: maintained
- target_id: AIMech:LargeMarginNearestNeighbor
  path: data/curated/LargeMarginNearestNeighbor.yaml
  label: Large margin nearest neighbor
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LargeMarginNearestNeighbor.yaml
    role: maintained
scope:
  description: All fields of the three added maintained medoid/linear-metric algorithms.
  selection: Exact three added IDs in the discovery report; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  exclusions:
  - target: Existing BIRCH and other maintained neighbors
    reason: Inspected for identity and scope comparison only; this verdict does not
      claim a full current scientific review of these older records.
  - target: Optional algorithm extensions, unread pages and implementations
    reason: Only declared primary-source pages were read. Online RCA, cFLD details,
      LMNN extensions and spatial-mining wrappers remain separate frontier items.
      No training or clustering benchmark was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 72.46s (0:01:12)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 230 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 50 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 47,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite source-convention calculations
  command: python3 research/discovery/metric-source-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  exit_code: 0
  expected_exit_code: 0
  summary: '{"clarans": {"observations": [0, 6, 10, 11], "old_medoids": [0, 10], "new_medoids":
    [6, 10], "old_cost": 5, "new_cost": 7, "per_point_changes": {"0": 6, "6": -4,
    "10": 0, "11": 0}, "complete_change": 2, "change_over_only_old_nonmedoids": -4,
    "interpretation": "Omitting the removed medoid reverses the sign of this swap''s
    cost change."}, "rca": {"chunklets": [[[0, 0], [1, 0], [2, 0]], [[10, 0], [11,
    0], [12, 0]]], "dimension": 2, "within_chunklet_covariance": [["2/3", "0"], ["0",
    "0"]], "sum_chunklet_size_minus_one": 4, "actual_rank": 1, "determinant": "0",
    "interpretation": "The sample-size count can exceed dimension while the covariance
    is singular."}, "squared_distance": {"points": [0, 1, 2], "squared_direct": 4,
    "sum_squared_segments": 2, "interpretation": "Squared Euclidean distance need
    not satisfy the metric triangle inequality."}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T095905Z-medoid-and-linear-metrics.json
  accessed_at: '2026-10-11T09:59:36Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases
    were normalized and compared. BIRCH matched AIMech:BIRCH and was excluded; the
    other three identities did not match. Complete ignored/hidden-inclusive searches
    of both checkouts returned 79 lines each, covering the existing BIRCH identity,
    proposals/reviews and discovery context. Ten exact AIO nodes and nine neighboring
    native records were inspected. A broader pinned-node name/synonym search for medoid,
    discriminant, relevant component, large margin, CLARANS and BIRCH yielded no class
    identity; native LDA/QDA were inspected as Gaussian classifier neighbors.
  search_scope: All 442 AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases,
    plus both whole checkouts with ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T09:59:36Z'
  support: supports
  locator: Ten exact CLASS nodes, definitions, all scoped synonyms and outgoing edges;
    source_analysis.aio_mapping_inspection
  summary: CLARANS relates to the UnsupervisedClustering task. RCA relates to feature
    transformation and nearest-neighbor classification while preserving its positive-equivalence
    side-information and batch-whitening scope. LMNN relates to nearest-neighbor classification
    and supervised learning tasks. AIO MetricLearning is specifically a deep neural
    network; neither linear algorithm is asserted as that class. Optional reduction
    does not make these concepts identical to PCA or unsupervised DimensionalityReduction.
    All positive mappings are related associations, not AIO equivalence or is-a claims.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T095905Z-medoid-and-linear-metrics.json
  accessed_at: '2026-10-11T09:59:36Z'
  support: supports
  locator: source_analysis.aio_mapping_inspection.native_neighbors and already_present
  summary: 'Nine maintained neighbors were compared: BIRCH, KMeans, CUREClustering,
    ROCKClustering, NeighborhoodComponentsAnalysis, LiftedStructuredEmbeddingLoss,
    LocallyLinearEmbedding, LinearDiscriminantAnalysis and QuadraticDiscriminantAnalysis.
    BIRCH was reused by identity rather than duplicated. The LDA/QDA records describe
    Gaussian classifiers, not the metric-learning algorithms or Fisher projection.'
- evidence_id: finite-calculations
  kind: record_content
  reference: research/discovery/metric-source-boundaries.py
  locator: 'calculate(): full versus restricted swap cost, exact covariance, squared
    distances'
  accessed_at: '2026-10-11T09:59:36Z'
  snapshot_sha256: 36961d983c5c08464bb4b6cec7e48ba29a169a57416a34ac27a1dfcbb35893a5
  support: supports
  summary: 'Original finite arithmetic executed: the CLARANS example has old cost5,
    new cost7, full delta+2 versus old-nonmedoid-only delta-4; RCA’s covariance is
    diag(2/3,0), rank1 despite sample-size count4 and dimension2; squared distance
    from0 to2 is4 versus two squared segments summing to2. These delimit source interpretations,
    not implementation accuracy or benchmark performance.'
- evidence_id: claransclustering-source
  kind: primary_source
  reference: https://www.vldb.org/conf/1994/P144.PDF
  locator: Sections 3.1–3.2, PDF pp. 4–5 (printed 147–148), graph objective and Algorithm
    CLARANS; Section 2.1, PDF p. 3 (printed 146), cost cases and Equation (5)
  accessed_at: '2026-10-11T09:51:25Z'
  snapshot_sha256: de9f91b1e1ee13e968eade273e116d2ec14ff3ebea0471c7608c5e796587a48d
  support: supports
  summary: 'Efficient and Effective Clustering Methods for Spatial Data Mining. VLDB
    1994, pp. 144–155; 12-page original proceedings PDF. Text pages actually read:
    []; image pages actually read: [1, 3, 4, 5]. A randomized medoid-clustering algorithm
    that searches fixed-size sets of representative observations by accepting improving
    single swaps and restarting after a budget of unsuccessful neighbor trials.'
- evidence_id: relevantcomponentanalysis-source
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume6/bar-hillel05a/bar-hillel05a.pdf
  locator: Section 2, Algorithm 1 and Equation (1), PDF pp. 4–6 (printed 940–942);
    Section 5, PDF p. 10, definition of N; Section 6 and Algorithm 2, PDF pp. 10–12
    (printed 946–948), dimensionality and rank qualifications
  accessed_at: '2026-10-11T09:51:25Z'
  snapshot_sha256: e6a710416aa0b13afa48a54614f4f781dc61e5fd0c5b47205fa4709cbd471f02
  support: supports
  summary: 'Learning a Mahalanobis Metric from Equivalence Constraints. Journal of
    Machine Learning Research 6 (2005), pp. 937–965; 29-page expanded primary paper.
    Text pages actually read: [1, 6]; image pages actually read: [2, 4, 5, 10, 11,
    12]. A partially supervised linear metric-learning procedure that estimates within-group
    covariance from positive equivalence constraints and whitens the representation
    using that covariance.'
- evidence_id: largemarginnearestneighbor-source
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume10/weinberger09a/weinberger09a.pdf
  locator: Section 2.1, PDF pp. 3–4 (printed 209–210), squared-distance parameterization;
    Sections 3.1–3.4, PDF pp. 9–15 (printed 215–221), Equations (10)–(14) and boxed
    semidefinite program; Section 3.5 for prediction-rule distinction
  accessed_at: '2026-10-11T09:51:25Z'
  snapshot_sha256: 514d0b11319e0f37c900bc51e18a8130867d5b739a0d6438097142f5d8d630d1
  support: supports
  summary: 'Distance Metric Learning for Large Margin Nearest Neighbor Classification.
    Journal of Machine Learning Research 10 (2009), pp. 207–244; 38-page expanded
    primary paper. Text pages actually read: [1]; image pages actually read: [3, 4,
    9, 10, 11, 12, 13, 14, 15]. A supervised metric-learning method that fits a positive-semidefinite
    distance matrix by pulling fixed same-class target neighbors together while penalizing
    margin violations by differently labeled observations.'
assessments:
- assessment_id: claransclustering
  area: evidence
  topic: Identity, definition, mechanism, evidence and mapping
  outcome: supported
  target_ids:
  - AIMech:CLARANSClustering
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - claransclustering-source
  - finite-calculations
  summary: CLARANS searches the graph of all k-object medoid sets. It samples possible
    swaps at each state rather than confining all medoids to a fixed subsample as
    CLARA does, and differs from PAM’s exhaustive best-swap search. Medoids are actual
    observations, unlike k-means centroids. The record covers the original 1994 clustering
    method, not its SD/NSD spatial data-mining wrappers or the expanded 2002 polygon-handling
    methods. No normalized identity match for this candidate was found across all
    442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases.
    The same search identified BIRCH as an existing native record and excluded it
    from additions. Full-checkout word-delimited fixed-string searches included ignored
    and hidden files, with 79 worktree and 79 main-checkout matching lines; these
    concern BIRCH identity/proposal/review context and discovery leads. Ten exact
    AIO CLASS nodes with scoped synonyms and outgoing edges, and nine neighboring
    native records, were inspected.
  details: 'For n observations, supplied dissimilarities and 1<=k<n, represent a search
    state by k selected observations M. Assign each observation to a nearest medoid
    and define F(M)=sum_(x in X)min_(m in M)d(x,m), over all n observations. A neighboring
    state replaces one selected medoid with one unselected observation, giving k(n-k)
    possible neighbors. Begin a run at an arbitrary state. Sample a random neighbor;
    if its total cost is strictly lower, accept it and reset the unsuccessful-trial
    counter. Otherwise increment that counter. After maxneighbor unsuccessful trials
    at the current state, compare its cost with the best completed run and restart
    until numlocal runs have finished. Return the lowest-cost retained state. Swaps
    are judged by the full objective difference, including the observation whose medoid
    role is removed. Curator calculation: with observations {0,6,10,11}, absolute
    distance and medoids {0,10}, swapping 0 for 6 increases the full cost from 5 to
    7. Summing changes only over the old nonmedoids gives -4 and misses the removed
    medoid’s contribution +6. This demonstrates why the full graph-state objective,
    not that restricted sum, must govern acceptance. The exact calculation is saved
    in research/discovery/metric-source-boundaries.py. Limitations: A sampled unsuccessful-trial
    budget does not certify a local minimum over all possible swaps or a global optimum.
    The paper’s quoted local-minimum terminology is a stopping heuristic. The original
    pseudocode specifies a random neighbor but does not state a sampling-without-replacement
    rule or a particular probability law. This record does not add one, and it does
    not treat the trial counter as a count of distinct neighbors. Section 2.1 describes
    cost contributions for currently nonselected objects before Equation (5). Interpreting
    that literally as excluding every current medoid can omit the removed medoid’s
    new assignment cost. The full-objective definition in Section 3.1 is retained;
    an original finite calculation demonstrates the omission, not an author-issued
    erratum or executed implementation. The requested k, dissimilarity, initialization,
    trial budget and restart count affect the result. The paper’s experimental numlocal=2
    and maxneighbor=max(250, 1.25% of k(n-k)) are experimental choices, not guarantees
    or identity requirements. No runtime or quality advantage is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Specific learning or search algorithm, not a model instance, generic
      task or performance assertion.
    evidence_ids:
    - claransclustering-source
  - name: aio-relations
    value: 'related_match: AIO:UnsupervisedClustering'
    definition: CLARANS is a specified medoid-search procedure for grouping unlabeled
      observations. The AIO target is a clustering task; this method-to-task relation
      is not equivalence or subclass membership.
    evidence_ids:
    - mapping
- assessment_id: relevantcomponentanalysis
  area: evidence
  topic: Identity, definition, mechanism, evidence and mapping
  outcome: supported
  target_ids:
  - AIMech:RelevantComponentAnalysis
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - relevantcomponentanalysis-source
  - finite-calculations
  summary: RCA forms chunklets from observations known to share a class without requiring
    their class names. Different chunklets need not represent different classes. It
    estimates variation within chunklets, unlike whitening by total covariance, and
    it does not optimize NCA’s stochastic neighbor reward. The maintained LDA record
    is a Gaussian classifier, not RCA or the optional constraints-based Fisher projection.
    This record describes batch RCA; online adaptation and optional dimensionality-reduction
    procedures are qualified extensions. No normalized identity match for this candidate
    was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native
    IDs/names/aliases. The same search identified BIRCH as an existing native record
    and excluded it from additions. Full-checkout word-delimited fixed-string searches
    included ignored and hidden files, with 79 worktree and 79 main-checkout matching
    lines; these concern BIRCH identity/proposal/review context and discovery leads.
    Ten exact AIO CLASS nodes with scoped synonyms and outgoing edges, and nine neighboring
    native records, were inspected.
  details: 'Take the transitive closure of positive same-class constraints to obtain
    chunklets C_j with means m_j. Let N be the total number of observations in the
    chunklets, as clarified in Section 5, and compute Chat=(1/N)sum_j sum_(x in C_j)(x-m_j)(x-m_j)^T.
    When Chat is positive definite on the represented space, use the symmetric whitening
    transform W=Chat^(-1/2) on the original feature vectors. Equivalently, compare
    vectors with squared distance (x-y)^T Chat^(-1)(x-y). Large within-chunklet variance
    directions receive less weight. The method uses positive constraints without requiring
    explicit class labels or negative constraints. The paper permits an optional reduction
    before whitening and describes a constraints-based Fisher discriminant projection;
    nonsingularity must hold in the retained space. Curator calculation: two chunklets
    {(0,0),(1,0),(2,0)} and {(10,0),(11,0),(12,0)} have within-chunklet covariance
    diag(2/3,0), of rank 1. The count sum_j(|C_j|-1)=4 exceeds the ambient dimension
    2 while the covariance is singular. This disproves treating the sample-size count
    as a general exact rank or invertibility certificate. The exact calculation is
    saved in research/discovery/metric-source-boundaries.py. Limitations: The inverse
    and inverse square root require a nonsingular covariance on the represented space.
    Few, singleton or geometrically redundant chunklets may give a singular estimate.
    This record does not invent a universal pseudoinverse or regularization fallback.
    Algorithm 2 calls sum_j(|C_j|-1) the covariance rank. In general it is a sample-size
    upper bound, not the actual rank; collinearity can leave the covariance singular
    even when that count exceeds the feature dimension. The preceding prose’s rank-greater-than-dimension
    condition is not a feasible matrix-rank requirement. The source heuristic is not
    copied as an invertibility guarantee. Whitening can amplify low-variance noise,
    and erroneous equivalence constraints can contaminate entire chunklets through
    transitive closure. Small within-group variance is not itself evidence of relevance
    to a downstream task. The paper’s likelihood and information-optimality results
    have stated modeling assumptions; this record claims neither universal classification
    improvement nor unconditional statistical optimality. Optional cFLD, online RCA
    and their implementation details require separate scope assessments. No model
    was trained.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Specific learning or search algorithm, not a model instance, generic
      task or performance assertion.
    evidence_ids:
    - relevantcomponentanalysis-source
  - name: aio-relations
    value: 'related_match: AIO:FeatureExtraction; related_match: AIO:KnearestNeighborClassificationAlgorithm'
    definition: RCA transforms feature vectors using learned within-chunklet covariance
      before downstream learning. This relates its representation-transform operation
      to AIO FeatureExtraction without asserting a deep neural-network identity or
      a specific downstream predictor. The learned distance can be used for nearest-neighbor
      classification, one stated application. Learning this representation is distinct
      from the target’s voting rule; the relation is an explicitly related method-to-application
      association.
    evidence_ids:
    - mapping
- assessment_id: largemarginnearestneighbor
  area: evidence
  topic: Identity, definition, mechanism, evidence and mapping
  outcome: supported
  target_ids:
  - AIMech:LargeMarginNearestNeighbor
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - largemarginnearestneighbor-source
  - finite-calculations
  summary: The core single-metric LMNN formulation fixes directed target-neighbor
    assignments before fitting and uses a convex objective in a positive-semidefinite
    matrix. It is not NCA’s stochastic classification objective, a generic triplet
    loss, or a deep embedding network. Iteratively reassigning targets, learning local
    metrics, kernelization and rank constraints are distinct extensions; their behavior
    is not inferred from the core convex program. The energy-based prediction rule
    in Section 3.5 is separate from ordinary k-nearest-neighbor voting. No normalized
    identity match for this candidate was found across all 442 pinned AIO labels/scoped
    synonyms and 227 preceding native IDs/names/aliases. The same search identified
    BIRCH as an existing native record and excluded it from additions. Full-checkout
    word-delimited fixed-string searches included ignored and hidden files, with 79
    worktree and 79 main-checkout matching lines; these concern BIRCH identity/proposal/review
    context and discovery leads. Ten exact AIO CLASS nodes with scoped synonyms and
    outgoing edges, and nine neighboring native records, were inspected.
  details: 'For labeled vectors choose k other same-class target neighbors T_i for
    each training point, usually using Euclidean distance before fitting; these directed
    sets remain fixed in the core method. Let d_M(i,j)=(x_i-x_j)^T M(x_i-x_j), with
    M positive semidefinite. Minimize (1-mu)sum_i sum_(j in T_i)d_M(i,j)+mu sum_i
    sum_(j in T_i)sum_(l:y_l!=y_i)max(0,1+d_M(i,j)-d_M(i,l)), with mu in [0,1]. The
    pull term concerns target neighbors, not all same-class pairs, and the hinge is
    not squared. Introducing nonnegative slack variables for the margin violations
    yields a semidefinite program. After learning, factor M=L^T L and use the learned
    distances for k-nearest-neighbor classification. The matrix-variable objective
    is convex for fixed target sets; optimizing directly in L is not generally convex.
    Curator calculation: for one-dimensional points 0,1,2 and M=1, d_M(0,2)=4 exceeds
    d_M(0,1)+d_M(1,2)=2. The squared expression used for training therefore need not
    satisfy a metric triangle inequality. The exact calculation is saved in research/discovery/metric-source-boundaries.py.
    Limitations: Each point needs enough other same-class observations for its chosen
    target count. Target selection, labels, weighting, feature scale and the solver
    affect the learned representation; training margins do not certify held-out accuracy.
    The source uses metric terminology for quadratic distances. The displayed d_M
    is a squared distance and does not itself generally satisfy the triangle inequality;
    its square root is a pseudometric when M is positive semidefinite and may collapse
    distinct points if M is rank deficient. Convexity applies to the fixed-target
    optimization over M, not to arbitrary factorized, rank-constrained or target-reassignment
    extensions. Convexity also does not imply a unique optimum, perfect training separation
    or a certified result from every numerical solver. The endpoints of the stated
    weight interval can remove one training term; mu=0 permits the collapsed M=0 solution.
    The paper’s unit margin is a scale convention. No benchmark, special-purpose solver
    implementation or extension was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Specific learning or search algorithm, not a model instance, generic
      task or performance assertion.
    evidence_ids:
    - largemarginnearestneighbor-source
  - name: aio-relations
    value: 'related_match: AIO:KnearestNeighborClassificationAlgorithm; related_match:
      AIO:SupervisedLearning'
    definition: LMNN learns the distance used in nearest-neighbor voting. The target
      describes the voting task, so this is a related metric-training-to-classification
      association, not algorithm identity. Class labels determine target eligibility
      and differently labeled margin constraints. The target is a broad learning task,
      while LMNN is a specific metric-learning algorithm; this related mapping preserves
      that abstraction difference.
    evidence_ids:
    - mapping
- assessment_id: clarans-objective
  area: consistency
  topic: State graph, first-improvement swaps and source accounting ambiguity
  outcome: supported
  target_ids:
  - AIMech:CLARANSClustering
  evidence_ids:
  - claransclustering-source
  - finite-calculations
  - neighbors
  summary: Retain the full graph-state cost and sampled-search stopping convention.
  details: The graph consists of k-subsets of actual observations, connected by a
    single medoid/nonmedoid swap. The algorithm accepts the first sampled strict improvement
    and resets its failure counter; it is not PAM best-swap selection or CLARA restriction
    to a fixed sample. The declared stopping budget does not certify a true neighborhood
    minimum. Source wording before Equation5 concerns nonselected observations; a
    literal restriction to those points can miss the removed medoid cost. The record
    uses Section3.1’s all-object objective and clearly labels the counterexample as
    curator analysis. Sampling without replacement, exact probability law, tie handling
    and global-optimum guarantees are not invented.
- assessment_id: rca-covariance
  area: consistency
  topic: Chunklet covariance, normalization and singularity
  outcome: supported
  target_ids:
  - AIMech:RelevantComponentAnalysis
  evidence_ids:
  - relevantcomponentanalysis-source
  - finite-calculations
  - neighbors
  summary: Retain batch whitening from positive equivalence constraints with actual
    matrix-domain limits.
  details: Chunklets are positive-constraint connected components and need not identify
    mutually distinct classes. Within-chunklet centering differs from total covariance;
    the normalization N is the number of points in chunklets, clarified in Section5.
    The symmetric inverse square root requires a positive-definite covariance on the
    represented space. The sample-size count in Algorithm2 is only an upper bound
    on rank; the original finite collinear example verifies the limitation. No pseudoinverse
    fallback or unconditional Gaussian optimality is supplied. Optional cFLD and online
    RCA are separate scope questions, not equivalences to the existing Gaussian LDA
    classifier.
- assessment_id: lmnn-convexity
  area: consistency
  topic: Fixed directed targets, convex matrix program and squared-distance terminology
  outcome: supported
  target_ids:
  - AIMech:LargeMarginNearestNeighbor
  evidence_ids:
  - largemarginnearestneighbor-source
  - finite-calculations
  - neighbors
  summary: Retain the core single-matrix LMNN procedure with fixed-target convexity
    only.
  details: The loss sums squared distances to selected same-class targets and unsquared
    unit-margin hinges over differently labeled observations, with complementary weights1-mu
    andmu. Directed target sets are fixed; convexity concerns the PSD matrixM, not
    unrestricted factor optimization or rank constraints. The squared distance itself
    is not a metric triangle-inequality distance, while its square root is a PSD-induced
    pseudometric. Slack feasibility is not guaranteed perfect separation, and numerical
    solvers are not automatically certified. The ordinary kNN application and Section3.5
    energy classifier remain distinct.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Algorithm/task and supervision boundaries
  outcome: supported
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Related mappings preserve the inspected abstraction and supervision differences.
  details: CLARANS relates to the UnsupervisedClustering task. RCA relates to feature
    transformation and nearest-neighbor classification while preserving its positive-equivalence
    side-information and batch-whitening scope. LMNN relates to nearest-neighbor classification
    and supervised learning tasks. AIO MetricLearning is specifically a deep neural
    network; neither linear algorithm is asserted as that class. Optional reduction
    does not make these concepts identical to PCA or unsupervised DimensionalityReduction.
    All positive mappings are related associations, not AIO equivalence or is-a claims.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:CLARANSClustering
  - AIMech:RelevantComponentAnalysis
  - AIMech:LargeMarginNearestNeighbor
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-calculations
  - claransclustering-source
  - relevantcomponentanalysis-source
  - largemarginnearestneighbor-source
  rationale: CLARANS searches medoid sets, RCA whitens within positive-equivalence
    groups and LMNN learns a fixed-target margin matrix. They have distinct inputs,
    objectives and update procedures. They do not duplicate BIRCH, Gaussian LDA/QDA,
    NCA, lifted loss or the inspected clustering methods. No AIO class rewrite, identity
    merge or DRAFT promotion follows.
limitations:
- Adversarial author self-review only; all three new records remain DRAFT.
- The declared source pages were inspected, not the entire29page RCA or38page LMNN
  paper. The1994 CLARANS version is not conflated with its expanded2002 article.
- Finite arithmetic qualifies cost accounting, rank and metric terminology. It is
  not an author erratum, algorithm execution or performance validation.
- The BIRCH identity match caused reuse, not an addition; its original abstract was
  read without claiming an all-fields review of the older native record.
- No new actionable repository defect was found after these qualifications; no review
  issue was manufactured. Prior immutable review bundles remain unchanged.
- Three positive additions and an unresolved frontier leave discovery active.
tags:
- native-concepts
- metric-learning
- clustering
- self-review
- discovery-ongoing
```
