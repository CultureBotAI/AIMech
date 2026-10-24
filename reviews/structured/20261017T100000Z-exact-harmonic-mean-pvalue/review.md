# Scientific author self-review of exact harmonic mean p-value combination test

- Review: 20261017T100000Z-exact-harmonic-mean-pvalue
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T09:58:00Z
- Finished UTC: 2026-10-17T10:00:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the exact harmonic mean p-value combination test as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators are supported with explicit exponential-integral overflow, Landau location-shift growth, and empty-confidence-set inconsistency boundaries. No actionable defect was found; author contour-integration code remains unverified.

## Scope And Provenance

All fields of the exact maintained ExactHarmonicMeanPValueTest record and its primary evidence.

Selection: Exact maintained ID: AIMech:ExactHarmonicMeanPValueTest
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 053b3bdf47013b747ecc8a195d9928e3db58b8e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ExactHarmonicMeanPValueTest | data/curated/ExactHarmonicMeanPValueTest.yaml | maintained | Exact harmonic mean p-value combination test |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:ExactHarmonicMeanPValueTest | Checked 442 record(s); 0 failed.<br>Checked 567 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 220 history record(s); 0 error(s).<br> |
| just vendored-check | passed | True | AIMech:ExactHarmonicMeanPValueTest | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:ExactHarmonicMeanPValueTest | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ExactHarmonicMeanPValueTest | Exited 0 without output. |
| Constructed exact harmonic mean p-value boundaries | passed | True | AIMech:ExactHarmonicMeanPValueTest | {"exact_m2_pareto_convolution": {"cdf_x5_equal_weights": 0.75605551, "cdf_x5_unequal_weights_02_08": 0.7690478, "q95_equal_weights": 21.725333, "q95_unequal_weights_01_09": 20.731245}, "example1_convex_confidence_interval": {"ehmp_connected_95_interval": [-0.1012, 0.1012], "ehmp_min_at_zero": 4.732618}, "landau_domain_of_attraction_shift": {"landau_shift_equal_weights": 5.027955, "landau_shift_harmonic_weights": 4.103562, "m": 100}, "large_p_insensitivity": {"T_EHMP": 100.500501, "p1": 0.005, "p2": 0.999, "p_value_EHMP": 0.01021248}} |

## Scientific And Domain Assessments

### Exact Harmonic Mean P-Value (EHMP) versus Half-Cauchy combination and asymptotic equal-weight HMP

identity: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Retain the exact harmonic mean p-value combination test as a distinct DRAFT mathematical_method.

Liu, Meng, &amp; Pillai (2025, Appendix A and E) derive the exact finite-m unequal-weight null distribution of T_HMP(p) = sum w_j / p_j via Laplace contour integration and prove strict convexity of its inverted confidence sets, distinguishing it from HCCT and from asymptotic equal-weight HMP.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Related mapping to DataDredgingBias is supported.

EHMP controls global Type I error across multiple dependent hypothesis tests, mitigating false-positive inflation from multiple testing (AIO:DataDredgingBias).

### pareto-reciprocal-statistic-and-laplace-contour-null

evidence: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Supported by Theorem A.1 and verified for m=2 equal and unequal weights.

Laplace-transform contour integration expresses the finite-m Pareto(1, 1) weighted-sum density via Ei_2(z) and Ramanujan's scaled series.

### unequal-weight-landau-domain-of-attraction-limit

evidence: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Supported by Theorem A.2 and Appendix E proof.

As m -&gt; infinity with max_j w_j -&gt; 0, (pi/2)(T_HMP - A_m) -&gt; Landau(0, 1) with A_m = 1 - gamma - sum w_j log w_j.

### convex-confidence-regions-via-pareto-convexity-dominance

evidence: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Supported by Theorem A.3 and verified on Example 1.

Because T_F(u) &gt;= T_{G_1}(u) for F ~ Pareto(1, 1), each 1 / p_j(theta) is strictly convex, yielding connected convex confidence regions.

### large-p-insensitivity-and-tail-resilience-under-dependence

evidence: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

Supported and verified numerically at p_1 = 0.005, p_2 = 0.999.

Each term 1 / p_j &gt;= 1 approaches 1 as p_j -&gt; 1, preventing large p-values from canceling small p-values.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ExactHarmonicMeanPValueTest.

The full record is consistent; retain DRAFT.

