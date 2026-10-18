# Scientific author self-review of Simes closed-testing concentration-set shortcut and double-asymptotic false discovery proportion consistency

- Review: 20261017T171700Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T17:15:00Z
- Finished UTC: 2026-10-17T17:17:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Simes closed-testing concentration-set shortcut and double-asymptotic false discovery proportion consistency as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Goeman, Meijer, Krebs, &amp; Solari (2019, Biometrika 106(4):841-856, arXiv:1611.06739v2) are supported with explicit Simes-inequality dependence, non-vanishing subset size c &gt; 0, and primary-source typographical notes.

## Scope And Provenance

All fields of the exact maintained SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency record and its primary evidence.

Selection: Exact maintained ID: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1d1a09228697924f7f74603232f8005f1e404dcc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | data/curated/SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml | maintained | Simes closed-testing concentration-set shortcut and double-asymptotic false discovery proportion consistency |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | All 605 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | Exited 0 without output. |
| Constructed Goeman-Meijer-Krebs-Solari 2019 exact Simes closed-testing shortcut, concentration set Z_alpha, adaptive BH bounds, and double-limit FDP consistency checks | passed | True | AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency | {<br>  "concept_id": "AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency",<br>  "primary_source": "Goeman, Meijer, Krebs, &amp; Solari (2019), Biometrika 106(4):841-856 (arXiv:1611.06739v2, DOI:10.1093/biomet/asz041)",<br>  "section_3_figure_1_non_consonant_and_gs2011_gap": {<br>    "h_alpha": 2,<br>    "non_rejected_local_sets": [<br>      [<br>        1,<br>        4<br>      ],<br>      [<br>        2,<br>        4<br>      ],<br>      [<br>        3,<br>        4<br>      ],<br>      [<br>        4<br>      ]<br>    ],<br>    "r_alpha_elementary": [],<br>    "t_alpha_L3_exact": 1,<br>    "trivial_fwer_bound_L3": 3,<br>    "t_alpha_L2_exact": 1,<br>    "gs2011_shortcut_L2": 2<br>  },<br>  "sections_4_and_5_exact_shortcut_and_concentration_set": {<br>    "m": 8,<br>    "h_alpha": 4,<br>    "pi_hat_alpha": 0.5,<br>    "r_alpha_size": 2,<br>    "z_alpha": 5,<br>    "b_alpha": 6,<br>    "d_alpha_Z": 4,<br>    "q_alpha_B_alpha": 0.333333,<br>    "verified_subsets": 256,<br>    "non_consonant_strict_subsets": 128,<br>    "q_half_B_005": 0.0,<br>    "two_q_pi_hat_half": 0.0<br>  },<br>  "sections_6_and_7_simes_detectability_and_double_limit_consistency": {<br>    "gamma": 0.7,<br>    "pi_bar_alpha_n25": 0.929996,<br>    "pi_hat_sim_m4000": 0.9235,<br>    "hommel_fwer_fraction_m4000": 0.01575,<br>    "theorem_2_jm_fraction_m4000": 0.0905,<br>    "theorem_2_q_alpha_jm": 0.232044,<br>    "theorem_2_upper_bound": 0.232499,<br>    "theorem_3_gamma_S": 0.6,<br>    "theorem_3_q_alpha_S_m_trajectory": {<br>      "m=200,n=16": 0.9,<br>      "m=1000,n=36": 0.712,<br>      "m=4000,n=81": 0.609<br>    },<br>    "bh_rejection_fraction_trajectory": {<br>      "m=200,n=16": 0.19,<br>      "m=1000,n=36": 0.298,<br>      "m=4000,n=81": 0.311<br>    },<br>    "bh_theoretical_limit": 0.310881<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency versus ReferenceFamilyJERPostHocConfidenceBounds and ForestStructuredDKWPostHocConfidenceBounds

identity: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Retain Simes closed-testing concentration-set shortcut and double-asymptotic false discovery proportion consistency as a distinct DRAFT mathematical_method.

Goeman, Meijer, Krebs, &amp; Solari (2019) establish the exact O(m log m) + O(&#124;S&#124;) Simes closed-testing shortcut via Hommel's h_alpha (Theorem 1), the minimal concentration set Z_alpha = L_{z_alpha} and Benjamini-Hochberg sandwich (Lemmas 4-5), non-vanishing non-consonant discovery power under Simes-detectability (Theorem 2), and double-limit FDP consistency at arbitrary relative growth rates of (m, n) (Theorem 3).

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Related mapping to DataDredgingBias is supported.

Simultaneous closed-testing FDP confidence bounds across all 2^m subsets protect against post hoc data dredging and arbitrary subset revision (AIO:DataDredgingBias).

### hommel-h-characterization-and-exact-linear-time-all-subset-shortcut

evidence: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Supported by Sections 3-4 (Equations 4-10, Figure 1, Lemmas 1-3, Theorem 1) and Appendix A (Equations 18-19).

Verified Figure 1 non-consonant rejections and Goeman-Solari (2011) shortcut failure on L_2 = {1,2}, and verified Lemmas 1-3 and Theorem 1 across all 256 subsets of an 8-hypothesis problem.

### concentration-set-minimality-and-benjamini-hochberg-sandwich-bounds

evidence: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Supported by Section 5 (Equations 11-12, Lemmas 4-5, Figure 2) and Appendix A (Equation 20).

Verified concentration set Z_alpha minimality, sandwich inequalities &#124;S cap R_alpha&#124; &lt;= d_alpha(S) &lt;= &#124;S cap Z_alpha&#124; &lt;= &#124;S cap B_alpha&#124; across all 256 subsets, and Lemma 5 simultaneous BH bounds.

### simes-detectability-limit-and-non-vanishing-non-consonant-power

evidence: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Supported by Section 6 (Equations 13-14, Lemma 6, Theorem 2) and Appendix A (Equation 21, Lemma 7).

Verified Lemma 6 convergence of h_alpha / m to bar_pi_alpha, Equation (14) decay of Hommel FWER discoveries, and Theorem 2 non-vanishing discovery fraction.

### double-asymptotic-fdp-consistency-at-arbitrary-relative-rates

evidence: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

Supported by Section 7 (Equations 15-17, Theorem 3, Figure 3) and Appendix A (Equations 22-24, Lemma 8).

Verified Theorem 3 double-limit convergence q_{alpha,m,n}(S_m) -&gt; gamma_S = 0.60 vs. BH rejection proportion limit (1 - gamma)/(1 - alpha*gamma).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.

The full record is consistent; retain DRAFT.

Read every field of SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T171500Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency.json | supports | No normalized identity match for Simes closed-testing concentration-set shortcut and double-asymptotic FDP consistency across 442 pinned AIO records and 604 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides frequentist post-selection and multiplicity error-control context via related_match. |
| calculation | research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py | supports | Executed pure-Python verification in research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py (SHA-256 636fe24ef831b4609c4b9524df6d94b5eb64b278711b4876eb6a094175aa2c4e): (1) Section 3 Figure 1 Non-Consonant Rejections &amp; Goeman-Solari (2011) Shortcut Gap: verified h_alpha = 2, R_alpha = [], t_alpha(L_3) = 1 &lt; &#124;L_3 \ R_alpha&#124; = 3, and exact t_alpha(L_2) = 1 &lt; Goeman-Solari (2011) shortcut 2. (2) Sections 4 &amp; 5 Exact Shortcut &amp; Concentration Set Z_alpha: verified Lemmas 1-4 and Theorem 1 across all 256 subsets of an 8-hypothesis problem (h_alpha = 4, z_alpha = 5 &lt;= b_alpha = 6, d_alpha(Z_alpha) = 4, q_alpha(B_alpha) = 0.333333, strict non-consonant gains on 128 subsets) and Lemma 5 simultaneous BH bounds. (3) Sections 6 &amp; 7 Simes-Detectability &amp; Double-Limit Consistency: verified Lemma 6 convergence pi_hat_{alpha,4000} = 0.9235 -&gt; bar_pi_alpha = 0.929996, vanishing Hommel FWER fraction 0.01575 vs. non-vanishing Theorem 2 fraction &#124;J_4000&#124;/4000 = 0.0905 with q_alpha(J_4000) = 0.232044 &lt;= bar_pi_alpha * q = 0.232499, and Theorem 3 double-limit trajectory q_{alpha,m,n}(S_m) -&gt; gamma_S = 0.6 ({'m=200,n=16': 0.9, 'm=1000,n=36': 0.712, 'm=4000,n=81': 0.609}) vs. BH limit 0.310881. |
| gmks2019-pdf | https://arxiv.org/pdf/1611.06739; Pages 1-27, Sections 1-8 and Appendix A (Equations 1-24, Lemmas 1-8, Theorems 1-3, Figures 1-3) | supports | All 27 pages of the full-text PDF of arXiv:1611.06739v2 read. Checked all definitions, lemmas, theorems, figures, and proofs. |
| gmks2019-crossref | https://api.crossref.org/works/10.1093/biomet/asz041; Biometrika 106(4):841-856 publication record | supports | Official Biometrika 106(4):841-856 Crossref record read and verified. |
| gmks2019-abs | https://arxiv.org/abs/1611.06739; arXiv:1611.06739v2 abstract and metadata | supports | arXiv:1611.06739v2 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Simes closed-testing concentration-set shortcut and double-asymptotic FDP consistency record, yielding 605 native and 442 unchanged generated records.
- All 27 PDF pages of arXiv:1611.06739v2 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T171700Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Simes closed-testing concentration-set shortcut
  and double-asymptotic false discovery proportion consistency
started_at: '2026-10-17T17:15:00Z'
finished_at: '2026-10-17T17:17:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ReferenceFamilyJERPostHocConfidenceBounds
    (Blanchard, Neuvial, & Roquain 2020) and ForestStructuredDKWPostHocConfidenceBounds
    (Durand, Blanchard, Neuvial, & Roquain 2020), verified the Section 3 Figure 1
    non-consonant rejections and Goeman-Solari (2011) shortcut failure on L_2 = {1,2},
    verified Lemmas 1-5 and Theorem 1 across all 256 subsets of an 8-hypothesis problem,
    verified Lemma 6, Theorem 2 non-vanishing power vs. vanishing Hommel FWER power,
    and Theorem 3 double-limit consistency, and documented four typographical slips
    in arXiv:1611.06739v2 (pp. 7, 8, 10, 23). This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Simes closed-testing concentration-set shortcut and double-asymptotic
  false discovery proportion consistency as a distinct DRAFT mathematical_method with
  related DataDredgingBias mapping. All four claims and locators across Goeman, Meijer,
  Krebs, & Solari (2019, Biometrika 106(4):841-856, arXiv:1611.06739v2) are supported
  with explicit Simes-inequality dependence, non-vanishing subset size c > 0, and
  primary-source typographical notes.
source:
  git_revision: 1d1a09228697924f7f74603232f8005f1e404dcc
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ForestStructuredDKWPostHocConfidenceBounds.yaml
    sha256: 9bae8e3738defe08500250ea05b7669885f8434e0ac0413058d9c332be8fa29f
    role: context
  - path: data/curated/HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality.yaml
    sha256: 6e35c0df6b71a10d35d4bfc2b25558014c91114141256210ef1fa9d1a78424c4
    role: context
  - path: data/curated/ReferenceFamilyJERPostHocConfidenceBounds.yaml
    sha256: 7e0edec4d6cecc10454f8004806f7bc4b178af9a5daa540242f1771d387050eb
    role: context
  - path: data/curated/SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml
    sha256: 41cef06cda3799d6493029160b8fbfce2e2d6ede43cb8250c851eb18216a078d
    role: target
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T171500Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency.json
    sha256: 3f0e4be1af6d5b4b09d8a81f3c5c302575172db5c6bc7afa26cfc814bd58b96e
    role: context
  - path: research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py
    sha256: 636fe24ef831b4609c4b9524df6d94b5eb64b278711b4876eb6a094175aa2c4e
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
- target_id: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  path: data/curated/SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml
  label: Simes closed-testing concentration-set shortcut and double-asymptotic false
    discovery proportion consistency
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml
    role: maintained
scope:
  description: All fields of the exact maintained SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
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
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: All 605 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Goeman-Meijer-Krebs-Solari 2019 exact Simes closed-testing shortcut,
    concentration set Z_alpha, adaptive BH bounds, and double-limit FDP consistency
    checks
  command: python3 research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency\"\
    ,\n  \"primary_source\": \"Goeman, Meijer, Krebs, & Solari (2019), Biometrika\
    \ 106(4):841-856 (arXiv:1611.06739v2, DOI:10.1093/biomet/asz041)\",\n  \"section_3_figure_1_non_consonant_and_gs2011_gap\"\
    : {\n    \"h_alpha\": 2,\n    \"non_rejected_local_sets\": [\n      [\n      \
    \  1,\n        4\n      ],\n      [\n        2,\n        4\n      ],\n      [\n\
    \        3,\n        4\n      ],\n      [\n        4\n      ]\n    ],\n    \"\
    r_alpha_elementary\": [],\n    \"t_alpha_L3_exact\": 1,\n    \"trivial_fwer_bound_L3\"\
    : 3,\n    \"t_alpha_L2_exact\": 1,\n    \"gs2011_shortcut_L2\": 2\n  },\n  \"\
    sections_4_and_5_exact_shortcut_and_concentration_set\": {\n    \"m\": 8,\n  \
    \  \"h_alpha\": 4,\n    \"pi_hat_alpha\": 0.5,\n    \"r_alpha_size\": 2,\n   \
    \ \"z_alpha\": 5,\n    \"b_alpha\": 6,\n    \"d_alpha_Z\": 4,\n    \"q_alpha_B_alpha\"\
    : 0.333333,\n    \"verified_subsets\": 256,\n    \"non_consonant_strict_subsets\"\
    : 128,\n    \"q_half_B_005\": 0.0,\n    \"two_q_pi_hat_half\": 0.0\n  },\n  \"\
    sections_6_and_7_simes_detectability_and_double_limit_consistency\": {\n    \"\
    gamma\": 0.7,\n    \"pi_bar_alpha_n25\": 0.929996,\n    \"pi_hat_sim_m4000\":\
    \ 0.9235,\n    \"hommel_fwer_fraction_m4000\": 0.01575,\n    \"theorem_2_jm_fraction_m4000\"\
    : 0.0905,\n    \"theorem_2_q_alpha_jm\": 0.232044,\n    \"theorem_2_upper_bound\"\
    : 0.232499,\n    \"theorem_3_gamma_S\": 0.6,\n    \"theorem_3_q_alpha_S_m_trajectory\"\
    : {\n      \"m=200,n=16\": 0.9,\n      \"m=1000,n=36\": 0.712,\n      \"m=4000,n=81\"\
    : 0.609\n    },\n    \"bh_rejection_fraction_trajectory\": {\n      \"m=200,n=16\"\
    : 0.19,\n      \"m=1000,n=36\": 0.298,\n      \"m=4000,n=81\": 0.311\n    },\n\
    \    \"bh_theoretical_limit\": 0.310881\n  },\n  \"all_assertions_passed\": true\n\
    }"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T171500Z-simes-closed-testing-concentration-shortcut-and-fdp-consistency.json
  accessed_at: '2026-10-17T17:15:00Z'
  support: supports
  summary: No normalized identity match for Simes closed-testing concentration-set
    shortcut and double-asymptotic FDP consistency across 442 pinned AIO records and
    604 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T17:15:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). Provides
    frequentist post-selection and multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py
  accessed_at: '2026-10-17T17:15:00Z'
  snapshot_sha256: 636fe24ef831b4609c4b9524df6d94b5eb64b278711b4876eb6a094175aa2c4e
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/simes-closed-testing-concentration-shortcut-and-fdp-consistency-boundaries.py
    (SHA-256 636fe24ef831b4609c4b9524df6d94b5eb64b278711b4876eb6a094175aa2c4e): (1)
    Section 3 Figure 1 Non-Consonant Rejections & Goeman-Solari (2011) Shortcut Gap:
    verified h_alpha = 2, R_alpha = [], t_alpha(L_3) = 1 < |L_3 \ R_alpha| = 3, and
    exact t_alpha(L_2) = 1 < Goeman-Solari (2011) shortcut 2. (2) Sections 4 & 5 Exact
    Shortcut & Concentration Set Z_alpha: verified Lemmas 1-4 and Theorem 1 across
    all 256 subsets of an 8-hypothesis problem (h_alpha = 4, z_alpha = 5 <= b_alpha
    = 6, d_alpha(Z_alpha) = 4, q_alpha(B_alpha) = 0.333333, strict non-consonant gains
    on 128 subsets) and Lemma 5 simultaneous BH bounds. (3) Sections 6 & 7 Simes-Detectability
    & Double-Limit Consistency: verified Lemma 6 convergence pi_hat_{alpha,4000} =
    0.9235 -> bar_pi_alpha = 0.929996, vanishing Hommel FWER fraction 0.01575 vs.
    non-vanishing Theorem 2 fraction |J_4000|/4000 = 0.0905 with q_alpha(J_4000) =
    0.232044 <= bar_pi_alpha * q = 0.232499, and Theorem 3 double-limit trajectory
    q_{alpha,m,n}(S_m) -> gamma_S = 0.6 ({''m=200,n=16'': 0.9, ''m=1000,n=36'': 0.712,
    ''m=4000,n=81'': 0.609}) vs. BH limit 0.310881.'
- evidence_id: gmks2019-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1611.06739
  locator: Pages 1-27, Sections 1-8 and Appendix A (Equations 1-24, Lemmas 1-8, Theorems
    1-3, Figures 1-3)
  accessed_at: '2026-10-17T17:15:00Z'
  snapshot_sha256: a3f4992cffde630eb0dedf047efbce6bab4b4ece682962bd544b5f5321dcce41
  support: supports
  summary: All 27 pages of the full-text PDF of arXiv:1611.06739v2 read. Checked all
    definitions, lemmas, theorems, figures, and proofs.
- evidence_id: gmks2019-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1093/biomet/asz041
  locator: Biometrika 106(4):841-856 publication record
  accessed_at: '2026-10-17T17:15:00Z'
  snapshot_sha256: ab62d4953d0e0bedf41c737d839e36bdcfa05a646895787d897bbfb48a47856a
  support: supports
  summary: Official Biometrika 106(4):841-856 Crossref record read and verified.
- evidence_id: gmks2019-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1611.06739
  locator: arXiv:1611.06739v2 abstract and metadata
  accessed_at: '2026-10-17T17:15:00Z'
  snapshot_sha256: c162b611101e90effd5b25886112940e1997dd1f3967429f85e3f81245c55d7f
  support: supports
  summary: arXiv:1611.06739v2 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
    versus ReferenceFamilyJERPostHocConfidenceBounds and ForestStructuredDKWPostHocConfidenceBounds
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - identity
  - gmks2019-pdf
  - gmks2019-crossref
  summary: Retain Simes closed-testing concentration-set shortcut and double-asymptotic
    false discovery proportion consistency as a distinct DRAFT mathematical_method.
  details: Goeman, Meijer, Krebs, & Solari (2019) establish the exact O(m log m) +
    O(|S|) Simes closed-testing shortcut via Hommel's h_alpha (Theorem 1), the minimal
    concentration set Z_alpha = L_{z_alpha} and Benjamini-Hochberg sandwich (Lemmas
    4-5), non-vanishing non-consonant discovery power under Simes-detectability (Theorem
    2), and double-limit FDP consistency at arbitrary relative growth rates of (m,
    n) (Theorem 3).
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - mapping
  - gmks2019-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Simultaneous closed-testing FDP confidence bounds across all 2^m subsets
    protect against post hoc data dredging and arbitrary subset revision (AIO:DataDredgingBias).
- assessment_id: hommel-h-characterization-and-exact-linear-time-all-subset-shortcut
  area: evidence
  topic: hommel-h-characterization-and-exact-linear-time-all-subset-shortcut
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - gmks2019-pdf
  - gmks2019-crossref
  - calculation
  summary: Supported by Sections 3-4 (Equations 4-10, Figure 1, Lemmas 1-3, Theorem
    1) and Appendix A (Equations 18-19).
  details: Verified Figure 1 non-consonant rejections and Goeman-Solari (2011) shortcut
    failure on L_2 = {1,2}, and verified Lemmas 1-3 and Theorem 1 across all 256 subsets
    of an 8-hypothesis problem.
- assessment_id: concentration-set-minimality-and-benjamini-hochberg-sandwich-bounds
  area: evidence
  topic: concentration-set-minimality-and-benjamini-hochberg-sandwich-bounds
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - gmks2019-pdf
  - calculation
  summary: Supported by Section 5 (Equations 11-12, Lemmas 4-5, Figure 2) and Appendix
    A (Equation 20).
  details: Verified concentration set Z_alpha minimality, sandwich inequalities |S
    cap R_alpha| <= d_alpha(S) <= |S cap Z_alpha| <= |S cap B_alpha| across all 256
    subsets, and Lemma 5 simultaneous BH bounds.
- assessment_id: simes-detectability-limit-and-non-vanishing-non-consonant-power
  area: evidence
  topic: simes-detectability-limit-and-non-vanishing-non-consonant-power
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - gmks2019-pdf
  - gmks2019-abs
  - calculation
  summary: Supported by Section 6 (Equations 13-14, Lemma 6, Theorem 2) and Appendix
    A (Equation 21, Lemma 7).
  details: Verified Lemma 6 convergence of h_alpha / m to bar_pi_alpha, Equation (14)
    decay of Hommel FWER discoveries, and Theorem 2 non-vanishing discovery fraction.
- assessment_id: double-asymptotic-fdp-consistency-at-arbitrary-relative-rates
  area: evidence
  topic: double-asymptotic-fdp-consistency-at-arbitrary-relative-rates
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - gmks2019-pdf
  - calculation
  summary: Supported by Section 7 (Equations 15-17, Theorem 3, Figure 3) and Appendix
    A (Equations 22-24, Lemma 8).
  details: Verified Theorem 3 double-limit convergence q_{alpha,m,n}(S_m) -> gamma_S
    = 0.60 vs. BH rejection proportion limit (1 - gamma)/(1 - alpha*gamma).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency
  evidence_ids:
  - identity
  - mapping
  - gmks2019-pdf
  - gmks2019-crossref
  - gmks2019-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of SimesClosedTestingConcentrationShortcutAndDoubleAsymptoticFDPConsistency.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Simes closed-testing concentration-set shortcut and double-asymptotic
  FDP consistency record, yielding 605 native and 442 unchanged generated records.
- All 27 PDF pages of arXiv:1611.06739v2 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- closed-testing
- simes-test
- post-hoc-inference
- self-review
- discovery-ongoing
```
