# Scientific author self-review of Zhou first-passage attractor community detection

- Review: 20261014T081237Z-zhou-attractor-community-detection
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T08:01:52Z
- Finished UTC: 2026-10-14T08:12:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the Zhou attractor-closure algorithm as DRAFT with related clustering-task and Markov-process mappings. The source and exact finite calculations support the scoped mechanism and its explicit non-nesting limitation.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:ZhouAttractorCommunityDetection
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c701fe26a6977e6d364c310adfc1a7aacb1abe3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ZhouAttractorCommunityDetection | data/curated/ZhouAttractorCommunityDetection.yaml | maintained | Zhou first-passage attractor community detection |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ZhouAttractorCommunityDetection | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 260.37s (0:04:20)<br>Checked 442 record(s); 0 failed.<br>Checked 699 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 389 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 390,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ZhouAttractorCommunityDetection | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ZhouAttractorCommunityDetection | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ZhouAttractorCommunityDetection | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:ZhouAttractorCommunityDetection | {"enumeration": {"connected_four_vertex_weighted_graphs": 624, "target_equations_checked": 2496, "arc_weights": [0, 1, 2]}, "chain": {"distance": [["4", "1", "4"], ["3", "2", "3"], ["4", "1", "4"]], "global_attractors": [[1], [1], [1]], "source_global_partition": [[0, 1, 2]], "incorrect_zero_diagonal_partition": [[0], [1], [2]]}, "cycle": {"distance": [["4", "3", "4", "3"], ["3", "4", "3", "4"], ["4", "3", "4", "3"], ["3", "4", "3", "4"]], "local_attractors": [[1, 3], [0, 2], [1, 3], [0, 2]], "all_tie_partition": [[0, 1, 2, 3]], "arbitrary_tie_partition": [[0, 1], [2, 3]], "source_index_squared": "1/2", "root_mean_square_squared": "1"}, "complete_four": {"distinct_adjacent_index_squared": "0"}, "local_global_nesting_counterexample": {"adjacency": [[0, 0, 0, 2], [0, 0, 2, 1], [0, 2, 0, 1], [2, 1, 1, 0]], "local": [[0, 1, 2, 3]], "global_partition": [[0, 3], [1, 2]]}, "hierarchy_simultaneous_cycle": {"adjacency": [[0, 1, 2, 2], [1, 0, 2, 2], [2, 2, 0, 1], [2, 2, 1, 0]], "within_pair_index_squared": "0", "cross_pair_index_squared": "25/288", "threshold": "Any nonnegative threshold below the cross-pair index produces friend sets {0,1} and {2,3}.", "synchronous_label_steps": [[0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]], "own_weight": "1", "other_community_weight": "4", "interpretation": "Every vertex remains strictly unstable. Labels swap simultaneously; the unlabeled partition is unchanged and step4 does not reach its stated stopping condition."}, "scope": "Exact finite curator arithmetic. First-passage solves work for periodic connected walks and do not require convergence of ordinary state probabilities. No author-code execution, complete source hierarchy implementation, biological validation or benchmark replication."} |

## Scientific And Domain Assessments

### Zhou first-passage attractor community detection

identity: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Retain this distinct DRAFT algorithm.

Retain a single local/global attractor-closure algorithm. It differs from edge deletion, centrality ranking, shortest-path sampling and the later adjacent-pair profile functional. The two modes do not justify two duplicate algorithm identities.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

The explicit AIO mapping assessment is supported within its stated scope.

Related UnsupervisedClustering preserves the method-to-task distinction; related MarkovChain identifies the passage process. Neither is an is-a assertion. HierarchicalClustering is rejected because the two modes need not be nested; MathematicalFunction alone omits the algorithm’s grouping operations. Thirteen complete contexts and six neighbors were assessed with hashes checked.

### weighted-walk-and-distance

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The source explicitly permits symmetric positive edge weights and self-connections. Zeroing the target column produces positive return time at the target and first hitting elsewhere. Independent absorbing-target solves and the recurrence verify all2496 finite target cases. Connected periodic walks have finite passage times despite nonconvergent ordinary state probabilities.

