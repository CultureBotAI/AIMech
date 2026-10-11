# Scientific self-review and resolved IDA-star order finding

- Review: 20261011T053851Z-foundational-search-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T05:38:48Z
- Finished UTC: 2026-10-11T05:38:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five supported search procedures retain their distinct identities and explicit AIO no-match assessments. The minor IDA-star order quantifier is corrected in both maintained owners and explicitly resolves the only predecessor finding. No actionable unresolved finding remains in this cohort.

## Scope And Provenance

Full scientific self-review of Dijkstra, breadth-first, depth-first, depth-first iterative deepening and IDA-star records.

Selection: Exactly the five maintained IDs in the foundational-search report.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base c8244be1161c5c7301533ae7951c8c869652e8f8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DijkstraShortestPath | data/curated/DijkstraShortestPath.yaml | maintained | Dijkstra shortest-path algorithm |
| AIMech:BreadthFirstSearch | data/curated/BreadthFirstSearch.yaml | maintained | Breadth-first search |
| AIMech:DepthFirstSearch | data/curated/DepthFirstSearch.yaml | maintained | Depth-first search |
| AIMech:DepthFirstIterativeDeepening | data/curated/DepthFirstIterativeDeepening.yaml | maintained | Depth-first iterative deepening |
| AIMech:IterativeDeepeningAStar | data/curated/IterativeDeepeningAStar.yaml | maintained | Iterative-deepening A-star search |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | Checked 124 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | Checked 24 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 23,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 55.16s<br>Checked 442 record(s); 0 failed.<br>Checked 124 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 24 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 23,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Search order, state/cost scope, evidence and AIO no-match assessment

evidence: supported. Targets: AIMech:DijkstraShortestPath.

The shortest-path method in Problem 2 of Dijkstra’s 1959 paper is curated here. Problem 1 in the same paper constructs a minimum spanning tree and is a distinct algorithm. A shortest-path tree need not be a minimum spanning tree; cost-prioritized search is distinct from breadth-first edge-count traversal and heuristic A-star search. No normalized identity match was found across the 442 AIO and 119 prior native records; ignored-inclusive text hits in the main checkout were dependency-package documentation and an unrelated package-metadata substring, not existing concept records.

Nonnegative edge weights are a precondition of the standard method; the record does not extend its settling rule to graphs with negative edges. The 1959 presentation assumes a connected graph. The cited implementation documents source-unreachable vertices separately; reaching an arbitrary node does not establish a path to every node. No particular heap implementation, asymptotic runtime, or universal advantage over other shortest-path algorithms is asserted.

### Search order, state/cost scope, evidence and AIO no-match assessment

evidence: supported. Targets: AIMech:BreadthFirstSearch.

BFS denotes breadth-first search in this record, not the abbreviation sometimes used for generic best-first search. FIFO layer traversal is distinct from a cost-priority queue for weighted paths and from depth-first traversal. No normalized identity match was found across the 442 AIO and 119 prior native records; ignored-inclusive text hits in the main checkout were dependency-package documentation and an unrelated package-metadata substring, not existing concept records.

Shortest distance means number of edges; arbitrary unequal edge costs are not minimized by FIFO traversal. The cited graph implementation tracks discovered vertices. Its visited-state storage and frontier memory must not be confused with a path-only tree-search implementation. Traversal from a single start reaches only its reachable component; the documentation describes separate visits for disconnected components.

### Search order, state/cost scope, evidence and AIO no-match assessment

evidence: supported. Targets: AIMech:DepthFirstSearch.

DFS denotes depth-first traversal, not depth-first iterative deepening or a shortest-path cost ordering. The visited-vertex graph traversal and a path-only tree search share the depth-first order but have different duplicate handling and memory requirements. No normalized identity match was found across the 442 AIO and 119 prior native records; ignored-inclusive text hits in the main checkout were dependency-package documentation and an unrelated package-metadata substring, not existing concept records.

Depth-first order alone does not guarantee that the first goal has a shortest path. A tree expansion can follow an infinite branch or repeat states indefinitely unless appropriate limits or duplicate controls are applied. The graph implementation retains vertex marks; the linear-in-depth memory description of a path-only search is not a universal memory bound for all DFS implementations.

### Search order, state/cost scope, evidence and AIO no-match assessment

evidence: supported. Targets: AIMech:DepthFirstIterativeDeepening.

This record denotes single-agent depth-bounded iterative deepening, also called iterative deepening depth-first search. It differs from IDA-star, whose limits apply to estimated path cost, and from time-managed minimax iterations in game-playing applications. No normalized identity match was found across the 442 AIO and 119 prior native records; ignored-inclusive text hits in the main checkout were dependency-package documentation and an unrelated package-metadata substring, not existing concept records.

