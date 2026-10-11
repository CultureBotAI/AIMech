# Adversarial review of historical Git-base availability

- Review: 20261011T055247Z-review-base-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T05:52:47Z
- Finished UTC: 2026-10-11T05:52:47Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

A fresh checkout cannot resolve a review base from a squash-merged and deleted feature branch. The local author checkout masked the missing-object defect. Historical review bytes and the governed validator must remain unchanged.

## Scope And Provenance

Availability of Git commits cited by immutable review provenance in fresh checkouts.

Selection: The AIMech CI setup that fetches full branch history and the trusted event base.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 06105fec7731186356a89180d7a02d731c74672b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ReviewBasePreparation | .github/workflows/validate-strict.yaml | maintained | Historical review Git-base preparation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh PR CI gate | failed | True | AIMech:ReviewBasePreparation | CI: 1 failed, 224 passed, 3 skipped. test_every_saved_structured_bundle_is_valid could not resolve c8244be1161c5c7301533ae7951c8c869652e8f8 in the prior successor review. |
| Independent fresh-clone object check | failed | True | AIMech:ReviewBasePreparation | After a public single-branch no-tags clone of PR #25, the object is absent. The operation did not reuse the author checkout’s Git object database. |

## Scientific And Domain Assessments

### Fresh-clone verification of retained review sources

provenance: concern. Targets: AIMech:ReviewBasePreparation.

The cited commit is still retrievable from PR history but is not fetched by normal branch checkout. No evidence supports editing immutable reviews or weakening provenance checks.

## Findings

### missing-base: Retrieve historical review bases before offline validation

major / open / confirmed; issue key: aimech-historical-review-base-fetch.

Explicitly retrieve and retain missing full commit IDs referenced by saved review source blocks. Validate all requested revisions before any network operation, fetch only from origin and preserve existing provenance checks.

## Recommended Actions And Acceptance Checks

### fetch-bases

Add local setup tooling and a CI preparation step, with regression coverage and fresh-clone verification.

- The missing pre-squash commit is absent before setup and present afterwards in a fresh clone.
- Malformed and unavailable revision inputs fail without weakening the gate.
- The strict offline gate and pinned-artifact check pass; existing review bundles remain byte-identical.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ci-failure | https://github.com/CultureBotAI/AIMech/actions/runs/38115980264/job/114400841644 | supports | The remote log identifies the missing pre-squash commit and exact historical review path. |
| setup | .github/workflows/validate-strict.yaml; checkout fetch-depth and Fetch and verify the trusted review base step | supports | Full-depth branch fetch and the event-base fetch do not enumerate commits named by existing saved review sources. |

## Limits And Additional Notes

- This is an infrastructure/provenance review, not a reassessment of the six concept records.
- Local validation passed because its object database retained branch history; fresh CI and clone results are the relevant negative evidence.
- This historical observation assesses the committed pre-fix workflow at 06105fec7731186356a89180d7a02d731c74672b, not the later working-tree fix. The committed workflow was re-read with git show.
- Two unsaved formatting attempts failed validation (YAML anchors, then a singular external_issue field). The canonical contract was followed after correcting the temporary generator; no saved review was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T055247Z-review-base-open
kind: repository
repository: CultureBotAI/AIMech
title: Adversarial review of historical Git-base availability
started_at: '2026-10-11T05:52:47Z'
finished_at: '2026-10-11T05:52:47Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent diagnosed its own publication workflow after
    fresh CI exposed a provenance failure.
skill: docs/record-reviews.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: A fresh checkout cannot resolve a review base from a squash-merged and deleted
  feature branch. The local author checkout masked the missing-object defect. Historical
  review bytes and the governed validator must remain unchanged.
source:
  git_revision: 06105fec7731186356a89180d7a02d731c74672b
  state: git_commit
  inputs:
  - path: .github/workflows/validate-strict.yaml
    sha256: 5f755428a1972aa056542ce4e0869077b777240aa7470a561279f8243c804cbb
    role: target
  - path: docs/record-review-profile.md
    sha256: ee64509af21eb4d2ca7e6a997300f2e4420f4651eeb4977f04d68a9e8207125a
    role: context
  - path: reviews/structured/20261011T053851Z-foundational-search-resolved/review.yaml
    sha256: 98c248685e45d6ed63c98abb55d2308d8d5c16d828121358cec0cb6b1abca45b
    role: context
