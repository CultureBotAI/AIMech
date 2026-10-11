# Scientific self-review of guided-search extensions

- Review: 20261011T144604Z-guided-search-extensions
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T14:43:43Z
- Finished UTC: 2026-10-11T14:46:04Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain GENET, EGLS and Lau–Tsang GGA as distinct DRAFT concepts. GENET has a justified broad ANN mapping; the optimization procedures have bounded no-match assessments. Source and executable-boundary limitations are explicit; no actionable curation finding remains in the declared scope.

## Scope And Provenance

All fields of three maintained concepts connected by the GENET/GLS/GGA research lineage.

Selection: Exact three IDs in the saved ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 549528b224d748e91da465fe8851e13fe11b2033.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GENET | data/curated/GENET.yaml | maintained | GENET |
| AIMech:ExtendedGuidedLocalSearch | data/curated/ExtendedGuidedLocalSearch.yaml | maintained | Extended Guided Local Search |
| AIMech:GuidedGeneticAlgorithm | data/curated/GuidedGeneticAlgorithm.yaml | maintained | Guided Genetic Algorithm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 76.48s (0:01:16)<br>Checked 442 record(s); 0 failed.<br>Checked 310 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 83 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 81,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm | Command exited0 with no output. |
| Finite guided-search boundary examples | passed | True | AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm | {"genet": {"synchronous_cycle": [[0, 0], [1, 1], [0, 0]], "sequential_solution": [1, 0], "atmost_variable_output": 0}, "egls": {"strict_aspiration": true, "equality_decided_by_aspiration": false}, "gga": {"templates": [[2, 2], [0, 1]], "lighter_parent_b_probability_gene1": "2/3", "zero_total_rule": "undefined in displayed rule; no fallback inferred"}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:GENET.

This is the GENET constraint-satisfaction architecture described by Davenport, Tsang, Wang and Zhu, including the general-constraint extension. It is not a biological genetic network, genetic algorithm, trained classifier or synonym of GLS. The binary network has inhibitory nogood connections, while the general-constraint extension includes constraint nodes and asymmetric fixed/adaptive connections. A Hopfield identity or globally symmetric network mapping would overstate that general architecture. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 4 and 4 lines respectively. All eight text hits were prior discovery leads in the two checkouts, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Create one cluster for each finite-domain variable and one label node per possible value, with exactly one active label per cluster. In the binary formulation, incompatible label pairs have inhibitory connections initially weighted −1; a label input sums the weights from currently active connected labels. A cluster activates a label of maximal input, breaking ties randomly. These updates need not be strict improvements. The described parallel implementation is explicitly not exactly synchronous, and the reported simulator selects variables sequentially. When an update cycle leaves the assignment unchanged, terminate if all active-label inputs are zero; otherwise reinforce violated connections, using W_new=W−V_i*V_j in the binary case. The extension represents higher-order constraints by constraint nodes with fixed label-to-constraint inputs and adaptive inhibitory outputs to labels. For a violated general constraint, all its outgoing connection weights are decremented according to Equation5; this must not be silently replaced by the binary active-endpoint rule. The paper defines distinct output functions for forbidden tuples and atmost constraints. Limits: The source explicitly says GENET is not complete: learning may create other local minima. It supplies no guarantee of finding a satisfying assignment or proving unsatisfiability within a finite budget. Exactly synchronous updates can oscillate; the source footnote excludes that interpretation of the parallel pseudocode. Ties can change assignments without strict objective improvement, distinguishing this mechanism from the strict hill-climbing record. The 1994 experiments use a sequential C++ simulation. Proposed speedups from future VLSI implementations are expectations, not measured hardware results curated here. The GENET2 conflicted-variable variant is not silently treated as the default variable-selection rule. General-constraint output functions and representations require care. At an atmost bound, activation in the same variable cluster must account for all participating values; independently inhibiting each inactive value can introduce a false penalty. No numerical benchmark result is curated.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:ExtendedGuidedLocalSearch.

EGLS here denotes the combined coefficient, aspiration and randomness extension in CSM371. GLS+A and GLS+R are separate ablations, not exact aliases of the combined algorithm. The method modifies the GLS search framework; it is not FLS activation-bit bookkeeping, simulated annealing, or a generic name for any later GLS extension. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 4 and 4 lines respectively. All eight text hits were prior discovery leads in the two checkouts, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Retain GLS feature counters, augmented objective h=g+lambda*sum(p_i*I_i), and penalty increments for present features tied for maximal cost/(1+p_i) utility. Scale lambda=a*C, where C estimates a characteristic cost contribution; the TSP illustration uses the first local-minimum tour cost divided by the number of cities. Add the report’s literal aspiration condition: accept an examined neighbor with g(s_next)&lt;g(best_so_far) even when h(s_next)&gt;h(s_current). This bypasses an augmented-cost rejection; it does not erase feature counters. Add randomization so that, with configured probability P_r per move, a randomly selected neighbor is accepted regardless of its objective or penalty quality. The combined EGLS uses all three changes. Its reported recommendations a=1 and P_r=.2 are experimental defaults, not universal constants or a proof of parameter independence. Limits: The report title does not establish a parameter-free algorithm. Feature definitions, neighborhood and local solver, cost estimate C, coefficient a, randomization probability P_r, initialization and stopping remain choices; the proposed defaults were evaluated only in the reported problem settings. The literal aspiration inequality is strict in both original improvement and augmented deterioration. It does not specify equality handling when h(s_next)=h(s_current); the underlying local solver and concrete implementation must declare that boundary and the order of random versus ordinary/aspiration moves. Scaling by a typical cost contribution is problem-dependent. The TSP first-tour average is not a universal normalization for arbitrary objectives, especially zero, negative or mixed-scale terms. Random moves can worsen either objective and need not improve exploration on a particular step. Aspiration protects access to an examined new original best, not global optimality or monotonic improvement of the entire trajectory. No comparative performance claim is curated.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:GuidedGeneticAlgorithm.

This record identifies the named Lau–Tsang GLS/genetic hybrid, not every algorithm described informally as guided genetic search. Later template-guided, fuzzy-guided or distributed algorithms are not asserted equivalent from their names. Generic GA supplies population evolution and GLS supplies feature penalties; GGA adds penalty-derived per-gene templates and specialized variation. It does not replace the population by the probability vector used in PBIL. LPGA is a problem-specific precursor, not an exact alias. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 4 and 4 lines respectively. All eight text hits were prior discovery leads in the two checkouts, not existing candidate records. Eight exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a population and a shared set of nonnegative feature-penalty counters, initially zero. Define each feature by an exhibited variable assignment or group of assignments and an application-specific undesirability cost. When the best current population member’s fitness remains unchanged for a configured number of generations, increment all maximal-utility present-feature counters, with utility cost/(1+counter). Use the augmented objective f+lambda*sum(counter*indicator) for the minimizing formulation and recompute each chromosome’s template: a gene weight sums counters for its exhibited features that involve that gene. Thus weights depend on the chromosome under shared penalties; offspring templates are recalculated, not inherited. At a crossover position with positive total parental weight, choose parent1’s value with probability weight2/(weight1+weight2), favoring the lighter gene. For mutation with positive total template weight, sample a gene in proportion to its weight and choose an objective-best domain value, with random tie handling in the displayed operator. The manuscript decrements a changed gene’s weight only if positive and allows repeated gene selection. Population replacement, mutation/crossover rates, stagnation threshold and stopping are configurable; the application uses elitist parent-plus-offspring replacement. These statements describe the documented framework and positive-weight operators, not a complete executable specification for all boundaries. Limits: The source initializes counters and template weights to zero but its displayed crossover and roulette rules divide by total weight or draw from an empty integer range when that total is zero. Neither inspected method supplies the fallback. A uniform fallback or pseudocount is an implementation decision requiring separate evidence; none is asserted here. The displayed mutation comparisons maximize g, whereas the article identifies the illustrated application as minimizing augmented cost and explicitly notes descent in footnote4. The record preserves this inconsistency and states objective-best selection with an explicit minimizing convention, rather than claiming the printed pseudocode is directly executable unchanged. The stagnation trigger is a heuristic, not a certificate that every possible improving gene change or population transition has been exhausted. The thesis’s future-work discussion states this limitation. Penalty updates need not escape all local traps or reach a global optimum. The application’s elitist replacement, finite mutation count, tie multiplicity and zero-weight handling do not define a unique universal implementation. Feature encoding, scaling and penalty semantics affect results; the reported benchmark superiority is not curated as a general guarantee.

### Activation, inhibition and general constraints

consistency: supported. Targets: AIMech:GENET.

Retain the connectionist architecture with its incompleteness and asynchronous qualification.

Critical images2–4 establish max-input/random-tie updates, the explicit nonsynchronous footnote, binary learning and general-constraint Equation5. The general network uses asymmetric constraint-node connections, rejecting a universal symmetric or Hopfield mapping. A broad ANN mapping follows the inspected definition and architecture, with direction local-to-broader-target. The finite inequality CSP shows simultaneous oscillation versus sequential repair, not a universal convergence proof. The atmost term depends on max activation across participating values within a cluster. Sequential experimental simulation and proposed VLSI acceleration are distinguished; numerical performance is not asserted.

### Three-part extension, strict aspiration and parameter scope

consistency: supported. Targets: AIMech:ExtendedGuidedLocalSearch.

Retain combined EGLS without claiming parameter independence.

The source names coefficient scaling, aspiration and randomness as the combined extension. The inspected aspiration test requires both strict original-best improvement and strict augmented deterioration; equality and move precedence are not invented. Default a=1/P_r=.2 and first-tour cost scaling are scoped recommendations. Random moves are not a temperature-based acceptance law. The finite example distinguishes a triggered aspiration from equality, without implementing the full algorithm or converting source recommendations into a theorem.

### Shared penalties, templates and unresolved operator boundaries

consistency: supported. Targets: AIMech:GuidedGeneticAlgorithm.

Retain the distinct framework with positive-total formulas and explicit source ambiguities.

Images13/14/16/18 of the author manuscript confirm shared feature counters, chromosome-dependent template sums and inverse parental weighting. The initial zero counters can leave total weight zero, while displayed sampling rules provide no fallback. The record does not invent uniform selection or pseudocounts. The mutation figure maximizes g despite the article’s minimizing application and descent footnote; the record explicitly discloses this discrepancy. Footnote5 guards decrements at zero. The unchanged-best trigger is not a local-optimum certificate, as thesis Section7.4 states. These gaps limit executable reproducibility, but do not erase the well-supported distinct framework identity. Final2001 journal metadata is distinguished from the2000 manuscript footer and unresolved1998/1999 thesis date.

### Connectionist architecture versus general optimization

grounding: supported. Targets: AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm.

Retain one justified broad mapping and two bounded no-match assessments.

Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms, comments and outgoing edges were inspected. GENET receives a broad_match to ArtificialNeuralNetwork: the target is broader than its connectionist architecture. HopfieldNetwork implies content-addressable memory, while SymmetricallyConnectedNetwork excludes the asymmetric general-constraint extension; neither is asserted. Network is broader still and adds no necessary second mapping. FeedbackNetwork has layer relations not established for GENET. EGLS and GGA receive bounded no-match assessments across the same eight targets: general assignment optimization is not necessarily a learning task, training strategy, neural architecture or evolutionary language model. Five native neighbors—GA, PBIL, GLS, FLS and strict hill climbing—separate population variation, distribution learning, penalty objectives, activation bookkeeping and strict local improvement. Neighbor mappings are context, not newly endorsed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:GENET, AIMech:ExtendedGuidedLocalSearch, AIMech:GuidedGeneticAlgorithm. Connectionist inhibitory search, a three-part GLS extension and penalty-guided genetic variation have distinct defining state and operations. Shared lineage and composition do not establish identity.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T144322Z-guided-search-extensions.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases; no normalized identity match. Full-checkout searches included ignored and hidden files in both worktree and main and returned four lines each, all prior candidate leads. All eight hits were inspected. Eight exact AIO nodes and five complete native neighbors were examined. Homonymous guided-genetic names were not assumed equivalent. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Eight exact CLASS nodes with scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms, comments and outgoing edges were inspected. GENET receives a broad_match to ArtificialNeuralNetwork: the target is broader than its connectionist architecture. HopfieldNetwork implies content-addressable memory, while SymmetricallyConnectedNetwork excludes the asymmetric general-constraint extension; neither is asserted. Network is broader still and adds no necessary second mapping. FeedbackNetwork has layer relations not established for GENET. EGLS and GGA receive bounded no-match assessments across the same eight targets: general assignment optimization is not necessarily a learning task, training strategy, neural architecture or evolutionary language model. Five native neighbors—GA, PBIL, GLS, FLS and strict hill climbing—separate population variation, distribution learning, penalty objectives, activation bookkeeping and strict local improvement. Neighbor mappings are context, not newly endorsed. |
| neighbors | research/discovery/20261011T144322Z-guided-search-extensions.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Full GA, PBIL, GLS, FLS and HillClimbing records distinguish population variation, distribution learning, feature penalties, active-region scanning and strict local improvement. Their prior mappings are contextual, not newly approved. |
| finite-conventions | research/discovery/guided-search-extensions-boundaries.py; calculate(): synchronous cycle, atmost variable term, strict aspiration, chromosome templates and zero totals | supports | Original finite cases distinguish synchronous oscillation from sequential assignment repair, atmost handling within a variable cluster, strict aspiration from equality, and shared-penalty template weights from undefined zero-total sampling. These are boundary examples, not benchmarks or convergence proofs. |
| genet-source-0 | https://cdn.aaai.org/AAAI/1994/AAAI94-049.pdf; PDF pp.1–4 (printed325–328), architecture, convergence/learning algorithms, footnote2, Equations1–9, and Generalised Constraint Representation; limitations and implementation discussion p.6 (printed330) | supports | GENET: A Connectionist Architecture for Solving Constraint Satisfaction Problems by Iterative Improvement. AAAI-94 proceedings, pp.325–330; six-page publisher PDF; method locators use PDF pages 1–6. Actual text, OCR and visual scopes are declared in source_analysis; extraction and rendering alone are not reading. |
| extendedguidedlocalsearch-source-0 | https://bracil.net/CSP/papers/MiTsFo-Gls%2BCsm371-2002.pdf; Sections2–6, PDF pp.2–5, GLS pseudocode, penalty coefficient, strict aspiration test and randomness; discussion/recommendations Sections7–8, pp.6–8 | supports | Extending Guided Local Search – towards a metaheuristic algorithm with no parameters to tune. University of Essex technical report CSM371, April 2002; UK Local Search Workshop, 16–17 April 2002, paper T15; 11-page author-hosted report. The title is an aspiration, not evidence that the algorithm has no parameters. Actual text, OCR and visual scopes are declared in source_analysis; extraction and rendering alone are not reading. |
| guidedgeneticalgorithm-source-0 | https://www.bracil.net/CSP/papers/LauTsang-Rlfap-Constraints2001.pdf; Section3.3.2–3.3.6, PDF pp.10–19, Equations9–10, Figures3/5/7, footnotes4–5; TablesII–III pp.20–21. The manuscript uses PDF/printed1–30, not final journal pages. | supports | Guided Genetic Algorithm and its Application to Radio Link Frequency Assignment Problems. 30-page author-hosted manuscript with typesetting footer 19 July 2000. The publisher verifies Constraints 6:373–398, October 2001, DOI below; this file is not the final journal pagination. Actual text, OCR and visual scopes are declared in source_analysis; extraction and rendering alone are not reading. |
| guidedgeneticalgorithm-source-1 | https://www.bracil.net/CSP/papers/Lau-Gga-PhD99.pdf; Chapter2, PDF pp.34–49 / printed26–41, especially templates and operators pp.41–48; Section7.4 PDF139 / printed131, non-certifying stagnation detector | supports | Guided Genetic Algorithm. 157-page University of Essex PhD thesis, undated cover. Author catalog/file labels it 1999, while the 2001 article reference lists 1998; the exact inspected bytes, not a resolved award date, identify this source. Chapter 2 PDF pp.34–49 corresponds to printed26–41. Actual text, OCR and visual scopes are declared in source_analysis; extraction and rendering alone are not reading. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- GGA zero-total sampling and source optimization-sign inconsistencies remain explicit. A concept record is not certification of an executable implementation.
- The GGA article uses author-manuscript pagination; the thesis date remains unresolved across source metadata. Exact hashes identify the inspected evidence.
- EGLS parameter defaults are scoped recommendations; GENET is incomplete and its proposed hardware acceleration is not an observed result.
- There are181 pending inspection leads plus unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T144604Z-guided-search-extensions
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of guided-search extensions
started_at: '2026-10-11T14:43:43Z'
finished_at: '2026-10-11T14:46:04Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all new fields against
    primary method sections, critical PDF images, eight exact AIO nodes, five full
    neighboring records and original finite counterexamples. Source gaps were preserved
    as explicit limits before writing the records. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain GENET, EGLS and Lau–Tsang GGA as distinct DRAFT concepts. GENET has
  a justified broad ANN mapping; the optimization procedures have bounded no-match
  assessments. Source and executable-boundary limitations are explicit; no actionable
  curation finding remains in the declared scope.
source:
  git_revision: 549528b224d748e91da465fe8851e13fe11b2033
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/FeedbackNetwork.yaml
    sha256: 74d1e22e6d446bd06278d8503785333cd4ae97c00cb4831a0c482347965ef0ba
    role: context
  - path: data/aio/HopfieldNetwork.yaml
    sha256: 042815574abb3502427a76bb970ab78fd1ef684fa5f807b41c948ddb62e63822
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/SymmetricallyConnectedNetwork.yaml
    sha256: 59d170d6424579ac8bf39b66c05cbfa611aebd2f1d3a9838dc66a14e276f5c42
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/ExtendedGuidedLocalSearch.yaml
    sha256: 47eecc6acd0b704f44caf4290b40e49bcbcae49e54fd2a67a51aace443c51e36
    role: target
  - path: data/curated/FastLocalSearch.yaml
    sha256: 2344a8d777fa40a5b41ae91d57337d9883c197b9fe3a13a991a79f2bc616a963
    role: context
  - path: data/curated/GENET.yaml
    sha256: 1b17f5fdcdaf35a366d98d8e9902e5417531782aa421b923e711be739f66f129
    role: target
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/GuidedGeneticAlgorithm.yaml
    sha256: 836ba491e26b23b5b8d6f42c966b2853b363ece1306bc26ef7cb9f7443f0ea57
    role: target
  - path: data/curated/GuidedLocalSearch.yaml
    sha256: 91618dff5e0ed6681aad81deb9be9c8e35ed43b42acad285ef473916852cdebc
    role: context
  - path: data/curated/HillClimbing.yaml
    sha256: 1f63c3e6341fecd3c78e00ae3ced9898c070ba9565dccc5511f3c67e6ea29476
    role: context
  - path: data/curated/PopulationBasedIncrementalLearning.yaml
    sha256: fb2500f70c8a0cf57639b33f7f89acf9f141adf75a238aa248e784afc09866d2
    role: context
  - path: research/discovery/20261011T144322Z-guided-search-extensions.json
    sha256: 9df795d4f54fb5689d3d036007ca816778ff93c9961ede5aba08bf74a81dbd58
    role: context
  - path: research/discovery/guided-search-extensions-boundaries.py
    sha256: ded39b6ccd39ec435cec3714e9ac3860f21b540b4da35449293c84202fe077aa
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
- target_id: AIMech:GENET
  path: data/curated/GENET.yaml
  label: GENET
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GENET.yaml
    role: maintained
- target_id: AIMech:ExtendedGuidedLocalSearch
  path: data/curated/ExtendedGuidedLocalSearch.yaml
  label: Extended Guided Local Search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExtendedGuidedLocalSearch.yaml
    role: maintained
- target_id: AIMech:GuidedGeneticAlgorithm
  path: data/curated/GuidedGeneticAlgorithm.yaml
  label: Guided Genetic Algorithm
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GuidedGeneticAlgorithm.yaml
    role: maintained
scope:
  description: All fields of three maintained concepts connected by the GENET/GLS/GGA
    research lineage.
  selection: Exact three IDs in the saved ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  exclusions:
  - target: Uninspected frontier leads and complete executable implementations
    reason: The batch does not exhaust search concepts, establish all GGA boundary
      conventions or execute original solvers.
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
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 76.48s (0:01:16)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 310 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 83 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 81,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
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
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
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
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Finite guided-search boundary examples
  command: python3 research/discovery/guided-search-extensions-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  exit_code: 0
  expected_exit_code: 0
  summary: '{"genet": {"synchronous_cycle": [[0, 0], [1, 1], [0, 0]], "sequential_solution":
    [1, 0], "atmost_variable_output": 0}, "egls": {"strict_aspiration": true, "equality_decided_by_aspiration":
    false}, "gga": {"templates": [[2, 2], [0, 1]], "lighter_parent_b_probability_gene1":
    "2/3", "zero_total_rule": "undefined in displayed rule; no fallback inferred"}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T144322Z-guided-search-extensions.json
  accessed_at: '2026-10-11T14:43:43Z'
  support: supports
  summary: Compared all 442 pinned AIO labels/scoped synonyms and 307 preceding native
    IDs/names/aliases; no normalized identity match. Full-checkout searches included
    ignored and hidden files in both worktree and main and returned four lines each,
    all prior candidate leads. All eight hits were inspected. Eight exact AIO nodes
    and five complete native neighbors were examined. Homonymous guided-genetic names
    were not assumed equivalent. Absence is bounded to this snapshot and semantic
    neighborhood.
  search_scope: All442 pinned AIO labels/scoped synonyms and307 preceding maintained
    IDs/names/aliases; both full checkouts including ignored and hidden files, four
    inspected candidate-lead lines each.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eight exact CLASS nodes with scoped synonyms/comments/outgoing edges in
    source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T14:43:43Z'
  support: supports
  summary: 'Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms,
    comments and outgoing edges were inspected. GENET receives a broad_match to ArtificialNeuralNetwork:
    the target is broader than its connectionist architecture. HopfieldNetwork implies
    content-addressable memory, while SymmetricallyConnectedNetwork excludes the asymmetric
    general-constraint extension; neither is asserted. Network is broader still and
    adds no necessary second mapping. FeedbackNetwork has layer relations not established
    for GENET. EGLS and GGA receive bounded no-match assessments across the same eight
    targets: general assignment optimization is not necessarily a learning task, training
    strategy, neural architecture or evolutionary language model. Five native neighbors—GA,
    PBIL, GLS, FLS and strict hill climbing—separate population variation, distribution
    learning, penalty objectives, activation bookkeeping and strict local improvement.
    Neighbor mappings are context, not newly endorsed.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T144322Z-guided-search-extensions.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T14:43:43Z'
  support: supports
  summary: Full GA, PBIL, GLS, FLS and HillClimbing records distinguish population
    variation, distribution learning, feature penalties, active-region scanning and
    strict local improvement. Their prior mappings are contextual, not newly approved.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/guided-search-extensions-boundaries.py
  locator: 'calculate(): synchronous cycle, atmost variable term, strict aspiration,
    chromosome templates and zero totals'
  accessed_at: '2026-10-11T14:43:43Z'
  snapshot_sha256: ded39b6ccd39ec435cec3714e9ac3860f21b540b4da35449293c84202fe077aa
  support: supports
  summary: Original finite cases distinguish synchronous oscillation from sequential
    assignment repair, atmost handling within a variable cluster, strict aspiration
    from equality, and shared-penalty template weights from undefined zero-total sampling.
    These are boundary examples, not benchmarks or convergence proofs.
