# Scientific author self-review of PERCH clustering

- Review: 20261013T231450Z-perch-clustering
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T23:09:32Z
- Finished UTC: 2026-10-13T23:14:50Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full author self-review retains PERCH as DRAFT and resolves the citation-locator finding after correcting and rereading the maintained record and source references. No unresolved finding remains in this record scope.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:PERCHClustering
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8c64bd062bfba0e5871a36a00066961b8d343d6a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PERCHClustering | data/curated/PERCHClustering.yaml | maintained | PERCH clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PERCHClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 159.42s (0:02:39)<br>Checked 442 record(s); 0 failed.<br>Checked 658 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 340 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 337,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PERCHClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:PERCHClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PERCHClustering | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:PERCHClustering | {"cached_min": {"left": [[0], [5], [10]], "right": [[4], [6]], "reported_squared": 16, "actual_squared": 1}, "cached_max": {"left": [[0, 1], [1, 0]], "right": [[10, -10]], "reported_squared": 202, "actual_squared": 221}, "pruning_units": {"points": ["0", "10"], "sse": "50", "paper_diagonal_times_count": "20", "python_half_child_distance_times_count": "10"}, "limits": "These are standalone evaluations of inspected scalar expressions for explicit point sets. They do not execute PERCH, construct an insertion history, establish reachability, or measure dendrogram purity or runtime."} |
| Corrected citation and predecessor-lineage verification | passed | True | AIMech:PERCHClustering | Verified exact corrected locators, the persisted same-key predecessor, all affected target IDs and absence of another same-key head in an ignored/hidden-inclusive bundle traversal. |

## Scientific And Domain Assessments

### PERCH clustering

identity: supported. Targets: AIMech:PERCHClustering.

Retain this distinct DRAFT algorithm.

Retain online nearest-leaf insertion with masking and balance rotations, distinct from BIRCH feature compression, CURE representatives, linkage chains, RS pointer-tree pruning and Genie inequality-triggered merging.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:PERCHClustering.

The declared AIO mapping is supported.

Related hierarchical and unsupervised clustering tasks are supported without algorithm/task equivalence. Nine annotated AIO contexts and five native records distinguish the method from classification, metric learning and scalar distance functions.

### online-insertion-and-rotation

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

The primary insertion algorithm and PNode split/rotate methods support a binary tree with revisable subtree placement. The masking definition distinguishes existence of a violating distance comparison from globally nearest cluster-pair merging.

### conditional-purity-theory

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

Theorem1 assumes strict separation and exact intended conditions; the record does not transfer its purity-one guarantee to arbitrary data, approximate beam search, arbitrary caps or every summary implementation.

### balancing-and-search

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

Balance rotations require a size-ratio improvement and geometric compatibility. Exact and finite-beam search differ. The paper acknowledges quadratic worst-case total work; no universal logarithmic height or insertion bound is asserted.

### implementation-boundary-of-geometric-summaries

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

The complete Python min/max cached expressions and explicit curator point sets give squared lower16 versus actual1 and squared upper202 versus actual221. These refute unrestricted scalar-bound readings, without a claimed reachable full execution or purity failure.

### collapsed-mode-and-storage

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

The paper Fact4 additionally assumes L&gt;K and strict separation. Original point IDs remain. PNode.collapse retains original leaf objects and feature arrays, so feature deletion and constant total memory are not assigned to the inspected implementation.

### flat-extraction-and-pruning-cost

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

For0,10, exact mean SSE50 exceeds both paper linear-distance count20 and Python heuristic10. The Scala entrypoint timing ends before pruning and serialization. No SSE-optimal pruning or full pipeline runtime is inferred.

### reported-evaluation

evidence: supported. Targets: AIMech:PERCHClustering.

Supported within the stated primary-source and mathematical scope.

The record separates dendrogram purity from pairwise F1, random arrival repetitions, selected hyperparameters, known-K pruning and source-specific beam/collapse/thread settings. Missing result marks and log-normalized time are qualified; no universal ranking is asserted.

### PERCH identity, conditional purity, masking and balance rotations, geometric-summary and squared-error boundaries, collapse storage and evaluation scope

consistency: supported. Targets: AIMech:PERCHClustering.

