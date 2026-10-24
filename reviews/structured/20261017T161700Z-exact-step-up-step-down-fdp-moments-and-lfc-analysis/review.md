# Scientific author self-review of exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis

- Review: 20261017T161700Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T16:15:00Z
- Finished UTC: 2026-10-17T16:17:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Roquain &amp; Villers (2011 Annals of Statistics 39(1):584-612) are supported with explicit Steck numerical stability, non-concave LFC, and Section 6.4 Eq. (34) recurrence limitations.

## Scope And Provenance

All fields of the exact maintained ExactStepUpStepDownFDPMomentsAndLFCAnalysis record and its primary evidence.

Selection: Exact maintained ID: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a39e83ae6c1cf0cb5a001fd894ca8d9f1c98168a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml | maintained | exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | All 599 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | Exited 0 without output. |
| Constructed Roquain-Villers 2011 exact step-up/step-down FDP moments, Condition (A), and FDP variance checks | passed | True | AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis | {<br>  "concept_id": "AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis",<br>  "primary_source": "Roquain &amp; Villers (2011), Annals of Statistics 39(1):584-612 (arXiv:1002.2845v2, DOI:10.1214/10-AOS847)",<br>  "theorem_3_1_moments_verification": {<br>    "m": 5,<br>    "pi0": 0.6,<br>    "alpha": 0.25,<br>    "moments_1_to_4": {<br>      "1": {<br>        "stirling_formula_eq13": 0.15,<br>        "conditional_binomial_eq11": 0.15<br>      },<br>      "2": {<br>        "stirling_formula_eq13": 0.1170884792,<br>        "conditional_binomial_eq11": 0.1170884792<br>      },<br>      "3": {<br>        "stirling_formula_eq13": 0.101398793,<br>        "conditional_binomial_eq11": 0.101398793<br>      },<br>      "4": {<br>        "stirling_formula_eq13": 0.0934439164,<br>        "conditional_binomial_eq11": 0.0934439164<br>      }<br>    },<br>    "s3_omitting_stirling_factor_3": 0.0875851833,<br>    "s3_stirling_correction_magnitude": 0.0138136097<br>  },<br>  "theorem_3_2_step_down_verification": {<br>    "non_binomial_conditional_l1_gap": 0.12385118,<br>    "lsd_fdr_m6_pi07_alpha02_uniform": 0.1288390608,<br>    "lsd_fdr_m6_pi07_alpha02_sqrt": 0.1259581312,<br>    "lsd_fdr_m6_pi07_alpha02_dirac_eq20": 0.1346047661,<br>    "lsd_fdr_m6_pi07_alpha02_dirac_eq21": 0.1346047661<br>  },<br>  "proposition_3_6_negative_correlation_counterexample": {<br>    "m": 2,<br>    "m0": 1,<br>    "alpha": 0.05,<br>    "fdr_lsu_at_rho_minus_1": 0.0375,<br>    "benjamini_yekutieli_upper_bound": 0.0375,<br>    "dirac_uniform_fdr": 0.025<br>  },<br>  "theorem_4_1_condition_a_and_su_vs_sd_lfc_split": {<br>    "s_lsd_m6_alpha02_true": [<br>      0.9137931,<br>      0.95108711,<br>      0.97138902,<br>      0.98431953,<br>      0.99333333,<br>      1.0<br>    ],<br>    "s_lsd_m6_alpha02_recursion_eq34": [<br>      0.87484276,<br>      0.94031958,<br>      0.96827094,<br>      0.98363858,<br>      0.99333333,<br>      1.0<br>    ],<br>    "eq34_max_discrepancy": 0.03895035,<br>    "q_concave_t_m5": [<br>      0.11466412,<br>      0.13277095,<br>      0.14706628,<br>      0.16120651,<br>      0.18<br>    ],<br>    "fdr_su_concave_t_uniform_f1": 0.45956142,<br>    "fdr_su_concave_t_dirac_f1": 0.453016,<br>    "fdr_sd_concave_t_uniform_f1": 0.34753598,<br>    "fdr_sd_concave_t_dirac_f1": 0.41564914<br>  },<br>  "theorem_4_3_fdp_variance_extrema": {<br>    "small_m6_pi07_alpha02": {<br>      "var_min_eq29": 0.05630184,<br>      "sd_min": 0.2372800877,<br>      "var_min_concave": 0.1134,<br>      "sd_min_concave": 0.3367491648,<br>      "var_max_eq30": 0.1204,<br>      "sd_max": 0.3469870315<br>    },<br>    "sparse_m10000_pi099_alpha005": {<br>      "sd_min": 0.021685,<br>      "sd_min_concave": 0.216852,<br>      "sd_max": 0.21691,<br>      "var_min": 0.00047025,<br>      "var_max": 0.04704975<br>    }<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### ExactStepUpStepDownFDPMomentsAndLFCAnalysis versus StepUpDownLeastFavorableConfigurationFDRBounds and ArchimedeanCopulaStepUpFDRBounds

identity: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Retain exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis as a distinct DRAFT mathematical_method.

ExactStepUpStepDownFDPMomentsAndLFCAnalysis establishes the conditional binomial law of step-up false rejections, the Stirling-number s-th moment formula for the FDP, the non-binomial conditional step-down law and exact joint rejection distribution, Condition (A) for step-down Dirac-uniform LFCs over concave alternatives, the m = 2 negatively correlated Gaussian counterexample attaining 3*alpha/4, and the exact closed-form minimum and maximum of Var[FDP(LSU)].

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Related mapping to DataDredgingBias is supported.

Exact FDP distribution, moment, variance, and LFC analyses for step-up and step-down multiple-testing procedures directly quantify and control false discovery rates, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).

### conditional-binomial-step-up-fdp-law-and-stirling-moment-formula

evidence: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Supported by Section 3.1.1 Theorem 3.1, Equations (11)-(15), and Section 6.2.

Verified exact agreement between Theorem 3.1 conditional binomial law (Equation (11)) and Stirling-number moment formula (Equation (13)) for s = 1..4, and confirmed the Stirling-number correction magnitude 0.0138136097 for s = 3.

### non-binomial-step-down-conditional-law-and-finner-roters-lsd-fdr

evidence: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Supported by Section 2.4 Lemma 2.1, Section 3.1.2 Theorem 3.2, Equations (16)-(21), and Section 6.3.

Verified non-binomial conditional step-down distribution under F_1(u) = sqrt(u) (L1 gap 0.12385118) and exact agreement of Equations (20) and (21) for Dirac-uniform LSD (0.1346047661).

### condition-a-step-down-concave-lfc-and-negative-correlation-counterexample

evidence: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Supported by Section 3.2 Proposition 3.6, Section 4.1.1-4.1.2 Theorem 4.1, Corollary 4.2, Equations (24)-(26), and Section 6.4.

Verified Condition (A) monotonicity of S_{m,k} ([0.9137931, 0.95108711, 0.97138902, 0.98431953, 0.99333333, 1.0]), the SU vs SD LFC split on t_k = 0.9*(k/m)^{9/10}, and the m = 2 negative-correlation counterexample where FDR(LSU) = 0.0375 = 3*alpha/4.

### exact-lsu-fdp-variance-bounds-and-sparse-convergence-rate

evidence: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

Supported by Section 4.2 Theorem 4.3, Equations (28)-(30), and Section 6.5 Equation (35).

Verified exact agreement between Theorem 4.3 closed-form variance extrema and Theorem 3.1 second moments, as well as the sparse benchmark at m = 10000, alpha = 0.05, 1 - pi_0 = 0.01 (min SD(FDP) = 0.021685 ~= 0.0217).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis.

The full record is consistent; retain DRAFT.

Read every field of ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, four primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T161500Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis.json | supports | No normalized identity match for exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis across 442 pinned AIO records and 598 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides frequentist multiplicity error-control context via related_match. |
| calculation | research/discovery/exact-step-up-step-down-fdp-moments-and-lfc-analysis-boundaries.py | supports | Constructed analytical and numerical checks for Theorem 3.1 conditional binomial and Stirling-number FDP moments, Theorem 3.2 step-down FDR and Finner-Roters LSD formula, Proposition 3.6 negative-correlation counterexample, Theorem 4.1 Condition (A) and SU vs SD LFC split, and Theorem 4.3 FDP variance extrema. |
| roquain-villers2011-pdf | https://arxiv.org/pdf/1002.2845; Pages 584-612, Sections 1-6 (Lemma 2.1, Theorems 3.1-3.2, Corollaries 3.3-3.5, Proposition 3.6, Theorems 4.1 and 4.3, Corollary 4.2, Equations (1)-(35)) | supports | All 28 pages of the full-text PDF of arXiv:1002.2845v2 read. Checked all definitions, lemmas, theorems, corollaries, propositions, equations, and proofs. |
| roquain-villers2011-ar5iv | https://ar5iv.labs.arxiv.org/html/1002.2845; Lines 1-667, Sections 1-6 | supports | All 667 lines of the full-text ar5iv HTML conversion of arXiv:1002.2845v2 read. |
| roquain-villers2011-crossref | https://api.crossref.org/works/10.1214/10-AOS847; Annals of Statistics 39(1):584-612 publication record | supports | Official Annals of Statistics 39(1):584-612 Crossref record read and verified. |
| roquain-villers2011-abs | https://arxiv.org/abs/1002.2845; arXiv:1002.2845v2 abstract and metadata | supports | arXiv:1002.2845v2 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT exact step-up and step-down false discovery proportion moment formulas and least favorable configuration analysis record, yielding 599 native and 442 unchanged generated records.
- All 28 PDF pages and 667 ar5iv HTML lines of Roquain &amp; Villers (2011, arXiv:1002.2845v2) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T161700Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of exact step-up and step-down false discovery
  proportion moment formulas and least favorable configuration analysis
started_at: '2026-10-17T16:15:00Z'
finished_at: '2026-10-17T16:17:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from StepUpDownLeastFavorableConfigurationFDRBounds
    (Blanchard et al. 2014) and ArchimedeanCopulaStepUpFDRBounds (Bodnar & Dickhaus
    2014), verified the Stirling-number third-moment correction over Ferreira & Zwinderman
    (2006), checked the Section 6.4 Eq. (34) recurrence exponent slip versus the true
    monotonicity of S_{m,k} from Eq. (21), and verified the Theorem 4.3 FDP variance
    extrema. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain exact step-up and step-down false discovery proportion moment formulas
  and least favorable configuration analysis as a distinct DRAFT mathematical_method
  with a related DataDredgingBias mapping. All four claims and locators across Roquain
  & Villers (2011 Annals of Statistics 39(1):584-612) are supported with explicit
  Steck numerical stability, non-concave LFC, and Section 6.4 Eq. (34) recurrence
  limitations.
source:
  git_revision: a39e83ae6c1cf0cb5a001fd894ca8d9f1c98168a
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ArchimedeanCopulaStepUpFDRBounds.yaml
    sha256: 8a1f1f0ef3c4ec4ac45ede2c42f6ada4aaff38b4a6c59bf4d2fc18265aef96d7
    role: context
  - path: data/curated/ContinuumMeasureSpaceStepUpFDRControl.yaml
    sha256: 498a31bc6bb08aee30af0e7c6162801b1333a932df59620b4b1eb56820498444
    role: context
  - path: data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml
    sha256: d58e0d5d29e1c28fe4115471e06c8d76d0f66c4265c51c4cf4f33134c4091593
    role: target
  - path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
    sha256: 651276db83f388cdf782125e0ac769bacdb09ce89e63ebf1e9378b3a0d36d91f
    role: context
  - path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
    sha256: 03444e07e1d84f9bdc618210e31fc12764d6e8dc40c4311bef2fe5a40c0e7a80
    role: context
  - path: data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml
    sha256: 364829550c002d6abacfff66a6b7f140112c4985d9e1148925c2e81ea34a0342
    role: context
  - path: research/discovery/20261017T161500Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis.json
    sha256: 6c91f1621c4cad266a854a90d7b18d464b833a3432ada8e9bae5b7b3602f39ca
    role: context
  - path: research/discovery/exact-step-up-step-down-fdp-moments-and-lfc-analysis-boundaries.py
    sha256: 95c4d9b1902b15d3bf177024d9bc7999edf79656e7084241d1fc87649c7043f1
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
- target_id: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  path: data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml
  label: exact step-up and step-down false discovery proportion moment formulas and
    least favorable configuration analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ExactStepUpStepDownFDPMomentsAndLFCAnalysis
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
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
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: All 599 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Roquain-Villers 2011 exact step-up/step-down FDP moments, Condition
    (A), and FDP variance checks
  command: python3 research/discovery/exact-step-up-step-down-fdp-moments-and-lfc-analysis-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis\"\
    ,\n  \"primary_source\": \"Roquain & Villers (2011), Annals of Statistics 39(1):584-612\
    \ (arXiv:1002.2845v2, DOI:10.1214/10-AOS847)\",\n  \"theorem_3_1_moments_verification\"\
    : {\n    \"m\": 5,\n    \"pi0\": 0.6,\n    \"alpha\": 0.25,\n    \"moments_1_to_4\"\
    : {\n      \"1\": {\n        \"stirling_formula_eq13\": 0.15,\n        \"conditional_binomial_eq11\"\
    : 0.15\n      },\n      \"2\": {\n        \"stirling_formula_eq13\": 0.1170884792,\n\
    \        \"conditional_binomial_eq11\": 0.1170884792\n      },\n      \"3\": {\n\
    \        \"stirling_formula_eq13\": 0.101398793,\n        \"conditional_binomial_eq11\"\
    : 0.101398793\n      },\n      \"4\": {\n        \"stirling_formula_eq13\": 0.0934439164,\n\
    \        \"conditional_binomial_eq11\": 0.0934439164\n      }\n    },\n    \"\
    s3_omitting_stirling_factor_3\": 0.0875851833,\n    \"s3_stirling_correction_magnitude\"\
    : 0.0138136097\n  },\n  \"theorem_3_2_step_down_verification\": {\n    \"non_binomial_conditional_l1_gap\"\
    : 0.12385118,\n    \"lsd_fdr_m6_pi07_alpha02_uniform\": 0.1288390608,\n    \"\
    lsd_fdr_m6_pi07_alpha02_sqrt\": 0.1259581312,\n    \"lsd_fdr_m6_pi07_alpha02_dirac_eq20\"\
    : 0.1346047661,\n    \"lsd_fdr_m6_pi07_alpha02_dirac_eq21\": 0.1346047661\n  },\n\
    \  \"proposition_3_6_negative_correlation_counterexample\": {\n    \"m\": 2,\n\
    \    \"m0\": 1,\n    \"alpha\": 0.05,\n    \"fdr_lsu_at_rho_minus_1\": 0.0375,\n\
    \    \"benjamini_yekutieli_upper_bound\": 0.0375,\n    \"dirac_uniform_fdr\":\
    \ 0.025\n  },\n  \"theorem_4_1_condition_a_and_su_vs_sd_lfc_split\": {\n    \"\
    s_lsd_m6_alpha02_true\": [\n      0.9137931,\n      0.95108711,\n      0.97138902,\n\
    \      0.98431953,\n      0.99333333,\n      1.0\n    ],\n    \"s_lsd_m6_alpha02_recursion_eq34\"\
    : [\n      0.87484276,\n      0.94031958,\n      0.96827094,\n      0.98363858,\n\
    \      0.99333333,\n      1.0\n    ],\n    \"eq34_max_discrepancy\": 0.03895035,\n\
    \    \"q_concave_t_m5\": [\n      0.11466412,\n      0.13277095,\n      0.14706628,\n\
    \      0.16120651,\n      0.18\n    ],\n    \"fdr_su_concave_t_uniform_f1\": 0.45956142,\n\
    \    \"fdr_su_concave_t_dirac_f1\": 0.453016,\n    \"fdr_sd_concave_t_uniform_f1\"\
    : 0.34753598,\n    \"fdr_sd_concave_t_dirac_f1\": 0.41564914\n  },\n  \"theorem_4_3_fdp_variance_extrema\"\
    : {\n    \"small_m6_pi07_alpha02\": {\n      \"var_min_eq29\": 0.05630184,\n \
    \     \"sd_min\": 0.2372800877,\n      \"var_min_concave\": 0.1134,\n      \"\
    sd_min_concave\": 0.3367491648,\n      \"var_max_eq30\": 0.1204,\n      \"sd_max\"\
    : 0.3469870315\n    },\n    \"sparse_m10000_pi099_alpha005\": {\n      \"sd_min\"\
    : 0.021685,\n      \"sd_min_concave\": 0.216852,\n      \"sd_max\": 0.21691,\n\
    \      \"var_min\": 0.00047025,\n      \"var_max\": 0.04704975\n    }\n  },\n\
    \  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T161500Z-exact-step-up-step-down-fdp-moments-and-lfc-analysis.json
  accessed_at: '2026-10-17T16:15:00Z'
  support: supports
  summary: No normalized identity match for exact step-up and step-down false discovery
    proportion moment formulas and least favorable configuration analysis across 442
    pinned AIO records and 598 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T16:15:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides frequentist multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/exact-step-up-step-down-fdp-moments-and-lfc-analysis-boundaries.py
  accessed_at: '2026-10-17T16:15:00Z'
  snapshot_sha256: 95c4d9b1902b15d3bf177024d9bc7999edf79656e7084241d1fc87649c7043f1
  support: supports
  summary: Constructed analytical and numerical checks for Theorem 3.1 conditional
    binomial and Stirling-number FDP moments, Theorem 3.2 step-down FDR and Finner-Roters
    LSD formula, Proposition 3.6 negative-correlation counterexample, Theorem 4.1
    Condition (A) and SU vs SD LFC split, and Theorem 4.3 FDP variance extrema.
- evidence_id: roquain-villers2011-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1002.2845
  locator: Pages 584-612, Sections 1-6 (Lemma 2.1, Theorems 3.1-3.2, Corollaries 3.3-3.5,
    Proposition 3.6, Theorems 4.1 and 4.3, Corollary 4.2, Equations (1)-(35))
  accessed_at: '2026-10-17T16:15:00Z'
  snapshot_sha256: 363776dd96ab56cb24dcbee7bd09b88d2809d0b07076554ecad504a55fe1303d
  support: supports
  summary: All 28 pages of the full-text PDF of arXiv:1002.2845v2 read. Checked all
    definitions, lemmas, theorems, corollaries, propositions, equations, and proofs.
- evidence_id: roquain-villers2011-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1002.2845
  locator: Lines 1-667, Sections 1-6
  accessed_at: '2026-10-17T16:15:00Z'
  snapshot_sha256: 3e487cf3fae9c8bd51998eeb36fb15ea701384d3a9c8f6c2f422b887e5679b42
  support: supports
  summary: All 667 lines of the full-text ar5iv HTML conversion of arXiv:1002.2845v2
    read.
- evidence_id: roquain-villers2011-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/10-AOS847
  locator: Annals of Statistics 39(1):584-612 publication record
  accessed_at: '2026-10-17T16:15:00Z'
  snapshot_sha256: 80297b7f626cb3769379ba12c3fcf3c85c2d54b247f630e7acf366d3e6278e48
  support: supports
  summary: Official Annals of Statistics 39(1):584-612 Crossref record read and verified.
- evidence_id: roquain-villers2011-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1002.2845
  locator: arXiv:1002.2845v2 abstract and metadata
  accessed_at: '2026-10-17T16:15:00Z'
  snapshot_sha256: b211939e19d7d28a8f619a5c6c7c1c8dbae95748267bdbc62285e9ad88cb1cd2
  support: supports
  summary: arXiv:1002.2845v2 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ExactStepUpStepDownFDPMomentsAndLFCAnalysis versus StepUpDownLeastFavorableConfigurationFDRBounds
    and ArchimedeanCopulaStepUpFDRBounds
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - identity
  - roquain-villers2011-pdf
  - roquain-villers2011-crossref
  summary: Retain exact step-up and step-down false discovery proportion moment formulas
    and least favorable configuration analysis as a distinct DRAFT mathematical_method.
  details: ExactStepUpStepDownFDPMomentsAndLFCAnalysis establishes the conditional
    binomial law of step-up false rejections, the Stirling-number s-th moment formula
    for the FDP, the non-binomial conditional step-down law and exact joint rejection
    distribution, Condition (A) for step-down Dirac-uniform LFCs over concave alternatives,
    the m = 2 negatively correlated Gaussian counterexample attaining 3*alpha/4, and
    the exact closed-form minimum and maximum of Var[FDP(LSU)].
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - mapping
  - roquain-villers2011-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Exact FDP distribution, moment, variance, and LFC analyses for step-up
    and step-down multiple-testing procedures directly quantify and control false
    discovery rates, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).
