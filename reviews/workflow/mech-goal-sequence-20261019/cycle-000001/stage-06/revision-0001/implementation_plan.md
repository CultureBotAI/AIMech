# AIMech Cycle 1 Stage 6 Infrastructure Plan

## Frozen Scope

- **Run / cycle / stage**: `mech-goal-sequence-20261019`, Cycle 1, Stage 6 (`infrastructure`)
- **Source revision**: `78dcdfa7ff0b44ceb19c929e657ee630aea423e0`
- **Frozen cutoff**: `2026-11-15T04:13:11Z`
- **Frozen ledger**: `INFRA_TASKS.md`, SHA-256 `56b898abab73acfd24d931a1cf246bd6417993fada6fccacc612ef0975c2622d`

The frozen machine-readable intake contains two tasks:

| Task | Frozen status | Issue | Stage 6 disposition |
| --- | --- | --- | --- |
| `aimech-infra-0001` | `resolved` | #429 | Already closed in PR #428 and excluded from the pending Stage 6 scope. |
| `aimech-infra-0002` | `open` | #431 | Deferred to upstream `CultureBotAI/culturebotai-claw` fleet profile work; carried forward with its existing issue URL. |

`aimech-infra-0002` is the only non-resolved task in the frozen notebook. Its remaining action is an upstream CLAW edit to `src/kg_microbe_fleet/fleet.yaml` and a canonical skill-adapter regeneration. The AIMech-local `review-open-issues` adapter already preserves `data/curated/*.yaml`, and the active `workflow/parent/*` files are vendored, hash-pinned parent artifacts that must not be edited in AIMech by hand.

## GitHub Issue Deduplication

The live open issue queue was swept before ranking or planning: Issues #454, #446, #445, #444, #443, #442, #441, #440, #439, #438, #437, #436, #435, #431, #406, #404, and #402 were open, with no issue comments.

| Rank | Issue | What it weakens | Who depends on it | What closes it |
| ---: | --- | --- | --- | --- |
| 1 | #454 | Upstream AIO class identity and hierarchy quality for nine generated `data/aio/*.yaml` records. | AIMech consumers of the pinned AIO projection. | Upstream AIO curation plus a reviewed AIMech AIO snapshot refresh; local generated YAML edits remain out of scope. |
| 2 | #431 | Canonical CLAW fleet metadata omits AIMech curated records and their LinkML schema when regenerating local adapters. | Future CLAW adapter regeneration for AIMech and fleet tooling that reads `mechs.aimech`. | Update `CultureBotAI/culturebotai-claw` fleet metadata and regenerate adapters through CLAW governance. |
| 3 | #443 | Reuse terms for `data/curated/*.yaml` are undeclared. | Curated-record data reusers and the site footer/export manifest work in PR #434. | Owner licence decision recorded in repository files and reflected in downstream presentation/export text. |
| 4 | #436 | Future Pages exports can traceback on unquoted YAML timestamps. | GitHub Pages deploys after PR #434 and anyone running `scripts/export_records.py`. | Harden `scripts/export_records.py` error reporting and keep content-preserving JSON encoding. |
| 5 | #445 | The text map omits 670 newer curated concepts. | Site users relying on the map and record pages linked to map coverage. | Rerun embedding recipes through their provenance-checked path and regenerate site output. |
| 6 | #435 | Every curation commit rewrites all record pages through a corpus-wide footer stamp. | Record curation PR authors and reviewers who otherwise fight generated-page conflicts. | Move corpus-wide build provenance to aggregate pages and test that unrelated record changes do not rewrite a record page. |
| 7 | #444 | No schema slot can express evidence-backed links from AIMech records to sibling-Mech records. | Cross-Mech site/catalogue users. | Owner decision and scoped schema/curation support for real sibling links, or an explicit no-action disposition. |
| 8 | #446 | Antigravity history sidecar timestamps disagree with affected records' `curation.updated_at` semantics. | Record-page curation-history readers after PR #434. | Decide the timestamp meaning, document it, and repair or qualify disagreeing records and sidecars. |
| 9 | #406 | Thirty-three recovered discovery questions lack queryable ownership dispositions. | Future add-record/source-review work that needs historical discovery context. | Preserve exact historical objects and reconcile each question to represented, source-only, deferred, or distinct-method outcomes. |
| 10 | #404 | Gent-Walsh 1995 SAT follow-up questions lack explicit owner/disposition records. | Future SAT local-search curation. | Resolve each source question to a pending owner or evidence-backed represented/equivalent disposition. |
| 11 | #402 | Four older bibliography pointers remain untriaged. | Future clustering, novelty-detection, outlier, and ICA curation. | Verify each citation and save dated source and identity dispositions. |
| 12 | #441 | Draft PR #434's map coverage wording infers stale embeddings from creation dates rather than a recorded fingerprint. | Site users reading the map coverage explanation. | Either soften the inference or compare `corpus_fingerprint` with the current corpus fingerprint. |
| 13 | #437 | Draft PR #434 status explanations would collide if the two schemas ever shared a bare status value. | Future site renders after status vocabulary expansion. | Key status meanings by schema plus status, or assert the enum values are disjoint. |
| 14 | #442 | Draft PR #434 autolinking mishandles URLs with square brackets. | Site readers if a future cited URL includes brackets. | Fix the URL/DOI character classes or bracket trimming. |
| 15 | #438 | Draft PR #434 adds an empty favicon link without documenting that sweep-affecting behavior. | PR #434 reviewers. | Document the favicon request suppression in the PR body or commit message. |
| 16 | #440 | Draft PR #434 renderer comments cite other repositories' issue numbers ambiguously. | Future maintainers reading the renderer source. | Expand those comments to full cross-repository issue references. |
| 17 | #439 | Draft PR #434 text overcounts committed pages in two test descriptions. | PR #434 reviewers. | Correct the PR body to distinguish committed pages from staged artifact pages. |

