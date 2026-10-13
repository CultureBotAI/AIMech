# Scientific author self-review of separator-node conflict diagnostic

- Review: 20261013T010759Z-separator-node-conflict
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T01:03:39Z
- Finished UTC: 2026-10-13T01:07:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the general separator-node conflict diagnostic as a distinct DRAFT algorithm with related Bayesian-network context. All seven claims and locators are supported with explicit partition, nuisance, score and calibration boundaries. No actionable defect was found; source implementation and empirical calibration remain unverified.

## Scope And Provenance

All fields of the exact maintained separator-node diagnostic and its primary evidence.

Selection: Exact maintained ID: AIMech:SeparatorNodeConflictDiagnostic
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 46cb0687d1a4b1b156675e7f982079bdf7cb6743.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SeparatorNodeConflictDiagnostic | data/curated/SeparatorNodeConflictDiagnostic.yaml | maintained | Separator-node conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SeparatorNodeConflictDiagnostic | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 121.35s (0:02:01)<br>Checked 442 record(s); 0 failed.<br>Checked 559 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 210 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 208,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SeparatorNodeConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SeparatorNodeConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SeparatorNodeConflictDiagnostic | Exited 0 without output. |
| Constructed score distinctions | passed | True | AIMech:SeparatorNodeConflictDiagnostic | {"discrete_agreement": {"identical_point_mass": 1, "identical_uniform_mass": 0.10000000000000002, "states": 10}, "limits": "Constructed score distributions only; no author code, MCMC, source model fit, empirical calibration or multiplicity guarantee.", "nonelliptical_symmetric_unimodal": {"covariance_diagonal": [2, 2], "density_level_tail": 0.7357588823428847, "density_ratio": 1.513180250744887, "distribution": "Independent Laplace(0,1) coordinates shifted by (1,0)", "empirical_radial_population_tail": 0.646479229909376, "null_mahalanobis": 0.5, "quadrature_refinement_difference": 1.1102230246251565e-16, "same_radius_points": [[1.0, 0.0], [0.7071067811865475, 0.7071067811865475]]}, "nonlinear_separator_scale": {"a_distribution": "Exp(1)", "assumption": "The second copy is a point mass; this is an analytic illustration of score dependence on the common separator scale, not an empirical evidence split.", "b_fixed": 0.6931471805599453, "log_scale_density_tail": 0.75, "original_and_log_scale_equal_tail": 1.0, "original_density_tail": 0.5}} |

## Scientific And Domain Assessments

### General separator diagnostic versus unit-level and approximate specializations

identity: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Retain the general diagnostic as a distinct DRAFT algorithm.

The selected scalar/vector separator and explicit information partition define this concept. Likelihood-versus-likelihood comparisons and arbitrary graph separators go beyond held-out unit effects; Gaussian-message screening is an approximation rather than the general identity. Empty aliases avoid claiming all local diagnostics or every operation called node splitting. The later simultaneous testing extension remains separate.

### Diagnostic-to-DAG representation relation

grounding: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Related BayesianNetwork mapping is supported.

The diagnostic is defined through Bayesian directed acyclic graph partitions and separator copies. BayesianNetwork captures that representation; related_match makes no equivalence or subclass assertion. PGM is broader and task-typed in the pin. Random effects, GLM, logistic/fixed-effects and regression are particular model or task contexts rather than the arbitrary separator mechanism. UnsupervisedLearning, VAE and EvaluationBias do not establish a mapping.

### separator-and-partitions

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

