# Scientific author self-review of Conditional calibration for false discovery rate control under dependence

- Review: 20261017T142700Z-conditional-calibration-for-false-discovery-rate-control
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T14:25:00Z
- Finished UTC: 2026-10-17T14:27:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Conditional calibration for false discovery rate control under dependence as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Fithian &amp; Lei (2022 AoS 50(6):3091-3118) are supported with explicit covariance-specification, randomized-pruning, and composite-null partial-sufficiency limitations.

## Scope And Provenance

All fields of the exact maintained ConditionalCalibrationForFalseDiscoveryRateControl record and its primary evidence.

Selection: Exact maintained ID: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5667ae21602ae25b759746ecb36e2a236af8947a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml | maintained | Conditional calibration for false discovery rate control under dependence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | All 586 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | Exited 0 without output. |
| Constructed conditional calibration for false discovery rate control checks | passed | True | AIMech:ConditionalCalibrationForFalseDiscoveryRateControl | {<br>  "claim1_lemma1_and_randomized_pruning_fdr": {<br>    "fdr_pruned_with_step3": 0.12775,<br>    "fdr_unpruned_without_step3": 0.22655,<br>    "lemma1_exact_match_rate": 1.0,<br>    "pruning_invoked_rate": 0.99825,<br>    "theoretical_fdr_bound": 0.133333<br>  },<br>  "claim2_dbh_dominance_and_safety": {<br>    "avg_discoveries_bh_pos": 1.641667,<br>    "avg_discoveries_by_neg": 1.466667,<br>    "avg_discoveries_dbh_pos": 1.683333,<br>    "avg_discoveries_dby_neg": 1.741667,<br>    "fdr_dbh_pos": 0.083333,<br>    "fdr_dby_neg": 0.075,<br>    "ind_exact_match_rate": 1.0,<br>    "neg_dby_dominance_rate": 1.0,<br>    "neg_dby_safe_rate": 1.0,<br>    "pos_cprds_dominance_rate": 1.0,<br>    "pos_cprds_safe_rate": 1.0<br>  },<br>  "claim3_knot_homotopy_and_recursive_refinement": {<br>    "avg_discoveries_iter1": 1.475,<br>    "avg_discoveries_iter2": 1.4875,<br>    "g_star_exact_knots": 0.038511,<br>    "g_star_fine_quadrature": 0.03849,<br>    "knot_vs_quadrature_abs_error": 2.082e-05,<br>    "recursive_refinement_monotone_rate": 1.0<br>  },<br>  "claim4_composite_null_and_misspecified_sigma_boundary": {<br>    "g_theta_0_boundary": 0.034368,<br>    "g_theta_minus_0_5": 0.013472,<br>    "g_theta_minus_1_0": 0.004235,<br>    "null0_fdr_contrib_misspecified_sigma": 0.1075,<br>    "target_per_hypothesis_alpha_over_m": 0.04<br>  }<br>} |

## Scientific And Domain Assessments

### ConditionalCalibrationForFalseDiscoveryRateControl versus EbhProcedure, SimultaneousPathwiseFalseDiscoveryProportionBounds, and AdaptivePValueThresholding

identity: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Retain Conditional calibration for false discovery rate control under dependence as a distinct DRAFT mathematical_method.

ConditionalCalibrationForFalseDiscoveryRateControl decomposes FDR into per-hypothesis expectations calibrated conditionally on a sufficient statistic S_i for the dependency of T_{-i} on T_i (Lemma 1, Theorem 1, dBH/dBY in Theorem 2), whereas EbhProcedure thresholds e-values without conditioning, SimultaneousPathwiseFalseDiscoveryProportionBounds constructs high-probability simultaneous FDP envelopes, and AdaptivePValueThresholding requires independent mirror-conservative null p-values.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Related mapping to DataDredgingBias is supported.

Conditional calibration and dBH/dBY control false discovery rate inflation across dependent multiple hypothesis tests without conservative BY log-factor penalties (AIO:DataDredgingBias).

