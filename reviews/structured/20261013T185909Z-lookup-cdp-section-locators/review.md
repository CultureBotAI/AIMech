# Lookup CDP primary-source section locator finding

- Review: 20261013T185909Z-lookup-cdp-section-locators
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T18:56:55Z
- Finished UTC: 2026-10-13T18:59:09Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding affects the section labels in two otherwise page-located citations.

## Scope And Provenance

Section attribution of CDP recurrence and frontier passages.

Selection: Exact maintained ID AIMech:LookupConditionalDistributionPrediction
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7cca784529fe8ffa9fb1af07286fefab7856ad74.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LookupConditionalDistributionPrediction | data/curated/LookupConditionalDistributionPrediction.yaml | maintained | Lookup Conditional Distribution Prediction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:LookupConditionalDistributionPrediction | The corrected record does not yet exist; its publication gates remain pending. |

## Scientific And Domain Assessments

### Source-section attribution

evidence: concern. Targets: AIMech:LookupConditionalDistributionPrediction.

Correct two section labels while retaining accurate page ranges.

The shallow-frontier-accounting locator names Section3 for PDFp5 although the frontier paragraph precedes the Section3 heading and belongs to Section2. The fixed-model-equivalence locator names Sections3–4 for PDFpp4–7 although the recurrence on PDFp4 is also in Section2. Their PDF/printed page ranges remain useful, but section labels should be corrected to Section2 and Sections2–4 respectively. Section7/7.1 references remain correct.

## Findings

### F1: Correct the CDP framework section labels in two evidence locators

minor / open / confirmed; issue key: lookup-cdp-recurrence-section-locators.

The shallow-frontier-accounting locator names Section3 for PDFp5 although the frontier paragraph precedes the Section3 heading and belongs to Section2. The fixed-model-equivalence locator names Sections3–4 for PDFpp4–7 although the recurrence on PDFp4 is also in Section2. Their PDF/printed page ranges remain useful, but section labels should be corrected to Section2 and Sections2–4 respectively. Section7/7.1 references remain correct.

## Recommended Actions And Acceptance Checks

### A1

Correct the two maintained locators, synchronize the discovery report, append correction history, recapture and reassess.

- The frontier locator cites Section2 and7; the recurrence locator cites Sections2–4 and7.1 with unchanged accurate page ranges.
- Record/report mirrors agree and rendered pages are regenerated.
- Corrected-input gates and a linked successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/LookupConditionalDistributionPrediction.yaml | supports | Complete maintained record read after capture; two claim locators misidentify Section2 content as Section3. |
| paper | https://webdocs.cs.ualberta.ca/~santanad/papers/2013/ARTINT2694.pdf; PDFpp3–5 / printed54–56, Section2 heading and boundary with Section3; PDFpp16–17 / printed67–68, Section7. | supports | All25 pages previously visually read. After capture, pages3–5,10–11,16–18 and21–24 reread. Section2 begins on PDFp3, includes the recurrence onp4 and ends before the Section3 heading near the bottom ofp5. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T185909Z-lookup-cdp-section-locators
kind: record
repository: CultureBotAI/AIMech
title: Lookup CDP primary-source section locator finding
started_at: '2026-10-13T18:56:55Z'
finished_at: '2026-10-13T18:59:09Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author compared the written claim locators with the actual primary
    PDF headings; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor finding affects the section labels in two otherwise page-located
  citations.
source:
  git_revision: 7cca784529fe8ffa9fb1af07286fefab7856ad74
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    sha256: 316d4e103eb9ebc513fd94573e8d0ee3c287cc569affd4249d5815db50f6793f
    role: context
  - path: data/curated/EpsilonTruncationCDP.yaml
    sha256: fca33999517a17fae9dbb7a755302a8450fc8dd8aaa0d1fb8d2c4ff27fecbf03
    role: context
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 0c3ea32d9b744d1324b6c58ef06d60e5a71a0d327d8c9a880ee89490dbd02a7e
    role: context
  - path: data/curated/LookupConditionalDistributionPrediction.yaml
    sha256: 2fdc651cfa5f1e7de067edf8dbc69fb1856f2436e5adc9392ec27f6745ee7481
    role: target
  - path: research/discovery/20261013T185653Z-lookup-conditional-distribution-prediction.json
    sha256: 4936d1de96f42b5692083fe2c0d8412233b41b29395ae8ff333106da3340fe0a
    role: context
  - path: research/discovery/lookup-cdp-boundaries.py
    sha256: 2bd5fcff459390f838e912b4043c50ae208678be1c3c48f8eebefb1413cdbd22
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
- target_id: AIMech:LookupConditionalDistributionPrediction
  path: data/curated/LookupConditionalDistributionPrediction.yaml
  label: Lookup Conditional Distribution Prediction
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LookupConditionalDistributionPrediction.yaml
    role: maintained
