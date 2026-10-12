# Scientific self-review of core-set SVDD: resolved

- Review: 20261012T102906Z-core-set-svdd-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T10:25:22Z
- Finished UTC: 2026-10-12T10:29:06Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the original CSVDD training algorithm. The source-locator finding is resolved; no actionable final-record finding remains within scope.

## Scope And Provenance

Every field of the selected core-subset training algorithm.

Selection: Exact maintained ID AIMech:CoreSetSupportVectorDataDescription, without sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 06fc5404037c897d64caa253591c4c6802c5c0bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CoreSetSupportVectorDataDescription | data/curated/CoreSetSupportVectorDataDescription.yaml | maintained | Core-set support vector data description |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CoreSetSupportVectorDataDescription | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 102.21s (0:01:42)<br>Checked 442 record(s); 0 failed.<br>Checked 518 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 164 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 160,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CoreSetSupportVectorDataDescription | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CoreSetSupportVectorDataDescription | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CoreSetSupportVectorDataDescription | Exited0 without output. |
| Exact CSVDD boundaries | passed | True | AIMech:CoreSetSupportVectorDataDescription | {"scope": "Exact displayed-formula illustrations; no model training or historical code execution.", "permitted_initialization": {"points": ["0", "1/10", "1"], "nu": "1/5", "epsilon": "1/5", "k": "5/4", "n0": 3, "z": "1/10", "radius": "4/5", "expanded_radius": "24/25", "expanded_outside": 0, "original_outside": 1, "original_outside_fraction": "1/3", "optimum_objective": "1/4", "stopped_objective": "277/300", "objective_ratio": "277/75"}, "subset_cap": {"full_n": 100, "core_n": 2, "nu": "1/10", "sum_full_caps": "1/5", "sum_rescaled_caps": "10", "interpretation": "This warns against retaining the full-data denominator; it does not identify the unpublished historical implementation."}, "center_dependence": {"optimal_radius": "1", "farthest_from_current": "2"}, "complexity_substitution": "Source M=O(1/(delta*epsilon)); fixed delta gives O(N/epsilon^2+epsilon^-4), whereas experimental delta=0.01*epsilon gives O(N/epsilon^4+epsilon^-8) under the same model and fixed k."} |

## Scientific And Domain Assessments

### Definition, aliases and training-algorithm scope

identity: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Retain the source-specific CSVDD algorithm.

An approximate one-class training algorithm that grows a core subset using the nearest expanded-sphere violator, refits support vector data description and enforces radius growth until the expanded sphere meets an outlier-count stopping rule. This record denotes the Chu-Tsang-Kwok2004 CSVDD training procedure. It is distinct from ordinary SVDD, squared-slack SVDD, sphere-based clustering and hard-MEB core-vector solvers. Later CVDD usage is not assumed to be an exact alias. Compared all442 pinned AIO IDs, labels and scoped synonyms with all517 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Whole-word fixed-string searches included ignored and hidden files in both checkouts, expanded names, CSVDD/CVDD acronyms and source identifiers. All83 distinct matched-text windows were inspected; the post-merge repeat retained exactly those windows at293 locations. Hits are unresolved CVDD/catalogue leads and unrelated uses of rapid, not an existing CSVDD record. Of94 semantic AIO rows,93 match the preceding full reading exactly and the additional EnergyBasedLLM row was read; all74 native name/definition rows were read or reused after exact equality checks. Fifteen annotated AIO CLASS nodes and outgoing edges were inspected, and24 contextual YAMLs retain byte-verified prior full readings. Absence is bounded to this pinned and maintained corpus.

### Related algorithm-to-task AIO mapping

grounding: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The related mapping does not imply two-class supervision or is-a membership.

AIO:BinaryClassification is related through the eventual accept/reject task of the trained support description. Its Classification ancestry is under SupervisedLearning; this related mapping asserts neither algorithm-task equivalence, is-a membership nor two-class supervision. AIO:SupportVectorMachine describes a supervised category-separating network with layer relationships, not this one-class subset-training procedure. UnsupervisedLearning and MachineLearningTask describe task scope; KernelLayer is a component, TrainingStrategy is defined as preprocessing, and DataPreparation/SelectionAndSamplingBias do not identify the iterative algorithm. Native SVDD defines sphere estimation, L2-loss SVDD changes the slack objective, SVC adds graph-component labels, CVM/generalized CVM use different enclosing-ball reductions and BVM changes center updates. Regression and density-model matches do not identify CSVDD.

### underlying soft sphere problem

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

The underlying target-only SVDD minimizes R²+(1/(nu*N))*sum_i xi_i with R&gt;=0, xi_i&gt;=0 and &#124;&#124;phi(x_i)-c&#124;&#124;²&lt;=R²+xi_i, for0&lt;nu&lt;1. Its displayed dual maximizes sum_i alpha_i*K_ii-alpha^T*K*alpha with sum(alpha)=1 and0&lt;=alpha_i&lt;=1/(nu*N). Thus the slack penalty is linear, not the squared-slack formulation used by L2-loss SVDD or a hard-MEB reformulation. Positive-semidefinite kernels permit feature-space distances without explicitly constructing features. Radius recovery from a free boundary coefficient requires such a coefficient to exist. Locators: Section II, PDF p2, primal and dual displays, center recovery and kernelization paragraph

### core initialization

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

