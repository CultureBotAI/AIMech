# Scientific self-review of local-search frameworks

- Review: 20261011T142110Z-local-search-frameworks
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T14:18:42Z
- Finished UTC: 2026-10-11T14:21:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Tabu Search, Guided Local Search and Iterated Local Search with explicit memory, penalty, acceptance and AIO boundaries. One minor provenance finding is resolved; no actionable finding remains within the declared scope.

## Scope And Provenance

All fields of three new maintained local-search framework records.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 3d674f776b786af1a882a6a5c793652d081a19f8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TabuSearch | data/curated/TabuSearch.yaml | maintained | Tabu search |
| AIMech:GuidedLocalSearch | data/curated/GuidedLocalSearch.yaml | maintained | Guided local search |
| AIMech:IteratedLocalSearch | data/curated/IteratedLocalSearch.yaml | maintained | Iterated local search |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 73.44s (0:01:13)<br>Checked 442 record(s); 0 failed.<br>Checked 304 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 80 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 78,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch | Command exited 0 with no output. |
| Finite local-search boundary examples | passed | True | AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch | {"tabu_tenure_one_cycle": ["A", "B", "C", "A"], "tabu_path_costs": [0, 1, 2, 0], "best_admissible_without_aspiration": 7, "with_declared_aspiration": 2, "gls_utilities": [2.0, 2.0, 0.0], "gls_tied_penalty_updates": [2, 1, 0], "gls_augmented_cost": 16, "equal_penalties_variable_cardinality": [16, 21], "equal_penalties_fixed_cardinality": [16, 15], "all_zero_utility_all_feature_ties": [0, 1], "present_only_ties": [0], "ils_optimized_candidate": "B", "ils_intermediate_cost": 100, "better_accepts_worse": false, "always_accepts_worse": true, "interpretation": "One-step reversal memory permits a longer cycle; a specified aspiration rule changes admissibility. GLS updates all positive-utility ties and must declare the all-zero case. Common penalties cancel only at fixed feature count. ILS tests the optimized candidate and supports different acceptance rules. These are finite boundary examples, not convergence proofs or performance tests."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations and bounded no-match assessment

evidence: supported. Targets: AIMech:TabuSearch.

This record denotes the tabu-search framework through the original Part I formulation. It is not merely a list of visited nodes, Ant System’s per-tour feasibility list, or a global best-first frontier. Recency restrictions, aspiration and longer-term memory are configurable mechanisms; no single fixed tenure or exact prohibition rule defines all variants. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 301 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 37 and 37 lines respectively. All 13 unique hit contents were inspected: prior local-search candidate leads, Ant System’s feasibility-list distinction, and their saved reports/reviews. These were references to methods rather than existing candidate records. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain the current solution, the best solution found, a neighborhood of applicable moves and memory-based tabu conditions on moves or their attributes. In the simple cost-minimizing version, choose the best admissible candidate under the configured evaluator even when every admissible move worsens the current objective, move there, and update the best-so-far record only on improvement. Update tabu memory so recent reversals or selected attributes remain restricted for a declared tenure, then expire restrictions according to that rule. Attribute-based restrictions can exclude unvisited solutions that share an attribute with a recent move. In the aspiration extension, a move satisfying the declared aspiration criterion can be admissible despite tabu status. Candidate sampling or approximate evaluation may replace full-neighborhood minimization. Intermediate-term memory can intensify search around features of good solutions, while longer-term frequency information can diversify it toward underexplored features; these are framework components whose concrete rules must be specified. Limits: Finite recency memory is not a proof of cycle freedom or eventual global optimality. Attribute-based restrictions can exclude useful unvisited moves, and aspiration overrides must be designed with their effect on cycling in mind. The Part II finiteness construction was not inspected or generalized here. The simple pseudocode stops when no admissible move exists, while the subsequent prose describes releasing oldest restrictions to restore a move. These are distinct handling choices; the conceptual record does not silently present them as one fully specified executable algorithm. Tabu tenure, attributes, aspiration thresholds, candidate lists, move connectivity, initialization and stopping affect the search. Choosing the best currently admissible move does not imply monotonic objective improvement or a globally optimal final solution. The source also discusses probabilistic, strategic-oscillation and mixed-integer extensions. This record does not instantiate all variants or curate performance comparisons. Memory-based search need not be a reinforcement-learning task.

### Identity, definition, mechanism, limitations and bounded no-match assessment

evidence: supported. Targets: AIMech:GuidedLocalSearch.

GLS is the named feature-penalty procedure, not all tabu search, a hard prohibition of recently visited moves, or Fast Local Search (FLS), which is a separately combinable neighborhood-reduction technique. The authors relate GLS to the broader tabu-search framework; that relationship does not make every tabu algorithm and the specified GLS update identical. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 301 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 37 and 37 lines respectively. All 13 unique hit contents were inspected: prior local-search candidate leads, Ant System’s feasibility-list distinction, and their saved reports/reviews. These were references to methods rather than existing candidate records. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Choose binary indicators I_i(s) for nontrivial solution features, feature costs c_i, a local-search procedure and penalty scale lambda. In the inspected basic formulation the c_i are fixed and nonnegative, and penalties p_i start at zero. Repeatedly run local search from the current solution using h(s)=g(s)+lambda*sum_i p_i*I_i(s), where g is the original cost. At an h-local minimum s_star, compute u_i=I_i(s_star)*c_i/(1+p_i). In the nondegenerate case of positive maximum utility, increment p_i by one for every feature tied at that maximum, then resume local search from the same solution under the modified h. Penalization can repeat without an intervening move. Feature costs enter the utility ranking, not as extra multipliers in the displayed penalty sum. Retain and return the best solution found according to g, rather than choosing it by the changing augmented objective. FLS and other accelerations may be combined with the local-search subroutine but are not required by this baseline. Limits: The source allows zero feature costs. If every utility is zero, the all-feature pseudocode makes absent features tie with present ones, whereas the prose says only local-minimum features are penalized. A concrete implementation must declare its zero-utility and eligible-feature convention; the record’s stated update is restricted to the positive-maximum case. Curator qualification of Equation 1: equal penalties contribute lambda*p times the number of active features. They cancel from move-cost differences only when that feature count is unchanged. The source’s equal-penalty cancellation statement is therefore not universal for variable-cardinality feature sets. Penalties are finite soft costs, not hard prohibitions. Their effect depends on lambda, objective scale, feature definition, move set and stopping. At lambda=0 the guidance vanishes; increasing penalties does not prove escape from every basin or convergence to a global optimum. Local minima are relative to h and the chosen neighborhood, not necessarily g. A deterministic penalty update does not make an entire implementation deterministic if its initial solution or local-search routine is randomized. The manuscript’s TSP comparisons do not establish universal superiority, and no benchmark results are curated.

### Identity, definition, mechanism, limitations and bounded no-match assessment

evidence: supported. Targets: AIMech:IteratedLocalSearch.

The ILS framework includes the common local-minimum formulation but permits a more general, possibly stochastic or history-dependent embedded optimizer. Historical names such as iterated Lin–Kernighan and large-step Markov chains denote particular developments, not exact aliases of every ILS configuration. Single-chain search distinguishes the framework from population selection and distribution refitting; optional restarts and hybrids require their own declared choices. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 301 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 37 and 37 lines respectively. All 13 unique hit contents were inspected: prior local-search candidate leads, Ant System’s feasibility-list distinction, and their saved reports/reviews. These were references to methods rather than existing candidate records. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Generate an initial solution and apply the embedded LocalSearch routine to obtain a current optimized solution. Repeat: perturb that current solution, apply LocalSearch to the perturbed intermediate point, then use an acceptance criterion comparing the current and candidate optimized solutions, potentially with search history, to choose the next current solution. Repeat until the declared termination condition. In the simplified deterministic memoryless setting, LocalSearch maps candidates into a reduced set of local optima, and perturbation followed by local search induces transitions among them. The general framework need not explicitly enumerate neighborhoods in that reduced space. Accepted variants include retaining only strict improvements, always accepting the newly optimized candidate, or temperature-dependent acceptance; improvement-only selection is not a universal requirement. Perturbation and acceptance may use history, and the embedded procedure can itself be stochastic or use memory. Limits: Perturbations that are too weak can return repeatedly to the same optimizer output; independent large perturbations remove the current solution’s influence from proposed starts and approach random-restart behavior. The full behavior still depends on the acceptance rule and the embedded optimizer. A deterministic memoryless embedded routine supports the simplified basin-of-attraction picture. General stochastic or history-dependent routines need not define the same fixed partition; history-free transition descriptions cannot be assumed for every ILS variant. Transitions between optimized solutions need not be reversible, and deterministic perturbations can produce short cycles. The framework alone is neither a target-invariant MCMC sampler nor a global-optimality or cycle-freedom guarantee. Initialization, perturbation, local-search termination, acceptance, best-so-far bookkeeping and restart conventions must be declared for an executable instance. The source reports sensitivity to module interactions, including settings worse than random restart; no universal performance ranking or empirical result is curated.

### Memory, admissibility and aspiration

consistency: supported. Targets: AIMech:TabuSearch.

Retain adaptive-memory search separately from a feasibility list.

Best admissible moves may worsen the objective while a separate best-so-far solution is retained. Attributes can prohibit unvisited states; aspiration can override restrictions. Finite reversal memory does not guarantee absence of longer cycles. Empty admissible sets stop the simple pseudocode, whereas later prose relaxes oldest restrictions: the record preserves the variant choice. Intermediate/long-term memory and probabilistic selection are not silently mandatory. Issue 87 is resolved by describing the observed footer without dating insertion.

### Feature utilities, ties and objective modification

consistency: supported. Targets: AIMech:GuidedLocalSearch.

Retain the specific penalty scheme with explicit numerical boundaries.

The augmented objective is g+lambda*sum(p_i*I_i), without multiplying by feature costs again. Costs enter I_i*c_i/(1+p_i); all positive maximum ties are penalized. The source prose and all-feature pseudocode leave an all-zero utility ambiguity, which is retained. Equal penalties preserve ordering only under constant active-feature count; the finite counterexample prevents overgeneralizing the source statement. Return the best original objective, not the lowest changing augmented objective. FLS is optional and the broader tabu-family relationship does not establish exact identity.

### Perturbation, reoptimization and acceptance

consistency: supported. Targets: AIMech:IteratedLocalSearch.

Retain a single-chain framework over embedded-optimizer outputs.

Acceptance tests the optimized candidate, not the intermediate perturbation. Strict improvement, unconditional acceptance and temperature-based acceptance are separate supported choices. Deterministic memoryless local minimization is a simplifying case; the source permits history and stochastic or other embedded optimizers. Independent large perturbations do not erase the acceptance rule. Neither global convergence, reversibility nor fixed stationary distributions follow from the generic framework.

### General optimization and AIO learning classes

grounding: supported. Targets: AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch.

Retain all three native identities with bounded no-match assessments.

Six exact AIO CLASS nodes were inspected with definitions, scoped synonyms, comments and outgoing edges: TrainingStrategy, MachineLearningTask, ReinforcementLearning, ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain. All three general optimization frameworks receive bounded aio_no_match assessments with six explicit rejection reasons. Optional learning applications, search-memory terminology and stochastic representations do not establish the identity of a learning task, language model or stochastic-model class. Seven native neighbors were read in full: simulated annealing, cross-entropy optimization, genetic algorithms, A-star, best-first search, ACO and Ant System. Local trajectory moves differ from global frontier expansion, population evolution, distribution fitting and constructive pheromone search. Ant System’s per-tour tabu list is feasibility memory rather than the tabu-search framework; GLS’s relation to the broader tabu family does not equate its particular penalty update with every member. Earlier neighboring records’ mappings were contextual evidence, not newly approved by this review.

## Findings

### tabu-scan-provenance: The footer’s date is treated as its insertion date.

minor / resolved / confirmed; issue key: CultureBotAI-AIMech-TabuSearch-scan-provenance.

The initial draft inferred that the footer was added in 2001. The maintained record now describes only the observed notice and preserves the distinct 1989 article date.

Disposition: The source version now states that the scan contains a 2001 copyright footer and that insertion time is not established. The 1989 publication identity and checksum are preserved. Ledger and append-only history were synchronized; changed inputs were reinspected and the post-fix gate passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:TabuSearch, AIMech:GuidedLocalSearch, AIMech:IteratedLocalSearch. Adaptive tabu restrictions, feature-penalized objectives and perturb/reoptimize/accept chains have distinct defining mechanisms. The source recognizes family overlap without establishing exact identity.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T141428Z-local-search-frameworks.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 301 preceding native IDs/names/aliases, including historical taboo/iterated-descent/chained-search terms. No normalized identity match was found. Full-checkout fixed-string searches included ignored/hidden files and returned 37 lines in both worktree and main. All 13 unique contents were inspected: prior candidate leads, Ant System feasibility-list distinctions, and their saved reviews/reports. Six exact AIO CLASS nodes and seven native neighboring records were read. Absence is bounded to this source snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Six exact CLASS nodes and outgoing edges in source_analysis.aio_mapping_inspection | supports | Six exact AIO CLASS nodes were inspected with definitions, scoped synonyms, comments and outgoing edges: TrainingStrategy, MachineLearningTask, ReinforcementLearning, ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain. All three general optimization frameworks receive bounded aio_no_match assessments with six explicit rejection reasons. Optional learning applications, search-memory terminology and stochastic representations do not establish the identity of a learning task, language model or stochastic-model class. Seven native neighbors were read in full: simulated annealing, cross-entropy optimization, genetic algorithms, A-star, best-first search, ACO and Ant System. Local trajectory moves differ from global frontier expansion, population evolution, distribution fitting and constructive pheromone search. Ant System’s per-tour tabu list is feasibility memory rather than the tabu-search framework; GLS’s relation to the broader tabu family does not equate its particular penalty update with every member. Earlier neighboring records’ mappings were contextual evidence, not newly approved by this review. |
| neighbors | research/discovery/20261011T141428Z-local-search-frameworks.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Seven native neighbors were read: simulated annealing, cross-entropy optimization, genetic algorithm, A-star, best-first search, ACO and Ant System. Their identity boundaries were assessed without approving all older claims or mappings. |
| finite-conventions | research/discovery/local-search-frameworks-boundaries.py; calculate(): tabu cycle and aspiration; GLS ties and penalty cancellation; ILS optimized-candidate acceptance | supports | Original finite examples expose a longer cycle under one-step reversal memory, aspiration-dependent admissibility, GLS positive ties and zero-utility ambiguity, the feature-cardinality condition for penalty cancellation, and acceptance of optimized ILS candidates. These are boundary calculations, not complete implementations, benchmarks or convergence proofs. |
| tabusearch-source-0 | https://leeds-faculty.colorado.edu/glover/TS%20-%20Part%20I-ORSA-aw.pdf; Section 2, PDF pp.2–4 / journal pp.191–193, Simple Tabu Search and attribute restrictions; Sections 3–4, PDF pp.6–7 / journal pp.195–196, aspiration; Section 8, PDF pp.10–11 / journal pp.199–200, intensification and diversification | supports | Tabu Search—Part I. ORSA Journal on Computing 1(3):190–206 (1989), 17-page author-hosted journal scan. The scan contains a 2001 copyright footer, distinct from the verified 1989 publication date; the footer’s insertion date is not established. Declared text and visual scopes are recorded in the ledger. Tabu PDF p.1 was additionally viewed during the successor review; extraction alone is not visual inspection. No author code or benchmark was run. |
| guidedlocalsearch-source-0 | https://bracil.net/CSP/papers/VouTsa-GlsTsP-Ejor99.pdf; Sections 3.1–3.3, manuscript/PDF pp.7–12, Equations 1–2 and Figure 1; Section 3.4, p.13; Section 4.2, pp.18–20; conclusions, pp.53–54 | supports | Guided Local Search and Its Application to the Traveling Salesman Problem. 62-page author manuscript, cover marked accepted March 1998 and bibliographically linked to European Journal of Operational Research 113(2):469–499 (March 1999). Locators use manuscript/PDF pages, not the shorter journal pagination. Declared text and visual scopes are recorded in the ledger. Tabu PDF p.1 was additionally viewed during the successor review; extraction alone is not visual inspection. No author code or benchmark was run. |
| iteratedlocalsearch-source-0 | https://arxiv.org/pdf/math/0102188v1; Introduction, PDF pp.1–2; Sections 2.1–2.4, PDF pp.3–9, framework assumptions and pseudocode across pp.7–8; Section 3.3, PDF pp.19–21, acceptance variants and problem dependence | supports | Iterated Local Search. arXiv:math/0102188v1, submitted 23 February 2001, 49-page chapter manuscript. The later handbook chapter and 2010/2019 revisions are not silently substituted. Declared text and visual scopes are recorded in the ledger. Tabu PDF p.1 was additionally viewed during the successor review; extraction alone is not visual inspection. No author code or benchmark was run. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- The initial provenance review compressed extracted-header and visual-footer inspection into one visual locator. Before that review, Tabu PDF p.1 was read as extracted text and p.3 was viewed. PDF p.1 was additionally viewed during this successor review, confirming the 1989 header and 2001 footer; this is not a retroactive claim of earlier visual inspection.
- Only declared pages were inspected. No author code, benchmark or full convergence-proof audit was performed.
- GLS zero-utility behavior and equal-penalty cardinality conditions remain explicit. The ILS source is arXiv v1 (2001), not a later handbook revision.
- Three additions leave 177 pending inspection leads plus other unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T142110Z-local-search-frameworks
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of local-search frameworks
started_at: '2026-10-11T14:18:42Z'
finished_at: '2026-10-11T14:21:10Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed three records using
    declared primary text, critical PDF images, six exact AIO nodes, seven native
    neighbors and original finite calculations. Issue 87 was recorded and corrected.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Tabu Search, Guided Local Search and Iterated Local Search with explicit
  memory, penalty, acceptance and AIO boundaries. One minor provenance finding is
  resolved; no actionable finding remains within the declared scope.
source:
  git_revision: 3d674f776b786af1a882a6a5c793652d081a19f8
  state: working_tree
  inputs:
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: context
  - path: data/curated/AntColonyOptimization.yaml
    sha256: d65642ea5cac777843fa0285d27a8b8bc129c2544528ba122c7144c0eb794f9d
    role: context
  - path: data/curated/AntSystem.yaml
    sha256: 89aa5c8e5a5d8ae3717bcd5c3be94d32543402900872533c1c4a6bbdf41f506c
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/GuidedLocalSearch.yaml
    sha256: 91618dff5e0ed6681aad81deb9be9c8e35ed43b42acad285ef473916852cdebc
    role: target
  - path: data/curated/IteratedLocalSearch.yaml
    sha256: 15a6a25711dabac3dff72b612cf7daa7a2ae5f9660a9a677c2d21163335f2ef0
    role: target
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/TabuSearch.yaml
    sha256: 6dae782f4d0c0b2a7195f471b7f73acb38fa036fb43ec15bacfa8f9a0264b844
    role: target
  - path: research/discovery/20261011T141428Z-local-search-frameworks.json
    sha256: ad35afc42b0ca69791dc3e860d34a6ef68320a368bfb6bfed33665f8e3ea8c79
    role: context
  - path: research/discovery/local-search-frameworks-boundaries.py
    sha256: d602b6d0ee9cfcc2511de28b722eb648c42756bb847d6d1e5a7eed6b1345a25f
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
- target_id: AIMech:TabuSearch
  path: data/curated/TabuSearch.yaml
  label: Tabu search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearch.yaml
    role: maintained
- target_id: AIMech:GuidedLocalSearch
  path: data/curated/GuidedLocalSearch.yaml
  label: Guided local search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GuidedLocalSearch.yaml
    role: maintained
- target_id: AIMech:IteratedLocalSearch
  path: data/curated/IteratedLocalSearch.yaml
  label: Iterated local search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IteratedLocalSearch.yaml
    role: maintained
scope:
  description: All fields of three new maintained local-search framework records.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbor inspection establishes boundaries, not a new complete review
      of older records.
  - target: Unread pages, implementations and benchmarks
    reason: Only declared source sections and images and finite curator calculations
      were inspected.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 73.44s (0:01:13)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 304 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 80 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 78,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
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
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Finite local-search boundary examples
  command: python3 research/discovery/local-search-frameworks-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  exit_code: 0
  expected_exit_code: 0
  summary: '{"tabu_tenure_one_cycle": ["A", "B", "C", "A"], "tabu_path_costs": [0,
    1, 2, 0], "best_admissible_without_aspiration": 7, "with_declared_aspiration":
    2, "gls_utilities": [2.0, 2.0, 0.0], "gls_tied_penalty_updates": [2, 1, 0], "gls_augmented_cost":
    16, "equal_penalties_variable_cardinality": [16, 21], "equal_penalties_fixed_cardinality":
    [16, 15], "all_zero_utility_all_feature_ties": [0, 1], "present_only_ties": [0],
    "ils_optimized_candidate": "B", "ils_intermediate_cost": 100, "better_accepts_worse":
    false, "always_accepts_worse": true, "interpretation": "One-step reversal memory
    permits a longer cycle; a specified aspiration rule changes admissibility. GLS
    updates all positive-utility ties and must declare the all-zero case. Common penalties
    cancel only at fixed feature count. ILS tests the optimized candidate and supports
    different acceptance rules. These are finite boundary examples, not convergence
    proofs or performance tests."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T141428Z-local-search-frameworks.json
  accessed_at: '2026-10-11T14:18:42Z'
  support: supports
  summary: 'Compared all 442 pinned AIO labels/scoped synonyms and 301 preceding native
    IDs/names/aliases, including historical taboo/iterated-descent/chained-search
    terms. No normalized identity match was found. Full-checkout fixed-string searches
    included ignored/hidden files and returned 37 lines in both worktree and main.
    All 13 unique contents were inspected: prior candidate leads, Ant System feasibility-list
    distinctions, and their saved reviews/reports. Six exact AIO CLASS nodes and seven
    native neighboring records were read. Absence is bounded to this source snapshot
    and semantic neighborhood.'
  search_scope: All 442 pinned AIO identities/scoped synonyms and 301 prior native
    IDs/names/aliases; historical taboo and iterated-descent terminology; both complete
    checkouts including ignored/hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Six exact CLASS nodes and outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T14:18:42Z'
  support: supports
  summary: 'Six exact AIO CLASS nodes were inspected with definitions, scoped synonyms,
    comments and outgoing edges: TrainingStrategy, MachineLearningTask, ReinforcementLearning,
    ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain. All three general optimization
    frameworks receive bounded aio_no_match assessments with six explicit rejection
    reasons. Optional learning applications, search-memory terminology and stochastic
    representations do not establish the identity of a learning task, language model
    or stochastic-model class. Seven native neighbors were read in full: simulated
    annealing, cross-entropy optimization, genetic algorithms, A-star, best-first
    search, ACO and Ant System. Local trajectory moves differ from global frontier
    expansion, population evolution, distribution fitting and constructive pheromone
    search. Ant System’s per-tour tabu list is feasibility memory rather than the
    tabu-search framework; GLS’s relation to the broader tabu family does not equate
    its particular penalty update with every member. Earlier neighboring records’
    mappings were contextual evidence, not newly approved by this review.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T141428Z-local-search-frameworks.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T14:18:42Z'
  support: supports
  summary: 'Seven native neighbors were read: simulated annealing, cross-entropy optimization,
    genetic algorithm, A-star, best-first search, ACO and Ant System. Their identity
    boundaries were assessed without approving all older claims or mappings.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/local-search-frameworks-boundaries.py
  locator: 'calculate(): tabu cycle and aspiration; GLS ties and penalty cancellation;
    ILS optimized-candidate acceptance'
  accessed_at: '2026-10-11T14:18:42Z'
  snapshot_sha256: d602b6d0ee9cfcc2511de28b722eb648c42756bb847d6d1e5a7eed6b1345a25f
  support: supports
  summary: Original finite examples expose a longer cycle under one-step reversal
    memory, aspiration-dependent admissibility, GLS positive ties and zero-utility
    ambiguity, the feature-cardinality condition for penalty cancellation, and acceptance
    of optimized ILS candidates. These are boundary calculations, not complete implementations,
    benchmarks or convergence proofs.
