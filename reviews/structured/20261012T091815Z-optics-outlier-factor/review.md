# Scientific self-review of OPTICS-OF and LOF boundaries

- Review: 20261012T091815Z-optics-outlier-factor
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T09:15:21Z
- Finished UTC: 2026-10-12T09:18:15Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain self-inclusive OPTICS-OF and self-excluded LOF as distinct scoring procedures. Original1999 parsed text is context only, while immutable official implementation supports OPTICS-OF mechanisms. No actionable defect remains in the two final records.

## Scope And Provenance

Every field of the selected local reachability-density scoring cohort.

Selection: Exact maintained IDs AIMech:OPTICSOutlierFactor and AIMech:LocalOutlierFactor, without sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 340d1710beea5d7e57c8b403ba2b6f9516767285.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OPTICSOutlierFactor | data/curated/OPTICSOutlierFactor.yaml | maintained | OPTICS outlier factor |
| AIMech:LocalOutlierFactor | data/curated/LocalOutlierFactor.yaml | maintained | Local outlier factor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 112.32s (0:01:52)<br>Checked 442 record(s); 0 failed.<br>Checked 513 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 158 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 154,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | Exited0 without output. |
| opticsof exact boundary calculations | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | {"data_0_1_3_self_inclusive_m2": ["1", "1", "3/2"], "corresponding_self_excluded_k1": ["1", "1", "2"], "data_0_1_3_self_inclusive_m3": ["1", "1", "1"], "corresponding_self_excluded_k2": ["11/12", "6/5", "11/12"], "identical_core_radii_do_not_make_algorithms_equivalent": true, "self_reachability_is_core_distance_not_zero": true, "all_reference_neighborhoods_give_score_one": true, "boundary_ties_score": "4/3", "truncated_score": "1", "self_only_and_duplicate_zero_means_undefined": true, "uniform_positive_scaling_preserves_defined_core_scores": true, "scope": "Exact arithmetic from inspected self-inclusive scoring formulas and pinned source, compared to self-excluded LOF. No Java execution, index-backend validation or benchmark reproduction."} |
| lof exact boundary calculations | passed | True | AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor | {"self_excluded_and_asymmetric_neighbor_radius": true, "k2_reachability_need_not_equal_raw_distance": true, "scores_at_k1": ["1", "1", "2"], "scores_at_k2": ["11/12", "6/5", "11/12"], "scores_can_be_below_one_and_rankings_change": true, "positive_uniform_scale_and_translation_invariant": true, "isolated_pair_both_score_one": true, "tie_inclusive_score": "3/2", "exact_k_truncation_score": "1", "zero_reachability_without_regularization_is_undefined": true, "fixed_additive_epsilon_breaks_exact_scale_invariance": true, "nonmonotonic_k_example": {"data": [0, 1, 2, 3, 4], "index": 0, "scores_by_k_1_to_4": ["1", "5/4", "44/45", "337/364"]}, "scope": "Exact finite rational calculations from Definitions3-7; no original implementation, learned model or benchmark executed."} |

## Scientific And Domain Assessments

### Identity, definition and concept scope

identity: supported. Targets: AIMech:OPTICSOutlierFactor.

Retain the distinct native DRAFT algorithm.

An unsupervised local outlier-scoring procedure that uses self-inclusive, tie-inclusive nearest neighborhoods to compute inverse mean neighbor-radius reachability and averages neighbor-to-query density ratios. This record denotes OPTICS-OF with the self-inclusive convention corroborated by the inspected ELKI implementation. It is distinct from OPTICS ordering, DBSCAN noise labels, original self-excluded LOF, neighbor-label voting and raw distance ranking. Original 1999 parsed text is context; mechanism claims are grounded in immutable official source and exact neighbor contracts. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 512 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches of both checkouts included ignored and hidden files, all aliases, the original title and DOI: 23 matches in each checkout were read in 19 distinct context windows at 46 locations. These are LOF comparison notes, prior searches and unresolved discovery context, not an existing OPTICS-OF record. All 99 semantic AIO rows, 13 annotated CLASS nodes with outgoing edges, 71 native identity-field matches and 21 contextual YAMLs were inspected or reused after unchanged-content checks. This is a bounded local corpus assessment.

### Related algorithm-to-task AIO association

grounding: supported. Targets: AIMech:OPTICSOutlierFactor.

Related mapping is supported without equivalence or subclassing.

OPTICS-OF computes relative local outlier scores from unlabeled observations, supporting a related algorithm-to-task association with AIO:UnsupervisedLearning. The target is a MachineLearningTask, so the link asserts neither equivalence nor subclassing. BinaryClassification and its supervised ancestry do not describe the unthresholded core. Clustering, DBSCAN and OPTICS produce cluster structure or a reachability ordering; this standalone score needs neither a partition nor an OPTICS traversal. The three AIO KnearestNeighbor classes concern voting or response averaging, unlike these density ratios. RegressionAnalysis, DimensionalityReduction, DataPreparation and SelectionAndSamplingBias do not identify the procedure. Native LOF differs by explicit self exclusion; domain-description and metric-learning methods have different rules or outputs.

### self inclusive locality

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

For a finite reference dataset D of n observations, a finite metric and 2&lt;=m&lt;=n, core_m(p) is the mth ordered distance to observations in D, including p itself. N_m(p) retains every observation at distance at most that boundary, including all ties. The inspected exact linear scans and heap include the indexed query and boundary ties; a fixed-count truncation is not the same convention. The m range describes the well-defined distinct-point metric case, not a claim that every constructor enforces it. Locators: OPTICSOF.run, passes 1-3; getKNN: retrieve query object without removing its database ID; getKNN: scan every relation ID; getKNN: scan every relation ID; insert, addToTies, toKNNList and toKNNListSqrt: retain boundary ties; Interface size and getKNNDistance contracts

### reachability and density ratios

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

For o in N_m(p), reach_m(p,o)=max(core_m(o),d(p,o)), using the neighbor radius. Set lrd_m(p)=&#124;N_m(p)&#124; divided by the sum of these reaches, and OF_m(p) to the mean of lrd_m(o)/lrd_m(p) over N_m(p). Thus self reachability is core_m(p), not zero, and the self term contributes a ratio of one when defined. The formulas require positive finite mean reaches for all densities used. These inverse-distance quantities are not normalized probability densities, and the resulting relative score is not an outlier probability or an automatic binary decision. Locators: OPTICSOF.run, passes 1-3

### standalone three pass computation

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

The inspected implementation first stores neighborhoods and core radii, then computes all local reachability densities, then averages their neighbor-to-query ratios. It does not run an OPTICS ordering or extract a clustering. Pairwise reachability in the score must not be replaced with a minimum reachability accumulated during an OPTICS traversal. Locators: OPTICSOF.run, passes 1-3; Parsed Definitions 4-7 and computational discussion, PDF pp5-6 and8; not visually verified

### distinct from self excluded lof

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

OPTICS-OF and original LOF are retained separately because including the query changes both density and score averaging. Under absolute distance, D={0,1,3} gives OPTICS-OF scores {1,1,3/2} at m=2, whereas self-excluded LOF gives {1,1,2} at k=1, despite identical core radii. At m=3, OPTICS-OF gives {1,1,1}, while LOF at k=2 gives {11/12,6/5,11/12}. These exact curator calculations rule out identifying the two procedures merely by shifting the neighbor-count parameter. Locators: OPTICSOF.run, passes 1-3; Definitions 3-7, printed/PDF pp3-4; exact comparisons in research/discovery/optics-outlier-factor-boundaries.py

### ties and scale boundaries

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

Boundary ties can change scores: for D={0,2,4,5} and m=2, point 2 has three retained neighbors and score 4/3; selecting only itself and neighbor 0 instead gives score 1. Positive uniform scaling of every distance cancels from defined density ratios, but feature-specific scaling can change neighborhoods. When m=n, every neighborhood is D and reach_m(p,o)=core_m(o), so all densities are equal and all defined scores are one. A score of one therefore does not by itself establish domain normality. Locators: OPTICSOF.run, passes 1-3; Boundary-tie retention; exact curator calculations in research/discovery/optics-outlier-factor-boundaries.py

