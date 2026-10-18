# Scientific author self-review of Self-consistency and dependency control framework for false discovery rate control

- Review: 20261017T153200Z-self-consistency-and-dependency-control-fdr-framework
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T15:30:00Z
- Finished UTC: 2026-10-17T15:32:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Self-consistency and dependency control framework for false discovery rate control as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Blanchard &amp; Roquain (2008 Electronic Journal of Statistics 2:963-992) are supported with explicit PRDS/monotonicity, prior-selectionnu trade-off, and adaptive plug-in monotonicity limitations.

## Scope And Provenance

All fields of the exact maintained SelfConsistencyAndDependencyControlFDRFramework record and its primary evidence.

Selection: Exact maintained ID: AIMech:SelfConsistencyAndDependencyControlFDRFramework
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4e4cdc5113ee3d9d9cd81dc94dfec4ad6bf91020.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SelfConsistencyAndDependencyControlFDRFramework | data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml | maintained | Self-consistency and dependency control framework for false discovery rate control |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | All 594 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | Exited 0 without output. |
| Constructed Blanchard-Roquain SC and DC framework checks | passed | True | AIMech:SelfConsistencyAndDependencyControlFDRFramework | {<br>  "concept_id": "AIMech:SelfConsistencyAndDependencyControlFDRFramework",<br>  "primary_source": "Blanchard &amp; Roquain (2008), Electronic Journal of Statistics 2:963-992 (arXiv:0802.1406v2, DOI:10.1214/08-EJS180)",<br>  "order_free_self_consistency": {<br>    "total_volume_lambda_H": 6.0,<br>    "pi_lambda_integral": 1.0,<br>    "fixed_point_checks": 4,<br>    "maximality_checks": 4,<br>    "disconnected_r_su": [<br>      0,<br>      2,<br>      3<br>    ],<br>    "contiguous_self_consistent_subset": [<br>      2,<br>      3<br>    ]<br>  },<br>  "arbitrary_dependence_beta_nu_family": {<br>    "m": 6,<br>    "alpha": 0.1,<br>    "gamma_m": 2.45,<br>    "adversarial_sup_expectations_over_c": {<br>      "linear_simes": 2.4500000000000006,<br>      "BY_harmonic": 0.9999999999999998,<br>      "Sarkar_uniform_quadratic": 1.0,<br>      "linear_prior_cubic": 0.9999999999999998,<br>      "Dirac_k3": 1.0<br>    },<br>    "worst_case_fdr_at_alpha_0_10": {<br>      "linear_simes": 0.24500000000000027,<br>      "BY_harmonic": 0.10000000000000013,<br>      "Sarkar_uniform_quadratic": 0.09999999999999998,<br>      "linear_prior_cubic": 0.09999999999999999,<br>      "Dirac_k3": 0.10000000000000002<br>    },<br>    "concentrated_signal_tier1_rejections": {<br>      "BY_harmonic": 0,<br>      "Sarkar_uniform_quadratic": 5,<br>      "linear_prior_cubic": 5<br>    },<br>    "concentrated_signal_tier2_rejections": {<br>      "BY_harmonic": 0,<br>      "Sarkar_uniform_quadratic": 0,<br>      "linear_prior_cubic": 5<br>    }<br>  },<br>  "step_down_log_convexity": {<br>    "checked_m_m0_pairs": 300,<br>    "max_log_convex_endpoint_ratio": 1.0000000000000002,<br>    "bl_step_down_i1_to_i5_m10": [<br>      0.005,<br>      0.006172839506172839,<br>      0.0078125,<br>      0.01020408163265306,<br>      0.013888888888888888<br>    ],<br>    "holm_step_down_i1_to_i5_m10": [<br>      0.005,<br>      0.005555555555555556,<br>      0.00625,<br>      0.0071428571428571435,<br>      0.008333333333333333<br>    ]<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### SelfConsistencyAndDependencyControlFDRFramework versus OptimalMultiWeightedStepUpProcedureForFDRControl and OptimalSpjotvollAndSieveGroupedPValueWeighting

identity: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Retain Self-consistency and dependency control framework for false discovery rate control as a distinct DRAFT mathematical_method.

SelfConsistencyAndDependencyControlFDRFramework establishes the general coupled Self-Consistency SC(alpha, pi, beta) and Dependency Control DC(beta) sufficiency framework on volume-measured hypothesis spaces (Definitions 2.2-2.6, Proposition 2.7), the order-free maximal self-consistent step-up characterization R_SU = L_Delta(r_hat) (Definition 3.1), the prior-integrated shape function family beta_nu(r) = int_0^r x d_nu(x) under arbitrary dependence (Lemma 3.2(iii), Proposition 3.7, Theorem 4.2), and the log-convexity step-down FDR bound (Theorem 4.6), whereas Roquain &amp; van de Wiel (2009) and Roeder &amp; Wasserman (2009) optimize prior weights under parametric alternative models.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Related mapping to DataDredgingBias is supported.

The Self-Consistency and Dependency Control framework bounds the doubly weighted False Discovery Rate across arbitrary hypothesis spaces and dependency structures, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).

### two-line-sc-dc-factorization-for-doubly-weighted-fdr

evidence: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Supported by Section 2.2-2.3 Definitions 2.2-2.6 and Proposition 2.7.

Verified Proposition 2.7 coupled SC+DC doubly weighted FDR bound on a hypothesis space with total volume Lambda(H) = 6.0 and prior density integral Pi(H) = 1.0.

### order-free-maximal-self-consistent-step-up-characterization

evidence: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Supported by Section 3.1 Definition 3.1, Section 4.1.4, and Section 4.2 Theorem 4.5.

Verified order-free maximal self-consistent step-up fixed-point identity &#124;L_Delta(r_hat)&#124; = r_hat (4 checks) and exhaustive 2^m subset maximality (4 checks), plus geometrically constrained contiguous subset [2, 3] subset R_SU = [0, 2, 3].

### prior-integrated-shape-function-family-under-arbitrary-dependence

evidence: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Supported by Section 3.2 Lemma 3.2, Propositions 3.3, 3.6, 3.7, and Section 4.1 Theorems 4.1-4.2.

Verified worst-case adversarial dependency control at m = 6, alpha = 0.1: linear Simes beta(r) = r has adversarial supremum ratio 2.4500000000000006 = gamma_6 and worst-case FDR = 0.24500000000000027 &gt; 0.1, whereas Benjamini-Yekutieli harmonic, Sarkar uniform quadratic, linear-prior cubic, and Dirac delta_3 priors all satisfy adversarial supremum ratio = 1.0 and worst-case FDR = 0.1.

### two-stage-adaptive-fdr-bound-and-step-down-log-convexity

evidence: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

Supported by Section 4.1.5 Lemma 4.3, Corollary 4.4, Section 4.2 Theorem 4.6, and Appendix A.2.

Verified Theorem 4.6 log-convexity endpoint bound across 300 (m, m_0) pairs (max endpoint ratio = 1.0000000000000002).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SelfConsistencyAndDependencyControlFDRFramework.

The full record is consistent; retain DRAFT.

Read every field of SelfConsistencyAndDependencyControlFDRFramework.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T153000Z-self-consistency-and-dependency-control-fdr-framework.json | supports | No normalized identity match for Self-consistency and dependency control framework for false discovery rate control across 442 pinned AIO records and 593 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides frequentist multiplicity error-control context via related_match. |
| calculation | research/discovery/self-consistency-and-dependency-control-fdr-framework-boundaries.py | supports | Constructed analytical and numerical checks for Proposition 2.7 coupled SC+DC doubly weighted FDR bound, Definition 3.1 order-free maximal self-consistent step-up fixed-point identity and subset maximality, Lemma 3.2(iii) and Proposition 3.7 prior-integrated shape functions beta_nu(r) = int_0^r x d_nu(x) under worst-case adversarial dependence, and Theorem 4.6 step-down log-convexity bound. |
| blanchard-roquain2008-ar5iv | https://ar5iv.labs.arxiv.org/html/0802.1406; Sections 1-5 and Appendix A (lines 1-839, Definitions 2.1-2.6, Proposition 2.7, Definition 3.1, Lemma 3.2, Propositions 3.3, 3.6, 3.7, Theorems 4.1-4.2, Lemma 4.3, Corollary 4.4, Theorems 4.5-4.6) | supports | All 839 lines of the full-text ar5iv HTML conversion of arXiv:0802.1406v2 read. Checked all definitions, lemmas, propositions, theorems, and Appendix A proofs. |
| blanchard-roquain2008-crossref | https://api.crossref.org/works/10.1214/08-EJS180; Electronic Journal of Statistics Vol. 2, pp. 963-992 (2008) publication record | supports | Official Electronic Journal of Statistics 2:963-992 Crossref record read and verified. |
| blanchard-roquain2008-abs | https://arxiv.org/abs/0802.1406; arXiv:0802.1406v2 abstract and Electronic Journal of Statistics 2008 metadata | supports | arXiv:0802.1406v2 abstract and Electronic Journal of Statistics 2008 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Self-consistency and dependency control framework for false discovery rate control record, yielding 594 native and 442 unchanged generated records.
- All 839 lines of Blanchard &amp; Roquain (2008, arXiv:0802.1406v2) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T153200Z-self-consistency-and-dependency-control-fdr-framework
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Self-consistency and dependency control framework
  for false discovery rate control
started_at: '2026-10-17T15:30:00Z'
finished_at: '2026-10-17T15:32:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from OptimalMultiWeightedStepUpProcedureForFDRControl
    (Roquain & van de Wiel 2009), AdaptiveDataDrivenOptimalPValueWeighting (Durand
    2019), and OptimalSpjotvollAndSieveGroupedPValueWeighting (Roeder & Wasserman
    2009), the PRDS and monotonicity requirements for linear Simes shape beta(r) =
    r, the prior-selection trade-off in beta_nu(r) = int_0^r x d_nu(x) under arbitrary
    dependence, and the coordinatewise monotonicity requirement on adaptive plug-in
    factors G(p) in Lemma 4.3. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Self-consistency and dependency control framework for false discovery
  rate control as a distinct DRAFT mathematical_method with a related DataDredgingBias
  mapping. All four claims and locators across Blanchard & Roquain (2008 Electronic
  Journal of Statistics 2:963-992) are supported with explicit PRDS/monotonicity,
  prior-selectionnu trade-off, and adaptive plug-in monotonicity limitations.
source:
  git_revision: 4e4cdc5113ee3d9d9cd81dc94dfec4ad6bf91020
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/AdaptiveDataDrivenOptimalPValueWeighting.yaml
    sha256: 87961708f5770edc0a05f6048c36f9d50507a48e453db008ec06cf37d9ecb32b
    role: context
  - path: data/curated/BayesOptimalPValueWeightingUnderGaussianPrior.yaml
    sha256: b41f7ac57487b427d7bb97fb02c2e4408d93c2427f772554459327e665e78056
    role: context
  - path: data/curated/ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies.yaml
    sha256: 97415576de3471717aa4c965626803a592de772077e8fabab033968b49bd05e5
    role: context
  - path: data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml
    sha256: 84d7094933c475533243366de9802790a89da87fb149ceffcb6ff304eacd3cf9
    role: context
  - path: data/curated/OptimalMultiWeightedStepUpProcedureForFDRControl.yaml
    sha256: 0ce681bedc7dae26198a31774cb3234dab960c9f788adebd3f28225aae14c1a8
    role: context
  - path: data/curated/OptimalSpjotvollAndSieveGroupedPValueWeighting.yaml
    sha256: 5bcc259bbbe4758e8fff9ec95e7b7c967e7431c39327bad2b771284bcf9e1841
    role: context
  - path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
    sha256: 03444e07e1d84f9bdc618210e31fc12764d6e8dc40c4311bef2fe5a40c0e7a80
    role: target
  - path: research/discovery/20261017T153000Z-self-consistency-and-dependency-control-fdr-framework.json
    sha256: 3065707bcaff7c9c0e7329f99dfe273bb501324b4b6741419d30d46c55843ef4
    role: context
  - path: research/discovery/self-consistency-and-dependency-control-fdr-framework-boundaries.py
    sha256: f15ec6f49ba57c20957030ee69fe11bf53cb9ae1849cf6c6b9961e348e1f547a
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
- target_id: AIMech:SelfConsistencyAndDependencyControlFDRFramework
  path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
  label: Self-consistency and dependency control framework for false discovery rate
    control
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
    role: maintained
scope:
  description: All fields of the exact maintained SelfConsistencyAndDependencyControlFDRFramework
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SelfConsistencyAndDependencyControlFDRFramework'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
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
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: All 594 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Blanchard-Roquain SC and DC framework checks
  command: python3 research/discovery/self-consistency-and-dependency-control-fdr-framework-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:SelfConsistencyAndDependencyControlFDRFramework\"\
    ,\n  \"primary_source\": \"Blanchard & Roquain (2008), Electronic Journal of Statistics\
    \ 2:963-992 (arXiv:0802.1406v2, DOI:10.1214/08-EJS180)\",\n  \"order_free_self_consistency\"\
    : {\n    \"total_volume_lambda_H\": 6.0,\n    \"pi_lambda_integral\": 1.0,\n \
    \   \"fixed_point_checks\": 4,\n    \"maximality_checks\": 4,\n    \"disconnected_r_su\"\
    : [\n      0,\n      2,\n      3\n    ],\n    \"contiguous_self_consistent_subset\"\
    : [\n      2,\n      3\n    ]\n  },\n  \"arbitrary_dependence_beta_nu_family\"\
    : {\n    \"m\": 6,\n    \"alpha\": 0.1,\n    \"gamma_m\": 2.45,\n    \"adversarial_sup_expectations_over_c\"\
    : {\n      \"linear_simes\": 2.4500000000000006,\n      \"BY_harmonic\": 0.9999999999999998,\n\
    \      \"Sarkar_uniform_quadratic\": 1.0,\n      \"linear_prior_cubic\": 0.9999999999999998,\n\
    \      \"Dirac_k3\": 1.0\n    },\n    \"worst_case_fdr_at_alpha_0_10\": {\n  \
    \    \"linear_simes\": 0.24500000000000027,\n      \"BY_harmonic\": 0.10000000000000013,\n\
    \      \"Sarkar_uniform_quadratic\": 0.09999999999999998,\n      \"linear_prior_cubic\"\
    : 0.09999999999999999,\n      \"Dirac_k3\": 0.10000000000000002\n    },\n    \"\
    concentrated_signal_tier1_rejections\": {\n      \"BY_harmonic\": 0,\n      \"\
    Sarkar_uniform_quadratic\": 5,\n      \"linear_prior_cubic\": 5\n    },\n    \"\
    concentrated_signal_tier2_rejections\": {\n      \"BY_harmonic\": 0,\n      \"\
    Sarkar_uniform_quadratic\": 0,\n      \"linear_prior_cubic\": 5\n    }\n  },\n\
    \  \"step_down_log_convexity\": {\n    \"checked_m_m0_pairs\": 300,\n    \"max_log_convex_endpoint_ratio\"\
    : 1.0000000000000002,\n    \"bl_step_down_i1_to_i5_m10\": [\n      0.005,\n  \
    \    0.006172839506172839,\n      0.0078125,\n      0.01020408163265306,\n   \
    \   0.013888888888888888\n    ],\n    \"holm_step_down_i1_to_i5_m10\": [\n   \
    \   0.005,\n      0.005555555555555556,\n      0.00625,\n      0.0071428571428571435,\n\
    \      0.008333333333333333\n    ]\n  },\n  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T153000Z-self-consistency-and-dependency-control-fdr-framework.json
  accessed_at: '2026-10-17T15:30:00Z'
  support: supports
  summary: No normalized identity match for Self-consistency and dependency control
    framework for false discovery rate control across 442 pinned AIO records and 593
    maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T15:30:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides frequentist multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/self-consistency-and-dependency-control-fdr-framework-boundaries.py
  accessed_at: '2026-10-17T15:30:00Z'
  snapshot_sha256: f15ec6f49ba57c20957030ee69fe11bf53cb9ae1849cf6c6b9961e348e1f547a
  support: supports
  summary: Constructed analytical and numerical checks for Proposition 2.7 coupled
    SC+DC doubly weighted FDR bound, Definition 3.1 order-free maximal self-consistent
    step-up fixed-point identity and subset maximality, Lemma 3.2(iii) and Proposition
    3.7 prior-integrated shape functions beta_nu(r) = int_0^r x d_nu(x) under worst-case
    adversarial dependence, and Theorem 4.6 step-down log-convexity bound.
- evidence_id: blanchard-roquain2008-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/0802.1406
  locator: Sections 1-5 and Appendix A (lines 1-839, Definitions 2.1-2.6, Proposition
    2.7, Definition 3.1, Lemma 3.2, Propositions 3.3, 3.6, 3.7, Theorems 4.1-4.2,
    Lemma 4.3, Corollary 4.4, Theorems 4.5-4.6)
  accessed_at: '2026-10-17T15:30:00Z'
  snapshot_sha256: 475022ac6bda3b24dd97d657ea03968fe49a4ae6fe32c367771f4d8d1a414d7f
  support: supports
  summary: All 839 lines of the full-text ar5iv HTML conversion of arXiv:0802.1406v2
    read. Checked all definitions, lemmas, propositions, theorems, and Appendix A
    proofs.
- evidence_id: blanchard-roquain2008-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/08-EJS180
  locator: Electronic Journal of Statistics Vol. 2, pp. 963-992 (2008) publication
    record
  accessed_at: '2026-10-17T15:30:00Z'
  snapshot_sha256: 02a775523a7b4c76ed516c0c92483a8e30d93e48f907fff4be9e02dbcd4f27c2
  support: supports
  summary: Official Electronic Journal of Statistics 2:963-992 Crossref record read
    and verified.
- evidence_id: blanchard-roquain2008-abs
  kind: primary_source
  reference: https://arxiv.org/abs/0802.1406
  locator: arXiv:0802.1406v2 abstract and Electronic Journal of Statistics 2008 metadata
  accessed_at: '2026-10-17T15:30:00Z'
  snapshot_sha256: 56c8e17d84115e0ad99c76372d88b7469fa71988c75bf9a4d57a9b07bcfda651
  support: supports
  summary: arXiv:0802.1406v2 abstract and Electronic Journal of Statistics 2008 metadata
    read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: SelfConsistencyAndDependencyControlFDRFramework versus OptimalMultiWeightedStepUpProcedureForFDRControl
    and OptimalSpjotvollAndSieveGroupedPValueWeighting
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - identity
  - blanchard-roquain2008-ar5iv
  - blanchard-roquain2008-crossref
  summary: Retain Self-consistency and dependency control framework for false discovery
    rate control as a distinct DRAFT mathematical_method.
  details: SelfConsistencyAndDependencyControlFDRFramework establishes the general
    coupled Self-Consistency SC(alpha, pi, beta) and Dependency Control DC(beta) sufficiency
    framework on volume-measured hypothesis spaces (Definitions 2.2-2.6, Proposition
    2.7), the order-free maximal self-consistent step-up characterization R_SU = L_Delta(r_hat)
    (Definition 3.1), the prior-integrated shape function family beta_nu(r) = int_0^r
    x d_nu(x) under arbitrary dependence (Lemma 3.2(iii), Proposition 3.7, Theorem
    4.2), and the log-convexity step-down FDR bound (Theorem 4.6), whereas Roquain
    & van de Wiel (2009) and Roeder & Wasserman (2009) optimize prior weights under
    parametric alternative models.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - mapping
  - blanchard-roquain2008-ar5iv
  summary: Related mapping to DataDredgingBias is supported.
  details: The Self-Consistency and Dependency Control framework bounds the doubly
    weighted False Discovery Rate across arbitrary hypothesis spaces and dependency
    structures, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).
