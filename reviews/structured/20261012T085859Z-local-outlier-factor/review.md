# Scientific self-review of local outlier factor

- Review: 20261012T085859Z-local-outlier-factor
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T08:53:36Z
- Finished UTC: 2026-10-12T08:58:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain original LOF with self exclusion, all boundary ties, oriented reachability and unregularized relative density ratios. Optional scale aggregation and versioned software thresholds, epsilon and novelty scoring remain distinct. No actionable defect in the final record was found.

## Scope And Provenance

Every field of the single maintained LOF record.

Selection: Exact maintained ID AIMech:LocalOutlierFactor, without sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c0052b03296cd8fd4476edd13927f91144d59e9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LocalOutlierFactor | data/curated/LocalOutlierFactor.yaml | maintained | Local outlier factor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:LocalOutlierFactor | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 149.66s (0:02:29)<br>Checked 442 record(s); 0 failed.<br>Checked 512 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 157 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 153,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:LocalOutlierFactor | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:LocalOutlierFactor | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:LocalOutlierFactor | Exited0 without output. |
| Exact LOF boundary calculations | passed | True | AIMech:LocalOutlierFactor | {"self_excluded_and_asymmetric_neighbor_radius": true, "k2_reachability_need_not_equal_raw_distance": true, "scores_at_k1": ["1", "1", "2"], "scores_at_k2": ["11/12", "6/5", "11/12"], "scores_can_be_below_one_and_rankings_change": true, "positive_uniform_scale_and_translation_invariant": true, "isolated_pair_both_score_one": true, "tie_inclusive_score": "3/2", "exact_k_truncation_score": "1", "zero_reachability_without_regularization_is_undefined": true, "fixed_additive_epsilon_breaks_exact_scale_invariance": true, "nonmonotonic_k_example": {"data": [0, 1, 2, 3, 4], "index": 0, "scores_by_k_1_to_4": ["1", "5/4", "44/45", "337/364"]}, "scope": "Exact finite rational calculations from Definitions3-7; no original implementation, learned model or benchmark executed."} |

## Scientific And Domain Assessments

### Original fixed-k LOF identity and algorithm scope

identity: supported. Targets: AIMech:LocalOutlierFactor.

Retain the supported native DRAFT algorithm.

All labels, aliases, scoped synonyms and record identities were checked. Both ignored-inclusive checkout searches were read in13 distinct windows at33 locations; pending leads and BASIC LOF are not native duplicates. The record denotes an unlabeled-data scoring algorithm, not an individual score, probability, trained checkpoint or generic neighbor method. The original full text supports tie-inclusive neighborhoods and reciprocal-mean reachability ratios. Earlier OPTICS-OF identity remains explicitly unresolved rather than asserted equivalent.

### Related UnsupervisedLearning task association

grounding: supported. Targets: AIMech:LocalOutlierFactor.

The related mapping is supported without equivalence or subclassing.

LOF infers neighborhood-relative outlier scores from unlabeled observations, giving a related algorithm-to-task association with AIO:UnsupervisedLearning. The target is a MachineLearningTask; this link is neither exact equivalence nor a subclass assertion. The core score does not itself assign two classes, so BinaryClassification and its supervised ancestry are not selected. Clustering and OPTICS/DBSCAN organize clusters or reachability orderings, whereas LOF does not require a partition. All three AIO KnearestNeighbor classes specify label voting or response averaging, not local reachability ratios; RegressionAnalysis requires dependent/independent-variable relationships. DimensionalityReduction, DataPreparation and SelectionAndSamplingBias do not identify this scoring procedure. Native neighbor-ratio and distance-norm domain descriptions, PDD, supervised metric learning and density clustering have different outputs or neighborhood rules.

### tie inclusive locality

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

For n reference observations and 1&lt;=k&lt;=n-1, k-distance(p) is the kth ordered distance to other observations, excluding p itself. N_k(p) contains every other observation whose distance is at most that boundary, including all ties, so its size can exceed k. The reference dataset and dissimilarity define locality; the procedure does not require labeled normal/outlier examples or an explicit clustering. Locators: Section 4, Definitions 3-4, printed/PDF p3; Section 1, p1