- evidence_id: tabusearch-source-0
  kind: primary_source
  reference: https://leeds-faculty.colorado.edu/glover/TS%20-%20Part%20I-ORSA-aw.pdf
  locator: Section 2, PDF pp.2–4 / journal pp.191–193, Simple Tabu Search and attribute
    restrictions; Sections 3–4, PDF pp.6–7 / journal pp.195–196, aspiration; Section
    8, PDF pp.10–11 / journal pp.199–200, intensification and diversification
  accessed_at: '2026-10-11T14:07:24Z'
  snapshot_sha256: fb1102afc415eb0d9d7e2a8ced4ec7047d1fea2f47c74c16e7cd8be290ea5a1a
  support: supports
  summary: Tabu Search—Part I. ORSA Journal on Computing 1(3):190–206 (1989), 17-page
    author-hosted journal scan. The scan contains a 2001 copyright footer, distinct
    from the verified 1989 publication date; the footer’s insertion date is not established.
    Declared text and visual scopes are recorded in the ledger. Tabu PDF p.1 was additionally
    viewed during the successor review; extraction alone is not visual inspection.
    No author code or benchmark was run.
- evidence_id: guidedlocalsearch-source-0
  kind: primary_source
  reference: https://bracil.net/CSP/papers/VouTsa-GlsTsP-Ejor99.pdf
  locator: Sections 3.1–3.3, manuscript/PDF pp.7–12, Equations 1–2 and Figure 1; Section
    3.4, p.13; Section 4.2, pp.18–20; conclusions, pp.53–54
  accessed_at: '2026-10-11T14:07:24Z'
  snapshot_sha256: 4550ebdad45d6d164b48525a4a71d9c29063e7bc2876a3302234b5ecc294b93f
  support: supports
  summary: Guided Local Search and Its Application to the Traveling Salesman Problem.
    62-page author manuscript, cover marked accepted March 1998 and bibliographically
    linked to European Journal of Operational Research 113(2):469–499 (March 1999).
    Locators use manuscript/PDF pages, not the shorter journal pagination. Declared
    text and visual scopes are recorded in the ledger. Tabu PDF p.1 was additionally
    viewed during the successor review; extraction alone is not visual inspection.
    No author code or benchmark was run.