- assessment_id: conditional-binomial-step-up-fdp-law-and-stirling-moment-formula
  area: evidence
  topic: conditional-binomial-step-up-fdp-law-and-stirling-moment-formula
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - roquain-villers2011-pdf
  - roquain-villers2011-ar5iv
  - calculation
  summary: Supported by Section 3.1.1 Theorem 3.1, Equations (11)-(15), and Section
    6.2.
  details: Verified exact agreement between Theorem 3.1 conditional binomial law (Equation
    (11)) and Stirling-number moment formula (Equation (13)) for s = 1..4, and confirmed
    the Stirling-number correction magnitude 0.0138136097 for s = 3.
- assessment_id: non-binomial-step-down-conditional-law-and-finner-roters-lsd-fdr
  area: evidence
  topic: non-binomial-step-down-conditional-law-and-finner-roters-lsd-fdr
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - roquain-villers2011-pdf
  - roquain-villers2011-ar5iv
  - calculation
  summary: Supported by Section 2.4 Lemma 2.1, Section 3.1.2 Theorem 3.2, Equations
    (16)-(21), and Section 6.3.
  details: Verified non-binomial conditional step-down distribution under F_1(u) =
    sqrt(u) (L1 gap 0.12385118) and exact agreement of Equations (20) and (21) for
    Dirac-uniform LSD (0.1346047661).
