# Scientific self-review of dispatch-dependent dual-queue planning and value functional

- Review: 20261016T074705Z-dispatch-dependent-dual-queue-planning-and-value-functional
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-16T07:47:04.970198Z
- Finished UTC: 2026-10-16T07:47:05.461091Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain distinct source-scoped DRAFT planner and mathematical-functional records with 11 claims and 21 limitations. Alternating synchronized queue control is separate from its dispatch-conditioned value rule. Fixed-model probability and prefix assumptions, estimation, source-version and dispatch-integration limits remain explicit.

## Scope And Provenance

Both exact current native records, all claims/limitations, bounded identity/mapping and source responsibility. Earlier literal readings remain attributed.

Selection: Exact AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base cc0c9ef618dae4da01fd32e8e4523e8481bcb138.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DispatchDependentDualQueuePlanning | data/curated/DispatchDependentDualQueuePlanning.yaml | maintained | Dispatch-dependent dual-queue planning |
| AIMech:DispatchDependentValueFunctional | data/curated/DispatchDependentValueFunctional.yaml | maintained | Dispatch-dependent value functional |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| render | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |
| source | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |
| gate | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |
| vendor | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |
| render-check | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |
| diff | passed | True | AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional | Actual successful required command; exact output/timing retained. |

## Scientific And Domain Assessments

### Dispatch-dependent dual-queue planning: temporal-planning-setting

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The selected setting is explicit in the primary paper. It separates concurrent dispatch from the simpler plan-then-execute setting without importing guarantees from the abstract metareasoning background.

The described procedure operates in concurrent propositional temporal planning with Boolean fluents, nonnegative-duration actions, start, invariant and end conditions, and start/end effects, known timed initial literals, and goals. Actions may be emitted incrementally before a complete plan is available, but each scheduled start must be at or after its emission time. This defines the source setting, not a general partially observable or stochastic-execution model.

### Dispatch-dependent dual-queue planning: goal-and-dispatch-priorities

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The priorities and tie rule are stated. The failure complement follows from the stated success event and tail description; equality mass remains on the success side. The distinction is also independently checked in the bounded math review.

The first open list uses the weighted goal-progress score f(i)=g(i)+w*h(i), where h(i) is relaxed-plan length. The second uses pf(i), described as the estimated probability of missing the deadline when all remaining undispatched actions on the path to i are assumed dispatched. Ties in pf are broken by f. Relating this score to the inclusive success event in Eq.3 gives the explicit interpretation pf(i,t)=1−V(i,t)=Pr[m&gt;d(i)−t] for that assumed-dispatch context; this complement is an interpretation of the prose interface, not a separately printed executable equation.

### Dispatch-dependent dual-queue planning: alternating-synchronized-frontier

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

This is the source-defined procedural distinction. No global stopping, duplicate-state or scheduler contract is inferred from this paragraph.

Node expansion alternates between the f-priority and pf-priority open lists. Selecting and removing a state from either list removes it from both; successors of the expansion are inserted into both. The lists therefore provide two orderings of the shared frontier rather than two independent searches whose outputs are combined.

### Dispatch-dependent dual-queue planning: periodic-failure-score-refresh

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The interval is retained as the described setting rather than an intrinsic parameter-free property. Fixed-model monotonicity does not constrain values after the estimated model changes.

The described implementation computes pf when a node is inserted, using the current time and then-current remaining-search-time estimate. It recomputes pf for all open nodes every 100 expansions with updated time and search-time estimates. The mechanism is periodic refresh, not continuously exact scoring or a proof that successive estimates are monotonic.

### Dispatch-dependent dual-queue planning: surrounding-dispatch-integration

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The source explicitly distinguishes expansion from dispatch and states the integration/removal. The original 2024 dispatch paper is retained as a follow-up rather than newly certified through this citation.

The evaluated planner is called dual in the paper and is implemented within the temporal planner identified there as OPTIC. It retains the earlier Coles et al. (2024) dispatch reasoning while removing that method’s restriction of search to a promising subtree; the two expansion priorities provide the alternative information-gathering mechanism. A dispatch threshold remains. Choosing a frontier node by pf is not itself the complete decision to execute an action.

### Dispatch-dependent dual-queue planning: limitation 1

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The conflict is visible in the source and independently confirmed; the draft does not apply that decreasing step as a valid CDF.

The background calls D_i a deadline CDF and Eq.1 uses 1−D_i, but the deterministic-deadline paragraph then assigns D_i=1 before or on latest_start and 0 afterward. That decreasing step is inconsistent with the stated CDF role. Both inspected PDF versions retain the presentation conflict; no implementation defect, original-paper erratum or silently repaired convention is asserted.

### Dispatch-dependent dual-queue planning: limitation 2

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Success/failure polarity and atom handling are explicitly qualified, without pretending that the complementary executable equation is printed.

Eq.3 is a success probability, whereas Section 4.1 describes a failure score. The complementary interpretation is pf=Pr[m&gt;d−t], with deadline equality counted as success; replacing &gt; by &gt;= needs an additional no-atom convention. The background Eq.1 survival convention and Eq.3 inclusive event must not be silently unified, and the prose does not provide a complete numerical implementation.

### Dispatch-dependent dual-queue planning: limitation 3

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The event-containment and endpoint qualifications are explicit curator deductions checked by the independent review, not a claim of strict decrease or unchanged estimates.

For a fixed remaining-search law M and fixed deadline d, V(t)=Pr[m&lt;=d−t] is nonincreasing. For nonnegative m and finite d, V(d)=Pr[m=0] and V(t)=0 is guaranteed for t&gt;d (it can also be zero earlier); it need not be zero exactly at d. These fixed-model facts do not make the periodically refreshed scores monotonic when estimates, relaxed plans or deadlines change.

### Dispatch-dependent dual-queue planning: limitation 4

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The source’s estimate status is preserved. No proof for a different weighted-search algorithm is imported.

Remaining search time is estimated from expansion-delay/search statistics and relaxed-plan length, while relaxed-plan deadline estimates are explicitly described as inadmissible. The scores are modeled probabilities, without a demonstrated calibration or error bound. The weighted f form does not transfer a weighted-A* quality bound, completeness theorem or successful-dispatch guarantee to this combined procedure.

### Dispatch-dependent dual-queue planning: limitation 5

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

This preserves the argument’s explicit structural condition and separates it from an optimal metalevel-policy theorem.

The none/all prefix argument requires a reasonable ancestor relaxed plan and a forward successor with a matching suffix. It matches assumed commitment contexts; it does not establish equality of node-specific search-time laws or probabilities, preservation of all relevant ancestors in the frontier, or sufficiency for arbitrary dispatch policies. Actual irreversible dispatch can make a goal unreachable.

### Dispatch-dependent dual-queue planning: limitation 6

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Two levels of modeling are distinguished; the record does not collapse their action assumptions.

The abstract metareasoning background uses mutually exclusive non-preemptible domain actions with computation concurrent with at most one action. The selected temporal-planning setting and multi-robot evaluation allow concurrent actions. The abstract exclusivity restriction must not be assigned to every evaluated action, nor does that evaluation establish arbitrary uncertain execution dynamics.

### Dispatch-dependent dual-queue planning: limitation 7

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The actual access boundary is retained; no unseen implementation behavior is asserted.

The paper gives prose queue and dispatch integration, not a complete executable specification. Duplicate-state handling, tie/cycle corner cases, sound dispatch and scheduling depend on the underlying planner and earlier dispatch procedure. Code is described as available from the authors upon request, but no request, code acquisition or algorithm execution occurred in this research.

### Dispatch-dependent dual-queue planning: limitation 8

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The source’s two citations remain a metadata/lineage question.

Section 4.1 associates OPTIC with Benton et al. (2012), while Section 5 cites Coles et al. (2012) for the implementation and the bibliography names that work COLIN. The discrepancy is retained without treating OPTIC and COLIN as aliases or diagnosing an implementation error.

### Dispatch-dependent dual-queue planning: limitation 9

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Evaluation parameter choices are not elevated to universal or parameter-free method properties.

The evaluation sets w=5, uses the described 100-expansion score refresh and tests dispatch thresholds 0.025, 0.1 and 0.25. Removing subtree focus or the earlier allocate-t_u search restriction does not remove these parameters. No universally best threshold or expansion-rate-independent setting is established.

### Dispatch-dependent dual-queue planning: limitation 10

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The benchmark population and timing interpretation remain limits rather than a positive general performance claim.

The reported evaluation uses 100 RCLL scenarios with one-, two- and three-robot variants and eight simulated expansion rates from 10 to 1000 expansions per second. Those rates are simulated timing, not measured hardware speed or complete queue/heuristic overhead. Sums across rates reuse scenarios and are not counts of independent scenarios; the experiment does not establish general deployment performance.

### Dispatch-dependent dual-queue planning: limitation 11

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The scope of the comparisons and diagnostic is retained without copying aggregate superiority into the definition or claims.

The paper’s virtual best solver selects a configuration by robot-count/domain and expansion-rate setting, not an explicitly instance-wise oracle. Aggregate coverage advantages are not uniform across settings, and the displayed tables report no confidence intervals or repeated-run uncertainty. No causal benefit or universal runtime advantage follows from the queue-agreement diagnostic.

### Dispatch-dependent dual-queue planning: limitation 12

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The selected name and prospective mapping reflect later adjudication; the original dossier’s earlier undecided wording remains unchanged as historical evidence.

The author and official PDFs are distinct byte artifacts of one 2025 work, with different title-block forms of Shimony’s name and layout metadata. The institutional 2029 date remains a metadata question. The curated descriptive name disambiguates the source-local dual label from the maintained 1987 game-tree DUAL* algorithm; aliases are empty. All original bibliography and follow-up questions remain retained, not resolved by this draft.

### Dispatch-dependent dual-queue planning: source-scoped definition

evidence: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The definition names the procedure actually described in the paper, excluding the mathematical score alone, generic concurrent planning, and an isolated benchmark configuration.

A concurrent temporal-planning search procedure that alternates node expansion between a weighted goal-progress open list and a dispatch-conditioned estimated-failure open list, synchronizes their frontier membership, and periodically refreshes failure estimates while retaining the surrounding temporal planner’s dispatch reasoning.

### Dispatch-dependent dual-queue planning: concept kind

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Retain algorithm for the alternating synchronized-frontier procedure, including its refresh and dispatch-integration boundary. A mathematical score alone does not specify those steps.

The source describes node selection, synchronized removal/insertion, score refresh and integration with existing dispatch reasoning. The record denotes that procedure, not generic CoPE, an OPTIC build or a parameterized evaluation result.

### Dispatch-dependent dual-queue planning: historical prospective identity

identity: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The descriptive name disambiguates the source-local dual label. Empty aliases avoid collision with the maintained 1987 game-tree DUAL* and avoid treating CoPE, OPTIC or COLIN as aliases.

The descriptive name disambiguates the paper’s source-local dual planner. It is not an alias for the maintained 1987 game-tree DUAL* algorithm, generic dual search, OPTIC/COLIN, or the CoPE problem setting; aliases are empty. The independently defined dispatch-dependent value functional is a scoring component, not this whole algorithm. Queue control, assumed-dispatch failure interpretation, estimation limits and surrounding dispatch logic define the selected scope. The identity assessment is historical prospective evidence captured at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f on 2026-10-16, with 807 native and 442 AIO records, 4,946 identity-field occurrences and 3,781 normalized values. Four repository roots were searched including ignored and hidden files; all 40 distinct matching contents were read. Selected comparisons covered 96 definition contexts, 21 closer native contexts, and 20 full AIO nodes with 62 incident edges. These observations do not allocate a future owner, select a future write base or establish whole-ontology semantic absence.

Current canonical identity: This record denotes the 2025 source-local dual planner as a descriptive, disambiguated temporal-planning procedure. Empty aliases preserve its distinction from maintained DUAL*, generic dual search, OPTIC/COLIN and the CoPE problem setting. Alternating synchronized goal-progress and modeled failure priorities, refreshing estimates and retaining the surrounding dispatch logic define the algorithm. The separately represented dispatch-dependent value functional is a scoring component, not the whole procedure. Current insertion context was reconciled at merged commit cc0c9ef618dae4da01fd32e8e4523e8481bcb138: 810 native and 442 pinned AIO records, 4,958 identity-field occurrences and 3,790 normalized values. Four ignored- and hidden-inclusive roots returned 49 distinct matching contents and 200 occurrences. Forty contents reuse exact historical reading with attribution; all nine new report/review contents were read. All 1,249 records from the historical assessment are byte-identical, and the three added ILBFS/RBFS identities and definitions were read as distinct search controls. The 20 selected AIO nodes and 62 incident edges were freshly read on the unchanged pin; historical whole-label screening and 96-definition/21-neighbor scientific context are attributed to their original reading. Existing main911 coordinates source tracking, without equating this 2025 family to its nine prior methods or resolving the independent 2023/2004 routes.

### Dispatch-dependent dual-queue planning: directional AIO assessment

grounding: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Retain bounded no-match for the 20 examined pinned AIO targets. A probability-valued component, robot application or two-priority search does not map the whole planner to a mathematical function, model or learning task.

All 442 pinned AIO IDs, labels and scoped synonyms were screened; 20 relevant full nodes, annotations and all 62 incident edges were freshly read. Selection follows planning, control, probability/time scoring and the most plausible generic type confusions, not a prescribed target count. These are the inspected targets, not all conceivable ontology classes. This is the historical 2026-10-16 prospective snapshot at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f, with 807 native and 442 AIO records; it is not a future insertion clearance.

No examined target identifies or usefully subsumes the two-queue temporal-planning procedure. Generic task overlap, robot applications and a mathematical component are insufficient mappings of the whole algorithm.

AIO:MachineLearningTask: The subject is a temporal-planning control procedure. Updating search-time estimates is a component, not evidence that this entire procedure is a process for building methods that learn from data. The source does not establish a specific learning-task identity or an informative method-level related mapping.
AIO:Model: The complete subject is an executable-style search and dispatch procedure, not merely an abstract representation of a complex system. Its embedded probability estimates and action model do not identify the planner as this generic model class.
AIO:MathematicalFunction: The complete planner maintains and alternates two open lists, expands nodes and interacts with dispatch decisions. Its functional score is a component; mapping that component does not map the entire algorithm to a mathematical rule.
AIO:ReasoningLLM: Explicit planning and deadline reasoning here do not use a large language model or language-task inference. The related synonym reasoning cannot expand this LLM class into all symbolic planning.
AIO:EmbodiedLLM: The robot benchmark does not make this symbolic temporal planner a language-grounded multimodal model. Application overlap is insufficient.
AIO:ReinforcementLearning: The inspected procedure searches a supplied temporal model and uses deadline/search-time estimates; it does not define reward-driven policy learning. Goal progress and information gathering are not by themselves reinforcement learning.
AIO:ReinforcementLearningLLM: There is no language-model reward fine-tuning or generated-text objective in the proposed procedure.
AIO:PolicyLayer: A planner deciding when to expand or dispatch is not a neural-network layer predicting an action distribution. Its probability is a timely-search estimate, not the output distribution of the described layer.
AIO:GraphConvolutionalPolicyNetwork: The subject neither uses graph convolution nor trains graph-generation policies with rewards and adversarial loss.
AIO:ActiveLearning: Expanding a node to improve dispatch information does not query an annotator for labels of new training points. Information gathering alone does not supply the target class identity.
AIO:TimeSeriesAnalysis: The algorithm is not a task of extracting characteristics from time-series observations; wall-clock dependence and refreshed estimates do not establish that task relation.
AIO:TimeSeriesForecasting: Estimated remaining search time guides planning, but the full algorithm is not a procedure for forecasting a time-series sequence from previous values.
AIO:SurvivalAnalysis: A tail probability of estimated search completion relative to a deadline is a scoring component. The complete planner is not the described time-to-event analysis task, and mere use of a probability tail is too generic for a useful related mapping.
AIO:ProportionalHazardsModel: The source does not impose a proportional-hazards regression model or multiplicative covariate effect on a hazard rate.
AIO:ProbabilisticGraphicalModel: The search tree is a space of partial action plans, not a graph specifying conditional dependence among random variables. A probability estimate at a search node does not turn the controller into this target task.
AIO:MarkovChain: The queue procedure is not a stochastic transition model whose next-event law depends only on the preceding state; the source score alone does not establish a Markov-chain identity.
AIO:BayesianNetwork: No directed acyclic conditional-dependence network is specified as the algorithm identity.
AIO:DecisionTree: A search tree of possible plans is not the pinned classification/decision-support tree model. Branching does not establish classifier or predictor identity.
AIO:ContinualLearning: Continued search and distribution refresh do not constitute the target deep neural network learning sequential tasks without access to old task data.
AIO:EnsembleLearning: Alternating two priorities on one shared search frontier is not a predictive ensemble of learned algorithms.

Current mapping context: The complete algorithm retains the accepted no-match assessment against 20 exact current AIO targets. Generic learning/task/model language, temporal probabilities, robot applications and the embedded mathematical score do not identify or usefully subsume the two-queue planning controller. The functional-only MathematicalFunction relation is not transferred to the planner; this is bounded target review, not whole-ontology semantic absence.

### Dispatch-dependent dual-queue planning: source versions and reading roles

provenance: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

The author PDF directly supports the definition and positive claims; the official PDF and metadata are a same-work version/publication comparison. Author, root and independent bounded readings retain separate scope.

Two native source rows across the records cite one author artifact of one work. The official version is retained separately and is not independent experimental replication. Root’s complete author-image reading supplements researcher352’s original full-text/image/diff work. Independent356 reviewed the full selected native cores/support and confirmed the narrow invariant-condition wording correction. Issue 418 remains open for actual canonical delivery. Root revalidated only the corrected algorithm preview; the unchanged functional preview retains its successful earlier result. The mixed receipt binds both exact hashes with problems[]; this is structural/claim-source evidence, not canonical or scientific acceptance. The exact 38 bibliography occurrences, 9 method leads, 12 questions and one historical route question remain linked without closure.

### Dispatch-dependent dual-queue planning: procedure versus functional boundary

scope: supported. Targets: AIMech:DispatchDependentDualQueuePlanning.

Retain the controller separately from its mathematical functional and from the game-tree DUAL* method. The two selected source scopes are related through the explicitly interpreted failure interface, not identical.

The complete planner needs queue state, estimate refresh and surrounding dispatch decisions. Preserve inclusive success versus strict complementary failure, the deadline-CDF conflict, conditional prefix reasoning, finite-deadline endpoint qualification, estimated probabilities, and weight/refresh/threshold and evaluation limits. No implementation theorem, calibrated success or universal performance is asserted.

### Dispatch-dependent value functional: prefix-conditioned-success-event

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The formal event, arguments and output type are source-defined. The law is estimated, so the probability is not represented as calibrated real-world success.

For a node i, partition its path H_i into an already committed prefix H_d and a remaining undispatched suffix H_c. Section 3 defines V(H_d,H_c)(t)=Pr_{m~M_i}[t+m&lt;=d(i)], where M_i models remaining search time and d(i)=latest_start(H_c,pi_i) depends on the undispatched path and a relaxed goal plan. The path-conditioned object returns a function of contemplated search start time; it is a modeled success probability with an inclusive deadline event.

### Dispatch-dependent value functional: path-and-relaxed-plan-deadline

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The construction and empty-path convention are explicit. The relaxed-plan bound is not mislabeled admissible.

The deadline construction takes the smaller of the latest-start bounds from the remaining path and the relaxed goal plan. The relaxed-plan bound uses the tightest action deadline slack relative to its estimated earliest time. When the remaining path is empty its path latest-start bound is taken as infinity, leaving the relaxed-plan bound to determine d(i). The latter bound is a heuristic estimate in this source.

### Dispatch-dependent value functional: family-of-assumed-dispatch-prefixes

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The count and partition transformation are explicit; describing a hypothetical commitment does not itself select an action.

Each prefix H_p of the remaining path H_c defines a different assumed-commitment context: move H_p to the end of H_d and compute the rule on the residual suffix. Thus a path with &#124;H_c&#124; remaining actions defines &#124;H_c&#124;+1 such functionals, including the none-dispatched and all-dispatched cases. These are hypothetical value evaluations, not commands to execute those actions.

### Dispatch-dependent value functional: fixed-model-monotonicity-and-endpoint

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

Set inclusion proves the bounded statement. The mass-at-zero endpoint and strict t&gt;d qualification avoid overstating the source prose.

With M and d fixed, increasing t can only shrink the event {m&lt;=d−t}, so V is nonincreasing, not necessarily strictly decreasing. If m is nonnegative and d finite, V(d)=Pr[m=0] and V(t)=0 for t&gt;d. These endpoint statements follow directly from Eq.3; they are curator deductions with explicit premises, not a claim that zero is reached at t=d or that refreshed estimates remain monotonic.

### Dispatch-dependent value functional: frozen-prefix-relaxation

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The inequality is a direct minimum/event argument under explicitly fixed quantities. It is not a general dominance claim for dispatching earlier.