- evidence_id: iteratedlocalsearch-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/math/0102188v1
  locator: Introduction, PDF pp.1–2; Sections 2.1–2.4, PDF pp.3–9, framework assumptions
    and pseudocode across pp.7–8; Section 3.3, PDF pp.19–21, acceptance variants and
    problem dependence
  accessed_at: '2026-10-11T14:07:24Z'
  snapshot_sha256: 6e60a8114c7d188e2b90d558a4e4387a9fab1b94b14768830ece01fa9175a070
  support: supports
  summary: Iterated Local Search. arXiv:math/0102188v1, submitted 23 February 2001,
    49-page chapter manuscript. The later handbook chapter and 2010/2019 revisions
    are not silently substituted. Declared text and visual scopes are recorded in
    the ledger. Tabu PDF p.1 was additionally viewed during the successor review;
    extraction alone is not visual inspection. No author code or benchmark was run.
assessments:
- assessment_id: tabusearch
  area: evidence
  topic: Identity, definition, mechanism, limitations and bounded no-match assessment
  outcome: supported
  target_ids:
  - AIMech:TabuSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - tabusearch-source-0
  summary: 'This record denotes the tabu-search framework through the original Part
    I formulation. It is not merely a list of visited nodes, Ant System’s per-tour
    feasibility list, or a global best-first frontier. Recency restrictions, aspiration
    and longer-term memory are configurable mechanisms; no single fixed tenure or
    exact prohibition rule defines all variants. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 301 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, returning 37 and 37 lines respectively. All 13 unique
    hit contents were inspected: prior local-search candidate leads, Ant System’s
    feasibility-list distinction, and their saved reports/reviews. These were references
    to methods rather than existing candidate records. Six exact AIO CLASS nodes with
    scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms
    were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  details: 'Maintain the current solution, the best solution found, a neighborhood
    of applicable moves and memory-based tabu conditions on moves or their attributes.
    In the simple cost-minimizing version, choose the best admissible candidate under
    the configured evaluator even when every admissible move worsens the current objective,
    move there, and update the best-so-far record only on improvement. Update tabu
    memory so recent reversals or selected attributes remain restricted for a declared
    tenure, then expire restrictions according to that rule. Attribute-based restrictions
    can exclude unvisited solutions that share an attribute with a recent move. In
    the aspiration extension, a move satisfying the declared aspiration criterion
    can be admissible despite tabu status. Candidate sampling or approximate evaluation
    may replace full-neighborhood minimization. Intermediate-term memory can intensify
    search around features of good solutions, while longer-term frequency information
    can diversify it toward underexplored features; these are framework components
    whose concrete rules must be specified. Limits: Finite recency memory is not a
    proof of cycle freedom or eventual global optimality. Attribute-based restrictions
    can exclude useful unvisited moves, and aspiration overrides must be designed
    with their effect on cycling in mind. The Part II finiteness construction was
    not inspected or generalized here. The simple pseudocode stops when no admissible
    move exists, while the subsequent prose describes releasing oldest restrictions
    to restore a move. These are distinct handling choices; the conceptual record
    does not silently present them as one fully specified executable algorithm. Tabu
    tenure, attributes, aspiration thresholds, candidate lists, move connectivity,
    initialization and stopping affect the search. Choosing the best currently admissible
    move does not imply monotonic objective improvement or a globally optimal final
    solution. The source also discusses probabilistic, strategic-oscillation and mixed-integer
    extensions. This record does not instantiate all variants or curate performance
    comparisons. Memory-based search need not be a reinforcement-learning task.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable optimization framework, not a trained instance or performance
      outcome.
    evidence_ids:
    - tabusearch-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Six exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms, comments and outgoing edges: TrainingStrategy, MachineLearningTask,
      ReinforcementLearning, ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain.
      All three general optimization frameworks receive bounded aio_no_match assessments
      with six explicit rejection reasons. Optional learning applications, search-memory
      terminology and stochastic representations do not establish the identity of
      a learning task, language model or stochastic-model class. Seven native neighbors
      were read in full: simulated annealing, cross-entropy optimization, genetic
      algorithms, A-star, best-first search, ACO and Ant System. Local trajectory
      moves differ from global frontier expansion, population evolution, distribution
      fitting and constructive pheromone search. Ant System’s per-tour tabu list is
      feasibility memory rather than the tabu-search framework; GLS’s relation to
      the broader tabu family does not equate its particular penalty update with every
      member. Earlier neighboring records’ mappings were contextual evidence, not
      newly approved by this review.'
    evidence_ids:
    - mapping
