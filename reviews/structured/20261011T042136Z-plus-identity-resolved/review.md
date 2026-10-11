# Curated identity plus-sign resolution

- Review: 20261011T042136Z-plus-identity-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:21:35Z
- Finished UTC: 2026-10-11T04:21:36Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The reproduced identity defect is resolved with semantic plus preservation, retained duplicate checks and dedicated regression coverage.

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
| python -m aimech check-source | passed | True | AIMech:curated-identity-validator | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:curated-identity-validator | Checked 442 record(s); 0 failed. |
| python -m aimech validate-curated | passed | True | AIMech:curated-identity-validator | Checked 82 curated concept record(s); 0 error(s). |
| python -m aimech seed --check | passed | True | AIMech:curated-identity-validator | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-history --base HEAD | passed | True | AIMech:curated-identity-validator | Checked 14 history record(s); 0 error(s). |
| python scripts/record_review.py check | passed | True | AIMech:curated-identity-validator | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 12,<br>  "coverage": "declared_scopes_only"<br>} |
| PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check | passed | True | AIMech:curated-identity-validator | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 40.06s<br>Checked 442 record(s); 0 failed.<br>Checked 82 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 14 history record(s); 0 error(s).<br>topClass is deprecated - use top_class<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 12,<br>  "coverage": "declared_scopes_only"<br>}<br> |
| PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check | passed | True | AIMech:curated-identity-validator | bash scripts/check_vendored_sync.sh<br>OK: 22 governed artifacts match the pinned claw revision<br> |
| python -m pytest tests/test_curated.py -q | passed | True | AIMech:curated-identity-validator | ...................................                                      [100%]<br>35 passed in 4.01s<br> |
| Python post-fix check of three base/++ pairs and a spelling-equivalent ++ alias | passed | True | AIMech:curated-identity-validator | All three base/++ pairs have distinct keys; the case/spacing variant still has the same ++ identity key. |

## Scientific And Domain Assessments

### Canonical identity comparison

identity: supported. Targets: AIMech:curated-identity-validator.

Plus suffix distinctions survive comparison and existing duplicate protections remain enforced.

A normalizer is a conservative collision check, not proof of semantic equivalence; manual alias and mechanism assessment remains required.

## Findings

### plus-identity: Preserve meaningful plus signs in concept identity keys

major / resolved / confirmed; issue key: aimech-curated-identity-plus-suffix.

Removing plus signs conflates distinct named variants with their base architectures and incorrectly rejects their coexistence. The defect is demonstrated for Deep Sets/Deep Sets++, PointNet/PointNet++ and Set Transformer/Set Transformer++. No currently published record is claimed to denote the wrong concept.

Disposition: Inspected the maintained normalizer and callers, validated distinct base/++ records together, checked duplicate spelling/alias and AIO protections, rejected symbol-only identities and passed complete required checks. The only same-key predecessor is explicitly superseded with its full target retained.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| normalization | src/aimech/curated.py; normalized_name and callers in validate_curated_record/validate_curated | supports | The normalizer now retains plus signs in identity keys, while the record-level nonempty-identity check independently requires an ASCII letter or digit. All existing collision callers still share the same normalizer. |
| reproduction | Python reproduction using aimech.curated.normalized_name on three base/++ name pairs | supports | All three distinct base/variant names collapse to the same identity key. Reproduction succeeded; this is evidence of the defect, not desired behavior. Pairs: Deep Sets/Deep Sets++; PointNet/PointNet++; Set Transformer/Set Transformer++. |
| scope | https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf; Section 4.3–4.4, PDF p. 6 | context_only | The source defines plus-plus architectures with changed residual and normalization constructions. Plus suffixes distinguish named variants rather than incidental typography. This review concerns the identity validator, not scientific approval of future records. |
| regressions | tests/test_curated.py | supports | Regression coverage exercises base/plus/plusplus coexistence, continued normalized spelling/alias collisions, matching AIO identities and rejection of symbol-only names. |

## Limits And Additional Notes

- Software self-review, not independent approval or a scientific assessment of the entire curated collection.
- The change is scoped to meaningful plus signs; other mathematical or Unicode notation may need separately evidenced handling.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T042136Z-plus-identity-resolved
kind: record
repository: CultureBotAI/AIMech
title: Curated identity plus-sign resolution
started_at: '2026-10-11T04:21:35Z'
finished_at: '2026-10-11T04:21:36Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent implemented the native validator and reassessed
    it during further concept discovery.
skill: /Users/marcin/.codex/skills/aimech-resolve-reviews/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The reproduced identity defect is resolved with semantic plus preservation,
  retained duplicate checks and dedicated regression coverage.
