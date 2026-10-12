# Scientific author self-review of derivative-observation GP regression

- Review: 20261012T205431Z-derivative-observation-gp
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T20:49:01Z
- Finished UTC: 2026-10-12T20:54:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the Gaussian derivative-value conditioning algorithm with an explicit related AIO task mapping and limits on compression, uncertainty and system identification; no actionable defect found in the captured record.

## Scope And Provenance

All maintained fields of the derivative-observation GP regression record.

Selection: Exact maintained ID: AIMech:DerivativeObservationGaussianProcessRegression
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb6fa7803142d4c3282204efdc7ab3423373e125.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DerivativeObservationGaussianProcessRegression | data/curated/DerivativeObservationGaussianProcessRegression.yaml | maintained | Derivative-observation Gaussian process regression |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DerivativeObservationGaussianProcessRegression | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 164.03s (0:02:44)<br>Checked 442 record(s); 0 failed.<br>Checked 540 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 187 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 185,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DerivativeObservationGaussianProcessRegression | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:DerivativeObservationGaussianProcessRegression | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:DerivativeObservationGaussianProcessRegression | Exited0 without output. |
| Analytic derivative-conditioning and dependence checks | passed | True | AIMech:DerivativeObservationGaussianProcessRegression | {"scope": "Curator analytic Gaussian-conditioning and exact rational illustrations; not a reproduction of Figures 2\u20135 or source software.", "unit_rbf_at_x1": {"f0_1_derivative0": {"mean": 0.6065306597126334, "variance": 0.26424111765711533}, "f0_1_derivative1": {"mean": 1.2130613194252668, "variance": 0.26424111765711533}, "derivative0_noise_variance1": {"mean": 0.6065306597126334, "variance": 0.4481808382428365}}, "finite_separation": [{"h": 1.0, "derivative_conditioned_variance": 0.26424111765711533, "two_exact_values_variance_at_h": 0.0}, {"h": 0.5, "derivative_conditioned_variance": 0.026499021160743763, "two_exact_values_variance_at_h": 0.0}, {"h": 0.1, "derivative_conditioned_variance": 4.966791334021052e-05, "two_exact_values_variance_at_h": 0.0}], "ols_at_x_0_1_2_unit_noise": {"intercept_slope_covariance": [["5/6", "-1/2"], ["-1/2", "1/2"]], "prediction_variance_at_x1_full_covariance": "1/3", "prediction_variance_at_x1_diagonal_only": "4/3"}, "duplicate_observation": {"correct_posterior_variance": "1/2", "false_independent_posterior_variance": "1/3"}, "limits": ["Conditioning formulas use fixed unit squared-exponential hyperparameters and known Gaussian noise variances.", "The two-value comparison is at a fixed nonzero separation, not the derivative limit as separation tends to zero.", "The OLS example is an unregularized illustrative covariance calculation, not validation of arbitrary ridge-prior scaling.", "The copied-observation example demonstrates dependence; it does not estimate the error in the paper\u2019s datasets."]} |

## Scientific And Domain Assessments

### Derivative values versus generic priors and virtual signs

identity: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

Retain a scoped Gaussian-conditioning algorithm identity.

The definition requires value and derivative-value observations, differentiated kernel blocks and a Gaussian error model. Generic GPR permits other observation structures. The existing monotonicity method uses sign factors and EP. The full local-linearization identification pipeline and direct/indirect kriging identity comparisons remain explicit follow-ups; the broad kriging label was not assigned as an alias. The one descriptive alias is noncolliding and denotes the same scoped method.

### Task relationship and rejected placements

grounding: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The single related regression mapping is justified.

The method estimates a response relation, but the AIO task does not name this algorithm. Linear fitting is optional observation preprocessing, GLM requires another predictor/link structure, time-series analysis is an application, and a graphical-model task does not specify the differentiated-kernel procedure. No exact or upstream subclass assertion is made.

### joint-kernel-derivatives

evidence: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The claim is supported within its stated assumptions.