### reachability density ratio

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

Define reach_k(p,o)=max(k-distance(o),d(p,o)), using the neighbor o's radius, not p's. Reachability is generally asymmetric. Local reachability density lrd_k(p) is the reciprocal of the mean reachability over o in N_k(p), and LOF_k(p) is the mean of lrd_k(o)/lrd_k(p) over that same neighborhood. These formulas require nonempty neighborhoods and positive finite mean reaches for the densities used. Reachability density has inverse-distance units; it is not a normalized probability density. LOF is a dimensionless relative score. Locators: Definitions 5-7, printed/PDF pp3-4

### relative score not probability

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

A large score indicates lower reachability density relative to neighbors; it is neither an outlier probability nor a universal decision threshold. The paper's near-one bound assumes a closed two-hop neighborhood and bounded positive reachability variation. Scores can be below one: for D={0,1,3} under absolute distance and k=2, the scores are {11/12,6/5,11/12}. At k=1 they are {1,1,2}, reversing the center-versus-endpoint ordering. Two arbitrarily separated observations both score one at k=1; absolute isolation alone is not enough. These examples are exact curator calculations. Locators: Definition 7 and Lemma 1, printed/PDF p4; Sections 5-6, pp4-8; research/discovery/local-outlier-factor-boundaries.py

### ties zeros and scale

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

Boundary ties are part of the original definition: D={0,2,4,5}, k=1 gives point 2 score 3/2 when both equidistant neighbors are retained, but score 1 if an exact-k implementation chooses only neighbor 0. Coincident observations can give zero mean reachability and undefined density ratios; the paper assumes no duplicates and mentions a distinct-coordinate alternative without making an additive regularizer part of core LOF. Multiplying every distance by a positive constant leaves the unregularized core score unchanged when defined; feature-specific rescaling can change neighborhoods and scores. For D={0,1,3}, k=2, reach(0,1)=2 exceeds d(0,1)=1, so the paper's informal k=2 raw-distance reduction is not generally implied by its self-excluded definitions. Locators: Definitions 3-7 and duplicate discussion, printed/PDF pp3-4; Section 6, p7; exact curator calculations in research/discovery/local-outlier-factor-boundaries.py

### neighborhood scale selection

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

Scores can vary nonmonotonically with k. The paper suggests choosing a lower and upper neighborhood size and ranking each point by its maximum LOF over that range; this is an optional multiscale ranking heuristic, distinct from a fixed-k score. Suggested lower bounds near 10 and common choices around 10-20 are empirical guidance, not mathematical validity constraints or universally optimal defaults. Small groups can appear ordinary relative to one another at some scales, so the chosen range affects which deviations are exposed. Locators: Section 6 and Figures 7-8, printed/PDF pp7-9

### versioned implementation conventions

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

The inspected scikit-learn 1.7.2-linked implementation uses a fixed neighbor count, excludes the indexed query for fitted training scores, and adds 1e-10 to mean reachability before inversion. It exposes negative LOF as negative_outlier_factor_; auto contamination chooses offset -1.5, while supplied contamination chooses a training-score percentile and labels scores strictly below it. These are implementation choices, not the paper's all-ties and unregularized definition or a universally validated 1.5 cutoff. Ties can prevent an exact requested outlier fraction. A fixed additive epsilon also prevents automatically transferring exact uniform-scale invariance. Locators: Definitions 3-7, printed/PDF pp3-4; soccer illustration and Table 3, p10; exact fixed-epsilon curator calculation; LocalOutlierFactor.fit, _predict and _local_reachability_density; KNeighborsMixin._kneighbors_reduce_func and kneighbors, including query_is_train and final fixed-shape self-removal

### novelty query distinction

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