- evidence_id: genet-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1994/AAAI94-049.pdf
  locator: PDF pp.1–4 (printed325–328), architecture, convergence/learning algorithms,
    footnote2, Equations1–9, and Generalised Constraint Representation; limitations
    and implementation discussion p.6 (printed330)
  accessed_at: '2026-10-11T14:30:00Z'
  snapshot_sha256: 5dfc2658b9e86ca60a45cef17d4538792fe7b092b737104a1fadd8b67cb8c6f0
  support: supports
  summary: 'GENET: A Connectionist Architecture for Solving Constraint Satisfaction
    Problems by Iterative Improvement. AAAI-94 proceedings, pp.325–330; six-page publisher
    PDF; method locators use PDF pages 1–6. Actual text, OCR and visual scopes are
    declared in source_analysis; extraction and rendering alone are not reading.'
- evidence_id: extendedguidedlocalsearch-source-0
  kind: primary_source
  reference: https://bracil.net/CSP/papers/MiTsFo-Gls%2BCsm371-2002.pdf
  locator: Sections2–6, PDF pp.2–5, GLS pseudocode, penalty coefficient, strict aspiration
    test and randomness; discussion/recommendations Sections7–8, pp.6–8
  accessed_at: '2026-10-11T14:30:00Z'
  snapshot_sha256: 4b74e69de0023a0a5c8734953cb9eff56d9e1c63e354df175937f625d17db769
  support: supports
  summary: Extending Guided Local Search – towards a metaheuristic algorithm with
    no parameters to tune. University of Essex technical report CSM371, April 2002;
    UK Local Search Workshop, 16–17 April 2002, paper T15; 11-page author-hosted report.
    The title is an aspiration, not evidence that the algorithm has no parameters.
    Actual text, OCR and visual scopes are declared in source_analysis; extraction
    and rendering alone are not reading.