### all-attractor-closure

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The source inequalities use &lt;=, retaining every minimizer. Closure in both directions gives weak components; minimality excludes unions of components. Local neighbor restriction and global inclusion of self follow the printed definitions. No desired group count or edge deletion is imported.

### return-and-tie-boundaries

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Exact path returns and cycle ties expose changes caused by zeroing the diagonal or selecting arbitrary single attractors. These are mathematical counterexamples, not benchmark outcomes.

### local-global-partition-boundary

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The four specified weighted edges reproduce a one-block local partition and two-block global partition. Thus local refinement of global is not guaranteed; the paper states an expectation, with a probabilistic relationship in its yeast example. The finite enumeration is clearly bounded.

### stability-and-center-diagnostics

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The source excludes self in own-community sums and compares each alternative community separately. Instability is measured after grouping; centers are self-attractors only when they exist. The record does not convert these diagnostics into enforced constraints.

### evaluation-and-extension-limits

evidence: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Historical weighted/unweighted input distinctions and the reported planted-network weakness are retained without numerical universal performance claims. Protein-functional interpretations remain hypotheses. The three proposed extensions and later dissimilarity method are deferred separately.

### target-column killing, positive returns, all-tie closure, periodic walks, local/global non-nesting and diagnostic-versus-membership semantics

consistency: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Constructed calculations support the stated distinctions.

Exact first-passage equations are compared with an independent absorbing-target solve on624 connected weighted four-node graphs. Explicit path/cycle cases test positive returns and all ties, and a weighted counterexample refutes guaranteed local/global nesting. The shared calculator also examines the later dissimilarity normalization and synchronous hierarchy cycling, which are separate source-method boundaries.

### All maintained fields

