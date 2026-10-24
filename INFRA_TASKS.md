# AIMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `aimech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/AIMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
- task_id: aimech-infra-0001
  summary: Enforce ConceptKind schema-to-renderer coverage in scripts/render_pages.py and tests/test_render_pages.py
  status: resolved
  issue_url: https://github.com/CultureBotAI/AIMech/issues/429
  disposition: Added task, bias, and risk entries to KIND_LABELS and KIND_BLURBS in scripts/render_pages.py and added test_kind_and_branch_labels_cover_schema_enums() in tests/test_render_pages.py while retaining assert len(unique_kinds) >= 9 (PR #428).
- task_id: aimech-infra-0002
  summary: Update upstream CLAW mechs.aimech fleet profile record_globs and schema_paths to include data/curated/*.yaml and src/aimech/schema/curated_concept.yaml and regenerate skill adapters
  status: open
  issue_url: https://github.com/CultureBotAI/AIMech/issues/431
  disposition: Preserved data/aio/*.yaml, data/curated/*.yaml locally in .claude/skills/review-open-issues/SKILL.md in PR #428; upstream CLAW src/kg_microbe_fleet/fleet.yaml update and adapter regeneration tracked in Issue #431.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `aimech-infra-0001` — Enforce `ConceptKind` schema-to-renderer coverage in `scripts/render_pages.py` and `tests/test_render_pages.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/AIMech/issues/429
- **Status**: `resolved`
- **Priority**: Medium
- **Dependencies**: None
- **Observation**: Curating the first `concept_kind: bias` record (`AIMech:DataPersistenceBias`, Round 826, commit `80dc760a`) exposed that `KIND_LABELS` and `KIND_BLURBS` in `scripts/render_pages.py` omitted 3 of the 12 `ConceptKind` permissible values (`task`, `bias`, `risk`) defined in `src/aimech/schema/curated_concept.yaml`, and `tests/test_render_pages.py` hardcoded `assert len(unique_kinds) == 9` without testing full schema enum coverage.
- **Evidence paths**: `scripts/render_pages.py`, `tests/test_render_pages.py`, `src/aimech/schema/curated_concept.yaml`, `data/curated/DataPersistenceBias.yaml`
- **Disposition**: Resolved in PR #428 by registering `task`, `bias`, and `risk` (along with the `origin/main` `coordination_mechanism` and `computational_paradigm` values) in `KIND_LABELS` and `KIND_BLURBS`, updating `test_curated_kind_pages()` to retain `assert len(unique_kinds) >= 9` alongside schema-derived and generated-page-set assertions, and adding `test_kind_and_branch_labels_cover_schema_enums()` in `tests/test_render_pages.py`.

### `aimech-infra-0002` — Update upstream CLAW `mechs.aimech` fleet profile (`record_globs` and `schema_paths`) and regenerate skill adapters

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/AIMech/issues/431
- **Status**: `open`
- **Priority**: Medium
- **Dependencies**: Upstream change in `CultureBotAI/culturebotai-claw` (`src/kg_microbe_fleet/fleet.yaml`)
- **Observation**: At pinned CLAW revision `a5d562962c75a2ad9efd8160b548df5944315422`, `src/kg_microbe_fleet/fleet.yaml` defines `mechs.aimech.record_globs: ["data/aio/*.yaml"]` and `mechs.aimech.schema_paths: ["src/aimech/schema/aimech.yaml"]`, omitting AIMech's maintained curated concept corpus (`data/curated/*.yaml`) and its native LinkML schema (`src/aimech/schema/curated_concept.yaml`). Canonical skill templates such as `src/kg_microbe_skills/canonical/review-open-issues.md` and `aimech-evolve-workflow` interpolate `record_globs` and `schema_paths` into `.claude/skills/*/SKILL.md` adapters, so adapter regeneration from the current upstream profile drops `data/curated/*.yaml` and `src/aimech/schema/curated_concept.yaml`.
- **Curated schema coverage assessment**: AIMech validates two distinct schemas and corpora: generated AIO records (`data/aio/*.yaml` against `src/aimech/schema/aimech.yaml`) and maintained curated concept records (`data/curated/*.yaml` against `src/aimech/schema/curated_concept.yaml`). Both `record_globs` (`data/aio/*.yaml`, `data/curated/*.yaml`) and both `schema_paths` (`src/aimech/schema/aimech.yaml`, `src/aimech/schema/curated_concept.yaml`) should be declared in `mechs.aimech` in `src/kg_microbe_fleet/fleet.yaml` so generated skill adapters accurately reflect AIMech's full schema and record scope.
- **Desired outcome**: Update `mechs.aimech.record_globs` and `mechs.aimech.schema_paths` in upstream `CultureBotAI/culturebotai-claw` (`src/kg_microbe_fleet/fleet.yaml`) to include `data/curated/*.yaml` and `src/aimech/schema/curated_concept.yaml`, and regenerate affected `.claude/skills/` adapters (`review-open-issues/SKILL.md`, `aimech-evolve-workflow/SKILL.md`) so curated scope is preserved across future adapter regenerations.
- **Evidence paths**: `.claude/skills/review-open-issues/SKILL.md`, `.claude/skills/aimech-evolve-workflow/SKILL.md`, `src/aimech/schema/curated_concept.yaml`, `src/aimech/schema/aimech.yaml`, `scripts/.vendored_canon_ref`
- **Disposition**: Open; `.claude/skills/review-open-issues/SKILL.md` (which is not in `vendored_artifacts.json`'s checksum manifest) has been restored in PR #428 to preserve `data/aio/*.yaml`, `data/curated/*.yaml` in both its Scope section and its ontology-grounding prioritization example while Issue #431 tracks the upstream `fleet.yaml` profile fix and adapter regeneration.


