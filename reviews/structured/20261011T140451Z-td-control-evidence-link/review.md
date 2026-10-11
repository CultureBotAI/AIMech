# TD control-application evidence-link self-review

- Review: 20261011T140451Z-td-control-evidence-link
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T14:04:13Z
- Finished UTC: 2026-10-11T14:04:51Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Link the inspected author-book source to a precise TD control-application scope claim.

## Scope And Provenance

TD source-to-claim linkage for its reinforcement-learning application.

Selection: Exact maintained TD record and author-book-draft evidence source.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3ec6606efefc44056a640b338097a6c368238332.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TemporalDifferenceLearning | data/curated/TemporalDifferenceLearning.yaml | maintained | Temporal-difference learning |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Validate curated corpus | failed | True | AIMech:TemporalDifferenceLearning | ERROR data/curated/TemporalDifferenceLearning.yaml: evidence_sources: uncited sources author-book-draft<br>Checked 301 curated concept record(s); 1 error(s).<br> |

## Scientific And Domain Assessments

### Evidence graph and control-application scope

evidence: concern. Targets: AIMech:TemporalDifferenceLearning.

The scientific connection is supported, but the maintained claim-to-source graph omits its precise citation.

## Findings

### td-control-evidence-link: TD author-book source is not linked to an asserted claim.

minor / open / confirmed; issue key: CultureBotAI-AIMech-TD-control-evidence-link.

Add a narrow scope claim that TD prediction can supply value estimates for control, with a precise citation to Section 6.4 of the versioned author draft. Keep prediction distinct from action selection and policy improvement; do not attach the book indiscriminately to unrelated 1988 equations.

## Recommended Actions And Acceptance Checks

### link-control-scope

Add the supported scope claim and citation, synchronize ledger/history, and save a successor review after validation.

- The new scope claim cites author-book-draft Section 6.4 with PDF and printed page locators.
- The claim preserves the distinction between TD prediction and the complete control algorithm.
- The ledger and append-only history record the correction; required checks pass and a successor resolves this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| book-scope | http://incompleteideas.net/book/bookdraft2016sep.pdf; Section 6.4, PDF pp.155–156 / printed pp.137–138, TD prediction applied to control | supports | The inspected author draft uses TD prediction for the evaluation component of on-policy control while improving the behavior policy. Prediction alone is not a policy optimizer. |
| draft | data/curated/TemporalDifferenceLearning.yaml; evidence_sources[source_id=author-book-draft], claims and aio_mappings | context_only | The book source is listed and the mapping rationale refers to Section 6.4, but no definition or claim cites its source_id. The native validator reports the unlinked source. |

## Limits And Additional Notes

- Partial author self-review of one evidence-link defect; not full-cohort approval.
- Curated validation failed as reported; the full publication gate has not yet been claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T140451Z-td-control-evidence-link
kind: record
repository: CultureBotAI/AIMech
title: TD control-application evidence-link self-review
started_at: '2026-10-11T14:04:13Z'
finished_at: '2026-10-11T14:04:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent checked the source-to-claim graph and inspected
    the cited book section. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Link the inspected author-book source to a precise TD control-application
  scope claim.
source:
  git_revision: 3ec6606efefc44056a640b338097a6c368238332
  state: working_tree
  inputs:
  - path: data/aio/ContinualLearning.yaml
    sha256: c55fe9b9214b2f98c463af6c6756d71d7b070e9f35cb1dbba0a1b400073bf9b3
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AntNet.yaml
    sha256: e7d511a9923dd43bea25f50c09619789c9fbeaa7f4677344007cc0a9c1836c50
    role: context
  - path: data/curated/AntQ.yaml
    sha256: a01fc6b6c6529db01836d0bf7b63a02948ea5dd640af3a9c6c5044f411c7acfe
    role: context
  - path: data/curated/DeepQNetwork.yaml
    sha256: ea346f5f8650c02e1d8d825c896797e3c022f20525d07b64b96f97ae96a1df2a
    role: context
  - path: data/curated/GeneralizedAdvantageEstimation.yaml
    sha256: 635b1bffb626af1c9eff6e17f1fda088aed1d05b55abc0fd4fd7be3ccf19ee77
    role: context
  - path: data/curated/ProximalPolicyOptimization.yaml
    sha256: 073aed5362b80546287548c4a1520105bb228b146a751cbccc879429f22b3661
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: context
  - path: data/curated/QRouting.yaml
    sha256: f518c72943e8f068c2e708fa3c0c64bedd8ad09c86e41ef06a82043ad0255ce4
    role: target
  - path: data/curated/Sarsa.yaml
    sha256: 8ac6efbbcfeda82ce462fbc7f6d641a9eab36b8749c6bdb0b7713ba43496e041
    role: target
  - path: data/curated/TemporalDifferenceLearning.yaml
    sha256: 11424ff95d5024359cd99dd5e4d21d763c2eafd60578dbff11c67627abfde091
    role: target
  - path: research/discovery/20261011T140315Z-temporal-prediction-and-routing.json
    sha256: 98852c6212282abd21543abccfbd4662fec3c87977174483725a52b81969678e
    role: context
  - path: research/discovery/temporal-prediction-and-routing-boundaries.py
    sha256: 9768653cb541ed19c47f4084dbcdf5eae0b0c3e49f28b400b3f345a1998598c9
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
- target_id: AIMech:TemporalDifferenceLearning
  path: data/curated/TemporalDifferenceLearning.yaml
  label: Temporal-difference learning
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalDifferenceLearning.yaml
    role: maintained
