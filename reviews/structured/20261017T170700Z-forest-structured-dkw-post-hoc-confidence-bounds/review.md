# Scientific author self-review of Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds

- Review: 20261017T170700Z-forest-structured-dkw-post-hoc-confidence-bounds
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T17:05:00Z
- Finished UTC: 2026-10-17T17:07:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Durand, Blanchard, Neuvial, &amp; Roquain (2020, Scandinavian Journal of Statistics 47(4):1114-1148, arXiv:1807.01470v2) are supported with explicit non-forest strict gap (Example 2.2), within-region independence and floor(log(K/alpha)/2) minimum cost limitations, and primary-source typographical notes.

## Scope And Provenance

All fields of the exact maintained ForestStructuredDKWPostHocConfidenceBounds record and its primary evidence.

Selection: Exact maintained ID: AIMech:ForestStructuredDKWPostHocConfidenceBounds
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 50ccefe5d67f47e5ec7f38eedc079ffd319d8d42.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ForestStructuredDKWPostHocConfidenceBounds | data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml | maintained | Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | All 604 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | Exited 0 without output. |
| Constructed Durand-Blanchard-Neuvial-Roquain 2020 forest interpolation, Algorithm 1 bottom-up tree DP, local DKW-Massart calibration, Figure 6 ratio bounds, and Simes-DKW hybrid envelope checks | passed | True | AIMech:ForestStructuredDKWPostHocConfidenceBounds | {<br>  "concept_id": "AIMech:ForestStructuredDKWPostHocConfidenceBounds",<br>  "primary_source": "Durand, Blanchard, Neuvial, &amp; Roquain (2020), Scandinavian Journal of Statistics 47(4):1114-1148 (arXiv:1807.01470v2, DOI:10.1111/sjos.12453)",<br>  "section_2_and_3_forest_interpolation_and_algorithm_1": {<br>    "example_2_2_non_forest_gap": {<br>      "v_star": 1,<br>      "v_tilde": 2,<br>      "v_bar": 2<br>    },<br>    "example_3_2_forest": {<br>      "depths": [<br>        1,<br>        2,<br>        2,<br>        2,<br>        3,<br>        3,<br>        3,<br>        1,<br>        2<br>      ],<br>      "num_atoms": 8,<br>      "max_disjoint_d": 5,<br>      "v_alg1_full_query": 13,<br>      "v_tilde_d_full_query": 13,<br>      "v_bar_full_query": 15<br>    },<br>    "small_forest_exhaustive_verification": {<br>      "verified_subsets": 256,<br>      "strict_gains_over_vbar": 62<br>    }<br>  },<br>  "section_4_and_5_dkw_calibration_figure_6_and_hybrid": {<br>    "empirical_jer_tree": 0.025,<br>    "empirical_jer_part": 0.035,<br>    "gw_dominance_checks": 3000,<br>    "strict_gw_improvements": 965,<br>    "figure_6_ratio_upper_bounds": {<br>      "0.5": 0.808293,<br>      "1.0": 0.631146,<br>      "1.75": 0.502728,<br>      "2.0": 0.492103,<br>      "3.0": 0.566919,<br>      "4.0": 0.798229,<br>      "5.0": 1.022236<br>    },<br>    "hybrid_envelope_comparison": {<br>      "small_k_10": {<br>        "v_simes": 0,<br>        "v_tree": 10,<br>        "v_hybrid": 0<br>      },<br>      "large_k_200": {<br>        "v_simes": 145,<br>        "v_tree": 71,<br>        "v_hybrid": 71<br>      }<br>    }<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### ForestStructuredDKWPostHocConfidenceBounds versus ReferenceFamilyJERPostHocConfidenceBounds and SimultaneousPathwiseFalseDiscoveryProportionBounds

identity: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Retain Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds as a distinct DRAFT mathematical_method.

ForestStructuredDKWPostHocConfidenceBounds defines multi-subset interpolation V_tilde^q_{R_ref}(S), proves exact optimality V^*_{R_ref}(S) = V_tilde_{R_ref}(S) = V_tilde^d_{R_ref}(S) on deterministic forest-structured reference families with O(Hm) bottom-up tree dynamic programming (Theorem 3.6, Algorithm 1), calibrates random local capacities zeta_k(X) via quadratic inversion of the Massart-DKW inequality (Proposition 4.1), proves the asymptotic 1 - r localized-signal improvement over Simes/Bonferroni (Proposition 4.5, Corollary 4.6), and introduces the Simes-DKW hybrid envelope V^gamma_{hybrid}(alpha, S).

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Related mapping to DataDredgingBias is supported.

Forest-structured DKW post hoc confidence bounds prevent post-selection data-snooping invalidation across all 2^m selected subsets (AIO:DataDredgingBias).

### multi-subset-interpolation-hierarchy-and-forest-exactness-theorem

evidence: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Supported by Section 2.3 (Lemma 2.1, Example 2.2), Section 3.1-3.2 (Definition 3.1, Lemma 3.3, Definition 3.5, Theorem 3.6, Corollary 3.7), Section 7.1-7.3, and Appendices A-B.

Verified Example 2.2 non-forest gap V^* = 1 &lt; V_tilde = 2, Algorithm 2 atomic decomposition, and Theorem 3.6 exact equality across all 256 subsets of an 8-element forest and on the 25-element forest of Example 3.2.

### bottom-up-dynamic-programming-algorithm-on-completed-forest

evidence: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Supported by Section 3.2 (Algorithm 1, Figures 4-5), Section 7.2.1, and Lemma A.2.

Verified that Algorithm 1 bottom-up recursion over the level partitions K^h of R_ref^oplus matches V^*_{R_ref}(S) and V_tilde^d_{R_ref}(S) exactly.

### local-dkw-massart-quadratic-inversion-calibration-and-gw-dominance

evidence: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Supported by Section 4.1 (Proposition 4.1, Remarks 4.2-4.4), Section 7.4 (Equation 32), and Appendix A (Lemma A.1, Equation 33).

Verified empirical JER control &lt;= alpha and strict dominance zeta_k(X) &lt;= zeta^{GW}_k(X) across 3,000 region-trials.

### localized-signal-asymptotic-improvement-and-simes-dkw-hybrid-envelope

evidence: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

Supported by Section 4.2 (Proposition 4.5, Figure 6, Corollary 4.6), Section 5.1-5.3 (Figures 7-10), and Section 7.5.

Verified Equation (23) Figure 6 ratio upper bounds and Section 5.3 Simes-DKW hybrid envelope complementarity at k = 10 and k = 200.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ForestStructuredDKWPostHocConfidenceBounds.

The full record is consistent; retain DRAFT.

Read every field of ForestStructuredDKWPostHocConfidenceBounds.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T170500Z-forest-structured-dkw-post-hoc-confidence-bounds.json | supports | No normalized identity match for forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds across 442 pinned AIO records and 603 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides frequentist post-selection and multiplicity error-control context via related_match. |
| calculation | research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py | supports | Executed pure-Python verification in research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py (SHA-256 33e506cbe878afedd9ef5e25ea394b6b744fe7bb06f6cc10f516135b5c1cf852): (1) Section 2.3 &amp; Section 3 Forest Interpolation &amp; Algorithm 1: verified Example 2.2 non-forest gap V^* = 1 &lt; V_tilde = 2, Example 3.2/3.4 depths [1, 2, 2, 2, 3, 3, 3, 1, 2], Algorithm 2 atomic partition (8 atoms), max disjoint count d = 5, and Algorithm 1 == V_tilde_R == V_tilde^d_R = 13 &lt; V_bar_R = 15, plus exhaustive verification across all 256 subsets of an 8-element forest (strict improvement over V_bar on 62 subsets). (2) Section 4.1 &amp; Remark 4.3 Local DKW-Massart Calibration: verified zeta_k(X) &lt;= zeta^{GW}_k(X) across 3000 region-trials (strict improvement on 965 region-trials) and empirical JER 0.025 (tree) and 0.035 (partition) &lt;= alpha = 0.05. (3) Section 4.2 Figure 6 &amp; Section 5.3 Hybrid Envelope: verified Equation (23) ratio trough 0.492103 at mu = 2.0 and crossing 0.798229 at mu = 4.0, and verified hybrid bound complementarity V^{0.02}_{hybrid}(0.05, S_10) = 0 (matching Simes 0 vs tree 10) and V^{0.02}_{hybrid}(0.05, S_200) = 71 (matching tree 71 vs Simes 145). |
| durand2020-pdf | https://arxiv.org/pdf/1807.01470; Pages 1-24, Sections 1-7 and Appendices A-B (Lemma 2.1, Example 2.2, Definition 3.1, Example 3.2, Lemma 3.3, Example 3.4, Definition 3.5, Theorem 3.6, Corollary 3.7, Algorithm 1, Proposition 4.1, Remarks 4.2-4.4, Proposition 4.5, Corollary 4.6, Figures 1-10, Lemmas A.1-A.4, Algorithm 2) | supports | All 24 pages of the full-text PDF of arXiv:1807.01470v2 read. Checked all definitions, lemmas, propositions, theorems, algorithms, figures, and proofs. |
| durand2020-crossref | https://api.crossref.org/works/10.1111/sjos.12453; Scandinavian Journal of Statistics 47(4):1114-1148 publication record | supports | Official Scandinavian Journal of Statistics 47(4):1114-1148 Crossref record read and verified. |
| durand2020-abs | https://arxiv.org/abs/1807.01470; arXiv:1807.01470v2 abstract and metadata | supports | arXiv:1807.01470v2 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds record, yielding 604 native and 442 unchanged generated records.
- All 24 PDF pages of arXiv:1807.01470v2 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T170700Z-forest-structured-dkw-post-hoc-confidence-bounds
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Forest-structured Dvoretzky-Kiefer-Wolfowitz
  post hoc confidence bounds
started_at: '2026-10-17T17:05:00Z'
finished_at: '2026-10-17T17:07:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ReferenceFamilyJERPostHocConfidenceBounds
    (Blanchard, Neuvial, & Roquain 2020) and SimultaneousPathwiseFalseDiscoveryProportionBounds
    (Katsevich & Ramdas 2020), verified the Example 2.2 non-forest gap V^* = 1 < V_tilde
    = 2, verified Algorithm 2 atomic decomposition and Theorem 3.6 / Algorithm 1 exactness
    across all 256 subsets of an 8-element forest and on the 25-element forest of
    Example 3.2, verified Proposition 4.1 JER control and Remark 4.3 / Lemma A.1 strict
    dominance over Genovese-Wasserman (2004) across 3,000 region-trials, verified
    Proposition 4.5 / Figure 6 localized-signal ratio bounds and Section 5.3 Simes-DKW
    hybrid bounds, and documented four typographical slips in arXiv:1807.01470v2 (pp.
    4, 9, 12, 15). This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds
  as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All
  four claims and locators across Durand, Blanchard, Neuvial, & Roquain (2020, Scandinavian
  Journal of Statistics 47(4):1114-1148, arXiv:1807.01470v2) are supported with explicit
  non-forest strict gap (Example 2.2), within-region independence and floor(log(K/alpha)/2)
  minimum cost limitations, and primary-source typographical notes.
source:
  git_revision: 50ccefe5d67f47e5ec7f38eedc079ffd319d8d42
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml
    sha256: 9bae8e3738defe08500250ea05b7669885f8434e0ac0413058d9c332be8fa29f
    role: target
  - path: data/curated/HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality.yaml
    sha256: 6e35c0df6b71a10d35d4bfc2b25558014c91114141256210ef1fa9d1a78424c4
    role: context
  - path: data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml
    sha256: 7e0edec4d6cecc10454f8004806f7bc4b178af9a5daa540242f1771d387050eb
    role: context
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T170500Z-forest-structured-dkw-post-hoc-confidence-bounds.json
    sha256: a0a24b6c8b1983da85869c3fc627ec83c8e56bfddca3d749c239771ad12519d4
    role: context
  - path: research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py
    sha256: 33e506cbe878afedd9ef5e25ea394b6b744fe7bb06f6cc10f516135b5c1cf852
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
- target_id: AIMech:ForestStructuredDKWPostHocConfidenceBounds
  path: data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml
  label: Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence bounds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ForestStructuredDKWPostHocConfidenceBounds
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ForestStructuredDKWPostHocConfidenceBounds'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
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
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 604 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Durand-Blanchard-Neuvial-Roquain 2020 forest interpolation, Algorithm
    1 bottom-up tree DP, local DKW-Massart calibration, Figure 6 ratio bounds, and
    Simes-DKW hybrid envelope checks
  command: python3 research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:ForestStructuredDKWPostHocConfidenceBounds\"\
    ,\n  \"primary_source\": \"Durand, Blanchard, Neuvial, & Roquain (2020), Scandinavian\
    \ Journal of Statistics 47(4):1114-1148 (arXiv:1807.01470v2, DOI:10.1111/sjos.12453)\"\
    ,\n  \"section_2_and_3_forest_interpolation_and_algorithm_1\": {\n    \"example_2_2_non_forest_gap\"\
    : {\n      \"v_star\": 1,\n      \"v_tilde\": 2,\n      \"v_bar\": 2\n    },\n\
    \    \"example_3_2_forest\": {\n      \"depths\": [\n        1,\n        2,\n\
    \        2,\n        2,\n        3,\n        3,\n        3,\n        1,\n    \
    \    2\n      ],\n      \"num_atoms\": 8,\n      \"max_disjoint_d\": 5,\n    \
    \  \"v_alg1_full_query\": 13,\n      \"v_tilde_d_full_query\": 13,\n      \"v_bar_full_query\"\
    : 15\n    },\n    \"small_forest_exhaustive_verification\": {\n      \"verified_subsets\"\
    : 256,\n      \"strict_gains_over_vbar\": 62\n    }\n  },\n  \"section_4_and_5_dkw_calibration_figure_6_and_hybrid\"\
    : {\n    \"empirical_jer_tree\": 0.025,\n    \"empirical_jer_part\": 0.035,\n\
    \    \"gw_dominance_checks\": 3000,\n    \"strict_gw_improvements\": 965,\n  \
    \  \"figure_6_ratio_upper_bounds\": {\n      \"0.5\": 0.808293,\n      \"1.0\"\
    : 0.631146,\n      \"1.75\": 0.502728,\n      \"2.0\": 0.492103,\n      \"3.0\"\
    : 0.566919,\n      \"4.0\": 0.798229,\n      \"5.0\": 1.022236\n    },\n    \"\
    hybrid_envelope_comparison\": {\n      \"small_k_10\": {\n        \"v_simes\"\
    : 0,\n        \"v_tree\": 10,\n        \"v_hybrid\": 0\n      },\n      \"large_k_200\"\
    : {\n        \"v_simes\": 145,\n        \"v_tree\": 71,\n        \"v_hybrid\"\
    : 71\n      }\n    }\n  },\n  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T170500Z-forest-structured-dkw-post-hoc-confidence-bounds.json
  accessed_at: '2026-10-17T17:05:00Z'
  support: supports
  summary: No normalized identity match for forest-structured Dvoretzky-Kiefer-Wolfowitz
    post hoc confidence bounds across 442 pinned AIO records and 603 maintained IDs,
    names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T17:05:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides
    frequentist post-selection and multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py
  accessed_at: '2026-10-17T17:05:00Z'
  snapshot_sha256: 33e506cbe878afedd9ef5e25ea394b6b744fe7bb06f6cc10f516135b5c1cf852
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/forest-structured-dkw-post-hoc-confidence-bounds-boundaries.py
    (SHA-256 33e506cbe878afedd9ef5e25ea394b6b744fe7bb06f6cc10f516135b5c1cf852): (1)
    Section 2.3 & Section 3 Forest Interpolation & Algorithm 1: verified Example 2.2
    non-forest gap V^* = 1 < V_tilde = 2, Example 3.2/3.4 depths [1, 2, 2, 2, 3, 3,
    3, 1, 2], Algorithm 2 atomic partition (8 atoms), max disjoint count d = 5, and
    Algorithm 1 == V_tilde_R == V_tilde^d_R = 13 < V_bar_R = 15, plus exhaustive verification
    across all 256 subsets of an 8-element forest (strict improvement over V_bar on
    62 subsets). (2) Section 4.1 & Remark 4.3 Local DKW-Massart Calibration: verified
    zeta_k(X) <= zeta^{GW}_k(X) across 3000 region-trials (strict improvement on 965
    region-trials) and empirical JER 0.025 (tree) and 0.035 (partition) <= alpha =
    0.05. (3) Section 4.2 Figure 6 & Section 5.3 Hybrid Envelope: verified Equation
    (23) ratio trough 0.492103 at mu = 2.0 and crossing 0.798229 at mu = 4.0, and
    verified hybrid bound complementarity V^{0.02}_{hybrid}(0.05, S_10) = 0 (matching
    Simes 0 vs tree 10) and V^{0.02}_{hybrid}(0.05, S_200) = 71 (matching tree 71
    vs Simes 145).'
- evidence_id: durand2020-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1807.01470
  locator: Pages 1-24, Sections 1-7 and Appendices A-B (Lemma 2.1, Example 2.2, Definition
    3.1, Example 3.2, Lemma 3.3, Example 3.4, Definition 3.5, Theorem 3.6, Corollary
    3.7, Algorithm 1, Proposition 4.1, Remarks 4.2-4.4, Proposition 4.5, Corollary
    4.6, Figures 1-10, Lemmas A.1-A.4, Algorithm 2)
  accessed_at: '2026-10-17T17:05:00Z'
  snapshot_sha256: c8e024a9c369dc010ef3f7af754267fc07dad921a2525ab3ed717e3cee077e9b
  support: supports
  summary: All 24 pages of the full-text PDF of arXiv:1807.01470v2 read. Checked all
    definitions, lemmas, propositions, theorems, algorithms, figures, and proofs.
- evidence_id: durand2020-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1111/sjos.12453
  locator: Scandinavian Journal of Statistics 47(4):1114-1148 publication record
  accessed_at: '2026-10-17T17:05:00Z'
  snapshot_sha256: ab88eb06001fb7ea657c92970f067c9b65236a97503b85893e8df9de5a9b37e5
  support: supports
  summary: Official Scandinavian Journal of Statistics 47(4):1114-1148 Crossref record
    read and verified.
- evidence_id: durand2020-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1807.01470
  locator: arXiv:1807.01470v2 abstract and metadata
  accessed_at: '2026-10-17T17:05:00Z'
  snapshot_sha256: 7bcfe7da684a82ac7adbd6b06f3d36b582472ea7714bc0486cb14b1456f1f0a5
  support: supports
  summary: arXiv:1807.01470v2 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ForestStructuredDKWPostHocConfidenceBounds versus ReferenceFamilyJERPostHocConfidenceBounds
    and SimultaneousPathwiseFalseDiscoveryProportionBounds
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - identity
  - durand2020-pdf
  - durand2020-crossref
  summary: Retain Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence
    bounds as a distinct DRAFT mathematical_method.
  details: ForestStructuredDKWPostHocConfidenceBounds defines multi-subset interpolation
    V_tilde^q_{R_ref}(S), proves exact optimality V^*_{R_ref}(S) = V_tilde_{R_ref}(S)
    = V_tilde^d_{R_ref}(S) on deterministic forest-structured reference families with
    O(Hm) bottom-up tree dynamic programming (Theorem 3.6, Algorithm 1), calibrates
    random local capacities zeta_k(X) via quadratic inversion of the Massart-DKW inequality
    (Proposition 4.1), proves the asymptotic 1 - r localized-signal improvement over
    Simes/Bonferroni (Proposition 4.5, Corollary 4.6), and introduces the Simes-DKW
    hybrid envelope V^gamma_{hybrid}(alpha, S).
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - mapping
  - durand2020-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Forest-structured DKW post hoc confidence bounds prevent post-selection
    data-snooping invalidation across all 2^m selected subsets (AIO:DataDredgingBias).
- assessment_id: multi-subset-interpolation-hierarchy-and-forest-exactness-theorem
  area: evidence
  topic: multi-subset-interpolation-hierarchy-and-forest-exactness-theorem
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - durand2020-pdf
  - durand2020-crossref
  - calculation
  summary: Supported by Section 2.3 (Lemma 2.1, Example 2.2), Section 3.1-3.2 (Definition
    3.1, Lemma 3.3, Definition 3.5, Theorem 3.6, Corollary 3.7), Section 7.1-7.3,
    and Appendices A-B.
  details: Verified Example 2.2 non-forest gap V^* = 1 < V_tilde = 2, Algorithm 2
    atomic decomposition, and Theorem 3.6 exact equality across all 256 subsets of
    an 8-element forest and on the 25-element forest of Example 3.2.
- assessment_id: bottom-up-dynamic-programming-algorithm-on-completed-forest
  area: evidence
  topic: bottom-up-dynamic-programming-algorithm-on-completed-forest
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - durand2020-pdf
  - durand2020-crossref
  - calculation
  summary: Supported by Section 3.2 (Algorithm 1, Figures 4-5), Section 7.2.1, and
    Lemma A.2.
  details: Verified that Algorithm 1 bottom-up recursion over the level partitions
    K^h of R_ref^oplus matches V^*_{R_ref}(S) and V_tilde^d_{R_ref}(S) exactly.
- assessment_id: local-dkw-massart-quadratic-inversion-calibration-and-gw-dominance
  area: evidence
  topic: local-dkw-massart-quadratic-inversion-calibration-and-gw-dominance
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - durand2020-pdf
  - calculation
  summary: Supported by Section 4.1 (Proposition 4.1, Remarks 4.2-4.4), Section 7.4
    (Equation 32), and Appendix A (Lemma A.1, Equation 33).
  details: Verified empirical JER control <= alpha and strict dominance zeta_k(X)
    <= zeta^{GW}_k(X) across 3,000 region-trials.
- assessment_id: localized-signal-asymptotic-improvement-and-simes-dkw-hybrid-envelope
  area: evidence
  topic: localized-signal-asymptotic-improvement-and-simes-dkw-hybrid-envelope
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - durand2020-pdf
  - durand2020-abs
  - calculation
  summary: Supported by Section 4.2 (Proposition 4.5, Figure 6, Corollary 4.6), Section
    5.1-5.3 (Figures 7-10), and Section 7.5.
  details: Verified Equation (23) Figure 6 ratio upper bounds and Section 5.3 Simes-DKW
    hybrid envelope complementarity at k = 10 and k = 200.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ForestStructuredDKWPostHocConfidenceBounds
  evidence_ids:
  - identity
  - mapping
  - durand2020-pdf
  - durand2020-crossref
  - durand2020-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ForestStructuredDKWPostHocConfidenceBounds.yaml: stable
    ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Forest-structured Dvoretzky-Kiefer-Wolfowitz post hoc confidence
  bounds record, yielding 604 native and 442 unchanged generated records.
- All 24 PDF pages of arXiv:1807.01470v2 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- post-hoc-inference
- forest-structure
- dkw-inequality
- self-review
- discovery-ongoing
```