If the node’s remaining-search law and relaxed-plan bound are held fixed, removing assumed-dispatched actions from the minimum over remaining path constraints cannot lower that path bound. Consequently the combined deadline and inclusive success probability cannot decrease in this frozen comparison. This mathematical comparison does not establish that actual irreversible dispatch improves achievable success when the frontier, model or feasible alternatives change.

### Dispatch-dependent value functional: conditional-none-all-context-correspondence

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The source’s reasonableness and successor/suffix assumptions remain explicit, and no equality of M_i across nodes is inferred.

The source motivates evaluating only the none-dispatched and all-dispatched cases across a forward search when a reasonable relaxed plan at an ancestor has a successor whose relaxed plan is the matching suffix. Under that structural assumption, an intermediate assumed commitment at the successor can correspond to an all-dispatched commitment context at the ancestor. This is a conditional correspondence of action contexts, not a proof of equal node-specific probabilities or an optimal policy over all prefixes.

### Dispatch-dependent value functional: limitation 1

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The functional is an assessed mathematical object in a planning model, not a true-world success oracle.

The probability is conditional on estimated remaining search time and an estimated deadline. Expansion-delay statistics and relaxed-plan length inform M_i, and the relaxed-plan deadline is explicitly inadmissible. No calibration, error bound or certainty that the chosen plan remains executable follows from Eq.3.

### Dispatch-dependent value functional: limitation 2

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The formal definition is usable within its stated event while the separate presentation conflict stays explicit.

The background deadline-CDF notation conflicts with its later decreasing deterministic step: Eq.1 uses 1−D_i after calling D_i a CDF, while the next page assigns one before/on the deadline and zero afterward. Eq.3’s inclusive success event is retained on its own terms. No silent repair of the background convention or identity between its strict survival event and Eq.3 at atoms is asserted.

### Dispatch-dependent value functional: limitation 3

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The inferred interface is separated from the source-defined functional and from finite-precision implementation choices.

The planner’s pf is described as a failure tail although Eq.3 defines success. The interface pf=1−V=Pr[m&gt;d−t] is an explicit complementary interpretation, not a separately printed executable formula. Equality belongs to success; a &gt;= failure event can differ when the law has atoms. The functional alone does not prescribe that queue interface or its numerical implementation.

### Dispatch-dependent value functional: limitation 4

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The source prose is narrowed to an event-theoretic statement with complete endpoint premises.

Monotonicity requires the distribution and deadline to remain fixed. With nonnegative remaining time and finite d, vanishing is assured for t&gt;d, while V(d)=Pr[m=0] can be positive. Updating M_i, the relaxed plan or deadline can increase a later recomputed value; infinite/no global deadlines and negative remaining times are outside the stated endpoint deduction.

### Dispatch-dependent value functional: limitation 5

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The formal input transformation does not provide a safe-dispatch theorem or a universal action model.

Removing path constraints in a frozen hypothetical comparison is not the same as performing an irreversible action. Actual dispatch restricts accessible subtrees and can invalidate alternatives or make a goal unreachable. The source’s background abstract action exclusivity also must not be transferred unqualified to the concurrent multi-robot planner.

### Dispatch-dependent value functional: limitation 6

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

Only the supported action-context correspondence is claimed; probability equality and policy sufficiency remain unresolved.

The none/all argument assumes matching ancestor/successor relaxed-plan structure. It does not prove equality of M_i laws, equal probabilities, retention of the requisite ancestors in OPEN, or sufficiency for arbitrary prefix policies and changed temporal constraints. It is a heuristic reduction argument rather than a general optimal metareasoning theorem.

### Dispatch-dependent value functional: limitation 7

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The separate mathematical_method boundary is source-grounded and prevents conflating a score with a complete algorithm.

This rule does not specify an estimator-training procedure, full search algorithm, scheduler, dispatch threshold, stopping test or duplicate-state policy. The source’s dual planner adds alternating queues, tie-breaking and periodic refresh, and uses an earlier dispatch integration. Those control rules and their reported performance are not properties of the mathematical functional alone.

### Dispatch-dependent value functional: limitation 8

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

Empirical evidence is retained as context and is not promoted to an independent functional-performance claim.

The simulated RCLL coverage and queue-agreement results assess complete configured planners rather than isolated correctness or calibration of this functional. Their repeated scenario/rate combinations, chosen weights and thresholds, and absent table uncertainty measures do not establish a universal benefit of the rule in other domains.

### Dispatch-dependent value functional: limitation 9

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

The exact inherited source questions persist even where the native record uses a narrower mathematical scope.

Evidence comes from the byte-distinct author and official PDFs of one 2025 work, not independent replications. Name-form, institutional-date and OPTIC/COLIN citation differences remain in research context. No referenced original algorithm or implementation is newly certified here, and all 38 bibliography occurrences and original follow-up objects remain unchanged in the retained ledger.

### Dispatch-dependent value functional: source-scoped definition

evidence: supported. Targets: AIMech:DispatchDependentValueFunctional.

The source independently defines this probability-valued time function. Mathematical_method describes the rule itself; the broad AIO mapping does not attach to the complete planner.

A dispatch-prefix-conditioned mathematical rule that returns, as a function of a contemplated search start time t, the modeled probability of finishing remaining search no later than a latest-start deadline estimated from the undispatched path and a relaxed goal plan: V(H_d,H_c)(t)=Pr_{m~M_i}[t+m&lt;=d(i)].

### Dispatch-dependent value functional: concept kind

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

Retain mathematical_method for the independently defined path-conditioned value rule, which returns a probability-valued function of time. It is not a second queue algorithm or a condition-only evaluation criterion.

Section 3 gives mathematical inputs, a named functional and Eq.3 separately from the later controller. PI acquisition supplies a representation precedent, not evidence of identity or the reason for splitting by itself.

### Dispatch-dependent value functional: historical prospective identity

identity: supported. Targets: AIMech:DispatchDependentValueFunctional.

The singularized source name and empty aliases denote the function-valued construction. Search-completion time, dispatch-prefix conditions and deadlines distinguish it from improvement acquisitions and generic time-dependent node scores.

The singularized name follows Section 3; aliases are empty. This source-defined rule maps a path/dispatch context to a function of time and is represented separately from the dual-queue controller that uses a complementary failure interpretation. It differs from probability-of-improvement acquisition because its random variable, conditioning, deadline and purpose concern search completion under dispatch commitments. That representation precedent does not establish identity. The functional-only broad_match to AIO:MathematicalFunction is a local inference; no upstream axiom, probability calibration or planner mapping is asserted. The identity assessment is historical prospective evidence captured at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f on 2026-10-16, with 807 native and 442 AIO records, 4,946 identity-field occurrences and 3,781 normalized values. Four repository roots were searched including ignored and hidden files; all 40 distinct matching contents were read. Selected comparisons covered 96 definition contexts, 21 closer native contexts, and 20 full AIO nodes with 62 incident edges. These observations do not allocate a future owner, select a future write base or establish whole-ontology semantic absence.

Current canonical identity: This record denotes the Section 3 dispatch-prefix-conditioned mathematical rule, with empty aliases and a scope distinct from the dual-queue controller. It maps planning/dispatch context to a function of contemplated search start time and models completion no later than the estimated deadline. Probability-of-improvement acquisition has a different random variable, conditioning, event and purpose; it is representation context, not an alias. The inclusive event, frozen-model assumptions, source deadline-CDF discrepancy and conditional prefix argument remain explicit. Current insertion context was reconciled at merged commit cc0c9ef618dae4da01fd32e8e4523e8481bcb138: 810 native and 442 pinned AIO records, 4,958 identity-field occurrences and 3,790 normalized values. Four ignored- and hidden-inclusive roots returned 49 distinct matching contents and 200 occurrences. Forty contents reuse exact historical reading with attribution; all nine new report/review contents were read. All 1,249 records from the historical assessment are byte-identical, and the three added ILBFS/RBFS identities and definitions were read as distinct search controls. The 20 selected AIO nodes and 62 incident edges were freshly read on the unchanged pin; historical whole-label screening and 96-definition/21-neighbor scientific context are attributed to their original reading. Existing main911 coordinates source tracking, without equating this 2025 family to its nine prior methods or resolving the independent 2023/2004 routes.

### Dispatch-dependent value functional: directional AIO assessment

grounding: supported. Targets: AIMech:DispatchDependentValueFunctional.

Retain the local broad_match to AIO:MathematicalFunction for this formal rule only. The target is broader and does not impose an activation-only or scalar-only restriction; this does not map the complete planner or assert an upstream axiom.

AIO:MathematicalFunction (broad_match): The proposed subject is the Section 3 mathematical rule itself: it maps a dispatch-prefix-conditioned planning context to a function of search start time. The target’s definition covers a rule assigning a dependent value from independent values and does not require a neural activation or a scalar codomain. This is a local broad-match inference for the functional only, not an exact match, an upstream axiom, a proof of probability calibration or a mapping of the complete planner.

Current mapping context: Retain the local broad_match to AIO:MathematicalFunction: the target is broader than this dispatch-conditioned rule assigning a modeled probability from planning context and time. The exact current node, annotations and incident edges support that abstraction. No exact match, upstream axiom, calibration claim or mapping of the full planner is asserted.

### Dispatch-dependent value functional: source versions and reading roles

provenance: supported. Targets: AIMech:DispatchDependentValueFunctional.

The author PDF directly supports the definition and positive claims; the official PDF and metadata are a same-work version/publication comparison. Author, root and independent bounded readings retain separate scope.

Two native source rows across the records cite one author artifact of one work. The official version is retained separately and is not independent experimental replication. Root’s complete author-image reading supplements researcher352’s original full-text/image/diff work. Independent356 reviewed the full selected native cores/support and confirmed the narrow invariant-condition wording correction. Issue 418 remains open for actual canonical delivery. Root revalidated only the corrected algorithm preview; the unchanged functional preview retains its successful earlier result. The mixed receipt binds both exact hashes with problems[]; this is structural/claim-source evidence, not canonical or scientific acceptance. The exact 38 bibliography occurrences, 9 method leads, 12 questions and one historical route question remain linked without closure.

### Dispatch-dependent value functional: procedure versus functional boundary

scope: supported. Targets: AIMech:DispatchDependentValueFunctional.

Retain the mathematical functional as a separate source-defined scope; it can be evaluated without alternating queues. It neither chooses a full dispatch policy nor supplies the complete search/scheduling procedure.

The inclusive event is m&lt;=d−t. The interpreted complementary queue failure event is m&gt;d−t. Fixed-law/fixed-deadline monotonicity is nonincrease; with m&gt;=0 and finite d, V(d)=P(m=0), while zero is guaranteed for t&gt;d and may occur earlier. The none/all argument matches commitment contexts under a relaxed-plan correspondence, not equal laws/probabilities or arbitrary-policy optimality.

### Actual canonical correspondence, current source responsibility and checks

provenance: supported. Targets: AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional.

Two DRAFT records retain 11 claims and 21 limitations, two declared source rows and one defining work. Five creation outputs and the actual capture/checks are bound. Only main 911 is updated; all 60 original source objects, 12 source limitations and current progress remain queryable alongside the complete incoming 363 projection. Issue 418 corrected a temporal-effects wording ambiguity before insertion. No algorithm execution, source exhaustion, source-question closure or publication completion is implied.

Current capture contains 79 inputs. Earlier source/version/identity readings remain attributed. The 2025 CoPE source progress and separate 2004/2005 manufacturing research progress do not overwrite historical retrieval observations. Manufacturing current identity and record curation remain pending independently.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:DispatchDependentDualQueuePlanning. Retain the source-defined dual-queue controller within the qualified temporal-planning setting. The descriptive label is distinct from 1987 DUAL* and generic CoPE. Its mathematical scoring component does not exhaust its stateful control and dispatch integration. Current canonical identity and source responsibility are bound to the actual decisions; no source-question closure is claimed.
- retain: AIMech:DispatchDependentValueFunctional. Retain the independently defined value functional as a mathematical_method with the functional-only broad mapping. Its probability event and hypothetical-prefix interface are separate from an algorithm, calibrated success oracle or universal dispatch policy. Current canonical identity and source responsibility are bound to the actual decisions; no source-question closure is claimed.
- split: AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional. Partition the two selected source scopes into the stateful search/dispatch controller and the independently defined mathematical value rule. This complete disjoint partition explains the current two-record representation; it does not split, rename or mutate an existing canonical record or AIO class. Shared paper, event interface or benchmark does not make the two concepts identical.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cope-scientific-support | /private/tmp/aimech-cope-two-native-core-data-20261016/scientific-support.v3.json; All selected definition/claim/limitation support rows and source roles. | context_only | Author support for exact selected cores; not an independent review. |
| cope-native-selection | /private/tmp/aimech-cope-two-native-core-data-20261016/handoff.v3.json; Selected algorithm v3 and unchanged functional core; narrow invariant-condition wording correction. | context_only | Prospective selection; no native validation or canonical insertion. |
| cope-identity-proposal | /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/identity-mapping-proposal.v2.json; Both prospective candidates, granularity, aliases and mapping rationale. | context_only | Historical prospective identity and source-grounded two-scope proposal. |
| cope-historical-search | /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/collection.json; Complete captured inventory, matching contents and root search provenance. | context_only | Historical prospective search, not later insertion clearance. |
| cope-aio-context | /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json; All selected 20 full pinned AIO nodes and 62 incident edges. | context_only | Pinned ontology assertions ground mappings, not independent scientific evidence for planner performance. |
| cope-native-comparisons | /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/native-neighbor-comparisons.json; All 21 historical closer-neighbor comparison narratives. | context_only | Maintained-neighbor context; no current whole-corpus identity claim. |
| cope-source-continuity | /private/tmp/aimech-cope-two-native-core-data-20261016/source-question-continuity.json; Exact original 38 bibliography occurrences, 9 method leads, 12 questions, source limitations and one additional historical route question. | context_only | References retain exact original objects and their unresolved status; no ownership closure. |
| cope-source-roles | /private/tmp/aimech-cope-scientific-review-fragments-20261016/source-metadata-and-roles.v3.json; Per-record native sources, source artifact roles, reading attribution and preview status. | context_only | Derived metadata projection; not a primary paper or native validation result. |
| cope-version-comparison | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/version-comparison.json; Author/official extracted-body differences and publication/name metadata. | context_only | Same-work version comparison; different PDF bytes do not imply independent studies. |
| cope-source-acquisition | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/network-acquisition.json; Successful author/official PDF and official metadata acquisition receipts. | context_only | Actual source access/hash provenance; not a curation event. |
| cope-original-reading | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/handoff.final.json; Original researcher reading scope and dossier references. | context_only | Researcher352 full author text/images and official text-diff reading; earlier pending review fields remain historical. |
| cope-independent-math | /private/tmp/aimech-cope-independent-granularity-math-review-20261016/assessment.json; Bounded independent granularity, event/complement, endpoint, prefix and mapping assessment. | context_only | Independent source/proposal review predating native cores; the later full core/support review and correction disposition are separately bound through source-role metadata. |
| cope-root-bounded-reading | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/root-bounded-source-reading.json; Root initial author images 2–5 and dossier readings. | context_only | Bounded supporting root source reading, without canonical acceptance. |
| cope-root-complete-author-reading | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/root-completed-author-reading.json; Root supplementary images 1,6,7,8 and prior pages 2–5 receipt. | context_only | Combined root reading covers all eight author images, figures/tables and nineteen references; not all official images or cited originals. |
| cope-root-scope-decision | /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/root-prospective-scope-decision.json; Prospective algorithm/formal-component distinction and functional-only mapping. | context_only | Root adjudication authorizes prospective DATA preparation, not current canonical identity or ownership. |
| cope-native-schema | /private/tmp/aimech-discovery-recovery-worktree-20261012/src/aimech/schema/curated_concept.yaml; ConceptKind, evidence and directional mapping fields. | context_only | Native representation contract, not scientific proof. |
| cope-preview-receipt | /private/tmp/aimech-cope-scientific-review-fragments-20261016/preview-yaml-handoff.v3.json; Actual TEMP serialization provenance and exact core correspondence. | context_only | Actual TEMP serialization and mixed validation linkage; it is not itself the native validator result. |
| cope-official-paper | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/official2025-network.pdf; Official title block, pp.8483–8490; comparison to author artifact. | context_only | Byte-distinct official version of the same IJCAI 2025 work; official image reading is not claimed beyond recorded scope. |
| cope-official-bibliography | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/official-bibtex-network.txt; Official publication title, author forms, venue, pages, year and DOI. | context_only | Official publication identity; source bytes are independently bound. |
| cope-planner-core | /private/tmp/aimech-cope-two-native-core-data-20261016/DispatchDependentDualQueuePlanning.native-core.v3.json; Complete selected prospective native core. | context_only | Exact selected DATA without invented canonical curation. |
| cope-planner-preview | /private/tmp/aimech-cope-scientific-review-fragments-20261016/previews/DispatchDependentDualQueuePlanning.v2.yaml; Complete prospective YAML and actual preview curation. | context_only | Exact TEMP serialization; later root native validation is separately bound. No canonical insertion or scientific proof. |
| cope-author-locator-01 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.1–2, Section 2.1, problem tuple and emission/start-time constraint; official pp.8483–8484. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-02 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4 Eq.3; p.5 Section 4.1, f, assumed-dispatch pf and tie-breaking; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-03 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.5, Section 4.1, dual open-list paragraph; official p.8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-04 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.5, Section 4.1, insertion and t_u=100 refresh paragraph; official p.8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-05 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.3–4, prior dispatch integration; p.6, opening of Section 5; official pp.8485–8486 and 8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-06 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.2 Eq.1 and p.3 deterministic-deadline paragraph; official pp.8484–8485. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-07 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.2,4–5, Eq.1, Eq.3 and Section 4.1; official pp.8484,8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-08 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4 Eq.3 and monotonicity paragraph; p.5 refresh paragraph; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-09 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.3 search-time/deadline estimation; pp.4–5 functional and algorithm; official pp.8485–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-10 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.4–5, Section 3 argument and Section 4 opening; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-11 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.2–3 background model; p.6 robot-count discussion; official pp.8484–8485 and 8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-12 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.5–6, including p.6 footnote 2; official pp.8487–8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-13 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.5–6 and p.8 references; official pp.8487–8488 and 8490. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-14 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.5–6, refresh rule and Section 5 parameter settings; official pp.8487–8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-15 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.6–7, Section 5, Figure 1 and Table 1; official pp.8488–8489. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-16 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.6–7, VBS definition, Tables 1–2; official pp.8488–8489. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-17 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.1 title block and p.8 references. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-18 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.5–6, Sections 4.1–5; official pp.8487–8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-functional-core | /private/tmp/aimech-cope-two-native-core-data-20261016/DispatchDependentValueFunctional.native-core.json; Complete selected prospective native core. | context_only | Exact selected DATA without invented canonical curation. |
| cope-functional-preview | /private/tmp/aimech-cope-scientific-review-fragments-20261016/previews/DispatchDependentValueFunctional.yaml; Complete prospective YAML and actual preview curation. | context_only | Exact TEMP serialization; later root native validation is separately bound. No canonical insertion or scientific proof. |
| cope-author-locator-19 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4, Section 3, footnote 1 and Eq.3; official p.8486. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-20 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.3, latest_start formulas; p.4, all-actions-dispatched limit following Eq.3; official pp.8485–8486. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-21 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4, Section 3 prefix construction; official p.8486. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-22 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4 Eq.3 and following monotonicity paragraph; p.5 refresh description; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-23 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.3 minimum latest_start definitions; p.4 prefix discussion; p.5 irreversible-dispatch warning; official pp.8485–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-24 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4, final Section 3 argument continuing on p.5; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-25 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.3 estimation discussion; p.4 Eq.3; official pp.8485–8486. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-26 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.2 Eq.1; p.3 deterministic-deadline paragraph; p.4 Eq.3; official pp.8484–8486. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-27 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4 Eq.3 and p.5 Section 4.1; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-28 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF p.4 monotonicity paragraph; p.5 refreshed M_i; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-29 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.3–5, abstract model, prefix construction and Section 4 warning; p.6 concurrent robots; official pp.8485–8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-30 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.4–5, Section 3 concluding argument; official pp.8486–8487. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-31 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.4–6, Sections 3–5; official pp.8486–8488. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-author-locator-32 | /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf; Author PDF pp.6–7, evaluation setup, Tables 1–2; official pp.8488–8489. | supports | Inspected author paper passage; the assessment states whether its use is direct support or a qualified curator deduction. |
| cope-root-preview-validation | /private/tmp/aimech-cope-scientific-review-fragments-20261016/root-preview-validation.v2.json; Corrected algorithm exact hash and one new native result; unchanged functional exact hash and retained prior result. | context_only | Root performed one revalidation of the corrected algorithm; the functional result is retained from its unchanged previously validated bytes. No functional rerun, canonical insertion, current-corpus clearance, full-collection check or scientific proof is claimed. |
| actual-write | /private/tmp/aimech-cohort364-write.json | context_only | Actual exclusive record/report/history creation, not publication. |
| actual-capture | /private/tmp/aimech-cohort364-checks-20261016/actual-capture.json | context_only | Actual native inspect capture of the current canonical inputs. |
| actual-reading | /private/tmp/aimech-cohort364-checks-20261016/root-actual-reading.final.json | context_only | Actual postcapture scientific and metadata reading with explicit prior roles. |
| actual-adversarial | /private/tmp/aimech-cohort364-actual-adversarial-review-20261016/assessment.json | context_only | Bounded actual record adversarial assessment; earlier source authorship is separately disclosed. |
| actual-decisions | /private/tmp/aimech-cohort364-current-rebind-20261016/current-decisions.accepted.json | context_only | Actual current identities, main 911 postimage, 60 current source-progress rows and separately attributed route progress; original source wrappers remain exact. |
| actual-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T073716Z-dispatch-dependent-dual-queue-planning-and-value-functional.json | context_only | Canonical report preserves the exact five-field predecessor 363 projection, 60 original source objects, 12 source limitations, current progress and independent 2025/2004 route scopes. |
| current-rebind | /private/tmp/aimech-cohort364-current-rebind-20261016/current-rebind-assessment.json | context_only | Fresh four-root ignored/hidden-inclusive search and exact record/source/owner rebind; earlier literal semantic readings remain attributed. |
| pre-insertion-correction | /private/tmp/aimech-cope-two-native-core-data-20261016/invariant-effects-correction.json | context_only | Before insertion, the temporal-setting claim was corrected to distinguish invariant conditions from start/end effects; other accepted science is unchanged. |
| pre-insertion-correction-disposition | /private/tmp/aimech-cope-native-core-independent-review-20261016/disposition.v3.json | context_only | Independent source correspondence confirms the narrow issue 418 correction; issue closure remains a separate postmerge event. |
| check-render | /private/tmp/aimech-cohort364-checks-20261016/render.json | context_only | Actual required command completed with exit 0. |
| check-source | /private/tmp/aimech-cohort364-checks-20261016/source.json | context_only | Actual required command completed with exit 0. |
| check-gate | /private/tmp/aimech-cohort364-checks-20261016/gate.json | context_only | Actual required command completed with exit 0. |
| check-vendor | /private/tmp/aimech-cohort364-checks-20261016/vendor.json | context_only | Actual required command completed with exit 0. |
| check-render-check | /private/tmp/aimech-cohort364-checks-20261016/render-check.json | context_only | Actual required command completed with exit 0. |
| check-diff | /private/tmp/aimech-cohort364-checks-20261016/diff.json | context_only | Actual required command completed with exit 0. |

