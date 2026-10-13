# Scientific author self-review of Complete multiway Karmarkar–Karp

- Review: 20261013T083223Z-complete-multiway-karmarkar-karp
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T08:27:14Z
- Finished UTC: 2026-10-13T08:32:23Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain complete multiway Karmarkar–Karp as a DRAFT algorithm with explicit AIO no-match. Six claims preserve complete-search assumptions, objective-value scope and experimental limits; adversarial author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CompleteMultiwayKarmarkarKarp
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2fdc631466528afe05479e16bd83400da1110e4b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CompleteMultiwayKarmarkarKarp | data/curated/CompleteMultiwayKarmarkarKarp.yaml | maintained | Complete multiway Karmarkar–Karp |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CompleteMultiwayKarmarkarKarp | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 116.71s (0:01:56)<br>Checked 442 record(s); 0 failed.<br>Checked 593 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 252 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 251,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CompleteMultiwayKarmarkarKarp | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CompleteMultiwayKarmarkarKarp | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CompleteMultiwayKarmarkarKarp | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CompleteMultiwayKarmarkarKarp | {"scope": "Seven exact-integer fixtures and one-node interruption; constructed algorithm and no runtime benchmark.", "results": [{"values": [8, 7, 6, 5, 4], "k": 3, "optimum_range": 3, "loads": [11, 11, 8], "indices": [[3, 2], [4, 1], [0]], "range": 3, "initial_range": 3, "incumbent_history": [3], "nodes": 14, "certified": true}, {"values": [2, 2, 2, 3, 3, 5], "k": 3, "optimum_range": 1, "loads": [6, 6, 5], "indices": [[2, 0, 1], [3, 4], [5]], "range": 1, "initial_range": 2, "incumbent_history": [2, 1], "nodes": 13, "certified": true}, {"values": [4, 4, 4, 6, 6, 9], "k": 3, "optimum_range": 3, "loads": [13, 10, 10], "indices": [[5, 0], [3, 1], [4, 2]], "range": 3, "initial_range": 3, "incumbent_history": [3], "nodes": 19, "certified": true}, {"values": [5, 5, 5, 5], "k": 3, "optimum_range": 5, "loads": [10, 5, 5], "indices": [[1, 3], [0], [2]], "range": 5, "initial_range": 5, "incumbent_history": [5], "nodes": 7, "certified": true}, {"values": [0, 0, 0], "k": 3, "optimum_range": 0, "loads": [0, 0, 0], "indices": [[2, 1], [], [0]], "range": 0, "initial_range": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [9], "k": 3, "optimum_range": 9, "loads": [9, 0, 0], "indices": [[0], [], []], "range": 9, "initial_range": 9, "incumbent_history": [9], "nodes": 1, "certified": true}, {"values": [8, 7, 6, 5, 4], "k": 4, "optimum_range": 3, "loads": [9, 8, 7, 6], "indices": [[4, 3], [0], [1], [2]], "range": 3, "initial_range": 3, "incumbent_history": [3], "nodes": 14, "certified": true}], "interrupted": {"loads": [7, 5, 5], "indices": [[1, 5], [0, 3], [2, 4]], "range": 2, "initial_range": 2, "incumbent_history": [2], "nodes": 1, "certified": false}, "objective_boundary": {"range_optimal_loads": [10, 10, 13], "minimum_range": 3, "minimum_makespan": 12}} |

## Scientific And Domain Assessments

### Complete multiway Karmarkar–Karp

identity: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Retain this distinct DRAFT algorithm.

The k&gt;=3 complete permutation search differs from the maintained one-composition heuristic, scalar two-way CKK, and CGA raw-item assignment. The combined multiway discovery lead is now addressed by two distinct maintained records.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Explicit no-match assessment is supported.

All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence.

### permutation-search

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Section7.4 selects subpartitions by normalized maximum, explores relative bin alignments and orders new compositions by their range. Indexed construction preserves the represented original items and distinguishes raw-item assignment.

### coverage-and-symmetry

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

The source’s uniqueness argument precedes normalization. The record explicitly separates all-membership enumeration from equal-load objective-value reduction, and does not confuse relative zero with empty bins.

### admissible-load-bound

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

The source sums all normalized components except the largest and distributes their total over k-1 bins for an optimistic lower bound. It is not an attainable completion; exact-rational fixture bounds preserve sound pruning.