- evidence_id: guidedgeneticalgorithm-source-0
  kind: primary_source
  reference: https://www.bracil.net/CSP/papers/LauTsang-Rlfap-Constraints2001.pdf
  locator: Section3.3.2–3.3.6, PDF pp.10–19, Equations9–10, Figures3/5/7, footnotes4–5;
    TablesII–III pp.20–21. The manuscript uses PDF/printed1–30, not final journal
    pages.
  accessed_at: '2026-10-11T14:38:41Z'
  snapshot_sha256: cd75523145caf41d9b30bb83aaa286bd4e83f9cf8fde3fd00ff440349c4d88da
  support: supports
  summary: Guided Genetic Algorithm and its Application to Radio Link Frequency Assignment
    Problems. 30-page author-hosted manuscript with typesetting footer 19 July 2000.
    The publisher verifies Constraints 6:373–398, October 2001, DOI below; this file
    is not the final journal pagination. Actual text, OCR and visual scopes are declared
    in source_analysis; extraction and rendering alone are not reading.
- evidence_id: guidedgeneticalgorithm-source-1
  kind: primary_source
  reference: https://www.bracil.net/CSP/papers/Lau-Gga-PhD99.pdf
  locator: Chapter2, PDF pp.34–49 / printed26–41, especially templates and operators
    pp.41–48; Section7.4 PDF139 / printed131, non-certifying stagnation detector
  accessed_at: '2026-10-11T14:31:41Z'
  snapshot_sha256: 13949c8ec915cdc67375bdfa7747f69a724d5472d15e5d30599751b8f92de5fb
  support: supports
  summary: Guided Genetic Algorithm. 157-page University of Essex PhD thesis, undated
    cover. Author catalog/file labels it 1999, while the 2001 article reference lists
    1998; the exact inspected bytes, not a resolved award date, identify this source.
    Chapter 2 PDF pp.34–49 corresponds to printed26–41. Actual text, OCR and visual
    scopes are declared in source_analysis; extraction and rendering alone are not
    reading.
