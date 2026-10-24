# Scientific author self-review of Reference-family joint error rate post hoc confidence bounds

- Review: 20261017T165700Z-reference-family-jer-post-hoc-confidence-bounds
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T16:55:00Z
- Finished UTC: 2026-10-17T16:57:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Reference-family joint error rate post hoc confidence bounds as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Blanchard, Neuvial, &amp; Roquain (2020, The Annals of Statistics 48(3):1281-1303, arXiv:1703.02307v3/v2) are supported with explicit non-nested NP-hardness, data-dependent permutation template gap (Meinshausen 2006 Equation 12), single-step balanced JER collapse O((log m)^{-1/8}), and primary-source typographical limitations.

## Scope And Provenance

All fields of the exact maintained ReferenceFamilyJERPostHocConfidenceBounds record and its primary evidence.

Selection: Exact maintained ID: AIMech:ReferenceFamilyJERPostHocConfidenceBounds
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0a301e545165fe8492befcf755628da13baabeb4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ReferenceFamilyJERPostHocConfidenceBounds | data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml | maintained | Reference-family joint error rate post hoc confidence bounds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | All 603 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | Exited 0 without output. |
| Constructed Blanchard-Neuvial-Roquain 2020 reference-family interpolation, Goeman-Solari shortcut equivalence, Simes Beta tail probabilities, and step-down lambda-calibration checks | passed | True | AIMech:ReferenceFamilyJERPostHocConfidenceBounds | {<br>  "concept_id": "AIMech:ReferenceFamilyJERPostHocConfidenceBounds",<br>  "primary_source": "Blanchard, Neuvial, &amp; Roquain (2020), The Annals of Statistics 48(3):1281-1303 (arXiv:1703.02307v3/v2, DOI:10.1214/19-AOS1847)",<br>  "section_2_and_8_structural_properties": {<br>    "triangle_np_hardness_gap": {<br>      "v_star_exact": 1,<br>      "v_bar_approx": 2<br>    },<br>    "self_consistency_idempotence_verified_subsets": 32,<br>    "nested_exactness_v_bar_eq_v_star_verified_subsets": 64,<br>    "goeman_solari_shortcut_equivalence_verified_subsets": 64,<br>    "admissible_sets_count": 3<br>  },<br>  "section_4_table_2_simes_unbalancedness": {<br>    "m": 1000,<br>    "alpha": 0.05,<br>    "exact_probabilities": {<br>      "1": 0.048772,<br>      "2": 0.0046748,<br>      "3": 0.00050152,<br>      "4": 5.6535e-05,<br>      "5": 6.5525e-06,<br>      "10": 1.6415e-10,<br>      "100": 5.7919e-93<br>    }<br>  },<br>  "sections_5_6_known_equicorrelation_step_down": {<br>    "rho": 0.5,<br>    "alpha": 0.2,<br>    "lambda_full_known": 0.361178,<br>    "lambda_oracle_known": 0.495548,<br>    "empirical_jer_simes": 0.085,<br>    "empirical_jer_single_step": 0.135,<br>    "empirical_jer_step_down": 0.1817,<br>    "empirical_jer_oracle": 0.1817,<br>    "mean_true_discovery_bound_simes": 13.0017,<br>    "mean_true_discovery_bound_step_down": 14.7567<br>  },<br>  "section_5_4_unknown_dependence_sign_flipping": {<br>    "B_flips": 99,<br>    "alpha": 0.2,<br>    "empirical_jer_single_step": 0.0333,<br>    "empirical_jer_step_down": 0.1667<br>  },<br>  "section_7_detection_boundary": {<br>    "beta": 0.6,<br>    "rho_star_balanced_hc": 0.1,<br>    "rho_star_linear_bh": 0.135089,<br>    "sparse_weak_r": 0.115<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### ReferenceFamilyJERPostHocConfidenceBounds versus SimultaneousPathwiseFalseDiscoveryProportionBounds and HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality

identity: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Retain Reference-family joint error rate post hoc confidence bounds as a distinct DRAFT mathematical_method.

ReferenceFamilyJERPostHocConfidenceBounds defines user-agnostic post hoc confidence bounds V^*_{R_ref}(R) and V_bar_{R_ref}(R) valid simultaneously over all 2^m subsets R subset N_m via reference-family JER control, single-step and step-down lambda-calibration under LeastFavor and Rand, Goeman-Solari closed-testing equivalence, and Higher Criticism detection optimality.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Related mapping to DataDredgingBias is supported.

Reference-family JER post hoc confidence bounds prevent post-selection data-snooping invalidation (AIO:DataDredgingBias).

### reference-family-jer-interpolation-equivalence-np-hardness-and-nested-optimality

evidence: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Supported by Section 2.2-2.3 (Propositions 2.1, 2.3, 2.4, 2.5 in v3; Propositions 2.1-2.4 and Appendix B.1 in v2) and Section 8.4.

Verified event equivalence, triangle-graph NP-hardness gap V^* = 1 &lt; V_bar = 2, self-consistency idempotence, nested exactness V_bar = V^*, and Section 8.4 admissibility.

### closed-testing-specialization-simes-shortcut-equivalence-and-unbalancedness

evidence: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Supported by Section 4.1-4.3 (Theorem 4.1, Tables 1-2 in v3), Section 8.1-8.3 (Lemmas 8.1-8.2 in v2), and Appendix A.1 (Proposition A.1(iv)).

Verified exact algebraic identity V_bar_{R_ref}(R) = V_bar^{GS}_alpha(R) across all 64 subsets and exact Table 2 Beta tail probabilities.

### threshold-templates-and-single-step-and-step-down-lambda-calibration

evidence: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Supported by Section 3.2, Section 5.1-5.4 (Definitions 5.1, 5.3, Lemma 5.2, Propositions 5.4-5.5, Algorithm 1, Theorems 5.7-5.8), and Appendix A in v3.

Verified single-step and step-down JER control under both known Gaussian equicorrelation (Theorem 5.7) and unknown-dependence sign-flipping (Theorem 5.8).

### linear-vs-balanced-template-asymptotic-conservativeness-and-higher-criticism-detection-optimality

evidence: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

Supported by Section 6.1-6.2 in v3 and Section 5.1-5.3, Section 7.1-7.3 (Theorems 7.2-7.3), Appendix A.1-A.2 (Proposition A.1, Lemmas A.2-A.3), and Appendix B.2-B.3 in v2.

Verified Proposition A.1 Beta quantile bounds, O((log m)^{-1/8}) single-step balanced JER decay under pi_0 &lt; 1, and Higher Criticism detection boundary rho^*(beta) vs. BH detection boundary.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ReferenceFamilyJERPostHocConfidenceBounds.

The full record is consistent; retain DRAFT.

Read every field of ReferenceFamilyJERPostHocConfidenceBounds.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, four primary sources with exact SHA-256 digests, pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T165500Z-reference-family-jer-post-hoc-confidence-bounds.json | supports | No normalized identity match for reference-family joint error rate post hoc confidence bounds across 442 pinned AIO records and 602 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides frequentist post-selection and multiplicity error-control context via related_match. |
| calculation | research/discovery/reference-family-jer-post-hoc-confidence-bounds-boundaries.py | supports | Constructed numerical checks verify (1) Section 2 and Section 8 structural properties: triangle-graph NP-hardness gap V^* = 1 &lt; V_bar = 2, self-consistency idempotence across all 32 subsets, nested exactness V_bar = V^* and Goeman-Solari shortcut equivalence across all 64 subsets, and Section 8.4 admissibility, (2) Section 4.3 Table 2 exact Beta tail probabilities (k=1: 0.048772, k=5: 6.5525e-06, k=100: 5.7919e-93) and Proposition A.1 bounds, and (3) Sections 5-6 single-step and step-down JER control under known Gaussian equicorrelation (rho=0.5: JER_Simes=0.085 &lt; JER_ss=0.135 &lt;= JER_sd=0.1817 &lt;= alpha=0.2) and unknown-dependence sign-flipping (B=99: JER_sd=0.1667 &lt;= 0.2). |
| bnr2020-v3-pdf | https://arxiv.org/pdf/1703.02307; Pages 1-29, Sections 1-8 and Appendix A (Propositions 2.1, 2.3, 2.4, 2.5, Conditions LeastFavor and Rand, Theorem 4.1, Tables 1-2, Definitions 5.1, 5.3, Lemma 5.2, Propositions 5.4-5.5, Algorithm 1, Theorems 5.7-5.8, Remarks 6.1-6.2) | supports | All 29 pages of the full-text PDF of arXiv:1703.02307v3 read. Checked all definitions, propositions, theorems, algorithms, tables, and proofs. |
| bnr2020-v2-pdf | https://arxiv.org/pdf/1703.02307v2; Pages 1-34, Sections 1-9 and Appendices A-D (Propositions 2.1-2.4, Theorems 7.2-7.3, Lemmas 8.1-8.2, Proposition A.1, Lemmas A.2-A.3) | supports | All 34 pages of the full-text PDF of arXiv:1703.02307v2 read, including complete appendices and proofs. |
| bnr2020-crossref | https://api.crossref.org/works/10.1214/19-AOS1847; The Annals of Statistics 48(3):1281-1303 publication record | supports | Official The Annals of Statistics 48(3):1281-1303 Crossref record read and verified. |
| bnr2020-abs | https://arxiv.org/abs/1703.02307; arXiv:1703.02307v3 abstract and metadata | supports | arXiv:1703.02307v3 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Reference-family joint error rate post hoc confidence bounds record, yielding 603 native and 442 unchanged generated records.
- All 29 PDF pages of arXiv:1703.02307v3 and all 34 PDF pages of arXiv:1703.02307v2 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T165700Z-reference-family-jer-post-hoc-confidence-bounds
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Reference-family joint error rate post hoc
  confidence bounds
started_at: '2026-10-17T16:55:00Z'
finished_at: '2026-10-17T16:57:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SimultaneousPathwiseFalseDiscoveryProportionBounds
    (Katsevich & Ramdas 2020) and HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality
    (Neuvial 2008), verified the triangle-graph NP-hardness gap V^* = 1 < V_bar =
    2, self-consistency idempotence, nested exactness V_bar = V^*, and Goeman-Solari
    (2011) Simes shortcut equivalence, computed exact Table 2 Beta tail probabilities,
    verified Theorems 5.7-5.8 single-step and step-down lambda-calibration under known
    equicorrelation and unknown-dependence sign-flipping, and documented three typographical
    slips in v3 (pp. 8, 19, 26). This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Reference-family joint error rate post hoc confidence bounds as a
  distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four
  claims and locators across Blanchard, Neuvial, & Roquain (2020, The Annals of Statistics
  48(3):1281-1303, arXiv:1703.02307v3/v2) are supported with explicit non-nested NP-hardness,
  data-dependent permutation template gap (Meinshausen 2006 Equation 12), single-step
  balanced JER collapse O((log m)^{-1/8}), and primary-source typographical limitations.
source:
  git_revision: 0a301e545165fe8492befcf755628da13baabeb4
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/AsymptoticallyOptimalRejectionCurveFDRControl.yaml
    sha256: fa6f6a7c44a7f51eaced5de206ddb6679c8bf92489442a4265e6b5c7a6373bf9
    role: context
  - path: data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml
    sha256: d58e0d5d29e1c28fe4115471e06c8d76d0f66c4265c51c4cf4f33134c4091593
    role: context
  - path: data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml
    sha256: 5a5948219058695b6b9d05e01f7285fa8bbcd1e34f823569989125e9eeeb6f89
    role: context
  - path: data/curated/HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality.yaml
    sha256: 6e35c0df6b71a10d35d4bfc2b25558014c91114141256210ef1fa9d1a78424c4
    role: context
  - path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
    sha256: 651276db83f388cdf782125e0ac769bacdb09ce89e63ebf1e9378b3a0d36d91f
    role: context
  - path: data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml
    sha256: 7e0edec4d6cecc10454f8004806f7bc4b178af9a5daa540242f1771d387050eb
    role: target
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T165500Z-reference-family-jer-post-hoc-confidence-bounds.json
    sha256: 61ad5eb08460b67af16b75558cb73d1ef7ab64278b1af090b3075b4cbec5d3eb
    role: context
  - path: research/discovery/reference-family-jer-post-hoc-confidence-bounds-boundaries.py
    sha256: ec2e60196e1983f307f7b7d68813a31deb5c5d1b1a3dcbcdd5def3b95ddabf74
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
- target_id: AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  path: data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml
  label: Reference-family joint error rate post hoc confidence bounds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ReferenceFamilyJERPostHocConfidenceBounds
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ReferenceFamilyJERPostHocConfidenceBounds'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
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
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 603 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Blanchard-Neuvial-Roquain 2020 reference-family interpolation,
    Goeman-Solari shortcut equivalence, Simes Beta tail probabilities, and step-down
    lambda-calibration checks
  command: python3 research/discovery/reference-family-jer-post-hoc-confidence-bounds-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:ReferenceFamilyJERPostHocConfidenceBounds\"\
    ,\n  \"primary_source\": \"Blanchard, Neuvial, & Roquain (2020), The Annals of\
    \ Statistics 48(3):1281-1303 (arXiv:1703.02307v3/v2, DOI:10.1214/19-AOS1847)\"\
    ,\n  \"section_2_and_8_structural_properties\": {\n    \"triangle_np_hardness_gap\"\
    : {\n      \"v_star_exact\": 1,\n      \"v_bar_approx\": 2\n    },\n    \"self_consistency_idempotence_verified_subsets\"\
    : 32,\n    \"nested_exactness_v_bar_eq_v_star_verified_subsets\": 64,\n    \"\
    goeman_solari_shortcut_equivalence_verified_subsets\": 64,\n    \"admissible_sets_count\"\
    : 3\n  },\n  \"section_4_table_2_simes_unbalancedness\": {\n    \"m\": 1000,\n\
    \    \"alpha\": 0.05,\n    \"exact_probabilities\": {\n      \"1\": 0.048772,\n\
    \      \"2\": 0.0046748,\n      \"3\": 0.00050152,\n      \"4\": 5.6535e-05,\n\
    \      \"5\": 6.5525e-06,\n      \"10\": 1.6415e-10,\n      \"100\": 5.7919e-93\n\
    \    }\n  },\n  \"sections_5_6_known_equicorrelation_step_down\": {\n    \"rho\"\
    : 0.5,\n    \"alpha\": 0.2,\n    \"lambda_full_known\": 0.361178,\n    \"lambda_oracle_known\"\
    : 0.495548,\n    \"empirical_jer_simes\": 0.085,\n    \"empirical_jer_single_step\"\
    : 0.135,\n    \"empirical_jer_step_down\": 0.1817,\n    \"empirical_jer_oracle\"\
    : 0.1817,\n    \"mean_true_discovery_bound_simes\": 13.0017,\n    \"mean_true_discovery_bound_step_down\"\
    : 14.7567\n  },\n  \"section_5_4_unknown_dependence_sign_flipping\": {\n    \"\
    B_flips\": 99,\n    \"alpha\": 0.2,\n    \"empirical_jer_single_step\": 0.0333,\n\
    \    \"empirical_jer_step_down\": 0.1667\n  },\n  \"section_7_detection_boundary\"\
    : {\n    \"beta\": 0.6,\n    \"rho_star_balanced_hc\": 0.1,\n    \"rho_star_linear_bh\"\
    : 0.135089,\n    \"sparse_weak_r\": 0.115\n  },\n  \"all_assertions_passed\":\
    \ true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T165500Z-reference-family-jer-post-hoc-confidence-bounds.json
  accessed_at: '2026-10-17T16:55:00Z'
  support: supports
  summary: No normalized identity match for reference-family joint error rate post
    hoc confidence bounds across 442 pinned AIO records and 602 maintained IDs, names,
    aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T16:55:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides
    frequentist post-selection and multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/reference-family-jer-post-hoc-confidence-bounds-boundaries.py
  accessed_at: '2026-10-17T16:55:00Z'
  snapshot_sha256: ec2e60196e1983f307f7b7d68813a31deb5c5d1b1a3dcbcdd5def3b95ddabf74
  support: supports
  summary: 'Constructed numerical checks verify (1) Section 2 and Section 8 structural
    properties: triangle-graph NP-hardness gap V^* = 1 < V_bar = 2, self-consistency
    idempotence across all 32 subsets, nested exactness V_bar = V^* and Goeman-Solari
    shortcut equivalence across all 64 subsets, and Section 8.4 admissibility, (2)
    Section 4.3 Table 2 exact Beta tail probabilities (k=1: 0.048772, k=5: 6.5525e-06,
    k=100: 5.7919e-93) and Proposition A.1 bounds, and (3) Sections 5-6 single-step
    and step-down JER control under known Gaussian equicorrelation (rho=0.5: JER_Simes=0.085
    < JER_ss=0.135 <= JER_sd=0.1817 <= alpha=0.2) and unknown-dependence sign-flipping
    (B=99: JER_sd=0.1667 <= 0.2).'
- evidence_id: bnr2020-v3-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1703.02307
  locator: Pages 1-29, Sections 1-8 and Appendix A (Propositions 2.1, 2.3, 2.4, 2.5,
    Conditions LeastFavor and Rand, Theorem 4.1, Tables 1-2, Definitions 5.1, 5.3,
    Lemma 5.2, Propositions 5.4-5.5, Algorithm 1, Theorems 5.7-5.8, Remarks 6.1-6.2)
  accessed_at: '2026-10-17T16:55:00Z'
  snapshot_sha256: 7711fc4b689e9da4ca76ffdbfeccb130e36699388750c5462eea515c217e76fd
  support: supports
  summary: All 29 pages of the full-text PDF of arXiv:1703.02307v3 read. Checked all
    definitions, propositions, theorems, algorithms, tables, and proofs.
- evidence_id: bnr2020-v2-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1703.02307v2
  locator: Pages 1-34, Sections 1-9 and Appendices A-D (Propositions 2.1-2.4, Theorems
    7.2-7.3, Lemmas 8.1-8.2, Proposition A.1, Lemmas A.2-A.3)
  accessed_at: '2026-10-17T16:55:00Z'
  snapshot_sha256: a14025460c2029ca6a87db880df41694deedf2b0bd094484556af0bfed8c47fe
  support: supports
  summary: All 34 pages of the full-text PDF of arXiv:1703.02307v2 read, including
    complete appendices and proofs.
- evidence_id: bnr2020-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/19-AOS1847
  locator: The Annals of Statistics 48(3):1281-1303 publication record
  accessed_at: '2026-10-17T16:55:00Z'
  snapshot_sha256: 2420271bd9a536d5a923b1a51b43ae3c50cda9466779861d2471559cc1293aac
  support: supports
  summary: Official The Annals of Statistics 48(3):1281-1303 Crossref record read
    and verified.
- evidence_id: bnr2020-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1703.02307
  locator: arXiv:1703.02307v3 abstract and metadata
  accessed_at: '2026-10-17T16:55:00Z'
  snapshot_sha256: 91c73d6251c4e1fe1adbf725bb47621e3bc55c372e4ef49b3d4494d1de0bab65
  support: supports
  summary: arXiv:1703.02307v3 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ReferenceFamilyJERPostHocConfidenceBounds versus SimultaneousPathwiseFalseDiscoveryProportionBounds
    and HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - identity
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - bnr2020-crossref
  summary: Retain Reference-family joint error rate post hoc confidence bounds as
    a distinct DRAFT mathematical_method.
  details: ReferenceFamilyJERPostHocConfidenceBounds defines user-agnostic post hoc
    confidence bounds V^*_{R_ref}(R) and V_bar_{R_ref}(R) valid simultaneously over
    all 2^m subsets R subset N_m via reference-family JER control, single-step and
    step-down lambda-calibration under LeastFavor and Rand, Goeman-Solari closed-testing
    equivalence, and Higher Criticism detection optimality.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - mapping
  - bnr2020-v3-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Reference-family JER post hoc confidence bounds prevent post-selection
    data-snooping invalidation (AIO:DataDredgingBias).
- assessment_id: reference-family-jer-interpolation-equivalence-np-hardness-and-nested-optimality
  area: evidence
  topic: reference-family-jer-interpolation-equivalence-np-hardness-and-nested-optimality
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - bnr2020-crossref
  - calculation
  summary: Supported by Section 2.2-2.3 (Propositions 2.1, 2.3, 2.4, 2.5 in v3; Propositions
    2.1-2.4 and Appendix B.1 in v2) and Section 8.4.
  details: Verified event equivalence, triangle-graph NP-hardness gap V^* = 1 < V_bar
    = 2, self-consistency idempotence, nested exactness V_bar = V^*, and Section 8.4
    admissibility.
- assessment_id: closed-testing-specialization-simes-shortcut-equivalence-and-unbalancedness
  area: evidence
  topic: closed-testing-specialization-simes-shortcut-equivalence-and-unbalancedness
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - bnr2020-abs
  - calculation
  summary: Supported by Section 4.1-4.3 (Theorem 4.1, Tables 1-2 in v3), Section 8.1-8.3
    (Lemmas 8.1-8.2 in v2), and Appendix A.1 (Proposition A.1(iv)).
  details: Verified exact algebraic identity V_bar_{R_ref}(R) = V_bar^{GS}_alpha(R)
    across all 64 subsets and exact Table 2 Beta tail probabilities.
- assessment_id: threshold-templates-and-single-step-and-step-down-lambda-calibration
  area: evidence
  topic: threshold-templates-and-single-step-and-step-down-lambda-calibration
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - calculation
  summary: Supported by Section 3.2, Section 5.1-5.4 (Definitions 5.1, 5.3, Lemma
    5.2, Propositions 5.4-5.5, Algorithm 1, Theorems 5.7-5.8), and Appendix A in v3.
  details: Verified single-step and step-down JER control under both known Gaussian
    equicorrelation (Theorem 5.7) and unknown-dependence sign-flipping (Theorem 5.8).
- assessment_id: linear-vs-balanced-template-asymptotic-conservativeness-and-higher-criticism-detection-optimality
  area: evidence
  topic: linear-vs-balanced-template-asymptotic-conservativeness-and-higher-criticism-detection-optimality
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - calculation
  summary: Supported by Section 6.1-6.2 in v3 and Section 5.1-5.3, Section 7.1-7.3
    (Theorems 7.2-7.3), Appendix A.1-A.2 (Proposition A.1, Lemmas A.2-A.3), and Appendix
    B.2-B.3 in v2.
  details: Verified Proposition A.1 Beta quantile bounds, O((log m)^{-1/8}) single-step
    balanced JER decay under pi_0 < 1, and Higher Criticism detection boundary rho^*(beta)
    vs. BH detection boundary.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ReferenceFamilyJERPostHocConfidenceBounds
  evidence_ids:
  - identity
  - mapping
  - bnr2020-v3-pdf
  - bnr2020-v2-pdf
  - bnr2020-crossref
  - bnr2020-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ReferenceFamilyJERPostHocConfidenceBounds.yaml: stable
    ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, four primary sources with exact SHA-256
    digests, pinned AIO mappings and rationales, four scoped limitations, and UTC
    curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Reference-family joint error rate post hoc confidence bounds record,
  yielding 603 native and 442 unchanged generated records.
- All 29 PDF pages of arXiv:1703.02307v3 and all 34 PDF pages of arXiv:1703.02307v2
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- post-hoc-inference
- joint-error-rate
- reference-families
- self-review
- discovery-ongoing
```
