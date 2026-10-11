# AntNet neighbor-eligibility self-review

- Review: 20261011T134916Z-antnet-neighbor-eligibility
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T13:48:05Z
- Finished UTC: 2026-10-11T13:49:16Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Replace AntNet’s soft unvisited-neighbor wording with the source’s required two-case eligible-set rule.

## Scope And Provenance

AntNet forward-ant next-hop eligibility wording.

Selection: Exact maintained record and method claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8d6f2185ea286454f2f5577e4e0686af6d0aaf32.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AntNet | data/curated/AntNet.yaml | maintained | AntNet |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Finite update and subset-normalization arithmetic | passed | True | AIMech:AntNet | The full-neighbor probabilities sum to one, but excluding the third neighbor leaves mass .59375 and requires conditional normalization. This supports the importance of an explicit eligible set; it is not an AntNet simulator. |

## Scientific And Domain Assessments

### Hard eligible-set rule versus soft preference

consistency: concern. Targets: AIMech:AntNet.

The wording should state the two cases explicitly to preserve cycle behavior and the meaning of the restricted-set normalization qualification.

## Findings

### antnet-neighbor-eligibility: AntNet eligibility is phrased as a soft preference.

minor / open / confirmed; issue key: CultureBotAI-AIMech-AntNet-neighbor-eligibility.

Preferably unvisited can permit revisiting despite available unvisited neighbors. The primary method restricts choices to unvisited neighbors whenever possible and falls back to all neighbors only when all were visited. Make the two cases explicit without changing the separate numerical-normalization qualification.

## Recommended Actions And Acceptance Checks

### clarify-eligibility

Correct the maintained method claim, synchronize ledger/history and save a successor review after checks.

- Explicitly choose only unvisited neighbors when any exist, otherwise use all neighbors.
- Retain the restricted-set renormalization and zero-queue qualifications.
- Synchronize the ledger, append history, pass required checks and save a linked resolved disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary-eligibility | https://arxiv.org/pdf/1105.5449; Section 4.1 item 3, PDF p.11 / journal p.327, verified against the page image | refutes | Choose among neighbors not already visited whenever any are available; use all neighbors only if all were previously visited. This is an eligibility constraint, not merely a preference. |
| draft | data/curated/AntNet.yaml; claims[claim_id=method].statement | context_only | The draft says preferably unvisited neighbors, which can be read as allowing an already visited neighbor while an unvisited choice exists. |

## Limits And Additional Notes

- Partial adversarial author self-review of a wording defect; not full-cohort approval.
- The full gate is in progress and is not reported as passed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T134916Z-antnet-neighbor-eligibility
kind: record
repository: CultureBotAI/AIMech
title: AntNet neighbor-eligibility self-review
started_at: '2026-10-11T13:48:05Z'
finished_at: '2026-10-11T13:49:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent compared the draft against the primary method
    text and page image. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Replace AntNet’s soft unvisited-neighbor wording with the source’s required
  two-case eligible-set rule.
source:
  git_revision: 8d6f2185ea286454f2f5577e4e0686af6d0aaf32
  state: working_tree
  inputs:
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
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
  - path: data/curated/AntColonyOptimization.yaml
    sha256: d65642ea5cac777843fa0285d27a8b8bc129c2544528ba122c7144c0eb794f9d
    role: target
  - path: data/curated/AntColonySystem.yaml
    sha256: 9069dd63cc6c1710594246d2817d162b6cd42f2ee383ad84e9cb7a17f94dfc2f
    role: context
  - path: data/curated/AntNet.yaml
    sha256: b1d6f7fc0f50d154d3f0e1ac74246e43acc460bdb0a0e4701da623f5c0303fea
    role: target
  - path: data/curated/AntQ.yaml
    sha256: a01fc6b6c6529db01836d0bf7b63a02948ea5dd640af3a9c6c5044f411c7acfe
    role: context
  - path: data/curated/AntSystem.yaml
    sha256: 89aa5c8e5a5d8ae3717bcd5c3be94d32543402900872533c1c4a6bbdf41f506c
    role: context
  - path: data/curated/DeepQNetwork.yaml
    sha256: ea346f5f8650c02e1d8d825c896797e3c022f20525d07b64b96f97ae96a1df2a
    role: context
  - path: data/curated/MaxMinAntSystem.yaml
    sha256: 6f50bb6ce0399ffeeeab89c1ebc7ab94e2360da5708618f7ac2ff2d3dad37837
    role: context
  - path: data/curated/PopulationBasedIncrementalLearning.yaml
    sha256: fb2500f70c8a0cf57639b33f7f89acf9f141adf75a238aa248e784afc09866d2
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: target
  - path: research/discovery/20261011T134751Z-value-learning-and-ant-routing.json
    sha256: 9c2bcefede1a1c9546e21c9dc8a4f9a099b778b3b283fa682264dbf4615a7fac
    role: context
  - path: research/discovery/value-learning-and-ant-routing-boundaries.py
    sha256: 4165542caeda9461f00b0f3974c0d13a03ac1f0bc4c255325fdb0cd708624b9b
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
- target_id: AIMech:AntNet
  path: data/curated/AntNet.yaml
  label: AntNet
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntNet.yaml
    role: maintained