Fit ordinary SVDD to a fixed-size random sample of n0 observations and select the sampled observation z closest to that fitted center as a probable inlier. Choose a random sampled x, find its farthest observation y in the full dataset, and set D=&#124;&#124;phi(x)-phi(y)&#124;&#124; and initial radius R1=D/k for k&gt;1. Start the core with z and center c1=phi(z). This initial center is an observation, not the fitted sample center; the initial radius need not equal the one-point minimum-enclosing-ball radius. The probable-inlier choice is a heuristic, not a guarantee that z is normal. Locators: Section III-A, PDF pp2-3, Equation1

### nearest violator and radius growth

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

At iteration i, compute P_i={x in the full dataset:&#124;&#124;phi(x)-c_i&#124;&#124;&gt;(1+epsilon)*R_i}. Stop when &#124;P_i&#124;&lt;nu*N, with a strict inequality. Otherwise select the observation in P_i outside the current core that is nearest to c_i, enlarge the core, refit SVDD on that subset, and enforce R_(i+1)&gt;=(1+delta*epsilon)*R_i for positive delta and epsilon. Repeat with the new center and radius. Nearest violating-point selection, soft subset refits and imposed radius growth distinguish this procedure from farthest-point hard-MEB core algorithms. Locators: Section III-B, PDF p3, steps1-7 and Equation2

### expanded quota and objective boundary

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

Termination checks the expanded radius (1+epsilon)*R, not the unexpanded sphere used by ordinary SVDD prediction. A permitted exact initialization illustrates the difference: use linear-kernel points0,1/10,1, nu=epsilon=1/5, n0=3, random x=0 and k=5/4. The initial sample SVDD has center1/2 and radius1/2; z=1/10 is its unique nearest observation. D=1 yields R1=4/5 and expanded radius24/25. No training point lies outside the expanded sphere, so the procedure stops immediately; one of three lies outside the original sphere, exceeding nu=1/5. The stopped sphere has full SVDD objective277/300 versus optimum1/4, a ratio277/75 greater than(1+epsilon)². This is exact curator arithmetic for allowed procedure choices, not a historical benchmark or claim about the paper’s experimental settings. Locators: Sections II and III-A/B, PDF pp2-3; curator derivation in research/discovery/core-set-svdd-boundaries.py

### conditional cost analysis

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

The source derives O(M²*N+M⁴) work for M core additions using unit-cost kernel evaluations and a cubic subset-QP cost, and states M&lt;=k/(delta*epsilon). Its O(N/epsilon²+epsilon^-4) form treats k and delta as fixed. The experiments instead set delta=0.01*epsilon; substitution into the same cost model gives O(N/epsilon^4+epsilon^-8) at fixed k. These expressions omit dimension-dependent kernel cost and input storage. The stated iteration argument uses the optimal full-data MEB radius as an enclosure bound, but an arbitrary current convex-hull center can require up to twice that radius: points0,2 have optimal radius1 at center1 and farthest distance2 from center0. The literal constant bound therefore needs its center assumptions checked; it is not a proof of soft-SVDD objective or decision-boundary approximation. Locators: Section III-C, PDF p3, Equation3; Section IV introduction, PDF pp3-4, parameter choices; curator dependence and center calculations in research/discovery/core-set-svdd-boundaries.py

### subproblem and implementation conventions

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

A reimplementation must specify the subset SVDD penalty convention, radius-growth enforcement, numerical tolerances and tie or missing-free-support handling. Merely retaining the full-data cap1/(nu*N) on a smaller equality-simplex subproblem can make it infeasible: for N=100, nu=1/10 and a two-point core, the sum of upper bounds is1/5&lt;1. Using the subset sample size gives a different cap. The paper says to run SVDD on the subset but does not expose a complete CSVDD implementation resolving all such choices. This feasibility calculation is not evidence that its historical code used the full-data cap. Locators: Sections II and III-B, PDF pp2-3, dual constraints and iterative steps5-6; curator exact cap calculation in research/discovery/core-set-svdd-boundaries.py

### empirical and identity scope

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Supported within the stated source and mathematical scope.

Section IV explicitly names the method Core-set Support Vector Data Description, CSVDD. The two application studies concern BioID-derived face detection and MNIST one-class digit detection, with selected Gaussian kernels, nu values, tolerances,20 random repetitions and historical MATLAB/MOSEK3, dd_tools and LIBSVM configurations. The reported time, memory failures and AUC trade-offs are specific to those data and implementations. They do not prove universal accuracy, speed or soft-objective approximation. This record does not equate CSVDD with every later method called core vector data description or CVDD. Locators: Sections IV-V, PDF pp3-6, Figures1-6 and TablesI-III

### Initialization versus fitted sample sphere

consistency: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The exact example follows permitted initialization choices.

For three linear-kernel observations, nu=1/5 makes cap5/3. Coefficients(1/2,0,1/2) give center1/2 and dual value1/4; the radius1/2 primal attains the same value and encloses every point. Observation1/10 is uniquely closest to that center. Choosing random x=0, k5/4 and epsilon1/5 yields initial center1/10 and radius4/5, not the sample center/radius. The source permits these choices; they differ from its experimental n0=20,k10. No iteration or inaccessible historical implementation is inferred.

### Expanded enclosure versus original prediction and soft objective

consistency: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

Termination alone supplies neither stronger conclusion.

The expanded radius24/25 covers all three features, while the unexpanded radius4/5 rejects the point1. Its rejection fraction1/3 exceeds nu1/5. With the displayed linear slack penalty, the stopped primal value is277/300 and the exact optimum is1/4; ratio277/75 exceeds36/25. The source explicitly distinguishes hard-MEB theory from soft-SVDD. This calculation limits interpretations of the heuristic; it does not refute a benchmark result or claim the authors proved that stronger ratio.

### Conditional asymptotics and moving-center enclosure

consistency: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The record preserves dependencies and qualifies the literal constant.

The stated sum of i*N+i^3 costs is O(M²*N+M⁴). Holding delta fixed versus setting delta=.01epsilon changes the epsilon dependence. Unit kernel and cubic QP assumptions exclude input storage and dimension costs. Optimal MEB radius is not a radius sufficient at every current center; the0,2 example establishes that limited geometric point, not a complete runtime failure or independently repaired theorem.

### Subset penalty, radius enforcement and numerical conventions

consistency: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The feasibility warning is explicitly distinct from historical code behavior.

A two-variable equality simplex with full-data caps1/10 is infeasible because the sum of caps is1/5. Rescaling by subset size changes that cap. The original procedure says to run SVDD on the subset and then enforce radius growth; the record does not invent the implementation, allege which cap it used, or silently assume free boundary support always exists.

### Source version, complete reading and claim locators

provenance: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The two locator labels now match the original PDF.

The original six-page PDF was fully read, including formulas,figures,tables and21 references. Section II lies on PDF2; experimental parameters precede IV-A and belong to the IV introduction on PDF4. The initial record cites II/PDF1-2 and IV-A/PDF4. These are minor locator imprecisions, not unsupported formulas or invented full-text access. The author catalogue’s printed425-430 range is distinct from the unnumbered inspected copy.

### Every selected field and bounded research coverage

provenance: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

All selected fields were inspected; remaining discovery is explicit.

Read the full record after canonical source capture: stable ID,name,CSVDD alias,typed scope,definition,identity notes,all definition/claim citations,all seven claims,source authors/version/URL/hash/access time,AIO pin and mapping,limitations,DRAFT status and actual curation provenance. Five newly deduplicated cohorts retain uninspected methods;448 pending cohorts and partial work prevent a saturation claim. No model training or benchmark was executed.

### Corrected source locators

evidence: supported. Targets: AIMech:CoreSetSupportVectorDataDescription.

The locator finding is resolved.

The underlying problem now cites Section II/PDF2 with precise display and prose scope; experimental settings cite the Section IV introduction/PDF3-4. Source metadata, algorithm, mapping, calculations and limitations remain intact.

## Findings

### source-locators: Point CSVDD claim locators to the actual source sections

minor / resolved / confirmed; issue key: aimech-csvdd-source-locators.

The initial underlying-soft-sphere claim cites Section II on PDF1-2, although that section and its primal/dual, center recovery and kernelization account are on PDF2. The cost claim assigns experimental parameter choices to IV-A, although they precede that subsection in the IV introduction on PDF4. Refine both locators; substantive formulas and exact calculations are supported.

Disposition: Both claim locators now identify the original PDF sections precisely; the discovery-report mirror and rendered page agree. Other record fields remain unchanged except updated curation time, checked structurally. Actual edit history was appended, final input hashes captured and all fields reread. Final required checks pass and ignored-inclusive lineage search was inspected.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:CoreSetSupportVectorDataDescription. CSVDD is the original nearest-violator, soft-subset-fit and radius-growth training heuristic. Ordinary SVDD, squared-slack variants, hard-MEB CVM and sphere-based clustering have different scopes. Later CVDD usage and source versions are not exact aliases without further inspection.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T101902Z-core-set-support-vector-data-description.json | supports | Compared all442 pinned AIO IDs, labels and scoped synonyms with all517 preceding native IDs, names and aliases. No normalized candidate identity collision was found. Whole-word fixed-string searches included ignored and hidden files in both checkouts, expanded names, CSVDD/CVDD acronyms and source identifiers. All83 distinct matched-text windows were inspected; the post-merge repeat retained exactly those windows at293 locations. Hits are unresolved CVDD/catalogue leads and unrelated uses of rapid, not an existing CSVDD record. Of94 semantic AIO rows,93 match the preceding full reading exactly and the additional EnergyBasedLLM row was read; all74 native name/definition rows were read or reused after exact equality checks. Fifteen annotated AIO CLASS nodes and outgoing edges were inspected, and24 contextual YAMLs retain byte-verified prior full readings. Absence is bounded to this pinned and maintained corpus. |
| mapping | sources/aio/aio.json; 15 annotated CLASS nodes/outgoing edges and24 byte-verified contextual YAMLs | supports | AIO:BinaryClassification is related through the eventual accept/reject task of the trained support description. Its Classification ancestry is under SupervisedLearning; this related mapping asserts neither algorithm-task equivalence, is-a membership nor two-class supervision. AIO:SupportVectorMachine describes a supervised category-separating network with layer relationships, not this one-class subset-training procedure. UnsupervisedLearning and MachineLearningTask describe task scope; KernelLayer is a component, TrainingStrategy is defined as preprocessing, and DataPreparation/SelectionAndSamplingBias do not identify the iterative algorithm. Native SVDD defines sphere estimation, L2-loss SVDD changes the slack objective, SVC adds graph-component labels, CVM/generalized CVM use different enclosing-ball reductions and BVM changes center updates. Regression and density-model matches do not identify CSVDD. |
| finite-boundaries | research/discovery/core-set-svdd-boundaries.py | supports | Exact primal-dual certificate for the initial three-point fit and allowed initialization demonstrate immediate expanded-quota termination without the corresponding original-radius quota or objective ratio. Additional arithmetic checks distinguish subset penalty scaling, center-dependent enclosure and delta-dependent asymptotic exponents. No historical implementation executed. |
| chu2004 | https://home.cse.ust.hk/~jamesk/papers/ijcnn04.pdf; IJCNN2004 proceedings, author catalogue pp425-430. All six author-hosted PDF pages visually read, including figures, tables and references. No printed-page labels are visible in this copy; locators use PDF pages. | supports | Scaling up Support Vector Data Description by Using Core-Sets. IJCNN2004 proceedings, author catalogue pp425-430. All six author-hosted PDF pages visually read, including figures, tables and references. No printed-page labels are visible in this copy; locators use PDF pages. |
| prior-locator-finding | reviews/structured/20261012T102345Z-core-set-svdd-open/review.yaml | supports | Initial scientific author self-review identifies these two bounded source-locator imprecisions and the same complete affected target. |

## Limits And Additional Notes

- Adversarial author self-review only; the record remains DRAFT.
- All six original CSVDD pages were visually read, including formulas, figures, tables and references. The author copy has no printed page labels; locators use PDF pages.
- No historical CSVDD implementation, numerical optimizer, model training, paid provider, data upload or benchmark was executed. Exact rational checks test displayed formulas and an allowed initialization only.
- Expanded-radius termination is not a quota at the unexpanded prediction radius, and the exact example also excludes an unconditional(1+epsilon)² full-objective guarantee. Source cost bounds retain parameter and center assumptions.
- RAPID, single-class MPM, LP novelty detection, F-SVDD and regularized multimodal variants remain incomplete primary-method readings. Secondary snippets and missing HTML equations are not mechanism evidence. Bibliographic version differences remain explicit.
- The collection reaches518 native DRAFT concepts;442 generated AIO records remain unchanged. There are448 pending cohorts plus partly addressed work, so discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T102906Z-core-set-svdd-resolved
kind: category
repository: CultureBotAI/AIMech
title: 'Scientific self-review of core-set SVDD: resolved'
started_at: '2026-10-12T10:25:22Z'
finished_at: '2026-10-12T10:29:06Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all six primary PDF pages, challenged
    initialization, stopping quota, soft-objective interpretation, moving-center and
    parameter-dependent complexity, and subset conventions with exact rational checks,
    then reread every selected record field. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the original CSVDD training algorithm. The source-locator finding
  is resolved; no actionable final-record finding remains within scope.
source:
  git_revision: 06fc5404037c897d64caa253591c4c6802c5c0bf
  state: working_tree
  inputs:
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/LeastsquaresAnalysis.yaml
    sha256: 666926bd17035ea825f0f521620b9c5538ff2a8695e7d37f96ab3b0cc8aa1d3c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RidgeRegression.yaml
    sha256: 7ee3be4552041e1ee2194a78eb0cbefe25283907027a6680395973dbf98636bb
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/BallVectorMachine.yaml
    sha256: 08e08546d0f28411efad82a84b2f6a56362f7284804bad569820d42bca548737
    role: context
  - path: data/curated/CoreSetSupportVectorDataDescription.yaml
    sha256: f02d6459178882f29b748532bf817d1477721d2f7402fbfe91305ac2eb6076f2
    role: target
  - path: data/curated/CoreVectorMachine.yaml
    sha256: ac41d81c889250fb49a7593cc9dfccbf1fc56f979c4584eb60ea2c5d420619bf
    role: context
  - path: data/curated/CoreVectorRegression.yaml
    sha256: 35ed0d44bad43789851e83ce7bea8ca0303030002d474861dabe8fe276054e97
    role: context
  - path: data/curated/GeneralizedCoreVectorMachine.yaml
    sha256: 44551b4922a2d7454570f5862448de86ae266fcdd2433e5fea681c6df6549091
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: context
  - path: data/curated/L2LossSupportVectorDataDescription.yaml
    sha256: 42d0072e69d90f8f70b87bec4393787ce23f2b9e494d1efa74aaad270cec1893
    role: context
  - path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    sha256: 9cfe6597d65d6a9dae4040f56bade8cba946a4b09c82c8f0b5adbec8b66a59dc
    role: context
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: context
  - path: research/discovery/20261012T101902Z-core-set-support-vector-data-description.json
    sha256: 441efd9e1642792e2b1b8888bd2f4b1462e11cd89ccaec84943497e3a869ac9e
    role: context
  - path: research/discovery/core-set-svdd-boundaries.py
    sha256: 9f40c8c6455215adf9c5348960290a436f3fa16ff05f8a8a6b8fa928ad3e20e7
    role: context
  - path: reviews/structured/20261012T102345Z-core-set-svdd-open/review.yaml
    sha256: cffbe661b63818f9ebedd808c75825b04c9fe18a97ad480b912e376824e98b92
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
- target_id: AIMech:CoreSetSupportVectorDataDescription
  path: data/curated/CoreSetSupportVectorDataDescription.yaml
  label: Core-set support vector data description
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CoreSetSupportVectorDataDescription.yaml
    role: maintained
scope:
  description: Every field of the selected core-subset training algorithm.
  selection: Exact maintained ID AIMech:CoreSetSupportVectorDataDescription, without
    sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  exclusions:
  - target: Contextual AIO/native records
    reason: Identity and mapping context only, not renewed scientific approval.
  - target: Historical software and benchmarks
    reason: Not executed or inspected; source mathematics defines the curated scope.
  - target: Generated website visual design
    reason: Freshness and validity checked without a separate visual-design review.
  - target: Remaining frontier
    reason: 448 pending cohorts and partly addressed work remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 102.21s (0:01:42)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 518 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 164 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 160,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
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
  - AIMech:CoreSetSupportVectorDataDescription
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
  - AIMech:CoreSetSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact CSVDD boundaries
  command: python3 research/discovery/core-set-svdd-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Exact displayed-formula illustrations; no model training or
    historical code execution.", "permitted_initialization": {"points": ["0", "1/10",
    "1"], "nu": "1/5", "epsilon": "1/5", "k": "5/4", "n0": 3, "z": "1/10", "radius":
    "4/5", "expanded_radius": "24/25", "expanded_outside": 0, "original_outside":
    1, "original_outside_fraction": "1/3", "optimum_objective": "1/4", "stopped_objective":
    "277/300", "objective_ratio": "277/75"}, "subset_cap": {"full_n": 100, "core_n":
    2, "nu": "1/10", "sum_full_caps": "1/5", "sum_rescaled_caps": "10", "interpretation":
    "This warns against retaining the full-data denominator; it does not identify
    the unpublished historical implementation."}, "center_dependence": {"optimal_radius":
    "1", "farthest_from_current": "2"}, "complexity_substitution": "Source M=O(1/(delta*epsilon));
    fixed delta gives O(N/epsilon^2+epsilon^-4), whereas experimental delta=0.01*epsilon
    gives O(N/epsilon^4+epsilon^-8) under the same model and fixed k."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T101902Z-core-set-support-vector-data-description.json
  accessed_at: '2026-10-12T10:25:22Z'
  support: supports
  summary: Compared all442 pinned AIO IDs, labels and scoped synonyms with all517
    preceding native IDs, names and aliases. No normalized candidate identity collision
    was found. Whole-word fixed-string searches included ignored and hidden files
    in both checkouts, expanded names, CSVDD/CVDD acronyms and source identifiers.
    All83 distinct matched-text windows were inspected; the post-merge repeat retained
    exactly those windows at293 locations. Hits are unresolved CVDD/catalogue leads
    and unrelated uses of rapid, not an existing CSVDD record. Of94 semantic AIO rows,93
    match the preceding full reading exactly and the additional EnergyBasedLLM row
    was read; all74 native name/definition rows were read or reused after exact equality
    checks. Fifteen annotated AIO CLASS nodes and outgoing edges were inspected, and24
    contextual YAMLs retain byte-verified prior full readings. Absence is bounded
    to this pinned and maintained corpus.
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 15 annotated CLASS nodes/outgoing edges and24 byte-verified contextual
    YAMLs
  accessed_at: '2026-10-12T10:25:22Z'
  support: supports
  summary: AIO:BinaryClassification is related through the eventual accept/reject
    task of the trained support description. Its Classification ancestry is under
    SupervisedLearning; this related mapping asserts neither algorithm-task equivalence,
    is-a membership nor two-class supervision. AIO:SupportVectorMachine describes
    a supervised category-separating network with layer relationships, not this one-class
    subset-training procedure. UnsupervisedLearning and MachineLearningTask describe
    task scope; KernelLayer is a component, TrainingStrategy is defined as preprocessing,
    and DataPreparation/SelectionAndSamplingBias do not identify the iterative algorithm.
    Native SVDD defines sphere estimation, L2-loss SVDD changes the slack objective,
    SVC adds graph-component labels, CVM/generalized CVM use different enclosing-ball
    reductions and BVM changes center updates. Regression and density-model matches
    do not identify CSVDD.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/core-set-svdd-boundaries.py
  accessed_at: '2026-10-12T10:25:22Z'
  snapshot_sha256: 9f40c8c6455215adf9c5348960290a436f3fa16ff05f8a8a6b8fa928ad3e20e7
  support: supports
  summary: Exact primal-dual certificate for the initial three-point fit and allowed
    initialization demonstrate immediate expanded-quota termination without the corresponding
    original-radius quota or objective ratio. Additional arithmetic checks distinguish
    subset penalty scaling, center-dependent enclosure and delta-dependent asymptotic
    exponents. No historical implementation executed.
