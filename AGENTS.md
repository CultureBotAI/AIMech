# AIMech Working Agreements

Read `README.md` for scope and `docs/sources.md` for evidence ownership.

- AIO is authoritative for imported vocabulary, not similarly named BioPortal
  AI/AION resources. Preserve its identifiers and license. Maintained concepts
  absent from AIO use local `AIMech:` IDs under `data/curated/`, inspected evidence
  and explicit AIO mapping assessments; follow `docs/curated-concepts.md`.
- `data/aio/` is generated. Fix the importer or propose an upstream ontology
  correction, then regenerate through a reviewed source-update process. Never
  promote imported terminology into scientific evidence or model evaluation.
- Run `just check` before publication. Local and CI gates must stay equivalent.
- Also run `just vendored-check` before publication; it verifies the immutable
  public CLAW revision and is required in CI, including merge groups.
- Review a record with `.claude/skills/review-yaml-record/SKILL.md`, and a cohort
  with `.claude/skills/review-category/SKILL.md`. Save structured timestamped
  outputs even for clean or blocked reviews once a target is identified. Read
  `docs/record-reviews.md`; a chat answer is not a persisted review.
- AIO class merging/splitting requires identity and scope evidence. A proposal
  is not permission to rewrite upstream identifiers or delete records.
- Use primary publications and versioned implementation documentation for
  mechanisms, limitations, bias, and evaluation claims. Preserve contradictory
  evidence. Do not run paid providers, train models, or upload data without
  explicit authorization.
- Curated changes require an append-only history sidecar using
  `just new-history`; record what actually happened, with actual UTC times.
  Importing an ontology is not a scientific curation event for every term.
- Do not modify vendored CLAW artifacts by hand. Changes originate in CLAW and
  arrive through a published, pinned governance release.
- Use dedicated Git worktrees for ongoing changes; preserve user edits and
  check current branch, origin, and status before writing or publishing.
- Search including ignored files (`rg --no-ignore --hidden`) before claiming
  something does not exist.

## Agent entry points

- This file is read by Codex and Antigravity directly and by Claude Code through
  the `CLAUDE.md` symlink; keep it the only instruction file.
Native curation skills live in `.claude/skills/` and are exposed at
`.agents/skills/` (including `review-open-issues`); the record and category
review skills use CLAW's structured output contract in `docs/record-reviews.md`.

See `docs/skills.md` for the task-specific skill index, including record
addition, concept research, source discovery, AIO updates and saved-review
resolution.