For a sufficiently mean-square differentiable scalar GP f, form a joint Gaussian vector of function values and selected partial derivative values. Its covariance blocks are k(x,x_prime), derivatives with respect to the appropriate first or second kernel argument, and mixed derivatives with respect to both arguments. Differentiate the latent kernel, then add the observation-error covariance. The inspected squared-exponential construction gives cov(f_prime(x),f(x_prime))=-(x-x_prime)*exp(-(x-x_prime)²/2) in the one-dimensional unit-kernel case. Modeling all derivatives through the same scalar function enforces mutual integrability of the latent derivative field; it does not force noisy observed gradients to be matched exactly. Locators: Sections 2.1–2.2, Equations 1–6 and Figure 1, PDF pp. 2–3; Section 4, PDF pp. 6–7

### gaussian-conditioning

evidence: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The claim is supported within its stated assumptions.

With fixed kernel parameters and additive jointly Gaussian observation errors independent of the latent function, combine the value and derivative observations in one Gaussian conditioning calculation. A full error covariance can retain correlations among observations. Posterior means and covariances are available for both values and derivatives. The paper fits kernel hyperparameters by joint marginal likelihood; conditional exactness under the specified Gaussian model does not integrate hyperparameter uncertainty or guarantee a globally optimal fit. Locators: Sections 2.1–2.3, Equations 2–3 and covariance construction, PDF pp. 2–4

### local-linearization-summaries

evidence: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The claim is supported within its stated assumptions.

An optional system-identification construction fits a local linear model to perturbation data around an operating point. Its intercept supplies a function-value observation and its D slopes supply D partial-derivative observations, with the estimated full (D+1)-dimensional coefficient covariance added as an error block. Treating different blocks as independent requires the corresponding error assumption. These summaries can reduce the dense GP system size when many locally linear observations are replaced by fewer coefficients; they are not generally a lossless representation of arbitrary nonlinear data. Locators: Section 2.3, Equations 7–9, PDF pp. 3–4; Section 4, PDF pp. 6–7

### mean-and-uncertainty

evidence: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The claim is supported within its stated assumptions.

Derivative observations can change both the posterior mean and its uncertainty. For a zero-mean unit squared-exponential GP conditioned on exact f(0)=1 and f_prime(0)=d, the mean at x is exp(-x²/2)*(1+x*d) and latent variance is 1-exp(-x²)*(1+x²). The zero-derivative symmetric example leaves the value-only mean unchanged, but d=1 changes it. At x=1 the variance is 1-2/e, about 0.2642. These are fixed-parameter curator conditioning calculations, not a reproduction of the paper’s fitted examples. Locators: Sections 2.1–2.2 and 2.4, Equations 2–6 and Figure 2, PDF pp. 2–5; analytic checks in research/discovery/derivative-gp-boundaries.py

### finite-difference-and-dependence

evidence: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The claim is supported within its stated assumptions.

Two exact function values at distinct locations are not literally the same observations as an exact derivative and a function value. With the unit kernel, f(0) and f(1) fix the variance at x=1 to zero, whereas f(0) and f_prime(0) leave variance 1-2/e. The source’s exact-equivalence wording therefore requires a derivative-limit qualification. Estimated slopes and reused raw data can also share errors: treating them as independent evidence can misstate uncertainty. A curator scalar Gaussian example gives posterior variance 1/2 from one noisy observation, but 1/3 when a copy is incorrectly counted as independent. Locators: Section 2.3 discussion following Equation 9, PDF p. 4; fixed-parameter finite-separation and dependence checks in research/discovery/derivative-gp-boundaries.py

### Latent kernel, observation error and integrability

consistency: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The record separates latent derivative covariance from measurement error.

The unit-RBF derivative in the first argument is -(x-x_prime)k; the opposite argument has the opposite sign and the mixed derivative is (1-delta²)k. Independent white observation noise is added after differentiation. The sufficiently differentiable scalar prior supplies compatible latent derivatives; observations with errors need not satisfy exact integrability or interpolation. No claim that all GP kernels are differentiable or all dynamical systems stable follows.

### Linearization summaries, prior scaling and dependent reuse

scope: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

Compression and coefficient covariance are appropriately qualified.

The source uses an estimated full coefficient block, not separate independent slopes. The exact unregularized three-point example has coefficient covariance [[5/6,-1/2],[-1/2,1/2]]; prediction variance at x1 is1/3 with that block and4/3 if its covariance is dropped. This is not validation of the source ridge-prior scaling. Block independence and independence from reused raw observations are assumptions. The copied-observation example checks dependence without claiming a measured error in the source data.

