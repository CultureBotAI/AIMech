# Scientific author self-review of Selectively traversed accumulation rules for structured false discovery rate control

- Review: 20261017T143700Z-selectively-traversed-accumulation-rules-for-structured-fdr-control
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T14:35:00Z
- Finished UTC: 2026-10-17T14:37:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Selectively traversed accumulation rules for structured false discovery rate control as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Lei, Ramdas, &amp; Fithian (2021 Biometrika 108(2):253-267) are supported with explicit null-independence, F_t-measurability, minimum-rejection-size, and no-look-back limitations.

## Scope And Provenance

All fields of the exact maintained SelectivelyTraversedAccumulationRulesForStructuredFDRControl record and its primary evidence.

Selection: Exact maintained ID: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f9deead5a4017fa32ca003f785dd9b576ee52526.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml | maintained | Selectively traversed accumulation rules for structured false discovery rate control |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | All 587 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | Exited 0 without output. |
| Constructed selectively traversed accumulation rules for structured FDR control checks | passed | True | AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl | {<br>  "claim1_accumulation_masking_and_prop21": {<br>    "forwardstop_max_H_inversion_err": 0.0,<br>    "seqstep_max_H_symmetry_err": 0.0,<br>    "seqstep_max_unif_cond_exp_err": 0.0,<br>    "seqstep_min_beta21_cond_exp": 1.155556<br>  },<br>  "claim2_tree_heredity_fdr_and_bottom_up_power": {<br>    "bh_subtree_constraint_valid_rate": 0.0,<br>    "fdr_star_tree": 0.049024,<br>    "power_star_bottom_up": 0.839,<br>    "power_topdown_hierarchical": 0.271,<br>    "star_subtree_constraint_valid_rate": 1.0<br>  },<br>  "claim3_one_group_em_and_structured_knockoffs": {<br>    "em_vs_oracle_initial_corr": 0.971733,<br>    "fdr_em_convex_interval": 0.067853,<br>    "fdr_structured_knockoffs": 0.050822,<br>    "power_canonical_convex_interval": 0.864286,<br>    "power_em_convex_interval": 0.965476,<br>    "power_structured_knockoffs": 0.783333<br>  },<br>  "claim4_asymptotic_power_and_small_alpha_boundary": {<br>    "fdr_filtration_violating_peeking_global_null": 1.0,<br>    "min_rejections_alpha_0_10_pstar_0_20": 12,<br>    "min_rejections_alpha_0_10_pstar_0_50": 19,<br>    "plain_accumulation_critical_pi1": 0.804109,<br>    "power_masked_star_uninformative_order": 0.819583,<br>    "power_plain_accumulation_uninformative_order": 0.0<br>  }<br>} |

## Scientific And Domain Assessments

### SelectivelyTraversedAccumulationRulesForStructuredFDRControl versus AdaptivePValueThresholding, FocusedBH, and SimultaneousPathwiseFalseDiscoveryProportionBounds

identity: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Retain Selectively traversed accumulation rules for structured false discovery rate control as a distinct DRAFT mathematical_method.

SelectivelyTraversedAccumulationRulesForStructuredFDRControl pairs general bounded accumulation functions h(p) with reflection maps s(p) via H(s(p)) = H(p) (Theorem 2.5) and interactively peels structured candidate sets R_t in K using F_t-measurable one-group EM or human-in-the-loop rules (Algorithm 2.1, Theorem 2.3), whereas AdaptivePValueThresholding adapts unconstrained coordinatewise p-value thresholds via two-group EM, FocusedBH filters unmasked p-values upfront and calibrates a single scalar threshold via permutation simulation, and SimultaneousPathwiseFalseDiscoveryProportionBounds constructs simultaneous high-probability upper envelopes across fixed nested paths.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Related mapping to DataDredgingBias is supported.

STAR prevents post-hoc selection and data-dredging bias during interactive hypothesis exploration under structural constraints by restricting peeling decisions to the masked filtration F_t (AIO:DataDredgingBias).

### integral-reflection-accumulation-masking-pairing-and-monotone-null-supermartingale-property