assessments:
- assessment_id: genet
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:GENET
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - genet-source-0
  summary: This is the GENET constraint-satisfaction architecture described by Davenport,
    Tsang, Wang and Zhu, including the general-constraint extension. It is not a biological
    genetic network, genetic algorithm, trained classifier or synonym of GLS. The
    binary network has inhibitory nogood connections, while the general-constraint
    extension includes constraint nodes and asymmetric fixed/adaptive connections.
    A Hopfield identity or globally symmetric network mapping would overstate that
    general architecture. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main,
    returning 4 and 4 lines respectively. All eight text hits were prior discovery
    leads in the two checkouts, not existing candidate records. Eight exact AIO CLASS
    nodes with scoped synonyms/comments and outgoing edges and five native neighboring
    mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Create one cluster for each finite-domain variable and one label node
    per possible value, with exactly one active label per cluster. In the binary formulation,
    incompatible label pairs have inhibitory connections initially weighted −1; a
    label input sums the weights from currently active connected labels. A cluster
    activates a label of maximal input, breaking ties randomly. These updates need
    not be strict improvements. The described parallel implementation is explicitly
    not exactly synchronous, and the reported simulator selects variables sequentially.
    When an update cycle leaves the assignment unchanged, terminate if all active-label
    inputs are zero; otherwise reinforce violated connections, using W_new=W−V_i*V_j
    in the binary case. The extension represents higher-order constraints by constraint
    nodes with fixed label-to-constraint inputs and adaptive inhibitory outputs to
    labels. For a violated general constraint, all its outgoing connection weights
    are decremented according to Equation5; this must not be silently replaced by
    the binary active-endpoint rule. The paper defines distinct output functions for
    forbidden tuples and atmost constraints. Limits: The source explicitly says GENET
    is not complete: learning may create other local minima. It supplies no guarantee
    of finding a satisfying assignment or proving unsatisfiability within a finite
    budget. Exactly synchronous updates can oscillate; the source footnote excludes
    that interpretation of the parallel pseudocode. Ties can change assignments without
    strict objective improvement, distinguishing this mechanism from the strict hill-climbing
    record. The 1994 experiments use a sequential C++ simulation. Proposed speedups
    from future VLSI implementations are expectations, not measured hardware results
    curated here. The GENET2 conflicted-variable variant is not silently treated as
    the default variable-selection rule. General-constraint output functions and representations
    require care. At an atmost bound, activation in the same variable cluster must
    account for all participating values; independently inhibiting each inactive value
    can introduce a false penalty. No numerical benchmark result is curated.'
  dimensions:
  - name: concept-kind
    value: architecture
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - genet-source-0
  - name: aio-assessment
    value: broad_match
    definition: 'Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges were inspected. GENET receives a broad_match to
      ArtificialNeuralNetwork: the target is broader than its connectionist architecture.
      HopfieldNetwork implies content-addressable memory, while SymmetricallyConnectedNetwork
      excludes the asymmetric general-constraint extension; neither is asserted. Network
      is broader still and adds no necessary second mapping. FeedbackNetwork has layer
      relations not established for GENET. EGLS and GGA receive bounded no-match assessments
      across the same eight targets: general assignment optimization is not necessarily
      a learning task, training strategy, neural architecture or evolutionary language
      model. Five native neighbors—GA, PBIL, GLS, FLS and strict hill climbing—separate
      population variation, distribution learning, penalty objectives, activation
      bookkeeping and strict local improvement. Neighbor mappings are context, not
      newly endorsed.'
    evidence_ids:
    - mapping