- assessment_id: guidedlocalsearch
  area: evidence
  topic: Identity, definition, mechanism, limitations and bounded no-match assessment
  outcome: supported
  target_ids:
  - AIMech:GuidedLocalSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - guidedlocalsearch-source-0
  summary: 'GLS is the named feature-penalty procedure, not all tabu search, a hard
    prohibition of recently visited moves, or Fast Local Search (FLS), which is a
    separately combinable neighborhood-reduction technique. The authors relate GLS
    to the broader tabu-search framework; that relationship does not make every tabu
    algorithm and the specified GLS update identical. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 301 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, returning 37 and 37 lines respectively. All 13 unique
    hit contents were inspected: prior local-search candidate leads, Ant System’s
    feasibility-list distinction, and their saved reports/reviews. These were references
    to methods rather than existing candidate records. Six exact AIO CLASS nodes with
    scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms
    were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  details: 'Choose binary indicators I_i(s) for nontrivial solution features, feature
    costs c_i, a local-search procedure and penalty scale lambda. In the inspected
    basic formulation the c_i are fixed and nonnegative, and penalties p_i start at
    zero. Repeatedly run local search from the current solution using h(s)=g(s)+lambda*sum_i
    p_i*I_i(s), where g is the original cost. At an h-local minimum s_star, compute
    u_i=I_i(s_star)*c_i/(1+p_i). In the nondegenerate case of positive maximum utility,
    increment p_i by one for every feature tied at that maximum, then resume local
    search from the same solution under the modified h. Penalization can repeat without
    an intervening move. Feature costs enter the utility ranking, not as extra multipliers
    in the displayed penalty sum. Retain and return the best solution found according
    to g, rather than choosing it by the changing augmented objective. FLS and other
    accelerations may be combined with the local-search subroutine but are not required
    by this baseline. Limits: The source allows zero feature costs. If every utility
    is zero, the all-feature pseudocode makes absent features tie with present ones,
    whereas the prose says only local-minimum features are penalized. A concrete implementation
    must declare its zero-utility and eligible-feature convention; the record’s stated
    update is restricted to the positive-maximum case. Curator qualification of Equation
    1: equal penalties contribute lambda*p times the number of active features. They
    cancel from move-cost differences only when that feature count is unchanged. The
    source’s equal-penalty cancellation statement is therefore not universal for variable-cardinality
    feature sets. Penalties are finite soft costs, not hard prohibitions. Their effect
    depends on lambda, objective scale, feature definition, move set and stopping.
    At lambda=0 the guidance vanishes; increasing penalties does not prove escape
    from every basin or convergence to a global optimum. Local minima are relative
    to h and the chosen neighborhood, not necessarily g. A deterministic penalty update
    does not make an entire implementation deterministic if its initial solution or
    local-search routine is randomized. The manuscript’s TSP comparisons do not establish
    universal superiority, and no benchmark results are curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable optimization framework, not a trained instance or performance
      outcome.
    evidence_ids:
    - guidedlocalsearch-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Six exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms, comments and outgoing edges: TrainingStrategy, MachineLearningTask,
      ReinforcementLearning, ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain.
      All three general optimization frameworks receive bounded aio_no_match assessments
      with six explicit rejection reasons. Optional learning applications, search-memory
      terminology and stochastic representations do not establish the identity of
      a learning task, language model or stochastic-model class. Seven native neighbors
      were read in full: simulated annealing, cross-entropy optimization, genetic
      algorithms, A-star, best-first search, ACO and Ant System. Local trajectory
      moves differ from global frontier expansion, population evolution, distribution
      fitting and constructive pheromone search. Ant System’s per-tour tabu list is
      feasibility memory rather than the tabu-search framework; GLS’s relation to
      the broader tabu family does not equate its particular penalty update with every
      member. Earlier neighboring records’ mappings were contextual evidence, not
      newly approved by this review.'
    evidence_ids:
    - mapping