- evidence_id: chu2004
  kind: primary_source
  reference: https://home.cse.ust.hk/~jamesk/papers/ijcnn04.pdf
  locator: IJCNN2004 proceedings, author catalogue pp425-430. All six author-hosted
    PDF pages visually read, including figures, tables and references. No printed-page
    labels are visible in this copy; locators use PDF pages.
  accessed_at: '2026-10-12T10:03:44Z'
  support: supports
  summary: Scaling up Support Vector Data Description by Using Core-Sets. IJCNN2004
    proceedings, author catalogue pp425-430. All six author-hosted PDF pages visually
    read, including figures, tables and references. No printed-page labels are visible
    in this copy; locators use PDF pages.
  snapshot_sha256: aaaaa600dad5cbf060c83950a26f4131d5a575c9b54dbf71793e435e0393f349
- evidence_id: prior-locator-finding
  kind: prior_review
  reference: reviews/structured/20261012T102345Z-core-set-svdd-open/review.yaml
  accessed_at: '2026-10-12T10:25:22Z'
  snapshot_sha256: cffbe661b63818f9ebedd808c75825b04c9fe18a97ad480b912e376824e98b92
  support: supports
  summary: Initial scientific author self-review identifies these two bounded source-locator
    imprecisions and the same complete affected target.
