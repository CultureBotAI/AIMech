# Scientific self-review of RAPID SVDD sampling: open

- Review: 20261012T104917Z-rapid-svdd-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T10:43:42Z
- Finished UTC: 2026-10-12T10:49:17Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Retain RAPID with source and guarantee qualifications. Minor operational-boundary wording and one locator need refinement.

## Scope And Provenance

Every field of one maintained RAPID record.

Selection: Exact maintained ID AIMech:RapidSupportVectorDataDescriptionSampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d6605b71a7da1075d57cb075aa296b45f2d68092.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RapidSupportVectorDataDescriptionSampling | data/curated/RapidSupportVectorDataDescriptionSampling.yaml | maintained | RAPID support vector data description sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RapidSupportVectorDataDescriptionSampling | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 124.18s (0:02:04)<br>Checked 442 record(s); 0 failed.<br>Checked 519 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 165 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 161,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RapidSupportVectorDataDescriptionSampling | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RapidSupportVectorDataDescriptionSampling | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RapidSupportVectorDataDescriptionSampling | Exited0 without output. |
| Exact RAPID boundaries | passed | True | AIMech:RapidSupportVectorDataDescriptionSampling | {"scope": "Exact formula and pseudocode illustrations; no historical Julia execution or benchmark.", "kernel": "k(x,y)=2^(-(x-y)^2), a specified standard Gaussian example.", "printed_old_set_threshold": {"points": [0, 1, 2], "initial": ["25/16", "2", "25/16"], "after_removing_middle": ["17/16", "1", "17/16"], "old_threshold": "1", "candidate_threshold": "17/16", "final": ["1/16", "1/2", "1"], "interpretation": "Printed Algorithm 2 accepts the middle removal; the candidate-set minimum would reject it. This is not the inspected public Julia code."}, "finite_global_boundary_nonidentity": {"points": [0, 1, 4], "alpha": ["1205376/4206007", "1198391/4206007", "1802240/4206007"], "weighted_boundary_score": "1804599/4206007", "unweighted_densities": ["98305/65536", "769/512", "65665/65536"], "derivative_factors": ["1198611/8412014", "-592128/4206007", "-3632841/2153475584"], "determinant": "3221209215/4294967296", "interpretation": "Distinct unweighted densities at three nonstationary hard-SVDD boundary crossings preclude a single common KDE level. This does not contradict an asymptotic consistency theorem or finite-set accept-all equivalence."}, "zero_percentage_code_convention": {"threshold": "81985/65536", "retained": 2, "total": 3, "interpretation": "The inspected midpoint/clamped-index formula excludes one uniquely least-dense point at percentage zero. No Julia code was run."}, "tie_convention": "Equal densities all pass the &gt;= split, regardless of percentage; exact requested removal fractions are not assured.", "current_loop_convention": "With m initial inliers, i=1 and while i&lt;m-2 permit at most m-3 accepted removals for m&gt;=3; smaller sets are unchanged."} |

## Scientific And Domain Assessments

### Source-specific identity and preprocessing role

identity: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Retain RAPID as a distinct preprocessing method.

A density-based training-subset selection method for support vector data description that prefilters low-density observations and greedily removes high-density inliers while testing a retained-density threshold on the original inlier set. RAPID denotes the Englhardt-Trittenbach-Kottke-Sick-Böhm density-pruning procedure, expanded as Reducing sAmples by Pruning of Inlier Densities. The intended candidate-set rule, printed pseudocode and versioned implementation conventions are distinguished below. It is neither an SVDD prediction rule nor a generic random-sampling algorithm. Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 518 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, RAPID, the publication title, DOI and arXiv identifier. All 126 distinct matched-text windows were read: these are prior discovery/review references, pending RAPID leads and ordinary uses of rapid, not an existing RAPID concept. All 125 semantic AIO rows and 114 native name/definition rows were read or reused after exact equality checks. Annotated AIO nodes and outgoing edges, and 29 contextual YAMLs with full readings, distinguish preprocessing, prediction tasks, neural components and neighboring subset-selection methods. Absence is bounded to this snapshot and maintained corpus.

### Local-to-broader AIO mapping

grounding: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

AIO preprocessing has broader scope without promising improved accuracy.

AIO:Preprocessing is broader: RAPID transforms the available observations into a selected training subset before an SVDD model is fitted. This mapping states the intended role of the procedure, not a guarantee of improved data quality or classifier accuracy. DataPreparation and TrainingStrategy are generic neighboring scopes, not exact names for this density-pruning method. BinaryClassification is the downstream accept/reject task rather than the selection algorithm. SupportVectorMachine describes a supervised category-separating network; KernelLayer is a neural component. SelectionAndSamplingBias is a bias condition, not a sample-selection procedure. Native SVDD fits a sphere; CSVDD grows a core using repeated SVDD fits, whereas RAPID prunes a density surrogate without those fits. CNNDD and CPDD use different distance-based consistency or coverage rules.

### density prefilter

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

For a finite observation set X and kernel k, compute the unnormalized empirical density d_X(x)=sum_{z in X} k(x,z). An expected-outlier parameter selects a low-density threshold; keep I={x in X:d_X(x)&gt;=theta_pre}, discard the other observations and recompute densities using only I as kernel centers. Subsequent subset selection prepares data for hard SVDD with C=1. This prefilter-plus-hard-fit procedure is not identical to fitting arbitrary-C soft SVDD on the original data. The paper leaves quantile index rounding, endpoints and ties under-specified; exact requested rejection fractions are not assured. Locators: Sections 2 and 4.1, PDF pp3-4 and8-10 / printed pp1351-1352 and1356-1358; Algorithm 1

### greedy pruning rule

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

The stated intended rule starts with S=I, selects a highest-density retained observation r, and subtracts its kernel contribution at every original inlier. For the candidate T=S minus {r}, define theta_T=min_{z in T} d_T(z). Accept the removal only if d_T(x)&gt;=theta_T for every x in I; otherwise stop and return the preceding S. The returned observations are used to train SVDD. The rule is a greedy density-surrogate selection, not repeated SVDD optimization, a globally minimum-cardinality subset, or a certified global solution of the mixed-integer problem. Locators: Section 4.3 prose, PDF pp13-14 / printed pp1361-1362; compare Algorithm 2; src/sampler/RAPID.jl, sample function, candidate mask update and feasibility test

### optimization and guarantee scope

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