- assessment_id: condition-a-step-down-concave-lfc-and-negative-correlation-counterexample
  area: evidence
  topic: condition-a-step-down-concave-lfc-and-negative-correlation-counterexample
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - roquain-villers2011-pdf
  - roquain-villers2011-ar5iv
  - calculation
  summary: Supported by Section 3.2 Proposition 3.6, Section 4.1.1-4.1.2 Theorem 4.1,
    Corollary 4.2, Equations (24)-(26), and Section 6.4.
  details: Verified Condition (A) monotonicity of S_{m,k} ([0.9137931, 0.95108711,
    0.97138902, 0.98431953, 0.99333333, 1.0]), the SU vs SD LFC split on t_k = 0.9*(k/m)^{9/10},
    and the m = 2 negative-correlation counterexample where FDR(LSU) = 0.0375 = 3*alpha/4.
- assessment_id: exact-lsu-fdp-variance-bounds-and-sparse-convergence-rate
  area: evidence
  topic: exact-lsu-fdp-variance-bounds-and-sparse-convergence-rate
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - roquain-villers2011-pdf
  - roquain-villers2011-ar5iv
  - calculation
  summary: Supported by Section 4.2 Theorem 4.3, Equations (28)-(30), and Section
    6.5 Equation (35).
  details: Verified exact agreement between Theorem 4.3 closed-form variance extrema
    and Theorem 3.1 second moments, as well as the sparse benchmark at m = 10000,
    alpha = 0.05, 1 - pi_0 = 0.01 (min SD(FDP) = 0.021685 ~= 0.0217).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ExactStepUpStepDownFDPMomentsAndLFCAnalysis
  evidence_ids:
  - identity
  - mapping
  - roquain-villers2011-pdf
  - roquain-villers2011-ar5iv
  - roquain-villers2011-crossref
  - roquain-villers2011-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, four primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT exact step-up and step-down false discovery proportion moment formulas
  and least favorable configuration analysis record, yielding 599 native and 442 unchanged
  generated records.
- All 28 PDF pages and 667 ar5iv HTML lines of Roquain & Villers (2011, arXiv:1002.2845v2)
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- false-discovery-proportion
- least-favorable-configuration
- self-review
- discovery-ongoing
```