assessments:
- assessment_id: identity-definition
  area: identity
  topic: Definition, aliases and training-algorithm scope
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - identity
  - chu2004
  summary: Retain the source-specific CSVDD algorithm.
  details: An approximate one-class training algorithm that grows a core subset using
    the nearest expanded-sphere violator, refits support vector data description and
    enforces radius growth until the expanded sphere meets an outlier-count stopping
    rule. This record denotes the Chu-Tsang-Kwok2004 CSVDD training procedure. It
    is distinct from ordinary SVDD, squared-slack SVDD, sphere-based clustering and
    hard-MEB core-vector solvers. Later CVDD usage is not assumed to be an exact alias.
    Compared all442 pinned AIO IDs, labels and scoped synonyms with all517 preceding
    native IDs, names and aliases. No normalized candidate identity collision was
    found. Whole-word fixed-string searches included ignored and hidden files in both
    checkouts, expanded names, CSVDD/CVDD acronyms and source identifiers. All83 distinct
    matched-text windows were inspected; the post-merge repeat retained exactly those
    windows at293 locations. Hits are unresolved CVDD/catalogue leads and unrelated
    uses of rapid, not an existing CSVDD record. Of94 semantic AIO rows,93 match the
    preceding full reading exactly and the additional EnergyBasedLLM row was read;
    all74 native name/definition rows were read or reused after exact equality checks.
    Fifteen annotated AIO CLASS nodes and outgoing edges were inspected, and24 contextual
    YAMLs retain byte-verified prior full readings. Absence is bounded to this pinned
    and maintained corpus.
