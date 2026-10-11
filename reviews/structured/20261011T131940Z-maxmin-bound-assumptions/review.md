# MAX–MIN bound-assumption self-review

- Review: 20261011T131940Z-maxmin-bound-assumptions
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T13:18:15Z
- Finished UTC: 2026-10-11T13:19:40Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The lower-bound formula needs its TSP and unit-exponent scope and an exact equation locator.

## Scope And Provenance

MAX–MIN lower trail-limit transcription and its scope.

Selection: Exact maintained record and method claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c694a649a01f4fbd3979c6aadc0df44125c71182.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MaxMinAntSystem | data/curated/MaxMinAntSystem.yaml | maintained | MAX–MIN Ant System |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original finite exponent diagnostic | passed | True | AIMech:MaxMinAntSystem | The simplified probabilities are .04999999999999999 for alpha=1 and .7404941146568779 for alpha=2; the unit-exponent assumption matters. |

## Scientific And Domain Assessments

### Scope and locator of the lower trail-limit heuristic

consistency: concern. Targets: AIMech:MaxMinAntSystem.

The approximation warning is useful but does not state all assumptions needed to interpret the displayed formula.

## Findings

### maxmin-bound-assumptions: MAX–MIN lower-bound formula omits its TSP and unit-exponent scope.

minor / open / confirmed; issue key: CultureBotAI-AIMech-MaxMinAntSystem-bound-assumptions.

The formula is a TSP approximation with n cities, avg=n/2, linear pheromone weighting and neglected heuristic differences. The draft leaves n undefined after a general exponent-based construction rule and omits Equations 10–11 from its locator. State the scope and correct the locator without changing the algorithm identity.

## Recommended Actions And Acceptance Checks

### qualify-bound

Qualify the maintained formula, correct its citation, extend the finite calculation, update ledger/history and save a successor review.

- Define n as TSP city count and avg=n/2 as the simplified branching approximation.
- State alpha=1 and neglected heuristic differences; cite Equations 8–11.
- Record the alpha=2 counterexample, pass repository checks, and save a successor disposition linked to issue 80.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary-bound | https://www.cs.ubc.ca/~hoos/Publ/fgcs00.pdf; Section 4.2, PDF pp.16–17, Equations 8–11 and footnote 5; Section 4.4, PDF p.18, alpha=1 settings | refutes | The displayed lower-limit rule uses a simplified TSP branch count and linear pheromone weights; it is Equation 11. The general construction rule raises trails to alpha. |
| draft | data/curated/MaxMinAntSystem.yaml; claims[claim_id=method].statement and associated evidence locators | context_only | The draft gives the general exponent rule and the simplified bound without defining n or stating alpha=1, and its equation-range locator stops at 9. |

## Limits And Additional Notes

- This partial scientific self-review isolates one formula-scope defect; it is not full-cohort approval.
- The full gate is still in progress. No unfinished check is reported as passed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T131940Z-maxmin-bound-assumptions
kind: record
repository: CultureBotAI/AIMech
title: MAX–MIN bound-assumption self-review
started_at: '2026-10-11T13:18:15Z'
finished_at: '2026-10-11T13:19:40Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent compared the draft with primary equations
    and a finite counterexample. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The lower-bound formula needs its TSP and unit-exponent scope and an exact
  equation locator.
source:
  git_revision: c694a649a01f4fbd3979c6aadc0df44125c71182
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
  - path: data/curated/AntColonySystem.yaml
    sha256: 9069dd63cc6c1710594246d2817d162b6cd42f2ee383ad84e9cb7a17f94dfc2f
    role: target
  - path: data/curated/AntSystem.yaml
    sha256: 89aa5c8e5a5d8ae3717bcd5c3be94d32543402900872533c1c4a6bbdf41f506c
    role: target
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: context
  - path: data/curated/DifferentialEvolution.yaml
    sha256: 8c937f585818445a809f6aa26c51c4195e1fe2e3a634d349762322f89e97ff68
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/MaxMinAntSystem.yaml
    sha256: 09dc20f65151d7b1dedb38beab0f17494a67723bdf1996cbaada069d2bac750e
    role: target
  - path: data/curated/ParticleSwarmOptimization.yaml
    sha256: bd0c2298ecb01d94702f09f6ef1766c3b51216b4a4dbca9ae1c99142f5807d08
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: research/discovery/20261011T131757Z-constructive-ant-search.json
    sha256: bd532ff1e1c9adfb1e6c4942010e25368fefc6b30c593ca56d12a4553ae672c8
    role: context
  - path: research/discovery/ant-search-boundaries.py
    sha256: d2ff5b1b530ffc01b717a6c17319dd1a84038e91294d28c9b8581423d9ea972d
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
- target_id: AIMech:MaxMinAntSystem
  path: data/curated/MaxMinAntSystem.yaml
  label: MAX–MIN Ant System
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaxMinAntSystem.yaml
    role: maintained