### sufficiency-based-bh-identity-and-three-step-conditional-calibration-randomized-pruning-fdr-theorem

evidence: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Supported by Section 2.1-2.4 Lemma 1, Proposition 1, Theorem 1, Example 1, Equations 3-13.

Verified Lemma 1 exact conditional FDR identity (100% match across 200 conditioning states) and Theorem 1 / Example 1 necessity of Step 3 randomized pruning (unpruned FDR = 0.22655 &gt; 0.20 vs. pruned FDR = 0.12775 &lt;= 0.133333).

### dependency-adjusted-bh-and-by-cprds-dominance-and-negative-dependence-adaptivity

evidence: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Supported by Section 3.1-3.2 Equations 14-16, Theorem 2, and Appendix A.1.

Verified exact reduction to BH under independence (100% match), 100% CPRDS safety and dominance dBH_1 supseteq BH under positive correlation (rho = 0.60), and 100% safety and dominance dBY_1 supseteq BY under negative equicorrelation (rho = -0.45, average discoveries 1.741667 vs. 1.466667).

### affine-gaussian-knot-homotopy-and-recursive-multi-step-refinement

evidence: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Supported by Section 2.2, Section 4.1 Proposition 2, Equations 18-21, and Section 4.3 Theorem 3, Equations 22-26.

Verified exact knot integration matching fine quadrature (abs error 2.082e-05) and monotonic multi-step recursive refinement (100% monotone, average discoveries 1.4875 vs. 1.475).

### one-sided-composite-null-boundary-suppression-and-covariance-misspecification-boundary

evidence: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

Supported by Section 3.3 Equation 17 and Section 2.2-2.4 Lemma 1 and Theorem 1.

Verified composite-null boundary suppression (g_0 = 0.034368 &gt; g_{-0.5} = 0.013472 &gt; g_{-1.0} = 0.004235) and covariance misspecification failure (null FDR contribution 0.1075 &gt; alpha/m = 0.04).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl.

The full record is consistent; retain DRAFT.

Read every field of ConditionalCalibrationForFalseDiscoveryRateControl.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T142500Z-conditional-calibration-for-false-discovery-rate-control.json | supports | No normalized identity match for conditional calibration for false discovery rate control across 442 pinned AIO records and 585 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides multiple-testing false-discovery rate control context via related_match. |
| calculation | research/discovery/conditional-calibration-for-false-discovery-rate-control-boundaries.py | supports | Constructed analytical and numerical checks for the sufficiency-based BH conditional FDR identity (Lemma 1), three-step conditional calibration and randomized pruning (Theorem 1 / Example 1), dBH/dBY CPRDS and negative-dependence dominance (Theorem 2), exact piecewise-constant knot integration (Proposition 2), multi-step recursive refinement (Theorem 3), and composite-null boundary suppression vs. covariance misspecification. |
| fithian2022-conditional-calibration-fdr-ar5iv | https://ar5iv.labs.arxiv.org/html/2007.10438; Sections 1-7 and Appendices A-C (lines 1-1304, Lemma 1, Propositions 1-2, Theorems 1-3, Equations 1-26) | supports | All 1,304 lines of the full-text ar5iv HTML conversion of arXiv:2007.10438v1 read. Checked all theorems, propositions, lemmas, examples, and proofs across Sections 1-7 and Appendices A-C. |
| fithian2022-conditional-calibration-fdr-crossref | https://api.crossref.org/works/10.1214/21-AOS2137; The Annals of Statistics Vol. 50, No. 6, pp. 3091-3118 publication record | supports | Official The Annals of Statistics 50(6):3091-3118 Crossref record read and verified. |
| fithian2022-conditional-calibration-fdr-abs | https://arxiv.org/abs/2007.10438; arXiv:2007.10438v1 abstract and AoS 2022 metadata | supports | arXiv:2007.10438v1 abstract and AoS 2022 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Conditional calibration for false discovery rate control under dependence record, yielding 586 native and 442 unchanged generated records.
- All 1,304 lines of Fithian &amp; Lei (2022, arXiv:2007.10438v1) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T142700Z-conditional-calibration-for-false-discovery-rate-control
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Conditional calibration for false discovery
  rate control under dependence