- assessment_id: task-mapping
  area: grounding
  topic: Related algorithm-to-task AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - mapping
  - chu2004
  summary: The related mapping does not imply two-class supervision or is-a membership.
  details: AIO:BinaryClassification is related through the eventual accept/reject
    task of the trained support description. Its Classification ancestry is under
    SupervisedLearning; this related mapping asserts neither algorithm-task equivalence,
    is-a membership nor two-class supervision. AIO:SupportVectorMachine describes
    a supervised category-separating network with layer relationships, not this one-class
    subset-training procedure. UnsupervisedLearning and MachineLearningTask describe
    task scope; KernelLayer is a component, TrainingStrategy is defined as preprocessing,
    and DataPreparation/SelectionAndSamplingBias do not identify the iterative algorithm.
    Native SVDD defines sphere estimation, L2-loss SVDD changes the slack objective,
    SVC adds graph-component labels, CVM/generalized CVM use different enclosing-ball
    reductions and BVM changes center updates. Regression and density-model matches
    do not identify CSVDD.
- assessment_id: underlying-soft-sphere-problem
  area: evidence
  topic: underlying soft sphere problem
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  summary: Supported within the stated source and mathematical scope.
  details: 'The underlying target-only SVDD minimizes R²+(1/(nu*N))*sum_i xi_i with
    R>=0, xi_i>=0 and ||phi(x_i)-c||²<=R²+xi_i, for0<nu<1. Its displayed dual maximizes
    sum_i alpha_i*K_ii-alpha^T*K*alpha with sum(alpha)=1 and0<=alpha_i<=1/(nu*N).
    Thus the slack penalty is linear, not the squared-slack formulation used by L2-loss
    SVDD or a hard-MEB reformulation. Positive-semidefinite kernels permit feature-space
    distances without explicitly constructing features. Radius recovery from a free
    boundary coefficient requires such a coefficient to exist. Locators: Section II,
    PDF p2, primal and dual displays, center recovery and kernelization paragraph'
