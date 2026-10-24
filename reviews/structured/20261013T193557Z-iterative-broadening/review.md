# Scientific author self-review of Iterative broadening

- Review: 20261013T193557Z-iterative-broadening
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T19:26:53Z
- Finished UTC: 2026-10-13T19:35:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain iterative broadening as a DRAFT native algorithm with a bounded AIO no-match assessment. All maintained fields assessed in author self-review; random-tree, approximation, finite-coverage and source-version limits remain explicit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:IterativeBroadening
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base eea7a76cf5e7d42dbe10fc709ec0e8f0da44e76b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IterativeBroadening | data/curated/IterativeBroadening.yaml | maintained | Iterative broadening |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:IterativeBroadening | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 246.28s (0:04:06)<br>Checked 442 record(s); 0 failed.<br>Checked 646 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 325 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 318,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:IterativeBroadening | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:IterativeBroadening | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:IterativeBroadening | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:IterativeBroadening | {"model_failure_depth1": "1/6", "model_failure_depth2": "61/216", "model_success_depth2": "155/216", "pigeonhole_cutoff": "b-s+1", "per_parent_width2_depth2_leaf_count": 4, "binary_width2_already_full": true, "repeated_vs_direct_node_visits": [7, 4], "changed_order_breaks_nested_failure": true, "first_goal_cost_vs_minimum": [10, 1], "scope": "Finite arithmetic and search constructions. Does not certify approximate expected-time analysis, infinite-tree completeness, author implementation or benchmark speedup."} |

## Scientific And Domain Assessments

### Iterative broadening

identity: supported. Targets: AIMech:IterativeBroadening.

Retain this distinct DRAFT algorithm.

Retain repeated depth-first passes with a growing per-parent successor cutoff. A global beam, repeated depth limits and discrepancy budgets are different controls. The1990 conference method is not assumed identical to the later journal formulation.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:IterativeBroadening.

The declared AIO mapping is supported.

Nine full annotated AIO contexts and five full native neighbors support a bounded no-match assessment. Generic learning, classifier-tree, language-model and bias-phenomenon classes do not identify this traversal policy.

### per-parent-breadth-passes

evidence: supported. Targets: AIMech:IterativeBroadening.

Supported within the stated primary-source and mathematical scope.

The first pass retains at most two children per parent, not two nodes globally per depth. A two-level example retains four leaves. Increasing cutoffs may repeat prior work.

### coverage-and-solution-boundaries

evidence: supported. Targets: AIMech:IterativeBroadening.

Supported within the stated primary-source and mathematical scope.

Finite terminating passes and an eventually sufficient cutoff provide the stated coverage conditions. A first-found cost10 goal can precede cost1. No arbitrary infinite-branch or minimum-cost guarantee is asserted.

### special-random-tree-model

evidence: supported. Targets: AIMech:IterativeBroadening.

Supported within the stated primary-source and mathematical scope.

The hypergeometric recurrence under b4,s2,c2 gives failure1/6 at depth1 and61/216 at depth2. Those calculations use the specific exactly-s-good-children model, not arbitrary random goal placement.

### approximation-and-printed-boundary

evidence: supported. Targets: AIMech:IterativeBroadening.

Supported within the stated primary-source and mathematical scope.

Pigeonhole counting gives b-s+1; later b+s-1 prose conflicts with the following sum. Conditional failure ratios require nested passes and positive conditioning probability. The source explicitly labels its successful-work approximation; no general speedup theorem is inferred.

### finite-empirical-boundaries

evidence: supported. Targets: AIMech:IterativeBroadening.

Supported within the stated primary-source and mathematical scope.

The configured tree samples and crossword combinations have limited scope. Constructed repeated traversal costs7 visits versus4 directly, and binary trees are already fully admitted at cutoff2. These are boundary examples, not source benchmarks.

### per-parent width, finite coverage, nested conditioning and the limits of the random-tree performance analysis

consistency: supported. Targets: AIMech:IterativeBroadening.