Depth measures operator count, not arbitrary accumulated edge cost. Finite branching is needed for each bounded iteration to finish. Repeated shallow work remains real. The paper’s exponential-tree analysis is conditional and does not establish uniform efficiency on graphs with many duplicate paths or near-unit branching. The 1986 erratum to the original journal paper was identified but its text could not be accessed. The procedure is corroborated by the 1992 primary paper; this record does not assert the original global time-and-space optimality theorem.

### Search order, state/cost scope, evidence and AIO no-match assessment

evidence: supported. Targets: AIMech:IterativeDeepeningAStar.

IDA-star is the cost-threshold variant of iterative deepening. The g value is the cost of the current search path and h estimates remaining cost. It does not maintain A-star’s complete open and closed lists, and its cutoff is not simply a depth limit. No normalized identity match was found across the 442 AIO and 119 prior native records; ignored-inclusive text hits in the main checkout were dependency-package documentation and an unrelated package-metadata substring, not existing concept records.

Lowest-cost solution arguments require an admissible heuristic and suitable search/termination assumptions; arbitrary heuristic estimates are not certified here. The method regenerates search paths. Many distinct cutoff values or duplicate routes can impose substantial additional work; this record does not claim the same runtime or expansion count as A-star on every graph. With a nonmonotone evaluation function, iterative deepening does not in general visit newly expanded nodes in best-first order within a cutoff. The original journal paper has an access-limited 1986 erratum. Its basic procedure is corroborated by the 1992 primary paper; the 1985 global asymptotic-optimality theorem is not asserted.

### Counterexample versus universal failure

scope: supported. Targets: AIMech:IterativeDeepeningAStar.

The corrected claim states only lack of a general best-first-order guarantee. The reviewed counterexample supports that scope. The native algorithm identity and threshold-update mechanism are unchanged; the mirrored discovery statement matches the record.

## Findings

### order-quantifier: Qualify IDA-star nonmonotone search-order claim

minor / resolved / confirmed; issue key: aimech-ida-search-order-quantifier.

The later-paper limitation is a failure of a general guarantee, not a theorem that every nonmonotone instance has a different expansion order. Replace categorical prevents wording with can cause or need not follow wording in the record and mirrored discovery entry. The identity, threshold-update algorithm and existing qualified limitation remain supported.

