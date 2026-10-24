# Scientific author self-review of E-value Benjamini-Hochberg procedure

- Review: 20261017T112200Z-evalue-benjamini-hochberg-procedure
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T11:20:00Z
- Finished UTC: 2026-10-17T11:22:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain E-value Benjamini-Hochberg procedure as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Wang &amp; Ramdas (2022) and Vovk &amp; Wang (2021) are supported with explicit unboosted conservatism, PRDS/sparse-regime comparison to BH/BY, and heterogeneous boosting rank-reversal limitations.

## Scope And Provenance

All fields of the exact maintained EValueBenjaminiHochbergProcedure record and its primary evidence.

Selection: Exact maintained ID: AIMech:EValueBenjaminiHochbergProcedure
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3ac54042afac9fa12b1ea752a877fd6417f552ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:EValueBenjaminiHochbergProcedure | data/curated/EValueBenjaminiHochbergProcedure.yaml | maintained | E-value Benjamini-Hochberg procedure |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:EValueBenjaminiHochbergProcedure | All AIMech schema, curated, seed, and history validations passed. |
| just vendored-check | passed | True | AIMech:EValueBenjaminiHochbergProcedure | Vendored CLAW review files match canonical checksums. |
| aimech check-source | passed | True | AIMech:EValueBenjaminiHochbergProcedure | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:EValueBenjaminiHochbergProcedure | Exited 0 without output. |
| Constructed E-value Benjamini-Hochberg procedure boundaries | passed | True | AIMech:EValueBenjaminiHochbergProcedure | {<br>  "boosting_examples": {<br>    "example_2_exact_y_alpha_K100": 0.048703,<br>    "example_2_power_ad_b": 6.324555,<br>    "example_3_gaussian_ad_b": {<br>      "delta_3": 1.373374,<br>      "delta_4": 1.11197<br>    },<br>    "example_5_power_prds_b": 8.944272,<br>    "example_6_gaussian_prds_b": {<br>      "delta_3": 7.881002,<br>      "delta_4": 10.321968<br>    }<br>  },<br>  "example_4_sharpness": {<br>    "K": 5,<br>    "K0": 3,<br>    "alpha": 0.05,<br>    "exact_fdr": 0.03,<br>    "null_e_value_expectation": 1.0,<br>    "theoretical_upper_bound": 0.03<br>  },<br>  "optimality_and_calibration": {<br>    "proposition_4_K": 6,<br>    "proposition_4_alpha_times_l_K": 0.1225,<br>    "proposition_4_harmonic_l_K": 2.45,<br>    "proposition_4_y_psi": 0.1225,<br>    "theorem_5_ebh_threshold": 60.0,<br>    "theorem_5_induced_fdr": 0.066667,<br>    "theorem_5_k0": 2,<br>    "theorem_5_violating_m_prime": 45.0<br>  },<br>  "stepdown_and_postselection": {<br>    "alpha": 0.05,<br>    "k_star": 3,<br>    "post_selection_amended_alpha": 0.04,<br>    "post_selection_rejected_0based": [<br>      2,<br>      3,<br>      4<br>    ],<br>    "post_selection_subset_size": 4,<br>    "rejected_0based": [<br>      2,<br>      3,<br>      4<br>    ],<br>    "t_alpha": 33.333333,<br>    "test_vector": [<br>      0.8,<br>      12.0,<br>      34.0,<br>      55.0,<br>      90.0<br>    ]<br>  }<br>} |

## Scientific And Domain Assessments

### E-Value Benjamini-Hochberg Procedure versus EValueCalibrationAndMerging

identity: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Retain E-value Benjamini-Hochberg procedure as a distinct DRAFT mathematical_method.

EValueBenjaminiHochbergProcedure formalizes step-down e-value FDR control at level alpha K_0 / K under arbitrary dependence, grid-truncation boosting T(x) under AD and PRDS, and self-consistent post-selection e-BH, distinct from global-null e-merging and closed-testing FWER adjustment.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Related mapping to DataDredgingBias is supported.

Self-consistent e-BH and post-selection e-BH preserve valid FDR control under arbitrary dependence, adaptive bandit stopping, and data-dependent screening, preventing data-dredging false-discovery inflation (AIO:DataDredgingBias).

