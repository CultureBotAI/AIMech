# Scientific author self-review of Complete balanced largest differencing

- Review: 20261013T085328Z-complete-balanced-largest-differencing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T08:46:23Z
- Finished UTC: 2026-10-13T08:53:28Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain complete balanced largest differencing as a DRAFT algorithm with explicit AIO no-match. Six claims preserve signed-state, general cardinality-target and exact-search boundaries; adversarial author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CompleteBalancedLargestDifferencing
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 957d748fc2041b518126094f3a67806c620acd3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CompleteBalancedLargestDifferencing | data/curated/CompleteBalancedLargestDifferencing.yaml | maintained | Complete balanced largest differencing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CompleteBalancedLargestDifferencing | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 194.05s (0:03:14)<br>Checked 442 record(s); 0 failed.<br>Checked 595 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 254 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 253,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CompleteBalancedLargestDifferencing | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CompleteBalancedLargestDifferencing | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CompleteBalancedLargestDifferencing | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CompleteBalancedLargestDifferencing | {"scope": "Eight fixed integer instances, all valid absolute cardinality targets, one-node interruption and two incompleteness boundaries; not author-code or performance replication.", "tested_targets": 23, "results": [{"values": [8, 7, 6, 5, 4], "residue": 0, "cardinality_difference": 1, "signed_cardinality": 1, "indices": [[4, 2, 3], [0, 1]], "loads": [15, 15], "target": 1, "nodes": 9, "incumbent_history": [2, 0], "certified_for_searched_tree": true}, {"values": [8, 7, 6, 5, 4], "residue": 14, "cardinality_difference": 3, "signed_cardinality": 3, "indices": [[2, 3, 4, 1], [0]], "loads": [22, 8], "target": 3, "nodes": 15, "incumbent_history": [14], "certified_for_searched_tree": true}, {"values": [8, 7, 6, 5, 4], "residue": 30, "cardinality_difference": 5, "signed_cardinality": 5, "indices": [[0, 1, 2, 3, 4], []], "loads": [30, 0], "target": 5, "nodes": 9, "incumbent_history": [30], "certified_for_searched_tree": true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 13, "cardinality_difference": 0, "signed_cardinality": 0, "indices": [[6, 7, 0, 5], [2, 3, 1, 4]], "loads": [353, 340], "target": 0, "nodes": 45, "incumbent_history": [73, 51, 13], "certified_for_searched_tree": true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 7, "cardinality_difference": 2, "signed_cardinality": -2, "indices": [[0, 3, 4], [1, 6, 7, 2, 5]], "loads": [350, 343], "target": 2, "nodes": 47, "incumbent_history": [7], "certified_for_searched_tree": true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 93, "cardinality_difference": 4, "signed_cardinality": 4, "indices": [[6, 7, 4, 5, 2, 3], [0, 1]], "loads": [393, 300], "target": 4, "nodes": 57, "incumbent_history": [113, 93], "certified_for_searched_tree": true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 293, "cardinality_difference": 6, "signed_cardinality": 6, "indices": [[2, 3, 4, 5, 1, 6, 7], [0]], "loads": [493, 200], "target": 6, "nodes": 37, "incumbent_history": [293], "certified_for_searched_tree": true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 693, "cardinality_difference": 8, "signed_cardinality": 8, "indices": [[0, 1, 2, 3, 4, 5, 6, 7], []], "loads": [693, 0], "target": 8, "nodes": 15, "incumbent_history": [693], "certified_for_searched_tree": true}, {"values": [100, 10, 9, 8], "residue": 89, "cardinality_difference": 0, "signed_cardinality": 0, "indices": [[0, 3], [1, 2]], "loads": [108, 19], "target": 0, "nodes": 5, "incumbent_history": [89], "certified_for_searched_tree": true}, {"values": [100, 10, 9, 8], "residue": 73, "cardinality_difference": 2, "signed_cardinality": -2, "indices": [[0], [1, 2, 3]], "loads": [100, 27], "target": 2, "nodes": 7, "incumbent_history": [73], "certified_for_searched_tree": true}, {"values": [100, 10, 9, 8], "residue": 127, "cardinality_difference": 4, "signed_cardinality": 4, "indices": [[0, 1, 2, 3], []], "loads": [127, 0], "target": 4, "nodes": 7, "incumbent_history": [127], "certified_for_searched_tree": true}, {"values": [9, 8, 7, 6, 5, 4, 3], "residue": 0, "cardinality_difference": 1, "signed_cardinality": -1, "indices": [[4, 0, 2], [5, 6, 1, 3]], "loads": [21, 21], "target": 1, "nodes": 0, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values": [9, 8, 7, 6, 5, 4, 3], "residue": 8, "cardinality_difference": 3, "signed_cardinality": 3, "indices": [[4, 5, 2, 3, 6], [0, 1]], "loads": [25, 17], "target": 3, "nodes": 35, "incumbent_history": [10, 8], "certified_for_searched_tree": true}, {"values": [9, 8, 7, 6, 5, 4, 3], "residue": 24, "cardinality_difference": 5, "signed_cardinality": 5, "indices": [[2, 3, 4, 5, 6, 1], [0]], "loads": [33, 9], "target": 5, "nodes": 29, "incumbent_history": [24], "certified_for_searched_tree": true}, {"values": [9, 8, 7, 6, 5, 4, 3], "residue": 42, "cardinality_difference": 7, "signed_cardinality": 7, "indices": [[0, 1, 2, 3, 4, 5, 6], []], "loads": [42, 0], "target": 7, "nodes": 13, "incumbent_history": [42], "certified_for_searched_tree": true}, {"values": [5, 5, 5, 5], "residue": 0, "cardinality_difference": 0, "signed_cardinality": 0, "indices": [[0, 3], [1, 2]], "loads": [10, 10], "target": 0, "nodes": 0, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values": [5, 5, 5, 5], "residue": 10, "cardinality_difference": 2, "signed_cardinality": 2, "indices": [[2, 3, 1], [0]], "loads": [15, 5], "target": 2, "nodes": 11, "incumbent_history": [10], "certified_for_searched_tree": true}, {"values": [5, 5, 5, 5], "residue": 20, "cardinality_difference": 4, "signed_cardinality": 4, "indices": [[0, 1, 2, 3], []], "loads": [20, 0], "target": 4, "nodes": 7, "incumbent_history": [20], "certified_for_searched_tree": true}, {"values": [0, 0, 0], "residue": 0, "cardinality_difference": 1, "signed_cardinality": -1, "indices": [[0], [1, 2]], "loads": [0, 0], "target": 1, "nodes": 0, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values": [0, 0, 0], "residue": 0, "cardinality_difference": 3, "signed_cardinality": 3, "indices": [[2, 0, 1], []], "loads": [0, 0], "target": 3, "nodes": 5, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values": [9], "residue": 9, "cardinality_difference": 1, "signed_cardinality": 1, "indices": [[0], []], "loads": [9, 0], "target": 1, "nodes": 1, "incumbent_history": [9], "certified_for_searched_tree": true}, {"values": [7, 7], "residue": 0, "cardinality_difference": 0, "signed_cardinality": 0, "indices": [[0], [1]], "loads": [7, 7], "target": 0, "nodes": 0, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values": [7, 7], "residue": 14, "cardinality_difference": 2, "signed_cardinality": 2, "indices": [[0, 1], []], "loads": [14, 0], "target": 2, "nodes": 3, "incumbent_history": [14], "certified_for_searched_tree": true}], "interrupted": {"residue": 2, "cardinality_difference": 1, "signed_cardinality": 1, "indices": [[4, 1, 3], [0, 2]], "loads": [16, 14], "target": 1, "nodes": 1, "incumbent_history": [2], "certified_for_searched_tree": false}, "restricted_initial_pairs": {"best_residue": 2, "global_balanced_optimum": 0}, "necessary_only_cardinality_bound": {"magnitudes": [2, 2, 2], "target": 0, "lower": 0, "upper": 6, "attainable": [2, 6]}} |

## Scientific And Domain Assessments

### Complete balanced largest differencing

identity: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Retain this distinct DRAFT algorithm.

The named Complete BLDM pseudocode handles feasible absolute cardinality targets. Its balanced first solution is BLDM, but the complete tree must include same-side initial pair choices. This differs from unconstrained CKK and the BLDM heuristic.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Explicit no-match assessment is supported.

All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence.

### signed-residual-state

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Equation8 combines signed counts by subtraction or addition with the same orientation as residual groups. Exact indexed fixtures check both identities at every visited state; zero load residuals preserve counts and memberships.

### two-phase-complete-branching

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Figure2 delays resorting until the list has at most ceil(n/2) entries, so initial decisions pair original neighbors. Both difference and sum remain branches. Restricting initial pairs gives residue2 instead of the full optimum0 on the five-weight counterexample.

### necessary-cardinality-bounds

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Equation9 is a necessary signed-sum interval. Clamping its lower bound at zero and checking root parity are direct deductions. Magnitudes2,2,2 have interval [0,6] but attainable absolute totals only2 and6, disproving sufficiency even when parity matches.

### load-bound-and-incumbent

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

The unconstrained residual bound remains a lower bound for the constrained subset of completions. Only valid target-count leaves update the incumbent. The calculation seeds BLDM only for balanced targets and uses exact integer arithmetic.

### anytime-and-complete-scope

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

All23 valid targets on eight fixtures agree with independent exhaustive subsets. A one-node balanced interruption retains residue2 without certification. The source’s first BLDM solution applies only to balanced targets; other targets need a valid leaf. Worst-case exponential scope remains.

### reported-experiments

evidence: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

The 25-bit experiment averages100 trials per point; Figure5 uses100-item150-bit instances and heterogeneous improvement across runs. Historical runtime and finite-precision effects remain explicit. Broad twelve-digit claims and a literal probability-one impossibility are not adopted.

### signed counts, complete initial branching, necessary-only cardinality pruning and constrained incumbent certification

consistency: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Constructed calculations support the stated distinctions.

Eight fixed integer instances cover all23 valid absolute cardinality targets and agree with independent exhaustive assignments. One-node interruption preserves an uncertified balanced residue2; fixing initial pairs yields2 while the full balanced optimum is0. Magnitudes2,2,2 admit target0 through interval bounds but only signed absolute sums2 or6 are attainable. No author-code or empirical replication.

### All maintained fields

provenance: supported. Targets: AIMech:CompleteBalancedLargestDifferencing.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read all maintained fields and six AIO target YAMLs after capture. Reread signed effective-cardinality state, both phases of difference/sum branching, necessary cardinality bounds, incumbent pruning and the complete-versus-interrupted evaluation. Checked all 23 feasible targets across eight small indexed instances.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T084516Z-complete-balanced-largest-differencing.json | supports | Compared all 442 pinned AIO and 594 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 39, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 67 AIO and 101 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Complete BLDM is the named Mertens two-phase search with signed effective-cardinality state and pruning. It explores same-side alternatives to initial adjacent pairs as well as later largest-residual pairs. Balanced targets obtain the BLDM first solution; the same source pseudocode handles other feasible absolute cardinality targets. This is distinct from the BLDM heuristic, PDM and unconstrained CKK. The pending lead and neighboring mentions are not prior maintained identities. |
| mapping | sources/aio/aio.json | supports | All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence. |
| mertens1999 | https://arxiv.org/pdf/cs/9903011v1; All 12 Mertens preprint pages read before curation, selected method and evaluation pages reread after capture. No later journal text, author implementation, empirical replication or unrestricted correctness certification. | supports | All 12 pages of the arXiv cs/9903011v1 PDF read. The margin and primary abstract identify submission on 11 March 1999; the downloaded PDF footer says 26 November 2024. The footer is not treated as the original publication date. Locators are PDF/printed pages 1–12; no later journal version or author implementation inspected. |
| calculation | research/discovery/complete-balanced-largest-differencing-boundaries.py | supports | Eight fixed integer instances cover all23 valid absolute cardinality targets and agree with independent exhaustive assignments. One-node interruption preserves an uncertified balanced residue2; fixing initial pairs yields2 while the full balanced optimum is0. Magnitudes2,2,2 admit target0 through interval bounds but only signed absolute sums2 or6 are attainable. No author-code or empirical replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 595 native and 442 unchanged generated records. The 779-entry main frontier retains 480 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 12 Mertens preprint pages visually read, including pseudocode, five figures, experiment details and references. Yakir primary metadata and abstract were inspected, but the public publisher PDF returned HTTP403; full proof and author implementations were not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T085328Z-complete-balanced-largest-differencing
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Complete balanced largest differencing
started_at: '2026-10-13T08:46:23Z'
finished_at: '2026-10-13T08:53:28Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged signed counts, complete initial branching,
    necessary-only cardinality pruning and constrained incumbent certification. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain complete balanced largest differencing as a DRAFT algorithm with explicit
  AIO no-match. Six claims preserve signed-state, general cardinality-target and exact-search
  boundaries; adversarial author self-review found no actionable defect.
source:
  git_revision: 957d748fc2041b518126094f3a67806c620acd3b
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
  - path: data/curated/BalancedLargestDifferencing.yaml
    sha256: 06a914d365f65b2d26a4d9103a22f7f282441fa6478769e83986e352c2b5f607
    role: context
  - path: data/curated/CompleteBalancedLargestDifferencing.yaml
    sha256: 1269b1c5ae0952a8c1b5705db683a5625b03c10f17410836e5797e4415f3e46d
    role: target
  - path: data/curated/CompleteKarmarkarKarp.yaml
    sha256: 65431bae97ba1ebb9e38b2a17a9b59fcc156087167173faf88308b5f38fddcca
    role: context
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/PairedDifferencing.yaml
    sha256: cf97c997c3654cf14d15b791faa92658e38b98a07751735e92f1de06aed035c0
    role: context
  - path: research/discovery/20261013T084516Z-complete-balanced-largest-differencing.json
    sha256: d05c20e624d353618616caafeb0986fd31380b9cc16ae3e776744577226100b5
    role: context
  - path: research/discovery/complete-balanced-largest-differencing-boundaries.py
    sha256: 4b6873709ace8df6724bc93663b27b5f86a37505506772d533776f3523e9d32b
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
- target_id: AIMech:CompleteBalancedLargestDifferencing
  path: data/curated/CompleteBalancedLargestDifferencing.yaml
  label: Complete balanced largest differencing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CompleteBalancedLargestDifferencing.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CompleteBalancedLargestDifferencing'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All 12 Mertens preprint pages read before curation, selected method and
      evaluation pages reread after capture. No later journal text, author implementation,
      empirical replication or unrestricted correctness certification.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 194.05s (0:03:14)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 595 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 254 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 253,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
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
  - AIMech:CompleteBalancedLargestDifferencing
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
  - AIMech:CompleteBalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/complete-balanced-largest-differencing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Eight fixed integer instances, all valid absolute cardinality
    targets, one-node interruption and two incompleteness boundaries; not author-code
    or performance replication.", "tested_targets": 23, "results": [{"values": [8,
    7, 6, 5, 4], "residue": 0, "cardinality_difference": 1, "signed_cardinality":
    1, "indices": [[4, 2, 3], [0, 1]], "loads": [15, 15], "target": 1, "nodes": 9,
    "incumbent_history": [2, 0], "certified_for_searched_tree": true}, {"values":
    [8, 7, 6, 5, 4], "residue": 14, "cardinality_difference": 3, "signed_cardinality":
    3, "indices": [[2, 3, 4, 1], [0]], "loads": [22, 8], "target": 3, "nodes": 15,
    "incumbent_history": [14], "certified_for_searched_tree": true}, {"values": [8,
    7, 6, 5, 4], "residue": 30, "cardinality_difference": 5, "signed_cardinality":
    5, "indices": [[0, 1, 2, 3, 4], []], "loads": [30, 0], "target": 5, "nodes": 9,
    "incumbent_history": [30], "certified_for_searched_tree": true}, {"values": [200,
    100, 90, 80, 70, 61, 50, 42], "residue": 13, "cardinality_difference": 0, "signed_cardinality":
    0, "indices": [[6, 7, 0, 5], [2, 3, 1, 4]], "loads": [353, 340], "target": 0,
    "nodes": 45, "incumbent_history": [73, 51, 13], "certified_for_searched_tree":
    true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 7, "cardinality_difference":
    2, "signed_cardinality": -2, "indices": [[0, 3, 4], [1, 6, 7, 2, 5]], "loads":
    [350, 343], "target": 2, "nodes": 47, "incumbent_history": [7], "certified_for_searched_tree":
    true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 93, "cardinality_difference":
    4, "signed_cardinality": 4, "indices": [[6, 7, 4, 5, 2, 3], [0, 1]], "loads":
    [393, 300], "target": 4, "nodes": 57, "incumbent_history": [113, 93], "certified_for_searched_tree":
    true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 293, "cardinality_difference":
    6, "signed_cardinality": 6, "indices": [[2, 3, 4, 5, 1, 6, 7], [0]], "loads":
    [493, 200], "target": 6, "nodes": 37, "incumbent_history": [293], "certified_for_searched_tree":
    true}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "residue": 693, "cardinality_difference":
    8, "signed_cardinality": 8, "indices": [[0, 1, 2, 3, 4, 5, 6, 7], []], "loads":
    [693, 0], "target": 8, "nodes": 15, "incumbent_history": [693], "certified_for_searched_tree":
    true}, {"values": [100, 10, 9, 8], "residue": 89, "cardinality_difference": 0,
    "signed_cardinality": 0, "indices": [[0, 3], [1, 2]], "loads": [108, 19], "target":
    0, "nodes": 5, "incumbent_history": [89], "certified_for_searched_tree": true},
    {"values": [100, 10, 9, 8], "residue": 73, "cardinality_difference": 2, "signed_cardinality":
    -2, "indices": [[0], [1, 2, 3]], "loads": [100, 27], "target": 2, "nodes": 7,
    "incumbent_history": [73], "certified_for_searched_tree": true}, {"values": [100,
    10, 9, 8], "residue": 127, "cardinality_difference": 4, "signed_cardinality":
    4, "indices": [[0, 1, 2, 3], []], "loads": [127, 0], "target": 4, "nodes": 7,
    "incumbent_history": [127], "certified_for_searched_tree": true}, {"values": [9,
    8, 7, 6, 5, 4, 3], "residue": 0, "cardinality_difference": 1, "signed_cardinality":
    -1, "indices": [[4, 0, 2], [5, 6, 1, 3]], "loads": [21, 21], "target": 1, "nodes":
    0, "incumbent_history": [0], "certified_for_searched_tree": true}, {"values":
    [9, 8, 7, 6, 5, 4, 3], "residue": 8, "cardinality_difference": 3, "signed_cardinality":
    3, "indices": [[4, 5, 2, 3, 6], [0, 1]], "loads": [25, 17], "target": 3, "nodes":
    35, "incumbent_history": [10, 8], "certified_for_searched_tree": true}, {"values":
    [9, 8, 7, 6, 5, 4, 3], "residue": 24, "cardinality_difference": 5, "signed_cardinality":
    5, "indices": [[2, 3, 4, 5, 6, 1], [0]], "loads": [33, 9], "target": 5, "nodes":
    29, "incumbent_history": [24], "certified_for_searched_tree": true}, {"values":
    [9, 8, 7, 6, 5, 4, 3], "residue": 42, "cardinality_difference": 7, "signed_cardinality":
    7, "indices": [[0, 1, 2, 3, 4, 5, 6], []], "loads": [42, 0], "target": 7, "nodes":
    13, "incumbent_history": [42], "certified_for_searched_tree": true}, {"values":
    [5, 5, 5, 5], "residue": 0, "cardinality_difference": 0, "signed_cardinality":
    0, "indices": [[0, 3], [1, 2]], "loads": [10, 10], "target": 0, "nodes": 0, "incumbent_history":
    [0], "certified_for_searched_tree": true}, {"values": [5, 5, 5, 5], "residue":
    10, "cardinality_difference": 2, "signed_cardinality": 2, "indices": [[2, 3, 1],
    [0]], "loads": [15, 5], "target": 2, "nodes": 11, "incumbent_history": [10], "certified_for_searched_tree":
    true}, {"values": [5, 5, 5, 5], "residue": 20, "cardinality_difference": 4, "signed_cardinality":
    4, "indices": [[0, 1, 2, 3], []], "loads": [20, 0], "target": 4, "nodes": 7, "incumbent_history":
    [20], "certified_for_searched_tree": true}, {"values": [0, 0, 0], "residue": 0,
    "cardinality_difference": 1, "signed_cardinality": -1, "indices": [[0], [1, 2]],
    "loads": [0, 0], "target": 1, "nodes": 0, "incumbent_history": [0], "certified_for_searched_tree":
    true}, {"values": [0, 0, 0], "residue": 0, "cardinality_difference": 3, "signed_cardinality":
    3, "indices": [[2, 0, 1], []], "loads": [0, 0], "target": 3, "nodes": 5, "incumbent_history":
    [0], "certified_for_searched_tree": true}, {"values": [9], "residue": 9, "cardinality_difference":
    1, "signed_cardinality": 1, "indices": [[0], []], "loads": [9, 0], "target": 1,
    "nodes": 1, "incumbent_history": [9], "certified_for_searched_tree": true}, {"values":
    [7, 7], "residue": 0, "cardinality_difference": 0, "signed_cardinality": 0, "indices":
    [[0], [1]], "loads": [7, 7], "target": 0, "nodes": 0, "incumbent_history": [0],
    "certified_for_searched_tree": true}, {"values": [7, 7], "residue": 14, "cardinality_difference":
    2, "signed_cardinality": 2, "indices": [[0, 1], []], "loads": [14, 0], "target":
    2, "nodes": 3, "incumbent_history": [14], "certified_for_searched_tree": true}],
    "interrupted": {"residue": 2, "cardinality_difference": 1, "signed_cardinality":
    1, "indices": [[4, 1, 3], [0, 2]], "loads": [16, 14], "target": 1, "nodes": 1,
    "incumbent_history": [2], "certified_for_searched_tree": false}, "restricted_initial_pairs":
    {"best_residue": 2, "global_balanced_optimum": 0}, "necessary_only_cardinality_bound":
    {"magnitudes": [2, 2, 2], "target": 0, "lower": 0, "upper": 6, "attainable": [2,
    6]}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T084516Z-complete-balanced-largest-differencing.json
  accessed_at: '2026-10-13T08:46:23Z'
  support: supports
  summary: Compared all 442 pinned AIO and 594 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    39, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 67 AIO and 101 native definitions, with every matched definition read.
    6 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. Complete BLDM is the named Mertens two-phase search with signed effective-cardinality
    state and pruning. It explores same-side alternatives to initial adjacent pairs
    as well as later largest-residual pairs. Balanced targets obtain the BLDM first
    solution; the same source pseudocode handles other feasible absolute cardinality
    targets. This is distinct from the BLDM heuristic, PDM and unconstrained CKK.
    The pending lead and neighboring mentions are not prior maintained identities.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T08:46:23Z'
  support: supports
  summary: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- evidence_id: mertens1999
  kind: primary_source
  reference: https://arxiv.org/pdf/cs/9903011v1
  locator: All 12 Mertens preprint pages read before curation, selected method and
    evaluation pages reread after capture. No later journal text, author implementation,
    empirical replication or unrestricted correctness certification.
  accessed_at: '2026-10-13T08:05:53Z'
  snapshot_sha256: fe0bcf132782ff8d59c7888b6ea0a7aae195bc3df69dddc728cc842a8258ecd3
  support: supports
  summary: All 12 pages of the arXiv cs/9903011v1 PDF read. The margin and primary
    abstract identify submission on 11 March 1999; the downloaded PDF footer says
    26 November 2024. The footer is not treated as the original publication date.
    Locators are PDF/printed pages 1–12; no later journal version or author implementation
    inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/complete-balanced-largest-differencing-boundaries.py
  accessed_at: '2026-10-13T08:47:02Z'
  snapshot_sha256: 4b6873709ace8df6724bc93663b27b5f86a37505506772d533776f3523e9d32b
  support: supports
  summary: Eight fixed integer instances cover all23 valid absolute cardinality targets
    and agree with independent exhaustive assignments. One-node interruption preserves
    an uncertified balanced residue2; fixing initial pairs yields2 while the full
    balanced optimum is0. Magnitudes2,2,2 admit target0 through interval bounds but
    only signed absolute sums2 or6 are attainable. No author-code or empirical replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Complete balanced largest differencing
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - identity
  - mertens1999
  summary: Retain this distinct DRAFT algorithm.
  details: The named Complete BLDM pseudocode handles feasible absolute cardinality
    targets. Its balanced first solution is BLDM, but the complete tree must include
    same-side initial pair choices. This differs from unconstrained CKK and the BLDM
    heuristic.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mapping
  - mertens1999
  summary: Explicit no-match assessment is supported.
  details: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- assessment_id: signed-residual-state
  area: evidence
  topic: signed-residual-state
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation8 combines signed counts by subtraction or addition with the same
    orientation as residual groups. Exact indexed fixtures check both identities at
    every visited state; zero load residuals preserve counts and memberships.