scope:
  description: AntNet forward-ant next-hop eligibility wording.
  selection: Exact maintained record and method claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AntNet
  exclusions:
  - target: Complete record and cohort approval
    reason: This partial observation isolates one mechanism wording defect; the full
      review follows remediation and checks.
checks:
- check_id: finite-eligibility
  name: Finite update and subset-normalization arithmetic
  command: python3 research/discovery/value-learning-and-ant-routing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AntNet
  exit_code: 0
  expected_exit_code: 0
  summary: The full-neighbor probabilities sum to one, but excluding the third neighbor
    leaves mass .59375 and requires conditional normalization. This supports the importance
    of an explicit eligible set; it is not an AntNet simulator.
evidence:
- evidence_id: primary-eligibility
  kind: primary_source
  reference: https://arxiv.org/pdf/1105.5449
  locator: Section 4.1 item 3, PDF p.11 / journal p.327, verified against the page
    image
  accessed_at: '2026-10-11T13:49:16Z'
  snapshot_sha256: bee45446fa421191bd2e9396261532b5a0a6c339c369792b37506a0242cd867d
  support: refutes
  summary: Choose among neighbors not already visited whenever any are available;
    use all neighbors only if all were previously visited. This is an eligibility
    constraint, not merely a preference.
- evidence_id: draft
  kind: record_content
  reference: data/curated/AntNet.yaml
  locator: claims[claim_id=method].statement
  accessed_at: '2026-10-11T13:49:16Z'
  support: context_only
  summary: The draft says preferably unvisited neighbors, which can be read as allowing
    an already visited neighbor while an unvisited choice exists.
assessments:
- assessment_id: eligibility-scope
  area: consistency
  topic: Hard eligible-set rule versus soft preference
  outcome: concern
  target_ids:
  - AIMech:AntNet
  evidence_ids:
  - primary-eligibility
  - draft
  summary: The wording should state the two cases explicitly to preserve cycle behavior
    and the meaning of the restricted-set normalization qualification.
findings:
- finding_id: antnet-neighbor-eligibility
  issue_key: CultureBotAI-AIMech-AntNet-neighbor-eligibility
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:AntNet
  field_paths:
  - claims[claim_id=method].statement
  evidence_ids:
  - primary-eligibility
  - draft
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntNet.yaml
    role: maintained
  title: AntNet eligibility is phrased as a soft preference.
  description: Preferably unvisited can permit revisiting despite available unvisited
    neighbors. The primary method restricts choices to unvisited neighbors whenever
    possible and falls back to all neighbors only when all were visited. Make the
    two cases explicit without changing the separate numerical-normalization qualification.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/83
actions:
- action_id: clarify-eligibility
  finding_ids:
  - antnet-neighbor-eligibility
  target_ids:
  - AIMech:AntNet
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntNet.yaml
    role: maintained
  description: Correct the maintained method claim, synchronize ledger/history and
    save a successor review after checks.
  acceptance_checks:
  - Explicitly choose only unvisited neighbors when any exist, otherwise use all neighbors.
  - Retain the restricted-set renormalization and zero-queue qualifications.
  - Synchronize the ledger, append history, pass required checks and save a linked
    resolved disposition.
boundary_decisions: []
limitations:
- Partial adversarial author self-review of a wording defect; not full-cohort approval.
- The full gate is in progress and is not reported as passed.
links:
- https://github.com/CultureBotAI/AIMech/issues/83
```