With novelty=True, the inspected implementation scores new queries against stored training-neighbor radii and training densities; it does not insert the new query batch into reference neighborhoods. Supplying training points through score_samples can include each query itself as a neighbor, unlike the fitted training-score calculation. Novelty-query scores therefore need not equal negative_outlier_factor_ on the training set. This source-scoped extension does not redefine the original dataset-level score, and no library runtime or historical-code equivalence was tested. Locators: Definitions 3-7, printed/PDF pp3-4; LocalOutlierFactor.score_samples, decision_function and their novelty docstrings; KNeighborsMixin.kneighbors: X is None training branch versus explicit-query branch

### computation and evaluation scope

evidence: supported. Targets: AIMech:LocalOutlierFactor.

Supported within the explicit source and parameter scope.

After neighborhoods are available, computing densities and scores visits the retained neighbor incidences for each chosen k. Original all-boundary-ties neighborhoods can contain n-1 observations even for small k, so O(n*k) storage or linear score work requires a bounded-neighborhood assumption. All-pairs search can require quadratic distance evaluations; index performance depends on data and dimension. The paper's synthetic, sports and color-histogram examples and historical wall-clock timings are conditional demonstrations, not universal accuracy or speed guarantees. The sports results use selected features and neighborhood ranges with domain interpretation, not held-out probability calibration. No numerical performance advantage is curated. Locators: Sections 7.1-7.3, Figures 9-11 and Table 3, printed/PDF pp9-11; Definition 4, p3

### Core equations and misleading boundary interpretations

consistency: supported. Targets: AIMech:LocalOutlierFactor.

The final record retains the defining conventions and concrete counterexamples.

The radius belongs to neighbor o, reachability is asymmetric, and the density is the reciprocal of a mean before neighbor/query ratios are averaged. The3-point examples verify below-one scores and changed rankings; the4-point tie example verifies3/2 versus1. Positive scaling cancels in unregularized ratios but not after a fixed additive epsilon. Duplicate zero means are not silently regularized. k must be at most n-1 under explicit self exclusion; printed theorem endpoints and self-inclusive partition wording do not replace Definitions3-7. A valid k2 example refutes the informal reduction to raw distance. None of these calculations establishes statistical calibration.

### Original definition versus pinned library behavior

consistency: supported. Targets: AIMech:LocalOutlierFactor.

The source-specific software discussion does not alter the mathematical identity.

Inspected code requests exactly k neighbors and removes self only when queries are omitted; duplicate tie handling still preserves fixed count. It adds1e-10 before inversion, negates scores, uses auto offset-1.5 or a percentile, and compares strictly. Tied scores can defeat exact fraction claims. Novelty queries use stored reference density/radii; explicitly querying training points can include self. No claim of historical implementation equivalence, backend audit, newest release or executed library behavior is made.

### Heuristics, experiments and neighbor incidence

evidence: supported. Targets: AIMech:LocalOutlierFactor.

No unsupported numerical superiority or universal complexity is asserted.

Max-over-k is optional and parameter dependence can be nonmonotonic. Suggested scales are empirical guidance. All-ties incidence may grow quadratically; index timings depend on dimension and data. Sports examples use chosen features and subjective interpretation, and color/synthetic examples do not prove general accuracy or calibrated probabilities. No performance claim requiring an invented evaluation context is present.

### Every target field and exact inspected source versions

provenance: supported. Targets: AIMech:LocalOutlierFactor.

All fields were reread after canonical input capture.