Disposition: Qualified the nonmonotone-order claim in the maintained record and discovery entry, re-read the primary counterexample, inspected changed bytes and hashes, and passed required acceptance checks. All saved review files were searched including hidden/ignored paths; the exact only predecessor and its affected-target union are retained.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:DijkstraShortestPath, AIMech:BreadthFirstSearch, AIMech:DepthFirstSearch, AIMech:DepthFirstIterativeDeepening, AIMech:IterativeDeepeningAStar. Retain distinct procedures based on FIFO depth ordering, recursive backtracking, minimum tentative weighted distance, repeated depth limits and repeated heuristic cost limits. Shared search applications do not establish equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T053332Z-foundational-search.json | supports | No normalized match across 442 AIO labels/scoped synonyms and 119 prior native identities. Hidden/ignored-inclusive full-text search returned zero lines in the isolated checkout and six in main: five dependency-documentation references and one unrelated package-metadata substring. None is an existing curated record. |
| mapping | sources/aio/aio.json; Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning | supports | Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning were read. All five use explicit aio_no_match with individual rejection reasons: graph-language models, learning tasks and functions do not denote these search procedures. This is a bounded inference about the pinned snapshot. |
| dijkstrashortestpath-0 | https://www.cs.yale.edu/homes/lans/readings/routing/dijkstra-routing-1959.pdf; Problem 2, printed pp. 270–271 / PDF pp. 2–3, Steps 1–2 and Remarks 1–2; connected-graph setup on p. 269 / PDF p. 1 | supports | Primary method Source version: Numerische Mathematik 1, 269–271 (1959); university-hosted scan. Actual rendered pages inspected: 1, 2, 3. |
| dijkstrashortestpath-1 | https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/dijkstra_shortest_paths.html; Algorithm description and DIJKSTRA pseudocode; weight_map, predecessor_map and distance_map parameters; Notes [1] | supports | The versioned implementation applies to directed or undirected graphs with nonnegative weights, maintains tentative labels in a minimum-priority queue, and returns source distances or predecessor data. Its shortest-path tree is not guaranteed to be a minimum spanning tree. Source version: Boost Graph Library documentation, Boost 1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation sources. |
| breadthfirstsearch-0 | https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/breadth_first_search.html; Opening traversal description; BFS(G, s) pseudocode; buffer(Buffer&amp; Q) parameter | supports | Primary method Source version: Boost Graph Library documentation, Boost 1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation sources. |
| breadthfirstsearch-1 | https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/dijkstra_shortest_paths.html; Opening description comparing nonnegative weighted shortest paths with unit-edge breadth-first search | supports | Unit-edge paths are within breadth-first search’s shortest-path scope; general nonnegative weighted paths require a cost-sensitive method such as Dijkstra’s algorithm. Source version: Boost Graph Library documentation, Boost 1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation sources. |
| depthfirstsearch-0 | https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/depth_first_search.html; Opening traversal description and DFS(G)/DFS-VISIT(G, u) pseudocode | supports | Primary method Source version: Boost Graph Library documentation, Boost 1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation sources. |
| depthfirstsearch-1 | https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf; Sections 3–4, printed pp. 99–100 / PDF pp. 3–4 | supports | The paper’s path-only depth-first search can revisit states along different paths, and an unbounded search without duplicate checks may fail to terminate. A chosen depth cutoff can miss a goal or permit a nonshortest first solution. Source version: Artificial Intelligence 27(1), 97–109 (1985); university-hosted scan; a separate 1986 erratum remains access-limited. Actual rendered pages inspected: 3, 4. |
| depthfirstiterativedeepening-0 | https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf; Section 4, printed pp. 100–102 / PDF pp. 4–6; procedure and exponential-tree analysis | supports | Primary method Source version: Artificial Intelligence 27(1), 97–109 (1985); university-hosted scan; a separate 1986 erratum remains access-limited. Actual rendered pages inspected: 3, 4. |
| depthfirstiterativedeepening-1 | https://cdn.aaai.org/AAAI/1992/AAAI92-082.pdf; Previous Work: Iterative Deepening, printed p. 533 / PDF p. 1 | supports | The later primary paper identifies depth-first iterative deepening by a depth-based cutoff, in contrast to IDA-star’s g+h cutoff, and describes repeated depth-first passes that keep the current search path. Source version: AAAI-92 proceedings, 533–538 (1992); official conference PDF. Actual rendered pages inspected: 1. |
| iterativedeepeningastar-0 | https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf; Section 6, printed pp. 103–105 / PDF pp. 7–9; threshold update and qualified heuristic analysis | supports | Primary method Source version: Artificial Intelligence 27(1), 97–109 (1985); university-hosted scan; a separate 1986 erratum remains access-limited. Actual rendered pages inspected: 7, 8. |
| iterativedeepeningastar-1 | https://cdn.aaai.org/AAAI/1992/AAAI92-082.pdf; Previous Work, printed pp. 533–534 / PDF pp. 1–2; Theoretical Results, printed p. 536 / PDF p. 4 | supports | The later paper corroborates the minimum-exceeded-value threshold update and explains that iterative deepening need not follow best-first order with a nonmonotone cost function. It also identifies tree cases with many distinct costs in which regeneration overhead is substantial. The original source snapshot and version are unchanged. Re-read PDF pp. 1–2 and inspected the rendered counterexample on p. 2; also inspected the neighboring RBFS pseudocode on p. 3. |
| order-wording | data/curated/IterativeDeepeningAStar.yaml; claims[claim_id=regeneration-and-order].statement | supports | The corrected statement says that iterative deepening need not follow best-first order with a nonmonotone cost function. It now agrees with the general-guarantee limitation and does not assert universal disagreement. |
| predecessor | reviews/structured/20261011T053535Z-foundational-search-open/review.yaml; findings[finding_id=order-quantifier] | supports | Resolved repository/review/finding identity and same issue key. Ignored-inclusive traversal of every saved review found this as the only occurrence/head; the affected-target union is the single IDA-star record. All five original cohort targets are retained. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval. All records remain DRAFT.
- The 1986 erratum is identified through publisher metadata but its full text remains unavailable; broad 1985 optimality claims are omitted.
- Dijkstra’s scan was read visually on all three pages; the original two problems are distinguished. Boost 1.80.0 is a pinned documentation version, not a claim about all current implementations.
- Graph visitation marks and tree-search path storage have different memory and duplicate-handling scope.
- The later corroborating primary paper has the same author, so it is not independent empirical validation.
- No model execution, puzzle solving, full proof certification or source-code audit was performed.
- All required structural checks passed; many discovery leads remain active.
- The original review remains immutable and reports the pre-fix wording. This successor resolves that bounded issue; it does not certify the inaccessible erratum or every theoretical claim in the papers.
- The first unsaved successor draft failed timestamp-prefix validation because its finish time advanced while composing it. The temporary generator was corrected; no saved review was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T053851Z-foundational-search-resolved
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review and resolved IDA-star order finding
started_at: '2026-10-11T05:38:48Z'
finished_at: '2026-10-11T05:38:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own records;
    no independent approval is claimed.
skill: /Users/marcin/.codex/skills/aimech-resolve-reviews/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five supported search procedures retain their distinct identities and
  explicit AIO no-match assessments. The minor IDA-star order quantifier is corrected
  in both maintained owners and explicitly resolves the only predecessor finding.
  No actionable unresolved finding remains in this cohort.
