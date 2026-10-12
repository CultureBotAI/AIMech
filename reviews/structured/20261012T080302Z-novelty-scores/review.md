# Scientific self-review of nearest-neighbor ratio and bootstrap-instability novelty detection

- Review: 20261012T080302Z-novelty-scores
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T07:58:05Z
- Finished UTC: 2026-10-12T08:03:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two distinct novelty-detection procedures with related AIO binary-decision mappings. All selected fields are supported with explicit source ambiguities and limits; no actionable final-record defect was found.

## Scope And Provenance

Every field of the two explicitly selected novelty-detection algorithms.

Selection: Exact maintained IDs AIMech:NearestNeighborRatioDataDescription and AIMech:BootstrapClassifierInstabilityNoveltyDetection, without sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 13fd55f549c54fa96b93d66020e2d61d71db3379.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NearestNeighborRatioDataDescription | data/curated/NearestNeighborRatioDataDescription.yaml | maintained | Nearest-neighbor ratio data description |
| AIMech:BootstrapClassifierInstabilityNoveltyDetection | data/curated/BootstrapClassifierInstabilityNoveltyDetection.yaml | maintained | Bootstrap classifier-instability novelty detection |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 144.87s (0:02:24)<br>Checked 442 record(s); 0 failed.<br>Checked 506 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 154 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 150,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection | Exited0 without output. |
| Exact novelty-score boundary calculations | passed | True | AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection | {"status": "passed", "nearest_tie_scores": ["10", "1/2"], "nearest_selection_differs_from_union_of_balls": true, "duplicate_ratio": "undefined 0/0", "singleton_has_no_other_neighbor": true, "distinct_training_ratios": "all zero", "bootstrap_variance": "1/4", "stable_outputs_variance": "0", "variance_threshold": "11/64", "standard_deviation_threshold": "1/2", "doubled_output_variance_threshold": "5/4", "interpretation": "Exact score-level counterexamples expose unspecified conventions and distinguish the source threshold formulas; no source policy is invented and no trained model is evaluated."} |

## Scientific And Domain Assessments

### Definition, identity and mapping scope

identity: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

Retain the distinct native DRAFT novelty-detection procedure with a related binary-decision task mapping.

This is the local distance-ratio detector described in Tax-Duin1998 Equation3 and Tax-Duin2000 Equations4-6. The 2000 paper studies a unit threshold and threshold sweeps; the 1998 paper uses a different, incompletely specified calibration convention. The core score is shared, but the complete experimental protocols are not asserted identical. The denominator concerns the selected reference point's own nearest other reference, not necessarily the query's second-nearest point. This method does not vote among class labels, average regression values, learn a supervised distance matrix, label density-connected components or optimize an enclosing sphere. Generic NN-d and NNDD acronyms are searched but not assigned as unique aliases. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 12 matching lines per checkout, eight distinct texts at 24 locations, were inspected as queries, bibliographic notes and pending leads in the preceding discovery ledger. A fresh semantic AIO search returned 65 label/synonym/definition rows, all read; eleven annotated class nodes and outgoing edges and eighteen contextual YAMLs were read or reused after unchanged-byte checks. A wider native neighbor search inspected names and definitions only. Absence is bounded to this pin and inspected corpus. A target-class data-description algorithm that scores a query by its distance to a nearest reference observation divided by that observation's nearest-other-reference spacing, and accepts queries whose ratio does not exceed a chosen threshold, where the denominator and neighbor-selection conventions are well defined.

### local spacing score

evidence: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

Supported within the explicitly stated assumptions and limitations.

For a reference set with at least two observations, select i minimizing &#124;&#124;x-x_i&#124;&#124;_2 and another reference j!=i minimizing &#124;&#124;x_i-x_j&#124;&#124;_2. When d2=&#124;&#124;x_i-x_j&#124;&#124;_2 is positive, use rho(x)=&#124;&#124;x-x_i&#124;&#124;_2/d2. The 2000 default accepts rho&lt;=1; increasing the threshold expands acceptance for a fixed reference set and neighbor-selection rule. The score uses Euclidean distances, not their squares, and the density motivation does not make rho a normalized probability or an outlier posterior. Source locators: tax2000: Section 2.2, printed p.673 / PDF p.2, Equations 3-6 and threshold paragraph; tax1998: Section 2.1, PDF pp.2-3, Equation 3

### duplicates ties and region

evidence: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

Supported within the explicitly stated assumptions and limitations.

The denominator requires excluding the selected reference observation itself. Duplicate coordinates can still make d2=0, including an undefined 0/0 for a matching query; a singleton reference set has no other neighbor. The sources do not specify a general duplicate or nearest-tie policy. Ties can affect the decision: for references {-1/10,0,2} and query 1, choosing 0 gives ratio 10 while choosing 2 gives 1/2. The nearest-selected rule is also not generally the union of all reference-centered balls with radii equal to local spacing: query 9/10 in the same example is rejected at unit threshold although it lies inside the radius-2 ball centered at 2. These are exact curator calculations, not repairs attributed to the papers. Source locators: tax2000: Section 2.2, printed p.673 / PDF p.2, Equations 4-6; curator examples in research/discovery/novelty-score-boundaries.py; tax1998: Section 2.1, PDF pp.2-3, Equation 3

### coverage and calibration

evidence: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

Supported within the explicitly stated assumptions and limitations.

With distinct reference coordinates and queries evaluated against the full reference set, each training point has ratio zero and is accepted at a nonnegative threshold. This does not guarantee acceptance of all future target observations, minimum-volume support estimation or a calibrated false-alarm rate. The 1998 calibration text says three standard deviations above the training-score mean, while its displayed Equation6 uses three times var. Its nonzero training-ratio histogram also requires a scoring convention beyond naive self-including resubstitution; the exact exclusion protocol is not established here. These settings are not silently substituted for the 2000 unit-threshold rule. Source locators: tax2000: Sections 2.2 and 5, printed pp.673 and 675 / PDF pp.2 and 4; curator training-query qualification; tax1998: Section 2.2 and experimental protocol, PDF pp.3-4, Equation 6 and Figure 1