### zero distance and parameter limits

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

With m=1 and a unique query location, the self-only neighborhood has zero mean reachability; duplicates can also produce zero means at larger m. The mathematical ratios are then undefined. The inspected parameterizer requires m&gt;1 and defaults to Euclidean distance, but its constructor does not enforce m&lt;=n. KNNList may report an infinite boundary when fewer than m neighbors exist. The scoring loop adds no epsilon; its lrd&gt;0 guard does not resolve infinity/infinity from coincident neighborhoods. A fallback zero or nonfinite output outside the stated finite domain is not evidence of normality. Locators: OPTICSOF.run, passes 1-3; Constructor and Par.configure; getKNNDistance: infinite distance if fewer than k neighbors

### implementation and computation scope

evidence: supported. Targets: AIMech:OPTICSOutlierFactor.

Supported within the stated source, parameter and implementation limits.

The evidence establishes the inspected release source and exact linear-query/tie contracts, not every index backend, historical implementation or runtime result. Stored all-ties neighborhoods can contain every observation even for small m, requiring quadratic neighbor incidences. All-pairs neighbor search can require quadratic distance evaluations, and selection/index costs need separate analysis; no universal near-linear or n-log-n complexity follows. The historical paper text and versioned test fixture provide context, but no figure-derived claim, numerical performance advantage, library benchmark or probability calibration is curated. Locators: OPTICSOF.run, passes 1-3; Boundary-tie storage; Full relation scan per query; Parsed computational and experimental prose, PDF pp7-8; figures not visually verified

### Identity, definition and concept scope

identity: supported. Targets: AIMech:LocalOutlierFactor.

Retain the distinct native DRAFT algorithm.

An unsupervised local outlier-scoring procedure that compares each observation's inverse mean reachability distance with those of its tie-inclusive nearest neighbors and returns their mean density ratio. This record denotes the original fixed-neighborhood LOF procedure, with optional scale aggregation and versioned implementation conventions explicitly separated. It is distinct from neighbor-label voting, raw kth-distance ranking, thresholded NNDD or PDD, DBSCAN noise labels and OPTICS reachability ordering. The initial LOF review left OPTICS-OF as an unresolved related identity comparison. The subsequent AIMech:OPTICSOutlierFactor record documents its distinct self-inclusive convention; the two are not treated as aliases. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 511 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches of both checkouts included ignored and hidden files, LOF, expanded names and both publication DOIs: 16 worktree and 17 main matches, comprising 13 distinct context windows at 33 locations, were read. They are pending discovery context and an unrelated BASIC-language LOF token in an ignored Pygments lexer. Semantic searches inspected 99 AIO name/synonym/definition rows and 70 native name/definition matches, reusing 85 and 67 unchanged previously read rows respectively. Thirteen annotated AIO CLASS nodes with outgoing edges and twenty contextual YAMLs were inspected or reused after unchanged-byte checks. This is a bounded corpus assessment, not absence from all ontologies.

### Related algorithm-to-task AIO association

grounding: supported. Targets: AIMech:LocalOutlierFactor.

Related mapping is supported without equivalence or subclassing.

LOF infers neighborhood-relative outlier scores from unlabeled observations, giving a related algorithm-to-task association with AIO:UnsupervisedLearning. The target is a MachineLearningTask; this link is neither exact equivalence nor a subclass assertion. The core score does not itself assign two classes, so BinaryClassification and its supervised ancestry are not selected. Clustering and OPTICS/DBSCAN organize clusters or reachability orderings, whereas LOF does not require a partition. All three AIO KnearestNeighbor classes specify label voting or response averaging, not local reachability ratios; RegressionAnalysis requires dependent/independent-variable relationships. DimensionalityReduction, DataPreparation and SelectionAndSamplingBias do not identify this scoring procedure. Native neighbor-ratio and distance-norm domain descriptions, PDD, supervised metric learning and density clustering have different outputs or neighborhood rules.

### tie inclusive locality

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

For n reference observations and 1&lt;=k&lt;=n-1, k-distance(p) is the kth ordered distance to other observations, excluding p itself. N_k(p) contains every other observation whose distance is at most that boundary, including all ties, so its size can exceed k. The reference dataset and dissimilarity define locality; the procedure does not require labeled normal/outlier examples or an explicit clustering. Locators: Section 4, Definitions 3-4, printed/PDF p3; Section 1, p1

### reachability density ratio

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

Define reach_k(p,o)=max(k-distance(o),d(p,o)), using the neighbor o's radius, not p's. Reachability is generally asymmetric. Local reachability density lrd_k(p) is the reciprocal of the mean reachability over o in N_k(p), and LOF_k(p) is the mean of lrd_k(o)/lrd_k(p) over that same neighborhood. These formulas require nonempty neighborhoods and positive finite mean reaches for the densities used. Reachability density has inverse-distance units; it is not a normalized probability density. LOF is a dimensionless relative score. Locators: Definitions 5-7, printed/PDF pp3-4

### relative score not probability

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

A large score indicates lower reachability density relative to neighbors; it is neither an outlier probability nor a universal decision threshold. The paper's near-one bound assumes a closed two-hop neighborhood and bounded positive reachability variation. Scores can be below one: for D={0,1,3} under absolute distance and k=2, the scores are {11/12,6/5,11/12}. At k=1 they are {1,1,2}, reversing the center-versus-endpoint ordering. Two arbitrarily separated observations both score one at k=1; absolute isolation alone is not enough. These examples are exact curator calculations. Locators: Definition 7 and Lemma 1, printed/PDF p4; Sections 5-6, pp4-8; research/discovery/local-outlier-factor-boundaries.py

### ties zeros and scale

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

Boundary ties are part of the original definition: D={0,2,4,5}, k=1 gives point 2 score 3/2 when both equidistant neighbors are retained, but score 1 if an exact-k implementation chooses only neighbor 0. Coincident observations can give zero mean reachability and undefined density ratios; the paper assumes no duplicates and mentions a distinct-coordinate alternative without making an additive regularizer part of core LOF. Multiplying every distance by a positive constant leaves the unregularized core score unchanged when defined; feature-specific rescaling can change neighborhoods and scores. For D={0,1,3}, k=2, reach(0,1)=2 exceeds d(0,1)=1, so the paper's informal k=2 raw-distance reduction is not generally implied by its self-excluded definitions. Locators: Definitions 3-7 and duplicate discussion, printed/PDF pp3-4; Section 6, p7; exact curator calculations in research/discovery/local-outlier-factor-boundaries.py

### neighborhood scale selection

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

Scores can vary nonmonotonically with k. The paper suggests choosing a lower and upper neighborhood size and ranking each point by its maximum LOF over that range; this is an optional multiscale ranking heuristic, distinct from a fixed-k score. Suggested lower bounds near 10 and common choices around 10-20 are empirical guidance, not mathematical validity constraints or universally optimal defaults. Small groups can appear ordinary relative to one another at some scales, so the chosen range affects which deviations are exposed. Locators: Section 6 and Figures 7-8, printed/PDF pp7-9

### versioned implementation conventions

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

The inspected scikit-learn 1.7.2-linked implementation uses a fixed neighbor count, excludes the indexed query for fitted training scores, and adds 1e-10 to mean reachability before inversion. It exposes negative LOF as negative_outlier_factor_; auto contamination chooses offset -1.5, while supplied contamination chooses a training-score percentile and labels scores strictly below it. These are implementation choices, not the paper's all-ties and unregularized definition or a universally validated 1.5 cutoff. Ties can prevent an exact requested outlier fraction. A fixed additive epsilon also prevents automatically transferring exact uniform-scale invariance. Locators: Definitions 3-7, printed/PDF pp3-4; soccer illustration and Table 3, p10; exact fixed-epsilon curator calculation; LocalOutlierFactor.fit, _predict and _local_reachability_density; KNeighborsMixin._kneighbors_reduce_func and kneighbors, including query_is_train and final fixed-shape self-removal