provenance: supported. Targets: AIMech:ZhouAttractorCommunityDetection.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Complete current record read before capture; byte-identical contents reassessed after source rereading. All six claims, aliases, definition, version/locator evidence, thirteen AIO contexts, six native neighbors and curation provenance examined. Positive returns and all minimizers are essential, and weak-component closure is explicitly a curator interpretation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T080011Z-zhou-attractor-community-detection.json | supports | Compared both cohort candidates against all 442 pinned AIO and 697 native identities; no normalized match. Ignored- and hidden-inclusive searches of three full checkouts returned 27,0,0 lines, all read as existing Zhou source URLs, abstract interpretations, query strings and pending leads. Semantic assessment covered 155 AIO and 542 native definitions: 155 AIO and541 prior native rows verified unchanged, plus the new Noh–Rieger row and full record read. Thirteen complete AIO contexts and six full native neighbors assessed. This algorithm groups vertices by closure under minimum first-passage attractors and reverse relations. It neither deletes high-betweenness edges nor optimizes modularity, ranks individual nodes, compares complete profile vectors, or constructs a guaranteed local-to-global hierarchy. |
| mapping | sources/aio/aio.json | supports | Related UnsupervisedClustering preserves the method-to-task distinction; related MarkovChain identifies the passage process. Neither is an is-a assertion. HierarchicalClustering is rejected because the two modes need not be nested; MathematicalFunction alone omits the algorithm’s grouping operations. Thirteen complete contexts and six neighbors were assessed with hashes checked. |
| zhou2003attractors | https://arxiv.org/pdf/physics/0302030v1; First-passage definition, PDF pp. 1–2; Equation 1 and local/global attractor community definitions, p. 2; Graph and walk specification, PDF p. 1; Equation 1 and its linear system, p. 2; curator independent absorbing-target checks in research/discovery/zhou-walk-boundaries.py; Local/global attractor definitions and three L-community conditions, PDF p. 2; weak-component equivalence is a curator interpretation of the two closure conditions; Equation 1 and non-strict attractor inequalities, PDF p. 2; exact path/cycle constructions in research/discovery/zhou-walk-boundaries.py; Local/global relationship discussion, PDF p. 2; yeast relationship qualification, p. 3; finite enumeration and explicit nesting counterexample in research/discovery/zhou-walk-boundaries.py; Community size, instability and center definitions, PDF p. 2; unstable members reported in examples, pp. 2–3; Examples and limitations, PDF pp. 2–3; Table I, p. 4; Figure 1, p. 5; proposed extensions, p. 3 | supports | arXiv physics/0302030v1, submitted and printed February11,2003; primary metadata links PRE67:041908(2003), DOI10.1103/PhysRevE.67.041908. All five PDF pages and25references read as text and images, including Equation1, all Figure1 panels and TableI. No journal-byte equivalence or author-software inspection. |
| calculation | research/discovery/zhou-walk-boundaries.py | supports | Exact first-passage equations are compared with an independent absorbing-target solve on624 connected weighted four-node graphs. Explicit path/cycle cases test positive returns and all ties, and a weighted counterexample refutes guaranteed local/global nesting. The shared calculator also examines the later dissimilarity normalization and synchronous hierarchy cycling, which are separate source-method boundaries. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- The first vendored-check attempt failed because the sandbox could not resolve the public canonical host. The actual network-enabled rerun passed all22 artifacts; this environmental failure is not reported as a scientific defect.
- This round adds one DRAFT concept, reaching 698 native and 442 unchanged AIO records. The main frontier has 883 entries, including 472 pending and 58 partly addressed cohorts; nested leads remain.
- All five PDF pages and25 references read as text; all five rendered pages, Equation1, Figure1 four panels and TableI visually inspected. Column-order extraction artifacts checked against page images.
- No journal-byte equivalence, author software, raw-network replication or biological-causality validation. Local/global nesting and state-probability convergence are not asserted.
- The original attractor-closure algorithm is added. The later profile functional, hierarchy adjustment, finite-temperature/coarse/local extensions and other community methods retain separate evidence and identity requirements.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T081237Z-zhou-attractor-community-detection
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Zhou first-passage attractor community detection
started_at: '2026-10-14T08:01:52Z'
finished_at: '2026-10-14T08:12:37Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged target-column killing, positive returns,
    all-tie closure, periodic walks, local/global non-nesting and diagnostic-versus-membership
    semantics. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the Zhou attractor-closure algorithm as DRAFT with related clustering-task
  and Markov-process mappings. The source and exact finite calculations support the
  scoped mechanism and its explicit non-nesting limitation.