### evidence and noise scope

evidence: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

Supported within the explicitly stated assumptions and limitations.

The rule depends on individual reference locations, feature scaling and threshold choice, and is sensitive to noise and sparse internal regions. The 2000 study compares synthetic uniform, Gaussian, heavy-tailed and embedded low-variance settings, with target-coverage versus outlier-acceptance tradeoffs. Its pump example uses 96 training objects with 64 autoregressive features and compares reduced representations and other detectors. The 1998 digit study reports poor nearest-neighbor results in many settings and includes training observations in its normal test population. Neither source establishes universal small-sample or high-dimensional superiority; no numerical performance claim or minimum-volume theorem is inferred from their summaries. Source locators: tax2000: Introduction and Sections 3-5, printed pp.672-675 / PDF pp.1-4, Figures 1-5; tax1998: Sections 3-4, PDF pp.4-8, Figures 1-3

### Definition, identity and mapping scope

identity: supported. Targets: AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Retain the distinct native DRAFT novelty-detection procedure with a related binary-decision task mapping.

This is the Tax-Duin1998 instability-based detector. Its novelty signal is variability of classifier outputs across bootstrap training sets, not the mean prediction used for ordinary bagging, nearest-neighbor spacing, a density estimate, vote entropy or a Bayesian posterior uncertainty. The published experiment uses labels among normal digit classes to train its base classifiers; target-versus-abnormal detection does not imply that the entire fitting procedure is label-free. The source's threshold notation is ambiguous, so the record preserves the procedure and that uncertainty rather than declaring an exact executable reference implementation. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 12 matching lines per checkout, eight distinct texts at 24 locations, were inspected as queries, bibliographic notes and pending leads in the preceding discovery ledger. A fresh semantic AIO search returned 65 label/synonym/definition rows, all read; eleven annotated class nodes and outgoing edges and eighteen contextual YAMLs were read or reused after unchanged-byte checks. A wider native neighbor search inspected names and definitions only. Absence is bounded to this pin and inspected corpus. A novelty-detection procedure that trains classifiers on bootstrap resamples of reference data, estimates the variance of their outputs at a query, and rejects queries with unusually high variability relative to a chosen reference-score threshold.

### bootstrap output variance

evidence: supported. Targets: AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Supported within the explicitly stated assumptions and limitations.

Draw bootstrap training sets of the original reference-set size, fit the chosen classifier to each, and compare their output values at the same query. The source defines rho(x)=E_b[out_b(x)^2]-(E_b[out_b(x)])^2, where the expectation is over bootstrap fits. Repeated fitted outputs estimate this variance; a large score indicates sensitivity to the sampled training set. It is not itself the probability that the query is novel. Base learner, output scaling, resampling and finite-ensemble variance-estimation conventions affect the result. Source locators: tax1998: Section 2.1, PDF p.3, Equation 4 and bootstrap paragraph

### published multiclass configuration

evidence: supported. Targets: AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Supported within the explicitly stated assumptions and limitations.

The digit experiment uses a linear classifier based on Fisher's criterion, with a normalized sigmoid of distance to its decision boundary as output. It fits one-versus-rest classifiers for nine retained digit classes, produces 25 bootstrap classifier sets and averages output variances over the nine class outputs to obtain one novelty score. The withheld tenth digit class supplies abnormal examples for evaluation. These counts and learner choices describe that experiment, not fixed requirements for every use of the variance-gating procedure. Source locators: tax1998: Section 3, PDF pp.3-4, feature, class-split and classifier paragraphs

### threshold ambiguity

evidence: supported. Targets: AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Supported within the explicitly stated assumptions and limitations.

Section2.2 motivates a threshold at the reference-score mean plus three standard deviations under a rough Gaussian-score assumption, but Equation6 writes mean plus three times var. These are different numerical rules unless var is being used for a different convention; the paper does not resolve that notation here. For reference scores {0,1/4}, the two thresholds are 1/2 and 11/64 respectively, so a query score of 1/4 receives different decisions. Doubling all classifier outputs multiplies variance scores by four; the literal mean-plus-three-variance threshold does not generally scale in the same way. The record does not select a hidden implementation convention or infer an exact false-alarm probability. Source locators: tax1998: Section 2.2, PDF p.3, prose and Equation 6; curator exact score calculations in research/discovery/novelty-score-boundaries.py

### stable outliers and evaluation

evidence: supported. Targets: AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Supported within the explicitly stated assumptions and limitations.

Outliers can receive low variance when all bootstrap classifiers extrapolate stably, and difficult normal observations can receive high variance. More bootstrap replicates can improve estimation of a fixed variability signal but do not guarantee that stable outliers acquire a detectable signal. The reported digit comparisons depend on representation and training-set size; the normal evaluation population includes training examples, and rotation-invariant features can make withheld digits indistinguishable from retained ones. The source itself reports stable-region failures and weaker results at larger sample sizes. This supports a bounded instability indicator, not a universal novelty detector or general performance advantage. Source locators: tax1998: Sections 3.1 and 4, PDF pp.5-8, Figures 2-3 and conclusion

### Distance ratio versus bootstrap output variance

consistency: supported. Targets: AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Retain two different novelty scores and fitting procedures.

The nearest-reference score compares a query distance with the selected reference point's own nearest-other spacing. The instability score compares repeated outputs across bootstrap fits. The latter experiment uses normal-class labels and a mean of nine output variances, not a label-free density estimate or ordinary bagging prediction. Sharing a rejection task and a source paper does not make the methods aliases. Generic NN-d and NNDD acronyms are deliberately not unique aliases.