started_at: '2026-10-17T14:25:00Z'
finished_at: '2026-10-17T14:27:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from EbhProcedure,
    SimultaneousPathwiseFalseDiscoveryProportionBounds, AdaptivePValueThresholding,
    and FocusedBH, the sufficiency requirement of Lemma 1 under covariance misspecification,
    the necessity of Step 3 randomized pruning in Theorem 1 / Example 1, and partial
    sufficiency under composite nulls (Section 3.3). This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Conditional calibration for false discovery rate control under dependence
  as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping.
  All four claims and locators across Fithian & Lei (2022 AoS 50(6):3091-3118) are
  supported with explicit covariance-specification, randomized-pruning, and composite-null
  partial-sufficiency limitations.
source:
  git_revision: 5667ae21602ae25b759746ecb36e2a236af8947a
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml
    sha256: 6167290e8178827ea950c80549426c871ba5e2b6d727b42b4a536d860e097946
    role: target
  - path: data/curated/ForkConvexExchangeabilityTestingBySafeEProcesses.yaml
    sha256: 300ea1665bdd8cedfa38746832f1e7d6b85a410eacb4a87ca16eab55ca833370
    role: context
  - path: data/curated/ModelXAnytimeValidConditionalIndependenceTesting.yaml
    sha256: 00eba6063c717bd325de163ab10f91b16f906630f6e81a4b04d61f7fa698445e
    role: context
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T142500Z-conditional-calibration-for-false-discovery-rate-control.json
    sha256: 0088ee7e33058ed25a0a53eea4112218a74415ae97c1cd68fc4e93e2b96c39f8
    role: context
  - path: research/discovery/conditional-calibration-for-false-discovery-rate-control-boundaries.py
    sha256: b2faa8358e24e389e3f4990eb3335d0ce511a19c1dc4f2c4b38bdd1c0cbec9b2
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
- target_id: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  path: data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml
  label: Conditional calibration for false discovery rate control under dependence
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ConditionalCalibrationForFalseDiscoveryRateControl
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ConditionalCalibrationForFalseDiscoveryRateControl'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
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
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 586 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed conditional calibration for false discovery rate control checks
  command: python3 research/discovery/conditional-calibration-for-false-discovery-rate-control-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"claim1_lemma1_and_randomized_pruning_fdr\": {\n    \"fdr_pruned_with_step3\"\
    : 0.12775,\n    \"fdr_unpruned_without_step3\": 0.22655,\n    \"lemma1_exact_match_rate\"\
    : 1.0,\n    \"pruning_invoked_rate\": 0.99825,\n    \"theoretical_fdr_bound\"\
    : 0.133333\n  },\n  \"claim2_dbh_dominance_and_safety\": {\n    \"avg_discoveries_bh_pos\"\
    : 1.641667,\n    \"avg_discoveries_by_neg\": 1.466667,\n    \"avg_discoveries_dbh_pos\"\
    : 1.683333,\n    \"avg_discoveries_dby_neg\": 1.741667,\n    \"fdr_dbh_pos\":\
    \ 0.083333,\n    \"fdr_dby_neg\": 0.075,\n    \"ind_exact_match_rate\": 1.0,\n\
    \    \"neg_dby_dominance_rate\": 1.0,\n    \"neg_dby_safe_rate\": 1.0,\n    \"\
    pos_cprds_dominance_rate\": 1.0,\n    \"pos_cprds_safe_rate\": 1.0\n  },\n  \"\
    claim3_knot_homotopy_and_recursive_refinement\": {\n    \"avg_discoveries_iter1\"\
    : 1.475,\n    \"avg_discoveries_iter2\": 1.4875,\n    \"g_star_exact_knots\":\
    \ 0.038511,\n    \"g_star_fine_quadrature\": 0.03849,\n    \"knot_vs_quadrature_abs_error\"\
    : 2.082e-05,\n    \"recursive_refinement_monotone_rate\": 1.0\n  },\n  \"claim4_composite_null_and_misspecified_sigma_boundary\"\
    : {\n    \"g_theta_0_boundary\": 0.034368,\n    \"g_theta_minus_0_5\": 0.013472,\n\
    \    \"g_theta_minus_1_0\": 0.004235,\n    \"null0_fdr_contrib_misspecified_sigma\"\
    : 0.1075,\n    \"target_per_hypothesis_alpha_over_m\": 0.04\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T142500Z-conditional-calibration-for-false-discovery-rate-control.json
  accessed_at: '2026-10-17T14:25:00Z'
  support: supports
  summary: No normalized identity match for conditional calibration for false discovery
    rate control across 442 pinned AIO records and 585 maintained IDs, names, aliases
    and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T14:25:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides multiple-testing false-discovery rate control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/conditional-calibration-for-false-discovery-rate-control-boundaries.py
  accessed_at: '2026-10-17T14:25:00Z'
  snapshot_sha256: b2faa8358e24e389e3f4990eb3335d0ce511a19c1dc4f2c4b38bdd1c0cbec9b2
  support: supports
  summary: Constructed analytical and numerical checks for the sufficiency-based BH
    conditional FDR identity (Lemma 1), three-step conditional calibration and randomized
    pruning (Theorem 1 / Example 1), dBH/dBY CPRDS and negative-dependence dominance
    (Theorem 2), exact piecewise-constant knot integration (Proposition 2), multi-step
    recursive refinement (Theorem 3), and composite-null boundary suppression vs.
    covariance misspecification.