## Limits And Additional Notes

- Mechanism and proof statements remain source-scoped; retained interface, cost, version and experimental qualifications are substantive.
- Historical primary and neighbor readings retain their original authorship; the current postmerge rebind does not claim a new whole-paper or whole-ontology reading.
- Native structural validation does not prove scientific truth. Canonical review save/check, committed-head review and publication are subsequent operations.
- The 44 selected corrected scientific assessments retain their scientific statements/support. Actual evidence links are appended; two historical identity details and two mapping details receive separate current context. The three boundary rationales record actual context instead of a prospective prerequisite. The selected temporal-planning-setting assessment already incorporates the pre-insertion issue 418 correction; it is not represented as unchanged from the superseded fragment.
- The 56 evidence templates preserve source roles, locators and historical instants. Every primary-source access time is populated and retained; null primary-source times are rejected. Null local derived-evidence times use actual attributed reading. UTC Z normalization preserves instants.
- This formal review is self_review. Researcher352 authored the CoPE source/core/fragment DATA; sibling356 supplied separate source/math/new-core readings. The assembler author prepared current source responsibility/rebind and writer interfaces and earlier ILBFS source work. Root actual reading and each bounded adversarial receipt retain their own roles, without certifying the entire workflow as independent.
- Current owner911 postimage: {"candidate": "MREC, MA-star, SMA-star and iterative threshold search", "url": "https://bayes.cs.ucla.edu/TRIBUTE/part1-heuristics-linked.pdf", "disposition": "partially_addressed", "next_check": "Retain every earlier cohort358/360/361 source obligation and historical resolution, including the distinct Bagchi1985/Nilsson1978/Michie1974 access questions and main7/main10/912 responsibilities. The Reinefeld–Schaeffer–Marsland1985 PNS original and the1987 journal original have now been read; their version/helper/retention boundaries and other cited originals remain pending. Preserve current journal1987 16 bibliography/9 questions/2 incidental routes and ijcai1985 7 bibliography/9 questions/3 added contexts, coordinating duplicate citation/ICAPS04 occurrences without deleting originals. Separately retain the CoPE2025 source family: 38 bibliography occurrences, nine method leads, 12 follow-up questions, the exact 2023 retrieval route and 12 source limitations. The 2025 full source now supports the distinct dual-queue planner and dispatch-dependent value functional; this source coordination does not equate either with the nine prior methods. The 2023 source identity remains pending. Separate 2004/2005 manufacturing primary research and lineage comparison have now been completed at their documented scope; current native identity/mapping and scoped record delivery remain pending. Keep all historical retrieval/status wrappers and the separately attributed later route progress.", "historical_origin": {"path": "research/discovery/20261011T053332Z-foundational-search.json", "pointer": "/new_frontier/8", "sha256": "59f36ac0138b557643ee5368a129b73ceeb064c974192812da38faaaa051ee5f"}, "record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch", "AIMech:MAStar", "AIMech:MAOStar", "AIMech:ITERSSSStar", "AIMech:InformedNegaScout", "AIMech:DUALStar", "AIMech:PartiallyInformedNegaScout", "AIMech:DispatchDependentDualQueuePlanning", "AIMech:DispatchDependentValueFunctional"], "cohort358_resolution": {"record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"], "reason": "Add the independently evidenced MREC (1989), SMA* (1992) and ITS (1994) procedures under the existing memory-search source umbrella. This shared source responsibility does not merge their algorithm identities. Original MA*/MAO* full-text and identity questions remain unresolved; IE retains its separate unchanged owner 912.", "previous_sha256": "87406a76bde4d268904976b031bb2f71ab137c7b81e644d3fe1a66394ed80b4d", "ownership_plan": {"path": "/private/tmp/aimech-cohort358-current-ownership-proposal-20261016/ownership-plan.proposed.json", "sha256": "18880abb169b9d54e364184ff1b8653bcb90e14bd16c25a809959182a4c03f29"}, "source_question_origin": {"path": "/private/tmp/aimech-memory-search-scientific-review-preparation-20261016/historical-source-accounting.json", "sha256": "06a89daf0d68561a588803af11832c08df1f2ca7114d018f807bf403ca6cf614"}}, "cohort360_resolution": {"record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "reason": "Add the two distinct source-scoped 1989 procedures MA* and MAO* under the existing memory-search source owner. The subsequent public scan resolves the base-method source responsibility without merging the algorithms or erasing historical access gaps, cohort358 provenance, variant questions or source qualifications.", "previous_sha256": "06b2078e773673df8df2b9173f21e79f85c11dc4cb70a4d93bb8537d7298647b", "ownership_plan": {"path": "/private/tmp/aimech-cohort360-current-ownership-proposal-20261016/ownership-plan.proposed.json", "sha256": "3d9d9aaeb1d1f99de2f1a1c09de4d15cc8dac24f7b5a6fc60e72df0eff072369"}, "source_question_origin": {"path": "/private/tmp/aimech-ma-mao-cohort360-preparation-20261016/source-questions.structure.json", "sha256": "da8a647a62277aab382265bb9d6aa3a74d0e1ebc9d3c200cac04901a856decb8"}}, "cohort361_resolution": {"record_ids": ["AIMech:ITERSSSStar"], "reason": "Represent the exact Bhattacharyya–Bagchi1986 ITERSSS* bibliography responsibility under the existing memory-search source umbrella, distinct from MA*/MAO*,SMA*,MREC,ITS and StockmanSSS*.", "previous_sha256": "f74140b7cf9fcb1cf801c2dcb40babbd4540f8ecc012320dee621f98c264fca7", "ownership_plan": {"path": "/private/tmp/aimech-cohort361-current-ownership-proposal-20261016/ownership-plan.proposed.json", "sha256": "4471c78603c7d25ed5bb17af99cb435f8a3b0fdfde1446c394dcbe744cbf4b3f"}, "source_question_origin": {"path": "/private/tmp/aimech-svpg-ie-itersss-cohort361-preparation-20261016/source-questions.v2.structure.json", "sha256": "d3e0a339a6c9a440a81ccffa58b4b51fe82ee1add053f0f1ea6cb5eeff4859fa"}}, "cohort362_resolution": {"record_ids": ["AIMech:InformedNegaScout", "AIMech:DUALStar", "AIMech:PartiallyInformedNegaScout"], "reason": "Represent the exact inherited1987 low-overhead source responsibility with distinct INS and DUAL* records, and its separately read1985 PNS source question with Partially Informed NegaScout. This shared source owner does not merge the three algorithms or equate them to MA*/MAO*/ITERSSS*.", "previous_sha256": "2606450c020ef6913baafa9b79233e7d75773b47a61be3ef35bf30685817a153", "ownership_plan": {"path": "/private/tmp/aimech-cohort362-current-ownership-proposal-20261016/ownership-plan.proposed.v2.json", "sha256": "3ebf455f10f0a5eaab9200b751aa8c23c4a0b36ae665c9e783fc26ad01e11e95"}, "source_question_origin": {"path": "/private/tmp/aimech-ins-dual-pns-cohort362-preparation-20261016/source-question-inputs.proposed.json", "sha256": "5e521995a6c2567779cae0141f30291086cf821c18a2c18312574d0e5fa53a0a"}}, "cohort364_resolution": {"record_ids": ["AIMech:DispatchDependentDualQueuePlanning", "AIMech:DispatchDependentValueFunctional"], "reason": "Add the two distinct source-scoped CoPE2025 subjects under the already explicit main911 retrieval/source coordinator. The algorithm and mathematical functional are not aliases of each other, DUAL*, PNS or the earlier memory/search methods. No original source question is deleted or closed.", "previous_sha256": "493c34a0a84e8869b4725edb1ec9ba3ced0fbc401ac5e01058092907ebef8b33", "source_plan": {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/accounting-proposal.json", "sha256": "0374601e324367d49509a44677644c77bac382aab4680e74c8647bbbe4e826b0"}, "source_question_origin": {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/original-source-objects.json", "sha256": "cd9ab0e78e98d34b80aa92fbea0c977e4138ae6c854beed78ad66d4198cb7413"}, "current_source_progress_sha256": "f061cdf13c51a01d417321e21726dd2ff2ddbd6cf3d2524a81e7683932fa65a7", "current_route_progress_sha256": "52d1de20d0dddc3a04e481d72d7c7f605d61f4742f76e836c2f1802a28f321b4"}}
- COPE2025-author-B01: pending_original_source_scope. Read the original OPTIC temporal-preference/continuous-cost work and resolve the Benton2012 versus Coles2012(COLIN) citation distinction; no identity collapse.
- COPE2025-author-B02: pending_original_source_scope. Read the 2018 clock-ticking temporal planner and distinguish planning-only execution assumptions from the 2025 concurrent dispatch procedure.
- COPE2025-author-B03: pending_original_source_scope. Read original forward-chaining partial-order planning and determine the exact component used by the 2025 implementation; do not equate all partial-order planners.
- COPE2025-author-B04: pending_original_source_scope. Read COLIN continuous numeric-change semantics and distinguish it from OPTIC and the 2025 queue controller; coordinate Q6.
- COPE2025-author-B05: pending_original_source_scope. Read the 2024 dispatch/commitment integration and its concurrency/safety assumptions; the 2025 paper is not a substitute for that original.
- COPE2025-author-B06: pending_original_source_scope. Read timed-literal/deadline language/model semantics if needed; a planning-language or deadline specification is not automatically a separate algorithm.
- COPE2025-author-B07: pending_original_source_scope. Read the 2017 durative-action metareasoning method and its computation/action allocation assumptions; preserve its distinction from the 2025 queue procedure.
- COPE2025-author-B08: pending_original_source_scope. Read original deadline-aware online search and its statistics/distribution assumptions; compare exact use in the 2025 completion-time estimate.
- COPE2025-author-B09: pending_original_source_scope. Retain maintained AIMech:WeightedAStar as algorithm context, while this exact Ebendt–Drechsler2009 source remains a separate original-reading question. Current WeightedAStar evidence cites Wilt/Ruml2012, Pohl1970 and Wilt2010, not this citation; do not transfer a quality theorem to the full CoPE planner.
- COPE2025-author-B10: pending_original_source_scope. Read PDDL2.2 specification as model/language context if needed; no new method identity follows from the benchmark language.
- COPE2025-author-B11: pending_original_source_scope. Acquire/read the original 2023 formal concurrent-planning model and resolve whether the historical cope-aaai-23 URL is this exact work/version; cross-link the route without assuming equivalence from its filename.
- COPE2025-author-B12: pending_original_source_scope. Read PDDL2.1 temporal-domain semantics if needed; keep language specification separate from the planner and dispatch functional.
- COPE2025-author-B13: pending_original_source_scope. Read the 2022 commitment procedure and its action/model assumptions; do not infer irreversible-action safety from the 2025 citation.
- COPE2025-author-B14: pending_original_source_scope. Read the Fast Downward system paper and identify the precise component/heuristic relation; maintained EnforcedHillClimbing is an FF2001 controller, not a Fast Downward equivalence.
- COPE2025-author-B15: pending_original_source_scope. Retain the RCLL benchmark/generator/version question; a benchmark reference is not automatically an AI method. Coordinate Q7 empirical scope.
- COPE2025-author-B16: pending_original_source_scope. Read original 1991 metareasoning principles and distinguish value-of-computation framework assumptions from this source-specific value functional.
- COPE2025-author-B17: pending_original_source_scope. Read the 2019 allocation model, exact deadline CDF/survival convention and expiry assumptions; coordinate Q1 without asserting an original implementation defect.
- COPE2025-author-B18: pending_original_source_scope. Read original 2021 DDA/situated temporal planning, deadline equality and dispatch integration; coordinate Q1/Q4 without treating the 2025 background conflict as an established original-source error.
- COPE2025-author-B19: pending_original_source_scope. Read real-time safe interval path planning and its temporal/collision model; maintained LRTA*/LSS/RTAA are context, not evidence that the exact method is represented.
- COPE2025-official-B01: pending_original_source_scope. Read the original OPTIC temporal-preference/continuous-cost work and resolve the Benton2012 versus Coles2012(COLIN) citation distinction; no identity collapse.
- COPE2025-official-B02: pending_original_source_scope. Read the 2018 clock-ticking temporal planner and distinguish planning-only execution assumptions from the 2025 concurrent dispatch procedure.
- COPE2025-official-B03: pending_original_source_scope. Read original forward-chaining partial-order planning and determine the exact component used by the 2025 implementation; do not equate all partial-order planners.
- COPE2025-official-B04: pending_original_source_scope. Read COLIN continuous numeric-change semantics and distinguish it from OPTIC and the 2025 queue controller; coordinate Q6.
- COPE2025-official-B05: pending_original_source_scope. Read the 2024 dispatch/commitment integration and its concurrency/safety assumptions; the 2025 paper is not a substitute for that original.
- COPE2025-official-B06: pending_original_source_scope. Read timed-literal/deadline language/model semantics if needed; a planning-language or deadline specification is not automatically a separate algorithm.
- COPE2025-official-B07: pending_original_source_scope. Read the 2017 durative-action metareasoning method and its computation/action allocation assumptions; preserve its distinction from the 2025 queue procedure.
- COPE2025-official-B08: pending_original_source_scope. Read original deadline-aware online search and its statistics/distribution assumptions; compare exact use in the 2025 completion-time estimate.
- COPE2025-official-B09: pending_original_source_scope. Retain maintained AIMech:WeightedAStar as algorithm context, while this exact Ebendt–Drechsler2009 source remains a separate original-reading question. Current WeightedAStar evidence cites Wilt/Ruml2012, Pohl1970 and Wilt2010, not this citation; do not transfer a quality theorem to the full CoPE planner.
- COPE2025-official-B10: pending_original_source_scope. Read PDDL2.2 specification as model/language context if needed; no new method identity follows from the benchmark language.
- COPE2025-official-B11: pending_original_source_scope. Acquire/read the original 2023 formal concurrent-planning model and resolve whether the historical cope-aaai-23 URL is this exact work/version; cross-link the route without assuming equivalence from its filename.
- COPE2025-official-B12: pending_original_source_scope. Read PDDL2.1 temporal-domain semantics if needed; keep language specification separate from the planner and dispatch functional.
- COPE2025-official-B13: pending_original_source_scope. Read the 2022 commitment procedure and its action/model assumptions; do not infer irreversible-action safety from the 2025 citation.
- COPE2025-official-B14: pending_original_source_scope. Read the Fast Downward system paper and identify the precise component/heuristic relation; maintained EnforcedHillClimbing is an FF2001 controller, not a Fast Downward equivalence.
- COPE2025-official-B15: pending_original_source_scope. Retain the RCLL benchmark/generator/version question; a benchmark reference is not automatically an AI method. Coordinate Q7 empirical scope.
- COPE2025-official-B16: pending_original_source_scope. Read original 1991 metareasoning principles and distinguish value-of-computation framework assumptions from this source-specific value functional.
- COPE2025-official-B17: pending_original_source_scope. Read the 2019 allocation model, exact deadline CDF/survival convention and expiry assumptions; coordinate Q1 without asserting an original implementation defect.
- COPE2025-official-B18: pending_original_source_scope. Read original 2021 DDA/situated temporal planning, deadline equality and dispatch integration; coordinate Q1/Q4 without treating the 2025 background conflict as an established original-source error.
- COPE2025-official-B19: pending_original_source_scope. Read real-time safe interval path planning and its temporal/collision model; maintained LRTA*/LSS/RTAA are context, not evidence that the exact method is represented.
- M1: source_scoped_algorithm_selected_for_addition_with_residuals. Retain exact synchronized queue control, refreshed failure estimates and surrounding dispatch logic; preserve all 12 algorithm limitations, prior-source integration and uninspected implementation/version questions.
- M2: source_scoped_functional_selected_for_addition_with_residuals. Preserve the inclusive completion event, strict complementary failure event, frozen-model qualifications, zero-time endpoint and conditional prefix argument; no global dispatch guarantee or calibrated-probability result is implied.
- M3: pending_problem_setting_originals. Read the defining 2023/2024 originals and decide setting versus procedure scope without promoting the umbrella label to a global alias.
- M4: pending_cited_method_original. Coordinate Q1, Q4 and both B18 occurrences; assess original CDF/dispatch semantics before any separate identity decision.
- M5: pending_formal_model_originals. Coordinate B11/B17 and cope-aaai-23 route; inspect original formal definitions and relation before record decisions.
- M6: retained_experimental_configuration. Bind their exact prior implementations/versions through Coles2024/Shperberg2021 before treating them as separate procedures.
- M7: pending_component_lineage. Coordinate B01/B03/B04 and Q6; current EnforcedHillClimbing/FF context does not resolve these source identities.
- M8: retained_configuration_family. Keep exact parameter/evaluation regime and Q7; do not invent separate records from configuration labels.
- M9: pending_related_method_originals. Coordinate B07/B13/B19 and existing real-time search context; inspect each original before alias or identity claims.
- Q1: pending_scoped_followup. Resolve the background deadline CDF polarity and deadline-equality convention against exact2019/2021 primary equations or a versioned implementation.
- Q2: pending_scoped_followup. Verify explicit pf=1−V computation and treatment of nontermination/infinite search time, success and failure mass before implementation-level curation.
- Q3: pending_scoped_followup. Assess the none/all-prefix reduction under changed/inconsistent relaxed plans and actual ancestor/frontier retention; keep it heuristic unless stronger proof is found.
- Q4: pending_scoped_followup. Read full Coles2024 dispatch logic and Elboher2023 metareasoning model to establish irreversible-action safety, temporal concurrency and exact planner integration boundaries.
- Q5: pending_scoped_followup. Identify an openly versioned author implementation if available; paper says code upon request, but no message is authorized or sent. Preserve exact queue refresh, duplicate/tie and scheduler questions.
- Q6: pending_scoped_followup. Resolve OPTIC/Benton2012 versus OPTIC/Coles2012(COLIN) citations without assuming algorithm identity or code error.
- Q7: pending_scoped_followup. Bind exact benchmark generator/version, prior100 RCLL scenarios, timing simulation, parameter choices and uncertainty if empirical claims are later curated.
- Q8: bounded_granularity_selected_for_addition. Preserve the original representation question and explicit boundaries in both records and the saved review; do not infer extensional novelty or close other source research.
- Q9: pending_scoped_followup. Reconcile official2025 DOI publication metadata with KCL’s observed2029 accepted/in-press listing and the exact author-name forms, preserving both original artifacts.
- Q10: pending_scoped_followup. Inspect the nineteen cited originals by source family when needed; a bibliography entry, benchmark, language specification or experimental priority combination is not automatically a concept.
- Q11: current_mapping_context_reconciled_with_bounded_scope. Keep mapping direction and algorithm/component distinction explicit. The broader 442-label historical screening is attributed, not a fresh semantic review of every ontology definition or a future-snapshot guarantee.
- Q12: existing_source_responsibility_reconciled_for_addition. Keep original 2023/2025/2004 route wrappers and all prior main911 resolutions exact. The cope-aaai-23 source-identity question remains pending; the separate 2004/2005 manufacturing research is complete at its documented scope, with current native identity/mapping and record delivery pending. No source closure follows from adding these two CoPE records.
- COPE-CONTEXT-1: pending_exact_route_source_identity. Inspect the exact historical cope-aaai-23.pdf primary route and compare its formal concurrent planning/execution model with the 2025 background and bibliography. Do not treat a filename as an algorithm or silently resolve any 2023 citation identity.
- Current independent route progress: {"cope2025": {"url": "https://www.cs.unh.edu/~ruml/papers/dual-cope-ijcai-2025.pdf", "historical_wrapper": {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json", "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer": "/predecessor_state/projection/source_accounting/source_groups/journal1987/incidental_retrieval_contexts/0", "sha256": "2ddf5074e69ef9e12de181ebcb1bdc7b4b28ecc1ab30174b21834ff1b0d2f790"}, "later_observation": {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json", "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer": "/source_accounting/separate_subsequent362_route_observation", "sha256": "05bdef12686ac508dfbf58f29e483ed09b3378af16750484a0e052d26ac90330"}, "source_handoff": {"path": "/private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/handoff.final.json", "sha256": "c598052cdade0c245a063da0f1405c1483b3bd9806800555383e8a80bfc25cea"}, "disposition": "full_primary_source_read_and_current_representation_proposed", "assessment": "The exact 2025 author PDF has subsequently been acquired and fully read as text and images by researcher352, with official-version comparison and separate root/sibling mathematical reading. The original unassessed retrieval and later title/abstract-only observations remain exact historical provenance. Current selection represents the dual-queue algorithm and dispatch-dependent value functional as distinct scopes coordinated at main911.", "represented_record_ids": ["AIMech:DispatchDependentDualQueuePlanning", "AIMech:DispatchDependentValueFunctional"], "responsible_owner": {"family": "main", "index": 911}, "next_check": "Retain all 38 bibliography occurrences, nine leads, 12 questions, historical 2023 route and 12 source limitations. Resolve prior-model/deadline conventions, dispatch integration, code/version access and metadata gaps separately; no source-question closure.", "closed": false}, "manufacturing2004": {"url": "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf", "historical_wrappers": [{"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json", "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer": "/predecessor_state/projection/source_accounting/source_groups/journal1987/incidental_retrieval_contexts/1", "sha256": "e8ac25b2d4e72cdf471f97a4c4cda75c81721a0fb4034d4ea11698657ed5e020"}, {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json", "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer": "/predecessor_state/projection/source_accounting/source_groups/ijcai1985/additional_context_questions/0", "sha256": "f6c89fe83e3c65176d45a57cef4004c0298ff250c9a65d008936b141964ed78a"}], "later_observation": {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json", "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer": "/source_accounting/separate_subsequent362_route_observation/original/sources/1"}, "disposition": "separate_primary_research_and_lineage_comparison_completed_curation_pending", "assessment": "The 2004 manufacturing source and expanded 2005 source have now been acquired and read separately, with source-lineage comparison and bounded independent qualifications. This later progress is attributed to those research handoffs and root reading; it does not rewrite either historical retrieval wrapper or the earlier title/abstract observation. Native identity/mapping selection and scoped record delivery remain pending independently of the two CoPE2025 subjects.", "represented_record_ids": [], "responsible_owner": {"family": "main", "index": 911}, "next_check": "Assess the reusable procedure against the current native/AIO context and curate a source-scoped common procedure only after selecting exact identity and qualifications. Preserve the 2004/2005 version differences, resource/temporal regression assumptions, domain restrictions, complete source obligations and both historical route wrappers; no manufacturing record or source closure is claimed here.", "closed": false, "source_handoffs": [{"path": "/private/tmp/aimech-online-manufacturing-source-research-20261016/handoff.final.json", "sha256": "19eabdba886f882522ea3c439054494882a057dd9655c913a48940d2caf181b4"}, {"path": "/private/tmp/aimech-manufacturing2005-lineage-research-20261016/handoff.v2.json", "sha256": "fb7b7f4f6586d8fc3a9ae487e18313d340389dc94d21829de714d8ddebcf4ce9"}]}}
- Pre-insertion scientific correction: [{"issue": "https://github.com/CultureBotAI/AIMech/issues/418", "scope": "pre_insertion_wording", "record_id": "AIMech:DispatchDependentDualQueuePlanning", "claim_id": "temporal-planning-setting", "disposition": {"path": "/private/tmp/aimech-cope-native-core-independent-review-20261016/disposition.v3.json", "sha256": "668ca478de7399a6942ff1bacb397d75febda45b8cadfde51bb67cd9e732aa09"}, "before": "start/end/invariant conditions and effects", "after": "start, invariant and end conditions, and start/end effects", "reason": "Invariant conditions were ambiguously grouped with effects. The source defines start/invariant/end conditions and start/end effects. Corrected before any canonical insertion; all other scientific fields remain unchanged.", "issue_closure_requested": false, "author_correction": {"path": "/private/tmp/aimech-cope-two-native-core-data-20261016/invariant-effects-correction.json", "sha256": "7cd8867de0d90a9da4d7c00740c580c5b1b6aadc7a5dea52af13e5a71493afd1"}, "selected_fragment_handoff": {"path": "/private/tmp/aimech-cope-scientific-review-fragments-20261016/handoff.v3.json", "sha256": "f793022acc7231c48ea1fd0cbaa5b78dc414167aad935623d45eed39f8f37897"}, "selected_preview_validation": {"path": "/private/tmp/aimech-cope-scientific-review-fragments-20261016/root-preview-validation.v2.json", "sha256": "bf9e86fa8d46e05ed24301bf1dd631aeac26d66a68da8a86b550cc72ac5991a2"}}]
- Canonical accounting digest: 1ae6579a867f0faa12725fec815a6a53040cde3a2b25b9a51da16964dd1827c6
- Historical original plan: {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/accounting-proposal.json", "sha256": "0374601e324367d49509a44677644c77bac382aab4680e74c8647bbbe4e826b0"}

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T074705Z-dispatch-dependent-dual-queue-planning-and-value-functional
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of dispatch-dependent dual-queue planning and value
  functional
started_at: '2026-10-16T07:47:04.970198Z'
finished_at: '2026-10-16T07:47:05.461091Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root made scope and insertion decisions and performed canonical
    writing/check/capture. Researcher352 authored source dossier, cores and fragments;
    researcher354 authored current rebind, source accounting and writer/review-assembler
    structure; researcher356 provided prior math advice and independent core/source
    correction review. This is self-review with separately attributed bounded adversarial
    reading, not wholly independent certification.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain distinct source-scoped DRAFT planner and mathematical-functional records
  with 11 claims and 21 limitations. Alternating synchronized queue control is separate
  from its dispatch-conditioned value rule. Fixed-model probability and prefix assumptions,
  estimation, source-version and dispatch-integration limits remain explicit.
source:
  git_revision: cc0c9ef618dae4da01fd32e8e4523e8481bcb138
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/ContinualLearning.yaml
    sha256: c55fe9b9214b2f98c463af6c6756d71d7b070e9f35cb1dbba0a1b400073bf9b3
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/EmbodiedLLM.yaml
    sha256: 86623545536a35b0bce09846c809818e9ff92fc6963d9fdb553c01db7b6db7d8
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/GraphConvolutionalPolicyNetwork.yaml
    sha256: c8a6e283e5d6c5ebc59e1db234d174dc3be79dd0f4a30cdb74e6494e65507d79
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/PolicyLayer.yaml
    sha256: 5bd260a08b56658940d21561cad7ee515e2f031ea860cb040406f102d98252bf
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProportionalHazardsModel.yaml
    sha256: 1869e9ca3c2fd499096d734674e1b865501ad621e925199d4067bd1d7fbd5ba6
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/SurvivalAnalysis.yaml
    sha256: 15110144a2f471cd0005fd8d3de7efdde478a51e5753c547e0cdbc6cd6eeb881
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/aio/TimeSeriesForecasting.yaml
    sha256: 88bbef37663508cc885b40d258cdb6b720c627c0f73af1935c01a372c18b3863
    role: context
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    sha256: 316d4e103eb9ebc513fd94573e8d0ee3c287cc569affd4249d5815db50f6793f
    role: context
  - path: data/curated/DUALStar.yaml
    sha256: 4ae9f919aa1dc766422d88c4d1996d672a50fb6f589c2d45a51dec2c5f0ae181
    role: context
  - path: data/curated/DispatchDependentDualQueuePlanning.yaml
    sha256: a83c718591ddbde6605819a2fe05d47679a48b1124f3316688e683c8139a4625
    role: target
  - path: data/curated/DispatchDependentValueFunctional.yaml
    sha256: 746046361ad3b018fd17b234bae5ea4bc9ced9ea498e9275f802d5b342ffb609
    role: target
  - path: data/curated/DualAveragingHamiltonianStepSize.yaml
    sha256: f140c7da7a288509d8c6afe961ad0d5f2913c52afad65452fe40cd7adedfb319
    role: context
  - path: data/curated/EnforcedHillClimbing.yaml
    sha256: 897d9d1e6437d068a16e83e1bc6431683ac8de49e6ea82ad8a0b553df812a54c
    role: context
  - path: data/curated/EntropySearch.yaml
    sha256: 786a3633b1212b280a7d65b37c7c408ac267554f218daa68d70101651019fafd
    role: context
  - path: data/curated/GreedyBestFirstSearch.yaml
    sha256: ec49328f0c41b8205dfe2816c9a01fdb50fa1e1292eacee71fc2872c7cc54020
    role: context
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 0c3ea32d9b744d1324b6c58ef06d60e5a71a0d327d8c9a880ee89490dbd02a7e
    role: context
  - path: data/curated/LearningRealTimeAStar.yaml
    sha256: 189cfd138de434f3bf350bcf5a18684712c602fc96b3f4ba0abeed5f80e65ceb
    role: context
  - path: data/curated/LocalSearchSpaceLearningRealTimeAStar.yaml
    sha256: 7ac410b5775e73d529bf5d98c93df6f90d187ee35ded28dcb773d4a2f7c461c2
    role: context
  - path: data/curated/MarkovDecisionProcess.yaml
    sha256: 9db1ed4a4b01f70cffafe2bcabe7be214779adacf4d7b31c9348ed5f9f54b907
    role: context
  - path: data/curated/OPTICS.yaml
    sha256: 538df2beab3517c798e773114cdaa01889642464b896623dd978cd02e3cc536a
    role: context
  - path: data/curated/PartiallyObservableMarkovDecisionProcess.yaml
    sha256: 2930142265ec082e972e8ccd05cff84685d611596a58af2af39c4f7b80a16577
    role: context
  - path: data/curated/ProbabilityOfImprovementAcquisition.yaml
    sha256: ab51005ea58b24f63a59266319ef806d1c51b27b7e2a6f48240708a4321af72e
    role: context
  - path: data/curated/QRouting.yaml
    sha256: f518c72943e8f068c2e708fa3c0c64bedd8ad09c86e41ef06a82043ad0255ce4
    role: context
  - path: data/curated/RBFSControlledReexpansion.yaml
    sha256: 6ed34a212cc75612117ef1daf276ba4b5e7a65eeb3c7fbb4a2a9890adccef8e4
    role: context
  - path: data/curated/RealTimeAStar.yaml
    sha256: 4c3378011e027f000c548f4fc56cd67b139c821cc157efe2f1bcf19d6ee3e7d3
    role: context
  - path: data/curated/RealTimeAdaptiveAStar.yaml
    sha256: fd094b4cbc70d64f22498cffa10b5adf4b84b252f2a49cce8faa66d67f5651bc
    role: context
  - path: data/curated/STRIPSPlanning.yaml
    sha256: 6b4e884b76dd3049bb7f3c8103738eafddfd8ed492587ca35adf9c846f49317d
    role: context
  - path: data/curated/WeightedAStar.yaml
    sha256: a5bf05341f6076ecdd8f1ee22f4f6edb8fd87307320d2998a63bee1da8982ae2
    role: context
  - path: docs/curated-concepts.md
    sha256: 79c497b615b9ba703d67ccfc1a925f5d5c3c527aff6ab323cd271aec8e5a40dc
    role: context
  - path: docs/record-review-profile.md
    sha256: 2d3e3a73264523c78930d17b0812e2d22887e25423fe7c38e0ddce922d9cec9d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/reports/dispatch-dependent-dual-queue-planning-and-value-functional/2026-10-16T073721Z-codex-b69b9c.yaml
    sha256: 1ab4ded254fbe4734b6aee68fc3fee614c52edc4e2590873ab5c9f43df787ef4
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261011T034528Z-reinforcement-learning-methods.json
    sha256: 77986405a5635886714741dba5154ac6b6b3aa3e73e7db09269a2cf2782e1c68
    role: context
  - path: research/discovery/20261011T035430Z-attribution-methods.json
    sha256: 8d0137e23ddc9f28ed1c1026d6bcf6310b82a5a11ea447477e0165a98c446500
    role: context
  - path: research/discovery/20261011T044233Z-flow-and-consistency-methods.json
    sha256: 1efa09e3896278d035b838cf5ee1152a70ea383c014c93d3763b6482f41b1d0b
    role: context
  - path: research/discovery/20261011T053332Z-foundational-search.json
    sha256: 59f36ac0138b557643ee5368a129b73ceeb064c974192812da38faaaa051ee5f
    role: context
  - path: research/discovery/20261011T054555Z-best-first-search.json
    sha256: 4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122
    role: context
  - path: research/discovery/20261012T071653Z-support-vector-sphere.json
    sha256: 26a5c75316bf7ab14b402cc64e1369c50418cf1e1a8570955fe5cf655bc8c95d
    role: context
  - path: research/discovery/20261012T073618Z-support-description.json
    sha256: 641021eca5b4c440875934019acbbd46fdca5c084ed5688990fc1fba16e9ebb8
    role: context
  - path: research/discovery/20261015T220733Z-lpga-minimin-and-restored-historical-pointers.json
    sha256: 70390ddcefe988c8db1883ad3c798d430425ca4d9c487ea0944de8bce5b9fa32
    role: context
  - path: research/discovery/20261015T225549Z-autowalksat-fixed-noise-controller.json
    sha256: 7ebc4da1f0029b920b1a71a484cd4bec3af9ac92c34894a06103c3ab247621d4
    role: context
  - path: research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.json
    sha256: cfb1da2d42702cf571b4b3594c8f408f33392a02bc7dd8b79c50a9b09adb279f
    role: context
  - path: research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.md
    sha256: 220b798255e6e9d71006e704b007bbddd8838693efd1c16dd901253d8640d9e6
    role: context
  - path: research/discovery/20261016T010736Z-enforced-hill-climbing-and-local-search-space-lrta.json
    sha256: 516283d10873d36554792b9cc6aac0352cdb000badd1dda54110a330fbd712b7
    role: context
  - path: research/discovery/20261016T020317Z-ritter-gallegos-two-stage-fitting-and-ieco-classification.json
    sha256: a2bf46b1870ccc44138e7c4a5f7a968bf9257a73beea87cbd9471b1177253a04
    role: context
  - path: research/discovery/20261016T025054Z-mrec-sma-star-and-iterative-threshold-search.json
    sha256: 24cac330ffb11e5a38b61d5926488b5332040a1b908f2451697a619a4bf4528c
    role: context
  - path: research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json
    sha256: 5aaa5f8a608224430161ccddacc1cc2cbd7ecedba79e8cec86b52ee81ec4056d
    role: context
  - path: research/discovery/20261016T042347Z-ma-star-and-mao-star.json
    sha256: 4575b88d2f6496e13bfa1772ea3ec12371289f8ffa8e25afa07a8f250eda818c
    role: context
  - path: research/discovery/20261016T051456Z-svpg-iterative-expansion-and-itersss-star.json
    sha256: 19ea70c53bdcf7cce15313526f3cfc28e1ad5c9c9f5b157af56b90ce2a0aecea
    role: context
  - path: research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.json
    sha256: ae343443b190b59e9105d5f509b7f623d4bb5cbe48e8d95d0823dd168812fbe3
    role: context
  - path: research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json
    sha256: 51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed
    role: context
  - path: research/discovery/20261016T073716Z-dispatch-dependent-dual-queue-planning-and-value-functional.json
    sha256: dd37059c78e9699ad1a4db48167f18d0455018e03ab295dcb829a5e2d9a66419
    role: context
  - path: research/discovery/20261016T073716Z-dispatch-dependent-dual-queue-planning-and-value-functional.md
    sha256: 9ebff8edc7967e23b94161f9b3362f9ac81081166ff4cde093a0bb2a418cf5e7
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/render_pages.py
    sha256: 81fae327c4670e269e8928b53f0370e2853767ec8e1b495f6206216ac03f304a
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
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: context
  - path: src/aimech/validation.py
    sha256: 274ed5e6bc97440515a1964b9b21927135a2e9a5a4808ae8daebccd3e172ffcc
    role: context
targets:
- target_id: AIMech:DispatchDependentDualQueuePlanning
  label: Dispatch-dependent dual-queue planning
  path: data/curated/DispatchDependentDualQueuePlanning.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DispatchDependentDualQueuePlanning.yaml
    role: maintained native concept record
- target_id: AIMech:DispatchDependentValueFunctional
  label: Dispatch-dependent value functional
  path: data/curated/DispatchDependentValueFunctional.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DispatchDependentValueFunctional.yaml
    role: maintained native concept record
scope:
  description: Both exact current native records, all claims/limitations, bounded
    identity/mapping and source responsibility. Earlier literal readings remain attributed.
  selection: Exact AIMech:DispatchDependentDualQueuePlanning, AIMech:DispatchDependentValueFunctional.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  exclusions:
  - target: Uninspected bibliography and source versions
    reason: Retained questions are not new concept assertions or completed research.
  - target: Algorithm executions and universal dispatch or planning guarantees
    reason: No source code, benchmark or full executable dispatch proof was run.
checks:
- check_id: check-render
  name: render
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: /private/tmp/aimech-recovery-venv/bin/python -B scripts/render_pages.py
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-render
- check_id: check-source
  name: source
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: /private/tmp/aimech-recovery-venv/bin/python -B -m aimech check-source
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-source
- check_id: check-gate
  name: gate
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: just check
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: vendor
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: just vendored-check
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-vendor
- check_id: check-render-check
  name: render-check
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: /private/tmp/aimech-recovery-venv/bin/python -B scripts/render_pages.py
    --check
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: diff
  status: passed
  required: true
  summary: Actual successful required command; exact output/timing retained.
  command: git diff --check
  exit_code: 0
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - check-diff
evidence:
- evidence_id: cope-scientific-support
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/scientific-support.v3.json
  locator: All selected definition/claim/limitation support rows and source roles.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Author support for exact selected cores; not an independent review.
  snapshot_sha256: eccab94410084c6452a806fc0e2171577f029bd01910f8dc92ff33b61005306c
- evidence_id: cope-native-selection
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/handoff.v3.json
  locator: Selected algorithm v3 and unchanged functional core; narrow invariant-condition
    wording correction.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Prospective selection; no native validation or canonical insertion.
  snapshot_sha256: 8bfffc8e7e57d823862a5058181e333932b495ae1663d92ddf5f247ee50c69d5
- evidence_id: cope-identity-proposal
  kind: record_content
  reference: /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/identity-mapping-proposal.v2.json
  locator: Both prospective candidates, granularity, aliases and mapping rationale.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Historical prospective identity and source-grounded two-scope proposal.
  snapshot_sha256: 4d7d1216a296c36c5504ee6a08ec717e20e659d9e35e35e55f0b4f4382bee146
- evidence_id: cope-historical-search
  kind: search
  reference: /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/collection.json
  locator: Complete captured inventory, matching contents and root search provenance.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Historical prospective search, not later insertion clearance.
  snapshot_sha256: 8586930e3ddaa4bbbb221f5db99371c74d07621832846571893464f109f4c687
  search_scope: 'Snapshot HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f: 807 native
    + 442 AIO records; 4,946 identity occurrences / 3,781 normalized values. Four
    roots include ignored and hidden files, excluding .git internals. All 40 distinct
    matching contents / 183 occurrences were read in the attributed proposal; current
    fragment assembly does not rerun that search.'
- evidence_id: cope-aio-context
  kind: authority
  reference: /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json
  locator: All selected 20 full pinned AIO nodes and 62 incident edges.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Pinned ontology assertions ground mappings, not independent scientific
    evidence for planner performance.
  snapshot_sha256: 922acfc3b3f2da1d223349ada32fd74b1047323d4211fceacb18e2fe82c6bec6
- evidence_id: cope-native-comparisons
  kind: record_content
  reference: /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/native-neighbor-comparisons.json
  locator: All 21 historical closer-neighbor comparison narratives.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Maintained-neighbor context; no current whole-corpus identity claim.
  snapshot_sha256: 083a42dc8e0e358d9b3302687d38df42e7dff87159a490726543f33b3060e543
- evidence_id: cope-source-continuity
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/source-question-continuity.json
  locator: Exact original 38 bibliography occurrences, 9 method leads, 12 questions,
    source limitations and one additional historical route question.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: References retain exact original objects and their unresolved status; no
    ownership closure.
  snapshot_sha256: a8fb76654a8ef8cc0654cf48c905bee16fd101fcaee3621b64aca40ebf586181
- evidence_id: cope-source-roles
  kind: record_content
  reference: /private/tmp/aimech-cope-scientific-review-fragments-20261016/source-metadata-and-roles.v3.json
  locator: Per-record native sources, source artifact roles, reading attribution and
    preview status.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Derived metadata projection; not a primary paper or native validation result.
  snapshot_sha256: b6c5ca0b3b377bae76d7bd9c44c8981786e8956ac27b6a507f4ec7834ed99ab9
- evidence_id: cope-version-comparison
  kind: record_content
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/version-comparison.json
  locator: Author/official extracted-body differences and publication/name metadata.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Same-work version comparison; different PDF bytes do not imply independent
    studies.
  snapshot_sha256: 2f1f64bbae9fec9b328d258f7ae4715519fb65796365237fb176c4fae767061e
- evidence_id: cope-source-acquisition
  kind: record_content
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/network-acquisition.json
  locator: Successful author/official PDF and official metadata acquisition receipts.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual source access/hash provenance; not a curation event.
  snapshot_sha256: 9994c78a1031b6b8d34d1e763f6c778678c55b02b2f03bc4a3b5d147d76aa577
- evidence_id: cope-original-reading
  kind: prior_review
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/handoff.final.json
  locator: Original researcher reading scope and dossier references.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Researcher352 full author text/images and official text-diff reading; earlier
    pending review fields remain historical.
  snapshot_sha256: c598052cdade0c245a063da0f1405c1483b3bd9806800555383e8a80bfc25cea
- evidence_id: cope-independent-math
  kind: prior_review
  reference: /private/tmp/aimech-cope-independent-granularity-math-review-20261016/assessment.json
  locator: Bounded independent granularity, event/complement, endpoint, prefix and
    mapping assessment.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Independent source/proposal review predating native cores; the later full
    core/support review and correction disposition are separately bound through source-role
    metadata.
  snapshot_sha256: a3d15201aaa173df1bc57cc47c245b174a71ec94aee3bc43ff5d97c6d7778e47
- evidence_id: cope-root-bounded-reading
  kind: prior_review
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/root-bounded-source-reading.json
  locator: Root initial author images 2–5 and dossier readings.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Bounded supporting root source reading, without canonical acceptance.
  snapshot_sha256: 15543ee2d23b1a3f6d2e54403146d1d2bd9d23eea6f00afe831293a751a0fe1c
- evidence_id: cope-root-complete-author-reading
  kind: prior_review
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/root-completed-author-reading.json
  locator: Root supplementary images 1,6,7,8 and prior pages 2–5 receipt.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Combined root reading covers all eight author images, figures/tables and
    nineteen references; not all official images or cited originals.
  snapshot_sha256: 9b5fcc794a4765714240613fa09ffcf1a7d33c2b2e621fc4c16086ca506bf6ad
- evidence_id: cope-root-scope-decision
  kind: prior_review
  reference: /private/tmp/aimech-cope-dual-identity-mapping-proposal-20261016/root-prospective-scope-decision.json
  locator: Prospective algorithm/formal-component distinction and functional-only
    mapping.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Root adjudication authorizes prospective DATA preparation, not current
    canonical identity or ownership.
  snapshot_sha256: 4d755cdd9cfdedbf630cf9681b781fc5cece7a318c8962421d9c78369a3b03ad
- evidence_id: cope-native-schema
  kind: authority
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/src/aimech/schema/curated_concept.yaml
  locator: ConceptKind, evidence and directional mapping fields.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Native representation contract, not scientific proof.
  snapshot_sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
- evidence_id: cope-preview-receipt
  kind: record_content
  reference: /private/tmp/aimech-cope-scientific-review-fragments-20261016/preview-yaml-handoff.v3.json
  locator: Actual TEMP serialization provenance and exact core correspondence.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual TEMP serialization and mixed validation linkage; it is not itself
    the native validator result.
  snapshot_sha256: 6a9af98532221bc255aa86b3ec4dd1bfd1496acfb17ccba7d4e76c0ed5f9c66b
- evidence_id: cope-official-paper
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/official2025-network.pdf
  locator: Official title block, pp.8483–8490; comparison to author artifact.
  accessed_at: '2026-10-16T06:32:13Z'
  support: context_only
  summary: Byte-distinct official version of the same IJCAI 2025 work; official image
    reading is not claimed beyond recorded scope.
  snapshot_sha256: a38570275b885d10311deeeb866ec053372f5d5c13077a322ef204969fc4dd20
- evidence_id: cope-official-bibliography
  kind: authority
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/official-bibtex-network.txt
  locator: Official publication title, author forms, venue, pages, year and DOI.
  accessed_at: '2026-10-16T06:32:13Z'
  support: context_only
  summary: Official publication identity; source bytes are independently bound.
  snapshot_sha256: 131cf040ecb78542e230834a71f2f645e956ff3406c4550a789acb6d11300e98
- evidence_id: cope-planner-core
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/DispatchDependentDualQueuePlanning.native-core.v3.json
  locator: Complete selected prospective native core.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Exact selected DATA without invented canonical curation.
  snapshot_sha256: 456a1c3d6eec235f9b7099cc6ee06c58818c47ec45cb81d6da6ac98577f0a392
- evidence_id: cope-planner-preview
  kind: record_content
  reference: /private/tmp/aimech-cope-scientific-review-fragments-20261016/previews/DispatchDependentDualQueuePlanning.v2.yaml
  locator: Complete prospective YAML and actual preview curation.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Exact TEMP serialization; later root native validation is separately bound.
    No canonical insertion or scientific proof.
  snapshot_sha256: 6fcf23c7ba8709e5342df4a7f53d3955014df7a0a0e9b9a4e633a591e3a9a7c1
- evidence_id: cope-author-locator-01
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.1–2, Section 2.1, problem tuple and emission/start-time constraint;
    official pp.8483–8484.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-02
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4 Eq.3; p.5 Section 4.1, f, assumed-dispatch pf and tie-breaking;
    official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-03
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.5, Section 4.1, dual open-list paragraph; official p.8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-04
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.5, Section 4.1, insertion and t_u=100 refresh paragraph; official
    p.8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-05
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.3–4, prior dispatch integration; p.6, opening of Section
    5; official pp.8485–8486 and 8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-06
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.2 Eq.1 and p.3 deterministic-deadline paragraph; official
    pp.8484–8485.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-07
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.2,4–5, Eq.1, Eq.3 and Section 4.1; official pp.8484,8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-08
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4 Eq.3 and monotonicity paragraph; p.5 refresh paragraph;
    official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-09
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.3 search-time/deadline estimation; pp.4–5 functional and algorithm;
    official pp.8485–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-10
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.4–5, Section 3 argument and Section 4 opening; official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-11
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.2–3 background model; p.6 robot-count discussion; official
    pp.8484–8485 and 8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-12
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.5–6, including p.6 footnote 2; official pp.8487–8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-13
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.5–6 and p.8 references; official pp.8487–8488 and 8490.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-14
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.5–6, refresh rule and Section 5 parameter settings; official
    pp.8487–8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-15
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.6–7, Section 5, Figure 1 and Table 1; official pp.8488–8489.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-16
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.6–7, VBS definition, Tables 1–2; official pp.8488–8489.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-17
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.1 title block and p.8 references.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-18
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.5–6, Sections 4.1–5; official pp.8487–8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-functional-core
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/DispatchDependentValueFunctional.native-core.json
  locator: Complete selected prospective native core.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Exact selected DATA without invented canonical curation.
  snapshot_sha256: c488afca0fc8427f97b733c195efb9a7ba513c4ca8e023600e67543ac7b8ccf9
- evidence_id: cope-functional-preview
  kind: record_content
  reference: /private/tmp/aimech-cope-scientific-review-fragments-20261016/previews/DispatchDependentValueFunctional.yaml
  locator: Complete prospective YAML and actual preview curation.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Exact TEMP serialization; later root native validation is separately bound.
    No canonical insertion or scientific proof.
  snapshot_sha256: f8acaaace87d29c12eb3c617d6368300306cee73146e016fb75a88a78c5bc4e5
- evidence_id: cope-author-locator-19
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4, Section 3, footnote 1 and Eq.3; official p.8486.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-20
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.3, latest_start formulas; p.4, all-actions-dispatched limit
    following Eq.3; official pp.8485–8486.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-21
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4, Section 3 prefix construction; official p.8486.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-22
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4 Eq.3 and following monotonicity paragraph; p.5 refresh description;
    official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-23
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.3 minimum latest_start definitions; p.4 prefix discussion;
    p.5 irreversible-dispatch warning; official pp.8485–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-24
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4, final Section 3 argument continuing on p.5; official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-25
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.3 estimation discussion; p.4 Eq.3; official pp.8485–8486.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-26
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.2 Eq.1; p.3 deterministic-deadline paragraph; p.4 Eq.3; official
    pp.8484–8486.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-27
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4 Eq.3 and p.5 Section 4.1; official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-28
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF p.4 monotonicity paragraph; p.5 refreshed M_i; official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-29
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.3–5, abstract model, prefix construction and Section 4 warning;
    p.6 concurrent robots; official pp.8485–8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-30
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.4–5, Section 3 concluding argument; official pp.8486–8487.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-31
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.4–6, Sections 3–5; official pp.8486–8488.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-author-locator-32
  kind: primary_source
  reference: /private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/author2025-network.pdf
  locator: Author PDF pp.6–7, evaluation setup, Tables 1–2; official pp.8488–8489.
  accessed_at: '2026-10-16T06:32:13Z'
  support: supports
  summary: Inspected author paper passage; the assessment states whether its use is
    direct support or a qualified curator deduction.
  snapshot_sha256: b81abd754f7becb49d22adce33803c3493512b54aceebf21ff71db93609d4be7
- evidence_id: cope-root-preview-validation
  kind: validation
  reference: /private/tmp/aimech-cope-scientific-review-fragments-20261016/root-preview-validation.v2.json
  locator: Corrected algorithm exact hash and one new native result; unchanged functional
    exact hash and retained prior result.
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Root performed one revalidation of the corrected algorithm; the functional
    result is retained from its unchanged previously validated bytes. No functional
    rerun, canonical insertion, current-corpus clearance, full-collection check or
    scientific proof is claimed.
  snapshot_sha256: bf9e86fa8d46e05ed24301bf1dd631aeac26d66a68da8a86b550cc72ac5991a2
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-cohort364-write.json
  snapshot_sha256: 5da96b6246610fa63edac9f8753305c9c2dfd3fe311436a520a592c80a4976cf
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual exclusive record/report/history creation, not publication.
- evidence_id: actual-capture
  kind: record_content
  reference: /private/tmp/aimech-cohort364-checks-20261016/actual-capture.json
  snapshot_sha256: a80379b18df19d93344f499258dd54d3b4bf0308b686465ddf45a7b0026fcafc
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual native inspect capture of the current canonical inputs.
- evidence_id: actual-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort364-checks-20261016/root-actual-reading.final.json
  snapshot_sha256: 7420e75ee207cf1a85c6c890bd68df34b32aa36cfddab5b854aae07504bebb4a
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual postcapture scientific and metadata reading with explicit prior
    roles.
- evidence_id: actual-adversarial
  kind: record_content
  reference: /private/tmp/aimech-cohort364-actual-adversarial-review-20261016/assessment.json
  snapshot_sha256: 54c8f5ff7fe67cf48e0b839e611df8895226e73ad94305218ee99a9d0957f348
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Bounded actual record adversarial assessment; earlier source authorship
    is separately disclosed.
- evidence_id: actual-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort364-current-rebind-20261016/current-decisions.accepted.json
  snapshot_sha256: 7ce176a404c3bd8e157bfa7eb8c8e2e0acb9c93d628c3aff2a13141840dbb6cb
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Actual current identities, main 911 postimage, 60 current source-progress
    rows and separately attributed route progress; original source wrappers remain
    exact.
- evidence_id: actual-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T073716Z-dispatch-dependent-dual-queue-planning-and-value-functional.json
  snapshot_sha256: dd37059c78e9699ad1a4db48167f18d0455018e03ab295dcb829a5e2d9a66419
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Canonical report preserves the exact five-field predecessor 363 projection,
    60 original source objects, 12 source limitations, current progress and independent
    2025/2004 route scopes.
- evidence_id: current-rebind
  kind: search
  reference: /private/tmp/aimech-cohort364-current-rebind-20261016/current-rebind-assessment.json
  snapshot_sha256: a7b56c4495108448b715f4f4126d90c7df1a6fc55650192dc1c650eb811eeaa4
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Fresh four-root ignored/hidden-inclusive search and exact record/source/owner
    rebind; earlier literal semantic readings remain attributed.
  search_scope: Four ignored- and hidden-inclusive roots, 49 distinct contents and
    200 occurrences; 40 exact historical semantic readings reused and nine new contents
    read by researcher354. Whole1252record identities reconciled; bounded20AIOtargets62edges.
    Root read the rebind narratives; no whole-ontology semantic absence claim.
- evidence_id: pre-insertion-correction
  kind: record_content
  reference: /private/tmp/aimech-cope-two-native-core-data-20261016/invariant-effects-correction.json
  snapshot_sha256: 7cd8867de0d90a9da4d7c00740c580c5b1b6aadc7a5dea52af13e5a71493afd1
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Before insertion, the temporal-setting claim was corrected to distinguish
    invariant conditions from start/end effects; other accepted science is unchanged.
- evidence_id: pre-insertion-correction-disposition
  kind: prior_review
  reference: /private/tmp/aimech-cope-native-core-independent-review-20261016/disposition.v3.json
  snapshot_sha256: 668ca478de7399a6942ff1bacb397d75febda45b8cadfde51bb67cd9e732aa09
  accessed_at: '2026-10-16T07:47:04.767193Z'
  support: context_only
  summary: Independent source correspondence confirms the narrow issue 418 correction;
    issue closure remains a separate postmerge event.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/render.json
  snapshot_sha256: e96925ecb72f0244a52c5440b8718a9f79d64a159e79b204f740a18b960cdb22
  accessed_at: '2026-10-16T07:37:51.984669Z'
  support: context_only
  summary: Actual required command completed with exit 0.
- evidence_id: check-source
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/source.json
  snapshot_sha256: 94de97a368045e38b872179c444fc3646e3fbfe6c74f898e3c4a947cf7000928
  accessed_at: '2026-10-16T07:37:53.743974Z'
  support: context_only
  summary: Actual required command completed with exit 0.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/gate.json
  snapshot_sha256: e2077969f9fc1112bc6ec4d22580f655cbce02069a2a8d5850cea9880467c142
  accessed_at: '2026-10-16T07:46:19.889772Z'
  support: context_only
  summary: Actual required command completed with exit 0.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/vendor.json
  snapshot_sha256: 45afc334351afd0d862b5e24b28ef81bce0256c1e4a811cd6a7b61035719e2b8
  accessed_at: '2026-10-16T07:46:22.910499Z'
  support: context_only
  summary: Actual required command completed with exit 0.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/render-check.json
  snapshot_sha256: 4f033732370332505559f1eacc0f92c85c13f567254fd2e82beb1c9ccc92eed6
  accessed_at: '2026-10-16T07:46:34.090726Z'
  support: context_only
  summary: Actual required command completed with exit 0.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort364-checks-20261016/diff.json
  snapshot_sha256: c31c21b7aa1f05a08a17f90c3825fa23af3d732bdadae1e6dac1982b7feb80d5
  accessed_at: '2026-10-16T07:46:34.278644Z'
  support: context_only
  summary: Actual required command completed with exit 0.
assessments:
- assessment_id: cope-planner-claim-temporal-planning-setting
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: temporal-planning-setting'
  outcome: supported
  summary: The selected setting is explicit in the primary paper. It separates concurrent
    dispatch from the simpler plan-then-execute setting without importing guarantees
    from the abstract metareasoning background.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-01
  - cope-planner-core
  - cope-scientific-support
  - actual-write
  - actual-reading
  - actual-adversarial
  - pre-insertion-correction
  - pre-insertion-correction-disposition
  details: The described procedure operates in concurrent propositional temporal planning
    with Boolean fluents, nonnegative-duration actions, start, invariant and end conditions,
    and start/end effects, known timed initial literals, and goals. Actions may be
    emitted incrementally before a complete plan is available, but each scheduled
    start must be at or after its emission time. This defines the source setting,
    not a general partially observable or stochastic-execution model.
- assessment_id: cope-planner-claim-goal-and-dispatch-priorities
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: goal-and-dispatch-priorities'
  outcome: supported
  summary: The priorities and tie rule are stated. The failure complement follows
    from the stated success event and tail description; equality mass remains on the
    success side. The distinction is also independently checked in the bounded math
    review.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-02
  - cope-planner-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The first open list uses the weighted goal-progress score f(i)=g(i)+w*h(i),
    where h(i) is relaxed-plan length. The second uses pf(i), described as the estimated
    probability of missing the deadline when all remaining undispatched actions on
    the path to i are assumed dispatched. Ties in pf are broken by f. Relating this
    score to the inclusive success event in Eq.3 gives the explicit interpretation
    pf(i,t)=1−V(i,t)=Pr[m>d(i)−t] for that assumed-dispatch context; this complement
    is an interpretation of the prose interface, not a separately printed executable
    equation.
- assessment_id: cope-planner-claim-alternating-synchronized-frontier
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: alternating-synchronized-frontier'
  outcome: supported
  summary: This is the source-defined procedural distinction. No global stopping,
    duplicate-state or scheduler contract is inferred from this paragraph.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-03
  - cope-planner-core
  - cope-scientific-support
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Node expansion alternates between the f-priority and pf-priority open lists.
    Selecting and removing a state from either list removes it from both; successors
    of the expansion are inserted into both. The lists therefore provide two orderings
    of the shared frontier rather than two independent searches whose outputs are
    combined.
- assessment_id: cope-planner-claim-periodic-failure-score-refresh
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: periodic-failure-score-refresh'
  outcome: supported
  summary: The interval is retained as the described setting rather than an intrinsic
    parameter-free property. Fixed-model monotonicity does not constrain values after
    the estimated model changes.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-04
  - cope-planner-core
  - cope-scientific-support
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The described implementation computes pf when a node is inserted, using
    the current time and then-current remaining-search-time estimate. It recomputes
    pf for all open nodes every 100 expansions with updated time and search-time estimates.
    The mechanism is periodic refresh, not continuously exact scoring or a proof that
    successive estimates are monotonic.
- assessment_id: cope-planner-claim-surrounding-dispatch-integration
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: surrounding-dispatch-integration'
  outcome: supported
  summary: The source explicitly distinguishes expansion from dispatch and states
    the integration/removal. The original 2024 dispatch paper is retained as a follow-up
    rather than newly certified through this citation.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-05
  - cope-planner-core
  - cope-scientific-support
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The evaluated planner is called dual in the paper and is implemented within
    the temporal planner identified there as OPTIC. It retains the earlier Coles et
    al. (2024) dispatch reasoning while removing that method’s restriction of search
    to a promising subtree; the two expansion priorities provide the alternative information-gathering
    mechanism. A dispatch threshold remains. Choosing a frontier node by pf is not
    itself the complete decision to execute an action.
- assessment_id: cope-planner-limitation-1
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 1'
  outcome: supported
  summary: The conflict is visible in the source and independently confirmed; the
    draft does not apply that decreasing step as a valid CDF.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-06
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The background calls D_i a deadline CDF and Eq.1 uses 1−D_i, but the deterministic-deadline
    paragraph then assigns D_i=1 before or on latest_start and 0 afterward. That decreasing
    step is inconsistent with the stated CDF role. Both inspected PDF versions retain
    the presentation conflict; no implementation defect, original-paper erratum or
    silently repaired convention is asserted.
- assessment_id: cope-planner-limitation-2
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 2'
  outcome: supported
  summary: Success/failure polarity and atom handling are explicitly qualified, without
    pretending that the complementary executable equation is printed.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-07
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Eq.3 is a success probability, whereas Section 4.1 describes a failure
    score. The complementary interpretation is pf=Pr[m>d−t], with deadline equality
    counted as success; replacing > by >= needs an additional no-atom convention.
    The background Eq.1 survival convention and Eq.3 inclusive event must not be silently
    unified, and the prose does not provide a complete numerical implementation.
- assessment_id: cope-planner-limitation-3
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 3'
  outcome: supported
  summary: The event-containment and endpoint qualifications are explicit curator
    deductions checked by the independent review, not a claim of strict decrease or
    unchanged estimates.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-08
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: For a fixed remaining-search law M and fixed deadline d, V(t)=Pr[m<=d−t]
    is nonincreasing. For nonnegative m and finite d, V(d)=Pr[m=0] and V(t)=0 is guaranteed
    for t>d (it can also be zero earlier); it need not be zero exactly at d. These
    fixed-model facts do not make the periodically refreshed scores monotonic when
    estimates, relaxed plans or deadlines change.
- assessment_id: cope-planner-limitation-4
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 4'
  outcome: supported
  summary: The source’s estimate status is preserved. No proof for a different weighted-search
    algorithm is imported.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-09
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Remaining search time is estimated from expansion-delay/search statistics
    and relaxed-plan length, while relaxed-plan deadline estimates are explicitly
    described as inadmissible. The scores are modeled probabilities, without a demonstrated
    calibration or error bound. The weighted f form does not transfer a weighted-A*
    quality bound, completeness theorem or successful-dispatch guarantee to this combined
    procedure.
- assessment_id: cope-planner-limitation-5
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 5'
  outcome: supported
  summary: This preserves the argument’s explicit structural condition and separates
    it from an optimal metalevel-policy theorem.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-10
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The none/all prefix argument requires a reasonable ancestor relaxed plan
    and a forward successor with a matching suffix. It matches assumed commitment
    contexts; it does not establish equality of node-specific search-time laws or
    probabilities, preservation of all relevant ancestors in the frontier, or sufficiency
    for arbitrary dispatch policies. Actual irreversible dispatch can make a goal
    unreachable.
- assessment_id: cope-planner-limitation-6
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 6'
  outcome: supported
  summary: Two levels of modeling are distinguished; the record does not collapse
    their action assumptions.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-11
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The abstract metareasoning background uses mutually exclusive non-preemptible
    domain actions with computation concurrent with at most one action. The selected
    temporal-planning setting and multi-robot evaluation allow concurrent actions.
    The abstract exclusivity restriction must not be assigned to every evaluated action,
    nor does that evaluation establish arbitrary uncertain execution dynamics.
- assessment_id: cope-planner-limitation-7
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 7'
  outcome: supported
  summary: The actual access boundary is retained; no unseen implementation behavior
    is asserted.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-12
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The paper gives prose queue and dispatch integration, not a complete executable
    specification. Duplicate-state handling, tie/cycle corner cases, sound dispatch
    and scheduling depend on the underlying planner and earlier dispatch procedure.
    Code is described as available from the authors upon request, but no request,
    code acquisition or algorithm execution occurred in this research.
- assessment_id: cope-planner-limitation-8
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 8'
  outcome: supported
  summary: The source’s two citations remain a metadata/lineage question.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-13
  - cope-version-comparison
  - cope-official-bibliography
  - cope-official-paper
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Section 4.1 associates OPTIC with Benton et al. (2012), while Section 5
    cites Coles et al. (2012) for the implementation and the bibliography names that
    work COLIN. The discrepancy is retained without treating OPTIC and COLIN as aliases
    or diagnosing an implementation error.
- assessment_id: cope-planner-limitation-9
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 9'
  outcome: supported
  summary: Evaluation parameter choices are not elevated to universal or parameter-free
    method properties.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-14
  - cope-root-complete-author-reading
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The evaluation sets w=5, uses the described 100-expansion score refresh
    and tests dispatch thresholds 0.025, 0.1 and 0.25. Removing subtree focus or the
    earlier allocate-t_u search restriction does not remove these parameters. No universally
    best threshold or expansion-rate-independent setting is established.
- assessment_id: cope-planner-limitation-10
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 10'
  outcome: supported
  summary: The benchmark population and timing interpretation remain limits rather
    than a positive general performance claim.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-15
  - cope-root-complete-author-reading
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The reported evaluation uses 100 RCLL scenarios with one-, two- and three-robot
    variants and eight simulated expansion rates from 10 to 1000 expansions per second.
    Those rates are simulated timing, not measured hardware speed or complete queue/heuristic
    overhead. Sums across rates reuse scenarios and are not counts of independent
    scenarios; the experiment does not establish general deployment performance.
- assessment_id: cope-planner-limitation-11
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 11'
  outcome: supported
  summary: The scope of the comparisons and diagnostic is retained without copying
    aggregate superiority into the definition or claims.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-16
  - cope-root-complete-author-reading
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The paper’s virtual best solver selects a configuration by robot-count/domain
    and expansion-rate setting, not an explicitly instance-wise oracle. Aggregate
    coverage advantages are not uniform across settings, and the displayed tables
    report no confidence intervals or repeated-run uncertainty. No causal benefit
    or universal runtime advantage follows from the queue-agreement diagnostic.
- assessment_id: cope-planner-limitation-12
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: limitation 12'
  outcome: supported
  summary: The selected name and prospective mapping reflect later adjudication; the
    original dossier’s earlier undecided wording remains unchanged as historical evidence.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-17
  - cope-official-paper
  - cope-official-bibliography
  - cope-version-comparison
  - cope-identity-proposal
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The author and official PDFs are distinct byte artifacts of one 2025 work,
    with different title-block forms of Shimony’s name and layout metadata. The institutional
    2029 date remains a metadata question. The curated descriptive name disambiguates
    the source-local dual label from the maintained 1987 game-tree DUAL* algorithm;
    aliases are empty. All original bibliography and follow-up questions remain retained,
    not resolved by this draft.
- assessment_id: cope-planner-definition
  area: evidence
  topic: 'Dispatch-dependent dual-queue planning: source-scoped definition'
  outcome: supported
  summary: The definition names the procedure actually described in the paper, excluding
    the mathematical score alone, generic concurrent planning, and an isolated benchmark
    configuration.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-18
  - cope-planner-core
  - cope-scientific-support
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  details: A concurrent temporal-planning search procedure that alternates node expansion
    between a weighted goal-progress open list and a dispatch-conditioned estimated-failure
    open list, synchronizes their frontier membership, and periodically refreshes
    failure estimates while retaining the surrounding temporal planner’s dispatch
    reasoning.
- assessment_id: cope-planner-concept-kind
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: concept kind'
  outcome: supported
  summary: Retain algorithm for the alternating synchronized-frontier procedure, including
    its refresh and dispatch-integration boundary. A mathematical score alone does
    not specify those steps.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-author-locator-18
  - cope-planner-core
  - cope-scientific-support
  - cope-root-scope-decision
  - cope-native-schema
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The source describes node selection, synchronized removal/insertion, score
    refresh and integration with existing dispatch reasoning. The record denotes that
    procedure, not generic CoPE, an OPTIC build or a parameterized evaluation result.
- assessment_id: cope-planner-historical-identity
  area: identity
  topic: 'Dispatch-dependent dual-queue planning: historical prospective identity'
  outcome: supported
  summary: The descriptive name disambiguates the source-local dual label. Empty aliases
    avoid collision with the maintained 1987 game-tree DUAL* and avoid treating CoPE,
    OPTIC or COLIN as aliases.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-identity-proposal
  - cope-historical-search
  - cope-native-comparisons
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  - actual-decisions
  - current-rebind
  details: 'The descriptive name disambiguates the paper’s source-local dual planner.
    It is not an alias for the maintained 1987 game-tree DUAL* algorithm, generic
    dual search, OPTIC/COLIN, or the CoPE problem setting; aliases are empty. The
    independently defined dispatch-dependent value functional is a scoring component,
    not this whole algorithm. Queue control, assumed-dispatch failure interpretation,
    estimation limits and surrounding dispatch logic define the selected scope. The
    identity assessment is historical prospective evidence captured at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f
    on 2026-10-16, with 807 native and 442 AIO records, 4,946 identity-field occurrences
    and 3,781 normalized values. Four repository roots were searched including ignored
    and hidden files; all 40 distinct matching contents were read. Selected comparisons
    covered 96 definition contexts, 21 closer native contexts, and 20 full AIO nodes
    with 62 incident edges. These observations do not allocate a future owner, select
    a future write base or establish whole-ontology semantic absence.


    Current canonical identity: This record denotes the 2025 source-local dual planner
    as a descriptive, disambiguated temporal-planning procedure. Empty aliases preserve
    its distinction from maintained DUAL*, generic dual search, OPTIC/COLIN and the
    CoPE problem setting. Alternating synchronized goal-progress and modeled failure
    priorities, refreshing estimates and retaining the surrounding dispatch logic
    define the algorithm. The separately represented dispatch-dependent value functional
    is a scoring component, not the whole procedure. Current insertion context was
    reconciled at merged commit cc0c9ef618dae4da01fd32e8e4523e8481bcb138: 810 native
    and 442 pinned AIO records, 4,958 identity-field occurrences and 3,790 normalized
    values. Four ignored- and hidden-inclusive roots returned 49 distinct matching
    contents and 200 occurrences. Forty contents reuse exact historical reading with
    attribution; all nine new report/review contents were read. All 1,249 records
    from the historical assessment are byte-identical, and the three added ILBFS/RBFS
    identities and definitions were read as distinct search controls. The 20 selected
    AIO nodes and 62 incident edges were freshly read on the unchanged pin; historical
    whole-label screening and 96-definition/21-neighbor scientific context are attributed
    to their original reading. Existing main911 coordinates source tracking, without
    equating this 2025 family to its nine prior methods or resolving the independent
    2023/2004 routes.'
- assessment_id: cope-planner-aio-mapping
  area: grounding
  topic: 'Dispatch-dependent dual-queue planning: directional AIO assessment'
  outcome: supported
  summary: Retain bounded no-match for the 20 examined pinned AIO targets. A probability-valued
    component, robot application or two-priority search does not map the whole planner
    to a mathematical function, model or learning task.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-identity-proposal
  - cope-aio-context
  - cope-independent-math
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  - actual-decisions
  - current-rebind
  details: 'All 442 pinned AIO IDs, labels and scoped synonyms were screened; 20 relevant
    full nodes, annotations and all 62 incident edges were freshly read. Selection
    follows planning, control, probability/time scoring and the most plausible generic
    type confusions, not a prescribed target count. These are the inspected targets,
    not all conceivable ontology classes. This is the historical 2026-10-16 prospective
    snapshot at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f, with 807 native and
    442 AIO records; it is not a future insertion clearance.


    No examined target identifies or usefully subsumes the two-queue temporal-planning
    procedure. Generic task overlap, robot applications and a mathematical component
    are insufficient mappings of the whole algorithm.


    AIO:MachineLearningTask: The subject is a temporal-planning control procedure.
    Updating search-time estimates is a component, not evidence that this entire procedure
    is a process for building methods that learn from data. The source does not establish
    a specific learning-task identity or an informative method-level related mapping.

    AIO:Model: The complete subject is an executable-style search and dispatch procedure,
    not merely an abstract representation of a complex system. Its embedded probability
    estimates and action model do not identify the planner as this generic model class.

    AIO:MathematicalFunction: The complete planner maintains and alternates two open
    lists, expands nodes and interacts with dispatch decisions. Its functional score
    is a component; mapping that component does not map the entire algorithm to a
    mathematical rule.

    AIO:ReasoningLLM: Explicit planning and deadline reasoning here do not use a large
    language model or language-task inference. The related synonym reasoning cannot
    expand this LLM class into all symbolic planning.

    AIO:EmbodiedLLM: The robot benchmark does not make this symbolic temporal planner
    a language-grounded multimodal model. Application overlap is insufficient.

    AIO:ReinforcementLearning: The inspected procedure searches a supplied temporal
    model and uses deadline/search-time estimates; it does not define reward-driven
    policy learning. Goal progress and information gathering are not by themselves
    reinforcement learning.

    AIO:ReinforcementLearningLLM: There is no language-model reward fine-tuning or
    generated-text objective in the proposed procedure.

    AIO:PolicyLayer: A planner deciding when to expand or dispatch is not a neural-network
    layer predicting an action distribution. Its probability is a timely-search estimate,
    not the output distribution of the described layer.

    AIO:GraphConvolutionalPolicyNetwork: The subject neither uses graph convolution
    nor trains graph-generation policies with rewards and adversarial loss.

    AIO:ActiveLearning: Expanding a node to improve dispatch information does not
    query an annotator for labels of new training points. Information gathering alone
    does not supply the target class identity.

    AIO:TimeSeriesAnalysis: The algorithm is not a task of extracting characteristics
    from time-series observations; wall-clock dependence and refreshed estimates do
    not establish that task relation.

    AIO:TimeSeriesForecasting: Estimated remaining search time guides planning, but
    the full algorithm is not a procedure for forecasting a time-series sequence from
    previous values.

    AIO:SurvivalAnalysis: A tail probability of estimated search completion relative
    to a deadline is a scoring component. The complete planner is not the described
    time-to-event analysis task, and mere use of a probability tail is too generic
    for a useful related mapping.

    AIO:ProportionalHazardsModel: The source does not impose a proportional-hazards
    regression model or multiplicative covariate effect on a hazard rate.

    AIO:ProbabilisticGraphicalModel: The search tree is a space of partial action
    plans, not a graph specifying conditional dependence among random variables. A
    probability estimate at a search node does not turn the controller into this target
    task.

    AIO:MarkovChain: The queue procedure is not a stochastic transition model whose
    next-event law depends only on the preceding state; the source score alone does
    not establish a Markov-chain identity.

    AIO:BayesianNetwork: No directed acyclic conditional-dependence network is specified
    as the algorithm identity.

    AIO:DecisionTree: A search tree of possible plans is not the pinned classification/decision-support
    tree model. Branching does not establish classifier or predictor identity.

    AIO:ContinualLearning: Continued search and distribution refresh do not constitute
    the target deep neural network learning sequential tasks without access to old
    task data.

    AIO:EnsembleLearning: Alternating two priorities on one shared search frontier
    is not a predictive ensemble of learned algorithms.


    Current mapping context: The complete algorithm retains the accepted no-match
    assessment against 20 exact current AIO targets. Generic learning/task/model language,
    temporal probabilities, robot applications and the embedded mathematical score
    do not identify or usefully subsume the two-queue planning controller. The functional-only
    MathematicalFunction relation is not transferred to the planner; this is bounded
    target review, not whole-ontology semantic absence.'
- assessment_id: cope-planner-source-roles
  area: provenance
  topic: 'Dispatch-dependent dual-queue planning: source versions and reading roles'
  outcome: supported
  summary: The author PDF directly supports the definition and positive claims; the
    official PDF and metadata are a same-work version/publication comparison. Author,
    root and independent bounded readings retain separate scope.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-planner-preview
  - cope-source-roles
  - cope-original-reading
  - cope-root-bounded-reading
  - cope-root-complete-author-reading
  - cope-independent-math
  - cope-official-paper
  - cope-official-bibliography
  - cope-version-comparison
  - cope-source-acquisition
  - cope-source-continuity
  - cope-preview-receipt
  - cope-root-preview-validation
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Two native source rows across the records cite one author artifact of one
    work. The official version is retained separately and is not independent experimental
    replication. Root’s complete author-image reading supplements researcher352’s
    original full-text/image/diff work. Independent356 reviewed the full selected
    native cores/support and confirmed the narrow invariant-condition wording correction.
    Issue 418 remains open for actual canonical delivery. Root revalidated only the
    corrected algorithm preview; the unchanged functional preview retains its successful
    earlier result. The mixed receipt binds both exact hashes with problems[]; this
    is structural/claim-source evidence, not canonical or scientific acceptance. The
    exact 38 bibliography occurrences, 9 method leads, 12 questions and one historical
    route question remain linked without closure.
- assessment_id: cope-planner-scope-boundary
  area: scope
  topic: 'Dispatch-dependent dual-queue planning: procedure versus functional boundary'
  outcome: supported
  summary: Retain the controller separately from its mathematical functional and from
    the game-tree DUAL* method. The two selected source scopes are related through
    the explicitly interpreted failure interface, not identical.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  evidence_ids:
  - cope-planner-core
  - cope-scientific-support
  - cope-identity-proposal
  - cope-independent-math
  - cope-root-scope-decision
  - cope-source-continuity
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The complete planner needs queue state, estimate refresh and surrounding
    dispatch decisions. Preserve inclusive success versus strict complementary failure,
    the deadline-CDF conflict, conditional prefix reasoning, finite-deadline endpoint
    qualification, estimated probabilities, and weight/refresh/threshold and evaluation
    limits. No implementation theorem, calibrated success or universal performance
    is asserted.
- assessment_id: cope-functional-claim-prefix-conditioned-success-event
  area: evidence
  topic: 'Dispatch-dependent value functional: prefix-conditioned-success-event'
  outcome: supported
  summary: The formal event, arguments and output type are source-defined. The law
    is estimated, so the probability is not represented as calibrated real-world success.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-19
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: For a node i, partition its path H_i into an already committed prefix H_d
    and a remaining undispatched suffix H_c. Section 3 defines V(H_d,H_c)(t)=Pr_{m~M_i}[t+m<=d(i)],
    where M_i models remaining search time and d(i)=latest_start(H_c,pi_i) depends
    on the undispatched path and a relaxed goal plan. The path-conditioned object
    returns a function of contemplated search start time; it is a modeled success
    probability with an inclusive deadline event.
- assessment_id: cope-functional-claim-path-and-relaxed-plan-deadline
  area: evidence
  topic: 'Dispatch-dependent value functional: path-and-relaxed-plan-deadline'
  outcome: supported
  summary: The construction and empty-path convention are explicit. The relaxed-plan
    bound is not mislabeled admissible.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-20
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The deadline construction takes the smaller of the latest-start bounds
    from the remaining path and the relaxed goal plan. The relaxed-plan bound uses
    the tightest action deadline slack relative to its estimated earliest time. When
    the remaining path is empty its path latest-start bound is taken as infinity,
    leaving the relaxed-plan bound to determine d(i). The latter bound is a heuristic
    estimate in this source.
- assessment_id: cope-functional-claim-family-of-assumed-dispatch-prefixes
  area: evidence
  topic: 'Dispatch-dependent value functional: family-of-assumed-dispatch-prefixes'
  outcome: supported
  summary: The count and partition transformation are explicit; describing a hypothetical
    commitment does not itself select an action.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-21
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: 'Each prefix H_p of the remaining path H_c defines a different assumed-commitment
    context: move H_p to the end of H_d and compute the rule on the residual suffix.
    Thus a path with |H_c| remaining actions defines |H_c|+1 such functionals, including
    the none-dispatched and all-dispatched cases. These are hypothetical value evaluations,
    not commands to execute those actions.'
- assessment_id: cope-functional-claim-fixed-model-monotonicity-and-endpoint
  area: evidence
  topic: 'Dispatch-dependent value functional: fixed-model-monotonicity-and-endpoint'
  outcome: supported
  summary: Set inclusion proves the bounded statement. The mass-at-zero endpoint and
    strict t>d qualification avoid overstating the source prose.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-22
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: With M and d fixed, increasing t can only shrink the event {m<=d−t}, so
    V is nonincreasing, not necessarily strictly decreasing. If m is nonnegative and
    d finite, V(d)=Pr[m=0] and V(t)=0 for t>d. These endpoint statements follow directly
    from Eq.3; they are curator deductions with explicit premises, not a claim that
    zero is reached at t=d or that refreshed estimates remain monotonic.
- assessment_id: cope-functional-claim-frozen-prefix-relaxation
  area: evidence
  topic: 'Dispatch-dependent value functional: frozen-prefix-relaxation'
  outcome: supported
  summary: The inequality is a direct minimum/event argument under explicitly fixed
    quantities. It is not a general dominance claim for dispatching earlier.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-23
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: If the node’s remaining-search law and relaxed-plan bound are held fixed,
    removing assumed-dispatched actions from the minimum over remaining path constraints
    cannot lower that path bound. Consequently the combined deadline and inclusive
    success probability cannot decrease in this frozen comparison. This mathematical
    comparison does not establish that actual irreversible dispatch improves achievable
    success when the frontier, model or feasible alternatives change.
- assessment_id: cope-functional-claim-conditional-none-all-context-correspondence
  area: evidence
  topic: 'Dispatch-dependent value functional: conditional-none-all-context-correspondence'
  outcome: supported
  summary: The source’s reasonableness and successor/suffix assumptions remain explicit,
    and no equality of M_i across nodes is inferred.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-24
  - cope-functional-core
  - cope-scientific-support
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The source motivates evaluating only the none-dispatched and all-dispatched
    cases across a forward search when a reasonable relaxed plan at an ancestor has
    a successor whose relaxed plan is the matching suffix. Under that structural assumption,
    an intermediate assumed commitment at the successor can correspond to an all-dispatched
    commitment context at the ancestor. This is a conditional correspondence of action
    contexts, not a proof of equal node-specific probabilities or an optimal policy
    over all prefixes.
- assessment_id: cope-functional-limitation-1
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 1'
  outcome: supported
  summary: The functional is an assessed mathematical object in a planning model,
    not a true-world success oracle.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-25
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The probability is conditional on estimated remaining search time and an
    estimated deadline. Expansion-delay statistics and relaxed-plan length inform
    M_i, and the relaxed-plan deadline is explicitly inadmissible. No calibration,
    error bound or certainty that the chosen plan remains executable follows from
    Eq.3.
- assessment_id: cope-functional-limitation-2
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 2'
  outcome: supported
  summary: The formal definition is usable within its stated event while the separate
    presentation conflict stays explicit.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-26
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: 'The background deadline-CDF notation conflicts with its later decreasing
    deterministic step: Eq.1 uses 1−D_i after calling D_i a CDF, while the next page
    assigns one before/on the deadline and zero afterward. Eq.3’s inclusive success
    event is retained on its own terms. No silent repair of the background convention
    or identity between its strict survival event and Eq.3 at atoms is asserted.'
- assessment_id: cope-functional-limitation-3
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 3'
  outcome: supported
  summary: The inferred interface is separated from the source-defined functional
    and from finite-precision implementation choices.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-27
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The planner’s pf is described as a failure tail although Eq.3 defines success.
    The interface pf=1−V=Pr[m>d−t] is an explicit complementary interpretation, not
    a separately printed executable formula. Equality belongs to success; a >= failure
    event can differ when the law has atoms. The functional alone does not prescribe
    that queue interface or its numerical implementation.
- assessment_id: cope-functional-limitation-4
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 4'
  outcome: supported
  summary: The source prose is narrowed to an event-theoretic statement with complete
    endpoint premises.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-28
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Monotonicity requires the distribution and deadline to remain fixed. With
    nonnegative remaining time and finite d, vanishing is assured for t>d, while V(d)=Pr[m=0]
    can be positive. Updating M_i, the relaxed plan or deadline can increase a later
    recomputed value; infinite/no global deadlines and negative remaining times are
    outside the stated endpoint deduction.
- assessment_id: cope-functional-limitation-5
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 5'
  outcome: supported
  summary: The formal input transformation does not provide a safe-dispatch theorem
    or a universal action model.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-29
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Removing path constraints in a frozen hypothetical comparison is not the
    same as performing an irreversible action. Actual dispatch restricts accessible
    subtrees and can invalidate alternatives or make a goal unreachable. The source’s
    background abstract action exclusivity also must not be transferred unqualified
    to the concurrent multi-robot planner.
- assessment_id: cope-functional-limitation-6
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 6'
  outcome: supported
  summary: Only the supported action-context correspondence is claimed; probability
    equality and policy sufficiency remain unresolved.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-30
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The none/all argument assumes matching ancestor/successor relaxed-plan
    structure. It does not prove equality of M_i laws, equal probabilities, retention
    of the requisite ancestors in OPEN, or sufficiency for arbitrary prefix policies
    and changed temporal constraints. It is a heuristic reduction argument rather
    than a general optimal metareasoning theorem.
- assessment_id: cope-functional-limitation-7
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 7'
  outcome: supported
  summary: The separate mathematical_method boundary is source-grounded and prevents
    conflating a score with a complete algorithm.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-31
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: This rule does not specify an estimator-training procedure, full search
    algorithm, scheduler, dispatch threshold, stopping test or duplicate-state policy.
    The source’s dual planner adds alternating queues, tie-breaking and periodic refresh,
    and uses an earlier dispatch integration. Those control rules and their reported
    performance are not properties of the mathematical functional alone.
- assessment_id: cope-functional-limitation-8
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 8'
  outcome: supported
  summary: Empirical evidence is retained as context and is not promoted to an independent
    functional-performance claim.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-32
  - cope-root-complete-author-reading
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The simulated RCLL coverage and queue-agreement results assess complete
    configured planners rather than isolated correctness or calibration of this functional.
    Their repeated scenario/rate combinations, chosen weights and thresholds, and
    absent table uncertainty measures do not establish a universal benefit of the
    rule in other domains.
- assessment_id: cope-functional-limitation-9
  area: scope
  topic: 'Dispatch-dependent value functional: limitation 9'
  outcome: supported
  summary: The exact inherited source questions persist even where the native record
    uses a narrower mathematical scope.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-source-continuity
  - cope-author-locator-17
  - cope-official-paper
  - cope-official-bibliography
  - cope-version-comparison
  - cope-identity-proposal
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Evidence comes from the byte-distinct author and official PDFs of one 2025
    work, not independent replications. Name-form, institutional-date and OPTIC/COLIN
    citation differences remain in research context. No referenced original algorithm
    or implementation is newly certified here, and all 38 bibliography occurrences
    and original follow-up objects remain unchanged in the retained ledger.
- assessment_id: cope-functional-definition
  area: evidence
  topic: 'Dispatch-dependent value functional: source-scoped definition'
  outcome: supported
  summary: The source independently defines this probability-valued time function.
    Mathematical_method describes the rule itself; the broad AIO mapping does not
    attach to the complete planner.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-19
  - cope-functional-core
  - cope-scientific-support
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  details: 'A dispatch-prefix-conditioned mathematical rule that returns, as a function
    of a contemplated search start time t, the modeled probability of finishing remaining
    search no later than a latest-start deadline estimated from the undispatched path
    and a relaxed goal plan: V(H_d,H_c)(t)=Pr_{m~M_i}[t+m<=d(i)].'
- assessment_id: cope-functional-concept-kind
  area: scope
  topic: 'Dispatch-dependent value functional: concept kind'
  outcome: supported
  summary: Retain mathematical_method for the independently defined path-conditioned
    value rule, which returns a probability-valued function of time. It is not a second
    queue algorithm or a condition-only evaluation criterion.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-author-locator-19
  - cope-functional-core
  - cope-scientific-support
  - cope-root-scope-decision
  - cope-native-schema
  - cope-independent-math
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Section 3 gives mathematical inputs, a named functional and Eq.3 separately
    from the later controller. PI acquisition supplies a representation precedent,
    not evidence of identity or the reason for splitting by itself.
- assessment_id: cope-functional-historical-identity
  area: identity
  topic: 'Dispatch-dependent value functional: historical prospective identity'
  outcome: supported
  summary: The singularized source name and empty aliases denote the function-valued
    construction. Search-completion time, dispatch-prefix conditions and deadlines
    distinguish it from improvement acquisitions and generic time-dependent node scores.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-identity-proposal
  - cope-historical-search
  - cope-native-comparisons
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  - actual-decisions
  - current-rebind
  details: 'The singularized name follows Section 3; aliases are empty. This source-defined
    rule maps a path/dispatch context to a function of time and is represented separately
    from the dual-queue controller that uses a complementary failure interpretation.
    It differs from probability-of-improvement acquisition because its random variable,
    conditioning, deadline and purpose concern search completion under dispatch commitments.
    That representation precedent does not establish identity. The functional-only
    broad_match to AIO:MathematicalFunction is a local inference; no upstream axiom,
    probability calibration or planner mapping is asserted. The identity assessment
    is historical prospective evidence captured at HEAD 7991f0c2fdc71e461117fc598529a2678ea8ef7f
    on 2026-10-16, with 807 native and 442 AIO records, 4,946 identity-field occurrences
    and 3,781 normalized values. Four repository roots were searched including ignored
    and hidden files; all 40 distinct matching contents were read. Selected comparisons
    covered 96 definition contexts, 21 closer native contexts, and 20 full AIO nodes
    with 62 incident edges. These observations do not allocate a future owner, select
    a future write base or establish whole-ontology semantic absence.


    Current canonical identity: This record denotes the Section 3 dispatch-prefix-conditioned
    mathematical rule, with empty aliases and a scope distinct from the dual-queue
    controller. It maps planning/dispatch context to a function of contemplated search
    start time and models completion no later than the estimated deadline. Probability-of-improvement
    acquisition has a different random variable, conditioning, event and purpose;
    it is representation context, not an alias. The inclusive event, frozen-model
    assumptions, source deadline-CDF discrepancy and conditional prefix argument remain
    explicit. Current insertion context was reconciled at merged commit cc0c9ef618dae4da01fd32e8e4523e8481bcb138:
    810 native and 442 pinned AIO records, 4,958 identity-field occurrences and 3,790
    normalized values. Four ignored- and hidden-inclusive roots returned 49 distinct
    matching contents and 200 occurrences. Forty contents reuse exact historical reading
    with attribution; all nine new report/review contents were read. All 1,249 records
    from the historical assessment are byte-identical, and the three added ILBFS/RBFS
    identities and definitions were read as distinct search controls. The 20 selected
    AIO nodes and 62 incident edges were freshly read on the unchanged pin; historical
    whole-label screening and 96-definition/21-neighbor scientific context are attributed
    to their original reading. Existing main911 coordinates source tracking, without
    equating this 2025 family to its nine prior methods or resolving the independent
    2023/2004 routes.'
- assessment_id: cope-functional-aio-mapping
  area: grounding
  topic: 'Dispatch-dependent value functional: directional AIO assessment'
  outcome: supported
  summary: Retain the local broad_match to AIO:MathematicalFunction for this formal
    rule only. The target is broader and does not impose an activation-only or scalar-only
    restriction; this does not map the complete planner or assert an upstream axiom.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-identity-proposal
  - cope-aio-context
  - cope-independent-math
  - cope-root-scope-decision
  - actual-write
  - actual-reading
  - actual-adversarial
  - actual-decisions
  - current-rebind
  details: 'AIO:MathematicalFunction (broad_match): The proposed subject is the Section
    3 mathematical rule itself: it maps a dispatch-prefix-conditioned planning context
    to a function of search start time. The target’s definition covers a rule assigning
    a dependent value from independent values and does not require a neural activation
    or a scalar codomain. This is a local broad-match inference for the functional
    only, not an exact match, an upstream axiom, a proof of probability calibration
    or a mapping of the complete planner.


    Current mapping context: Retain the local broad_match to AIO:MathematicalFunction:
    the target is broader than this dispatch-conditioned rule assigning a modeled
    probability from planning context and time. The exact current node, annotations
    and incident edges support that abstraction. No exact match, upstream axiom, calibration
    claim or mapping of the full planner is asserted.'
- assessment_id: cope-functional-source-roles
  area: provenance
  topic: 'Dispatch-dependent value functional: source versions and reading roles'
  outcome: supported
  summary: The author PDF directly supports the definition and positive claims; the
    official PDF and metadata are a same-work version/publication comparison. Author,
    root and independent bounded readings retain separate scope.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-functional-preview
  - cope-source-roles
  - cope-original-reading
  - cope-root-bounded-reading
  - cope-root-complete-author-reading
  - cope-independent-math
  - cope-official-paper
  - cope-official-bibliography
  - cope-version-comparison
  - cope-source-acquisition
  - cope-source-continuity
  - cope-preview-receipt
  - cope-root-preview-validation
  - actual-write
  - actual-reading
  - actual-adversarial
  details: Two native source rows across the records cite one author artifact of one
    work. The official version is retained separately and is not independent experimental
    replication. Root’s complete author-image reading supplements researcher352’s
    original full-text/image/diff work. Independent356 reviewed the full selected
    native cores/support and confirmed the narrow invariant-condition wording correction.
    Issue 418 remains open for actual canonical delivery. Root revalidated only the
    corrected algorithm preview; the unchanged functional preview retains its successful
    earlier result. The mixed receipt binds both exact hashes with problems[]; this
    is structural/claim-source evidence, not canonical or scientific acceptance. The
    exact 38 bibliography occurrences, 9 method leads, 12 questions and one historical
    route question remain linked without closure.
- assessment_id: cope-functional-scope-boundary
  area: scope
  topic: 'Dispatch-dependent value functional: procedure versus functional boundary'
  outcome: supported
  summary: Retain the mathematical functional as a separate source-defined scope;
    it can be evaluated without alternating queues. It neither chooses a full dispatch
    policy nor supplies the complete search/scheduling procedure.
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - cope-functional-core
  - cope-scientific-support
  - cope-identity-proposal
  - cope-independent-math
  - cope-root-scope-decision
  - cope-source-continuity
  - actual-write
  - actual-reading
  - actual-adversarial
  details: The inclusive event is m<=d−t. The interpreted complementary queue failure
    event is m>d−t. Fixed-law/fixed-deadline monotonicity is nonincrease; with m>=0
    and finite d, V(d)=P(m=0), while zero is guaranteed for t>d and may occur earlier.
    The none/all argument matches commitment contexts under a relaxed-plan correspondence,
    not equal laws/probabilities or arbitrary-policy optimality.
- assessment_id: actual-pair-governance
  area: provenance
  topic: Actual canonical correspondence, current source responsibility and checks
  outcome: supported
  summary: Two DRAFT records retain 11 claims and 21 limitations, two declared source
    rows and one defining work. Five creation outputs and the actual capture/checks
    are bound. Only main 911 is updated; all 60 original source objects, 12 source
    limitations and current progress remain queryable alongside the complete incoming
    363 projection. Issue 418 corrected a temporal-effects wording ambiguity before
    insertion. No algorithm execution, source exhaustion, source-question closure
    or publication completion is implied.
  details: Current capture contains 79 inputs. Earlier source/version/identity readings
    remain attributed. The 2025 CoPE source progress and separate 2004/2005 manufacturing
    research progress do not overwrite historical retrieval observations. Manufacturing
    current identity and record curation remain pending independently.
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  evidence_ids:
  - actual-write
  - actual-capture
  - actual-reading
  - actual-adversarial
  - actual-decisions
  - actual-report
  - current-rebind
  - pre-insertion-correction
  - pre-insertion-correction-disposition
  - check-render
  - check-source
  - check-gate
  - check-vendor
  - check-render-check
  - check-diff
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  rationale: Retain the source-defined dual-queue controller within the qualified
    temporal-planning setting. The descriptive label is distinct from 1987 DUAL* and
    generic CoPE. Its mathematical scoring component does not exhaust its stateful
    control and dispatch integration. Current canonical identity and source responsibility
    are bound to the actual decisions; no source-question closure is claimed.
  evidence_ids:
  - cope-planner-core
  - cope-identity-proposal
  - cope-independent-math
  - cope-source-continuity
  - actual-decisions
  - current-rebind
  - actual-reading
- action: retain
  target_ids:
  - AIMech:DispatchDependentValueFunctional
  rationale: Retain the independently defined value functional as a mathematical_method
    with the functional-only broad mapping. Its probability event and hypothetical-prefix
    interface are separate from an algorithm, calibrated success oracle or universal
    dispatch policy. Current canonical identity and source responsibility are bound
    to the actual decisions; no source-question closure is claimed.
  evidence_ids:
  - cope-functional-core
  - cope-identity-proposal
  - cope-aio-context
  - cope-independent-math
  - cope-source-continuity
  - actual-decisions
  - current-rebind
  - actual-reading
- action: split
  target_ids:
  - AIMech:DispatchDependentDualQueuePlanning
  - AIMech:DispatchDependentValueFunctional
  rationale: Partition the two selected source scopes into the stateful search/dispatch
    controller and the independently defined mathematical value rule. This complete
    disjoint partition explains the current two-record representation; it does not
    split, rename or mutate an existing canonical record or AIO class. Shared paper,
    event interface or benchmark does not make the two concepts identical.
  evidence_ids:
  - cope-identity-proposal
  - cope-root-scope-decision
  - cope-independent-math
  - cope-scientific-support
  - actual-decisions
  - current-rebind
  - actual-reading
  proposed_groups:
  - label: Stateful temporal-planning controller
    target_ids:
    - AIMech:DispatchDependentDualQueuePlanning
  - label: Dispatch-prefix-conditioned mathematical functional
    target_ids:
    - AIMech:DispatchDependentValueFunctional
limitations:
- Mechanism and proof statements remain source-scoped; retained interface, cost, version
  and experimental qualifications are substantive.
- Historical primary and neighbor readings retain their original authorship; the current
  postmerge rebind does not claim a new whole-paper or whole-ontology reading.
- Native structural validation does not prove scientific truth. Canonical review save/check,
  committed-head review and publication are subsequent operations.
notes:
- The 44 selected corrected scientific assessments retain their scientific statements/support.
  Actual evidence links are appended; two historical identity details and two mapping
  details receive separate current context. The three boundary rationales record actual
  context instead of a prospective prerequisite. The selected temporal-planning-setting
  assessment already incorporates the pre-insertion issue 418 correction; it is not
  represented as unchanged from the superseded fragment.
- The 56 evidence templates preserve source roles, locators and historical instants.
  Every primary-source access time is populated and retained; null primary-source
  times are rejected. Null local derived-evidence times use actual attributed reading.
  UTC Z normalization preserves instants.
- This formal review is self_review. Researcher352 authored the CoPE source/core/fragment
  DATA; sibling356 supplied separate source/math/new-core readings. The assembler
  author prepared current source responsibility/rebind and writer interfaces and earlier
  ILBFS source work. Root actual reading and each bounded adversarial receipt retain
  their own roles, without certifying the entire workflow as independent.
- 'Current owner911 postimage: {"candidate": "MREC, MA-star, SMA-star and iterative
  threshold search", "url": "https://bayes.cs.ucla.edu/TRIBUTE/part1-heuristics-linked.pdf",
  "disposition": "partially_addressed", "next_check": "Retain every earlier cohort358/360/361
  source obligation and historical resolution, including the distinct Bagchi1985/Nilsson1978/Michie1974
  access questions and main7/main10/912 responsibilities. The Reinefeld–Schaeffer–Marsland1985
  PNS original and the1987 journal original have now been read; their version/helper/retention
  boundaries and other cited originals remain pending. Preserve current journal1987
  16 bibliography/9 questions/2 incidental routes and ijcai1985 7 bibliography/9 questions/3
  added contexts, coordinating duplicate citation/ICAPS04 occurrences without deleting
  originals. Separately retain the CoPE2025 source family: 38 bibliography occurrences,
  nine method leads, 12 follow-up questions, the exact 2023 retrieval route and 12
  source limitations. The 2025 full source now supports the distinct dual-queue planner
  and dispatch-dependent value functional; this source coordination does not equate
  either with the nine prior methods. The 2023 source identity remains pending. Separate
  2004/2005 manufacturing primary research and lineage comparison have now been completed
  at their documented scope; current native identity/mapping and scoped record delivery
  remain pending. Keep all historical retrieval/status wrappers and the separately
  attributed later route progress.", "historical_origin": {"path": "research/discovery/20261011T053332Z-foundational-search.json",
  "pointer": "/new_frontier/8", "sha256": "59f36ac0138b557643ee5368a129b73ceeb064c974192812da38faaaa051ee5f"},
  "record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch",
  "AIMech:MAStar", "AIMech:MAOStar", "AIMech:ITERSSSStar", "AIMech:InformedNegaScout",
  "AIMech:DUALStar", "AIMech:PartiallyInformedNegaScout", "AIMech:DispatchDependentDualQueuePlanning",
  "AIMech:DispatchDependentValueFunctional"], "cohort358_resolution": {"record_ids":
  ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"],
  "reason": "Add the independently evidenced MREC (1989), SMA* (1992) and ITS (1994)
  procedures under the existing memory-search source umbrella. This shared source
  responsibility does not merge their algorithm identities. Original MA*/MAO* full-text
  and identity questions remain unresolved; IE retains its separate unchanged owner
  912.", "previous_sha256": "87406a76bde4d268904976b031bb2f71ab137c7b81e644d3fe1a66394ed80b4d",
  "ownership_plan": {"path": "/private/tmp/aimech-cohort358-current-ownership-proposal-20261016/ownership-plan.proposed.json",
  "sha256": "18880abb169b9d54e364184ff1b8653bcb90e14bd16c25a809959182a4c03f29"}, "source_question_origin":
  {"path": "/private/tmp/aimech-memory-search-scientific-review-preparation-20261016/historical-source-accounting.json",
  "sha256": "06a89daf0d68561a588803af11832c08df1f2ca7114d018f807bf403ca6cf614"}},
  "cohort360_resolution": {"record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "reason":
  "Add the two distinct source-scoped 1989 procedures MA* and MAO* under the existing
  memory-search source owner. The subsequent public scan resolves the base-method
  source responsibility without merging the algorithms or erasing historical access
  gaps, cohort358 provenance, variant questions or source qualifications.", "previous_sha256":
  "06b2078e773673df8df2b9173f21e79f85c11dc4cb70a4d93bb8537d7298647b", "ownership_plan":
  {"path": "/private/tmp/aimech-cohort360-current-ownership-proposal-20261016/ownership-plan.proposed.json",
  "sha256": "3d9d9aaeb1d1f99de2f1a1c09de4d15cc8dac24f7b5a6fc60e72df0eff072369"}, "source_question_origin":
  {"path": "/private/tmp/aimech-ma-mao-cohort360-preparation-20261016/source-questions.structure.json",
  "sha256": "da8a647a62277aab382265bb9d6aa3a74d0e1ebc9d3c200cac04901a856decb8"}},
  "cohort361_resolution": {"record_ids": ["AIMech:ITERSSSStar"], "reason": "Represent
  the exact Bhattacharyya–Bagchi1986 ITERSSS* bibliography responsibility under the
  existing memory-search source umbrella, distinct from MA*/MAO*,SMA*,MREC,ITS and
  StockmanSSS*.", "previous_sha256": "f74140b7cf9fcb1cf801c2dcb40babbd4540f8ecc012320dee621f98c264fca7",
  "ownership_plan": {"path": "/private/tmp/aimech-cohort361-current-ownership-proposal-20261016/ownership-plan.proposed.json",
  "sha256": "4471c78603c7d25ed5bb17af99cb435f8a3b0fdfde1446c394dcbe744cbf4b3f"}, "source_question_origin":
  {"path": "/private/tmp/aimech-svpg-ie-itersss-cohort361-preparation-20261016/source-questions.v2.structure.json",
  "sha256": "d3e0a339a6c9a440a81ccffa58b4b51fe82ee1add053f0f1ea6cb5eeff4859fa"}},
  "cohort362_resolution": {"record_ids": ["AIMech:InformedNegaScout", "AIMech:DUALStar",
  "AIMech:PartiallyInformedNegaScout"], "reason": "Represent the exact inherited1987
  low-overhead source responsibility with distinct INS and DUAL* records, and its
  separately read1985 PNS source question with Partially Informed NegaScout. This
  shared source owner does not merge the three algorithms or equate them to MA*/MAO*/ITERSSS*.",
  "previous_sha256": "2606450c020ef6913baafa9b79233e7d75773b47a61be3ef35bf30685817a153",
  "ownership_plan": {"path": "/private/tmp/aimech-cohort362-current-ownership-proposal-20261016/ownership-plan.proposed.v2.json",
  "sha256": "3ebf455f10f0a5eaab9200b751aa8c23c4a0b36ae665c9e783fc26ad01e11e95"}, "source_question_origin":
  {"path": "/private/tmp/aimech-ins-dual-pns-cohort362-preparation-20261016/source-question-inputs.proposed.json",
  "sha256": "5e521995a6c2567779cae0141f30291086cf821c18a2c18312574d0e5fa53a0a"}},
  "cohort364_resolution": {"record_ids": ["AIMech:DispatchDependentDualQueuePlanning",
  "AIMech:DispatchDependentValueFunctional"], "reason": "Add the two distinct source-scoped
  CoPE2025 subjects under the already explicit main911 retrieval/source coordinator.
  The algorithm and mathematical functional are not aliases of each other, DUAL*,
  PNS or the earlier memory/search methods. No original source question is deleted
  or closed.", "previous_sha256": "493c34a0a84e8869b4725edb1ec9ba3ced0fbc401ac5e01058092907ebef8b33",
  "source_plan": {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/accounting-proposal.json",
  "sha256": "0374601e324367d49509a44677644c77bac382aab4680e74c8647bbbe4e826b0"}, "source_question_origin":
  {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/original-source-objects.json",
  "sha256": "cd9ab0e78e98d34b80aa92fbea0c977e4138ae6c854beed78ad66d4198cb7413"}, "current_source_progress_sha256":
  "f061cdf13c51a01d417321e21726dd2ff2ddbd6cf3d2524a81e7683932fa65a7", "current_route_progress_sha256":
  "52d1de20d0dddc3a04e481d72d7c7f605d61f4742f76e836c2f1802a28f321b4"}}'