Constructed calculations support the stated distinctions.

Standalone expressions yield cached squared lower16 versus actual1, and cached squared upper202 versus actual221. On points0,10 the paper linear-distance cost20 and Python heuristic10 are below squared error50. These checks do not execute PERCH or establish a reachable purity failure.

### All maintained fields

provenance: supported. Targets: AIMech:PERCHClustering.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed every final maintained field and all seven claims against the complete initial scientific reading. Only four paper locator strings and the actual updated_at changed. Visually verified Assumption1/Section3.1, Theorem1/Section3.3, Fact4/Section4.2 and Algorithm1/p.8 after the corrective capture. Retained implementation, theory and evaluation boundaries. DRAFT remains.

### Paper section, result and page locators

evidence: supported. Targets: AIMech:PERCHClustering.

Corrected citations now agree with the inspected primary paper.

## Findings

### paper-locators: Correct PERCH paper section and result locators

minor / resolved / confirmed; issue key: aimech-perch-citation-locators.

The initial record located separability/Theorem1 in Section4 and collapse in Section5/Theorem2. In the inspected v1, those are Sections3.1/3.3 and Section4.2/Fact4. The insertion/definition locators also need to identify Algorithm1 on PDF p.8 explicitly.

Disposition: The corrected maintained citations were compared with the visually reread paper: sections, page numbers, Theorem1 and Fact4 now agree. The report mirror and history agree with the final bytes. Required gates passed. The sole same-key predecessor was explicitly resolved with the same affected target; ignored/hidden bundles were included in the lineage scan.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T230139Z-perch-clustering.json | supports | Compared all 442 pinned AIO and 657 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 18, 0, 0 lines. All distinct match contents were read, including pending discovery entries and source-reading observations. Recovery hits concern pending PERCH discovery notes and primary-source context; none identifies an existing standalone PERCH record. Both other checkouts returned no matches including ignored and hidden files. Semantic matching covered 26 AIO and 174 native definitions, all read; unchanged definitions were byte-compared with the preceding full assessment. 9 full annotated AIO node/edge/generated contexts and 5 full native records were inspected. Retain online nearest-leaf insertion with masking and balance rotations. It differs from immutable linkage chains, BIRCH feature compression, CURE representatives, RS pruning and Genie inequality-based merging. PERCH-C/B/BC name modes with additional assumptions, not unconditional exact-theory aliases. |
| mapping | sources/aio/aio.json | supports | Related hierarchical and unsupervised clustering tasks are supported without algorithm/task equivalence. Nine annotated AIO contexts and five native records distinguish the method from classification, metric learning and scalar distance functions. |
| perch2017 | https://arxiv.org/pdf/1704.01858v1; Sections3–5, PDF pp.3–9; Algorithm1, p.8; Sections3.2–3.3, masking definition and rotations, PDF pp.4–5; Algorithm1, p.8; Section3.1, Assumption1, PDF p.4; Section3.3, Theorem1 and proof, pp.5–6; Sections4–5, pp.6–9; Section4, balance rotations; Sections5–6.4; Section4.2, collapsed mode and Fact4, PDF p.7; Section6.3, extracting flat clusterings; Section6, Figures3–5 and experimental settings | supports | arXiv1704.01858v1,6April2017;PDF dated7April2017. All20 pages visually read. Conference typeset version not compared. |
| perch-python | https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/python/xcluster/models/PNode.py; PNode._split_down, _rotate and recursive_rotate_if_masked; PNode.recursive_rotate_if_unbalanced, can_rotate_for_balance, a_star_exact and a_star_beam; PNode._update_children_min_d, _update_children_max_d, min_distance and max_distance; PNode.collapse, leaves and true_leaves | supports | Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019. Complete cited file statically read, not executed; not asserted identical to the2017 benchmark implementation. |
| perch-pruning | https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/python/xcluster/models/pruning_heuristics.py; pick_k_approx_km_cost | supports | Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019. Complete cited file statically read, not executed; not asserted identical to the2017 benchmark implementation. |
| perch-entry | https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/scala/xcluster/eval/RunPerch.scala; RunPerch.main, start/end timing and subsequent serialization/extraction | supports | Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019. Complete cited file statically read, not executed; not asserted identical to the2017 benchmark implementation. |
| calculation | research/discovery/perch-geometric-boundaries.py | supports | Standalone expressions yield cached squared lower16 versus actual1, and cached squared upper202 versus actual221. On points0,10 the paper linear-distance cost20 and Python heuristic10 are below squared error50. These checks do not execute PERCH or establish a reachable purity failure. |
| locator-recheck | https://arxiv.org/pdf/1704.01858v1; PDF pp.4–6: Assumption1 and Theorem1 in Sections3.1/3.3; p.7: Section4.2 Fact4; p.8: Algorithm1; p.9: Section5. | supports | Visually rechecked the actual versioned paper headings, named results and displayed algorithm against the maintained citations. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 658 native and 442 unchanged generated records. The 843-entry main frontier retains 473 pending and 58 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All20 paper pages and complete cited Python core, pruning utilities and Scala entrypoint read. Other Scala core remains only partially inspected. No author program execution.
- No author-code execution, training, paid service, hardware measurement or empirical replication. The complete cited primary and implementation sources were read; historical experiments and floating-point behavior were not reproduced. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T231450Z-perch-clustering
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of PERCH clustering
started_at: '2026-10-13T23:09:32Z'
finished_at: '2026-10-13T23:14:50Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged PERCH identity, conditional purity, masking
    and balance rotations, geometric-summary and squared-error boundaries, collapse
    storage and evaluation scope. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/aimech-resolve-reviews/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Full author self-review retains PERCH as DRAFT and resolves the citation-locator
  finding after correcting and rereading the maintained record and source references.
  No unresolved finding remains in this record scope.
