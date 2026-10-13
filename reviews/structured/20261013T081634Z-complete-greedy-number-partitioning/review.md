# Scientific author self-review of Complete greedy number partitioning

- Review: 20261013T081634Z-complete-greedy-number-partitioning
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T08:12:09Z
- Finished UTC: 2026-10-13T08:16:34Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain complete greedy number partitioning as a DRAFT algorithm with an explicit no-match assessment. Six claims preserve exact-search assumptions and the primary source’s contradicted range/makespan equivalence; adversarial author self-review found no actionable record defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CompleteGreedyNumberPartitioning
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ffe0f5151616f68164fad0cc5ef00298de2858a0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CompleteGreedyNumberPartitioning | data/curated/CompleteGreedyNumberPartitioning.yaml | maintained | Complete greedy number partitioning |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CompleteGreedyNumberPartitioning | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 128.13s (0:02:08)<br>Checked 442 record(s); 0 failed.<br>Checked 591 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 250 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 249,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CompleteGreedyNumberPartitioning | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CompleteGreedyNumberPartitioning | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CompleteGreedyNumberPartitioning | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CompleteGreedyNumberPartitioning | {"scope": "Eight fixed integer fixtures, one interruption and two objective/bound counterexamples; not an empirical experiment.", "results": [{"values": [8, 7, 6, 5, 4], "k": 2, "greedy_loads": [13, 17], "best_range": 0, "incumbent_history": [4, 2, 0], "nodes": 16, "certified": true}, {"values": [8, 7, 6, 5, 4], "k": 3, "greedy_loads": [8, 11, 11], "best_range": 3, "incumbent_history": [3], "nodes": 13, "certified": true}, {"values": [4, 4, 4, 6, 6, 9], "k": 3, "greedy_loads": [10, 10, 13], "best_range": 3, "incumbent_history": [3], "nodes": 23, "certified": true}, {"values": [5, 5, 5, 5], "k": 3, "greedy_loads": [5, 5, 10], "best_range": 5, "incumbent_history": [5], "nodes": 7, "certified": true}, {"values": [0, 0, 0], "k": 3, "greedy_loads": [0, 0, 0], "best_range": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [9], "k": 3, "greedy_loads": [0, 0, 9], "best_range": 9, "incumbent_history": [9], "nodes": 2, "certified": true}, {"values": [10, 3, 2], "k": 2, "greedy_loads": [5, 10], "best_range": 5, "incumbent_history": [5], "nodes": 2, "certified": true}, {"values": [3, 2, 2], "k": 2, "greedy_loads": [3, 4], "best_range": 1, "incumbent_history": [1], "nodes": 0, "certified": true}], "interrupted": {"best_range": 4, "incumbent_history": [4], "nodes": 1, "certified": false}, "range_vs_makespan": {"values": [4, 4, 4, 6, 6, 9], "minimum_range": 3, "range_optimal_loads": [10, 10, 13], "minimum_makespan": 12, "makespan_optimal_loads": [9, 12, 12]}, "optimistic_bound": {"partial_loads": [10, 0, 0], "remaining": [4], "bound": 8, "attainable_minimum_range": 10}} |

## Scientific And Domain Assessments

### Complete greedy number partitioning

identity: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Retain this distinct DRAFT algorithm.

CGA denotes complete item-to-bin assignment with a greedy child order; two-way and multiway forms share this mechanism. KK/CKK residual composition and generic DFS or discrepancy search remain distinct identities.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Explicit no-match assessment is supported.

All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence.

### greedy-first-assignment

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

The source specifies descending original weights and lighter-bin-first choices. The record unifies two-way and k-way forms under the range objective, without confusing residual composition or makespan.

### symmetry-scope

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

Skipping equal current loads preserves objective-value coverage for interchangeable unconstrained bins. It need not enumerate every membership partition and does not transfer to bin-specific constraints.

### optimistic-range-bound

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

The Section7.2 average bound is admissible but may be unattainable. The fixed (10,0,0) plus item4 calculation gives bound8 and best range10; only the two-way dominance case is asserted attainable.

### complete-versus-interrupted

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

Exhaustive finite search with sound bounds is exact. The integer0/1 lower bound depends on total modulo k and must actually be attained to certify early. The one-node example remains uncertified; no polynomial guarantee is implied.

### range-is-not-makespan

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