source:
  git_revision: 03016c6a386cff3b9aefd6fc21e80d9d27e63896
  state: working_tree
  inputs:
  - path: docs/curated-concepts.md
    sha256: 0b6f6aa0ffa770e8521b51b90e227ace92be8a8fff49f1e066d836cc11c11c2e
    role: context
  - path: reviews/structured/20261011T041710Z-plus-identity-open/review.yaml
    sha256: 88303e2bde360206f558ca2c45fde4a4a41c97f831441d34ce8f4c7a0f917703
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: target
  - path: src/aimech/schema/curated_concept.yaml
    sha256: dfcbacdcdeb7429bfa947d7c1c8431e5d0b886f593daaa359588273ba2a2c6e0
    role: context
  - path: tests/test_curated.py
    sha256: 6ea5759c0ff4f486de52710df689b9c66272e69908a8c8923f1fc822e920b3e6
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
  name: python -m aimech check-source
  command: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
- check_id: check-1
  name: python -m aimech validate
  command: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
- check_id: check-2
  name: python -m aimech validate-curated
  command: python -m aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 82 curated concept record(s); 0 error(s).
- check_id: check-3
  name: python -m aimech seed --check
  command: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
- check_id: check-4
  name: python -m aimech validate-history --base HEAD
  command: python -m aimech validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 14 history record(s); 0 error(s).
- check_id: check-5
  name: python scripts/record_review.py check
  command: python scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 12,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}"
- check_id: check-6
  name: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: "uv run --locked --extra dev python scripts/check.py\nAll checks passed!\n\
    ........................................................................ [ 31%]\n\
    ........................................................................ [ 63%]\n\
    ........................................................................ [ 94%]\n\
    .........sss                                                             [100%]\n\
    225 passed, 3 skipped in 40.06s\nChecked 442 record(s); 0 failed.\nChecked 82\
    \ curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing, 0 changed,\
    \ 0 unexpected.\nChecked 14 history record(s); 0 error(s).\ntopClass is deprecated\
    \ - use top_class\n{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\"\
    : 12,\n  \"coverage\": \"declared_scopes_only\"\n}\n"
- check_id: check-7
  name: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: 'bash scripts/check_vendored_sync.sh

    OK: 22 governed artifacts match the pinned claw revision

    '
- check_id: check-8
  name: python -m pytest tests/test_curated.py -q
  command: python -m pytest tests/test_curated.py -q
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: '...................................                                      [100%]

    35 passed in 4.01s

    '
- check_id: check-9
  name: Python post-fix check of three base/++ pairs and a spelling-equivalent ++
    alias
  command: Python post-fix check of three base/++ pairs and a spelling-equivalent
    ++ alias
  status: passed
  required: true
  target_ids:
  - AIMech:curated-identity-validator
  exit_code: 0
  expected_exit_code: 0
  summary: All three base/++ pairs have distinct keys; the case/spacing variant still
    has the same ++ identity key.
evidence:
- evidence_id: normalization
  kind: record_content
  reference: src/aimech/curated.py
  locator: normalized_name and callers in validate_curated_record/validate_curated
  accessed_at: '2026-10-11T04:21:35Z'
  support: supports
  summary: The normalizer now retains plus signs in identity keys, while the record-level
    nonempty-identity check independently requires an ASCII letter or digit. All existing
    collision callers still share the same normalizer.
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
- evidence_id: regressions
  kind: record_content
  reference: tests/test_curated.py
  accessed_at: '2026-10-11T04:21:35Z'
  support: supports
  summary: Regression coverage exercises base/plus/plusplus coexistence, continued
    normalized spelling/alias collisions, matching AIO identities and rejection of
    symbol-only names.
assessments:
- assessment_id: identity-behavior
  area: identity
  topic: Canonical identity comparison
  outcome: supported
  target_ids:
  - AIMech:curated-identity-validator
  evidence_ids:
  - normalization
  - reproduction
  - scope
  - regressions
  summary: Plus suffix distinctions survive comparison and existing duplicate protections
    remain enforced.
  details: A normalizer is a conservative collision check, not proof of semantic equivalence;
    manual alias and mechanism assessment remains required.
findings:
- finding_id: plus-identity
  issue_key: aimech-curated-identity-plus-suffix
  category: identity
  severity: major
  status: resolved
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
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261011T041710Z-plus-identity-open
    finding_id: plus-identity
  disposition_reason: Inspected the maintained normalizer and callers, validated distinct
    base/++ records together, checked duplicate spelling/alias and AIO protections,
    rejected symbol-only identities and passed complete required checks. The only
    same-key predecessor is explicitly superseded with its full target retained.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/13
actions: []
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