source:
  git_revision: 8c64bd062bfba0e5871a36a00066961b8d343d6a
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/BIRCH.yaml
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    role: context
  - path: data/curated/CUREClustering.yaml
    sha256: ab437b2bd33b77ed821e8695bc15ba90de4fc216d4cafff09da7e48060d42cba
    role: context
  - path: data/curated/GenieClustering.yaml
    sha256: 4bd69f9d4dbf5be9e97c4a5f8bba9d674fab7e240f1d49abc017e4d04dd58181
    role: context
  - path: data/curated/NearestNeighborChainClustering.yaml
    sha256: 29edd6535409cbf8a1fb3c806de4d52f0f33473d597439c40af4c895fa49746a
    role: context
  - path: data/curated/PERCHClustering.yaml
    sha256: 11f440fe63b081583796d7420e44685aa50726223deb9ae50e8f702afe614bb1
    role: target
  - path: data/curated/ReciprocalNearestNeighborsSupportedClustering.yaml
    sha256: e3bc2d88143b46989b642e695be1c94d11d090c67606f91c970bd1c4ece47738
    role: context
  - path: research/discovery/20261013T230139Z-perch-clustering.json
    sha256: ad79f01cba828f946c667646844e736b620719264f12a2be11e1aaf46f1cee35
    role: context
  - path: research/discovery/perch-geometric-boundaries.py
    sha256: cbe8237e11da752cf7c07fbaea83e670e51925789aff27c7b6925469829f64f8
    role: context
  - path: reviews/structured/20261013T230801Z-perch-clustering/review.yaml
    sha256: ff679742113cce894d474ea16fa73c1b6449a63e4e78545923aa5c2b9cecd177
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
- target_id: AIMech:PERCHClustering
  path: data/curated/PERCHClustering.yaml
  label: PERCH clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PERCHClustering.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:PERCHClustering'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PERCHClustering
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All20 primary pages and complete cited files read. Complete Scala core,
      other source revisions and numerical/empirical behavior were not audited. No
      author code execution, full reachable counterexample, benchmark or training.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PERCHClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 159.42s (0:02:39)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 658 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 340 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 337,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PERCHClustering
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
  - AIMech:PERCHClustering
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
  - AIMech:PERCHClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/perch-geometric-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PERCHClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"cached_min": {"left": [[0], [5], [10]], "right": [[4], [6]], "reported_squared":
    16, "actual_squared": 1}, "cached_max": {"left": [[0, 1], [1, 0]], "right": [[10,
    -10]], "reported_squared": 202, "actual_squared": 221}, "pruning_units": {"points":
    ["0", "10"], "sse": "50", "paper_diagonal_times_count": "20", "python_half_child_distance_times_count":
    "10"}, "limits": "These are standalone evaluations of inspected scalar expressions
    for explicit point sets. They do not execute PERCH, construct an insertion history,
    establish reachability, or measure dendrogram purity or runtime."}'
