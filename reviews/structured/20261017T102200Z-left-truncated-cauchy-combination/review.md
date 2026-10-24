# Scientific author self-review of left-truncated Cauchy combination test

- Review: 20261017T102200Z-left-truncated-cauchy-combination
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T10:20:00Z
- Finished UTC: 2026-10-17T10:22:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the left-truncated Cauchy combination test as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Fang et al. (2023) and Gui, Jiang, &amp; Wang (2023) are supported with explicit finite-sample stability loss, GCLT shift, and truncation-threshold tuning boundaries. No actionable defect was found; author R/GWAS pipelines remain unverified.

## Scope And Provenance

All fields of the exact maintained LeftTruncatedCauchyCombinationTest record and its primary evidence.

Selection: Exact maintained ID: AIMech:LeftTruncatedCauchyCombinationTest
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 202a48a2166e86eb8169dd35b26ed47bad4b7ebc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LeftTruncatedCauchyCombinationTest | data/curated/LeftTruncatedCauchyCombinationTest.yaml | maintained | Left-truncated Cauchy combination test |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:LeftTruncatedCauchyCombinationTest | All AIMech schema, curated, seed, and history validations passed. |
| just vendored-check | passed | True | AIMech:LeftTruncatedCauchyCombinationTest | Vendored CLAW review files match canonical checksums. |
| aimech check-source | passed | True | AIMech:LeftTruncatedCauchyCombinationTest | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:LeftTruncatedCauchyCombinationTest | Exited 0 without output. |
| Constructed left-truncated Cauchy combination boundaries | passed | True | AIMech:LeftTruncatedCauchyCombinationTest | {<br>  "concept_id": "AIMech:LeftTruncatedCauchyCombinationTest",<br>  "boundary_limits": {<br>    "max_rel_diff_p0_05_vs_half_cauchy": 6.104540043087295e-13,<br>    "max_rel_diff_p0_10_vs_standard_cauchy": 0.0,<br>    "cond_lower_bound_p0_09": -3.077683537175253,<br>    "winsorized_lower_bound_delta_001": -31.820515953773857<br>  },<br>  "cancellation_immunity_p1_1e-4_p2_1-1e-6": {<br>    "standard_cct_mean_stat": -157563.39371035108,<br>    "standard_cct_combined_p": 0.9999979797979806,<br>    "cond_left_truncated_sum_stat_p0_09": 3533.6987649768485,<br>    "cond_left_truncated_combined_p_p0_09": 0.0002001741888014842,<br>    "winsorized_left_truncated_mean_stat_delta_001": 1575.6391205815275,<br>    "winsorized_left_truncated_combined_p_delta_001": 0.00020201951023418596<br>  },<br>  "fang_prop3_prop4_verification": {<br>    "n_tests": 10,<br>    "t_thresh": 100.0,<br>    "prop4_lower_bound": 0.003182992764908188,<br>    "prop4_sharp_upper_bound": 0.003471650826855522,<br>    "prop4_binomial_upper_bound": 0.003516004233141369,<br>    "mc_empirical_tail_prob": 0.00326,<br>    "prop3_gclt_n50_delta001": {<br>      "nu_delta": -31.820515953773857,<br>      "f1n": 3.074140806502033,<br>      "f2n": 0.019411035201823756,<br>      "theta_n": 0.0001779445628941012,<br>      "n_theta_n": 0.00889722814470506<br>    }<br>  }<br>} |

## Scientific And Domain Assessments

### Left-Truncated Cauchy Combination Test versus standard Cauchy and Half-Cauchy combination tests

identity: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Retain the left-truncated Cauchy combination test as a distinct DRAFT mathematical_method.

Fang et al. (2023, Section 2.2) and Gui, Jiang, &amp; Wang (2023, Section 2.2) define negative-support left-truncated Cauchy combination tests (nu_delta &lt; 0 or c &lt; 0) that eliminate unbounded negative penalties as p_i -&gt; 1 while differing from both untruncated CauchyCombinationTest and strictly non-negative HalfCauchyCombinationTest (c = 0).

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Related mapping to DataDredgingBias is supported.

Left-truncated Cauchy combination controls global Type I error across multiple dependent hypothesis tests, mitigating false-positive inflation from multiple testing (AIO:DataDredgingBias).

### winsorized-and-conditional-left-truncated-cauchy-transformations

evidence: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Supported by Fang et al. Section 2.2 and Gui et al. Section 2.2 and verified numerically.

Winsorized truncation p_i^tr = min(p_i, 1 - delta) bounds scores at nu_delta = tan(pi*(delta - 0.5)), while conditional left truncation bounds scores at c = tan(pi*(0.5 - p_0)).

### regularly-varying-index-one-and-asymptotic-dependence-robustness

evidence: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Supported by Theorems 1-3 in Fang et al. (2023) and Section 3.1.2-3.1.3 in Gui et al. (2023).

