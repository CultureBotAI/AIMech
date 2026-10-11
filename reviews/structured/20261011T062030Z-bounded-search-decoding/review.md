# Scientific self-review of bounded graph search and sequence decoding

- Review: 20261011T062030Z-bounded-search-decoding
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T06:20:30Z
- Finished UTC: 2026-10-11T06:20:30Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All six maintained identities, mechanisms and explicit AIO assessments are supported in their stated scopes. No actionable record defect remains in this review. Source-level nonmonotonicity concerns, implementation limits and unresolved candidates are retained without promoting DRAFT status.

## Scope And Provenance

Full review of three bounded graph-search procedures and three related sequence-decoding procedures.

Selection: Exactly the six IDs in the bounded-search-decoding discovery ledger; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 4a65f776d6b3b19b343f10a23a92d5256547d445.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BreadthFirstBranchAndBound | data/curated/BreadthFirstBranchAndBound.yaml | maintained | Breadth-first branch-and-bound search |
| AIMech:BreadthFirstIDAStar | data/curated/BreadthFirstIDAStar.yaml | maintained | Breadth-first iterative-deepening A-star |
| AIMech:DivideConquerBeamSearch | data/curated/DivideConquerBeamSearch.yaml | maintained | Divide-and-conquer beam search |
| AIMech:SequenceBestFirstBeamSearch | data/curated/SequenceBestFirstBeamSearch.yaml | maintained | Best-first beam search with per-length budgets |
| AIMech:SequenceAStarBeamSearch | data/curated/SequenceAStarBeamSearch.yaml | maintained | A-star beam search for sequence decoding |
| AIMech:MemoryReducedSequenceBeamSearch | data/curated/MemoryReducedSequenceBeamSearch.yaml | maintained | Memory-reduced best-first beam search for sequence decoding |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | Checked 141 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | Checked 29 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 29,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 58.67s<br>Checked 442 record(s); 0 failed.<br>Checked 141 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 29 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 29,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite-tree analysis | passed | False | AIMech:SequenceBestFirstBeamSearch | Actual run and assertion completed: layer beam returns 10, per-length best-first with exact remaining bounds returns -5. Output saved in research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json. |

## Scientific And Domain Assessments

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:BreadthFirstBranchAndBound.

The BFBnB search strategy is distinguished from BFIDA*, which obtains bounds by repeated searches, and from width-pruned beam search. Breadth-first heuristic search names the broader family in Zhou and Hansen; that umbrella phrase is not asserted as an exact alias. Frontier, sparse-memory and layered duplicate-detection implementations are alternatives, not mandatory simultaneous components. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

The scope is uniform positive costs and an admissible heuristic. A valid upper bound must cover a real solution for a single-pass optimal-solution guarantee; an unsuccessful hypothetical contour does not establish that the original problem is unsolvable. The layered implementation needs enough previous-layer information for the graph structure; retaining one previous layer is not a universal duplicate-elimination rule for directed graphs. Memory-saving implementations can still run out of memory in a large frontier. The paper explicitly does not prove universally lower peak memory than best-first search. The f≥U option is valid for improving an actual incumbent, not for an inclusive hypothetical contour with no stored solution. Preserving the incumbent when no improvement exists is an explicit operational consequence of that distinction. The record does not certify the printed pseudocode for all base cases, graph-locality claims under every pruning policy, or nonuniform-cost extensions.

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:BreadthFirstIDAStar.

BFIDA* changes the inner traversal of cost-contour iterative deepening to breadth-first branch-and-bound. It is distinct from depth-first IDA*, depth-limited iterative-deepening DFS, and a single BFBnB search with a supplied incumbent bound. The memory implementation can use frontier or layered duplicate handling. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

The hypothetical threshold is inclusive. Reusing strict incumbent pruning at T=f(start) without a retained solution would be a different procedure. This method repeats breadth-first contours and retains frontier/duplicate information; it does not inherit the path-linear storage of depth-first IDA*. The asymptotic node-expansion analysis assumes exponential growth of distinct nodes per iteration; the directed-graph result additionally constrains solution depth relative to stored layers. It is not an unconditional wall-clock optimum. Large layers and tie contours can still be costly. Solvable finite-depth cases require sufficient memory; no universal termination guarantee on infinite unsolvable graphs is asserted.

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:DivideConquerBeamSearch.

Divide-and-conquer beam search is the approximate search procedure introduced by Zhou and Hansen in 2004. It differs from divide-and-conquer beam-stack search, which adds systematic backtracking and replay under saved beam ranges. Relay reconstruction alone does not revisit every branch discarded by beam pruning. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

Permanent width pruning can discard every solution path; ordinary DCBS is neither complete nor guaranteed optimal. The reported current, previous, next and relay layers count retained search-node layers, not all temporary successors, recursive reconstruction state or output storage. The original developed search setting has uniform edge costs. Its planning implementation uses an inadmissible additive heuristic for ranking and a separate admissible heuristic for lower bounds; ranking and safe cost pruning must not be conflated. Larger permitted beams and reconstruction improvements do not establish monotonic quality or a universal speed advantage.

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:SequenceBestFirstBeamSearch.

This is the 2020 sequence-decoding meaning of best-first beam search. Its per-length budget is distinct from AIMech:GlobalFrontierBeamSearch, which caps the entire open list. The qualified name avoids treating those different pruning rules as exact synonyms. The h=0 procedure is a specialization of the paper’s A-star beam framework. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

The finite beam is an approximation to exact sequence-model decoding; equality to a specified beam procedure is not global MAP optimality. Sequence length limits, EOS handling and compatible deterministic tie conventions are part of the comparison. Arbitrary implementations with different stopping or tie rules need not return identical hypotheses. Queue counts are counts of retained hypotheses, not total bytes including neural states, model parameters, backpointers and temporary successors. No numerical speedup or benchmark-quality claim is curated. The beam-equivalence claim is restricted to nonincreasing scores and h=0. The paper also asserts a nonmonotonic stop-only extension; this record does not adopt that guarantee because a saved curator finite-tree counterexample exposes a conflict with unchanged per-length pruning. The optimized queue-of-beams representation can retain hypotheses at several lengths. The per-length budget is not a global queue-capacity bound.

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:SequenceAStarBeamSearch.