### base-ebh-stepdown-threshold-equivalence-and-self-consistent-fdr-control

evidence: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Supported by Section 4.1 Proposition 1, Section 5 Theorem 2 / Proposition 2, and Section 5.1.

Verified exact agreement between step-down rejection k_e^* = 3 and threshold t_alpha = 33.333333 on e = (0.8, 12.0, 34.0, 55.0, 90.0) and post-selection self-consistency at amended level alpha_tilde = 0.04.

### grid-truncation-boosting-under-arbitrary-dependence-and-sharpness

evidence: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Supported by Section 4.2, Section 6.1 Lemma 1(iii), and Section 6.2 Theorem 3 &amp; Examples 2-4.

Verified Example 4 exact FDR = 0.03 = alpha K_0 / K, Example 2 power boosting b_AD = 6.324555 (exact K=100 y_alpha = 0.048703 &lt;= 0.05), and Example 3 Gaussian boosting b_AD = 1.373374 (delta = 3) and 1.11197 (delta = 4).

### prds-fdr-bound-and-exact-quantile-boosting-factor

evidence: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Supported by Section 6.1 Lemma 1(ii) and Section 6.3 Theorem 4, Proposition 3, &amp; Examples 5-6.

Verified Example 5 PRDS quantile boosting b_PRDS = 8.944272 with exact ratio z_{alpha,k}(b) / y_bar_{alpha,k}(b) = lambda = 0.5, and Example 6 Gaussian PRDS boosting b_PRDS = 7.881002 (delta = 3) and 10.321968 (delta = 4).

### monotone-transform-optimality-and-bh-by-calibration-unification

evidence: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

Supported by Section 6.4 Theorem 5 and Section 6.5 Propositions 4-5 in Wang &amp; Ramdas (2022).

Verified Theorem 5 counterexample construction yielding FDR = 0.066667 &gt; 0.05 when phi^(-1)(K/k_0) &lt; K/(k_0 alpha), and Proposition 4 exact equality y_psi = 0.1225 = alpha * l_6 for psi(p) = alpha / p.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:EValueBenjaminiHochbergProcedure.

The full record is consistent; retain DRAFT.

Read every field of EValueBenjaminiHochbergProcedure.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, two full-text primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T112000Z-evalue-benjamini-hochberg-procedure.json | supports | No normalized identity match for E-value Benjamini-Hochberg procedure across 442 pinned AIO records and 571 maintained IDs, names, aliases and scoped synonyms. Fixed-string search returned only 7 lines in Round 176 discovery/review files where arXiv:2009.02824 was listed as a pending frontier lead. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides arbitrary-dependence, optional-stopping, and post-selection multiple-testing context via related_match. |
| calculation | research/discovery/evalue-benjamini-hochberg-procedure-boundaries.py | supports | Constructed analytical and numerical checks for Proposition 1 step-down/threshold equivalence, Section 5.1 post-selection self-consistency, Example 4 FDR tightness, Examples 2, 3, 5, and 6 boosting factors under arbitrary dependence and PRDS, Theorem 5 optimality counterexample, and Proposition 4 exact recovery of the BY harmonic factor. |
| wang-ramdas2022-ebh | https://ar5iv.labs.arxiv.org/html/2009.02824; Sections 4-8 (lines 160-558, Propositions 1-5, Lemma 1, Theorems 2-5, Examples 2-7) and Appendices A-C (lines 1066-1231) | supports | All 1,242 lines of the full-text ar5iv HTML conversion of arXiv:2009.02824 read. Checked Propositions 1-6, Lemma 1, Theorems 1-5, Examples 1-7, and Appendices A-C. |
| vovk-wang2021-evalues | https://ar5iv.labs.arxiv.org/html/1912.06116; Section 2 (lines 26-74) and Section 5 (lines 138-169) | supports | All 1,288 lines of arXiv:1912.06116 read. Checked p-to-e power calibrators and closed-testing FWER contrast. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT E-value Benjamini-Hochberg procedure record, yielding 572 native and 442 unchanged generated records.
- All 1,242 lines of Wang &amp; Ramdas (2022, arXiv:2009.02824) and all 1,288 lines of Vovk &amp; Wang (2021, arXiv:1912.06116) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T112200Z-evalue-benjamini-hochberg-procedure
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of E-value Benjamini-Hochberg procedure
started_at: '2026-10-17T11:20:00Z'
finished_at: '2026-10-17T11:22:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from EValueCalibrationAndMerging,
    conservatism of unboosted base e-BH when marginal null distributions are unknown,
    domination by classical BH under PRDS with uniform p-values and by BY in ultra-sparse
    rejection regimes, and rank-reversal under heterogeneous boosting factors. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain E-value Benjamini-Hochberg procedure as a distinct DRAFT mathematical_method
  with related DataDredgingBias mapping. All four claims and locators across Wang
  & Ramdas (2022) and Vovk & Wang (2021) are supported with explicit unboosted conservatism,
  PRDS/sparse-regime comparison to BH/BY, and heterogeneous boosting rank-reversal
  limitations.