- 'COPE2025-author-B01: pending_original_source_scope. Read the original OPTIC temporal-preference/continuous-cost
  work and resolve the Benton2012 versus Coles2012(COLIN) citation distinction; no
  identity collapse.'
- 'COPE2025-author-B02: pending_original_source_scope. Read the 2018 clock-ticking
  temporal planner and distinguish planning-only execution assumptions from the 2025
  concurrent dispatch procedure.'
- 'COPE2025-author-B03: pending_original_source_scope. Read original forward-chaining
  partial-order planning and determine the exact component used by the 2025 implementation;
  do not equate all partial-order planners.'
- 'COPE2025-author-B04: pending_original_source_scope. Read COLIN continuous numeric-change
  semantics and distinguish it from OPTIC and the 2025 queue controller; coordinate
  Q6.'
- 'COPE2025-author-B05: pending_original_source_scope. Read the 2024 dispatch/commitment
  integration and its concurrency/safety assumptions; the 2025 paper is not a substitute
  for that original.'
- 'COPE2025-author-B06: pending_original_source_scope. Read timed-literal/deadline
  language/model semantics if needed; a planning-language or deadline specification
  is not automatically a separate algorithm.'
- 'COPE2025-author-B07: pending_original_source_scope. Read the 2017 durative-action
  metareasoning method and its computation/action allocation assumptions; preserve
  its distinction from the 2025 queue procedure.'