This names the finite-beam A-star decoding framework in Meister, Vieira and Cotterell, not every algorithm informally called A-star beam search. The h=0 specialization has its own per-length best-first record. A finite per-length budget distinguishes the framework from unpruned A* and from a whole-frontier capacity cap. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

The finite beam is an approximation to exact sequence-model decoding; equality to a specified beam procedure is not global MAP optimality. Sequence length limits, EOS handling and compatible deterministic tie conventions are part of the comparison. Arbitrary implementations with different stopping or tie rules need not return identical hypotheses. Queue counts are counts of retained hypotheses, not total bytes including neural states, model parameters, backpointers and temporary successors. No numerical speedup or benchmark-quality claim is curated. Admissibility of h does not preserve the zero-heuristic beam’s output after finite pruning. This is explicitly acknowledged in Section 4.1. Unpruned A-star guarantees cannot be transferred to the finite-beam framework merely because its heuristic is admissible. No unrestricted nonmonotonic stopping theorem is asserted. Application to a particular score requires checking the direction and validity of its future-reward bound, terminal behavior and stopping policy.

### Identity, pruning rules, conditional guarantees, memory scope and AIO assessment

evidence: supported. Targets: AIMech:MemoryReducedSequenceBeamSearch.

This is the memory-reduced variant in Meister, Vieira and Cotterell Section 3.3. Its eviction first chooses the earliest active length, so it differs from globally removing the worst-ranked hypothesis. It also differs from the base per-length best-first procedure, which can retain hypotheses at several lengths without this extra capacity pruning. No normalized identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations, scope contrasts and DCBSS substring matches, plus seven public certificate-data substring matches, not existing concept records.

The finite beam is an approximation to exact sequence-model decoding; equality to a specified beam procedure is not global MAP optimality. Sequence length limits, EOS handling and compatible deterministic tie conventions are part of the comparison. Arbitrary implementations with different stopping or tie rules need not return identical hypotheses. Queue counts are counts of retained hypotheses, not total bytes including neural states, model parameters, backpointers and temporary successors. No numerical speedup or benchmark-quality claim is curated. Additional capacity eviction can remove paths retained by the unmodified beam procedure, so its same-output guarantee is not inherited. The memory/quality tradeoff is empirical and problem dependent. The queue cap does not bound the entire decoder or neural model memory. The earliest-length eviction is not a global worst-score eviction rule. No guarantee for arbitrary nonmonotonic scores or globally optimal sequence decoding is asserted.

### Attempts to transfer guarantees across different pruning rules

scope: supported. Targets: AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch.

The records preserve the distinctions that defeat unconditional guarantee claims: actual versus hypothetical cost bounds, width pruning versus complete backtracking, per-length versus whole-frontier limits, heuristic changes to beam membership, and extra queue eviction.

BFIDA-star explicitly uses a nonnegative admissible heuristic with h(goal)=0 in its unit-cost scope. No nonuniform-cost theorem, universal peak-memory improvement, unconditional wall-clock optimum or global-MAP claim is asserted. Source inconsistencies and unresolved implementation assumptions remain explicit limitations.

### Scope and provenance of the nonmonotone illustration

evidence: supported. Targets: AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch.

The finite-tree calculation supports withholding the broad stop-only equivalence claim under the stated interpretation, while leaving the monotone decoder record intact.