The primary defines range but also states an overbroad objective equivalence. That assertion is explicitly retained as contradictory evidence. Exhaustive fixed-instance load enumeration verifies range-optimal (10,10,13) and smaller makespan12 via (9,12,12); no secondary source or numerical experiment is substituted for the direct counterexample.

### reported-comparisons

evidence: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Supported within the stated primary-source and mathematical scope.

The compared algorithms, input distributions and implementation node conventions are preserved. Historical CKK advantages do not imply universal ordering or improvement at every expansion.

### greedy-first enumeration, symmetry scope, optimistic multiway bounds and nonequivalent range/makespan objectives

consistency: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Constructed calculations support the stated distinctions.

Eight exact-integer fixtures compare a constructed CGA-style search with exhaustive assignment states. A one-node interruption retains an uncertified greedy residue; a multiway lower bound is strictly optimistic. A fixed six-weight example separates range-minimizing and makespan-minimizing solutions. No author implementation or performance experiment.

### All maintained fields

provenance: supported. Targets: AIMech:CompleteGreedyNumberPartitioning.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read all maintained fields and six examined-target YAMLs after capture. Reread the two-way greedy and complete mechanisms, k-way branch symmetry and range bound, and three-way experimental scope. The complete manuscript was read before curation. Rechecked the constructed unattainable lower-bound and range-versus-makespan examples, including the explicitly contradictory source statement.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T081051Z-complete-greedy-number-partitioning.json | supports | Compared all 442 pinned AIO and 589 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 63, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 67 AIO and 96 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. The named CGA performs complete item-to-bin assignment with a greedy successor order. It is distinct from generic DFS, discrepancy ordering and KK/CKK residual composition. Its two-way and multiway forms share this item-assignment mechanism and are retained in one range-minimization record; k-way bounds are not asserted to be attainable. Existing hits are neighboring records, rendered text and discovery leads. No suitable pinned AIO counterpart was identified. |
| mapping | sources/aio/aio.json | supports | All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence. |
| korf1997 | https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf; All31 manuscript pages read, selected algorithm and evaluation pages reread after capture. Later1998 publisher metadata was read; final journal full text and author code were not inspected. Constructed arithmetic only. | supports | University-hosted31-page manuscript dated27June1997, read in full. DOI identifies the later1998 Artificial Intelligence106(2):181–203 publication; its final typeset text was not inspected. Locators refer to manuscript PDF/printed pages1–31. |
| calculation | research/discovery/complete-greedy-number-partitioning-boundaries.py | supports | Eight exact-integer fixtures compare a constructed CGA-style search with exhaustive assignment states. A one-node interruption retains an uncertified greedy residue; a multiway lower bound is strictly optimistic. A fixed six-weight example separates range-minimizing and makespan-minimizing solutions. No author implementation or performance experiment. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 590 native and 442 unchanged generated records. The 774-entry main frontier retains 480 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All31 pages of the dated1997 manuscript visually read, with two-way and multiway algorithm and evaluation sections inspected. Later1998 publisher metadata was read; final typeset full text and author implementation remain uninspected. Constructed arithmetic only.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T081634Z-complete-greedy-number-partitioning
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Complete greedy number partitioning
started_at: '2026-10-13T08:12:09Z'
finished_at: '2026-10-13T08:16:34Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged greedy-first enumeration, symmetry scope,
    optimistic multiway bounds and nonequivalent range/makespan objectives. This is
    adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain complete greedy number partitioning as a DRAFT algorithm with an explicit
  no-match assessment. Six claims preserve exact-search assumptions and the primary
  source’s contradicted range/makespan equivalence; adversarial author self-review
  found no actionable record defect.