- assessment_id: core-initialization
  area: evidence
  topic: core initialization
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  summary: Supported within the stated source and mathematical scope.
  details: 'Fit ordinary SVDD to a fixed-size random sample of n0 observations and
    select the sampled observation z closest to that fitted center as a probable inlier.
    Choose a random sampled x, find its farthest observation y in the full dataset,
    and set D=||phi(x)-phi(y)|| and initial radius R1=D/k for k>1. Start the core
    with z and center c1=phi(z). This initial center is an observation, not the fitted
    sample center; the initial radius need not equal the one-point minimum-enclosing-ball
    radius. The probable-inlier choice is a heuristic, not a guarantee that z is normal.
    Locators: Section III-A, PDF pp2-3, Equation1'
- assessment_id: nearest-violator-and-radius-growth
  area: evidence
  topic: nearest violator and radius growth
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  summary: Supported within the stated source and mathematical scope.
  details: 'At iteration i, compute P_i={x in the full dataset:||phi(x)-c_i||>(1+epsilon)*R_i}.
    Stop when |P_i|<nu*N, with a strict inequality. Otherwise select the observation
    in P_i outside the current core that is nearest to c_i, enlarge the core, refit
    SVDD on that subset, and enforce R_(i+1)>=(1+delta*epsilon)*R_i for positive delta
    and epsilon. Repeat with the new center and radius. Nearest violating-point selection,
    soft subset refits and imposed radius growth distinguish this procedure from farthest-point
    hard-MEB core algorithms. Locators: Section III-B, PDF p3, steps1-7 and Equation2'