Select a scalar or vector separator theta in a Bayesian DAG and specify which sources of information belong to partitions a and b. Replace the selected node by copies theta_a and theta_b and obtain proper partition-specific distributions p_a(theta_a&#124;y_a) and p_b(theta_b&#124;y_b). Depending on the split, these compare a prior with a likelihood contribution, one likelihood with the remaining prior and likelihood, or distinct likelihood contributions with explicit reference priors. Complete splitting requires removing shared dependence pathways, potentially by duplicating a vector of separator and nuisance nodes. Independent observed data sets alone do not prove that retained latent variables or priors leave the replicate distributions independent. The choice of partition is part of the diagnostic question.

### reference-prior-and-scale

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

A likelihood contribution must be combined with an explicit reference prior and normalized to define a distribution for its separator copy. The source proposes flat priors on a suitable transformed scale h(theta), or Jeffreys priors where appropriate, and calls for prior sensitivity assessment. In one dimension a prior flat in a differentiable one-to-one h corresponds to a density proportional to &#124;h'(theta)&#124; in theta; this is a change-of-variables statement, not a guarantee that every separator has a natural global flattening transformation. Improper priors are usable only if each required split posterior is proper. Weak identification, prior dominance and changes of parameter scale remain substantive choices rather than technical details.

### split-versus-cut

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

A full node split prevents feedback in both directions across the duplicated interface. A nuisance cut instead prevents a selected partition from updating a shared nuisance distribution while allowing that nuisance uncertainty to influence its separator copy. The cut therefore does not automatically make theta_a and theta_b independent. State the joint replication law, normalized conditional distributions and pairing of nuisance draws; use independent posterior draws only when independence is justified by the split. For vector differences, covariance terms from retained dependence must be included rather than automatically adding the marginal covariance matrices.

### discrete-agreement

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

For copies on the same discrete state space and independent partition posteriors, the source defines agreement as P(theta_a=theta_b)=sum_k p_a(k)*p_b(k). If the copies are dependent, equality instead uses their joint probabilities. This is a posterior agreement mass under the replication law, not the posterior probability of the entire model and not a generally uniform frequentist p-value. Its magnitude depends on concentration and state-space granularity: identical diffuse distributions can have small equality mass.

### continuous-scores

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

For a continuous scalar separator define delta=h(theta_a)-h(theta_b) on a declared common scale, and inspect its posterior distribution. A signed tail P(delta&gt;0), its complement, or a stated two-sided equal-tail score 2*min(P(delta&gt;0),P(delta&lt;=0)) measures directional disagreement. The source also defines the density-level score P(p_delta(delta)&lt;p_delta(0)); small values place zero in a low-density region. Under suitable continuous symmetric unimodal densities with no positive-probability density ties, the two-sided equal-tail and density-level scores coincide; they need not coincide for skewed or multimodal distributions. Density plateaus, mixed/discrete support and ties require an explicit convention. Kernel estimates introduce bandwidth, kernel and Monte Carlo uncertainty; a score is not a posterior point-null probability for a continuous difference.

### multivariate-score-options

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

For a k-dimensional continuous difference with finite mean m and positive-definite covariance S, one option under a justified multivariate Gaussian approximation is the upper chi-square_k reference tail at m^T*S^-1*m. Another uses samples to estimate P((delta-m)^T*S^-1*(delta-m)&gt;m^T*S^-1*m), a posterior radial score. A third estimates P(p_delta(delta)&lt;p_delta(0)) from a multivariate density. These are separate choices. In particular, symmetry and unimodality alone do not imply ellipsoidal density contours, so the radial and density-level scores are not interchangeable on those assumptions alone; this distinction is curator reasoning. Singular covariance, deterministic constraints or non-existent moments require a separately justified construction, not an unqualified inverse or chi-square_k calculation.

### interpretation-and-calibration

evidence: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

Supported with the stated construction and limitations.

A conflict score points to local incompatibility under a particular partition, prior and scale; it does not establish which evidence source or model component is wrong. Posterior Gaussianity alone does not establish repeated-data calibration, and the source explicitly presents a practical framework rather than a general proof of uniformity for every split. Density-level scores can change under nonlinear changes of separator scale, even where a common strictly increasing scalar transformation preserves the sign comparison. Repeated fits and high-dimensional density estimation can be costly. Scores from different splits may be dependent, and systematic searches or multiple testing require their own assessed correction and calibration assumptions. Conflicting evidence may be masked or coexist with apparent aggregate model fit; source exclusion or clinical conclusions require further analysis.

### Nonelliptical contours and nonlinear separator scales

consistency: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

The record preserves score distinctions and states curator reasoning.

A shifted product-Laplace difference has covariance 2I and null Mahalanobis distance squared 0.5, but density tail 2/e=0.7357588823 versus radial tail 0.6464792299. Refined deterministic quadrature agrees to floating-point precision. The same-radius points have unequal density. An exponential separator and fixed second copy give density tails 0.5 before a common log transform and 0.75 after it, with equal-tail score 1 in both scales. The explicitly constructed point-mass comparison is not portrayed as an application fit. Identical ten-state uniform copies have equality probability 0.1, demonstrating why agreement mass is not a model probability or calibrated p-value.

### Proper distributions, joint replication law and calibration

consistency: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

No unsupported independence or universal uniformity claim was found.

The full split and one-way nuisance cut are distinguished. The latter may retain dependence and covariance terms, so the record requires a joint law rather than automatically summing marginal covariances. Reference-prior normalization and split-posterior propriety are explicit. The chi-square formula is conditional on justified Gaussian scoring; it is not asserted to provide a universal repeated-data theorem. Discrete and density ties, deterministic constraints and singular/missing covariance moments are explicitly outside the unqualified inverse calculation.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SeparatorNodeConflictDiagnostic.

The full record is consistent; retain DRAFT.

Read every field: stable ID, name, empty aliases, algorithm kind, definition evidence, identity notes, seven claims and locators, source title/authors/version/URLs/access date/hash, pinned mapping revision and rationale, five limitations and actual UTC curation provenance. Verified exact report mirror, capture and context hashes, source bytes and rerun calculation output. The later multiple-testing source is retained as discovery follow-up rather than scientific evidence for this record. No actionable defect was found in this one-record author self-review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T010323Z-separator-node-conflict.json | supports | No normalized identity match for the proposed general separator-node and multiple-testing node conflict diagnostics across 442 pinned AIO records and 558 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 218, 0 and 0 lines. All 218 were assessed: 84 identical prior lines reused, 123 new short rows read, and 11 new long rows read or checked exactly against previously read record text and query results. Hits describe existing unit-level and Gaussian-message diagnostics, their mirrors, source metadata and pending general-method leads. Assessed 55 semantic AIO rows and 203 native names/definitions; all 55 and 202 were verified equal to earlier complete readings, and the new unit-level definition was read. Ten full AIO nodes, annotations, incident edges and generated records, plus six native context records, were read or verified unchanged. This identity denotes arbitrary selected separator information splits, including likelihood-versus-likelihood splits; it is broader in scope than the unit-level held-out prior/likelihood construction and differs from its Gaussian-message approximation. It does not denote generic DAG inference, cut-posterior fitting, every local conflict measure or the later simultaneous multiple-testing extension. |
| mapping | sources/aio/aio.json | supports | Assessed 55 semantic AIO rows and 203 native definitions, including verified unchanged readings. Ten full AIO nodes, annotations, incident edges and generated records plus six native context records were read or verified unchanged. After capture, reread full BayesianNetwork and ProbabilisticGraphicalModel YAMLs; context hashes still match. BayesianNetwork supplies directed acyclic graph representation context, not an algorithm superclass. |
| calculation | research/discovery/separator-conflict-boundaries.py | supports | Constructed shifted product-Laplace difference with exact density-level tail and refined quadrature radial tail; exponential versus log-scale separator density ordering with a fixed comparison copy; identical discrete uniform versus point-mass agreement. No MCMC, model fitting, empirical calibration or author software. |
| presanis2013 | https://arxiv.org/pdf/1310.0628v1; Section 2.2, PDF p. 4; Section 3 and Figure 3, pp. 7–10; shared nuisance variance, p. 17; discussion, pp. 19–20 | supports | All 22 primary pages read in preparation, including all figures, Table 1 and references. After capture, visually reread pp. 4, 7–10, 17 and 19–20. Checked arbitrary separator partitions, reference priors, full splitting versus cuts, discrete agreement, signed tails, density-level and multivariate radial scores, prior/scale sensitivity and bounded interpretation. No universal calibration claim or source implementation verification is imported. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT separator-node diagnostic, yielding 559 native and 442 unchanged generated records. The 744-entry main frontier retains 484 pending and 57 partly addressed cohorts; five new nested source leads remain.
- All 22 pages of the primary electronic reprint were read, including Figures 1–16, Table 1 and references. No author implementation, original application data analysis, MCMC, empirical calibration or benchmark was run. Constructed analytic and quadrature examples check distinctions between radial and density scores, nonlinear scale choices and discrete agreement; they are not reproductions of source experiments.
- The later multiple-testing paper was fully read as follow-up discovery, with source formula ambiguities retained in source_analysis; it is not silently used to claim a multiple-testing implementation in this record.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T010759Z-separator-node-conflict
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of separator-node conflict diagnostic
started_at: '2026-10-13T01:03:39Z'
finished_at: '2026-10-13T01:07:59Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged definition distinctness, split/cut dependence,
    reference-prior propriety, score orientation and equivalence, transformation effects,
    calibration, mapping and source support. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the general separator-node conflict diagnostic as a distinct DRAFT
  algorithm with related Bayesian-network context. All seven claims and locators are
  supported with explicit partition, nuisance, score and calibration boundaries. No
  actionable defect was found; source implementation and empirical calibration remain
  unverified.
source:
  git_revision: 46cb0687d1a4b1b156675e7f982079bdf7cb6743
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
  - path: data/curated/LocalOutlierFactor.yaml
    sha256: b9293fde56804e7df6d3056e00b08240ca9dc8711a715bda54d064cfd9bc8812
    role: context
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/PartiallyNoncenteredGLMMVariationalInference.yaml
    sha256: 9c5bfdf2ad7cee069ecf1559d3df296ac7c7c0c807a49eee5644f984e7abc361
    role: context
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: target
  - path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    sha256: 27235b4323710bcd53fb73d6dbe06f0eb115a3d6cbf52600345f9c7c68c45c99
    role: context
  - path: research/discovery/20261013T010323Z-separator-node-conflict.json
    sha256: 8e47dfdef8d1d9ea54cee6cd391925292f02e29361226b399bb45630b38105d7
    role: context
  - path: research/discovery/separator-conflict-boundaries.py
    sha256: ed6d9096de0ac2a4c5ae29a90558182a747bf10b9b28cdbeb71528ad971137e0
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
- target_id: AIMech:SeparatorNodeConflictDiagnostic
  path: data/curated/SeparatorNodeConflictDiagnostic.yaml
  label: Separator-node conflict diagnostic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    role: maintained
scope:
  description: All fields of the exact maintained separator-node diagnostic and its
    primary evidence.
  selection: 'Exact maintained ID: AIMech:SeparatorNodeConflictDiagnostic'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  exclusions:
  - target: Simultaneous multiple-testing and INLA extensions
    reason: Separate pending concepts; follow-up reading is not an implementation
      or calibration assessment of this general record.
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical calibration
    reason: No author code, model fitting, MCMC or repeated-data simulation run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 121.35s (0:02:01)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 559 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 210 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 208,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
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
  - AIMech:SeparatorNodeConflictDiagnostic
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
  - AIMech:SeparatorNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed score distinctions
  command: python3 research/discovery/separator-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: '{"discrete_agreement": {"identical_point_mass": 1, "identical_uniform_mass":
    0.10000000000000002, "states": 10}, "limits": "Constructed score distributions
    only; no author code, MCMC, source model fit, empirical calibration or multiplicity
    guarantee.", "nonelliptical_symmetric_unimodal": {"covariance_diagonal": [2, 2],
    "density_level_tail": 0.7357588823428847, "density_ratio": 1.513180250744887,
    "distribution": "Independent Laplace(0,1) coordinates shifted by (1,0)", "empirical_radial_population_tail":
    0.646479229909376, "null_mahalanobis": 0.5, "quadrature_refinement_difference":
    1.1102230246251565e-16, "same_radius_points": [[1.0, 0.0], [0.7071067811865475,
    0.7071067811865475]]}, "nonlinear_separator_scale": {"a_distribution": "Exp(1)",
    "assumption": "The second copy is a point mass; this is an analytic illustration
    of score dependence on the common separator scale, not an empirical evidence split.",
    "b_fixed": 0.6931471805599453, "log_scale_density_tail": 0.75, "original_and_log_scale_equal_tail":
    1.0, "original_density_tail": 0.5}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T010323Z-separator-node-conflict.json
  accessed_at: '2026-10-13T01:03:39Z'
  support: supports
  summary: 'No normalized identity match for the proposed general separator-node and
    multiple-testing node conflict diagnostics across 442 pinned AIO records and 558
    maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive
    fixed-string searches of the recovery, older discovery and original Documents
    checkouts returned 218, 0 and 0 lines. All 218 were assessed: 84 identical prior
    lines reused, 123 new short rows read, and 11 new long rows read or checked exactly
    against previously read record text and query results. Hits describe existing
    unit-level and Gaussian-message diagnostics, their mirrors, source metadata and
    pending general-method leads. Assessed 55 semantic AIO rows and 203 native names/definitions;
    all 55 and 202 were verified equal to earlier complete readings, and the new unit-level
    definition was read. Ten full AIO nodes, annotations, incident edges and generated
    records, plus six native context records, were read or verified unchanged. This
    identity denotes arbitrary selected separator information splits, including likelihood-versus-likelihood
    splits; it is broader in scope than the unit-level held-out prior/likelihood construction
    and differs from its Gaussian-message approximation. It does not denote generic
    DAG inference, cut-posterior fitting, every local conflict measure or the later
    simultaneous multiple-testing extension.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T01:03:39Z'
  support: supports
  summary: Assessed 55 semantic AIO rows and 203 native definitions, including verified
    unchanged readings. Ten full AIO nodes, annotations, incident edges and generated
    records plus six native context records were read or verified unchanged. After
    capture, reread full BayesianNetwork and ProbabilisticGraphicalModel YAMLs; context
    hashes still match. BayesianNetwork supplies directed acyclic graph representation
    context, not an algorithm superclass.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/separator-conflict-boundaries.py
  accessed_at: '2026-10-13T01:03:39Z'
  snapshot_sha256: ed6d9096de0ac2a4c5ae29a90558182a747bf10b9b28cdbeb71528ad971137e0
  support: supports
  summary: Constructed shifted product-Laplace difference with exact density-level
    tail and refined quadrature radial tail; exponential versus log-scale separator
    density ordering with a fixed comparison copy; identical discrete uniform versus
    point-mass agreement. No MCMC, model fitting, empirical calibration or author
    software.