source:
  git_revision: c8244be1161c5c7301533ae7951c8c869652e8f8
  state: working_tree
  inputs:
  - path: data/curated/BreadthFirstSearch.yaml
    sha256: 25594b4ff18b87ff44d5a00667bf64b06aac662f55baaf6190c2d170d6408748
    role: target
  - path: data/curated/DepthFirstIterativeDeepening.yaml
    sha256: 2e01d2da093397d74a7647e624015b8b0f54d14c7420e00d3ded18a576ce605d
    role: target
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: target
  - path: data/curated/DijkstraShortestPath.yaml
    sha256: 071e00cd1f866ecf4ac09bb8da375a6bb6c576d6453dd70ad062058b9278e496
    role: target
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: target
  - path: research/discovery/20261011T053332Z-foundational-search.json
    sha256: 59f36ac0138b557643ee5368a129b73ceeb064c974192812da38faaaa051ee5f
    role: context
  - path: reviews/structured/20261011T053535Z-foundational-search-open/review.yaml
    sha256: e3b29e071bb92419586f81c52db537add48cf6e49512aa4555ce95328cad21ab
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:DijkstraShortestPath
  path: data/curated/DijkstraShortestPath.yaml
  label: Dijkstra shortest-path algorithm
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DijkstraShortestPath.yaml
    role: maintained_record
- target_id: AIMech:BreadthFirstSearch
  path: data/curated/BreadthFirstSearch.yaml
  label: Breadth-first search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BreadthFirstSearch.yaml
    role: maintained_record
- target_id: AIMech:DepthFirstSearch
  path: data/curated/DepthFirstSearch.yaml
  label: Depth-first search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DepthFirstSearch.yaml
    role: maintained_record
- target_id: AIMech:DepthFirstIterativeDeepening
  path: data/curated/DepthFirstIterativeDeepening.yaml
  label: Depth-first iterative deepening
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DepthFirstIterativeDeepening.yaml
    role: maintained_record
- target_id: AIMech:IterativeDeepeningAStar
  path: data/curated/IterativeDeepeningAStar.yaml
  label: Iterative-deepening A-star search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeDeepeningAStar.yaml
    role: maintained_record
scope:
  description: Full scientific self-review of Dijkstra, breadth-first, depth-first,
    depth-first iterative deepening and IDA-star records.
  selection: Exactly the five maintained IDs in the foundational-search report.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exclusions:
  - target: Universal optimality, complete proof certification and benchmark reproduction
    reason: The record scope is inspected procedures and qualified limitations, with
      the 1986 erratum still access-limited.
  - target: Weighted A-star, RBFS and the other recorded frontier methods
    reason: They require separate method, identity and mapping assessments.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 124 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    '
- check_id: required-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 24 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 23,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 31%]\n........................................................................\
    \ [ 63%]\n........................................................................\
    \ [ 94%]\n.........sss                                                       \
    \      [100%]\n225 passed, 3 skipped in 55.16s\nChecked 442 record(s); 0 failed.\n\
    Checked 124 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 24 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 23,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T053332Z-foundational-search.json
  accessed_at: '2026-10-11T05:35:34Z'
  support: supports
  summary: 'No normalized match across 442 AIO labels/scoped synonyms and 119 prior
    native identities. Hidden/ignored-inclusive full-text search returned zero lines
    in the isolated checkout and six in main: five dependency-documentation references
    and one unrelated package-metadata substring. None is an existing curated record.'
  search_scope: All 442 pinned AIO identities and scoped synonyms, 119 preceding native
    records, and both complete checkouts including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM,
    MachineLearningTask, MathematicalFunction and ReinforcementLearning
  accessed_at: '2026-10-11T05:35:34Z'
  support: supports
  summary: 'Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM,
    MachineLearningTask, MathematicalFunction and ReinforcementLearning were read.
    All five use explicit aio_no_match with individual rejection reasons: graph-language
    models, learning tasks and functions do not denote these search procedures. This
    is a bounded inference about the pinned snapshot.'
- evidence_id: dijkstrashortestpath-0
  kind: primary_source
  reference: https://www.cs.yale.edu/homes/lans/readings/routing/dijkstra-routing-1959.pdf
  locator: Problem 2, printed pp. 270–271 / PDF pp. 2–3, Steps 1–2 and Remarks 1–2;
    connected-graph setup on p. 269 / PDF p. 1
  accessed_at: '2026-10-11T05:25:07Z'
  snapshot_sha256: baa66780e853ef06e8bf9c0d8c37e2e0a652e9f5252811e97fb2848d0514fba5
  support: supports
  summary: 'Primary method Source version: Numerische Mathematik 1, 269–271 (1959);
    university-hosted scan. Actual rendered pages inspected: 1, 2, 3.'