- assessment_id: extendedguidedlocalsearch
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:ExtendedGuidedLocalSearch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - extendedguidedlocalsearch-source-0
  summary: EGLS here denotes the combined coefficient, aspiration and randomness extension
    in CSM371. GLS+A and GLS+R are separate ablations, not exact aliases of the combined
    algorithm. The method modifies the GLS search framework; it is not FLS activation-bit
    bookkeeping, simulated annealing, or a generic name for any later GLS extension.
    No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 307 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, returning 4 and
    4 lines respectively. All eight text hits were prior discovery leads in the two
    checkouts, not existing candidate records. Eight exact AIO CLASS nodes with scoped
    synonyms/comments and outgoing edges and five native neighboring mechanisms were
    inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Retain GLS feature counters, augmented objective h=g+lambda*sum(p_i*I_i),
    and penalty increments for present features tied for maximal cost/(1+p_i) utility.
    Scale lambda=a*C, where C estimates a characteristic cost contribution; the TSP
    illustration uses the first local-minimum tour cost divided by the number of cities.
    Add the report’s literal aspiration condition: accept an examined neighbor with
    g(s_next)<g(best_so_far) even when h(s_next)>h(s_current). This bypasses an augmented-cost
    rejection; it does not erase feature counters. Add randomization so that, with
    configured probability P_r per move, a randomly selected neighbor is accepted
    regardless of its objective or penalty quality. The combined EGLS uses all three
    changes. Its reported recommendations a=1 and P_r=.2 are experimental defaults,
    not universal constants or a proof of parameter independence. Limits: The report
    title does not establish a parameter-free algorithm. Feature definitions, neighborhood
    and local solver, cost estimate C, coefficient a, randomization probability P_r,
    initialization and stopping remain choices; the proposed defaults were evaluated
    only in the reported problem settings. The literal aspiration inequality is strict
    in both original improvement and augmented deterioration. It does not specify
    equality handling when h(s_next)=h(s_current); the underlying local solver and
    concrete implementation must declare that boundary and the order of random versus
    ordinary/aspiration moves. Scaling by a typical cost contribution is problem-dependent.
    The TSP first-tour average is not a universal normalization for arbitrary objectives,
    especially zero, negative or mixed-scale terms. Random moves can worsen either
    objective and need not improve exploration on a particular step. Aspiration protects
    access to an examined new original best, not global optimality or monotonic improvement
    of the entire trajectory. No comparative performance claim is curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - extendedguidedlocalsearch-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges were inspected. GENET receives a broad_match to
      ArtificialNeuralNetwork: the target is broader than its connectionist architecture.
      HopfieldNetwork implies content-addressable memory, while SymmetricallyConnectedNetwork
      excludes the asymmetric general-constraint extension; neither is asserted. Network
      is broader still and adds no necessary second mapping. FeedbackNetwork has layer
      relations not established for GENET. EGLS and GGA receive bounded no-match assessments
      across the same eight targets: general assignment optimization is not necessarily
      a learning task, training strategy, neural architecture or evolutionary language
      model. Five native neighbors—GA, PBIL, GLS, FLS and strict hill climbing—separate
      population variation, distribution learning, penalty objectives, activation
      bookkeeping and strict local improvement. Neighbor mappings are context, not
      newly endorsed.'
    evidence_ids:
    - mapping
