# Scientific author self-review of sequential score-discrepancy conflict diagnostic

- Review: 20261017T084800Z-sequential-score-conflict
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T08:46:00Z
- Finished UTC: 2026-10-17T08:48:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the sequential score-discrepancy conflict diagnostic as a distinct DRAFT algorithm with related Bayesian-network context. All five claims and locators are supported with explicit parent-child DAG partition, single-draw Monte Carlo variance scaling, and dependent p-value combination boundaries. No actionable defect was found; author MCMC code and empirical calibration remain unverified.

## Scope And Provenance

All fields of the exact maintained sequential score-discrepancy conflict diagnostic and its primary evidence.

Selection: Exact maintained ID: AIMech:SequentialScoreDiscrepancyConflictDiagnostic
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5eecae31f3ad6f8790ea5af62e6052f0594a1728.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SequentialScoreDiscrepancyConflictDiagnostic | data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml | maintained | Sequential score-discrepancy conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:SequentialScoreDiscrepancyConflictDiagnostic | Checked 442 record(s); 0 failed.<br>Checked 563 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 216 history record(s); 0 error(s).<br> |
| just vendored-check | passed | True | AIMech:SequentialScoreDiscrepancyConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:SequentialScoreDiscrepancyConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SequentialScoreDiscrepancyConflictDiagnostic | Exited 0 without output. |
| Constructed sequential score conflict boundaries | passed | True | AIMech:SequentialScoreDiscrepancyConflictDiagnostic | {"dependent_pvalue_combinations": {"comonotonic_hcct_p": 0.04, "comonotonic_min_order_p": 0.4, "comonotonic_u": 0.04, "heterogeneous_hcct_p": 0.00936006, "heterogeneous_hcct_t": 68.00956456, "heterogeneous_min_order_p": 0.01, "null_boundary_hcct_p": 0.7195622}, "limits": "Constructed analytic two-stage normal DAG and closed-form p-value combination checks only; no MCMC, real-data epidemic model fit, or empirical repeated-data calibration simulation.", "single_draw_vs_exact_score_scaling": {"cond_var_single_given_y_obs": 1.25, "expected_cond_var": 0.375, "s_exact_obs": 0.875, "var_s_exact": 0.125, "var_s_single_marginal": 0.5, "variance_inflation_ratio": 4.0}} |

## Scientific And Domain Assessments

### Sequential DAG score conflict check versus general prior-expansion score and node splitting

identity: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Retain the sequential score-discrepancy conflict diagnostic as a distinct DRAFT algorithm.

The diagnostic combines two-stage parent-to-child DAG posterior propagation with conditional prior-expansion score evaluation on the child submodel and dependent p-value aggregation across parent draws (Algorithm 1 of Yang et al. 2026). It is distinct from the general Nott et al. (2020) prior-expansion score diagnostic and from node-splitting methods that duplicate separator nodes.

### Diagnostic-to-BayesianNetwork representation relation

grounding: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Related BayesianNetwork mapping is supported.

The diagnostic operates on a parent-child partition of a Bayesian directed acyclic graph. BayesianNetwork provides the graphical representation context via related_match.

### two-stage-dag-parent-child-partition

evidence: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Supported with explicit submodel propriety boundaries.

