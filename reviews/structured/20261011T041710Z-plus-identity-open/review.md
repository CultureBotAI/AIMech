# Curated identity plus-sign finding

- Review: 20261011T041710Z-plus-identity-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:17:10Z
- Finished UTC: 2026-10-11T04:17:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

A reproduced identity-key defect prevents distinct plus-suffixed architecture names from coexisting; existing passing schema tests do not detect this case.

## Scope And Provenance

Maintained concept-name normalization and its record/collection callers.

Selection: Exactly the maintained curated identity validator; all name-normalization callers inspected.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 03016c6a386cff3b9aefd6fc21e80d9d27e63896.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:curated-identity-validator | src/aimech/curated.py | maintained | Curated identity validator |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m pytest tests/test_curated.py -q | passed | True | AIMech:curated-identity-validator | ..............................                                           [100%]<br>30 passed in 4.15s |
| Python reproduction using aimech.curated.normalized_name on three base/++ name pairs | passed | True | AIMech:curated-identity-validator | All three distinct base/variant names collapse to the same identity key. Reproduction succeeded; this is evidence of the defect, not desired behavior. |

## Scientific And Domain Assessments

### Canonical identity comparison

identity: concern. Targets: AIMech:curated-identity-validator.

The comparison erases a distinction supported by named architecture definitions.

A normalizer is a conservative collision check, not proof of semantic equivalence; manual alias and mechanism assessment remains required.

## Findings

### plus-identity: Preserve meaningful plus signs in concept identity keys

major / open / confirmed; issue key: aimech-curated-identity-plus-suffix.

Removing plus signs conflates distinct named variants with their base architectures and incorrectly rejects their coexistence. The defect is demonstrated for Deep Sets/Deep Sets++, PointNet/PointNet++ and Set Transformer/Set Transformer++. No currently published record is claimed to denote the wrong concept.

## Recommended Actions And Acceptance Checks

### preserve-plus

Preserve semantic plus signs in identity comparison without weakening duplicate spelling, alias or AIO collision checks; keep names containing no letters/digits invalid.

- Validate distinct base, plus and plus-plus records in one collection.
- Equivalent spacing/case and aliases still collide, including AIO exact identities.
- Symbol-only names remain invalid.
- Run focused regression tests, complete just check and just vendored-check.
- Document normalization behavior and save an evidence-backed successor with this issue key and exact predecessor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| normalization | src/aimech/curated.py; normalized_name and callers in validate_curated_record/validate_curated | supports | The normalizer removes every non-ASCII-alphanumeric character, including meaningful plus signs; the resulting keys are used for within-record and cross-record identity collision checks. |
| reproduction | Python reproduction using aimech.curated.normalized_name on three base/++ name pairs | supports | All three distinct base/variant names collapse to the same identity key. Reproduction succeeded; this is evidence of the defect, not desired behavior. Pairs: Deep Sets/Deep Sets++; PointNet/PointNet++; Set Transformer/Set Transformer++. |
| scope | https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf; Section 4.3–4.4, PDF p. 6 | context_only | The source defines plus-plus architectures with changed residual and normalization constructions. Plus suffixes distinguish named variants rather than incidental typography. This review concerns the identity validator, not scientific approval of future records. |

## Limits And Additional Notes

- Software self-review, not independent approval or a scientific assessment of the entire curated collection.
- The change is scoped to meaningful plus signs; other mathematical or Unicode notation may need separately evidenced handling.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T041710Z-plus-identity-open
kind: record
repository: CultureBotAI/AIMech
title: Curated identity plus-sign finding
started_at: '2026-10-11T04:17:10Z'
finished_at: '2026-10-11T04:17:10Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent implemented the native validator and reassessed
    it during further concept discovery.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: A reproduced identity-key defect prevents distinct plus-suffixed architecture
  names from coexisting; existing passing schema tests do not detect this case.
source:
  git_revision: 03016c6a386cff3b9aefd6fc21e80d9d27e63896
  state: working_tree
  inputs:
  - path: docs/curated-concepts.md
    sha256: 68d52b76cd68cbf33c080d8ae836e21ca04282e0e20ce11ed85d66bc0910837d
    role: context
  - path: src/aimech/curated.py
    sha256: b9a87f14341119f89fffac2cfb29fab222d0fcc9ac999990650e349e06d9cfc3
    role: target
  - path: src/aimech/schema/curated_concept.yaml
    sha256: dfcbacdcdeb7429bfa947d7c1c8431e5d0b886f593daaa359588273ba2a2c6e0
    role: context
  - path: tests/test_curated.py
    sha256: 8dd0902901be8a7c1da61fb80c5ffd8c9e131293d0d805ff35d4c26b04a4a664
    role: context
