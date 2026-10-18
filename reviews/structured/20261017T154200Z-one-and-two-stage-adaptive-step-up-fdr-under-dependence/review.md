# Scientific author self-review of One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence

- Review: 20261017T154200Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T15:40:00Z
- Finished UTC: 2026-10-17T15:42:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Blanchard &amp; Roquain (2009 Journal of Machine Learning Research 10:2837-2871) are supported with explicit sparse-signal mu*, PRDS monotonicity reversal, and two-stage budget-splitting limitations.

## Scope And Provenance

All fields of the exact maintained OneAndTwoStageAdaptiveStepUpFDRUnderDependence record and its primary evidence.

Selection: Exact maintained ID: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7d173a1660b7ab82a2bb0f3bceda471b6c9a3ca6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml | maintained | One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | All 595 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | Exited 0 without output. |
| Constructed Blanchard-Roquain 2009 adaptive step-up FDR checks | passed | True | AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence | {<br>  "concept_id": "AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence",<br>  "primary_source": "Blanchard &amp; Roquain (2009), Journal of Machine Learning Research 10:2837-2871 (arXiv:0707.0536v3)",<br>  "section_3_1_br_1s_and_lemma_2": {<br>    "m": 10,<br>    "alpha": 0.05,<br>    "br_1s_alpha_thresholds_first5": [<br>      0.00475,<br>      0.010556,<br>      0.017813,<br>      0.027143,<br>      0.039583<br>    ],<br>    "lsu_thresholds_first5": [<br>      0.005,<br>      0.01,<br>      0.015,<br>      0.02,<br>      0.025<br>    ],<br>    "max_fdr_br_1s_alpha": 0.04649744,<br>    "lemma_2_mu_star_pi0_05_alpha_005": 1.511105,<br>    "asymptotic_lsu_rej_prop_mu_1_2": 0.008,<br>    "asymptotic_lsu_rej_prop_mu_2_0": 0.184<br>  },<br>  "section_3_2_plug_in_hierarchy": {<br>    "m": 10,<br>    "alpha": 0.05,<br>    "lambda": 0.05,<br>    "max_ratio_E_G1_times_pi0": 1.0,<br>    "first_stage_r0_lsu_count": 4,<br>    "first_stage_r0_br1s_count": 5,<br>    "G3_bky06": 1.142857,<br>    "G4_br2s": 1.333333,<br>    "G1_storey": 1.6,<br>    "second_stage_rejections": {<br>      "LSU": 1,<br>      "BKY06_alpha": 2,<br>      "BR_2S_alpha": 3,<br>      "Storey_alpha": 4<br>    }<br>  },<br>  "section_3_3_maximal_dependence": {<br>    "m": 20,<br>    "alpha": 0.05,<br>    "lambda_1": 0.045455,<br>    "lambda_2": 0.5,<br>    "fdr_storey_1_2": 0.5,<br>    "fdr_quant_median": 0.083333,<br>    "fdr_quant_k0_opt": 0.05,<br>    "fdr_br_1s_alpha": 0.05,<br>    "fdr_br_2s_alpha": 0.05,<br>    "fdr_bky06_alpha": 0.05,<br>    "fdr_storey_alpha": 0.05<br>  },<br>  "section_4_dependence_theorems_4_1_and_4_2": {<br>    "kappa": 2.0,<br>    "crossover_proportion_F2_inv_2": 0.625,<br>    "markov_factor_exact_equality_checked": true,<br>    "low_pi0_example_m20_m0_2": {<br>      "r0_holm_count": 15,<br>      "r0_lsu_alpha_over_4_count": 15,<br>      "f2_factor": 3.414214,<br>      "rejections_non_adaptive_lsu": 15,<br>      "rejections_theorem_4_1": 18,<br>      "rejections_theorem_4_2": 18<br>    }<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### OneAndTwoStageAdaptiveStepUpFDRUnderDependence versus SelfConsistencyAndDependencyControlFDRFramework

identity: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Retain One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence as a distinct DRAFT mathematical_method.

OneAndTwoStageAdaptiveStepUpFDRUnderDependence formulates the one-stage piecewise inverse-volume procedure BR-1S-lambda (Theorem 3.1) and Lemma 2 Gaussian signal threshold mu*, the unified coordinate-wise non-increasing plug-in theorem and two-stage BR-2S-lambda procedure (Theorem 3.2, Corollary 1), the exact comonotonic maximal-dependence FDR formulas (Proposition 1), and the Markov-inequality F_kappa two-stage FDR-to-FDR procedure under PRDS and arbitrary dependence (Theorem 4.2), which are not encoded in SelfConsistencyAndDependencyControlFDRFramework (Blanchard &amp; Roquain 2008).

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Related mapping to DataDredgingBias is supported.

One-stage and two-stage adaptive step-up procedures adjust step-up thresholds for the unknown null proportion pi_0 while controlling the finite-sample False Discovery Rate, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).

### one-stage-piecewise-inverse-volume-step-up-and-gaussian-signal-threshold

evidence: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Supported by Section 3.1 Theorem 3.1, Lemma 2, Appendix A.2, and Appendix B Lemma 7.

Verified exact finite-sample FDR bound for BR-1S-alpha (max FDR = 0.04649744 &lt;= 0.05) and Lemma 2 Gaussian signal threshold mu* = 1.511105.

### unified-plug-in-self-consistency-theorem-and-br-2s-dominance

evidence: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Supported by Section 3.2 Theorem 3.2, Corollary 1, and Appendix A.3.

Verified max_q pi_0 E[G_1(p_{0,h})] = 1.0 and strict plug-in hierarchy G_3 = 1.142857 &lt; G_4 = 1.333333 &lt; G_1 = 1.6 yielding second-stage rejections {'LSU': 1, 'BKY06_alpha': 2, 'BR_2S_alpha': 3, 'Storey_alpha': 4}.

### maximal-comonotonic-dependence-fdr-and-lambda-alpha-robustness

evidence: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Supported by Section 3.3 Proposition 1, Section 5.2, and Appendix A.4.

Verified comonotonic maximal-dependence FDR at m = 20, alpha = 0.05: Storey-1/2 FDR = 0.5 = 10 alpha and Quant-1/2 FDR = 0.083333, whereas BR-1S-alpha, BR-2S-alpha, BKY06-alpha, and Storey-alpha all achieve exact FDR = 0.05.

### two-stage-fwer-and-markov-fdr-adaptive-step-up-under-dependence

evidence: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

Supported by Section 4 Lemma 3, Theorems 4.1-4.2, and Appendix A.5.

Verified Markov transformation F_2(0.75) = 3.414214 with crossover proportion F_2^{-1}(2) = 0.625 and rejections increasing from 15 (LSU) to 18 (Theorems 4.1 &amp; 4.2).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence.

The full record is consistent; retain DRAFT.

Read every field of OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, two primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T154000Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence.json | supports | No normalized identity match for One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence across 442 pinned AIO records and 594 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides frequentist multiplicity error-control context via related_match. |
| calculation | research/discovery/one-and-two-stage-adaptive-step-up-fdr-under-dependence-boundaries.py | supports | Constructed analytical and numerical checks for Theorem 3.1 BR-1S-alpha finite-sample FDR bound and Lemma 2 Gaussian signal threshold mu*, Theorem 3.2 and Corollary 1 plug-in hierarchy G_3 &lt; G_4 &lt; G_1, Proposition 1 comonotonic maximal-dependence FDR formulas, and Theorems 4.1-4.2 two-stage FWER and Markov F_kappa adaptive step-up procedures. |
| blanchard-roquain2009-ar5iv | https://ar5iv.labs.arxiv.org/html/0707.0536; Sections 1-6 and Appendices A-B (lines 1-989, Theorems 3.1-3.2, Lemma 2, Corollary 1, Proposition 1, Lemma 3, Theorems 4.1-4.2, Lemma 7) | supports | All 989 lines of the full-text ar5iv HTML conversion of arXiv:0707.0536v3 read. Checked all definitions, lemmas, propositions, theorems, and Appendix A-B proofs. |
| blanchard-roquain2009-abs | https://arxiv.org/abs/0707.0536; arXiv:0707.0536v3 abstract and Journal of Machine Learning Research 10 (2009) 2837-2871 metadata | supports | arXiv:0707.0536v3 abstract and JMLR 10 (2009) 2837-2871 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT One-stage and two-stage adaptive step-up procedures for false discovery rate control under independence and dependence record, yielding 595 native and 442 unchanged generated records.
- All 989 lines of Blanchard &amp; Roquain (2009, arXiv:0707.0536v3) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T154200Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of One-stage and two-stage adaptive step-up procedures
  for false discovery rate control under independence and dependence
started_at: '2026-10-17T15:40:00Z'
finished_at: '2026-10-17T15:42:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SelfConsistencyAndDependencyControlFDRFramework
    (Blanchard & Roquain 2008), OptimalMultiWeightedStepUpProcedureForFDRControl (Roquain
    & van de Wiel 2009), and AdaptiveDataDrivenOptimalPValueWeighting (Durand 2019),
    the low-signal threshold mu* limitation for BR-1S-alpha (Lemma 2), the reversal
    of G(p) monotonicity between independence (Theorem 3.2) and PRDS (Lemma 3), and
    the high first-stage rejection crossover F_2^{-1}(2) = 0.625 required for Theorem
    4.2 to dominate non-adaptive step-up. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain One-stage and two-stage adaptive step-up procedures for false discovery
  rate control under independence and dependence as a distinct DRAFT mathematical_method
  with a related DataDredgingBias mapping. All four claims and locators across Blanchard
  & Roquain (2009 Journal of Machine Learning Research 10:2837-2871) are supported
  with explicit sparse-signal mu*, PRDS monotonicity reversal, and two-stage budget-splitting
  limitations.
source:
  git_revision: 7d173a1660b7ab82a2bb0f3bceda471b6c9a3ca6
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/AdaptiveDataDrivenOptimalPValueWeighting.yaml
    sha256: 87961708f5770edc0a05f6048c36f9d50507a48e453db008ec06cf37d9ecb32b
    role: context
  - path: data/curated/ConstrainedConvexPValueWeightingInMonotoneLikelihoodRatioFamilies.yaml
    sha256: 97415576de3471717aa4c965626803a592de772077e8fabab033968b49bd05e5
    role: context
  - path: data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml
    sha256: 84d7094933c475533243366de9802790a89da87fb149ceffcb6ff304eacd3cf9
    role: context
  - path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
    sha256: 651276db83f388cdf782125e0ac769bacdb09ce89e63ebf1e9378b3a0d36d91f
    role: target
  - path: data/curated/OptimalMultiWeightedStepUpProcedureForFDRControl.yaml
    sha256: 0ce681bedc7dae26198a31774cb3234dab960c9f788adebd3f28225aae14c1a8
    role: context
  - path: data/curated/OptimalSpjotvollAndSieveGroupedPValueWeighting.yaml
    sha256: 5bcc259bbbe4758e8fff9ec95e7b7c967e7431c39327bad2b771284bcf9e1841
    role: context
  - path: data/curated/SelfConsistencyAndDependencyControlFDRFramework.yaml
    sha256: 03444e07e1d84f9bdc618210e31fc12764d6e8dc40c4311bef2fe5a40c0e7a80
    role: context
  - path: research/discovery/20261017T154000Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence.json
    sha256: 4ae77eff4bc1bda047b286718ebd24fc63f65b44cd8a5ec0d1c837c48665bb74
    role: context
  - path: research/discovery/one-and-two-stage-adaptive-step-up-fdr-under-dependence-boundaries.py
    sha256: 2f6a3346c39be738333ae9b9ec214ced7192718d3ecb781afbfcb9997117f1b1
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
- target_id: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
  label: One-stage and two-stage adaptive step-up procedures for false discovery rate
    control under independence and dependence
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml
    role: maintained
scope:
  description: All fields of the exact maintained OneAndTwoStageAdaptiveStepUpFDRUnderDependence
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
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
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: All 595 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Blanchard-Roquain 2009 adaptive step-up FDR checks
  command: python3 research/discovery/one-and-two-stage-adaptive-step-up-fdr-under-dependence-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence\"\
    ,\n  \"primary_source\": \"Blanchard & Roquain (2009), Journal of Machine Learning\
    \ Research 10:2837-2871 (arXiv:0707.0536v3)\",\n  \"section_3_1_br_1s_and_lemma_2\"\
    : {\n    \"m\": 10,\n    \"alpha\": 0.05,\n    \"br_1s_alpha_thresholds_first5\"\
    : [\n      0.00475,\n      0.010556,\n      0.017813,\n      0.027143,\n     \
    \ 0.039583\n    ],\n    \"lsu_thresholds_first5\": [\n      0.005,\n      0.01,\n\
    \      0.015,\n      0.02,\n      0.025\n    ],\n    \"max_fdr_br_1s_alpha\":\
    \ 0.04649744,\n    \"lemma_2_mu_star_pi0_05_alpha_005\": 1.511105,\n    \"asymptotic_lsu_rej_prop_mu_1_2\"\
    : 0.008,\n    \"asymptotic_lsu_rej_prop_mu_2_0\": 0.184\n  },\n  \"section_3_2_plug_in_hierarchy\"\
    : {\n    \"m\": 10,\n    \"alpha\": 0.05,\n    \"lambda\": 0.05,\n    \"max_ratio_E_G1_times_pi0\"\
    : 1.0,\n    \"first_stage_r0_lsu_count\": 4,\n    \"first_stage_r0_br1s_count\"\
    : 5,\n    \"G3_bky06\": 1.142857,\n    \"G4_br2s\": 1.333333,\n    \"G1_storey\"\
    : 1.6,\n    \"second_stage_rejections\": {\n      \"LSU\": 1,\n      \"BKY06_alpha\"\
    : 2,\n      \"BR_2S_alpha\": 3,\n      \"Storey_alpha\": 4\n    }\n  },\n  \"\
    section_3_3_maximal_dependence\": {\n    \"m\": 20,\n    \"alpha\": 0.05,\n  \
    \  \"lambda_1\": 0.045455,\n    \"lambda_2\": 0.5,\n    \"fdr_storey_1_2\": 0.5,\n\
    \    \"fdr_quant_median\": 0.083333,\n    \"fdr_quant_k0_opt\": 0.05,\n    \"\
    fdr_br_1s_alpha\": 0.05,\n    \"fdr_br_2s_alpha\": 0.05,\n    \"fdr_bky06_alpha\"\
    : 0.05,\n    \"fdr_storey_alpha\": 0.05\n  },\n  \"section_4_dependence_theorems_4_1_and_4_2\"\
    : {\n    \"kappa\": 2.0,\n    \"crossover_proportion_F2_inv_2\": 0.625,\n    \"\
    markov_factor_exact_equality_checked\": true,\n    \"low_pi0_example_m20_m0_2\"\
    : {\n      \"r0_holm_count\": 15,\n      \"r0_lsu_alpha_over_4_count\": 15,\n\
    \      \"f2_factor\": 3.414214,\n      \"rejections_non_adaptive_lsu\": 15,\n\
    \      \"rejections_theorem_4_1\": 18,\n      \"rejections_theorem_4_2\": 18\n\
    \    }\n  },\n  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T154000Z-one-and-two-stage-adaptive-step-up-fdr-under-dependence.json
  accessed_at: '2026-10-17T15:40:00Z'
  support: supports
  summary: No normalized identity match for One-stage and two-stage adaptive step-up
    procedures for false discovery rate control under independence and dependence
    across 442 pinned AIO records and 594 maintained IDs, names, aliases and scoped
    synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T15:40:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides frequentist multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/one-and-two-stage-adaptive-step-up-fdr-under-dependence-boundaries.py
  accessed_at: '2026-10-17T15:40:00Z'
  snapshot_sha256: 2f6a3346c39be738333ae9b9ec214ced7192718d3ecb781afbfcb9997117f1b1
  support: supports
  summary: Constructed analytical and numerical checks for Theorem 3.1 BR-1S-alpha
    finite-sample FDR bound and Lemma 2 Gaussian signal threshold mu*, Theorem 3.2
    and Corollary 1 plug-in hierarchy G_3 < G_4 < G_1, Proposition 1 comonotonic maximal-dependence
    FDR formulas, and Theorems 4.1-4.2 two-stage FWER and Markov F_kappa adaptive
    step-up procedures.
- evidence_id: blanchard-roquain2009-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/0707.0536
  locator: Sections 1-6 and Appendices A-B (lines 1-989, Theorems 3.1-3.2, Lemma 2,
    Corollary 1, Proposition 1, Lemma 3, Theorems 4.1-4.2, Lemma 7)
  accessed_at: '2026-10-17T15:40:00Z'
  snapshot_sha256: aacce975911525720fafd136396a274f0b7afcbd9fc579bf5430478f5a791cd3
  support: supports
  summary: All 989 lines of the full-text ar5iv HTML conversion of arXiv:0707.0536v3
    read. Checked all definitions, lemmas, propositions, theorems, and Appendix A-B
    proofs.
- evidence_id: blanchard-roquain2009-abs
  kind: primary_source
  reference: https://arxiv.org/abs/0707.0536
  locator: arXiv:0707.0536v3 abstract and Journal of Machine Learning Research 10
    (2009) 2837-2871 metadata
  accessed_at: '2026-10-17T15:40:00Z'
  snapshot_sha256: 3670e39f2766195b8e4bdc30d402e063944b1d2e1fc1c588fcdcf46247ebd90e
  support: supports
  summary: arXiv:0707.0536v3 abstract and JMLR 10 (2009) 2837-2871 metadata read and
    verified.
assessments:
- assessment_id: identity
  area: identity
  topic: OneAndTwoStageAdaptiveStepUpFDRUnderDependence versus SelfConsistencyAndDependencyControlFDRFramework
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - identity
  - blanchard-roquain2009-ar5iv
  - blanchard-roquain2009-abs
  summary: Retain One-stage and two-stage adaptive step-up procedures for false discovery
    rate control under independence and dependence as a distinct DRAFT mathematical_method.
  details: OneAndTwoStageAdaptiveStepUpFDRUnderDependence formulates the one-stage
    piecewise inverse-volume procedure BR-1S-lambda (Theorem 3.1) and Lemma 2 Gaussian
    signal threshold mu*, the unified coordinate-wise non-increasing plug-in theorem
    and two-stage BR-2S-lambda procedure (Theorem 3.2, Corollary 1), the exact comonotonic
    maximal-dependence FDR formulas (Proposition 1), and the Markov-inequality F_kappa
    two-stage FDR-to-FDR procedure under PRDS and arbitrary dependence (Theorem 4.2),
    which are not encoded in SelfConsistencyAndDependencyControlFDRFramework (Blanchard
    & Roquain 2008).
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - mapping
  - blanchard-roquain2009-ar5iv
  summary: Related mapping to DataDredgingBias is supported.
  details: One-stage and two-stage adaptive step-up procedures adjust step-up thresholds
    for the unknown null proportion pi_0 while controlling the finite-sample False
    Discovery Rate, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).