scope:
  description: Section attribution of CDP recurrence and frontier passages.
  selection: Exact maintained ID AIMech:LookupConditionalDistributionPrediction
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:LookupConditionalDistributionPrediction
  exclusions:
  - target: Corrected-input complete review
    reason: Pending locator correction and publication gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:LookupConditionalDistributionPrediction
  summary: The corrected record does not yet exist; its publication gates remain pending.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/LookupConditionalDistributionPrediction.yaml
  accessed_at: '2026-10-13T18:59:09Z'
  snapshot_sha256: 2fdc651cfa5f1e7de067edf8dbc69fb1856f2436e5adc9392ec27f6745ee7481
  support: supports
  summary: Complete maintained record read after capture; two claim locators misidentify
    Section2 content as Section3.
- evidence_id: paper
  kind: primary_source
  reference: https://webdocs.cs.ualberta.ca/~santanad/papers/2013/ARTINT2694.pdf
  accessed_at: '2026-10-13T17:23:34Z'
  snapshot_sha256: ee16910b3529eab60bc1527773d4d91d77d81778a153d33f7a8d6e80c09f6fba
  support: supports
  locator: PDFpp3–5 / printed54–56, Section2 heading and boundary with Section3; PDFpp16–17
    / printed67–68, Section7.
  summary: All25 pages previously visually read. After capture, pages3–5,10–11,16–18
    and21–24 reread. Section2 begins on PDFp3, includes the recurrence onp4 and ends
    before the Section3 heading near the bottom ofp5.
assessments:
- assessment_id: section-locators
  area: evidence
  topic: Source-section attribution
  outcome: concern
  target_ids:
  - AIMech:LookupConditionalDistributionPrediction
  evidence_ids:
  - record
  - paper
  summary: Correct two section labels while retaining accurate page ranges.
  details: The shallow-frontier-accounting locator names Section3 for PDFp5 although
    the frontier paragraph precedes the Section3 heading and belongs to Section2.
    The fixed-model-equivalence locator names Sections3–4 for PDFpp4–7 although the
    recurrence on PDFp4 is also in Section2. Their PDF/printed page ranges remain
    useful, but section labels should be corrected to Section2 and Sections2–4 respectively.
    Section7/7.1 references remain correct.
findings:
- finding_id: F1
  issue_key: lookup-cdp-recurrence-section-locators
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the CDP framework section labels in two evidence locators
  description: The shallow-frontier-accounting locator names Section3 for PDFp5 although
    the frontier paragraph precedes the Section3 heading and belongs to Section2.
    The fixed-model-equivalence locator names Sections3–4 for PDFpp4–7 although the
    recurrence on PDFp4 is also in Section2. Their PDF/printed page ranges remain
    useful, but section labels should be corrected to Section2 and Sections2–4 respectively.
    Section7/7.1 references remain correct.
  target_ids:
  - AIMech:LookupConditionalDistributionPrediction
  field_paths:
  - claims[shallow-frontier-accounting].evidence[0].locator
  - claims[fixed-model-equivalence].evidence[0].locator
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LookupConditionalDistributionPrediction.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct the two maintained locators, synchronize the discovery report,
    append correction history, recapture and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:LookupConditionalDistributionPrediction
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LookupConditionalDistributionPrediction.yaml
    role: maintained
  acceptance_checks:
  - The frontier locator cites Section2 and7; the recurrence locator cites Sections2–4
    and7.1 with unchanged accurate page ranges.
  - Record/report mirrors agree and rendered pages are regenerated.
  - Corrected-input gates and a linked successor review pass.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- citation-provenance
```