Constructed calculations support the stated distinctions.

Exact constructions distinguish a per-parent width cap from a global beam, verify the special hypergeometric failure recurrence and b-s+1 coverage condition, and show repeated work, first-goal cost and nonnested reordered-cutoff limits. No author code or benchmark replication.

### All maintained fields

provenance: supported. Targets: AIMech:IterativeBroadening.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed every maintained field, source version and provenance, per-parent versus global width, terminating-pass coverage, first-goal cost, the special good-child tree distribution, nested failure conditioning, explicit expected-time approximation and finite empirical scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T192651Z-iterative-broadening.json | supports | Compared all 442 pinned AIO and 644 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 232, 122, 121 lines. All distinct match contents were inspected. Semantic matching covered 72 AIO and 129 native definitions, with every matched definition read. 9 full annotated AIO node/edge/generated contexts and 5 full native records were inspected. Retain repeated depth-first passes with an increasing per-parent successor cutoff. A global depth-layer or frontier beam, repeated depth cutoffs and discrepancy-budget backtracking restrict different portions of the search tree. The1990 conference formulation starts with cutoff2; no alias to every width-adaptive search is asserted. |
| mapping | sources/aio/aio.json | supports | Nine full annotated AIO contexts and five full native neighbors support a bounded no-match assessment. Generic learning, classifier-tree, language-model and bias-phenomenon classes do not identify this traversal policy. |
| ginsberg1990broadening | https://cdn.aaai.org/AAAI/1990/AAAI90-033.pdf; All five official AAAI1990 PDF pages visually inspected: Sections1–6, Equations1–6, Proposition3.1, Figures1–5, acknowledgments and four references. The1992 journal full text, author code and empirical replication are excluded. | supports | Official AAAI1990 proceedings PDF, five pages, printed216–220. All pages visually inspected: Sections1–6, Equations1–6 and unnumbered expressions, Proposition3.1, Figures1–5 including table cells, acknowledgments and four references. The later1992 journal article, author software and replication were not inspected. |
| calculation | research/discovery/iterative-broadening-boundaries.py | supports | Exact constructions distinguish a per-parent width cap from a global beam, verify the special hypergeometric failure recurrence and b-s+1 coverage condition, and show repeated work, first-goal cost and nonnested reordered-cutoff limits. No author code or benchmark replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 645 native and 442 unchanged generated records. The 830-entry main frontier retains 473 pending and 58 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All five official AAAI1990 pages visually inspected, printed216–220: full abstract, Sections1–6, Equations1–6 and unnumbered expressions, Proposition3.1, Figures1–5 including all table cells, acknowledgments and all four references. Journal1992 full text, author implementation and replication excluded.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T193557Z-iterative-broadening
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Iterative broadening
started_at: '2026-10-13T19:26:53Z'
finished_at: '2026-10-13T19:35:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged per-parent width, finite coverage, nested
    conditioning and the limits of the random-tree performance analysis. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain iterative broadening as a DRAFT native algorithm with a bounded AIO
  no-match assessment. All maintained fields assessed in author self-review; random-tree,
  approximation, finite-coverage and source-version limits remain explicit.