- assessment_id: guidedgeneticalgorithm
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:GuidedGeneticAlgorithm
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - guidedgeneticalgorithm-source-0
  - guidedgeneticalgorithm-source-1
  summary: This record identifies the named Lau–Tsang GLS/genetic hybrid, not every
    algorithm described informally as guided genetic search. Later template-guided,
    fuzzy-guided or distributed algorithms are not asserted equivalent from their
    names. Generic GA supplies population evolution and GLS supplies feature penalties;
    GGA adds penalty-derived per-gene templates and specialized variation. It does
    not replace the population by the probability vector used in PBIL. LPGA is a problem-specific
    precursor, not an exact alias. No normalized identity match was found across all
    442 pinned AIO labels/scoped synonyms and 307 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 4 and 4 lines respectively. All eight text hits were prior
    discovery leads in the two checkouts, not existing candidate records. Eight exact
    AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five native
    neighboring mechanisms were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.
  details: 'Maintain a population and a shared set of nonnegative feature-penalty
    counters, initially zero. Define each feature by an exhibited variable assignment
    or group of assignments and an application-specific undesirability cost. When
    the best current population member’s fitness remains unchanged for a configured
    number of generations, increment all maximal-utility present-feature counters,
    with utility cost/(1+counter). Use the augmented objective f+lambda*sum(counter*indicator)
    for the minimizing formulation and recompute each chromosome’s template: a gene
    weight sums counters for its exhibited features that involve that gene. Thus weights
    depend on the chromosome under shared penalties; offspring templates are recalculated,
    not inherited. At a crossover position with positive total parental weight, choose
    parent1’s value with probability weight2/(weight1+weight2), favoring the lighter
    gene. For mutation with positive total template weight, sample a gene in proportion
    to its weight and choose an objective-best domain value, with random tie handling
    in the displayed operator. The manuscript decrements a changed gene’s weight only
    if positive and allows repeated gene selection. Population replacement, mutation/crossover
    rates, stagnation threshold and stopping are configurable; the application uses
    elitist parent-plus-offspring replacement. These statements describe the documented
    framework and positive-weight operators, not a complete executable specification
    for all boundaries. Limits: The source initializes counters and template weights
    to zero but its displayed crossover and roulette rules divide by total weight
    or draw from an empty integer range when that total is zero. Neither inspected
    method supplies the fallback. A uniform fallback or pseudocount is an implementation
    decision requiring separate evidence; none is asserted here. The displayed mutation
    comparisons maximize g, whereas the article identifies the illustrated application
    as minimizing augmented cost and explicitly notes descent in footnote4. The record
    preserves this inconsistency and states objective-best selection with an explicit
    minimizing convention, rather than claiming the printed pseudocode is directly
    executable unchanged. The stagnation trigger is a heuristic, not a certificate
    that every possible improving gene change or population transition has been exhausted.
    The thesis’s future-work discussion states this limitation. Penalty updates need
    not escape all local traps or reach a global optimum. The application’s elitist
    replacement, finite mutation count, tie multiplicity and zero-weight handling
    do not define a unique universal implementation. Feature encoding, scaling and
    penalty semantics affect results; the reported benchmark superiority is not curated
    as a general guarantee.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - guidedgeneticalgorithm-source-0
    - guidedgeneticalgorithm-source-1
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms,
      comments and outgoing edges were inspected. GENET receives a broad_match to
      ArtificialNeuralNetwork: the target is broader than its connectionist architecture.
      HopfieldNetwork implies content-addressable memory, while SymmetricallyConnectedNetwork
      excludes the asymmetric general-constraint extension; neither is asserted. Network
      is broader still and adds no necessary second mapping. FeedbackNetwork has layer
      relations not established for GENET. EGLS and GGA receive bounded no-match assessments
      across the same eight targets: general assignment optimization is not necessarily
      a learning task, training strategy, neural architecture or evolutionary language
      model. Five native neighbors—GA, PBIL, GLS, FLS and strict hill climbing—separate
      population variation, distribution learning, penalty objectives, activation
      bookkeeping and strict local improvement. Neighbor mappings are context, not
      newly endorsed.'
    evidence_ids:
    - mapping