source:
  git_revision: 3ac54042afac9fa12b1ea752a877fd6417f552ab
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
  - path: data/curated/EValueBenjaminiHochbergProcedure.yaml
    sha256: a9553e05b33722aab92042bef82fe67208d2ddb565f7133125bdb2cb79b27057
    role: target
  - path: data/curated/EValueCalibrationAndMerging.yaml
    sha256: f5246f4bae50e562eaa72b28da34d9ab2100831ad5a4e148447754f4debd2107
    role: context
  - path: data/curated/ExactHarmonicMeanPValueTest.yaml
    sha256: e37fe73ff6637f2951762fe4cceca81cd277e7f3d8dafaad63ca150e314a9793
    role: context
  - path: data/curated/GeneralizedMeanPValueMerging.yaml
    sha256: 099a7959a7d93ae42c966e7ca9e54c90581ba3c54218810baead7bd017e58396
    role: context
  - path: data/curated/HalfCauchyCombinationTest.yaml
    sha256: 16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e
    role: context
  - path: data/curated/LeftTruncatedCauchyCombinationTest.yaml
    sha256: 6f330e91bd1f1994411c626759aee135f6dc781c2b3107e2c9db78e26c5685f6
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/ProjectedHotellingT2DivideAndCombineConfidenceRegion.yaml
    sha256: e90c5c9448b52371dbe720d48eebd14211970a06202b343e255f35248e7101f0
    role: context
  - path: research/discovery/20261017T112000Z-evalue-benjamini-hochberg-procedure.json
    sha256: d79ce6ecf1c00830263aa037281f614901eef74abe58450dc4ae19933aae286a
    role: context
  - path: research/discovery/evalue-benjamini-hochberg-procedure-boundaries.py
    sha256: 1d31fa066cc9b75f87cf6456f126c5f4e16d31e65252a9b1708448954dc57934
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
- target_id: AIMech:EValueBenjaminiHochbergProcedure
  path: data/curated/EValueBenjaminiHochbergProcedure.yaml
  label: E-value Benjamini-Hochberg procedure
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EValueBenjaminiHochbergProcedure.yaml
    role: maintained