- evidence_id: dijkstrashortestpath-1
  kind: primary_source
  reference: https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/dijkstra_shortest_paths.html
  locator: Algorithm description and DIJKSTRA pseudocode; weight_map, predecessor_map
    and distance_map parameters; Notes [1]
  accessed_at: '2026-10-11T05:28:31Z'
  snapshot_sha256: 3bcfc6120324410d33985bfac9e1fac5fe50d66321602ac7aa109144a2eddd04
  support: supports
  summary: 'The versioned implementation applies to directed or undirected graphs
    with nonnegative weights, maintains tentative labels in a minimum-priority queue,
    and returns source distances or predecessor data. Its shortest-path tree is not
    guaranteed to be a minimum spanning tree. Source version: Boost Graph Library
    documentation, Boost 1.80.0 (2022). Actual rendered pages inspected: none; versioned
    HTML for documentation sources.'
- evidence_id: breadthfirstsearch-0
  kind: primary_source
  reference: https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/breadth_first_search.html
  locator: Opening traversal description; BFS(G, s) pseudocode; buffer(Buffer& Q)
    parameter
  accessed_at: '2026-10-11T05:28:31Z'
  snapshot_sha256: 2a265e09d076352b458651d7a09b48c60ccb5a5e5f708fe6c52891d147ea73d2
  support: supports
  summary: 'Primary method Source version: Boost Graph Library documentation, Boost
    1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation
    sources.'
- evidence_id: breadthfirstsearch-1
  kind: primary_source
  reference: https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/dijkstra_shortest_paths.html
  locator: Opening description comparing nonnegative weighted shortest paths with
    unit-edge breadth-first search
  accessed_at: '2026-10-11T05:28:31Z'
  snapshot_sha256: 3bcfc6120324410d33985bfac9e1fac5fe50d66321602ac7aa109144a2eddd04
  support: supports
  summary: 'Unit-edge paths are within breadth-first search’s shortest-path scope;
    general nonnegative weighted paths require a cost-sensitive method such as Dijkstra’s
    algorithm. Source version: Boost Graph Library documentation, Boost 1.80.0 (2022).
    Actual rendered pages inspected: none; versioned HTML for documentation sources.'
- evidence_id: depthfirstsearch-0
  kind: primary_source
  reference: https://www.boost.org/doc/libs/1_80_0/libs/graph/doc/depth_first_search.html
  locator: Opening traversal description and DFS(G)/DFS-VISIT(G, u) pseudocode
  accessed_at: '2026-10-11T05:28:31Z'
  snapshot_sha256: 68ba0b3d02ba7f9de59ceb9f2804ed143eae729c2c562b23e307fccf375c6a90
  support: supports
  summary: 'Primary method Source version: Boost Graph Library documentation, Boost
    1.80.0 (2022). Actual rendered pages inspected: none; versioned HTML for documentation
    sources.'
- evidence_id: depthfirstsearch-1
  kind: primary_source
  reference: https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf
  locator: Sections 3–4, printed pp. 99–100 / PDF pp. 3–4
  accessed_at: '2026-10-11T05:23:52Z'
  snapshot_sha256: 44fc92b6885a43e2beb45db301830dfe97044b142aee9637cd67e6f9bb448894
  support: supports
  summary: 'The paper’s path-only depth-first search can revisit states along different
    paths, and an unbounded search without duplicate checks may fail to terminate.
    A chosen depth cutoff can miss a goal or permit a nonshortest first solution.
    Source version: Artificial Intelligence 27(1), 97–109 (1985); university-hosted
    scan; a separate 1986 erratum remains access-limited. Actual rendered pages inspected:
    3, 4.'
- evidence_id: depthfirstiterativedeepening-0
  kind: primary_source
  reference: https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf
  locator: Section 4, printed pp. 100–102 / PDF pp. 4–6; procedure and exponential-tree
    analysis
  accessed_at: '2026-10-11T05:23:52Z'
  snapshot_sha256: 44fc92b6885a43e2beb45db301830dfe97044b142aee9637cd67e6f9bb448894
  support: supports
  summary: 'Primary method Source version: Artificial Intelligence 27(1), 97–109 (1985);
    university-hosted scan; a separate 1986 erratum remains access-limited. Actual
    rendered pages inspected: 3, 4.'
- evidence_id: depthfirstiterativedeepening-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1992/AAAI92-082.pdf
  locator: 'Previous Work: Iterative Deepening, printed p. 533 / PDF p. 1'
  accessed_at: '2026-10-11T05:28:08Z'
  snapshot_sha256: f30adb0c2776cc24fe49192bf49151cd4d52303019cca8b2d941bc7e7a118987
  support: supports
  summary: 'The later primary paper identifies depth-first iterative deepening by
    a depth-based cutoff, in contrast to IDA-star’s g+h cutoff, and describes repeated
    depth-first passes that keep the current search path. Source version: AAAI-92
    proceedings, 533–538 (1992); official conference PDF. Actual rendered pages inspected:
    1.'