- check_id: locator-lineage
  name: Corrected citation and predecessor-lineage verification
  command: python3 /private/tmp/aimech-review-batch265.py 265 --resolve-locator-finding
  status: passed
  required: true
  target_ids:
  - AIMech:PERCHClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Verified exact corrected locators, the persisted same-key predecessor,
    all affected target IDs and absence of another same-key head in an ignored/hidden-inclusive
    bundle traversal.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T230139Z-perch-clustering.json
  accessed_at: '2026-10-13T23:09:32Z'
  support: supports
  summary: Compared all 442 pinned AIO and 657 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    18, 0, 0 lines. All distinct match contents were read, including pending discovery
    entries and source-reading observations. Recovery hits concern pending PERCH discovery
    notes and primary-source context; none identifies an existing standalone PERCH
    record. Both other checkouts returned no matches including ignored and hidden
    files. Semantic matching covered 26 AIO and 174 native definitions, all read;
    unchanged definitions were byte-compared with the preceding full assessment. 9
    full annotated AIO node/edge/generated contexts and 5 full native records were
    inspected. Retain online nearest-leaf insertion with masking and balance rotations.
    It differs from immutable linkage chains, BIRCH feature compression, CURE representatives,
    RS pruning and Genie inequality-based merging. PERCH-C/B/BC name modes with additional
    assumptions, not unconditional exact-theory aliases.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T23:09:32Z'
  support: supports
  summary: Related hierarchical and unsupervised clustering tasks are supported without
    algorithm/task equivalence. Nine annotated AIO contexts and five native records
    distinguish the method from classification, metric learning and scalar distance
    functions.
- evidence_id: perch2017
  kind: primary_source
  reference: https://arxiv.org/pdf/1704.01858v1
  locator: Sections3–5, PDF pp.3–9; Algorithm1, p.8; Sections3.2–3.3, masking definition
    and rotations, PDF pp.4–5; Algorithm1, p.8; Section3.1, Assumption1, PDF p.4;
    Section3.3, Theorem1 and proof, pp.5–6; Sections4–5, pp.6–9; Section4, balance
    rotations; Sections5–6.4; Section4.2, collapsed mode and Fact4, PDF p.7; Section6.3,
    extracting flat clusterings; Section6, Figures3–5 and experimental settings
  accessed_at: '2026-10-13T21:57:12Z'
  snapshot_sha256: 28b8a3c5566bc8d4fd7d394a1c4eca375a022cd89b91f1adbb6a880fa020fb8f
  support: supports
  summary: arXiv1704.01858v1,6April2017;PDF dated7April2017. All20 pages visually
    read. Conference typeset version not compared.
- evidence_id: perch-python
  kind: primary_source
  reference: https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/python/xcluster/models/PNode.py
  locator: PNode._split_down, _rotate and recursive_rotate_if_masked; PNode.recursive_rotate_if_unbalanced,
    can_rotate_for_balance, a_star_exact and a_star_beam; PNode._update_children_min_d,
    _update_children_max_d, min_distance and max_distance; PNode.collapse, leaves
    and true_leaves
  accessed_at: '2026-10-13T22:10:29Z'
  snapshot_sha256: dcc14168ac855173fbc4eb805773dab81690129fb8d2e1d5b36b9c8c75b07d11
  support: supports
  summary: Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019.
    Complete cited file statically read, not executed; not asserted identical to the2017
    benchmark implementation.
- evidence_id: perch-pruning
  kind: primary_source
  reference: https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/python/xcluster/models/pruning_heuristics.py
  locator: pick_k_approx_km_cost
  accessed_at: '2026-10-13T22:10:29Z'
  snapshot_sha256: 9cc682a6566db277b5b96a464748ce1556346d30ab49e18d4d2d68be8b376b9a
  support: supports
  summary: Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019.
    Complete cited file statically read, not executed; not asserted identical to the2017
    benchmark implementation.