All completions have depth three and the discrepancy is not tie-dependent. The illustration omits optional older-layer deletion, stores completed incumbents rather than repeated EOS padding, and uses an exact descendant bound. It is a scoped curator analysis, not an author erratum, benchmark replication, general proof checker or implementation audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:BreadthFirstBranchAndBound, AIMech:BreadthFirstIDAStar, AIMech:DivideConquerBeamSearch, AIMech:SequenceBestFirstBeamSearch, AIMech:SequenceAStarBeamSearch, AIMech:MemoryReducedSequenceBeamSearch. A supplied cost bound, repeated cost contours, approximate width pruning with relay reconstruction, per-length score-priority decoding, future-heuristic priority, and earliest-length capacity eviction define distinguishable procedures. Parent/specialization relationships and shared words do not make them equivalent. None is lumped with a language-model task or global frontier-cap algorithm.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T061704Z-bounded-search-decoding.json | supports | No normalized match across all 442 AIO labels/scoped synonyms and 135 preceding native identities. Both checkouts were searched with ignored and hidden files included. The 67 shared text hits are previous source citations, frontier leads, scope contrasts and DCBSS substring matches in seven maintained paths; seven additional main-checkout hits are incidental substrings in public certificate data. No new identity duplicates an existing record. DCBS was a search candidate alias but was omitted from the final record because the two fully inspected defining papers do not establish that short form. |
| mapping | sources/aio/aio.json; Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing, GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning | supports | The three graph-search procedures use explicit no-match assessments after exact CLASS definitions, synonyms and incident edges were examined for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning. For the three sequence decoders, the exact NaturalLanguageProcessing CLASS and its is_a MachineLearningTask edge support an explicitly related algorithm-to-application-domain mapping grounded in the primary paper’s central NLP scope. No decoder-to-task subclass or trained-model identity is asserted. Semantic label/synonym scans covered search, beam, planning, heuristic, path, graph, sequence, structured and language terminology. |
| breadthfirstbranchandbound-0 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf; Sections 3–3.5, printed pp. 389–395 / PDF pp. 5–11; Figure 2 and the actual-incumbent versus hypothetical-bound distinction on printed pp. 393–394 | supports | A heuristic graph-search procedure that expands states in breadth-first layers and prunes candidate paths whose accumulated cost plus an admissible remaining-cost estimate exceeds a supplied solution-cost bound; the formulation curated here assumes uniform positive edge costs, scaled to one. Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected rendered PDF pages: 9, 10, 11, 12, 13, 22. |
| breadthfirstbranchandbound-1 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf; Sections 2.2–3.4, 6.1–6.2; printed pp. 387–392 and 405–406 / PDF pp. 3–8 and 21–22 | supports | The authors consider frontier, sparse-memory and layered duplicate handling, and relay-based path recovery. The potential reduction in stored search nodes is problem dependent; neither a fixed total-memory bound nor a universal advantage over A* follows. Nonuniform-cost extensions are outlined as future work. Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected rendered PDF pages: 9, 10, 11, 12, 13, 22. |
| breadthfirstidastar-0 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf; Section 4, printed p. 395 / PDF p. 11; Section 3.5 Figure 2, printed p. 394 / PDF p. 10 | supports | An iterative-deepening heuristic graph-search algorithm that repeatedly runs breadth-first branch-and-bound within increasing hypothetical f=g+h cost bounds, beginning at the start-state f value, until a solution is found; the curated formulation uses unit edge costs and a nonnegative admissible heuristic with h(goal)=0. Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected rendered PDF pages: 9, 10, 11, 12, 13, 22. |
| breadthfirstidastar-1 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf; Section 4.1 Theorems 4–5, Section 4.2, and Section 6.2; printed pp. 396–397 and 406 / PDF pp. 12–13 and 22 | supports | The expansion-count theorems depend on growth assumptions, while breadth-first traversal restricts beneficial tie-breaking within a contour. Memory remains governed by the retained search frontier and duplicate-detection strategy. Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected rendered PDF pages: 12, 13, 22. |
| divideconquerbeamsearch-0 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-icaps2004.pdf; Divide-and-Conquer Beam Search, PDF p. 6; Figure 3 and path reconstruction, PDF p. 5; experimental implementation description, PDF p. 8 | supports | A memory-limited breadth-first heuristic search that discards least-promising open nodes when its chosen capacity is reached and recovers a solution through relay-based divide-and-conquer reconstruction instead of retaining every predecessor layer. Version: ICAPS 2004 proceedings, 92–100; university-hosted proceedings PDF with unnumbered body pages. Actually inspected rendered PDF pages: 3, 4, 5, 6. |
| divideconquerbeamsearch-1 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf; Section 6.2, printed p. 406 / PDF p. 22 | supports | The later journal account identifies the same approximate procedure as layered BFBnB plus deletion of high-f open nodes at the memory limit, and distinguishes it from a subsequent complete backtracking extension. Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected rendered PDF pages: 22. |
| divideconquerbeamsearch-2 | https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-icaps2004.pdf; Divide-and-Conquer Beam Search vs. weighted A*, PDF p. 8 | supports | The planning experiments use the nonadmissible additive heuristic to guide approximate search while separately evaluating an admissible max-pair lower bound. A favorable experimental comparison does not convert the ranking function into an admissible cost bound. Version: ICAPS 2004 proceedings, 92–100; university-hosted proceedings PDF with unnumbered body pages. Actually inspected rendered PDF pages: 3, 4, 5, 6. |
| sequencebestfirstbeamsearch-0 | https://aclanthology.org/2020.tacl-1.51.pdf; Algorithm 2 and Table 1, printed pp. 797–798 / PDF pp. 3–4; Sections 3.2–4.1, printed pp. 798–801 / PDF pp. 4–7 | supports | The sequence-decoding beam procedure of Meister, Vieira and Cotterell that prioritizes active hypotheses by decreasing accumulated score, breaks score ties by shorter length, and limits accepted expansions to k hypotheses at each sequence length without a future-score heuristic. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| sequencebestfirstbeamsearch-1 | https://aclanthology.org/2020.tacl-1.51.pdf; Section 4.1, A Note on Heuristics, printed p. 801 / PDF p. 7 | supports | The paper explicitly limits its beam-output equivalence proof to the zero-heuristic case; an optimistic future-score heuristic can change which paths survive finite-beam pruning. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| sequencebestfirstbeamsearch-2 | https://aclanthology.org/2020.tacl-1.51.pdf; Sections 1–2, printed pp. 795–796 / PDF pp. 1–2 | supports | The method is defined for sequential structured prediction and developed in the paper around natural-language sequence transduction, including translation and abstractive summarization. The decoder is separate from the trained model that supplies scores. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| sequenceastarbeamsearch-0 | https://aclanthology.org/2020.tacl-1.51.pdf; Section 3, Algorithm 2 and Table 1; Definition 3.1; printed pp. 797–798 / PDF pp. 3–4 | supports | A sequence-decoding beam framework that ranks active hypotheses by accumulated score plus an optimistic future-score heuristic, uses shorter length to break score ties, and limits accepted expansions to k hypotheses per sequence length. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| sequenceastarbeamsearch-1 | https://aclanthology.org/2020.tacl-1.51.pdf; Section 4.1, A Note on Heuristics, printed p. 801 / PDF p. 7 | supports | With finite pruning, even an admissible future-score heuristic can alter which hypotheses survive compared with ordinary width-k beam search. The paper distinguishes the zero-heuristic equivalence result from this more general framework. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| memoryreducedsequencebeamsearch-0 | https://aclanthology.org/2020.tacl-1.51.pdf; Section 3.3, Memory-Reduced Best-First Beam Search, printed pp. 799–800 / PDF pp. 5–6 | supports | A capacity-limited variant of per-length best-first sequence beam search that, when its chosen total queue capacity is reached, removes the worst-scoring active hypothesis from the earliest active sequence length. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| memoryreducedsequencebeamsearch-1 | https://aclanthology.org/2020.tacl-1.51.pdf; Section 3.3 memory-reduced variant, printed pp. 799–800 / PDF pp. 5–6 | supports | The variant adds pruning to the base decoder by limiting queue capacity and targeting the earliest active time step for eviction. The paper presents it as a separate memory-reduced method, not as the unchanged monotone-beam equivalence construction. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| nonmonotone-analysis | research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json; Finite width-two tree, full traces and declared interpretation limits; companion script research/validation/20261011T061704Z-nonmonotone-beam-counterexample.py | supports | A curator-authored executable illustration returns score 10 under layer beam and -5 under per-length best-first search with exact remaining-completion bounds. The result concerns unchanged per-length pruning under nonmonotone scores. This is not execution of the authors implementation and does not refute the monotone method. |
| contested-source | https://arxiv.org/pdf/2007.03909v5; PDF p. 7, Non-monotonic Scoring Functions and Equation 6; compare published TACL printed p. 801 / PDF p. 7 | context_only | The later arXiv version repeats a stop-only route to a k-optimality guarantee for scores bounded above. This broader assertion is preserved as contested source context; the new record asserts only the supported monotone-score equivalence. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval; all six records remain DRAFT.
- The BFHS methods are scoped to uniform positive edge costs; no universal duplicate-elimination, runtime or memory theorem is asserted.
- NLP beam equivalence is limited to the stated monotone zero-heuristic setting with compatible tie, EOS and length conventions.
- The nonmonotone counterexample is a curator-authored finite-tree illustration, not an audit or execution of the author code.
- The published NLP source and later arXiv revision are distinguished. Primary sources and inspection scopes are preserved without redistributing the full papers.
- Repeated source identifiers refer to different passages, not independent studies.
- The short DCBS alias was omitted before record creation because the inspected defining papers did not establish it; no claim of absence throughout the literature is made.
- The first history invocation failed on uv cache access before writing; the corrected invocation used the intended worktree environment and succeeded.
- An unsaved draft used context instead of the review schema enum context_only; validation rejected it before saving, and the enum was corrected without changing the scientific assessment.
- All required checks passed. The saved review covers only these six targets and does not retire unrelated historical findings. Discovery remains ongoing.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T062030Z-bounded-search-decoding
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of bounded graph search and sequence decoding
started_at: '2026-10-11T06:20:30Z'
finished_at: '2026-10-11T06:20:30Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own six records
    and source assumptions. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All six maintained identities, mechanisms and explicit AIO assessments are
  supported in their stated scopes. No actionable record defect remains in this review.
  Source-level nonmonotonicity concerns, implementation limits and unresolved candidates
  are retained without promoting DRAFT status.