source:
  git_revision: eea7a76cf5e7d42dbe10fc709ec0e8f0da44e76b
  state: working_tree
  inputs:
  - path: data/aio/ComputationalBias.yaml
    sha256: 5a8e7fa4ce6862f3ed08a7389f4f6d746eb90c3d5ee9e54d586f9584ccce4697
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ModelSelectionBias.yaml
    sha256: bda8341c8437cd555e92572580e23bc27363ebc6dff31e2335e62368b003bfa9
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
  - path: data/curated/BULB.yaml
    sha256: daac190f8e4e5c66eb9ed6a4a32eee911fc756b8fc068b47522a34814ae6df50
    role: context
  - path: data/curated/BeamSearch.yaml
    sha256: aec9aab4ec700ecfc6aa4b71c98f33bdbb456d131748729a98480abef34875bc
    role: context
  - path: data/curated/DepthFirstIterativeDeepening.yaml
    sha256: 2e01d2da093397d74a7647e624015b8b0f54d14c7420e00d3ded18a576ce605d
    role: context
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/GlobalFrontierBeamSearch.yaml
    sha256: 9aab298f05ea47fadb17df3bc0cc536ea954777aa47f9ee1e231937c8443ea6b
    role: context
  - path: data/curated/IterativeBroadening.yaml
    sha256: 64a82bfd9daef91902e8f4d1985ea1d727b18a094bb7027d8743ce701b1586e5
    role: target
  - path: research/discovery/20261013T192651Z-iterative-broadening.json
    sha256: b603939164effa0da3a123843fc7053385989520fb737b19debbc6637d77203a
    role: context
  - path: research/discovery/iterative-broadening-boundaries.py
    sha256: 9ea0389140577e3bc9338cd70f00e87c490a5c95f0c6784192f460f2462d80a0
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
- target_id: AIMech:IterativeBroadening
  path: data/curated/IterativeBroadening.yaml
  label: Iterative broadening
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeBroadening.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:IterativeBroadening'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:IterativeBroadening
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: 'All five official AAAI1990 PDF pages visually inspected: Sections1–6,
      Equations1–6, Proposition3.1, Figures1–5, acknowledgments and four references.
      The1992 journal full text, author code and empirical replication are excluded.'
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBroadening
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 246.28s (0:04:06)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 646 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 325 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 318,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBroadening
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
  - AIMech:IterativeBroadening
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
  - AIMech:IterativeBroadening
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/iterative-broadening-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBroadening
  exit_code: 0
  expected_exit_code: 0
  summary: '{"model_failure_depth1": "1/6", "model_failure_depth2": "61/216", "model_success_depth2":
    "155/216", "pigeonhole_cutoff": "b-s+1", "per_parent_width2_depth2_leaf_count":
    4, "binary_width2_already_full": true, "repeated_vs_direct_node_visits": [7, 4],
    "changed_order_breaks_nested_failure": true, "first_goal_cost_vs_minimum": [10,
    1], "scope": "Finite arithmetic and search constructions. Does not certify approximate
    expected-time analysis, infinite-tree completeness, author implementation or benchmark
    speedup."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T192651Z-iterative-broadening.json
  accessed_at: '2026-10-13T19:26:53Z'
  support: supports
  summary: Compared all 442 pinned AIO and 644 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    232, 122, 121 lines. All distinct match contents were inspected. Semantic matching
    covered 72 AIO and 129 native definitions, with every matched definition read.
    9 full annotated AIO node/edge/generated contexts and 5 full native records were
    inspected. Retain repeated depth-first passes with an increasing per-parent successor
    cutoff. A global depth-layer or frontier beam, repeated depth cutoffs and discrepancy-budget
    backtracking restrict different portions of the search tree. The1990 conference
    formulation starts with cutoff2; no alias to every width-adaptive search is asserted.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T19:26:53Z'
  support: supports
  summary: Nine full annotated AIO contexts and five full native neighbors support
    a bounded no-match assessment. Generic learning, classifier-tree, language-model
    and bias-phenomenon classes do not identify this traversal policy.