- 'COPE2025-author-B08: pending_original_source_scope. Read original deadline-aware
  online search and its statistics/distribution assumptions; compare exact use in
  the 2025 completion-time estimate.'
- 'COPE2025-author-B09: pending_original_source_scope. Retain maintained AIMech:WeightedAStar
  as algorithm context, while this exact Ebendt–Drechsler2009 source remains a separate
  original-reading question. Current WeightedAStar evidence cites Wilt/Ruml2012, Pohl1970
  and Wilt2010, not this citation; do not transfer a quality theorem to the full CoPE
  planner.'
- 'COPE2025-author-B10: pending_original_source_scope. Read PDDL2.2 specification
  as model/language context if needed; no new method identity follows from the benchmark
  language.'
- 'COPE2025-author-B11: pending_original_source_scope. Acquire/read the original 2023
  formal concurrent-planning model and resolve whether the historical cope-aaai-23
  URL is this exact work/version; cross-link the route without assuming equivalence
  from its filename.'
- 'COPE2025-author-B12: pending_original_source_scope. Read PDDL2.1 temporal-domain
  semantics if needed; keep language specification separate from the planner and dispatch
  functional.'
- 'COPE2025-author-B13: pending_original_source_scope. Read the 2022 commitment procedure
  and its action/model assumptions; do not infer irreversible-action safety from the
  2025 citation.'