- assessment_id: one-stage-piecewise-inverse-volume-step-up-and-gaussian-signal-threshold
  area: evidence
  topic: one-stage-piecewise-inverse-volume-step-up-and-gaussian-signal-threshold
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - blanchard-roquain2009-ar5iv
  - blanchard-roquain2009-abs
  - calculation
  summary: Supported by Section 3.1 Theorem 3.1, Lemma 2, Appendix A.2, and Appendix
    B Lemma 7.
  details: Verified exact finite-sample FDR bound for BR-1S-alpha (max FDR = 0.04649744
    <= 0.05) and Lemma 2 Gaussian signal threshold mu* = 1.511105.
- assessment_id: unified-plug-in-self-consistency-theorem-and-br-2s-dominance
  area: evidence
  topic: unified-plug-in-self-consistency-theorem-and-br-2s-dominance
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - blanchard-roquain2009-ar5iv
  - calculation
  summary: Supported by Section 3.2 Theorem 3.2, Corollary 1, and Appendix A.3.
  details: 'Verified max_q pi_0 E[G_1(p_{0,h})] = 1.0 and strict plug-in hierarchy
    G_3 = 1.142857 < G_4 = 1.333333 < G_1 = 1.6 yielding second-stage rejections {''LSU'':
    1, ''BKY06_alpha'': 2, ''BR_2S_alpha'': 3, ''Storey_alpha'': 4}.'