- evidence_id: presanis2013
  kind: primary_source
  reference: https://arxiv.org/pdf/1310.0628v1
  locator: Section 2.2, PDF p. 4; Section 3 and Figure 3, pp. 7–10; shared nuisance
    variance, p. 17; discussion, pp. 19–20
  accessed_at: '2026-10-13T00:33:39Z'
  snapshot_sha256: 9cff5092b47d7ba20f9ae654b6ea63bd4fdf75ea8ccfdb663427ccab36f3d3a0
  support: supports
  summary: All 22 primary pages read in preparation, including all figures, Table
    1 and references. After capture, visually reread pp. 4, 7–10, 17 and 19–20. Checked
    arbitrary separator partitions, reference priors, full splitting versus cuts,
    discrete agreement, signed tails, density-level and multivariate radial scores,
    prior/scale sensitivity and bounded interpretation. No universal calibration claim
    or source implementation verification is imported.
assessments:
- assessment_id: identity
  area: identity
  topic: General separator diagnostic versus unit-level and approximate specializations
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - identity
  - presanis2013
  summary: Retain the general diagnostic as a distinct DRAFT algorithm.
  details: The selected scalar/vector separator and explicit information partition
    define this concept. Likelihood-versus-likelihood comparisons and arbitrary graph
    separators go beyond held-out unit effects; Gaussian-message screening is an approximation
    rather than the general identity. Empty aliases avoid claiming all local diagnostics
    or every operation called node splitting. The later simultaneous testing extension
    remains separate.