- evidence_id: iterativedeepeningastar-0
  kind: primary_source
  reference: https://cse.sc.edu/~mgv/csce580f12/gradPres/korf_IDAStar_1985.pdf
  locator: Section 6, printed pp. 103–105 / PDF pp. 7–9; threshold update and qualified
    heuristic analysis
  accessed_at: '2026-10-11T05:23:52Z'
  snapshot_sha256: 44fc92b6885a43e2beb45db301830dfe97044b142aee9637cd67e6f9bb448894
  support: supports
  summary: 'Primary method Source version: Artificial Intelligence 27(1), 97–109 (1985);
    university-hosted scan; a separate 1986 erratum remains access-limited. Actual
    rendered pages inspected: 7, 8.'
- evidence_id: iterativedeepeningastar-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1992/AAAI92-082.pdf
  locator: Previous Work, printed pp. 533–534 / PDF pp. 1–2; Theoretical Results,
    printed p. 536 / PDF p. 4
  accessed_at: '2026-10-11T05:28:08Z'
  snapshot_sha256: f30adb0c2776cc24fe49192bf49151cd4d52303019cca8b2d941bc7e7a118987
  support: supports
  summary: The later paper corroborates the minimum-exceeded-value threshold update
    and explains that iterative deepening need not follow best-first order with a
    nonmonotone cost function. It also identifies tree cases with many distinct costs
    in which regeneration overhead is substantial. The original source snapshot and
    version are unchanged. Re-read PDF pp. 1–2 and inspected the rendered counterexample
    on p. 2; also inspected the neighboring RBFS pseudocode on p. 3.
- evidence_id: order-wording
  kind: record_content
  reference: data/curated/IterativeDeepeningAStar.yaml
  locator: claims[claim_id=regeneration-and-order].statement
  accessed_at: '2026-10-11T05:38:48Z'
  support: supports
  summary: The corrected statement says that iterative deepening need not follow best-first
    order with a nonmonotone cost function. It now agrees with the general-guarantee
    limitation and does not assert universal disagreement.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T053535Z-foundational-search-open/review.yaml
  locator: findings[finding_id=order-quantifier]
  accessed_at: '2026-10-11T05:38:48Z'
  support: supports
  summary: Resolved repository/review/finding identity and same issue key. Ignored-inclusive
    traversal of every saved review found this as the only occurrence/head; the affected-target
    union is the single IDA-star record. All five original cohort targets are retained.
assessments:
- assessment_id: dijkstrashortestpath
  area: evidence
  topic: Search order, state/cost scope, evidence and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:DijkstraShortestPath
  evidence_ids:
  - identity
  - mapping
  - dijkstrashortestpath-0
  - dijkstrashortestpath-1
  summary: The shortest-path method in Problem 2 of Dijkstra’s 1959 paper is curated
    here. Problem 1 in the same paper constructs a minimum spanning tree and is a
    distinct algorithm. A shortest-path tree need not be a minimum spanning tree;
    cost-prioritized search is distinct from breadth-first edge-count traversal and
    heuristic A-star search. No normalized identity match was found across the 442
    AIO and 119 prior native records; ignored-inclusive text hits in the main checkout
    were dependency-package documentation and an unrelated package-metadata substring,
    not existing concept records.
  details: Nonnegative edge weights are a precondition of the standard method; the
    record does not extend its settling rule to graphs with negative edges. The 1959
    presentation assumes a connected graph. The cited implementation documents source-unreachable
    vertices separately; reaching an arbitrary node does not establish a path to every
    node. No particular heap implementation, asymptotic runtime, or universal advantage
    over other shortest-path algorithms is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A graph or state-space search procedure, not a learned model or one
      solved problem instance.
    evidence_ids:
    - dijkstrashortestpath-0
    - dijkstrashortestpath-1
  - name: aio-mapping
    value: explicit no-match
    definition: Each of six inspected AIO targets is rejected for a stated scope mismatch;
      no absence from other snapshots or ontologies is implied.
    evidence_ids:
    - mapping
    - identity