Source IDs, titles, authors, DOI, exact URLs, downloaded hashes and actual access times match inspected bytes. Printed/PDF pagination is explicit. All12 primary pages and the complete pinned LOF module were read; only relevant neighbor-search methods were fully reviewed in the larger module. Actual write provenance and history are retained. All442 generated AIO records remain unchanged. Record stays DRAFT;20 context YAMLs inform boundaries without renewed scientific approval, and440 pending cohorts plus partial work remain.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T085323Z-local-outlier-factor.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 511 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches of both checkouts included ignored and hidden files, LOF, expanded names and both publication DOIs: 16 worktree and 17 main matches, comprising 13 distinct context windows at 33 locations, were read. They are pending discovery context and an unrelated BASIC-language LOF token in an ignored Pygments lexer. Semantic searches inspected 99 AIO name/synonym/definition rows and 70 native name/definition matches, reusing 85 and 67 unchanged previously read rows respectively. Thirteen annotated AIO CLASS nodes with outgoing edges and twenty contextual YAMLs were inspected or reused after unchanged-byte checks. This is a bounded corpus assessment, not absence from all ontologies. |
| mapping | sources/aio/aio.json; Thirteen annotated CLASS nodes/outgoing edges and twenty contextual YAMLs | supports | LOF infers neighborhood-relative outlier scores from unlabeled observations, giving a related algorithm-to-task association with AIO:UnsupervisedLearning. The target is a MachineLearningTask; this link is neither exact equivalence nor a subclass assertion. The core score does not itself assign two classes, so BinaryClassification and its supervised ancestry are not selected. Clustering and OPTICS/DBSCAN organize clusters or reachability orderings, whereas LOF does not require a partition. All three AIO KnearestNeighbor classes specify label voting or response averaging, not local reachability ratios; RegressionAnalysis requires dependent/independent-variable relationships. DimensionalityReduction, DataPreparation and SelectionAndSamplingBias do not identify this scoring procedure. Native neighbor-ratio and distance-norm domain descriptions, PDD, supervised metric learning and density clustering have different outputs or neighborhood rules. |
| finite-boundaries | research/discovery/local-outlier-factor-boundaries.py; Exact self-exclusion, tie, reachability, score, zero-distance, neighborhood-size and scaling calculations | supports | Exact rational calculations verify oriented neighbor-radius reachability, non-rawk2 reaches, below-one values, changing rankings, uniform scaling, isolated-pair scores, all-ties versus exact-k differences, zero-reach undefinedness, nonmonotonic k dependence and fixed-epsilon loss of exact scale invariance. This is a transparent definition check, not historical or modern library execution or a benchmark. |
| breunig2000 | https://cse.hkust.edu.hk/~raywong/comp5331/References/LOFIdentifyingDensityBasedLocalOutliers.pdf; Definitions3-7 and Lemma1, printed/PDFpp3-4; theorem and parameter discussionpp5-8; Figures7-11/Table3 and computational discussionpp8-11; all12 pages read. | supports | LOF: Identifying Density-Based Local Outliers. SIGMOD 2000 method; exact university-hosted 12-page author-layout PDF, all pages visually read. Printed pages 1-12 coincide with PDF pages; no offset to proceedings pages 93-104 is inferred. |
| sklearn-lof | https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_lof.py; Entire _lof.py: fit, _predict, score_samples, decision_function and _local_reachability_density, with parameter/novelty docstrings. | supports | scikit-learn LocalOutlierFactor implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. Entire _lof.py read; no execution. |
| sklearn-neighbors | https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_base.py; KNeighborsMixin._kneighbors_reduce_func and entire kneighbors, including fixed-count selection and self-removal. | supports | scikit-learn KNeighborsMixin implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func and kneighbors fully read; remaining module and backend implementations not fully audited. |

## Limits And Additional Notes

- Adversarial author self-review only; the record remains DRAFT.
- All12 primary PDF pages were visually read; printed1-12 pagination is used without an inferred proceedings offset. Complete pinned _lof.py and relevant KNeighborsMixin methods were read; remaining backend code and library runtime were not audited.
- Original LOF is self-excluded, tie-inclusive and unregularized. Source theorem endpoints/partition wording and informal k2 simplification are not allowed to override the explicit core definitions. Exact rational examples support the stated qualifications.
- Relative density scores are not probabilities or universal binary labels. Optional max-over-k aggregation, heuristic parameter guidance and modern novelty-query/threshold conventions are separated from the fixed-k core.
- No numerical performance advantage is curated. Historical sports, synthetic, image and runtime demonstrations do not establish universal accuracy, calibration or complexity. All-ties incidence can be quadratic.
- The HKUST public primary copy supplied full text after legacy links, redirects and timeouts failed. No access control was bypassed. No full PDF or library implementation is redistributed; exact curator calculations are maintained separately.
- One native DRAFT addition brings the collection to512; all442 generated AIO records are unchanged. Three pending source cohorts and the retained partial LOF cohort leave440 pending cohorts, so discovery remains incomplete.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T085859Z-local-outlier-factor
kind: record
repository: CultureBotAI/AIMech
title: Scientific self-review of local outlier factor
started_at: '2026-10-12T08:53:36Z'
finished_at: '2026-10-12T08:58:59Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all12 primary PDF pages and pinned
    official code, reread every final-record field after canonical inspection, checked
    ignored-inclusive identities and annotated AIO mapping context, and challenged
    score/tie/scale/zero-distance conventions with exact rational calculations. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain original LOF with self exclusion, all boundary ties, oriented reachability
  and unregularized relative density ratios. Optional scale aggregation and versioned
  software thresholds, epsilon and novelty scoring remain distinct. No actionable
  defect in the final record was found.
