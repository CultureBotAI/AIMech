# Scientific author self-review of Half-Cauchy combination test

- Review: 20261017T093700Z-half-cauchy-combination-test
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T09:35:00Z
- Finished UTC: 2026-10-17T09:37:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the Half-Cauchy combination test as a distinct DRAFT mathematical_method with related DataDredgingBias and BayesianNetwork mappings. All four claims and locators are supported with explicit Landau location-shift growth, finite-threshold dependence, and empty-confidence-set inconsistency boundaries. No actionable defect was found; author R code and GWAS pipelines remain unverified.

## Scope And Provenance

All fields of the exact maintained Half-Cauchy combination test record and its primary evidence.

Selection: Exact maintained ID: AIMech:HalfCauchyCombinationTest
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8a5775fb3485519987a940766a642b65dda033ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HalfCauchyCombinationTest | data/curated/HalfCauchyCombinationTest.yaml | maintained | Half-Cauchy combination test |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:HalfCauchyCombinationTest | Checked 442 record(s); 0 failed.<br>Checked 566 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 219 history record(s); 0 error(s).<br> |
| just vendored-check | passed | True | AIMech:HalfCauchyCombinationTest | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:HalfCauchyCombinationTest | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HalfCauchyCombinationTest | Exited 0 without output. |
| Constructed Half-Cauchy combination test boundaries | passed | True | AIMech:HalfCauchyCombinationTest | {"example1_confidence_sets": {"cct_disconnected_positive_roots": [0.1038, 0.1212, 0.1277], "cct_q95": 6.313752, "eq37_inconsistency_lower_bound": 0.795775, "hcct_connected_95_interval": [-0.1015, 0.1015], "hcct_min_at_zero": 2.901421, "hcct_q95": 13.687511}, "landau_domain_of_attraction_shift": {"landau_shift_equal_weights": 3.200895, "landau_shift_harmonic_weights": 2.612409, "m": 100}, "large_p_insensitivity": {"T_CCT": -127.326049, "T_HCCT": 63.661454, "p1": 0.005, "p2": 0.999, "p_value_CCT": 0.99750009, "p_value_HCCT": 0.01024157}} |

## Scientific And Domain Assessments

### Half-Cauchy combination test versus two-sided Cauchy combination and harmonic-mean p-value tests

identity: supported. Targets: AIMech:HalfCauchyCombinationTest.

Retain the Half-Cauchy combination test as a distinct DRAFT mathematical_method.

Liu, Meng, &amp; Pillai (2025) define T_HC(p) = sum w_j tan((1 - p_j) pi / 2) on [0, infinity), distinct from the full-support Cauchy transformation tan((0.5 - p_j) pi) of Liu &amp; Xie (2020) and from reciprocal Pareto harmonic-mean combination.

### Mappings to AIO:DataDredgingBias and AIO:BayesianNetwork

grounding: supported. Targets: AIMech:HalfCauchyCombinationTest.

Related mappings to DataDredgingBias and BayesianNetwork are supported.

HCCT controls global Type I error across multiple dependent hypothesis tests (mitigating DataDredgingBias) and combines node-specific conflict p-values in Bayesian networks.

### half-cauchy-tangent-map-and-large-p-insensitivity

evidence: supported. Targets: AIMech:HalfCauchyCombinationTest.

Supported and verified numerically at p_1 = 0.005, p_2 = 0.999.

Because tan((1 - p_j) pi / 2) &gt;= 0 and vanishes at p_j = 1, large p-values cannot cancel small p-values.

### exact-convolution-and-landau-domain-of-attraction-null

evidence: supported. Targets: AIMech:HalfCauchyCombinationTest.

Supported and verified via Theorem 2.3 m=2 density/CDF and Theorem 2.1 Landau shift.

The m=2 closed-form density/CDF matches numerical convolution to machine precision, and the location shift A_m = (2/pi)(1 - gamma - sum w_j log w_j) governs the Landau limit.

### convex-confidence-regions-and-inconsistency-lower-bound

evidence: supported. Targets: AIMech:HalfCauchyCombinationTest.

Supported and verified by reproducing Example 1 (Section 1.2) and Equation (3.7).

Each term tan((1 - p_j(theta)) pi / 2) is strictly convex in theta under normal location-scale tests, yielding connected convex confidence sets and the inter-study inconsistency bound.

### asymptotic-validity-under-dependent-test-statistics

evidence: supported. Targets: AIMech:HalfCauchyCombinationTest.