- assessment_id: breadthfirstsearch
  area: evidence
  topic: Search order, state/cost scope, evidence and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:BreadthFirstSearch
  evidence_ids:
  - identity
  - mapping
  - breadthfirstsearch-0
  - breadthfirstsearch-1
  summary: BFS denotes breadth-first search in this record, not the abbreviation sometimes
    used for generic best-first search. FIFO layer traversal is distinct from a cost-priority
    queue for weighted paths and from depth-first traversal. No normalized identity
    match was found across the 442 AIO and 119 prior native records; ignored-inclusive
    text hits in the main checkout were dependency-package documentation and an unrelated
    package-metadata substring, not existing concept records.
  details: Shortest distance means number of edges; arbitrary unequal edge costs are
    not minimized by FIFO traversal. The cited graph implementation tracks discovered
    vertices. Its visited-state storage and frontier memory must not be confused with
    a path-only tree-search implementation. Traversal from a single start reaches
    only its reachable component; the documentation describes separate visits for
    disconnected components.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A graph or state-space search procedure, not a learned model or one
      solved problem instance.
    evidence_ids:
    - breadthfirstsearch-0
    - breadthfirstsearch-1
  - name: aio-mapping
    value: explicit no-match
    definition: Each of six inspected AIO targets is rejected for a stated scope mismatch;
      no absence from other snapshots or ontologies is implied.
    evidence_ids:
    - mapping
    - identity
- assessment_id: depthfirstsearch
  area: evidence
  topic: Search order, state/cost scope, evidence and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:DepthFirstSearch
  evidence_ids:
  - identity
  - mapping
  - depthfirstsearch-0
  - depthfirstsearch-1
  summary: DFS denotes depth-first traversal, not depth-first iterative deepening
    or a shortest-path cost ordering. The visited-vertex graph traversal and a path-only
    tree search share the depth-first order but have different duplicate handling
    and memory requirements. No normalized identity match was found across the 442
    AIO and 119 prior native records; ignored-inclusive text hits in the main checkout
    were dependency-package documentation and an unrelated package-metadata substring,
    not existing concept records.
  details: Depth-first order alone does not guarantee that the first goal has a shortest
    path. A tree expansion can follow an infinite branch or repeat states indefinitely
    unless appropriate limits or duplicate controls are applied. The graph implementation
    retains vertex marks; the linear-in-depth memory description of a path-only search
    is not a universal memory bound for all DFS implementations.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A graph or state-space search procedure, not a learned model or one
      solved problem instance.
    evidence_ids:
    - depthfirstsearch-0
    - depthfirstsearch-1
  - name: aio-mapping
    value: explicit no-match
    definition: Each of six inspected AIO targets is rejected for a stated scope mismatch;
      no absence from other snapshots or ontologies is implied.
    evidence_ids:
    - mapping
    - identity
- assessment_id: depthfirstiterativedeepening
  area: evidence
  topic: Search order, state/cost scope, evidence and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:DepthFirstIterativeDeepening
  evidence_ids:
  - identity
  - mapping
  - depthfirstiterativedeepening-0
  - depthfirstiterativedeepening-1
  summary: This record denotes single-agent depth-bounded iterative deepening, also
    called iterative deepening depth-first search. It differs from IDA-star, whose
    limits apply to estimated path cost, and from time-managed minimax iterations
    in game-playing applications. No normalized identity match was found across the
    442 AIO and 119 prior native records; ignored-inclusive text hits in the main
    checkout were dependency-package documentation and an unrelated package-metadata
    substring, not existing concept records.
  details: Depth measures operator count, not arbitrary accumulated edge cost. Finite
    branching is needed for each bounded iteration to finish. Repeated shallow work
    remains real. The paper’s exponential-tree analysis is conditional and does not
    establish uniform efficiency on graphs with many duplicate paths or near-unit
    branching. The 1986 erratum to the original journal paper was identified but its
    text could not be accessed. The procedure is corroborated by the 1992 primary
    paper; this record does not assert the original global time-and-space optimality
    theorem.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A graph or state-space search procedure, not a learned model or one
      solved problem instance.
    evidence_ids:
    - depthfirstiterativedeepening-0
    - depthfirstiterativedeepening-1
  - name: aio-mapping
    value: explicit no-match
    definition: Each of six inspected AIO targets is rejected for a stated scope mismatch;
      no absence from other snapshots or ontologies is implied.
    evidence_ids:
    - mapping
    - identity
- assessment_id: iterativedeepeningastar
  area: evidence
  topic: Search order, state/cost scope, evidence and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:IterativeDeepeningAStar
  evidence_ids:
  - identity
  - mapping
  - iterativedeepeningastar-0
  - iterativedeepeningastar-1
  summary: IDA-star is the cost-threshold variant of iterative deepening. The g value
    is the cost of the current search path and h estimates remaining cost. It does
    not maintain A-star’s complete open and closed lists, and its cutoff is not simply
    a depth limit. No normalized identity match was found across the 442 AIO and 119
    prior native records; ignored-inclusive text hits in the main checkout were dependency-package
    documentation and an unrelated package-metadata substring, not existing concept
    records.
  details: Lowest-cost solution arguments require an admissible heuristic and suitable
    search/termination assumptions; arbitrary heuristic estimates are not certified
    here. The method regenerates search paths. Many distinct cutoff values or duplicate
    routes can impose substantial additional work; this record does not claim the
    same runtime or expansion count as A-star on every graph. With a nonmonotone evaluation
    function, iterative deepening does not in general visit newly expanded nodes in
    best-first order within a cutoff. The original journal paper has an access-limited
    1986 erratum. Its basic procedure is corroborated by the 1992 primary paper; the
    1985 global asymptotic-optimality theorem is not asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A graph or state-space search procedure, not a learned model or one
      solved problem instance.
    evidence_ids:
    - iterativedeepeningastar-0
    - iterativedeepeningastar-1
  - name: aio-mapping
    value: explicit no-match
    definition: Each of six inspected AIO targets is rejected for a stated scope mismatch;
      no absence from other snapshots or ontologies is implied.
    evidence_ids:
    - mapping
    - identity
