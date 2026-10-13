# Teacher forcing primary-source locator review

- Review: 20261013T064753Z-teacher-forcing-locators-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T06:45:17Z
- Finished UTC: 2026-10-13T06:47:53Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed minor evidence-locator defect; source statements remain supported. Correct the section and page locations before final review.

## Scope And Provenance

Teacher-forcing definition and claim evidence locators in Bengio2015.

Selection: Exact maintained target AIMech:TeacherForcing
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95615ff21d8f70591df2c69b915e988ee700b075.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TeacherForcing | data/curated/TeacherForcing.yaml | maintained | Teacher forcing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:TeacherForcing | Pending correction; no final passing verdict asserted. |

## Scientific And Domain Assessments

### Primary-source section and page accuracy

evidence: concern. Targets: AIMech:TeacherForcing.

Correct the locators without changing supported scientific claims.

Several Bengio2015 evidence locators identify the wrong section or page span. The method is Section2.4 on pp.3–4, not Section3 (Related Work). Figure1 is on p.4, outside the definition and hidden-state locators ending on p.3. Table3 and the Conclusion are on p.8, outside the empirical-scope locator ending on p.7. The inspected source supports the statements, but these locators impede direct verification. Correct all occurrences and the report mirror without changing the supported mechanism.

## Findings

### F1: Correct the Bengio2015 section and page locators

minor / open / confirmed; issue key: teacher-forcing-bengio2015-locators.

Several Bengio2015 evidence locators identify the wrong section or page span. The method is Section2.4 on pp.3–4, not Section3 (Related Work). Figure1 is on p.4, outside the definition and hidden-state locators ending on p.3. Table3 and the Conclusion are on p.8, outside the empirical-scope locator ending on p.7. The inspected source supports the statements, but these locators impede direct verification. Correct all occurrences and the report mirror without changing the supported mechanism.

## Recommended Actions And Acceptance Checks

### A1

Correct every affected evidence locator, synchronize the report, append an actual EDIT event, recapture and reassess corrected inputs.

- Method Section2.4 and Figure1 page4 are located correctly.
- Table3 and Conclusion page8 are included; report mirror and history agree.
- Final corrected-input validation passes and a successor resolves the finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/TeacherForcing.yaml | supports | The definition and four claim-specific locator patterns contain incorrect section or page references. |
| bengio2015 | https://proceedings.neurips.cc/paper/2015/file/e995f98d56967d946471af29d7bf99f1-Paper.pdf; All nine pages read; printed/PDF pp.2–4,7–8 reread after capture. Section2.4 spans3–4, Figures1–2 are on4, Table3 and Conclusion on8. | supports | The primary article supports the mechanism but contradicts the draft locator labels. |

## Limits And Additional Notes

- Partial author self-review; no independent approval or scientific status promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T064753Z-teacher-forcing-locators-open
kind: record
repository: CultureBotAI/AIMech
title: Teacher forcing primary-source locator review
started_at: '2026-10-13T06:45:17Z'
finished_at: '2026-10-13T06:47:53Z'
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
summary: One confirmed minor evidence-locator defect; source statements remain supported.
  Correct the section and page locations before final review.
source:
  git_revision: 95615ff21d8f70591df2c69b915e988ee700b075
  state: working_tree
  inputs:
  - path: data/aio/AutoregressiveLanguageModel.yaml
    sha256: 1ee5824569635aab5df1b1f23eaabca463bd7ef87d1b22e9d9c42375a49ec800
    role: context
  - path: data/aio/DifferentiableLLM.yaml
    sha256: b8a40c81f74e60c62abed98282803859d0f00ad7e3b9c3d161d63002575f50a3
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/DocumentNADE.yaml
    sha256: fd0969626c9aa10b8d5d876c3d537cbef1b317090c49944334e00131060b9d27
    role: context
  - path: data/curated/MeanTeacher.yaml
    sha256: 606e863163715f48b89fb35dc090bb32d5d2ca70c099d1fdfac563104ada27b7
    role: context
  - path: data/curated/RealTimeRecurrentLearning.yaml
    sha256: 56d96389c192a6a7e40852add607c729c48ac19aeb4cc5ef6c44b1a5c3190e7c
    role: context
  - path: data/curated/TeacherForcing.yaml
    sha256: 1270a5db44f3f36f7722739713371467ee1151b586e03fb94a4403a84de73324
    role: target
  - path: research/discovery/20261013T064459Z-teacher-forcing.json
    sha256: 8d74ffdb244e4760d94bcc1af2c5641171dae0fc26fb3b18f12c4c07bbc245b3
    role: context
  - path: research/discovery/teacher-forcing-boundaries.py
    sha256: 5c279d0943c0d56f2125e106cdd0a0e078bc2804fc4b17d34ad41ec048bb5ef6
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
- target_id: AIMech:TeacherForcing
  path: data/curated/TeacherForcing.yaml
  label: Teacher forcing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TeacherForcing.yaml
    role: maintained