- 'COPE2025-author-B14: pending_original_source_scope. Read the Fast Downward system
  paper and identify the precise component/heuristic relation; maintained EnforcedHillClimbing
  is an FF2001 controller, not a Fast Downward equivalence.'
- 'COPE2025-author-B15: pending_original_source_scope. Retain the RCLL benchmark/generator/version
  question; a benchmark reference is not automatically an AI method. Coordinate Q7
  empirical scope.'
- 'COPE2025-author-B16: pending_original_source_scope. Read original 1991 metareasoning
  principles and distinguish value-of-computation framework assumptions from this
  source-specific value functional.'
- 'COPE2025-author-B17: pending_original_source_scope. Read the 2019 allocation model,
  exact deadline CDF/survival convention and expiry assumptions; coordinate Q1 without
  asserting an original implementation defect.'
- 'COPE2025-author-B18: pending_original_source_scope. Read original 2021 DDA/situated
  temporal planning, deadline equality and dispatch integration; coordinate Q1/Q4
  without treating the 2025 background conflict as an established original-source
  error.'
- 'COPE2025-author-B19: pending_original_source_scope. Read real-time safe interval
  path planning and its temporal/collision model; maintained LRTA*/LSS/RTAA are context,
  not evidence that the exact method is represented.'
- 'COPE2025-official-B01: pending_original_source_scope. Read the original OPTIC temporal-preference/continuous-cost
  work and resolve the Benton2012 versus Coles2012(COLIN) citation distinction; no
  identity collapse.'