- assessment_id: two-phase-complete-branching
  area: evidence
  topic: two-phase-complete-branching
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure2 delays resorting until the list has at most ceil(n/2) entries,
    so initial decisions pair original neighbors. Both difference and sum remain branches.
    Restricting initial pairs gives residue2 instead of the full optimum0 on the five-weight
    counterexample.
- assessment_id: necessary-cardinality-bounds
  area: evidence
  topic: necessary-cardinality-bounds
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation9 is a necessary signed-sum interval. Clamping its lower bound
    at zero and checking root parity are direct deductions. Magnitudes2,2,2 have interval
    [0,6] but attainable absolute totals only2 and6, disproving sufficiency even when
    parity matches.
- assessment_id: load-bound-and-incumbent
  area: evidence
  topic: load-bound-and-incumbent
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The unconstrained residual bound remains a lower bound for the constrained
    subset of completions. Only valid target-count leaves update the incumbent. The
    calculation seeds BLDM only for balanced targets and uses exact integer arithmetic.
- assessment_id: anytime-and-complete-scope
  area: evidence
  topic: anytime-and-complete-scope
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: All23 valid targets on eight fixtures agree with independent exhaustive
    subsets. A one-node balanced interruption retains residue2 without certification.
    The source’s first BLDM solution applies only to balanced targets; other targets
    need a valid leaf. Worst-case exponential scope remains.
