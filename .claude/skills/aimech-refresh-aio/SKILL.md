---
name: aimech-refresh-aio
description: Assess and carry out an explicitly scoped AIMech AIO snapshot update with whole-corpus change accounting, structured review, and reproduction checks. Use for pinned ontology upgrades, not automatic pulls or a single missing pinned record.
---

# Refresh AIMech's AIO Source

Use inside AIMech. Resolve paths from the repository root and read `AGENTS.md`,
`CLAUDE.md`, `docs/sources.md`, and the shared native procedure at
`.claude/skills/aimech-add-record/references/source-updates.md`. That procedure
owns the migration details; this skill makes the update workflow discoverable.
Read the current importer, source manifest and schema as well: there is no
generic force/overwrite/prune command to assume exists.

## Bound the update

Establish whether the user asked for a candidate assessment or an applied source
refresh. An update scan is read-only with respect to authoritative inputs. An
explicit refresh may proceed within its approved scope; request a decision only
when the actual migration introduces materially additional scope, such as removed
identities or a new representation requiring schema changes.

Verify a specific candidate upstream Git revision, release JSON, version IRI and
license from the official AIO repository. Resolve requests for "latest" from the
current upstream state. Do not use BioPortal counts, local reference OWL files or
publication prose to replace the pinned JSON authority. If the input is already
byte-identical and its provenance unchanged, report a no-op rather than rewriting
retrieval timestamps or generating artificial history.

## Plan before replacing records

Work in an isolated worktree and apply the referenced source-update procedure.
Compare old/candidate graphs by exact IRI and distinguish semantic changes from
source-provenance changes. Count named AIO `CLASS` nodes, not external classes.
Preserve all identity removals, changed assertions and unsupported constructs in
the assessment instead of silently dropping them to pass validation.

Projection success covers only the constructs the importer consumes. Compare
the full old/candidate graph for new logical constructs and annotations as well,
including `equivalentNodesSets` and logical definition axioms. Record intentional
non-projected metadata separately. An unrepresented assertion that changes
identity or meaning needs an explicit compatibility/representation decision;
`check-source` and `build_records` alone do not establish semantic compatibility.

Use `aimech.importer.build_records(candidate_root)` to compute proposed bytes in
separate staging. A source change can affect every record's provenance even when
only one class changes. `seed --write` creates all missing records and refuses
changed/unexpected files; it is not a source migration tool. Never delete the
corpus to bypass that refusal or invent a `--force`, `--prune`, or per-ID flag.

Save a timestamped proposal under the user's destination or
`research/source-updates/<YYYYMMDDTHHMMSSZ>-<slug>/`, including a human-readable
assessment and machine-readable migration manifest. Account for old/new source
revisions and hashes, added/changed/removed paths, proposed output hashes,
identity decisions, importer/schema compatibility, validation results, scope
approval and rollback inputs. Protect edited inputs and require expected old
hashes before any authorized replacement; reassess drift rather than overwriting.

For an applied update, use a reviewed migration implementing those protections.
The current native CLI has no overwrite migration command. If one is needed,
implement and test it within the user's authorized scope or leave an actionable
proposal; do not claim the planned migration ran.

## Verify and report

Persist source-update findings through the native record/category review skills
and `docs/record-reviews.md`, including YAML and helper-rendered Markdown for
resolved targets. Reinspect after candidate inputs change; a source diff is not
itself a scientific review. Keep upstream ontology and local importer ownership
distinct, and retain `NOT_REVIEWED` on generated concepts.

Keep projection staging separate from review persistence. Inspect and save
candidate reviews from a real, identity-validated AIMech Git worktree with the
actual assessed inputs available there. A plain temporary directory is not a
valid review root. The helper saves to that root's fixed `reviews/structured/`
directory; it has no `save --output-dir` option. Link the saved pair from the
proposal instead of inventing an external review-output flag or substituting
hashes from a different candidate tree.

After an authorized application, run `aimech check-source`, native validation,
`aimech seed --check`, history validation against the reviewed base, and the
`CLAUDE.md` quality gates. Append actual session history for the source update
using `uv run --locked aimech new-history`; do not manufacture one scientific
curation event per imported term. Report exact old/new revisions, corpus impact,
saved proposal/review/history paths, executed checks and any unresolved work.

Publication, upstream issue submission, paid research and changes to shared CLAW
artifacts are not implied by this skill. Follow the user's separate instructions
for those actions without repeating approvals already given for the current task.