source:
  git_revision: c0052b03296cd8fd4476edd13927f91144d59e9e
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
    sha256: 559b99ff18a857ee7f928bce57795798047d9c870acc1c1275b191f7c5b1b670
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
  - path: data/curated/PrototypeBasedDomainDescription.yaml
    sha256: 3b4fce38fde950f9edc3bbef8cbfde5fa8e1d8075eb98a758eb89abd3ca69874
    role: context
  - path: research/discovery/20261012T085323Z-local-outlier-factor.json
    sha256: f72fa6b1b1f07b3f2a8910689778d0a6dd337c179c4c94dc41a489d849b2e1a8
    role: context
  - path: research/discovery/local-outlier-factor-boundaries.py
    sha256: 94310e4d5dc70233224a77259936ba6bd80411af504610023cc4131b51bba131
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
  description: Every field of the single maintained LOF record.
  selection: Exact maintained ID AIMech:LocalOutlierFactor, without sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:LocalOutlierFactor
  exclusions:
  - target: Twenty contextual AIO/native records
    reason: Identity and mapping context only, not renewed scientific approval.
  - target: Earlier OPTICS-OF and other local-density methods
    reason: Full identity and method comparison remains on the frontier.
  - target: Library runtime, backend implementations and historical benchmarks
    reason: Source reading and finite definition calculations only.
  - target: Generated website
    reason: Freshness/validity checks, without separate visual-design review.
  - target: Remaining discovery frontier
    reason: 440 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 149.66s (0:02:29)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 512 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 157 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 153,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
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
  - AIMech:LocalOutlierFactor
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact LOF boundary calculations
  command: python3 research/discovery/local-outlier-factor-boundaries.py
  status: passed
  required: true
  target_ids:
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
  reference: research/discovery/20261012T085323Z-local-outlier-factor.json
  accessed_at: '2026-10-12T08:53:36Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 511
    preceding native IDs, names and aliases. No normalized identity collision was
    found. Fixed-string whole-word searches of both checkouts included ignored and
    hidden files, LOF, expanded names and both publication DOIs: 16 worktree and 17
    main matches, comprising 13 distinct context windows at 33 locations, were read.
    They are pending discovery context and an unrelated BASIC-language LOF token in
    an ignored Pygments lexer. Semantic searches inspected 99 AIO name/synonym/definition
    rows and 70 native name/definition matches, reusing 85 and 67 unchanged previously
    read rows respectively. Thirteen annotated AIO CLASS nodes with outgoing edges
    and twenty contextual YAMLs were inspected or reused after unchanged-byte checks.
    This is a bounded corpus assessment, not absence from all ontologies.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Thirteen annotated CLASS nodes/outgoing edges and twenty contextual YAMLs
  accessed_at: '2026-10-12T08:53:36Z'
  support: supports
  summary: LOF infers neighborhood-relative outlier scores from unlabeled observations,
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
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/local-outlier-factor-boundaries.py
  locator: Exact self-exclusion, tie, reachability, score, zero-distance, neighborhood-size
    and scaling calculations
  accessed_at: '2026-10-12T08:53:36Z'
  snapshot_sha256: 94310e4d5dc70233224a77259936ba6bd80411af504610023cc4131b51bba131
  support: supports
  summary: Exact rational calculations verify oriented neighbor-radius reachability,
    non-rawk2 reaches, below-one values, changing rankings, uniform scaling, isolated-pair
    scores, all-ties versus exact-k differences, zero-reach undefinedness, nonmonotonic
    k dependence and fixed-epsilon loss of exact scale invariance. This is a transparent
    definition check, not historical or modern library execution or a benchmark.
