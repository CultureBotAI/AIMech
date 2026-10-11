# Scientific self-review of sat-noise methods

- Review: 20261011T152249Z-sat-noise
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T15:18:42Z
- Finished UTC: 2026-10-11T15:22:49Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain GSAT with random walk, GSAT with random noise and classical WalkSAT/SKC as distinct DRAFT concepts with bounded AIO no-match assessments. Different candidate distributions and flip-ranking/priority rules are supported by primary sources and original finite examples. No actionable curation finding remains in the declared scope.

## Scope And Provenance

All fields of three maintained sat-noise and SAT-search concepts.

Selection: Exact three IDs in the saved ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base a0391a865fc798914f048afeb65fd5472cf660ed.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GSATWithRandomWalk | data/curated/GSATWithRandomWalk.yaml | maintained | GSAT with random walk |
| AIMech:GSATWithRandomNoise | data/curated/GSATWithRandomNoise.yaml | maintained | GSAT with random noise |
| AIMech:WalkSAT | data/curated/WalkSAT.yaml | maintained | WalkSAT |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 122.20s (0:02:02)<br>Checked 442 record(s); 0 failed.<br>Checked 319 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 86 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 84,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT | Command exited0 with no output. |
| Finite sat-noise boundary examples | passed | True | AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT | {"focused_probabilities": {"1": "1/3", "2": "1/3", "3": "1/3"}, "pure_clause_first_probabilities": {"1": "1/2", "2": "1/4", "3": "1/4"}, "unrestricted_noise_probability_for_d": "1/4", "break_vs_gain": {"1": {"make": 1, "break": 1, "gain": 0}, "2": {"make": 4, "break": 2, "gain": 2}}, "freebie_scores": {"1": {"make": 1, "break": 0, "gain": 1}, "2": {"make": 1, "break": 1, "gain": 0}}, "interpretation": "These finite CNF substitutions distinguish variable-union sampling, clause-first sampling, unrestricted noise, break-only ranking and zero-break priority. Pure clause-first sampling is not asserted to be SKC at p=1 because freebies override its coin."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:GSATWithRandomWalk.

This is the mixed random-walk extension of GSAT described by Selman and Kautz and clarified in the later noise paper. Its focused move samples a duplicate-free union of eligible variables, not a clause followed by one of its variables. The latter distribution underlies the separately described WSAT family. It is also distinct from unrestricted GSAT random noise and from a pure clause-first walk for 2-SAT. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 316 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All seven unique lines were inspected, and the sorted checkout hit sets were identical: neighboring GSAT/WalkSAT mentions and saved review/ledger references, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and four full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a complete assignment of the variables in the input CNF formula. Stop successfully when it satisfies the formula. Otherwise, with fixed probability p, select uniformly from the distinct variables appearing in at least one currently unsatisfied clause and flip the chosen variable. With probability 1−p, evaluate all single-variable flips and choose a largest increase in the total number of satisfied clauses, breaking tied best choices randomly as in GSAT. The random and greedy branches can make non-improving moves. The extension can use the GSAT outer random-initialization, per-attempt flip budget and restart/attempt budget. The 1994 paper explicitly explains the duplicate-free variable list, which gives equal probabilities to eligible variables even when their clause occurrence counts differ. The UBCSAT project documents GWSAT as GSAT with Random Walk and associates that named implementation with the Selman–Kautz extension. Limits: The focused random branch and the global greedy branch use different candidate sets. Replacing the former by random-clause-then-random-variable sampling changes the transition distribution, even at p=1. Shared behavior at p=0 does not make the full variant identical to basic GSAT. Finite search failure is not a proof of unsatisfiability. The polynomial analysis cited for pure random walks on satisfiable 2-CNF does not establish a corresponding general-CNF bound for this mixture. The noise parameter, CNF encoding, initialization and outer budgets affect behavior. No single best p, universal speedup or numerical benchmark claim is curated. Empty clauses or empty candidate sets require explicit handling outside the described nonempty-variable flip rule. The record curates the move policy and its stated GSAT context, not an executed solver or a certification of every loop boundary. The original GSAT pre-flip-only pseudocode boundary remains an implementation choice to declare.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:GSATWithRandomNoise.

This is the random-noise strategy explicitly contrasted with the focused random-walk GSAT strategy in the 1994 primary paper. The defining difference is the random branch’s eligible variable set. It is not simulated annealing, Gaussian input noise, neural weight noise, or WalkSAT’s clause-first selection. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 316 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All seven unique lines were inspected, and the sorted checkout hit sets were identical: neighboring GSAT/WalkSAT mentions and saved review/ledger references, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and four full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Start from a complete assignment for a CNF formula and test whether it is satisfying. At a search step, with probability p choose a formula variable uniformly and flip it, irrespective of whether it appears in an unsatisfied clause or improves the clause count. With probability 1−p take a globally best GSAT flip, using the largest increase in the number of satisfied clauses and random tie handling. Apply the chosen outer flip and attempt budgets with random restarts as in the GSAT experiments. This unrestricted noise replaces the eligible-variable restriction in GSAT with random walk. It can perturb a variable whose current occurrences are all in satisfied clauses, and it uses no temperature-dependent acceptance test. Limits: A noise move need not help satisfy a currently violated clause and can break previously satisfied clauses. Conversely, the mechanism does not assert that every random move is uphill. Finite search failure is inconclusive about satisfiability. Empirical comparisons on the paper’s selected instances and tuned settings are not universal performance orderings or general runtime bounds. At p=0 the move policy reduces to basic GSAT, while p=1 selects only unrestricted random flips; the entire parameterized policy is not identical to either endpoint. The formula’s variable universe and treatment of empty clauses/candidate sets must be explicit. The record describes the source’s noise policy, not an executed reference implementation, a weighted MAX-SAT extension or automatic parameter adaptation. It does not silently repair the original GSAT final-flip check boundary.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:WalkSAT.

This record curates the classical SKC variable-selection rule under the commonly used WalkSAT name. It does not equate every later WalkSAT heuristic, the earlier underspecified WSAT family description, pure clause-first random walk, or global GSAT-with-walk selection with that exact rule. The 1994 source gives the clause-first lineage; the authors’ 2004 solver description explicitly supplies the zero-break priority and breakcount-based choice. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 316 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 7 and 7 lines respectively. All seven unique lines were inspected, and the sorted checkout hit sets were identical: neighboring GSAT/WalkSAT mentions and saved review/ledger references, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and four full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a complete truth assignment and stop successfully when all clauses are satisfied. Otherwise randomly choose an unsatisfied nonempty clause. For each candidate variable in that clause, its breakcount is the number of currently satisfied clauses that would become unsatisfied if it were flipped. If any candidate has breakcount zero, choose one such candidate at random. Only when there is no zero-break candidate, choose a random variable from the selected clause with probability p; with probability 1−p choose a candidate of minimum breakcount, breaking ties randomly. Flip the chosen variable and repeat under the application’s stopping budget. Breakcount omits how many previously unsatisfied clauses become satisfied, so it need not rank candidates like GSAT’s global net-gain score. Random restarts are an optional outer strategy; the described 2004 competition configuration uses one long run. Limits: The zero-break branch precedes the noise coin, including at p=1. That setting is therefore not generally identical to a pure random-clause/random-variable walk. Removing the priority changes the specified SKC heuristic. Candidate selection is restricted to the chosen clause and can miss the globally best net-gain flip. Minimizing breakcount is different from minimizing breakcount minus makecount; replacing one by the other changes the heuristic. A finite unsuccessful run does not prove UNSAT, and the pure 2-CNF random-walk guarantee is not automatically a guarantee for this SKC policy on general formulas. The noise setting and restart strategy are not universal constants. The move rule needs a nonempty selected clause and a declared formula representation. Empty clauses require separate handling; duplicate clauses, literal normalization and weighted extensions can change counts or sampling and are not silently normalized here. AutoWalksat, Rnovelty, Rnovelty+ and later software additions are distinct procedures or configurations, not exact aliases of this SKC record. No author implementation or numerical solver benchmark was run.

### Focused variable sampling and global greedy flips

consistency: supported. Targets: AIMech:GSATWithRandomWalk.

Retain the mixed GSAT walk policy, distinct from clause-first sampling.

The1993 StrategyIII mixes a variable in some unsatisfied clause with the standard global GSAT best move. The1994 paper clarifies that its focused branch uses a duplicate-free variable list. The finite example yields1/3 each for three eligible variables, whereas pure clause-first selection yields1/2,1/4,1/4. The GWSAT alias is supported by project documentation; its access level is documentation and its malformed catalog bibliography is not adopted. Finite failure, outer budgets and the original GSAT final-flip check boundary remain explicit.

### Unrestricted noise versus focused walk and annealing

consistency: supported. Targets: AIMech:GSATWithRandomNoise.

Retain the explicitly named unrestricted random-noise variant.

The1994 source removes the eligible-variable restriction from the random branch, preserving the GSAT greedy branch. The finite example has a variable outside the unsatisfied-clause union whose flip breaks a satisfied clause. No temperature acceptance test is involved. Shared p=0 behavior does not make the complete parameterized policy identical to the focused variant; no universal performance ordering is asserted.

### Clause-first SKC selection, freebies and breakcount

consistency: supported. Targets: AIMech:WalkSAT.

Retain classical SKC with explicitly bounded use of the WalkSAT name.

The2004 primary solver description specifies zero-break choice before the random/greedy coin and distinguishes breakcount from makecount. The finite cases show the freebie override at p=1 and a break-only ranking opposite to net-gain ranking. The earlier1994 WSAT description is lineage context, not evidence that every variant implements the exact SKC rule. Optional restarts are accurately scoped: the2004 competition configuration used one long run. The record does not inherit the pure2-CNF random-walk bound for arbitrary formulas or report failure as UNSAT.

### SAT move policies versus learning/model/layer classes

grounding: supported. Targets: AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT.

Retain three native identities with bounded no-match assessments.

Eight exact AIO CLASS nodes were inspected with definitions, scoped synonyms/comments and outgoing edges. All three symbolic SAT-search policies receive bounded no-match assessments. Logical formulas do not make a language model; random flips do not make a neural noise layer or training strategy. Solving a fixed formula is not automatically a learning task, and a possible Markov representation does not establish a specific algorithm-to-network-class mapping. Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records, read in this and preceding rounds, distinguish global net-gain flips, conflicted-variable repair, temperature-dependent acceptance and sampled action-value learning. Their prior mappings are context, not newly approved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:GSATWithRandomWalk, AIMech:GSATWithRandomNoise, AIMech:WalkSAT. Uniform variable-union sampling, unrestricted noise and clause-first selection with zero-break priority define different move policies. Shared GSAT lineage, parameter endpoints and SAT applications do not establish identity.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T151714Z-sat-noise.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 316 preceding native IDs/names/aliases; no normalized match. Full-checkout text searches included ignored and hidden files and returned seven lines each. All seven unique lines were inspected and sorted outputs were identical: neighboring GSAT/WalkSAT mentions and saved review/ledger references, not existing candidate records. Eight exact AIO nodes and four complete native neighbors were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Eight exact CLASS nodes with scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Eight exact AIO CLASS nodes were inspected with definitions, scoped synonyms/comments and outgoing edges. All three symbolic SAT-search policies receive bounded no-match assessments. Logical formulas do not make a language model; random flips do not make a neural noise layer or training strategy. Solving a fixed formula is not automatically a learning task, and a possible Markov representation does not establish a specific algorithm-to-network-class mapping. Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records, read in this and preceding rounds, distinguish global net-gain flips, conflicted-variable repair, temperature-dependent acceptance and sampled action-value learning. Their prior mappings are context, not newly approved. |
| neighbors | research/discovery/20261011T151714Z-sat-noise.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records distinguish global net-gain flips, conflicted-variable repair, temperature-dependent acceptance and sampled action-value learning. Their prior mappings are contextual, not newly approved. |
| finite-conventions | research/discovery/sat-noise-boundaries.py; calculate(): variable-union versus clause-first probabilities, unrestricted noise, break versus net-gain ranking and zero-break priority | supports | Original finite CNF substitutions distinguish uniform variable-union sampling from clause-first sampling, show an unrestricted noise move outside the eligible union, separate breakcount from net-gain ranking, and verify that a zero-break candidate overrides the SKC noise coin even at p=1. No author solver or benchmark was executed. |
| gsatwithrandomwalk-source-0 | https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf; The Random Walk Strategy, PDF2 / printed338; Modifying the Random Walk Strategy, PDF5 / printed341, duplicate-free variable list versus clause-first WSAT sampling | supports | Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343; seven-page publisher scan. The source compares specific parameter settings and instance classes, not a universal dominance result. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| gsatwithrandomwalk-source-1 | https://www.cs.cornell.edu/selman/papers/pdf/93.ijcai.gsatext.pdf; Section3.3 and StrategyIII, PDF4; Section2 and Figure1, PDF1–2, GSAT context | supports | Domain-Independent Extensions to GSAT: Solving Large Structured Satisfiability Problems. Six-page author-hosted manuscript marked to appear in Proceedings of IJCAI-93. PDF page numbers identify this inspected version; final proceedings pagination is not substituted. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| gsatwithrandomwalk-source-2 | https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/; GWSAT: GSAT with Random Walk entry; algorithm identifier gwsat | supports | Algorithms in UBCSAT. Undated archived project algorithm documentation, HTTP snapshot captured during this curation. Only the GWSAT entry and relevant index headings were inspected for naming and discovery; catalog bibliographic text is not authoritative publication metadata. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| gsatwithrandomnoise-source-0 | https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf; The Random Walk Strategy, PDF2 / printed338; random-noise variation and experimental parameter context, PDF3 / printed339 | supports | Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343; seven-page publisher scan. The source compares specific parameter settings and instance classes, not a universal dominance result. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| walksat-source-0 | https://www.cs.virginia.edu/~rmw7my/papers/walksat.pdf; PDF/printed1, breakcount/makecount definitions and SKC steps1–3; PDF/printed2, variant distinctions and single-run/no-restart competition configuration | supports | Walksat in the 2004 SAT Competition. Two-page author-hosted SAT Competition 2004 solver description, printed/PDF pp.1–2. Defines the SKC rule and distinguishes AutoWalksat and Rnovelty+; this is not documentation for every later software version. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| walksat-source-1 | https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf; Modifying the Random Walk Strategy, PDF5 / printed341, clause-first WSAT lineage and sampling contrast | supports | Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343; seven-page publisher scan. The source compares specific parameter settings and instance classes, not a universal dominance result. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- Finite search failure is not an UNSAT proof. Pure random-walk bounds do not automatically cover the curated mixed policies on arbitrary formulas.
- The WalkSAT record explicitly scopes the classical SKC rule; later variants, weighted extensions and source-code boundary conventions are not silently included.
- Only declared PDF/OCR/HTML scopes were inspected. The UBCSAT page supports naming, not a full-catalog implementation audit. No author solver or numerical benchmark was executed.
- There are188 pending inspection leads plus unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T152249Z-sat-noise
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of sat-noise methods
started_at: '2026-10-11T15:18:42Z'
finished_at: '2026-10-11T15:22:49Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all new fields against
    primary method sections, critical PDF images, eight exact AIO nodes, four full
    neighboring records and original finite counterexamples. Sampling distributions,
    source-version boundaries, zero-break priority, optional restarts and documentation
    access types were preserved before record creation. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain GSAT with random walk, GSAT with random noise and classical WalkSAT/SKC
  as distinct DRAFT concepts with bounded AIO no-match assessments. Different candidate
  distributions and flip-ranking/priority rules are supported by primary sources and
  original finite examples. No actionable curation finding remains in the declared
  scope.
source:
  git_revision: a0391a865fc798914f048afeb65fd5472cf660ed
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/NoiseDenseLayer.yaml
    sha256: fc4cefe872103228071e21e0567f2bb2d4a8a597c66dc58cee9cb8d568684a67
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/GSAT.yaml
    sha256: cfad196dde77b2b47bb3cbc2f1cce46bafe138025d937d744fd5404c5bcaeb80
    role: context
  - path: data/curated/GSATWithRandomNoise.yaml
    sha256: 570339c1bc59fadeca67cd75d6bebb39014d675eed929fc013d2179de793752a
    role: target
  - path: data/curated/GSATWithRandomWalk.yaml
    sha256: 5d63a89898da6fa4b60fd75387c72505f9390a3bba23aa423a7e2de3f6eed27b
    role: target
  - path: data/curated/MinConflicts.yaml
    sha256: 12b23515b6d3d3ae662a67519dd0f0f15f10a7f2b5b7aa88815a76e4a8309512
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/WalkSAT.yaml
    sha256: 7f28176fc24fe30c94bfd14a74304cae1021787abf87ebcfdbde6b19bc11fd23
    role: target
  - path: research/discovery/20261011T151714Z-sat-noise.json
    sha256: e42e91c1daaf78ef35ee7d53d721ed67a80bdc9fa0d15dcafd91c1546ae59ed2
    role: context
  - path: research/discovery/sat-noise-boundaries.py
    sha256: 81715afcbf73b63b7cb2185657ae4df3c60b7d807a3e796c784edf5ac638b1e0
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
- target_id: AIMech:GSATWithRandomWalk
  path: data/curated/GSATWithRandomWalk.yaml
  label: GSAT with random walk
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GSATWithRandomWalk.yaml
    role: maintained
- target_id: AIMech:GSATWithRandomNoise
  path: data/curated/GSATWithRandomNoise.yaml
  label: GSAT with random noise
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GSATWithRandomNoise.yaml
    role: maintained
- target_id: AIMech:WalkSAT
  path: data/curated/WalkSAT.yaml
  label: WalkSAT
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/WalkSAT.yaml
    role: maintained
scope:
  description: All fields of three maintained sat-noise and SAT-search concepts.
  selection: Exact three IDs in the saved ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  exclusions:
  - target: Uninspected frontier leads and complete executable implementations
    reason: The batch does not exhaust SAT search or execute original solvers. Other
      WalkSAT variants and newly identified UBCSAT cohorts remain frontier leads.
  - target: Prior corpus, unread pages and empirical performance
    reason: Older records are boundary context. Only declared source sections/images
      and finite curator examples support this review.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 122.20s (0:02:02)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 319 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 86 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 84,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
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
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
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
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Finite sat-noise boundary examples
  command: python3 research/discovery/sat-noise-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  exit_code: 0
  expected_exit_code: 0
  summary: '{"focused_probabilities": {"1": "1/3", "2": "1/3", "3": "1/3"}, "pure_clause_first_probabilities":
    {"1": "1/2", "2": "1/4", "3": "1/4"}, "unrestricted_noise_probability_for_d":
    "1/4", "break_vs_gain": {"1": {"make": 1, "break": 1, "gain": 0}, "2": {"make":
    4, "break": 2, "gain": 2}}, "freebie_scores": {"1": {"make": 1, "break": 0, "gain":
    1}, "2": {"make": 1, "break": 1, "gain": 0}}, "interpretation": "These finite
    CNF substitutions distinguish variable-union sampling, clause-first sampling,
    unrestricted noise, break-only ranking and zero-break priority. Pure clause-first
    sampling is not asserted to be SKC at p=1 because freebies override its coin."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T151714Z-sat-noise.json
  accessed_at: '2026-10-11T15:18:42Z'
  support: supports
  summary: 'Compared all 442 pinned AIO labels/scoped synonyms and 316 preceding native
    IDs/names/aliases; no normalized match. Full-checkout text searches included ignored
    and hidden files and returned seven lines each. All seven unique lines were inspected
    and sorted outputs were identical: neighboring GSAT/WalkSAT mentions and saved
    review/ledger references, not existing candidate records. Eight exact AIO nodes
    and four complete native neighbors were inspected. Absence is bounded to this
    snapshot and semantic neighborhood.'
  search_scope: 'All442 pinned AIO labels/scoped synonyms and316 preceding maintained
    IDs/names/aliases; both full checkouts including ignored and hidden files. All
    seven unique text hits inspected, sorted outputs identical: neighboring GSAT/WalkSAT
    mentions and saved references. Additional GWSAT naming aliases from project documentation
    were included in the final scan.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eight exact CLASS nodes with scoped synonyms/comments/outgoing edges in
    source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T15:18:42Z'
  support: supports
  summary: Eight exact AIO CLASS nodes were inspected with definitions, scoped synonyms/comments
    and outgoing edges. All three symbolic SAT-search policies receive bounded no-match
    assessments. Logical formulas do not make a language model; random flips do not
    make a neural noise layer or training strategy. Solving a fixed formula is not
    automatically a learning task, and a possible Markov representation does not establish
    a specific algorithm-to-network-class mapping. Full GSAT, MinConflicts, SimulatedAnnealing
    and QLearning records, read in this and preceding rounds, distinguish global net-gain
    flips, conflicted-variable repair, temperature-dependent acceptance and sampled
    action-value learning. Their prior mappings are context, not newly approved.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T151714Z-sat-noise.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T15:18:42Z'
  support: supports
  summary: Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records distinguish
    global net-gain flips, conflicted-variable repair, temperature-dependent acceptance
    and sampled action-value learning. Their prior mappings are contextual, not newly
    approved.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/sat-noise-boundaries.py
  locator: 'calculate(): variable-union versus clause-first probabilities, unrestricted
    noise, break versus net-gain ranking and zero-break priority'
  accessed_at: '2026-10-11T15:18:42Z'
  snapshot_sha256: 81715afcbf73b63b7cb2185657ae4df3c60b7d807a3e796c784edf5ac638b1e0
  support: supports
  summary: Original finite CNF substitutions distinguish uniform variable-union sampling
    from clause-first sampling, show an unrestricted noise move outside the eligible
    union, separate breakcount from net-gain ranking, and verify that a zero-break
    candidate overrides the SKC noise coin even at p=1. No author solver or benchmark
    was executed.
- evidence_id: gsatwithrandomwalk-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf
  locator: The Random Walk Strategy, PDF2 / printed338; Modifying the Random Walk
    Strategy, PDF5 / printed341, duplicate-free variable list versus clause-first
    WSAT sampling
  accessed_at: '2026-10-11T15:07:33Z'
  snapshot_sha256: fd839ba6780a260e0bcfebcdf169f381ba5b88c27c17981ef4b3dacd144ff1f9
  support: supports
  summary: Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343;
    seven-page publisher scan. The source compares specific parameter settings and
    instance classes, not a universal dominance result. Actual paper and HTML reading
    scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
- evidence_id: gsatwithrandomwalk-source-1
  kind: primary_source
  reference: https://www.cs.cornell.edu/selman/papers/pdf/93.ijcai.gsatext.pdf
  locator: Section3.3 and StrategyIII, PDF4; Section2 and Figure1, PDF1–2, GSAT context
  accessed_at: '2026-10-11T15:08:36Z'
  snapshot_sha256: f301bd7ff353fbcc3b7d089e43be34fa8d224a10dbfcfbca4bb2cfad3b35e4c3
  support: supports
  summary: 'Domain-Independent Extensions to GSAT: Solving Large Structured Satisfiability
    Problems. Six-page author-hosted manuscript marked to appear in Proceedings of
    IJCAI-93. PDF page numbers identify this inspected version; final proceedings
    pagination is not substituted. Actual paper and HTML reading scopes are declared
    in source_analysis; extraction, rendering and a full-text access label do not
    establish that every page was read.'
- evidence_id: gsatwithrandomwalk-source-2
  kind: primary_source
  reference: https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/
  locator: 'GWSAT: GSAT with Random Walk entry; algorithm identifier gwsat'
  accessed_at: '2026-10-11T15:12:59Z'
  snapshot_sha256: 032a526131abb5d2a325a7e3fb4e8aa50d807cdba73121a71466e442931f1193
  support: supports
  summary: Algorithms in UBCSAT. Undated archived project algorithm documentation,
    HTTP snapshot captured during this curation. Only the GWSAT entry and relevant
    index headings were inspected for naming and discovery; catalog bibliographic
    text is not authoritative publication metadata. Actual paper and HTML reading
    scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
- evidence_id: gsatwithrandomnoise-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf
  locator: The Random Walk Strategy, PDF2 / printed338; random-noise variation and
    experimental parameter context, PDF3 / printed339
  accessed_at: '2026-10-11T15:07:33Z'
  snapshot_sha256: fd839ba6780a260e0bcfebcdf169f381ba5b88c27c17981ef4b3dacd144ff1f9
  support: supports
  summary: Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343;
    seven-page publisher scan. The source compares specific parameter settings and
    instance classes, not a universal dominance result. Actual paper and HTML reading
    scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
- evidence_id: walksat-source-0
  kind: primary_source
  reference: https://www.cs.virginia.edu/~rmw7my/papers/walksat.pdf
  locator: PDF/printed1, breakcount/makecount definitions and SKC steps1–3; PDF/printed2,
    variant distinctions and single-run/no-restart competition configuration
  accessed_at: '2026-10-11T15:10:47Z'
  snapshot_sha256: 525f46d2f9fd9d32cc46daee6b15a0ece5fcef17af614e74d6143643ed2cf74f
  support: supports
  summary: Walksat in the 2004 SAT Competition. Two-page author-hosted SAT Competition
    2004 solver description, printed/PDF pp.1–2. Defines the SKC rule and distinguishes
    AutoWalksat and Rnovelty+; this is not documentation for every later software
    version. Actual paper and HTML reading scopes are declared in source_analysis;
    extraction, rendering and a full-text access label do not establish that every
    page was read.
- evidence_id: walksat-source-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1994/AAAI94-051.pdf
  locator: Modifying the Random Walk Strategy, PDF5 / printed341, clause-first WSAT
    lineage and sampling contrast
  accessed_at: '2026-10-11T15:07:33Z'
  snapshot_sha256: fd839ba6780a260e0bcfebcdf169f381ba5b88c27c17981ef4b3dacd144ff1f9
  support: supports
  summary: Noise Strategies for Improving Local Search. AAAI-94 proceedings, pp.337–343;
    seven-page publisher scan. The source compares specific parameter settings and
    instance classes, not a universal dominance result. Actual paper and HTML reading
    scopes are declared in source_analysis; extraction, rendering and a full-text
    access label do not establish that every page was read.
assessments:
- assessment_id: gsatwithrandomwalk
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:GSATWithRandomWalk
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - gsatwithrandomwalk-source-0
  - gsatwithrandomwalk-source-1
  - gsatwithrandomwalk-source-2
  summary: 'This is the mixed random-walk extension of GSAT described by Selman and
    Kautz and clarified in the later noise paper. Its focused move samples a duplicate-free
    union of eligible variables, not a clause followed by one of its variables. The
    latter distribution underlies the separately described WSAT family. It is also
    distinct from unrestricted GSAT random noise and from a pure clause-first walk
    for 2-SAT. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 316 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, returning 7 and
    7 lines respectively. All seven unique lines were inspected, and the sorted checkout
    hit sets were identical: neighboring GSAT/WalkSAT mentions and saved review/ledger
    references, not existing candidate records. Eight exact AIO CLASS nodes with scoped
    synonyms/comments and outgoing edges and four full native neighboring records
    were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  details: 'Maintain a complete assignment of the variables in the input CNF formula.
    Stop successfully when it satisfies the formula. Otherwise, with fixed probability
    p, select uniformly from the distinct variables appearing in at least one currently
    unsatisfied clause and flip the chosen variable. With probability 1−p, evaluate
    all single-variable flips and choose a largest increase in the total number of
    satisfied clauses, breaking tied best choices randomly as in GSAT. The random
    and greedy branches can make non-improving moves. The extension can use the GSAT
    outer random-initialization, per-attempt flip budget and restart/attempt budget.
    The 1994 paper explicitly explains the duplicate-free variable list, which gives
    equal probabilities to eligible variables even when their clause occurrence counts
    differ. The UBCSAT project documents GWSAT as GSAT with Random Walk and associates
    that named implementation with the Selman–Kautz extension. Limits: The focused
    random branch and the global greedy branch use different candidate sets. Replacing
    the former by random-clause-then-random-variable sampling changes the transition
    distribution, even at p=1. Shared behavior at p=0 does not make the full variant
    identical to basic GSAT. Finite search failure is not a proof of unsatisfiability.
    The polynomial analysis cited for pure random walks on satisfiable 2-CNF does
    not establish a corresponding general-CNF bound for this mixture. The noise parameter,
    CNF encoding, initialization and outer budgets affect behavior. No single best
    p, universal speedup or numerical benchmark claim is curated. Empty clauses or
    empty candidate sets require explicit handling outside the described nonempty-variable
    flip rule. The record curates the move policy and its stated GSAT context, not
    an executed solver or a certification of every loop boundary. The original GSAT
    pre-flip-only pseudocode boundary remains an implementation choice to declare.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - gsatwithrandomwalk-source-0
    - gsatwithrandomwalk-source-1
    - gsatwithrandomwalk-source-2
  - name: aio-assessment
    value: bounded_no_match
    definition: Eight exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms/comments and outgoing edges. All three symbolic SAT-search policies
      receive bounded no-match assessments. Logical formulas do not make a language
      model; random flips do not make a neural noise layer or training strategy. Solving
      a fixed formula is not automatically a learning task, and a possible Markov
      representation does not establish a specific algorithm-to-network-class mapping.
      Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records, read in this
      and preceding rounds, distinguish global net-gain flips, conflicted-variable
      repair, temperature-dependent acceptance and sampled action-value learning.
      Their prior mappings are context, not newly approved.
    evidence_ids:
    - mapping
- assessment_id: gsatwithrandomnoise
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:GSATWithRandomNoise
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - gsatwithrandomnoise-source-0
  summary: 'This is the random-noise strategy explicitly contrasted with the focused
    random-walk GSAT strategy in the 1994 primary paper. The defining difference is
    the random branch’s eligible variable set. It is not simulated annealing, Gaussian
    input noise, neural weight noise, or WalkSAT’s clause-first selection. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    316 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in worktree and main, returning 7 and 7 lines respectively.
    All seven unique lines were inspected, and the sorted checkout hit sets were identical:
    neighboring GSAT/WalkSAT mentions and saved review/ledger references, not existing
    candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and
    outgoing edges and four full native neighboring records were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.'
  details: 'Start from a complete assignment for a CNF formula and test whether it
    is satisfying. At a search step, with probability p choose a formula variable
    uniformly and flip it, irrespective of whether it appears in an unsatisfied clause
    or improves the clause count. With probability 1−p take a globally best GSAT flip,
    using the largest increase in the number of satisfied clauses and random tie handling.
    Apply the chosen outer flip and attempt budgets with random restarts as in the
    GSAT experiments. This unrestricted noise replaces the eligible-variable restriction
    in GSAT with random walk. It can perturb a variable whose current occurrences
    are all in satisfied clauses, and it uses no temperature-dependent acceptance
    test. Limits: A noise move need not help satisfy a currently violated clause and
    can break previously satisfied clauses. Conversely, the mechanism does not assert
    that every random move is uphill. Finite search failure is inconclusive about
    satisfiability. Empirical comparisons on the paper’s selected instances and tuned
    settings are not universal performance orderings or general runtime bounds. At
    p=0 the move policy reduces to basic GSAT, while p=1 selects only unrestricted
    random flips; the entire parameterized policy is not identical to either endpoint.
    The formula’s variable universe and treatment of empty clauses/candidate sets
    must be explicit. The record describes the source’s noise policy, not an executed
    reference implementation, a weighted MAX-SAT extension or automatic parameter
    adaptation. It does not silently repair the original GSAT final-flip check boundary.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - gsatwithrandomnoise-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: Eight exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms/comments and outgoing edges. All three symbolic SAT-search policies
      receive bounded no-match assessments. Logical formulas do not make a language
      model; random flips do not make a neural noise layer or training strategy. Solving
      a fixed formula is not automatically a learning task, and a possible Markov
      representation does not establish a specific algorithm-to-network-class mapping.
      Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records, read in this
      and preceding rounds, distinguish global net-gain flips, conflicted-variable
      repair, temperature-dependent acceptance and sampled action-value learning.
      Their prior mappings are context, not newly approved.
    evidence_ids:
    - mapping
- assessment_id: walksat
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:WalkSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - walksat-source-0
  - walksat-source-1
  summary: 'This record curates the classical SKC variable-selection rule under the
    commonly used WalkSAT name. It does not equate every later WalkSAT heuristic,
    the earlier underspecified WSAT family description, pure clause-first random walk,
    or global GSAT-with-walk selection with that exact rule. The 1994 source gives
    the clause-first lineage; the authors’ 2004 solver description explicitly supplies
    the zero-break priority and breakcount-based choice. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 316 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, returning 7 and 7 lines respectively. All seven unique
    lines were inspected, and the sorted checkout hit sets were identical: neighboring
    GSAT/WalkSAT mentions and saved review/ledger references, not existing candidate
    records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing
    edges and four full native neighboring records were inspected. Absence is bounded
    to this snapshot and semantic neighborhood.'
  details: 'Maintain a complete truth assignment and stop successfully when all clauses
    are satisfied. Otherwise randomly choose an unsatisfied nonempty clause. For each
    candidate variable in that clause, its breakcount is the number of currently satisfied
    clauses that would become unsatisfied if it were flipped. If any candidate has
    breakcount zero, choose one such candidate at random. Only when there is no zero-break
    candidate, choose a random variable from the selected clause with probability
    p; with probability 1−p choose a candidate of minimum breakcount, breaking ties
    randomly. Flip the chosen variable and repeat under the application’s stopping
    budget. Breakcount omits how many previously unsatisfied clauses become satisfied,
    so it need not rank candidates like GSAT’s global net-gain score. Random restarts
    are an optional outer strategy; the described 2004 competition configuration uses
    one long run. Limits: The zero-break branch precedes the noise coin, including
    at p=1. That setting is therefore not generally identical to a pure random-clause/random-variable
    walk. Removing the priority changes the specified SKC heuristic. Candidate selection
    is restricted to the chosen clause and can miss the globally best net-gain flip.
    Minimizing breakcount is different from minimizing breakcount minus makecount;
    replacing one by the other changes the heuristic. A finite unsuccessful run does
    not prove UNSAT, and the pure 2-CNF random-walk guarantee is not automatically
    a guarantee for this SKC policy on general formulas. The noise setting and restart
    strategy are not universal constants. The move rule needs a nonempty selected
    clause and a declared formula representation. Empty clauses require separate handling;
    duplicate clauses, literal normalization and weighted extensions can change counts
    or sampling and are not silently normalized here. AutoWalksat, Rnovelty, Rnovelty+
    and later software additions are distinct procedures or configurations, not exact
    aliases of this SKC record. No author implementation or numerical solver benchmark
    was run.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - walksat-source-0
    - walksat-source-1
  - name: aio-assessment
    value: bounded_no_match
    definition: Eight exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms/comments and outgoing edges. All three symbolic SAT-search policies
      receive bounded no-match assessments. Logical formulas do not make a language
      model; random flips do not make a neural noise layer or training strategy. Solving
      a fixed formula is not automatically a learning task, and a possible Markov
      representation does not establish a specific algorithm-to-network-class mapping.
      Full GSAT, MinConflicts, SimulatedAnnealing and QLearning records, read in this
      and preceding rounds, distinguish global net-gain flips, conflicted-variable
      repair, temperature-dependent acceptance and sampled action-value learning.
      Their prior mappings are context, not newly approved.
    evidence_ids:
    - mapping
- assessment_id: gwsat-boundaries
  area: consistency
  topic: Focused variable sampling and global greedy flips
  outcome: supported
  target_ids:
  - AIMech:GSATWithRandomWalk
  evidence_ids:
  - gsatwithrandomwalk-source-0
  - gsatwithrandomwalk-source-1
  - gsatwithrandomwalk-source-2
  - finite-conventions
  summary: Retain the mixed GSAT walk policy, distinct from clause-first sampling.
  details: The1993 StrategyIII mixes a variable in some unsatisfied clause with the
    standard global GSAT best move. The1994 paper clarifies that its focused branch
    uses a duplicate-free variable list. The finite example yields1/3 each for three
    eligible variables, whereas pure clause-first selection yields1/2,1/4,1/4. The
    GWSAT alias is supported by project documentation; its access level is documentation
    and its malformed catalog bibliography is not adopted. Finite failure, outer budgets
    and the original GSAT final-flip check boundary remain explicit.
- assessment_id: noise-boundaries
  area: consistency
  topic: Unrestricted noise versus focused walk and annealing
  outcome: supported
  target_ids:
  - AIMech:GSATWithRandomNoise
  evidence_ids:
  - gsatwithrandomnoise-source-0
  - finite-conventions
  summary: Retain the explicitly named unrestricted random-noise variant.
  details: The1994 source removes the eligible-variable restriction from the random
    branch, preserving the GSAT greedy branch. The finite example has a variable outside
    the unsatisfied-clause union whose flip breaks a satisfied clause. No temperature
    acceptance test is involved. Shared p=0 behavior does not make the complete parameterized
    policy identical to the focused variant; no universal performance ordering is
    asserted.
- assessment_id: walksat-boundaries
  area: consistency
  topic: Clause-first SKC selection, freebies and breakcount
  outcome: supported
  target_ids:
  - AIMech:WalkSAT
  evidence_ids:
  - walksat-source-0
  - walksat-source-1
  - finite-conventions
  summary: Retain classical SKC with explicitly bounded use of the WalkSAT name.
  details: 'The2004 primary solver description specifies zero-break choice before
    the random/greedy coin and distinguishes breakcount from makecount. The finite
    cases show the freebie override at p=1 and a break-only ranking opposite to net-gain
    ranking. The earlier1994 WSAT description is lineage context, not evidence that
    every variant implements the exact SKC rule. Optional restarts are accurately
    scoped: the2004 competition configuration used one long run. The record does not
    inherit the pure2-CNF random-walk bound for arbitrary formulas or report failure
    as UNSAT.'
- assessment_id: mapping-boundaries
  area: grounding
  topic: SAT move policies versus learning/model/layer classes
  outcome: supported
  target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three native identities with bounded no-match assessments.
  details: Eight exact AIO CLASS nodes were inspected with definitions, scoped synonyms/comments
    and outgoing edges. All three symbolic SAT-search policies receive bounded no-match
    assessments. Logical formulas do not make a language model; random flips do not
    make a neural noise layer or training strategy. Solving a fixed formula is not
    automatically a learning task, and a possible Markov representation does not establish
    a specific algorithm-to-network-class mapping. Full GSAT, MinConflicts, SimulatedAnnealing
    and QLearning records, read in this and preceding rounds, distinguish global net-gain
    flips, conflicted-variable repair, temperature-dependent acceptance and sampled
    action-value learning. Their prior mappings are context, not newly approved.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:GSATWithRandomWalk
  - AIMech:GSATWithRandomNoise
  - AIMech:WalkSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - gsatwithrandomwalk-source-0
  - gsatwithrandomwalk-source-1
  - gsatwithrandomwalk-source-2
  - gsatwithrandomnoise-source-0
  - walksat-source-0
  - walksat-source-1
  rationale: Uniform variable-union sampling, unrestricted noise and clause-first
    selection with zero-break priority define different move policies. Shared GSAT
    lineage, parameter endpoints and SAT applications do not establish identity.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- Finite search failure is not an UNSAT proof. Pure random-walk bounds do not automatically
  cover the curated mixed policies on arbitrary formulas.
- The WalkSAT record explicitly scopes the classical SKC rule; later variants, weighted
  extensions and source-code boundary conventions are not silently included.
- Only declared PDF/OCR/HTML scopes were inspected. The UBCSAT page supports naming,
  not a full-catalog implementation audit. No author solver or numerical benchmark
  was executed.
- There are188 pending inspection leads plus unresolved dispositions; discovery remains
  active.
links: []
tags:
- native-concepts
- sat-search
- self-review
- discovery-ongoing
```