### Two nearby values and a derivative-limit statement

consistency: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

The source literal finite-separation equivalence is not repeated as a theorem.

For exact f0 and f_prime0 under the unit kernel, variance at h is1-exp(-h²)(1+h²)&gt;0 for h!=0; an exact observation at h fixes its variance to0. The calculator verifies h1,0.5,0.1. At small h the variance tends to0, which is consistent with a derivative limit without making finite observations identical. The exact value of d can change the mean even though fixed-parameter covariance does not depend on observed values.

### System-identification illustrations and global claims

scope: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

No universal identification or performance guarantee is asserted.

The source explicitly says equilibrium linearisations alone do not specify global dynamics. The record retains this qualification and labels the150-point comparison as an illustration. Source time-index/noise notation requires resolution before any numerical reproduction; the record does not reproduce or silently repair it. Kernel fitting can change variance comparisons, so fixed-model conditioning is separated from refitting.

### Complete record and report mirror

provenance: supported. Targets: AIMech:DerivativeObservationGaussianProcessRegression.

All maintained fields are consistent with the captured inputs.

Read stable ID, name, one alias, algorithm kind, definition and evidence, identity scope, five typed claims and their locators, exact primary version/access/hash, pinned AIO snapshot, one related mapping, five limitations and actual DRAFT curation timestamps. The report entry equals the YAML. PDF page indices avoid conflicting bibliographic ranges. No primary implementation or empirical experiment was executed; the record remains DRAFT.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T204844Z-derivative-observation-gp.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms and 539 native IDs, names and aliases against the proposed name, ID, descriptive variants and neighboring gradient-enhanced terminology: no normalized identity match. Ignored- and hidden-inclusive full-text searches in the recovery worktree, older discovery worktree and original Documents checkout returned 23, zero and zero lines. All returned lines were inspected; they contain virtual-sign contextual mentions, a pending derivative-observation cohort or an unrelated recursive-estimation derivative calculation. Read all 34 semantic AIO rows, 66 native name/definition neighbors, five complete annotated AIO CLASS nodes with incident edges and their generated records, and both complete native GP neighbors. Generic GPR does not require derivative observations; the virtual-derivative monotonicity algorithm uses non-Gaussian sign likelihoods and EP. This record specifies Gaussian conditioning on derivative values. Local-linearization summaries are an optional source of those observations, not a second identity established here. Direct gradient-enhanced kriging may overlap; the umbrella also includes indirect Taylor pseudo-observations, so no blanket alias is asserted without its own full-method comparison. The absence assessment is bounded to the inspected snapshot and records. |
| mapping | sources/aio/aio.json | supports | Read all 34 semantic AIO rows, 66 native name/definition neighbors, five full annotated CLASS nodes with incident edges, their generated records and both complete GP neighbors. RegressionAnalysis supplies a task relationship; four other targets were rejected with explicit scope reasons. |
| paper | https://proceedings.neurips.cc/paper_files/paper/2002/file/5b8e4fd39d9786228649a8a8bec4e008-Paper.pdf; Official Advances in Neural Information Processing Systems 15 (NIPS 2002) proceedings PDF, eight pages without printed page numbers; also cited as the 2003 volume. All eight pages, five figures and references visually read. Citations use PDF page indices because secondary bibliographic page ranges differ. | supports | All eight original pages, five figures and references visually read. After capture, reread PDF3–4 covariance derivatives, local regression summaries, full coefficient-error covariance, finite-value equivalence wording and hyperparameter fitting. Equations 2–6, Figure2 and the PDF6–7 global-identification limitations were checked against the record. |
| calculation | research/discovery/derivative-gp-boundaries.py | supports | Fixed-parameter Gaussian formulas distinguish mean/variance effects, finite values from derivative limits, full coefficient covariance from its diagonal, and a dependent copy from independent evidence. These are curator calculations, not source-code or empirical replication. |

## Limits And Additional Notes