Read every field of ExactHarmonicMeanPValueTest.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, full-text primary source with exact SHA-256 digest, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T095800Z-exact-harmonic-mean-pvalue.json | supports | No normalized identity match for the exact harmonic mean p-value combination test across 442 pinned AIO records and 566 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources, research, history, and reviews returned 7 lines (referencing only prior frontier tracking entries). Distinct from AIMech:HalfCauchyCombinationTest and asymptotic equal-weight HMP. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match. |
| calculation | research/discovery/exact-harmonic-mean-pvalue-boundaries.py | supports | Constructed exact analytical and quadrature checks for (1) m=2 equal and unequal-weight Pareto(1, 1) convolution density and CDF vs. Simpson quadrature, (2) insensitivity of EHMP to p_2 = 0.999 when p_1 = 0.005 (p_EHMP = 0.01021248), (3) Example 1 strict convexity and connected 95% confidence interval [-0.1012, 0.1012], and (4) Theorem A.2 Landau location shifts A_m = 1 - gamma - sum w_j log w_j. |
| liu-meng-pillai2025 | https://arxiv.org/html/2501.01065v1; Section 2.1, Section 2.3, Section 3.1, Appendix A (Theorems A.1-A.3, lines 1645-1680), Appendix E (lines 2148-2165) | supports | All 2,200 lines of the full-text HTML conversion of arXiv:2501.01065v1 read. Checked Theorems A.1-A.3 and their proofs in Appendix E. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT exact harmonic mean p-value combination test record, yielding 567 native and 442 unchanged generated records.
- All 2,200 lines of Liu, Meng, &amp; Pillai (2025, arXiv:2501.01065v1) were read. No author contour-integration code or GWAS pipeline was run; constructed numerical checks verify exact m=2 unequal-weight Pareto(1, 1) convolution, large-p insensitivity, Example 1 confidence-set convexity, and Theorem A.2 Landau location shifts only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T100000Z-exact-harmonic-mean-pvalue
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of exact harmonic mean p-value combination test
started_at: '2026-10-17T09:58:00Z'
finished_at: '2026-10-17T10:00:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from the Half-Cauchy
    combination test (HCCT) and asymptotic equal-weight HMP (Wilson 2019), exponential-integral
    overflow in Theorem A.1 and Ramanujan's scaled series, unequal-weight Landau location
    shifts in Theorem A.2, and convexity dominance in Theorem A.3. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the exact harmonic mean p-value combination test as a distinct DRAFT
  mathematical_method with related DataDredgingBias mapping. All four claims and locators
  are supported with explicit exponential-integral overflow, Landau location-shift
  growth, and empty-confidence-set inconsistency boundaries. No actionable defect
  was found; author contour-integration code remains unverified.