Observed data are partitioned into y_pa and y_ch around separator block theta_2; Stage 1 fits the parent submodel to y_pa_obs to draw theta_1^(1), ..., theta_1^(M) ~ p(theta_1 &#124; y_pa_obs), inducing conditional priors p(theta_2 &#124; theta_1^(m)) for Stage 2.

### conditional-prior-expansion-score-discrepancy

evidence: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Supported with positive-definite conditional covariance requirements.

Embedding p(theta_2 &#124; theta_1) into p(theta_2 &#124; theta_1, alpha) defines for each parent draw theta_1^(m) the conditional Fisher score S_alpha^(m)(y_ch) and quadratic discrepancy S_alpha^(m)(y_ch)^T V_{S^(m)}^(-1) S_alpha^(m)(y_ch).

### single-draw-posterior-score-approximation-and-scaling

evidence: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Supported with the Appendix D.2 variance scaling boundary verified.

Approximating the conditional posterior expectation by a single draw theta_2^(m) ~ p(theta_2 &#124; y_ch, theta_1^(m)) avoids an inner MCMC chain per parent draw, but adds conditional posterior Monte Carlo variance. In the normal hierarchical model (Appendix D.2, p. 43), the single-draw score has marginal variance 1/2 compared to tau^4 / (2*(sigma^2+tau^2)^2) for the exact conditional expectation, requiring matched estimators or explicit variance scaling.

### dependent-pvalue-aggregation

evidence: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Supported with explicit dependence and tail-approximation caveats.

The M conditional p-values p^(1), ..., p^(M) share y_ch_obs and are combined via order-statistic bounds or the Half-Cauchy Combination Test T_HCCT = (1/M) sum_m tan((pi/2)*(1 - p^(m))).

### avoidance-of-split-posterior-density-estimation

evidence: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

Supported as stated.

Evaluating conflict through conditional prior-expansion scores and scalar p-value combination avoids multivariate kernel density estimation on split-posterior differences.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SequentialScoreDiscrepancyConflictDiagnostic.

The full record is consistent; retain DRAFT.

Read every field of SequentialScoreDiscrepancyConflictDiagnostic.yaml: stable ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes, five claims and locators, two full-text primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T084600Z-sequential-score-conflict.json | supports | No normalized identity match for the sequential score-discrepancy conflict diagnostic across 442 pinned AIO records and 562 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources, research, history, and reviews returned 78 lines (all referencing the Round 167 discovery report and prior-expansion record that noted Yang et al. 2026 Section 3.1 as a separate pending concept). This concept denotes the two-stage parent-to-child DAG posterior propagation and conditional prior-expansion score check with dependent p-value aggregation (Algorithm 1 of Yang et al. 2026). |
| mapping | sources/aio/aio.json | supports | Inspected BayesianNetwork, ProbabilisticGraphicalModel, and EvaluationBias in the pinned AIO snapshot (2026-07-22). BayesianNetwork supplies directed acyclic graph and parent-child conditional factorization context as a related_match rather than an algorithm superclass. |
| calculation | research/discovery/sequential-score-conflict-boundaries.py | supports | Constructed exact analytic checks for (1) conditional posterior-expectation score vs. single-draw score estimator variance inflation ratio ((sigma^2 + tau^2)/tau^2)^2 in the two-stage normal DAG (Appendix D.2, p. 43), and (2) comonotonic invariance vs. M-fold conservatism of Half-Cauchy Combination Test (HCCT) and minimum order-statistic bounds. No MCMC, epidemic model fitting, or author software. |
| yang2026 | https://arxiv.org/pdf/2511.02977v2; Section 1, PDF pp. 2-4; Section 2.3-2.4, pp. 11-13; Section 3.1 and Algorithm 1, pp. 13-16; Section 4, pp. 21-28; Appendix D.2, p. 43 | supports | All 52 pages of the primary manuscript read, including Equations (6)-(15), Algorithm 1, simulation studies (Section 4), epidemic case study (Section 5), and Appendix D.2 (p. 43). Checked two-stage parent-child DAG partition, conditional prior-expansion score evaluation, single-draw approximation and variance scaling, and dependent p-value combination. |
| presanis2013 | https://arxiv.org/pdf/1310.0628v1; Section 2.1-2.2, PDF pp. 3-5 | supports | All 22 pages of the primary electronic reprint read, establishing the DAG separator node and ancestor/descendant evidence partition framework. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT sequential score-discrepancy conflict diagnostic, yielding 563 native and 442 unchanged generated records.
- All 52 pages of Yang et al. (2026) and all 22 pages of Presanis et al. (2013) were read. No author MCMC implementation, epidemic model fit, or empirical repeated-data calibration benchmark was run; constructed analytic examples verify variance scaling and p-value combination boundaries only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T084800Z-sequential-score-conflict
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of sequential score-discrepancy conflict diagnostic
started_at: '2026-10-17T08:46:00Z'
finished_at: '2026-10-17T08:48:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from general prior-expansion
    scores and separator node-splitting, two-stage parent-to-child DAG partitioning,
    single-draw versus exact conditional posterior-expectation score variance scaling
    (Appendix D.2), dependent p-value aggregation via order statistics and Half-Cauchy
    Combination Test, mapping and source support. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the sequential score-discrepancy conflict diagnostic as a distinct
  DRAFT algorithm with related Bayesian-network context. All five claims and locators
  are supported with explicit parent-child DAG partition, single-draw Monte Carlo
  variance scaling, and dependent p-value combination boundaries. No actionable defect
  was found; author MCMC code and empirical calibration remain unverified.
source:
  git_revision: 5eecae31f3ad6f8790ea5af62e6052f0594a1728
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/curated/CrossValidatedPriorLikelihoodConflictDiagnostic.yaml
    sha256: 92c4daf84d56e0ea6528ee512063fcf8d7fc8c69795bff9fe19fe5de8c65d119
    role: context
  - path: data/curated/GaussianMessageConflictDiagnostic.yaml
    sha256: adc6c4f1c16288b59515f77401ff4d1c2a02f673a00a91963de6e3fa588c4cff
    role: context
  - path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
    sha256: c97bf3553a26f7bb84a4539bf0cfed7d6bbe5170c7df411deb77ca1cf868f0b1
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/PriorExpansionScoreConflictDiagnostic.yaml
    sha256: a52b0ed1f942269c6a9fe0f48683b4d69a0706f522633b70e85bc05f48d8f792
    role: context
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: context
  - path: data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml
    sha256: 14d75f7ce1e21b32cf87cad76dc462d8ac60cf68d1fff58c12e6ba115c001871
    role: target
  - path: research/discovery/20261017T084600Z-sequential-score-conflict.json
    sha256: 81aaf0fe93cf31e04bee3b0a0ba4b61a0676fe509e884fbdc879e55f716f21db
    role: context
  - path: research/discovery/sequential-score-conflict-boundaries.py
    sha256: 20f6156c7e7ce5e2bd37e6ee24c490bf45b9755005b3177e967045c0d8c386e7
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
- target_id: AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  path: data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml
  label: Sequential score-discrepancy conflict diagnostic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml
    role: maintained
scope:
  description: All fields of the exact maintained sequential score-discrepancy conflict
    diagnostic and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SequentialScoreDiscrepancyConflictDiagnostic'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  exclusions:
  - target: Mixture-approximation node-splitting conflict diagnostic
    reason: Separate pending concept in Yang et al. (2026) Section 3.2 (Algorithm
      2); kept distinct from Section 3.1 Algorithm 1.
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical calibration
    reason: No author MCMC code, real-data epidemic model fit, or repeated-data calibration
      simulation run.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    Checked 563 curated concept record(s); 0 error(s).

    AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    Checked 216 history record(s); 0 error(s).

    '
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    '
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
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
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed sequential score conflict boundaries
  command: python3 research/discovery/sequential-score-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: '{"dependent_pvalue_combinations": {"comonotonic_hcct_p": 0.04, "comonotonic_min_order_p":
    0.4, "comonotonic_u": 0.04, "heterogeneous_hcct_p": 0.00936006, "heterogeneous_hcct_t":
    68.00956456, "heterogeneous_min_order_p": 0.01, "null_boundary_hcct_p": 0.7195622},
    "limits": "Constructed analytic two-stage normal DAG and closed-form p-value combination
    checks only; no MCMC, real-data epidemic model fit, or empirical repeated-data
    calibration simulation.", "single_draw_vs_exact_score_scaling": {"cond_var_single_given_y_obs":
    1.25, "expected_cond_var": 0.375, "s_exact_obs": 0.875, "var_s_exact": 0.125,
    "var_s_single_marginal": 0.5, "variance_inflation_ratio": 4.0}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T084600Z-sequential-score-conflict.json
  accessed_at: '2026-10-17T08:46:00Z'
  support: supports
  summary: No normalized identity match for the sequential score-discrepancy conflict
    diagnostic across 442 pinned AIO records and 562 maintained IDs, names, aliases
    and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across
    data, sources, research, history, and reviews returned 78 lines (all referencing
    the Round 167 discovery report and prior-expansion record that noted Yang et al.
    2026 Section 3.1 as a separate pending concept). This concept denotes the two-stage
    parent-to-child DAG posterior propagation and conditional prior-expansion score
    check with dependent p-value aggregation (Algorithm 1 of Yang et al. 2026).
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T08:46:00Z'
  support: supports
  summary: Inspected BayesianNetwork, ProbabilisticGraphicalModel, and EvaluationBias
    in the pinned AIO snapshot (2026-07-22). BayesianNetwork supplies directed acyclic
    graph and parent-child conditional factorization context as a related_match rather
    than an algorithm superclass.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/sequential-score-conflict-boundaries.py
  accessed_at: '2026-10-17T08:46:00Z'
  snapshot_sha256: 20f6156c7e7ce5e2bd37e6ee24c490bf45b9755005b3177e967045c0d8c386e7
  support: supports
  summary: Constructed exact analytic checks for (1) conditional posterior-expectation
    score vs. single-draw score estimator variance inflation ratio ((sigma^2 + tau^2)/tau^2)^2
    in the two-stage normal DAG (Appendix D.2, p. 43), and (2) comonotonic invariance
    vs. M-fold conservatism of Half-Cauchy Combination Test (HCCT) and minimum order-statistic
    bounds. No MCMC, epidemic model fitting, or author software.
- evidence_id: yang2026
  kind: primary_source
  reference: https://arxiv.org/pdf/2511.02977v2
  locator: Section 1, PDF pp. 2-4; Section 2.3-2.4, pp. 11-13; Section 3.1 and Algorithm
    1, pp. 13-16; Section 4, pp. 21-28; Appendix D.2, p. 43
  accessed_at: '2026-10-17T08:20:00Z'
  snapshot_sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d
  support: supports
  summary: All 52 pages of the primary manuscript read, including Equations (6)-(15),
    Algorithm 1, simulation studies (Section 4), epidemic case study (Section 5),
    and Appendix D.2 (p. 43). Checked two-stage parent-child DAG partition, conditional
    prior-expansion score evaluation, single-draw approximation and variance scaling,
    and dependent p-value combination.
- evidence_id: presanis2013
  kind: primary_source
  reference: https://arxiv.org/pdf/1310.0628v1
  locator: Section 2.1-2.2, PDF pp. 3-5
  accessed_at: '2026-10-17T08:20:00Z'
  snapshot_sha256: 9cff5092b47d7ba20f9ae654b6ea63bd4fdf75ea8ccfdb663427ccab36f3d3a0
  support: supports
  summary: All 22 pages of the primary electronic reprint read, establishing the DAG
    separator node and ancestor/descendant evidence partition framework.
assessments:
- assessment_id: identity
  area: identity
  topic: Sequential DAG score conflict check versus general prior-expansion score
    and node splitting
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - identity
  - yang2026
  - presanis2013
  summary: Retain the sequential score-discrepancy conflict diagnostic as a distinct
    DRAFT algorithm.
  details: The diagnostic combines two-stage parent-to-child DAG posterior propagation
    with conditional prior-expansion score evaluation on the child submodel and dependent
    p-value aggregation across parent draws (Algorithm 1 of Yang et al. 2026). It
    is distinct from the general Nott et al. (2020) prior-expansion score diagnostic
    and from node-splitting methods that duplicate separator nodes.
- assessment_id: mapping
  area: grounding
  topic: Diagnostic-to-BayesianNetwork representation relation
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - mapping
  - yang2026
  - presanis2013
  summary: Related BayesianNetwork mapping is supported.
  details: The diagnostic operates on a parent-child partition of a Bayesian directed
    acyclic graph. BayesianNetwork provides the graphical representation context via
    related_match.
- assessment_id: two-stage-dag-parent-child-partition
  area: evidence
  topic: two-stage-dag-parent-child-partition
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - yang2026
  - presanis2013
  summary: Supported with explicit submodel propriety boundaries.
  details: Observed data are partitioned into y_pa and y_ch around separator block
    theta_2; Stage 1 fits the parent submodel to y_pa_obs to draw theta_1^(1), ...,
    theta_1^(M) ~ p(theta_1 | y_pa_obs), inducing conditional priors p(theta_2 | theta_1^(m))
    for Stage 2.
- assessment_id: conditional-prior-expansion-score-discrepancy
  area: evidence
  topic: conditional-prior-expansion-score-discrepancy
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - yang2026
  - calculation
  summary: Supported with positive-definite conditional covariance requirements.
  details: Embedding p(theta_2 | theta_1) into p(theta_2 | theta_1, alpha) defines
    for each parent draw theta_1^(m) the conditional Fisher score S_alpha^(m)(y_ch)
    and quadratic discrepancy S_alpha^(m)(y_ch)^T V_{S^(m)}^(-1) S_alpha^(m)(y_ch).
- assessment_id: single-draw-posterior-score-approximation-and-scaling
  area: evidence
  topic: single-draw-posterior-score-approximation-and-scaling
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - yang2026
  - calculation
  summary: Supported with the Appendix D.2 variance scaling boundary verified.
  details: Approximating the conditional posterior expectation by a single draw theta_2^(m)
    ~ p(theta_2 | y_ch, theta_1^(m)) avoids an inner MCMC chain per parent draw, but
    adds conditional posterior Monte Carlo variance. In the normal hierarchical model
    (Appendix D.2, p. 43), the single-draw score has marginal variance 1/2 compared
    to tau^4 / (2*(sigma^2+tau^2)^2) for the exact conditional expectation, requiring
    matched estimators or explicit variance scaling.
- assessment_id: dependent-pvalue-aggregation
  area: evidence
  topic: dependent-pvalue-aggregation
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - yang2026
  - calculation
  summary: Supported with explicit dependence and tail-approximation caveats.
  details: The M conditional p-values p^(1), ..., p^(M) share y_ch_obs and are combined
    via order-statistic bounds or the Half-Cauchy Combination Test T_HCCT = (1/M)
    sum_m tan((pi/2)*(1 - p^(m))).
- assessment_id: avoidance-of-split-posterior-density-estimation
  area: evidence
  topic: avoidance-of-split-posterior-density-estimation
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - yang2026
  summary: Supported as stated.
  details: Evaluating conflict through conditional prior-expansion scores and scalar
    p-value combination avoids multivariate kernel density estimation on split-posterior
    differences.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SequentialScoreDiscrepancyConflictDiagnostic
  evidence_ids:
  - identity
  - mapping
  - yang2026
  - presanis2013
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of SequentialScoreDiscrepancyConflictDiagnostic.yaml:
    stable ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes,
    five claims and locators, two full-text primary sources with exact SHA-256 digests,
    pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT sequential score-discrepancy conflict diagnostic, yielding 563 native
  and 442 unchanged generated records.
- All 52 pages of Yang et al. (2026) and all 22 pages of Presanis et al. (2013) were
  read. No author MCMC implementation, epidemic model fit, or empirical repeated-data
  calibration benchmark was run; constructed analytic examples verify variance scaling
  and p-value combination boundaries only.
related_reviews: []
links: []
tags:
- native-concepts
- model-diagnostics
- bayesian-dags
- self-review
- discovery-ongoing
```