- assessment_id: maximal-comonotonic-dependence-fdr-and-lambda-alpha-robustness
  area: evidence
  topic: maximal-comonotonic-dependence-fdr-and-lambda-alpha-robustness
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - blanchard-roquain2009-ar5iv
  - calculation
  summary: Supported by Section 3.3 Proposition 1, Section 5.2, and Appendix A.4.
  details: 'Verified comonotonic maximal-dependence FDR at m = 20, alpha = 0.05: Storey-1/2
    FDR = 0.5 = 10 alpha and Quant-1/2 FDR = 0.083333, whereas BR-1S-alpha, BR-2S-alpha,
    BKY06-alpha, and Storey-alpha all achieve exact FDR = 0.05.'
- assessment_id: two-stage-fwer-and-markov-fdr-adaptive-step-up-under-dependence
  area: evidence
  topic: two-stage-fwer-and-markov-fdr-adaptive-step-up-under-dependence
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - blanchard-roquain2009-ar5iv
  - calculation
  summary: Supported by Section 4 Lemma 3, Theorems 4.1-4.2, and Appendix A.5.
  details: Verified Markov transformation F_2(0.75) = 3.414214 with crossover proportion
    F_2^{-1}(2) = 0.625 and rejections increasing from 15 (LSU) to 18 (Theorems 4.1
    & 4.2).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:OneAndTwoStageAdaptiveStepUpFDRUnderDependence
  evidence_ids:
  - identity
  - mapping
  - blanchard-roquain2009-ar5iv
  - blanchard-roquain2009-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of OneAndTwoStageAdaptiveStepUpFDRUnderDependence.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, two primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT One-stage and two-stage adaptive step-up procedures for false discovery
  rate control under independence and dependence record, yielding 595 native and 442
  unchanged generated records.
- All 989 lines of Blanchard & Roquain (2009, arXiv:0707.0536v3) were read in full
  text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- adaptive-procedures
- arbitrary-dependence
- self-review
- discovery-ongoing
```
