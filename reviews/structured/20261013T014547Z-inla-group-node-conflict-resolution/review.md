# Scientific author review and resolution of INLA group node conflict diagnostic

- Review: 20261013T014547Z-inla-group-node-conflict-resolution
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T01:40:27Z
- Finished UTC: 2026-10-13T01:45:47Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete corrected INLA group diagnostic is supported within explicit static-source, replication, rank and calibration limits. Resolve the one evidence-locator finding after actual post-edit gates; the record remains DRAFT.

## Scope And Provenance

All maintained fields of the INLA group diagnostic and the single saved locator finding.

Selection: Exact maintained ID AIMech:INLAGroupNodeConflictDiagnostic and F1 in 20261013T013734Z-inla-conflict-locators-initial
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8c2c991039ba083ae4f20af4b0953d0fdaf2fb1b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:INLAGroupNodeConflictDiagnostic | data/curated/INLAGroupNodeConflictDiagnostic.yaml | maintained | INLA group node conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:INLAGroupNodeConflictDiagnostic | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 113.79s (0:01:53)<br>Checked 442 record(s); 0 failed.<br>Checked 561 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 214 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 213,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:INLAGroupNodeConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:INLAGroupNodeConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:INLAGroupNodeConflictDiagnostic | Exited 0 without output. |
| Constructed nuisance/covariance/rank checks | passed | True | AIMech:INLAGroupNodeConflictDiagnostic | {"frozen_nuisance_mixture": {"mean": 1.0, "variance": 2.0, "weights": [0.5, 0.5]}, "posterior_as_prior_update": {"mean": 1.8, "variance": 1.3599999999999994, "weights": [0.1, 0.9]}, "rank_thresholds": {"absolute_rank": 2, "consistent_full_rank_chi2_tail": 0.36787944117144233, "consistent_retained_chi1_tail": 0.317310507862914, "covariance_diagonal": [100.0, 0.01], "full_rank_quadratic": 2.0, "mean": [10.0, 0.1], "mixed_convention_chi2_tail": 0.6065306597126334, "relative_pseudoinverse_rank": 1, "retained_quadratic": 1.0, "scaled_absolute_rank": 0, "scaled_relative_rank": 1}, "scope": "Constructed analytic examples only; no R-INLA runtime, empirical calibration or historical reproduction.", "shared_nuisance": {"cross_covariance": 1, "independent_replication_difference_variance": 4, "marginal_variances": [2, 2], "shared_difference_variance": 2}} |

## Scientific And Domain Assessments

### INLA linear-predictor specialization

identity: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Retain the distinct DRAFT algorithm.

The procedure chooses a group-level latent predictor vector and two INLA fits per group. Generic INLA fitting, arbitrary separator splitting, unit-level prior/likelihood replication, Gaussian-message screening and simultaneous maxT adjustment do not specify this same mechanism. The software function name is not asserted as a universal ontology alias.

### Diagnostic-to-representation relation

grounding: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Related BayesianNetwork mapping is supported.

The paper describes the split as a Bayesian graphical-model information partition. BayesianNetwork supplies graph representation context. Random-effects/GLM applications are narrower model examples; the PGM task node is a broader, less precise abstraction. No ontology or generated YAML is modified.

### grouped-latent-predictors

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

Partition the observed data indices into declared groups. For each group j, split the corresponding vector of latent linear predictors eta_j into a copy informed by the remaining groups and a copy informed by the selected group. This specialization uses latent Gaussian models and INLA approximations. It assesses one group versus the rest on the latent predictor scale, rather than arbitrary separators, all possible partitions, or pointwise predictive residuals.

### two-fits-and-summaries

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

Perform a remaining-data INLA fit with the selected group responses omitted, retaining predictions at those indices, then a within-group fit. The fitted distributions must be proper and have the finite moments required for the summaries. Obtain the predictor-vector means and covariance matrices through linear combinations. Use remaining minus within for the mean difference. The inspected helper makes two fits per group, supplies the remaining fit through control.update to the within fit, and adds the two marginal covariance matrices. The within distribution therefore also depends on information supplied by the remaining fit; its notation as conditioning only on group data is abbreviated.

### replication-and-covariance

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

The sum S=S_remaining+S_within is the covariance of a difference under independent draws from the two fitted marginal laws, conditional on the observed data and chosen fits. If the intended replication instead shares a nuisance draw, its cross-covariance C contributes S=S_remaining+S_within-C-C^T. Cutting feedback does not by itself remove that dependence. Distinguish this posterior replication choice from dependence of fitted summaries over repeated data; separate fits alone do not prove sampling calibration.