- evidence_id: ginsberg1990broadening
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1990/AAAI90-033.pdf
  locator: 'All five official AAAI1990 PDF pages visually inspected: Sections1–6,
    Equations1–6, Proposition3.1, Figures1–5, acknowledgments and four references.
    The1992 journal full text, author code and empirical replication are excluded.'
  accessed_at: '2026-10-13T18:35:24Z'
  snapshot_sha256: d671cd081aea5dbf73dc7455dae971aee16df34b350f3aae325d35ad3f02122c
  support: supports
  summary: 'Official AAAI1990 proceedings PDF, five pages, printed216–220. All pages
    visually inspected: Sections1–6, Equations1–6 and unnumbered expressions, Proposition3.1,
    Figures1–5 including table cells, acknowledgments and four references. The later1992
    journal article, author software and replication were not inspected.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/iterative-broadening-boundaries.py
  accessed_at: '2026-10-13T19:27:18Z'
  snapshot_sha256: 9ea0389140577e3bc9338cd70f00e87c490a5c95f0c6784192f460f2462d80a0
  support: supports
  summary: Exact constructions distinguish a per-parent width cap from a global beam,
    verify the special hypergeometric failure recurrence and b-s+1 coverage condition,
    and show repeated work, first-goal cost and nonnested reordered-cutoff limits.
    No author code or benchmark replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Iterative broadening
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - identity
  - ginsberg1990broadening
  summary: Retain this distinct DRAFT algorithm.
  details: Retain repeated depth-first passes with a growing per-parent successor
    cutoff. A global beam, repeated depth limits and discrepancy budgets are different
    controls. The1990 conference method is not assumed identical to the later journal
    formulation.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - mapping
  - ginsberg1990broadening
  summary: The declared AIO mapping is supported.
  details: Nine full annotated AIO contexts and five full native neighbors support
    a bounded no-match assessment. Generic learning, classifier-tree, language-model
    and bias-phenomenon classes do not identify this traversal policy.
- assessment_id: per-parent-breadth-passes
  area: evidence
  topic: per-parent-breadth-passes
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The first pass retains at most two children per parent, not two nodes globally
    per depth. A two-level example retains four leaves. Increasing cutoffs may repeat
    prior work.
- assessment_id: coverage-and-solution-boundaries
  area: evidence
  topic: coverage-and-solution-boundaries
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Finite terminating passes and an eventually sufficient cutoff provide the
    stated coverage conditions. A first-found cost10 goal can precede cost1. No arbitrary
    infinite-branch or minimum-cost guarantee is asserted.
- assessment_id: special-random-tree-model
  area: evidence
  topic: special-random-tree-model
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The hypergeometric recurrence under b4,s2,c2 gives failure1/6 at depth1
    and61/216 at depth2. Those calculations use the specific exactly-s-good-children
    model, not arbitrary random goal placement.
- assessment_id: approximation-and-printed-boundary
  area: evidence
  topic: approximation-and-printed-boundary
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pigeonhole counting gives b-s+1; later b+s-1 prose conflicts with the following
    sum. Conditional failure ratios require nested passes and positive conditioning
    probability. The source explicitly labels its successful-work approximation; no
    general speedup theorem is inferred.
- assessment_id: finite-empirical-boundaries
  area: evidence
  topic: finite-empirical-boundaries
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The configured tree samples and crossword combinations have limited scope.
    Constructed repeated traversal costs7 visits versus4 directly, and binary trees
    are already fully admitted at cutoff2. These are boundary examples, not source
    benchmarks.
- assessment_id: constructed-boundaries
  area: consistency
  topic: per-parent width, finite coverage, nested conditioning and the limits of
    the random-tree performance analysis
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - ginsberg1990broadening
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact constructions distinguish a per-parent width cap from a global beam,
    verify the special hypergeometric failure recurrence and b-s+1 coverage condition,
    and show repeated work, first-goal cost and nonnested reordered-cutoff limits.
    No author code or benchmark replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:IterativeBroadening
  evidence_ids:
  - identity
  - mapping
  - ginsberg1990broadening
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed every maintained field, source version and
    provenance, per-parent versus global width, terminating-pass coverage, first-goal
    cost, the special good-child tree distribution, nested failure conditioning, explicit
    expected-time approximation and finite empirical scope.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 645 native and 442 unchanged generated records.
  The 830-entry main frontier retains 473 pending and 58 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- 'All five official AAAI1990 pages visually inspected, printed216–220: full abstract,
  Sections1–6, Equations1–6 and unnumbered expressions, Proposition3.1, Figures1–5
  including all table cells, acknowledgments and all four references. Journal1992
  full text, author implementation and replication excluded.'
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