- 'COPE2025-official-B02: pending_original_source_scope. Read the 2018 clock-ticking
  temporal planner and distinguish planning-only execution assumptions from the 2025
  concurrent dispatch procedure.'
- 'COPE2025-official-B03: pending_original_source_scope. Read original forward-chaining
  partial-order planning and determine the exact component used by the 2025 implementation;
  do not equate all partial-order planners.'
- 'COPE2025-official-B04: pending_original_source_scope. Read COLIN continuous numeric-change
  semantics and distinguish it from OPTIC and the 2025 queue controller; coordinate
  Q6.'
- 'COPE2025-official-B05: pending_original_source_scope. Read the 2024 dispatch/commitment
  integration and its concurrency/safety assumptions; the 2025 paper is not a substitute
  for that original.'
- 'COPE2025-official-B06: pending_original_source_scope. Read timed-literal/deadline
  language/model semantics if needed; a planning-language or deadline specification
  is not automatically a separate algorithm.'
- 'COPE2025-official-B07: pending_original_source_scope. Read the 2017 durative-action
  metareasoning method and its computation/action allocation assumptions; preserve
  its distinction from the 2025 queue procedure.'
- 'COPE2025-official-B08: pending_original_source_scope. Read original deadline-aware
  online search and its statistics/distribution assumptions; compare exact use in
  the 2025 completion-time estimate.'