- assessment_id: iteratedlocalsearch
  area: evidence
  topic: Identity, definition, mechanism, limitations and bounded no-match assessment
  outcome: supported
  target_ids:
  - AIMech:IteratedLocalSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - iteratedlocalsearch-source-0
  summary: 'The ILS framework includes the common local-minimum formulation but permits
    a more general, possibly stochastic or history-dependent embedded optimizer. Historical
    names such as iterated Lin–Kernighan and large-step Markov chains denote particular
    developments, not exact aliases of every ILS configuration. Single-chain search
    distinguishes the framework from population selection and distribution refitting;
    optional restarts and hybrids require their own declared choices. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    301 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in worktree and main, returning 37 and 37 lines respectively.
    All 13 unique hit contents were inspected: prior local-search candidate leads,
    Ant System’s feasibility-list distinction, and their saved reports/reviews. These
    were references to methods rather than existing candidate records. Six exact AIO
    CLASS nodes with scoped synonyms/comments and outgoing edges and seven native
    neighboring mechanisms were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.'
  details: 'Generate an initial solution and apply the embedded LocalSearch routine
    to obtain a current optimized solution. Repeat: perturb that current solution,
    apply LocalSearch to the perturbed intermediate point, then use an acceptance
    criterion comparing the current and candidate optimized solutions, potentially
    with search history, to choose the next current solution. Repeat until the declared
    termination condition. In the simplified deterministic memoryless setting, LocalSearch
    maps candidates into a reduced set of local optima, and perturbation followed
    by local search induces transitions among them. The general framework need not
    explicitly enumerate neighborhoods in that reduced space. Accepted variants include
    retaining only strict improvements, always accepting the newly optimized candidate,
    or temperature-dependent acceptance; improvement-only selection is not a universal
    requirement. Perturbation and acceptance may use history, and the embedded procedure
    can itself be stochastic or use memory. Limits: Perturbations that are too weak
    can return repeatedly to the same optimizer output; independent large perturbations
    remove the current solution’s influence from proposed starts and approach random-restart
    behavior. The full behavior still depends on the acceptance rule and the embedded
    optimizer. A deterministic memoryless embedded routine supports the simplified
    basin-of-attraction picture. General stochastic or history-dependent routines
    need not define the same fixed partition; history-free transition descriptions
    cannot be assumed for every ILS variant. Transitions between optimized solutions
    need not be reversible, and deterministic perturbations can produce short cycles.
    The framework alone is neither a target-invariant MCMC sampler nor a global-optimality
    or cycle-freedom guarantee. Initialization, perturbation, local-search termination,
    acceptance, best-so-far bookkeeping and restart conventions must be declared for
    an executable instance. The source reports sensitivity to module interactions,
    including settings worse than random restart; no universal performance ranking
    or empirical result is curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable optimization framework, not a trained instance or performance
      outcome.
    evidence_ids:
    - iteratedlocalsearch-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Six exact AIO CLASS nodes were inspected with definitions, scoped
      synonyms, comments and outgoing edges: TrainingStrategy, MachineLearningTask,
      ReinforcementLearning, ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain.
      All three general optimization frameworks receive bounded aio_no_match assessments
      with six explicit rejection reasons. Optional learning applications, search-memory
      terminology and stochastic representations do not establish the identity of
      a learning task, language model or stochastic-model class. Seven native neighbors
      were read in full: simulated annealing, cross-entropy optimization, genetic
      algorithms, A-star, best-first search, ACO and Ant System. Local trajectory
      moves differ from global frontier expansion, population evolution, distribution
      fitting and constructive pheromone search. Ant System’s per-tour tabu list is
      feasibility memory rather than the tabu-search framework; GLS’s relation to
      the broader tabu family does not equate its particular penalty update with every
      member. Earlier neighboring records’ mappings were contextual evidence, not
      newly approved by this review.'
    evidence_ids:
    - mapping