### quadratic-reference

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

For mean difference m and a positive semidefinite covariance S, the reported discrepancy is Q=m^T*S^+*m. With a justified centered Gaussian reference on the retained r-dimensional subspace, use the upper chi-square_r tail. S^+ denotes the Moore–Penrose pseudoinverse; rank deficiency is allowed. A null outside the affine support requires separate treatment because the pseudoinverse drops nullspace displacement. A numerical cutoff must define the same retained subspace for both Q and r. Approximate posterior normality is not by itself a theorem about repeated-data p-value calibration.

### posterior-as-prior-is-not-a-general-cut

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

The paper equates passing the remaining-data hyperparameter posterior as the within-fit prior with a multiple-imputation cut. Static tracing of the pinned 2026 ordinary integration path instead shows prior-density substitution followed by a new local-data marginal likelihood and new integration weights. Generically, if q_minus(theta) is the supplied prior approximation and Z_j(theta) the local evidence, an ordinary update weights theta proportionally to q_minus(theta)*Z_j(theta); a frozen-weight cut retains q_minus(theta) while normalizing the conditional local distribution at each theta. These coincide only under additional conditions, such as constant local evidence. The helper does not itself configure the USER_EXPERT supplied-weight exception. This is a bounded source-code inference, not a runtime result or a claim about the exact 2017 release.

### implementation-rank-mismatch

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

In the pinned helper, degrees of freedom count covariance eigenvalues above the absolute threshold 0.001, whereas inla.ginv with tol=0.001 retains singular values above 0.001 times the largest singular value. These can select different ranks: for diagonal covariance (100, 0.01), the former counts two directions and the latter retains one. Rescaling predictor units can change the absolute-rank count. This discrepancy qualifies that implementation; it is not the mathematical rank convention of the diagnostic and was not tested by running R-INLA.

### calibration-and-implementation-scope

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

Supported with the explicit mathematical and implementation limits.

The source leaves a systematic study of power and calibration for future work. A small score flags incompatibility under the chosen model, grouping, priors, approximation and reference; it does not identify which data source is wrong or establish a posterior probability of equality. Benjamini–Hochberg adjustments in the examples do not establish general FDR control for dependent approximate conflict scores. The inspected experimental helper requires data.frame input and a named response and rejects a predictor A matrix. Its supported software interface is narrower than the broad latent Gaussian model family.

### Prior substitution, replication and rank conventions

consistency: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

The record distinguishes the intended method from bounded implementation observations.

The update serializer/parser supplies a previous-posterior approximation as an extra prior density. The ordinary objective includes local-data likelihood, and ordinary integration uses the newly evaluated density; USER_EXPERT is an explicit separate supplied-weight path. The record therefore does not certify a generic frozen cut. The two-state example changes mixture weights from [0.5,0.5] to [0.1,0.9], means from 1 to 1.8 and variances from 2 to 1.36. Shared-nuisance Gaussian copies have difference variance 2 versus 4 for independently sampled marginals. For covariance diag(100,0.01) and mean [10,0.1], absolute rank is 2 and relative pseudoinverse rank 1: mixed-convention tail 0.6065306597 differs from retained-rank tail 0.3173105079 and full-rank tail 0.3678794412. These are constructed checks, not measured software outcomes.

### Exact source line endpoints

evidence: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

All affected locators now include their named operations.

The fit-summary range reaches covariance line 158; mean/covariance uses 157–158; control.update and its within-fit call use 153–154; statistic/tail uses 169–175; the rank-only range is precisely 170–174. Read the corrected full YAML and numbered statements after fresh input capture. The report mirror and append-only EDIT history agree; scientific statements are unchanged.

### Full record and version boundaries

provenance: supported. Targets: AIMech:INLAGroupNodeConflictDiagnostic.

All maintained fields are coherent; retain DRAFT.

Read the stable ID, name, empty aliases, algorithm kind, definition, identity notes, seven claims with citations, eight source records, pinned related mapping, six limitations and actual UTC curation provenance. Checked source bytes, report mirror and captured inputs. The paper and 2026 code revision are kept distinct; source dates and introductory sign ambiguity are preserved. The newer score-discrepancy paper is incomplete discovery follow-up, not evidence for this record.

## Findings

### F1: Include the cited R-INLA statements in their evidence line ranges

minor / resolved / confirmed; issue key: inla-group-conflict-cut-source-locators.