evidence: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Supported by Section 2.1 Proposition 2.1, Section 2.3 Theorem 2.5, Equation 5, and Appendices A.1, A.3, B.3.

Verified Theorem 2.5 H(s(p)) = H(p) symmetry (max error 0.0 for SeqStep and 0.0 for truncated ForwardStop), Uniform(0,1) conditional expectation E[h(p)&#124;g(p)] = 1 (max error 0.0), and Proposition 2.1 conservative Beta(2,1) lower bound (min E[h(p)&#124;g(p)] = 1.155556 &gt;= 1).

### interactive-filtration-peeling-optional-stopping-fdr-control-under-hard-structural-constraints

evidence: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Supported by Section 2.1-2.2 Algorithm 2.1, Theorem 2.3, Section 4, Appendix A.2 Lemma A.4, and Appendix D.

Verified finite-sample FDR control (0.049024 &lt;= 0.20) with 100% rooted-subtree constraint satisfaction (1.0 vs. standard BH 0.0) and bottom-up leaf peeling power gain over top-down hierarchical testing (0.839 vs. 0.271).

### model-assisted-one-group-em-peeling-scores-and-structured-knockoff-variable-selection

evidence: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Supported by Section 3.2, Section 4-6, and Appendix B.4 Equations 17-18, Examples 1-2.

Verified one-group EM score correlation with oracle smoother (0.971733), higher spatial convex-interval power than canonical scores (0.965476 vs. 0.864286) with controlled FDR (0.067853 &lt;= 0.15), and structured knockoff FDR control (0.050822 &lt;= 0.15, power 0.783333).

### asymptotic-power-dominance-over-plain-accumulation-tests-and-minimum-rejection-boundary

evidence: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

Supported by Section 2.2, Section 3.1, Section 5.2, and Appendix I.1-I.3 Equations 19-22.

Verified asymptotic power dominance over plain accumulation tests under uninformative ordering (0.819583 vs. 0.0 when pi_1 = 0.25 &lt; 0.804109), minimum rejection floor (19 at p_*=0.5 vs. 12 at p_*=0.2), and filtration-violating peeking failure (global-null FDR = 1.0 &gt; 0.20).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl.

The full record is consistent; retain DRAFT.

Read every field of SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T143500Z-selectively-traversed-accumulation-rules-for-structured-fdr-control.json | supports | No normalized identity match for selectively traversed accumulation rules for structured false discovery rate control across 442 pinned AIO records and 586 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides interactive multiple-testing false-discovery rate control context via related_match. |
| calculation | research/discovery/selectively-traversed-accumulation-rules-for-structured-fdr-control-boundaries.py | supports | Constructed analytical and numerical checks for integral-reflection accumulation-masking pairing (Theorem 2.5) and conservative null expectation bound (Proposition 2.1), interactive filtration peeling FDR control under rooted-tree heredity (Theorem 2.3), one-group EM peeling scores (Appendix B.4) and structured knockoffs (Section 6), and asymptotic power dominance over plain accumulation tests (Appendix I). |
| lei2021-star-structured-fdr-ar5iv | https://ar5iv.labs.arxiv.org/html/1710.02776; Sections 1-6 and Appendices A-I (lines 1-1509, Algorithm 2.1, Proposition 2.1, Theorems 2.3 and 2.5, Equations 1-22) | supports | All 1,509 lines of the full-text ar5iv HTML conversion of arXiv:1710.02776v2 read. Checked all theorems, propositions, lemmas, algorithms, and proofs across Sections 1-6 and Appendices A-I. |
| lei2021-star-structured-fdr-crossref | https://api.crossref.org/works/10.1093/biomet/asaa064; Biometrika Vol. 108, Issue 2, pp. 253-267 publication record | supports | Official Biometrika 108(2):253-267 Crossref record read and verified. |
| lei2021-star-structured-fdr-abs | https://arxiv.org/abs/1710.02776; arXiv:1710.02776v2 abstract and Biometrika 2021 metadata | supports | arXiv:1710.02776v2 abstract and Biometrika 2021 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Selectively traversed accumulation rules for structured false discovery rate control record, yielding 587 native and 442 unchanged generated records.
- All 1,509 lines of Lei, Ramdas, &amp; Fithian (2021, arXiv:1710.02776v2) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T143700Z-selectively-traversed-accumulation-rules-for-structured-fdr-control
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Selectively traversed accumulation rules for
  structured false discovery rate control
started_at: '2026-10-17T14:35:00Z'
finished_at: '2026-10-17T14:37:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from AdaptivePValueThresholding,
    FocusedBH, and SimultaneousPathwiseFalseDiscoveryProportionBounds, the null independence
    and F_t-measurability requirements of Theorem 2.3, the minimum rejection size
    floor ceil(h(1)/alpha - 1) in Section 5.2, and the no-look-back restriction of
    interactive peeling. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Selectively traversed accumulation rules for structured false discovery
  rate control as a distinct DRAFT mathematical_method with a related DataDredgingBias
  mapping. All four claims and locators across Lei, Ramdas, & Fithian (2021 Biometrika
  108(2):253-267) are supported with explicit null-independence, F_t-measurability,
  minimum-rejection-size, and no-look-back limitations.
source:
  git_revision: f9deead5a4017fa32ca003f785dd9b576ee52526
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml
    sha256: 6167290e8178827ea950c80549426c871ba5e2b6d727b42b4a536d860e097946
    role: context
  - path: data/curated/ForkConvexExchangeabilityTestingBySafeEProcesses.yaml
    sha256: 300ea1665bdd8cedfa38746832f1e7d6b85a410eacb4a87ca16eab55ca833370
    role: context
  - path: data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml
    sha256: d701f5a7c2cc640bfc6cfa0d3fd87253f9f6a5f231a80bcaa14901dbf52486a9
    role: target
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T143500Z-selectively-traversed-accumulation-rules-for-structured-fdr-control.json
    sha256: ff0177ca044eccefc0cdbd65cd1f5556f58a579205c9ded566e2f2af8a3945bd
    role: context
  - path: research/discovery/selectively-traversed-accumulation-rules-for-structured-fdr-control-boundaries.py
    sha256: 744b9e21b9908f3caaf31e3db9c1b5deb95d1c587578b6cb799e1e890b7b6ea9
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
- target_id: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  path: data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml
  label: Selectively traversed accumulation rules for structured false discovery rate
    control
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml
    role: maintained
scope:
  description: All fields of the exact maintained SelectivelyTraversedAccumulationRulesForStructuredFDRControl
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
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
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 587 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed selectively traversed accumulation rules for structured FDR control
    checks
  command: python3 research/discovery/selectively-traversed-accumulation-rules-for-structured-fdr-control-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"claim1_accumulation_masking_and_prop21\": {\n    \"forwardstop_max_H_inversion_err\"\
    : 0.0,\n    \"seqstep_max_H_symmetry_err\": 0.0,\n    \"seqstep_max_unif_cond_exp_err\"\
    : 0.0,\n    \"seqstep_min_beta21_cond_exp\": 1.155556\n  },\n  \"claim2_tree_heredity_fdr_and_bottom_up_power\"\
    : {\n    \"bh_subtree_constraint_valid_rate\": 0.0,\n    \"fdr_star_tree\": 0.049024,\n\
    \    \"power_star_bottom_up\": 0.839,\n    \"power_topdown_hierarchical\": 0.271,\n\
    \    \"star_subtree_constraint_valid_rate\": 1.0\n  },\n  \"claim3_one_group_em_and_structured_knockoffs\"\
    : {\n    \"em_vs_oracle_initial_corr\": 0.971733,\n    \"fdr_em_convex_interval\"\
    : 0.067853,\n    \"fdr_structured_knockoffs\": 0.050822,\n    \"power_canonical_convex_interval\"\
    : 0.864286,\n    \"power_em_convex_interval\": 0.965476,\n    \"power_structured_knockoffs\"\
    : 0.783333\n  },\n  \"claim4_asymptotic_power_and_small_alpha_boundary\": {\n\
    \    \"fdr_filtration_violating_peeking_global_null\": 1.0,\n    \"min_rejections_alpha_0_10_pstar_0_20\"\
    : 12,\n    \"min_rejections_alpha_0_10_pstar_0_50\": 19,\n    \"plain_accumulation_critical_pi1\"\
    : 0.804109,\n    \"power_masked_star_uninformative_order\": 0.819583,\n    \"\
    power_plain_accumulation_uninformative_order\": 0.0\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T143500Z-selectively-traversed-accumulation-rules-for-structured-fdr-control.json
  accessed_at: '2026-10-17T14:35:00Z'
  support: supports
  summary: No normalized identity match for selectively traversed accumulation rules
    for structured false discovery rate control across 442 pinned AIO records and
    586 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T14:35:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides interactive multiple-testing false-discovery rate control context via
    related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/selectively-traversed-accumulation-rules-for-structured-fdr-control-boundaries.py
  accessed_at: '2026-10-17T14:35:00Z'
  snapshot_sha256: 744b9e21b9908f3caaf31e3db9c1b5deb95d1c587578b6cb799e1e890b7b6ea9
  support: supports
  summary: Constructed analytical and numerical checks for integral-reflection accumulation-masking
    pairing (Theorem 2.5) and conservative null expectation bound (Proposition 2.1),
    interactive filtration peeling FDR control under rooted-tree heredity (Theorem
    2.3), one-group EM peeling scores (Appendix B.4) and structured knockoffs (Section
    6), and asymptotic power dominance over plain accumulation tests (Appendix I).
- evidence_id: lei2021-star-structured-fdr-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1710.02776
  locator: Sections 1-6 and Appendices A-I (lines 1-1509, Algorithm 2.1, Proposition
    2.1, Theorems 2.3 and 2.5, Equations 1-22)
  accessed_at: '2026-10-17T14:35:00Z'
  snapshot_sha256: 0aca9bd13ad69478f54a7497ca753df3b5b0fc7304c8304e0e8287292dbb76fa
  support: supports
  summary: All 1,509 lines of the full-text ar5iv HTML conversion of arXiv:1710.02776v2
    read. Checked all theorems, propositions, lemmas, algorithms, and proofs across
    Sections 1-6 and Appendices A-I.
- evidence_id: lei2021-star-structured-fdr-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1093/biomet/asaa064
  locator: Biometrika Vol. 108, Issue 2, pp. 253-267 publication record
  accessed_at: '2026-10-17T14:35:00Z'
  snapshot_sha256: f2e31895442898d6f0b6b6cdf46fc6bce259ed9304652a2694f7ba10d70c65ba
  support: supports
  summary: Official Biometrika 108(2):253-267 Crossref record read and verified.
- evidence_id: lei2021-star-structured-fdr-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1710.02776
  locator: arXiv:1710.02776v2 abstract and Biometrika 2021 metadata
  accessed_at: '2026-10-17T14:35:00Z'
  snapshot_sha256: 64ad42aee0a91894f831dc3d3206c4009c4a8eca793a8ae966c3876770962de2
  support: supports
  summary: arXiv:1710.02776v2 abstract and Biometrika 2021 metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: SelectivelyTraversedAccumulationRulesForStructuredFDRControl versus AdaptivePValueThresholding,
    FocusedBH, and SimultaneousPathwiseFalseDiscoveryProportionBounds
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - identity
  - lei2021-star-structured-fdr-ar5iv
  - lei2021-star-structured-fdr-crossref
  summary: Retain Selectively traversed accumulation rules for structured false discovery
    rate control as a distinct DRAFT mathematical_method.
  details: SelectivelyTraversedAccumulationRulesForStructuredFDRControl pairs general
    bounded accumulation functions h(p) with reflection maps s(p) via H(s(p)) = H(p)
    (Theorem 2.5) and interactively peels structured candidate sets R_t in K using
    F_t-measurable one-group EM or human-in-the-loop rules (Algorithm 2.1, Theorem
    2.3), whereas AdaptivePValueThresholding adapts unconstrained coordinatewise p-value
    thresholds via two-group EM, FocusedBH filters unmasked p-values upfront and calibrates
    a single scalar threshold via permutation simulation, and SimultaneousPathwiseFalseDiscoveryProportionBounds
    constructs simultaneous high-probability upper envelopes across fixed nested paths.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - mapping
  - lei2021-star-structured-fdr-ar5iv
  summary: Related mapping to DataDredgingBias is supported.
  details: STAR prevents post-hoc selection and data-dredging bias during interactive
    hypothesis exploration under structural constraints by restricting peeling decisions
    to the masked filtration F_t (AIO:DataDredgingBias).
- assessment_id: integral-reflection-accumulation-masking-pairing-and-monotone-null-supermartingale-property
  area: evidence
  topic: integral-reflection-accumulation-masking-pairing-and-monotone-null-supermartingale-property
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - lei2021-star-structured-fdr-ar5iv
  - lei2021-star-structured-fdr-abs
  - calculation
  summary: Supported by Section 2.1 Proposition 2.1, Section 2.3 Theorem 2.5, Equation
    5, and Appendices A.1, A.3, B.3.
  details: Verified Theorem 2.5 H(s(p)) = H(p) symmetry (max error 0.0 for SeqStep
    and 0.0 for truncated ForwardStop), Uniform(0,1) conditional expectation E[h(p)|g(p)]
    = 1 (max error 0.0), and Proposition 2.1 conservative Beta(2,1) lower bound (min
    E[h(p)|g(p)] = 1.155556 >= 1).
- assessment_id: interactive-filtration-peeling-optional-stopping-fdr-control-under-hard-structural-constraints
  area: evidence
  topic: interactive-filtration-peeling-optional-stopping-fdr-control-under-hard-structural-constraints
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - lei2021-star-structured-fdr-ar5iv
  - lei2021-star-structured-fdr-crossref
  - calculation
  summary: Supported by Section 2.1-2.2 Algorithm 2.1, Theorem 2.3, Section 4, Appendix
    A.2 Lemma A.4, and Appendix D.
  details: Verified finite-sample FDR control (0.049024 <= 0.20) with 100% rooted-subtree
    constraint satisfaction (1.0 vs. standard BH 0.0) and bottom-up leaf peeling power
    gain over top-down hierarchical testing (0.839 vs. 0.271).
- assessment_id: model-assisted-one-group-em-peeling-scores-and-structured-knockoff-variable-selection
  area: evidence
  topic: model-assisted-one-group-em-peeling-scores-and-structured-knockoff-variable-selection
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - lei2021-star-structured-fdr-ar5iv
  - calculation
  summary: Supported by Section 3.2, Section 4-6, and Appendix B.4 Equations 17-18,
    Examples 1-2.
  details: Verified one-group EM score correlation with oracle smoother (0.971733),
    higher spatial convex-interval power than canonical scores (0.965476 vs. 0.864286)
    with controlled FDR (0.067853 <= 0.15), and structured knockoff FDR control (0.050822
    <= 0.15, power 0.783333).
- assessment_id: asymptotic-power-dominance-over-plain-accumulation-tests-and-minimum-rejection-boundary
  area: evidence
  topic: asymptotic-power-dominance-over-plain-accumulation-tests-and-minimum-rejection-boundary
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - lei2021-star-structured-fdr-ar5iv
  - calculation
  summary: Supported by Section 2.2, Section 3.1, Section 5.2, and Appendix I.1-I.3
    Equations 19-22.
  details: Verified asymptotic power dominance over plain accumulation tests under
    uninformative ordering (0.819583 vs. 0.0 when pi_1 = 0.25 < 0.804109), minimum
    rejection floor (19 at p_*=0.5 vs. 12 at p_*=0.2), and filtration-violating peeking
    failure (global-null FDR = 1.0 > 0.20).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl
  evidence_ids:
  - identity
  - mapping
  - lei2021-star-structured-fdr-ar5iv
  - lei2021-star-structured-fdr-crossref
  - lei2021-star-structured-fdr-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Selectively traversed accumulation rules for structured false discovery
  rate control record, yielding 587 native and 442 unchanged generated records.
- All 1,509 lines of Lei, Ramdas, & Fithian (2021, arXiv:1710.02776v2) were read in
  full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- interactive-testing
- structural-constraints
- accumulation-tests
- self-review
- discovery-ongoing
```
