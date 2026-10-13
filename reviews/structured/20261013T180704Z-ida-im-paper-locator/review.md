# IDA*IM primary-paper locator finding

- Review: 20261013T180704Z-ida-im-paper-locator
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T18:06:04Z
- Finished UTC: 2026-10-13T18:07:04Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor primary-paper locator provenance issue.

## Scope And Provenance

Provenance of the constructed two-goal example.

Selection: Exact maintained ID AIMech:IDAStarIncrementalModel
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 494a4e1381f7ee799c8970f09336b3afa3948783.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IDAStarIncrementalModel | data/curated/IDAStarIncrementalModel.yaml | maintained | IDA* with an Incremental Model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:IDAStarIncrementalModel | Correction and its publication gates have not yet run. |

## Scientific And Domain Assessments

### Local example provenance

evidence: concern. Targets: AIMech:IDAStarIncrementalModel.

Restrict primary-paper locator to actual source passages.

The final-iteration-and-correctness-scope evidence locator appends a constructed two-goal threshold example to the burns2013im primary-paper citation. That example is maintained in research/discovery/ida-im-boundaries.py, not a passage in the cited PDF. Keep only actual paper sections/pages in this locator and retain the calculation under its separately identified discovery/review evidence.

## Findings

### F1: Keep the local example outside the primary-paper locator

minor / open / confirmed; issue key: ida-im-paper-locator-local-example.

The final-iteration-and-correctness-scope evidence locator appends a constructed two-goal threshold example to the burns2013im primary-paper citation. That example is maintained in research/discovery/ida-im-boundaries.py, not a passage in the cited PDF. Keep only actual paper sections/pages in this locator and retain the calculation under its separately identified discovery/review evidence.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained locator, synchronize report, append history, recapture and reassess.

- Primary-paper locator lists only actual manuscript sections/pages; local calculation retains separate evidence ownership.
- Corrected record/report agree and rendered pages are regenerated.
- Corrected-input gates and linked successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/IDAStarIncrementalModel.yaml | supports | Complete record read after capture; the primary-paper locator includes a locally constructed example. |
| paper | https://www.cs.unh.edu/~ruml/papers/im-amai-13.pdf; PDF pages 10–13, Sections 4–4.2. | supports | All 24 manuscript pages previously read; pages 5–13, 16–21 and 24 visually reread after capture. The cited text describes final branch-and-bound, while the constructed two-goal calculation is local evidence. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T180704Z-ida-im-paper-locator
kind: record
repository: CultureBotAI/AIMech
title: IDA*IM primary-paper locator finding
started_at: '2026-10-13T18:06:04Z'
finished_at: '2026-10-13T18:07:04Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author checked source locators against the manuscript and local
    calculation; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor primary-paper locator provenance issue.
source:
  git_revision: 494a4e1381f7ee799c8970f09336b3afa3948783
  state: working_tree
  inputs:
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/curated/BreadthFirstIDAStar.yaml
    sha256: 6a769cf81b4b128f652ba6b7340563a855a12e73f9a689e5f3d83d6baae0b20c
    role: context
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 077b5924af54bda151c2fbadcd173d1a856627530a187078c56c932d959949ef
    role: target
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/RBFSControlledReexpansion.yaml
    sha256: 6ed34a212cc75612117ef1daf276ba4b5e7a65eeb3c7fbb4a2a9890adccef8e4
    role: context
  - path: research/discovery/20261013T180602Z-ida-star-incremental-model.json
    sha256: a5042cac122c2661aacdf402d8063345a72f7287249e80131c5918a4c7471528
    role: context
  - path: research/discovery/ida-im-boundaries.py
    sha256: 5ef7d94ae73cd29b9ff661a7ab384ef882dfe6dbfc84335df87acc369907c548
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
- target_id: AIMech:IDAStarIncrementalModel
  path: data/curated/IDAStarIncrementalModel.yaml
  label: IDA* with an Incremental Model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IDAStarIncrementalModel.yaml
    role: maintained
scope:
  description: Provenance of the constructed two-goal example.
  selection: Exact maintained ID AIMech:IDAStarIncrementalModel
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:IDAStarIncrementalModel
  exclusions:
  - target: Corrected-input complete review
    reason: Pending correction and publication gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:IDAStarIncrementalModel
  summary: Correction and its publication gates have not yet run.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/IDAStarIncrementalModel.yaml
  accessed_at: '2026-10-13T18:07:04Z'
  snapshot_sha256: 077b5924af54bda151c2fbadcd173d1a856627530a187078c56c932d959949ef
  support: supports
  summary: Complete record read after capture; the primary-paper locator includes
    a locally constructed example.
- evidence_id: paper
  kind: primary_source
  reference: https://www.cs.unh.edu/~ruml/papers/im-amai-13.pdf
  accessed_at: '2026-10-13T16:44:38Z'
  snapshot_sha256: fd8b123fff9071db47b98df13362b1085dec51189ed2e20d5d12204efdc45d99
  support: supports
  locator: PDF pages 10–13, Sections 4–4.2.
  summary: All 24 manuscript pages previously read; pages 5–13, 16–21 and 24 visually
    reread after capture. The cited text describes final branch-and-bound, while the
    constructed two-goal calculation is local evidence.
assessments:
- assessment_id: locator-provenance
  area: evidence
  topic: Local example provenance
  outcome: concern
  target_ids:
  - AIMech:IDAStarIncrementalModel
  evidence_ids:
  - record
  - paper
  summary: Restrict primary-paper locator to actual source passages.
  details: The final-iteration-and-correctness-scope evidence locator appends a constructed
    two-goal threshold example to the burns2013im primary-paper citation. That example
    is maintained in research/discovery/ida-im-boundaries.py, not a passage in the
    cited PDF. Keep only actual paper sections/pages in this locator and retain the
    calculation under its separately identified discovery/review evidence.
findings:
- finding_id: F1
  issue_key: ida-im-paper-locator-local-example
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Keep the local example outside the primary-paper locator
  description: The final-iteration-and-correctness-scope evidence locator appends
    a constructed two-goal threshold example to the burns2013im primary-paper citation.
    That example is maintained in research/discovery/ida-im-boundaries.py, not a passage
    in the cited PDF. Keep only actual paper sections/pages in this locator and retain
    the calculation under its separately identified discovery/review evidence.
  target_ids:
  - AIMech:IDAStarIncrementalModel
  field_paths:
  - claims[final-iteration-and-correctness-scope].evidence[0].locator
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IDAStarIncrementalModel.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct the maintained locator, synchronize report, append history,
    recapture and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:IDAStarIncrementalModel
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IDAStarIncrementalModel.yaml
    role: maintained
  acceptance_checks:
  - Primary-paper locator lists only actual manuscript sections/pages; local calculation
    retains separate evidence ownership.
  - Corrected record/report agree and rendered pages are regenerated.
  - Corrected-input gates and linked successor review pass.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- citation-provenance
```