- assessment_id: expanded-quota-and-objective-boundary
  area: evidence
  topic: expanded quota and objective boundary
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'Termination checks the expanded radius (1+epsilon)*R, not the unexpanded
    sphere used by ordinary SVDD prediction. A permitted exact initialization illustrates
    the difference: use linear-kernel points0,1/10,1, nu=epsilon=1/5, n0=3, random
    x=0 and k=5/4. The initial sample SVDD has center1/2 and radius1/2; z=1/10 is
    its unique nearest observation. D=1 yields R1=4/5 and expanded radius24/25. No
    training point lies outside the expanded sphere, so the procedure stops immediately;
    one of three lies outside the original sphere, exceeding nu=1/5. The stopped sphere
    has full SVDD objective277/300 versus optimum1/4, a ratio277/75 greater than(1+epsilon)².
    This is exact curator arithmetic for allowed procedure choices, not a historical
    benchmark or claim about the paper’s experimental settings. Locators: Sections
    II and III-A/B, PDF pp2-3; curator derivation in research/discovery/core-set-svdd-boundaries.py'
- assessment_id: conditional-cost-analysis
  area: evidence
  topic: conditional cost analysis
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'The source derives O(M²*N+M⁴) work for M core additions using unit-cost
    kernel evaluations and a cubic subset-QP cost, and states M<=k/(delta*epsilon).
    Its O(N/epsilon²+epsilon^-4) form treats k and delta as fixed. The experiments
    instead set delta=0.01*epsilon; substitution into the same cost model gives O(N/epsilon^4+epsilon^-8)
    at fixed k. These expressions omit dimension-dependent kernel cost and input storage.
    The stated iteration argument uses the optimal full-data MEB radius as an enclosure
    bound, but an arbitrary current convex-hull center can require up to twice that
    radius: points0,2 have optimal radius1 at center1 and farthest distance2 from
    center0. The literal constant bound therefore needs its center assumptions checked;
    it is not a proof of soft-SVDD objective or decision-boundary approximation. Locators:
    Section III-C, PDF p3, Equation3; Section IV introduction, PDF pp3-4, parameter
    choices; curator dependence and center calculations in research/discovery/core-set-svdd-boundaries.py'
- assessment_id: subproblem-and-implementation-conventions
  area: evidence
  topic: subproblem and implementation conventions
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'A reimplementation must specify the subset SVDD penalty convention, radius-growth
    enforcement, numerical tolerances and tie or missing-free-support handling. Merely
    retaining the full-data cap1/(nu*N) on a smaller equality-simplex subproblem can
    make it infeasible: for N=100, nu=1/10 and a two-point core, the sum of upper
    bounds is1/5<1. Using the subset sample size gives a different cap. The paper
    says to run SVDD on the subset but does not expose a complete CSVDD implementation
    resolving all such choices. This feasibility calculation is not evidence that
    its historical code used the full-data cap. Locators: Sections II and III-B, PDF
    pp2-3, dual constraints and iterative steps5-6; curator exact cap calculation
    in research/discovery/core-set-svdd-boundaries.py'
- assessment_id: empirical-and-identity-scope
  area: evidence
  topic: empirical and identity scope
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  summary: Supported within the stated source and mathematical scope.
  details: 'Section IV explicitly names the method Core-set Support Vector Data Description,
    CSVDD. The two application studies concern BioID-derived face detection and MNIST
    one-class digit detection, with selected Gaussian kernels, nu values, tolerances,20
    random repetitions and historical MATLAB/MOSEK3, dd_tools and LIBSVM configurations.
    The reported time, memory failures and AUC trade-offs are specific to those data
    and implementations. They do not prove universal accuracy, speed or soft-objective
    approximation. This record does not equate CSVDD with every later method called
    core vector data description or CVDD. Locators: Sections IV-V, PDF pp3-6, Figures1-6
    and TablesI-III'
- assessment_id: adversarial-init-certificate
  area: consistency
  topic: Initialization versus fitted sample sphere
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: The exact example follows permitted initialization choices.
  details: For three linear-kernel observations, nu=1/5 makes cap5/3. Coefficients(1/2,0,1/2)
    give center1/2 and dual value1/4; the radius1/2 primal attains the same value
    and encloses every point. Observation1/10 is uniquely closest to that center.
    Choosing random x=0, k5/4 and epsilon1/5 yields initial center1/10 and radius4/5,
    not the sample center/radius. The source permits these choices; they differ from
    its experimental n0=20,k10. No iteration or inaccessible historical implementation
    is inferred.
- assessment_id: adversarial-quota-objective
  area: consistency
  topic: Expanded enclosure versus original prediction and soft objective
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: Termination alone supplies neither stronger conclusion.
  details: The expanded radius24/25 covers all three features, while the unexpanded
    radius4/5 rejects the point1. Its rejection fraction1/3 exceeds nu1/5. With the
    displayed linear slack penalty, the stopped primal value is277/300 and the exact
    optimum is1/4; ratio277/75 exceeds36/25. The source explicitly distinguishes hard-MEB
    theory from soft-SVDD. This calculation limits interpretations of the heuristic;
    it does not refute a benchmark result or claim the authors proved that stronger
    ratio.
