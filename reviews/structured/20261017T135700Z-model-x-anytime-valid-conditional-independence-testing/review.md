# Scientific author self-review of Model-X anytime-valid conditional independence testing via e-processes

- Review: 20261017T135700Z-model-x-anytime-valid-conditional-independence-testing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T13:55:00Z
- Finished UTC: 2026-10-17T13:57:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Model-X anytime-valid conditional independence testing via e-processes as a distinct DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings. All four claims and locators across Grünwald, Henzi, &amp; Lardy (2024 JASA 119(546):1554-1565) and Shaer, Maman, &amp; Romano (2023 NeurIPS 36) are supported with explicit Model-X misspecification, Monte Carlo sample-size cap, and burn-in truncation limitations.

## Scope And Provenance

All fields of the exact maintained ModelXAnytimeValidConditionalIndependenceTesting record and its primary evidence.

Selection: Exact maintained ID: AIMech:ModelXAnytimeValidConditionalIndependenceTesting
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 84803ed6d63a35fac7f743d67f35b8e9678229e4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ModelXAnytimeValidConditionalIndependenceTesting | data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml | maintained | Model-X anytime-valid conditional independence testing via e-processes |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | All 583 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | Exited 0 without output. |
| Constructed Model-X anytime-valid conditional independence testing checks | passed | True | AIMech:ModelXAnytimeValidConditionalIndependenceTesting | {"claim1_exact_and_mc_conditional_e_statistic": {"exact_e_cond_expectation": 1.0, "mc_naive_cond_expectation": 1.239524, "mc_plus_one_cond_expectation": 1.0, "mc_plus_one_max_bound": 2.333333, "null_anytime_rejection_rate_m2": 0.034}, "claim2_gro_conditional_mutual_information_and_kl_regret": {"cmi_i_x_y_given_z": 0.12312, "gro_expected_log_growth": 0.12312, "max_e_gro_vs_likelihood_ratio_diff": 4e-16, "plugin_expected_log_growth": 0.096722, "prop4_exact_decomposition_diff": 0.0, "prop4_kl_lower_bound": 0.092637}, "claim3_tv_robustness_under_model_x_misspecification": {"null_reject_prob_under_hat_q": 0.0, "null_reject_prob_under_true_q": 0.0, "product_tv_distance": 0.057797, "theorem6_upper_bound_alpha_plus_tv": 0.157797}, "claim4_sequential_logistic_e_crt_and_truncation": {"alt_anytime_power": 1.0, "alt_mean_per_step_log_growth": 0.083661, "null_anytime_type1_error": 0.025, "single_step_e_truncated_eps005": 0.1, "single_step_e_untruncated_eps0": 1.9e-13}} |

## Scientific And Domain Assessments

### ModelXAnytimeValidConditionalIndependenceTesting versus SequentialKernelizedIndependenceTestingByBetting and KernelConditionalIndependenceTest

identity: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Retain Model-X anytime-valid conditional independence testing via e-processes as a distinct DRAFT mathematical_method.

ModelXAnytimeValidConditionalIndependenceTesting tests conditional independence X _&#124;&#124;_ Y &#124; Z under the Model-X assumption via conditional e-variables and Monte Carlo plus-one randomization draws without requiring i.i.d. outcome/covariate streams, whereas SequentialKernelizedIndependenceTestingByBetting tests unconditional independence X _&#124;&#124;_ Y by pairing i.i.d. observations and KernelConditionalIndependenceTest is a fixed-sample asymptotic test.

### Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis

grounding: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.

Model-X conditional e-processes guarantee anytime-valid Type-I error control under optional stopping (AIO:DataDredgingBias) and remain valid test martingales under arbitrary serial dependence of (Y_n, Z_n) (Proposition 3; AIO:TimeSeriesAnalysis).

### conditional-e-variable-monte-carlo-plus-one-exchangeability-and-test-martingale

evidence: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Supported by Section 2.1-2.2 Propositions 1-3, Equations 1-4, and Appendix A.