Several cut.R evidence locators end before the statements they claim to locate: control.update is on line 153, after the cited 149–152; sigma.diff is on line 158, after cited 153–157 and 88–157; pval is on line 175, after cited 167–174. The primary PDF supports the algorithm and the complete source was read, so this is a locator-precision defect rather than a change to the mechanism. Correct the maintained locators and mirrored report using the pinned numbered source.

Disposition: Corrected the maintained locators and exact report mirror, appended EDIT history, freshly captured and reread the corrected fields against numbered pinned source, and passed actual post-edit publication gates. Scientific statements are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T013528Z-inla-group-node-conflict.json | supports | No normalized identity match for the INLA group-conflict candidate among all 442 pinned AIO and 560 maintained IDs, names, aliases and scoped synonyms. Fixed-string searches include ignored and hidden files in the recovery, older discovery and original Documents checkouts, returning 185, 0 and 0 lines. Hit paths were classified and canonical diagnostic records and the relevant pending INLA/source notes inspected; generated mirrors and long metadata/search-index lines are not separate method definitions and were not all read line by line. The semantic assessment covers 61 AIO rows and 214 native names/definitions: 61 and 213 prior rows were verified unchanged, and the one new multiple-testing definition was read. Ten full AIO nodes with incident edges and generated records and eight native context records were read or verified against prior full readings. This distinct procedure fixes the split to group-level latent predictors and computes its summaries with INLA. It is not generic INLA fitting, arbitrary separator diagnostics, Gaussian-message screening, simultaneous maxT inference or a software-package instance. |
| mapping | sources/aio/aio.json | supports | Verified unchanged AIO nodes and context hashes. The semantic assessment includes 61 AIO rows and 214 native definitions, with verified prior readings and the new multiple-testing definition read. BayesianNetwork is graph representation context; the diagnostic does not claim an ontology equivalence or subclass. |
| calculation | research/discovery/inla-conflict-boundaries.py | supports | Constructed two-state nuisance weights, correlated Gaussian replicas and a diagonal covariance show posterior-as-prior reweighting, covariance pairing and mismatched numerical ranks. No R-INLA, source application or empirical calibration was run. |
| predecessor | reviews/structured/20261013T013734Z-inla-conflict-locators-initial/review.yaml | supports | Read the initial finding, verified its exact issue key and affected-target union. Ignored-inclusive review search found only this predecessor bundle and no competing successor. Its actual native-validation pass is distinct from the pending post-edit publication gates. |
| ferkingstad2017 | https://arxiv.org/pdf/1708.03272v4; Sections 2.1–2.3, PDF pp. 3–10; discussion, pp. 18–19; Section 2.3 and implementation, PDF pp. 9–10; Shared parameters and covariance construction, PDF pp. 8–10; Section 2.3, PDF pp. 9–10; discussion, pp. 18–19; Section 2.3, PDF pp. 9–10; Examples and discussion, PDF pp. 11–19 | supports | Complete 22-page primary paper read in preparation, with all figures, Table 1 and references. After original capture, visually reread pp. 7–10 and 18–19. These source bytes and scientific statements are unchanged after the locator correction. No source application, calibration experiment or R-INLA execution is certified. |
| cut2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/cut.R; inla.cut, lines 88–158; mu.diff and sigma.diff, lines 157–158; Discrepancy and chi-square tail, lines 169–175; control.update assignment and within-fit call, lines 153–154; min.eigen.value, lin.pred.df and lin.pred.Delta, lines 170–174; Documentation experimental marker and input checks, lines 1–78; A-matrix check, lines 121–128 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| sections2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/sections.R; inla.update.section, lines 1875–1895 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| parse2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/inlaprog/src/inla-parse.c; inla_parse_update, lines 20859–20939 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| inlac2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/inlaprog/src/inla.c; inla_extra update branch, lines 1615–1623; inla_update_density, lines 7346–7388 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| domin2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/gmrflib/domin-interface.c; GMRFLib_opt_f_intern, lines 286–342 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| integration2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/gmrflib/approx-inference.c; GMRFLib_ai_marginal_hyperparam, lines 389–557; integration weights, lines 2140–2225 and 2510–2585 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |
| utils2026 | https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/utils.R; Complete inla.ginv helper, lines 816–846 | supports | Read the stated functions at the immutable revision. After original capture reread the cited implementation trace, including all numbered cut.R lines; after correction capture rechecked the exact corrected cut.R endpoints. Other source regions are not certified. This is static source analysis, not software execution. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- One new DRAFT concept, yielding 561 native and 442 unchanged generated records. The 746-entry main frontier retains 484 pending and 57 partly addressed cohorts; discovery is incomplete.
- Official source inspection is limited to the named revision and cited functions. No R-INLA installation, compilation, model fitting, MCMC, benchmark, biomedical inference or repeated-data calibration was performed. Constructed algebraic examples illustrate weighting, covariance and rank boundaries only.
- Primary-paper reading and pinned source-code inspection are different evidence versions. Earlier source-note unresolved statuses describe earlier observations; the latest_assessment records the completed static trace and does not establish runtime or historical behavior.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T014547Z-inla-group-node-conflict-resolution
kind: record
repository: CultureBotAI/AIMech
title: Scientific author review and resolution of INLA group node conflict diagnostic
started_at: '2026-10-13T01:40:27Z'
finished_at: '2026-10-13T01:45:47Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged identity, representation mapping, posterior-as-prior
    versus frozen-cut semantics, covariance pairing, rank thresholds, calibration,
    source versions and exact locators. This is adversarial author self-review, not
    independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md; aimech-resolve-reviews
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete corrected INLA group diagnostic is supported within explicit
  static-source, replication, rank and calibration limits. Resolve the one evidence-locator
  finding after actual post-edit gates; the record remains DRAFT.