- assessment_id: adversarial-complexity
  area: consistency
  topic: Conditional asymptotics and moving-center enclosure
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: The record preserves dependencies and qualifies the literal constant.
  details: The stated sum of i*N+i^3 costs is O(M²*N+M⁴). Holding delta fixed versus
    setting delta=.01epsilon changes the epsilon dependence. Unit kernel and cubic
    QP assumptions exclude input storage and dimension costs. Optimal MEB radius is
    not a radius sufficient at every current center; the0,2 example establishes that
    limited geometric point, not a complete runtime failure or independently repaired
    theorem.
- assessment_id: adversarial-subproblem
  area: consistency
  topic: Subset penalty, radius enforcement and numerical conventions
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - finite-boundaries
  summary: The feasibility warning is explicitly distinct from historical code behavior.
  details: A two-variable equality simplex with full-data caps1/10 is infeasible because
    the sum of caps is1/5. Rescaling by subset size changes that cap. The original
    procedure says to run SVDD on the subset and then enforce radius growth; the record
    does not invent the implementation, allege which cap it used, or silently assume
    free boundary support always exists.
- assessment_id: primary-evidence-locators
  area: provenance
  topic: Source version, complete reading and claim locators
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  summary: The two locator labels now match the original PDF.
  details: The original six-page PDF was fully read, including formulas,figures,tables
    and21 references. Section II lies on PDF2; experimental parameters precede IV-A
    and belong to the IV introduction on PDF4. The initial record cites II/PDF1-2
    and IV-A/PDF4. These are minor locator imprecisions, not unsupported formulas
    or invented full-text access. The author catalogue’s printed425-430 range is distinct
    from the unnumbered inspected copy.
- assessment_id: complete-fields-and-frontier
  area: provenance
  topic: Every selected field and bounded research coverage
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - identity
  - mapping
  - chu2004
  summary: All selected fields were inspected; remaining discovery is explicit.
  details: 'Read the full record after canonical source capture: stable ID,name,CSVDD
    alias,typed scope,definition,identity notes,all definition/claim citations,all
    seven claims,source authors/version/URL/hash/access time,AIO pin and mapping,limitations,DRAFT
    status and actual curation provenance. Five newly deduplicated cohorts retain
    uninspected methods;448 pending cohorts and partial work prevent a saturation
    claim. No model training or benchmark was executed.'
- assessment_id: locator-resolution
  area: evidence
  topic: Corrected source locators
  outcome: supported
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - prior-locator-finding
  summary: The locator finding is resolved.
  details: The underlying problem now cites Section II/PDF2 with precise display and
    prose scope; experimental settings cite the Section IV introduction/PDF3-4. Source
    metadata, algorithm, mapping, calculations and limitations remain intact.
findings:
- finding_id: source-locators
  issue_key: aimech-csvdd-source-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Point CSVDD claim locators to the actual source sections
  description: The initial underlying-soft-sphere claim cites Section II on PDF1-2,
    although that section and its primal/dual, center recovery and kernelization account
    are on PDF2. The cost claim assigns experimental parameter choices to IV-A, although
    they precede that subsection in the IV introduction on PDF4. Refine both locators;
    substantive formulas and exact calculations are supported.
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  field_paths:
  - claims[claim_id=underlying-soft-sphere-problem].evidence[0].locator
  - claims[claim_id=conditional-cost-analysis].evidence[0].locator
  - entries[id=AIMech:CoreSetSupportVectorDataDescription].claims
  evidence_ids:
  - chu2004
  - prior-locator-finding
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CoreSetSupportVectorDataDescription.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T101902Z-core-set-support-vector-data-description.json
    role: discovery_report
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/172
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261012T102345Z-core-set-svdd-open
    finding_id: source-locators
  disposition_reason: Both claim locators now identify the original PDF sections precisely;
    the discovery-report mirror and rendered page agree. Other record fields remain
    unchanged except updated curation time, checked structurally. Actual edit history
    was appended, final input hashes captured and all fields reread. Final required
    checks pass and ignored-inclusive lineage search was inspected.
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:CoreSetSupportVectorDataDescription
  evidence_ids:
  - chu2004
  - identity
  rationale: CSVDD is the original nearest-violator, soft-subset-fit and radius-growth
    training heuristic. Ordinary SVDD, squared-slack variants, hard-MEB CVM and sphere-based
    clustering have different scopes. Later CVDD usage and source versions are not
    exact aliases without further inspection.
limitations:
- Adversarial author self-review only; the record remains DRAFT.
- All six original CSVDD pages were visually read, including formulas, figures, tables
  and references. The author copy has no printed page labels; locators use PDF pages.
- No historical CSVDD implementation, numerical optimizer, model training, paid provider,
  data upload or benchmark was executed. Exact rational checks test displayed formulas
  and an allowed initialization only.
- Expanded-radius termination is not a quota at the unexpanded prediction radius,
  and the exact example also excludes an unconditional(1+epsilon)² full-objective
  guarantee. Source cost bounds retain parameter and center assumptions.
- RAPID, single-class MPM, LP novelty detection, F-SVDD and regularized multimodal
  variants remain incomplete primary-method readings. Secondary snippets and missing
  HTML equations are not mechanism evidence. Bibliographic version differences remain
  explicit.
- The collection reaches518 native DRAFT concepts;442 generated AIO records remain
  unchanged. There are448 pending cohorts plus partly addressed work, so discovery
  continues.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261012T102345Z-core-set-svdd-open
  relationship: Successor resolves the source-locator finding for its complete affected-target
    union.
links:
- https://github.com/CultureBotAI/AIMech/issues/172
tags:
- native-concepts
- kernel-training
- self-review
- discovery-ongoing
```