Verified exact conditional expectation E_{H_0}[E &#124; Y, Z] = 1.0 and Monte Carlo plus-one exact conditional expectation E_{H_0}[E^{(M)} &#124; Y, Z] = 1.0 (max bound 2.333333 &lt;= 3, null anytime rejection rate 0.034 &lt;= 0.10) vs. naive MC inflation 1.239524 &gt; 1.

### gro-conditional-mutual-information-and-conditional-kl-regret-identity

evidence: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Supported by Section 3.1-3.2 Theorem 4, Proposition 4, and Equations 5-9.

Verified GRO conditional e-variable equality with conditional likelihood ratio (max diff 4e-16), GRO log-growth equality with conditional mutual information I(X; Y &#124; Z) = 0.12312 &gt; 0.096722, and exact Proposition 4 conditional KL decomposition diff 0.0.

### total-variation-type-i-error-bound-under-model-x-misspecification

evidence: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Supported by Section 4 Proposition 5 and Theorem 6.

Verified Theorem 6 nonasymptotic Type-I error bound under covariate law misspecification (empirical rejection probability 0.0 &lt;= alpha + d_TV = 0.157797).

### truncation-protection-against-zero-lock-in-and-sequential-e-crt-betting

evidence: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

Supported by Section 3.2, Section 5 Equation 10, and Shaer, Maman, &amp; Romano (2023).

Verified single-step truncation floor (0.1 for eps=0.05 vs. 1.9e-13 untruncated under an outlier) and sequential logistic Model-X e-process null anytime Type-I error 0.025 &lt;= 0.05 and alternative power 1.0.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ModelXAnytimeValidConditionalIndependenceTesting.

The full record is consistent; retain DRAFT.

Read every field of ModelXAnytimeValidConditionalIndependenceTesting.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, four primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T135500Z-model-x-anytime-valid-conditional-independence-testing.json | supports | No normalized identity match for Model-X anytime-valid conditional independence testing across 442 pinned AIO records and 582 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias, TimeSeriesAnalysis, and LogisticRegression in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide optional-stopping and sequential-stream context via related_match. |
| calculation | research/discovery/model-x-anytime-valid-conditional-independence-testing-boundaries.py | supports | Constructed analytical and numerical checks for exact and Monte Carlo plus-one conditional e-variables, GRO conditional mutual information optimality and KL regret decomposition, Theorem 6 Total Variation robustness under Model-X misspecification, and sequential logistic e-CRT truncation, Type-I error, and power. |
| grunwald2024-model-x-ci-ar5iv | https://ar5iv.labs.arxiv.org/html/2209.12637; Sections 1-6 and Appendix A (lines 1-636, Propositions 1-5, Theorems 4 &amp; 6, Equations 1-10) | supports | All 636 lines of the full-text ar5iv HTML conversion of arXiv:2209.12637v2 read. Checked all theorems, propositions, equations, and proofs across Sections 1-6 and Appendix A. |
| grunwald2024-model-x-ci-crossref | https://api.crossref.org/works/10.1080/01621459.2023.2205607; Journal of the American Statistical Association Vol. 119, Issue 546, pp. 1554-1565 publication record | supports | Official JASA 119(546):1554-1565 Crossref record read and verified. |
| grunwald2024-model-x-ci-abs | https://arxiv.org/abs/2209.12637; arXiv:2209.12637v2 abstract and JASA 2024 metadata | supports | arXiv:2209.12637v2 abstract and JASA 2024 metadata read and verified. |
| shaer2023-ecrt-abs | https://arxiv.org/abs/2210.00354; arXiv:2210.00354v3 abstract (NeurIPS 2023 sequential Model-X e-CRT) | supports | arXiv:2210.00354v3 abstract on sequential Model-X e-CRT via betting read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Model-X anytime-valid conditional independence testing via e-processes record, yielding 583 native and 442 unchanged generated records.
- All 636 lines of Grünwald, Henzi, &amp; Lardy (2024, arXiv:2209.12637v2) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T135700Z-model-x-anytime-valid-conditional-independence-testing
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Model-X anytime-valid conditional independence
  testing via e-processes
started_at: '2026-10-17T13:55:00Z'
finished_at: '2026-10-17T13:57:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SequentialKernelizedIndependenceTestingByBetting
    and KernelConditionalIndependenceTest, the cumulative Total Variation misspecification
    degradation over long horizons in Theorem 6, the M+1 single-step cap of the Monte
    Carlo plus-one estimator in Proposition 2, and the necessity of truncation eps
    > 0 during sequential plug-in burn-in (Section 3.2, Section 5). This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Model-X anytime-valid conditional independence testing via e-processes
  as a distinct DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis
  mappings. All four claims and locators across Grünwald, Henzi, & Lardy (2024 JASA
  119(546):1554-1565) and Shaer, Maman, & Romano (2023 NeurIPS 36) are supported with
  explicit Model-X misspecification, Monte Carlo sample-size cap, and burn-in truncation
  limitations.
source:
  git_revision: 84803ed6d63a35fac7f743d67f35b8e9678229e4
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml
    sha256: 00eba6063c717bd325de163ab10f91b16f906630f6e81a4b04d61f7fa698445e
    role: target
  - path: data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml
    sha256: 7ab66808e86837214be02e6ca9183a7ebd19df51f6c6dbd9ddadfd84a1d81afe
    role: context
  - path: data/curated/SequentialKernelizedIndependenceTestingByBetting.yaml
    sha256: 13d50b1f150eec5c72de7b682597b072d55c89440d57ca0e2585bdf2b2d561d9
    role: context
  - path: research/discovery/20261017T135500Z-model-x-anytime-valid-conditional-independence-testing.json
    sha256: b65d8a81a089e39ae58ac2fd1f8b1037a1fd11012e03d099c003005fcd256b7a
    role: context
  - path: research/discovery/model-x-anytime-valid-conditional-independence-testing-boundaries.py
    sha256: 545fe37b8a23e0d4e620ced865d70eb33118c5de17b9bc8bbdcbd193aa794fbf
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
- target_id: AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  path: data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml
  label: Model-X anytime-valid conditional independence testing via e-processes
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ModelXAnytimeValidConditionalIndependenceTesting
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ModelXAnytimeValidConditionalIndependenceTesting'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: maintain-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 583 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Model-X anytime-valid conditional independence testing checks
  command: python3 research/discovery/model-x-anytime-valid-conditional-independence-testing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  exit_code: 0
  expected_exit_code: 0
  summary: '{"claim1_exact_and_mc_conditional_e_statistic": {"exact_e_cond_expectation":
    1.0, "mc_naive_cond_expectation": 1.239524, "mc_plus_one_cond_expectation": 1.0,
    "mc_plus_one_max_bound": 2.333333, "null_anytime_rejection_rate_m2": 0.034}, "claim2_gro_conditional_mutual_information_and_kl_regret":
    {"cmi_i_x_y_given_z": 0.12312, "gro_expected_log_growth": 0.12312, "max_e_gro_vs_likelihood_ratio_diff":
    4e-16, "plugin_expected_log_growth": 0.096722, "prop4_exact_decomposition_diff":
    0.0, "prop4_kl_lower_bound": 0.092637}, "claim3_tv_robustness_under_model_x_misspecification":
    {"null_reject_prob_under_hat_q": 0.0, "null_reject_prob_under_true_q": 0.0, "product_tv_distance":
    0.057797, "theorem6_upper_bound_alpha_plus_tv": 0.157797}, "claim4_sequential_logistic_e_crt_and_truncation":
    {"alt_anytime_power": 1.0, "alt_mean_per_step_log_growth": 0.083661, "null_anytime_type1_error":
    0.025, "single_step_e_truncated_eps005": 0.1, "single_step_e_untruncated_eps0":
    1.9e-13}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T135500Z-model-x-anytime-valid-conditional-independence-testing.json
  accessed_at: '2026-10-17T13:55:00Z'
  support: supports
  summary: No normalized identity match for Model-X anytime-valid conditional independence
    testing across 442 pinned AIO records and 582 maintained IDs, names, aliases and
    scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T13:55:00Z'
  support: supports
  summary: Inspected DataDredgingBias, TimeSeriesAnalysis, and LogisticRegression
    in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis
    provide optional-stopping and sequential-stream context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/model-x-anytime-valid-conditional-independence-testing-boundaries.py
  accessed_at: '2026-10-17T13:55:00Z'
  snapshot_sha256: 545fe37b8a23e0d4e620ced865d70eb33118c5de17b9bc8bbdcbd193aa794fbf
  support: supports
  summary: Constructed analytical and numerical checks for exact and Monte Carlo plus-one
    conditional e-variables, GRO conditional mutual information optimality and KL
    regret decomposition, Theorem 6 Total Variation robustness under Model-X misspecification,
    and sequential logistic e-CRT truncation, Type-I error, and power.
- evidence_id: grunwald2024-model-x-ci-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2209.12637
  locator: Sections 1-6 and Appendix A (lines 1-636, Propositions 1-5, Theorems 4
    & 6, Equations 1-10)
  accessed_at: '2026-10-17T13:55:00Z'
  snapshot_sha256: 2a68c4355f736174f431b7610664b603bb0210fdfeb010de3ba0461ea9ee8b16
  support: supports
  summary: All 636 lines of the full-text ar5iv HTML conversion of arXiv:2209.12637v2
    read. Checked all theorems, propositions, equations, and proofs across Sections
    1-6 and Appendix A.
- evidence_id: grunwald2024-model-x-ci-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1080/01621459.2023.2205607
  locator: Journal of the American Statistical Association Vol. 119, Issue 546, pp.
    1554-1565 publication record
  accessed_at: '2026-10-17T13:55:00Z'
  snapshot_sha256: 8efce92ca7a71b0526bbc4370bb510433bd1de67a6ec01e4818ca3cd563083ba
  support: supports
  summary: Official JASA 119(546):1554-1565 Crossref record read and verified.
- evidence_id: grunwald2024-model-x-ci-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2209.12637
  locator: arXiv:2209.12637v2 abstract and JASA 2024 metadata
  accessed_at: '2026-10-17T13:55:00Z'
  snapshot_sha256: 2ffb4cdf23e82030c267f75ccd5bee104b88a42099cf4bb84adb6934bb1c4131
  support: supports
  summary: arXiv:2209.12637v2 abstract and JASA 2024 metadata read and verified.
- evidence_id: shaer2023-ecrt-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2210.00354
  locator: arXiv:2210.00354v3 abstract (NeurIPS 2023 sequential Model-X e-CRT)
  accessed_at: '2026-10-17T13:55:00Z'
  snapshot_sha256: 397b2ffe9dac56cd2303888dd2bfdf0b34cca3994404cf80ef8f7b709d84b8d3
  support: supports
  summary: arXiv:2210.00354v3 abstract on sequential Model-X e-CRT via betting read
    and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ModelXAnytimeValidConditionalIndependenceTesting versus SequentialKernelizedIndependenceTestingByBetting
    and KernelConditionalIndependenceTest
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - identity
  - grunwald2024-model-x-ci-ar5iv
  - grunwald2024-model-x-ci-crossref
  summary: Retain Model-X anytime-valid conditional independence testing via e-processes
    as a distinct DRAFT mathematical_method.
  details: ModelXAnytimeValidConditionalIndependenceTesting tests conditional independence
    X _||_ Y | Z under the Model-X assumption via conditional e-variables and Monte
    Carlo plus-one randomization draws without requiring i.i.d. outcome/covariate
    streams, whereas SequentialKernelizedIndependenceTestingByBetting tests unconditional
    independence X _||_ Y by pairing i.i.d. observations and KernelConditionalIndependenceTest
    is a fixed-sample asymptotic test.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - mapping
  - grunwald2024-model-x-ci-ar5iv
  summary: Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.
  details: Model-X conditional e-processes guarantee anytime-valid Type-I error control
    under optional stopping (AIO:DataDredgingBias) and remain valid test martingales
    under arbitrary serial dependence of (Y_n, Z_n) (Proposition 3; AIO:TimeSeriesAnalysis).
- assessment_id: conditional-e-variable-monte-carlo-plus-one-exchangeability-and-test-martingale
  area: evidence
  topic: conditional-e-variable-monte-carlo-plus-one-exchangeability-and-test-martingale
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - grunwald2024-model-x-ci-ar5iv
  - grunwald2024-model-x-ci-abs
  - calculation
  summary: Supported by Section 2.1-2.2 Propositions 1-3, Equations 1-4, and Appendix
    A.
  details: Verified exact conditional expectation E_{H_0}[E | Y, Z] = 1.0 and Monte
    Carlo plus-one exact conditional expectation E_{H_0}[E^{(M)} | Y, Z] = 1.0 (max
    bound 2.333333 <= 3, null anytime rejection rate 0.034 <= 0.10) vs. naive MC inflation
    1.239524 > 1.
- assessment_id: gro-conditional-mutual-information-and-conditional-kl-regret-identity
  area: evidence
  topic: gro-conditional-mutual-information-and-conditional-kl-regret-identity
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - grunwald2024-model-x-ci-ar5iv
  - grunwald2024-model-x-ci-crossref
  - calculation
  summary: Supported by Section 3.1-3.2 Theorem 4, Proposition 4, and Equations 5-9.
  details: Verified GRO conditional e-variable equality with conditional likelihood
    ratio (max diff 4e-16), GRO log-growth equality with conditional mutual information
    I(X; Y | Z) = 0.12312 > 0.096722, and exact Proposition 4 conditional KL decomposition
    diff 0.0.
- assessment_id: total-variation-type-i-error-bound-under-model-x-misspecification
  area: evidence
  topic: total-variation-type-i-error-bound-under-model-x-misspecification
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - grunwald2024-model-x-ci-ar5iv
  - calculation
  summary: Supported by Section 4 Proposition 5 and Theorem 6.
  details: Verified Theorem 6 nonasymptotic Type-I error bound under covariate law
    misspecification (empirical rejection probability 0.0 <= alpha + d_TV = 0.157797).
- assessment_id: truncation-protection-against-zero-lock-in-and-sequential-e-crt-betting
  area: evidence
  topic: truncation-protection-against-zero-lock-in-and-sequential-e-crt-betting
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - grunwald2024-model-x-ci-ar5iv
  - shaer2023-ecrt-abs
  - calculation
  summary: Supported by Section 3.2, Section 5 Equation 10, and Shaer, Maman, & Romano
    (2023).
  details: Verified single-step truncation floor (0.1 for eps=0.05 vs. 1.9e-13 untruncated
    under an outlier) and sequential logistic Model-X e-process null anytime Type-I
    error 0.025 <= 0.05 and alternative power 1.0.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ModelXAnytimeValidConditionalIndependenceTesting
  evidence_ids:
  - identity
  - mapping
  - grunwald2024-model-x-ci-ar5iv
  - grunwald2024-model-x-ci-crossref
  - grunwald2024-model-x-ci-abs
  - shaer2023-ecrt-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ModelXAnytimeValidConditionalIndependenceTesting.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, four primary sources with exact SHA-256
    digests, two pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Model-X anytime-valid conditional independence testing via e-processes
  record, yielding 583 native and 442 unchanged generated records.
- All 636 lines of Grünwald, Henzi, & Lardy (2024, arXiv:2209.12637v2) were read in
  full text.
related_reviews: []
links: []
tags:
- native-concepts
- conditional-independence
- model-x
- e-processes
- anytime-valid-inference
- test-martingales
- self-review
- discovery-ongoing
```