### novelty query distinction

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

With novelty=True, the inspected implementation scores new queries against stored training-neighbor radii and training densities; it does not insert the new query batch into reference neighborhoods. Supplying training points through score_samples can include each query itself as a neighbor, unlike the fitted training-score calculation. Novelty-query scores therefore need not equal negative_outlier_factor_ on the training set. This source-scoped extension does not redefine the original dataset-level score, and no library runtime or historical-code equivalence was tested. Locators: Definitions 3-7, printed/PDF pp3-4; LocalOutlierFactor.score_samples, decision_function and their novelty docstrings; KNeighborsMixin.kneighbors: X is None training branch versus explicit-query branch

### computation and evaluation scope

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the stated source, parameter and implementation limits.

After neighborhoods are available, computing densities and scores visits the retained neighbor incidences for each chosen k. Original all-boundary-ties neighborhoods can contain n-1 observations even for small k, so O(n*k) storage or linear score work requires a bounded-neighborhood assumption. All-pairs search can require quadratic distance evaluations; index performance depends on data and dimension. The paper's synthetic, sports and color-histogram examples and historical wall-clock timings are conditional demonstrations, not universal accuracy or speed guarantees. The sports results use selected features and neighborhood ranges with domain interpretation, not held-out probability calibration. No numerical performance advantage is curated. Locators: Sections 7.1-7.3, Figures 9-11 and Table 3, printed/PDF pp9-11; Definition 4, p3

### Distinct procedures despite common density-ratio form

consistency: supported. Targets: AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor.

Retain OPTICS-OF and LOF separately.

The exact queries include the indexed observation, heap serialization retains boundary ties and the main OPTICSOF loop does not remove self. Self reach is the own core radius, and its density-ratio contribution is one. LOF Definitions3-7 exclude self. On0,1,3, m2 versusk1 gives3/2 versus2 for the endpoint despite identical radii; m3 gives allones whilek2 LOF differs. Identical formulas with different neighborhoods are not equivalent algorithms. No undocumented parameter shift, tie truncation or epsilon is substituted.

### Singularities, all-reference neighborhoods and computational limits

consistency: supported. Targets: AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor.

The final records qualify boundary cases instead of interpreting invalid scores as normality.

Self-only m1 or coincident neighborhoods can create zero means and nonfinite ratios; the code lrd&gt;0 guard does not regularize infinity/infinity. The distinct-point finite metric domain2&lt;=m&lt;=n and constructor limitations are explicit. Withm=n, symmetry makes every reach equal to the neighbor core and every density equal. Uniform scaling cancels in the unregularized formulas but fixed sklearn epsilon changes that property. Tie incidence can be quadratic. Neither score is a probability or a universal binary threshold.

### Versioned source authority and honest original-PDF limits

provenance: supported. Targets: AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor.

Mechanism evidence and context-only sources remain separated.

All eight ELKI files were fully read; the test was not executed. Original1999 parsed prose was read across all9pages but figures/equations were not visually verified and the PDF download failed. It is context only; immutable code and exact neighbor contracts support the curated mechanism. The earlier full12-page LOF visual reading and pinned sklearn reading were reused with unchanged source-byte checks. Every final record field was reread after canonical inspection; a second capture added the unchanged LOF calculator and verified target hashes without changing the reviewed records.

### Resolve historical LOF note without altering its mechanism

provenance: supported. Targets: AIMech:LocalOutlierFactor.

The LOF update is limited to its comparison note and actual curation time.

The original claims, evidence, mapping and limitations compare structurally equal to the preceding saved report. Its formerly unresolved OPTICS-OF identity comparison now points to the separately maintained record. Existing author self-review remains immutable; this successor cohort review covers both final records. All442 generated AIO records are unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:OPTICSOutlierFactor, AIMech:LocalOutlierFactor. Self inclusion changes density and score averaging even with identical core radii. Exact3-point counterexamples rule out equivalence by neighbor-count shift. Neither algorithm requires an OPTICS ordering or a clustering; retain both separately from those concepts.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T091349Z-optics-outlier-factor.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 512 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches of both checkouts included ignored and hidden files, all aliases, the original title and DOI: 23 matches in each checkout were read in 19 distinct context windows at 46 locations. These are LOF comparison notes, prior searches and unresolved discovery context, not an existing OPTICS-OF record. All 99 semantic AIO rows, 13 annotated CLASS nodes with outgoing edges, 71 native identity-field matches and 21 contextual YAMLs were inspected or reused after unchanged-content checks. This is a bounded local corpus assessment. |
| mapping | sources/aio/aio.json; 13 annotated CLASS nodes/outgoing edges and21 contextual YAMLs | supports | OPTICS-OF computes relative local outlier scores from unlabeled observations, supporting a related algorithm-to-task association with AIO:UnsupervisedLearning. The target is a MachineLearningTask, so the link asserts neither equivalence nor subclassing. BinaryClassification and its supervised ancestry do not describe the unthresholded core. Clustering, DBSCAN and OPTICS produce cluster structure or a reachability ordering; this standalone score needs neither a partition nor an OPTICS traversal. The three AIO KnearestNeighbor classes concern voting or response averaging, unlike these density ratios. RegressionAnalysis, DimensionalityReduction, DataPreparation and SelectionAndSamplingBias do not identify the procedure. Native LOF differs by explicit self exclusion; domain-description and metric-learning methods have different rules or outputs. |
| finite-boundaries | research/discovery/optics-outlier-factor-boundaries.py | supports | Exact finite rational calculations verify self inclusion, self reach equal to core radius, differing LOF scores despite identical radii, all-reference score one, all-ties versus truncated neighborhoods, uniform scaling and undefined zero means. These are formula checks, not ELKI execution or benchmark reproduction. |
| lof-boundaries | research/discovery/local-outlier-factor-boundaries.py | supports | Exact rational calculations verify oriented neighbor-radius reachability, non-rawk2 reaches, below-one values, changing rankings, uniform scaling, isolated-pair scores, all-ties versus exact-k differences, zero-reach undefinedness, nonmonotonic k dependence and fixed-epsilon loss of exact scale invariance. This is a transparent definition check, not historical or modern library execution or a benchmark. Reexecuted unchanged exact calculation; result matches prior recorded output. |
| elki-opticsof | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki/src/main/java/elki/outlier/OPTICSOF.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI OPTICSOF-0.8.0.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| elki-wrapper | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-api/src/main/java/elki/database/query/knn/WrappedKNNDBIDByLookup.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI WrappedKNNDBIDByLookup.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| elki-heap | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-dbids-int/src/main/java/elki/database/ids/integer/DoubleIntegerDBIDKNNHeap.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI DoubleIntegerDBIDKNNHeap.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| elki-list | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-dbids/src/main/java/elki/database/ids/KNNList.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI KNNList.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| elki-linear-object | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-database/src/main/java/elki/database/query/knn/LinearScanEuclideanKNNByObject.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI LinearScanEuclideanKNNByObject.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| elki-linear-id | https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-database/src/main/java/elki/database/query/knn/LinearScanKNNByDBID.java; Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. | supports | ELKI LinearScanKNNByDBID.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution or complete alternative-index audit. |
| breunig2000 | https://cse.hkust.edu.hk/~raywong/comp5331/References/LOFIdentifyingDensityBasedLocalOutliers.pdf; SIGMOD 2000 method; exact university-hosted 12-page author-layout PDF, all pages visually read. Printed pages 1-12 coincide with PDF pages; no offset to proceedings pages 93-104 is inferred. | supports | LOF: Identifying Density-Based Local Outliers. SIGMOD 2000 method; exact university-hosted 12-page author-layout PDF, all pages visually read. Printed pages 1-12 coincide with PDF pages; no offset to proceedings pages 93-104 is inferred. |
| breunig1999-context | https://scispace.com/pdf/optics-of-identifying-local-outliers-3rszd792dd.pdf; PKDD 1999, nine-page author-layout mirror. All parsed prose read, but equations and figures not visually verified; context only. Direct PDF download failed; no PDF checksum or proceedings-page offset asserted. | context_only | OPTICS-OF: Identifying Local Outliers. PKDD 1999, nine-page author-layout mirror. All parsed prose read, but equations and figures not visually verified; context only. Direct PDF download failed; no PDF checksum or proceedings-page offset asserted. |
| sklearn-lof | https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_lof.py; Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. Entire _lof.py read; no execution. | supports | scikit-learn LocalOutlierFactor implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. Entire _lof.py read; no execution. |
| sklearn-neighbors | https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_base.py; Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func and kneighbors fully read; remaining module and backend implementations not fully audited. | supports | scikit-learn KNeighborsMixin implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func and kneighbors fully read; remaining module and backend implementations not fully audited. |