targets:
- target_id: AIMech:ReviewBasePreparation
  path: .github/workflows/validate-strict.yaml
  label: Historical review Git-base preparation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: .github/workflows/validate-strict.yaml
    role: ci_setup
scope:
  description: Availability of Git commits cited by immutable review provenance in
    fresh checkouts.
  selection: The AIMech CI setup that fetches full branch history and the trusted
    event base.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ReviewBasePreparation
checks:
- check_id: ci-gate
  name: Fresh PR CI gate
  command: just check
  status: failed
  required: true
  target_ids:
  - AIMech:ReviewBasePreparation
  exit_code: 1
  expected_exit_code: 0
  summary: 'CI: 1 failed, 224 passed, 3 skipped. test_every_saved_structured_bundle_is_valid
    could not resolve c8244be1161c5c7301533ae7951c8c869652e8f8 in the prior successor
    review.'
- check_id: fresh-object
  name: Independent fresh-clone object check
  command: git cat-file -e c8244be1161c5c7301533ae7951c8c869652e8f8^{commit}
  status: failed
  required: true
  target_ids:
  - AIMech:ReviewBasePreparation
  exit_code: 128
  expected_exit_code: 0
  summary: 'After a public single-branch no-tags clone of PR #25, the object is absent.
    The operation did not reuse the author checkout’s Git object database.'
evidence:
- evidence_id: ci-failure
  kind: validation
  reference: https://github.com/CultureBotAI/AIMech/actions/runs/38115980264/job/114400841644
  accessed_at: '2026-10-11T05:52:47Z'
  support: supports
  summary: The remote log identifies the missing pre-squash commit and exact historical
    review path.
- evidence_id: setup
  kind: record_content
  reference: .github/workflows/validate-strict.yaml
  locator: checkout fetch-depth and Fetch and verify the trusted review base step
  accessed_at: '2026-10-11T05:52:47Z'
  support: supports
  summary: Full-depth branch fetch and the event-base fetch do not enumerate commits
    named by existing saved review sources.
assessments:
- assessment_id: availability
  area: provenance
  topic: Fresh-clone verification of retained review sources
  outcome: concern
  target_ids:
  - AIMech:ReviewBasePreparation
  evidence_ids:
  - ci-failure
  - setup
  summary: The cited commit is still retrievable from PR history but is not fetched
    by normal branch checkout. No evidence supports editing immutable reviews or weakening
    provenance checks.
findings:
- finding_id: missing-base
  issue_key: aimech-historical-review-base-fetch
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:ReviewBasePreparation
  field_paths:
  - jobs.validate-strict.steps
  evidence_ids:
  - ci-failure
  - setup
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: .github/workflows/validate-strict.yaml
    role: ci_setup
  title: Retrieve historical review bases before offline validation
  description: Explicitly retrieve and retain missing full commit IDs referenced by
    saved review source blocks. Validate all requested revisions before any network
    operation, fetch only from origin and preserve existing provenance checks.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/26
actions:
- action_id: fetch-bases
  finding_ids:
  - missing-base
  target_ids:
  - AIMech:ReviewBasePreparation
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: .github/workflows/validate-strict.yaml
    role: ci_setup
  description: Add local setup tooling and a CI preparation step, with regression
    coverage and fresh-clone verification.
  acceptance_checks:
  - The missing pre-squash commit is absent before setup and present afterwards in
    a fresh clone.
  - Malformed and unavailable revision inputs fail without weakening the gate.
  - The strict offline gate and pinned-artifact check pass; existing review bundles
    remain byte-identical.
limitations:
- This is an infrastructure/provenance review, not a reassessment of the six concept
  records.
- Local validation passed because its object database retained branch history; fresh
  CI and clone results are the relevant negative evidence.
tags:
- ci
- provenance
- self-review
- needs-curation
notes:
- This historical observation assesses the committed pre-fix workflow at 06105fec7731186356a89180d7a02d731c74672b,
  not the later working-tree fix. The committed workflow was re-read with git show.
- Two unsaved formatting attempts failed validation (YAML anchors, then a singular
  external_issue field). The canonical contract was followed after correcting the
  temporary generator; no saved review was overwritten.
```