- evidence_id: breunig2000
  kind: primary_source
  reference: https://cse.hkust.edu.hk/~raywong/comp5331/References/LOFIdentifyingDensityBasedLocalOutliers.pdf
  locator: Definitions3-7 and Lemma1, printed/PDFpp3-4; theorem and parameter discussionpp5-8;
    Figures7-11/Table3 and computational discussionpp8-11; all12 pages read.
  accessed_at: '2026-10-12T08:37:29Z'
  snapshot_sha256: d6e378582bf7a0f6f9e34e2b11b0b4e7bc9016b4f20e5bc041760f6bb57cb566
  support: supports
  summary: 'LOF: Identifying Density-Based Local Outliers. SIGMOD 2000 method; exact
    university-hosted 12-page author-layout PDF, all pages visually read. Printed
    pages 1-12 coincide with PDF pages; no offset to proceedings pages 93-104 is inferred.'
- evidence_id: sklearn-lof
  kind: primary_source
  reference: https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_lof.py
  locator: 'Entire _lof.py: fit, _predict, score_samples, decision_function and _local_reachability_density,
    with parameter/novelty docstrings.'
  accessed_at: '2026-10-12T08:42:45Z'
  snapshot_sha256: a05774d4db7d6ded41374f68b1b678c5f672d1e8454cddea9ebe7841aa4b4e63
  support: supports
  summary: scikit-learn LocalOutlierFactor implementation. Immutable source commit
    1eb422d6c5f46a98a318f341de3e4709f9521bfe linked by scikit-learn 1.7.2 API documentation.
    Entire _lof.py read; no execution.
- evidence_id: sklearn-neighbors
  kind: primary_source
  reference: https://raw.githubusercontent.com/scikit-learn/scikit-learn/1eb422d6c5f46a98a318f341de3e4709f9521bfe/sklearn/neighbors/_base.py
  locator: KNeighborsMixin._kneighbors_reduce_func and entire kneighbors, including
    fixed-count selection and self-removal.
  accessed_at: '2026-10-12T08:47:20Z'
  snapshot_sha256: 6686ee9f3f36ae7ab9b572a90931e689345e8d5ab6b1879361fb2ea15990d9e5
  support: supports
  summary: scikit-learn KNeighborsMixin implementation. Immutable source commit 1eb422d6c5f46a98a318f341de3e4709f9521bfe
    linked by scikit-learn 1.7.2 API documentation. KNeighborsMixin._kneighbors_reduce_func
    and kneighbors fully read; remaining module and backend implementations not fully
    audited.
assessments:
- assessment_id: identity-and-definition
  area: identity
  topic: Original fixed-k LOF identity and algorithm scope
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - identity
  - breunig2000
  summary: Retain the supported native DRAFT algorithm.
  details: All labels, aliases, scoped synonyms and record identities were checked.
    Both ignored-inclusive checkout searches were read in13 distinct windows at33
    locations; pending leads and BASIC LOF are not native duplicates. The record denotes
    an unlabeled-data scoring algorithm, not an individual score, probability, trained
    checkpoint or generic neighbor method. The original full text supports tie-inclusive
    neighborhoods and reciprocal-mean reachability ratios. Earlier OPTICS-OF identity
    remains explicitly unresolved rather than asserted equivalent.