Supported by Theorems 4.1-4.5 with explicit extreme-tail and finite-m caveats.

Tail equivalence holds as t -&gt; infinity under pairwise quasi-asymptotic independence or arbitrary bivariate normal correlations.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HalfCauchyCombinationTest.

The full record is consistent; retain DRAFT.

Read every field of HalfCauchyCombinationTest.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, two full-text primary sources with exact SHA-256 digests, pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T093500Z-half-cauchy-combination-test.json | supports | No normalized identity match for the Half-Cauchy combination test across 442 pinned AIO records and 565 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources, research, history, and reviews returned 26 lines (referencing only prior frontier tracking entries). Distinct from two-sided Cauchy combination and harmonic-mean p-value combination. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias, BayesianNetwork, EvaluationBias, and EnsembleLearning in the pinned AIO snapshot (2026-07-22). DataDredgingBias and BayesianNetwork provide multiple-testing and graphical conflict-aggregation context via related_match. |
| calculation | research/discovery/half-cauchy-combination-test-boundaries.py | supports | Constructed exact analytical and quadrature checks for (1) insensitivity of HCCT to p_2 = 0.999 when p_1 = 0.005 (p_HCCT = 0.01024157 vs. p_CCT = 0.99750009), (2) Theorem 2.3 exact m=2 Half-Cauchy convolution density and CDF vs. quadrature, (3) Example 1 (Section 1.2) showing disconnected 3-interval CCT 95% confidence sets vs. connected convex HCCT 95% interval [-0.1015, 0.1015] and the Equation (3.7) inconsistency lower bound, and (4) Theorem 2.1 Landau location shifts A_m. |
| liu-meng-pillai2025 | https://arxiv.org/html/2501.01065v1; Sections 1-6, Theorems 2.1-4.5, Appendices A-F, lines 1-2200 | supports | All 2,200 lines of the full-text HTML conversion of arXiv:2501.01065v1 read. Checked Equations (1.2)-(4.9), Theorems 2.1-4.5, Example 1, and Appendices A-F. |
| yang2026 | https://arxiv.org/pdf/2511.02977v2; Section 4.1, PDF p. 25 | supports | All 52 pages of the primary PDF read, confirming the application of heavy-tailed p-value combination tests to dependent conflict p-values in Bayesian graphical models. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Half-Cauchy combination test record, yielding 566 native and 442 unchanged generated records.
- All 2,200 lines of Liu, Meng, &amp; Pillai (2025, arXiv:2501.01065v1) and all 52 pages of Yang, Nott, &amp; Presanis (2026, arXiv:2511.02977v2) were read. No author R package or empirical GWAS pipeline was run; constructed numerical checks verify large-p insensitivity, exact m=2 convolution, Example 1 confidence-set convexity, and Landau location shifts only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T093700Z-half-cauchy-combination-test
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Half-Cauchy combination test
started_at: '2026-10-17T09:35:00Z'
finished_at: '2026-10-17T09:37:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from the two-sided
    Cauchy Combination Test (CCT) and Harmonic Mean P-Value (HMP), exact m=2 Half-Cauchy
    convolution vs. Landau location-shifted stable approximation as m grows, strict
    convexity of confidence sets vs. disconnected CCT sets, and finite-threshold tail
    accuracy under dependence. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the Half-Cauchy combination test as a distinct DRAFT mathematical_method
  with related DataDredgingBias and BayesianNetwork mappings. All four claims and
  locators are supported with explicit Landau location-shift growth, finite-threshold
  dependence, and empty-confidence-set inconsistency boundaries. No actionable defect
  was found; author R code and GWAS pipelines remain unverified.
