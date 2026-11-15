# AIMech Cycle 1 Stage 6 Validation

## Preflight

| Check | Result |
| --- | --- |
| Canonical branch and base | `main` and `origin/main` both resolved to `78dcdfa7ff0b44ceb19c929e657ee630aea423e0`. |
| Predecessor commit sequence | PR #456 was still merged at `0d2eea9863af2f88908cb9cc8a5ecec0d86263aa`; Issues #451, #452, and #453 were closed by that merge; Issue #454 remained open for the deferred upstream AIO findings. |
| Stage 6 branch | `codex/mc1114-aimech-c1s6-infra` was created from `origin/main`; no local or remote branch with that name existed at cutoff. |
| Existing draft PRs | PR #458 only adds inert files under `workflow/candidates/repository-freshness-v1/`; PR #434 is the independent site feature branch. Neither was reused, merged, or modified. |
| Open issue sweep | All 17 open issues were read before ranking or deduplicating Stage 6 work. |
| Frozen workflow | The pinned Cycle 1 workflow SHA-256 is `65c56ed7473f8837d460c2d8b160c5afe7a9147803e21f9f327dc6bd6e88df1f`; Stage 6 requires `infra_snapshot`, `implementation_plan`, and `validation`. |

## Intake and Plan

| Check | Command or evidence | Result |
| --- | --- | --- |
| Frozen ledger snapshot | `shasum -a 256 reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` | `56b898abab73acfd24d931a1cf246bd6417993fada6fccacc612ef0975c2622d`, matching `INFRA_TASKS.md` at the cutoff. |
| Frozen snapshot immutability | `git show 78dcdfa7ff0b44ceb19c929e657ee630aea423e0:INFRA_TASKS.md \| diff -u - reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` | Passed with no diff. |
| Updated ledger parse | `validate_infra_notebook(Path("INFRA_TASKS.md").read_bytes(), "CultureBotAI/AIMech")` | Parsed 2 tasks: `aimech-infra-0001:resolved`, `aimech-infra-0002:deferred`. |
| Workflow profile | `python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml` | Passed with `Workflow profile valid`. |
| Ownership boundaries | `git diff --name-only -- data/aio data/curated research/discovery workflow/parent workflow/candidates .github pages scripts/fulltext_access.py tests/test_fulltext_access.py` | Passed with no changed paths. |

## Final Checks

| Check | Command or evidence | Result |
| --- | --- | --- |
| Saved-review Git bases | `rg --no-ignore --hidden -o 'git_revision: [0-9a-f]{40}' reviews/structured reviews/workflow \| sed 's/.*git_revision: //' \| sort -u \| git cat-file --batch-check='%(objectname) %(objecttype)' \| rg ' missing$'` | Passed with no missing saved-review base commits after fetching the eight exact historical SHAs not reachable from the live branch set. |
| Focused saved-review contract | `uv run --locked --extra dev python -m pytest tests/test_record_review_contract.py::test_every_saved_structured_bundle_is_valid -q` | Passed: `1 passed in 503.42s`. |
| Project check | `just check` | Passed: `324 passed, 3 skipped`; `Checked 442 record(s); 0 failed.`; `Checked 1487 curated concept record(s); 0 error(s).`; `AIO: 442 records; 0 missing, 0 changed, 0 unexpected.`; `Checked 1142 history record(s); 0 error(s).`; `valid_reviews: 1135`. |
| Vendored CLAW check | `just vendored-check` | Passed: `OK: 22 governed artifacts match the pinned claw revision`. |
| Final ownership boundaries | `git diff --name-only -- data/aio data/curated research/discovery workflow/parent workflow/candidates .github pages scripts/fulltext_access.py tests/test_fulltext_access.py` | Passed with no changed paths. |
| Final evidence manifest | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/evidence.yaml --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation` | Passed at the final saved artifact hashes. |
