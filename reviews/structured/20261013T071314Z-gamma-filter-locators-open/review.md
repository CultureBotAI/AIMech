# Gamma filter primary-source locator review

- Review: 20261013T071314Z-gamma-filter-locators-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T07:11:36Z
- Finished UTC: 2026-10-13T07:13:14Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed minor source-location finding affecting three locators and one section attribution. Correct before final review.

## Scope And Provenance

Gamma-filter mechanism and experimental source-location accuracy.

Selection: Exact maintained target AIMech:GammaFilter
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 979c918cbf59603232be85a07bcec0fd0db95110.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GammaFilter | data/curated/GammaFilter.yaml | maintained | Gamma filter |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:GammaFilter | Pending correction. |

## Scientific And Domain Assessments

### Primary-source section and figure accuracy

evidence: concern. Targets: AIMech:GammaFilter.

Correct the inaccurate source descriptions.

The stability locator names SectionIII.A, but stability is SectionIII.B. The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C span. The experimental locator names Figures4–6, but only Figures4–5 show the two identification studies; Figure6 is a transform illustration on printed p.655. The statement places deferred signal applications in Discussion, while that sentence is in SectionIV on printed p.654. Correct these source-location descriptions; the mathematical and experimental scope remains supported.

## Findings

### F1: Correct Gamma filter section and figure references

minor / open / confirmed; issue key: gamma-filter-principe1993-locators.

The stability locator names SectionIII.A, but stability is SectionIII.B. The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C span. The experimental locator names Figures4–6, but only Figures4–5 show the two identification studies; Figure6 is a transform illustration on printed p.655. The statement places deferred signal applications in Discussion, while that sentence is in SectionIV on printed p.654. Correct these source-location descriptions; the mathematical and experimental scope remains supported.

## Recommended Actions And Acceptance Checks

### A1

Correct the three locators and section attribution, synchronize report and EDIT history, then recapture and reassess.

- Stability III.B, impulse-response III.A and experimental Figures4–5 are located correctly.
- Deferred applications are attributed to SectionIV on p.654.
- Report mirror, history and fresh corrected-input review agree; required gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/GammaFilter.yaml | supports | Three locators and one section attribution require correction. |
| principe1993 | https://www.cnel.ufl.edu/wp-content/uploads/courses/EEL6504/principe_gamma_1993.pdf; All eight pages read; PDF pp.2,4,6–7 reread after capture. Printed p.650 locates III.A definitions and III.B stability; p.654 contains experiments and deferred applications; p.655 Figure6 concerns the transform. | supports | Primary article supports the underlying claims but identifies different source locations. |

## Limits And Additional Notes

- Partial author self-review; no independent approval or scientific status promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T071314Z-gamma-filter-locators-open
kind: record
repository: CultureBotAI/AIMech
title: Gamma filter primary-source locator review
started_at: '2026-10-13T07:11:36Z'
finished_at: '2026-10-13T07:13:14Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author checked maintained locators against the actual printed
    primary paper during adversarial rereading; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed minor source-location finding affecting three locators and
  one section attribution. Correct before final review.
source:
  git_revision: 979c918cbf59603232be85a07bcec0fd0db95110
  state: working_tree
  inputs:
  - path: data/aio/Convolution1DLayer.yaml
    sha256: 4d7c7bef628e3b308ad22eb41f2959bb65e34edebfd9336c9d7c05dc9feb645c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/Perceptron.yaml
    sha256: 6b1cc7cb96bfe03ed8720cca04490657976eea656fab6674d7ef685c34216915
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/GammaFilter.yaml
    sha256: 3b1d1d8ce24e6e07aad72189d4944d8a3fd2b04c0e8a1f8cd03e67afb58873cf
    role: target
  - path: data/curated/GammaNeuralModel.yaml
    sha256: 496ce0a31262d619eac9d487ca2ed3e5971abbd28c9dce1688a5be50430a6fb5
    role: context
  - path: data/curated/IteratedWienerFilter.yaml
    sha256: 803905a00467ecfc963cbd5a24f5616013484c0d0ce57d205c386868346addac
    role: context
  - path: data/curated/LinearStateSpaceLayer.yaml
    sha256: 05d7d834a8c0db4c33613384cde4a250838290cce6960fda10e7209da318c151
    role: context
  - path: data/curated/PseudoLinearRegressionEstimation.yaml
    sha256: 70f7a23a68a1248b2aaf11252bdaffb5e72c61d805eed6e7099ec2d4ddeaaffc
    role: context
  - path: research/discovery/20261013T071125Z-gamma-filter.json
    sha256: d01647c95e060572a8a24513b90554febcf07e2e1142285537bcea0db92cd04d
    role: context
  - path: research/discovery/gamma-filter-boundaries.py
    sha256: 3d655b6cc5590e0210cdb5b5c164306c1a1ab988430fdfd1276ff2ab4d93df74
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
- target_id: AIMech:GammaFilter
  path: data/curated/GammaFilter.yaml
  label: Gamma filter
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GammaFilter.yaml
    role: maintained