- assessment_id: mapping-direction
  area: grounding
  topic: Related UnsupervisedLearning task association
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - mapping
  - breunig2000
  summary: The related mapping is supported without equivalence or subclassing.
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
- assessment_id: claim-tie-inclusive-locality
  area: evidence
  topic: tie inclusive locality
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the explicit source and parameter scope.
  details: 'For n reference observations and 1<=k<=n-1, k-distance(p) is the kth ordered
    distance to other observations, excluding p itself. N_k(p) contains every other
    observation whose distance is at most that boundary, including all ties, so its
    size can exceed k. The reference dataset and dissimilarity define locality; the
    procedure does not require labeled normal/outlier examples or an explicit clustering.
    Locators: Section 4, Definitions 3-4, printed/PDF p3; Section 1, p1'
- assessment_id: claim-reachability-density-ratio
  area: evidence
  topic: reachability density ratio
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the explicit source and parameter scope.
  details: 'Define reach_k(p,o)=max(k-distance(o),d(p,o)), using the neighbor o''s
    radius, not p''s. Reachability is generally asymmetric. Local reachability density
    lrd_k(p) is the reciprocal of the mean reachability over o in N_k(p), and LOF_k(p)
    is the mean of lrd_k(o)/lrd_k(p) over that same neighborhood. These formulas require
    nonempty neighborhoods and positive finite mean reaches for the densities used.
    Reachability density has inverse-distance units; it is not a normalized probability
    density. LOF is a dimensionless relative score. Locators: Definitions 5-7, printed/PDF
    pp3-4'
- assessment_id: claim-relative-score-not-probability
  area: evidence
  topic: relative score not probability
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - finite-boundaries
  summary: Supported within the explicit source and parameter scope.
  details: 'A large score indicates lower reachability density relative to neighbors;
    it is neither an outlier probability nor a universal decision threshold. The paper''s
    near-one bound assumes a closed two-hop neighborhood and bounded positive reachability
    variation. Scores can be below one: for D={0,1,3} under absolute distance and
    k=2, the scores are {11/12,6/5,11/12}. At k=1 they are {1,1,2}, reversing the
    center-versus-endpoint ordering. Two arbitrarily separated observations both score
    one at k=1; absolute isolation alone is not enough. These examples are exact curator
    calculations. Locators: Definition 7 and Lemma 1, printed/PDF p4; Sections 5-6,
    pp4-8; research/discovery/local-outlier-factor-boundaries.py'
- assessment_id: claim-ties-zeros-and-scale
  area: evidence
  topic: ties zeros and scale
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - finite-boundaries
  summary: Supported within the explicit source and parameter scope.
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
- assessment_id: claim-neighborhood-scale-selection
  area: evidence
  topic: neighborhood scale selection
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - finite-boundaries
  summary: Supported within the explicit source and parameter scope.
  details: 'Scores can vary nonmonotonically with k. The paper suggests choosing a
    lower and upper neighborhood size and ranking each point by its maximum LOF over
    that range; this is an optional multiscale ranking heuristic, distinct from a
    fixed-k score. Suggested lower bounds near 10 and common choices around 10-20
    are empirical guidance, not mathematical validity constraints or universally optimal
    defaults. Small groups can appear ordinary relative to one another at some scales,
    so the chosen range affects which deviations are exposed. Locators: Section 6
    and Figures 7-8, printed/PDF pp7-9'
- assessment_id: claim-versioned-implementation-conventions
  area: evidence
  topic: versioned implementation conventions
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  - finite-boundaries
  summary: Supported within the explicit source and parameter scope.
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
- assessment_id: claim-novelty-query-distinction
  area: evidence
  topic: novelty query distinction
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  summary: Supported within the explicit source and parameter scope.
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
- assessment_id: claim-computation-and-evaluation-scope
  area: evidence
  topic: computation and evaluation scope
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  summary: Supported within the explicit source and parameter scope.
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
- assessment_id: adversarial-formula-check
  area: consistency
  topic: Core equations and misleading boundary interpretations
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - finite-boundaries
  summary: The final record retains the defining conventions and concrete counterexamples.
  details: The radius belongs to neighbor o, reachability is asymmetric, and the density
    is the reciprocal of a mean before neighbor/query ratios are averaged. The3-point
    examples verify below-one scores and changed rankings; the4-point tie example
    verifies3/2 versus1. Positive scaling cancels in unregularized ratios but not
    after a fixed additive epsilon. Duplicate zero means are not silently regularized.
    k must be at most n-1 under explicit self exclusion; printed theorem endpoints
    and self-inclusive partition wording do not replace Definitions3-7. A valid k2
    example refutes the informal reduction to raw distance. None of these calculations
    establishes statistical calibration.