### Reference exclusion, ties and acceptance geometry

consistency: supported. Targets: AIMech:NearestNeighborRatioDataDescription.

The record preserves undefined and convention-dependent cases instead of inventing a historical implementation.

A singleton has no other reference; duplicates can leave a zero denominator after index exclusion. For references {-1/10,0,2}, query1 yields ratios10 or1/2 depending on the nearest tie. Query9/10 is rejected at unit threshold even though it lies in the spacing-radius ball centered at2. Thus the selected-nearest rule is not generally a union of all such balls. Distinct training queries score0 under self-including resubstitution; this establishes neither future target coverage nor minimum volume. The nonzero1998 training histogram indicates a further scoring convention whose precise exclusions are not established.

### Standard deviation versus variance threshold

consistency: supported. Targets: AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection.

Contradictory source notation is explicit and is not silently repaired.

The1998 prose says mean plus three standard deviations but Equation6 writes mean plus three times var. With empirical scores{0,1/4}, the alternatives give1/2 and11/64; query1/4 changes decision. Doubling classifier outputs quadruples the variance score, but the literal mean-plus-three-variance rule is not scale covariant. These calculations use a declared empirical moment convention, not a claim about the unspecified historical variance divisor. The2000 unit threshold and threshold sweeps are kept separate from the1998 calibration.

### Source versions, interpretation and empirical scope

provenance: supported. Targets: AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection.

All thirteen primary PDF pages were read; the records preserve source and evaluation limits.

All four scanned2000 pages and all nine unnumbered1998 manuscript pages were visually inspected, including figures and references. The2000 printed-page offset is671; the1998 PDF is not assigned an inferred proceedings-page offset. The digit experiment includes training observations among normal test examples and representation-induced withheld-class ambiguity. Stable extrapolation can defeat bootstrap novelty detection even with many replicates. The pump and synthetic comparisons depend on representation, sample size and thresholds. No numerical benchmark advantage, probability calibration or universal optimality is asserted. Exact arithmetic is not an implementation reproduction. Contextual records receive no renewed scientific approval;432 pending discovery cohorts remain.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NearestNeighborRatioDataDescription, AIMech:BootstrapClassifierInstabilityNoveltyDetection. Local reference-spacing ratios and bootstrap classifier-output variances use distinct mechanisms and assumptions. Their common novelty-decision task does not establish equivalence. Preserve distinctions from neighbor voting, learned metric transformations, sphere descriptions and prediction averaging.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T075739Z-novelty-scores.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, acronyms and source identifiers. All 12 matching lines per checkout, eight distinct texts at 24 locations, were inspected as queries, bibliographic notes and pending leads in the preceding discovery ledger. A fresh semantic AIO search returned 65 label/synonym/definition rows, all read; eleven annotated class nodes and outgoing edges and eighteen contextual YAMLs were read or reused after unchanged-byte checks. A wider native neighbor search inspected names and definitions only. Absence is bounded to this pin and inspected corpus. |
| mapping | sources/aio/aio.json; Eleven annotated class nodes and outgoing edges, eleven generated YAMLs and seven native neighboring records | supports | The accept-versus-reject output is related to AIO:BinaryClassification. This is a method-to-task association, not an is-a or exact-match assertion. Its Classification parent is under SupervisedLearning; the related mapping does not assert representative training data from the abnormal class. Inspected BinaryClassification, Classification, SupervisedLearning, UnsupervisedLearning, MachineLearningTask, Model, three KnearestNeighbor nodes, EnsembleLearning and UncertaintyBias with their annotations and outgoing edges. The pinned nearest-neighbor nodes specify label plurality or value averaging, not local distance-ratio rejection. EnsembleLearning emphasizes combined prediction, not the particular bootstrap-variance novelty signal, and UncertaintyBias denotes a sampling bias rather than a detector. Generic models and learning tasks do not identify these procedures. Bagging, DBSCAN, OPTICS, NCA, LMNN and both SVDD loss variants supply distinct contextual mechanisms and receive no renewed scientific approval. |
| finite-boundaries | research/discovery/novelty-score-boundaries.py; Exact rational nearest-reference selection, ties, duplicates, training resubstitution and alternative calibration formulas | supports | Exact nearest-neighbor examples show decision-changing ties, undefined duplicate ratios, singleton failure and disagreement with a naive union-of-balls region. Distinct training queries have zero score without guaranteeing future coverage. Bootstrap moment examples distinguish mean-plus-three-variance from mean-plus-three-standard-deviation and show output-scaling dependence. These are curator score-level calculations, not historical experiments. |
| tax2000 | https://rduin.nl/papers/icpr_00_dd.pdf; Introduction and Sections 3-5, printed pp.672-675 / PDF pp.1-4, Figures 1-5; Section 2.2, printed p.673 / PDF p.2, Equations 3-6; Section 2.2, printed p.673 / PDF p.2, Equations 3-6 and threshold paragraph; Section 2.2, printed p.673 / PDF p.2, Equations 4-6; curator examples in research/discovery/novelty-score-boundaries.py; Sections 2.2 and 5, printed pp.673 and 675 / PDF pp.2 and 4; curator training-query qualification | supports | Data Description in Subspaces. ICPR 2000 proceedings, volume 2, printed pp.672-675. Exact author-hosted four-page scan, all pages visually read; PDF-page offset671. Full method, figures, assumptions and evaluation limits inspected; historical experiments were not reproduced. |
| tax1998 | https://rduin.nl/papers/stipr_98_outlier.pdf; Section 2.1, PDF p.3, Equation 4 and bootstrap paragraph; Section 2.1, PDF p.3, Equation 4; Section 2.2 thresholding and Section 3, PDF pp.3-4; Section 2.1, PDF pp.2-3, Equation 3; Section 2.2 and experimental protocol, PDF pp.3-4, Equation 6 and Figure 1; Section 2.2, PDF p.3, prose and Equation 6; curator exact score calculations in research/discovery/novelty-score-boundaries.py; Section 3, PDF pp.3-4, feature, class-split and classifier paragraphs; Sections 3-4, PDF pp.4-8, Figures 1-3; Sections 3.1 and 4, PDF pp.5-8, Figures 2-3 and conclusion | supports | Outlier Detection using Classifier Instability. Exact unnumbered nine-page author-hosted manuscript, all pages visually read. Author bibliography identifies SSPR/SPR1998, LNCS1451:593-601; locators use PDF pages, without asserting identical proceedings pagination. Full method, figures, assumptions and evaluation limits inspected; historical experiments were not reproduced. |