source:
  git_revision: 4a65f776d6b3b19b343f10a23a92d5256547d445
  state: working_tree
  inputs:
  - path: data/curated/BreadthFirstBranchAndBound.yaml
    sha256: f81b9d69d5cab18ce6584b1fc61be1e25a51b7a12ba3822628a8fe3793bcbfd0
    role: target
  - path: data/curated/BreadthFirstIDAStar.yaml
    sha256: 6a769cf81b4b128f652ba6b7340563a855a12e73f9a689e5f3d83d6baae0b20c
    role: target
  - path: data/curated/DivideConquerBeamSearch.yaml
    sha256: 29b97b304240e2e3f2ef2906d1f2d1dc3b25f91014ba1ebd0edd8e482f2e6d49
    role: target
  - path: data/curated/MemoryReducedSequenceBeamSearch.yaml
    sha256: 6b724b11873c4972672889f5f6c183f3375cd7f5aa96bd10afff9db88c13c23f
    role: target
  - path: data/curated/SequenceAStarBeamSearch.yaml
    sha256: 32c4f34dd1b9b21d6158b14cac860aa7a44053422e0a449de61f29cdfc315f9a
    role: target
  - path: data/curated/SequenceBestFirstBeamSearch.yaml
    sha256: 9bc305bdd3245324d1889389c19b356221021298a0b9d3cd3fdc62fb5f6ce0f0
    role: target
  - path: research/discovery/20261011T061704Z-bounded-search-decoding.json
    sha256: 9d8659cf3d2a6de90271acf589f306cdacfb5b889f582d096eb20a08c03e7b9a
    role: context
  - path: research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json
    sha256: e13977073ad03d0463ec43c8c174520eda51d3c8906ae44dffc955e072fdbfb3
    role: context
  - path: research/validation/20261011T061704Z-nonmonotone-beam-counterexample.py
    sha256: 1b2e073109814fc1a8fa0ce12b55553a5f6eee2400a9a085cac24f67fe0d665f
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
- target_id: AIMech:BreadthFirstBranchAndBound
  path: data/curated/BreadthFirstBranchAndBound.yaml
  label: Breadth-first branch-and-bound search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BreadthFirstBranchAndBound.yaml
    role: maintained_record
- target_id: AIMech:BreadthFirstIDAStar
  path: data/curated/BreadthFirstIDAStar.yaml
  label: Breadth-first iterative-deepening A-star
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BreadthFirstIDAStar.yaml
    role: maintained_record
- target_id: AIMech:DivideConquerBeamSearch
  path: data/curated/DivideConquerBeamSearch.yaml
  label: Divide-and-conquer beam search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DivideConquerBeamSearch.yaml
    role: maintained_record
- target_id: AIMech:SequenceBestFirstBeamSearch
  path: data/curated/SequenceBestFirstBeamSearch.yaml
  label: Best-first beam search with per-length budgets
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SequenceBestFirstBeamSearch.yaml
    role: maintained_record
- target_id: AIMech:SequenceAStarBeamSearch
  path: data/curated/SequenceAStarBeamSearch.yaml
  label: A-star beam search for sequence decoding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SequenceAStarBeamSearch.yaml
    role: maintained_record
- target_id: AIMech:MemoryReducedSequenceBeamSearch
  path: data/curated/MemoryReducedSequenceBeamSearch.yaml
  label: Memory-reduced best-first beam search for sequence decoding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MemoryReducedSequenceBeamSearch.yaml
    role: maintained_record
scope:
  description: Full review of three bounded graph-search procedures and three related
    sequence-decoding procedures.
  selection: Exactly the six IDs in the bounded-search-decoding discovery ledger;
    no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exclusions:
  - target: BSIDA-star, duplicate-detection methods and other pending frontiers
    reason: Their discriminating primary-method or identity checks remain recorded
      as follow-up work.
  - target: Numerical performance comparisons, formal proof certification and full
      author implementation audit
    reason: No model/benchmark execution was undertaken. The curator finite-tree illustration
      is explicitly limited to its recorded assumptions.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
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
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
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
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 141 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
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
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 29 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 29,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 58.67s\nChecked 442 record(s); 0 failed.\n\
    Checked 141 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 29 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 29,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: curator-illustration
  name: Finite-tree analysis
  command: python3 research/validation/20261011T061704Z-nonmonotone-beam-counterexample.py
  status: passed
  required: false
  target_ids:
  - AIMech:SequenceBestFirstBeamSearch
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual run and assertion completed: layer beam returns 10, per-length
    best-first with exact remaining bounds returns -5. Output saved in research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json.'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T061704Z-bounded-search-decoding.json
  accessed_at: '2026-10-11T06:20:30Z'
  support: supports
  summary: No normalized match across all 442 AIO labels/scoped synonyms and 135 preceding
    native identities. Both checkouts were searched with ignored and hidden files
    included. The 67 shared text hits are previous source citations, frontier leads,
    scope contrasts and DCBSS substring matches in seven maintained paths; seven additional
    main-checkout hits are incidental substrings in public certificate data. No new
    identity duplicates an existing record. DCBS was a search candidate alias but
    was omitted from the final record because the two fully inspected defining papers
    do not establish that short form.
  search_scope: All 442 AIO labels/scoped synonyms and 135 preceding native IDs/names/aliases;
    both updated checkouts with ignored and hidden files included.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing,
    GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction
    and ReinforcementLearning
  accessed_at: '2026-10-11T06:20:30Z'
  support: supports
  summary: The three graph-search procedures use explicit no-match assessments after
    exact CLASS definitions, synonyms and incident edges were examined for GraphLanguageModel,
    ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and
    ReinforcementLearning. For the three sequence decoders, the exact NaturalLanguageProcessing
    CLASS and its is_a MachineLearningTask edge support an explicitly related algorithm-to-application-domain
    mapping grounded in the primary paper’s central NLP scope. No decoder-to-task
    subclass or trained-model identity is asserted. Semantic label/synonym scans covered
    search, beam, planning, heuristic, path, graph, sequence, structured and language
    terminology.