- evidence_id: perch-entry
  kind: primary_source
  reference: https://raw.githubusercontent.com/iesl/xcluster/16eab0012f570878017c3f96343ac5b858a35de9/src/scala/xcluster/eval/RunPerch.scala
  locator: RunPerch.main, start/end timing and subsequent serialization/extraction
  accessed_at: '2026-10-13T22:10:29Z'
  snapshot_sha256: aae079842b58c9614b5c6798deb14703311f5389ad49c598cfa46d860c68f88b
  support: supports
  summary: Author repository commit16eab0012f570878017c3f96343ac5b858a35de9,20August2019.
    Complete cited file statically read, not executed; not asserted identical to the2017
    benchmark implementation.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/perch-geometric-boundaries.py
  accessed_at: '2026-10-13T23:12:47Z'
  snapshot_sha256: cbe8237e11da752cf7c07fbaea83e670e51925789aff27c7b6925469829f64f8
  support: supports
  summary: Standalone expressions yield cached squared lower16 versus actual1, and
    cached squared upper202 versus actual221. On points0,10 the paper linear-distance
    cost20 and Python heuristic10 are below squared error50. These checks do not execute
    PERCH or establish a reachable purity failure.
- evidence_id: locator-recheck
  kind: primary_source
  reference: https://arxiv.org/pdf/1704.01858v1
  locator: 'PDF pp.4–6: Assumption1 and Theorem1 in Sections3.1/3.3; p.7: Section4.2
    Fact4; p.8: Algorithm1; p.9: Section5.'
  accessed_at: '2026-10-13T23:12:47Z'
  snapshot_sha256: 28b8a3c5566bc8d4fd7d394a1c4eca375a022cd89b91f1adbb6a880fa020fb8f
  support: supports
  summary: Visually rechecked the actual versioned paper headings, named results and
    displayed algorithm against the maintained citations.
assessments:
- assessment_id: identity
  area: identity
  topic: PERCH clustering
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - identity
  - perch2017
  - perch-python
  - perch-pruning
  - perch-entry
  summary: Retain this distinct DRAFT algorithm.
  details: Retain online nearest-leaf insertion with masking and balance rotations,
    distinct from BIRCH feature compression, CURE representatives, linkage chains,
    RS pointer-tree pruning and Genie inequality-triggered merging.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - mapping
  - perch2017
  - perch-python
  - perch-pruning
  - perch-entry
  summary: The declared AIO mapping is supported.
  details: Related hierarchical and unsupervised clustering tasks are supported without
    algorithm/task equivalence. Nine annotated AIO contexts and five native records
    distinguish the method from classification, metric learning and scalar distance
    functions.
- assessment_id: online-insertion-and-rotation
  area: evidence
  topic: online-insertion-and-rotation
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  - perch-python
  summary: Supported within the stated primary-source and mathematical scope.
  details: The primary insertion algorithm and PNode split/rotate methods support
    a binary tree with revisable subtree placement. The masking definition distinguishes
    existence of a violating distance comparison from globally nearest cluster-pair
    merging.
- assessment_id: conditional-purity-theory
  area: evidence
  topic: conditional-purity-theory
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  summary: Supported within the stated primary-source and mathematical scope.
  details: Theorem1 assumes strict separation and exact intended conditions; the record
    does not transfer its purity-one guarantee to arbitrary data, approximate beam
    search, arbitrary caps or every summary implementation.
- assessment_id: balancing-and-search
  area: evidence
  topic: balancing-and-search
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  - perch-python
  summary: Supported within the stated primary-source and mathematical scope.
  details: Balance rotations require a size-ratio improvement and geometric compatibility.
    Exact and finite-beam search differ. The paper acknowledges quadratic worst-case
    total work; no universal logarithmic height or insertion bound is asserted.
- assessment_id: implementation-boundary-of-geometric-summaries
  area: evidence
  topic: implementation-boundary-of-geometric-summaries
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch-python
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The complete Python min/max cached expressions and explicit curator point
    sets give squared lower16 versus actual1 and squared upper202 versus actual221.
    These refute unrestricted scalar-bound readings, without a claimed reachable full
    execution or purity failure.