source:
  git_revision: 8c2c991039ba083ae4f20af4b0953d0fdaf2fb1b
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/FixedEffectsModel.yaml
    sha256: ce9b21b60e99bf7abfd19b9b480d5c73777ba59f38af53c3fa2d6bfc50f71a86
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RandomEffectsModel.yaml
    sha256: 4e3f50ef012b217822c2b731cce1b07dff14e66826f26d7717a6dab42d482d4c
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/CrossValidatedPriorLikelihoodConflictDiagnostic.yaml
    sha256: 92c4daf84d56e0ea6528ee512063fcf8d7fc8c69795bff9fe19fe5de8c65d119
    role: context
  - path: data/curated/GaussianMessageConflictDiagnostic.yaml
    sha256: adc6c4f1c16288b59515f77401ff4d1c2a02f673a00a91963de6e3fa588c4cff
    role: context
  - path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
    sha256: c97bf3553a26f7bb84a4539bf0cfed7d6bbe5170c7df411deb77ca1cf868f0b1
    role: target
  - path: data/curated/LocalOutlierFactor.yaml
    sha256: b9293fde56804e7df6d3056e00b08240ca9dc8711a715bda54d064cfd9bc8812
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/PartiallyNoncenteredGLMMVariationalInference.yaml
    sha256: 9c5bfdf2ad7cee069ecf1559d3df296ac7c7c0c807a49eee5644f984e7abc361
    role: context
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: context
  - path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    sha256: 27235b4323710bcd53fb73d6dbe06f0eb115a3d6cbf52600345f9c7c68c45c99
    role: context
  - path: research/discovery/20261013T013528Z-inla-group-node-conflict.json
    sha256: 62bae2c55e41c07b3f58c98f46cf13c9830b7b37005ac21ff62edb5d5de069bb
    role: context
  - path: research/discovery/inla-conflict-boundaries.py
    sha256: f07c864e17c82725e8d165168cacfbc8640357dbb9ce88ef74c208ba2e375bf0
    role: context
  - path: reviews/structured/20261013T013734Z-inla-conflict-locators-initial/review.yaml
    sha256: f4b311ee0e13248af91bf030440d7f8fdd6c58457cf13d3eeb9f4f54ef1bdbd0
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
- target_id: AIMech:INLAGroupNodeConflictDiagnostic
  path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
  label: INLA group node conflict diagnostic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
    role: maintained