- evidence_id: breadthfirstbranchandbound-0
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf
  locator: Sections 3–3.5, printed pp. 389–395 / PDF pp. 5–11; Figure 2 and the actual-incumbent
    versus hypothetical-bound distinction on printed pp. 393–394
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 9f094b2d1e98822236c3c0957703fc1adc47798db0754240f6fbc93887934a54
  support: supports
  summary: 'A heuristic graph-search procedure that expands states in breadth-first
    layers and prunes candidate paths whose accumulated cost plus an admissible remaining-cost
    estimate exceeds a supplied solution-cost bound; the formulation curated here
    assumes uniform positive edge costs, scaled to one. Version: Artificial Intelligence
    170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected
    rendered PDF pages: 9, 10, 11, 12, 13, 22.'
- evidence_id: breadthfirstbranchandbound-1
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf
  locator: Sections 2.2–3.4, 6.1–6.2; printed pp. 387–392 and 405–406 / PDF pp. 3–8
    and 21–22
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 9f094b2d1e98822236c3c0957703fc1adc47798db0754240f6fbc93887934a54
  support: supports
  summary: 'The authors consider frontier, sparse-memory and layered duplicate handling,
    and relay-based path recovery. The potential reduction in stored search nodes
    is problem dependent; neither a fixed total-memory bound nor a universal advantage
    over A* follows. Nonuniform-cost extensions are outlined as future work. Version:
    Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published
    PDF. Actually inspected rendered PDF pages: 9, 10, 11, 12, 13, 22.'
- evidence_id: breadthfirstidastar-0
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf
  locator: Section 4, printed p. 395 / PDF p. 11; Section 3.5 Figure 2, printed p.
    394 / PDF p. 10
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 9f094b2d1e98822236c3c0957703fc1adc47798db0754240f6fbc93887934a54
  support: supports
  summary: 'An iterative-deepening heuristic graph-search algorithm that repeatedly
    runs breadth-first branch-and-bound within increasing hypothetical f=g+h cost
    bounds, beginning at the start-state f value, until a solution is found; the curated
    formulation uses unit edge costs and a nonnegative admissible heuristic with h(goal)=0.
    Version: Artificial Intelligence 170(4–5), 385–408 (2006); university-hosted published
    PDF. Actually inspected rendered PDF pages: 9, 10, 11, 12, 13, 22.'
- evidence_id: breadthfirstidastar-1
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf
  locator: Section 4.1 Theorems 4–5, Section 4.2, and Section 6.2; printed pp. 396–397
    and 406 / PDF pp. 12–13 and 22
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 9f094b2d1e98822236c3c0957703fc1adc47798db0754240f6fbc93887934a54
  support: supports
  summary: 'The expansion-count theorems depend on growth assumptions, while breadth-first
    traversal restricts beneficial tie-breaking within a contour. Memory remains governed
    by the retained search frontier and duplicate-detection strategy. Version: Artificial
    Intelligence 170(4–5), 385–408 (2006); university-hosted published PDF. Actually
    inspected rendered PDF pages: 12, 13, 22.'
- evidence_id: divideconquerbeamsearch-0
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-icaps2004.pdf
  locator: Divide-and-Conquer Beam Search, PDF p. 6; Figure 3 and path reconstruction,
    PDF p. 5; experimental implementation description, PDF p. 8
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 3fd76738c1717a9faf11155add0cb5f2691c72af8ec84ada0bee8e4561ddf646
  support: supports
  summary: 'A memory-limited breadth-first heuristic search that discards least-promising
    open nodes when its chosen capacity is reached and recovers a solution through
    relay-based divide-and-conquer reconstruction instead of retaining every predecessor
    layer. Version: ICAPS 2004 proceedings, 92–100; university-hosted proceedings
    PDF with unnumbered body pages. Actually inspected rendered PDF pages: 3, 4, 5,
    6.'
- evidence_id: divideconquerbeamsearch-1
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-aij2006.pdf
  locator: Section 6.2, printed p. 406 / PDF p. 22
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 9f094b2d1e98822236c3c0957703fc1adc47798db0754240f6fbc93887934a54
  support: supports
  summary: 'The later journal account identifies the same approximate procedure as
    layered BFBnB plus deletion of high-f open nodes at the memory limit, and distinguishes
    it from a subsequent complete backtracking extension. Version: Artificial Intelligence
    170(4–5), 385–408 (2006); university-hosted published PDF. Actually inspected
    rendered PDF pages: 22.'
- evidence_id: divideconquerbeamsearch-2
  kind: primary_source
  reference: https://ai.dmi.unibas.ch/research/reading_group/zhou-hansen-icaps2004.pdf
  locator: Divide-and-Conquer Beam Search vs. weighted A*, PDF p. 8
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 3fd76738c1717a9faf11155add0cb5f2691c72af8ec84ada0bee8e4561ddf646
  support: supports
  summary: 'The planning experiments use the nonadmissible additive heuristic to guide
    approximate search while separately evaluating an admissible max-pair lower bound.
    A favorable experimental comparison does not convert the ranking function into
    an admissible cost bound. Version: ICAPS 2004 proceedings, 92–100; university-hosted
    proceedings PDF with unnumbered body pages. Actually inspected rendered PDF pages:
    3, 4, 5, 6.'