### anytime-certification

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

The constructed search agrees with exhaustive assignments on seven fixtures. A one-node interruption retains a feasible range2 without certification, whereas full search reaches1. Integer lower bounds require actual attainment; no polynomial worst-case claim is made.

### range-objective

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

The source’s objective-equivalence statement is explicitly contradictory evidence. The six-weight exhaustive example shows a range-optimal tie with largest load13 although makespan12 is feasible and optimal.

### reported-evaluation-scope

evidence: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Section7.5 identifies 100 uniform-integer trials per point and distinguishes per-node cost from total search cost. The record keeps the three-way distribution and precision scope.

### complete permutation coverage, objective-value symmetry, normalized bounds, interrupted incumbents and range/makespan distinction

consistency: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Constructed calculations support the stated distinctions.

Seven indexed exact-integer fixtures compare a constructed permutation search against exhaustive item assignments. A one-node interruption retains range2 without certification, while complete search attains1. Every returned partition covers each original index once. The objective counterexample preserves range3 versus makespan12. No author-code execution or performance experiment.

### All maintained fields

provenance: supported. Targets: AIMech:CompleteMultiwayKarmarkarKarp.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read every maintained field and six examined-target YAMLs after capture. Reread relative permutation branching, normalization, the pre-normalization uniqueness argument and objective-value symmetry, average load bounds and three-way evaluation scope. Rechecked indexed fixed examples, interrupted certification and range/makespan contradiction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T082539Z-complete-multiway-karmarkar-karp.json | supports | Compared all 442 pinned AIO and 591 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 88, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 67 AIO and 98 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. This k&gt;=3 complete vector-subpartition search explores relative bin permutations. It extends the maintained multiway heuristic with exhaustive alternatives and bounds; the scalar two-way CKK and raw-item CGA remain distinct. Text matches are neighboring records and the partly addressed combined multiway discovery lead. No suitable pinned AIO counterpart was identified. |
| mapping | sources/aio/aio.json | supports | All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence. |
| korf1997 | https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf; All 31 Korf manuscript pages read before curation; selected multiway-method pages reread after capture. Final journal full text and author code uninspected. Constructed exact arithmetic only. | supports | University-hosted31-page manuscript dated27June1997, read in full. DOI identifies the later1998 Artificial Intelligence106(2):181–203 publication; its final typeset text was not inspected. Locators refer to manuscript PDF/printed pages1–31. |
| calculation | research/discovery/complete-multiway-karmarkar-karp-boundaries.py | supports | Seven indexed exact-integer fixtures compare a constructed permutation search against exhaustive item assignments. A one-node interruption retains range2 without certification, while complete search attains1. Every returned partition covers each original index once. The objective counterexample preserves range3 versus makespan12. No author-code execution or performance experiment. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 592 native and 442 unchanged generated records. The 776-entry main frontier retains 480 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 31 pages of the dated Korf manuscript visually read. The source defines and evaluates complete multiway search. Final 1998 typeset full text and author code remain uninspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T083223Z-complete-multiway-karmarkar-karp
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Complete multiway Karmarkar–Karp
started_at: '2026-10-13T08:27:14Z'
finished_at: '2026-10-13T08:32:23Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged complete permutation coverage, objective-value
    symmetry, normalized bounds, interrupted incumbents and range/makespan distinction.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain complete multiway Karmarkar–Karp as a DRAFT algorithm with explicit
  AIO no-match. Six claims preserve complete-search assumptions, objective-value scope
  and experimental limits; adversarial author self-review found no actionable defect.