source:
  git_revision: ffe0f5151616f68164fad0cc5ef00298de2858a0
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
    role: target
  - path: data/curated/CompleteKarmarkarKarp.yaml
    sha256: 65431bae97ba1ebb9e38b2a17a9b59fcc156087167173faf88308b5f38fddcca
    role: context
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/KarmarkarKarpDifferencing.yaml
    sha256: 3bfbfa6fc45fe53b3bda3c61ace7e2beb7d39b8dec3ee93b360d5cfe0d6afdfc
    role: context
  - path: data/curated/LimitedDiscrepancySearch.yaml
    sha256: 144d2daed4c13fdca8e6b1251fa64c4c486354ac6d80c2c5e51b828b0cabbee1
    role: context
  - path: research/discovery/20261013T081051Z-complete-greedy-number-partitioning.json
    sha256: 501c36c33de990d0b48b0194b25f25c21a6ab3b853fa2f5b9b508b1c621fca0f
    role: context
  - path: research/discovery/complete-greedy-number-partitioning-boundaries.py
    sha256: d3315fe23a6ef79f75aa916e3390d1f71c4b26e6eedb4a8023a508b6eff1655b
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
- target_id: AIMech:CompleteGreedyNumberPartitioning
  path: data/curated/CompleteGreedyNumberPartitioning.yaml
  label: Complete greedy number partitioning
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CompleteGreedyNumberPartitioning.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CompleteGreedyNumberPartitioning'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All31 manuscript pages read, selected algorithm and evaluation pages reread
      after capture. Later1998 publisher metadata was read; final journal full text
      and author code were not inspected. Constructed arithmetic only.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 128.13s (0:02:08)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 591 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 250 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 249,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
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
  - AIMech:CompleteGreedyNumberPartitioning
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
  - AIMech:CompleteGreedyNumberPartitioning
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/complete-greedy-number-partitioning-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Eight fixed integer fixtures, one interruption and two objective/bound
    counterexamples; not an empirical experiment.", "results": [{"values": [8, 7,
    6, 5, 4], "k": 2, "greedy_loads": [13, 17], "best_range": 0, "incumbent_history":
    [4, 2, 0], "nodes": 16, "certified": true}, {"values": [8, 7, 6, 5, 4], "k": 3,
    "greedy_loads": [8, 11, 11], "best_range": 3, "incumbent_history": [3], "nodes":
    13, "certified": true}, {"values": [4, 4, 4, 6, 6, 9], "k": 3, "greedy_loads":
    [10, 10, 13], "best_range": 3, "incumbent_history": [3], "nodes": 23, "certified":
    true}, {"values": [5, 5, 5, 5], "k": 3, "greedy_loads": [5, 5, 10], "best_range":
    5, "incumbent_history": [5], "nodes": 7, "certified": true}, {"values": [0, 0,
    0], "k": 3, "greedy_loads": [0, 0, 0], "best_range": 0, "incumbent_history": [0],
    "nodes": 0, "certified": true}, {"values": [9], "k": 3, "greedy_loads": [0, 0,
    9], "best_range": 9, "incumbent_history": [9], "nodes": 2, "certified": true},
    {"values": [10, 3, 2], "k": 2, "greedy_loads": [5, 10], "best_range": 5, "incumbent_history":
    [5], "nodes": 2, "certified": true}, {"values": [3, 2, 2], "k": 2, "greedy_loads":
    [3, 4], "best_range": 1, "incumbent_history": [1], "nodes": 0, "certified": true}],
    "interrupted": {"best_range": 4, "incumbent_history": [4], "nodes": 1, "certified":
    false}, "range_vs_makespan": {"values": [4, 4, 4, 6, 6, 9], "minimum_range": 3,
    "range_optimal_loads": [10, 10, 13], "minimum_makespan": 12, "makespan_optimal_loads":
    [9, 12, 12]}, "optimistic_bound": {"partial_loads": [10, 0, 0], "remaining": [4],
    "bound": 8, "attainable_minimum_range": 10}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T081051Z-complete-greedy-number-partitioning.json
  accessed_at: '2026-10-13T08:12:09Z'
  support: supports
  summary: Compared all 442 pinned AIO and 589 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    63, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 67 AIO and 96 native definitions, with every matched definition read.
    6 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. The named CGA performs complete item-to-bin assignment with a greedy
    successor order. It is distinct from generic DFS, discrepancy ordering and KK/CKK
    residual composition. Its two-way and multiway forms share this item-assignment
    mechanism and are retained in one range-minimization record; k-way bounds are
    not asserted to be attainable. Existing hits are neighboring records, rendered
    text and discovery leads. No suitable pinned AIO counterpart was identified.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T08:12:09Z'
  support: supports
  summary: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- evidence_id: korf1997
  kind: primary_source
  reference: https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf
  locator: All31 manuscript pages read, selected algorithm and evaluation pages reread
    after capture. Later1998 publisher metadata was read; final journal full text
    and author code were not inspected. Constructed arithmetic only.
  accessed_at: '2026-10-13T07:27:28Z'
  snapshot_sha256: 00751dfacfb610eaca973274764704476ecef22865526b9528eb88e07dc09074
  support: supports
  summary: University-hosted31-page manuscript dated27June1997, read in full. DOI
    identifies the later1998 Artificial Intelligence106(2):181–203 publication; its
    final typeset text was not inspected. Locators refer to manuscript PDF/printed
    pages1–31.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/complete-greedy-number-partitioning-boundaries.py
  accessed_at: '2026-10-13T08:13:46Z'
  snapshot_sha256: d3315fe23a6ef79f75aa916e3390d1f71c4b26e6eedb4a8023a508b6eff1655b
  support: supports
  summary: Eight exact-integer fixtures compare a constructed CGA-style search with
    exhaustive assignment states. A one-node interruption retains an uncertified greedy
    residue; a multiway lower bound is strictly optimistic. A fixed six-weight example
    separates range-minimizing and makespan-minimizing solutions. No author implementation
    or performance experiment.