- evidence_id: fithian2022-conditional-calibration-fdr-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2007.10438
  locator: Sections 1-7 and Appendices A-C (lines 1-1304, Lemma 1, Propositions 1-2,
    Theorems 1-3, Equations 1-26)
  accessed_at: '2026-10-17T14:25:00Z'
  snapshot_sha256: 3d199e8460e412f938c6fadae545d7ac86ddac5ae3c276fb367ed2dd21e283ca
  support: supports
  summary: All 1,304 lines of the full-text ar5iv HTML conversion of arXiv:2007.10438v1
    read. Checked all theorems, propositions, lemmas, examples, and proofs across
    Sections 1-7 and Appendices A-C.
- evidence_id: fithian2022-conditional-calibration-fdr-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/21-AOS2137
  locator: The Annals of Statistics Vol. 50, No. 6, pp. 3091-3118 publication record
  accessed_at: '2026-10-17T14:25:00Z'
  snapshot_sha256: 0da632f9a9738883608821f45e1112036619f11fd13df8a1cdef954f03ac6711
  support: supports
  summary: Official The Annals of Statistics 50(6):3091-3118 Crossref record read
    and verified.
- evidence_id: fithian2022-conditional-calibration-fdr-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2007.10438
  locator: arXiv:2007.10438v1 abstract and AoS 2022 metadata
  accessed_at: '2026-10-17T14:25:00Z'
  snapshot_sha256: d6affd9d3855f47b4e74deccb560adaf52dd327140b3fe4e57bcc2b83f00e0ae
  support: supports
  summary: arXiv:2007.10438v1 abstract and AoS 2022 metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ConditionalCalibrationForFalseDiscoveryRateControl versus EbhProcedure, SimultaneousPathwiseFalseDiscoveryProportionBounds,
    and AdaptivePValueThresholding
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - identity
  - fithian2022-conditional-calibration-fdr-ar5iv
  - fithian2022-conditional-calibration-fdr-crossref
  summary: Retain Conditional calibration for false discovery rate control under dependence
    as a distinct DRAFT mathematical_method.
  details: ConditionalCalibrationForFalseDiscoveryRateControl decomposes FDR into
    per-hypothesis expectations calibrated conditionally on a sufficient statistic
    S_i for the dependency of T_{-i} on T_i (Lemma 1, Theorem 1, dBH/dBY in Theorem
    2), whereas EbhProcedure thresholds e-values without conditioning, SimultaneousPathwiseFalseDiscoveryProportionBounds
    constructs high-probability simultaneous FDP envelopes, and AdaptivePValueThresholding
    requires independent mirror-conservative null p-values.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - mapping
  - fithian2022-conditional-calibration-fdr-ar5iv
  summary: Related mapping to DataDredgingBias is supported.
  details: Conditional calibration and dBH/dBY control false discovery rate inflation
    across dependent multiple hypothesis tests without conservative BY log-factor
    penalties (AIO:DataDredgingBias).