source:
  git_revision: 2fdc631466528afe05479e16bd83400da1110e4b
  state: working_tree
  inputs:
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/curated/CompleteGreedyNumberPartitioning.yaml
    sha256: 449aea6d4207da9e65e090c87cb49235af72c91d33deb0ac30525cdfdb7b3ebb
    role: context
  - path: data/curated/CompleteKarmarkarKarp.yaml
    sha256: 65431bae97ba1ebb9e38b2a17a9b59fcc156087167173faf88308b5f38fddcca
    role: context
  - path: data/curated/CompleteMultiwayKarmarkarKarp.yaml
    sha256: edb8294a842cddc1bd0487c0a8db2202d539fcdf201a13ef2c8147cd3bb16849
    role: target
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/MultiwayKarmarkarKarpDifferencing.yaml
    sha256: 95e58060777b89d40091db19dbac12f6375a4f7f82c27b6aa5456526ec137842
    role: context
  - path: research/discovery/20261013T082539Z-complete-multiway-karmarkar-karp.json
    sha256: 54e52ede64971d41a22ae39ad5033d50fbe0a00377c00efbd7df8b0b2413b9e1
    role: context
  - path: research/discovery/complete-multiway-karmarkar-karp-boundaries.py
    sha256: 74c05cde798d2be2c61b5b51ef7cd674872708e592ccab1409f87cbb098a3125
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
- target_id: AIMech:CompleteMultiwayKarmarkarKarp
  path: data/curated/CompleteMultiwayKarmarkarKarp.yaml
  label: Complete multiway Karmarkar–Karp
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CompleteMultiwayKarmarkarKarp.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CompleteMultiwayKarmarkarKarp'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All 31 Korf manuscript pages read before curation; selected multiway-method
      pages reread after capture. Final journal full text and author code uninspected.
      Constructed exact arithmetic only.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 116.71s (0:01:56)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 593 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 252 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 251,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/complete-multiway-karmarkar-karp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Seven exact-integer fixtures and one-node interruption; constructed
    algorithm and no runtime benchmark.", "results": [{"values": [8, 7, 6, 5, 4],
    "k": 3, "optimum_range": 3, "loads": [11, 11, 8], "indices": [[3, 2], [4, 1],
    [0]], "range": 3, "initial_range": 3, "incumbent_history": [3], "nodes": 14, "certified":
    true}, {"values": [2, 2, 2, 3, 3, 5], "k": 3, "optimum_range": 1, "loads": [6,
    6, 5], "indices": [[2, 0, 1], [3, 4], [5]], "range": 1, "initial_range": 2, "incumbent_history":
    [2, 1], "nodes": 13, "certified": true}, {"values": [4, 4, 4, 6, 6, 9], "k": 3,
    "optimum_range": 3, "loads": [13, 10, 10], "indices": [[5, 0], [3, 1], [4, 2]],
    "range": 3, "initial_range": 3, "incumbent_history": [3], "nodes": 19, "certified":
    true}, {"values": [5, 5, 5, 5], "k": 3, "optimum_range": 5, "loads": [10, 5, 5],
    "indices": [[1, 3], [0], [2]], "range": 5, "initial_range": 5, "incumbent_history":
    [5], "nodes": 7, "certified": true}, {"values": [0, 0, 0], "k": 3, "optimum_range":
    0, "loads": [0, 0, 0], "indices": [[2, 1], [], [0]], "range": 0, "initial_range":
    0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [9], "k":
    3, "optimum_range": 9, "loads": [9, 0, 0], "indices": [[0], [], []], "range":
    9, "initial_range": 9, "incumbent_history": [9], "nodes": 1, "certified": true},
    {"values": [8, 7, 6, 5, 4], "k": 4, "optimum_range": 3, "loads": [9, 8, 7, 6],
    "indices": [[4, 3], [0], [1], [2]], "range": 3, "initial_range": 3, "incumbent_history":
    [3], "nodes": 14, "certified": true}], "interrupted": {"loads": [7, 5, 5], "indices":
    [[1, 5], [0, 3], [2, 4]], "range": 2, "initial_range": 2, "incumbent_history":
    [2], "nodes": 1, "certified": false}, "objective_boundary": {"range_optimal_loads":
    [10, 10, 13], "minimum_range": 3, "minimum_makespan": 12}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T082539Z-complete-multiway-karmarkar-karp.json
  accessed_at: '2026-10-13T08:27:14Z'
  support: supports
  summary: Compared all 442 pinned AIO and 591 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    88, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 67 AIO and 98 native definitions, with every matched definition read.
    6 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. This k>=3 complete vector-subpartition search explores relative bin
    permutations. It extends the maintained multiway heuristic with exhaustive alternatives
    and bounds; the scalar two-way CKK and raw-item CGA remain distinct. Text matches
    are neighboring records and the partly addressed combined multiway discovery lead.
    No suitable pinned AIO counterpart was identified.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T08:27:14Z'
  support: supports
  summary: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- evidence_id: korf1997
  kind: primary_source
  reference: https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf
  locator: All 31 Korf manuscript pages read before curation; selected multiway-method
    pages reread after capture. Final journal full text and author code uninspected.
    Constructed exact arithmetic only.
  accessed_at: '2026-10-13T07:27:28Z'
  snapshot_sha256: 00751dfacfb610eaca973274764704476ecef22865526b9528eb88e07dc09074
  support: supports
  summary: University-hosted31-page manuscript dated27June1997, read in full. DOI
    identifies the later1998 Artificial Intelligence106(2):181–203 publication; its
    final typeset text was not inspected. Locators refer to manuscript PDF/printed
    pages1–31.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/complete-multiway-karmarkar-karp-boundaries.py
  accessed_at: '2026-10-13T08:29:03Z'
  snapshot_sha256: 74c05cde798d2be2c61b5b51ef7cd674872708e592ccab1409f87cbb098a3125
  support: supports
  summary: Seven indexed exact-integer fixtures compare a constructed permutation
    search against exhaustive item assignments. A one-node interruption retains range2
    without certification, while complete search attains1. Every returned partition
    covers each original index once. The objective counterexample preserves range3
    versus makespan12. No author-code execution or performance experiment.