- assessment_id: tabu-boundaries
  area: consistency
  topic: Memory, admissibility and aspiration
  outcome: supported
  target_ids:
  - AIMech:TabuSearch
  evidence_ids:
  - tabusearch-source-0
  - finite-conventions
  - neighbors
  summary: Retain adaptive-memory search separately from a feasibility list.
  details: 'Best admissible moves may worsen the objective while a separate best-so-far
    solution is retained. Attributes can prohibit unvisited states; aspiration can
    override restrictions. Finite reversal memory does not guarantee absence of longer
    cycles. Empty admissible sets stop the simple pseudocode, whereas later prose
    relaxes oldest restrictions: the record preserves the variant choice. Intermediate/long-term
    memory and probabilistic selection are not silently mandatory. Issue 87 is resolved
    by describing the observed footer without dating insertion.'
- assessment_id: gls-boundaries
  area: consistency
  topic: Feature utilities, ties and objective modification
  outcome: supported
  target_ids:
  - AIMech:GuidedLocalSearch
  evidence_ids:
  - guidedlocalsearch-source-0
  - finite-conventions
  summary: Retain the specific penalty scheme with explicit numerical boundaries.
  details: The augmented objective is g+lambda*sum(p_i*I_i), without multiplying by
    feature costs again. Costs enter I_i*c_i/(1+p_i); all positive maximum ties are
    penalized. The source prose and all-feature pseudocode leave an all-zero utility
    ambiguity, which is retained. Equal penalties preserve ordering only under constant
    active-feature count; the finite counterexample prevents overgeneralizing the
    source statement. Return the best original objective, not the lowest changing
    augmented objective. FLS is optional and the broader tabu-family relationship
    does not establish exact identity.