- Author self-review only; the record remains DRAFT.
- Original synchronization and old round141 cleanup await explicit approval after automatic review rejection; the readable original checkout was included in identity searches.
- Added one native DRAFT algorithm, bringing the total to540 with442 unchanged generated records. Discovery remains active:479 pending and53 partly addressed cohorts plus other unresolved scopes; no saturation claim.
- All eight primary derivative-GP pages and figures were visually read; formulas on PDF3–5 were reread while resolving boundary claims. Flow and detection PDFs were already read during previous preparation but remain pending their unresolved coupling and score-normalization audits. No implementation or empirical model was executed.
- The primary PDF’s text extraction garbles mathematical notation; equations were verified from rendered pages. Source bibliographic page ranges differ, so all claim locators use exact PDF page indices.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T205431Z-derivative-observation-gp
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of derivative-observation GP regression
started_at: '2026-10-12T20:49:01Z'
finished_at: '2026-10-12T20:54:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent challenged its own identity, mapping, kernel
    derivatives, finite-observation equivalence and uncertainty claims against primary
    passages and analytic calculations. This is author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the Gaussian derivative-value conditioning algorithm with an explicit
  related AIO task mapping and limits on compression, uncertainty and system identification;
  no actionable defect found in the captured record.
source:
  git_revision: cb6fa7803142d4c3282204efdc7ab3423373e125
  state: working_tree
  inputs:
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/curated/DerivativeObservationGaussianProcessRegression.yaml
    sha256: 888850faa100e14b96057c516e7d65d01ed2932a142577d101660c73dbf90905
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/MonotonicGaussianProcessWithVirtualDerivatives.yaml
    sha256: 9b72af4401c813c1fb3d51aa894a080ca96b86b37a051d8e7bb86a73b54e9cfd
    role: context
  - path: research/discovery/20261012T204844Z-derivative-observation-gp.json
    sha256: 94b0f8ca8ac778016bf5d221b667ba0ba32d13dd9e4d9249dc7d746650bc3497
    role: context
  - path: research/discovery/derivative-gp-boundaries.py
    sha256: 9c316ca0160f2494c3500e4ff793dcd6a76054461d3c1bb2ea79523c6d1a0415
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
- target_id: AIMech:DerivativeObservationGaussianProcessRegression
  path: data/curated/DerivativeObservationGaussianProcessRegression.yaml
  label: Derivative-observation Gaussian process regression
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DerivativeObservationGaussianProcessRegression.yaml
    role: maintained