- assessment_id: genet-boundaries
  area: consistency
  topic: Activation, inhibition and general constraints
  outcome: supported
  target_ids:
  - AIMech:GENET
  evidence_ids:
  - genet-source-0
  - finite-conventions
  - mapping
  summary: Retain the connectionist architecture with its incompleteness and asynchronous
    qualification.
  details: Critical images2–4 establish max-input/random-tie updates, the explicit
    nonsynchronous footnote, binary learning and general-constraint Equation5. The
    general network uses asymmetric constraint-node connections, rejecting a universal
    symmetric or Hopfield mapping. A broad ANN mapping follows the inspected definition
    and architecture, with direction local-to-broader-target. The finite inequality
    CSP shows simultaneous oscillation versus sequential repair, not a universal convergence
    proof. The atmost term depends on max activation across participating values within
    a cluster. Sequential experimental simulation and proposed VLSI acceleration are
    distinguished; numerical performance is not asserted.
- assessment_id: egls-boundaries
  area: consistency
  topic: Three-part extension, strict aspiration and parameter scope
  outcome: supported
  target_ids:
  - AIMech:ExtendedGuidedLocalSearch
  evidence_ids:
  - extendedguidedlocalsearch-source-0
  - finite-conventions
  summary: Retain combined EGLS without claiming parameter independence.
  details: The source names coefficient scaling, aspiration and randomness as the
    combined extension. The inspected aspiration test requires both strict original-best
    improvement and strict augmented deterioration; equality and move precedence are
    not invented. Default a=1/P_r=.2 and first-tour cost scaling are scoped recommendations.
    Random moves are not a temperature-based acceptance law. The finite example distinguishes
    a triggered aspiration from equality, without implementing the full algorithm
    or converting source recommendations into a theorem.