targets:
- target_id: AIMech:curated-identity-validator
  path: src/aimech/curated.py
  label: Curated identity validator
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/curated.py
    role: maintained identity comparison and validation
scope:
  description: Maintained concept-name normalization and its record/collection callers.
  selection: Exactly the maintained curated identity validator; all name-normalization
    callers inspected.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:curated-identity-validator
  exclusions:
  - target: Scientific review of architecture records and general Unicode normalization
    reason: This is a bounded software review of meaningful ASCII plus suffixes, not
      a new universal identity or status-promotion policy.
checks:
- check_id: check-0
  name: python -m pytest tests/test_curated.py -q
  command: python -m pytest tests/test_curated.py -q
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: '..............................                                           [100%]

    30 passed in 4.15s'
- check_id: check-1
  name: Python reproduction using aimech.curated.normalized_name on three base/++
    name pairs
  command: Python reproduction using aimech.curated.normalized_name on three base/++
    name pairs
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: All three distinct base/variant names collapse to the same identity key.
    Reproduction succeeded; this is evidence of the defect, not desired behavior.
evidence:
- evidence_id: normalization
  kind: record_content
  reference: src/aimech/curated.py
  locator: normalized_name and callers in validate_curated_record/validate_curated
  accessed_at: '2026-10-11T04:17:10Z'
  support: supports
  summary: The normalizer removes every non-ASCII-alphanumeric character, including
    meaningful plus signs; the resulting keys are used for within-record and cross-record
    identity collision checks.
- evidence_id: reproduction
  kind: validation
  reference: Python reproduction using aimech.curated.normalized_name on three base/++
    name pairs
  accessed_at: '2026-10-11T04:15:39Z'
  support: supports
  summary: 'All three distinct base/variant names collapse to the same identity key.
    Reproduction succeeded; this is evidence of the defect, not desired behavior.
    Pairs: Deep Sets/Deep Sets++; PointNet/PointNet++; Set Transformer/Set Transformer++.'
- evidence_id: scope
  kind: primary_source
  reference: https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf
  locator: Section 4.3–4.4, PDF p. 6
  accessed_at: '2026-10-11T04:14:52Z'
  snapshot_sha256: 9b302c6977e34aaba6dce3d6e4c173850c5a8e3ad7f381fa7c578d7c67d3a28d
  support: context_only
  summary: The source defines plus-plus architectures with changed residual and normalization
    constructions. Plus suffixes distinguish named variants rather than incidental
    typography. This review concerns the identity validator, not scientific approval
    of future records.
assessments:
- assessment_id: identity-behavior
  area: identity
  topic: Canonical identity comparison
  outcome: concern
  target_ids:
  - AIMech:curated-identity-validator
  evidence_ids:
  - normalization
  - reproduction
  - scope
  summary: The comparison erases a distinction supported by named architecture definitions.
  details: A normalizer is a conservative collision check, not proof of semantic equivalence;
    manual alias and mechanism assessment remains required.
findings:
- finding_id: plus-identity
  issue_key: aimech-curated-identity-plus-suffix
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Preserve meaningful plus signs in concept identity keys
  description: Removing plus signs conflates distinct named variants with their base
    architectures and incorrectly rejects their coexistence. The defect is demonstrated
    for Deep Sets/Deep Sets++, PointNet/PointNet++ and Set Transformer/Set Transformer++.
    No currently published record is claimed to denote the wrong concept.
  target_ids:
  - AIMech:curated-identity-validator
  field_paths:
  - normalized_name
  evidence_ids:
  - normalization
  - reproduction
  - scope
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/curated.py
    role: maintained identity comparison and validation
  normalization_reason: 'Major representation defect: valid distinct concepts cannot
    coexist under their canonical names. Existing duplicate protections should be
    retained rather than bypassed.'
actions:
- action_id: preserve-plus
  description: Preserve semantic plus signs in identity comparison without weakening
    duplicate spelling, alias or AIO collision checks; keep names containing no letters/digits
    invalid.
  finding_ids:
  - plus-identity
  target_ids:
  - AIMech:curated-identity-validator
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/curated.py
    role: maintained identity comparison and validation
  acceptance_checks:
  - Validate distinct base, plus and plus-plus records in one collection.
  - Equivalent spacing/case and aliases still collide, including AIO exact identities.
  - Symbol-only names remain invalid.
  - Run focused regression tests, complete just check and just vendored-check.
  - Document normalization behavior and save an evidence-backed successor with this
    issue key and exact predecessor.
limitations:
- Software self-review, not independent approval or a scientific assessment of the
  entire curated collection.
- The change is scoped to meaningful plus signs; other mathematical or Unicode notation
  may need separately evidenced handling.
tags:
- identity-validation
- self-review
- plus-suffix
```