source:
  git_revision: 1c701fe26a6977e6d364c310adfc1a7aacb1abe3
  state: working_tree
  inputs:
  - path: data/aio/BidirectionalLayer.yaml
    sha256: e5a9046594e0cc0b0ddf152c6d84745d25b3a3246273babbd7a859f01d7270c8
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/DeepActiveLearning.yaml
    sha256: b04c9aa74728adbe1bd907cb3f0e15b263bda18ed29660babce092daeed2b4f9
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/RankingBias.yaml
    sha256: 3e931657e0ee2a47e36a7858dbb8f26f00b565040f4fedd138f55353551160b0
    role: context
  - path: data/aio/RepresentationBias.yaml
    sha256: 5ac7d1455814eb8305b1ab9d0934e61fc50c09fe3dfd7724da5fdb4a21f360b2
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/DefinitionFilteredGirvanNewman.yaml
    sha256: 7e5d1a8f59abb37f4f9201f99d1a47b578aaac41eb8768d44e02b69a1a6992eb
    role: context
  - path: data/curated/GirvanNewmanCommunityDetection.yaml
    sha256: 0233486104552b70b0fb6cea4c4cd4cff9eb88e763025e14f1890731084b9afa
    role: context
  - path: data/curated/NewmanRandomWalkBetweennessMatrix.yaml
    sha256: 9ed2e0ea7ac76abbf3de52341f78f4944e73b6215af2008fff08888d9fb59bd8
    role: context
  - path: data/curated/NohRiegerRandomWalkCentrality.yaml
    sha256: e96329ed333e5a3658b3ebfa688c5e9b6a8eb2009607adecce3cd6df2d338843
    role: context
  - path: data/curated/PageRank.yaml
    sha256: 8561bc6973069e960effb6f14cd8eaa377e7d5e52ab6c15e2ea4a96f7eeb52e6
    role: context
  - path: data/curated/RiondatoKornaropoulosBetweennessSampling.yaml
    sha256: ea24a1a5cf5019380c36640508cc8a7458203f4491276551898d5477da07f6b8
    role: context
  - path: data/curated/ZhouAttractorCommunityDetection.yaml
    sha256: 5c9e1ef015d93e705d8091714a911c5c0df1a52cf51fb7904b2833cd85d85a15
    role: target
  - path: research/discovery/20261014T080011Z-zhou-attractor-community-detection.json
    sha256: 3d85eb44680e4bcd9a7dd14cba0a100cfc6d7e4caefbee35c94dea9e2da1f4de
    role: context
  - path: research/discovery/zhou-walk-boundaries.py
    sha256: aa2eeb77450d900b0cb5428043c5538b6d635ad705f8c6bd333a54397b44bff0
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
- target_id: AIMech:ZhouAttractorCommunityDetection
  path: data/curated/ZhouAttractorCommunityDetection.yaml
  label: Zhou first-passage attractor community detection
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ZhouAttractorCommunityDetection.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:ZhouAttractorCommunityDetection'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: No author implementation, raw-network benchmark, journal-byte equivalence
      or biological hypothesis validation. Numerical solver/tie-tolerance choices
      remain outside scope.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 260.37s (0:04:20)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 699 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 389 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 390,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
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
  - AIMech:ZhouAttractorCommunityDetection
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
  - AIMech:ZhouAttractorCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/zhou-walk-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: '{"enumeration": {"connected_four_vertex_weighted_graphs": 624, "target_equations_checked":
    2496, "arc_weights": [0, 1, 2]}, "chain": {"distance": [["4", "1", "4"], ["3",
    "2", "3"], ["4", "1", "4"]], "global_attractors": [[1], [1], [1]], "source_global_partition":
    [[0, 1, 2]], "incorrect_zero_diagonal_partition": [[0], [1], [2]]}, "cycle": {"distance":
    [["4", "3", "4", "3"], ["3", "4", "3", "4"], ["4", "3", "4", "3"], ["3", "4",
    "3", "4"]], "local_attractors": [[1, 3], [0, 2], [1, 3], [0, 2]], "all_tie_partition":
    [[0, 1, 2, 3]], "arbitrary_tie_partition": [[0, 1], [2, 3]], "source_index_squared":
    "1/2", "root_mean_square_squared": "1"}, "complete_four": {"distinct_adjacent_index_squared":
    "0"}, "local_global_nesting_counterexample": {"adjacency": [[0, 0, 0, 2], [0,
    0, 2, 1], [0, 2, 0, 1], [2, 1, 1, 0]], "local": [[0, 1, 2, 3]], "global_partition":
    [[0, 3], [1, 2]]}, "hierarchy_simultaneous_cycle": {"adjacency": [[0, 1, 2, 2],
    [1, 0, 2, 2], [2, 2, 0, 1], [2, 2, 1, 0]], "within_pair_index_squared": "0", "cross_pair_index_squared":
    "25/288", "threshold": "Any nonnegative threshold below the cross-pair index produces
    friend sets {0,1} and {2,3}.", "synchronous_label_steps": [[0, 0, 1, 1], [1, 1,
    0, 0], [0, 0, 1, 1]], "own_weight": "1", "other_community_weight": "4", "interpretation":
    "Every vertex remains strictly unstable. Labels swap simultaneously; the unlabeled
    partition is unchanged and step4 does not reach its stated stopping condition."},
    "scope": "Exact finite curator arithmetic. First-passage solves work for periodic
    connected walks and do not require convergence of ordinary state probabilities.
    No author-code execution, complete source hierarchy implementation, biological
    validation or benchmark replication."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T080011Z-zhou-attractor-community-detection.json
  accessed_at: '2026-10-14T08:01:52Z'
  support: supports
  summary: 'Compared both cohort candidates against all 442 pinned AIO and 697 native
    identities; no normalized match. Ignored- and hidden-inclusive searches of three
    full checkouts returned 27,0,0 lines, all read as existing Zhou source URLs, abstract
    interpretations, query strings and pending leads. Semantic assessment covered
    155 AIO and 542 native definitions: 155 AIO and541 prior native rows verified
    unchanged, plus the new Noh–Rieger row and full record read. Thirteen complete
    AIO contexts and six full native neighbors assessed. This algorithm groups vertices
    by closure under minimum first-passage attractors and reverse relations. It neither
    deletes high-betweenness edges nor optimizes modularity, ranks individual nodes,
    compares complete profile vectors, or constructs a guaranteed local-to-global
    hierarchy.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T08:01:52Z'
  support: supports
  summary: Related UnsupervisedClustering preserves the method-to-task distinction;
    related MarkovChain identifies the passage process. Neither is an is-a assertion.
    HierarchicalClustering is rejected because the two modes need not be nested; MathematicalFunction
    alone omits the algorithm’s grouping operations. Thirteen complete contexts and
    six neighbors were assessed with hashes checked.