## Limits And Additional Notes

- Adversarial author self-review only; both maintained records remain DRAFT.
- All thirteen primary PDF pages were visually read. The four-page2000 PDF is a scan, with printed offset671; the nine-page1998 author manuscript is unnumbered and cited by PDF page. Neither text extraction alone was treated as full reading.
- The nearest-neighbor score is shared across the two sources, but their calibration protocols differ. The earlier training-score exclusion and variance-versus-standard-deviation threshold notation remain explicit limitations, not invented implementation policies.
- Bootstrap output variability can miss stable outliers and detect difficult normal points. Training labels and the digit evaluation's overlap with training data are retained; no general novelty guarantee or benchmark superiority is asserted.
- The initial sandbox PDF download could not resolve the host; authorized network access retrieved the public author PDF. Other web opens encountered a PubMed browser challenge, internal DOI/click errors and an Angiulli PDF timeout; these are access limits, not evidence of absence.
- No full paper is redistributed. Exact rational score examples were checked; no classifier was trained and no historical implementation or benchmark was executed.
- The two new records bring native DRAFT concepts to506, with442 generated AIO records unchanged. Two new pending source cohorts and the accounted frontier leave432 pending cohorts; no saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T080302Z-novelty-scores
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of nearest-neighbor ratio and bootstrap-instability
  novelty detection
started_at: '2026-10-12T07:58:05Z'
finished_at: '2026-10-12T08:03:02Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all thirteen primary PDF pages, inspected
    ignored-inclusive identity matches and annotated mapping context, reread every
    field of both final records, and challenged reference selection, duplicates, ties,
    acceptance regions, calibration, bootstrap supervision and empirical scope with
    exact calculations. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain two distinct novelty-detection procedures with related AIO binary-decision
  mappings. All selected fields are supported with explicit source ambiguities and
  limits; no actionable final-record defect was found.
source:
  git_revision: 13fd55f549c54fa96b93d66020e2d61d71db3379
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
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
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UncertaintyBias.yaml
    sha256: b013064a48a14beef5040486a8d1cbd11d9c503739d6fc89f73460b08f38e8f3
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/Bagging.yaml
    sha256: c7860fed789012e17dd1f696a44dbc71be12fe393fa1dec96a3245940ec86d81
    role: context
  - path: data/curated/BootstrapClassifierInstabilityNoveltyDetection.yaml
    sha256: 736ee984372216632b2d4fc3c0eb3e2139647eb64b993d2d6479ece5d57d0821
    role: target
  - path: data/curated/DBSCAN.yaml
    sha256: de7d744d1f7761af64ce963cf5759853d70a586b4188eea757751357e5035f44
    role: context
  - path: data/curated/L2LossSupportVectorDataDescription.yaml
    sha256: 42d0072e69d90f8f70b87bec4393787ce23f2b9e494d1efa74aaad270cec1893
    role: context
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: context
  - path: data/curated/NearestNeighborRatioDataDescription.yaml
    sha256: 93d66c76f275d5dbc06a80c69af19dd9bceaa9cd564945f17db714f6faaf1f28
    role: target
  - path: data/curated/NeighborhoodComponentsAnalysis.yaml
    sha256: 9aa5fa5229196181f23e7ba5910dba00623a60e558b97233e6cefc1f0fbbd577
    role: context
  - path: data/curated/OPTICS.yaml
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: context
  - path: research/discovery/20261012T075739Z-novelty-scores.json
    sha256: e88bbe902f26584c0731f5bdc7dc83d7d9a66264c5edd70ba25b5687727649e7
    role: context
  - path: research/discovery/novelty-score-boundaries.py
    sha256: 906ae53748c600dccf8ffcdc7707182c625f41e63ff00ecde193fded7dcaceb7
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
- target_id: AIMech:NearestNeighborRatioDataDescription
  path: data/curated/NearestNeighborRatioDataDescription.yaml
  label: Nearest-neighbor ratio data description
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NearestNeighborRatioDataDescription.yaml
    role: maintained
- target_id: AIMech:BootstrapClassifierInstabilityNoveltyDetection
  path: data/curated/BootstrapClassifierInstabilityNoveltyDetection.yaml
  label: Bootstrap classifier-instability novelty detection
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BootstrapClassifierInstabilityNoveltyDetection.yaml
    role: maintained