- 'COPE2025-official-B09: pending_original_source_scope. Retain maintained AIMech:WeightedAStar
  as algorithm context, while this exact Ebendt–Drechsler2009 source remains a separate
  original-reading question. Current WeightedAStar evidence cites Wilt/Ruml2012, Pohl1970
  and Wilt2010, not this citation; do not transfer a quality theorem to the full CoPE
  planner.'
- 'COPE2025-official-B10: pending_original_source_scope. Read PDDL2.2 specification
  as model/language context if needed; no new method identity follows from the benchmark
  language.'
- 'COPE2025-official-B11: pending_original_source_scope. Acquire/read the original
  2023 formal concurrent-planning model and resolve whether the historical cope-aaai-23
  URL is this exact work/version; cross-link the route without assuming equivalence
  from its filename.'
- 'COPE2025-official-B12: pending_original_source_scope. Read PDDL2.1 temporal-domain
  semantics if needed; keep language specification separate from the planner and dispatch
  functional.'
- 'COPE2025-official-B13: pending_original_source_scope. Read the 2022 commitment
  procedure and its action/model assumptions; do not infer irreversible-action safety
  from the 2025 citation.'
- 'COPE2025-official-B14: pending_original_source_scope. Read the Fast Downward system
  paper and identify the precise component/heuristic relation; maintained EnforcedHillClimbing
  is an FF2001 controller, not a Fast Downward equivalence.'
- 'COPE2025-official-B15: pending_original_source_scope. Retain the RCLL benchmark/generator/version
  question; a benchmark reference is not automatically an AI method. Coordinate Q7
  empirical scope.'
- 'COPE2025-official-B16: pending_original_source_scope. Read original 1991 metareasoning
  principles and distinguish value-of-computation framework assumptions from this
  source-specific value functional.'
- 'COPE2025-official-B17: pending_original_source_scope. Read the 2019 allocation
  model, exact deadline CDF/survival convention and expiry assumptions; coordinate
  Q1 without asserting an original implementation defect.'
- 'COPE2025-official-B18: pending_original_source_scope. Read original 2021 DDA/situated
  temporal planning, deadline equality and dispatch integration; coordinate Q1/Q4
  without treating the 2025 background conflict as an established original-source
  error.'
- 'COPE2025-official-B19: pending_original_source_scope. Read real-time safe interval
  path planning and its temporal/collision model; maintained LRTA*/LSS/RTAA are context,
  not evidence that the exact method is represented.'
- 'M1: source_scoped_algorithm_selected_for_addition_with_residuals. Retain exact
  synchronized queue control, refreshed failure estimates and surrounding dispatch
  logic; preserve all 12 algorithm limitations, prior-source integration and uninspected
  implementation/version questions.'
- 'M2: source_scoped_functional_selected_for_addition_with_residuals. Preserve the
  inclusive completion event, strict complementary failure event, frozen-model qualifications,
  zero-time endpoint and conditional prefix argument; no global dispatch guarantee
  or calibrated-probability result is implied.'
- 'M3: pending_problem_setting_originals. Read the defining 2023/2024 originals and
  decide setting versus procedure scope without promoting the umbrella label to a
  global alias.'
- 'M4: pending_cited_method_original. Coordinate Q1, Q4 and both B18 occurrences;
  assess original CDF/dispatch semantics before any separate identity decision.'
- 'M5: pending_formal_model_originals. Coordinate B11/B17 and cope-aaai-23 route;
  inspect original formal definitions and relation before record decisions.'
- 'M6: retained_experimental_configuration. Bind their exact prior implementations/versions
  through Coles2024/Shperberg2021 before treating them as separate procedures.'
- 'M7: pending_component_lineage. Coordinate B01/B03/B04 and Q6; current EnforcedHillClimbing/FF
  context does not resolve these source identities.'
- 'M8: retained_configuration_family. Keep exact parameter/evaluation regime and Q7;
  do not invent separate records from configuration labels.'
- 'M9: pending_related_method_originals. Coordinate B07/B13/B19 and existing real-time
  search context; inspect each original before alias or identity claims.'
- 'Q1: pending_scoped_followup. Resolve the background deadline CDF polarity and deadline-equality
  convention against exact2019/2021 primary equations or a versioned implementation.'
- 'Q2: pending_scoped_followup. Verify explicit pf=1−V computation and treatment of
  nontermination/infinite search time, success and failure mass before implementation-level
  curation.'
- 'Q3: pending_scoped_followup. Assess the none/all-prefix reduction under changed/inconsistent
  relaxed plans and actual ancestor/frontier retention; keep it heuristic unless stronger
  proof is found.'
- 'Q4: pending_scoped_followup. Read full Coles2024 dispatch logic and Elboher2023
  metareasoning model to establish irreversible-action safety, temporal concurrency
  and exact planner integration boundaries.'
- 'Q5: pending_scoped_followup. Identify an openly versioned author implementation
  if available; paper says code upon request, but no message is authorized or sent.
  Preserve exact queue refresh, duplicate/tie and scheduler questions.'
- 'Q6: pending_scoped_followup. Resolve OPTIC/Benton2012 versus OPTIC/Coles2012(COLIN)
  citations without assuming algorithm identity or code error.'
- 'Q7: pending_scoped_followup. Bind exact benchmark generator/version, prior100 RCLL
  scenarios, timing simulation, parameter choices and uncertainty if empirical claims
  are later curated.'
- 'Q8: bounded_granularity_selected_for_addition. Preserve the original representation
  question and explicit boundaries in both records and the saved review; do not infer
  extensional novelty or close other source research.'
- 'Q9: pending_scoped_followup. Reconcile official2025 DOI publication metadata with
  KCL’s observed2029 accepted/in-press listing and the exact author-name forms, preserving
  both original artifacts.'
- 'Q10: pending_scoped_followup. Inspect the nineteen cited originals by source family
  when needed; a bibliography entry, benchmark, language specification or experimental
  priority combination is not automatically a concept.'
- 'Q11: current_mapping_context_reconciled_with_bounded_scope. Keep mapping direction
  and algorithm/component distinction explicit. The broader 442-label historical screening
  is attributed, not a fresh semantic review of every ontology definition or a future-snapshot
  guarantee.'
- 'Q12: existing_source_responsibility_reconciled_for_addition. Keep original 2023/2025/2004
  route wrappers and all prior main911 resolutions exact. The cope-aaai-23 source-identity
  question remains pending; the separate 2004/2005 manufacturing research is complete
  at its documented scope, with current native identity/mapping and record delivery
  pending. No source closure follows from adding these two CoPE records.'
- 'COPE-CONTEXT-1: pending_exact_route_source_identity. Inspect the exact historical
  cope-aaai-23.pdf primary route and compare its formal concurrent planning/execution
  model with the 2025 background and bibliography. Do not treat a filename as an algorithm
  or silently resolve any 2023 citation identity.'
- 'Current independent route progress: {"cope2025": {"url": "https://www.cs.unh.edu/~ruml/papers/dual-cope-ijcai-2025.pdf",
  "historical_wrapper": {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json",
  "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer":
  "/predecessor_state/projection/source_accounting/source_groups/journal1987/incidental_retrieval_contexts/0",
  "sha256": "2ddf5074e69ef9e12de181ebcb1bdc7b4b28ecc1ab30174b21834ff1b0d2f790"}, "later_observation":
  {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json",
  "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer":
  "/source_accounting/separate_subsequent362_route_observation", "sha256": "05bdef12686ac508dfbf58f29e483ed09b3378af16750484a0e052d26ac90330"},
  "source_handoff": {"path": "/private/tmp/aimech-dispatch-dependent-cope-source-research-20261016/handoff.final.json",
  "sha256": "c598052cdade0c245a063da0f1405c1483b3bd9806800555383e8a80bfc25cea"}, "disposition":
  "full_primary_source_read_and_current_representation_proposed", "assessment": "The
  exact 2025 author PDF has subsequently been acquired and fully read as text and
  images by researcher352, with official-version comparison and separate root/sibling
  mathematical reading. The original unassessed retrieval and later title/abstract-only
  observations remain exact historical provenance. Current selection represents the
  dual-queue algorithm and dispatch-dependent value functional as distinct scopes
  coordinated at main911.", "represented_record_ids": ["AIMech:DispatchDependentDualQueuePlanning",
  "AIMech:DispatchDependentValueFunctional"], "responsible_owner": {"family": "main",
  "index": 911}, "next_check": "Retain all 38 bibliography occurrences, nine leads,
  12 questions, historical 2023 route and 12 source limitations. Resolve prior-model/deadline
  conventions, dispatch integration, code/version access and metadata gaps separately;
  no source-question closure.", "closed": false}, "manufacturing2004": {"url": "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf",
  "historical_wrappers": [{"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json",
  "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer":
  "/predecessor_state/projection/source_accounting/source_groups/journal1987/incidental_retrieval_contexts/1",
  "sha256": "e8ac25b2d4e72cdf471f97a4c4cda75c81721a0fb4034d4ea11698657ed5e020"}, {"report":
  {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json",
  "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer":
  "/predecessor_state/projection/source_accounting/source_groups/ijcai1985/additional_context_questions/0",
  "sha256": "f6c89fe83e3c65176d45a57cef4004c0298ff250c9a65d008936b141964ed78a"}],
  "later_observation": {"report": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T065212Z-iterative-linear-best-first-search-rbfs-epsilon-and-rbfs-kth-root.json",
  "sha256": "51ef12569ed3a7030a559d1192180881aa4d4c3630413b292f1c7e5e6c2436ed"}, "pointer":
  "/source_accounting/separate_subsequent362_route_observation/original/sources/1"},
  "disposition": "separate_primary_research_and_lineage_comparison_completed_curation_pending",
  "assessment": "The 2004 manufacturing source and expanded 2005 source have now been
  acquired and read separately, with source-lineage comparison and bounded independent
  qualifications. This later progress is attributed to those research handoffs and
  root reading; it does not rewrite either historical retrieval wrapper or the earlier
  title/abstract observation. Native identity/mapping selection and scoped record
  delivery remain pending independently of the two CoPE2025 subjects.", "represented_record_ids":
  [], "responsible_owner": {"family": "main", "index": 911}, "next_check": "Assess
  the reusable procedure against the current native/AIO context and curate a source-scoped
  common procedure only after selecting exact identity and qualifications. Preserve
  the 2004/2005 version differences, resource/temporal regression assumptions, domain
  restrictions, complete source obligations and both historical route wrappers; no
  manufacturing record or source closure is claimed here.", "closed": false, "source_handoffs":
  [{"path": "/private/tmp/aimech-online-manufacturing-source-research-20261016/handoff.final.json",
  "sha256": "19eabdba886f882522ea3c439054494882a057dd9655c913a48940d2caf181b4"}, {"path":
  "/private/tmp/aimech-manufacturing2005-lineage-research-20261016/handoff.v2.json",
  "sha256": "fb7b7f4f6586d8fc3a9ae487e18313d340389dc94d21829de714d8ddebcf4ce9"}]}}'
- 'Pre-insertion scientific correction: [{"issue": "https://github.com/CultureBotAI/AIMech/issues/418",
  "scope": "pre_insertion_wording", "record_id": "AIMech:DispatchDependentDualQueuePlanning",
  "claim_id": "temporal-planning-setting", "disposition": {"path": "/private/tmp/aimech-cope-native-core-independent-review-20261016/disposition.v3.json",
  "sha256": "668ca478de7399a6942ff1bacb397d75febda45b8cadfde51bb67cd9e732aa09"}, "before":
  "start/end/invariant conditions and effects", "after": "start, invariant and end
  conditions, and start/end effects", "reason": "Invariant conditions were ambiguously
  grouped with effects. The source defines start/invariant/end conditions and start/end
  effects. Corrected before any canonical insertion; all other scientific fields remain
  unchanged.", "issue_closure_requested": false, "author_correction": {"path": "/private/tmp/aimech-cope-two-native-core-data-20261016/invariant-effects-correction.json",
  "sha256": "7cd8867de0d90a9da4d7c00740c580c5b1b6aadc7a5dea52af13e5a71493afd1"}, "selected_fragment_handoff":
  {"path": "/private/tmp/aimech-cope-scientific-review-fragments-20261016/handoff.v3.json",
  "sha256": "f793022acc7231c48ea1fd0cbaa5b78dc414167aad935623d45eed39f8f37897"}, "selected_preview_validation":
  {"path": "/private/tmp/aimech-cope-scientific-review-fragments-20261016/root-preview-validation.v2.json",
  "sha256": "bf9e86fa8d46e05ed24301bf1dd631aeac26d66a68da8a86b550cc72ac5991a2"}}]'
- 'Canonical accounting digest: 1ae6579a867f0faa12725fec815a6a53040cde3a2b25b9a51da16964dd1827c6'
- 'Historical original plan: {"path": "/private/tmp/aimech-cope-source-accounting-proposal-20261016/accounting-proposal.json",
  "sha256": "0374601e324367d49509a44677644c77bac382aab4680e74c8647bbbe4e826b0"}'
tags:
- source-scoped
- temporal-planning
- mathematical-method
```