The source SOP minimizes the range theta_max-theta_min of empirical densities over the original inlier set, subject to nonempty binary subset selection and a selected minimum-density witness. Minimum cardinality is a tie-breaker between SOP optima. Theorem 1 establishes a finite-inlier label statement for exactly uniform densities, not a quantitative bound on a continuous decision boundary under approximate uniformity. Theorem 2 uses separated density extrema and a small-bandwidth limiting argument, while its displayed comparison treats old extrema as if they remained extrema after removal. Those steps do not establish an unconditional finite-data SVDD boundary-preservation guarantee for greedy pruning. Locators: Section 4.2, PDF pp10-13 / printed pp1358-1361; Theorems 1-2, Equations 5-8 and Remarks 3-4

### finite density boundary distinction

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

Unweighted kernel-density level sets and fitted finite-sample SVDD decision regions are generally different. An exact curator example uses k(x,y)=2^(-(x-y)^2) on points 0,1,4. Positive hard-SVDD coefficients (1205376,1198391,1802240)/4206007 give the same weighted boundary score 1804599/4206007 at all three nonstationary boundary crossings. Their unweighted densities are respectively 98305/65536, 769/512 and 65665/65536, so no single unweighted-density threshold has all three as boundary points. This challenges an unqualified global identity, not the trivial fact that two rules can accept the same finite inlier set. The cited Vert-Vert results concern asymptotic density-level estimation under distribution, regularization and bandwidth conditions; they do not supply that finite global identity. Locators: Section 4.1 Characteristic 1 and following equivalence argument, PDF p9 / printed p1357; curator calculation in research/discovery/rapid-svdd-boundaries.py; Section 2 assumptions, Theorems 3,8,9 and Section 8.1, PDF pp3,5,7-8,33 / printed pp819,821,823-824,849

### printed pseudocode discrepancy

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

Printed Algorithm 2 subtracts r from the density sum but computes the minimum over the old S before deleting r. This differs from the candidate-set rule in the prose and inspected Julia code. For the specified Gaussian kernel 2^(-(x-y)^2), with retained inliers 0,1,2, removing the middle point leaves densities (17/16,1,17/16). The old-set minimum 1 accepts the removal, whereas the candidate-set minimum 17/16 rejects it because the removed middle observation is still an original inlier. The literal printed flow can continue to one point for this nonidentical dataset. This is exact pseudocode arithmetic after retaining all three inliers, not an execution of the public code or its percentage-prefilter convention. Locators: Section 4.3, Algorithm 2 lines 4-8, PDF p13 / printed p1361; single-point interpretation PDF p14 / printed p1362; curator calculation in research/discovery/rapid-svdd-boundaries.py; src/sampler/RAPID.jl, sample_mask[idx]=false before minimum

### versioned code conventions

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

At the inspected public commit, RAPID removes r from the candidate mask before the minimum test and reconstructs the final mask from accepted removals, undoing a failed candidate. For m initial inliers, its loop starts at i=1 and continues while i&lt;m-2, permitting at most m-3 accepted removals when m&gt;=3; smaller sets are unchanged. The percentage threshold clamps floor(p_out*N) to the one-based index range and averages adjacent sorted densities. With a unique minimum it can exclude one observation at p_out=0; equal-density ties can retain all observations. The source also offers a ground-truth mask and a mode deriving p_out from supplied labels, so all package configurations are not unsupervised. These are source-code observations, not verified historical experimental behavior. Locators: src/sampler/RAPID.jl complete sample function; src/pwc.jl OutlierPercentageThresholdStrategy, GroundTruthThresholdStrategy and split_masks; curator exact threshold illustration

### kernel and experiment version

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