source:
  git_revision: 8a5775fb3485519987a940766a642b65dda033ea
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/curated/HalfCauchyCombinationTest.yaml
    sha256: 16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e
    role: target
  - path: data/curated/LogarithmicOpinionPool.yaml
    sha256: bdff4b82fa80ae38dd1a1295afdf9f5c0d877632818ea25841ca7a4adce2f430
    role: context
  - path: data/curated/MixtureApproximationNodeSplittingDiagnostic.yaml
    sha256: 28fef075fcf205209c1ea251fc3d23aa34529d2f34b0087f18eb6d5690750952
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/PriorExpansionScoreConflictDiagnostic.yaml
    sha256: a52b0ed1f942269c6a9fe0f48683b4d69a0706f522633b70e85bc05f48d8f792
    role: context
  - path: data/curated/PriorToPosteriorDivergenceConflictDiagnostic.yaml
    sha256: d1df8267a5bde0e2caf13c64e51c1f826b3374cfa784565af3c1755c779933a1
    role: context
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: context
  - path: data/curated/SequentialScoreDiscrepancyConflictDiagnostic.yaml
    sha256: 14d75f7ce1e21b32cf87cad76dc462d8ac60cf68d1fff58c12e6ba115c001871
    role: context
  - path: research/discovery/20261017T093500Z-half-cauchy-combination-test.json
    sha256: 07982d42a338c8a02194609f3128f3cabb976a1b7b963b2f86e1bcf0c06fa3ed
    role: context
  - path: research/discovery/half-cauchy-combination-test-boundaries.py
    sha256: 0263679759caeb837b0ee68bb7783d0b9566370eee9fa0a28052967a77e73991
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
- target_id: AIMech:HalfCauchyCombinationTest
  path: data/curated/HalfCauchyCombinationTest.yaml
  label: Half-Cauchy combination test
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HalfCauchyCombinationTest.yaml
    role: maintained
scope:
  description: All fields of the exact maintained Half-Cauchy combination test record
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HalfCauchyCombinationTest'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HalfCauchyCombinationTest
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical GWAS/meta-analysis fits
    reason: No author R implementation or genomic study data run.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    Checked 566 curated concept record(s); 0 error(s).

    AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    Checked 219 history record(s); 0 error(s).

    '
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:HalfCauchyCombinationTest
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
  - AIMech:HalfCauchyCombinationTest
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
  - AIMech:HalfCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Half-Cauchy combination test boundaries
  command: python3 research/discovery/half-cauchy-combination-test-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: '{"example1_confidence_sets": {"cct_disconnected_positive_roots": [0.1038,
    0.1212, 0.1277], "cct_q95": 6.313752, "eq37_inconsistency_lower_bound": 0.795775,
    "hcct_connected_95_interval": [-0.1015, 0.1015], "hcct_min_at_zero": 2.901421,
    "hcct_q95": 13.687511}, "landau_domain_of_attraction_shift": {"landau_shift_equal_weights":
    3.200895, "landau_shift_harmonic_weights": 2.612409, "m": 100}, "large_p_insensitivity":
    {"T_CCT": -127.326049, "T_HCCT": 63.661454, "p1": 0.005, "p2": 0.999, "p_value_CCT":
    0.99750009, "p_value_HCCT": 0.01024157}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T093500Z-half-cauchy-combination-test.json
  accessed_at: '2026-10-17T09:35:00Z'
  support: supports
  summary: No normalized identity match for the Half-Cauchy combination test across
    442 pinned AIO records and 565 maintained IDs, names, aliases and scoped synonyms.
    Ignored- and hidden-inclusive fixed-string searches across data, sources, research,
    history, and reviews returned 26 lines (referencing only prior frontier tracking
    entries). Distinct from two-sided Cauchy combination and harmonic-mean p-value
    combination.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T09:35:00Z'
  support: supports
  summary: Inspected DataDredgingBias, BayesianNetwork, EvaluationBias, and EnsembleLearning
    in the pinned AIO snapshot (2026-07-22). DataDredgingBias and BayesianNetwork
    provide multiple-testing and graphical conflict-aggregation context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/half-cauchy-combination-test-boundaries.py
  accessed_at: '2026-10-17T09:35:00Z'
  snapshot_sha256: 0263679759caeb837b0ee68bb7783d0b9566370eee9fa0a28052967a77e73991
  support: supports
  summary: Constructed exact analytical and quadrature checks for (1) insensitivity
    of HCCT to p_2 = 0.999 when p_1 = 0.005 (p_HCCT = 0.01024157 vs. p_CCT = 0.99750009),
    (2) Theorem 2.3 exact m=2 Half-Cauchy convolution density and CDF vs. quadrature,
    (3) Example 1 (Section 1.2) showing disconnected 3-interval CCT 95% confidence
    sets vs. connected convex HCCT 95% interval [-0.1015, 0.1015] and the Equation
    (3.7) inconsistency lower bound, and (4) Theorem 2.1 Landau location shifts A_m.
- evidence_id: liu-meng-pillai2025
  kind: primary_source
  reference: https://arxiv.org/html/2501.01065v1
  locator: Sections 1-6, Theorems 2.1-4.5, Appendices A-F, lines 1-2200
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 2fe912b58a74ff5008a52f8f319cef872ffe8f0510fbadb94f14d7cbe265f6e3
  support: supports
  summary: All 2,200 lines of the full-text HTML conversion of arXiv:2501.01065v1
    read. Checked Equations (1.2)-(4.9), Theorems 2.1-4.5, Example 1, and Appendices
    A-F.
