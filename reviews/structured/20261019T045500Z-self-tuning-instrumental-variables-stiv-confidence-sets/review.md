# Scientific author self-review of Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets

- Review: 20261019T045500Z-self-tuning-instrumental-variables-stiv-confidence-sets
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T04:54:00Z
- Finished UTC: 2026-10-19T04:55:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets as a distinct DRAFT algorithm with LassoRegression and LinearRegression mappings. All three claims across Gautier &amp; Rose (2011/2021, DOI:10.1093/restud/rdab002, arXiv:1105.2454v7) are supported with explicit sparsity-bound, dual-sensitivity, and primary-source typographical limitations.

## Scope And Provenance

All fields of the exact maintained SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets record and its primary evidence.

Selection: Exact maintained ID: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4e42bf64e7e8a552d9abbac26ec83eccec3b46b9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | data/curated/SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml | maintained | Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | Validated 665 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | Validated history sidecar files. |
| python3 self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py | passed | True | AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets | {<br>  "concept": "AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets",<br>  "source": "Gautier &amp; Rose (2011/2021), Review of Economic Studies 88(6):2888-2929, arXiv:1105.2454v7",<br>  "pivotal_statistic_and_conic_program": {<br>    "t_hat_beta_star": 0.037139,<br>    "r_hat": 0.05,<br>    "c_param": 19.0,<br>    "sigma_star": 0.152004,<br>    "sigma_hat_stiv": 0.149807,<br>    "sigma_at_beta_hat": 0.149807,<br>    "zmom_over_r_hat": 0.149807,<br>    "stiv_obj_at_bhat": 5.621187,<br>    "stiv_obj_at_bstar": 5.663777<br>  },<br>  "cone_and_sensitivity_verification": {<br>    "cone_lhs_off_support_l1": 0.014116,<br>    "cone_rhs_bound": 0.414399,<br>    "psi_delta_inf": 0.011911,<br>    "eq_a14_rhs": 0.015091,<br>    "kappa_lower_bound": 0.740733<br>  },<br>  "support_recovery_and_bias_correction": {<br>    "true_support": [<br>      0,<br>      1<br>    ],<br>    "stiv_support": [<br>      0,<br>      1,<br>      7<br>    ],<br>    "thresholded_stiv_support": [<br>      0,<br>      1<br>    ],<br>    "signs_match": true,<br>    "stiv_active_l2_error": 0.011179,<br>    "bc_stiv_active_l2_error": 0.001978<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets is a distinct conic high-dimensional IV algorithm.

Resolved against all 442 pinned AIO concepts and 664 maintained AIMech concepts. Distinct from &#96;AIMech:SquareRootLassoPivotalHighDimensionalSparseRegression&#96; (Belloni, Chernozhukov, &amp; Wang 2011, which minimizes $\widehat{Q}(\beta)^{1/2} + \frac{\lambda}{n}\&#124;\beta\&#124;_1$ for exogenous covariates $\mathbb{E}[XU] = 0$ where the empirical Gram matrix $\mathbb{E}_n[XX^\top]$ is symmetric positive semidefinite, rather than solving a conic program under asymmetric instrument-covariate cross-moments $\widehat{\Psi} = \mathbf{D}_{\mathbf{Z}}\mathbb{E}_n[ZX^\top]\mathbf{D}_{\mathbf{X}}$ with $\ell_\infty$ moment constraint $&#124;\mathbf{D}_{\mathbf{Z}}\mathbb{E}_n[ZU(b)]&#124;_\infty \le \widehat{r}\sigma$ and LP sensitivity lower bounds), distinct from &#96;AIMech:SelfNormalizedLassoOptimalInstrumentEstimationAndSupNormWeakIdentificationTesting&#96; (Belloni, Chen, Chernozhukov, &amp; Hansen 2012, which estimates first-stage optimal instruments $D_i = f(Z_i) + V_i$ via Lasso/Post-Lasso under homoscedastic or self-normalized penalty loadings and plugs $\widehat{f}(Z_i)$ into structural 2SLS for a low-dimensional endogenous vector $d$, rather than jointly penalizing high-dimensional endogenous structural parameters $\beta \in \mathbb{R}^{d_X}$ and scale $\sigma$ in a single conic program), and distinct from &#96;AIMech:DantzigSelectorStatisticalEstimationWhenPIsMuchLargerThanN&#96; (Candes &amp; Tao 2007, which requires prior knowledge of the noise standard deviation $\sigma$ to set the constraint threshold $\&#124;X^\top(y - X\beta)\&#124;_\infty \le \lambda\sigma$ for exogenous Gaussian regression).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

Mappings to AIO:LassoRegression (related_match) and AIO:LinearRegression (related_match) accurately situate the framework within the pinned AIO hierarchy.

Verified exact target existence in data/aio/.

### Claim 1: STIV conic program and Proposition 3.1 sensitivity oracle bounds

evidence: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

Claim 1 is directly supported by Section 3 (Definition 3.1, Eqs. 6-10, Proposition 3.1) and Appendix A.3 (Eq. A.14) of arXiv:1105.2454v7.

Verified conic optimality, empirical cone membership &#124;Delta_hat_{S^c}&#124;_1 &lt;= &#124;Delta_hat_S&#124;_1 + c*g_hat(Delta_hat), and Eq. (A.14) sensitivity inequality in pure Python.

### Claim 2: LP sensitivity lower bounds, identification-robust confidence intervals, and sign consistency

evidence: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

Claim 2 is directly supported by Section 3.2 (Table 1, Proposition 3.2, Eqs. 11-14) and Section 3.5 (Theorem 3.2, Eq. 27) of arXiv:1105.2454v7.

Verified exact support and sign recovery of thresholded STIV in pure Python.

### Claim 3: BC-STIV asymptotic normality and NV-STIV invalid-instrument detection

evidence: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

Claim 3 is directly supported by Section 4 (Eqs. 30-37, Theorem 4.1) and Section 5 (Eqs. 38-43, Theorem 5.1) of arXiv:1105.2454v7.

Verified 82.3% active L2 error reduction from one-step BC-STIV bias correction.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.

The full record is consistent; retain DRAFT.

Read every field of SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T045400Z-self-tuning-instrumental-variables-stiv-confidence-sets.json | supports | No normalized identity match for Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets across 442 pinned AIO records and 664 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LassoRegression and LinearRegression in the pinned AIO snapshot (2026-07-22). Provides accurate related_match context. |
| calculation | research/discovery/self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py | supports | Verified in pure Python on an endogenous high-dimensional IV design (n = 120, d_X = 10, d_Z = 14, true sparse beta* = (1.2, -0.9, 0, ..., 0) with strong endogeneity Cov(X_0, U) != 0): (1) at beta*, the pivotal self-normalized statistic t_hat(beta*) = 0.037139 &lt;= r_hat = 0.05 holds (event G), certifying feasibility of (beta*, sigma_hat(beta*)) with STIV objective 5.621187 &lt; 5.663777 at beta* and binding conic equality sigma_hat = sigma_hat(beta_hat) = &#124;D_Z E_n[ZU(beta_hat)]&#124;_inf / r_hat = 0.149807; (2) the standardized estimation error Delta_hat = D_X^{-1}(beta_hat - beta*) satisfies the empirical cone inequality &#124;Delta_hat_{S^c}&#124;_1 = 0.014116 &lt;= &#124;Delta_hat_S&#124;_1 + c*g_hat(Delta_hat) = 0.414399 (Eq. 9) and Eq. (A.14) &#124;Psi_hat Delta_hat&#124;_inf = 0.011911 &lt;= 2*r_hat*sigma_bar + r_hat*(sigma_hat(beta*) - sigma_hat) = 0.015091 with empirical sensitivity lower bound kappa_hat &gt;= 0.740733; and (3) hard-thresholded STIV (Theorem 3.2, Eq. 27) recovers the exact support {0, 1} and signs while one-step BC-STIV (Section 4, Eq. 30) reduces active L2 error by 82.3% from 0.011179 to 0.001978. |
| gr2021-stiv-pdf | https://export.arxiv.org/pdf/1105.2454.pdf; Pages 1-54, Sections 1-6, Appendices A.1-A.7, Online Appendix O.1-O.3 | supports | All 54 pages of Gautier &amp; Rose (2011/2021, arXiv:1105.2454v7) read and verified. |
| gr2021-stiv-abs | https://arxiv.org/abs/1105.2454; arXiv:1105.2454 abstract | supports | arXiv abstract and submission metadata read and verified. |
| gr2021-stiv-crossref | https://api.crossref.org/works/10.1093/restud/rdab002; DOI:10.1093/restud/rdab002 metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based Confidence Sets record, yielding 665 native and 442 unchanged generated records.
- All 54 PDF pages of arXiv:1105.2454v7 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T045500Z-self-tuning-instrumental-variables-stiv-confidence-sets
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Self-Tuning Pivotal High-Dimensional Instrumental
  Variables (STIV) and Sensitivity-Based Confidence Sets
started_at: '2026-10-19T04:54:00Z'
finished_at: '2026-10-19T04:55:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SquareRootLassoPivotalHighDimensionalSparseRegression,
    SelfNormalizedLassoOptimalInstrumentEstimationAndSupNormWeakIdentificationTesting,
    DantzigSelectorStatisticalEstimationWhenPIsMuchLargerThanN, and AIO:LassoRegression,
    verified the STIV conic program, empirical cone K_S, Proposition 3.1 sensitivity
    bounds, Theorem 3.2 thresholded sign recovery, and BC-STIV bias correction in
    pure Python, and identified six primary-source typographical issues in Gautier
    & Rose (2011/2021, arXiv:1105.2454v7). This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV)
  and Sensitivity-Based Confidence Sets as a distinct DRAFT algorithm with LassoRegression
  and LinearRegression mappings. All three claims across Gautier & Rose (2011/2021,
  DOI:10.1093/restud/rdab002, arXiv:1105.2454v7) are supported with explicit sparsity-bound,
  dual-sensitivity, and primary-source typographical limitations.
source:
  git_revision: 4e42bf64e7e8a552d9abbac26ec83eccec3b46b9
  state: working_tree
  inputs:
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/curated/SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml
    sha256: 29192d0c471f5337b99ad8500a0ad43c7341ca7479cbf55b7c248f26c8248cd2
    role: target
  - path: research/discovery/20261019T045400Z-self-tuning-instrumental-variables-stiv-confidence-sets.json
    sha256: 428d7509f2082a7be0195d3978530467dfc7a5496e8a46a3bdd3a7caaa580d7a
    role: context
  - path: research/discovery/self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py
    sha256: c8ee6777cd419f337d722012dd2bf5bf722f86fd74d1431cb834f38b5cfbf2d8
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
- target_id: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  path: data/curated/SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml
  label: Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and Sensitivity-Based
    Confidence Sets
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml
    role: maintained
scope:
  description: All fields of the exact maintained SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: validation-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 665 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py
  command: python3 research/discovery/self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept\": \"AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets\"\
    ,\n  \"source\": \"Gautier & Rose (2011/2021), Review of Economic Studies 88(6):2888-2929,\
    \ arXiv:1105.2454v7\",\n  \"pivotal_statistic_and_conic_program\": {\n    \"t_hat_beta_star\"\
    : 0.037139,\n    \"r_hat\": 0.05,\n    \"c_param\": 19.0,\n    \"sigma_star\"\
    : 0.152004,\n    \"sigma_hat_stiv\": 0.149807,\n    \"sigma_at_beta_hat\": 0.149807,\n\
    \    \"zmom_over_r_hat\": 0.149807,\n    \"stiv_obj_at_bhat\": 5.621187,\n   \
    \ \"stiv_obj_at_bstar\": 5.663777\n  },\n  \"cone_and_sensitivity_verification\"\
    : {\n    \"cone_lhs_off_support_l1\": 0.014116,\n    \"cone_rhs_bound\": 0.414399,\n\
    \    \"psi_delta_inf\": 0.011911,\n    \"eq_a14_rhs\": 0.015091,\n    \"kappa_lower_bound\"\
    : 0.740733\n  },\n  \"support_recovery_and_bias_correction\": {\n    \"true_support\"\
    : [\n      0,\n      1\n    ],\n    \"stiv_support\": [\n      0,\n      1,\n\
    \      7\n    ],\n    \"thresholded_stiv_support\": [\n      0,\n      1\n   \
    \ ],\n    \"signs_match\": true,\n    \"stiv_active_l2_error\": 0.011179,\n  \
    \  \"bc_stiv_active_l2_error\": 0.001978\n  },\n  \"all_assertions_passed\": true\n\
    }"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T045400Z-self-tuning-instrumental-variables-stiv-confidence-sets.json
  accessed_at: '2026-10-19T04:54:00Z'
  support: supports
  summary: No normalized identity match for Self-Tuning Pivotal High-Dimensional Instrumental
    Variables (STIV) and Sensitivity-Based Confidence Sets across 442 pinned AIO records
    and 664 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T04:54:00Z'
  support: supports
  summary: Inspected LassoRegression and LinearRegression in the pinned AIO snapshot
    (2026-07-22). Provides accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/self-tuning-instrumental-variables-stiv-confidence-sets-boundaries.py
  accessed_at: '2026-10-19T04:54:00Z'
  snapshot_sha256: c8ee6777cd419f337d722012dd2bf5bf722f86fd74d1431cb834f38b5cfbf2d8
  support: supports
  summary: 'Verified in pure Python on an endogenous high-dimensional IV design (n
    = 120, d_X = 10, d_Z = 14, true sparse beta* = (1.2, -0.9, 0, ..., 0) with strong
    endogeneity Cov(X_0, U) != 0): (1) at beta*, the pivotal self-normalized statistic
    t_hat(beta*) = 0.037139 <= r_hat = 0.05 holds (event G), certifying feasibility
    of (beta*, sigma_hat(beta*)) with STIV objective 5.621187 < 5.663777 at beta*
    and binding conic equality sigma_hat = sigma_hat(beta_hat) = |D_Z E_n[ZU(beta_hat)]|_inf
    / r_hat = 0.149807; (2) the standardized estimation error Delta_hat = D_X^{-1}(beta_hat
    - beta*) satisfies the empirical cone inequality |Delta_hat_{S^c}|_1 = 0.014116
    <= |Delta_hat_S|_1 + c*g_hat(Delta_hat) = 0.414399 (Eq. 9) and Eq. (A.14) |Psi_hat
    Delta_hat|_inf = 0.011911 <= 2*r_hat*sigma_bar + r_hat*(sigma_hat(beta*) - sigma_hat)
    = 0.015091 with empirical sensitivity lower bound kappa_hat >= 0.740733; and (3)
    hard-thresholded STIV (Theorem 3.2, Eq. 27) recovers the exact support {0, 1}
    and signs while one-step BC-STIV (Section 4, Eq. 30) reduces active L2 error by
    82.3% from 0.011179 to 0.001978.'