scope:
  description: All fields of the exact maintained EValueBenjaminiHochbergProcedure
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:EValueBenjaminiHochbergProcedure'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exit_code: 0
  expected_exit_code: 0
  summary: All AIMech schema, curated, seed, and history validations passed.
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW review files match canonical checksums.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed E-value Benjamini-Hochberg procedure boundaries
  command: python3 research/discovery/evalue-benjamini-hochberg-procedure-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"boosting_examples\": {\n    \"example_2_exact_y_alpha_K100\": 0.048703,\n\
    \    \"example_2_power_ad_b\": 6.324555,\n    \"example_3_gaussian_ad_b\": {\n\
    \      \"delta_3\": 1.373374,\n      \"delta_4\": 1.11197\n    },\n    \"example_5_power_prds_b\"\
    : 8.944272,\n    \"example_6_gaussian_prds_b\": {\n      \"delta_3\": 7.881002,\n\
    \      \"delta_4\": 10.321968\n    }\n  },\n  \"example_4_sharpness\": {\n   \
    \ \"K\": 5,\n    \"K0\": 3,\n    \"alpha\": 0.05,\n    \"exact_fdr\": 0.03,\n\
    \    \"null_e_value_expectation\": 1.0,\n    \"theoretical_upper_bound\": 0.03\n\
    \  },\n  \"optimality_and_calibration\": {\n    \"proposition_4_K\": 6,\n    \"\
    proposition_4_alpha_times_l_K\": 0.1225,\n    \"proposition_4_harmonic_l_K\":\
    \ 2.45,\n    \"proposition_4_y_psi\": 0.1225,\n    \"theorem_5_ebh_threshold\"\
    : 60.0,\n    \"theorem_5_induced_fdr\": 0.066667,\n    \"theorem_5_k0\": 2,\n\
    \    \"theorem_5_violating_m_prime\": 45.0\n  },\n  \"stepdown_and_postselection\"\
    : {\n    \"alpha\": 0.05,\n    \"k_star\": 3,\n    \"post_selection_amended_alpha\"\
    : 0.04,\n    \"post_selection_rejected_0based\": [\n      2,\n      3,\n     \
    \ 4\n    ],\n    \"post_selection_subset_size\": 4,\n    \"rejected_0based\":\
    \ [\n      2,\n      3,\n      4\n    ],\n    \"t_alpha\": 33.333333,\n    \"\
    test_vector\": [\n      0.8,\n      12.0,\n      34.0,\n      55.0,\n      90.0\n\
    \    ]\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T112000Z-evalue-benjamini-hochberg-procedure.json
  accessed_at: '2026-10-17T11:20:00Z'
  support: supports
  summary: No normalized identity match for E-value Benjamini-Hochberg procedure across
    442 pinned AIO records and 571 maintained IDs, names, aliases and scoped synonyms.
    Fixed-string search returned only 7 lines in Round 176 discovery/review files
    where arXiv:2009.02824 was listed as a pending frontier lead.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T11:20:00Z'
  support: supports
  summary: Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot
    (2026-07-22). DataDredgingBias provides arbitrary-dependence, optional-stopping,
    and post-selection multiple-testing context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/evalue-benjamini-hochberg-procedure-boundaries.py
  accessed_at: '2026-10-17T11:20:00Z'
  snapshot_sha256: 1d31fa066cc9b75f87cf6456f126c5f4e16d31e65252a9b1708448954dc57934
  support: supports
  summary: Constructed analytical and numerical checks for Proposition 1 step-down/threshold
    equivalence, Section 5.1 post-selection self-consistency, Example 4 FDR tightness,
    Examples 2, 3, 5, and 6 boosting factors under arbitrary dependence and PRDS,
    Theorem 5 optimality counterexample, and Proposition 4 exact recovery of the BY
    harmonic factor.
- evidence_id: wang-ramdas2022-ebh
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2009.02824
  locator: Sections 4-8 (lines 160-558, Propositions 1-5, Lemma 1, Theorems 2-5, Examples
    2-7) and Appendices A-C (lines 1066-1231)
  accessed_at: '2026-10-17T11:20:00Z'
  snapshot_sha256: 26bd39717641ca16a7b1bbfc1d1e962853428ad3fbcbf6a82687bfa6536e901c
  support: supports
  summary: All 1,242 lines of the full-text ar5iv HTML conversion of arXiv:2009.02824
    read. Checked Propositions 1-6, Lemma 1, Theorems 1-5, Examples 1-7, and Appendices
    A-C.
- evidence_id: vovk-wang2021-evalues
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1912.06116
  locator: Section 2 (lines 26-74) and Section 5 (lines 138-169)
  accessed_at: '2026-10-17T11:05:00Z'
  snapshot_sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda
  support: supports
  summary: All 1,288 lines of arXiv:1912.06116 read. Checked p-to-e power calibrators
    and closed-testing FWER contrast.