scope:
  description: Every field of the two explicitly selected novelty-detection algorithms.
  selection: Exact maintained IDs AIMech:NearestNeighborRatioDataDescription and AIMech:BootstrapClassifierInstabilityNoveltyDetection,
    without sampling.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  exclusions:
  - target: Eighteen contextual AIO/native YAMLs
    reason: Eleven generated and seven maintained neighboring records inform identity
      and mapping scope, without renewed scientific approval.
  - target: Historical implementation and benchmark reproduction
    reason: Only declared exact arithmetic examples were executed; no classifier was
      trained.
  - target: Generated website
    reason: Freshness and validity checks do not constitute a separate visual-design
      review.
  - target: Remaining discovery frontier
    reason: 432 pending cohorts and other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 144.87s (0:02:24)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 506 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 154 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 150,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
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
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
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
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact novelty-score boundary calculations
  command: python3 research/discovery/novelty-score-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  exit_code: 0
  expected_exit_code: 0
  summary: '{"status": "passed", "nearest_tie_scores": ["10", "1/2"], "nearest_selection_differs_from_union_of_balls":
    true, "duplicate_ratio": "undefined 0/0", "singleton_has_no_other_neighbor": true,
    "distinct_training_ratios": "all zero", "bootstrap_variance": "1/4", "stable_outputs_variance":
    "0", "variance_threshold": "11/64", "standard_deviation_threshold": "1/2", "doubled_output_variance_threshold":
    "5/4", "interpretation": "Exact score-level counterexamples expose unspecified
    conventions and distinguish the source threshold formulas; no source policy is
    invented and no trained model is evaluated."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T075739Z-novelty-scores.json
  accessed_at: '2026-10-12T07:58:05Z'
  support: supports
  summary: Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504
    preceding native IDs, names and aliases. No normalized candidate identity collision
    was found. Fixed-string whole-word searches included ignored and hidden files
    in both checkouts, expanded names, acronyms and source identifiers. All 12 matching
    lines per checkout, eight distinct texts at 24 locations, were inspected as queries,
    bibliographic notes and pending leads in the preceding discovery ledger. A fresh
    semantic AIO search returned 65 label/synonym/definition rows, all read; eleven
    annotated class nodes and outgoing edges and eighteen contextual YAMLs were read
    or reused after unchanged-byte checks. A wider native neighbor search inspected
    names and definitions only. Absence is bounded to this pin and inspected corpus.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eleven annotated class nodes and outgoing edges, eleven generated YAMLs
    and seven native neighboring records
  accessed_at: '2026-10-12T07:58:05Z'
  support: supports
  summary: The accept-versus-reject output is related to AIO:BinaryClassification.
    This is a method-to-task association, not an is-a or exact-match assertion. Its
    Classification parent is under SupervisedLearning; the related mapping does not
    assert representative training data from the abnormal class. Inspected BinaryClassification,
    Classification, SupervisedLearning, UnsupervisedLearning, MachineLearningTask,
    Model, three KnearestNeighbor nodes, EnsembleLearning and UncertaintyBias with
    their annotations and outgoing edges. The pinned nearest-neighbor nodes specify
    label plurality or value averaging, not local distance-ratio rejection. EnsembleLearning
    emphasizes combined prediction, not the particular bootstrap-variance novelty
    signal, and UncertaintyBias denotes a sampling bias rather than a detector. Generic
    models and learning tasks do not identify these procedures. Bagging, DBSCAN, OPTICS,
    NCA, LMNN and both SVDD loss variants supply distinct contextual mechanisms and
    receive no renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/novelty-score-boundaries.py
  locator: Exact rational nearest-reference selection, ties, duplicates, training
    resubstitution and alternative calibration formulas
  accessed_at: '2026-10-12T07:58:05Z'
  snapshot_sha256: 906ae53748c600dccf8ffcdc7707182c625f41e63ff00ecde193fded7dcaceb7
  support: supports
  summary: Exact nearest-neighbor examples show decision-changing ties, undefined
    duplicate ratios, singleton failure and disagreement with a naive union-of-balls
    region. Distinct training queries have zero score without guaranteeing future
    coverage. Bootstrap moment examples distinguish mean-plus-three-variance from
    mean-plus-three-standard-deviation and show output-scaling dependence. These are
    curator score-level calculations, not historical experiments.
- evidence_id: tax2000
  kind: primary_source
  reference: https://rduin.nl/papers/icpr_00_dd.pdf
  locator: Introduction and Sections 3-5, printed pp.672-675 / PDF pp.1-4, Figures
    1-5; Section 2.2, printed p.673 / PDF p.2, Equations 3-6; Section 2.2, printed
    p.673 / PDF p.2, Equations 3-6 and threshold paragraph; Section 2.2, printed p.673
    / PDF p.2, Equations 4-6; curator examples in research/discovery/novelty-score-boundaries.py;
    Sections 2.2 and 5, printed pp.673 and 675 / PDF pp.2 and 4; curator training-query
    qualification
  accessed_at: '2026-10-12T07:42:12Z'
  snapshot_sha256: 880da8ebd7fec58daca2c2dbde13f989d389d525cff476c0ccef9837fe627def
  support: supports
  summary: Data Description in Subspaces. ICPR 2000 proceedings, volume 2, printed
    pp.672-675. Exact author-hosted four-page scan, all pages visually read; PDF-page
    offset671. Full method, figures, assumptions and evaluation limits inspected;
    historical experiments were not reproduced.
- evidence_id: tax1998
  kind: primary_source
  reference: https://rduin.nl/papers/stipr_98_outlier.pdf
  locator: Section 2.1, PDF p.3, Equation 4 and bootstrap paragraph; Section 2.1,
    PDF p.3, Equation 4; Section 2.2 thresholding and Section 3, PDF pp.3-4; Section
    2.1, PDF pp.2-3, Equation 3; Section 2.2 and experimental protocol, PDF pp.3-4,
    Equation 6 and Figure 1; Section 2.2, PDF p.3, prose and Equation 6; curator exact
    score calculations in research/discovery/novelty-score-boundaries.py; Section
    3, PDF pp.3-4, feature, class-split and classifier paragraphs; Sections 3-4, PDF
    pp.4-8, Figures 1-3; Sections 3.1 and 4, PDF pp.5-8, Figures 2-3 and conclusion
  accessed_at: '2026-10-12T07:46:39Z'
  snapshot_sha256: e6be8fdbbfc63236407da3a4fa066b176849c57463e37be339e60260f4cf009e
  support: supports
  summary: Outlier Detection using Classifier Instability. Exact unnumbered nine-page
    author-hosted manuscript, all pages visually read. Author bibliography identifies
    SSPR/SPR1998, LNCS1451:593-601; locators use PDF pages, without asserting identical
    proceedings pagination. Full method, figures, assumptions and evaluation limits
    inspected; historical experiments were not reproduced.