- assessment_id: collapsed-mode-and-storage
  area: evidence
  topic: collapsed-mode-and-storage
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  - perch-python
  summary: Supported within the stated primary-source and mathematical scope.
  details: The paper Fact4 additionally assumes L>K and strict separation. Original
    point IDs remain. PNode.collapse retains original leaf objects and feature arrays,
    so feature deletion and constant total memory are not assigned to the inspected
    implementation.
- assessment_id: flat-extraction-and-pruning-cost
  area: evidence
  topic: flat-extraction-and-pruning-cost
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  - perch-pruning
  - perch-entry
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: For0,10, exact mean SSE50 exceeds both paper linear-distance count20 and
    Python heuristic10. The Scala entrypoint timing ends before pruning and serialization.
    No SSE-optimal pruning or full pipeline runtime is inferred.
- assessment_id: reported-evaluation
  area: evidence
  topic: reported-evaluation
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  summary: Supported within the stated primary-source and mathematical scope.
  details: The record separates dendrogram purity from pairwise F1, random arrival
    repetitions, selected hyperparameters, known-K pruning and source-specific beam/collapse/thread
    settings. Missing result marks and log-normalized time are qualified; no universal
    ranking is asserted.
- assessment_id: constructed-boundaries
  area: consistency
  topic: PERCH identity, conditional purity, masking and balance rotations, geometric-summary
    and squared-error boundaries, collapse storage and evaluation scope
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - perch2017
  - perch-python
  - perch-pruning
  - perch-entry
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Standalone expressions yield cached squared lower16 versus actual1, and
    cached squared upper202 versus actual221. On points0,10 the paper linear-distance
    cost20 and Python heuristic10 are below squared error50. These checks do not execute
    PERCH or establish a reachable purity failure.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - identity
  - mapping
  - perch2017
  - perch-python
  - perch-pruning
  - perch-entry
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed every final maintained field and all seven
    claims against the complete initial scientific reading. Only four paper locator
    strings and the actual updated_at changed. Visually verified Assumption1/Section3.1,
    Theorem1/Section3.3, Fact4/Section4.2 and Algorithm1/p.8 after the corrective
    capture. Retained implementation, theory and evaluation boundaries. DRAFT remains.
- assessment_id: paper-locators
  area: evidence
  topic: Paper section, result and page locators
  outcome: supported
  target_ids:
  - AIMech:PERCHClustering
  evidence_ids:
  - locator-recheck
  summary: Corrected citations now agree with the inspected primary paper.
findings:
- finding_id: paper-locators
  issue_key: aimech-perch-citation-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct PERCH paper section and result locators
  description: The initial record located separability/Theorem1 in Section4 and collapse
    in Section5/Theorem2. In the inspected v1, those are Sections3.1/3.3 and Section4.2/Fact4.
    The insertion/definition locators also need to identify Algorithm1 on PDF p.8
    explicitly.
  target_ids:
  - AIMech:PERCHClustering
  field_paths:
  - definition_evidence/0/locator
  - claims/online-insertion-and-rotation/evidence/0/locator
  - claims/conditional-purity-theory/evidence/0/locator
  - claims/collapsed-mode-and-storage/evidence/0/locator
  evidence_ids:
  - locator-recheck
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PERCHClustering.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/320
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T230801Z-perch-clustering
    finding_id: paper-locators
  disposition_reason: 'The corrected maintained citations were compared with the visually
    reread paper: sections, page numbers, Theorem1 and Fact4 now agree. The report
    mirror and history agree with the final bytes. Required gates passed. The sole
    same-key predecessor was explicitly resolved with the same affected target; ignored/hidden
    bundles were included in the lineage scan.'
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 658 native and 442 unchanged generated records.
  The 843-entry main frontier retains 473 pending and 58 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All20 paper pages and complete cited Python core, pruning utilities and Scala entrypoint
  read. Other Scala core remains only partially inspected. No author program execution.
- No author-code execution, training, paid service, hardware measurement or empirical
  replication. The complete cited primary and implementation sources were read; historical
  experiments and floating-point behavior were not reproduced. Constructed checks
  test stated boundaries only.
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