scope:
  description: All maintained fields of the INLA group diagnostic and the single saved
    locator finding.
  selection: Exact maintained ID AIMech:INLAGroupNodeConflictDiagnostic and F1 in
    20261013T013734Z-inla-conflict-locators-initial
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  exclusions:
  - target: R-INLA runtime, historical versions and uninspected source regions
    reason: Static trace only; no fitting, compilation or software reproduction.
  - target: Empirical calibration or biomedical outcomes
    reason: No repeated-data study or original application reproduction.
  - target: Neighboring records and pending methods
    reason: Identity context and discovery only, not global scientific review.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 113.79s (0:01:53)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 561 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 214 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 213,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
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
  - AIMech:INLAGroupNodeConflictDiagnostic
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
  - AIMech:INLAGroupNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed nuisance/covariance/rank checks
  command: python3 research/discovery/inla-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: '{"frozen_nuisance_mixture": {"mean": 1.0, "variance": 2.0, "weights":
    [0.5, 0.5]}, "posterior_as_prior_update": {"mean": 1.8, "variance": 1.3599999999999994,
    "weights": [0.1, 0.9]}, "rank_thresholds": {"absolute_rank": 2, "consistent_full_rank_chi2_tail":
    0.36787944117144233, "consistent_retained_chi1_tail": 0.317310507862914, "covariance_diagonal":
    [100.0, 0.01], "full_rank_quadratic": 2.0, "mean": [10.0, 0.1], "mixed_convention_chi2_tail":
    0.6065306597126334, "relative_pseudoinverse_rank": 1, "retained_quadratic": 1.0,
    "scaled_absolute_rank": 0, "scaled_relative_rank": 1}, "scope": "Constructed analytic
    examples only; no R-INLA runtime, empirical calibration or historical reproduction.",
    "shared_nuisance": {"cross_covariance": 1, "independent_replication_difference_variance":
    4, "marginal_variances": [2, 2], "shared_difference_variance": 2}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T013528Z-inla-group-node-conflict.json
  accessed_at: '2026-10-13T01:40:27Z'
  support: supports
  summary: 'No normalized identity match for the INLA group-conflict candidate among
    all 442 pinned AIO and 560 maintained IDs, names, aliases and scoped synonyms.
    Fixed-string searches include ignored and hidden files in the recovery, older
    discovery and original Documents checkouts, returning 185, 0 and 0 lines. Hit
    paths were classified and canonical diagnostic records and the relevant pending
    INLA/source notes inspected; generated mirrors and long metadata/search-index
    lines are not separate method definitions and were not all read line by line.
    The semantic assessment covers 61 AIO rows and 214 native names/definitions: 61
    and 213 prior rows were verified unchanged, and the one new multiple-testing definition
    was read. Ten full AIO nodes with incident edges and generated records and eight
    native context records were read or verified against prior full readings. This
    distinct procedure fixes the split to group-level latent predictors and computes
    its summaries with INLA. It is not generic INLA fitting, arbitrary separator diagnostics,
    Gaussian-message screening, simultaneous maxT inference or a software-package
    instance.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T01:40:27Z'
  support: supports
  summary: Verified unchanged AIO nodes and context hashes. The semantic assessment
    includes 61 AIO rows and 214 native definitions, with verified prior readings
    and the new multiple-testing definition read. BayesianNetwork is graph representation
    context; the diagnostic does not claim an ontology equivalence or subclass.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/inla-conflict-boundaries.py
  accessed_at: '2026-10-13T01:40:27Z'
  snapshot_sha256: f07c864e17c82725e8d165168cacfbc8640357dbb9ce88ef74c208ba2e375bf0
  support: supports
  summary: Constructed two-state nuisance weights, correlated Gaussian replicas and
    a diagonal covariance show posterior-as-prior reweighting, covariance pairing
    and mismatched numerical ranks. No R-INLA, source application or empirical calibration
    was run.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261013T013734Z-inla-conflict-locators-initial/review.yaml
  accessed_at: '2026-10-13T01:40:27Z'
  snapshot_sha256: f4b311ee0e13248af91bf030440d7f8fdd6c58457cf13d3eeb9f4f54ef1bdbd0
  support: supports
  summary: Read the initial finding, verified its exact issue key and affected-target
    union. Ignored-inclusive review search found only this predecessor bundle and
    no competing successor. Its actual native-validation pass is distinct from the
    pending post-edit publication gates.
- evidence_id: ferkingstad2017
  kind: primary_source
  reference: https://arxiv.org/pdf/1708.03272v4
  locator: Sections 2.1–2.3, PDF pp. 3–10; discussion, pp. 18–19; Section 2.3 and
    implementation, PDF pp. 9–10; Shared parameters and covariance construction, PDF
    pp. 8–10; Section 2.3, PDF pp. 9–10; discussion, pp. 18–19; Section 2.3, PDF pp.
    9–10; Examples and discussion, PDF pp. 11–19
  accessed_at: '2026-10-13T00:56:46Z'
  snapshot_sha256: 4f6e83ce3665edb7bb6fc6bd8ce69a69f24ee2f36d0c9326fbe202016ebfb8a3
  support: supports
  summary: Complete 22-page primary paper read in preparation, with all figures, Table
    1 and references. After original capture, visually reread pp. 7–10 and 18–19.
    These source bytes and scientific statements are unchanged after the locator correction.
    No source application, calibration experiment or R-INLA execution is certified.