- assessment_id: mapping
  area: grounding
  topic: Diagnostic-to-DAG representation relation
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - mapping
  - presanis2013
  summary: Related BayesianNetwork mapping is supported.
  details: The diagnostic is defined through Bayesian directed acyclic graph partitions
    and separator copies. BayesianNetwork captures that representation; related_match
    makes no equivalence or subclass assertion. PGM is broader and task-typed in the
    pin. Random effects, GLM, logistic/fixed-effects and regression are particular
    model or task contexts rather than the arbitrary separator mechanism. UnsupervisedLearning,
    VAE and EvaluationBias do not establish a mapping.
- assessment_id: separator-and-partitions
  area: evidence
  topic: separator-and-partitions
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  summary: Supported with the stated construction and limitations.
  details: Select a scalar or vector separator theta in a Bayesian DAG and specify
    which sources of information belong to partitions a and b. Replace the selected
    node by copies theta_a and theta_b and obtain proper partition-specific distributions
    p_a(theta_a|y_a) and p_b(theta_b|y_b). Depending on the split, these compare a
    prior with a likelihood contribution, one likelihood with the remaining prior
    and likelihood, or distinct likelihood contributions with explicit reference priors.
    Complete splitting requires removing shared dependence pathways, potentially by
    duplicating a vector of separator and nuisance nodes. Independent observed data
    sets alone do not prove that retained latent variables or priors leave the replicate
    distributions independent. The choice of partition is part of the diagnostic question.
