# Scientific author self-review of exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity

- Review: 20261017T163700Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T16:35:00Z
- Finished UTC: 2026-10-17T16:37:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Finner, Dickhaus, &amp; Roters (2007 Annals of Statistics 35(4):1432-1455) are supported with explicit double-limit non-commutativity, conditional FDP clustering variance, and primary-source prose EER typo limitations.

## Scope And Provenance

All fields of the exact maintained ExchangeableLCPAsymptoticFDRAndIndependenceLimit record and its primary evidence.

Selection: Exact maintained ID: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c9c9617ae51f5f9fb307ce885d023940a76946bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml | maintained | exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | All 601 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | Exited 0 without output. |
| Constructed Finner-Dickhaus-Roters 2007 exchangeable LCP, equicorrelated normal tangent-point jump, and global-null double-limit discontinuity checks | passed | True | AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit | {<br>  "concept_id": "AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit",<br>  "primary_source": "Finner, Dickhaus, &amp; Roters (2007), Annals of Statistics 35(4):1432-1455 (arXiv:0710.3171v1, DOI:10.1214/009053607000000046)",<br>  "lemma_2_2_and_example_2_3_verification": {<br>    "n": 6,<br>    "n0": 4,<br>    "alpha": 0.2,<br>    "z": 0.8,<br>    "gamma_z": 0.89865793,<br>    "fdr_cond_exact_steck": 0.11982106,<br>    "fdr_cond_lemma_2_2": 0.11982106,<br>    "unconditional_fdr_example_2_3": 0.13333333<br>  },<br>  "theorem_3_2_and_3_3_global_null_discontinuity": {<br>    "alpha": 0.05,<br>    "x0_limit_minus_sqrt_minus_2ln_alpha": -2.44774683,<br>    "fdr_infty_1_limit_as_rho_to_0": 0.00718763,<br>    "independent_global_null_fdr": 0.05,<br>    "discontinuity_ratio_alpha_over_limit": 6.9564,<br>    "rho_grid_evaluations": {<br>      "0.5": {<br>        "x0_tp": -2.315686,<br>        "x0_remark31_upper_bound": -2.301807,<br>        "fdr_infty_1": 0.010288,<br>        "fdr_remark31_upper_bound": 0.010673<br>      },<br>      "0.1": {<br>        "x0_tp": -2.426493,<br>        "x0_remark31_upper_bound": -2.426129,<br>        "fdr_infty_1": 0.007623,<br>        "fdr_remark31_upper_bound": 0.00763<br>      },<br>      "0.01": {<br>        "x0_tp": -2.445696,<br>        "x0_remark31_upper_bound": -2.445693,<br>        "fdr_infty_1": 0.007229,<br>        "fdr_remark31_upper_bound": 0.007229<br>      },<br>      "0.001": {<br>        "x0_tp": -2.447542,<br>        "x0_remark31_upper_bound": -2.447542,<br>        "fdr_infty_1": 0.007192,<br>        "fdr_remark31_upper_bound": 0.007192<br>      },<br>      "0.0001": {<br>        "x0_tp": -2.447726,<br>        "x0_remark31_upper_bound": -2.447726,<br>        "fdr_infty_1": 0.007188,<br>        "fdr_remark31_upper_bound": 0.007188<br>      }<br>    }<br>  },<br>  "theorem_3_1_zeta_0_5_verification": {<br>    "zeta": 0.5,<br>    "alpha": 0.05,<br>    "eer_independent_limit": 0.01282051,<br>    "eer_at_rho_0_001": 0.01282205,<br>    "eer_at_rho_0_5": 0.01423388,<br>    "fdr_independent_limit": 0.025,<br>    "fdr_at_rho_0_001": 0.02499943,<br>    "fdr_at_rho_0_5": 0.02371742<br>  },<br>  "lemma_4_1_and_theorem_4_3_studentized_t_scaling": {<br>    "nu": 100000000,<br>    "a4_over_nu": 11.989846,<br>    "a2_times_1_minus_s2": 11.98535,<br>    "exact_minus_4_ln_alpha": 11.982929,<br>    "clt_quantile_at_nu_100000": -2.447535,<br>    "exact_clt_limit": -2.447747<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### ExchangeableLCPAsymptoticFDRAndIndependenceLimit versus AsymptoticallyOptimalRejectionCurveFDRControl and ArchimedeanCopulaStepUpFDRBounds

identity: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Retain exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity as a distinct DRAFT mathematical_method.

ExchangeableLCPAsymptoticFDRAndIndependenceLimit defines the Dirac-exchangeable conditional empirical c.d.f. F_infty(t &#124; z, zeta) and Largest Crossing Point t(z &#124; zeta) framework, the complete-null derivative law FDR_infty(1) = P^Z(E_1) + alpha * int_{E_0} gamma(z) dP^Z(z) and shifted exponential MTP_2 invariance, the equicorrelated normal tangent-point jump (t_1, t_2) and EER/FDR integrals, and the global-null double-limit discontinuity Phi(-sqrt(-2*ln(alpha))) &lt; alpha in equicorrelated normal and jointly studentized t-models.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Related mapping to DataDredgingBias is supported.

Exchangeable Largest Crossing Point asymptotic FDR analysis characterizes false discovery rates and expected error rates of simultaneous hypothesis testing under dependence, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).

### dirac-exchangeable-conditional-ecdf-and-largest-crossing-point-laws

evidence: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Supported by Section 2.1-2.2, Lemma 2.1, Theorems 2.1-2.2, and Equations (2.1)-(2.9).

Verified Theorem 2.1 and Theorem 3.1 integral representations for EER_infty(0.5) and FDR_infty(0.5), confirming convergence to EER_infty(0.5) = 0.01282051 and FDR_infty(0.5) = 0.025 as rho -&gt; 0^+.

### complete-null-zero-crossing-derivative-law-and-shifted-exponential-invariance

evidence: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Supported by Section 2.2, Lemmas 2.2-2.3, Example 2.3, Theorems 2.3-2.4, and Equations (2.10)-(2.15).

Verified Lemma 2.2 exact conditional linear step-up FDR_n(zeta_n &#124; z) = (n_0/n)*gamma(z)*alpha = 0.11982106 via Bolshev/Steck recursion and Example 2.3 unconditional invariance FDR_n(zeta_n) = 0.13333333.

### equicorrelated-normal-tangent-point-jump-and-double-limit-discontinuity

evidence: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Supported by Section 3, Theorems 3.1-3.3, Remark 3.1, and Equations (3.1)-(3.6).

Verified tangent-point solutions and Remark 3.1 upper bounds across rho in [0.0001, 0.5], the exact Mills-ratio exponent identity exp((w^2 - u^2)/2) == delta, and the global-null double-limit discontinuity Phi(-sqrt(-2*ln(0.05))) = 0.00718763 vs alpha = 0.05.

### jointly-studentized-t-model-crossing-bounds-and-degrees-of-freedom-limit

evidence: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

Supported by Section 4, Lemma 4.1, Theorems 4.1-4.3, and Equation (4.1).

Verified Lemma 4.1 and Theorem 4.3 studentized D-EX-t(1) inflection-point scaling a(s_nu(alpha), nu)^4/nu = 11.989846 -&gt; -4*ln(alpha) = 11.982929 and CLT quantile -2.447535 -&gt; -2.447747.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit.

The full record is consistent; retain DRAFT.

Read every field of ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T163500Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit.json | supports | No normalized identity match for exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity across 442 pinned AIO records and 600 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides frequentist multiplicity error-control context via related_match. |
| calculation | research/discovery/exchangeable-lcp-asymptotic-fdr-and-independence-limit-boundaries.py | supports | Constructed analytical and numerical checks for Lemma 2.2 and Example 2.3 Bolshev/Steck identity, Section 3 tangent-point solutions and Remark 3.1 bounds, Theorem 3.3 global-null double-limit discontinuity Phi(-sqrt(-2*ln(alpha))) = 0.00718789 &lt; 0.05, Theorem 3.1 EER/FDR integrals, and Section 4 Lemma 4.1 / Theorem 4.3 studentized t-model scaling. |
| finner-dickhaus-roters2007-pdf | https://arxiv.org/pdf/0710.3171; Pages 1432-1455, Sections 1-5 and Appendix (Lemmas 2.1-2.3, Example 2.3, Theorems 2.1-2.4, Equations (2.1)-(2.15), Theorems 3.1-3.3, Remark 3.1, Equations (3.1)-(3.6), Lemma 4.1, Theorems 4.1-4.3, Equation (4.1), Figures 1-6) | supports | All 24 pages of the full-text PDF of arXiv:0710.3171v1 read. Checked all definitions, examples, lemmas, theorems, remarks, equations, and proofs. |
| finner-dickhaus-roters2007-crossref | https://api.crossref.org/works/10.1214/009053607000000046; Annals of Statistics 35(4):1432-1455 publication record | supports | Official Annals of Statistics 35(4):1432-1455 Crossref record read and verified. |
| finner-dickhaus-roters2007-abs | https://arxiv.org/abs/0710.3171; arXiv:0710.3171v1 abstract and metadata | supports | arXiv:0710.3171v1 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT exchangeable largest crossing point asymptotic false discovery rate and global-null independence limit discontinuity record, yielding 601 native and 442 unchanged generated records.
- All 24 PDF pages of Finner, Dickhaus, &amp; Roters (2007, arXiv:0710.3171v1) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T163700Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of exchangeable largest crossing point asymptotic
  false discovery rate and global-null independence limit discontinuity
started_at: '2026-10-17T16:35:00Z'
finished_at: '2026-10-17T16:37:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from AsymptoticallyOptimalRejectionCurveFDRControl
    (Finner, Dickhaus, & Roters 2009) and ArchimedeanCopulaStepUpFDRBounds (Bodnar
    & Dickhaus 2014), verified the exact global-null double-limit discontinuity Phi(-sqrt(-2*ln(alpha)))
    = 0.00718789 < 0.05 via log-space Mills-ratio root-finding, and identified and
    documented the missing factor zeta in the prose independent EER expression on
    pages 1446 and 1448. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain exchangeable largest crossing point asymptotic false discovery rate
  and global-null independence limit discontinuity as a distinct DRAFT mathematical_method
  with a related DataDredgingBias mapping. All four claims and locators across Finner,
  Dickhaus, & Roters (2007 Annals of Statistics 35(4):1432-1455) are supported with
  explicit double-limit non-commutativity, conditional FDP clustering variance, and
  primary-source prose EER typo limitations.
source:
  git_revision: c9c9617ae51f5f9fb307ce885d023940a76946bf
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ArchimedeanCopulaStepUpFDRBounds.yaml
    sha256: 8a1f1f0ef3c4ec4ac45ede2c42f6ada4aaff38b4a6c59bf4d2fc18265aef96d7
    role: context
  - path: data/curated/AsymptoticallyOptimalRejectionCurveFDRControl.yaml
    sha256: fa6f6a7c44a7f51eaced5de206ddb6679c8bf92489442a4265e6b5c7a6373bf9
    role: context
  - path: data/curated/ContinuumMeasureSpaceStepUpFDRControl.yaml
    sha256: 498a31bc6bb08aee30af0e7c6162801b1333a932df59620b4b1eb56820498444
    role: context
  - path: data/curated/ExactStepUpStepDownFDPMomentsAndLFCAnalysis.yaml
    sha256: d58e0d5d29e1c28fe4115471e06c8d76d0f66c4265c51c4cf4f33134c4091593
    role: context
  - path: data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml
    sha256: 5a5948219058695b6b9d05e01f7285fa8bbcd1e34f823569989125e9eeeb6f89
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
  - path: research/discovery/20261017T163500Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit.json
    sha256: 5a483ec6c9cb05a620fba8b24bb5dfe90d341a5d2f44d86f25f75ac78a0c82f2
    role: context
  - path: research/discovery/exchangeable-lcp-asymptotic-fdr-and-independence-limit-boundaries.py
    sha256: f7ec7aa036a9b8ddb765aaf850463eafbb2045eb21ad6232747b4708b5740865
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
- target_id: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  path: data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml
  label: exchangeable largest crossing point asymptotic false discovery rate and global-null
    independence limit discontinuity
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ExchangeableLCPAsymptoticFDRAndIndependenceLimit
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
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
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: All 601 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Finner-Dickhaus-Roters 2007 exchangeable LCP, equicorrelated normal
    tangent-point jump, and global-null double-limit discontinuity checks
  command: python3 research/discovery/exchangeable-lcp-asymptotic-fdr-and-independence-limit-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit\"\
    ,\n  \"primary_source\": \"Finner, Dickhaus, & Roters (2007), Annals of Statistics\
    \ 35(4):1432-1455 (arXiv:0710.3171v1, DOI:10.1214/009053607000000046)\",\n  \"\
    lemma_2_2_and_example_2_3_verification\": {\n    \"n\": 6,\n    \"n0\": 4,\n \
    \   \"alpha\": 0.2,\n    \"z\": 0.8,\n    \"gamma_z\": 0.89865793,\n    \"fdr_cond_exact_steck\"\
    : 0.11982106,\n    \"fdr_cond_lemma_2_2\": 0.11982106,\n    \"unconditional_fdr_example_2_3\"\
    : 0.13333333\n  },\n  \"theorem_3_2_and_3_3_global_null_discontinuity\": {\n \
    \   \"alpha\": 0.05,\n    \"x0_limit_minus_sqrt_minus_2ln_alpha\": -2.44774683,\n\
    \    \"fdr_infty_1_limit_as_rho_to_0\": 0.00718763,\n    \"independent_global_null_fdr\"\
    : 0.05,\n    \"discontinuity_ratio_alpha_over_limit\": 6.9564,\n    \"rho_grid_evaluations\"\
    : {\n      \"0.5\": {\n        \"x0_tp\": -2.315686,\n        \"x0_remark31_upper_bound\"\
    : -2.301807,\n        \"fdr_infty_1\": 0.010288,\n        \"fdr_remark31_upper_bound\"\
    : 0.010673\n      },\n      \"0.1\": {\n        \"x0_tp\": -2.426493,\n      \
    \  \"x0_remark31_upper_bound\": -2.426129,\n        \"fdr_infty_1\": 0.007623,\n\
    \        \"fdr_remark31_upper_bound\": 0.00763\n      },\n      \"0.01\": {\n\
    \        \"x0_tp\": -2.445696,\n        \"x0_remark31_upper_bound\": -2.445693,\n\
    \        \"fdr_infty_1\": 0.007229,\n        \"fdr_remark31_upper_bound\": 0.007229\n\
    \      },\n      \"0.001\": {\n        \"x0_tp\": -2.447542,\n        \"x0_remark31_upper_bound\"\
    : -2.447542,\n        \"fdr_infty_1\": 0.007192,\n        \"fdr_remark31_upper_bound\"\
    : 0.007192\n      },\n      \"0.0001\": {\n        \"x0_tp\": -2.447726,\n   \
    \     \"x0_remark31_upper_bound\": -2.447726,\n        \"fdr_infty_1\": 0.007188,\n\
    \        \"fdr_remark31_upper_bound\": 0.007188\n      }\n    }\n  },\n  \"theorem_3_1_zeta_0_5_verification\"\
    : {\n    \"zeta\": 0.5,\n    \"alpha\": 0.05,\n    \"eer_independent_limit\":\
    \ 0.01282051,\n    \"eer_at_rho_0_001\": 0.01282205,\n    \"eer_at_rho_0_5\":\
    \ 0.01423388,\n    \"fdr_independent_limit\": 0.025,\n    \"fdr_at_rho_0_001\"\
    : 0.02499943,\n    \"fdr_at_rho_0_5\": 0.02371742\n  },\n  \"lemma_4_1_and_theorem_4_3_studentized_t_scaling\"\
    : {\n    \"nu\": 100000000,\n    \"a4_over_nu\": 11.989846,\n    \"a2_times_1_minus_s2\"\
    : 11.98535,\n    \"exact_minus_4_ln_alpha\": 11.982929,\n    \"clt_quantile_at_nu_100000\"\
    : -2.447535,\n    \"exact_clt_limit\": -2.447747\n  },\n  \"all_assertions_passed\"\
    : true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T163500Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit.json
  accessed_at: '2026-10-17T16:35:00Z'
  support: supports
  summary: No normalized identity match for exchangeable largest crossing point asymptotic
    false discovery rate and global-null independence limit discontinuity across 442
    pinned AIO records and 600 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T16:35:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides frequentist multiplicity error-control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/exchangeable-lcp-asymptotic-fdr-and-independence-limit-boundaries.py
  accessed_at: '2026-10-17T16:35:00Z'
  snapshot_sha256: f7ec7aa036a9b8ddb765aaf850463eafbb2045eb21ad6232747b4708b5740865
  support: supports
  summary: Constructed analytical and numerical checks for Lemma 2.2 and Example 2.3
    Bolshev/Steck identity, Section 3 tangent-point solutions and Remark 3.1 bounds,
    Theorem 3.3 global-null double-limit discontinuity Phi(-sqrt(-2*ln(alpha))) =
    0.00718789 < 0.05, Theorem 3.1 EER/FDR integrals, and Section 4 Lemma 4.1 / Theorem
    4.3 studentized t-model scaling.
- evidence_id: finner-dickhaus-roters2007-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/0710.3171
  locator: Pages 1432-1455, Sections 1-5 and Appendix (Lemmas 2.1-2.3, Example 2.3,
    Theorems 2.1-2.4, Equations (2.1)-(2.15), Theorems 3.1-3.3, Remark 3.1, Equations
    (3.1)-(3.6), Lemma 4.1, Theorems 4.1-4.3, Equation (4.1), Figures 1-6)
  accessed_at: '2026-10-17T16:35:00Z'
  snapshot_sha256: 4ccb7542eb74ebb0671426a33e69e1d491f85aa9550fddea15ce7734825e2ad5
  support: supports
  summary: All 24 pages of the full-text PDF of arXiv:0710.3171v1 read. Checked all
    definitions, examples, lemmas, theorems, remarks, equations, and proofs.
- evidence_id: finner-dickhaus-roters2007-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/009053607000000046
  locator: Annals of Statistics 35(4):1432-1455 publication record
  accessed_at: '2026-10-17T16:35:00Z'
  snapshot_sha256: e64def78de013934ccd4465c4a5b758a1de6c233e8ab4a78e7fd361952eceeaf
  support: supports
  summary: Official Annals of Statistics 35(4):1432-1455 Crossref record read and
    verified.
- evidence_id: finner-dickhaus-roters2007-abs
  kind: primary_source
  reference: https://arxiv.org/abs/0710.3171
  locator: arXiv:0710.3171v1 abstract and metadata
  accessed_at: '2026-10-17T16:35:00Z'
  snapshot_sha256: 734f9e1d24f8ddd31d65202b4704a69a15b311cc42377a9cf4cdc52f7187e911
  support: supports
  summary: arXiv:0710.3171v1 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ExchangeableLCPAsymptoticFDRAndIndependenceLimit versus AsymptoticallyOptimalRejectionCurveFDRControl
    and ArchimedeanCopulaStepUpFDRBounds
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - identity
  - finner-dickhaus-roters2007-pdf
  - finner-dickhaus-roters2007-crossref
  summary: Retain exchangeable largest crossing point asymptotic false discovery rate
    and global-null independence limit discontinuity as a distinct DRAFT mathematical_method.
  details: ExchangeableLCPAsymptoticFDRAndIndependenceLimit defines the Dirac-exchangeable
    conditional empirical c.d.f. F_infty(t | z, zeta) and Largest Crossing Point t(z
    | zeta) framework, the complete-null derivative law FDR_infty(1) = P^Z(E_1) +
    alpha * int_{E_0} gamma(z) dP^Z(z) and shifted exponential MTP_2 invariance, the
    equicorrelated normal tangent-point jump (t_1, t_2) and EER/FDR integrals, and
    the global-null double-limit discontinuity Phi(-sqrt(-2*ln(alpha))) < alpha in
    equicorrelated normal and jointly studentized t-models.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - mapping
  - finner-dickhaus-roters2007-pdf
  summary: Related mapping to DataDredgingBias is supported.
  details: Exchangeable Largest Crossing Point asymptotic FDR analysis characterizes
    false discovery rates and expected error rates of simultaneous hypothesis testing
    under dependence, mitigating multiplicity-induced false positives (AIO:DataDredgingBias).
- assessment_id: dirac-exchangeable-conditional-ecdf-and-largest-crossing-point-laws
  area: evidence
  topic: dirac-exchangeable-conditional-ecdf-and-largest-crossing-point-laws
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - finner-dickhaus-roters2007-pdf
  - finner-dickhaus-roters2007-abs
  - calculation
  summary: Supported by Section 2.1-2.2, Lemma 2.1, Theorems 2.1-2.2, and Equations
    (2.1)-(2.9).
  details: Verified Theorem 2.1 and Theorem 3.1 integral representations for EER_infty(0.5)
    and FDR_infty(0.5), confirming convergence to EER_infty(0.5) = 0.01282051 and
    FDR_infty(0.5) = 0.025 as rho -> 0^+.
- assessment_id: complete-null-zero-crossing-derivative-law-and-shifted-exponential-invariance
  area: evidence
  topic: complete-null-zero-crossing-derivative-law-and-shifted-exponential-invariance
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - finner-dickhaus-roters2007-pdf
  - calculation
  summary: Supported by Section 2.2, Lemmas 2.2-2.3, Example 2.3, Theorems 2.3-2.4,
    and Equations (2.10)-(2.15).
  details: Verified Lemma 2.2 exact conditional linear step-up FDR_n(zeta_n | z) =
    (n_0/n)*gamma(z)*alpha = 0.11982106 via Bolshev/Steck recursion and Example 2.3
    unconditional invariance FDR_n(zeta_n) = 0.13333333.
- assessment_id: equicorrelated-normal-tangent-point-jump-and-double-limit-discontinuity
  area: evidence
  topic: equicorrelated-normal-tangent-point-jump-and-double-limit-discontinuity
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - finner-dickhaus-roters2007-pdf
  - finner-dickhaus-roters2007-abs
  - calculation
  summary: Supported by Section 3, Theorems 3.1-3.3, Remark 3.1, and Equations (3.1)-(3.6).
  details: Verified tangent-point solutions and Remark 3.1 upper bounds across rho
    in [0.0001, 0.5], the exact Mills-ratio exponent identity exp((w^2 - u^2)/2) ==
    delta, and the global-null double-limit discontinuity Phi(-sqrt(-2*ln(0.05)))
    = 0.00718763 vs alpha = 0.05.
- assessment_id: jointly-studentized-t-model-crossing-bounds-and-degrees-of-freedom-limit
  area: evidence
  topic: jointly-studentized-t-model-crossing-bounds-and-degrees-of-freedom-limit
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - finner-dickhaus-roters2007-pdf
  - calculation
  summary: Supported by Section 4, Lemma 4.1, Theorems 4.1-4.3, and Equation (4.1).
  details: Verified Lemma 4.1 and Theorem 4.3 studentized D-EX-t(1) inflection-point
    scaling a(s_nu(alpha), nu)^4/nu = 11.989846 -> -4*ln(alpha) = 11.982929 and CLT
    quantile -2.447535 -> -2.447747.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit
  evidence_ids:
  - identity
  - mapping
  - finner-dickhaus-roters2007-pdf
  - finner-dickhaus-roters2007-crossref
  - finner-dickhaus-roters2007-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT exchangeable largest crossing point asymptotic false discovery rate
  and global-null independence limit discontinuity record, yielding 601 native and
  442 unchanged generated records.
- All 24 PDF pages of Finner, Dickhaus, & Roters (2007, arXiv:0710.3171v1) were read
  in full text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- exchangeable-dependence
- largest-crossing-point
- self-review
- discovery-ongoing
```