Left-truncated Cauchy satisfies Condition (A2.2) and belongs to R_{-1} with gamma = 1, p = 1, q = 0, guaranteeing asymptotic tail equivalence under arbitrary correlation &#124;rho_{ij}&#124; &lt; 1 and Donoho-Jin sparse optimality.

### gclt-stable-approximation-and-finite-sample-tail-bounds

evidence: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Supported by Propositions 3-4 and Appendix A proof and verified via Monte Carlo and Simpson quadrature.

Verified Proposition 4 bounds (0.003183 &lt;= 0.003260 &lt;= 0.003472 &lt;= 0.003516) for n=10, delta=0.01, t=100 and Proposition 3 GCLT location shift theta_n.

### power-recovery-under-discrete-and-negatively-correlated-p-values

evidence: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

Supported by Section 4.3 and Section 5 of Fang et al. (2023) and verified on (1e-4, 1 - 1e-6).

Prevents p-values near 1 in discrete Fisher exact tests or neuroticism GWAS genes (SLC2A9, PCSK6) from cancelling true small-p signals.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:LeftTruncatedCauchyCombinationTest.

The full record is consistent; retain DRAFT.

Read every field of LeftTruncatedCauchyCombinationTest.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, two full-text primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T102000Z-left-truncated-cauchy-combination.json | supports | No normalized identity match for the left-truncated Cauchy combination test across 442 pinned AIO records and 567 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources, research, history, and reviews returned 0 lines. Distinct from AIMech:CauchyCombinationTest and AIMech:HalfCauchyCombinationTest. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match. |
| calculation | research/discovery/left-truncated-cauchy-combination-boundaries.py | supports | Constructed analytical and Monte Carlo checks for (1) p_0 = 0.5 Half-Cauchy and p_0 = 1.0 standard Cauchy boundaries, (2) elimination of negative score cancellation on (p_1 = 1e-4, p_2 = 1 - 1e-6), and (3) Fang et al. Proposition 3/4 GCLT and binomial tail bounds. |
| fang-chang-park-tseng2023 | https://ar5iv.labs.arxiv.org/html/2103.12967; Section 2.2 (Propositions 3-4), Section 3 (Theorems 1-3), Section 4.3, Section 5, Appendix A (lines 508, 528-535) | supports | All 546 lines of the full-text ar5iv HTML conversion of arXiv:2103.12967 read. Checked Propositions 3-4, Theorems 1-3, and their proofs in Appendix A. |
| gui-jiang-wang2023 | https://arxiv.org/html/2310.20460v1; Section 2.2 (Equation 4 and Table 1, lines 134-219), Section 3.1.2-3.1.3 (lines 290-430) | supports | All 1,071 lines of the full-text arXiv HTML conversion of arXiv:2310.20460v1 read. Checked conditional left-truncated heavy-tailed transformations and Section 3.1.2-3.1.3. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT left-truncated Cauchy combination test record, yielding 568 native and 442 unchanged generated records.
- All 546 lines of Fang et al. (2023, arXiv:2103.12967) and all 1,071 lines of Gui, Jiang, &amp; Wang (2023, arXiv:2310.20460v1) were read. No author R package or neuroticism GWAS pipeline was run; constructed numerical checks verify boundary limits, negative-penalty cancellation immunity, and Proposition 3/4 GCLT and binomial tail bounds only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T102200Z-left-truncated-cauchy-combination
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of left-truncated Cauchy combination test
started_at: '2026-10-17T10:20:00Z'
finished_at: '2026-10-17T10:22:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from standard
    CauchyCombinationTest (Liu & Xie 2020) and HalfCauchyCombinationTest (Liu, Meng,
    & Pillai 2025), loss of exact finite-sample Cauchy stability under left truncation,
    GCLT location-shift growth in Proposition 3, and binomial tail bounds in Proposition
    4. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the left-truncated Cauchy combination test as a distinct DRAFT mathematical_method
  with related DataDredgingBias mapping. All four claims and locators across Fang
  et al. (2023) and Gui, Jiang, & Wang (2023) are supported with explicit finite-sample
  stability loss, GCLT shift, and truncation-threshold tuning boundaries. No actionable
  defect was found; author R/GWAS pipelines remain unverified.