- assessment_id: sufficiency-based-bh-identity-and-three-step-conditional-calibration-randomized-pruning-fdr-theorem
  area: evidence
  topic: sufficiency-based-bh-identity-and-three-step-conditional-calibration-randomized-pruning-fdr-theorem
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - fithian2022-conditional-calibration-fdr-ar5iv
  - fithian2022-conditional-calibration-fdr-abs
  - calculation
  summary: Supported by Section 2.1-2.4 Lemma 1, Proposition 1, Theorem 1, Example
    1, Equations 3-13.
  details: Verified Lemma 1 exact conditional FDR identity (100% match across 200
    conditioning states) and Theorem 1 / Example 1 necessity of Step 3 randomized
    pruning (unpruned FDR = 0.22655 > 0.20 vs. pruned FDR = 0.12775 <= 0.133333).
- assessment_id: dependency-adjusted-bh-and-by-cprds-dominance-and-negative-dependence-adaptivity
  area: evidence
  topic: dependency-adjusted-bh-and-by-cprds-dominance-and-negative-dependence-adaptivity
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - fithian2022-conditional-calibration-fdr-ar5iv
  - fithian2022-conditional-calibration-fdr-crossref
  - calculation
  summary: Supported by Section 3.1-3.2 Equations 14-16, Theorem 2, and Appendix A.1.
  details: Verified exact reduction to BH under independence (100% match), 100% CPRDS
    safety and dominance dBH_1 supseteq BH under positive correlation (rho = 0.60),
    and 100% safety and dominance dBY_1 supseteq BY under negative equicorrelation
    (rho = -0.45, average discoveries 1.741667 vs. 1.466667).
- assessment_id: affine-gaussian-knot-homotopy-and-recursive-multi-step-refinement
  area: evidence
  topic: affine-gaussian-knot-homotopy-and-recursive-multi-step-refinement
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - fithian2022-conditional-calibration-fdr-ar5iv
  - calculation
  summary: Supported by Section 2.2, Section 4.1 Proposition 2, Equations 18-21, and
    Section 4.3 Theorem 3, Equations 22-26.
  details: Verified exact knot integration matching fine quadrature (abs error 2.082e-05)
    and monotonic multi-step recursive refinement (100% monotone, average discoveries
    1.4875 vs. 1.475).
- assessment_id: one-sided-composite-null-boundary-suppression-and-covariance-misspecification-boundary
  area: evidence
  topic: one-sided-composite-null-boundary-suppression-and-covariance-misspecification-boundary
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - fithian2022-conditional-calibration-fdr-ar5iv
  - calculation
  summary: Supported by Section 3.3 Equation 17 and Section 2.2-2.4 Lemma 1 and Theorem
    1.
  details: Verified composite-null boundary suppression (g_0 = 0.034368 > g_{-0.5}
    = 0.013472 > g_{-1.0} = 0.004235) and covariance misspecification failure (null
    FDR contribution 0.1075 > alpha/m = 0.04).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ConditionalCalibrationForFalseDiscoveryRateControl
  evidence_ids:
  - identity
  - mapping
  - fithian2022-conditional-calibration-fdr-ar5iv
  - fithian2022-conditional-calibration-fdr-crossref
  - fithian2022-conditional-calibration-fdr-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ConditionalCalibrationForFalseDiscoveryRateControl.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Conditional calibration for false discovery rate control under dependence
  record, yielding 586 native and 442 unchanged generated records.
- All 1,304 lines of Fithian & Lei (2022, arXiv:2007.10438v1) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- conditional-calibration
- dbh
- dependence
- self-review
- discovery-ongoing
```