- assessment_id: gga-boundaries
  area: consistency
  topic: Shared penalties, templates and unresolved operator boundaries
  outcome: supported
  target_ids:
  - AIMech:GuidedGeneticAlgorithm
  evidence_ids:
  - guidedgeneticalgorithm-source-0
  - guidedgeneticalgorithm-source-1
  - finite-conventions
  summary: Retain the distinct framework with positive-total formulas and explicit
    source ambiguities.
  details: Images13/14/16/18 of the author manuscript confirm shared feature counters,
    chromosome-dependent template sums and inverse parental weighting. The initial
    zero counters can leave total weight zero, while displayed sampling rules provide
    no fallback. The record does not invent uniform selection or pseudocounts. The
    mutation figure maximizes g despite the article’s minimizing application and descent
    footnote; the record explicitly discloses this discrepancy. Footnote5 guards decrements
    at zero. The unchanged-best trigger is not a local-optimum certificate, as thesis
    Section7.4 states. These gaps limit executable reproducibility, but do not erase
    the well-supported distinct framework identity. Final2001 journal metadata is
    distinguished from the2000 manuscript footer and unresolved1998/1999 thesis date.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Connectionist architecture versus general optimization
  outcome: supported
  target_ids:
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain one justified broad mapping and two bounded no-match assessments.
  details: 'Eight exact pinned AIO CLASS nodes with definitions, scoped synonyms,
    comments and outgoing edges were inspected. GENET receives a broad_match to ArtificialNeuralNetwork:
    the target is broader than its connectionist architecture. HopfieldNetwork implies
    content-addressable memory, while SymmetricallyConnectedNetwork excludes the asymmetric
    general-constraint extension; neither is asserted. Network is broader still and
    adds no necessary second mapping. FeedbackNetwork has layer relations not established
    for GENET. EGLS and GGA receive bounded no-match assessments across the same eight
    targets: general assignment optimization is not necessarily a learning task, training
    strategy, neural architecture or evolutionary language model. Five native neighbors—GA,
    PBIL, GLS, FLS and strict hill climbing—separate population variation, distribution
    learning, penalty objectives, activation bookkeeping and strict local improvement.
    Neighbor mappings are context, not newly endorsed.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:GENET
  - AIMech:ExtendedGuidedLocalSearch
  - AIMech:GuidedGeneticAlgorithm
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - genet-source-0
  - extendedguidedlocalsearch-source-0
  - guidedgeneticalgorithm-source-0
  - guidedgeneticalgorithm-source-1
  rationale: Connectionist inhibitory search, a three-part GLS extension and penalty-guided
    genetic variation have distinct defining state and operations. Shared lineage
    and composition do not establish identity.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- GGA zero-total sampling and source optimization-sign inconsistencies remain explicit.
  A concept record is not certification of an executable implementation.
- The GGA article uses author-manuscript pagination; the thesis date remains unresolved
  across source metadata. Exact hashes identify the inspected evidence.
- EGLS parameter defaults are scoped recommendations; GENET is incomplete and its
  proposed hardware acceleration is not an observed result.
- There are181 pending inspection leads plus unresolved dispositions; discovery remains
  active.
links: []
tags:
- native-concepts
- constraint-search
- self-review
- discovery-ongoing
```
