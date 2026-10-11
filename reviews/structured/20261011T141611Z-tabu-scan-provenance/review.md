# Tabu source-date wording self-review

- Review: 20261011T141611Z-tabu-scan-provenance
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T14:14:42Z
- Finished UTC: 2026-10-11T14:16:11Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Describe the observed 2001 copyright footer without inferring when it was inserted.

## Scope And Provenance

Source-version provenance wording only.

Selection: Exact TabuSearch evidence-source version field.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3d674f776b786af1a882a6a5c793652d081a19f8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TabuSearch | data/curated/TabuSearch.yaml | maintained | Tabu search |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Verify pinned AIO source | passed | True | AIMech:TabuSearch | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |

## Scientific And Domain Assessments

### Observed notice versus inferred insertion date

provenance: concern. Targets: AIMech:TabuSearch.

Preserve the publication/scan distinction while removing the unsupported insertion-date inference.

## Findings

### tabu-scan-provenance: The footer’s date is treated as its insertion date.

minor / open / confirmed; issue key: CultureBotAI-AIMech-TabuSearch-scan-provenance.

Replace added in 2001 with a description that the scan contains a 2001 copyright footer. Retain the verified 1989 article date and exact source checksum.

## Recommended Actions And Acceptance Checks

### qualify-scan-date

Correct the source version, synchronize ledger/history, and save a linked successor after checks.

- The version describes the visible 2001 notice without inferring insertion time.
- The 1989 article date and inspected source checksum remain accurate.
- Ledger/history and successor disposition preserve the correction; required checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| pdf-dates | https://leeds-faculty.colorado.edu/glover/TS%20-%20Part%20I-ORSA-aw.pdf; PDF p.1 journal header and PDF p.3 copyright footer, visually inspected | supports | The article header identifies volume 1 number 3, Summer 1989; the scan footer says Copyright 2001. Those observations do not date insertion of the footer. |
| draft | data/curated/TabuSearch.yaml; evidence_sources[0].version | context_only | The draft describes a footer added in 2001, going beyond the date visibly printed in it. |

## Limits And Additional Notes

- Provenance-only partial author self-review; scientific_review is false.
- The full gate is still running and is not reported as passed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T141611Z-tabu-scan-provenance
kind: record
repository: CultureBotAI/AIMech
title: Tabu source-date wording self-review
started_at: '2026-10-11T14:14:42Z'
finished_at: '2026-10-11T14:16:11Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent compared source-version wording with the
    inspected PDF cover and footer. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: false
summary: Describe the observed 2001 copyright footer without inferring when it was
  inserted.
source:
  git_revision: 3d674f776b786af1a882a6a5c793652d081a19f8
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
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: context
  - path: data/curated/AntColonyOptimization.yaml
    sha256: d65642ea5cac777843fa0285d27a8b8bc129c2544528ba122c7144c0eb794f9d
    role: context
  - path: data/curated/AntSystem.yaml
    sha256: 89aa5c8e5a5d8ae3717bcd5c3be94d32543402900872533c1c4a6bbdf41f506c
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/GuidedLocalSearch.yaml
    sha256: 91618dff5e0ed6681aad81deb9be9c8e35ed43b42acad285ef473916852cdebc
    role: target
  - path: data/curated/IteratedLocalSearch.yaml
    sha256: 15a6a25711dabac3dff72b612cf7daa7a2ae5f9660a9a677c2d21163335f2ef0
    role: target
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/TabuSearch.yaml
    sha256: 3427acad82c3475a354d07a935be8b9ac86023af42d270cd5d81f7a565650f9e
    role: target
  - path: research/discovery/20261011T141428Z-local-search-frameworks.json
    sha256: 17a16fcd08f768b286d6bda7dfb412027bc290e0799de027df00e5986f970487
    role: context
  - path: research/discovery/local-search-frameworks-boundaries.py
    sha256: d602b6d0ee9cfcc2511de28b722eb648c42756bb847d6d1e5a7eed6b1345a25f
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
- target_id: AIMech:TabuSearch
  path: data/curated/TabuSearch.yaml
  label: Tabu search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearch.yaml
    role: maintained
scope:
  description: Source-version provenance wording only.
  selection: Exact TabuSearch evidence-source version field.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TabuSearch
  exclusions:
  - target: Mechanism and full cohort approval
    reason: This partial observation isolates a provenance wording defect; scientific
      assessment follows correction and required checks.
checks:
- check_id: source-pin
  name: Verify pinned AIO source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:TabuSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
evidence:
- evidence_id: pdf-dates
  kind: primary_source
  reference: https://leeds-faculty.colorado.edu/glover/TS%20-%20Part%20I-ORSA-aw.pdf
  locator: PDF p.1 journal header and PDF p.3 copyright footer, visually inspected
  accessed_at: '2026-10-11T14:07:24Z'
  snapshot_sha256: fb1102afc415eb0d9d7e2a8ced4ec7047d1fea2f47c74c16e7cd8be290ea5a1a
  support: supports
  summary: The article header identifies volume 1 number 3, Summer 1989; the scan
    footer says Copyright 2001. Those observations do not date insertion of the footer.
- evidence_id: draft
  kind: record_content
  reference: data/curated/TabuSearch.yaml
  locator: evidence_sources[0].version
  accessed_at: '2026-10-11T14:16:11Z'
  support: context_only
  summary: The draft describes a footer added in 2001, going beyond the date visibly
    printed in it.
assessments:
- assessment_id: date-scope
  area: provenance
  topic: Observed notice versus inferred insertion date
  outcome: concern
  target_ids:
  - AIMech:TabuSearch
  evidence_ids:
  - pdf-dates
  - draft
  summary: Preserve the publication/scan distinction while removing the unsupported
    insertion-date inference.
findings:
- finding_id: tabu-scan-provenance
  issue_key: CultureBotAI-AIMech-TabuSearch-scan-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:TabuSearch
  field_paths:
  - evidence_sources[0].version
  evidence_ids:
  - pdf-dates
  - draft
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearch.yaml
    role: maintained
  title: The footer’s date is treated as its insertion date.
  description: Replace added in 2001 with a description that the scan contains a 2001
    copyright footer. Retain the verified 1989 article date and exact source checksum.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/87
actions:
- action_id: qualify-scan-date
  finding_ids:
  - tabu-scan-provenance
  target_ids:
  - AIMech:TabuSearch
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearch.yaml
    role: maintained
  description: Correct the source version, synchronize ledger/history, and save a
    linked successor after checks.
  acceptance_checks:
  - The version describes the visible 2001 notice without inferring insertion time.
  - The 1989 article date and inspected source checksum remain accurate.
  - Ledger/history and successor disposition preserve the correction; required checks
    pass.
boundary_decisions: []
limitations:
- Provenance-only partial author self-review; scientific_review is false.
- The full gate is still running and is not reported as passed.
links:
- https://github.com/CultureBotAI/AIMech/issues/87
```