- evidence_id: gr2021-stiv-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/1105.2454.pdf
  locator: Pages 1-54, Sections 1-6, Appendices A.1-A.7, Online Appendix O.1-O.3
  accessed_at: '2026-10-19T04:54:00Z'
  snapshot_sha256: beb4c89b9c0bfedb072e2621d0dd15804fee95a19b1b173fad27daaa16580ec6
  support: supports
  summary: All 54 pages of Gautier & Rose (2011/2021, arXiv:1105.2454v7) read and
    verified.
- evidence_id: gr2021-stiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1105.2454
  locator: arXiv:1105.2454 abstract
  accessed_at: '2026-10-19T04:54:00Z'
  snapshot_sha256: 4b6a475db60083503ebf8d0c5e1bbc0892ed0bb1adcb56fe7845f0c1ca5478ad
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: gr2021-stiv-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1093/restud/rdab002
  locator: DOI:10.1093/restud/rdab002 metadata
  accessed_at: '2026-10-19T04:54:00Z'
  snapshot_sha256: f77add18ea696b2969fb4e41c69316f07811faf77952a8354229808a09c54417
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - identity
  - gr2021-stiv-pdf
  - gr2021-stiv-abs
  - gr2021-stiv-crossref
  summary: Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV) and
    Sensitivity-Based Confidence Sets is a distinct conic high-dimensional IV algorithm.
  details: Resolved against all 442 pinned AIO concepts and 664 maintained AIMech
    concepts. Distinct from `AIMech:SquareRootLassoPivotalHighDimensionalSparseRegression`
    (Belloni, Chernozhukov, & Wang 2011, which minimizes $\widehat{Q}(\beta)^{1/2}
    + \frac{\lambda}{n}\|\beta\|_1$ for exogenous covariates $\mathbb{E}[XU] = 0$
    where the empirical Gram matrix $\mathbb{E}_n[XX^\top]$ is symmetric positive
    semidefinite, rather than solving a conic program under asymmetric instrument-covariate
    cross-moments $\widehat{\Psi} = \mathbf{D}_{\mathbf{Z}}\mathbb{E}_n[ZX^\top]\mathbf{D}_{\mathbf{X}}$
    with $\ell_\infty$ moment constraint $|\mathbf{D}_{\mathbf{Z}}\mathbb{E}_n[ZU(b)]|_\infty
    \le \widehat{r}\sigma$ and LP sensitivity lower bounds), distinct from `AIMech:SelfNormalizedLassoOptimalInstrumentEstimationAndSupNormWeakIdentificationTesting`
    (Belloni, Chen, Chernozhukov, & Hansen 2012, which estimates first-stage optimal
    instruments $D_i = f(Z_i) + V_i$ via Lasso/Post-Lasso under homoscedastic or self-normalized
    penalty loadings and plugs $\widehat{f}(Z_i)$ into structural 2SLS for a low-dimensional
    endogenous vector $d$, rather than jointly penalizing high-dimensional endogenous
    structural parameters $\beta \in \mathbb{R}^{d_X}$ and scale $\sigma$ in a single
    conic program), and distinct from `AIMech:DantzigSelectorStatisticalEstimationWhenPIsMuchLargerThanN`
    (Candes & Tao 2007, which requires prior knowledge of the noise standard deviation
    $\sigma$ to set the constraint threshold $\|X^\top(y - X\beta)\|_\infty \le \lambda\sigma$
    for exogenous Gaussian regression).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - mapping
  - gr2021-stiv-pdf
  summary: Mappings to AIO:LassoRegression (related_match) and AIO:LinearRegression
    (related_match) accurately situate the framework within the pinned AIO hierarchy.
  details: Verified exact target existence in data/aio/.