- evidence_id: sequencebestfirstbeamsearch-0
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Algorithm 2 and Table 1, printed pp. 797–798 / PDF pp. 3–4; Sections 3.2–4.1,
    printed pp. 798–801 / PDF pp. 4–7
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The sequence-decoding beam procedure of Meister, Vieira and Cotterell
    that prioritizes active hypotheses by decreasing accumulated score, breaks score
    ties by shorter length, and limits accepted expansions to k hypotheses at each
    sequence length without a future-score heuristic. Version: Transactions of the
    Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published
    PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: sequencebestfirstbeamsearch-1
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Section 4.1, A Note on Heuristics, printed p. 801 / PDF p. 7
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The paper explicitly limits its beam-output equivalence proof to the zero-heuristic
    case; an optimistic future-score heuristic can change which paths survive finite-beam
    pruning. Version: Transactions of the Association for Computational Linguistics
    8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF
    pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: sequencebestfirstbeamsearch-2
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Sections 1–2, printed pp. 795–796 / PDF pp. 1–2
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The method is defined for sequential structured prediction and developed
    in the paper around natural-language sequence transduction, including translation
    and abstractive summarization. The decoder is separate from the trained model
    that supplies scores. Version: Transactions of the Association for Computational
    Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected
    rendered PDF pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: sequenceastarbeamsearch-0
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Section 3, Algorithm 2 and Table 1; Definition 3.1; printed pp. 797–798
    / PDF pp. 3–4
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'A sequence-decoding beam framework that ranks active hypotheses by accumulated
    score plus an optimistic future-score heuristic, uses shorter length to break
    score ties, and limits accepted expansions to k hypotheses per sequence length.
    Version: Transactions of the Association for Computational Linguistics 8, 795–809
    (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3,
    4, 5, 6, 7, 8.'
- evidence_id: sequenceastarbeamsearch-1
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Section 4.1, A Note on Heuristics, printed p. 801 / PDF p. 7
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'With finite pruning, even an admissible future-score heuristic can alter
    which hypotheses survive compared with ordinary width-k beam search. The paper
    distinguishes the zero-heuristic equivalence result from this more general framework.
    Version: Transactions of the Association for Computational Linguistics 8, 795–809
    (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3,
    4, 5, 6, 7, 8.'
- evidence_id: memoryreducedsequencebeamsearch-0
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Section 3.3, Memory-Reduced Best-First Beam Search, printed pp. 799–800
    / PDF pp. 5–6
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'A capacity-limited variant of per-length best-first sequence beam search
    that, when its chosen total queue capacity is reached, removes the worst-scoring
    active hypothesis from the earliest active sequence length. Version: Transactions
    of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology
    published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: memoryreducedsequencebeamsearch-1
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Section 3.3 memory-reduced variant, printed pp. 799–800 / PDF pp. 5–6
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The variant adds pruning to the base decoder by limiting queue capacity
    and targeting the earliest active time step for eviction. The paper presents it
    as a separate memory-reduced method, not as the unchanged monotone-beam equivalence
    construction. Version: Transactions of the Association for Computational Linguistics
    8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF
    pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: nonmonotone-analysis
  kind: record_content
  reference: research/validation/20261011T061704Z-nonmonotone-beam-counterexample.json
  locator: Finite width-two tree, full traces and declared interpretation limits;
    companion script research/validation/20261011T061704Z-nonmonotone-beam-counterexample.py
  accessed_at: '2026-10-11T06:20:30Z'
  snapshot_sha256: e13977073ad03d0463ec43c8c174520eda51d3c8906ae44dffc955e072fdbfb3
  support: supports
  summary: A curator-authored executable illustration returns score 10 under layer
    beam and -5 under per-length best-first search with exact remaining-completion
    bounds. The result concerns unchanged per-length pruning under nonmonotone scores.
    This is not execution of the authors implementation and does not refute the monotone
    method.
- evidence_id: contested-source
  kind: primary_source
  reference: https://arxiv.org/pdf/2007.03909v5
  locator: PDF p. 7, Non-monotonic Scoring Functions and Equation 6; compare published
    TACL printed p. 801 / PDF p. 7
  accessed_at: '2026-10-11T06:07:08Z'
  snapshot_sha256: 590be6b9362b98a955dd49f01bd33d33eb0668cd7dde93e8466ae8cf11231023
  support: context_only
  summary: The later arXiv version repeats a stop-only route to a k-optimality guarantee
    for scores bounded above. This broader assertion is preserved as contested source
    context; the new record asserts only the supported monotone-score equivalence.
assessments:
- assessment_id: breadthfirstbranchandbound
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  evidence_ids:
  - identity
  - mapping
  - breadthfirstbranchandbound-0
  - breadthfirstbranchandbound-1
  summary: The BFBnB search strategy is distinguished from BFIDA*, which obtains bounds
    by repeated searches, and from width-pruned beam search. Breadth-first heuristic
    search names the broader family in Zhou and Hansen; that umbrella phrase is not
    asserted as an exact alias. Frontier, sparse-memory and layered duplicate-detection
    implementations are alternatives, not mandatory simultaneous components. No normalized
    identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive
    text hits in the main checkout were prior discovery leads, source citations, scope
    contrasts and DCBSS substring matches, plus seven public certificate-data substring
    matches, not existing concept records.
  details: The scope is uniform positive costs and an admissible heuristic. A valid
    upper bound must cover a real solution for a single-pass optimal-solution guarantee;
    an unsuccessful hypothetical contour does not establish that the original problem
    is unsolvable. The layered implementation needs enough previous-layer information
    for the graph structure; retaining one previous layer is not a universal duplicate-elimination
    rule for directed graphs. Memory-saving implementations can still run out of memory
    in a large frontier. The paper explicitly does not prove universally lower peak
    memory than best-first search. The f≥U option is valid for improving an actual
    incumbent, not for an inclusive hypothetical contour with no stored solution.
    Preserving the incumbent when no improvement exists is an explicit operational
    consequence of that distinction. The record does not certify the printed pseudocode
    for all base cases, graph-locality claims under every pruning policy, or nonuniform-cost
    extensions.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - breadthfirstbranchandbound-0
    - breadthfirstbranchandbound-1
  - name: aio-assessment
    value: explicit no-match
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: breadthfirstidastar
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:BreadthFirstIDAStar
  evidence_ids:
  - identity
  - mapping
  - breadthfirstidastar-0
  - breadthfirstidastar-1
  summary: BFIDA* changes the inner traversal of cost-contour iterative deepening
    to breadth-first branch-and-bound. It is distinct from depth-first IDA*, depth-limited
    iterative-deepening DFS, and a single BFBnB search with a supplied incumbent bound.
    The memory implementation can use frontier or layered duplicate handling. No normalized
    identity match was found across the 442 AIO and 135 prior native records; ignored-inclusive
    text hits in the main checkout were prior discovery leads, source citations, scope
    contrasts and DCBSS substring matches, plus seven public certificate-data substring
    matches, not existing concept records.
  details: The hypothetical threshold is inclusive. Reusing strict incumbent pruning
    at T=f(start) without a retained solution would be a different procedure. This
    method repeats breadth-first contours and retains frontier/duplicate information;
    it does not inherit the path-linear storage of depth-first IDA*. The asymptotic
    node-expansion analysis assumes exponential growth of distinct nodes per iteration;
    the directed-graph result additionally constrains solution depth relative to stored
    layers. It is not an unconditional wall-clock optimum. Large layers and tie contours
    can still be costly. Solvable finite-depth cases require sufficient memory; no
    universal termination guarantee on infinite unsolvable graphs is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - breadthfirstidastar-0
    - breadthfirstidastar-1
  - name: aio-assessment
    value: explicit no-match
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: divideconquerbeamsearch
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:DivideConquerBeamSearch
  evidence_ids:
  - identity
  - mapping
  - divideconquerbeamsearch-0
  - divideconquerbeamsearch-1
  - divideconquerbeamsearch-2
  summary: Divide-and-conquer beam search is the approximate search procedure introduced
    by Zhou and Hansen in 2004. It differs from divide-and-conquer beam-stack search,
    which adds systematic backtracking and replay under saved beam ranges. Relay reconstruction
    alone does not revisit every branch discarded by beam pruning. No normalized identity
    match was found across the 442 AIO and 135 prior native records; ignored-inclusive
    text hits in the main checkout were prior discovery leads, source citations, scope
    contrasts and DCBSS substring matches, plus seven public certificate-data substring
    matches, not existing concept records.
  details: Permanent width pruning can discard every solution path; ordinary DCBS
    is neither complete nor guaranteed optimal. The reported current, previous, next
    and relay layers count retained search-node layers, not all temporary successors,
    recursive reconstruction state or output storage. The original developed search
    setting has uniform edge costs. Its planning implementation uses an inadmissible
    additive heuristic for ranking and a separate admissible heuristic for lower bounds;
    ranking and safe cost pruning must not be conflated. Larger permitted beams and
    reconstruction improvements do not establish monotonic quality or a universal
    speed advantage.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - divideconquerbeamsearch-0
    - divideconquerbeamsearch-1
    - divideconquerbeamsearch-2
  - name: aio-assessment
    value: explicit no-match
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: sequencebestfirstbeamsearch
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:SequenceBestFirstBeamSearch
  evidence_ids:
  - identity
  - mapping
  - sequencebestfirstbeamsearch-0
  - sequencebestfirstbeamsearch-1
  - sequencebestfirstbeamsearch-2
  summary: This is the 2020 sequence-decoding meaning of best-first beam search. Its
    per-length budget is distinct from AIMech:GlobalFrontierBeamSearch, which caps
    the entire open list. The qualified name avoids treating those different pruning
    rules as exact synonyms. The h=0 procedure is a specialization of the paper’s
    A-star beam framework. No normalized identity match was found across the 442 AIO
    and 135 prior native records; ignored-inclusive text hits in the main checkout
    were prior discovery leads, source citations, scope contrasts and DCBSS substring
    matches, plus seven public certificate-data substring matches, not existing concept
    records.
  details: The finite beam is an approximation to exact sequence-model decoding; equality
    to a specified beam procedure is not global MAP optimality. Sequence length limits,
    EOS handling and compatible deterministic tie conventions are part of the comparison.
    Arbitrary implementations with different stopping or tie rules need not return
    identical hypotheses. Queue counts are counts of retained hypotheses, not total
    bytes including neural states, model parameters, backpointers and temporary successors.
    No numerical speedup or benchmark-quality claim is curated. The beam-equivalence
    claim is restricted to nonincreasing scores and h=0. The paper also asserts a
    nonmonotonic stop-only extension; this record does not adopt that guarantee because
    a saved curator finite-tree counterexample exposes a conflict with unchanged per-length
    pruning. The optimized queue-of-beams representation can retain hypotheses at
    several lengths. The per-length budget is not a global queue-capacity bound.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - sequencebestfirstbeamsearch-0
    - sequencebestfirstbeamsearch-1
    - sequencebestfirstbeamsearch-2
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: sequenceastarbeamsearch
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:SequenceAStarBeamSearch
  evidence_ids:
  - identity
  - mapping
  - sequenceastarbeamsearch-0
  - sequenceastarbeamsearch-1
  summary: This names the finite-beam A-star decoding framework in Meister, Vieira
    and Cotterell, not every algorithm informally called A-star beam search. The h=0
    specialization has its own per-length best-first record. A finite per-length budget
    distinguishes the framework from unpruned A* and from a whole-frontier capacity
    cap. No normalized identity match was found across the 442 AIO and 135 prior native
    records; ignored-inclusive text hits in the main checkout were prior discovery
    leads, source citations, scope contrasts and DCBSS substring matches, plus seven
    public certificate-data substring matches, not existing concept records.
  details: The finite beam is an approximation to exact sequence-model decoding; equality
    to a specified beam procedure is not global MAP optimality. Sequence length limits,
    EOS handling and compatible deterministic tie conventions are part of the comparison.
    Arbitrary implementations with different stopping or tie rules need not return
    identical hypotheses. Queue counts are counts of retained hypotheses, not total
    bytes including neural states, model parameters, backpointers and temporary successors.
    No numerical speedup or benchmark-quality claim is curated. Admissibility of h
    does not preserve the zero-heuristic beam’s output after finite pruning. This
    is explicitly acknowledged in Section 4.1. Unpruned A-star guarantees cannot be
    transferred to the finite-beam framework merely because its heuristic is admissible.
    No unrestricted nonmonotonic stopping theorem is asserted. Application to a particular
    score requires checking the direction and validity of its future-reward bound,
    terminal behavior and stopping policy.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - sequenceastarbeamsearch-0
    - sequenceastarbeamsearch-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: memoryreducedsequencebeamsearch
  area: evidence
  topic: Identity, pruning rules, conditional guarantees, memory scope and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:MemoryReducedSequenceBeamSearch
  evidence_ids:
  - identity
  - mapping
  - memoryreducedsequencebeamsearch-0
  - memoryreducedsequencebeamsearch-1
  summary: This is the memory-reduced variant in Meister, Vieira and Cotterell Section
    3.3. Its eviction first chooses the earliest active length, so it differs from
    globally removing the worst-ranked hypothesis. It also differs from the base per-length
    best-first procedure, which can retain hypotheses at several lengths without this
    extra capacity pruning. No normalized identity match was found across the 442
    AIO and 135 prior native records; ignored-inclusive text hits in the main checkout
    were prior discovery leads, source citations, scope contrasts and DCBSS substring
    matches, plus seven public certificate-data substring matches, not existing concept
    records.
  details: The finite beam is an approximation to exact sequence-model decoding; equality
    to a specified beam procedure is not global MAP optimality. Sequence length limits,
    EOS handling and compatible deterministic tie conventions are part of the comparison.
    Arbitrary implementations with different stopping or tie rules need not return
    identical hypotheses. Queue counts are counts of retained hypotheses, not total
    bytes including neural states, model parameters, backpointers and temporary successors.
    No numerical speedup or benchmark-quality claim is curated. Additional capacity
    eviction can remove paths retained by the unmodified beam procedure, so its same-output
    guarantee is not inherited. The memory/quality tradeoff is empirical and problem
    dependent. The queue cap does not bound the entire decoder or neural model memory.
    The earliest-length eviction is not a global worst-score eviction rule. No guarantee
    for arbitrary nonmonotonic scores or globally optimal sequence decoding is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - memoryreducedsequencebeamsearch-0
    - memoryreducedsequencebeamsearch-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: adversarial-guarantees
  area: scope
  topic: Attempts to transfer guarantees across different pruning rules
  outcome: supported
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  evidence_ids:
  - breadthfirstbranchandbound-0
  - breadthfirstidastar-1
  - divideconquerbeamsearch-1
  - sequencebestfirstbeamsearch-1
  - sequenceastarbeamsearch-1
  - memoryreducedsequencebeamsearch-0
  - nonmonotone-analysis
  - contested-source
  summary: 'The records preserve the distinctions that defeat unconditional guarantee
    claims: actual versus hypothetical cost bounds, width pruning versus complete
    backtracking, per-length versus whole-frontier limits, heuristic changes to beam
    membership, and extra queue eviction.'
  details: BFIDA-star explicitly uses a nonnegative admissible heuristic with h(goal)=0
    in its unit-cost scope. No nonuniform-cost theorem, universal peak-memory improvement,
    unconditional wall-clock optimum or global-MAP claim is asserted. Source inconsistencies
    and unresolved implementation assumptions remain explicit limitations.
- assessment_id: curator-counterexample
  area: evidence
  topic: Scope and provenance of the nonmonotone illustration
  outcome: supported
  target_ids:
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  evidence_ids:
  - nonmonotone-analysis
  - contested-source
  - sequencebestfirstbeamsearch-0
  summary: The finite-tree calculation supports withholding the broad stop-only equivalence
    claim under the stated interpretation, while leaving the monotone decoder record
    intact.
  details: All completions have depth three and the discrepancy is not tie-dependent.
    The illustration omits optional older-layer deletion, stores completed incumbents
    rather than repeated EOS padding, and uses an exact descendant bound. It is a
    scoped curator analysis, not an author erratum, benchmark replication, general
    proof checker or implementation audit.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:BreadthFirstBranchAndBound
  - AIMech:BreadthFirstIDAStar
  - AIMech:DivideConquerBeamSearch
  - AIMech:SequenceBestFirstBeamSearch
  - AIMech:SequenceAStarBeamSearch
  - AIMech:MemoryReducedSequenceBeamSearch
  evidence_ids:
  - identity
  - mapping
  - breadthfirstbranchandbound-0
  - breadthfirstbranchandbound-1
  - breadthfirstidastar-0
  - breadthfirstidastar-1
  - divideconquerbeamsearch-0
  - divideconquerbeamsearch-1
  - divideconquerbeamsearch-2
  - sequencebestfirstbeamsearch-0
  - sequencebestfirstbeamsearch-1
  - sequencebestfirstbeamsearch-2
  - sequenceastarbeamsearch-0
  - sequenceastarbeamsearch-1
  - memoryreducedsequencebeamsearch-0
  - memoryreducedsequencebeamsearch-1
  - nonmonotone-analysis
  - contested-source
  rationale: A supplied cost bound, repeated cost contours, approximate width pruning
    with relay reconstruction, per-length score-priority decoding, future-heuristic
    priority, and earliest-length capacity eviction define distinguishable procedures.
    Parent/specialization relationships and shared words do not make them equivalent.
    None is lumped with a language-model task or global frontier-cap algorithm.
limitations:
- Adversarial author self-review, not independent approval; all six records remain
  DRAFT.
- The BFHS methods are scoped to uniform positive edge costs; no universal duplicate-elimination,
  runtime or memory theorem is asserted.
- NLP beam equivalence is limited to the stated monotone zero-heuristic setting with
  compatible tie, EOS and length conventions.
- The nonmonotone counterexample is a curator-authored finite-tree illustration, not
  an audit or execution of the author code.
- The published NLP source and later arXiv revision are distinguished. Primary sources
  and inspection scopes are preserved without redistributing the full papers.
- Repeated source identifiers refer to different passages, not independent studies.
- The short DCBS alias was omitted before record creation because the inspected defining
  papers did not establish it; no claim of absence throughout the literature is made.
- The first history invocation failed on uv cache access before writing; the corrected
  invocation used the intended worktree environment and succeeded.
- An unsaved draft used context instead of the review schema enum context_only; validation
  rejected it before saving, and the enum was corrected without changing the scientific
  assessment.
- All required checks passed. The saved review covers only these six targets and does
  not retire unrelated historical findings. Discovery remains ongoing.
tags:
- native-concepts
- bounded-search
- sequence-decoding
- primary-papers
- self-review
- discovery-ongoing
```