## Limits And Additional Notes

- Adversarial author self-review only; both records remain DRAFT.
- The first vendored-check attempt failed because sandbox DNS was unavailable; the permitted public fetch retry passed all22 pinned artifacts.
- The1999paper was read as complete parsed prose, not a visually verified PDF. Direct mirror403, alternate university404, CiteSeer404, old-host TLS name mismatch, redirects and unavailable screenshot/browser surfaces are recorded. No certificate verification or access control was bypassed.
- Mechanism claims rely on exact official ELKI0.8.0 source bytes: main class, test and six neighbor-contract/query files fully read. Alternative index backends and QueryBuilder internals were not fully audited; no Java code was executed.
- Self-inclusive OPTICS-OF is distinguished from original self-excluded LOF by exact rational examples despite matching radii. Ties, self reach, m=n, m1 and duplicate singularities are explicit; source guards are not treated as mathematical regularization.
- No paper figure-derived or numerical performance advantage is curated. The test fixture was read but not executed; historical accuracy, runtime and calibration are not reproduced.
- The prior12-page LOF paper was visually read and its unchanged source bytes reused. All existing LOF claims remain unchanged; its identity note now identifies the subsequent comparison record. Both final records receive a full-field category self-review.
- One addition brings native coverage to513 while all442 generated AIO records remain unchanged. The LMU catalogue adds one pending source cohort, leaving441 pending and other unresolved dispositions. Discovery is ongoing.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T091815Z-optics-outlier-factor
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of OPTICS-OF and LOF boundaries
started_at: '2026-10-12T09:15:21Z'
finished_at: '2026-10-12T09:18:15Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent inspected complete versioned ELKI source
    and relevant exact-query contracts, compared the fully read LOF source, reread
    all final target fields, examined ignored-inclusive identity and mapping context,
    and challenged self/tie/zero/scale behavior with exact rational calculations.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain self-inclusive OPTICS-OF and self-excluded LOF as distinct scoring
  procedures. Original1999 parsed text is context only, while immutable official implementation
  supports OPTICS-OF mechanisms. No actionable defect remains in the two final records.
source:
  git_revision: 340d1710beea5d7e57c8b403ba2b6f9516767285
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/KnearestNeighborAlgorithm.yaml
    sha256: cdb4ab16dea60d54981c94dd2474ac427ffd0e35b728b6356e12cecf87b7a5c0
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/KnearestNeighborRegressionAlgorithm.yaml
    sha256: d601b4b9fe609add6e8f9fad5cd43c623bbae548ec8eb36b1b75515fa58d56d2
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: context
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: context
  - path: data/curated/LocalOutlierFactor.yaml
    sha256: b9293fde56804e7df6d3056e00b08240ca9dc8711a715bda54d064cfd9bc8812
    role: target
  - path: data/curated/NearestNeighborDistanceNormDataDescription.yaml
    sha256: a6751b2f10223f689904cfec7d6a880a263d16be0716eb007fb7fa289c8e86bb
    role: context
  - path: data/curated/NearestNeighborRatioDataDescription.yaml
    sha256: 93d66c76f275d5dbc06a80c69af19dd9bceaa9cd564945f17db714f6faaf1f28
    role: context
  - path: data/curated/NeighborhoodComponentsAnalysis.yaml
    sha256: 9aa5fa5229196181f23e7ba5910dba00623a60e558b97233e6cefc1f0fbbd577
    role: context
  - path: data/curated/OPTICS.yaml
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    role: context
  - path: data/curated/OPTICSOutlierFactor.yaml
    sha256: fecfad5c8d862a5622fc7ba63c60f839ba80cb0c5077d14a39ed77e08daf6270
    role: target
  - path: data/curated/PrototypeBasedDomainDescription.yaml
    sha256: 3b4fce38fde950f9edc3bbef8cbfde5fa8e1d8075eb98a758eb89abd3ca69874
    role: context
  - path: research/discovery/20261012T091349Z-optics-outlier-factor.json
    sha256: 16667a2ce7e628d965cccb39c06c508176e5d88fe9c24cab391b7f7dfd5a9979
    role: context
  - path: research/discovery/local-outlier-factor-boundaries.py
    sha256: 94310e4d5dc70233224a77259936ba6bd80411af504610023cc4131b51bba131
    role: context
  - path: research/discovery/optics-outlier-factor-boundaries.py
    sha256: b87b237a08c1c7237127bd78cab38316cac9d1c73fbc2931a0defb7d8d0e0c49
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:OPTICSOutlierFactor
  path: data/curated/OPTICSOutlierFactor.yaml
  label: OPTICS outlier factor
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OPTICSOutlierFactor.yaml
    role: maintained
- target_id: AIMech:LocalOutlierFactor
  path: data/curated/LocalOutlierFactor.yaml
  label: Local outlier factor
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LocalOutlierFactor.yaml
    role: maintained
scope:
  description: Every field of the selected local reachability-density scoring cohort.
  selection: Exact maintained IDs AIMech:OPTICSOutlierFactor and AIMech:LocalOutlierFactor,
    without sampling.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exclusions:
  - target: Other contextual AIO/native records
    reason: Identity and mapping context, not renewed scientific approval.
  - target: Original1999 visual equations, figures and experimental values
    reason: Parsed prose only; no successful PDF visual inspection.
  - target: Alternative index backends, QueryBuilder internals and Java execution
    reason: Not a complete runtime/backend audit.
  - target: Generated website
    reason: Freshness/validity checks, without separate visual-design review.
  - target: Remaining discovery frontier
    reason: 441 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 112.32s (0:01:52)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 513 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 158 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 154,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: opticsof-exact-boundaries
  name: opticsof exact boundary calculations
  command: python3 research/discovery/optics-outlier-factor-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: '{"data_0_1_3_self_inclusive_m2": ["1", "1", "3/2"], "corresponding_self_excluded_k1":
    ["1", "1", "2"], "data_0_1_3_self_inclusive_m3": ["1", "1", "1"], "corresponding_self_excluded_k2":
    ["11/12", "6/5", "11/12"], "identical_core_radii_do_not_make_algorithms_equivalent":
    true, "self_reachability_is_core_distance_not_zero": true, "all_reference_neighborhoods_give_score_one":
    true, "boundary_ties_score": "4/3", "truncated_score": "1", "self_only_and_duplicate_zero_means_undefined":
    true, "uniform_positive_scaling_preserves_defined_core_scores": true, "scope":
    "Exact arithmetic from inspected self-inclusive scoring formulas and pinned source,
    compared to self-excluded LOF. No Java execution, index-backend validation or
    benchmark reproduction."}'