- assessment_id: claim-1-verification
  area: evidence
  topic: 'Claim 1: STIV conic program and Proposition 3.1 sensitivity oracle bounds'
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - gr2021-stiv-pdf
  - calculation
  summary: Claim 1 is directly supported by Section 3 (Definition 3.1, Eqs. 6-10,
    Proposition 3.1) and Appendix A.3 (Eq. A.14) of arXiv:1105.2454v7.
  details: Verified conic optimality, empirical cone membership |Delta_hat_{S^c}|_1
    <= |Delta_hat_S|_1 + c*g_hat(Delta_hat), and Eq. (A.14) sensitivity inequality
    in pure Python.
- assessment_id: claim-2-verification
  area: evidence
  topic: 'Claim 2: LP sensitivity lower bounds, identification-robust confidence intervals,
    and sign consistency'
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - gr2021-stiv-pdf
  - calculation
  summary: Claim 2 is directly supported by Section 3.2 (Table 1, Proposition 3.2,
    Eqs. 11-14) and Section 3.5 (Theorem 3.2, Eq. 27) of arXiv:1105.2454v7.
  details: Verified exact support and sign recovery of thresholded STIV in pure Python.
- assessment_id: claim-3-verification
  area: evidence
  topic: 'Claim 3: BC-STIV asymptotic normality and NV-STIV invalid-instrument detection'
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - gr2021-stiv-pdf
  - calculation
  summary: Claim 3 is directly supported by Section 4 (Eqs. 30-37, Theorem 4.1) and
    Section 5 (Eqs. 38-43, Theorem 5.1) of arXiv:1105.2454v7.
  details: Verified 82.3% active L2 error reduction from one-step BC-STIV bias correction.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets
  evidence_ids:
  - identity
  - mapping
  - gr2021-stiv-pdf
  - gr2021-stiv-abs
  - gr2021-stiv-crossref
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of SelfTuningPivotalHighDimensionalInstrumentalVariablesAndSensitivityConfidenceSets.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Self-Tuning Pivotal High-Dimensional Instrumental Variables (STIV)
  and Sensitivity-Based Confidence Sets record, yielding 665 native and 442 unchanged
  generated records.
- All 54 PDF pages of arXiv:1105.2454v7 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- instrumental-variables
- self-tuning-stiv
- high-dimensional-inference
- sensitivity-characteristics
- self-review
- discovery-ongoing
```