- assessment_id: ils-boundaries
  area: consistency
  topic: Perturbation, reoptimization and acceptance
  outcome: supported
  target_ids:
  - AIMech:IteratedLocalSearch
  evidence_ids:
  - iteratedlocalsearch-source-0
  - finite-conventions
  summary: Retain a single-chain framework over embedded-optimizer outputs.
  details: Acceptance tests the optimized candidate, not the intermediate perturbation.
    Strict improvement, unconditional acceptance and temperature-based acceptance
    are separate supported choices. Deterministic memoryless local minimization is
    a simplifying case; the source permits history and stochastic or other embedded
    optimizers. Independent large perturbations do not erase the acceptance rule.
    Neither global convergence, reversibility nor fixed stationary distributions follow
    from the generic framework.
- assessment_id: mapping-boundaries
  area: grounding
  topic: General optimization and AIO learning classes
  outcome: supported
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with bounded no-match assessments.
  details: 'Six exact AIO CLASS nodes were inspected with definitions, scoped synonyms,
    comments and outgoing edges: TrainingStrategy, MachineLearningTask, ReinforcementLearning,
    ReinforcementLearningLLM, EvolutionaryLLM and MarkovChain. All three general optimization
    frameworks receive bounded aio_no_match assessments with six explicit rejection
    reasons. Optional learning applications, search-memory terminology and stochastic
    representations do not establish the identity of a learning task, language model
    or stochastic-model class. Seven native neighbors were read in full: simulated
    annealing, cross-entropy optimization, genetic algorithms, A-star, best-first
    search, ACO and Ant System. Local trajectory moves differ from global frontier
    expansion, population evolution, distribution fitting and constructive pheromone
    search. Ant System’s per-tour tabu list is feasibility memory rather than the
    tabu-search framework; GLS’s relation to the broader tabu family does not equate
    its particular penalty update with every member. Earlier neighboring records’
    mappings were contextual evidence, not newly approved by this review.'