- assessment_id: reference-prior-and-scale
  area: evidence
  topic: reference-prior-and-scale
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  summary: Supported with the stated construction and limitations.
  details: A likelihood contribution must be combined with an explicit reference prior
    and normalized to define a distribution for its separator copy. The source proposes
    flat priors on a suitable transformed scale h(theta), or Jeffreys priors where
    appropriate, and calls for prior sensitivity assessment. In one dimension a prior
    flat in a differentiable one-to-one h corresponds to a density proportional to
    |h'(theta)| in theta; this is a change-of-variables statement, not a guarantee
    that every separator has a natural global flattening transformation. Improper
    priors are usable only if each required split posterior is proper. Weak identification,
    prior dominance and changes of parameter scale remain substantive choices rather
    than technical details.
- assessment_id: split-versus-cut
  area: evidence
  topic: split-versus-cut
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  summary: Supported with the stated construction and limitations.
  details: A full node split prevents feedback in both directions across the duplicated
    interface. A nuisance cut instead prevents a selected partition from updating
    a shared nuisance distribution while allowing that nuisance uncertainty to influence
    its separator copy. The cut therefore does not automatically make theta_a and
    theta_b independent. State the joint replication law, normalized conditional distributions
    and pairing of nuisance draws; use independent posterior draws only when independence
    is justified by the split. For vector differences, covariance terms from retained
    dependence must be included rather than automatically adding the marginal covariance
    matrices.