source:
  git_revision: 202a48a2166e86eb8169dd35b26ed47bad4b7ebc
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
    role: context
  - path: data/curated/HalfCauchyCombinationTest.yaml
    sha256: 16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e
    role: context
  - path: data/curated/LeftTruncatedCauchyCombinationTest.yaml
    sha256: 6f330e91bd1f1994411c626759aee135f6dc781c2b3107e2c9db78e26c5685f6
    role: target
  - path: data/curated/LogarithmicOpinionPool.yaml
    sha256: bdff4b82fa80ae38dd1a1295afdf9f5c0d877632818ea25841ca7a4adce2f430
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: research/discovery/20261017T102000Z-left-truncated-cauchy-combination.json
    sha256: 134e88dcde9b85e0919d171a0366adc45f76714c4d043c40eed76c11c5e48a0a
    role: context
  - path: research/discovery/left-truncated-cauchy-combination-boundaries.py
    sha256: 2d6f6f20afe04fc73872e4aaa7f71759ecb7a53d27dc59ded13b76302c9b91ea
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
- target_id: AIMech:LeftTruncatedCauchyCombinationTest
  path: data/curated/LeftTruncatedCauchyCombinationTest.yaml
  label: Left-truncated Cauchy combination test
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LeftTruncatedCauchyCombinationTest.yaml
    role: maintained