- check_id: lof-exact-boundaries
  name: lof exact boundary calculations
  command: python3 research/discovery/local-outlier-factor-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: '{"self_excluded_and_asymmetric_neighbor_radius": true, "k2_reachability_need_not_equal_raw_distance":
    true, "scores_at_k1": ["1", "1", "2"], "scores_at_k2": ["11/12", "6/5", "11/12"],
    "scores_can_be_below_one_and_rankings_change": true, "positive_uniform_scale_and_translation_invariant":
    true, "isolated_pair_both_score_one": true, "tie_inclusive_score": "3/2", "exact_k_truncation_score":
    "1", "zero_reachability_without_regularization_is_undefined": true, "fixed_additive_epsilon_breaks_exact_scale_invariance":
    true, "nonmonotonic_k_example": {"data": [0, 1, 2, 3, 4], "index": 0, "scores_by_k_1_to_4":
    ["1", "5/4", "44/45", "337/364"]}, "scope": "Exact finite rational calculations
    from Definitions3-7; no original implementation, learned model or benchmark executed."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T091349Z-optics-outlier-factor.json
  accessed_at: '2026-10-12T09:15:21Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 512
    preceding native IDs, names and aliases. No normalized identity collision was
    found. Fixed-string whole-word searches of both checkouts included ignored and
    hidden files, all aliases, the original title and DOI: 23 matches in each checkout
    were read in 19 distinct context windows at 46 locations. These are LOF comparison
    notes, prior searches and unresolved discovery context, not an existing OPTICS-OF
    record. All 99 semantic AIO rows, 13 annotated CLASS nodes with outgoing edges,
    71 native identity-field matches and 21 contextual YAMLs were inspected or reused
    after unchanged-content checks. This is a bounded local corpus assessment.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 13 annotated CLASS nodes/outgoing edges and21 contextual YAMLs
  accessed_at: '2026-10-12T09:15:21Z'
  support: supports
  summary: OPTICS-OF computes relative local outlier scores from unlabeled observations,
    supporting a related algorithm-to-task association with AIO:UnsupervisedLearning.
    The target is a MachineLearningTask, so the link asserts neither equivalence nor
    subclassing. BinaryClassification and its supervised ancestry do not describe
    the unthresholded core. Clustering, DBSCAN and OPTICS produce cluster structure
    or a reachability ordering; this standalone score needs neither a partition nor
    an OPTICS traversal. The three AIO KnearestNeighbor classes concern voting or
    response averaging, unlike these density ratios. RegressionAnalysis, DimensionalityReduction,
    DataPreparation and SelectionAndSamplingBias do not identify the procedure. Native
    LOF differs by explicit self exclusion; domain-description and metric-learning
    methods have different rules or outputs.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/optics-outlier-factor-boundaries.py
  accessed_at: '2026-10-12T09:15:21Z'
  snapshot_sha256: b87b237a08c1c7237127bd78cab38316cac9d1c73fbc2931a0defb7d8d0e0c49
  support: supports
  summary: Exact finite rational calculations verify self inclusion, self reach equal
    to core radius, differing LOF scores despite identical radii, all-reference score
    one, all-ties versus truncated neighborhoods, uniform scaling and undefined zero
    means. These are formula checks, not ELKI execution or benchmark reproduction.
- evidence_id: lof-boundaries
  kind: record_content
  reference: research/discovery/local-outlier-factor-boundaries.py
  accessed_at: '2026-10-12T09:15:21Z'
  snapshot_sha256: 94310e4d5dc70233224a77259936ba6bd80411af504610023cc4131b51bba131
  support: supports
  summary: Exact rational calculations verify oriented neighbor-radius reachability,
    non-rawk2 reaches, below-one values, changing rankings, uniform scaling, isolated-pair
    scores, all-ties versus exact-k differences, zero-reach undefinedness, nonmonotonic
    k dependence and fixed-epsilon loss of exact scale invariance. This is a transparent
    definition check, not historical or modern library execution or a benchmark. Reexecuted
    unchanged exact calculation; result matches prior recorded output.
- evidence_id: elki-opticsof
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki/src/main/java/elki/outlier/OPTICSOF.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:00:41Z'
  support: supports
  summary: ELKI OPTICSOF-0.8.0.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  snapshot_sha256: 67331ab9311aa8dec9f5188fb0a7c1eae25a5196df41f28ca253cfcb6a43bffd
- evidence_id: elki-wrapper
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-api/src/main/java/elki/database/query/knn/WrappedKNNDBIDByLookup.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:01:48Z'
  support: supports
  summary: ELKI WrappedKNNDBIDByLookup.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  snapshot_sha256: 9970de97961c2bd2ffc7a00059995acd4966c8dd08c4dd7412f0af3cd004c3f5
- evidence_id: elki-heap
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-dbids-int/src/main/java/elki/database/ids/integer/DoubleIntegerDBIDKNNHeap.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:01:48Z'
  support: supports
  summary: ELKI DoubleIntegerDBIDKNNHeap.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  snapshot_sha256: f2f56eb3d72b3917bd4dce0b2bd77be576184ac7c7cc8655c110d277a3460882
- evidence_id: elki-list
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-core-dbids/src/main/java/elki/database/ids/KNNList.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:01:48Z'
  support: supports
  summary: ELKI KNNList.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  snapshot_sha256: f7480775c25b335eb56ce9b54fc539a205864c04ced7f069fa3998d353774fbb
- evidence_id: elki-linear-object
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-database/src/main/java/elki/database/query/knn/LinearScanEuclideanKNNByObject.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:01:48Z'
  support: supports
  summary: ELKI LinearScanEuclideanKNNByObject.java. Release 0.8.0 immutable commit
    ff7ac7f3853b958a4a47486522bc7510210583c6. Entire file read; no Java execution
    or complete alternative-index audit.
  snapshot_sha256: 9b40694372e8ab2dc4d881af12579d2214d4c5a70a652c7e20ee7c379a8d5044
- evidence_id: elki-linear-id
  kind: primary_source
  reference: https://raw.githubusercontent.com/elki-project/elki/ff7ac7f3853b958a4a47486522bc7510210583c6/elki-database/src/main/java/elki/database/query/knn/LinearScanKNNByDBID.java
  locator: Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  accessed_at: '2026-10-12T09:01:48Z'
  support: supports
  summary: ELKI LinearScanKNNByDBID.java. Release 0.8.0 immutable commit ff7ac7f3853b958a4a47486522bc7510210583c6.
    Entire file read; no Java execution or complete alternative-index audit.
  snapshot_sha256: 72bf3d5626ba5355f053360c38cfe318e52bb859884a666fc4c09dcec10a5e39
- evidence_id: breunig2000
  kind: primary_source
  reference: https://cse.hkust.edu.hk/~raywong/comp5331/References/LOFIdentifyingDensityBasedLocalOutliers.pdf
  locator: SIGMOD 2000 method; exact university-hosted 12-page author-layout PDF,
    all pages visually read. Printed pages 1-12 coincide with PDF pages; no offset
    to proceedings pages 93-104 is inferred.
  accessed_at: '2026-10-12T08:37:29Z'
  support: supports
  summary: 'LOF: Identifying Density-Based Local Outliers. SIGMOD 2000 method; exact
    university-hosted 12-page author-layout PDF, all pages visually read. Printed
    pages 1-12 coincide with PDF pages; no offset to proceedings pages 93-104 is inferred.'
  snapshot_sha256: d6e378582bf7a0f6f9e34e2b11b0b4e7bc9016b4f20e5bc041760f6bb57cb566
- evidence_id: breunig1999-context
  kind: primary_source
  reference: https://scispace.com/pdf/optics-of-identifying-local-outliers-3rszd792dd.pdf
  locator: PKDD 1999, nine-page author-layout mirror. All parsed prose read, but equations
    and figures not visually verified; context only. Direct PDF download failed; no
    PDF checksum or proceedings-page offset asserted.
  accessed_at: '2026-10-12T09:03:14Z'
  support: context_only
  summary: 'OPTICS-OF: Identifying Local Outliers. PKDD 1999, nine-page author-layout
    mirror. All parsed prose read, but equations and figures not visually verified;
    context only. Direct PDF download failed; no PDF checksum or proceedings-page
    offset asserted.'