- assessment_id: discrete-agreement
  area: evidence
  topic: discrete-agreement
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  - calculation
  summary: Supported with the stated construction and limitations.
  details: 'For copies on the same discrete state space and independent partition
    posteriors, the source defines agreement as P(theta_a=theta_b)=sum_k p_a(k)*p_b(k).
    If the copies are dependent, equality instead uses their joint probabilities.
    This is a posterior agreement mass under the replication law, not the posterior
    probability of the entire model and not a generally uniform frequentist p-value.
    Its magnitude depends on concentration and state-space granularity: identical
    diffuse distributions can have small equality mass.'
- assessment_id: continuous-scores
  area: evidence
  topic: continuous-scores
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  - calculation
  summary: Supported with the stated construction and limitations.
  details: For a continuous scalar separator define delta=h(theta_a)-h(theta_b) on
    a declared common scale, and inspect its posterior distribution. A signed tail
    P(delta>0), its complement, or a stated two-sided equal-tail score 2*min(P(delta>0),P(delta<=0))
    measures directional disagreement. The source also defines the density-level score
    P(p_delta(delta)<p_delta(0)); small values place zero in a low-density region.
    Under suitable continuous symmetric unimodal densities with no positive-probability
    density ties, the two-sided equal-tail and density-level scores coincide; they
    need not coincide for skewed or multimodal distributions. Density plateaus, mixed/discrete
    support and ties require an explicit convention. Kernel estimates introduce bandwidth,
    kernel and Monte Carlo uncertainty; a score is not a posterior point-null probability
    for a continuous difference.
- assessment_id: multivariate-score-options
  area: evidence
  topic: multivariate-score-options
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  - calculation
  summary: Supported with the stated construction and limitations.
  details: For a k-dimensional continuous difference with finite mean m and positive-definite
    covariance S, one option under a justified multivariate Gaussian approximation
    is the upper chi-square_k reference tail at m^T*S^-1*m. Another uses samples to
    estimate P((delta-m)^T*S^-1*(delta-m)>m^T*S^-1*m), a posterior radial score. A
    third estimates P(p_delta(delta)<p_delta(0)) from a multivariate density. These
    are separate choices. In particular, symmetry and unimodality alone do not imply
    ellipsoidal density contours, so the radial and density-level scores are not interchangeable
    on those assumptions alone; this distinction is curator reasoning. Singular covariance,
    deterministic constraints or non-existent moments require a separately justified
    construction, not an unqualified inverse or chi-square_k calculation.