scope:
  description: TD source-to-claim linkage for its reinforcement-learning application.
  selection: Exact maintained TD record and author-book-draft evidence source.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TemporalDifferenceLearning
  exclusions:
  - target: Full cohort approval
    reason: This partial observation isolates one evidence-link defect; the complete
      cohort review follows correction and required checks.
checks:
- check_id: curated-validation
  name: Validate curated corpus
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: failed
  required: true
  target_ids:
  - AIMech:TemporalDifferenceLearning
  exit_code: 1
  expected_exit_code: 0
  summary: 'ERROR data/curated/TemporalDifferenceLearning.yaml: evidence_sources:
    uncited sources author-book-draft

    Checked 301 curated concept record(s); 1 error(s).

    '
evidence:
- evidence_id: book-scope
  kind: primary_source
  reference: http://incompleteideas.net/book/bookdraft2016sep.pdf
  locator: Section 6.4, PDF pp.155–156 / printed pp.137–138, TD prediction applied
    to control
  accessed_at: '2026-10-11T13:53:08Z'
  snapshot_sha256: 94b195c3d5f73878039453d8fc771494df0c140fd6978fd0c6d29178a56023b5
  support: supports
  summary: The inspected author draft uses TD prediction for the evaluation component
    of on-policy control while improving the behavior policy. Prediction alone is
    not a policy optimizer.
- evidence_id: draft
  kind: record_content
  reference: data/curated/TemporalDifferenceLearning.yaml
  locator: evidence_sources[source_id=author-book-draft], claims and aio_mappings
  accessed_at: '2026-10-11T14:04:51Z'
  support: context_only
  summary: The book source is listed and the mapping rationale refers to Section 6.4,
    but no definition or claim cites its source_id. The native validator reports the
    unlinked source.
assessments:
- assessment_id: evidence-link
  area: evidence
  topic: Evidence graph and control-application scope
  outcome: concern
  target_ids:
  - AIMech:TemporalDifferenceLearning
  evidence_ids:
  - book-scope
  - draft
  summary: The scientific connection is supported, but the maintained claim-to-source
    graph omits its precise citation.
findings:
- finding_id: td-control-evidence-link
  issue_key: CultureBotAI-AIMech-TD-control-evidence-link
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:TemporalDifferenceLearning
  field_paths:
  - claims
  - evidence_sources[source_id=author-book-draft]
  evidence_ids:
  - book-scope
  - draft
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalDifferenceLearning.yaml
    role: maintained
  title: TD author-book source is not linked to an asserted claim.
  description: Add a narrow scope claim that TD prediction can supply value estimates
    for control, with a precise citation to Section 6.4 of the versioned author draft.
    Keep prediction distinct from action selection and policy improvement; do not
    attach the book indiscriminately to unrelated 1988 equations.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/85
actions:
- action_id: link-control-scope
  finding_ids:
  - td-control-evidence-link
  target_ids:
  - AIMech:TemporalDifferenceLearning
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalDifferenceLearning.yaml
    role: maintained
  description: Add the supported scope claim and citation, synchronize ledger/history,
    and save a successor review after validation.
  acceptance_checks:
  - The new scope claim cites author-book-draft Section 6.4 with PDF and printed page
    locators.
  - The claim preserves the distinction between TD prediction and the complete control
    algorithm.
  - The ledger and append-only history record the correction; required checks pass
    and a successor resolves this finding.
boundary_decisions: []
limitations:
- Partial author self-review of one evidence-link defect; not full-cohort approval.
- Curated validation failed as reported; the full publication gate has not yet been
  claimed.
links:
- https://github.com/CultureBotAI/AIMech/issues/85
```