scope:
  description: All fields of the exact maintained LeftTruncatedCauchyCombinationTest
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:LeftTruncatedCauchyCombinationTest'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source R packages and neuroticism GWAS pipelines
    reason: No author R package or empirical GWAS data run.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: All AIMech schema, curated, seed, and history validations passed.
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW review files match canonical checksums.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed left-truncated Cauchy combination boundaries
  command: python3 research/discovery/left-truncated-cauchy-combination-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:LeftTruncatedCauchyCombinationTest\",\n\
    \  \"boundary_limits\": {\n    \"max_rel_diff_p0_05_vs_half_cauchy\": 6.104540043087295e-13,\n\
    \    \"max_rel_diff_p0_10_vs_standard_cauchy\": 0.0,\n    \"cond_lower_bound_p0_09\"\
    : -3.077683537175253,\n    \"winsorized_lower_bound_delta_001\": -31.820515953773857\n\
    \  },\n  \"cancellation_immunity_p1_1e-4_p2_1-1e-6\": {\n    \"standard_cct_mean_stat\"\
    : -157563.39371035108,\n    \"standard_cct_combined_p\": 0.9999979797979806,\n\
    \    \"cond_left_truncated_sum_stat_p0_09\": 3533.6987649768485,\n    \"cond_left_truncated_combined_p_p0_09\"\
    : 0.0002001741888014842,\n    \"winsorized_left_truncated_mean_stat_delta_001\"\
    : 1575.6391205815275,\n    \"winsorized_left_truncated_combined_p_delta_001\"\
    : 0.00020201951023418596\n  },\n  \"fang_prop3_prop4_verification\": {\n    \"\
    n_tests\": 10,\n    \"t_thresh\": 100.0,\n    \"prop4_lower_bound\": 0.003182992764908188,\n\
    \    \"prop4_sharp_upper_bound\": 0.003471650826855522,\n    \"prop4_binomial_upper_bound\"\
    : 0.003516004233141369,\n    \"mc_empirical_tail_prob\": 0.00326,\n    \"prop3_gclt_n50_delta001\"\
    : {\n      \"nu_delta\": -31.820515953773857,\n      \"f1n\": 3.074140806502033,\n\
    \      \"f2n\": 0.019411035201823756,\n      \"theta_n\": 0.0001779445628941012,\n\
    \      \"n_theta_n\": 0.00889722814470506\n    }\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T102000Z-left-truncated-cauchy-combination.json
  accessed_at: '2026-10-17T10:20:00Z'
  support: supports
  summary: No normalized identity match for the left-truncated Cauchy combination
    test across 442 pinned AIO records and 567 maintained IDs, names, aliases and
    scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data,
    sources, research, history, and reviews returned 0 lines. Distinct from AIMech:CauchyCombinationTest
    and AIMech:HalfCauchyCombinationTest.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T10:20:00Z'
  support: supports
  summary: Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot
    (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/left-truncated-cauchy-combination-boundaries.py
  accessed_at: '2026-10-17T10:20:00Z'
  snapshot_sha256: 2d6f6f20afe04fc73872e4aaa7f71759ecb7a53d27dc59ded13b76302c9b91ea
  support: supports
  summary: Constructed analytical and Monte Carlo checks for (1) p_0 = 0.5 Half-Cauchy
    and p_0 = 1.0 standard Cauchy boundaries, (2) elimination of negative score cancellation
    on (p_1 = 1e-4, p_2 = 1 - 1e-6), and (3) Fang et al. Proposition 3/4 GCLT and
    binomial tail bounds.
- evidence_id: fang-chang-park-tseng2023
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2103.12967
  locator: Section 2.2 (Propositions 3-4), Section 3 (Theorems 1-3), Section 4.3,
    Section 5, Appendix A (lines 508, 528-535)
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 432b18ec119b33e5b3cd66b32bb71015a243bb7dd28362cf7c9557f0e78a8402
  support: supports
  summary: All 546 lines of the full-text ar5iv HTML conversion of arXiv:2103.12967
    read. Checked Propositions 3-4, Theorems 1-3, and their proofs in Appendix A.
- evidence_id: gui-jiang-wang2023
  kind: primary_source
  reference: https://arxiv.org/html/2310.20460v1
  locator: Section 2.2 (Equation 4 and Table 1, lines 134-219), Section 3.1.2-3.1.3
    (lines 290-430)
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 3f487fc6bca4b5db326053b80a172ec71bee5387faa78dc2605e6bf91c795f71
  support: supports
  summary: All 1,071 lines of the full-text arXiv HTML conversion of arXiv:2310.20460v1
    read. Checked conditional left-truncated heavy-tailed transformations and Section
    3.1.2-3.1.3.
assessments:
- assessment_id: identity
  area: identity
  topic: Left-Truncated Cauchy Combination Test versus standard Cauchy and Half-Cauchy
    combination tests
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - identity
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  summary: Retain the left-truncated Cauchy combination test as a distinct DRAFT mathematical_method.
  details: Fang et al. (2023, Section 2.2) and Gui, Jiang, & Wang (2023, Section 2.2)
    define negative-support left-truncated Cauchy combination tests (nu_delta < 0
    or c < 0) that eliminate unbounded negative penalties as p_i -> 1 while differing
    from both untruncated CauchyCombinationTest and strictly non-negative HalfCauchyCombinationTest
    (c = 0).
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - mapping
  - fang-chang-park-tseng2023
  summary: Related mapping to DataDredgingBias is supported.
  details: Left-truncated Cauchy combination controls global Type I error across multiple
    dependent hypothesis tests, mitigating false-positive inflation from multiple
    testing (AIO:DataDredgingBias).
- assessment_id: winsorized-and-conditional-left-truncated-cauchy-transformations
  area: evidence
  topic: winsorized-and-conditional-left-truncated-cauchy-transformations
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  - calculation
  summary: Supported by Fang et al. Section 2.2 and Gui et al. Section 2.2 and verified
    numerically.
  details: Winsorized truncation p_i^tr = min(p_i, 1 - delta) bounds scores at nu_delta
    = tan(pi*(delta - 0.5)), while conditional left truncation bounds scores at c
    = tan(pi*(0.5 - p_0)).
- assessment_id: regularly-varying-index-one-and-asymptotic-dependence-robustness
  area: evidence
  topic: regularly-varying-index-one-and-asymptotic-dependence-robustness
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  summary: Supported by Theorems 1-3 in Fang et al. (2023) and Section 3.1.2-3.1.3
    in Gui et al. (2023).
  details: Left-truncated Cauchy satisfies Condition (A2.2) and belongs to R_{-1}
    with gamma = 1, p = 1, q = 0, guaranteeing asymptotic tail equivalence under arbitrary
    correlation |rho_{ij}| < 1 and Donoho-Jin sparse optimality.
- assessment_id: gclt-stable-approximation-and-finite-sample-tail-bounds
  area: evidence
  topic: gclt-stable-approximation-and-finite-sample-tail-bounds
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - fang-chang-park-tseng2023
  - calculation
  summary: Supported by Propositions 3-4 and Appendix A proof and verified via Monte
    Carlo and Simpson quadrature.
  details: Verified Proposition 4 bounds (0.003183 <= 0.003260 <= 0.003472 <= 0.003516)
    for n=10, delta=0.01, t=100 and Proposition 3 GCLT location shift theta_n.
- assessment_id: power-recovery-under-discrete-and-negatively-correlated-p-values
  area: evidence
  topic: power-recovery-under-discrete-and-negatively-correlated-p-values
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  - calculation
  summary: Supported by Section 4.3 and Section 5 of Fang et al. (2023) and verified
    on (1e-4, 1 - 1e-6).
  details: Prevents p-values near 1 in discrete Fisher exact tests or neuroticism
    GWAS genes (SLC2A9, PCSK6) from cancelling true small-p signals.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:LeftTruncatedCauchyCombinationTest
  evidence_ids:
  - identity
  - mapping
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of LeftTruncatedCauchyCombinationTest.yaml: stable ID,
    name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes,
    four claims and locators, two full-text primary sources with exact SHA-256 digests,
    pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT left-truncated Cauchy combination test record, yielding 568 native
  and 442 unchanged generated records.
- All 546 lines of Fang et al. (2023, arXiv:2103.12967) and all 1,071 lines of Gui,
  Jiang, & Wang (2023, arXiv:2310.20460v1) were read. No author R package or neuroticism
  GWAS pipeline was run; constructed numerical checks verify boundary limits, negative-penalty
  cancellation immunity, and Proposition 3/4 GCLT and binomial tail bounds only.
related_reviews: []
links: []
tags:
- native-concepts
- hypothesis-testing
- multiple-testing
- self-review
- discovery-ongoing
```