assessments:
- assessment_id: identity
  area: identity
  topic: Complete multiway Karmarkar–Karp
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - identity
  - korf1997
  summary: Retain this distinct DRAFT algorithm.
  details: The k>=3 complete permutation search differs from the maintained one-composition
    heuristic, scalar two-way CKK, and CGA raw-item assignment. The combined multiway
    discovery lead is now addressed by two distinct maintained records.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - mapping
  - korf1997
  summary: Explicit no-match assessment is supported.
  details: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- assessment_id: permutation-search
  area: evidence
  topic: permutation-search
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section7.4 selects subpartitions by normalized maximum, explores relative
    bin alignments and orders new compositions by their range. Indexed construction
    preserves the represented original items and distinguishes raw-item assignment.
- assessment_id: coverage-and-symmetry
  area: evidence
  topic: coverage-and-symmetry
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source’s uniqueness argument precedes normalization. The record explicitly
    separates all-membership enumeration from equal-load objective-value reduction,
    and does not confuse relative zero with empty bins.
- assessment_id: admissible-load-bound
  area: evidence
  topic: admissible-load-bound
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source sums all normalized components except the largest and distributes
    their total over k-1 bins for an optimistic lower bound. It is not an attainable
    completion; exact-rational fixture bounds preserve sound pruning.
- assessment_id: anytime-certification
  area: evidence
  topic: anytime-certification
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The constructed search agrees with exhaustive assignments on seven fixtures.
    A one-node interruption retains a feasible range2 without certification, whereas
    full search reaches1. Integer lower bounds require actual attainment; no polynomial
    worst-case claim is made.
- assessment_id: range-objective
  area: evidence
  topic: range-objective
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source’s objective-equivalence statement is explicitly contradictory
    evidence. The six-weight exhaustive example shows a range-optimal tie with largest
    load13 although makespan12 is feasible and optimal.
- assessment_id: reported-evaluation-scope
  area: evidence
  topic: reported-evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section7.5 identifies 100 uniform-integer trials per point and distinguishes
    per-node cost from total search cost. The record keeps the three-way distribution
    and precision scope.
- assessment_id: constructed-boundaries
  area: consistency
  topic: complete permutation coverage, objective-value symmetry, normalized bounds,
    interrupted incumbents and range/makespan distinction
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Seven indexed exact-integer fixtures compare a constructed permutation
    search against exhaustive item assignments. A one-node interruption retains range2
    without certification, while complete search attains1. Every returned partition
    covers each original index once. The objective counterexample preserves range3
    versus makespan12. No author-code execution or performance experiment.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CompleteMultiwayKarmarkarKarp
  evidence_ids:
  - identity
  - mapping
  - korf1997
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read every maintained field and six examined-target
    YAMLs after capture. Reread relative permutation branching, normalization, the
    pre-normalization uniqueness argument and objective-value symmetry, average load
    bounds and three-way evaluation scope. Rechecked indexed fixed examples, interrupted
    certification and range/makespan contradiction.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 592 native and 442 unchanged generated records.
  The 776-entry main frontier retains 480 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All 31 pages of the dated Korf manuscript visually read. The source defines and
  evaluates complete multiway search. Final 1998 typeset full text and author code
  remain uninspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