scope:
  description: Gamma-filter mechanism and experimental source-location accuracy.
  selection: Exact maintained target AIMech:GammaFilter
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:GammaFilter
  exclusions:
  - target: Corrected-input scientific review and gates
    reason: Pending remediation; this partial review preserves the finding.
checks:
- check_id: publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:GammaFilter
  summary: Pending correction.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/GammaFilter.yaml
  accessed_at: '2026-10-13T07:13:14Z'
  snapshot_sha256: 3b1d1d8ce24e6e07aad72189d4944d8a3fd2b04c0e8a1f8cd03e67afb58873cf
  support: supports
  summary: Three locators and one section attribution require correction.
- evidence_id: principe1993
  kind: primary_source
  reference: https://www.cnel.ufl.edu/wp-content/uploads/courses/EEL6504/principe_gamma_1993.pdf
  accessed_at: '2026-10-13T06:52:29Z'
  snapshot_sha256: 0c4cf590b91e07237a9975c08a4e4f35a8c153fcc7acec965c7e9019f61d584a
  support: supports
  locator: All eight pages read; PDF pp.2,4,6–7 reread after capture. Printed p.650
    locates III.A definitions and III.B stability; p.654 contains experiments and
    deferred applications; p.655 Figure6 concerns the transform.
  summary: Primary article supports the underlying claims but identifies different
    source locations.
assessments:
- assessment_id: locators
  area: evidence
  topic: Primary-source section and figure accuracy
  outcome: concern
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - record
  - principe1993
  summary: Correct the inaccurate source descriptions.
  details: The stability locator names SectionIII.A, but stability is SectionIII.B.
    The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C
    span. The experimental locator names Figures4–6, but only Figures4–5 show the
    two identification studies; Figure6 is a transform illustration on printed p.655.
    The statement places deferred signal applications in Discussion, while that sentence
    is in SectionIV on printed p.654. Correct these source-location descriptions;
    the mathematical and experimental scope remains supported.
findings:
- finding_id: F1
  issue_key: gamma-filter-principe1993-locators
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct Gamma filter section and figure references
  description: The stability locator names SectionIII.A, but stability is SectionIII.B.
    The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C
    span. The experimental locator names Figures4–6, but only Figures4–5 show the
    two identification studies; Figure6 is a transform illustration on printed p.655.
    The statement places deferred signal applications in Discussion, while that sentence
    is in SectionIV on printed p.654. Correct these source-location descriptions;
    the mathematical and experimental scope remains supported.
  target_ids:
  - AIMech:GammaFilter
  field_paths:
  - claims[claim_id=fixed-memory-stability].evidence
  - claims[claim_id=dispersive-memory].evidence
  - claims[claim_id=system-identification-evidence]
  evidence_ids:
  - record
  - principe1993
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GammaFilter.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct the three locators and section attribution, synchronize report
    and EDIT history, then recapture and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:GammaFilter
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GammaFilter.yaml
    role: maintained
  acceptance_checks:
  - Stability III.B, impulse-response III.A and experimental Figures4–5 are located
    correctly.
  - Deferred applications are attributed to SectionIV on p.654.
  - Report mirror, history and fresh corrected-input review agree; required gates
    pass.
limitations:
- Partial author self-review; no independent approval or scientific status promotion.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- source-locators
```