- evidence_id: sklearn-lof
  kind: primary_source
  reference: https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_lof.py
  locator: Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked
    by scikit-learn 1.7.2 API documentation. Entire _lof.py read; no execution.
  accessed_at: '2026-10-12T08:42:45Z'
  support: supports
  summary: scikit-learn LocalOutlierFactor implementation. Immutable source commit
    1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation.
    Entire _lof.py read; no execution.
  snapshot_sha256: a05774d4db7d6ded41374f68b1b678c5f672d1e8454cddea9ebe7841aa4b4e63
- evidence_id: sklearn-neighbors
  kind: primary_source
  reference: https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_base.py
  locator: Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked
    by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func
    and kneighbors fully read; remaining module and backend implementations not fully
    audited.
  accessed_at: '2026-10-12T08:47:20Z'
  support: supports
  summary: scikit-learn KNeighborsMixin implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe
    linked by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func
    and kneighbors fully read; remaining module and backend implementations not fully
    audited.
  snapshot_sha256: 6686ee9f3f36ae7ab9b572a90931e689345e8d5ab6b1879361fb2ea15990d9e5
assessments:
- assessment_id: opticsoutlierfactor-identity
  area: identity
  topic: Identity, definition and concept scope
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - identity
  - elki-opticsof
  - elki-heap
  - elki-linear-id
  summary: Retain the distinct native DRAFT algorithm.
  details: 'An unsupervised local outlier-scoring procedure that uses self-inclusive,
    tie-inclusive nearest neighborhoods to compute inverse mean neighbor-radius reachability
    and averages neighbor-to-query density ratios. This record denotes OPTICS-OF with
    the self-inclusive convention corroborated by the inspected ELKI implementation.
    It is distinct from OPTICS ordering, DBSCAN noise labels, original self-excluded
    LOF, neighbor-label voting and raw distance ranking. Original 1999 parsed text
    is context; mechanism claims are grounded in immutable official source and exact
    neighbor contracts. Compared all 442 pinned AIO IDs, labels and scoped synonyms
    with all 512 preceding native IDs, names and aliases. No normalized identity collision
    was found. Fixed-string whole-word searches of both checkouts included ignored
    and hidden files, all aliases, the original title and DOI: 23 matches in each
    checkout were read in 19 distinct context windows at 46 locations. These are LOF
    comparison notes, prior searches and unresolved discovery context, not an existing
    OPTICS-OF record. All 99 semantic AIO rows, 13 annotated CLASS nodes with outgoing
    edges, 71 native identity-field matches and 21 contextual YAMLs were inspected
    or reused after unchanged-content checks. This is a bounded local corpus assessment.'
- assessment_id: opticsoutlierfactor-mapping
  area: grounding
  topic: Related algorithm-to-task AIO association
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - mapping
  - elki-opticsof
  - elki-heap
  - elki-linear-id
  summary: Related mapping is supported without equivalence or subclassing.
  details: OPTICS-OF computes relative local outlier scores from unlabeled observations,
    supporting a related algorithm-to-task association with AIO:UnsupervisedLearning.
    The target is a MachineLearningTask, so the link asserts neither equivalence nor
    subclassing. BinaryClassification and its supervised ancestry do not describe
    the unthresholded core. Clustering, DBSCAN and OPTICS produce cluster structure
    or a reachability ordering; this standalone score needs neither a partition nor
    an OPTICS traversal. The three AIO KnearestNeighbor classes concern voting or
    response averaging, unlike these density ratios. RegressionAnalysis, DimensionalityReduction,
    DataPreparation and SelectionAndSamplingBias do not identify the procedure. Native
    LOF differs by explicit self exclusion; domain-description and metric-learning
    methods have different rules or outputs.
- assessment_id: opticsoutlierfactor-self-inclusive-locality
  area: evidence
  topic: self inclusive locality
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-wrapper
  - elki-linear-object
  - elki-linear-id
  - elki-heap
  - elki-list
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'For a finite reference dataset D of n observations, a finite metric and
    2<=m<=n, core_m(p) is the mth ordered distance to observations in D, including
    p itself. N_m(p) retains every observation at distance at most that boundary,
    including all ties. The inspected exact linear scans and heap include the indexed
    query and boundary ties; a fixed-count truncation is not the same convention.
    The m range describes the well-defined distinct-point metric case, not a claim
    that every constructor enforces it. Locators: OPTICSOF.run, passes 1-3; getKNN:
    retrieve query object without removing its database ID; getKNN: scan every relation
    ID; getKNN: scan every relation ID; insert, addToTies, toKNNList and toKNNListSqrt:
    retain boundary ties; Interface size and getKNNDistance contracts'
- assessment_id: opticsoutlierfactor-reachability-and-density-ratios
  area: evidence
  topic: reachability and density ratios
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'For o in N_m(p), reach_m(p,o)=max(core_m(o),d(p,o)), using the neighbor
    radius. Set lrd_m(p)=|N_m(p)| divided by the sum of these reaches, and OF_m(p)
    to the mean of lrd_m(o)/lrd_m(p) over N_m(p). Thus self reachability is core_m(p),
    not zero, and the self term contributes a ratio of one when defined. The formulas
    require positive finite mean reaches for all densities used. These inverse-distance
    quantities are not normalized probability densities, and the resulting relative
    score is not an outlier probability or an automatic binary decision. Locators:
    OPTICSOF.run, passes 1-3'
- assessment_id: opticsoutlierfactor-standalone-three-pass-computation
  area: evidence
  topic: standalone three pass computation
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - breunig1999-context
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'The inspected implementation first stores neighborhoods and core radii,
    then computes all local reachability densities, then averages their neighbor-to-query
    ratios. It does not run an OPTICS ordering or extract a clustering. Pairwise reachability
    in the score must not be replaced with a minimum reachability accumulated during
    an OPTICS traversal. Locators: OPTICSOF.run, passes 1-3; Parsed Definitions 4-7
    and computational discussion, PDF pp5-6 and8; not visually verified'
- assessment_id: opticsoutlierfactor-distinct-from-self-excluded-lof
  area: evidence
  topic: distinct from self excluded lof
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - breunig2000
  - finite-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'OPTICS-OF and original LOF are retained separately because including the
    query changes both density and score averaging. Under absolute distance, D={0,1,3}
    gives OPTICS-OF scores {1,1,3/2} at m=2, whereas self-excluded LOF gives {1,1,2}
    at k=1, despite identical core radii. At m=3, OPTICS-OF gives {1,1,1}, while LOF
    at k=2 gives {11/12,6/5,11/12}. These exact curator calculations rule out identifying
    the two procedures merely by shifting the neighbor-count parameter. Locators:
    OPTICSOF.run, passes 1-3; Definitions 3-7, printed/PDF pp3-4; exact comparisons
    in research/discovery/optics-outlier-factor-boundaries.py'
- assessment_id: opticsoutlierfactor-ties-and-scale-boundaries
  area: evidence
  topic: ties and scale boundaries
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-heap
  - finite-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'Boundary ties can change scores: for D={0,2,4,5} and m=2, point 2 has
    three retained neighbors and score 4/3; selecting only itself and neighbor 0 instead
    gives score 1. Positive uniform scaling of every distance cancels from defined
    density ratios, but feature-specific scaling can change neighborhoods. When m=n,
    every neighborhood is D and reach_m(p,o)=core_m(o), so all densities are equal
    and all defined scores are one. A score of one therefore does not by itself establish
    domain normality. Locators: OPTICSOF.run, passes 1-3; Boundary-tie retention;
    exact curator calculations in research/discovery/optics-outlier-factor-boundaries.py'