- assessment_id: two-line-sc-dc-factorization-for-doubly-weighted-fdr
  area: evidence
  topic: two-line-sc-dc-factorization-for-doubly-weighted-fdr
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - blanchard-roquain2008-ar5iv
  - blanchard-roquain2008-abs
  - calculation
  summary: Supported by Section 2.2-2.3 Definitions 2.2-2.6 and Proposition 2.7.
  details: Verified Proposition 2.7 coupled SC+DC doubly weighted FDR bound on a hypothesis
    space with total volume Lambda(H) = 6.0 and prior density integral Pi(H) = 1.0.
- assessment_id: order-free-maximal-self-consistent-step-up-characterization
  area: evidence
  topic: order-free-maximal-self-consistent-step-up-characterization
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - blanchard-roquain2008-ar5iv
  - calculation
  summary: Supported by Section 3.1 Definition 3.1, Section 4.1.4, and Section 4.2
    Theorem 4.5.
  details: Verified order-free maximal self-consistent step-up fixed-point identity
    |L_Delta(r_hat)| = r_hat (4 checks) and exhaustive 2^m subset maximality (4 checks),
    plus geometrically constrained contiguous subset [2, 3] subset R_SU = [0, 2, 3].
- assessment_id: prior-integrated-shape-function-family-under-arbitrary-dependence
  area: evidence
  topic: prior-integrated-shape-function-family-under-arbitrary-dependence
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - blanchard-roquain2008-ar5iv
  - calculation
  summary: Supported by Section 3.2 Lemma 3.2, Propositions 3.3, 3.6, 3.7, and Section
    4.1 Theorems 4.1-4.2.
  details: 'Verified worst-case adversarial dependency control at m = 6, alpha = 0.1:
    linear Simes beta(r) = r has adversarial supremum ratio 2.4500000000000006 = gamma_6
    and worst-case FDR = 0.24500000000000027 > 0.1, whereas Benjamini-Yekutieli harmonic,
    Sarkar uniform quadratic, linear-prior cubic, and Dirac delta_3 priors all satisfy
    adversarial supremum ratio = 1.0 and worst-case FDR = 0.1.'
- assessment_id: two-stage-adaptive-fdr-bound-and-step-down-log-convexity
  area: evidence
  topic: two-stage-adaptive-fdr-bound-and-step-down-log-convexity
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - blanchard-roquain2008-ar5iv
  - calculation
  summary: Supported by Section 4.1.5 Lemma 4.3, Corollary 4.4, Section 4.2 Theorem
    4.6, and Appendix A.2.
  details: Verified Theorem 4.6 log-convexity endpoint bound across 300 (m, m_0) pairs
    (max endpoint ratio = 1.0000000000000002).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SelfConsistencyAndDependencyControlFDRFramework
  evidence_ids:
  - identity
  - mapping
  - blanchard-roquain2008-ar5iv
  - blanchard-roquain2008-crossref
  - blanchard-roquain2008-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of SelfConsistencyAndDependencyControlFDRFramework.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Self-consistency and dependency control framework for false discovery
  rate control record, yielding 594 native and 442 unchanged generated records.
- All 839 lines of Blanchard & Roquain (2008, arXiv:0802.1406v2) were read in full
  text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- self-consistency
- arbitrary-dependence
- self-review
- discovery-ongoing
```