assessments:
- assessment_id: nearestneighborratiodatadescription-identity
  area: identity
  topic: Definition, identity and mapping scope
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - identity
  - mapping
  - tax2000
  - tax1998
  summary: Retain the distinct native DRAFT novelty-detection procedure with a related
    binary-decision task mapping.
  details: This is the local distance-ratio detector described in Tax-Duin1998 Equation3
    and Tax-Duin2000 Equations4-6. The 2000 paper studies a unit threshold and threshold
    sweeps; the 1998 paper uses a different, incompletely specified calibration convention.
    The core score is shared, but the complete experimental protocols are not asserted
    identical. The denominator concerns the selected reference point's own nearest
    other reference, not necessarily the query's second-nearest point. This method
    does not vote among class labels, average regression values, learn a supervised
    distance matrix, label density-connected components or optimize an enclosing sphere.
    Generic NN-d and NNDD acronyms are searched but not assigned as unique aliases.
    Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504 preceding
    native IDs, names and aliases. No normalized candidate identity collision was
    found. Fixed-string whole-word searches included ignored and hidden files in both
    checkouts, expanded names, acronyms and source identifiers. All 12 matching lines
    per checkout, eight distinct texts at 24 locations, were inspected as queries,
    bibliographic notes and pending leads in the preceding discovery ledger. A fresh
    semantic AIO search returned 65 label/synonym/definition rows, all read; eleven
    annotated class nodes and outgoing edges and eighteen contextual YAMLs were read
    or reused after unchanged-byte checks. A wider native neighbor search inspected
    names and definitions only. Absence is bounded to this pin and inspected corpus.
    A target-class data-description algorithm that scores a query by its distance
    to a nearest reference observation divided by that observation's nearest-other-reference
    spacing, and accepts queries whose ratio does not exceed a chosen threshold, where
    the denominator and neighbor-selection conventions are well defined.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A scoring and decision procedure, not a particular fitted classifier.
    evidence_ids:
    - tax2000
    - tax1998
  - name: aio-mapping
    value: related_match
    definition: The two-outcome decision relates the method to a task; it does not
      assert exact equivalence or representative abnormal-class training data.
    evidence_ids:
    - mapping
- assessment_id: nearestneighborratiodatadescription-local-spacing-score
  area: evidence
  topic: local spacing score
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - tax2000
  - tax1998
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'For a reference set with at least two observations, select i minimizing
    ||x-x_i||_2 and another reference j!=i minimizing ||x_i-x_j||_2. When d2=||x_i-x_j||_2
    is positive, use rho(x)=||x-x_i||_2/d2. The 2000 default accepts rho<=1; increasing
    the threshold expands acceptance for a fixed reference set and neighbor-selection
    rule. The score uses Euclidean distances, not their squares, and the density motivation
    does not make rho a normalized probability or an outlier posterior. Source locators:
    tax2000: Section 2.2, printed p.673 / PDF p.2, Equations 3-6 and threshold paragraph;
    tax1998: Section 2.1, PDF pp.2-3, Equation 3'
- assessment_id: nearestneighborratiodatadescription-duplicates-ties-and-region
  area: evidence
  topic: duplicates ties and region
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - tax2000
  - tax1998
  - finite-boundaries
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'The denominator requires excluding the selected reference observation
    itself. Duplicate coordinates can still make d2=0, including an undefined 0/0
    for a matching query; a singleton reference set has no other neighbor. The sources
    do not specify a general duplicate or nearest-tie policy. Ties can affect the
    decision: for references {-1/10,0,2} and query 1, choosing 0 gives ratio 10 while
    choosing 2 gives 1/2. The nearest-selected rule is also not generally the union
    of all reference-centered balls with radii equal to local spacing: query 9/10
    in the same example is rejected at unit threshold although it lies inside the
    radius-2 ball centered at 2. These are exact curator calculations, not repairs
    attributed to the papers. Source locators: tax2000: Section 2.2, printed p.673
    / PDF p.2, Equations 4-6; curator examples in research/discovery/novelty-score-boundaries.py;
    tax1998: Section 2.1, PDF pp.2-3, Equation 3'
- assessment_id: nearestneighborratiodatadescription-coverage-and-calibration
  area: evidence
  topic: coverage and calibration
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - tax2000
  - tax1998
  - finite-boundaries
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'With distinct reference coordinates and queries evaluated against the
    full reference set, each training point has ratio zero and is accepted at a nonnegative
    threshold. This does not guarantee acceptance of all future target observations,
    minimum-volume support estimation or a calibrated false-alarm rate. The 1998 calibration
    text says three standard deviations above the training-score mean, while its displayed
    Equation6 uses three times var. Its nonzero training-ratio histogram also requires
    a scoring convention beyond naive self-including resubstitution; the exact exclusion
    protocol is not established here. These settings are not silently substituted
    for the 2000 unit-threshold rule. Source locators: tax2000: Sections 2.2 and 5,
    printed pp.673 and 675 / PDF pp.2 and 4; curator training-query qualification;
    tax1998: Section 2.2 and experimental protocol, PDF pp.3-4, Equation 6 and Figure
    1'