scope:
  description: MAX–MIN lower trail-limit transcription and its scope.
  selection: Exact maintained record and method claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:MaxMinAntSystem
  exclusions:
  - target: Complete record and cohort approval
    reason: This observation isolates one mathematical-scope defect; the final cohort
      review follows remediation and required checks.
checks:
- check_id: exponent-counterexample
  name: Original finite exponent diagnostic
  command: 'Python stdlib: n=10, p_best=.05, upper=2; compare (upper**alpha/(upper**alpha+(n/2-1)*lower**alpha))**n
    for alpha=1 and 2'
  status: passed
  required: true
  target_ids:
  - AIMech:MaxMinAntSystem
  exit_code: 0
  expected_exit_code: 0
  summary: The simplified probabilities are .04999999999999999 for alpha=1 and .7404941146568779
    for alpha=2; the unit-exponent assumption matters.
evidence:
- evidence_id: primary-bound
  kind: primary_source
  reference: https://www.cs.ubc.ca/~hoos/Publ/fgcs00.pdf
  locator: Section 4.2, PDF pp.16–17, Equations 8–11 and footnote 5; Section 4.4,
    PDF p.18, alpha=1 settings
  accessed_at: '2026-10-11T13:19:40Z'
  snapshot_sha256: 0d4052ac21364e50e5b6aefb5fe2eda14e9c376698435aa81e4ab500dcb1b53a
  support: refutes
  summary: The displayed lower-limit rule uses a simplified TSP branch count and linear
    pheromone weights; it is Equation 11. The general construction rule raises trails
    to alpha.
- evidence_id: draft
  kind: record_content
  reference: data/curated/MaxMinAntSystem.yaml
  locator: claims[claim_id=method].statement and associated evidence locators
  accessed_at: '2026-10-11T13:19:40Z'
  support: context_only
  summary: The draft gives the general exponent rule and the simplified bound without
    defining n or stating alpha=1, and its equation-range locator stops at 9.
assessments:
- assessment_id: bound-scope
  area: consistency
  topic: Scope and locator of the lower trail-limit heuristic
  outcome: concern
  target_ids:
  - AIMech:MaxMinAntSystem
  evidence_ids:
  - primary-bound
  - draft
  summary: The approximation warning is useful but does not state all assumptions
    needed to interpret the displayed formula.
findings:
- finding_id: maxmin-bound-assumptions
  issue_key: CultureBotAI-AIMech-MaxMinAntSystem-bound-assumptions
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:MaxMinAntSystem
  field_paths:
  - claims[claim_id=method].statement
  - definition_evidence
  - claims[claim_id=method].evidence
  evidence_ids:
  - primary-bound
  - draft
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaxMinAntSystem.yaml
    role: maintained
  title: MAX–MIN lower-bound formula omits its TSP and unit-exponent scope.
  description: The formula is a TSP approximation with n cities, avg=n/2, linear pheromone
    weighting and neglected heuristic differences. The draft leaves n undefined after
    a general exponent-based construction rule and omits Equations 10–11 from its
    locator. State the scope and correct the locator without changing the algorithm
    identity.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/80
actions:
- action_id: qualify-bound
  finding_ids:
  - maxmin-bound-assumptions
  target_ids:
  - AIMech:MaxMinAntSystem
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaxMinAntSystem.yaml
    role: maintained
  description: Qualify the maintained formula, correct its citation, extend the finite
    calculation, update ledger/history and save a successor review.
  acceptance_checks:
  - Define n as TSP city count and avg=n/2 as the simplified branching approximation.
  - State alpha=1 and neglected heuristic differences; cite Equations 8–11.
  - Record the alpha=2 counterexample, pass repository checks, and save a successor
    disposition linked to issue 80.
boundary_decisions: []
limitations:
- This partial scientific self-review isolates one formula-scope defect; it is not
  full-cohort approval.
- The full gate is still in progress. No unfinished check is reported as passed.
links:
- https://github.com/CultureBotAI/AIMech/issues/80
```