- assessment_id: opticsoutlierfactor-zero-distance-and-parameter-limits
  area: evidence
  topic: zero distance and parameter limits
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-list
  - finite-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'With m=1 and a unique query location, the self-only neighborhood has zero
    mean reachability; duplicates can also produce zero means at larger m. The mathematical
    ratios are then undefined. The inspected parameterizer requires m>1 and defaults
    to Euclidean distance, but its constructor does not enforce m<=n. KNNList may
    report an infinite boundary when fewer than m neighbors exist. The scoring loop
    adds no epsilon; its lrd>0 guard does not resolve infinity/infinity from coincident
    neighborhoods. A fallback zero or nonfinite output outside the stated finite domain
    is not evidence of normality. Locators: OPTICSOF.run, passes 1-3; Constructor
    and Par.configure; getKNNDistance: infinite distance if fewer than k neighbors'
- assessment_id: opticsoutlierfactor-implementation-and-computation-scope
  area: evidence
  topic: implementation and computation scope
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-heap
  - elki-linear-id
  - breunig1999-context
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'The evidence establishes the inspected release source and exact linear-query/tie
    contracts, not every index backend, historical implementation or runtime result.
    Stored all-ties neighborhoods can contain every observation even for small m,
    requiring quadratic neighbor incidences. All-pairs neighbor search can require
    quadratic distance evaluations, and selection/index costs need separate analysis;
    no universal near-linear or n-log-n complexity follows. The historical paper text
    and versioned test fixture provide context, but no figure-derived claim, numerical
    performance advantage, library benchmark or probability calibration is curated.
    Locators: OPTICSOF.run, passes 1-3; Boundary-tie storage; Full relation scan per
    query; Parsed computational and experimental prose, PDF pp7-8; figures not visually
    verified'
- assessment_id: localoutlierfactor-identity
  area: identity
  topic: Identity, definition and concept scope
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - identity
  - breunig2000
  summary: Retain the distinct native DRAFT algorithm.
  details: 'An unsupervised local outlier-scoring procedure that compares each observation''s
    inverse mean reachability distance with those of its tie-inclusive nearest neighbors
    and returns their mean density ratio. This record denotes the original fixed-neighborhood
    LOF procedure, with optional scale aggregation and versioned implementation conventions
    explicitly separated. It is distinct from neighbor-label voting, raw kth-distance
    ranking, thresholded NNDD or PDD, DBSCAN noise labels and OPTICS reachability
    ordering. The initial LOF review left OPTICS-OF as an unresolved related identity
    comparison. The subsequent AIMech:OPTICSOutlierFactor record documents its distinct
    self-inclusive convention; the two are not treated as aliases. Compared all 442
    pinned AIO IDs, labels and scoped synonyms with all 511 preceding native IDs,
    names and aliases. No normalized identity collision was found. Fixed-string whole-word
    searches of both checkouts included ignored and hidden files, LOF, expanded names
    and both publication DOIs: 16 worktree and 17 main matches, comprising 13 distinct
    context windows at 33 locations, were read. They are pending discovery context
    and an unrelated BASIC-language LOF token in an ignored Pygments lexer. Semantic
    searches inspected 99 AIO name/synonym/definition rows and 70 native name/definition
    matches, reusing 85 and 67 unchanged previously read rows respectively. Thirteen
    annotated AIO CLASS nodes with outgoing edges and twenty contextual YAMLs were
    inspected or reused after unchanged-byte checks. This is a bounded corpus assessment,
    not absence from all ontologies.'
- assessment_id: localoutlierfactor-mapping
  area: grounding
  topic: Related algorithm-to-task AIO association
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - mapping
  - breunig2000
  summary: Related mapping is supported without equivalence or subclassing.
  details: LOF infers neighborhood-relative outlier scores from unlabeled observations,
    giving a related algorithm-to-task association with AIO:UnsupervisedLearning.
    The target is a MachineLearningTask; this link is neither exact equivalence nor
    a subclass assertion. The core score does not itself assign two classes, so BinaryClassification
    and its supervised ancestry are not selected. Clustering and OPTICS/DBSCAN organize
    clusters or reachability orderings, whereas LOF does not require a partition.
    All three AIO KnearestNeighbor classes specify label voting or response averaging,
    not local reachability ratios; RegressionAnalysis requires dependent/independent-variable
    relationships. DimensionalityReduction, DataPreparation and SelectionAndSamplingBias
    do not identify this scoring procedure. Native neighbor-ratio and distance-norm
    domain descriptions, PDD, supervised metric learning and density clustering have
    different outputs or neighborhood rules.
- assessment_id: localoutlierfactor-tie-inclusive-locality
  area: evidence
  topic: tie inclusive locality
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'For n reference observations and 1<=k<=n-1, k-distance(p) is the kth ordered
    distance to other observations, excluding p itself. N_k(p) contains every other
    observation whose distance is at most that boundary, including all ties, so its
    size can exceed k. The reference dataset and dissimilarity define locality; the
    procedure does not require labeled normal/outlier examples or an explicit clustering.
    Locators: Section 4, Definitions 3-4, printed/PDF p3; Section 1, p1'
- assessment_id: localoutlierfactor-reachability-density-ratio
  area: evidence
  topic: reachability density ratio
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'Define reach_k(p,o)=max(k-distance(o),d(p,o)), using the neighbor o''s
    radius, not p''s. Reachability is generally asymmetric. Local reachability density
    lrd_k(p) is the reciprocal of the mean reachability over o in N_k(p), and LOF_k(p)
    is the mean of lrd_k(o)/lrd_k(p) over that same neighborhood. These formulas require
    nonempty neighborhoods and positive finite mean reaches for the densities used.
    Reachability density has inverse-distance units; it is not a normalized probability
    density. LOF is a dimensionless relative score. Locators: Definitions 5-7, printed/PDF
    pp3-4'
- assessment_id: localoutlierfactor-relative-score-not-probability
  area: evidence
  topic: relative score not probability
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - lof-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'A large score indicates lower reachability density relative to neighbors;
    it is neither an outlier probability nor a universal decision threshold. The paper''s
    near-one bound assumes a closed two-hop neighborhood and bounded positive reachability
    variation. Scores can be below one: for D={0,1,3} under absolute distance and
    k=2, the scores are {11/12,6/5,11/12}. At k=1 they are {1,1,2}, reversing the
    center-versus-endpoint ordering. Two arbitrarily separated observations both score
    one at k=1; absolute isolation alone is not enough. These examples are exact curator
    calculations. Locators: Definition 7 and Lemma 1, printed/PDF p4; Sections 5-6,
    pp4-8; research/discovery/local-outlier-factor-boundaries.py'
- assessment_id: localoutlierfactor-ties-zeros-and-scale
  area: evidence
  topic: ties zeros and scale
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - lof-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'Boundary ties are part of the original definition: D={0,2,4,5}, k=1 gives
    point 2 score 3/2 when both equidistant neighbors are retained, but score 1 if
    an exact-k implementation chooses only neighbor 0. Coincident observations can
    give zero mean reachability and undefined density ratios; the paper assumes no
    duplicates and mentions a distinct-coordinate alternative without making an additive
    regularizer part of core LOF. Multiplying every distance by a positive constant
    leaves the unregularized core score unchanged when defined; feature-specific rescaling
    can change neighborhoods and scores. For D={0,1,3}, k=2, reach(0,1)=2 exceeds
    d(0,1)=1, so the paper''s informal k=2 raw-distance reduction is not generally
    implied by its self-excluded definitions. Locators: Definitions 3-7 and duplicate
    discussion, printed/PDF pp3-4; Section 6, p7; exact curator calculations in research/discovery/local-outlier-factor-boundaries.py'
- assessment_id: localoutlierfactor-neighborhood-scale-selection
  area: evidence
  topic: neighborhood scale selection
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - lof-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'Scores can vary nonmonotonically with k. The paper suggests choosing a
    lower and upper neighborhood size and ranking each point by its maximum LOF over
    that range; this is an optional multiscale ranking heuristic, distinct from a
    fixed-k score. Suggested lower bounds near 10 and common choices around 10-20
    are empirical guidance, not mathematical validity constraints or universally optimal
    defaults. Small groups can appear ordinary relative to one another at some scales,
    so the chosen range affects which deviations are exposed. Locators: Section 6
    and Figures 7-8, printed/PDF pp7-9'