scope:
  description: All maintained fields of the derivative-observation GP regression record.
  selection: 'Exact maintained ID: AIMech:DerivativeObservationGaussianProcessRegression'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  exclusions:
  - target: Specialized local/global identification, gradient-enhanced kriging, flow
      and detection methods
    reason: Separate identity and full-method audits remain pending.
  - target: Source implementation and empirical replication
    reason: Paper reading and curator analytic checks only; no training or implementation
      execution.
  - target: Contextual native and generated neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 164.03s (0:02:44)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 540 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 187 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 185,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
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
  - AIMech:DerivativeObservationGaussianProcessRegression
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
  - AIMech:DerivativeObservationGaussianProcessRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculations
  name: Analytic derivative-conditioning and dependence checks
  command: python3 research/discovery/derivative-gp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Curator analytic Gaussian-conditioning and exact rational illustrations;
    not a reproduction of Figures 2\u20135 or source software.", "unit_rbf_at_x1":
    {"f0_1_derivative0": {"mean": 0.6065306597126334, "variance": 0.26424111765711533},
    "f0_1_derivative1": {"mean": 1.2130613194252668, "variance": 0.26424111765711533},
    "derivative0_noise_variance1": {"mean": 0.6065306597126334, "variance": 0.4481808382428365}},
    "finite_separation": [{"h": 1.0, "derivative_conditioned_variance": 0.26424111765711533,
    "two_exact_values_variance_at_h": 0.0}, {"h": 0.5, "derivative_conditioned_variance":
    0.026499021160743763, "two_exact_values_variance_at_h": 0.0}, {"h": 0.1, "derivative_conditioned_variance":
    4.966791334021052e-05, "two_exact_values_variance_at_h": 0.0}], "ols_at_x_0_1_2_unit_noise":
    {"intercept_slope_covariance": [["5/6", "-1/2"], ["-1/2", "1/2"]], "prediction_variance_at_x1_full_covariance":
    "1/3", "prediction_variance_at_x1_diagonal_only": "4/3"}, "duplicate_observation":
    {"correct_posterior_variance": "1/2", "false_independent_posterior_variance":
    "1/3"}, "limits": ["Conditioning formulas use fixed unit squared-exponential hyperparameters
    and known Gaussian noise variances.", "The two-value comparison is at a fixed
    nonzero separation, not the derivative limit as separation tends to zero.", "The
    OLS example is an unregularized illustrative covariance calculation, not validation
    of arbitrary ridge-prior scaling.", "The copied-observation example demonstrates
    dependence; it does not estimate the error in the paper\u2019s datasets."]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T204844Z-derivative-observation-gp.json
  accessed_at: '2026-10-12T20:49:01Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms and 539 native
    IDs, names and aliases against the proposed name, ID, descriptive variants and
    neighboring gradient-enhanced terminology: no normalized identity match. Ignored-
    and hidden-inclusive full-text searches in the recovery worktree, older discovery
    worktree and original Documents checkout returned 23, zero and zero lines. All
    returned lines were inspected; they contain virtual-sign contextual mentions,
    a pending derivative-observation cohort or an unrelated recursive-estimation derivative
    calculation. Read all 34 semantic AIO rows, 66 native name/definition neighbors,
    five complete annotated AIO CLASS nodes with incident edges and their generated
    records, and both complete native GP neighbors. Generic GPR does not require derivative
    observations; the virtual-derivative monotonicity algorithm uses non-Gaussian
    sign likelihoods and EP. This record specifies Gaussian conditioning on derivative
    values. Local-linearization summaries are an optional source of those observations,
    not a second identity established here. Direct gradient-enhanced kriging may overlap;
    the umbrella also includes indirect Taylor pseudo-observations, so no blanket
    alias is asserted without its own full-method comparison. The absence assessment
    is bounded to the inspected snapshot and records.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T20:49:01Z'
  support: supports
  summary: Read all 34 semantic AIO rows, 66 native name/definition neighbors, five
    full annotated CLASS nodes with incident edges, their generated records and both
    complete GP neighbors. RegressionAnalysis supplies a task relationship; four other
    targets were rejected with explicit scope reasons.
- evidence_id: paper
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2002/file/5b8e4fd39d9786228649a8a8bec4e008-Paper.pdf
  locator: Official Advances in Neural Information Processing Systems 15 (NIPS 2002)
    proceedings PDF, eight pages without printed page numbers; also cited as the 2003
    volume. All eight pages, five figures and references visually read. Citations
    use PDF page indices because secondary bibliographic page ranges differ.
  accessed_at: '2026-10-12T15:03:09Z'
  snapshot_sha256: 72c7205d979b8c836c4cee652ec8959f17368c94be40c1a446ce47978991fff1
  support: supports
  summary: All eight original pages, five figures and references visually read. After
    capture, reread PDF3–4 covariance derivatives, local regression summaries, full
    coefficient-error covariance, finite-value equivalence wording and hyperparameter
    fitting. Equations 2–6, Figure2 and the PDF6–7 global-identification limitations
    were checked against the record.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/derivative-gp-boundaries.py
  accessed_at: '2026-10-12T20:49:01Z'
  snapshot_sha256: 9c316ca0160f2494c3500e4ff793dcd6a76054461d3c1bb2ea79523c6d1a0415
  support: supports
  summary: Fixed-parameter Gaussian formulas distinguish mean/variance effects, finite
    values from derivative limits, full coefficient covariance from its diagonal,
    and a dependent copy from independent evidence. These are curator calculations,
    not source-code or empirical replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Derivative values versus generic priors and virtual signs
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - identity
  - paper
  summary: Retain a scoped Gaussian-conditioning algorithm identity.
  details: The definition requires value and derivative-value observations, differentiated
    kernel blocks and a Gaussian error model. Generic GPR permits other observation
    structures. The existing monotonicity method uses sign factors and EP. The full
    local-linearization identification pipeline and direct/indirect kriging identity
    comparisons remain explicit follow-ups; the broad kriging label was not assigned
    as an alias. The one descriptive alias is noncolliding and denotes the same scoped
    method.
- assessment_id: grounding
  area: grounding
  topic: Task relationship and rejected placements
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - mapping
  - paper
  summary: The single related regression mapping is justified.
  details: The method estimates a response relation, but the AIO task does not name
    this algorithm. Linear fitting is optional observation preprocessing, GLM requires
    another predictor/link structure, time-series analysis is an application, and
    a graphical-model task does not specify the differentiated-kernel procedure. No
    exact or upstream subclass assertion is made.
- assessment_id: joint-kernel-derivatives
  area: evidence
  topic: joint-kernel-derivatives
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The claim is supported within its stated assumptions.
  details: 'For a sufficiently mean-square differentiable scalar GP f, form a joint
    Gaussian vector of function values and selected partial derivative values. Its
    covariance blocks are k(x,x_prime), derivatives with respect to the appropriate
    first or second kernel argument, and mixed derivatives with respect to both arguments.
    Differentiate the latent kernel, then add the observation-error covariance. The
    inspected squared-exponential construction gives cov(f_prime(x),f(x_prime))=-(x-x_prime)*exp(-(x-x_prime)²/2)
    in the one-dimensional unit-kernel case. Modeling all derivatives through the
    same scalar function enforces mutual integrability of the latent derivative field;
    it does not force noisy observed gradients to be matched exactly. Locators: Sections
    2.1–2.2, Equations 1–6 and Figure 1, PDF pp. 2–3; Section 4, PDF pp. 6–7'
- assessment_id: gaussian-conditioning
  area: evidence
  topic: gaussian-conditioning
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The claim is supported within its stated assumptions.
  details: 'With fixed kernel parameters and additive jointly Gaussian observation
    errors independent of the latent function, combine the value and derivative observations
    in one Gaussian conditioning calculation. A full error covariance can retain correlations
    among observations. Posterior means and covariances are available for both values
    and derivatives. The paper fits kernel hyperparameters by joint marginal likelihood;
    conditional exactness under the specified Gaussian model does not integrate hyperparameter
    uncertainty or guarantee a globally optimal fit. Locators: Sections 2.1–2.3, Equations
    2–3 and covariance construction, PDF pp. 2–4'
- assessment_id: local-linearization-summaries
  area: evidence
  topic: local-linearization-summaries
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The claim is supported within its stated assumptions.
  details: 'An optional system-identification construction fits a local linear model
    to perturbation data around an operating point. Its intercept supplies a function-value
    observation and its D slopes supply D partial-derivative observations, with the
    estimated full (D+1)-dimensional coefficient covariance added as an error block.
    Treating different blocks as independent requires the corresponding error assumption.
    These summaries can reduce the dense GP system size when many locally linear observations
    are replaced by fewer coefficients; they are not generally a lossless representation
    of arbitrary nonlinear data. Locators: Section 2.3, Equations 7–9, PDF pp. 3–4;
    Section 4, PDF pp. 6–7'
- assessment_id: mean-and-uncertainty
  area: evidence
  topic: mean-and-uncertainty
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The claim is supported within its stated assumptions.
  details: 'Derivative observations can change both the posterior mean and its uncertainty.
    For a zero-mean unit squared-exponential GP conditioned on exact f(0)=1 and f_prime(0)=d,
    the mean at x is exp(-x²/2)*(1+x*d) and latent variance is 1-exp(-x²)*(1+x²).
    The zero-derivative symmetric example leaves the value-only mean unchanged, but
    d=1 changes it. At x=1 the variance is 1-2/e, about 0.2642. These are fixed-parameter
    curator conditioning calculations, not a reproduction of the paper’s fitted examples.
    Locators: Sections 2.1–2.2 and 2.4, Equations 2–6 and Figure 2, PDF pp. 2–5; analytic
    checks in research/discovery/derivative-gp-boundaries.py'
- assessment_id: finite-difference-and-dependence
  area: evidence
  topic: finite-difference-and-dependence
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The claim is supported within its stated assumptions.
  details: 'Two exact function values at distinct locations are not literally the
    same observations as an exact derivative and a function value. With the unit kernel,
    f(0) and f(1) fix the variance at x=1 to zero, whereas f(0) and f_prime(0) leave
    variance 1-2/e. The source’s exact-equivalence wording therefore requires a derivative-limit
    qualification. Estimated slopes and reused raw data can also share errors: treating
    them as independent evidence can misstate uncertainty. A curator scalar Gaussian
    example gives posterior variance 1/2 from one noisy observation, but 1/3 when
    a copy is incorrectly counted as independent. Locators: Section 2.3 discussion
    following Equation 9, PDF p. 4; fixed-parameter finite-separation and dependence
    checks in research/discovery/derivative-gp-boundaries.py'
- assessment_id: covariance
  area: consistency
  topic: Latent kernel, observation error and integrability
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The record separates latent derivative covariance from measurement error.
  details: The unit-RBF derivative in the first argument is -(x-x_prime)k; the opposite
    argument has the opposite sign and the mixed derivative is (1-delta²)k. Independent
    white observation noise is added after differentiation. The sufficiently differentiable
    scalar prior supplies compatible latent derivatives; observations with errors
    need not satisfy exact integrability or interpolation. No claim that all GP kernels
    are differentiable or all dynamical systems stable follows.
- assessment_id: compression
  area: scope
  topic: Linearization summaries, prior scaling and dependent reuse
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: Compression and coefficient covariance are appropriately qualified.
  details: The source uses an estimated full coefficient block, not separate independent
    slopes. The exact unregularized three-point example has coefficient covariance
    [[5/6,-1/2],[-1/2,1/2]]; prediction variance at x1 is1/3 with that block and4/3
    if its covariance is dropped. This is not validation of the source ridge-prior
    scaling. Block independence and independence from reused raw observations are
    assumptions. The copied-observation example checks dependence without claiming
    a measured error in the source data.
- assessment_id: finite-values
  area: consistency
  topic: Two nearby values and a derivative-limit statement
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  - calculation
  summary: The source literal finite-separation equivalence is not repeated as a theorem.
  details: For exact f0 and f_prime0 under the unit kernel, variance at h is1-exp(-h²)(1+h²)>0
    for h!=0; an exact observation at h fixes its variance to0. The calculator verifies
    h1,0.5,0.1. At small h the variance tends to0, which is consistent with a derivative
    limit without making finite observations identical. The exact value of d can change
    the mean even though fixed-parameter covariance does not depend on observed values.
- assessment_id: applications
  area: scope
  topic: System-identification illustrations and global claims
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - paper
  summary: No universal identification or performance guarantee is asserted.
  details: The source explicitly says equilibrium linearisations alone do not specify
    global dynamics. The record retains this qualification and labels the150-point
    comparison as an illustration. Source time-index/noise notation requires resolution
    before any numerical reproduction; the record does not reproduce or silently repair
    it. Kernel fitting can change variance comparisons, so fixed-model conditioning
    is separated from refitting.
- assessment_id: all-fields
  area: provenance
  topic: Complete record and report mirror
  outcome: supported
  target_ids:
  - AIMech:DerivativeObservationGaussianProcessRegression
  evidence_ids:
  - identity
  - mapping
  - paper
  - calculation
  summary: All maintained fields are consistent with the captured inputs.
  details: Read stable ID, name, one alias, algorithm kind, definition and evidence,
    identity scope, five typed claims and their locators, exact primary version/access/hash,
    pinned AIO snapshot, one related mapping, five limitations and actual DRAFT curation
    timestamps. The report entry equals the YAML. PDF page indices avoid conflicting
    bibliographic ranges. No primary implementation or empirical experiment was executed;
    the record remains DRAFT.
findings: []
actions: []
limitations:
- Author self-review only; the record remains DRAFT.
- Original synchronization and old round141 cleanup await explicit approval after
  automatic review rejection; the readable original checkout was included in identity
  searches.
- Added one native DRAFT algorithm, bringing the total to540 with442 unchanged generated
  records. Discovery remains active:479 pending and53 partly addressed cohorts plus
  other unresolved scopes; no saturation claim.
- All eight primary derivative-GP pages and figures were visually read; formulas on
  PDF3–5 were reread while resolving boundary claims. Flow and detection PDFs were
  already read during previous preparation but remain pending their unresolved coupling
  and score-normalization audits. No implementation or empirical model was executed.
- The primary PDF’s text extraction garbles mathematical notation; equations were
  verified from rendered pages. Source bibliographic page ranges differ, so all claim
  locators use exact PDF page indices.
related_reviews: []
links: []
tags:
- native-concepts
- gaussian-processes
- self-review
- discovery-ongoing
```