- evidence_id: zhou2003attractors
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/0302030v1
  locator: First-passage definition, PDF pp. 1–2; Equation 1 and local/global attractor
    community definitions, p. 2; Graph and walk specification, PDF p. 1; Equation
    1 and its linear system, p. 2; curator independent absorbing-target checks in
    research/discovery/zhou-walk-boundaries.py; Local/global attractor definitions
    and three L-community conditions, PDF p. 2; weak-component equivalence is a curator
    interpretation of the two closure conditions; Equation 1 and non-strict attractor
    inequalities, PDF p. 2; exact path/cycle constructions in research/discovery/zhou-walk-boundaries.py;
    Local/global relationship discussion, PDF p. 2; yeast relationship qualification,
    p. 3; finite enumeration and explicit nesting counterexample in research/discovery/zhou-walk-boundaries.py;
    Community size, instability and center definitions, PDF p. 2; unstable members
    reported in examples, pp. 2–3; Examples and limitations, PDF pp. 2–3; Table I,
    p. 4; Figure 1, p. 5; proposed extensions, p. 3
  accessed_at: '2026-10-14T07:32:16Z'
  snapshot_sha256: 2da11ce6cf7ed05ce8ab4fa79de23e5af43f8846b12942193e8bf133c1506a11
  support: supports
  summary: arXiv physics/0302030v1, submitted and printed February11,2003; primary
    metadata links PRE67:041908(2003), DOI10.1103/PhysRevE.67.041908. All five PDF
    pages and25references read as text and images, including Equation1, all Figure1
    panels and TableI. No journal-byte equivalence or author-software inspection.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/zhou-walk-boundaries.py
  accessed_at: '2026-10-14T08:04:40Z'
  snapshot_sha256: aa2eeb77450d900b0cb5428043c5538b6d635ad705f8c6bd333a54397b44bff0
  support: supports
  summary: Exact first-passage equations are compared with an independent absorbing-target
    solve on624 connected weighted four-node graphs. Explicit path/cycle cases test
    positive returns and all ties, and a weighted counterexample refutes guaranteed
    local/global nesting. The shared calculator also examines the later dissimilarity
    normalization and synchronous hierarchy cycling, which are separate source-method
    boundaries.
assessments:
- assessment_id: identity
  area: identity
  topic: Zhou first-passage attractor community detection
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - identity
  - zhou2003attractors
  summary: Retain this distinct DRAFT algorithm.
  details: Retain a single local/global attractor-closure algorithm. It differs from
    edge deletion, centrality ranking, shortest-path sampling and the later adjacent-pair
    profile functional. The two modes do not justify two duplicate algorithm identities.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - mapping
  - zhou2003attractors
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related UnsupervisedClustering preserves the method-to-task distinction;
    related MarkovChain identifies the passage process. Neither is an is-a assertion.
    HierarchicalClustering is rejected because the two modes need not be nested; MathematicalFunction
    alone omits the algorithm’s grouping operations. Thirteen complete contexts and
    six neighbors were assessed with hashes checked.