- assessment_id: implementation-separation
  area: consistency
  topic: Original definition versus pinned library behavior
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  - finite-boundaries
  summary: The source-specific software discussion does not alter the mathematical
    identity.
  details: Inspected code requests exactly k neighbors and removes self only when
    queries are omitted; duplicate tie handling still preserves fixed count. It adds1e-10
    before inversion, negates scores, uses auto offset-1.5 or a percentile, and compares
    strictly. Tied scores can defeat exact fraction claims. Novelty queries use stored
    reference density/radii; explicitly querying training points can include self.
    No claim of historical implementation equivalence, backend audit, newest release
    or executed library behavior is made.
- assessment_id: empirical-and-computational-scope
  area: evidence
  topic: Heuristics, experiments and neighbor incidence
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - breunig2000
  - finite-boundaries
  summary: No unsupported numerical superiority or universal complexity is asserted.
  details: Max-over-k is optional and parameter dependence can be nonmonotonic. Suggested
    scales are empirical guidance. All-ties incidence may grow quadratically; index
    timings depend on dimension and data. Sports examples use chosen features and
    subjective interpretation, and color/synthetic examples do not prove general accuracy
    or calibrated probabilities. No performance claim requiring an invented evaluation
    context is present.
- assessment_id: provenance-and-completeness
  area: provenance
  topic: Every target field and exact inspected source versions
  outcome: supported
  target_ids:
  - AIMech:LocalOutlierFactor
  evidence_ids:
  - identity
  - mapping
  - breunig2000
  - sklearn-lof
  - sklearn-neighbors
  summary: All fields were reread after canonical input capture.
  details: Source IDs, titles, authors, DOI, exact URLs, downloaded hashes and actual
    access times match inspected bytes. Printed/PDF pagination is explicit. All12
    primary pages and the complete pinned LOF module were read; only relevant neighbor-search
    methods were fully reviewed in the larger module. Actual write provenance and
    history are retained. All442 generated AIO records remain unchanged. Record stays
    DRAFT;20 context YAMLs inform boundaries without renewed scientific approval,
    and440 pending cohorts plus partial work remain.
findings: []
actions: []
limitations:
- Adversarial author self-review only; the record remains DRAFT.
- All12 primary PDF pages were visually read; printed1-12 pagination is used without
  an inferred proceedings offset. Complete pinned _lof.py and relevant KNeighborsMixin
  methods were read; remaining backend code and library runtime were not audited.
- Original LOF is self-excluded, tie-inclusive and unregularized. Source theorem endpoints/partition
  wording and informal k2 simplification are not allowed to override the explicit
  core definitions. Exact rational examples support the stated qualifications.
- Relative density scores are not probabilities or universal binary labels. Optional
  max-over-k aggregation, heuristic parameter guidance and modern novelty-query/threshold
  conventions are separated from the fixed-k core.
- No numerical performance advantage is curated. Historical sports, synthetic, image
  and runtime demonstrations do not establish universal accuracy, calibration or complexity.
  All-ties incidence can be quadratic.
- The HKUST public primary copy supplied full text after legacy links, redirects and
  timeouts failed. No access control was bypassed. No full PDF or library implementation
  is redistributed; exact curator calculations are maintained separately.
- One native DRAFT addition brings the collection to512; all442 generated AIO records
  are unchanged. Three pending source cohorts and the retained partial LOF cohort
  leave440 pending cohorts, so discovery remains incomplete.
links: []
tags:
- native-concepts
- local-outlier-factor
- self-review
- discovery-ongoing
```