- evidence_id: cut2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/cut.R
  locator: inla.cut, lines 88–158; mu.diff and sigma.diff, lines 157–158; Discrepancy
    and chi-square tail, lines 169–175; control.update assignment and within-fit call,
    lines 153–154; min.eigen.value, lin.pred.df and lin.pred.Delta, lines 170–174;
    Documentation experimental marker and input checks, lines 1–78; A-matrix check,
    lines 121–128
  accessed_at: '2026-10-13T01:05:03Z'
  snapshot_sha256: f7a36f50ca94d0fde21057e698af8457ea9920568e1c943f23c15276f8bdfcd0
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: sections2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/sections.R
  locator: inla.update.section, lines 1875–1895
  accessed_at: '2026-10-13T01:05:48Z'
  snapshot_sha256: 4e01dd8f3c94836f272abf83d4d92802b748c50135d1e2808940b071d3ebaf92
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: parse2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/inlaprog/src/inla-parse.c
  locator: inla_parse_update, lines 20859–20939
  accessed_at: '2026-10-13T01:12:11Z'
  snapshot_sha256: f07f2defde065e3e4bd4daad2db15fe55e43e59a2f23744da21410b6a336265e
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: inlac2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/inlaprog/src/inla.c
  locator: inla_extra update branch, lines 1615–1623; inla_update_density, lines 7346–7388
  accessed_at: '2026-10-13T01:11:14Z'
  snapshot_sha256: 6bd722684049ab1a54bdd1d9e7574cbc250304e1d1f89c30e75c2ca05394f545
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: domin2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/gmrflib/domin-interface.c
  locator: GMRFLib_opt_f_intern, lines 286–342
  accessed_at: '2026-10-13T01:14:45Z'
  snapshot_sha256: 8f9afb51e92d361f7e7a112f68c8cc9b162f3a3f627ed8a2a6c1328d93ff252b
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: integration2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/gmrflib/approx-inference.c
  locator: GMRFLib_ai_marginal_hyperparam, lines 389–557; integration weights, lines
    2140–2225 and 2510–2585
  accessed_at: '2026-10-13T01:13:06Z'
  snapshot_sha256: 56e71bd2e5d9760dfe0e62a08f172f6126b499c82c574333a5ddd2e71aa699e4
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
- evidence_id: utils2026
  kind: primary_source
  reference: https://github.com/hrue/r-inla/blob/5bc4c7f223c679bb4b99171aaca490d72e96494c/rinla/R/utils.R
  locator: Complete inla.ginv helper, lines 816–846
  accessed_at: '2026-10-13T01:13:52Z'
  snapshot_sha256: aba074dd4c42982c288f37776f72d3beb9b870d60dea6282380948d5e40e856e
  support: supports
  summary: Read the stated functions at the immutable revision. After original capture
    reread the cited implementation trace, including all numbered cut.R lines; after
    correction capture rechecked the exact corrected cut.R endpoints. Other source
    regions are not certified. This is static source analysis, not software execution.
assessments:
- assessment_id: identity
  area: identity
  topic: INLA linear-predictor specialization
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - identity
  - ferkingstad2017
  summary: Retain the distinct DRAFT algorithm.
  details: The procedure chooses a group-level latent predictor vector and two INLA
    fits per group. Generic INLA fitting, arbitrary separator splitting, unit-level
    prior/likelihood replication, Gaussian-message screening and simultaneous maxT
    adjustment do not specify this same mechanism. The software function name is not
    asserted as a universal ontology alias.
- assessment_id: mapping
  area: grounding
  topic: Diagnostic-to-representation relation
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - mapping
  - ferkingstad2017
  summary: Related BayesianNetwork mapping is supported.
  details: The paper describes the split as a Bayesian graphical-model information
    partition. BayesianNetwork supplies graph representation context. Random-effects/GLM
    applications are narrower model examples; the PGM task node is a broader, less
    precise abstraction. No ontology or generated YAML is modified.
- assessment_id: grouped-latent-predictors
  area: evidence
  topic: grouped-latent-predictors
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  summary: Supported with the explicit mathematical and implementation limits.
  details: Partition the observed data indices into declared groups. For each group
    j, split the corresponding vector of latent linear predictors eta_j into a copy
    informed by the remaining groups and a copy informed by the selected group. This
    specialization uses latent Gaussian models and INLA approximations. It assesses
    one group versus the rest on the latent predictor scale, rather than arbitrary
    separators, all possible partitions, or pointwise predictive residuals.