- evidence_id: yang2026
  kind: primary_source
  reference: https://arxiv.org/pdf/2511.02977v2
  locator: Section 4.1, PDF p. 25
  accessed_at: '2026-10-17T08:20:00Z'
  snapshot_sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d
  support: supports
  summary: All 52 pages of the primary PDF read, confirming the application of heavy-tailed
    p-value combination tests to dependent conflict p-values in Bayesian graphical
    models.
assessments:
- assessment_id: identity
  area: identity
  topic: Half-Cauchy combination test versus two-sided Cauchy combination and harmonic-mean
    p-value tests
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - identity
  - liu-meng-pillai2025
  summary: Retain the Half-Cauchy combination test as a distinct DRAFT mathematical_method.
  details: Liu, Meng, & Pillai (2025) define T_HC(p) = sum w_j tan((1 - p_j) pi /
    2) on [0, infinity), distinct from the full-support Cauchy transformation tan((0.5
    - p_j) pi) of Liu & Xie (2020) and from reciprocal Pareto harmonic-mean combination.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:DataDredgingBias and AIO:BayesianNetwork
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - mapping
  - liu-meng-pillai2025
  - yang2026
  summary: Related mappings to DataDredgingBias and BayesianNetwork are supported.
  details: HCCT controls global Type I error across multiple dependent hypothesis
    tests (mitigating DataDredgingBias) and combines node-specific conflict p-values
    in Bayesian networks.
- assessment_id: half-cauchy-tangent-map-and-large-p-insensitivity
  area: evidence
  topic: half-cauchy-tangent-map-and-large-p-insensitivity
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported and verified numerically at p_1 = 0.005, p_2 = 0.999.
  details: Because tan((1 - p_j) pi / 2) >= 0 and vanishes at p_j = 1, large p-values
    cannot cancel small p-values.
- assessment_id: exact-convolution-and-landau-domain-of-attraction-null
  area: evidence
  topic: exact-convolution-and-landau-domain-of-attraction-null
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported and verified via Theorem 2.3 m=2 density/CDF and Theorem 2.1
    Landau shift.
  details: The m=2 closed-form density/CDF matches numerical convolution to machine
    precision, and the location shift A_m = (2/pi)(1 - gamma - sum w_j log w_j) governs
    the Landau limit.
- assessment_id: convex-confidence-regions-and-inconsistency-lower-bound
  area: evidence
  topic: convex-confidence-regions-and-inconsistency-lower-bound
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported and verified by reproducing Example 1 (Section 1.2) and Equation
    (3.7).
  details: Each term tan((1 - p_j(theta)) pi / 2) is strictly convex in theta under
    normal location-scale tests, yielding connected convex confidence sets and the
    inter-study inconsistency bound.
- assessment_id: asymptotic-validity-under-dependent-test-statistics
  area: evidence
  topic: asymptotic-validity-under-dependent-test-statistics
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - liu-meng-pillai2025
  - yang2026
  summary: Supported by Theorems 4.1-4.5 with explicit extreme-tail and finite-m caveats.
  details: Tail equivalence holds as t -> infinity under pairwise quasi-asymptotic
    independence or arbitrary bivariate normal correlations.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HalfCauchyCombinationTest
  evidence_ids:
  - identity
  - mapping
  - liu-meng-pillai2025
  - yang2026
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of HalfCauchyCombinationTest.yaml: stable ID, name, aliases,
    mathematical_method kind, definition, definition_evidence, identity_notes, four
    claims and locators, two full-text primary sources with exact SHA-256 digests,
    pinned AIO mappings and rationales, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Half-Cauchy combination test record, yielding 566 native and 442
  unchanged generated records.
- All 2,200 lines of Liu, Meng, & Pillai (2025, arXiv:2501.01065v1) and all 52 pages
  of Yang, Nott, & Presanis (2026, arXiv:2511.02977v2) were read. No author R package
  or empirical GWAS pipeline was run; constructed numerical checks verify large-p
  insensitivity, exact m=2 convolution, Example 1 confidence-set convexity, and Landau
  location shifts only.
related_reviews: []
links: []
tags:
- native-concepts
- hypothesis-testing
- multiple-testing
- self-review
- discovery-ongoing
```