- assessment_id: weighted-walk-and-distance
  area: evidence
  topic: weighted-walk-and-distance
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source explicitly permits symmetric positive edge weights and self-connections.
    Zeroing the target column produces positive return time at the target and first
    hitting elsewhere. Independent absorbing-target solves and the recurrence verify
    all2496 finite target cases. Connected periodic walks have finite passage times
    despite nonconvergent ordinary state probabilities.
- assessment_id: all-attractor-closure
  area: evidence
  topic: all-attractor-closure
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source inequalities use <=, retaining every minimizer. Closure in both
    directions gives weak components; minimality excludes unions of components. Local
    neighbor restriction and global inclusion of self follow the printed definitions.
    No desired group count or edge deletion is imported.
- assessment_id: return-and-tie-boundaries
  area: evidence
  topic: return-and-tie-boundaries
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exact path returns and cycle ties expose changes caused by zeroing the
    diagonal or selecting arbitrary single attractors. These are mathematical counterexamples,
    not benchmark outcomes.
- assessment_id: local-global-partition-boundary
  area: evidence
  topic: local-global-partition-boundary
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The four specified weighted edges reproduce a one-block local partition
    and two-block global partition. Thus local refinement of global is not guaranteed;
    the paper states an expectation, with a probabilistic relationship in its yeast
    example. The finite enumeration is clearly bounded.
- assessment_id: stability-and-center-diagnostics
  area: evidence
  topic: stability-and-center-diagnostics
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source excludes self in own-community sums and compares each alternative
    community separately. Instability is measured after grouping; centers are self-attractors
    only when they exist. The record does not convert these diagnostics into enforced
    constraints.
- assessment_id: evaluation-and-extension-limits
  area: evidence
  topic: evaluation-and-extension-limits
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  summary: Supported within the stated primary-source and mathematical scope.
  details: Historical weighted/unweighted input distinctions and the reported planted-network
    weakness are retained without numerical universal performance claims. Protein-functional
    interpretations remain hypotheses. The three proposed extensions and later dissimilarity
    method are deferred separately.
- assessment_id: constructed-boundaries
  area: consistency
  topic: target-column killing, positive returns, all-tie closure, periodic walks,
    local/global non-nesting and diagnostic-versus-membership semantics
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - zhou2003attractors
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact first-passage equations are compared with an independent absorbing-target
    solve on624 connected weighted four-node graphs. Explicit path/cycle cases test
    positive returns and all ties, and a weighted counterexample refutes guaranteed
    local/global nesting. The shared calculator also examines the later dissimilarity
    normalization and synchronous hierarchy cycling, which are separate source-method
    boundaries.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:ZhouAttractorCommunityDetection
  evidence_ids:
  - identity
  - mapping
  - zhou2003attractors
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Complete current record read before capture; byte-identical
    contents reassessed after source rereading. All six claims, aliases, definition,
    version/locator evidence, thirteen AIO contexts, six native neighbors and curation
    provenance examined. Positive returns and all minimizers are essential, and weak-component
    closure is explicitly a curator interpretation.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- The first vendored-check attempt failed because the sandbox could not resolve the
  public canonical host. The actual network-enabled rerun passed all22 artifacts;
  this environmental failure is not reported as a scientific defect.
- This round adds one DRAFT concept, reaching 698 native and 442 unchanged AIO records.
  The main frontier has 883 entries, including 472 pending and 58 partly addressed
  cohorts; nested leads remain.
- All five PDF pages and25 references read as text; all five rendered pages, Equation1,
  Figure1 four panels and TableI visually inspected. Column-order extraction artifacts
  checked against page images.
- No journal-byte equivalence, author software, raw-network replication or biological-causality
  validation. Local/global nesting and state-probability convergence are not asserted.
- The original attractor-closure algorithm is added. The later profile functional,
  hierarchy adjustment, finite-temperature/coarse/local extensions and other community
  methods retain separate evidence and identity requirements.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