- assessment_id: interpretation-and-calibration
  area: evidence
  topic: interpretation-and-calibration
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  - calculation
  summary: Supported with the stated construction and limitations.
  details: A conflict score points to local incompatibility under a particular partition,
    prior and scale; it does not establish which evidence source or model component
    is wrong. Posterior Gaussianity alone does not establish repeated-data calibration,
    and the source explicitly presents a practical framework rather than a general
    proof of uniformity for every split. Density-level scores can change under nonlinear
    changes of separator scale, even where a common strictly increasing scalar transformation
    preserves the sign comparison. Repeated fits and high-dimensional density estimation
    can be costly. Scores from different splits may be dependent, and systematic searches
    or multiple testing require their own assessed correction and calibration assumptions.
    Conflicting evidence may be masked or coexist with apparent aggregate model fit;
    source exclusion or clinical conclusions require further analysis.
- assessment_id: scores-and-scale
  area: consistency
  topic: Nonelliptical contours and nonlinear separator scales
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  - calculation
  summary: The record preserves score distinctions and states curator reasoning.
  details: A shifted product-Laplace difference has covariance 2I and null Mahalanobis
    distance squared 0.5, but density tail 2/e=0.7357588823 versus radial tail 0.6464792299.
    Refined deterministic quadrature agrees to floating-point precision. The same-radius
    points have unequal density. An exponential separator and fixed second copy give
    density tails 0.5 before a common log transform and 0.75 after it, with equal-tail
    score 1 in both scales. The explicitly constructed point-mass comparison is not
    portrayed as an application fit. Identical ten-state uniform copies have equality
    probability 0.1, demonstrating why agreement mass is not a model probability or
    calibrated p-value.
- assessment_id: dependence-and-calibration
  area: consistency
  topic: Proper distributions, joint replication law and calibration
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - presanis2013
  summary: No unsupported independence or universal uniformity claim was found.
  details: The full split and one-way nuisance cut are distinguished. The latter may
    retain dependence and covariance terms, so the record requires a joint law rather
    than automatically summing marginal covariances. Reference-prior normalization
    and split-posterior propriety are explicit. The chi-square formula is conditional
    on justified Gaussian scoring; it is not asserted to provide a universal repeated-data
    theorem. Discrete and density ties, deterministic constraints and singular/missing
    covariance moments are explicitly outside the unqualified inverse calculation.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SeparatorNodeConflictDiagnostic
  evidence_ids:
  - identity
  - mapping
  - presanis2013
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field: stable ID, name, empty aliases, algorithm kind, definition
    evidence, identity notes, seven claims and locators, source title/authors/version/URLs/access
    date/hash, pinned mapping revision and rationale, five limitations and actual
    UTC curation provenance. Verified exact report mirror, capture and context hashes,
    source bytes and rerun calculation output. The later multiple-testing source is
    retained as discovery follow-up rather than scientific evidence for this record.
    No actionable defect was found in this one-record author self-review.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT separator-node diagnostic, yielding 559 native and 442 unchanged
  generated records. The 744-entry main frontier retains 484 pending and 57 partly
  addressed cohorts; five new nested source leads remain.
- All 22 pages of the primary electronic reprint were read, including Figures 1–16,
  Table 1 and references. No author implementation, original application data analysis,
  MCMC, empirical calibration or benchmark was run. Constructed analytic and quadrature
  examples check distinctions between radial and density scores, nonlinear scale choices
  and discrete agreement; they are not reproductions of source experiments.
- The later multiple-testing paper was fully read as follow-up discovery, with source
  formula ambiguities retained in source_analysis; it is not silently used to claim
  a multiple-testing implementation in this record.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; only the isolated recovery checkout is
  changed.
related_reviews: []
links: []
tags:
- native-concepts
- model-diagnostics
- separator-nodes
- self-review
- discovery-ongoing
```