scope:
  description: Teacher-forcing definition and claim evidence locators in Bengio2015.
  selection: Exact maintained target AIMech:TeacherForcing
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:TeacherForcing
  exclusions:
  - target: Final corrected-input scientific review and publication gates
    reason: This partial record preserves the locator finding before remediation.
checks:
- check_id: publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:TeacherForcing
  summary: Pending correction; no final passing verdict asserted.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/TeacherForcing.yaml
  accessed_at: '2026-10-13T06:47:53Z'
  snapshot_sha256: 1270a5db44f3f36f7722739713371467ee1151b586e03fb94a4403a84de73324
  support: supports
  summary: The definition and four claim-specific locator patterns contain incorrect
    section or page references.
- evidence_id: bengio2015
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper/2015/file/e995f98d56967d946471af29d7bf99f1-Paper.pdf
  accessed_at: '2026-10-13T06:27:25Z'
  snapshot_sha256: ab71fd38a31df07e90e7ec019b19654de8f633484a76c0a68e36133f888454a0
  support: supports
  locator: All nine pages read; printed/PDF pp.2–4,7–8 reread after capture. Section2.4
    spans3–4, Figures1–2 are on4, Table3 and Conclusion on8.
  summary: The primary article supports the mechanism but contradicts the draft locator
    labels.
assessments:
- assessment_id: locators
  area: evidence
  topic: Primary-source section and page accuracy
  outcome: concern
  target_ids:
  - AIMech:TeacherForcing
  evidence_ids:
  - record
  - bengio2015
  summary: Correct the locators without changing supported scientific claims.
  details: Several Bengio2015 evidence locators identify the wrong section or page
    span. The method is Section2.4 on pp.3–4, not Section3 (Related Work). Figure1
    is on p.4, outside the definition and hidden-state locators ending on p.3. Table3
    and the Conclusion are on p.8, outside the empirical-scope locator ending on p.7.
    The inspected source supports the statements, but these locators impede direct
    verification. Correct all occurrences and the report mirror without changing the
    supported mechanism.
findings:
- finding_id: F1
  issue_key: teacher-forcing-bengio2015-locators
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Bengio2015 section and page locators
  description: Several Bengio2015 evidence locators identify the wrong section or
    page span. The method is Section2.4 on pp.3–4, not Section3 (Related Work). Figure1
    is on p.4, outside the definition and hidden-state locators ending on p.3. Table3
    and the Conclusion are on p.8, outside the empirical-scope locator ending on p.7.
    The inspected source supports the statements, but these locators impede direct
    verification. Correct all occurrences and the report mirror without changing the
    supported mechanism.
  target_ids:
  - AIMech:TeacherForcing
  field_paths:
  - definition_evidence[source_id=bengio2015].locator
  - claims.evidence[source_id=bengio2015].locator
  evidence_ids:
  - record
  - bengio2015
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TeacherForcing.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct every affected evidence locator, synchronize the report, append
    an actual EDIT event, recapture and reassess corrected inputs.
  finding_ids:
  - F1
  target_ids:
  - AIMech:TeacherForcing
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TeacherForcing.yaml
    role: maintained
  acceptance_checks:
  - Method Section2.4 and Figure1 page4 are located correctly.
  - Table3 and Conclusion page8 are included; report mirror and history agree.
  - Final corrected-input validation passes and a successor resolves the finding.
limitations:
- Partial author self-review; no independent approval or scientific status promotion.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- source-locators
```