- assessment_id: two-fits-and-summaries
  area: evidence
  topic: two-fits-and-summaries
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  summary: Supported with the explicit mathematical and implementation limits.
  details: Perform a remaining-data INLA fit with the selected group responses omitted,
    retaining predictions at those indices, then a within-group fit. The fitted distributions
    must be proper and have the finite moments required for the summaries. Obtain
    the predictor-vector means and covariance matrices through linear combinations.
    Use remaining minus within for the mean difference. The inspected helper makes
    two fits per group, supplies the remaining fit through control.update to the within
    fit, and adds the two marginal covariance matrices. The within distribution therefore
    also depends on information supplied by the remaining fit; its notation as conditioning
    only on group data is abbreviated.
- assessment_id: replication-and-covariance
  area: evidence
  topic: replication-and-covariance
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  - calculation
  summary: Supported with the explicit mathematical and implementation limits.
  details: The sum S=S_remaining+S_within is the covariance of a difference under
    independent draws from the two fitted marginal laws, conditional on the observed
    data and chosen fits. If the intended replication instead shares a nuisance draw,
    its cross-covariance C contributes S=S_remaining+S_within-C-C^T. Cutting feedback
    does not by itself remove that dependence. Distinguish this posterior replication
    choice from dependence of fitted summaries over repeated data; separate fits alone
    do not prove sampling calibration.
- assessment_id: quadratic-reference
  area: evidence
  topic: quadratic-reference
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  - calculation
  summary: Supported with the explicit mathematical and implementation limits.
  details: For mean difference m and a positive semidefinite covariance S, the reported
    discrepancy is Q=m^T*S^+*m. With a justified centered Gaussian reference on the
    retained r-dimensional subspace, use the upper chi-square_r tail. S^+ denotes
    the Moore–Penrose pseudoinverse; rank deficiency is allowed. A null outside the
    affine support requires separate treatment because the pseudoinverse drops nullspace
    displacement. A numerical cutoff must define the same retained subspace for both
    Q and r. Approximate posterior normality is not by itself a theorem about repeated-data
    p-value calibration.
- assessment_id: posterior-as-prior-is-not-a-general-cut
  area: evidence
  topic: posterior-as-prior-is-not-a-general-cut
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  - sections2026
  - parse2026
  - inlac2026
  - domin2026
  - integration2026
  - calculation
  summary: Supported with the explicit mathematical and implementation limits.
  details: The paper equates passing the remaining-data hyperparameter posterior as
    the within-fit prior with a multiple-imputation cut. Static tracing of the pinned
    2026 ordinary integration path instead shows prior-density substitution followed
    by a new local-data marginal likelihood and new integration weights. Generically,
    if q_minus(theta) is the supplied prior approximation and Z_j(theta) the local
    evidence, an ordinary update weights theta proportionally to q_minus(theta)*Z_j(theta);
    a frozen-weight cut retains q_minus(theta) while normalizing the conditional local
    distribution at each theta. These coincide only under additional conditions, such
    as constant local evidence. The helper does not itself configure the USER_EXPERT
    supplied-weight exception. This is a bounded source-code inference, not a runtime
    result or a claim about the exact 2017 release.
- assessment_id: implementation-rank-mismatch
  area: evidence
  topic: implementation-rank-mismatch
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - cut2026
  - utils2026
  - calculation
  summary: Supported with the explicit mathematical and implementation limits.
  details: 'In the pinned helper, degrees of freedom count covariance eigenvalues
    above the absolute threshold 0.001, whereas inla.ginv with tol=0.001 retains singular
    values above 0.001 times the largest singular value. These can select different
    ranks: for diagonal covariance (100, 0.01), the former counts two directions and
    the latter retains one. Rescaling predictor units can change the absolute-rank
    count. This discrepancy qualifies that implementation; it is not the mathematical
    rank convention of the diagnostic and was not tested by running R-INLA.'
- assessment_id: calibration-and-implementation-scope
  area: evidence
  topic: calibration-and-implementation-scope
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  summary: Supported with the explicit mathematical and implementation limits.
  details: The source leaves a systematic study of power and calibration for future
    work. A small score flags incompatibility under the chosen model, grouping, priors,
    approximation and reference; it does not identify which data source is wrong or
    establish a posterior probability of equality. Benjamini–Hochberg adjustments
    in the examples do not establish general FDR control for dependent approximate
    conflict scores. The inspected experimental helper requires data.frame input and
    a named response and rejects a predictor A matrix. Its supported software interface
    is narrower than the broad latent Gaussian model family.