- assessment_id: nearestneighborratiodatadescription-evidence-and-noise-scope
  area: evidence
  topic: evidence and noise scope
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - tax2000
  - tax1998
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'The rule depends on individual reference locations, feature scaling and
    threshold choice, and is sensitive to noise and sparse internal regions. The 2000
    study compares synthetic uniform, Gaussian, heavy-tailed and embedded low-variance
    settings, with target-coverage versus outlier-acceptance tradeoffs. Its pump example
    uses 96 training objects with 64 autoregressive features and compares reduced
    representations and other detectors. The 1998 digit study reports poor nearest-neighbor
    results in many settings and includes training observations in its normal test
    population. Neither source establishes universal small-sample or high-dimensional
    superiority; no numerical performance claim or minimum-volume theorem is inferred
    from their summaries. Source locators: tax2000: Introduction and Sections 3-5,
    printed pp.672-675 / PDF pp.1-4, Figures 1-5; tax1998: Sections 3-4, PDF pp.4-8,
    Figures 1-3'
- assessment_id: bootstrapclassifierinstabilitynoveltydetection-identity
  area: identity
  topic: Definition, identity and mapping scope
  outcome: supported
  target_ids:
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - identity
  - mapping
  - tax1998
  summary: Retain the distinct native DRAFT novelty-detection procedure with a related
    binary-decision task mapping.
  details: This is the Tax-Duin1998 instability-based detector. Its novelty signal
    is variability of classifier outputs across bootstrap training sets, not the mean
    prediction used for ordinary bagging, nearest-neighbor spacing, a density estimate,
    vote entropy or a Bayesian posterior uncertainty. The published experiment uses
    labels among normal digit classes to train its base classifiers; target-versus-abnormal
    detection does not imply that the entire fitting procedure is label-free. The
    source's threshold notation is ambiguous, so the record preserves the procedure
    and that uncertainty rather than declaring an exact executable reference implementation.
    Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 504 preceding
    native IDs, names and aliases. No normalized candidate identity collision was
    found. Fixed-string whole-word searches included ignored and hidden files in both
    checkouts, expanded names, acronyms and source identifiers. All 12 matching lines
    per checkout, eight distinct texts at 24 locations, were inspected as queries,
    bibliographic notes and pending leads in the preceding discovery ledger. A fresh
    semantic AIO search returned 65 label/synonym/definition rows, all read; eleven
    annotated class nodes and outgoing edges and eighteen contextual YAMLs were read
    or reused after unchanged-byte checks. A wider native neighbor search inspected
    names and definitions only. Absence is bounded to this pin and inspected corpus.
    A novelty-detection procedure that trains classifiers on bootstrap resamples of
    reference data, estimates the variance of their outputs at a query, and rejects
    queries with unusually high variability relative to a chosen reference-score threshold.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A scoring and decision procedure, not a particular fitted classifier.
    evidence_ids:
    - tax1998
  - name: aio-mapping
    value: related_match
    definition: The two-outcome decision relates the method to a task; it does not
      assert exact equivalence or representative abnormal-class training data.
    evidence_ids:
    - mapping
- assessment_id: bootstrapclassifierinstabilitynoveltydetection-bootstrap-output-variance
  area: evidence
  topic: bootstrap output variance
  outcome: supported
  target_ids:
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  - finite-boundaries
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'Draw bootstrap training sets of the original reference-set size, fit the
    chosen classifier to each, and compare their output values at the same query.
    The source defines rho(x)=E_b[out_b(x)^2]-(E_b[out_b(x)])^2, where the expectation
    is over bootstrap fits. Repeated fitted outputs estimate this variance; a large
    score indicates sensitivity to the sampled training set. It is not itself the
    probability that the query is novel. Base learner, output scaling, resampling
    and finite-ensemble variance-estimation conventions affect the result. Source
    locators: tax1998: Section 2.1, PDF p.3, Equation 4 and bootstrap paragraph'
- assessment_id: bootstrapclassifierinstabilitynoveltydetection-published-multiclass-configuration
  area: evidence
  topic: published multiclass configuration
  outcome: supported
  target_ids:
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'The digit experiment uses a linear classifier based on Fisher''s criterion,
    with a normalized sigmoid of distance to its decision boundary as output. It fits
    one-versus-rest classifiers for nine retained digit classes, produces 25 bootstrap
    classifier sets and averages output variances over the nine class outputs to obtain
    one novelty score. The withheld tenth digit class supplies abnormal examples for
    evaluation. These counts and learner choices describe that experiment, not fixed
    requirements for every use of the variance-gating procedure. Source locators:
    tax1998: Section 3, PDF pp.3-4, feature, class-split and classifier paragraphs'
- assessment_id: bootstrapclassifierinstabilitynoveltydetection-threshold-ambiguity
  area: evidence
  topic: threshold ambiguity
  outcome: supported
  target_ids:
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  - finite-boundaries
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'Section2.2 motivates a threshold at the reference-score mean plus three
    standard deviations under a rough Gaussian-score assumption, but Equation6 writes
    mean plus three times var. These are different numerical rules unless var is being
    used for a different convention; the paper does not resolve that notation here.
    For reference scores {0,1/4}, the two thresholds are 1/2 and 11/64 respectively,
    so a query score of 1/4 receives different decisions. Doubling all classifier
    outputs multiplies variance scores by four; the literal mean-plus-three-variance
    threshold does not generally scale in the same way. The record does not select
    a hidden implementation convention or infer an exact false-alarm probability.
    Source locators: tax1998: Section 2.2, PDF p.3, prose and Equation 6; curator
    exact score calculations in research/discovery/novelty-score-boundaries.py'