findings:
- finding_id: tabu-scan-provenance
  issue_key: CultureBotAI-AIMech-TabuSearch-scan-provenance
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  target_ids:
  - AIMech:TabuSearch
  field_paths:
  - evidence_sources[0].version
  evidence_ids:
  - tabusearch-source-0
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearch.yaml
    role: maintained
  title: The footer’s date is treated as its insertion date.
  description: The initial draft inferred that the footer was added in 2001. The maintained
    record now describes only the observed notice and preserves the distinct 1989
    article date.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/87
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261011T141611Z-tabu-scan-provenance
    finding_id: tabu-scan-provenance
  disposition_reason: The source version now states that the scan contains a 2001
    copyright footer and that insertion time is not established. The 1989 publication
    identity and checksum are preserved. Ledger and append-only history were synchronized;
    changed inputs were reinspected and the post-fix gate passed.
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:TabuSearch
  - AIMech:GuidedLocalSearch
  - AIMech:IteratedLocalSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - tabusearch-source-0
  - guidedlocalsearch-source-0
  - iteratedlocalsearch-source-0
  rationale: Adaptive tabu restrictions, feature-penalized objectives and perturb/reoptimize/accept
    chains have distinct defining mechanisms. The source recognizes family overlap
    without establishing exact identity.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- The initial provenance review compressed extracted-header and visual-footer inspection
  into one visual locator. Before that review, Tabu PDF p.1 was read as extracted
  text and p.3 was viewed. PDF p.1 was additionally viewed during this successor review,
  confirming the 1989 header and 2001 footer; this is not a retroactive claim of earlier
  visual inspection.
- Only declared pages were inspected. No author code, benchmark or full convergence-proof
  audit was performed.
- GLS zero-utility behavior and equal-penalty cardinality conditions remain explicit.
  The ILS source is arXiv v1 (2001), not a later handbook revision.
- Three additions leave 177 pending inspection leads plus other unresolved dispositions;
  discovery remains active.
links:
- https://github.com/CultureBotAI/AIMech/issues/87
tags:
- native-concepts
- local-search
- metaheuristics
- self-review
- discovery-ongoing
```