- assessment_id: reported-experiments
  area: evidence
  topic: reported-experiments
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: The 25-bit experiment averages100 trials per point; Figure5 uses100-item150-bit
    instances and heterogeneous improvement across runs. Historical runtime and finite-precision
    effects remain explicit. Broad twelve-digit claims and a literal probability-one
    impossibility are not adopted.
- assessment_id: constructed-boundaries
  area: consistency
  topic: signed counts, complete initial branching, necessary-only cardinality pruning
    and constrained incumbent certification
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Eight fixed integer instances cover all23 valid absolute cardinality targets
    and agree with independent exhaustive assignments. One-node interruption preserves
    an uncertified balanced residue2; fixing initial pairs yields2 while the full
    balanced optimum is0. Magnitudes2,2,2 admit target0 through interval bounds but
    only signed absolute sums2 or6 are attainable. No author-code or empirical replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CompleteBalancedLargestDifferencing
  evidence_ids:
  - identity
  - mapping
  - mertens1999
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read all maintained fields and six AIO target YAMLs
    after capture. Reread signed effective-cardinality state, both phases of difference/sum
    branching, necessary cardinality bounds, incumbent pruning and the complete-versus-interrupted
    evaluation. Checked all 23 feasible targets across eight small indexed instances.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 595 native and 442 unchanged generated records.
  The 779-entry main frontier retains 480 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All 12 Mertens preprint pages visually read, including pseudocode, five figures,
  experiment details and references. Yakir primary metadata and abstract were inspected,
  but the public publisher PDF returned HTTP403; full proof and author implementations
  were not inspected.
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