- assessment_id: bootstrapclassifierinstabilitynoveltydetection-stable-outliers-and-evaluation
  area: evidence
  topic: stable outliers and evaluation
  outcome: supported
  target_ids:
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  summary: Supported within the explicitly stated assumptions and limitations.
  details: 'Outliers can receive low variance when all bootstrap classifiers extrapolate
    stably, and difficult normal observations can receive high variance. More bootstrap
    replicates can improve estimation of a fixed variability signal but do not guarantee
    that stable outliers acquire a detectable signal. The reported digit comparisons
    depend on representation and training-set size; the normal evaluation population
    includes training examples, and rotation-invariant features can make withheld
    digits indistinguishable from retained ones. The source itself reports stable-region
    failures and weaker results at larger sample sizes. This supports a bounded instability
    indicator, not a universal novelty detector or general performance advantage.
    Source locators: tax1998: Sections 3.1 and 4, PDF pp.5-8, Figures 2-3 and conclusion'
- assessment_id: score-identity-boundary
  area: consistency
  topic: Distance ratio versus bootstrap output variance
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  - tax2000
  - identity
  - mapping
  summary: Retain two different novelty scores and fitting procedures.
  details: The nearest-reference score compares a query distance with the selected
    reference point's own nearest-other spacing. The instability score compares repeated
    outputs across bootstrap fits. The latter experiment uses normal-class labels
    and a mean of nine output variances, not a label-free density estimate or ordinary
    bagging prediction. Sharing a rejection task and a source paper does not make
    the methods aliases. Generic NN-d and NNDD acronyms are deliberately not unique
    aliases.
- assessment_id: neighbor-geometry
  area: consistency
  topic: Reference exclusion, ties and acceptance geometry
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  evidence_ids:
  - tax1998
  - tax2000
  - finite-boundaries
  summary: The record preserves undefined and convention-dependent cases instead of
    inventing a historical implementation.
  details: A singleton has no other reference; duplicates can leave a zero denominator
    after index exclusion. For references {-1/10,0,2}, query1 yields ratios10 or1/2
    depending on the nearest tie. Query9/10 is rejected at unit threshold even though
    it lies in the spacing-radius ball centered at2. Thus the selected-nearest rule
    is not generally a union of all such balls. Distinct training queries score0 under
    self-including resubstitution; this establishes neither future target coverage
    nor minimum volume. The nonzero1998 training histogram indicates a further scoring
    convention whose precise exclusions are not established.
- assessment_id: calibration-ambiguity
  area: consistency
  topic: Standard deviation versus variance threshold
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  - tax2000
  - finite-boundaries
  summary: Contradictory source notation is explicit and is not silently repaired.
  details: The1998 prose says mean plus three standard deviations but Equation6 writes
    mean plus three times var. With empirical scores{0,1/4}, the alternatives give1/2
    and11/64; query1/4 changes decision. Doubling classifier outputs quadruples the
    variance score, but the literal mean-plus-three-variance rule is not scale covariant.
    These calculations use a declared empirical moment convention, not a claim about
    the unspecified historical variance divisor. The2000 unit threshold and threshold
    sweeps are kept separate from the1998 calibration.
- assessment_id: evaluation-and-provenance
  area: provenance
  topic: Source versions, interpretation and empirical scope
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - tax1998
  - tax2000
  summary: All thirteen primary PDF pages were read; the records preserve source and
    evaluation limits.
  details: All four scanned2000 pages and all nine unnumbered1998 manuscript pages
    were visually inspected, including figures and references. The2000 printed-page
    offset is671; the1998 PDF is not assigned an inferred proceedings-page offset.
    The digit experiment includes training observations among normal test examples
    and representation-induced withheld-class ambiguity. Stable extrapolation can
    defeat bootstrap novelty detection even with many replicates. The pump and synthetic
    comparisons depend on representation, sample size and thresholds. No numerical
    benchmark advantage, probability calibration or universal optimality is asserted.
    Exact arithmetic is not an implementation reproduction. Contextual records receive
    no renewed scientific approval;432 pending discovery cohorts remain.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NearestNeighborRatioDataDescription
  - AIMech:BootstrapClassifierInstabilityNoveltyDetection
  evidence_ids:
  - identity
  - mapping
  - tax1998
  - tax2000
  - finite-boundaries
  rationale: Local reference-spacing ratios and bootstrap classifier-output variances
    use distinct mechanisms and assumptions. Their common novelty-decision task does
    not establish equivalence. Preserve distinctions from neighbor voting, learned
    metric transformations, sphere descriptions and prediction averaging.
limitations:
- Adversarial author self-review only; both maintained records remain DRAFT.
- All thirteen primary PDF pages were visually read. The four-page2000 PDF is a scan,
  with printed offset671; the nine-page1998 author manuscript is unnumbered and cited
  by PDF page. Neither text extraction alone was treated as full reading.
- The nearest-neighbor score is shared across the two sources, but their calibration
  protocols differ. The earlier training-score exclusion and variance-versus-standard-deviation
  threshold notation remain explicit limitations, not invented implementation policies.
- Bootstrap output variability can miss stable outliers and detect difficult normal
  points. Training labels and the digit evaluation's overlap with training data are
  retained; no general novelty guarantee or benchmark superiority is asserted.
- The initial sandbox PDF download could not resolve the host; authorized network
  access retrieved the public author PDF. Other web opens encountered a PubMed browser
  challenge, internal DOI/click errors and an Angiulli PDF timeout; these are access
  limits, not evidence of absence.
- No full paper is redistributed. Exact rational score examples were checked; no classifier
  was trained and no historical implementation or benchmark was executed.
- The two new records bring native DRAFT concepts to506, with442 generated AIO records
  unchanged. Two new pending source cohorts and the accounted frontier leave432 pending
  cohorts; no saturation.
links: []
tags:
- native-concepts
- novelty-detection
- self-review
- discovery-ongoing
```
