# Scientific author self-review of Step-up-down least favorable configuration and two-population Steck false discovery rate bounds

- Review: 20261017T155700Z-step-up-down-least-favorable-configuration-fdr-bounds
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T15:55:00Z
- Finished UTC: 2026-10-17T15:57:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Step-up-down least favorable configuration and two-population Steck false discovery rate bounds as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Blanchard, Dickhaus, Roquain, &amp; Villers (2014 Statistica Sinica 24(1):1-23) are supported with explicit intermediate-order LFC failure, sparsity-regime, and AORC order limitations.

## Scope And Provenance

All fields of the exact maintained StepUpDownLeastFavorableConfigurationFDRBounds record and its primary evidence.

Selection: Exact maintained ID: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ccadcce0663ae9fa879c1113daf1502961fee44.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml | maintained | Step-up-down least favorable configuration and two-population Steck false discovery rate bounds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | All 597 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | Exited 0 without output. |
| Constructed Blanchard-Dickhaus-Roquain-Villers 2014 step-up-down LFC and Steck recursion checks | passed | True | AIMech:StepUpDownLeastFavorableConfigurationFDRBounds | {<br>  "concept_id": "AIMech:StepUpDownLeastFavorableConfigurationFDRBounds",<br>  "primary_source": "Blanchard, Dickhaus, Roquain, &amp; Villers (2014), Statistica Sinica 24(1):1-23 (arXiv:1108.5262v1, DOI:10.5705/ss.2011.205)",<br>  "proposition_4_1_counterexample": {<br>    "m": 10,<br>    "m0": 7,<br>    "alpha": 0.5,<br>    "fm_fdr_uniform_alt": {<br>      "1": 0.280884,<br>      "2": 0.320328,<br>      "3": 0.33568,<br>      "4": 0.342981,<br>      "5": 0.346685,<br>      "6": 0.348561,<br>      "7": 0.349461,<br>      "8": 0.349844,<br>      "9": 0.349974,<br>      "10": 0.35<br>    },<br>    "fm_fdr_dirac_uniform": {<br>      "1": 0.32985,<br>      "2": 0.32985,<br>      "3": 0.32985,<br>      "4": 0.32985,<br>      "5": 0.336128,<br>      "6": 0.342451,<br>      "7": 0.346717,<br>      "8": 0.348944,<br>      "9": 0.349806,<br>      "10": 0.35<br>    },<br>    "rm_fdr_uniform_alt": {<br>      "1": 0.280884,<br>      "2": 0.320328,<br>      "3": 0.33568,<br>      "4": 0.342981,<br>      "5": 0.346685,<br>      "6": 0.348561,<br>      "7": 0.349461,<br>      "8": 0.349844,<br>      "9": 0.349974,<br>      "10": 0.35<br>    },<br>    "rm_fdr_dirac_uniform": {<br>      "1": 0.324164,<br>      "2": 0.325755,<br>      "3": 0.329258,<br>      "4": 0.33406,<br>      "5": 0.339161,<br>      "6": 0.34364,<br>      "7": 0.34693,<br>      "8": 0.348897,<br>      "9": 0.349774,<br>      "10": 0.35<br>    },<br>    "counterexample_lambdas_fm": [<br>      3,<br>      4,<br>      5,<br>      6,<br>      7,<br>      8,<br>      9<br>    ],<br>    "counterexample_lambdas_rm": [<br>      3,<br>      4,<br>      5,<br>      6,<br>      7,<br>      8,<br>      9<br>    ]<br>  },<br>  "lemma_4_3_figure_6_bracketing": {<br>    "k_hat_over_m_lam8": 0.7,<br>    "u_lam8_lower": 0.7,<br>    "k_hat_over_m_lam4": 0.7,<br>    "u_lam4_lower": 0.4,<br>    "u_lam4_upper": 0.8<br>  },<br>  "theorem_4_4_and_corollary_4_5_rates": {<br>    "100": {<br>      "delta_m": 0.172838,<br>      "fdr_excess_upper_bound_linear": 0.195683,<br>      "scaled_by_sqrt_log_m_over_m": 0.911863<br>    },<br>    "1000": {<br>      "delta_m": 0.060812,<br>      "fdr_excess_upper_bound_linear": 0.056525,<br>      "scaled_by_sqrt_log_m_over_m": 0.680098<br>    },<br>    "10000": {<br>      "delta_m": 0.021661,<br>      "fdr_excess_upper_bound_linear": 0.019789,<br>      "scaled_by_sqrt_log_m_over_m": 0.652057<br>    },<br>    "100000": {<br>      "delta_m": 0.007607,<br>      "fdr_excess_upper_bound_linear": 0.007018,<br>      "scaled_by_sqrt_log_m_over_m": 0.654045<br>    }<br>  },<br>  "lemma_b_1_extreme_sd_exceeds_su": {<br>    "t0": 0.2,<br>    "critical_t0": 0.158018,<br>    "fdr_sd": 0.790285,<br>    "fdr_su": 0.7<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### StepUpDownLeastFavorableConfigurationFDRBounds versus SelfConsistencyAndDependencyControlFDRFramework and ContinuumMeasureSpaceStepUpFDRControl

identity: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Retain Step-up-down least favorable configuration and two-population Steck false discovery rate bounds as a distinct DRAFT mathematical_method.

StepUpDownLeastFavorableConfigurationFDRBounds establishes the two-population generalized Steck recursion (Proposition 5.1), disproves the finite-sample Dirac-uniform LFC conjecture for intermediate linear step-up-down procedures (Proposition 4.1), and derives continuous fixed-point bracketing and DKW perturbation bounds (Lemma 4.3, Theorem 4.4, Corollary 4.5), which are not covered by countable self-consistency or continuum step-up records.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Related mapping to DataDredgingBias is supported.

Step-up-down multiple testing procedures and their finite-sample LFC and perturbation bounds control false discoveries across simultaneous tests, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).

### two-population-steck-recursion-and-exact-sud-fdr

evidence: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Supported by Section 5.1-5.2 Proposition 5.1, Theorem 5.2, Corollary 5.3, and Section 7.1.

Verified two-population Steck recursion against one-population Steck recursion when F(u)=u and cross-checked exact RM FDR via binomial conditioning vs Equation (26).

### intermediate-lsud-dirac-uniform-lfc-counterexample

evidence: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Supported by Section 4.1 Proposition 4.1, Equation (8), and Figure 3.

Verified exact counterexample at m = 10, m_0 = 7, alpha = 0.5 across all lambda in [3, 4, 5, 6, 7, 8, 9] in both FM and RM models.

### continuous-threshold-bracketing-and-dkw-perturbation-bound

evidence: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Supported by Section 4.2 Definition 4.2, Lemma 4.3, Theorem 4.4, and Section 7.2-7.3.

Verified Lemma 4.3 continuous fixed-point bracketing on the Figure 6 configuration: U_lower = 0.4 &lt;= hat_k/m = 0.7 &lt;= U_upper = 0.8.

### vanishing-rate-for-linear-and-aorc-step-up-down

evidence: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

Supported by Section 4.2 Examples 1-2, Section 4.3 Corollary 4.5, and Section 7.4.

Verified O(sqrt((log m)/m)) decay of Theorem 4.4 / Corollary 4.5 perturbation bound across m in {100, 1000, 10000, 100000} (at m = 100000: bound = 0.007018).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds.

The full record is consistent; retain DRAFT.

Read every field of StepUpDownLeastFavorableConfigurationFDRBounds.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, four primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T155500Z-step-up-down-least-favorable-configuration-fdr-bounds.json | supports | No normalized identity match for Step-up-down least favorable configuration and two-population Steck false discovery rate bounds across 442 pinned AIO records and 596 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides frequentist multiplicity error-control context via related_match. |
| calculation | research/discovery/step-up-down-least-favorable-configuration-fdr-bounds-boundaries.py | supports | Constructed analytical and numerical checks for Proposition 5.1 two-population Steck recursion, Corollary 5.3 exact SUD FDR in FM and RM, Proposition 4.1 finite-sample counterexample to the Dirac-uniform LFC conjecture, Lemma 4.3 continuous fixed-point bracketing, Theorem 4.4 and Corollary 4.5 perturbation bounds, and Lemma B.1. |
| blanchard-dickhaus-roquain-villers2014-pdf | https://arxiv.org/pdf/1108.5262; Pages 1-33, Sections 1-7 and Appendices A-C (Definitions 2.1-2.2, Theorem 3.1, Conjecture 3.2, Proposition 4.1, Definition 4.2, Lemma 4.3, Theorem 4.4, Corollary 4.5, Proposition 5.1, Theorem 5.2, Corollary 5.3, Corollary A.1, Lemma B.1, Lemma C.1) | supports | All 33 pages of the full-text PDF of arXiv:1108.5262v1 read. Checked all definitions, lemmas, propositions, theorems, corollaries, and proofs. |
| blanchard-dickhaus-roquain-villers2014-ar5iv | https://ar5iv.labs.arxiv.org/html/1108.5262; Lines 1-987, Sections 1-7 and Appendices A-C | supports | All 987 lines of the full-text ar5iv HTML conversion of arXiv:1108.5262v1 read. |
| blanchard-dickhaus-roquain-villers2014-crossref | https://api.crossref.org/works/10.5705/ss.2011.205; Statistica Sinica 24(1):1-23 publication record | supports | Official Statistica Sinica 24(1):1-23 Crossref record read and verified. |
| blanchard-dickhaus-roquain-villers2014-abs | https://arxiv.org/abs/1108.5262; arXiv:1108.5262v1 abstract and metadata | supports | arXiv:1108.5262v1 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Step-up-down least favorable configuration and two-population Steck false discovery rate bounds record, yielding 597 native and 442 unchanged generated records.
- All 33 PDF pages and 987 ar5iv HTML lines of Blanchard, Dickhaus, Roquain, &amp; Villers (2014, arXiv:1108.5262v1) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T155700Z-step-up-down-least-favorable-configuration-fdr-bounds
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Step-up-down least favorable configuration
  and two-population Steck false discovery rate bounds
started_at: '2026-10-17T15:55:00Z'
finished_at: '2026-10-17T15:57:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SelfConsistencyAndDependencyControlFDRFramework
    (Blanchard & Roquain 2008), OneAndTwoStageAdaptiveStepUpFDRUnderDependence (Blanchard
    & Roquain 2009), and ContinuumMeasureSpaceStepUpFDRControl (Blanchard, Delattre,
    & Roquain 2014), verified the finite-sample failure of the Dirac-uniform LFC for
    intermediate LSUD_lambda across all lambda in {1, ..., 10}, checked the sparsity
    constraint (1 - zeta_m)^{-1} sqrt((log m)/m) = o(1) and AORC order constraint
    lambda_m/m < v_delta, and verified Lemma B.1 where FDR(SD) > FDR(SU). This is
    adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Step-up-down least favorable configuration and two-population Steck
  false discovery rate bounds as a distinct DRAFT mathematical_method with a related
  DataDredgingBias mapping. All four claims and locators across Blanchard, Dickhaus,
  Roquain, & Villers (2014 Statistica Sinica 24(1):1-23) are supported with explicit
  intermediate-order LFC failure, sparsity-regime, and AORC order limitations.
source:
  git_revision: 9ccadcce0663ae9fa879c1113daf1502961fee44
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ContinuumMeasureSpaceStepUpFDRControl.yaml
    sha256: 498a31bc6bb08aee30af0e7c6162801b1333a932df59620b4b1eb56820498444
    role: context
  - path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
    sha256: 651276db83f388cdf782125e0ac769bacdb09ce89e63ebf1e9378b3a0d36d91f
    role: context
  - path: data/curated/OptimalSpjotvollAndSieveGroupedPValueWeighting.yaml
    sha256: 5bcc259bbbe4758e8fff9ec95e7b7c967e7431c39327bad2b771284bcf9e1841
    role: context
  - path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
    sha256: 03444e07e1d84f9bdc618210e31fc12764d6e8dc40c4311bef2fe5a40c0e7a80
    role: context
  - path: data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml
    sha256: 364829550c002d6abacfff66a6b7f140112c4985d9e1148925c2e81ea34a0342
    role: target
  - path: research/discovery/20261017T155500Z-step-up-down-least-favorable-configuration-fdr-bounds.json
    sha256: cd2bd4ad996d4d1a5e97b05f5f265961e415eeb33ef63d3b7ecd2a62c4d948a9
    role: context
  - path: research/discovery/step-up-down-least-favorable-configuration-fdr-bounds-boundaries.py
    sha256: bc5c1e73bdf0ad38b5e1c0a9b58781cd7ee995b6cff434bb7aba6dc69f509e17
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
- target_id: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  path: data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml
  label: Step-up-down least favorable configuration and two-population Steck false
    discovery rate bounds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StepUpDownLeastFavorableConfigurationFDRBounds.yaml
    role: maintained
scope:
  description: All fields of the exact maintained StepUpDownLeastFavorableConfigurationFDRBounds
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:StepUpDownLeastFavorableConfigurationFDRBounds'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
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
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 597 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Blanchard-Dickhaus-Roquain-Villers 2014 step-up-down LFC and Steck
    recursion checks
  command: python3 research/discovery/step-up-down-least-favorable-configuration-fdr-bounds-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:StepUpDownLeastFavorableConfigurationFDRBounds\"\
    ,\n  \"primary_source\": \"Blanchard, Dickhaus, Roquain, & Villers (2014), Statistica\
    \ Sinica 24(1):1-23 (arXiv:1108.5262v1, DOI:10.5705/ss.2011.205)\",\n  \"proposition_4_1_counterexample\"\
    : {\n    \"m\": 10,\n    \"m0\": 7,\n    \"alpha\": 0.5,\n    \"fm_fdr_uniform_alt\"\
    : {\n      \"1\": 0.280884,\n      \"2\": 0.320328,\n      \"3\": 0.33568,\n \
    \     \"4\": 0.342981,\n      \"5\": 0.346685,\n      \"6\": 0.348561,\n     \
    \ \"7\": 0.349461,\n      \"8\": 0.349844,\n      \"9\": 0.349974,\n      \"10\"\
    : 0.35\n    },\n    \"fm_fdr_dirac_uniform\": {\n      \"1\": 0.32985,\n     \
    \ \"2\": 0.32985,\n      \"3\": 0.32985,\n      \"4\": 0.32985,\n      \"5\":\
    \ 0.336128,\n      \"6\": 0.342451,\n      \"7\": 0.346717,\n      \"8\": 0.348944,\n\
    \      \"9\": 0.349806,\n      \"10\": 0.35\n    },\n    \"rm_fdr_uniform_alt\"\
    : {\n      \"1\": 0.280884,\n      \"2\": 0.320328,\n      \"3\": 0.33568,\n \
    \     \"4\": 0.342981,\n      \"5\": 0.346685,\n      \"6\": 0.348561,\n     \
    \ \"7\": 0.349461,\n      \"8\": 0.349844,\n      \"9\": 0.349974,\n      \"10\"\
    : 0.35\n    },\n    \"rm_fdr_dirac_uniform\": {\n      \"1\": 0.324164,\n    \
    \  \"2\": 0.325755,\n      \"3\": 0.329258,\n      \"4\": 0.33406,\n      \"5\"\
    : 0.339161,\n      \"6\": 0.34364,\n      \"7\": 0.34693,\n      \"8\": 0.348897,\n\
    \      \"9\": 0.349774,\n      \"10\": 0.35\n    },\n    \"counterexample_lambdas_fm\"\
    : [\n      3,\n      4,\n      5,\n      6,\n      7,\n      8,\n      9\n   \
    \ ],\n    \"counterexample_lambdas_rm\": [\n      3,\n      4,\n      5,\n   \
    \   6,\n      7,\n      8,\n      9\n    ]\n  },\n  \"lemma_4_3_figure_6_bracketing\"\
    : {\n    \"k_hat_over_m_lam8\": 0.7,\n    \"u_lam8_lower\": 0.7,\n    \"k_hat_over_m_lam4\"\
    : 0.7,\n    \"u_lam4_lower\": 0.4,\n    \"u_lam4_upper\": 0.8\n  },\n  \"theorem_4_4_and_corollary_4_5_rates\"\
    : {\n    \"100\": {\n      \"delta_m\": 0.172838,\n      \"fdr_excess_upper_bound_linear\"\
    : 0.195683,\n      \"scaled_by_sqrt_log_m_over_m\": 0.911863\n    },\n    \"1000\"\
    : {\n      \"delta_m\": 0.060812,\n      \"fdr_excess_upper_bound_linear\": 0.056525,\n\
    \      \"scaled_by_sqrt_log_m_over_m\": 0.680098\n    },\n    \"10000\": {\n \
    \     \"delta_m\": 0.021661,\n      \"fdr_excess_upper_bound_linear\": 0.019789,\n\
    \      \"scaled_by_sqrt_log_m_over_m\": 0.652057\n    },\n    \"100000\": {\n\
    \      \"delta_m\": 0.007607,\n      \"fdr_excess_upper_bound_linear\": 0.007018,\n\
    \      \"scaled_by_sqrt_log_m_over_m\": 0.654045\n    }\n  },\n  \"lemma_b_1_extreme_sd_exceeds_su\"\
    : {\n    \"t0\": 0.2,\n    \"critical_t0\": 0.158018,\n    \"fdr_sd\": 0.790285,\n\
    \    \"fdr_su\": 0.7\n  },\n  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T155500Z-step-up-down-least-favorable-configuration-fdr-bounds.json
  accessed_at: '2026-10-17T15:55:00Z'
  support: supports
  summary: No normalized identity match for Step-up-down least favorable configuration
    and two-population Steck false discovery rate bounds across 442 pinned AIO records
    and 596 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T15:55:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides frequentist multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/step-up-down-least-favorable-configuration-fdr-bounds-boundaries.py
  accessed_at: '2026-10-17T15:55:00Z'
  snapshot_sha256: bc5c1e73bdf0ad38b5e1c0a9b58781cd7ee995b6cff434bb7aba6dc69f509e17
  support: supports
  summary: Constructed analytical and numerical checks for Proposition 5.1 two-population
    Steck recursion, Corollary 5.3 exact SUD FDR in FM and RM, Proposition 4.1 finite-sample
    counterexample to the Dirac-uniform LFC conjecture, Lemma 4.3 continuous fixed-point
    bracketing, Theorem 4.4 and Corollary 4.5 perturbation bounds, and Lemma B.1.
- evidence_id: blanchard-dickhaus-roquain-villers2014-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1108.5262
  locator: Pages 1-33, Sections 1-7 and Appendices A-C (Definitions 2.1-2.2, Theorem
    3.1, Conjecture 3.2, Proposition 4.1, Definition 4.2, Lemma 4.3, Theorem 4.4,
    Corollary 4.5, Proposition 5.1, Theorem 5.2, Corollary 5.3, Corollary A.1, Lemma
    B.1, Lemma C.1)
  accessed_at: '2026-10-17T15:55:00Z'
  snapshot_sha256: 3276246bf48077619f74aa42f44a9707d4dab17309e1fb1377814a3321453bd1
  support: supports
  summary: All 33 pages of the full-text PDF of arXiv:1108.5262v1 read. Checked all
    definitions, lemmas, propositions, theorems, corollaries, and proofs.
- evidence_id: blanchard-dickhaus-roquain-villers2014-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1108.5262
  locator: Lines 1-987, Sections 1-7 and Appendices A-C
  accessed_at: '2026-10-17T15:55:00Z'
  snapshot_sha256: ff44c60469e2615968d6008f77ade067d262e89dd3854daf870f371c727ac4aa
  support: supports
  summary: All 987 lines of the full-text ar5iv HTML conversion of arXiv:1108.5262v1
    read.
- evidence_id: blanchard-dickhaus-roquain-villers2014-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.5705/ss.2011.205
  locator: Statistica Sinica 24(1):1-23 publication record
  accessed_at: '2026-10-17T15:55:00Z'
  snapshot_sha256: b5a8c00ddcee85cd3f63afdadbd4b1313692f2afb9c65184c662c9dfda69580b
  support: supports
  summary: Official Statistica Sinica 24(1):1-23 Crossref record read and verified.
- evidence_id: blanchard-dickhaus-roquain-villers2014-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1108.5262
  locator: arXiv:1108.5262v1 abstract and metadata
  accessed_at: '2026-10-17T15:55:00Z'
  snapshot_sha256: 3a141ad1099f65a122b41b04ca60754c794d396a3011dfb77cb10de14fc7a4a2
  support: supports
  summary: arXiv:1108.5262v1 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: StepUpDownLeastFavorableConfigurationFDRBounds versus SelfConsistencyAndDependencyControlFDRFramework
    and ContinuumMeasureSpaceStepUpFDRControl
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - identity
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-crossref
  summary: Retain Step-up-down least favorable configuration and two-population Steck
    false discovery rate bounds as a distinct DRAFT mathematical_method.
  details: StepUpDownLeastFavorableConfigurationFDRBounds establishes the two-population
    generalized Steck recursion (Proposition 5.1), disproves the finite-sample Dirac-uniform
    LFC conjecture for intermediate linear step-up-down procedures (Proposition 4.1),
    and derives continuous fixed-point bracketing and DKW perturbation bounds (Lemma
    4.3, Theorem 4.4, Corollary 4.5), which are not covered by countable self-consistency
    or continuum step-up records.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - mapping
  - blanchard-dickhaus-roquain-villers2014-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Step-up-down multiple testing procedures and their finite-sample LFC and
    perturbation bounds control false discoveries across simultaneous tests, mitigating
    multiplicity-induced false positives (AIO:DataDredgingBias).
- assessment_id: two-population-steck-recursion-and-exact-sud-fdr
  area: evidence
  topic: two-population-steck-recursion-and-exact-sud-fdr
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-ar5iv
  - calculation
  summary: Supported by Section 5.1-5.2 Proposition 5.1, Theorem 5.2, Corollary 5.3,
    and Section 7.1.
  details: Verified two-population Steck recursion against one-population Steck recursion
    when F(u)=u and cross-checked exact RM FDR via binomial conditioning vs Equation
    (26).
- assessment_id: intermediate-lsud-dirac-uniform-lfc-counterexample
  area: evidence
  topic: intermediate-lsud-dirac-uniform-lfc-counterexample
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-ar5iv
  - calculation
  summary: Supported by Section 4.1 Proposition 4.1, Equation (8), and Figure 3.
  details: Verified exact counterexample at m = 10, m_0 = 7, alpha = 0.5 across all
    lambda in [3, 4, 5, 6, 7, 8, 9] in both FM and RM models.
- assessment_id: continuous-threshold-bracketing-and-dkw-perturbation-bound
  area: evidence
  topic: continuous-threshold-bracketing-and-dkw-perturbation-bound
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-ar5iv
  - calculation
  summary: Supported by Section 4.2 Definition 4.2, Lemma 4.3, Theorem 4.4, and Section
    7.2-7.3.
  details: 'Verified Lemma 4.3 continuous fixed-point bracketing on the Figure 6 configuration:
    U_lower = 0.4 <= hat_k/m = 0.7 <= U_upper = 0.8.'
- assessment_id: vanishing-rate-for-linear-and-aorc-step-up-down
  area: evidence
  topic: vanishing-rate-for-linear-and-aorc-step-up-down
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-ar5iv
  - calculation
  summary: Supported by Section 4.2 Examples 1-2, Section 4.3 Corollary 4.5, and Section
    7.4.
  details: 'Verified O(sqrt((log m)/m)) decay of Theorem 4.4 / Corollary 4.5 perturbation
    bound across m in {100, 1000, 10000, 100000} (at m = 100000: bound = 0.007018).'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:StepUpDownLeastFavorableConfigurationFDRBounds
  evidence_ids:
  - identity
  - mapping
  - blanchard-dickhaus-roquain-villers2014-pdf
  - blanchard-dickhaus-roquain-villers2014-ar5iv
  - blanchard-dickhaus-roquain-villers2014-crossref
  - blanchard-dickhaus-roquain-villers2014-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of StepUpDownLeastFavorableConfigurationFDRBounds.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, four primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Step-up-down least favorable configuration and two-population Steck
  false discovery rate bounds record, yielding 597 native and 442 unchanged generated
  records.
- All 33 PDF pages and 987 ar5iv HTML lines of Blanchard, Dickhaus, Roquain, & Villers
  (2014, arXiv:1108.5262v1) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- step-up-down
- least-favorable-configuration
- steck-recursion
- self-review
- discovery-ongoing
```