source:
  git_revision: 053b3bdf47013b747ecc8a195d9928e3db58b8e3
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
  - path: data/curated/ExactHarmonicMeanPValueTest.yaml
    sha256: e37fe73ff6637f2951762fe4cceca81cd277e7f3d8dafaad63ca150e314a9793
    role: target
  - path: data/curated/HalfCauchyCombinationTest.yaml
    sha256: 16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e
    role: context
  - path: data/curated/LogarithmicOpinionPool.yaml
    sha256: bdff4b82fa80ae38dd1a1295afdf9f5c0d877632818ea25841ca7a4adce2f430
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/PriorToPosteriorDivergenceConflictDiagnostic.yaml
    sha256: d1df8267a5bde0e2caf13c64e51c1f826b3374cfa784565af3c1755c779933a1
    role: context
  - path: research/discovery/20261017T095800Z-exact-harmonic-mean-pvalue.json
    sha256: c2a9c55880670bda7cfc3a55bfbe4d0668d2e4d57882448b243450513f2846cd
    role: context
  - path: research/discovery/exact-harmonic-mean-pvalue-boundaries.py
    sha256: 9a622dc1dc2eb9d6c36fdc7c9076c2bb253092422bf0ff4489f9e1fbf192782a
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
- target_id: AIMech:ExactHarmonicMeanPValueTest
  path: data/curated/ExactHarmonicMeanPValueTest.yaml
  label: Exact harmonic mean p-value combination test
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExactHarmonicMeanPValueTest.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ExactHarmonicMeanPValueTest record
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ExactHarmonicMeanPValueTest'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical GWAS/meta-analysis fits
    reason: No author contour-integration code or genomic study data run.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    Checked 567 curated concept record(s); 0 error(s).

    AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    Checked 220 history record(s); 0 error(s).

    '
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
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
  - AIMech:ExactHarmonicMeanPValueTest
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
  - AIMech:ExactHarmonicMeanPValueTest
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed exact harmonic mean p-value boundaries
  command: python3 research/discovery/exact-harmonic-mean-pvalue-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  exit_code: 0
  expected_exit_code: 0
  summary: '{"exact_m2_pareto_convolution": {"cdf_x5_equal_weights": 0.75605551, "cdf_x5_unequal_weights_02_08":
    0.7690478, "q95_equal_weights": 21.725333, "q95_unequal_weights_01_09": 20.731245},
    "example1_convex_confidence_interval": {"ehmp_connected_95_interval": [-0.1012,
    0.1012], "ehmp_min_at_zero": 4.732618}, "landau_domain_of_attraction_shift": {"landau_shift_equal_weights":
    5.027955, "landau_shift_harmonic_weights": 4.103562, "m": 100}, "large_p_insensitivity":
    {"T_EHMP": 100.500501, "p1": 0.005, "p2": 0.999, "p_value_EHMP": 0.01021248}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T095800Z-exact-harmonic-mean-pvalue.json
  accessed_at: '2026-10-17T09:58:00Z'
  support: supports
  summary: No normalized identity match for the exact harmonic mean p-value combination
    test across 442 pinned AIO records and 566 maintained IDs, names, aliases and
    scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data,
    sources, research, history, and reviews returned 7 lines (referencing only prior
    frontier tracking entries). Distinct from AIMech:HalfCauchyCombinationTest and
    asymptotic equal-weight HMP.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T09:58:00Z'
  support: supports
  summary: Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot
    (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/exact-harmonic-mean-pvalue-boundaries.py
  accessed_at: '2026-10-17T09:58:00Z'
  snapshot_sha256: 9a622dc1dc2eb9d6c36fdc7c9076c2bb253092422bf0ff4489f9e1fbf192782a
  support: supports
  summary: Constructed exact analytical and quadrature checks for (1) m=2 equal and
    unequal-weight Pareto(1, 1) convolution density and CDF vs. Simpson quadrature,
    (2) insensitivity of EHMP to p_2 = 0.999 when p_1 = 0.005 (p_EHMP = 0.01021248),
    (3) Example 1 strict convexity and connected 95% confidence interval [-0.1012,
    0.1012], and (4) Theorem A.2 Landau location shifts A_m = 1 - gamma - sum w_j
    log w_j.
- evidence_id: liu-meng-pillai2025
  kind: primary_source
  reference: https://arxiv.org/html/2501.01065v1
  locator: Section 2.1, Section 2.3, Section 3.1, Appendix A (Theorems A.1-A.3, lines
    1645-1680), Appendix E (lines 2148-2165)
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 2fe912b58a74ff5008a52f8f319cef872ffe8f0510fbadb94f14d7cbe265f6e3
  support: supports
  summary: All 2,200 lines of the full-text HTML conversion of arXiv:2501.01065v1
    read. Checked Theorems A.1-A.3 and their proofs in Appendix E.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Harmonic Mean P-Value (EHMP) versus Half-Cauchy combination and asymptotic
    equal-weight HMP
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - identity
  - liu-meng-pillai2025
  summary: Retain the exact harmonic mean p-value combination test as a distinct DRAFT
    mathematical_method.
  details: Liu, Meng, & Pillai (2025, Appendix A and E) derive the exact finite-m
    unequal-weight null distribution of T_HMP(p) = sum w_j / p_j via Laplace contour
    integration and prove strict convexity of its inverted confidence sets, distinguishing
    it from HCCT and from asymptotic equal-weight HMP.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - mapping
  - liu-meng-pillai2025
  summary: Related mapping to DataDredgingBias is supported.
  details: EHMP controls global Type I error across multiple dependent hypothesis
    tests, mitigating false-positive inflation from multiple testing (AIO:DataDredgingBias).
- assessment_id: pareto-reciprocal-statistic-and-laplace-contour-null
  area: evidence
  topic: pareto-reciprocal-statistic-and-laplace-contour-null
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported by Theorem A.1 and verified for m=2 equal and unequal weights.
  details: Laplace-transform contour integration expresses the finite-m Pareto(1,
    1) weighted-sum density via Ei_2(z) and Ramanujan's scaled series.
- assessment_id: unequal-weight-landau-domain-of-attraction-limit
  area: evidence
  topic: unequal-weight-landau-domain-of-attraction-limit
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported by Theorem A.2 and Appendix E proof.
  details: As m -> infinity with max_j w_j -> 0, (pi/2)(T_HMP - A_m) -> Landau(0,
    1) with A_m = 1 - gamma - sum w_j log w_j.
- assessment_id: convex-confidence-regions-via-pareto-convexity-dominance
  area: evidence
  topic: convex-confidence-regions-via-pareto-convexity-dominance
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported by Theorem A.3 and verified on Example 1.
  details: Because T_F(u) >= T_{G_1}(u) for F ~ Pareto(1, 1), each 1 / p_j(theta)
    is strictly convex, yielding connected convex confidence regions.
- assessment_id: large-p-insensitivity-and-tail-resilience-under-dependence
  area: evidence
  topic: large-p-insensitivity-and-tail-resilience-under-dependence
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - liu-meng-pillai2025
  - calculation
  summary: Supported and verified numerically at p_1 = 0.005, p_2 = 0.999.
  details: Each term 1 / p_j >= 1 approaches 1 as p_j -> 1, preventing large p-values
    from canceling small p-values.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ExactHarmonicMeanPValueTest
  evidence_ids:
  - identity
  - mapping
  - liu-meng-pillai2025
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ExactHarmonicMeanPValueTest.yaml: stable ID, name,
    aliases, mathematical_method kind, definition, definition_evidence, identity_notes,
    four claims and locators, full-text primary source with exact SHA-256 digest,
    pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT exact harmonic mean p-value combination test record, yielding 567
  native and 442 unchanged generated records.
- All 2,200 lines of Liu, Meng, & Pillai (2025, arXiv:2501.01065v1) were read. No
  author contour-integration code or GWAS pipeline was run; constructed numerical
  checks verify exact m=2 unequal-weight Pareto(1, 1) convolution, large-p insensitivity,
  Example 1 confidence-set convexity, and Theorem A.2 Landau location shifts only.
related_reviews: []
links: []
tags:
- native-concepts
- hypothesis-testing
- multiple-testing
- self-review
- discovery-ongoing
```