- assessment_id: implementation-boundaries
  area: consistency
  topic: Prior substitution, replication and rank conventions
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - ferkingstad2017
  - cut2026
  - sections2026
  - parse2026
  - inlac2026
  - domin2026
  - integration2026
  - utils2026
  - calculation
  summary: The record distinguishes the intended method from bounded implementation
    observations.
  details: 'The update serializer/parser supplies a previous-posterior approximation
    as an extra prior density. The ordinary objective includes local-data likelihood,
    and ordinary integration uses the newly evaluated density; USER_EXPERT is an explicit
    separate supplied-weight path. The record therefore does not certify a generic
    frozen cut. The two-state example changes mixture weights from [0.5,0.5] to [0.1,0.9],
    means from 1 to 1.8 and variances from 2 to 1.36. Shared-nuisance Gaussian copies
    have difference variance 2 versus 4 for independently sampled marginals. For covariance
    diag(100,0.01) and mean [10,0.1], absolute rank is 2 and relative pseudoinverse
    rank 1: mixed-convention tail 0.6065306597 differs from retained-rank tail 0.3173105079
    and full-rank tail 0.3678794412. These are constructed checks, not measured software
    outcomes.'
- assessment_id: resolved-locators
  area: evidence
  topic: Exact source line endpoints
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - predecessor
  - cut2026
  summary: All affected locators now include their named operations.
  details: The fit-summary range reaches covariance line 158; mean/covariance uses
    157–158; control.update and its within-fit call use 153–154; statistic/tail uses
    169–175; the rank-only range is precisely 170–174. Read the corrected full YAML
    and numbered statements after fresh input capture. The report mirror and append-only
    EDIT history agree; scientific statements are unchanged.
- assessment_id: complete-fields
  area: provenance
  topic: Full record and version boundaries
  outcome: supported
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  evidence_ids:
  - identity
  - mapping
  - ferkingstad2017
  - cut2026
  - calculation
  - predecessor
  summary: All maintained fields are coherent; retain DRAFT.
  details: Read the stable ID, name, empty aliases, algorithm kind, definition, identity
    notes, seven claims with citations, eight source records, pinned related mapping,
    six limitations and actual UTC curation provenance. Checked source bytes, report
    mirror and captured inputs. The paper and 2026 code revision are kept distinct;
    source dates and introductory sign ambiguity are preserved. The newer score-discrepancy
    paper is incomplete discovery follow-up, not evidence for this record.
findings:
- finding_id: F1
  issue_key: inla-group-conflict-cut-source-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Include the cited R-INLA statements in their evidence line ranges
  description: 'Several cut.R evidence locators end before the statements they claim
    to locate: control.update is on line 153, after the cited 149–152; sigma.diff
    is on line 158, after cited 153–157 and 88–157; pval is on line 175, after cited
    167–174. The primary PDF supports the algorithm and the complete source was read,
    so this is a locator-precision defect rather than a change to the mechanism. Correct
    the maintained locators and mirrored report using the pinned numbered source.'
  target_ids:
  - AIMech:INLAGroupNodeConflictDiagnostic
  field_paths:
  - claims[claim_id=two-fits-and-summaries].evidence
  - claims[claim_id=replication-and-covariance].evidence
  - claims[claim_id=quadratic-reference].evidence
  - claims[claim_id=posterior-as-prior-is-not-a-general-cut].evidence
  evidence_ids:
  - predecessor
  - cut2026
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T013734Z-inla-conflict-locators-initial
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/225
  disposition_reason: Corrected the maintained locators and exact report mirror, appended
    EDIT history, freshly captured and reread the corrected fields against numbered
    pinned source, and passed actual post-edit publication gates. Scientific statements
    are unchanged.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- One new DRAFT concept, yielding 561 native and 442 unchanged generated records.
  The 746-entry main frontier retains 484 pending and 57 partly addressed cohorts;
  discovery is incomplete.
- Official source inspection is limited to the named revision and cited functions.
  No R-INLA installation, compilation, model fitting, MCMC, benchmark, biomedical
  inference or repeated-data calibration was performed. Constructed algebraic examples
  illustrate weighting, covariance and rank boundaries only.
- Primary-paper reading and pinned source-code inspection are different evidence versions.
  Earlier source-note unresolved statuses describe earlier observations; the latest_assessment
  records the completed static trace and does not establish runtime or historical
  behavior.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; only the isolated recovery checkout is
  changed.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T013734Z-inla-conflict-locators-initial
  relationship: Resolves the sole locator finding after maintained correction and
    fresh review.
links:
- https://github.com/CultureBotAI/AIMech/issues/225
tags:
- native-concepts
- inla
- model-diagnostics
- self-review
- review-resolution
- discovery-ongoing
```