assessments:
- assessment_id: identity
  area: identity
  topic: E-Value Benjamini-Hochberg Procedure versus EValueCalibrationAndMerging
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - identity
  - wang-ramdas2022-ebh
  - vovk-wang2021-evalues
  summary: Retain E-value Benjamini-Hochberg procedure as a distinct DRAFT mathematical_method.
  details: EValueBenjaminiHochbergProcedure formalizes step-down e-value FDR control
    at level alpha K_0 / K under arbitrary dependence, grid-truncation boosting T(x)
    under AD and PRDS, and self-consistent post-selection e-BH, distinct from global-null
    e-merging and closed-testing FWER adjustment.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - mapping
  - wang-ramdas2022-ebh
  summary: Related mapping to DataDredgingBias is supported.
  details: Self-consistent e-BH and post-selection e-BH preserve valid FDR control
    under arbitrary dependence, adaptive bandit stopping, and data-dependent screening,
    preventing data-dredging false-discovery inflation (AIO:DataDredgingBias).
- assessment_id: base-ebh-stepdown-threshold-equivalence-and-self-consistent-fdr-control
  area: evidence
  topic: base-ebh-stepdown-threshold-equivalence-and-self-consistent-fdr-control
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - wang-ramdas2022-ebh
  - calculation
  summary: Supported by Section 4.1 Proposition 1, Section 5 Theorem 2 / Proposition
    2, and Section 5.1.
  details: Verified exact agreement between step-down rejection k_e^* = 3 and threshold
    t_alpha = 33.333333 on e = (0.8, 12.0, 34.0, 55.0, 90.0) and post-selection self-consistency
    at amended level alpha_tilde = 0.04.
- assessment_id: grid-truncation-boosting-under-arbitrary-dependence-and-sharpness
  area: evidence
  topic: grid-truncation-boosting-under-arbitrary-dependence-and-sharpness
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - wang-ramdas2022-ebh
  - calculation
  summary: Supported by Section 4.2, Section 6.1 Lemma 1(iii), and Section 6.2 Theorem
    3 & Examples 2-4.
  details: Verified Example 4 exact FDR = 0.03 = alpha K_0 / K, Example 2 power boosting
    b_AD = 6.324555 (exact K=100 y_alpha = 0.048703 <= 0.05), and Example 3 Gaussian
    boosting b_AD = 1.373374 (delta = 3) and 1.11197 (delta = 4).
- assessment_id: prds-fdr-bound-and-exact-quantile-boosting-factor
  area: evidence
  topic: prds-fdr-bound-and-exact-quantile-boosting-factor
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - wang-ramdas2022-ebh
  - calculation
  summary: Supported by Section 6.1 Lemma 1(ii) and Section 6.3 Theorem 4, Proposition
    3, & Examples 5-6.
  details: Verified Example 5 PRDS quantile boosting b_PRDS = 8.944272 with exact
    ratio z_{alpha,k}(b) / y_bar_{alpha,k}(b) = lambda = 0.5, and Example 6 Gaussian
    PRDS boosting b_PRDS = 7.881002 (delta = 3) and 10.321968 (delta = 4).
- assessment_id: monotone-transform-optimality-and-bh-by-calibration-unification
  area: evidence
  topic: monotone-transform-optimality-and-bh-by-calibration-unification
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - wang-ramdas2022-ebh
  - calculation
  summary: Supported by Section 6.4 Theorem 5 and Section 6.5 Propositions 4-5 in
    Wang & Ramdas (2022).
  details: Verified Theorem 5 counterexample construction yielding FDR = 0.066667
    > 0.05 when phi^(-1)(K/k_0) < K/(k_0 alpha), and Proposition 4 exact equality
    y_psi = 0.1225 = alpha * l_6 for psi(p) = alpha / p.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:EValueBenjaminiHochbergProcedure
  evidence_ids:
  - identity
  - mapping
  - wang-ramdas2022-ebh
  - vovk-wang2021-evalues
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of EValueBenjaminiHochbergProcedure.yaml: stable ID,
    name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes,
    four claims and locators, two full-text primary sources with exact SHA-256 digests,
    pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT E-value Benjamini-Hochberg procedure record, yielding 572 native
  and 442 unchanged generated records.
- All 1,242 lines of Wang & Ramdas (2022, arXiv:2009.02824) and all 1,288 lines of
  Vovk & Wang (2021, arXiv:1912.06116) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- hypothesis-testing
- e-values
- false-discovery-rate
- multiple-testing
- self-review
- discovery-ongoing
```