The paper calls exp(-gamma*&#124;&#124;x-y&#124;&#124;) Gaussian in its displayed formula, omitting the squared norm. The inspected sampling code delegates to MLKernels.GaussianKernel; the evaluation-pinned MLKernels v0.4.0 implements exp(-gamma*&#124;&#124;x-y&#124;&#124;^2). These formulas must not be silently conflated. Although the MLKernels tree matches the evaluation manifest, its OneClassSampling entry points to an author-local development directory without a revision or tree hash. The inspected public sampling commit therefore cannot be identified as the exact experimental version from that manifest. Locators: Section 2 displayed kernel following Equation 1, PDF p3 / printed p1351; src/density_util.jl, get_gaussian_kernel and KDECache; squaredexponential.jl GaussianKernel alias, basefunction and kappa; src/basefunctions/squaredeuclidean.jl; Manifest.toml, MLKernels lines516-520 and OneClassSampling lines629-633

### cost and evaluation boundaries

evidence: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Supported within the stated source and mathematical scope.

The source gives O(N^2) sampling work under unit-cost kernel evaluation, and its optional Gram matrix and inspected KDE cache use quadratic storage. Input dimension, parameter selection and the downstream SVDD fit add costs. The experiments compare selected synthetic mixtures and real outlier datasets with specified bandwidth heuristics and prefiltering; the main setup supplies the true outlier percentage. Some costly competitors are excluded and the full-data baseline is limited to smaller datasets. These results do not establish universal speed, accuracy, compression or preserved generalization. The method still requires a kernel and an outlier-setting convention; no numerical performance advantage is curated. Locators: Section 4.3 cost, PDF p14 / printed p1362; Sections 5 and Appendix A, PDF pp14-24 / printed pp1362-1372; Figures 4-14 and Tables 2-3; src/density_util.jl, KDECache full kernel matrix

### Finite weighted SVDD versus unweighted density

consistency: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

The counterexample is bounded to exact finite global identity.

For distinct Gaussian-kernel points0,1,4, the exact Gram matrix has positive leading principal minors. Its equality-simplex stationary solution has positive coefficients below C=1, so it is the unique hard-SVDD dual optimum. Kalpha=q1 and sumalpha=1 imply squared radius1-q and acceptance weightedscore&gt;=q. Nonzero score derivatives at all three points establish actual boundary crossings. Unequal unweighted row sums prohibit a single KDE threshold at those three crossings. This does not challenge consistency in probability or finite-set accept-all agreement. Only the declared Vert-Vert passages were reviewed; no complete proof audit is claimed.

### Old versus candidate set in the minimum

consistency: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Paper prose, printed algorithm and public code are kept distinct.

All27 primary pages were visually read, with PDF3,8,11,13 reread for the final record. On0,1,2 the central removal passes the printed old-set threshold but fails the candidate-set rule. The example starts from a specified retained inlier set, not from the public percentage-prefilter result. The public code stops with at least3 when m&gt;=3 and thus does not perform this removal on three inliers; the record does not accuse that implementation of the printed discrepancy.

### Kernel implementation and historical dependency pin

provenance: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

The kernel dependency is pinned; the experimental sampling revision is not.

The MLKernels v0.4.0 Git tree matches the evaluation manifest exactly and its full squared-exponential/base-distance files implement squared Euclidean distance. The paper display omits the square. OneClassSampling uses an author-local manifest path with no revision, so the separately inspected public commit is not asserted to reproduce historical experiments. The recorded MLKernels author was verified from its license as Tim Thatcher.

### Quantile, label and cost conventions

consistency: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

No exact rejection fraction or universal unsupervised configuration is claimed.

One-based clamping and midpoint selection can reject a unique minimum at percentage0. Equal densities can all survive. Ground-truth masks and label-derived percentages are explicit alternatives; they are not conflated with a supplied unsupervised estimate. Quadratic unit-kernel sampling work excludes feature cost, bandwidth choice and downstream fitting; no universal empirical advantage is curated.

### Nonempty input and candidate minimum

evidence: concern. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Minor mechanism and locator refinement required.

The source uses a unit-diagonal kernel and density sorting requires nonempty input. Algorithm2 caps removals at &#124;I&#124;-1, returning a singleton rather than taking the minimum of an empty candidate; the public code has a stricter minimum-size convention, already recorded. The initial mechanism description omits these operational assumptions, and its discrepancy locator should include deletion line9. This finding concerns AIMech completeness, not a new source theorem or an attributed code repair.

### Complete selected record and research scope

provenance: supported. Targets: AIMech:RapidSupportVectorDataDescriptionSampling.

Every selected record field was read after canonical capture.

Read stable ID,name,aliases,kind,definition,identity notes,definition evidence,all8 claims and citations,all5 source records including authors/access/version/hashes,exact AIO snapshot,mapping,limitations,DRAFT status and actual curation provenance. Both new source cohorts remain pending full-method reading.449 pending cohorts and partial work prevent saturation. No Julia code, model training or benchmark was run.

## Findings

### pruning-boundaries: State the RAPID kernel and nonempty-candidate conventions

minor / open / confirmed; issue key: aimech-rapid-pruning-boundaries.

The initial density-prefilter claim omits nonempty input and k(x,x)=1. The intended greedy rule should stop at a singleton instead of leaving an empty-candidate minimum undefined. The printed-discrepancy locator should extend through deletion line9. The separately documented public-code minimum-size convention is supported and must be retained.

## Recommended Actions And Acceptance Checks

### state-boundaries

Clarify the input/kernel setting and intended singleton stop, extend the line locator, mirror the report, append edit history and save a successor review after checks.

- Nonempty finite input and unit kernel diagonal are explicit.
- Only nonempty candidate subsets are tested; singleton return is explicit.
- Algorithm2 locator includes deletion line9.
- Public-code convention and exact calculations remain unchanged.
- Required checks pass and successor retains issue key and complete target.

## Category Boundaries

- retain: AIMech:RapidSupportVectorDataDescriptionSampling. The density-pruning procedure differs from sphere fitting, nearest-violator CSVDD core growth, nearest-neighbor condensation and prototype covering. Pseudocode and implementation discrepancies are preserved within one source-scoped concept, without inventing corrected algorithms as separate records.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T104313Z-rapid-svdd-sampling.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 518 preceding native IDs, names and aliases. No normalized identity collision was found. Fixed-string whole-word searches included ignored and hidden files in both checkouts, expanded names, RAPID, the publication title, DOI and arXiv identifier. All 126 distinct matched-text windows were read: these are prior discovery/review references, pending RAPID leads and ordinary uses of rapid, not an existing RAPID concept. All 125 semantic AIO rows and 114 native name/definition rows were read or reused after exact equality checks. Annotated AIO nodes and outgoing edges, and 29 contextual YAMLs with full readings, distinguish preprocessing, prediction tasks, neural components and neighboring subset-selection methods. Absence is bounded to this snapshot and maintained corpus. |
| mapping | sources/aio/aio.json; Eleven declared annotated CLASS nodes and outgoing edges;29 full-read contextual YAMLs | supports | AIO:Preprocessing is broader: RAPID transforms the available observations into a selected training subset before an SVDD model is fitted. This mapping states the intended role of the procedure, not a guarantee of improved data quality or classifier accuracy. DataPreparation and TrainingStrategy are generic neighboring scopes, not exact names for this density-pruning method. BinaryClassification is the downstream accept/reject task rather than the selection algorithm. SupportVectorMachine describes a supervised category-separating network; KernelLayer is a neural component. SelectionAndSamplingBias is a bias condition, not a sample-selection procedure. Native SVDD fits a sphere; CSVDD grows a core using repeated SVDD fits, whereas RAPID prunes a density surrogate without those fits. CNNDD and CPDD use different distance-based consistency or coverage rules. |
| finite-boundaries | research/discovery/rapid-svdd-boundaries.py | supports | Exact rational Gaussian examples establish the old-S versus candidate-S pseudocode discrepancy, finite hard-SVDD/unweighted-KDE boundary nonidentity and the inspected percentage formula at zero. Static loop analysis establishes the public code minimum-size convention. No historical code was executed. |
| englhardt2022 | https://link.springer.com/content/pdf/10.1007/s10994-022-06149-0.pdf; Version of record, 7 April 2022, Machine Learning 111:1349-1375. All 27 PDF pages visually read, including figures, tables, algorithms and references. Printed page = PDF page + 1348. | supports | Efficient SVDD sampling with approximation guarantees for the decision boundary. Version of record, 7 April 2022, Machine Learning 111:1349-1375. All 27 PDF pages visually read, including figures, tables, algorithms and references. Printed page = PDF page + 1348. |
| rapid-code | https://github.com/englhardt/OneClassSampling.jl/tree/a4964843b884cd25dd953d424be928145425e94a; Commit a4964843b884cd25dd953d424be928145425e94a. Complete RAPID.jl, pwc.jl, density_util.jl, sampler_util.jl, sampler_base.jl and README read. SHA-256 identifies RAPID.jl; other inspected file hashes are retained in the discovery report. Code was read, not executed. | supports | OneClassSampling.jl RAPID implementation and density utilities. Commit a4964843b884cd25dd953d424be928145425e94a. Complete RAPID.jl, pwc.jl, density_util.jl, sampler_util.jl, sampler_base.jl and README read. SHA-256 identifies RAPID.jl; other inspected file hashes are retained in the discovery report. Code was read, not executed. |
| evaluation-manifest | https://github.com/englhardt/ocs-evaluation/blob/051b6f27d4085c00d951801cabf2310c24a6b316/Manifest.toml; Commit 051b6f27d4085c00d951801cabf2310c24a6b316. MLKernels and OneClassSampling entries inspected; whole manifest not scientifically reviewed or executed. | supports | ocs-evaluation dependency manifest. Commit 051b6f27d4085c00d951801cabf2310c24a6b316. MLKernels and OneClassSampling entries inspected; whole manifest not scientifically reviewed or executed. |
| mlkernels | https://github.com/trthatcher/MLKernels.jl/blob/38e6aec6a621b446e46d76ee82c908177a22d407/src/kernelfunctions/mercer/squaredexponential.jl; v0.4.0, commit 38e6aec6a621b446e46d76ee82c908177a22d407, tree d8ae6ac28480a25ddaae9ad9108371035ef9a346 exactly matching the evaluation manifest. Squared-exponential, exponential and squared-Euclidean files fully read; SHA-256 identifies squaredexponential.jl. | supports | MLKernels.jl Gaussian kernel implementation. v0.4.0, commit 38e6aec6a621b446e46d76ee82c908177a22d407, tree d8ae6ac28480a25ddaae9ad9108371035ef9a346 exactly matching the evaluation manifest. Squared-exponential, exponential and squared-Euclidean files fully read; SHA-256 identifies squaredexponential.jl. |
| vert2006 | https://jmlr.csail.mit.edu/papers/volume7/vert06a/vert06a.pdf; JMLR 7:817-854 (2006), 38-page PDF. Scoped context reading: visual PDF pages 3,5,7,8,33 (printed 819,821,823,824,849), with Section 2 and 8 extracted text. This is not a complete proof audit. | supports | Consistency and Convergence Rates of One-Class SVMs and Related Algorithms. JMLR 7:817-854 (2006), 38-page PDF. Scoped context reading: visual PDF pages 3,5,7,8,33 (printed 819,821,823,824,849), with Section 2 and 8 extracted text. This is not a complete proof audit. |

## Limits And Additional Notes

- Author self-review only; record remains DRAFT.
- All27 final RAPID PDF pages were visually read, including14 figures,3 tables,3 algorithms,2 theorems, remarks and references. The cited consistency paper was read only in the specified scope, not as a complete proof audit.
- Public author source and the evaluation-pinned kernel dependency were inspected without executing Julia, installing their dependencies, fitting models or benchmarking. The evaluation manifest does not pin the sampling package revision.
- Exact rational calculations distinguish printed pseudocode, intended candidate-set feasibility, finite SVDD versus unweighted KDE boundaries and percentage-threshold conventions. They are curator illustrations, not historical experimental results.
- Primary abstracts support the new source leads; their full mathematical methods and version comparisons remain pending. An unsuccessful project link or noisy correction search is not evidence that sources or corrections do not exist.
- There are519 native DRAFT records and442 unchanged generated AIO records. The frontier has449 pending cohorts plus partially addressed work; no saturation claim is made.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T104917Z-rapid-svdd-open
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific self-review of RAPID SVDD sampling: open'
started_at: '2026-10-12T10:43:42Z'
finished_at: '2026-10-12T10:49:17Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read all27 final-paper pages, inspected
    versioned code and the pinned kernel dependency, challenged finite-boundary and
    pseudocode claims with exact arithmetic, and reread every field after canonical
    capture. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Retain RAPID with source and guarantee qualifications. Minor operational-boundary
  wording and one locator need refinement.
source:
  git_revision: d6605b71a7da1075d57cb075aa296b45f2d68092
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
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
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
  - path: data/curated/CondensedNearestNeighborDataDomainDescription.yaml
    sha256: 7a9a70a3bda10bd66dec59c5560471f68af26c9603f707c878c48f69a427a02a
    role: context
  - path: data/curated/CondensedPrototypeBasedDomainDescription.yaml
    sha256: 97c4c87b9023f63170576613b537eb81964d7365ae1600105ac5f911ecca43a8
    role: context
  - path: data/curated/CoreSetSupportVectorDataDescription.yaml
    sha256: f02d6459178882f29b748532bf817d1477721d2f7402fbfe91305ac2eb6076f2
    role: context
  - path: data/curated/CoreVectorMachine.yaml
    sha256: ac41d81c889250fb49a7593cc9dfccbf1fc56f979c4584eb60ea2c5d420619bf
    role: context
  - path: data/curated/CoreVectorRegression.yaml
    sha256: 35ed0d44bad43789851e83ce7bea8ca0303030002d474861dabe8fe276054e97
    role: context
  - path: data/curated/FastCondensedPrototypeBasedDomainDescription.yaml
    sha256: af96a4d9b08517140732b60a7e9e7c2883ea2eb7e008f718fceeafeb42f32cdc
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
  - path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
    sha256: 77a63946ca8c4f95a38b9d763b4158bd2d020eac512d5ca02671d743719137eb
    role: target
  - path: data/curated/SemidefiniteMaximumMarginClustering.yaml
    sha256: 9cfe6597d65d6a9dae4040f56bade8cba946a4b09c82c8f0b5adbec8b66a59dc
    role: context
  - path: data/curated/SupportVectorClustering.yaml
    sha256: f15f79f69443b23faa8247bb4fb67d86caeb2a80a86ae0e8c97dd247e152ad3a
    role: context
  - path: data/curated/SupportVectorDataDescription.yaml
    sha256: 45e181fa0ce8eeeda5c10e6e3fbce658b05bfd650e7c9c6bf77501d7fa315b7b
    role: context
  - path: research/discovery/20261012T104313Z-rapid-svdd-sampling.json
    sha256: 782d50311b738d60faf42fe7e7a6c35ac333e6238da4502e99c0a49e3881b474
    role: context
  - path: research/discovery/rapid-svdd-boundaries.py
    sha256: 0ea61fab1928326ab95383a2b96764f80a23fbf558f3034fd77de9beada974e3
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
- target_id: AIMech:RapidSupportVectorDataDescriptionSampling
  path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
  label: RAPID support vector data description sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
    role: maintained
scope:
  description: Every field of one maintained RAPID record.
  selection: Exact maintained ID AIMech:RapidSupportVectorDataDescriptionSampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  exclusions:
  - target: Contextual AIO/native records
    reason: Identity and mapping context only, not renewed scientific approval.
  - target: Historical execution and benchmarks
    reason: Code was read but not executed; historical sampling revision is not pinned.
  - target: Vert-Vert complete proof
    reason: Only declared theorem/assumption passages reviewed.
  - target: Remaining frontier
    reason: 449 pending cohorts and partly addressed work remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 124.18s (0:02:04)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 519 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 165 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 161,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
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
  - AIMech:RapidSupportVectorDataDescriptionSampling
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
  - AIMech:RapidSupportVectorDataDescriptionSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: exact-boundaries
  name: Exact RAPID boundaries
  command: python3 research/discovery/rapid-svdd-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Exact formula and pseudocode illustrations; no historical Julia
    execution or benchmark.", "kernel": "k(x,y)=2^(-(x-y)^2), a specified standard
    Gaussian example.", "printed_old_set_threshold": {"points": [0, 1, 2], "initial":
    ["25/16", "2", "25/16"], "after_removing_middle": ["17/16", "1", "17/16"], "old_threshold":
    "1", "candidate_threshold": "17/16", "final": ["1/16", "1/2", "1"], "interpretation":
    "Printed Algorithm 2 accepts the middle removal; the candidate-set minimum would
    reject it. This is not the inspected public Julia code."}, "finite_global_boundary_nonidentity":
    {"points": [0, 1, 4], "alpha": ["1205376/4206007", "1198391/4206007", "1802240/4206007"],
    "weighted_boundary_score": "1804599/4206007", "unweighted_densities": ["98305/65536",
    "769/512", "65665/65536"], "derivative_factors": ["1198611/8412014", "-592128/4206007",
    "-3632841/2153475584"], "determinant": "3221209215/4294967296", "interpretation":
    "Distinct unweighted densities at three nonstationary hard-SVDD boundary crossings
    preclude a single common KDE level. This does not contradict an asymptotic consistency
    theorem or finite-set accept-all equivalence."}, "zero_percentage_code_convention":
    {"threshold": "81985/65536", "retained": 2, "total": 3, "interpretation": "The
    inspected midpoint/clamped-index formula excludes one uniquely least-dense point
    at percentage zero. No Julia code was run."}, "tie_convention": "Equal densities
    all pass the >= split, regardless of percentage; exact requested removal fractions
    are not assured.", "current_loop_convention": "With m initial inliers, i=1 and
    while i<m-2 permit at most m-3 accepted removals for m>=3; smaller sets are unchanged."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T104313Z-rapid-svdd-sampling.json
  accessed_at: '2026-10-12T10:43:42Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 518
    preceding native IDs, names and aliases. No normalized identity collision was
    found. Fixed-string whole-word searches included ignored and hidden files in both
    checkouts, expanded names, RAPID, the publication title, DOI and arXiv identifier.
    All 126 distinct matched-text windows were read: these are prior discovery/review
    references, pending RAPID leads and ordinary uses of rapid, not an existing RAPID
    concept. All 125 semantic AIO rows and 114 native name/definition rows were read
    or reused after exact equality checks. Annotated AIO nodes and outgoing edges,
    and 29 contextual YAMLs with full readings, distinguish preprocessing, prediction
    tasks, neural components and neighboring subset-selection methods. Absence is
    bounded to this snapshot and maintained corpus.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison and included as explicit identity
    terms in the full-text whole-word searches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eleven declared annotated CLASS nodes and outgoing edges;29 full-read contextual
    YAMLs
  accessed_at: '2026-10-12T10:43:42Z'
  support: supports
  summary: 'AIO:Preprocessing is broader: RAPID transforms the available observations
    into a selected training subset before an SVDD model is fitted. This mapping states
    the intended role of the procedure, not a guarantee of improved data quality or
    classifier accuracy. DataPreparation and TrainingStrategy are generic neighboring
    scopes, not exact names for this density-pruning method. BinaryClassification
    is the downstream accept/reject task rather than the selection algorithm. SupportVectorMachine
    describes a supervised category-separating network; KernelLayer is a neural component.
    SelectionAndSamplingBias is a bias condition, not a sample-selection procedure.
    Native SVDD fits a sphere; CSVDD grows a core using repeated SVDD fits, whereas
    RAPID prunes a density surrogate without those fits. CNNDD and CPDD use different
    distance-based consistency or coverage rules.'
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/rapid-svdd-boundaries.py
  accessed_at: '2026-10-12T10:43:42Z'
  snapshot_sha256: 0ea61fab1928326ab95383a2b96764f80a23fbf558f3034fd77de9beada974e3
  support: supports
  summary: Exact rational Gaussian examples establish the old-S versus candidate-S
    pseudocode discrepancy, finite hard-SVDD/unweighted-KDE boundary nonidentity and
    the inspected percentage formula at zero. Static loop analysis establishes the
    public code minimum-size convention. No historical code was executed.
- evidence_id: englhardt2022
  kind: primary_source
  reference: https://link.springer.com/content/pdf/10.1007/s10994-022-06149-0.pdf
  locator: Version of record, 7 April 2022, Machine Learning 111:1349-1375. All 27
    PDF pages visually read, including figures, tables, algorithms and references.
    Printed page = PDF page + 1348.
  accessed_at: '2026-10-12T10:22:47Z'
  support: supports
  summary: Efficient SVDD sampling with approximation guarantees for the decision
    boundary. Version of record, 7 April 2022, Machine Learning 111:1349-1375. All
    27 PDF pages visually read, including figures, tables, algorithms and references.
    Printed page = PDF page + 1348.
  snapshot_sha256: 1e926feb7ef74f17490a5de4fb959fe6d9ecdb91e439628fb40f7fa6cabb317e
- evidence_id: rapid-code
  kind: primary_source
  reference: https://github.com/englhardt/OneClassSampling.jl/tree/a4964843b884cd25dd953d424be928145425e94a
  locator: Commit a4964843b884cd25dd953d424be928145425e94a. Complete RAPID.jl, pwc.jl,
    density_util.jl, sampler_util.jl, sampler_base.jl and README read. SHA-256 identifies
    RAPID.jl; other inspected file hashes are retained in the discovery report. Code
    was read, not executed.
  accessed_at: '2026-10-12T10:41:52Z'
  support: supports
  summary: OneClassSampling.jl RAPID implementation and density utilities. Commit
    a4964843b884cd25dd953d424be928145425e94a. Complete RAPID.jl, pwc.jl, density_util.jl,
    sampler_util.jl, sampler_base.jl and README read. SHA-256 identifies RAPID.jl;
    other inspected file hashes are retained in the discovery report. Code was read,
    not executed.
  snapshot_sha256: 8a13216d478d0d5a98a16eade79374480cabee430d9f3eb7c7b4f117263e0c23
- evidence_id: evaluation-manifest
  kind: primary_source
  reference: https://github.com/englhardt/ocs-evaluation/blob/051b6f27d4085c00d951801cabf2310c24a6b316/Manifest.toml
  locator: Commit 051b6f27d4085c00d951801cabf2310c24a6b316. MLKernels and OneClassSampling
    entries inspected; whole manifest not scientifically reviewed or executed.
  accessed_at: '2026-10-12T10:41:52Z'
  support: supports
  summary: ocs-evaluation dependency manifest. Commit 051b6f27d4085c00d951801cabf2310c24a6b316.
    MLKernels and OneClassSampling entries inspected; whole manifest not scientifically
    reviewed or executed.
  snapshot_sha256: f165f86c8013a12f446c642b894a62ba5562d676de273597a0f4f744fa74ea43
- evidence_id: mlkernels
  kind: primary_source
  reference: https://github.com/trthatcher/MLKernels.jl/blob/38e6aec6a621b446e46d76ee82c908177a22d407/src/kernelfunctions/mercer/squaredexponential.jl
  locator: v0.4.0, commit 38e6aec6a621b446e46d76ee82c908177a22d407, tree d8ae6ac28480a25ddaae9ad9108371035ef9a346
    exactly matching the evaluation manifest. Squared-exponential, exponential and
    squared-Euclidean files fully read; SHA-256 identifies squaredexponential.jl.
  accessed_at: '2026-10-12T10:36:00Z'
  support: supports
  summary: MLKernels.jl Gaussian kernel implementation. v0.4.0, commit 38e6aec6a621b446e46d76ee82c908177a22d407,
    tree d8ae6ac28480a25ddaae9ad9108371035ef9a346 exactly matching the evaluation
    manifest. Squared-exponential, exponential and squared-Euclidean files fully read;
    SHA-256 identifies squaredexponential.jl.
  snapshot_sha256: 407693f7b5d9c038d1bc7f6d5194677186db71ea8bcdad149d959e3476f7e76b
- evidence_id: vert2006
  kind: primary_source
  reference: https://jmlr.csail.mit.edu/papers/volume7/vert06a/vert06a.pdf
  locator: 'JMLR 7:817-854 (2006), 38-page PDF. Scoped context reading: visual PDF
    pages 3,5,7,8,33 (printed 819,821,823,824,849), with Section 2 and 8 extracted
    text. This is not a complete proof audit.'
  accessed_at: '2026-10-12T10:34:53Z'
  support: supports
  summary: 'Consistency and Convergence Rates of One-Class SVMs and Related Algorithms.
    JMLR 7:817-854 (2006), 38-page PDF. Scoped context reading: visual PDF pages 3,5,7,8,33
    (printed 819,821,823,824,849), with Section 2 and 8 extracted text. This is not
    a complete proof audit.'
  snapshot_sha256: e1bf86aad7a250b956c563965e0efbed903eae20428047f710685aac22422b3e
assessments:
- assessment_id: identity-definition
  area: identity
  topic: Source-specific identity and preprocessing role
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - identity
  - englhardt2022
  - rapid-code
  summary: Retain RAPID as a distinct preprocessing method.
  details: 'A density-based training-subset selection method for support vector data
    description that prefilters low-density observations and greedily removes high-density
    inliers while testing a retained-density threshold on the original inlier set.
    RAPID denotes the Englhardt-Trittenbach-Kottke-Sick-Böhm density-pruning procedure,
    expanded as Reducing sAmples by Pruning of Inlier Densities. The intended candidate-set
    rule, printed pseudocode and versioned implementation conventions are distinguished
    below. It is neither an SVDD prediction rule nor a generic random-sampling algorithm.
    Compared all 442 pinned AIO IDs, labels and scoped synonyms with all 518 preceding
    native IDs, names and aliases. No normalized identity collision was found. Fixed-string
    whole-word searches included ignored and hidden files in both checkouts, expanded
    names, RAPID, the publication title, DOI and arXiv identifier. All 126 distinct
    matched-text windows were read: these are prior discovery/review references, pending
    RAPID leads and ordinary uses of rapid, not an existing RAPID concept. All 125
    semantic AIO rows and 114 native name/definition rows were read or reused after
    exact equality checks. Annotated AIO nodes and outgoing edges, and 29 contextual
    YAMLs with full readings, distinguish preprocessing, prediction tasks, neural
    components and neighboring subset-selection methods. Absence is bounded to this
    snapshot and maintained corpus.'
- assessment_id: preprocessing-mapping
  area: grounding
  topic: Local-to-broader AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - mapping
  - englhardt2022
  summary: AIO preprocessing has broader scope without promising improved accuracy.
  details: 'AIO:Preprocessing is broader: RAPID transforms the available observations
    into a selected training subset before an SVDD model is fitted. This mapping states
    the intended role of the procedure, not a guarantee of improved data quality or
    classifier accuracy. DataPreparation and TrainingStrategy are generic neighboring
    scopes, not exact names for this density-pruning method. BinaryClassification
    is the downstream accept/reject task rather than the selection algorithm. SupportVectorMachine
    describes a supervised category-separating network; KernelLayer is a neural component.
    SelectionAndSamplingBias is a bias condition, not a sample-selection procedure.
    Native SVDD fits a sphere; CSVDD grows a core using repeated SVDD fits, whereas
    RAPID prunes a density surrogate without those fits. CNNDD and CPDD use different
    distance-based consistency or coverage rules.'
- assessment_id: density-prefilter
  area: evidence
  topic: density prefilter
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  summary: Supported within the stated source and mathematical scope.
  details: 'For a finite observation set X and kernel k, compute the unnormalized
    empirical density d_X(x)=sum_{z in X} k(x,z). An expected-outlier parameter selects
    a low-density threshold; keep I={x in X:d_X(x)>=theta_pre}, discard the other
    observations and recompute densities using only I as kernel centers. Subsequent
    subset selection prepares data for hard SVDD with C=1. This prefilter-plus-hard-fit
    procedure is not identical to fitting arbitrary-C soft SVDD on the original data.
    The paper leaves quantile index rounding, endpoints and ties under-specified;
    exact requested rejection fractions are not assured. Locators: Sections 2 and
    4.1, PDF pp3-4 and8-10 / printed pp1351-1352 and1356-1358; Algorithm 1'
- assessment_id: greedy-pruning-rule
  area: evidence
  topic: greedy pruning rule
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  summary: Supported within the stated source and mathematical scope.
  details: 'The stated intended rule starts with S=I, selects a highest-density retained
    observation r, and subtracts its kernel contribution at every original inlier.
    For the candidate T=S minus {r}, define theta_T=min_{z in T} d_T(z). Accept the
    removal only if d_T(x)>=theta_T for every x in I; otherwise stop and return the
    preceding S. The returned observations are used to train SVDD. The rule is a greedy
    density-surrogate selection, not repeated SVDD optimization, a globally minimum-cardinality
    subset, or a certified global solution of the mixed-integer problem. Locators:
    Section 4.3 prose, PDF pp13-14 / printed pp1361-1362; compare Algorithm 2; src/sampler/RAPID.jl,
    sample function, candidate mask update and feasibility test'
- assessment_id: optimization-and-guarantee-scope
  area: evidence
  topic: optimization and guarantee scope
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  summary: Supported within the stated source and mathematical scope.
  details: 'The source SOP minimizes the range theta_max-theta_min of empirical densities
    over the original inlier set, subject to nonempty binary subset selection and
    a selected minimum-density witness. Minimum cardinality is a tie-breaker between
    SOP optima. Theorem 1 establishes a finite-inlier label statement for exactly
    uniform densities, not a quantitative bound on a continuous decision boundary
    under approximate uniformity. Theorem 2 uses separated density extrema and a small-bandwidth
    limiting argument, while its displayed comparison treats old extrema as if they
    remained extrema after removal. Those steps do not establish an unconditional
    finite-data SVDD boundary-preservation guarantee for greedy pruning. Locators:
    Section 4.2, PDF pp10-13 / printed pp1358-1361; Theorems 1-2, Equations 5-8 and
    Remarks 3-4'
- assessment_id: finite-density-boundary-distinction
  area: evidence
  topic: finite density boundary distinction
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - vert2006
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'Unweighted kernel-density level sets and fitted finite-sample SVDD decision
    regions are generally different. An exact curator example uses k(x,y)=2^(-(x-y)^2)
    on points 0,1,4. Positive hard-SVDD coefficients (1205376,1198391,1802240)/4206007
    give the same weighted boundary score 1804599/4206007 at all three nonstationary
    boundary crossings. Their unweighted densities are respectively 98305/65536, 769/512
    and 65665/65536, so no single unweighted-density threshold has all three as boundary
    points. This challenges an unqualified global identity, not the trivial fact that
    two rules can accept the same finite inlier set. The cited Vert-Vert results concern
    asymptotic density-level estimation under distribution, regularization and bandwidth
    conditions; they do not supply that finite global identity. Locators: Section
    4.1 Characteristic 1 and following equivalence argument, PDF p9 / printed p1357;
    curator calculation in research/discovery/rapid-svdd-boundaries.py; Section 2
    assumptions, Theorems 3,8,9 and Section 8.1, PDF pp3,5,7-8,33 / printed pp819,821,823-824,849'
- assessment_id: printed-pseudocode-discrepancy
  area: evidence
  topic: printed pseudocode discrepancy
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'Printed Algorithm 2 subtracts r from the density sum but computes the
    minimum over the old S before deleting r. This differs from the candidate-set
    rule in the prose and inspected Julia code. For the specified Gaussian kernel
    2^(-(x-y)^2), with retained inliers 0,1,2, removing the middle point leaves densities
    (17/16,1,17/16). The old-set minimum 1 accepts the removal, whereas the candidate-set
    minimum 17/16 rejects it because the removed middle observation is still an original
    inlier. The literal printed flow can continue to one point for this nonidentical
    dataset. This is exact pseudocode arithmetic after retaining all three inliers,
    not an execution of the public code or its percentage-prefilter convention. Locators:
    Section 4.3, Algorithm 2 lines 4-8, PDF p13 / printed p1361; single-point interpretation
    PDF p14 / printed p1362; curator calculation in research/discovery/rapid-svdd-boundaries.py;
    src/sampler/RAPID.jl, sample_mask[idx]=false before minimum'
- assessment_id: versioned-code-conventions
  area: evidence
  topic: versioned code conventions
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - rapid-code
  - finite-boundaries
  summary: Supported within the stated source and mathematical scope.
  details: 'At the inspected public commit, RAPID removes r from the candidate mask
    before the minimum test and reconstructs the final mask from accepted removals,
    undoing a failed candidate. For m initial inliers, its loop starts at i=1 and
    continues while i<m-2, permitting at most m-3 accepted removals when m>=3; smaller
    sets are unchanged. The percentage threshold clamps floor(p_out*N) to the one-based
    index range and averages adjacent sorted densities. With a unique minimum it can
    exclude one observation at p_out=0; equal-density ties can retain all observations.
    The source also offers a ground-truth mask and a mode deriving p_out from supplied
    labels, so all package configurations are not unsupervised. These are source-code
    observations, not verified historical experimental behavior. Locators: src/sampler/RAPID.jl
    complete sample function; src/pwc.jl OutlierPercentageThresholdStrategy, GroundTruthThresholdStrategy
    and split_masks; curator exact threshold illustration'
- assessment_id: kernel-and-experiment-version
  area: evidence
  topic: kernel and experiment version
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  - mlkernels
  - evaluation-manifest
  summary: Supported within the stated source and mathematical scope.
  details: 'The paper calls exp(-gamma*||x-y||) Gaussian in its displayed formula,
    omitting the squared norm. The inspected sampling code delegates to MLKernels.GaussianKernel;
    the evaluation-pinned MLKernels v0.4.0 implements exp(-gamma*||x-y||^2). These
    formulas must not be silently conflated. Although the MLKernels tree matches the
    evaluation manifest, its OneClassSampling entry points to an author-local development
    directory without a revision or tree hash. The inspected public sampling commit
    therefore cannot be identified as the exact experimental version from that manifest.
    Locators: Section 2 displayed kernel following Equation 1, PDF p3 / printed p1351;
    src/density_util.jl, get_gaussian_kernel and KDECache; squaredexponential.jl GaussianKernel
    alias, basefunction and kappa; src/basefunctions/squaredeuclidean.jl; Manifest.toml,
    MLKernels lines516-520 and OneClassSampling lines629-633'
- assessment_id: cost-and-evaluation-boundaries
  area: evidence
  topic: cost and evaluation boundaries
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  summary: Supported within the stated source and mathematical scope.
  details: 'The source gives O(N^2) sampling work under unit-cost kernel evaluation,
    and its optional Gram matrix and inspected KDE cache use quadratic storage. Input
    dimension, parameter selection and the downstream SVDD fit add costs. The experiments
    compare selected synthetic mixtures and real outlier datasets with specified bandwidth
    heuristics and prefiltering; the main setup supplies the true outlier percentage.
    Some costly competitors are excluded and the full-data baseline is limited to
    smaller datasets. These results do not establish universal speed, accuracy, compression
    or preserved generalization. The method still requires a kernel and an outlier-setting
    convention; no numerical performance advantage is curated. Locators: Section 4.3
    cost, PDF p14 / printed p1362; Sections 5 and Appendix A, PDF pp14-24 / printed
    pp1362-1372; Figures 4-14 and Tables 2-3; src/density_util.jl, KDECache full kernel
    matrix'
- assessment_id: adversarial-boundary-proof
  area: consistency
  topic: Finite weighted SVDD versus unweighted density
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - vert2006
  - finite-boundaries
  summary: The counterexample is bounded to exact finite global identity.
  details: For distinct Gaussian-kernel points0,1,4, the exact Gram matrix has positive
    leading principal minors. Its equality-simplex stationary solution has positive
    coefficients below C=1, so it is the unique hard-SVDD dual optimum. Kalpha=q1
    and sumalpha=1 imply squared radius1-q and acceptance weightedscore>=q. Nonzero
    score derivatives at all three points establish actual boundary crossings. Unequal
    unweighted row sums prohibit a single KDE threshold at those three crossings.
    This does not challenge consistency in probability or finite-set accept-all agreement.
    Only the declared Vert-Vert passages were reviewed; no complete proof audit is
    claimed.
- assessment_id: adversarial-pseudocode
  area: consistency
  topic: Old versus candidate set in the minimum
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  - finite-boundaries
  summary: Paper prose, printed algorithm and public code are kept distinct.
  details: All27 primary pages were visually read, with PDF3,8,11,13 reread for the
    final record. On0,1,2 the central removal passes the printed old-set threshold
    but fails the candidate-set rule. The example starts from a specified retained
    inlier set, not from the public percentage-prefilter result. The public code stops
    with at least3 when m>=3 and thus does not perform this removal on three inliers;
    the record does not accuse that implementation of the printed discrepancy.
- assessment_id: adversarial-version
  area: provenance
  topic: Kernel implementation and historical dependency pin
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  - mlkernels
  - evaluation-manifest
  summary: The kernel dependency is pinned; the experimental sampling revision is
    not.
  details: The MLKernels v0.4.0 Git tree matches the evaluation manifest exactly and
    its full squared-exponential/base-distance files implement squared Euclidean distance.
    The paper display omits the square. OneClassSampling uses an author-local manifest
    path with no revision, so the separately inspected public commit is not asserted
    to reproduce historical experiments. The recorded MLKernels author was verified
    from its license as Tim Thatcher.
- assessment_id: adversarial-parameters
  area: consistency
  topic: Quantile, label and cost conventions
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  - finite-boundaries
  summary: No exact rejection fraction or universal unsupervised configuration is
    claimed.
  details: One-based clamping and midpoint selection can reject a unique minimum at
    percentage0. Equal densities can all survive. Ground-truth masks and label-derived
    percentages are explicit alternatives; they are not conflated with a supplied
    unsupervised estimate. Quadratic unit-kernel sampling work excludes feature cost,
    bandwidth choice and downstream fitting; no universal empirical advantage is curated.
- assessment_id: mechanism-boundaries
  area: evidence
  topic: Nonempty input and candidate minimum
  outcome: concern
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - englhardt2022
  - rapid-code
  summary: Minor mechanism and locator refinement required.
  details: The source uses a unit-diagonal kernel and density sorting requires nonempty
    input. Algorithm2 caps removals at |I|-1, returning a singleton rather than taking
    the minimum of an empty candidate; the public code has a stricter minimum-size
    convention, already recorded. The initial mechanism description omits these operational
    assumptions, and its discrepancy locator should include deletion line9. This finding
    concerns AIMech completeness, not a new source theorem or an attributed code repair.
- assessment_id: all-fields
  area: provenance
  topic: Complete selected record and research scope
  outcome: supported
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - identity
  - mapping
  - englhardt2022
  - rapid-code
  - evaluation-manifest
  - mlkernels
  - vert2006
  summary: Every selected record field was read after canonical capture.
  details: Read stable ID,name,aliases,kind,definition,identity notes,definition evidence,all8
    claims and citations,all5 source records including authors/access/version/hashes,exact
    AIO snapshot,mapping,limitations,DRAFT status and actual curation provenance.
    Both new source cohorts remain pending full-method reading.449 pending cohorts
    and partial work prevent saturation. No Julia code, model training or benchmark
    was run.
findings:
- finding_id: pruning-boundaries
  issue_key: aimech-rapid-pruning-boundaries
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: State the RAPID kernel and nonempty-candidate conventions
  description: The initial density-prefilter claim omits nonempty input and k(x,x)=1.
    The intended greedy rule should stop at a singleton instead of leaving an empty-candidate
    minimum undefined. The printed-discrepancy locator should extend through deletion
    line9. The separately documented public-code minimum-size convention is supported
    and must be retained.
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  field_paths:
  - claims[claim_id=density-prefilter].statement
  - claims[claim_id=greedy-pruning-rule].statement
  - claims[claim_id=printed-pseudocode-discrepancy].evidence[0].locator
  evidence_ids:
  - englhardt2022
  - rapid-code
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T104313Z-rapid-svdd-sampling.json
    role: discovery_report
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/174
actions:
- action_id: state-boundaries
  description: Clarify the input/kernel setting and intended singleton stop, extend
    the line locator, mirror the report, append edit history and save a successor
    review after checks.
  finding_ids:
  - pruning-boundaries
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RapidSupportVectorDataDescriptionSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T104313Z-rapid-svdd-sampling.json
    role: discovery_report
  acceptance_checks:
  - Nonempty finite input and unit kernel diagonal are explicit.
  - Only nonempty candidate subsets are tested; singleton return is explicit.
  - Algorithm2 locator includes deletion line9.
  - Public-code convention and exact calculations remain unchanged.
  - Required checks pass and successor retains issue key and complete target.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:RapidSupportVectorDataDescriptionSampling
  evidence_ids:
  - identity
  - englhardt2022
  - rapid-code
  rationale: The density-pruning procedure differs from sphere fitting, nearest-violator
    CSVDD core growth, nearest-neighbor condensation and prototype covering. Pseudocode
    and implementation discrepancies are preserved within one source-scoped concept,
    without inventing corrected algorithms as separate records.
limitations:
- Author self-review only; record remains DRAFT.
- All27 final RAPID PDF pages were visually read, including14 figures,3 tables,3 algorithms,2
  theorems, remarks and references. The cited consistency paper was read only in the
  specified scope, not as a complete proof audit.
- Public author source and the evaluation-pinned kernel dependency were inspected
  without executing Julia, installing their dependencies, fitting models or benchmarking.
  The evaluation manifest does not pin the sampling package revision.
- Exact rational calculations distinguish printed pseudocode, intended candidate-set
  feasibility, finite SVDD versus unweighted KDE boundaries and percentage-threshold
  conventions. They are curator illustrations, not historical experimental results.
- Primary abstracts support the new source leads; their full mathematical methods
  and version comparisons remain pending. An unsuccessful project link or noisy correction
  search is not evidence that sources or corrections do not exist.
- There are519 native DRAFT records and442 unchanged generated AIO records. The frontier
  has449 pending cohorts plus partially addressed work; no saturation claim is made.
related_reviews: []
links:
- https://github.com/CultureBotAI/AIMech/issues/174
tags:
- native-concepts
- preprocessing
- self-review
- discovery-ongoing
```