- assessment_id: localoutlierfactor-versioned-implementation-conventions
  area: evidence
  topic: versioned implementation conventions
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  - lof-boundaries
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'The inspected scikit-learn 1.7.2-linked implementation uses a fixed neighbor
    count, excludes the indexed query for fitted training scores, and adds 1e-10 to
    mean reachability before inversion. It exposes negative LOF as negative_outlier_factor_;
    auto contamination chooses offset -1.5, while supplied contamination chooses a
    training-score percentile and labels scores strictly below it. These are implementation
    choices, not the paper''s all-ties and unregularized definition or a universally
    validated 1.5 cutoff. Ties can prevent an exact requested outlier fraction. A
    fixed additive epsilon also prevents automatically transferring exact uniform-scale
    invariance. Locators: Definitions 3-7, printed/PDF pp3-4; soccer illustration
    and Table 3, p10; exact fixed-epsilon curator calculation; LocalOutlierFactor.fit,
    _predict and _local_reachability_density; KNeighborsMixin._kneighbors_reduce_func
    and kneighbors, including query_is_train and final fixed-shape self-removal'
- assessment_id: localoutlierfactor-novelty-query-distinction
  area: evidence
  topic: novelty query distinction
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'With novelty=True, the inspected implementation scores new queries against
    stored training-neighbor radii and training densities; it does not insert the
    new query batch into reference neighborhoods. Supplying training points through
    score_samples can include each query itself as a neighbor, unlike the fitted training-score
    calculation. Novelty-query scores therefore need not equal negative_outlier_factor_
    on the training set. This source-scoped extension does not redefine the original
    dataset-level score, and no library runtime or historical-code equivalence was
    tested. Locators: Definitions 3-7, printed/PDF pp3-4; LocalOutlierFactor.score_samples,
    decision_function and their novelty docstrings; KNeighborsMixin.kneighbors: X
    is None training branch versus explicit-query branch'
- assessment_id: localoutlierfactor-computation-and-evaluation-scope
  area: evidence
  topic: computation and evaluation scope
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the stated source, parameter and implementation limits.
  details: 'After neighborhoods are available, computing densities and scores visits
    the retained neighbor incidences for each chosen k. Original all-boundary-ties
    neighborhoods can contain n-1 observations even for small k, so O(n*k) storage
    or linear score work requires a bounded-neighborhood assumption. All-pairs search
    can require quadratic distance evaluations; index performance depends on data
    and dimension. The paper''s synthetic, sports and color-histogram examples and
    historical wall-clock timings are conditional demonstrations, not universal accuracy
    or speed guarantees. The sports results use selected features and neighborhood
    ranges with domain interpretation, not held-out probability calibration. No numerical
    performance advantage is curated. Locators: Sections 7.1-7.3, Figures 9-11 and
    Table 3, printed/PDF pp9-11; Definition 4, p3'
- assessment_id: self-inclusion-boundary
  area: consistency
  topic: Distinct procedures despite common density-ratio form
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-wrapper
  - elki-heap
  - elki-linear-id
  - elki-linear-object
  - elki-list
  - breunig2000
  - finite-boundaries
  summary: Retain OPTICS-OF and LOF separately.
  details: The exact queries include the indexed observation, heap serialization retains
    boundary ties and the main OPTICSOF loop does not remove self. Self reach is the
    own core radius, and its density-ratio contribution is one. LOF Definitions3-7
    exclude self. On0,1,3, m2 versusk1 gives3/2 versus2 for the endpoint despite identical
    radii; m3 gives allones whilek2 LOF differs. Identical formulas with different
    neighborhoods are not equivalent algorithms. No undocumented parameter shift,
    tie truncation or epsilon is substituted.
- assessment_id: adversarial-boundaries
  area: consistency
  topic: Singularities, all-reference neighborhoods and computational limits
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-list
  - elki-heap
  - finite-boundaries
  - lof-boundaries
  summary: The final records qualify boundary cases instead of interpreting invalid
    scores as normality.
  details: Self-only m1 or coincident neighborhoods can create zero means and nonfinite
    ratios; the code lrd>0 guard does not regularize infinity/infinity. The distinct-point
    finite metric domain2<=m<=n and constructor limitations are explicit. Withm=n,
    symmetry makes every reach equal to the neighbor core and every density equal.
    Uniform scaling cancels in the unregularized formulas but fixed sklearn epsilon
    changes that property. Tie incidence can be quadratic. Neither score is a probability
    or a universal binary threshold.
- assessment_id: evidence-access-and-provenance
  area: provenance
  topic: Versioned source authority and honest original-PDF limits
  outcome: supported
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - elki-opticsof
  - breunig1999-context
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  summary: Mechanism evidence and context-only sources remain separated.
  details: All eight ELKI files were fully read; the test was not executed. Original1999
    parsed prose was read across all9pages but figures/equations were not visually
    verified and the PDF download failed. It is context only; immutable code and exact
    neighbor contracts support the curated mechanism. The earlier full12-page LOF
    visual reading and pinned sklearn reading were reused with unchanged source-byte
    checks. Every final record field was reread after canonical inspection; a second
    capture added the unchanged LOF calculator and verified target hashes without
    changing the reviewed records.
- assessment_id: maintenance-scope
  area: provenance
  topic: Resolve historical LOF note without altering its mechanism
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - identity
  - breunig2000
  - elki-opticsof
  - finite-boundaries
  summary: The LOF update is limited to its comparison note and actual curation time.
  details: The original claims, evidence, mapping and limitations compare structurally
    equal to the preceding saved report. Its formerly unresolved OPTICS-OF identity
    comparison now points to the separately maintained record. Existing author self-review
    remains immutable; this successor cohort review covers both final records. All442
    generated AIO records are unchanged.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:OPTICSOutlierFactor
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - elki-opticsof
  - elki-heap
  - elki-linear-id
  - breunig2000
  - finite-boundaries
  rationale: Self inclusion changes density and score averaging even with identical
    core radii. Exact3-point counterexamples rule out equivalence by neighbor-count
    shift. Neither algorithm requires an OPTICS ordering or a clustering; retain both
    separately from those concepts.
limitations:
- Adversarial author self-review only; both records remain DRAFT.
- The first vendored-check attempt failed because sandbox DNS was unavailable; the
  permitted public fetch retry passed all22 pinned artifacts.
- The1999paper was read as complete parsed prose, not a visually verified PDF. Direct
  mirror403, alternate university404, CiteSeer404, old-host TLS name mismatch, redirects
  and unavailable screenshot/browser surfaces are recorded. No certificate verification
  or access control was bypassed.
- 'Mechanism claims rely on exact official ELKI0.8.0 source bytes: main class, test
  and six neighbor-contract/query files fully read. Alternative index backends and
  QueryBuilder internals were not fully audited; no Java code was executed.'
- Self-inclusive OPTICS-OF is distinguished from original self-excluded LOF by exact
  rational examples despite matching radii. Ties, self reach, m=n, m1 and duplicate
  singularities are explicit; source guards are not treated as mathematical regularization.
- No paper figure-derived or numerical performance advantage is curated. The test
  fixture was read but not executed; historical accuracy, runtime and calibration
  are not reproduced.
- The prior12-page LOF paper was visually read and its unchanged source bytes reused.
  All existing LOF claims remain unchanged; its identity note now identifies the subsequent
  comparison record. Both final records receive a full-field category self-review.
- One addition brings native coverage to513 while all442 generated AIO records remain
  unchanged. The LMU catalogue adds one pending source cohort, leaving441 pending
  and other unresolved dispositions. Discovery is ongoing.
links: []
tags:
- native-concepts
- local-outlier-scoring
- self-review
- discovery-ongoing
```