- assessment_id: order-quantifier
  area: scope
  topic: Counterexample versus universal failure
  outcome: supported
  target_ids:
  - AIMech:IterativeDeepeningAStar
  evidence_ids:
  - iterativedeepeningastar-1
  - order-wording
  - predecessor
  summary: The corrected claim states only lack of a general best-first-order guarantee.
    The reviewed counterexample supports that scope. The native algorithm identity
    and threshold-update mechanism are unchanged; the mirrored discovery statement
    matches the record.
findings:
- finding_id: order-quantifier
  issue_key: aimech-ida-search-order-quantifier
  category: scope
  severity: minor
  status: resolved
  certainty: confirmed
  target_ids:
  - AIMech:IterativeDeepeningAStar
  field_paths:
  - claims[claim_id=regeneration-and-order].statement
  - entries[id=AIMech:IterativeDeepeningAStar].additional_evidence[claim_id=regeneration-and-order].claim
  evidence_ids:
  - iterativedeepeningastar-1
  - order-wording
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeDeepeningAStar.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261011T053332Z-foundational-search.json
    role: discovery_report
  title: Qualify IDA-star nonmonotone search-order claim
  description: The later-paper limitation is a failure of a general guarantee, not
    a theorem that every nonmonotone instance has a different expansion order. Replace
    categorical prevents wording with can cause or need not follow wording in the
    record and mirrored discovery entry. The identity, threshold-update algorithm
    and existing qualified limitation remain supported.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261011T053535Z-foundational-search-open
    finding_id: order-quantifier
  disposition_reason: Qualified the nonmonotone-order claim in the maintained record
    and discovery entry, re-read the primary counterexample, inspected changed bytes
    and hashes, and passed required acceptance checks. All saved review files were
    searched including hidden/ignored paths; the exact only predecessor and its affected-target
    union are retained.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/24
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:DijkstraShortestPath
  - AIMech:BreadthFirstSearch
  - AIMech:DepthFirstSearch
  - AIMech:DepthFirstIterativeDeepening
  - AIMech:IterativeDeepeningAStar
  evidence_ids:
  - identity
  - mapping
  - dijkstrashortestpath-0
  - dijkstrashortestpath-1
  - breadthfirstsearch-0
  - breadthfirstsearch-1
  - depthfirstsearch-0
  - depthfirstsearch-1
  - depthfirstiterativedeepening-0
  - depthfirstiterativedeepening-1
  - iterativedeepeningastar-0
  - iterativedeepeningastar-1
  rationale: Retain distinct procedures based on FIFO depth ordering, recursive backtracking,
    minimum tentative weighted distance, repeated depth limits and repeated heuristic
    cost limits. Shared search applications do not establish equivalence.
limitations:
- Adversarial author self-review, not independent approval. All records remain DRAFT.
- The 1986 erratum is identified through publisher metadata but its full text remains
  unavailable; broad 1985 optimality claims are omitted.
- Dijkstra’s scan was read visually on all three pages; the original two problems
  are distinguished. Boost 1.80.0 is a pinned documentation version, not a claim about
  all current implementations.
- Graph visitation marks and tree-search path storage have different memory and duplicate-handling
  scope.
- The later corroborating primary paper has the same author, so it is not independent
  empirical validation.
- No model execution, puzzle solving, full proof certification or source-code audit
  was performed.
- All required structural checks passed; many discovery leads remain active.
- The original review remains immutable and reports the pre-fix wording. This successor
  resolves that bounded issue; it does not certify the inaccessible erratum or every
  theoretical claim in the papers.
tags:
- native-concepts
- search-algorithms
- self-review
- resolved-finding
- discovery-ongoing
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261011T053535Z-foundational-search-open
  relationship: Explicit successor resolving the same order-quantifier issue key after
    a bounded claim-scope correction; all five cohort targets retained.
notes:
- The first unsaved successor draft failed timestamp-prefix validation because its
  finish time advanced while composing it. The temporary generator was corrected;
  no saved review was overwritten.
```