assessments:
- assessment_id: identity
  area: identity
  topic: Complete greedy number partitioning
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - identity
  - korf1997
  summary: Retain this distinct DRAFT algorithm.
  details: CGA denotes complete item-to-bin assignment with a greedy child order;
    two-way and multiway forms share this mechanism. KK/CKK residual composition and
    generic DFS or discrepancy search remain distinct identities.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - mapping
  - korf1997
  summary: Explicit no-match assessment is supported.
  details: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- assessment_id: greedy-first-assignment
  area: evidence
  topic: greedy-first-assignment
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source specifies descending original weights and lighter-bin-first
    choices. The record unifies two-way and k-way forms under the range objective,
    without confusing residual composition or makespan.
- assessment_id: symmetry-scope
  area: evidence
  topic: symmetry-scope
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Skipping equal current loads preserves objective-value coverage for interchangeable
    unconstrained bins. It need not enumerate every membership partition and does
    not transfer to bin-specific constraints.
- assessment_id: optimistic-range-bound
  area: evidence
  topic: optimistic-range-bound
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The Section7.2 average bound is admissible but may be unattainable. The
    fixed (10,0,0) plus item4 calculation gives bound8 and best range10; only the
    two-way dominance case is asserted attainable.
- assessment_id: complete-versus-interrupted
  area: evidence
  topic: complete-versus-interrupted
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exhaustive finite search with sound bounds is exact. The integer0/1 lower
    bound depends on total modulo k and must actually be attained to certify early.
    The one-node example remains uncertified; no polynomial guarantee is implied.
- assessment_id: range-is-not-makespan
  area: evidence
  topic: range-is-not-makespan
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The primary defines range but also states an overbroad objective equivalence.
    That assertion is explicitly retained as contradictory evidence. Exhaustive fixed-instance
    load enumeration verifies range-optimal (10,10,13) and smaller makespan12 via
    (9,12,12); no secondary source or numerical experiment is substituted for the
    direct counterexample.
- assessment_id: reported-comparisons
  area: evidence
  topic: reported-comparisons
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: The compared algorithms, input distributions and implementation node conventions
    are preserved. Historical CKK advantages do not imply universal ordering or improvement
    at every expansion.
- assessment_id: constructed-boundaries
  area: consistency
  topic: greedy-first enumeration, symmetry scope, optimistic multiway bounds and
    nonequivalent range/makespan objectives
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - korf1997
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Eight exact-integer fixtures compare a constructed CGA-style search with
    exhaustive assignment states. A one-node interruption retains an uncertified greedy
    residue; a multiway lower bound is strictly optimistic. A fixed six-weight example
    separates range-minimizing and makespan-minimizing solutions. No author implementation
    or performance experiment.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CompleteGreedyNumberPartitioning
  evidence_ids:
  - identity
  - mapping
  - korf1997
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read all maintained fields and six examined-target
    YAMLs after capture. Reread the two-way greedy and complete mechanisms, k-way
    branch symmetry and range bound, and three-way experimental scope. The complete
    manuscript was read before curation. Rechecked the constructed unattainable lower-bound
    and range-versus-makespan examples, including the explicitly contradictory source
    statement.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 590 native and 442 unchanged generated records.
  The 774-entry main frontier retains 480 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All31 pages of the dated1997 manuscript visually read, with two-way and multiway
  algorithm and evaluation sections inspected. Later1998 publisher metadata was read;
  final typeset full text and author implementation remain uninspected. Constructed
  arithmetic only.
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