No open issue duplicates `aimech-infra-0002`: #431 is the existing owner. Issue #454 intentionally tracks deferred upstream AIO record-boundary findings and stays outside the Stage 6 implementation plan. Draft PRs #458 and #434 have separate owners and scopes; Stage 6 neither merges nor activates them.

## Selected Work

1. Preserve the frozen Stage 6 input by saving `infra_snapshot.md` with the exact `INFRA_TASKS.md` bytes from the cutoff.
2. Reconcile the one pending frozen task against #431 and mark it `deferred`, not `resolved`, because the remaining mutation belongs in the upstream CLAW repository and future adapter regeneration.
3. Preserve the local AIMech scope guard in `.claude/skills/review-open-issues/SKILL.md`, which still names both `data/aio/*.yaml` and `data/curated/*.yaml`.
4. Preserve the active vendored workflow parent and schema snapshots unchanged.
5. Validate the updated `INFRA_TASKS.md`, the effective workflow profile, the Stage 6 evidence manifest, `just check`, and `just vendored-check`.

No new GitHub issue is needed for the frozen intake: #431 already owns `aimech-infra-0002`, #429 owns the already-resolved task, and the live issue queue had no untracked Stage 6 infrastructure requirement.

## Acceptance Criteria

- The Stage 6 evidence manifest covers exactly the single non-resolved task from the frozen snapshot, `aimech-infra-0002`.
- `aimech-infra-0002` retains `https://github.com/CultureBotAI/AIMech/issues/431` and has an explicit upstream-deferral disposition.
- `INFRA_TASKS.md` remains schema-valid, preserves `aimech-infra-0001`, and records the Stage 6 disposition for `aimech-infra-0002`.
- No `data/aio/*.yaml`, `data/curated/*.yaml`, `workflow/parent/*`, draft PR #458 files, or draft PR #434 files are modified.
- The final branch passes `just check`, `just vendored-check`, and CLAW `validate-evidence` with required outputs `infra_snapshot`, `implementation_plan`, and `validation`.
