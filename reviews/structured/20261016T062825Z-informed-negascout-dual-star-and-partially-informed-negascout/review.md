# Scientific self-review of informed NegaScout, DUAL* and partially informed NegaScout

- Review: 20261016T062825Z-informed-negascout-dual-star-and-partially-informed-negascout
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-16T06:26:30.228559Z
- Finished UTC: 2026-10-16T06:28:25.096279Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain informed NegaScout, DUAL* and partially informed NegaScout as three source-scoped DRAFT algorithms. Sixteen claims and 28 limitations preserve their information-retention, game-tree control and source-interface boundaries. Three declared rows identify two defining primary works. One approved INS limitation updates separately completed 1985 access attribution; version and other source questions remain separately tracked.

## Scope And Provenance

Three exact current native records from accepted cohort362 creation; all selected claims and limitations assessed. Historical source and neighbor readings remain separately attributed.

Selection: Exact AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:InformedNegaScout | data/curated/InformedNegaScout.yaml | maintained | Informed NegaScout |
| AIMech:DUALStar | data/curated/DUALStar.yaml | maintained | DUAL* |
| AIMech:PartiallyInformedNegaScout | data/curated/PartiallyInformedNegaScout.yaml | maintained | Partially Informed NegaScout |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |
| just vendored-check | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |
| uv run --locked aimech check-source | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |
| just render | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |
| just render-check | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |
| git diff --check | passed | True | AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout | Actual completed command exited0; exact output and timing retained. |

## Scientific And Domain Assessments

### Informed NegaScout: adjacent-window-probes

evidence: supported. Targets: AIMech:InformedNegaScout.

This combines the Section2 explanation with the actual Figure3 guards, including the remembered-PROVEBEST branch. It does not claim every non-cutoff failed-high probe is re-searched or that all returned merits are exact values.

In the displayed integer-score INS procedure, the first successor uses the incoming open window and later initial-search successors use an adjacent-value minimal window around the current bound. A failed-high probe may require an opened-window re-search; the displayed first-successor, fail-low, beta-cutoff, depth-at-most-two and remembered PROVEBEST cases determine when that additional search is avoided.

### Informed NegaScout: ignore-left-information

evidence: supported. Targets: AIMech:InformedNegaScout.

The relative depth is measured from the root of the re-search, not an absolute universal MIN/MAX parity. The text describes the inferior left region and the extreme-merit transformation; no modern implementation equivalence is inferred.

INS retains the path information identifying the leftmost terminal variation responsible for the initial failure. During a later re-search, previously examined inferior siblings to the left of that variation at even relative levels can be skipped. The source presents ignore-left pruning as a special case of prove-best pruning using remembered extreme merits and successor ordering.

### Informed NegaScout: prove-best-upper-bounds

evidence: supported. Targets: AIMech:InformedNegaScout.

The source stores upper bounds and explicitly tests max(a,alpha), not a alone. For the hand values a=2, alpha=5 and next upper bound4, the test succeeds and the displayed update returns4, which is still below alpha and can be only a fail-low bound. This clarifies the incoming-threshold case without executing INS, asserting all values exact, repairing helpers or certifying the complete algorithm.

At odd levels relative to a re-search root, INS retains successor upper bounds from the initial traversal. It uses them to order successors, stop when the larger of the current result a and incoming alpha reaches the next remaining upper bound, and narrow later search windows. Figure3 tests max(a,alpha)&gt;=merit[i+1] and then sets a=max(a,merit[i+1]); the returned result can remain only a fail-low bound. The negamax score orientation and validity of the retained bounds are part of this source-scoped interpretation.

### Informed NegaScout: recursive-information-storage

evidence: supported. Targets: AIMech:InformedNegaScout.

The paragraph explicitly distinguishes the information types and the experiments’ linked storage from the optional hash representation. It does not supply the missing merit-population or cache contract, and does not establish a fixed total-memory guarantee.

The complete-information INS presentation saves information recursively throughout the initial search subtree: the relevant successor index at ignore-left nodes and returned successor merits at prove-best nodes. SaveInfo and GetInfo hide its storage management. The reported experiments use a linked tree retaining all this information; the paper separately describes a hash-table option that can lose information through conflicts.

### Informed NegaScout: research-flag-and-unvisited-region

evidence: supported. Targets: AIMech:InformedNegaScout.

The two flag variables have visibly different roles. This states the printed control flow without silently adding assignments to the merit array or claiming executable C semantics.

Figure3 distinguishes the invocation’s research flag from a mutable resflag. A re-search invocation retrieves and sorts remembered successor information; when the procedure moves beyond remembered ignore-left information, resflag becomes false for subsequent recursive calls. The displayed SaveInfo call is guarded by research being false, and the procedure returns its current score or bound.

### Informed NegaScout: reported-comparison-design

evidence: supported. Targets: AIMech:InformedNegaScout.

The claim records the experiment’s design and metric only. The authors note sampling variability and the ranking depends on depth parity, ordering and width; no plot ordinate or broad superiority is newly asserted.

The journal compares INS with NS, PNS, SSS* and DUAL* on generated uniform-width, fixed-depth trees with random or specified sibling ordering. The plotted terminal-visit counts are percentages of a minimal game-tree size, averaged over the same twenty sample trees for each displayed setting; they are not wall-clock measurements or universal node-dominance guarantees.

### Informed NegaScout: finite-tree-scope

scope: supported. Targets: AIMech:InformedNegaScout.

Restricts the record to the described abstraction; it does not infer that all possible extensions are impossible.

The source-scoped procedure and experiments concern finite, fixed-depth alternating game trees, with uniform positive branching in the displays. No general cyclic-graph duplicate policy, stochastic-game semantics, quiescence treatment or arbitrary early-terminal interface is established.

### Informed NegaScout: integer-window-and-bounds

scope: supported. Targets: AIMech:InformedNegaScout.

The source’s int declarations and a+1 window supply the discrete scope; the fail-low/high explanation supplies the bound distinction.

The adjacent-value window uses integer score units. A failed-window return may be a bound rather than an exact minimax value; arbitrary real-valued epsilon rules, floating-point tolerances and terminal scoring conventions are not specified.

### Informed NegaScout: hidden-storage-contract

scope: supported. Targets: AIMech:InformedNegaScout.

Preserves the documented abstraction and visible omission. No implementation fix or failure is asserted from an abbreviated pseudocode display.

Figure3 delegates storage to SaveInfo/GetInfo and does not visibly populate merit with each returned v during the initial loop. Array initialization, value capture, cache misses, validity and lifetime therefore remain source-presentation questions rather than a complete executable contract or a proved algorithm defect.

### Informed NegaScout: last-successor-interface

scope: supported. Targets: AIMech:InformedNegaScout.

The scientific-draft author’s earlier visual reading confirms both the array access and the nearby last-successor comment; exact implementation completion remains a follow-up.

The displayed pseudocode uses one-based successor indices and reads merit[i+1]. Excluding the i==w case is stated in a comment rather than encoded in that Boolean guard. The listing is not directly executable C and must not be silently repaired.

### Informed NegaScout: storage-budget-boundary

scope: supported. Targets: AIMech:InformedNegaScout.

The source explicitly separates all-information linked storage from a tunable hash option. The limit avoids converting that option into the fixed-memory guarantees of different algorithms.

A finite hash table can lose remembered information and potential cutoffs; the reported full-information experiment instead retains the generated subtree. Neither establishes a hard total byte bound including the recursion stack, successor arrays, cache policy and allocator overhead.

### Informed NegaScout: empirical-external-validity

scope: supported. Targets: AIMech:InformedNegaScout.

The source gives contrasting odd/even behavior and notes finite-sample uncertainty; the draft does not claim a reproduced benchmark.

Terminal-count curves are conditional on the supplied tree generator, width, depth parity, ordering and twenty shared samples. The paper discusses sampling variability; these results do not prove universal dominance over SSS*, DUAL*, NS, PNS or alpha-beta.

### Informed NegaScout: timing-portability

scope: supported. Targets: AIMech:InformedNegaScout.

Keeps cost metrics separate and leaves the technical-report version question open.

Preliminary execution-time and OPEN-management observations describe the authors’ implementations, with details deferred to report12. They are not reproduced results, hardware-independent speedups or evidence that fewer terminal visits always means lower time.

### Informed NegaScout: neighbor-and-version-identity

scope: supported. Targets: AIMech:InformedNegaScout.

Preserves the source-specific INS/PNS and PVS lineage boundaries while distinguishing the separately completed 1985 source reading from unresolved version and other cited-lineage questions.

The paper’s PNS stores relevant upper bounds only at the first level, and its footnote discusses NegaScout/PVS lineage. Those descriptions do not by themselves establish PNS as this full INS procedure, global PVS aliases, or equivalence to all later implementations. The 1985 original has been read separately; its version differences and the other cited lineage questions remain separately tracked.

### Informed NegaScout: artifact-version-scope

scope: supported. Targets: AIMech:InformedNegaScout.

This is a provenance limitation supported by the original acquisition/reading ledger in addition to the cited journal pages. The secondary rendering stays research context, not an unused native source row. The journal locator contextualizes the procedure/publication only; the added provenance refs directly support the present reading/version/assurance boundary. No claim that the journal reports this curator’s access history is made.

The defining evidence is the inspected15-page author-hosted1987 journal reproduction. The separate18-page author rendering was inspected only in selected regions, and the TR85-16 route has a cover/title/page-count discrepancy; neither is treated as a wholly equivalent publisher artifact or a fully read independent defining source.

### Informed NegaScout: no-implementation-proof

scope: supported. Targets: AIMech:InformedNegaScout.

An explicit curator assurance boundary, not a claim that the paper or algorithm is false. The journal locator contextualizes the procedure/publication only; the added provenance refs directly support the present reading/version/assurance boundary. No claim that the journal reports this curator’s access history is made.

The draft records the described pruning and recursion mechanism while retaining the abbreviated helper and guard conventions. It does not certify a full correctness or node-dominance theorem, execute INS, or import uninspected proofs from SSS*, NegaScout or alpha-beta references.

### Informed NegaScout: defining procedure

evidence: supported. Targets: AIMech:InformedNegaScout.

Source-specific procedure definition, limited to the inspected journal account. It does not allocate an ontology identity, mapping or alias, certify executable pseudocode, or assert a universal performance theorem.

An adversarial game-tree search procedure that augments NegaScout’s minimal-window traversal with recursively retained information from an initial search, using remembered inferior left regions and successor upper bounds to guide a later re-search.

### Informed NegaScout: kind

scope: supported. Targets: AIMech:InformedNegaScout.

INS denotes the selected recursive adversarial game-tree search procedure. Minimal-window probes and retained information guide re-search; it is an algorithm, not a trained model, task, benchmark or hard-memory-budget method.

The accepted algorithm kind is retained. Integer score units, finite alternating-tree abstraction and missing helper contracts limit implementation and theorem claims.

### Informed NegaScout: identity

identity: supported. Targets: AIMech:InformedNegaScout.

Retain the full name Informed NegaScout and empty global aliases for the source-specific 1987 complete-information procedure. Bare INS is source-local; baseline NegaScout, PNS, Principal Variation Search and later implementations are not asserted exact aliases.

The accepted historical inventory/search assessment is reused with its stated scope. It is not rerun here and cannot establish current noncollision, novelty, owner responsibility or a future base. Previously accepted identity notes (verbatim historical wording): This proposal selects the1987 recursively informed NegaScout procedure: retained ignore-left regions and successor upper bounds influence later re-search. It does not collapse PNS, baseline NegaScout, Principal Variation Search, generic alpha-beta or all later INS implementations. The1985 official paper is an additional version question under separate review. Bare INS is source-local and omitted from global aliases. At the historical04:51–04:52UTC branch360 snapshot, all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive roots supplied749 distinct matching contents. The reading covers747 full contents plus all matching leaves in two large wrappers. This is prospective historical evidence, not future current-state clearance.

### Informed NegaScout: mapping

grounding: supported. Targets: AIMech:InformedNegaScout.

Retain the accepted bounded aio_no_match and all thirty rejection reasons. Computed minimax bounds, recursive calls, optional hashing and game-tree structure do not establish a learning task, neural architecture, language model, classifier or neural layer.

The pinned definitions, synonyms and incident edges belong to the accepted prior mapping assessment. No positive exact, broader, narrower or specifically related target was selected; this fragment does not claim ontology-wide impossibility or a fresh 442-class semantic read. Previously accepted search scope (verbatim historical wording): Historical prospective snapshot on 2026-10-16 at 04:51–04:52 UTC, branch goal/discover-ai-concepts-round360, HEAD 3cd85f801666b505b906cedab979423e4f305c40. Compared all 801 maintained and 442 pinned AIO identities (1,243 records; 4,927 identity-field occurrences; 3,766 normalized values). Four fixed-string, case-insensitive, word-delimited searches included ignored and hidden files and excluded .git internals: 10,522 occurrences in 749 distinct contents. Fresh semantic reading covers 747 complete contents and all matching leaves in two large historical wrappers; unrelated wrapper fields were not reread. Read all 30 full candidate AIO nodes and 97 incident triples plus 20 maintained native definitions, identity fields, claim statements and limitations. This historical scope does not clear any future base or assign a source owner.

### Informed NegaScout: source

provenance: supported. Targets: AIMech:InformedNegaScout.

Both candidate records use the same fifteen-page author-hosted 1987 journal reproduction as their sole declared defining artifact. For INS, the positive mechanism locators are the minimal-window discussion, ignore-left/prove-best explanation and Figure3, with the exact max(a,alpha) guard and potentially fail-low returned bound.

The source row, DOI, URL, hash, publication/version qualification and historical access time remain exact. Partially inspected alternate rendering, TR85-16 and earlier1985 INS/PNS evidence remain separately attributed version questions. Later PNS research does not rewrite the historical objects or supply a full1987 helper contract.

### Informed NegaScout: boundary

scope: supported. Targets: AIMech:InformedNegaScout.

Retain full-information INS as distinct from the partial PNS policy and the LIVE/SOLVED DUAL* controller. Preserve the source-relative odd/even levels, research/resflag distinction, max(a,alpha) threshold and returned-bound qualification; do not silently complete merit storage or last-successor guards.

Six claims and ten limitations are copied from the accepted preview. Generated-tree terminal-count comparisons remain separate from implementation timing; no universal dominance, executable correctness, hard byte limit or uninspected predecessor theorem is certified.

### DUAL*: max-rooted-dual-scheduling

evidence: supported. Targets: AIMech:DUALStar.

The MAX-rooted use is the source-specific directional choice, not a global claim that DUAL* is identical to SSS* or every routine called dual-ss*. The increasing-merit statement concerns ordered insertion; push/pop remain distinct operations.

The paper constructs DUAL* from the dual of SSS* by interchanging MAX and MIN behavior, replacing the minimum operation with a maximum, and changing ordered insertion to increasing merit. It deliberately applies this dual procedure to a MAX-rooted tree, producing a left-to-right traversal of root successors while using the dual search within their subtrees.

### DUAL*: descriptor-and-list-operations

evidence: supported. Targets: AIMech:DUALStar.

This is a source description of the descriptor and helper conventions, not an independent invariant proof that every intermediate OPEN arrangement is globally sorted. Equal-merit placement is expressly retained.

The displayed DUAL* descriptor contains a node, LIVE or SOLVED status, and merit h. The initial root descriptor is LIVE with a negative-infinity bound. The paper distinguishes push/pop from insert; insert places a descriptor in increasing merit order behind entries with equal merit.

### DUAL*: live-node-processing

evidence: supported. Targets: AIMech:DUALStar.

The claim labels its interpretation rather than repairing the display silently. The leaf test is printed separately from MAX/MIN tests, so executable behavior requires a precise node-type convention.

Under the intended terminal-versus-interior interpretation of Figure4, a LIVE leaf becomes SOLVED with merit max(Evaluate(node),h); a LIVE interior MAX node pushes its first child; and a LIVE interior MIN node pushes all children in reverse order. The printed separate leaf/MAX/MIN predicates require the source-interface qualification retained in the limitations.

### DUAL*: solved-node-processing

evidence: supported. Targets: AIMech:DUALStar.

The root guard precedes parent use in the display. The purge target is stated as the paper’s stored-successor operation; its exact transitive descendant/list implementation is not supplied or generalized to shared graphs.

For a SOLVED descriptor, Figure4 returns h if the node is the root. Otherwise, a solved MAX node purges the parent’s stored successors and pushes the parent as SOLVED; a solved MIN node pushes the next unexamined sibling as LIVE if one remains, or otherwise pushes the parent as SOLVED.

### DUAL*: source-stated-space-scope

evidence: supported. Targets: AIMech:DUALStar.

This is the source’s storage characterization for the studied tree algorithms, not a newly derived exact closed form or a bound on allocator/runtime bytes. A short OPEN list in some examples does not imply linear space.

The journal describes complete-information SSS*, DUAL* and INS storage requirements as exponential with search depth, despite their differing descriptors and retained frontier sizes. DUAL* is not presented as a user-specified hard byte-budget search procedure.

### DUAL*: reported-comparison-design

evidence: supported. Targets: AIMech:DUALStar.

The source separates terminal visits from timing and refers detailed overheads to report12. This claim preserves the comparison design and limits without converting implementation-specific ratios into portable speedups.

DUAL* is evaluated with the other search algorithms on the same generated trees of specified width, depth and sibling ordering. Figures5–7 report normalized terminal-node visits averaged over twenty shared samples; odd/even depth and ordering can change relative rankings. Separate preliminary timing observations concern the authors’ implementations and OPEN-list overhead.

### DUAL*: finite-tree-scope

scope: supported. Targets: AIMech:DUALStar.

Keeps the source abstraction and root choice explicit instead of generalizing to every search problem.

The selected DUAL* is the paper’s MAX-rooted use on finite, fixed-depth alternating game trees. The displays assume positive uniform branching for interior nodes; cyclic/shared graphs, stochastic games and arbitrary early-terminal conventions are not supplied.

### DUAL*: leaf-and-parity-interface

scope: supported. Targets: AIMech:DUALStar.

The scientific-draft author’s earlier visual reading confirms the independent conditionals. The supported record states an interpretation with this qualification, not a silently amended program.

Figure4 prints independent LIVE tests for LEAFNODE, MAXNODE and MINNODE, while SOLVED processing uses the game-node type. The intended distinction between terminal and interior predicates, retained parity and terminal transitions must be specified before executable verification; the abbreviation alone does not prove a defect.

### DUAL*: purge-and-list-interface

scope: supported. Targets: AIMech:DUALStar.

The insert equal-merit convention is known, but a complete graph/list implementation contract is not. No descendant implementation is manufactured.

Purge is described as deleting stored successors from OPEN. Its exact transitive descendant selection, tie behavior in all operations, node identity and list-maintenance semantics remain helper-contract questions; arbitrary graph sharing or cycles are not justified by that description.

### DUAL*: exhaustion-and-termination-interface

scope: supported. Targets: AIMech:DUALStar.

Distinguishes the visible success return from unspecified exceptional interfaces without claiming a valid finite game tree necessarily encounters them.

The displayed control loop is unconditional and terminates on a SOLVED root. Empty-OPEN failure, malformed node types and invalid child/sibling data are not given separate semantics; no execution-level termination or failure theorem is certified from the pseudocode.

### DUAL*: memory-boundary

scope: supported. Targets: AIMech:DUALStar.

The word low overhead and a smaller frontier in some cases do not establish an asymptotically linear or externally bounded memory guarantee.

The source describes complete-information storage as exponential with depth. It supplies no user-enforced byte budget, eviction scheme or total-runtime memory bound; this DUAL* must not be relabeled as a fixed-budget search method.

### DUAL*: empirical-external-validity

scope: supported. Targets: AIMech:DUALStar.

Retains the metric and design; source-stated selected performance is not extrapolated to all games or implementations.

The normalized terminal-count comparisons use specified generated tree families and twenty shared samples, with ranking changes across depth parity and ordering. They are not universal node-count dominance, proof of optimal search ordering or a reproduced game-playing result.

### DUAL*: timing-portability

scope: supported. Targets: AIMech:DUALStar.

No external benchmark was run. The unresolved technical-report version remains explicit.

The preliminary timing ratios and OPEN-list profiles are implementation-specific, and the detailed overhead analysis is deferred to report12. They do not establish hardware-independent slowdowns or speedups, nor convert terminal visits into elapsed time.

### DUAL*: dual-ss-and-sss-lineage

scope: supported. Targets: AIMech:DUALStar.

Original parallel and SSS* sources remain distinct pending questions; the current claim is source-specific rooted scheduling.

The journal compares DUAL* to SSS* and mentions Kumar–Kanal’s parallel dual-ss* routine. Its suggestion that one-process measurements could fill a missing comparison does not establish global aliases or complete equivalence to that parallel formulation.

### DUAL*: artifact-version-scope

scope: supported. Targets: AIMech:DUALStar.

The rendering and report metadata are retained in research provenance rather than being promoted to uninspected positive claim sources. The journal locator contextualizes the procedure/publication only; the added provenance refs directly support the present reading/version/assurance boundary. No claim that the journal reports this curator’s access history is made.

The selected defining artifact is the inspected1987 author-hosted journal reproduction. Only selected regions of the separate author rendering and the TR85-16 cover route were inspected; no whole-text or method equivalence, publisher-byte identity or independent replication is claimed.

### DUAL*: proof-and-cost-model-boundary

scope: supported. Targets: AIMech:DUALStar.

An explicit boundary on the present author’s assurance. The separately bound independent review assesses source control flow; it does not certify a complete implementation. The journal locator contextualizes the procedure/publication only; the added provenance refs directly support the present reading/version/assurance boundary. No claim that the journal reports this curator’s access history is made.

The draft preserves the source’s descriptor updates, MAX-root choice and measured comparison scope. It does not certify the full minimax invariant, exact computational cost, implementation correctness or theorem claims from uninspected predecessor references.

### DUAL*: defining procedure

evidence: supported. Targets: AIMech:DUALStar.

Source-specific procedure definition, limited to the inspected journal account. It does not allocate an ontology identity, mapping or alias, certify executable pseudocode, or assert a universal performance theorem.

The source’s MAX-rooted application of the dual of SSS*, using LIVE/SOLVED node descriptors, maximum-based merit updates and dual MAX/MIN expansion rules to search root successors from left to right.

### DUAL*: kind

scope: supported. Targets: AIMech:DUALStar.

DUAL* denotes the selected MAX-rooted descriptor-based game-tree search procedure. LIVE/SOLVED state, dual MAX/MIN transitions and explicit list operations are algorithmic control, rather than a trained model, learning task or generic mathematical duality.

The accepted algorithm kind is retained. Source-specific root choice, finite-tree assumptions and helper interfaces limit the interpretation; the title low overhead does not establish linear memory or a hard user byte budget.

### DUAL*: identity

identity: supported. Targets: AIMech:DUALStar.

Retain the literal name DUAL* and empty global aliases for the 1987 MAX-rooted use of the dual of SSS*. It remains distinct from INS, SSS*, mathematical duality, Hamiltonian dual averaging and the uninspected parallel dual-ss* lineage.

Bare DUAL is not added as an alias. Historical normalized inventory and source-specific comparisons are attributed to the accepted preparation, without fresh current noncollision or owner allocation. Previously accepted identity notes (verbatim historical wording): This proposal selects the1987 MAX-rooted dual-of-SSS* procedure with LIVE/SOLVED descriptors, maximum merit, increasing OPEN order and dual MAX/MIN transitions. It is distinct from INS, SSS*, generic mathematical duality and Hamiltonian dual averaging. The earlier parallel dual-ss* citation is lineage to inspect, not an exact alias. Bare DUAL is omitted; the literal name keeps its star. At the historical04:51–04:52UTC branch360 snapshot, all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive roots supplied749 distinct matching contents. The reading covers747 full contents plus all matching leaves in two large wrappers. This is prospective historical evidence, not future current-state clearance.

### DUAL*: mapping

grounding: supported. Targets: AIMech:DUALStar.

Retain the accepted bounded aio_no_match and all thirty rejection reasons. Alternating-player search, MAX/MIN scalar operations, stored descriptors and adversarial terminology do not establish learned models, GAN training, neural maximum/minimum layers, classification or reinforcement learning.

The selected pinned-AIO context is inherited from its accepted prior reading. No positive target relation is asserted, and neither shared tree shape nor generic memory supplies one. This is a bounded assessment, not an all-ontology semantic absence claim. Previously accepted search scope (verbatim historical wording): Historical prospective snapshot on 2026-10-16 at 04:51–04:52 UTC, branch goal/discover-ai-concepts-round360, HEAD 3cd85f801666b505b906cedab979423e4f305c40. Compared all 801 maintained and 442 pinned AIO identities (1,243 records; 4,927 identity-field occurrences; 3,766 normalized values). Four fixed-string, case-insensitive, word-delimited searches included ignored and hidden files and excluded .git internals: 10,522 occurrences in 749 distinct contents. Fresh semantic reading covers 747 complete contents and all matching leaves in two large historical wrappers; unrelated wrapper fields were not reread. Read all 30 full candidate AIO nodes and 97 incident triples plus 20 maintained native definitions, identity fields, claim statements and limitations. This historical scope does not clear any future base or assign a source owner.

### DUAL*: source

provenance: supported. Targets: AIMech:DUALStar.

The defining source for DUAL* is the same exact fifteen-page 1987 journal reproduction used by INS. Section3 and Figure4 support the MAX-rooted choice, LIVE/SOLVED processing and separate push/pop versus ordered insert conventions; the later experimental section supplies the qualified comparison design.

Two record-level source rows represent one artifact and one work. Publisher-byte identity, disputed issue number, full alternate-rendering equivalence and independently reproduced performance are not asserted. The sixteen bibliography objects, nine questions and two incidental retrieval objects remain exact and separately queryable.

### DUAL*: boundary

scope: supported. Targets: AIMech:DUALStar.

Retain the source-specific MAX-rooted DUAL* controller, including maximum-based merits and increasing-merit insertion behind ties. Keep intended terminal/interior interpretation, root-before-parent success handling and purge/list/empty-OPEN boundaries explicit.

Six accepted claims and ten limitations remain unchanged. No global SSS*/parallel-dual alias, complete minimax invariant, graph-sharing extension, hard byte-budget property, portable speedup or implementation certification is inferred.

### Partially Informed NegaScout: near-root-prove-best-retention

evidence: supported. Targets: AIMech:PartiallyInformedNegaScout.

The explicit PNS sentence selects near-root prove-best information. The immediately preceding explanation identifies prove-best data as upper bounds after all descendants have been examined without a beta cutoff. The draft keeps this narrow link and does not turn the source’s unspecified near-root phrase into a fixed level count.

The described PNS version retains information for prove-best cutoffs near the root of each subtree. Section 2 explains the relevant information as successor upper bounds from an initial traversal that examined every descendant without a beta cutoff; Section 3 selects only part of that information for PNS. The paper does not specify a numerical retention depth.

### Partially Informed NegaScout: initial-principal-variation

evidence: supported. Targets: AIMech:PartiallyInformedNegaScout.

The source defines the retained principal variation by the initial search’s selected terminal path. The statement does not upgrade that initial path to a permanently valid exact minimax path or invent later replacement/eviction rules.

PNS also maintains the principal variation, defined here as the path to the terminal node that the initial search considered best. This identifies the retained path; the paper does not give a separate PNS procedure specifying its later updates.

### Partially Informed NegaScout: particular-partial-information-policy

evidence: supported. Targets: AIMech:PartiallyInformedNegaScout.

The introduction distinguishes PNS, NS and INS, and Section 3 explicitly says several compromise policies can be devised before describing its own version. This is a source-level distinction, not a completed current-inventory or global acronym decision.

The authors introduce PNS as a particular compromise between baseline NegaScout and the complete-information INS subtree map. They explicitly allow other possible compromise policies. The PNS description therefore identifies this retention policy rather than every method that saves some NegaScout search information.

### Partially Informed NegaScout: reported-comparison-design

evidence: supported. Targets: AIMech:PartiallyInformedNegaScout.

The design details come from Section 4 and the two figure labels. The count unit is leaves/terminal nodes normalized to minimal game-tree size, not elapsed time. No plotted values, superiority claim or missing INS/SSS* value is fabricated.

The paper includes PNS in comparisons with AB, NS, INS and SSS* on generated trees with random ordering or a 60% probability that the first descendant is best. Each plotted point averages twenty runs, and terminal-node counts are normalized to minimal game-tree size. Figures 4 and 5 show width-5 and width-20 settings; INS and SSS* results at depths 7 and 8 in Figure 5 are unavailable because of memory constraints. This describes the study design, not a numeric performance guarantee.

### Partially Informed NegaScout: limitation 1

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

The full four-page inspection finds a prose PNS description alongside explicit NS and INS listings. It supports a bounded missing-specification observation in this artifact, not an assertion that no implementation exists elsewhere.

PNS is described in prose, while Figure 1 lists NS and the appendix lists INS. No complete PNS listing, exact near-root retention depth, principal-variation update rule, bound-storage interface, eviction policy or cache lifetime is supplied. These details must not be filled in by silently copying INS.

### Partially Informed NegaScout: limitation 2

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

Figure 3 labels upper bounds separately from the re-searched exact example value. The explicit max(a,alpha) and last-successor guard belong to the INS appendix. No PNS listing establishes their exact transfer, and the draft claims no implementation theorem.

The prove-best explanation depends on valid successor upper bounds and distinguishes those bounds from a true value obtained during re-search. It does not establish that all failed-window returns are exact values or that every complete INS guard and cutoff is retained by PNS. The descriptive PNS policy is not a certified executable implementation or an independently proved optimality theorem.

### Partially Informed NegaScout: limitation 3

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

Integer declarations, unit-width probes and width/depth tree interfaces constrain the displayed context. Broader environments are not disproved; their extension is simply outside the inspected PNS contract.

The displayed base procedures use integer scores, adjacent-value windows and a tree of supplied width and depth. This draft does not extend PNS to arbitrary real-valued window tolerances, cyclic graphs, transposition handling, stochastic games, quiescence search or unspecified early-terminal conventions.

### Partially Informed NegaScout: limitation 4

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

The summation occurs in the complete INS discussion before the PNS compromise, and the hash-table proposal names INS. Ambiguous expression rendering is retained. A total PNS memory guarantee is not inferred from either passage.

The source does not supply a precise PNS space formula or a hard total-memory cap. The partly ambiguous summation on p.1041 concerns retention of all INS information, and the later hash-table suggestion also concerns INS. Neither is a specified PNS storage implementation or a bound covering its entire stack and data structures.

### Partially Informed NegaScout: limitation 5

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

This is a version qualification, grounded in the fresh 1985 sentence and the separately attributed earlier 1987 primary reading/comparison. Different descriptions are not sufficient to prove incompatible implementations or exact equivalence.

The 1985 description combines near-root prove-best information with principal-variation retention; the later 1987 journal describes PNS using first-level upper bounds. Their exact implementation, retention-depth and path-management correspondence remains a version question, rather than an established equivalence or demonstrated contradiction.

### Partially Informed NegaScout: limitation 6

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

The source fixes the generated-tree comparison setting and says variability work continues. The draft reproduces design context only; it does not generalize sampled curves or claim a rerun.

The terminal-count comparisons depend on the generated trees, width, depth parity, ordering and twenty-run samples. The paper says further variability measurements are in progress. No curve digitization, runtime reproduction or universal node-dominance claim is made here.

### Partially Informed NegaScout: limitation 7

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

The source explicitly makes timing implementation-dependent and distinguishes terminal counts from overhead. PNS preference is an author observation in that context. Ratios concerning INS and SSS* are not transplanted to PNS.

The reported preferences for PNS and execution-overhead observations describe the authors’ implementations and cost model. They do not establish portable speedups, byte budgets or that fewer terminal visits always yield lower running time; timing claims about INS or SSS* must not be reassigned to PNS.

### Partially Informed NegaScout: limitation 8

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

Artifact properties and access/read scope are inspection metadata. The official acquisition and full image reading support this disclosure; some reconstructed characters remain uncertain and the seven cited full works remain unread in this draft.

The defining artifact is the inspected official-hosted four-page 1985 publication reconstructed by ABBYY in 2006. Extracted text omits listings and parts of the bibliography; all four page images were inspected, but some formula and reference characters remain ambiguous. The seven cited originals were not inspected for this draft and are retained as source questions rather than imported proof evidence.

### Partially Informed NegaScout: defining retention policy

evidence: supported. Targets: AIMech:PartiallyInformedNegaScout.

The source explicitly names PNS and describes two retained information components. The definition preserves the particular 1985 policy and intended re-search use without asserting a storage bound, speedup, fixed retention depth or complete executable contract.

A NegaScout variant for adversarial game-tree search that retains prove-best information near the root of each subtree and the principal variation from an initial search to guide a later re-search, as the particular partial-information policy described in the 1985 paper.

### Partially Informed NegaScout: algorithm kind

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

The source names an operational partial-information NegaScout policy for adversarial game-tree search. It is appropriately described as an algorithm, with its available retention mechanism stated and its absent complete listing qualified. It is neither a trained model nor a benchmark or generic memory-saving task.

The descriptive algorithm kind does not certify a full executable interface. Exact near-root retention depth, principal-variation updates, storage rules and complete pruning control remain unresolved. The INS appendix and baseline NS listing must not be silently recast as the missing PNS listing.

### Partially Informed NegaScout: source-local identity and historical comparison

identity: supported. Targets: AIMech:PartiallyInformedNegaScout.

Retain the full name Partially Informed NegaScout with aliases empty. The selected scope is the particular 1985 policy. Bare PNS is unsuitable as a global alias because a separate primary abstract uses it for Proof-Number Search. The 1987 INS and DUAL* previews are prospective comparisons; later maintained SVPG, IE and ITERSSS records remain separate methods.

This record draft denotes the particular partial-information NegaScout policy described in the official 1985 paper: prove-best information near each subtree root and the principal variation from its initial search. It does not identify all partial NegaScout policies, the complete-information 1987 INS procedure, baseline NegaScout, Principal Variation Search, DUAL* or proof-number search. The source-local abbreviation PNS is omitted from global aliases because a separate primary publication explicitly uses PNS for Proof-Number Search. The 1985 near-root-plus-path description and the 1987 first-level upper-bound description remain an unresolved version question. Historical comparison at 05:11–05:12 UTC on 2026-10-16 covered 801 native and 442 pinned AIO records at HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c, with four ignored- and hidden-inclusive search roots. A separate subsequent comparison read the newly added SVPG, Iterative Expansion and ITERSSS* records and current main 911 source context. That bounded supplement does not constitute a new complete inventory or assign PNS a source owner. Full source and evidence limitations remain explicit. The historical four-root search includes hidden and ignored files. All 7 bibliography objects, 9 original questions and 3 additional context questions remain retained. No current canonical absence, source-owner allocation or closure is inferred.

### Partially Informed NegaScout: bounded 30-target AIO no-match

grounding: supported. Targets: AIMech:PartiallyInformedNegaScout.

Retain the accepted explicit no-match assessment and all 30 target-specific reasons. Generic memory, recursion, tree structure, adversarial wording and game applications do not establish identity or an informative source-backed relation to the inspected model, task, neural architecture and tensor-layer concepts.

Historical prospective collection on 2026-10-16 from 05:11:39 to 05:12:47 UTC, branch goal/discover-ai-concepts-round361, HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c. Compared all 1,243 record identities (801 native and 442 pinned AIO; 4,927 field occurrences and 3,766 normalized values). All 18 normalized probes, including the proposed local ID, were clear. Four ignored- and hidden-inclusive fixed-string, case-insensitive, word-delimited searches produced 10 distinct matching contents and 14 occurrences; every content and occurrence binding was read. The complete identity DATA matched the previously read INS/DUAL snapshot exactly. Fresh semantic context covered 114 native identity/definition projections, 12 selected native definitions and all their claim statements, 30 complete annotated AIO nodes and 97 incident triples, and the prospective INS/DUAL drafts. The three actual records added afterward were read in a separate bounded supplement; their addition was reported to bring native counts to 804. No later whole-inventory clearance, global source exhaustion or future ownership is claimed.

No suitable positive AIO mapping was identified for this source-specific partial NegaScout procedure. The inspected targets concern learned models, learning tasks, tensor layers or broad mathematical/representational classes. Shared memory, recursion, tree shape, adversarial terminology or game applications alone do not establish an informative source-backed relation. This is a bounded curator assessment of the pinned snapshot, not an upstream ontology assertion.

AIO:ActiveLearning: Acquiring bounds during game-tree search is not interactively querying labels for training data. The 1985 title does not establish the pinned active-learning task.
AIO:ArtificialNeuralNetwork: PNS specifies no artificial-neuron architecture or neural training; its stored search information is not a neural network.
AIO:CausalGraphicalModel: An alternating game tree is not a causal probabilistic representation of a data-generating process.
AIO:Classification: PNS searches values/moves in a supplied game tree; it does not classify observations into learned classes.
AIO:DecisionTree: The pinned node is a Classification subclass. Its broader decision-support comment does not identify a partial NegaScout game-tree search algorithm with a classification tree.
AIO:GenerativeAdversarialNetwork: Adversarial game-tree evaluation does not imply competing generative/discriminative neural networks or GAN training.
AIO:GraphConvolutionalPolicyNetwork: PNS uses neither graph convolutions nor a trained goal-directed graph-generation policy network.
AIO:GraphLanguageModel: A game-tree representation is not a graph language model; the source supplies no language-model mechanism.
AIO:HashingLayer: Partial search-information storage does not establish categorical feature hashing or a preprocessing layer. The PNS storage contract is itself incompletely specified.
AIO:HierarchicalClassification: Successive game moves form a search hierarchy, not a hierarchy of classification labels.
AIO:MachineLearningTask: Retaining already computed search bounds is not on its own a task of building methods that learn from data. No such learning task is defined for this PNS.
AIO:MathematicalFunction: Generic score arithmetic does not supply an informative relation from the operational partial NegaScout algorithm to the pinned scalar-function class.
AIO:MaximumLayer: The pinned operation merges tensors elementwise. Bound comparisons in game-tree re-search do not constitute that layer.
AIO:MemoryAugmentedLLM: PNS is not a language model and its retained bounds/principal variation do not establish external-memory LLM identity.
AIO:MemoryCellLayer: Selective retention of search information is not a layer made of neural memory cells.
AIO:MinimumLayer: The pinned tensor minimum merge is distinct from search-window control and alternating-player value propagation.
AIO:Model: The very broad representation class does not identify the source operational procedure or supply a defensible informative mapping merely because a search tree represents a game.
AIO:Network: Interconnected search nodes do not make the algorithm itself the pinned generic Network concept; topology alone is insufficient.
AIO:NeuralTuringMachineNetwork: The source PNS has no differentiable neural memory controller; using memory does not establish this architecture.
AIO:NeuroSymbolicLLM: No neural language model or neural-symbolic integration appears in the selected PNS procedure.
AIO:PolicyLayer: The PNS description does not define a neural layer outputting a probability distribution over actions.
AIO:ProbabilisticGraphicalModel: Its game tree contains alternatives and score bounds, not a model of random-variable conditional dependencies.
AIO:RandomForest: PNS is not an ensemble of learned classification/regression trees. Generated experimental trees are inputs, not trained forest estimators.
AIO:ReasoningLLM: Game-tree reasoning does not establish a large language model or the pinned reasoning architecture.
AIO:RecursiveLLM: Search recursion is a control convention, not a recursive language-model architecture.
AIO:RecursiveLanguageModel: The selected source does not build recursive representations for language modeling.
AIO:RecursiveNeuralNetwork: Recursive game-tree traversal does not apply learned neural weights over structured inputs.
AIO:ReinforcementLearning: The described finite game-tree search with supplied scores and retained bounds does not learn a policy from reward interactions. A game application alone does not justify even an algorithm-to-task related mapping.
AIO:ReinforcementLearningLLM: PNS is not a language model fine-tuned through reinforcement learning.
AIO:TrainingStrategy: The source controls search and information retention, not preprocessing or model-training strategy.

### Partially Informed NegaScout: defining evidence and separate contexts

provenance: supported. Targets: AIMech:PartiallyInformedNegaScout.

The official-hosted four-page 1985 paper supplies the definition and every positive claim citation. Its later ABBYY reconstruction metadata is not a new algorithm version. The 1987 journal remains a separate primary version context, while the 2022 abstract and 1994 institutional metadata establish acronym/retrieval context only.

Preserve the exact downloaded 1985 PDF hash, original URL, source access time and full-image reading attribution. Text extraction omitted listings and some bibliography/formula characters remain ambiguous. Neither the 1987 summary, the INS appendix, a bibliography entry nor acronym metadata supplies a complete PNS implementation. Seven original bibliography objects and nine original questions remain byte-exact; three additional context-only retrieval questions remain separate. The historical native validation checks structural/per-record requirements and supplies no scientific or future inventory clearance. All full-paper reading is attributed to the earlier researcher and independent source reviewer; this fragment assembly does not repeat it.

### Partially Informed NegaScout: retain source and acronym boundaries

scope: supported. Targets: AIMech:PartiallyInformedNegaScout.

Retain the particular 1985 PNS policy separately from complete-information INS, baseline NegaScout/PVS, DUAL*, proof-number search and unrelated memory-limited or recursive searches. The 1985 near-root-plus-principal-variation description and 1987 first-level upper-bound wording are a version question, not demonstrated contradiction or proven full equivalence. Keep the missing PNS listing, retention depth, PV maintenance, score/bound, storage and implementation interfaces explicit; no runtime, space or universal performance theorem follows.

The prove-best statement retains the root-accepted immediate-successor-branch interpretation, not enumeration of every descendant leaf. The 2022 abstract demonstrates the ambiguous PNS expansion but does not support a new Proof-Number Search or PN-MCTS record here. The current main 911 umbrella and its later ITERSSS responsibility are context, not a PNS owner assignment. All original and added questions remain unchanged and no source family is declared exhausted.

### Actual current records, source responsibilities and checks

provenance: supported. Targets: AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout.

Actual three records retain 16 claims and 28 limitations across two primary PDF artifacts/two works and three declared source rows. The 1987 journal defines INS/DUAL; the 1985 proceedings defines PNS. The 1987 PNS comparison is context on the shared artifact. Six exclusive creation outputs, one CREATE event, 87 captured inputs, parsed generated pages and six successful required checks are bound. Current source responsibility follows the accepted plan: {"additional_source_question_count": 0, "changed_main_indexes": [911], "changed_nested_indexes": [], "historical_source_responsibility_links": 2, "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_source_objects": 46, "source_object_counts": {"ijcai1985": {"additional_context_questions": 3, "bibliography": 7, "source_questions": 9}, "journal1987": {"bibliography": 16, "incidental_retrieval_contexts": 2, "source_questions": 9}}}. The 46 source objects and two historical links remain explicit. One approved INS access-attribution correction is applied; version questions remain pending. Complete actual 361 inherited accounting and older 360 source durability remain exact. No research exhaustion or publication completion is implied.

Actual canonical fields, 46 original objects, two historical responsibility links, current additional questions and inherited projection were assessed with exact receipts. Historical primary reading remains attributed. The correction updates access status only. Review save, committed-head verification and publication remain subsequent operations.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:InformedNegaScout. Retain full-information INS as distinct from the partial PNS policy and the LIVE/SOLVED DUAL* controller. Preserve the source-relative odd/even levels, research/resflag distinction, max(a,alpha) threshold and returned-bound qualification; do not silently complete merit storage or last-successor guards.
- retain: AIMech:DUALStar. Retain the source-specific MAX-rooted DUAL* controller, including maximum-based merits and increasing-merit insertion behind ties. Keep intended terminal/interior interpretation, root-before-parent success handling and purge/list/empty-OPEN boundaries explicit.
- retain: AIMech:PartiallyInformedNegaScout. Retain the particular 1985 PNS policy separately from complete-information INS, baseline NegaScout/PVS, DUAL*, proof-number search and unrelated memory-limited or recursive searches. The 1985 near-root-plus-principal-variation description and 1987 first-level upper-bound wording are a version question, not demonstrated contradiction or proven full equivalence. Keep the missing PNS listing, retention depth, PV maintenance, score/bound, storage and implementation interfaces explicit; no runtime, space or universal performance theorem follows.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ins-dual-accepted-support | /private/tmp/aimech-ins-dual-review-fragments-20261016/accepted-scientific-support.original.json; records | context_only | Exact root-accepted source support; original historical author-reading statements are attributed and do not assert a fresh primary reread by this fragment author. |
| ins-dual-source-roles | /private/tmp/aimech-ins-dual-review-fragments-20261016/source-metadata-and-roles.original.json; native_evidence_rows | context_only | Two native source rows share the one defining 1987 journal PDF; partially read alternate rendering and earlier versions remain separate research context. |
| ins-dual-original-questions | /private/tmp/aimech-ins-dual-review-fragments-20261016/source-question-continuity.original.json; journal_references; source_questions; exact_original_pointer_object | context_only | All sixteen bibliography and nine question objects and the exact original responsibility wrapper retained unchanged; no future owner or closure. |
| ins-dual-additional-context | /private/tmp/aimech-ins-dual-review-fragments-20261016/additional-source-context.original.json; incidental_retrieval_contexts; additional_1985_route | context_only | Two exact historical retrieval objects remain separate; the 1985 route advances an existing version question and does not add a positive 1987 native evidence row. |
| ins-dual-historical-identity | /private/tmp/aimech-ins-dual-identity-mapping-proposal-20261016/proposal.json; complete prospective proposal | context_only | Historical identity/no-match assessment, with explicit ignored-inclusive scope; no current inventory or owner clearance. |
| ins-dual-pinned-aio-context | /private/tmp/aimech-ins-dual-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json; thirty full nodes and97 incident triples | context_only | Bounded pinned-AIO context previously read in the accepted identity preparation; no new all-ontology semantic review. |
| ins-dual-root-native-acceptance | /private/tmp/aimech-ins-dual-native-data-preparation-20261016/root-native-data-acceptance.json; complete static native-data acceptance | context_only | Root accepted exact prospective scientific/identity/no-match DATA and separately authorized historical TEMP validation. |
| ins-dual-root-preview-readback | /private/tmp/aimech-ins-dual-native-preview-20261016/root-native-preview-readback.json; complete root readback | context_only | Root accepted exact historical TEMP preview transfer and actual validator receipts; this is not a new current repository gate. |
| ins-dual-independent-source-review | /private/tmp/aimech-ins-dual-independent-source-audit-20261016/assessment.final.json; bounded source/control review | context_only | Separate sibling source/control review, with scope and source-reading attribution retained; not an implementation certification. |
| ins-dual-threshold-disposition | /private/tmp/aimech-ins-dual-independent-source-audit-20261016/finding-disposition.v2.json; INS threshold finding disposition | context_only | Preserves max(a,alpha) guard precision and fail-low return qualification from the accepted correction. |
| ins-accepted-preview | /private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.native-preview.json; complete accepted TEMP native preview | context_only | Exact accepted prospective native content with historical curation; no actual canonical or future delivery assertion. |
| ins-historical-native-validation | /private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.validation.json; complete historical TEMP per-record validation receipt | context_only | Actual earlier TEMP native-schema validation; not a scientific proof, current repository gate or permission for canonical insertion. |
| ins-dual-primary-1 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section2, printed p.186 / PDF p.2; Figure3, printed p.191 / PDF p.7 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-2 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections2.2–2.3 and Figure2, printed pp.188–190 / PDF pp.4–6 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-3 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections2.2–2.3 and Figure2, printed pp.188–190 / PDF pp.4–6; Figure3, printed p.191 / PDF p.7 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-4 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section2.3, printed p.190 / PDF p.6; Figure3, printed p.191 / PDF p.7 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-5 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure3, printed p.191 / PDF p.7; storage explanation, printed p.190 / PDF p.6 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-6 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections4.1.1–4.1.2, printed pp.193–194 / PDF pp.9–10; Figures5–7, printed pp.195–197 / PDF pp.11–13 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-7 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections1–2 and Figures3–4, printed pp.186,191–192 / PDF pp.2,7–8; Section4.1, printed pp.193–194 / PDF pp.9–10 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-8 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure3, printed p.191 / PDF p.7 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-9 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section2.3, printed p.190 / PDF p.6; Section4 opening, printed p.193 / PDF p.9 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-10 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections4.1.1–4.1.2, printed pp.193–194 / PDF pp.9–10; Figures5–7 and Section5, printed pp.195–198 / PDF pp.11–14 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-11 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section4 opening, printed p.193 / PDF p.9; Section4.2, printed p.198 / PDF p.14; reference12, printed p.199 / PDF p.15 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-12 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section1 and footnote1, printed p.186 / PDF p.2; Section2.3, printed p.190 / PDF p.6; references2–9, printed p.199 / PDF p.15 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-13 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Journal header, printed p.185 / PDF p.1, and references/dates, printed p.199 / PDF p.15; separately retained source-versions-and-roles and TR85-16 question | context_only | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-provenance-1 | /private/tmp/aimech-ins-dual-scientific-data-draft-20261016/draft-author-reading.json; complete source/reading provenance object | supports | Direct provenance for curator access, version and assurance limitations; no claim that the primary paper reports this later curation history. |
| ins-dual-provenance-2 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/source-versions-and-roles.json; complete source/reading provenance object | supports | Direct provenance for curator access, version and assurance limitations; no claim that the primary paper reports this later curation history. |
| ins-dual-provenance-3 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/bibliography-and-followups.json; complete source/reading provenance object | supports | Direct provenance for curator access, version and assurance limitations; no claim that the primary paper reports this later curation history. |
| ins-dual-primary-14 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections2–5, printed pp.186–198 / PDF pp.2–14; references, printed p.199 / PDF p.15 | context_only | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-15 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections1–2.3, printed pp.186,188–191 / PDF pp.2,4–7 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| dual-accepted-preview | /private/tmp/aimech-ins-dual-native-preview-20261016/DUALStar.native-preview.json; complete accepted TEMP native preview | context_only | Exact accepted prospective native content with historical curation; no actual canonical or future delivery assertion. |
| dual-historical-native-validation | /private/tmp/aimech-ins-dual-native-preview-20261016/DUALStar.validation.json; complete historical TEMP per-record validation receipt | context_only | Actual earlier TEMP native-schema validation; not a scientific proof, current repository gate or permission for canonical insertion. |
| ins-dual-primary-16 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section3, printed pp.191–193 / PDF pp.7–9; Figure4, printed p.192 / PDF p.8 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-17 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure4 and surrounding Section3 prose, printed pp.192–193 / PDF pp.8–9 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-18 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure4, printed p.192 / PDF p.8 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-19 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure4, printed p.192 / PDF p.8; purge description, printed p.193 / PDF p.9 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-20 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section4 opening, printed p.193 / PDF p.9; Section4.2, printed p.198 / PDF p.14 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-21 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections4.1.1–4.2, printed pp.193–198 / PDF pp.9–14; Figures5–7, printed pp.195–197 / PDF pp.11–13 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-22 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections1 and3, printed pp.186,191–193 / PDF pp.2,7–9; Section4.1, printed pp.193–194 / PDF pp.9–10 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-23 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Figure4 and Section3 continuation, printed pp.192–193 / PDF pp.8–9 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-24 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections4.1.1–4.1.2 and Figures5–7, printed pp.193–197 / PDF pp.9–13; Section5, printed p.198 / PDF p.14 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-25 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section3, printed pp.191–193 / PDF pp.7–9; reference13, printed p.199 / PDF p.15 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-26 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Sections3–5, printed pp.191–198 / PDF pp.7–14; references, printed p.199 / PDF p.15 | context_only | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| ins-dual-primary-27 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section3 and Figure4, printed pp.191–193 / PDF pp.7–9 | supports | Selected 1987 journal procedure/publication context; prior primary reading is attributed. Curator access and assurance statements rely on their separate provenance evidence. |
| pns-accepted-preview | /private/tmp/aimech-pns-native-preview-20261016/PartiallyInformedNegaScout.native-preview.json; complete prospective native preview | context_only | Exact root-read TEMP preview with actual historical curation. It is not a future canonical record. |
| pns-accepted-core | /private/tmp/aimech-pns-native-data-preparation-20261016/PartiallyInformedNegaScout.native-core.json; complete native-shaped core | context_only | Accepted four-claim/eight-limitation DATA with source-scoped identity and 30-target no-match; this fragment author also authored that science and identity work. |
| pns-accepted-support | /private/tmp/aimech-pns-scientific-data-draft-20261016/scientific-support.json; definition, claims and limitations | context_only | Exact accepted source-support narratives. Original pending metadata remains historical; later acceptances are separately bound. |
| pns-source-roles | /private/tmp/aimech-pns-native-data-preparation-20261016/source-metadata-and-roles.json; complete metadata and roles | context_only | Derived source-role metadata: 1985 defining artifact; 1987 version context; acronym metadata supplies no positive PNS mechanism evidence. |
| pns-original-questions | /private/tmp/aimech-pns-review-fragments-20261016/source-question-continuity.original.json; bibliography and additional_questions; all original wrapper fields | context_only | Seven original bibliography objects and nine questions, byte-exact with historical pending wording. |
| pns-extra-questions | /private/tmp/aimech-pns-review-fragments-20261016/additional-context-questions.original.json; questions[0:3] | context_only | Three separate context-only retrieval questions: author-index PNS PDF, 1994 Proof-number original, and 2022 PN-MCTS paper. No novelty or owner allocation. |
| pns-identity-proposal | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/identity-mapping-proposal.json; source-specific identity and prospective boundaries | context_only | Accepted historical identity proposal; aliases remain empty and canonical owner/base/cohort remain unset. |
| pns-historical-search | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/collection.json; counts, normalized probes, scans and search_groups | context_only | Historical collection with exact raw scan provenance; semantic reading and supplemental current context are separately attributed. |
| pns-aio-context | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json; 30 complete annotated nodes and 97 incident triples | context_only | Exact pinned AIO context inspected for the bounded no-match proposal; no whole-ontology absence theorem. |
| pns-mapping-assessment | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/aio-mapping-assessment.json; all 30 examined targets and rationales | context_only | Full source-specific target rejection reasons; only the declared ActiveLearning spacing correction differs in the native DATA. |
| pns-post-snapshot-context | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/post-snapshot-context-assessment.json; three actual record comparisons and current main911 context | context_only | Later SVPG, IE and ITERSSS record context plus one partial source owner. This bounded supplement is not a new global identity or owner clearance. |
| pns-acronym-context | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json; primary abstract and institutional metadata reading scope | context_only | The 2022 primary abstract explicitly expands Proof-Number Search as PNS. The 1994 record is metadata-only; full papers remain unread here and the publisher403 is retained. |
| pns-root-science | /private/tmp/aimech-pns-scientific-data-draft-20261016/root-scientific-data-acceptance.json; accepted scope and immediate-successor interpretation | context_only | Root accepted the source-scoped science, including the immediate-successor-branch sense of the prove-best statement. This is not a formal saved canonical review. |
| pns-root-identity | /private/tmp/aimech-pns-identity-mapping-proposal-20261016/root-prospective-identity-acceptance.json; prospective identity/no-match acceptance | context_only | Root accepted prospective identifier/name/empty aliases and 30-target no-match with bounded historical reading attribution. |
| pns-root-native-core | /private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json; exact native-core acceptance | context_only | Root read exact native core, science transfer and metadata; authorizes only the separately recorded TEMP preview event. |
| pns-root-preview | /private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json; actual preview/validation readback | context_only | Root verified exact accepted core plus actual curation; no canonical or future ownership acceptance. |
| pns-independent-science | /private/tmp/aimech-pns-independent-draft-audit-20261016/assessment.json; bounded independent source/draft assessment | context_only | Sibling354 read all four 1985 primary images and source DATA; prior source reading is attributed, not freshly repeated by this fragment assembly. |
| pns-independent-native | /private/tmp/aimech-pns-native-data-independent-audit-20261016/assessment.json; complete independent native DATA review | context_only | Sibling354 checked exact science, source continuity, 30 full AIO nodes/97 edges and stated neighbor scope; no current runtime clearance. |
| pns-preview-validation | /private/tmp/aimech-pns-native-preview-20261016/PartiallyInformedNegaScout.validation.json; one actual validate_curated_record invocation, errors[] | context_only | Historical structural/per-record semantics result only; neither scientific certification nor future whole-inventory validation. |
| pns-primary-01 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 2, Figure 3, and Section 3, printed p.1041 / PDF p.2 | supports | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-02 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 3, PNS paragraph, printed p.1041 / PDF p.2 | supports | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-03 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Introduction, printed p.1040 / PDF p.1; Section 3, printed p.1041 / PDF p.2 | supports | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-04 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 4 and Figures 4–5, printed p.1042 / PDF p.3 | supports | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-05 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 3, printed p.1041 / PDF p.2; Figure 1, printed p.1040 / PDF p.1; Appendix heading and listing, printed p.1043 / PDF p.4 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-06 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 2 and Figure 3, printed p.1041 / PDF p.2; Appendix, printed p.1043 / PDF p.4 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-07 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Introduction and Figure 1, printed p.1040 / PDF p.1; Appendix, printed p.1043 / PDF p.4 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-08 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 3, printed p.1041 / PDF p.2; Section 5, printed p.1042 / PDF p.3 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-09 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 3, printed p.1041 / PDF p.2 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-10 | /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf; Section 2.3, printed p.190 / PDF p.6 | context_only | Separate 1987 journal primary context for PNS first-level wording; it does not define the full 1985 PNS implementation or establish exact version equivalence. |
| pns-primary-11 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Section 4 and Figures 4–5; conclusion final paragraph, printed p.1042 / PDF p.3 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-12 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Sections 4–5, printed p.1042 / PDF p.3 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-13 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Official PDF metadata; complete pp.1040–1043; references, printed p.1043 / PDF p.4 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-14 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Introduction, printed p.1040 / PDF p.1; Section 3, PNS paragraph, printed p.1041 / PDF p.2 | supports | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| pns-primary-15 | /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf; Complete official-hosted 1985 PDF, printed pp.1040–1043; PNS description in Section 3 on p.1041 | context_only | Inspected official-hosted four-page 1985 artifact. Locator supports the bounded source interpretation; no executable contract or uninspected reference proof is imported. |
| actual-write | /private/tmp/aimech-cohort362-write.json | context_only | Actual exclusive creation of three native records, report pair and CREATE history. |
| captured-inputs | /private/tmp/aimech-cohort362-postwrite-20261016/actual-capture.json | context_only | Actual canonical input-byte and maintained-target capture. |
| postcapture-reading | /private/tmp/aimech-cohort362-postwrite-20261016/root-postcapture-reading.json | context_only | Actual root reading of source-scoped canonical records, metadata and all retained question objects; historical source reading stays separately attributed. |
| governance-assessment | /private/tmp/aimech-cohort362-governance-20261016/assessment.json | context_only | Actual byte preservation, dynamic owner-plan reconstruction, inherited metadata and parsed-page audit. |
| rendered-pages | /private/tmp/aimech-cohort362-governance-20261016/rendered-pages.json | context_only | Actual generated-page bytes and parsed content; no visual/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort362-actual-scientific-audit-20261016/assessment.json | context_only | Actual record scientific assessment with its own attributed source-reading scope. |
| current-identity-collection | /private/tmp/aimech-cohort362-current-collection-v2-20261016/collection.json | context_only | Actual scoped ignored-inclusive identity collection; mechanical capture is distinct from human semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/assessment.current.v2.json | context_only | Actual attributed current identity and source-question assessment. |
| root-decisions | /private/tmp/aimech-cohort362-current-decisions.v2.json | context_only | Exact current record identity decisions, dynamic accepted ownership and retained source questions. |
| ownership-plan | /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/ownership-plan.proposed.v2.json | context_only | Two distinct source groups retain 46 original objects and two separate historical responsibility links; current additional questions remain explicit. |
| ownership-plan-acceptance | /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/root-ownership-acceptance.json | context_only | Actual root acceptance of current source responsibility; no whole-issue closure. |
| current-discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.json | context_only | Canonical durable report containing the exact recursively queryable predecessor_state bundle and separate current source responsibilities. |
| inherited-source-durability | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.json | context_only | The current canonical predecessor bundle preserves actual360 source_durability with the reconstructible exact JSON manifest and all 100 original asset metadata/provenance objects. This inherited SHA-256 does not identify a publisher PDF. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/informed-negascout-dual-star-and-partially-informed-negascout/2026-10-16T061701Z-codex-e1a1bb.yaml | context_only | Actual single CREATE event for the report. |
| review-support | /private/tmp/aimech-cohort362-review-assembly-preparation-20261016/review-support.prepared.json | context_only | Exact historical per-claim and per-limitation narrative support. |
| approved-access-attribution-correction | /private/tmp/aimech-cohort362-wording-correction-20261016/root-accepted-correction.json | context_only | Exact root-approved INS limitation8 access-attribution correction, with historical before/after and separately completed PNS reading. Issue415 tracks the correction; research/version questions remain separate. |
| correction-pns-reading-1 | /private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json | context_only | Attributed accepted PNS source/native reading supporting the access-status correction. |
| correction-pns-reading-2 | /private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json | context_only | Attributed accepted PNS source/native reading supporting the access-status correction. |
| check-gate | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-gate.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-vendor | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-vendor.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-check-source | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-check-source.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-render.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render-check | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-render-check.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-diff | /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-diff.json | context_only | Actual completed required command, exit0; scope is its recorded output. |

## Limits And Additional Notes

- Source-scoped mechanisms and mathematical/control-flow boundaries retain accepted fragment narratives except the precisely attributed INS limitation8 access-status correction. Native schema validation is evidence of structural validity, not scientific proof.
- INS/DUAL source and core authorship, PNS source/native/fragment authorship, earlier independent source reviews and this assembly authorship remain separately attributed.
- Actual current identity/no-match and responsibility decisions are bound to this collection and accepted owner plan. Earlier source, identity and neighbor readings remain separately attributed; the current snapshot does not clear future additions.
- Actual six creation outputs, one CREATE history, 87 capture inputs and 7 parsed generated pages are bound. Six required commands passed; earlier failed attempts remain explicit. Canonical review save/check and publication are subsequent operations.
- The 62 scientific narratives originate from the two accepted fragments, with the shared INS/DUAL group included once. The approved INS limitation 8 summary/details are the sole scientific-narrative correction. All scientific assessments receive separately attributed actual evidence links. The 78 original evidence templates retain their metadata except actual local access times and UTC normalization. The 63rd assessment records current governance. Correction evidence and both PNS reading receipts link directly from the corrected assessment; original fragments stay immutable.
- Local evidence access instants come from actual attributed postcapture reading. Primary acquisition times retain their historical instants, normalized to UTC Z. Historical identities/access statements elsewhere remain explicitly historical; current identity notes are separately bound.
- The1987 journal defines INS/DUAL; the1985 proceedings defines PNS. The1987 PNS version-comparison citation is context on an already counted artifact, not another defining PNS source.
- Original source objects and historical responsibilities remain distinct from the actual current dispositions bound here. Issue415 tracks the approved access-attribution repair; source/version questions and inherited issues retain their separate scopes. No issue closure, discovery exhaustion or implementation certification is implied.
- The shared 1987 source group retains16 bibliography objects,9 source questions and2 incidental contexts once for INS and DUAL*. The1985 PNS group retains7 bibliography objects,9 source questions and3 additional contexts. These46 objects and2 separately counted historical responsibility links are source accounting, not46 new concepts. The PNS link is also an original1987 question; it is not a newly discovered second question.
- {"added_record_ids": [], "assessment": "The Stockman1979 SSS* original is already an explicit pending source under main911 in the ITERSSS* accounting. Neither DUAL* nor the existing ITERSSS* record makes original SSS* identical or fully inspected.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group": "journal1987", "kind": "bibliography", "next_check": "Read the original SSS* procedure and proof under its own scope; coordinate the identical Stockman citation in the1985 and1986 ledgers.", "original": {"exact_original_object": {"exact_extracted_citation": "Stockman, G.C., A minimax algorithm better than alpha-beta?, Artificial Intelligence 12(2) \n(1979) 179-196.", "locator": "printed p.199 / PDF p.15, reference1", "number": 1, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "e65f5558c42abab080d698173292ee91848f5143a9d22d7c77693e19d1a75763", "pointer": "/journal_references/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Pearl1980 minimax-tree analysis is a separate original. The retained citation and the new procedures do not inspect its asymptotic arguments or establish SCOUT identity.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the exact1980 paper and its assumptions; distinguish its procedure/theory scope from Pearl1984 book context and the1987 INS procedure.", "original": {"exact_original_object": {"exact_extracted_citation": "Pearl, J., Asymptotic properties of minimax trees and game-seraching procedures, Artificial \nIntelligence 14(2) (1980) 113-138.", "locator": "printed p.199 / PDF p.15, reference2", "number": 2, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 1, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "79b7afdb65502307dc1812c61f98ee0ba34e7672a320485e7f1bcca43e9b0809", "pointer": "/journal_references/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Fishburn1984 is the cited book, distinct from the1981 report cited by the1985 PNS paper. Similar titles do not prove identical versions.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect the1984 book and independently compare the1981 Technical Report431 before merging source or minimal-window lineage claims.", "original": {"exact_original_object": {"exact_extracted_citation": "Fishburn, J.P., Analysis of Speedup in Distributed Algorithms (UMI Research Press, Ann \nArbor, MI, 1984).", "locator": "printed p.199 / PDF p.15, reference3", "number": 3, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 2, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "404a0d030a162c6e2d0aeefd5a65758ce80d52b8b1be5de839e682ebbb92c74a", "pointer": "/journal_references/2"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1982 parallel strongly ordered game-tree work is a separate source, not the sequential INS or DUAL* mechanism.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect the original parallel search, ordering and correctness assumptions; reconcile the reconstructed1985 reference metadata separately.", "original": {"exact_original_object": {"exact_extracted_citation": "Marsland, T.A. and Campbell, M.S., Parallel search of strongly ordered game trees, ACM \nComput. Surv. 14(4) (1982) 533-552.", "locator": "printed p.199 / PDF p.15, reference4", "number": 4, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 3, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "3893deb1cf5862c2e620154da58879038bd1d9749a1b0a7eb192d0329b45fbef", "pointer": "/journal_references/3"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The IJCAI1983 alpha-beta implementation comparison remains a distinct lineage/performance original.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the1983 implementation comparisons before generalizing NegaScout/PVS names, overhead or runtime claims.", "original": {"exact_original_object": {"exact_extracted_citation": "Marsland, T,A., Relative efficiency of alpha-beta implementations, in: Proceedings 1JCAI-83, \nKarlsruhe, F.R.G. (1983) 763-766.", "locator": "printed p.199 / PDF p.15, reference5", "number": 5, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 4, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "6a383b41c881bad193bed7a6ac5112062d70d51607e5e73e96876d3bc2758d85", "pointer": "/journal_references/4"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1983 minimax comparison is not represented merely by adding two procedures it later informs.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect its concrete comparator algorithms, move ordering, parity and empirical setup; coordinate the same citation in the1985 bibliography.", "original": {"exact_original_object": {"exact_extracted_citation": "Campbell, M.S. and Marsland, T.A., A comparison of minimax tree search algorithms, \nArtificial Intelligence 20(4) (1983) 347-367.", "locator": "printed p.199 / PDF p.15, reference6", "number": 6, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 5, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "7fb6fd2ba0e1d1abd0925db0cc499132e0f9540f2bb2bee791bf62e8177641ca", "pointer": "/journal_references/5"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Reinefeld1983 is the original NegaScout improvement source, not a global alias established by the1987 footnote.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the exact Scout/NegaScout original and verify title/issue/pages and algorithm boundaries before adopting global NS/PVS aliases.", "original": {"exact_original_object": {"exact_extracted_citation": "Reinefeld, A., An improvement of the Scout tree search algorithm, 1CCA J. 6(4) (1983) 4-14.", "locator": "printed p.199 / PDF p.15, reference7", "number": 7, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 6, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "11611e80cbf31d9ccb21873d699fa04f2c9a14a1cc2b9383e273bc27b28ca3fe", "pointer": "/journal_references/6"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1985 empirical pruning comparison is independent of the separately read IJCAI1985 PNS paper despite sharing a year.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read Musczycka–Shinghal and its exact tree/pruning protocol; preserve the extracted citation spelling until original verification.", "original": {"exact_original_object": {"exact_extracted_citation": "Musczycka, A. and Shinghal, R., An empirical comparison of pruning strategies in game trees, \nIEEE Trans. Syst. Man Cybern. 15 (3) (1985) 389-399.", "locator": "printed p.199 / PDF p.15, reference8", "number": 8, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 7, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "4e8a47b94eeb96cd255163933cfaaef76120bc8f88447b119d0012855235cf94", "pointer": "/journal_references/7"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "This exact reference9 points to the official1985 paper now fully read for source-specific PNS and bounded earlier-INS comparison. Its historical not-read status remains unchanged inside original. The separately counted ijcai1985 responsibility link records proposed PNS representation; version and implementation questions remain open.", "disposition": "retained_context", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Use the existing1985 dossier and PNS record scope; pursue retention-depth, helper/storage, score and1985/1987 display differences without treating the paper as unread or as a global INS/PNS equivalence.", "original": {"exact_original_object": {"exact_extracted_citation": "Reinefeld, A., Schaeffer, J. and Marsland, T.A., Information acquisition in minimal window \nsearch, in: Proceedings 1JCAI-85, Los Angeles, CA (1985) 1040-1043.", "locator": "printed p.199 / PDF p.15, reference9", "number": 9, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 8, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "245284e1d03a251de1dd84552f1289e0bd78bd35f7e51ec4cecb261e006aa850", "pointer": "/journal_references/8"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Baudet1978 is the asynchronous-multiprocessor dissertation, not automatically the separate alpha-beta branching article retained in ITERSSS*.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Acquire and inspect this exact dissertation for the cited simulation/parallel assumptions; keep works with the same author/year distinct.", "original": {"exact_original_object": {"exact_extracted_citation": "Baudet, G.M., The design and analysis of algorithms for asynchronous multiprocessors, Ph.D. \nDissertation, Carnegie Mellon University, Pittsburgh, PA, 1978.", "locator": "printed p.199 / PDF p.15, reference10", "number": 10, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 9, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "22a41080f79081a4706a313ff52fe2f295466e42592cf833f093e9e42cf0fb0c", "pointer": "/journal_references/9"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Schaeffer1986 thesis supplies deferred experimental/search-knowledge detail and remains an independent original.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect the thesis tree generator, score distribution, ordering and timing context before stronger empirical synthesis.", "original": {"exact_original_object": {"exact_extracted_citation": "Schaeffer, J., Experiments in search and knowledge, Ph.D. Thesis, University of Waterloo, \nWaterloo, Ont., 1986.", "locator": "printed p.199 / PDF p.15, reference11", "number": 11, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 10, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "a9686fd5c71c85a8f94b0de6c0cabfeae72c99cfb4523bd546ff0d6400553e90", "pointer": "/journal_references/10"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "TR85-16 remains a title/date/page-count and incomplete-access question. The inspected cover and partial author rendering do not establish a fully read equivalent version.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Compare the27-page index description with the19-page linked rendering and exact1987 references; inspect full method/timing sections before version equivalence.", "original": {"exact_original_object": {"exact_extracted_citation": "Reinefeld, A., Marsland, T.A. and Schaeffer, J., Is best first search best?, Tech. Rept. \nTR85-16, Computing Science Department, University of Alberta, Edmonton, Alta., 1985.", "locator": "printed p.199 / PDF p.15, reference12", "number": 12, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 11, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "3e5d383fb477c917552ebb6f02439934d80f026b2d665f9a05ff484449bd69ea", "pointer": "/journal_references/11"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Kumar–Kanal1984 parallel branch-and-bound/dual-ss* is not automatically the journal sequential MAX-rooted DUAL*. Generic AND/OR similarities do not discharge this source.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the original parallel formulation and duality conventions; compare sequential control, node parity and purge semantics independently.", "original": {"exact_original_object": {"exact_extracted_citation": "Kumar, V. and Kanal, L.N., Parallel branch-and-bound formulations for AND/OR tree search, \nIEEE Trans. Pattern Anal. Mach. Intell. 6(6) (1984) 768-778.", "locator": "printed p.199 / PDF p.15, reference13", "number": 13, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 12, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "1bebe2fec20635f3d3248559841f796187930e5a5fa81385bb3c4074ac020d8c", "pointer": "/journal_references/12"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Slagle–Dixon game-tree experiments are a distinct original and their extracted venue/year/page fields are retained without silent correction.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect the original programs, scoring/order protocol and bibliographic fields before transferring experimental conclusions.", "original": {"exact_original_object": {"exact_extracted_citation": "Slagle, J. and Dixon, J., Experiments with some programs that search game trees, J. ACM 2 \n(1969) 189-207.", "locator": "printed p.199 / PDF p.15, reference14", "number": 14, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 13, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "54a8e59f219827ebdcd77ce83b947a747f79b552ffc12e4e3536cd381bce8d3d", "pointer": "/journal_references/13"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Roizen–Pearl yes-and-no comparison is a separate theoretical/empirical source, not the Stockman defining article.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check": "Read its exact comparator assumptions and strengths/limits before asserting SSS*, DUAL* or alpha-beta dominance.", "original": {"exact_original_object": {"exact_extracted_citation": "Roizen, I. and Pearl, J., A minimax algorithm better than alpha-beta? Yes and no, Artificial \nIntelligence 21(1,2) (1983) 199-220.", "locator": "printed p.199 / PDF p.15, reference15", "number": 15, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 14, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "771a8e5bc1183646115e705cdaa754f7a13fda3db704cb6519a9e8e83361d78f", "pointer": "/journal_references/14"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Knuth–Moore1975 already has explicit pending main911 responsibility in the ITERSSS* ledger. Single-agent Minimin alpha pruning under main290 does not represent this two-player alpha-beta original.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group": "journal1987", "kind": "bibliography", "next_check": "Read the exact alpha-beta comparator and ordering/theorem premises; coordinate1985/1986/1987 citation occurrences without erasing any original.", "original": {"exact_original_object": {"exact_extracted_citation": "Knuth, D.E. and Moore, R.W., An analysis of alpha-beta pruning, Artificial Intelligence 6(4) \n(1975) 293-326.", "locator": "printed p.199 / PDF p.15, reference16", "number": 16, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status": "Retained bibliography; not automatically a new concept; original not read in this task."}, "index": 15, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "9dcd6260bcec3cdcabcadff0c09c4a5ac971103ac8f4b46db4b3325f7fba5009", "pointer": "/journal_references/15"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The current source-scoped INS record retains the incomplete helper/storage contract. Reading1985 exposes an explicit last-successor guard but does not resolve merit initialization, cache lifetime or all terminal conventions.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Seek exact author code/full report and compare both printed listings without silently repairing either.", "original": {"exact_original_object": {"id": "INS-STORAGE-INTERFACE", "locators": ["pp.190–191", "author rendering PDF7–8"], "question": "Inspect author code/report for exact merit population, GetInfo/SaveInfo behavior, final-successor guard, cache misses and terminal conventions; preserve the journal display without silent repair.", "status": "pending_source_clarification"}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "367bf24b013490cf76d77cc041458b2c8104d3fd586ae3ff3105b956d9a30188", "pointer": "/source_questions/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The DUAL* record preserves source-local leaf/interior/parity and OPEN/purge qualifications; its addition does not complete every helper or tie interface.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Inspect a complete author implementation or fuller account of node-kind, purge descendant and priority/tie rules.", "original": {"exact_original_object": {"id": "DUAL-CONTROLFLOW-INTERFACE", "locators": ["pp.191–193", "author rendering PDF10"], "question": "Clarify leaf versus interior node tests, retained game-node parity, purge descendant scope, OPEN operations and tie order against the SSS*/dual source lineage.", "status": "pending_source_clarification"}, "index": 1, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "3bd540af87392919f409d047709e9b870d2fba3c4fe82708042d5f8257dc25fc", "pointer": "/source_questions/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The original PNS-1985 question is now partly answered: the official four-page source has been fully read and source-specific PNS is proposed separately. The exact historical pending_original_reading object stays unchanged; the ijcai1985 historical link carries representation. Retention, storage, version and global-lineage questions remain.", "disposition": "retained_context", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Follow the nine explicit1985 source questions and the separate PNS link; do not continue to describe the official1985 source as unread.", "original": {"exact_original_object": {"id": "PNS-1985", "question": "Read Information acquisition in minimal window search (IJCAI1985,1040–1043), compare full INS/PNS procedure and source versions before any PNS identity or split.", "reference_numbers": [9], "status": "pending_original_reading"}, "index": 2, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "f0f7c946f02d85a86271faa8e4a6ee94984a5405f8de87f3451275296ae1a070", "pointer": "/source_questions/2"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The original Reinefeld1983/SCOUT/PAB/PVS sources remain pending. Reading the1985 and1987 descriptions alone does not establish global aliases.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Inspect the named originals and exact control-flow/version relationships individually.", "original": {"exact_original_object": {"id": "NEGASCOUT-LINEAGE", "question": "Read Reinefeld1983 and the SCOUT/PAB/PVS source lineage; the journal footnote does not alone establish global aliases or every practical implementation.", "reference_numbers": [2, 3, 4, 5, 7], "status": "pending_original_reading"}, "index": 3, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "7b66a7646bc3c02df972c33f28819751219e596cf8dacfc9f8d83e072f3ee615", "pointer": "/source_questions/3"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The parallel dual-ss* lineage is distinct from the selected sequential DUAL* scope and remains uninspected.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Read Kumar–Kanal1984 and compare MAX-root orientation, parallel scheduling and purge/state conventions.", "original": {"exact_original_object": {"id": "DUAL-SS-LINEAGE", "question": "Read Kumar–Kanal1984 parallel dual-ss* source, distinguish parallel formulation from this sequential MAX-rooted use; similarity is not a completed identity decision.", "reference_numbers": [13], "status": "pending_original_reading"}, "index": 4, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "5ee363e5b770c68aba17d326cb5b5aaac291ebfe56145fd5dacceb0612422d23", "pointer": "/source_questions/4"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The shared main911 ledger already retains original SSS* and alpha-beta comparison sources. ITERSSS* is a separate memory-controlled algorithm, while Minimin is single-agent; neither closes this comparison question.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group": "journal1987", "kind": "source_questions", "next_check": "Read each named primary original and preserve fixed-order, score, memory and implementation assumptions before any identity or dominance claim.", "original": {"exact_original_object": {"id": "SSS-COMPARISON", "question": "Preserve SSS*, alpha-beta and their theoretical comparisons as primary-source questions; do not collapse DUAL* into SSS* or Minimin.", "reference_numbers": [1, 6, 8, 14, 15, 16], "status": "pending_original_reading"}, "index": 5, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "fca7f5909a8f4850fc964aaf970961cb7ed28afb69fe44435515a1d1dad5c482", "pointer": "/source_questions/5"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The TR85-16 cover/title/page-count discrepancy remains unresolved and is not repaired by the new1985 proceedings reading.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Acquire or trace the original report and compare full text against the19-page rendering and1987 reproduction.", "original": {"exact_original_object": {"id": "TR85-16-VERSION", "question": "Inspect the linked19-page rendering titled Is Best First Search Really Best? (cover re-created22March2013 from2November1985 files). Author index calls report TR85-16 Is Best First Search Best?, October1985,27pages. Treat this as a source/version discrepancy to trace, not an identical original27-page byte artifact.", "reference_numbers": [12], "status": "cover_only_route_read_full_text_pending", "url": "https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR85-16.pdf"}, "index": 6, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "f8bf15125a920e5112389ff616b42ea8877bcb7a3a4cb91ee3b40f943a663d6e", "pointer": "/source_questions/6"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The new records make no reproduced timing claim. Deferred dissertation/thesis/report details and their differing cost models remain pending.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Inspect references10–12 for exact generator, score range, sample protocol, implementation and timing denominators.", "original": {"exact_original_object": {"id": "EXPERIMENTAL-PROVENANCE", "question": "Inspect the1986 thesis and report for tree generator, integer range, ordering, timing setup and overhead definitions before any stronger performance claim or benchmark reproduction.", "reference_numbers": [10, 11, 12], "status": "pending_original_reading"}, "index": 7, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "02ec15c55d2094ef20f3177adb2867f08d7868a2fa89e9bfbaa24b477b09606f", "pointer": "/source_questions/7"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Only selected regions of the18-page author rendering were compared with the full15-page journal reproduction; complete textual/mathematical equivalence remains unestablished.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check": "Compare every section before using the alternate rendering as an equivalent full defining artifact.", "original": {"exact_original_object": {"artifacts": [{"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf", "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/author-revised-rendering.pdf", "sha256": "3f297ccc3530ddde68cc1095cf1d97fa07fd9bea57f8b084eb960ad992580b87"}], "id": "AUTHOR-VERSION-COMPARISON", "question": "Compare all journal and author-rendering sections if their provenance is used beyond the selected cover/Figure3/Figure4 correspondence; partial matching does not establish complete textual or mathematical equivalence.", "status": "pending_complete_version_comparison"}, "index": 8, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "e57b9e3d4127513576546c49b4685e64c8ecf4f1edea4157e622d9944ce3e02d", "pointer": "/source_questions/8"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The dual-cope-ijcai-2025 filename is an unread retrieval lead, not evidence for DUAL* identity or a related algorithm. Responsibility is newly attached to the existing main911 source umbrella for inspection.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "incidental_retrieval_contexts", "next_check": "Acquire the exact URL, verify title/version and read the method before any identity comparison; retain original source_catalog pointer63.", "original": {"exact_original_object": {"assessment": "A filename token is not a method identity. No equation, full paper or owner allocation is inferred; retain outside the selected1987 scope.", "exact_original_object": "https://www.cs.unh.edu/~ruml/papers/dual-cope-ijcai-2025.pdf", "group": 644, "pointer": "/source_catalog/pdf_links/63", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json", "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}, "status": "unassessed historical author-index retrieval context"}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/additional-source-context.json", "sha256": "29639a1ee0016588dc9b098ac97fc19171fe2c15274536f9d1da75f6ef2efb6c"}, "original_object_sha256": "6384fa88e0525401f70af5a4b48352cb89c48cf8deb6a60e07cee93889ce4fb9", "pointer": "/incidental_retrieval_contexts/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The ICAPS04 pns filename is an unread route. The pair incidental wrapper and PNS additional_context_questions[0] are the same URL/pointer, retained as two historical occurrences of one coordinated retrieval question.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind": "incidental_retrieval_contexts", "next_check": "Acquire the exact author PDF and determine its PNS expansion before any method/identity claim; coordinate the two wrappers under main911.", "original": {"exact_original_object": {"assessment": "A filename token is not a method identity. No equation, full paper or owner allocation is inferred; retain outside the selected1987 scope.", "exact_original_object": "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf", "group": 645, "pointer": "/source_catalog/pdf_links/87", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json", "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}, "status": "unassessed historical author-index retrieval context"}, "index": 1, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/additional-source-context.json", "sha256": "29639a1ee0016588dc9b098ac97fc19171fe2c15274536f9d1da75f6ef2efb6c"}, "original_object_sha256": "62ca6aee107b9685810dd72f3f2ab64d00d2f87272f239927c6aab204e55c9ad", "pointer": "/incidental_retrieval_contexts/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1981 Fishburn Technical Report431 is distinct from the1984 book cited by the1987 work.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read this exact report and compare the book only after access; preserve separate versions and publication metadata.", "original": {"exact_original_object": {"authors_as_read": "J.P. Fishburn", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry1", "number": 1, "publication_reading": "University of Wisconsin Technical Report431, Madison, May1981", "qualification": "Distinct report reference; do not substitute the1984 book cited in1987.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "Analysis of speedup in distributed algorithms"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "a3ce356df322beee360c80047a52beb3f64397605dd7f4e7b01b1b57aeb76fbb", "pointer": "/bibliography/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The Knuth–Moore alpha-beta original shares the explicit main911 source responsibility already present in ITERSSS* and the1987 bibliography.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group": "ijcai1985", "kind": "bibliography", "next_check": "Inspect its exact algorithm/order/proof assumptions; coordinate all citation occurrences without treating Minimin alpha pruning as the same method.", "original": {"exact_original_object": {"authors_as_read": "D.E. Knuth and W. Moore", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry2", "number": 2, "publication_reading": "Artificial Intelligence6 (1975),293–326", "qualification": "Original not read in this task.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "An analysis of alpha-beta pruning"}, "index": 1, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "510766742f162452d804b4573bf171e90de4663a41eef517af3124c45aeb94e2", "pointer": "/bibliography/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Pearl1980 minimax-tree analysis matches the1987 citation family but is still an uninspected original, distinct from Pearl1984 book context.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read the original and its stated assumptions; coordinate1985 and1987 occurrences while retaining both exact citations.", "original": {"exact_original_object": {"authors_as_read": "J. Pearl", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry3", "number": 3, "publication_reading": "Artificial Intelligence14 (1980),113–138", "qualification": "Original not read in this task.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "Asymptotic properties of minimax trees and game searching procedures"}, "index": 2, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "a33784cfca3ccb574e7a8af6caf993eb2ed833eab06e29c71aa822b018aeaaf2", "pointer": "/bibliography/2"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The parallel strongly ordered game-tree article remains pending; the reconstructed1985 issue/year fields require verification against its original.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read the original source and reconcile bibliographic reconstruction with1987 reference4; do not silently normalize ambiguous fields.", "original": {"exact_original_object": {"authors_as_read": "T.A. Marsland and M.S. Campbell", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry4", "number": 4, "publication_reading": "ACM Computing Surveys14, issue/year characters require verification; pages533–552", "qualification": "Selected reconstructed artifact issue field differs visually from1987 reference; no correction silently asserted.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "Parallel search of strongly ordered game trees"}, "index": 3, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "5598efd743e0ea239eb3c53ebe78fb5f0976e319d1749a221ae2f529cdc71be2", "pointer": "/bibliography/3"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The original Reinefeld Scout improvement remains pending; the selected1985 reconstruction has uncertain issue/page characters.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read the exact1983 source and verify bibliographic fields before asserting NegaScout/PVS equivalence.", "original": {"exact_original_object": {"authors_as_read": "A. Reinefeld", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry5", "number": 5, "publication_reading": "ICCA Journal6 (1983); issue/page rendering unclear", "qualification": "Selected artifact renders title/issue/page characters inconsistently; normalized Scout context is attributed, exact original image retained.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "An improvement of the Scout tree search algorithm"}, "index": 4, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "6df363489669144f71df3b9d6c42c6f720d3ef8152000a7cbea64dd0128f2d0c", "pointer": "/bibliography/4"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Stockman SSS* already has main911 pending responsibility. The new PNS/INS/DUAL* and existing ITERSSS* procedures do not absorb its defining scope.", "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group": "ijcai1985", "kind": "bibliography", "next_check": "Inspect original SSS* and coordinate1985/1986/1987 citation occurrences while retaining each source object.", "original": {"exact_original_object": {"authors_as_read": "G.C. Stockman", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry6", "number": 6, "publication_reading": "Artificial Intelligence12,2 (1979),179–196", "qualification": "Original not read in this task.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "A minimax algorithm better than alpha-beta"}, "index": 5, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "ecd814b8f6d7b9213b5eff343a93fea6ace56b8a8d0fbc1070050b20190e8114", "pointer": "/bibliography/5"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1983 minimax comparison is the same citation family as1987 reference6 but remains a separate uninspected source.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read exact comparators, score/order assumptions and empirical setup before any cross-paper performance conclusion.", "original": {"exact_original_object": {"authors_as_read": "M. Campbell and T.A. Marsland", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator": "p1043 References, entry7", "number": 7, "publication_reading": "Artificial Intelligence20 (1983),347–367", "qualification": "Original not read in this task.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection", "title_reading": "A comparison of minimax tree search algorithms"}, "index": 6, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "cd078500a8476c7bf2e2f0da2900f04b5151535d730df772bc3660b7fdf3a88d", "pointer": "/bibliography/6"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1985 near-root/subtree description and1987 first-level wording are preserved as source/version scope. Full1985 reading does not determine an unspecified general fixed retention depth.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Seek an explicit PNS listing or author clarification of near-root retention across subtrees and versions.", "original": {"exact_original_object": {"current_owner": null, "id": "PNS-RETENTION-DEPTH", "locator": "p1041 Section3;1987p190", "question": "Clarify near-root prove-best retention for each subtree versus1987 first-level wording; do not assume an unspecified fixed depth.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "194dd2c01e2f3e0837f5560510ae2d9ddc556d87c295d5e67180dd74e85acdc2", "pointer": "/additional_questions/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1985 appendix specifies INS, not a full PNS implementation. The new PNS record deliberately leaves PV/bound retention and cache policy incomplete.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Find a primary PNS listing or author implementation for PV updates, bound validity, eviction and lifetime.", "original": {"exact_original_object": {"current_owner": null, "id": "PNS-PV-AND-BOUND-INTERFACE", "locator": "p1041 Section3; p1043 Appendix", "question": "Find a full PNS listing or author implementation defining PV retention, update, bound validity, eviction and cache lifetime. The1985 appendix is INS only.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 1, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "b77523e0805467596b6467d1afedd80301da6982c7f600bce381b75becfccf70", "pointer": "/additional_questions/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Both source displays have now been inspected:1985 has the explicit i&lt;w guard, while1987 expresses the last-successor exclusion in a comment and adds a kind assignment. This observed difference does not certify executable/version equivalence.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Preserve the exact two listings and inspect author implementation/version history before executable claims.", "original": {"exact_original_object": {"current_owner": null, "id": "INS-1985-1987-DISPLAY", "locator": "p1043 Appendix;1987Figure3p191", "question": "Retain explicit1985 i&lt;w guard and1987 comment-only guard plus the additional kind assignment; assess implementation/version correspondence before executable claims.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 2, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "ee54367185a8749b4dbbbc08c39e4532045ec63e193f78844719adb3c62db478", "pointer": "/additional_questions/2"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Reading both sources leaves GetInfo/SaveInfo/Sort and initial merit population delegated or incomplete.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Seek exact storage and cache-miss conventions; do not patch either source silently.", "original": {"exact_original_object": {"current_owner": null, "id": "INS-SCORE-STORAGE", "locator": "p1043 Appendix;1987pp190–191", "question": "Resolve delegated GetInfo/SaveInfo/Sort and invisible initial score population, including cache misses and lifetime, without patching either source silently.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 3, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "79d48bec3db245ab4c8170c581058c8ccb9045ee03dc678d9062bd2afccd135a", "pointer": "/additional_questions/3"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The exact storage summation remains limited by reconstructed artifact clarity; the native PNS record makes no exact total-memory guarantee from it.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Acquire a clearer original scan before asserting exponent/index bounds or total implementation memory.", "original": {"exact_original_object": {"current_owner": null, "id": "INS-STORAGE-FORMULA-ARTIFACT", "locator": "p1041 Section3", "question": "Acquire a clearer original scan for the p1041 storage summation before claiming its exact exponent, index bounds or a total-memory guarantee.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 4, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "f4059c75601202310b571d5d10e0884249f2bc465daf606e357b1751a644b272", "pointer": "/additional_questions/4"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1985 and1987 timing descriptions use different denominators/context; no numeric synthesis follows from their joint reading.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Trace original implementation and timing definitions before comparing or combining results.", "original": {"exact_original_object": {"current_owner": null, "id": "TIMING-VERSION-COST-MODEL", "locator": "p1042 Section4–5;1987p198", "question": "Trace the differing1985/1987 timing denominators and implementation cost models before any numeric performance synthesis.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 5, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "3253f5ef8a0b970b73b135bb94ebff099259e6033ee0325e143574812d54c543", "pointer": "/additional_questions/5"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The1981 Fishburn report and1984 book remain separate source-version questions.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Inspect both originals and establish relevant minimal-window lineage rather than equating matching titles.", "original": {"exact_original_object": {"current_owner": null, "id": "FISHBURN-REPORT-BOOK", "locator": "p1043 reference1;1987p199reference3", "question": "Inspect1981 Technical Report431 separately from the1984 book cited by1987; determine relevant minimal-window provenance.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 6, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "499e8b2a2058d6ca85eef32163d3c59ac7ef68689ae52deb3b3537b16589cd45", "pointer": "/additional_questions/6"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Ambiguous reconstruction in1985 references4/5 remains a bibliographic verification question despite the1987 cross-reference context.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Verify the exact originals/images and record any correction explicitly; retain the original extracted objects.", "original": {"exact_original_object": {"current_owner": null, "id": "BIBLIOGRAPHIC-RECONSTRUCTION", "locator": "p1043 References; PDFmetadata", "question": "Verify reference4/5 issue/page/title fields against original bibliographies because the selected official ABBYY artifact has ambiguous reconstructed characters.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 7, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "b7fd6acb8dbbf53f76545a1f142975665eb9366f8db4916e9795b7f99b310272", "pointer": "/additional_questions/7"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The requested current identity/owner comparison has been performed for this exact362 collection: no normalized candidate collision, all328 matching contents read and current native/AIO contexts compared. This is bounded current evidence, not global novelty or proof-number-search equivalence.", "disposition": "retained_context", "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Recheck identity at any changed write base; keep the independent proof-number and PNMCTS source questions pending.", "original": {"exact_original_object": {"current_owner": null, "id": "PNS-CURRENT-IDENTITY", "locator": "Current research recommendation only; no new search performed", "question": "Run future ignored-inclusive record/frontier/AIO reconciliation for source-specific Partially Informed NegaScout, distinguishing INS, NS/PVS and unrelated PNS expansions.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_source_or_current_identity_inspection"}, "index": 8, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "62b0f8a65706f023a4e4cf5be0344cae208e4d8fbb8816faf8f79974b8eac57a", "pointer": "/additional_questions/8"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "This is the same ICAPS04 URL/pointer as journal1987 incidental_retrieval_contexts[1], with a different historical wrapper. Both occurrences remain exact; source identity is unestablished.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "additional_context_questions", "next_check": "Coordinate one retrieval/primary-method inspection under main911 and determine the actual PNS expansion before relation claims.", "original": {"exact_original_object": {"exact_url": "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf", "future_owner": null, "next_check": "Acquire exact author-hosted PDF, verify title/version and which expansion of pns it uses; compare current identities only after method reading.", "origin": {"pointer": "/source_catalog/pdf_links/87", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json", "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}}, "question_id": "PNS-IDX-ICAPS04", "status": "pending_original_retrieval"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json", "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256": "a8b26fae214ca33ed5e0bfc82a3cda932e6e976a8a0cdca2d59fa87234f327f9", "pointer": "/questions/0"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Allis–van der Meulen–van den Herik1994 Proof-number search is an independent PNS expansion known here only from metadata. It is not Partially Informed NegaScout.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "additional_context_questions", "next_check": "Preserve the publisher403 route and obtain accessible full primary text before method/identity curation.", "original": {"exact_original_object": {"authors": ["L.V. Allis", "M. van der Meulen", "H.J. van den Herik"], "future_owner": null, "next_check": "Find accessible primary full text and assess defining proof/disproof mechanism before any record or identity decision. Preserve publisher403 route.", "origin": {"path": "/private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json", "sha256": "da8749d9822c729ba4f738166200878ee5722b5ae3b9bb79e5e8dd647fecb701"}, "publication": "Artificial Intelligence66(1),91–124,1994", "question_id": "PNS-ACRONYM-PROOF1994", "status": "metadata_only_primary_fulltext_pending", "title": "Proof-number search"}, "index": 1, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json", "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256": "9679f5c773397a0fcb424a2f9b73667f10a5ef6d2c19abf71adef6549903b279", "pointer": "/questions/1"}, "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The2022 proof-number/MCTS hybrid is a separate abstract-level primary lead, not evidence for this1985 PNS mechanism.", "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "additional_context_questions", "next_check": "Read the full primary method and bibliography before any new record or equivalence decision.", "original": {"exact_original_object": {"future_owner": null, "next_check": "Read full primary method and source bibliography if this distinct hybrid is considered for discovery. The present task uses only acronym evidence.", "origin": {"path": "/private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json", "sha256": "da8749d9822c729ba4f738166200878ee5722b5ae3b9bb79e5e8dd647fecb701"}, "question_id": "PNS-ACRONYM-PNMCTS2022", "status": "abstract_only_primary_fulltext_pending", "title": "Combining Monte-Carlo Tree Search with Proof-Number Search", "version": "arXiv:2206.03965v1"}, "index": 2, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json", "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256": "20239e6c1faec3ac4c0bea96920436390c299dd94b405eac067d844ce497dcb3", "pointer": "/questions/2"}, "responsible_owner": {"family": "main", "index": 911}}
- Historical responsibility link journal1987: {"added_record_ids": ["AIMech:InformedNegaScout", "AIMech:DUALStar"], "assessment": "The exact Low overhead alternatives to SSS* reference7 inherited from the1989 MA*/MAO* bibliography is represented by two distinct source-scoped records: INS and DUAL*. The full15-page1987 reproduction has been read. Main911 is the existing source responsibility, not a claim that these algorithms equal MA*/MAO*, ITERSSS* or each other.", "disposition": "represented_by_added_record", "existing_record_ids": [], "next_check": "Retain all16 bibliography,9 source questions and2 incidental retrieval objects, together with independent1985/version/helper/lineage scopes; no source-family exhaustion or issue closure.", "original": {"exact_original_object": {"authors": "T. A. Marsland; A. Reinefeld; J. Schaeffer", "future_owner": null, "next_check": "Game-tree restricted-memory variants; original not freshly acquired/read.", "publication": "Artificial Intelligence31,185–199,1987", "reference_number": 7, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Low overhead alternatives to SSS*"}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256": "12cd5640826b81734e4485f8d19bee015282545f694ef2d6681326f3de45192f", "pointer": "/exact_original_pointer_object/exact_original_object"}, "responsible_owner": {"family": "main", "index": 911}}
- Historical responsibility link ijcai1985: {"added_record_ids": ["AIMech:PartiallyInformedNegaScout"], "assessment": "The exact PNS-1985 original-reading question, also retained once as a1987 source-question occurrence, is represented by the separately defined1985 Partially Informed NegaScout record following full official-paper reading. This is source-specific representation, not complete implementation/version resolution or a proof-number-search alias.", "disposition": "represented_by_added_record", "existing_record_ids": [], "next_check": "Retain all7 bibliography,9 source questions and3 additional context objects, including retention-depth, storage, score, timing and acronym boundaries. Preserve historical pending status only inside the exact original object.", "original": {"exact_original_object": {"id": "PNS-1985", "question": "Read Information acquisition in minimal window search (IJCAI1985,1040–1043), compare full INS/PNS procedure and source versions before any PNS identity or split.", "reference_numbers": [9], "status": "pending_original_reading"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json", "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256": "f0f7c946f02d85a86271faa8e4a6ee94984a5405f8de87f3451275296ae1a070", "pointer": "/original_PNS1985_question"}, "responsible_owner": {"family": "main", "index": 911}}
- The exact full actual361 projection remains recursively accessible once under predecessor_state/projection, including its165 original objects,3 later access questions and2 restored tracking questions. Earlier402/404/406,356/357/358/359 obligations and360 scan-manifest bytes/all100 asset metadata objects remain inherited. No source exhaustion or issue closure is asserted here.
- Inherited predecessor_state: exact object SHA256 b5bf2ccc458a00299fcec5f2bd9818a36fd3cb4be7d026364c12b24f4bf07bf8; original references remain under predecessor_state/projection/predecessor_state.
- Inherited predecessor_state_sha256: exact object SHA256 8c3a464bcd3931025ca1ba4143c43bd408da7812eb3c4bee3a3d0146746d0957; original references remain under predecessor_state/projection/predecessor_state_sha256.
- Inherited source_accounting: exact object SHA256 3ccb5df1a0fbf065471fa12c35f8b16b8dbbb700b3ab99c7039a93dd691d9fbc; original references remain under predecessor_state/projection/source_accounting.
- Inherited frontier_result: exact object SHA256 88dc2e869fa9dad355e204ef421f1bf74e7a65082c69cc6d323d3dff7066849d; original references remain under predecessor_state/projection/frontier_result.
- Approved access-attribution correction (issue415 tracking; no research closure): {"accepted_root_ref": {"path": "/private/tmp/aimech-cohort362-wording-correction-20261016/root-accepted-correction.json", "sha256": "bda7c17e335fe6a5ae8b852e620076a0f01c4c973de707c3edf2311fc29111d9"}, "exact_accepted_correction": {"accepted": true, "after": "The paper’s PNS stores relevant upper bounds only at the first level, and its footnote discusses NegaScout/PVS lineage. Those descriptions do not by themselves establish PNS as this full INS procedure, global PVS aliases, or equivalence to all later implementations. The 1985 original has been read separately; its version differences and the other cited lineage questions remain separately tracked.", "assessment": "Root freshly read all three selected definitions,16 claims and28 limitations and identified a stale present-tense access claim. Sibling356 independently confirmed the exact defect in conversation. The earlier complete1985 paper reading remains attributed to the accepted PNS scientific/native lineage. This correction updates access attribution only, preserving the unresolved1985/1987 version correspondence and other cited lineage questions. No source exhaustion or algorithm defect is asserted.", "before": "The paper’s PNS stores relevant upper bounds only at the first level, and its footnote discusses NegaScout/PVS lineage. Those descriptions do not by themselves establish PNS as this full INS procedure, global PVS aliases, or equivalence to all later implementations; the cited originals remain pending.", "evidence": [{"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json", "sha256": "c1ff1a62918393a360054de311f191f0879b68efed2baaf659b3ee61a169de77"}, {"path": "/private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json", "sha256": "9c653872bbea06f7c5754085da863c43a4ad8382952e2480daa698034a223579"}], "field": "limitations", "historical_preview": {"path": "/private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.native-preview.json", "sha256": "732d869fc587033b0b23ca9616c326433b9dde75ad08df3082c0e7b942443aaa"}, "index": 7, "issue": "https://github.com/CultureBotAI/AIMech/issues/415", "path": "data/curated/InformedNegaScout.yaml", "record_id": "AIMech:InformedNegaScout", "recorded_at": "2026-10-16T06:03:07.166585Z", "scope": "Only this precise limitation string may change from the accepted historical scientific payload; separately required current identity_notes and actual curation time remain permitted."}}
- Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "changed_main_indexes": [911], "changed_nested_indexes": [], "historical_source_responsibility_links": 2, "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_source_objects": 46, "source_object_counts": {"ijcai1985": {"additional_context_questions": 3, "bibliography": 7, "source_questions": 9}, "journal1987": {"bibliography": 16, "incidental_retrieval_contexts": 2, "source_questions": 9}}}
- Actual source accounting digest (sorted compact JSON UTF-8): 095ee33fb7187ebb148606e6dd5e71040816932d169efa926315819fd2bdcfdd
- Actual historical/current identity changes: [{"id": "AIMech:InformedNegaScout", "field": "identity_notes", "historical": "This proposal selects the1987 recursively informed NegaScout procedure: retained ignore-left regions and successor upper bounds influence later re-search. It does not collapse PNS, baseline NegaScout, Principal Variation Search, generic alpha-beta or all later INS implementations. The1985 official paper is an additional version question under separate review. Bare INS is source-local and omitted from global aliases. At the historical04:51–04:52UTC branch360 snapshot, all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive roots supplied749 distinct matching contents. The reading covers747 full contents plus all matching leaves in two large wrappers. This is prospective historical evidence, not future current-state clearance.", "current": "Current prewrite comparison at merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f on 2026-10-16 compared 1,246 records (804 native, 442 pinned AIO), 4,937 identity-field occurrences and 3,774 normalized values. Candidate identity collisions were empty; ITERSSS* was the sole normalized context match. Four explicit roots were searched with ignored and hidden files included, using literal source/name probes and separate word-bounded INS/PNS context probes. The 328 distinct complete matching contents were semantically reviewed, and all 602 occurrence references were mechanically reconstructed; the successor collection preserved their exact line multisets. This record selects the 1987 complete-information NegaScout procedure with recursive retained bounds and ignore-left/prove-best control. It remains distinct from the separately defined 1985 partial-information policy, baseline NegaScout/PVS, DUAL*, SSS* and memory-controlled ITERSSS*. INS is source-local and is not a global alias. The 1985 source has now been read separately; its correspondence to the 1987 helper/storage/retention descriptions and the other original lineage sources remain tracked. Main911 carries the existing source responsibility while retaining all earlier records and unresolved questions. The pinned 30-target AIO no-match assessment is retained with its historical reading scope; current identity clearance is bounded to the inspected corpus and explicit search roots, not global novelty.", "root_decision": "records/AIMech:InformedNegaScout/identity_notes"}, {"id": "AIMech:DUALStar", "field": "identity_notes", "historical": "This proposal selects the1987 MAX-rooted dual-of-SSS* procedure with LIVE/SOLVED descriptors, maximum merit, increasing OPEN order and dual MAX/MIN transitions. It is distinct from INS, SSS*, generic mathematical duality and Hamiltonian dual averaging. The earlier parallel dual-ss* citation is lineage to inspect, not an exact alias. Bare DUAL is omitted; the literal name keeps its star. At the historical04:51–04:52UTC branch360 snapshot, all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive roots supplied749 distinct matching contents. The reading covers747 full contents plus all matching leaves in two large wrappers. This is prospective historical evidence, not future current-state clearance.", "current": "Current prewrite comparison at merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f on 2026-10-16 compared 1,246 records (804 native, 442 pinned AIO), 4,937 identity-field occurrences and 3,774 normalized values. Candidate identity collisions were empty; ITERSSS* was the sole normalized context match. Four explicit roots were searched with ignored and hidden files included, using literal source/name probes and separate word-bounded INS/PNS context probes. The 328 distinct complete matching contents were semantically reviewed, and all 602 occurrence references were mechanically reconstructed; the successor collection preserved their exact line multisets. This record selects the 1987 MAX-rooted application of the dual of SSS*, with LIVE/SOLVED descriptors, increasing ordered merit and dual MAX/MIN rules. It is distinct from INS/PNS, SSS*, ITERSSS*, generic duality, dual averaging and the uninspected parallel dual-ss* or RecDual* formulations. Bare DUAL is omitted from aliases. Source-specific node-kind, parity, purge and tie interfaces remain explicit; no hard byte budget or full correctness certification is inferred. Main911 carries source responsibility without merging any of these identities. The pinned 30-target AIO no-match assessment is retained with its historical reading scope; current identity clearance is bounded to the inspected corpus and explicit search roots, not global novelty.", "root_decision": "records/AIMech:DUALStar/identity_notes"}, {"id": "AIMech:PartiallyInformedNegaScout", "field": "identity_notes", "historical": "This record draft denotes the particular partial-information NegaScout policy described in the official 1985 paper: prove-best information near each subtree root and the principal variation from its initial search. It does not identify all partial NegaScout policies, the complete-information 1987 INS procedure, baseline NegaScout, Principal Variation Search, DUAL* or proof-number search. The source-local abbreviation PNS is omitted from global aliases because a separate primary publication explicitly uses PNS for Proof-Number Search. The 1985 near-root-plus-path description and the 1987 first-level upper-bound description remain an unresolved version question. Historical comparison at 05:11–05:12 UTC on 2026-10-16 covered 801 native and 442 pinned AIO records at HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c, with four ignored- and hidden-inclusive search roots. A separate subsequent comparison read the newly added SVPG, Iterative Expansion and ITERSSS* records and current main 911 source context. That bounded supplement does not constitute a new complete inventory or assign PNS a source owner. Full source and evidence limitations remain explicit.", "current": "Current prewrite comparison at merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f on 2026-10-16 compared 1,246 records (804 native, 442 pinned AIO), 4,937 identity-field occurrences and 3,774 normalized values. Candidate identity collisions were empty; ITERSSS* was the sole normalized context match. Four explicit roots were searched with ignored and hidden files included, using literal source/name probes and separate word-bounded INS/PNS context probes. The 328 distinct complete matching contents were semantically reviewed, and all 602 occurrence references were mechanically reconstructed; the successor collection preserved their exact line multisets. This record denotes the particular 1985 partial-information NegaScout policy retaining near-root prove-best information and the initial principal variation. It is distinct from the complete-information 1987 INS, baseline NegaScout/PVS, DUAL*, all possible partial policies and proof-number search. PNS remains omitted from global aliases. The 1985 near-root-plus-path and 1987 first-level descriptions remain an unresolved version/interface question despite completed reading of both selected primary sources. Main911 carries this separate source responsibility; the proof-number/MCTS and ICAPS04 retrieval questions remain pending. The pinned 30-target AIO no-match assessment is retained with its historical reading scope; current identity clearance is bounded to the inspected corpus and explicit search roots, not global novelty.", "root_decision": "records/AIMech:PartiallyInformedNegaScout/identity_notes"}]

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T062825Z-informed-negascout-dual-star-and-partially-informed-negascout
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of informed NegaScout, DUAL* and partially informed
  NegaScout
started_at: '2026-10-16T06:26:30.228559Z'
finished_at: '2026-10-16T06:28:25.096279Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author self-review with separately attributed primary-source,
    current-data and mathematical reviews. Earlier scientific and helper authorship
    is disclosed in those receipts; this is not independent approval of the whole
    workflow.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain informed NegaScout, DUAL* and partially informed NegaScout as three
  source-scoped DRAFT algorithms. Sixteen claims and 28 limitations preserve their
  information-retention, game-tree control and source-interface boundaries. Three
  declared rows identify two defining primary works. One approved INS limitation updates
  separately completed 1985 access attribution; version and other source questions
  remain separately tracked.
source:
  git_revision: b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/GenerativeAdversarialNetwork.yaml
    sha256: 4f5080d92af8eaea513deed39c60679f0eb7a62d03e5be0d0d8d5c966a9a4544
    role: context
  - path: data/aio/GraphConvolutionalPolicyNetwork.yaml
    sha256: c8a6e283e5d6c5ebc59e1db234d174dc3be79dd0f4a30cdb74e6494e65507d79
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/HashingLayer.yaml
    sha256: a54a2804b0fe6dde37475887d0a8fd3ad8e1f1e335af5d0e7a7ec784e359082d
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MaximumLayer.yaml
    sha256: 7e034921f50c25cba46a261fc2f30b638ec7c5129fb150ee8d26373b4a6f3d54
    role: context
  - path: data/aio/MemoryAugmentedLLM.yaml
    sha256: 8727073cb355b965f54a2f0e58997f862f6b734c9143511008c26f9d31a965fd
    role: context
  - path: data/aio/MemoryCellLayer.yaml
    sha256: 290f04d7838e185381b29b22e67f8765de74242d687d23b0ffae2dad9d3f7237
    role: context
  - path: data/aio/MinimumLayer.yaml
    sha256: 4765d394b6b8c98e13ff0babd273d0da05c863cb469bc7f8c33ac35e19c432cd
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/NeuralTuringMachineNetwork.yaml
    sha256: bb483a9f90d767bcae50856c6084f31fe855d510d352419a5130fa4fc036be79
    role: context
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/PolicyLayer.yaml
    sha256: 5bd260a08b56658940d21561cad7ee515e2f031ea860cb040406f102d98252bf
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RandomForest.yaml
    sha256: cfdce4625131a8da239adf1b3957fadbc5433ddc8fc4ac8a3be5fe9018ce66ab
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/RecursiveLLM.yaml
    sha256: f483ebcf26ac7bea6c0ae9aba097e94813654a063cd0bbee3cf3b0c89de29d81
    role: context
  - path: data/aio/RecursiveLanguageModel.yaml
    sha256: 617d0f86964cea89a7259598acad60a111f6044fb10db598f060d42aaaecff02
    role: context
  - path: data/aio/RecursiveNeuralNetwork.yaml
    sha256: fc7949310ee18ab614ad18b837bb4722e694ae86de5e300e841bf555bbcf4ba6
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
  - path: data/curated/ANDORAbstractionSampling.yaml
    sha256: 556f32f65f14c2e5525ec84aa2d40977a03a70353d7ea9982e12b9d509aaccfd
    role: context
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/CART.yaml
    sha256: 7c462535877d208fb47c6e418f7c9bdd0305b51cada89db1388fad19845f0178
    role: context
  - path: data/curated/DUALStar.yaml
    sha256: 4ae9f919aa1dc766422d88c4d1996d672a50fb6f589c2d45a51dec2c5f0ae181
    role: target
  - path: data/curated/DepthFirstIterativeDeepening.yaml
    sha256: 2e01d2da093397d74a7647e624015b8b0f54d14c7420e00d3ded18a576ce605d
    role: context
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/DualAveragingHamiltonianStepSize.yaml
    sha256: f140c7da7a288509d8c6afe961ad0d5f2913c52afad65452fe40cd7adedfb319
    role: context
  - path: data/curated/ID3.yaml
    sha256: 5d0bbbe3eff68ad1b163c763d7b73ea7aa9535851096c5be4ec32b9dc34eab01
    role: context
  - path: data/curated/InformedBacktrackingRepair.yaml
    sha256: d77f6e102a78b4a2d1af288c9c29f26e7182ee071fff40d28323edd8ed533d14
    role: context
  - path: data/curated/InformedNegaScout.yaml
    sha256: 642387b625824662bd044a096940519a30267d52c317fd8d45917a79d102893d
    role: target
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/IterativeThresholdSearch.yaml
    sha256: bd24d2cd8bf58105833b7fde36a5ba43da19e1bb8425ccff2bc8aefe68cc62ac
    role: context
  - path: data/curated/MAOStar.yaml
    sha256: 8856d812fbfad12e40bd79f321cc935ed2166d60dc044bf164cb24328c1f9477
    role: context
  - path: data/curated/MAStar.yaml
    sha256: b92ce9ec4eed5198b58a24d1d256c7287c734a47219c4922dde36aa05640b66c
    role: context
  - path: data/curated/MREC.yaml
    sha256: 0a6b229e7b98ddc60d52843f82f1d344374136f2ff4e870238358dd51e2f785b
    role: context
  - path: data/curated/MiniminAlphaPruning.yaml
    sha256: 505221f4325e60c6de5494ccd0afac193b394c57bf3687d334741327eeb461a3
    role: context
  - path: data/curated/PartiallyInformedNegaScout.yaml
    sha256: ffde7520ece1efaf8c26dc3186f8cd747e6255c369d6755cacb0da2c8cd1281a
    role: target
  - path: data/curated/RealTimeAStar.yaml
    sha256: 4c3378011e027f000c548f4fc56cd67b139c821cc157efe2f1bcf19d6ee3e7d3
    role: context
  - path: data/curated/RealTimeAdaptiveAStar.yaml
    sha256: fd094b4cbc70d64f22498cffa10b5adf4b84b252f2a49cce8faa66d67f5651bc
    role: context
  - path: data/curated/RecursiveBestFirstSearch.yaml
    sha256: 8ec921263592df64c798eed093ffc2b454c5e1c79c915edcb154bef63dbae6ab
    role: context
  - path: data/curated/SimpleRecursiveBestFirstSearch.yaml
    sha256: ed513766e81bbf1801453eb8053bf999bc91666bcbae5bb7fd48f20bc2052c19
    role: context
  - path: data/curated/SimplifiedMemoryBoundedAStar.yaml
    sha256: d4aa8a11ebc00d66ca19371add0b1ea2b10ad674fbc16aa75a33ce4d8424cac6
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
  - path: history/reports/informed-negascout-dual-star-and-partially-informed-negascout/2026-10-16T061701Z-codex-e1a1bb.yaml
    sha256: 37d1d1581e3c770772acc1eb26f48279ed9d9f7b83afb580df3dca737fb49f38
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
  - path: research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.md
    sha256: f4dde02e76eba4c9ec66a125a0a039d6c736929d4cc5bfd3a4888b980283e5c0
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
scope:
  description: Three exact current native records from accepted cohort362 creation;
    all selected claims and limitations assessed. Historical source and neighbor readings
    remain separately attributed.
  selection: Exact AIMech:InformedNegaScout, AIMech:DUALStar, AIMech:PartiallyInformedNegaScout.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  exclusions:
  - target: Baseline NegaScout/PVS, original SSS*, parallel dual-ss* and other PNS
      acronym senses
    reason: Source lineage, common names and conditional relationships do not establish
      aliases.
  - target: Uninspected bibliography methods and unresolved version/storage questions
    reason: Retained source questions are not new concept counts or completed research.
  - target: Whole inherited issues and source families
    reason: Complete predecessor responsibilities must remain queryable; no broad
      closure or saturation is inferred.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: just check
  exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: just vendored-check
  exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: uv run --locked aimech check-source
  exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: just render
  exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: just render-check
  exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - check-diff
evidence:
- evidence_id: ins-dual-accepted-support
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-review-fragments-20261016/accepted-scientific-support.original.json
  locator: records
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact root-accepted source support; original historical author-reading
    statements are attributed and do not assert a fresh primary reread by this fragment
    author.
  snapshot_sha256: 42b5f034b546a207ddc14e9058314ac171497d2304cbae5e7b89d1584ed068c1
- evidence_id: ins-dual-source-roles
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-review-fragments-20261016/source-metadata-and-roles.original.json
  locator: native_evidence_rows
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Two native source rows share the one defining 1987 journal PDF; partially
    read alternate rendering and earlier versions remain separate research context.
  snapshot_sha256: 78062b4331d22b8465189c8b1d663d25b27ebfd587c4ed5587449e0633130776
- evidence_id: ins-dual-original-questions
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-review-fragments-20261016/source-question-continuity.original.json
  locator: journal_references; source_questions; exact_original_pointer_object
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: All sixteen bibliography and nine question objects and the exact original
    responsibility wrapper retained unchanged; no future owner or closure.
  snapshot_sha256: 7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85
- evidence_id: ins-dual-additional-context
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-review-fragments-20261016/additional-source-context.original.json
  locator: incidental_retrieval_contexts; additional_1985_route
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Two exact historical retrieval objects remain separate; the 1985 route
    advances an existing version question and does not add a positive 1987 native
    evidence row.
  snapshot_sha256: 29639a1ee0016588dc9b098ac97fc19171fe2c15274536f9d1da75f6ef2efb6c
- evidence_id: ins-dual-historical-identity
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-identity-mapping-proposal-20261016/proposal.json
  locator: complete prospective proposal
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Historical identity/no-match assessment, with explicit ignored-inclusive
    scope; no current inventory or owner clearance.
  snapshot_sha256: b63a7676e55f8d4ac10de75fc1ed05c9042cf8e2a7d0ad9480182fcd205345a9
  search_scope: 'Historical prospective snapshot on 2026-10-16 at 04:51–04:52 UTC,
    branch goal/discover-ai-concepts-round360, HEAD 3cd85f801666b505b906cedab979423e4f305c40.
    Compared all 801 maintained and 442 pinned AIO identities (1,243 records; 4,927
    identity-field occurrences; 3,766 normalized values). Four fixed-string, case-insensitive,
    word-delimited searches included ignored and hidden files and excluded .git internals:
    10,522 occurrences in 749 distinct contents. Fresh semantic reading covers 747
    complete contents and all matching leaves in two large historical wrappers; unrelated
    wrapper fields were not reread. Read all 30 full candidate AIO nodes and 97 incident
    triples plus 20 maintained native definitions, identity fields, claim statements
    and limitations. This historical scope does not clear any future base or assign
    a source owner.'
- evidence_id: ins-dual-pinned-aio-context
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json
  locator: thirty full nodes and97 incident triples
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Bounded pinned-AIO context previously read in the accepted identity preparation;
    no new all-ontology semantic review.
  snapshot_sha256: ac96ead79e5b0f2ac5dc8d37bfa5168f78869e64fbe5cb6180989e5c8694c550
- evidence_id: ins-dual-root-native-acceptance
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-native-data-preparation-20261016/root-native-data-acceptance.json
  locator: complete static native-data acceptance
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root accepted exact prospective scientific/identity/no-match DATA and separately
    authorized historical TEMP validation.
  snapshot_sha256: 2e92c13b95a42cd3c3f0b27307ef7de3fc0731a523df252c34d3ec6dadd1dc1a
- evidence_id: ins-dual-root-preview-readback
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-native-preview-20261016/root-native-preview-readback.json
  locator: complete root readback
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root accepted exact historical TEMP preview transfer and actual validator
    receipts; this is not a new current repository gate.
  snapshot_sha256: fa785455185d97f5d968531c08147fc6f0844db0af4c2e163727fab5ffb6a00e
- evidence_id: ins-dual-independent-source-review
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-independent-source-audit-20261016/assessment.final.json
  locator: bounded source/control review
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Separate sibling source/control review, with scope and source-reading attribution
    retained; not an implementation certification.
  snapshot_sha256: 2f08b897921948adc5ab2fd5dce20e5ce233fc66747406dea49f6d2ec7361e35
- evidence_id: ins-dual-threshold-disposition
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-independent-source-audit-20261016/finding-disposition.v2.json
  locator: INS threshold finding disposition
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Preserves max(a,alpha) guard precision and fail-low return qualification
    from the accepted correction.
  snapshot_sha256: ed7151efb6f02d1e58b29cfc7aa2cc48b449fb608709a679817035a70a20046b
- evidence_id: ins-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.native-preview.json
  locator: complete accepted TEMP native preview
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact accepted prospective native content with historical curation; no
    actual canonical or future delivery assertion.
  snapshot_sha256: 732d869fc587033b0b23ca9616c326433b9dde75ad08df3082c0e7b942443aaa
- evidence_id: ins-historical-native-validation
  kind: validation
  reference: /private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.validation.json
  locator: complete historical TEMP per-record validation receipt
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Actual earlier TEMP native-schema validation; not a scientific proof, current
    repository gate or permission for canonical insertion.
  snapshot_sha256: 2cd315da895b79a651ec40337ed985c6b04633e8ff03a6d0c3ad0211e48f9d72
- evidence_id: ins-dual-primary-1
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section2, printed p.186 / PDF p.2; Figure3, printed p.191 / PDF p.7
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-2
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections2.2–2.3 and Figure2, printed pp.188–190 / PDF pp.4–6
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-3
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections2.2–2.3 and Figure2, printed pp.188–190 / PDF pp.4–6; Figure3,
    printed p.191 / PDF p.7
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-4
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section2.3, printed p.190 / PDF p.6; Figure3, printed p.191 / PDF p.7
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-5
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure3, printed p.191 / PDF p.7; storage explanation, printed p.190 /
    PDF p.6
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-6
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections4.1.1–4.1.2, printed pp.193–194 / PDF pp.9–10; Figures5–7, printed
    pp.195–197 / PDF pp.11–13
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-7
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections1–2 and Figures3–4, printed pp.186,191–192 / PDF pp.2,7–8; Section4.1,
    printed pp.193–194 / PDF pp.9–10
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-8
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure3, printed p.191 / PDF p.7
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-9
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section2.3, printed p.190 / PDF p.6; Section4 opening, printed p.193 /
    PDF p.9
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-10
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections4.1.1–4.1.2, printed pp.193–194 / PDF pp.9–10; Figures5–7 and Section5,
    printed pp.195–198 / PDF pp.11–14
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-11
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section4 opening, printed p.193 / PDF p.9; Section4.2, printed p.198 /
    PDF p.14; reference12, printed p.199 / PDF p.15
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-12
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section1 and footnote1, printed p.186 / PDF p.2; Section2.3, printed p.190
    / PDF p.6; references2–9, printed p.199 / PDF p.15
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-13
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Journal header, printed p.185 / PDF p.1, and references/dates, printed
    p.199 / PDF p.15; separately retained source-versions-and-roles and TR85-16 question
  accessed_at: '2026-10-16T04:31:29Z'
  support: context_only
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-provenance-1
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-scientific-data-draft-20261016/draft-author-reading.json
  locator: complete source/reading provenance object
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: supports
  summary: Direct provenance for curator access, version and assurance limitations;
    no claim that the primary paper reports this later curation history.
  snapshot_sha256: fee8e007877d1cedbd6acf153b6b1afeb751cfc12170557b99b40b7ddb3589ec
- evidence_id: ins-dual-provenance-2
  kind: record_content
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/source-versions-and-roles.json
  locator: complete source/reading provenance object
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: supports
  summary: Direct provenance for curator access, version and assurance limitations;
    no claim that the primary paper reports this later curation history.
  snapshot_sha256: 956dd7dcdd4c7c0b393dce7aa6b5677af699f996baae5ed1ff26dfc240046d4e
- evidence_id: ins-dual-provenance-3
  kind: record_content
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/bibliography-and-followups.json
  locator: complete source/reading provenance object
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: supports
  summary: Direct provenance for curator access, version and assurance limitations;
    no claim that the primary paper reports this later curation history.
  snapshot_sha256: 92aa6e467a01a0b96f750666d8067cd5152bee817628aff0f663abe815dc8c9c
- evidence_id: ins-dual-primary-14
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections2–5, printed pp.186–198 / PDF pp.2–14; references, printed p.199
    / PDF p.15
  accessed_at: '2026-10-16T04:31:29Z'
  support: context_only
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-15
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections1–2.3, printed pp.186,188–191 / PDF pp.2,4–7
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: dual-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-ins-dual-native-preview-20261016/DUALStar.native-preview.json
  locator: complete accepted TEMP native preview
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact accepted prospective native content with historical curation; no
    actual canonical or future delivery assertion.
  snapshot_sha256: 58dcfd351447511d804a188da9061e92870307139adf42c5e3810a0c6fe80bb2
- evidence_id: dual-historical-native-validation
  kind: validation
  reference: /private/tmp/aimech-ins-dual-native-preview-20261016/DUALStar.validation.json
  locator: complete historical TEMP per-record validation receipt
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Actual earlier TEMP native-schema validation; not a scientific proof, current
    repository gate or permission for canonical insertion.
  snapshot_sha256: c97121d8ed9d2b59f081e0b826990669ca25c14bda546b51f584bd0d36fbea87
- evidence_id: ins-dual-primary-16
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section3, printed pp.191–193 / PDF pp.7–9; Figure4, printed p.192 / PDF
    p.8
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-17
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure4 and surrounding Section3 prose, printed pp.192–193 / PDF pp.8–9
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-18
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure4, printed p.192 / PDF p.8
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-19
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure4, printed p.192 / PDF p.8; purge description, printed p.193 / PDF
    p.9
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-20
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section4 opening, printed p.193 / PDF p.9; Section4.2, printed p.198 /
    PDF p.14
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-21
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections4.1.1–4.2, printed pp.193–198 / PDF pp.9–14; Figures5–7, printed
    pp.195–197 / PDF pp.11–13
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-22
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections1 and3, printed pp.186,191–193 / PDF pp.2,7–9; Section4.1, printed
    pp.193–194 / PDF pp.9–10
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-23
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Figure4 and Section3 continuation, printed pp.192–193 / PDF pp.8–9
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-24
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections4.1.1–4.1.2 and Figures5–7, printed pp.193–197 / PDF pp.9–13; Section5,
    printed p.198 / PDF p.14
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-25
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section3, printed pp.191–193 / PDF pp.7–9; reference13, printed p.199 /
    PDF p.15
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-26
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Sections3–5, printed pp.191–198 / PDF pp.7–14; references, printed p.199
    / PDF p.15
  accessed_at: '2026-10-16T04:31:29Z'
  support: context_only
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: ins-dual-primary-27
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section3 and Figure4, printed pp.191–193 / PDF pp.7–9
  accessed_at: '2026-10-16T04:31:29Z'
  support: supports
  summary: Selected 1987 journal procedure/publication context; prior primary reading
    is attributed. Curator access and assurance statements rely on their separate
    provenance evidence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: pns-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-pns-native-preview-20261016/PartiallyInformedNegaScout.native-preview.json
  locator: complete prospective native preview
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact root-read TEMP preview with actual historical curation. It is not
    a future canonical record.
  snapshot_sha256: 7dd6ee5e8e5436dc8ae9857103e24124f8088ff95d18443bf092c3ce63649376
- evidence_id: pns-accepted-core
  kind: record_content
  reference: /private/tmp/aimech-pns-native-data-preparation-20261016/PartiallyInformedNegaScout.native-core.json
  locator: complete native-shaped core
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Accepted four-claim/eight-limitation DATA with source-scoped identity and
    30-target no-match; this fragment author also authored that science and identity
    work.
  snapshot_sha256: 6e165eeb43caf3ad513aa90423e8b6d38d07687ebc26438911722f3c189f6aa1
- evidence_id: pns-accepted-support
  kind: record_content
  reference: /private/tmp/aimech-pns-scientific-data-draft-20261016/scientific-support.json
  locator: definition, claims and limitations
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact accepted source-support narratives. Original pending metadata remains
    historical; later acceptances are separately bound.
  snapshot_sha256: 343048f4b4fc4eb4d7c98d2634aa69dade07584ad0c9a1cdf75e77b595d8e5dc
- evidence_id: pns-source-roles
  kind: record_content
  reference: /private/tmp/aimech-pns-native-data-preparation-20261016/source-metadata-and-roles.json
  locator: complete metadata and roles
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: 'Derived source-role metadata: 1985 defining artifact; 1987 version context;
    acronym metadata supplies no positive PNS mechanism evidence.'
  snapshot_sha256: cb92e5fce29e2fd0e3398a87036f3cb237ea7c7092a438342c53211e4717ee2d
- evidence_id: pns-original-questions
  kind: record_content
  reference: /private/tmp/aimech-pns-review-fragments-20261016/source-question-continuity.original.json
  locator: bibliography and additional_questions; all original wrapper fields
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Seven original bibliography objects and nine questions, byte-exact with
    historical pending wording.
  snapshot_sha256: 37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4
- evidence_id: pns-extra-questions
  kind: record_content
  reference: /private/tmp/aimech-pns-review-fragments-20261016/additional-context-questions.original.json
  locator: questions[0:3]
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: 'Three separate context-only retrieval questions: author-index PNS PDF,
    1994 Proof-number original, and 2022 PN-MCTS paper. No novelty or owner allocation.'
  snapshot_sha256: 97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3
- evidence_id: pns-identity-proposal
  kind: record_content
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/identity-mapping-proposal.json
  locator: source-specific identity and prospective boundaries
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Accepted historical identity proposal; aliases remain empty and canonical
    owner/base/cohort remain unset.
  snapshot_sha256: 4cce885f0678b44a3707db98ae953b709dab86af37aaaeaf40e3ad9dad41e732
- evidence_id: pns-historical-search
  kind: search
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/collection.json
  locator: counts, normalized probes, scans and search_groups
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Historical collection with exact raw scan provenance; semantic reading
    and supplemental current context are separately attributed.
  snapshot_sha256: 7a3f7c8c63a3b1335bfd0c00af2b2b3ff9376c01109c2d2468eaf6673a12aeab
  search_scope: Historical prospective collection on 2026-10-16 from 05:11:39 to 05:12:47
    UTC, branch goal/discover-ai-concepts-round361, HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c.
    Compared all 1,243 record identities (801 native and 442 pinned AIO; 4,927 field
    occurrences and 3,766 normalized values). All 18 normalized probes, including
    the proposed local ID, were clear. Four ignored- and hidden-inclusive fixed-string,
    case-insensitive, word-delimited searches produced 10 distinct matching contents
    and 14 occurrences; every content and occurrence binding was read. The complete
    identity DATA matched the previously read INS/DUAL snapshot exactly. Fresh semantic
    context covered 114 native identity/definition projections, 12 selected native
    definitions and all their claim statements, 30 complete annotated AIO nodes and
    97 incident triples, and the prospective INS/DUAL drafts. The three actual records
    added afterward were read in a separate bounded supplement; their addition was
    reported to bring native counts to 804. No later whole-inventory clearance, global
    source exhaustion or future ownership is claimed.
- evidence_id: pns-aio-context
  kind: record_content
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/selected-aio-full-nodes-and-edges.json
  locator: 30 complete annotated nodes and 97 incident triples
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Exact pinned AIO context inspected for the bounded no-match proposal; no
    whole-ontology absence theorem.
  snapshot_sha256: 9dde3d5ca30260512beccb8e9a2bb2e04eff65e9cb9e1008a83d5498c433b0aa
- evidence_id: pns-mapping-assessment
  kind: record_content
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/aio-mapping-assessment.json
  locator: all 30 examined targets and rationales
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Full source-specific target rejection reasons; only the declared ActiveLearning
    spacing correction differs in the native DATA.
  snapshot_sha256: 6d85019d434e7cd8fb1a34537435bfeaec2ad4222a49b8ff696f67ebd0c2a49e
- evidence_id: pns-post-snapshot-context
  kind: record_content
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/post-snapshot-context-assessment.json
  locator: three actual record comparisons and current main911 context
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Later SVPG, IE and ITERSSS record context plus one partial source owner.
    This bounded supplement is not a new global identity or owner clearance.
  snapshot_sha256: 02b9d1d28823518c18c612d7a3e7abdc20d29b1c9192e5b57aa480440d5a79a4
- evidence_id: pns-acronym-context
  kind: record_content
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json
  locator: primary abstract and institutional metadata reading scope
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: The 2022 primary abstract explicitly expands Proof-Number Search as PNS.
    The 1994 record is metadata-only; full papers remain unread here and the publisher403
    is retained.
  snapshot_sha256: da8749d9822c729ba4f738166200878ee5722b5ae3b9bb79e5e8dd647fecb701
- evidence_id: pns-root-science
  kind: prior_review
  reference: /private/tmp/aimech-pns-scientific-data-draft-20261016/root-scientific-data-acceptance.json
  locator: accepted scope and immediate-successor interpretation
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root accepted the source-scoped science, including the immediate-successor-branch
    sense of the prove-best statement. This is not a formal saved canonical review.
  snapshot_sha256: de672d1556e471fc1a3058738eae2147a9feea66808debb31aa2f8d9d24d2dcb
- evidence_id: pns-root-identity
  kind: prior_review
  reference: /private/tmp/aimech-pns-identity-mapping-proposal-20261016/root-prospective-identity-acceptance.json
  locator: prospective identity/no-match acceptance
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root accepted prospective identifier/name/empty aliases and 30-target no-match
    with bounded historical reading attribution.
  snapshot_sha256: f158f6e2ac04a49fd032a63db8304698d3c9e36bc7697fd2634b536f686935a0
- evidence_id: pns-root-native-core
  kind: prior_review
  reference: /private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json
  locator: exact native-core acceptance
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root read exact native core, science transfer and metadata; authorizes
    only the separately recorded TEMP preview event.
  snapshot_sha256: c1ff1a62918393a360054de311f191f0879b68efed2baaf659b3ee61a169de77
- evidence_id: pns-root-preview
  kind: prior_review
  reference: /private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json
  locator: actual preview/validation readback
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Root verified exact accepted core plus actual curation; no canonical or
    future ownership acceptance.
  snapshot_sha256: 9c653872bbea06f7c5754085da863c43a4ad8382952e2480daa698034a223579
- evidence_id: pns-independent-science
  kind: prior_review
  reference: /private/tmp/aimech-pns-independent-draft-audit-20261016/assessment.json
  locator: bounded independent source/draft assessment
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Sibling354 read all four 1985 primary images and source DATA; prior source
    reading is attributed, not freshly repeated by this fragment assembly.
  snapshot_sha256: 5f50eec50e7debf3f81732cdc1eb761edcfe7d2a9b2423a072a95e16393ab494
- evidence_id: pns-independent-native
  kind: prior_review
  reference: /private/tmp/aimech-pns-native-data-independent-audit-20261016/assessment.json
  locator: complete independent native DATA review
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Sibling354 checked exact science, source continuity, 30 full AIO nodes/97
    edges and stated neighbor scope; no current runtime clearance.
  snapshot_sha256: 0b4aa75c66f32a9282a217730917a89a444845c2cbfdeeffa1d295ecba014d77
- evidence_id: pns-preview-validation
  kind: validation
  reference: /private/tmp/aimech-pns-native-preview-20261016/PartiallyInformedNegaScout.validation.json
  locator: one actual validate_curated_record invocation, errors[]
  accessed_at: '2026-10-16T06:18:56.817795Z'
  support: context_only
  summary: Historical structural/per-record semantics result only; neither scientific
    certification nor future whole-inventory validation.
  snapshot_sha256: a1e3b0fcb27ac8afec73ab623d98203d7afa751650d029327868d69dc2be4c08
- evidence_id: pns-primary-01
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 2, Figure 3, and Section 3, printed p.1041 / PDF p.2
  accessed_at: '2026-10-16T04:55:30Z'
  support: supports
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-02
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 3, PNS paragraph, printed p.1041 / PDF p.2
  accessed_at: '2026-10-16T04:55:30Z'
  support: supports
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-03
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Introduction, printed p.1040 / PDF p.1; Section 3, printed p.1041 / PDF
    p.2
  accessed_at: '2026-10-16T04:55:30Z'
  support: supports
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-04
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 4 and Figures 4–5, printed p.1042 / PDF p.3
  accessed_at: '2026-10-16T04:55:30Z'
  support: supports
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-05
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 3, printed p.1041 / PDF p.2; Figure 1, printed p.1040 / PDF p.1;
    Appendix heading and listing, printed p.1043 / PDF p.4
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-06
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 2 and Figure 3, printed p.1041 / PDF p.2; Appendix, printed p.1043
    / PDF p.4
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-07
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Introduction and Figure 1, printed p.1040 / PDF p.1; Appendix, printed
    p.1043 / PDF p.4
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-08
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 3, printed p.1041 / PDF p.2; Section 5, printed p.1042 / PDF p.3
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-09
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 3, printed p.1041 / PDF p.2
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-10
  kind: primary_source
  reference: /private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf
  locator: Section 2.3, printed p.190 / PDF p.6
  accessed_at: '2026-10-16T04:31:29Z'
  support: context_only
  summary: Separate 1987 journal primary context for PNS first-level wording; it does
    not define the full 1985 PNS implementation or establish exact version equivalence.
  snapshot_sha256: cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0
- evidence_id: pns-primary-11
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Section 4 and Figures 4–5; conclusion final paragraph, printed p.1042 /
    PDF p.3
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-12
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Sections 4–5, printed p.1042 / PDF p.3
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-13
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Official PDF metadata; complete pp.1040–1043; references, printed p.1043
    / PDF p.4
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-14
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Introduction, printed p.1040 / PDF p.1; Section 3, PNS paragraph, printed
    p.1041 / PDF p.2
  accessed_at: '2026-10-16T04:55:30Z'
  support: supports
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: pns-primary-15
  kind: primary_source
  reference: /private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf
  locator: Complete official-hosted 1985 PDF, printed pp.1040–1043; PNS description
    in Section 3 on p.1041
  accessed_at: '2026-10-16T04:55:30Z'
  support: context_only
  summary: Inspected official-hosted four-page 1985 artifact. Locator supports the
    bounded source interpretation; no executable contract or uninspected reference
    proof is imported.
  snapshot_sha256: 0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-cohort362-write.json
  snapshot_sha256: edaebba5f830994e9f69469e399958ce86f1b6bf9ddbb626ee6b1925045159f7
  accessed_at: '2026-10-16T06:26:45.339026Z'
  support: context_only
  summary: Actual exclusive creation of three native records, report pair and CREATE
    history.
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-capture.json
  snapshot_sha256: 9c9b6a9ee5ca7165b199399bda96f49bfa896b8b2e32354e9fd21641aa27372e
  accessed_at: '2026-10-16T06:26:45.339538Z'
  support: context_only
  summary: Actual canonical input-byte and maintained-target capture.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/root-postcapture-reading.json
  snapshot_sha256: e14a763adaf8b4a5de3206bbe98416eec5ad63e03852731d5bc59359b32945a1
  accessed_at: '2026-10-16T06:26:45.339807Z'
  support: context_only
  summary: Actual root reading of source-scoped canonical records, metadata and all
    retained question objects; historical source reading stays separately attributed.
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort362-governance-20261016/assessment.json
  snapshot_sha256: e9bf36faab9e1e77a81a84c4d16c4688ada3f82dd4a925893d344ee0999207f9
  accessed_at: '2026-10-16T06:26:45.340257Z'
  support: context_only
  summary: Actual byte preservation, dynamic owner-plan reconstruction, inherited
    metadata and parsed-page audit.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort362-governance-20261016/rendered-pages.json
  snapshot_sha256: fd8103e73be285de5f0e20091cb1c91a7fd0c6db27f662660cff9a044ab06ead
  accessed_at: '2026-10-16T06:26:45.340582Z'
  support: context_only
  summary: Actual generated-page bytes and parsed content; no visual/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort362-actual-scientific-audit-20261016/assessment.json
  snapshot_sha256: c299af0544c46bfed65a7009b07bc5e3f6a274875c867750a434828d65de3490
  accessed_at: '2026-10-16T06:26:45.340869Z'
  support: context_only
  summary: Actual record scientific assessment with its own attributed source-reading
    scope.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort362-current-collection-v2-20261016/collection.json
  snapshot_sha256: 98f8ff42df54837ec4d2bd140abeb2d02cd28b0e3d303d7f796a0584fe7e1a39
  accessed_at: '2026-10-16T06:26:45.347550Z'
  support: context_only
  summary: Actual scoped ignored-inclusive identity collection; mechanical capture
    is distinct from human semantic reading.
  search_scope: Four named roots, ignored and hidden files included. 328 complete
    distinct contents semantically read by sibling356;602 occurrence references mechanically
    reconstructed. Root current metadata/collision results/main911/selected longest
    contents plus exact successor multiset correspondence read.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/assessment.current.v2.json
  snapshot_sha256: 76426e7a10bb920dc1077e0506a7a479b93df796d737367c3e2a5c278427e4d3
  accessed_at: '2026-10-16T06:26:45.347872Z'
  support: context_only
  summary: Actual attributed current identity and source-question assessment.
  search_scope: Four named roots, ignored and hidden files included. 328 complete
    distinct contents semantically read by sibling356;602 occurrence references mechanically
    reconstructed. Root current metadata/collision results/main911/selected longest
    contents plus exact successor multiset correspondence read.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort362-current-decisions.v2.json
  snapshot_sha256: e0f2c07c05785e59018010cc5312605017937f6428a8bfc7bfd9e75a86da0292
  accessed_at: '2026-10-16T06:26:45.349965Z'
  support: context_only
  summary: Exact current record identity decisions, dynamic accepted ownership and
    retained source questions.
- evidence_id: ownership-plan
  kind: record_content
  reference: /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/ownership-plan.proposed.v2.json
  snapshot_sha256: 3ebf455f10f0a5eaab9200b751aa8c23c4a0b36ae665c9e783fc26ad01e11e95
  accessed_at: '2026-10-16T06:26:45.350454Z'
  support: context_only
  summary: Two distinct source groups retain 46 original objects and two separate
    historical responsibility links; current additional questions remain explicit.
- evidence_id: ownership-plan-acceptance
  kind: record_content
  reference: /private/tmp/aimech-cohort362-current-ownership-proposal-20261016/root-ownership-acceptance.json
  snapshot_sha256: d031854ae34abfbfc8f9bf0ed94a1c7ebba1e401810b3a7ef1a9d6bafbba98de
  accessed_at: '2026-10-16T06:26:45.350670Z'
  support: context_only
  summary: Actual root acceptance of current source responsibility; no whole-issue
    closure.
- evidence_id: current-discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.json
  snapshot_sha256: ae343443b190b59e9105d5f509b7f623d4bb5cbe48e8d95d0823dd168812fbe3
  accessed_at: '2026-10-16T06:26:45.367508Z'
  support: context_only
  summary: Canonical durable report containing the exact recursively queryable predecessor_state
    bundle and separate current source responsibilities.
- evidence_id: inherited-source-durability
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T061644Z-informed-negascout-dual-star-and-partially-informed-negascout.json
  snapshot_sha256: ae343443b190b59e9105d5f509b7f623d4bb5cbe48e8d95d0823dd168812fbe3
  accessed_at: '2026-10-16T06:26:45.385265Z'
  support: context_only
  summary: The current canonical predecessor bundle preserves actual360 source_durability
    with the reconstructible exact JSON manifest and all 100 original asset metadata/provenance
    objects. This inherited SHA-256 does not identify a publisher PDF.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/informed-negascout-dual-star-and-partially-informed-negascout/2026-10-16T061701Z-codex-e1a1bb.yaml
  snapshot_sha256: 37d1d1581e3c770772acc1eb26f48279ed9d9f7b83afb580df3dca737fb49f38
  accessed_at: '2026-10-16T06:26:45.385622Z'
  support: context_only
  summary: Actual single CREATE event for the report.
- evidence_id: review-support
  kind: record_content
  reference: /private/tmp/aimech-cohort362-review-assembly-preparation-20261016/review-support.prepared.json
  snapshot_sha256: c1791658594075a882ec564928227df3b46b28ee54908841bbb54acb7034dff3
  accessed_at: '2026-10-16T06:26:45.386331Z'
  support: context_only
  summary: Exact historical per-claim and per-limitation narrative support.
- evidence_id: approved-access-attribution-correction
  kind: record_content
  reference: /private/tmp/aimech-cohort362-wording-correction-20261016/root-accepted-correction.json
  snapshot_sha256: bda7c17e335fe6a5ae8b852e620076a0f01c4c973de707c3edf2311fc29111d9
  accessed_at: '2026-10-16T06:26:45.386566Z'
  support: context_only
  summary: Exact root-approved INS limitation8 access-attribution correction, with
    historical before/after and separately completed PNS reading. Issue415 tracks
    the correction; research/version questions remain separate.
- evidence_id: correction-pns-reading-1
  kind: prior_review
  reference: /private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json
  snapshot_sha256: c1ff1a62918393a360054de311f191f0879b68efed2baaf659b3ee61a169de77
  accessed_at: '2026-10-16T06:26:45.386794Z'
  support: context_only
  summary: Attributed accepted PNS source/native reading supporting the access-status
    correction.
- evidence_id: correction-pns-reading-2
  kind: prior_review
  reference: /private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json
  snapshot_sha256: 9c653872bbea06f7c5754085da863c43a4ad8382952e2480daa698034a223579
  accessed_at: '2026-10-16T06:26:45.387012Z'
  support: context_only
  summary: Attributed accepted PNS source/native reading supporting the access-status
    correction.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-gate.json
  snapshot_sha256: a16c2a438a5c44820095049b73ac2e61a3c2181b6b7222a765d0aee4020279e5
  accessed_at: '2026-10-16T06:26:03.966405Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-vendor.json
  snapshot_sha256: 5b4d90076a553cab35dd7724b1226dc63f40f98e58f8c18340b976d0efe7a7e0
  accessed_at: '2026-10-16T06:26:07.184813Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-check-source.json
  snapshot_sha256: 43ec3373b1f99a24423cceba361263afa210dd065d39bc112f021cc531a9815a
  accessed_at: '2026-10-16T06:26:08.945753Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-render.json
  snapshot_sha256: 316d1fe0a2886a4f21c610360f2be4ddf180f5fcc5eb440bd6059638397396b8
  accessed_at: '2026-10-16T06:17:32.996306Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-render-check.json
  snapshot_sha256: cc765c0ab11b1548e8ee636fc992522bdfe4c09deb2962858f5fa86fcc308653
  accessed_at: '2026-10-16T06:26:19.485751Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort362-postwrite-20261016/actual-check-diff.json
  snapshot_sha256: c099f1b400ea782bf8496481faf6832a32692baf82bc40e47e0f33ab05c4f5a4
  accessed_at: '2026-10-16T06:26:19.960723Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
assessments:
- assessment_id: ins-claim-adjacent-window-probes
  area: evidence
  topic: 'Informed NegaScout: adjacent-window-probes'
  outcome: supported
  summary: This combines the Section2 explanation with the actual Figure3 guards,
    including the remembered-PROVEBEST branch. It does not claim every non-cutoff
    failed-high probe is re-searched or that all returned merits are exact values.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-1
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: In the displayed integer-score INS procedure, the first successor uses
    the incoming open window and later initial-search successors use an adjacent-value
    minimal window around the current bound. A failed-high probe may require an opened-window
    re-search; the displayed first-successor, fail-low, beta-cutoff, depth-at-most-two
    and remembered PROVEBEST cases determine when that additional search is avoided.
- assessment_id: ins-claim-ignore-left-information
  area: evidence
  topic: 'Informed NegaScout: ignore-left-information'
  outcome: supported
  summary: The relative depth is measured from the root of the re-search, not an absolute
    universal MIN/MAX parity. The text describes the inferior left region and the
    extreme-merit transformation; no modern implementation equivalence is inferred.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-2
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: INS retains the path information identifying the leftmost terminal variation
    responsible for the initial failure. During a later re-search, previously examined
    inferior siblings to the left of that variation at even relative levels can be
    skipped. The source presents ignore-left pruning as a special case of prove-best
    pruning using remembered extreme merits and successor ordering.
- assessment_id: ins-claim-prove-best-upper-bounds
  area: evidence
  topic: 'Informed NegaScout: prove-best-upper-bounds'
  outcome: supported
  summary: The source stores upper bounds and explicitly tests max(a,alpha), not a
    alone. For the hand values a=2, alpha=5 and next upper bound4, the test succeeds
    and the displayed update returns4, which is still below alpha and can be only
    a fail-low bound. This clarifies the incoming-threshold case without executing
    INS, asserting all values exact, repairing helpers or certifying the complete
    algorithm.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-3
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-threshold-disposition
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: At odd levels relative to a re-search root, INS retains successor upper
    bounds from the initial traversal. It uses them to order successors, stop when
    the larger of the current result a and incoming alpha reaches the next remaining
    upper bound, and narrow later search windows. Figure3 tests max(a,alpha)>=merit[i+1]
    and then sets a=max(a,merit[i+1]); the returned result can remain only a fail-low
    bound. The negamax score orientation and validity of the retained bounds are part
    of this source-scoped interpretation.
- assessment_id: ins-claim-recursive-information-storage
  area: evidence
  topic: 'Informed NegaScout: recursive-information-storage'
  outcome: supported
  summary: The paragraph explicitly distinguishes the information types and the experiments’
    linked storage from the optional hash representation. It does not supply the missing
    merit-population or cache contract, and does not establish a fixed total-memory
    guarantee.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-4
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'The complete-information INS presentation saves information recursively
    throughout the initial search subtree: the relevant successor index at ignore-left
    nodes and returned successor merits at prove-best nodes. SaveInfo and GetInfo
    hide its storage management. The reported experiments use a linked tree retaining
    all this information; the paper separately describes a hash-table option that
    can lose information through conflicts.'
- assessment_id: ins-claim-research-flag-and-unvisited-region
  area: evidence
  topic: 'Informed NegaScout: research-flag-and-unvisited-region'
  outcome: supported
  summary: The two flag variables have visibly different roles. This states the printed
    control flow without silently adding assignments to the merit array or claiming
    executable C semantics.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-5
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Figure3 distinguishes the invocation’s research flag from a mutable resflag.
    A re-search invocation retrieves and sorts remembered successor information; when
    the procedure moves beyond remembered ignore-left information, resflag becomes
    false for subsequent recursive calls. The displayed SaveInfo call is guarded by
    research being false, and the procedure returns its current score or bound.
- assessment_id: ins-claim-reported-comparison-design
  area: evidence
  topic: 'Informed NegaScout: reported-comparison-design'
  outcome: supported
  summary: The claim records the experiment’s design and metric only. The authors
    note sampling variability and the ranking depends on depth parity, ordering and
    width; no plot ordinate or broad superiority is newly asserted.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-6
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The journal compares INS with NS, PNS, SSS* and DUAL* on generated uniform-width,
    fixed-depth trees with random or specified sibling ordering. The plotted terminal-visit
    counts are percentages of a minimal game-tree size, averaged over the same twenty
    sample trees for each displayed setting; they are not wall-clock measurements
    or universal node-dominance guarantees.
- assessment_id: ins-limitation-finite-tree-scope
  area: scope
  topic: 'Informed NegaScout: finite-tree-scope'
  outcome: supported
  summary: Restricts the record to the described abstraction; it does not infer that
    all possible extensions are impossible.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-7
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source-scoped procedure and experiments concern finite, fixed-depth
    alternating game trees, with uniform positive branching in the displays. No general
    cyclic-graph duplicate policy, stochastic-game semantics, quiescence treatment
    or arbitrary early-terminal interface is established.
- assessment_id: ins-limitation-integer-window-and-bounds
  area: scope
  topic: 'Informed NegaScout: integer-window-and-bounds'
  outcome: supported
  summary: The source’s int declarations and a+1 window supply the discrete scope;
    the fail-low/high explanation supplies the bound distinction.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-1
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The adjacent-value window uses integer score units. A failed-window return
    may be a bound rather than an exact minimax value; arbitrary real-valued epsilon
    rules, floating-point tolerances and terminal scoring conventions are not specified.
- assessment_id: ins-limitation-hidden-storage-contract
  area: scope
  topic: 'Informed NegaScout: hidden-storage-contract'
  outcome: supported
  summary: Preserves the documented abstraction and visible omission. No implementation
    fix or failure is asserted from an abbreviated pseudocode display.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-4
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Figure3 delegates storage to SaveInfo/GetInfo and does not visibly populate
    merit with each returned v during the initial loop. Array initialization, value
    capture, cache misses, validity and lifetime therefore remain source-presentation
    questions rather than a complete executable contract or a proved algorithm defect.
- assessment_id: ins-limitation-last-successor-interface
  area: scope
  topic: 'Informed NegaScout: last-successor-interface'
  outcome: supported
  summary: The scientific-draft author’s earlier visual reading confirms both the
    array access and the nearby last-successor comment; exact implementation completion
    remains a follow-up.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-8
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed pseudocode uses one-based successor indices and reads merit[i+1].
    Excluding the i==w case is stated in a comment rather than encoded in that Boolean
    guard. The listing is not directly executable C and must not be silently repaired.
- assessment_id: ins-limitation-storage-budget-boundary
  area: scope
  topic: 'Informed NegaScout: storage-budget-boundary'
  outcome: supported
  summary: The source explicitly separates all-information linked storage from a tunable
    hash option. The limit avoids converting that option into the fixed-memory guarantees
    of different algorithms.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-9
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: A finite hash table can lose remembered information and potential cutoffs;
    the reported full-information experiment instead retains the generated subtree.
    Neither establishes a hard total byte bound including the recursion stack, successor
    arrays, cache policy and allocator overhead.
- assessment_id: ins-limitation-empirical-external-validity
  area: scope
  topic: 'Informed NegaScout: empirical-external-validity'
  outcome: supported
  summary: The source gives contrasting odd/even behavior and notes finite-sample
    uncertainty; the draft does not claim a reproduced benchmark.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-10
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Terminal-count curves are conditional on the supplied tree generator, width,
    depth parity, ordering and twenty shared samples. The paper discusses sampling
    variability; these results do not prove universal dominance over SSS*, DUAL*,
    NS, PNS or alpha-beta.
- assessment_id: ins-limitation-timing-portability
  area: scope
  topic: 'Informed NegaScout: timing-portability'
  outcome: supported
  summary: Keeps cost metrics separate and leaves the technical-report version question
    open.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-11
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Preliminary execution-time and OPEN-management observations describe the
    authors’ implementations, with details deferred to report12. They are not reproduced
    results, hardware-independent speedups or evidence that fewer terminal visits
    always means lower time.
- assessment_id: ins-limitation-neighbor-and-version-identity
  area: scope
  topic: 'Informed NegaScout: neighbor-and-version-identity'
  outcome: supported
  summary: Preserves the source-specific INS/PNS and PVS lineage boundaries while
    distinguishing the separately completed 1985 source reading from unresolved version
    and other cited-lineage questions.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-12
  - ins-accepted-preview
  - ins-dual-accepted-support
  - approved-access-attribution-correction
  - correction-pns-reading-1
  - correction-pns-reading-2
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The paper’s PNS stores relevant upper bounds only at the first level, and
    its footnote discusses NegaScout/PVS lineage. Those descriptions do not by themselves
    establish PNS as this full INS procedure, global PVS aliases, or equivalence to
    all later implementations. The 1985 original has been read separately; its version
    differences and the other cited lineage questions remain separately tracked.
- assessment_id: ins-limitation-artifact-version-scope
  area: scope
  topic: 'Informed NegaScout: artifact-version-scope'
  outcome: supported
  summary: This is a provenance limitation supported by the original acquisition/reading
    ledger in addition to the cited journal pages. The secondary rendering stays research
    context, not an unused native source row. The journal locator contextualizes the
    procedure/publication only; the added provenance refs directly support the present
    reading/version/assurance boundary. No claim that the journal reports this curator’s
    access history is made.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-13
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-provenance-1
  - ins-dual-provenance-2
  - ins-dual-provenance-3
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The defining evidence is the inspected15-page author-hosted1987 journal
    reproduction. The separate18-page author rendering was inspected only in selected
    regions, and the TR85-16 route has a cover/title/page-count discrepancy; neither
    is treated as a wholly equivalent publisher artifact or a fully read independent
    defining source.
- assessment_id: ins-limitation-no-implementation-proof
  area: scope
  topic: 'Informed NegaScout: no-implementation-proof'
  outcome: supported
  summary: An explicit curator assurance boundary, not a claim that the paper or algorithm
    is false. The journal locator contextualizes the procedure/publication only; the
    added provenance refs directly support the present reading/version/assurance boundary.
    No claim that the journal reports this curator’s access history is made.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-14
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-provenance-1
  - ins-dual-provenance-2
  - ins-dual-provenance-3
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The draft records the described pruning and recursion mechanism while retaining
    the abbreviated helper and guard conventions. It does not certify a full correctness
    or node-dominance theorem, execute INS, or import uninspected proofs from SSS*,
    NegaScout or alpha-beta references.
- assessment_id: ins-definition
  area: evidence
  topic: 'Informed NegaScout: defining procedure'
  outcome: supported
  summary: Source-specific procedure definition, limited to the inspected journal
    account. It does not allocate an ontology identity, mapping or alias, certify
    executable pseudocode, or assert a universal performance theorem.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-dual-primary-15
  - ins-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: An adversarial game-tree search procedure that augments NegaScout’s minimal-window
    traversal with recursively retained information from an initial search, using
    remembered inferior left regions and successor upper bounds to guide a later re-search.
- assessment_id: ins-kind
  area: scope
  topic: 'Informed NegaScout: kind'
  outcome: supported
  summary: INS denotes the selected recursive adversarial game-tree search procedure.
    Minimal-window probes and retained information guide re-search; it is an algorithm,
    not a trained model, task, benchmark or hard-memory-budget method.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-primary-15
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The accepted algorithm kind is retained. Integer score units, finite alternating-tree
    abstraction and missing helper contracts limit implementation and theorem claims.
- assessment_id: ins-identity
  area: identity
  topic: 'Informed NegaScout: identity'
  outcome: supported
  summary: Retain the full name Informed NegaScout and empty global aliases for the
    source-specific 1987 complete-information procedure. Bare INS is source-local;
    baseline NegaScout, PNS, Principal Variation Search and later implementations
    are not asserted exact aliases.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-historical-identity
  - ins-dual-root-native-acceptance
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'The accepted historical inventory/search assessment is reused with its
    stated scope. It is not rerun here and cannot establish current noncollision,
    novelty, owner responsibility or a future base. Previously accepted identity notes
    (verbatim historical wording): This proposal selects the1987 recursively informed
    NegaScout procedure: retained ignore-left regions and successor upper bounds influence
    later re-search. It does not collapse PNS, baseline NegaScout, Principal Variation
    Search, generic alpha-beta or all later INS implementations. The1985 official
    paper is an additional version question under separate review. Bare INS is source-local
    and omitted from global aliases. At the historical04:51–04:52UTC branch360 snapshot,
    all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized
    values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive
    roots supplied749 distinct matching contents. The reading covers747 full contents
    plus all matching leaves in two large wrappers. This is prospective historical
    evidence, not future current-state clearance.'
- assessment_id: ins-mapping
  area: grounding
  topic: 'Informed NegaScout: mapping'
  outcome: supported
  summary: Retain the accepted bounded aio_no_match and all thirty rejection reasons.
    Computed minimax bounds, recursive calls, optional hashing and game-tree structure
    do not establish a learning task, neural architecture, language model, classifier
    or neural layer.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-historical-identity
  - ins-dual-root-native-acceptance
  - ins-dual-pinned-aio-context
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'The pinned definitions, synonyms and incident edges belong to the accepted
    prior mapping assessment. No positive exact, broader, narrower or specifically
    related target was selected; this fragment does not claim ontology-wide impossibility
    or a fresh 442-class semantic read. Previously accepted search scope (verbatim
    historical wording): Historical prospective snapshot on 2026-10-16 at 04:51–04:52
    UTC, branch goal/discover-ai-concepts-round360, HEAD 3cd85f801666b505b906cedab979423e4f305c40.
    Compared all 801 maintained and 442 pinned AIO identities (1,243 records; 4,927
    identity-field occurrences; 3,766 normalized values). Four fixed-string, case-insensitive,
    word-delimited searches included ignored and hidden files and excluded .git internals:
    10,522 occurrences in 749 distinct contents. Fresh semantic reading covers 747
    complete contents and all matching leaves in two large historical wrappers; unrelated
    wrapper fields were not reread. Read all 30 full candidate AIO nodes and 97 incident
    triples plus 20 maintained native definitions, identity fields, claim statements
    and limitations. This historical scope does not clear any future base or assign
    a source owner.'
- assessment_id: ins-source
  area: provenance
  topic: 'Informed NegaScout: source'
  outcome: supported
  summary: Both candidate records use the same fifteen-page author-hosted 1987 journal
    reproduction as their sole declared defining artifact. For INS, the positive mechanism
    locators are the minimal-window discussion, ignore-left/prove-best explanation
    and Figure3, with the exact max(a,alpha) guard and potentially fail-low returned
    bound.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-source-roles
  - ins-dual-original-questions
  - ins-dual-additional-context
  - ins-dual-independent-source-review
  - ins-dual-primary-15
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source row, DOI, URL, hash, publication/version qualification and historical
    access time remain exact. Partially inspected alternate rendering, TR85-16 and
    earlier1985 INS/PNS evidence remain separately attributed version questions. Later
    PNS research does not rewrite the historical objects or supply a full1987 helper
    contract.
- assessment_id: ins-boundary
  area: scope
  topic: 'Informed NegaScout: boundary'
  outcome: supported
  summary: Retain full-information INS as distinct from the partial PNS policy and
    the LIVE/SOLVED DUAL* controller. Preserve the source-relative odd/even levels,
    research/resflag distinction, max(a,alpha) threshold and returned-bound qualification;
    do not silently complete merit storage or last-successor guards.
  target_ids:
  - AIMech:InformedNegaScout
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-source-roles
  - ins-dual-original-questions
  - ins-dual-additional-context
  - ins-dual-independent-source-review
  - ins-dual-primary-15
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Six claims and ten limitations are copied from the accepted preview. Generated-tree
    terminal-count comparisons remain separate from implementation timing; no universal
    dominance, executable correctness, hard byte limit or uninspected predecessor
    theorem is certified.
- assessment_id: dual-claim-max-rooted-dual-scheduling
  area: evidence
  topic: 'DUAL*: max-rooted-dual-scheduling'
  outcome: supported
  summary: The MAX-rooted use is the source-specific directional choice, not a global
    claim that DUAL* is identical to SSS* or every routine called dual-ss*. The increasing-merit
    statement concerns ordered insertion; push/pop remain distinct operations.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-16
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The paper constructs DUAL* from the dual of SSS* by interchanging MAX and
    MIN behavior, replacing the minimum operation with a maximum, and changing ordered
    insertion to increasing merit. It deliberately applies this dual procedure to
    a MAX-rooted tree, producing a left-to-right traversal of root successors while
    using the dual search within their subtrees.
- assessment_id: dual-claim-descriptor-and-list-operations
  area: evidence
  topic: 'DUAL*: descriptor-and-list-operations'
  outcome: supported
  summary: This is a source description of the descriptor and helper conventions,
    not an independent invariant proof that every intermediate OPEN arrangement is
    globally sorted. Equal-merit placement is expressly retained.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-17
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed DUAL* descriptor contains a node, LIVE or SOLVED status,
    and merit h. The initial root descriptor is LIVE with a negative-infinity bound.
    The paper distinguishes push/pop from insert; insert places a descriptor in increasing
    merit order behind entries with equal merit.
- assessment_id: dual-claim-live-node-processing
  area: evidence
  topic: 'DUAL*: live-node-processing'
  outcome: supported
  summary: The claim labels its interpretation rather than repairing the display silently.
    The leaf test is printed separately from MAX/MIN tests, so executable behavior
    requires a precise node-type convention.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-18
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Under the intended terminal-versus-interior interpretation of Figure4,
    a LIVE leaf becomes SOLVED with merit max(Evaluate(node),h); a LIVE interior MAX
    node pushes its first child; and a LIVE interior MIN node pushes all children
    in reverse order. The printed separate leaf/MAX/MIN predicates require the source-interface
    qualification retained in the limitations.
- assessment_id: dual-claim-solved-node-processing
  area: evidence
  topic: 'DUAL*: solved-node-processing'
  outcome: supported
  summary: The root guard precedes parent use in the display. The purge target is
    stated as the paper’s stored-successor operation; its exact transitive descendant/list
    implementation is not supplied or generalized to shared graphs.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-19
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: For a SOLVED descriptor, Figure4 returns h if the node is the root. Otherwise,
    a solved MAX node purges the parent’s stored successors and pushes the parent
    as SOLVED; a solved MIN node pushes the next unexamined sibling as LIVE if one
    remains, or otherwise pushes the parent as SOLVED.
- assessment_id: dual-claim-source-stated-space-scope
  area: evidence
  topic: 'DUAL*: source-stated-space-scope'
  outcome: supported
  summary: This is the source’s storage characterization for the studied tree algorithms,
    not a newly derived exact closed form or a bound on allocator/runtime bytes. A
    short OPEN list in some examples does not imply linear space.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-20
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The journal describes complete-information SSS*, DUAL* and INS storage
    requirements as exponential with search depth, despite their differing descriptors
    and retained frontier sizes. DUAL* is not presented as a user-specified hard byte-budget
    search procedure.
- assessment_id: dual-claim-reported-comparison-design
  area: evidence
  topic: 'DUAL*: reported-comparison-design'
  outcome: supported
  summary: The source separates terminal visits from timing and refers detailed overheads
    to report12. This claim preserves the comparison design and limits without converting
    implementation-specific ratios into portable speedups.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-21
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: DUAL* is evaluated with the other search algorithms on the same generated
    trees of specified width, depth and sibling ordering. Figures5–7 report normalized
    terminal-node visits averaged over twenty shared samples; odd/even depth and ordering
    can change relative rankings. Separate preliminary timing observations concern
    the authors’ implementations and OPEN-list overhead.
- assessment_id: dual-limitation-finite-tree-scope
  area: scope
  topic: 'DUAL*: finite-tree-scope'
  outcome: supported
  summary: Keeps the source abstraction and root choice explicit instead of generalizing
    to every search problem.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-22
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The selected DUAL* is the paper’s MAX-rooted use on finite, fixed-depth
    alternating game trees. The displays assume positive uniform branching for interior
    nodes; cyclic/shared graphs, stochastic games and arbitrary early-terminal conventions
    are not supplied.
- assessment_id: dual-limitation-leaf-and-parity-interface
  area: scope
  topic: 'DUAL*: leaf-and-parity-interface'
  outcome: supported
  summary: The scientific-draft author’s earlier visual reading confirms the independent
    conditionals. The supported record states an interpretation with this qualification,
    not a silently amended program.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-18
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Figure4 prints independent LIVE tests for LEAFNODE, MAXNODE and MINNODE,
    while SOLVED processing uses the game-node type. The intended distinction between
    terminal and interior predicates, retained parity and terminal transitions must
    be specified before executable verification; the abbreviation alone does not prove
    a defect.
- assessment_id: dual-limitation-purge-and-list-interface
  area: scope
  topic: 'DUAL*: purge-and-list-interface'
  outcome: supported
  summary: The insert equal-merit convention is known, but a complete graph/list implementation
    contract is not. No descendant implementation is manufactured.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-23
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Purge is described as deleting stored successors from OPEN. Its exact transitive
    descendant selection, tie behavior in all operations, node identity and list-maintenance
    semantics remain helper-contract questions; arbitrary graph sharing or cycles
    are not justified by that description.
- assessment_id: dual-limitation-exhaustion-and-termination-interface
  area: scope
  topic: 'DUAL*: exhaustion-and-termination-interface'
  outcome: supported
  summary: Distinguishes the visible success return from unspecified exceptional interfaces
    without claiming a valid finite game tree necessarily encounters them.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-18
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed control loop is unconditional and terminates on a SOLVED
    root. Empty-OPEN failure, malformed node types and invalid child/sibling data
    are not given separate semantics; no execution-level termination or failure theorem
    is certified from the pseudocode.
- assessment_id: dual-limitation-memory-boundary
  area: scope
  topic: 'DUAL*: memory-boundary'
  outcome: supported
  summary: The word low overhead and a smaller frontier in some cases do not establish
    an asymptotically linear or externally bounded memory guarantee.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-20
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source describes complete-information storage as exponential with depth.
    It supplies no user-enforced byte budget, eviction scheme or total-runtime memory
    bound; this DUAL* must not be relabeled as a fixed-budget search method.
- assessment_id: dual-limitation-empirical-external-validity
  area: scope
  topic: 'DUAL*: empirical-external-validity'
  outcome: supported
  summary: Retains the metric and design; source-stated selected performance is not
    extrapolated to all games or implementations.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-24
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The normalized terminal-count comparisons use specified generated tree
    families and twenty shared samples, with ranking changes across depth parity and
    ordering. They are not universal node-count dominance, proof of optimal search
    ordering or a reproduced game-playing result.
- assessment_id: dual-limitation-timing-portability
  area: scope
  topic: 'DUAL*: timing-portability'
  outcome: supported
  summary: No external benchmark was run. The unresolved technical-report version
    remains explicit.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-11
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The preliminary timing ratios and OPEN-list profiles are implementation-specific,
    and the detailed overhead analysis is deferred to report12. They do not establish
    hardware-independent slowdowns or speedups, nor convert terminal visits into elapsed
    time.
- assessment_id: dual-limitation-dual-ss-and-sss-lineage
  area: scope
  topic: 'DUAL*: dual-ss-and-sss-lineage'
  outcome: supported
  summary: Original parallel and SSS* sources remain distinct pending questions; the
    current claim is source-specific rooted scheduling.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-25
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The journal compares DUAL* to SSS* and mentions Kumar–Kanal’s parallel
    dual-ss* routine. Its suggestion that one-process measurements could fill a missing
    comparison does not establish global aliases or complete equivalence to that parallel
    formulation.
- assessment_id: dual-limitation-artifact-version-scope
  area: scope
  topic: 'DUAL*: artifact-version-scope'
  outcome: supported
  summary: The rendering and report metadata are retained in research provenance rather
    than being promoted to uninspected positive claim sources. The journal locator
    contextualizes the procedure/publication only; the added provenance refs directly
    support the present reading/version/assurance boundary. No claim that the journal
    reports this curator’s access history is made.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-13
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-provenance-1
  - ins-dual-provenance-2
  - ins-dual-provenance-3
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The selected defining artifact is the inspected1987 author-hosted journal
    reproduction. Only selected regions of the separate author rendering and the TR85-16
    cover route were inspected; no whole-text or method equivalence, publisher-byte
    identity or independent replication is claimed.
- assessment_id: dual-limitation-proof-and-cost-model-boundary
  area: scope
  topic: 'DUAL*: proof-and-cost-model-boundary'
  outcome: supported
  summary: An explicit boundary on the present author’s assurance. The separately
    bound independent review assesses source control flow; it does not certify a complete
    implementation. The journal locator contextualizes the procedure/publication only;
    the added provenance refs directly support the present reading/version/assurance
    boundary. No claim that the journal reports this curator’s access history is made.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-26
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-provenance-1
  - ins-dual-provenance-2
  - ins-dual-provenance-3
  - ins-dual-independent-source-review
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The draft preserves the source’s descriptor updates, MAX-root choice and
    measured comparison scope. It does not certify the full minimax invariant, exact
    computational cost, implementation correctness or theorem claims from uninspected
    predecessor references.
- assessment_id: dual-definition
  area: evidence
  topic: 'DUAL*: defining procedure'
  outcome: supported
  summary: Source-specific procedure definition, limited to the inspected journal
    account. It does not allocate an ontology identity, mapping or alias, certify
    executable pseudocode, or assert a universal performance theorem.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - ins-dual-primary-27
  - dual-accepted-preview
  - ins-dual-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source’s MAX-rooted application of the dual of SSS*, using LIVE/SOLVED
    node descriptors, maximum-based merit updates and dual MAX/MIN expansion rules
    to search root successors from left to right.
- assessment_id: dual-kind
  area: scope
  topic: 'DUAL*: kind'
  outcome: supported
  summary: DUAL* denotes the selected MAX-rooted descriptor-based game-tree search
    procedure. LIVE/SOLVED state, dual MAX/MIN transitions and explicit list operations
    are algorithmic control, rather than a trained model, learning task or generic
    mathematical duality.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-primary-27
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The accepted algorithm kind is retained. Source-specific root choice, finite-tree
    assumptions and helper interfaces limit the interpretation; the title low overhead
    does not establish linear memory or a hard user byte budget.
- assessment_id: dual-identity
  area: identity
  topic: 'DUAL*: identity'
  outcome: supported
  summary: Retain the literal name DUAL* and empty global aliases for the 1987 MAX-rooted
    use of the dual of SSS*. It remains distinct from INS, SSS*, mathematical duality,
    Hamiltonian dual averaging and the uninspected parallel dual-ss* lineage.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-historical-identity
  - ins-dual-root-native-acceptance
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'Bare DUAL is not added as an alias. Historical normalized inventory and
    source-specific comparisons are attributed to the accepted preparation, without
    fresh current noncollision or owner allocation. Previously accepted identity notes
    (verbatim historical wording): This proposal selects the1987 MAX-rooted dual-of-SSS*
    procedure with LIVE/SOLVED descriptors, maximum merit, increasing OPEN order and
    dual MAX/MIN transitions. It is distinct from INS, SSS*, generic mathematical
    duality and Hamiltonian dual averaging. The earlier parallel dual-ss* citation
    is lineage to inspect, not an exact alias. Bare DUAL is omitted; the literal name
    keeps its star. At the historical04:51–04:52UTC branch360 snapshot, all1243 record
    identities (801native/442AIO;4927 field occurrences/3766 normalized values) were
    compared without an exact normalized candidate collision. Four ignored/hidden-inclusive
    roots supplied749 distinct matching contents. The reading covers747 full contents
    plus all matching leaves in two large wrappers. This is prospective historical
    evidence, not future current-state clearance.'
- assessment_id: dual-mapping
  area: grounding
  topic: 'DUAL*: mapping'
  outcome: supported
  summary: Retain the accepted bounded aio_no_match and all thirty rejection reasons.
    Alternating-player search, MAX/MIN scalar operations, stored descriptors and adversarial
    terminology do not establish learned models, GAN training, neural maximum/minimum
    layers, classification or reinforcement learning.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-historical-identity
  - ins-dual-root-native-acceptance
  - ins-dual-pinned-aio-context
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'The selected pinned-AIO context is inherited from its accepted prior reading.
    No positive target relation is asserted, and neither shared tree shape nor generic
    memory supplies one. This is a bounded assessment, not an all-ontology semantic
    absence claim. Previously accepted search scope (verbatim historical wording):
    Historical prospective snapshot on 2026-10-16 at 04:51–04:52 UTC, branch goal/discover-ai-concepts-round360,
    HEAD 3cd85f801666b505b906cedab979423e4f305c40. Compared all 801 maintained and
    442 pinned AIO identities (1,243 records; 4,927 identity-field occurrences; 3,766
    normalized values). Four fixed-string, case-insensitive, word-delimited searches
    included ignored and hidden files and excluded .git internals: 10,522 occurrences
    in 749 distinct contents. Fresh semantic reading covers 747 complete contents
    and all matching leaves in two large historical wrappers; unrelated wrapper fields
    were not reread. Read all 30 full candidate AIO nodes and 97 incident triples
    plus 20 maintained native definitions, identity fields, claim statements and limitations.
    This historical scope does not clear any future base or assign a source owner.'
- assessment_id: dual-source
  area: provenance
  topic: 'DUAL*: source'
  outcome: supported
  summary: The defining source for DUAL* is the same exact fifteen-page 1987 journal
    reproduction used by INS. Section3 and Figure4 support the MAX-rooted choice,
    LIVE/SOLVED processing and separate push/pop versus ordered insert conventions;
    the later experimental section supplies the qualified comparison design.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-source-roles
  - ins-dual-original-questions
  - ins-dual-additional-context
  - ins-dual-independent-source-review
  - ins-dual-primary-27
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Two record-level source rows represent one artifact and one work. Publisher-byte
    identity, disputed issue number, full alternate-rendering equivalence and independently
    reproduced performance are not asserted. The sixteen bibliography objects, nine
    questions and two incidental retrieval objects remain exact and separately queryable.
- assessment_id: dual-boundary
  area: scope
  topic: 'DUAL*: boundary'
  outcome: supported
  summary: Retain the source-specific MAX-rooted DUAL* controller, including maximum-based
    merits and increasing-merit insertion behind ties. Keep intended terminal/interior
    interpretation, root-before-parent success handling and purge/list/empty-OPEN
    boundaries explicit.
  target_ids:
  - AIMech:DUALStar
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-source-roles
  - ins-dual-original-questions
  - ins-dual-additional-context
  - ins-dual-independent-source-review
  - ins-dual-primary-27
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Six accepted claims and ten limitations remain unchanged. No global SSS*/parallel-dual
    alias, complete minimax invariant, graph-sharing extension, hard byte-budget property,
    portable speedup or implementation certification is inferred.
- assessment_id: pns-claim-near-root-prove-best-retention
  area: evidence
  topic: 'Partially Informed NegaScout: near-root-prove-best-retention'
  outcome: supported
  summary: The explicit PNS sentence selects near-root prove-best information. The
    immediately preceding explanation identifies prove-best data as upper bounds after
    all descendants have been examined without a beta cutoff. The draft keeps this
    narrow link and does not turn the source’s unspecified near-root phrase into a
    fixed level count.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-01
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The described PNS version retains information for prove-best cutoffs near
    the root of each subtree. Section 2 explains the relevant information as successor
    upper bounds from an initial traversal that examined every descendant without
    a beta cutoff; Section 3 selects only part of that information for PNS. The paper
    does not specify a numerical retention depth.
  dimensions:
  - name: source_descendant_meaning
    value: Immediate successor branches, not all descendant leaves
    definition: The accepted source interpretation concerns each successor return
      supplying an upper bound without a parent beta cutoff. It does not assert exhaustive
      enumeration of every leaf below those successors.
    evidence_ids:
    - pns-root-science
    - pns-primary-01
- assessment_id: pns-claim-initial-principal-variation
  area: evidence
  topic: 'Partially Informed NegaScout: initial-principal-variation'
  outcome: supported
  summary: The source defines the retained principal variation by the initial search’s
    selected terminal path. The statement does not upgrade that initial path to a
    permanently valid exact minimax path or invent later replacement/eviction rules.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-02
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: PNS also maintains the principal variation, defined here as the path to
    the terminal node that the initial search considered best. This identifies the
    retained path; the paper does not give a separate PNS procedure specifying its
    later updates.
- assessment_id: pns-claim-particular-partial-information-policy
  area: evidence
  topic: 'Partially Informed NegaScout: particular-partial-information-policy'
  outcome: supported
  summary: The introduction distinguishes PNS, NS and INS, and Section 3 explicitly
    says several compromise policies can be devised before describing its own version.
    This is a source-level distinction, not a completed current-inventory or global
    acronym decision.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-03
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The authors introduce PNS as a particular compromise between baseline NegaScout
    and the complete-information INS subtree map. They explicitly allow other possible
    compromise policies. The PNS description therefore identifies this retention policy
    rather than every method that saves some NegaScout search information.
- assessment_id: pns-claim-reported-comparison-design
  area: evidence
  topic: 'Partially Informed NegaScout: reported-comparison-design'
  outcome: supported
  summary: The design details come from Section 4 and the two figure labels. The count
    unit is leaves/terminal nodes normalized to minimal game-tree size, not elapsed
    time. No plotted values, superiority claim or missing INS/SSS* value is fabricated.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-04
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The paper includes PNS in comparisons with AB, NS, INS and SSS* on generated
    trees with random ordering or a 60% probability that the first descendant is best.
    Each plotted point averages twenty runs, and terminal-node counts are normalized
    to minimal game-tree size. Figures 4 and 5 show width-5 and width-20 settings;
    INS and SSS* results at depths 7 and 8 in Figure 5 are unavailable because of
    memory constraints. This describes the study design, not a numeric performance
    guarantee.
- assessment_id: pns-limit-1
  area: scope
  topic: 'Partially Informed NegaScout: limitation 1'
  outcome: supported
  summary: The full four-page inspection finds a prose PNS description alongside explicit
    NS and INS listings. It supports a bounded missing-specification observation in
    this artifact, not an assertion that no implementation exists elsewhere.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-05
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: PNS is described in prose, while Figure 1 lists NS and the appendix lists
    INS. No complete PNS listing, exact near-root retention depth, principal-variation
    update rule, bound-storage interface, eviction policy or cache lifetime is supplied.
    These details must not be filled in by silently copying INS.
- assessment_id: pns-limit-2
  area: scope
  topic: 'Partially Informed NegaScout: limitation 2'
  outcome: supported
  summary: Figure 3 labels upper bounds separately from the re-searched exact example
    value. The explicit max(a,alpha) and last-successor guard belong to the INS appendix.
    No PNS listing establishes their exact transfer, and the draft claims no implementation
    theorem.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-06
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The prove-best explanation depends on valid successor upper bounds and
    distinguishes those bounds from a true value obtained during re-search. It does
    not establish that all failed-window returns are exact values or that every complete
    INS guard and cutoff is retained by PNS. The descriptive PNS policy is not a certified
    executable implementation or an independently proved optimality theorem.
- assessment_id: pns-limit-3
  area: scope
  topic: 'Partially Informed NegaScout: limitation 3'
  outcome: supported
  summary: Integer declarations, unit-width probes and width/depth tree interfaces
    constrain the displayed context. Broader environments are not disproved; their
    extension is simply outside the inspected PNS contract.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-07
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed base procedures use integer scores, adjacent-value windows
    and a tree of supplied width and depth. This draft does not extend PNS to arbitrary
    real-valued window tolerances, cyclic graphs, transposition handling, stochastic
    games, quiescence search or unspecified early-terminal conventions.
- assessment_id: pns-limit-4
  area: scope
  topic: 'Partially Informed NegaScout: limitation 4'
  outcome: supported
  summary: The summation occurs in the complete INS discussion before the PNS compromise,
    and the hash-table proposal names INS. Ambiguous expression rendering is retained.
    A total PNS memory guarantee is not inferred from either passage.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-08
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source does not supply a precise PNS space formula or a hard total-memory
    cap. The partly ambiguous summation on p.1041 concerns retention of all INS information,
    and the later hash-table suggestion also concerns INS. Neither is a specified
    PNS storage implementation or a bound covering its entire stack and data structures.
- assessment_id: pns-limit-5
  area: scope
  topic: 'Partially Informed NegaScout: limitation 5'
  outcome: supported
  summary: This is a version qualification, grounded in the fresh 1985 sentence and
    the separately attributed earlier 1987 primary reading/comparison. Different descriptions
    are not sufficient to prove incompatible implementations or exact equivalence.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-09
  - pns-primary-10
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The 1985 description combines near-root prove-best information with principal-variation
    retention; the later 1987 journal describes PNS using first-level upper bounds.
    Their exact implementation, retention-depth and path-management correspondence
    remains a version question, rather than an established equivalence or demonstrated
    contradiction.
- assessment_id: pns-limit-6
  area: scope
  topic: 'Partially Informed NegaScout: limitation 6'
  outcome: supported
  summary: The source fixes the generated-tree comparison setting and says variability
    work continues. The draft reproduces design context only; it does not generalize
    sampled curves or claim a rerun.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-11
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The terminal-count comparisons depend on the generated trees, width, depth
    parity, ordering and twenty-run samples. The paper says further variability measurements
    are in progress. No curve digitization, runtime reproduction or universal node-dominance
    claim is made here.
- assessment_id: pns-limit-7
  area: scope
  topic: 'Partially Informed NegaScout: limitation 7'
  outcome: supported
  summary: The source explicitly makes timing implementation-dependent and distinguishes
    terminal counts from overhead. PNS preference is an author observation in that
    context. Ratios concerning INS and SSS* are not transplanted to PNS.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-12
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The reported preferences for PNS and execution-overhead observations describe
    the authors’ implementations and cost model. They do not establish portable speedups,
    byte budgets or that fewer terminal visits always yield lower running time; timing
    claims about INS or SSS* must not be reassigned to PNS.
- assessment_id: pns-limit-8
  area: scope
  topic: 'Partially Informed NegaScout: limitation 8'
  outcome: supported
  summary: Artifact properties and access/read scope are inspection metadata. The
    official acquisition and full image reading support this disclosure; some reconstructed
    characters remain uncertain and the seven cited full works remain unread in this
    draft.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-13
  - pns-accepted-preview
  - pns-accepted-support
  - pns-independent-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The defining artifact is the inspected official-hosted four-page 1985 publication
    reconstructed by ABBYY in 2006. Extracted text omits listings and parts of the
    bibliography; all four page images were inspected, but some formula and reference
    characters remain ambiguous. The seven cited originals were not inspected for
    this draft and are retained as source questions rather than imported proof evidence.
- assessment_id: pns-definition
  area: evidence
  topic: 'Partially Informed NegaScout: defining retention policy'
  outcome: supported
  summary: The source explicitly names PNS and describes two retained information
    components. The definition preserves the particular 1985 policy and intended re-search
    use without asserting a storage bound, speedup, fixed retention depth or complete
    executable contract.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-14
  - pns-accepted-core
  - pns-accepted-support
  - pns-root-science
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: A NegaScout variant for adversarial game-tree search that retains prove-best
    information near the root of each subtree and the principal variation from an
    initial search to guide a later re-search, as the particular partial-information
    policy described in the 1985 paper.
- assessment_id: pns-concept-kind
  area: scope
  topic: 'Partially Informed NegaScout: algorithm kind'
  outcome: supported
  summary: The source names an operational partial-information NegaScout policy for
    adversarial game-tree search. It is appropriately described as an algorithm, with
    its available retention mechanism stated and its absent complete listing qualified.
    It is neither a trained model nor a benchmark or generic memory-saving task.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-14
  - pns-accepted-core
  - pns-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The descriptive algorithm kind does not certify a full executable interface.
    Exact near-root retention depth, principal-variation updates, storage rules and
    complete pruning control remain unresolved. The INS appendix and baseline NS listing
    must not be silently recast as the missing PNS listing.
- assessment_id: pns-historical-identity
  area: identity
  topic: 'Partially Informed NegaScout: source-local identity and historical comparison'
  outcome: supported
  summary: Retain the full name Partially Informed NegaScout with aliases empty. The
    selected scope is the particular 1985 policy. Bare PNS is unsuitable as a global
    alias because a separate primary abstract uses it for Proof-Number Search. The
    1987 INS and DUAL* previews are prospective comparisons; later maintained SVPG,
    IE and ITERSSS records remain separate methods.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-accepted-preview
  - pns-identity-proposal
  - pns-historical-search
  - pns-root-identity
  - pns-acronym-context
  - pns-post-snapshot-context
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'This record draft denotes the particular partial-information NegaScout
    policy described in the official 1985 paper: prove-best information near each
    subtree root and the principal variation from its initial search. It does not
    identify all partial NegaScout policies, the complete-information 1987 INS procedure,
    baseline NegaScout, Principal Variation Search, DUAL* or proof-number search.
    The source-local abbreviation PNS is omitted from global aliases because a separate
    primary publication explicitly uses PNS for Proof-Number Search. The 1985 near-root-plus-path
    description and the 1987 first-level upper-bound description remain an unresolved
    version question. Historical comparison at 05:11–05:12 UTC on 2026-10-16 covered
    801 native and 442 pinned AIO records at HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c,
    with four ignored- and hidden-inclusive search roots. A separate subsequent comparison
    read the newly added SVPG, Iterative Expansion and ITERSSS* records and current
    main 911 source context. That bounded supplement does not constitute a new complete
    inventory or assign PNS a source owner. Full source and evidence limitations remain
    explicit. The historical four-root search includes hidden and ignored files. All
    7 bibliography objects, 9 original questions and 3 additional context questions
    remain retained. No current canonical absence, source-owner allocation or closure
    is inferred.'
- assessment_id: pns-aio-no-match
  area: grounding
  topic: 'Partially Informed NegaScout: bounded 30-target AIO no-match'
  outcome: supported
  summary: Retain the accepted explicit no-match assessment and all 30 target-specific
    reasons. Generic memory, recursion, tree structure, adversarial wording and game
    applications do not establish identity or an informative source-backed relation
    to the inspected model, task, neural architecture and tensor-layer concepts.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-accepted-preview
  - pns-mapping-assessment
  - pns-aio-context
  - pns-root-identity
  - pns-independent-native
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'Historical prospective collection on 2026-10-16 from 05:11:39 to 05:12:47
    UTC, branch goal/discover-ai-concepts-round361, HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c.
    Compared all 1,243 record identities (801 native and 442 pinned AIO; 4,927 field
    occurrences and 3,766 normalized values). All 18 normalized probes, including
    the proposed local ID, were clear. Four ignored- and hidden-inclusive fixed-string,
    case-insensitive, word-delimited searches produced 10 distinct matching contents
    and 14 occurrences; every content and occurrence binding was read. The complete
    identity DATA matched the previously read INS/DUAL snapshot exactly. Fresh semantic
    context covered 114 native identity/definition projections, 12 selected native
    definitions and all their claim statements, 30 complete annotated AIO nodes and
    97 incident triples, and the prospective INS/DUAL drafts. The three actual records
    added afterward were read in a separate bounded supplement; their addition was
    reported to bring native counts to 804. No later whole-inventory clearance, global
    source exhaustion or future ownership is claimed.


    No suitable positive AIO mapping was identified for this source-specific partial
    NegaScout procedure. The inspected targets concern learned models, learning tasks,
    tensor layers or broad mathematical/representational classes. Shared memory, recursion,
    tree shape, adversarial terminology or game applications alone do not establish
    an informative source-backed relation. This is a bounded curator assessment of
    the pinned snapshot, not an upstream ontology assertion.


    AIO:ActiveLearning: Acquiring bounds during game-tree search is not interactively
    querying labels for training data. The 1985 title does not establish the pinned
    active-learning task.

    AIO:ArtificialNeuralNetwork: PNS specifies no artificial-neuron architecture or
    neural training; its stored search information is not a neural network.

    AIO:CausalGraphicalModel: An alternating game tree is not a causal probabilistic
    representation of a data-generating process.

    AIO:Classification: PNS searches values/moves in a supplied game tree; it does
    not classify observations into learned classes.

    AIO:DecisionTree: The pinned node is a Classification subclass. Its broader decision-support
    comment does not identify a partial NegaScout game-tree search algorithm with
    a classification tree.

    AIO:GenerativeAdversarialNetwork: Adversarial game-tree evaluation does not imply
    competing generative/discriminative neural networks or GAN training.

    AIO:GraphConvolutionalPolicyNetwork: PNS uses neither graph convolutions nor a
    trained goal-directed graph-generation policy network.

    AIO:GraphLanguageModel: A game-tree representation is not a graph language model;
    the source supplies no language-model mechanism.

    AIO:HashingLayer: Partial search-information storage does not establish categorical
    feature hashing or a preprocessing layer. The PNS storage contract is itself incompletely
    specified.

    AIO:HierarchicalClassification: Successive game moves form a search hierarchy,
    not a hierarchy of classification labels.

    AIO:MachineLearningTask: Retaining already computed search bounds is not on its
    own a task of building methods that learn from data. No such learning task is
    defined for this PNS.

    AIO:MathematicalFunction: Generic score arithmetic does not supply an informative
    relation from the operational partial NegaScout algorithm to the pinned scalar-function
    class.

    AIO:MaximumLayer: The pinned operation merges tensors elementwise. Bound comparisons
    in game-tree re-search do not constitute that layer.

    AIO:MemoryAugmentedLLM: PNS is not a language model and its retained bounds/principal
    variation do not establish external-memory LLM identity.

    AIO:MemoryCellLayer: Selective retention of search information is not a layer
    made of neural memory cells.

    AIO:MinimumLayer: The pinned tensor minimum merge is distinct from search-window
    control and alternating-player value propagation.

    AIO:Model: The very broad representation class does not identify the source operational
    procedure or supply a defensible informative mapping merely because a search tree
    represents a game.

    AIO:Network: Interconnected search nodes do not make the algorithm itself the
    pinned generic Network concept; topology alone is insufficient.

    AIO:NeuralTuringMachineNetwork: The source PNS has no differentiable neural memory
    controller; using memory does not establish this architecture.

    AIO:NeuroSymbolicLLM: No neural language model or neural-symbolic integration
    appears in the selected PNS procedure.

    AIO:PolicyLayer: The PNS description does not define a neural layer outputting
    a probability distribution over actions.

    AIO:ProbabilisticGraphicalModel: Its game tree contains alternatives and score
    bounds, not a model of random-variable conditional dependencies.

    AIO:RandomForest: PNS is not an ensemble of learned classification/regression
    trees. Generated experimental trees are inputs, not trained forest estimators.

    AIO:ReasoningLLM: Game-tree reasoning does not establish a large language model
    or the pinned reasoning architecture.

    AIO:RecursiveLLM: Search recursion is a control convention, not a recursive language-model
    architecture.

    AIO:RecursiveLanguageModel: The selected source does not build recursive representations
    for language modeling.

    AIO:RecursiveNeuralNetwork: Recursive game-tree traversal does not apply learned
    neural weights over structured inputs.

    AIO:ReinforcementLearning: The described finite game-tree search with supplied
    scores and retained bounds does not learn a policy from reward interactions. A
    game application alone does not justify even an algorithm-to-task related mapping.

    AIO:ReinforcementLearningLLM: PNS is not a language model fine-tuned through reinforcement
    learning.

    AIO:TrainingStrategy: The source controls search and information retention, not
    preprocessing or model-training strategy.'
- assessment_id: pns-source-roles
  area: provenance
  topic: 'Partially Informed NegaScout: defining evidence and separate contexts'
  outcome: supported
  summary: The official-hosted four-page 1985 paper supplies the definition and every
    positive claim citation. Its later ABBYY reconstruction metadata is not a new
    algorithm version. The 1987 journal remains a separate primary version context,
    while the 2022 abstract and 1994 institutional metadata establish acronym/retrieval
    context only.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-15
  - pns-primary-10
  - pns-source-roles
  - pns-original-questions
  - pns-extra-questions
  - pns-independent-science
  - pns-independent-native
  - pns-root-preview
  - pns-preview-validation
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Preserve the exact downloaded 1985 PDF hash, original URL, source access
    time and full-image reading attribution. Text extraction omitted listings and
    some bibliography/formula characters remain ambiguous. Neither the 1987 summary,
    the INS appendix, a bibliography entry nor acronym metadata supplies a complete
    PNS implementation. Seven original bibliography objects and nine original questions
    remain byte-exact; three additional context-only retrieval questions remain separate.
    The historical native validation checks structural/per-record requirements and
    supplies no scientific or future inventory clearance. All full-paper reading is
    attributed to the earlier researcher and independent source reviewer; this fragment
    assembly does not repeat it.
- assessment_id: pns-version-acronym-boundary
  area: scope
  topic: 'Partially Informed NegaScout: retain source and acronym boundaries'
  outcome: supported
  summary: Retain the particular 1985 PNS policy separately from complete-information
    INS, baseline NegaScout/PVS, DUAL*, proof-number search and unrelated memory-limited
    or recursive searches. The 1985 near-root-plus-principal-variation description
    and 1987 first-level upper-bound wording are a version question, not demonstrated
    contradiction or proven full equivalence. Keep the missing PNS listing, retention
    depth, PV maintenance, score/bound, storage and implementation interfaces explicit;
    no runtime, space or universal performance theorem follows.
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - pns-primary-15
  - pns-primary-10
  - pns-root-science
  - pns-accepted-support
  - pns-identity-proposal
  - pns-acronym-context
  - pns-original-questions
  - pns-extra-questions
  - pns-post-snapshot-context
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The prove-best statement retains the root-accepted immediate-successor-branch
    interpretation, not enumeration of every descendant leaf. The 2022 abstract demonstrates
    the ambiguous PNS expansion but does not support a new Proof-Number Search or
    PN-MCTS record here. The current main 911 umbrella and its later ITERSSS responsibility
    are context, not a PNS owner assignment. All original and added questions remain
    unchanged and no source family is declared exhausted.
- assessment_id: actual-current-governance
  area: provenance
  topic: Actual current records, source responsibilities and checks
  outcome: supported
  summary: 'Actual three records retain 16 claims and 28 limitations across two primary
    PDF artifacts/two works and three declared source rows. The 1987 journal defines
    INS/DUAL; the 1985 proceedings defines PNS. The 1987 PNS comparison is context
    on the shared artifact. Six exclusive creation outputs, one CREATE event, 87 captured
    inputs, parsed generated pages and six successful required checks are bound. Current
    source responsibility follows the accepted plan: {"additional_source_question_count":
    0, "changed_main_indexes": [911], "changed_nested_indexes": [], "historical_source_responsibility_links":
    2, "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_source_objects":
    46, "source_object_counts": {"ijcai1985": {"additional_context_questions": 3,
    "bibliography": 7, "source_questions": 9}, "journal1987": {"bibliography": 16,
    "incidental_retrieval_contexts": 2, "source_questions": 9}}}. The 46 source objects
    and two historical links remain explicit. One approved INS access-attribution
    correction is applied; version questions remain pending. Complete actual 361 inherited
    accounting and older 360 source durability remain exact. No research exhaustion
    or publication completion is implied.'
  target_ids:
  - AIMech:InformedNegaScout
  - AIMech:DUALStar
  - AIMech:PartiallyInformedNegaScout
  evidence_ids:
  - actual-write
  - captured-inputs
  - postcapture-reading
  - governance-assessment
  - rendered-pages
  - actual-scientific-assessment
  - creation-history
  - current-discovery-report
  - inherited-source-durability
  - root-decisions
  - ownership-plan
  - ownership-plan-acceptance
  - approved-access-attribution-correction
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
  details: Actual canonical fields, 46 original objects, two historical responsibility
    links, current additional questions and inherited projection were assessed with
    exact receipts. Historical primary reading remains attributed. The correction
    updates access status only. Review save, committed-head verification and publication
    remain subsequent operations.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:InformedNegaScout
  rationale: Retain full-information INS as distinct from the partial PNS policy and
    the LIVE/SOLVED DUAL* controller. Preserve the source-relative odd/even levels,
    research/resflag distinction, max(a,alpha) threshold and returned-bound qualification;
    do not silently complete merit storage or last-successor guards.
  evidence_ids:
  - ins-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-original-questions
  - ins-dual-historical-identity
  - actual-write
  - root-decisions
  - postcapture-reading
- action: retain
  target_ids:
  - AIMech:DUALStar
  rationale: Retain the source-specific MAX-rooted DUAL* controller, including maximum-based
    merits and increasing-merit insertion behind ties. Keep intended terminal/interior
    interpretation, root-before-parent success handling and purge/list/empty-OPEN
    boundaries explicit.
  evidence_ids:
  - dual-accepted-preview
  - ins-dual-accepted-support
  - ins-dual-original-questions
  - ins-dual-historical-identity
  - actual-write
  - root-decisions
  - postcapture-reading
- action: retain
  target_ids:
  - AIMech:PartiallyInformedNegaScout
  rationale: Retain the particular 1985 PNS policy separately from complete-information
    INS, baseline NegaScout/PVS, DUAL*, proof-number search and unrelated memory-limited
    or recursive searches. The 1985 near-root-plus-principal-variation description
    and 1987 first-level upper-bound wording are a version question, not demonstrated
    contradiction or proven full equivalence. Keep the missing PNS listing, retention
    depth, PV maintenance, score/bound, storage and implementation interfaces explicit;
    no runtime, space or universal performance theorem follows.
  evidence_ids:
  - pns-accepted-preview
  - pns-accepted-support
  - pns-identity-proposal
  - pns-acronym-context
  - pns-original-questions
  - pns-extra-questions
  - actual-write
  - root-decisions
  - postcapture-reading
targets:
- target_id: AIMech:InformedNegaScout
  label: Informed NegaScout
  path: data/curated/InformedNegaScout.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/InformedNegaScout.yaml
    role: maintained native concept record
- target_id: AIMech:DUALStar
  label: DUAL*
  path: data/curated/DUALStar.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DUALStar.yaml
    role: maintained native concept record
- target_id: AIMech:PartiallyInformedNegaScout
  label: Partially Informed NegaScout
  path: data/curated/PartiallyInformedNegaScout.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartiallyInformedNegaScout.yaml
    role: maintained native concept record
limitations:
- Source-scoped mechanisms and mathematical/control-flow boundaries retain accepted
  fragment narratives except the precisely attributed INS limitation8 access-status
  correction. Native schema validation is evidence of structural validity, not scientific
  proof.
- INS/DUAL source and core authorship, PNS source/native/fragment authorship, earlier
  independent source reviews and this assembly authorship remain separately attributed.
- Actual current identity/no-match and responsibility decisions are bound to this
  collection and accepted owner plan. Earlier source, identity and neighbor readings
  remain separately attributed; the current snapshot does not clear future additions.
- Actual six creation outputs, one CREATE history, 87 capture inputs and 7 parsed
  generated pages are bound. Six required commands passed; earlier failed attempts
  remain explicit. Canonical review save/check and publication are subsequent operations.
tags:
- source-scoped
- game-tree-search
- minimal-window-search
notes:
- The 62 scientific narratives originate from the two accepted fragments, with the
  shared INS/DUAL group included once. The approved INS limitation 8 summary/details
  are the sole scientific-narrative correction. All scientific assessments receive
  separately attributed actual evidence links. The 78 original evidence templates
  retain their metadata except actual local access times and UTC normalization. The
  63rd assessment records current governance. Correction evidence and both PNS reading
  receipts link directly from the corrected assessment; original fragments stay immutable.
- Local evidence access instants come from actual attributed postcapture reading.
  Primary acquisition times retain their historical instants, normalized to UTC Z.
  Historical identities/access statements elsewhere remain explicitly historical;
  current identity notes are separately bound.
- The1987 journal defines INS/DUAL; the1985 proceedings defines PNS. The1987 PNS version-comparison
  citation is context on an already counted artifact, not another defining PNS source.
- Original source objects and historical responsibilities remain distinct from the
  actual current dispositions bound here. Issue415 tracks the approved access-attribution
  repair; source/version questions and inherited issues retain their separate scopes.
  No issue closure, discovery exhaustion or implementation certification is implied.
- The shared 1987 source group retains16 bibliography objects,9 source questions and2
  incidental contexts once for INS and DUAL*. The1985 PNS group retains7 bibliography
  objects,9 source questions and3 additional contexts. These46 objects and2 separately
  counted historical responsibility links are source accounting, not46 new concepts.
  The PNS link is also an original1987 question; it is not a newly discovered second
  question.
- '{"added_record_ids": [], "assessment": "The Stockman1979 SSS* original is already
  an explicit pending source under main911 in the ITERSSS* accounting. Neither DUAL*
  nor the existing ITERSSS* record makes original SSS* identical or fully inspected.",
  "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"],
  "group": "journal1987", "kind": "bibliography", "next_check": "Read the original
  SSS* procedure and proof under its own scope; coordinate the identical Stockman
  citation in the1985 and1986 ledgers.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Stockman, G.C., A minimax algorithm better than alpha-beta?, Artificial Intelligence
  12(2) \n(1979) 179-196.", "locator": "printed p.199 / PDF p.15, reference1", "number":
  1, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "e65f5558c42abab080d698173292ee91848f5143a9d22d7c77693e19d1a75763", "pointer": "/journal_references/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Pearl1980 minimax-tree analysis is a separate
  original. The retained citation and the new procedures do not inspect its asymptotic
  arguments or establish SCOUT identity.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the exact1980
  paper and its assumptions; distinguish its procedure/theory scope from Pearl1984
  book context and the1987 INS procedure.", "original": {"exact_original_object":
  {"exact_extracted_citation": "Pearl, J., Asymptotic properties of minimax trees
  and game-seraching procedures, Artificial \nIntelligence 14(2) (1980) 113-138.",
  "locator": "printed p.199 / PDF p.15, reference2", "number": 2, "source": {"path":
  "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 1, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "79b7afdb65502307dc1812c61f98ee0ba34e7672a320485e7f1bcca43e9b0809", "pointer": "/journal_references/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Fishburn1984 is the cited book, distinct
  from the1981 report cited by the1985 PNS paper. Similar titles do not prove identical
  versions.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "journal1987", "kind": "bibliography", "next_check": "Inspect the1984 book and independently
  compare the1981 Technical Report431 before merging source or minimal-window lineage
  claims.", "original": {"exact_original_object": {"exact_extracted_citation": "Fishburn,
  J.P., Analysis of Speedup in Distributed Algorithms (UMI Research Press, Ann \nArbor,
  MI, 1984).", "locator": "printed p.199 / PDF p.15, reference3", "number": 3, "source":
  {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 2, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "404a0d030a162c6e2d0aeefd5a65758ce80d52b8b1be5de839e682ebbb92c74a", "pointer": "/journal_references/2"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1982 parallel strongly ordered game-tree
  work is a separate source, not the sequential INS or DUAL* mechanism.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "bibliography", "next_check": "Inspect the original parallel search, ordering and
  correctness assumptions; reconcile the reconstructed1985 reference metadata separately.",
  "original": {"exact_original_object": {"exact_extracted_citation": "Marsland, T.A.
  and Campbell, M.S., Parallel search of strongly ordered game trees, ACM \nComput.
  Surv. 14(4) (1982) 533-552.", "locator": "printed p.199 / PDF p.15, reference4",
  "number": 4, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 3, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "3893deb1cf5862c2e620154da58879038bd1d9749a1b0a7eb192d0329b45fbef", "pointer": "/journal_references/3"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The IJCAI1983 alpha-beta implementation
  comparison remains a distinct lineage/performance original.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check":
  "Read the1983 implementation comparisons before generalizing NegaScout/PVS names,
  overhead or runtime claims.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Marsland, T,A., Relative efficiency of alpha-beta implementations, in: Proceedings
  1JCAI-83, \nKarlsruhe, F.R.G. (1983) 763-766.", "locator": "printed p.199 / PDF
  p.15, reference5", "number": 5, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 4, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "6a383b41c881bad193bed7a6ac5112062d70d51607e5e73e96876d3bc2758d85", "pointer": "/journal_references/4"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1983 minimax comparison is not represented
  merely by adding two procedures it later informs.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check":
  "Inspect its concrete comparator algorithms, move ordering, parity and empirical
  setup; coordinate the same citation in the1985 bibliography.", "original": {"exact_original_object":
  {"exact_extracted_citation": "Campbell, M.S. and Marsland, T.A., A comparison of
  minimax tree search algorithms, \nArtificial Intelligence 20(4) (1983) 347-367.",
  "locator": "printed p.199 / PDF p.15, reference6", "number": 6, "source": {"path":
  "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 5, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "7fb6fd2ba0e1d1abd0925db0cc499132e0f9540f2bb2bee791bf62e8177641ca", "pointer": "/journal_references/5"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Reinefeld1983 is the original NegaScout
  improvement source, not a global alias established by the1987 footnote.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "bibliography", "next_check": "Read the exact Scout/NegaScout original and verify
  title/issue/pages and algorithm boundaries before adopting global NS/PVS aliases.",
  "original": {"exact_original_object": {"exact_extracted_citation": "Reinefeld, A.,
  An improvement of the Scout tree search algorithm, 1CCA J. 6(4) (1983) 4-14.", "locator":
  "printed p.199 / PDF p.15, reference7", "number": 7, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 6, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "11611e80cbf31d9ccb21873d699fa04f2c9a14a1cc2b9383e273bc27b28ca3fe", "pointer": "/journal_references/6"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1985 empirical pruning comparison is
  independent of the separately read IJCAI1985 PNS paper despite sharing a year.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "journal1987",
  "kind": "bibliography", "next_check": "Read Musczycka–Shinghal and its exact tree/pruning
  protocol; preserve the extracted citation spelling until original verification.",
  "original": {"exact_original_object": {"exact_extracted_citation": "Musczycka, A.
  and Shinghal, R., An empirical comparison of pruning strategies in game trees, \nIEEE
  Trans. Syst. Man Cybern. 15 (3) (1985) 389-399.", "locator": "printed p.199 / PDF
  p.15, reference8", "number": 8, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 7, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "4e8a47b94eeb96cd255163933cfaaef76120bc8f88447b119d0012855235cf94", "pointer": "/journal_references/7"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "This exact reference9 points to the official1985
  paper now fully read for source-specific PNS and bounded earlier-INS comparison.
  Its historical not-read status remains unchanged inside original. The separately
  counted ijcai1985 responsibility link records proposed PNS representation; version
  and implementation questions remain open.", "disposition": "retained_context", "existing_record_ids":
  [], "group": "journal1987", "kind": "bibliography", "next_check": "Use the existing1985
  dossier and PNS record scope; pursue retention-depth, helper/storage, score and1985/1987
  display differences without treating the paper as unread or as a global INS/PNS
  equivalence.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Reinefeld, A., Schaeffer, J. and Marsland, T.A., Information acquisition in minimal
  window \nsearch, in: Proceedings 1JCAI-85, Los Angeles, CA (1985) 1040-1043.", "locator":
  "printed p.199 / PDF p.15, reference9", "number": 9, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 8, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "245284e1d03a251de1dd84552f1289e0bd78bd35f7e51ec4cecb261e006aa850", "pointer": "/journal_references/8"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Baudet1978 is the asynchronous-multiprocessor
  dissertation, not automatically the separate alpha-beta branching article retained
  in ITERSSS*.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "journal1987", "kind": "bibliography", "next_check": "Acquire and inspect this exact
  dissertation for the cited simulation/parallel assumptions; keep works with the
  same author/year distinct.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Baudet, G.M., The design and analysis of algorithms for asynchronous multiprocessors,
  Ph.D. \nDissertation, Carnegie Mellon University, Pittsburgh, PA, 1978.", "locator":
  "printed p.199 / PDF p.15, reference10", "number": 10, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 9, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "22a41080f79081a4706a313ff52fe2f295466e42592cf833f093e9e42cf0fb0c", "pointer": "/journal_references/9"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Schaeffer1986 thesis supplies deferred
  experimental/search-knowledge detail and remains an independent original.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "bibliography", "next_check": "Inspect the thesis tree generator, score distribution,
  ordering and timing context before stronger empirical synthesis.", "original": {"exact_original_object":
  {"exact_extracted_citation": "Schaeffer, J., Experiments in search and knowledge,
  Ph.D. Thesis, University of Waterloo, \nWaterloo, Ont., 1986.", "locator": "printed
  p.199 / PDF p.15, reference11", "number": 11, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 10, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "a9686fd5c71c85a8f94b0de6c0cabfeae72c99cfb4523bd546ff0d6400553e90", "pointer": "/journal_references/10"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "TR85-16 remains a title/date/page-count
  and incomplete-access question. The inspected cover and partial author rendering
  do not establish a fully read equivalent version.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "journal1987", "kind": "bibliography", "next_check":
  "Compare the27-page index description with the19-page linked rendering and exact1987
  references; inspect full method/timing sections before version equivalence.", "original":
  {"exact_original_object": {"exact_extracted_citation": "Reinefeld, A., Marsland,
  T.A. and Schaeffer, J., Is best first search best?, Tech. Rept. \nTR85-16, Computing
  Science Department, University of Alberta, Edmonton, Alta., 1985.", "locator": "printed
  p.199 / PDF p.15, reference12", "number": 12, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 11, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "3e5d383fb477c917552ebb6f02439934d80f026b2d665f9a05ff484449bd69ea", "pointer": "/journal_references/11"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Kumar–Kanal1984 parallel branch-and-bound/dual-ss*
  is not automatically the journal sequential MAX-rooted DUAL*. Generic AND/OR similarities
  do not discharge this source.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "journal1987", "kind": "bibliography", "next_check": "Read the original
  parallel formulation and duality conventions; compare sequential control, node parity
  and purge semantics independently.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Kumar, V. and Kanal, L.N., Parallel branch-and-bound formulations for AND/OR tree
  search, \nIEEE Trans. Pattern Anal. Mach. Intell. 6(6) (1984) 768-778.", "locator":
  "printed p.199 / PDF p.15, reference13", "number": 13, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 12, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "1bebe2fec20635f3d3248559841f796187930e5a5fa81385bb3c4074ac020d8c", "pointer": "/journal_references/12"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Slagle–Dixon game-tree experiments are
  a distinct original and their extracted venue/year/page fields are retained without
  silent correction.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "journal1987", "kind": "bibliography", "next_check": "Inspect the original
  programs, scoring/order protocol and bibliographic fields before transferring experimental
  conclusions.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Slagle, J. and Dixon, J., Experiments with some programs that search game trees,
  J. ACM 2 \n(1969) 189-207.", "locator": "printed p.199 / PDF p.15, reference14",
  "number": 14, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 13, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "54a8e59f219827ebdcd77ce83b947a747f79b552ffc12e4e3536cd381bce8d3d", "pointer": "/journal_references/13"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Roizen–Pearl yes-and-no comparison is a
  separate theoretical/empirical source, not the Stockman defining article.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "bibliography", "next_check": "Read its exact comparator assumptions and strengths/limits
  before asserting SSS*, DUAL* or alpha-beta dominance.", "original": {"exact_original_object":
  {"exact_extracted_citation": "Roizen, I. and Pearl, J., A minimax algorithm better
  than alpha-beta? Yes and no, Artificial \nIntelligence 21(1,2) (1983) 199-220.",
  "locator": "printed p.199 / PDF p.15, reference15", "number": 15, "source": {"path":
  "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 14, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "771a8e5bc1183646115e705cdaa754f7a13fda3db704cb6519a9e8e83361d78f", "pointer": "/journal_references/14"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Knuth–Moore1975 already has explicit pending
  main911 responsibility in the ITERSSS* ledger. Single-agent Minimin alpha pruning
  under main290 does not represent this two-player alpha-beta original.", "disposition":
  "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"], "group":
  "journal1987", "kind": "bibliography", "next_check": "Read the exact alpha-beta
  comparator and ordering/theorem premises; coordinate1985/1986/1987 citation occurrences
  without erasing any original.", "original": {"exact_original_object": {"exact_extracted_citation":
  "Knuth, D.E. and Moore, R.W., An analysis of alpha-beta pruning, Artificial Intelligence
  6(4) \n(1975) 293-326.", "locator": "printed p.199 / PDF p.15, reference16", "number":
  16, "source": {"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, "status":
  "Retained bibliography; not automatically a new concept; original not read in this
  task."}, "index": 15, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "9dcd6260bcec3cdcabcadff0c09c4a5ac971103ac8f4b46db4b3325f7fba5009", "pointer": "/journal_references/15"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The current source-scoped INS record retains
  the incomplete helper/storage contract. Reading1985 exposes an explicit last-successor
  guard but does not resolve merit initialization, cache lifetime or all terminal
  conventions.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "journal1987", "kind": "source_questions", "next_check": "Seek exact author code/full
  report and compare both printed listings without silently repairing either.", "original":
  {"exact_original_object": {"id": "INS-STORAGE-INTERFACE", "locators": ["pp.190–191",
  "author rendering PDF7–8"], "question": "Inspect author code/report for exact merit
  population, GetInfo/SaveInfo behavior, final-successor guard, cache misses and terminal
  conventions; preserve the journal display without silent repair.", "status": "pending_source_clarification"},
  "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "367bf24b013490cf76d77cc041458b2c8104d3fd586ae3ff3105b956d9a30188", "pointer": "/source_questions/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The DUAL* record preserves source-local
  leaf/interior/parity and OPEN/purge qualifications; its addition does not complete
  every helper or tie interface.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "journal1987", "kind": "source_questions", "next_check": "Inspect a
  complete author implementation or fuller account of node-kind, purge descendant
  and priority/tie rules.", "original": {"exact_original_object": {"id": "DUAL-CONTROLFLOW-INTERFACE",
  "locators": ["pp.191–193", "author rendering PDF10"], "question": "Clarify leaf
  versus interior node tests, retained game-node parity, purge descendant scope, OPEN
  operations and tie order against the SSS*/dual source lineage.", "status": "pending_source_clarification"},
  "index": 1, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "3bd540af87392919f409d047709e9b870d2fba3c4fe82708042d5f8257dc25fc", "pointer": "/source_questions/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The original PNS-1985 question is now partly
  answered: the official four-page source has been fully read and source-specific
  PNS is proposed separately. The exact historical pending_original_reading object
  stays unchanged; the ijcai1985 historical link carries representation. Retention,
  storage, version and global-lineage questions remain.", "disposition": "retained_context",
  "existing_record_ids": [], "group": "journal1987", "kind": "source_questions", "next_check":
  "Follow the nine explicit1985 source questions and the separate PNS link; do not
  continue to describe the official1985 source as unread.", "original": {"exact_original_object":
  {"id": "PNS-1985", "question": "Read Information acquisition in minimal window search
  (IJCAI1985,1040–1043), compare full INS/PNS procedure and source versions before
  any PNS identity or split.", "reference_numbers": [9], "status": "pending_original_reading"},
  "index": 2, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "f0f7c946f02d85a86271faa8e4a6ee94984a5405f8de87f3451275296ae1a070", "pointer": "/source_questions/2"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The original Reinefeld1983/SCOUT/PAB/PVS
  sources remain pending. Reading the1985 and1987 descriptions alone does not establish
  global aliases.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "journal1987", "kind": "source_questions", "next_check": "Inspect the named
  originals and exact control-flow/version relationships individually.", "original":
  {"exact_original_object": {"id": "NEGASCOUT-LINEAGE", "question": "Read Reinefeld1983
  and the SCOUT/PAB/PVS source lineage; the journal footnote does not alone establish
  global aliases or every practical implementation.", "reference_numbers": [2, 3,
  4, 5, 7], "status": "pending_original_reading"}, "index": 3, "origin": {"path":
  "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "7b66a7646bc3c02df972c33f28819751219e596cf8dacfc9f8d83e072f3ee615", "pointer": "/source_questions/3"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The parallel dual-ss* lineage is distinct
  from the selected sequential DUAL* scope and remains uninspected.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "source_questions", "next_check": "Read Kumar–Kanal1984 and compare MAX-root orientation,
  parallel scheduling and purge/state conventions.", "original": {"exact_original_object":
  {"id": "DUAL-SS-LINEAGE", "question": "Read Kumar–Kanal1984 parallel dual-ss* source,
  distinguish parallel formulation from this sequential MAX-rooted use; similarity
  is not a completed identity decision.", "reference_numbers": [13], "status": "pending_original_reading"},
  "index": 4, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "5ee363e5b770c68aba17d326cb5b5aaac291ebfe56145fd5dacceb0612422d23", "pointer": "/source_questions/4"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The shared main911 ledger already retains
  original SSS* and alpha-beta comparison sources. ITERSSS* is a separate memory-controlled
  algorithm, while Minimin is single-agent; neither closes this comparison question.",
  "disposition": "existing_pending_owner", "existing_record_ids": ["AIMech:ITERSSSStar"],
  "group": "journal1987", "kind": "source_questions", "next_check": "Read each named
  primary original and preserve fixed-order, score, memory and implementation assumptions
  before any identity or dominance claim.", "original": {"exact_original_object":
  {"id": "SSS-COMPARISON", "question": "Preserve SSS*, alpha-beta and their theoretical
  comparisons as primary-source questions; do not collapse DUAL* into SSS* or Minimin.",
  "reference_numbers": [1, 6, 8, 14, 15, 16], "status": "pending_original_reading"},
  "index": 5, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "fca7f5909a8f4850fc964aaf970961cb7ed28afb69fe44435515a1d1dad5c482", "pointer": "/source_questions/5"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The TR85-16 cover/title/page-count discrepancy
  remains unresolved and is not repaired by the new1985 proceedings reading.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "source_questions", "next_check": "Acquire or trace the original report and compare
  full text against the19-page rendering and1987 reproduction.", "original": {"exact_original_object":
  {"id": "TR85-16-VERSION", "question": "Inspect the linked19-page rendering titled
  Is Best First Search Really Best? (cover re-created22March2013 from2November1985
  files). Author index calls report TR85-16 Is Best First Search Best?, October1985,27pages.
  Treat this as a source/version discrepancy to trace, not an identical original27-page
  byte artifact.", "reference_numbers": [12], "status": "cover_only_route_read_full_text_pending",
  "url": "https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR85-16.pdf"}, "index":
  6, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "f8bf15125a920e5112389ff616b42ea8877bcb7a3a4cb91ee3b40f943a663d6e", "pointer": "/source_questions/6"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The new records make no reproduced timing
  claim. Deferred dissertation/thesis/report details and their differing cost models
  remain pending.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "journal1987", "kind": "source_questions", "next_check": "Inspect references10–12
  for exact generator, score range, sample protocol, implementation and timing denominators.",
  "original": {"exact_original_object": {"id": "EXPERIMENTAL-PROVENANCE", "question":
  "Inspect the1986 thesis and report for tree generator, integer range, ordering,
  timing setup and overhead definitions before any stronger performance claim or benchmark
  reproduction.", "reference_numbers": [10, 11, 12], "status": "pending_original_reading"},
  "index": 7, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "02ec15c55d2094ef20f3177adb2867f08d7868a2fa89e9bfbaa24b477b09606f", "pointer": "/source_questions/7"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Only selected regions of the18-page author
  rendering were compared with the full15-page journal reproduction; complete textual/mathematical
  equivalence remains unestablished.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "journal1987", "kind": "source_questions", "next_check": "Compare every
  section before using the alternate rendering as an equivalent full defining artifact.",
  "original": {"exact_original_object": {"artifacts": [{"path": "/private/tmp/aimech-low-overhead-sss-source-research-20261016/journal1987-author-hosted.pdf",
  "sha256": "cd73f50f0356a948ace89aea2dff7a1ef59d21c5a9c0fd349151931db2ed0bd0"}, {"path":
  "/private/tmp/aimech-low-overhead-sss-source-research-20261016/author-revised-rendering.pdf",
  "sha256": "3f297ccc3530ddde68cc1095cf1d97fa07fd9bea57f8b084eb960ad992580b87"}],
  "id": "AUTHOR-VERSION-COMPARISON", "question": "Compare all journal and author-rendering
  sections if their provenance is used beyond the selected cover/Figure3/Figure4 correspondence;
  partial matching does not establish complete textual or mathematical equivalence.",
  "status": "pending_complete_version_comparison"}, "index": 8, "origin": {"path":
  "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "e57b9e3d4127513576546c49b4685e64c8ecf4f1edea4157e622d9944ce3e02d", "pointer": "/source_questions/8"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The dual-cope-ijcai-2025 filename is an
  unread retrieval lead, not evidence for DUAL* identity or a related algorithm. Responsibility
  is newly attached to the existing main911 source umbrella for inspection.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "journal1987", "kind":
  "incidental_retrieval_contexts", "next_check": "Acquire the exact URL, verify title/version
  and read the method before any identity comparison; retain original source_catalog
  pointer63.", "original": {"exact_original_object": {"assessment": "A filename token
  is not a method identity. No equation, full paper or owner allocation is inferred;
  retain outside the selected1987 scope.", "exact_original_object": "https://www.cs.unh.edu/~ruml/papers/dual-cope-ijcai-2025.pdf",
  "group": 644, "pointer": "/source_catalog/pdf_links/63", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json",
  "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}, "status":
  "unassessed historical author-index retrieval context"}, "index": 0, "origin": {"path":
  "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/additional-source-context.json",
  "sha256": "29639a1ee0016588dc9b098ac97fc19171fe2c15274536f9d1da75f6ef2efb6c"}, "original_object_sha256":
  "6384fa88e0525401f70af5a4b48352cb89c48cf8deb6a60e07cee93889ce4fb9", "pointer": "/incidental_retrieval_contexts/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The ICAPS04 pns filename is an unread route.
  The pair incidental wrapper and PNS additional_context_questions[0] are the same
  URL/pointer, retained as two historical occurrences of one coordinated retrieval
  question.", "disposition": "pending_inspection", "existing_record_ids": [], "group":
  "journal1987", "kind": "incidental_retrieval_contexts", "next_check": "Acquire the
  exact author PDF and determine its PNS expansion before any method/identity claim;
  coordinate the two wrappers under main911.", "original": {"exact_original_object":
  {"assessment": "A filename token is not a method identity. No equation, full paper
  or owner allocation is inferred; retain outside the selected1987 scope.", "exact_original_object":
  "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf", "group": 645, "pointer":
  "/source_catalog/pdf_links/87", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json",
  "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}, "status":
  "unassessed historical author-index retrieval context"}, "index": 1, "origin": {"path":
  "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/additional-source-context.json",
  "sha256": "29639a1ee0016588dc9b098ac97fc19171fe2c15274536f9d1da75f6ef2efb6c"}, "original_object_sha256":
  "62ca6aee107b9685810dd72f3f2ab64d00d2f87272f239927c6aab204e55c9ad", "pointer": "/incidental_retrieval_contexts/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1981 Fishburn Technical Report431 is
  distinct from the1984 book cited by the1987 work.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography", "next_check":
  "Read this exact report and compare the book only after access; preserve separate
  versions and publication metadata.", "original": {"exact_original_object": {"authors_as_read":
  "J.P. Fishburn", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry1", "number": 1, "publication_reading": "University of Wisconsin
  Technical Report431, Madison, May1981", "qualification": "Distinct report reference;
  do not substitute the1984 book cited in1987.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_original_source_inspection", "title_reading": "Analysis of speedup in distributed
  algorithms"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "a3ce356df322beee360c80047a52beb3f64397605dd7f4e7b01b1b57aeb76fbb", "pointer": "/bibliography/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The Knuth–Moore alpha-beta original shares
  the explicit main911 source responsibility already present in ITERSSS* and the1987
  bibliography.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:ITERSSSStar"], "group": "ijcai1985", "kind": "bibliography", "next_check":
  "Inspect its exact algorithm/order/proof assumptions; coordinate all citation occurrences
  without treating Minimin alpha pruning as the same method.", "original": {"exact_original_object":
  {"authors_as_read": "D.E. Knuth and W. Moore", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry2", "number": 2, "publication_reading": "Artificial Intelligence6
  (1975),293–326", "qualification": "Original not read in this task.", "source": {"path":
  "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256":
  "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection",
  "title_reading": "An analysis of alpha-beta pruning"}, "index": 1, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "510766742f162452d804b4573bf171e90de4663a41eef517af3124c45aeb94e2", "pointer": "/bibliography/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Pearl1980 minimax-tree analysis matches
  the1987 citation family but is still an uninspected original, distinct from Pearl1984
  book context.", "disposition": "pending_inspection", "existing_record_ids": [],
  "group": "ijcai1985", "kind": "bibliography", "next_check": "Read the original and
  its stated assumptions; coordinate1985 and1987 occurrences while retaining both
  exact citations.", "original": {"exact_original_object": {"authors_as_read": "J.
  Pearl", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry3", "number": 3, "publication_reading": "Artificial Intelligence14
  (1980),113–138", "qualification": "Original not read in this task.", "source": {"path":
  "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256":
  "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection",
  "title_reading": "Asymptotic properties of minimax trees and game searching procedures"},
  "index": 2, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "a33784cfca3ccb574e7a8af6caf993eb2ed833eab06e29c71aa822b018aeaaf2", "pointer": "/bibliography/2"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The parallel strongly ordered game-tree
  article remains pending; the reconstructed1985 issue/year fields require verification
  against its original.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "bibliography", "next_check": "Read the original
  source and reconcile bibliographic reconstruction with1987 reference4; do not silently
  normalize ambiguous fields.", "original": {"exact_original_object": {"authors_as_read":
  "T.A. Marsland and M.S. Campbell", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry4", "number": 4, "publication_reading": "ACM Computing Surveys14,
  issue/year characters require verification; pages533–552", "qualification": "Selected
  reconstructed artifact issue field differs visually from1987 reference; no correction
  silently asserted.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_original_source_inspection", "title_reading": "Parallel search of strongly
  ordered game trees"}, "index": 3, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "5598efd743e0ea239eb3c53ebe78fb5f0976e319d1749a221ae2f529cdc71be2", "pointer": "/bibliography/3"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The original Reinefeld Scout improvement
  remains pending; the selected1985 reconstruction has uncertain issue/page characters.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985",
  "kind": "bibliography", "next_check": "Read the exact1983 source and verify bibliographic
  fields before asserting NegaScout/PVS equivalence.", "original": {"exact_original_object":
  {"authors_as_read": "A. Reinefeld", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry5", "number": 5, "publication_reading": "ICCA Journal6 (1983);
  issue/page rendering unclear", "qualification": "Selected artifact renders title/issue/page
  characters inconsistently; normalized Scout context is attributed, exact original
  image retained.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_original_source_inspection", "title_reading": "An improvement of the Scout
  tree search algorithm"}, "index": 4, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "6df363489669144f71df3b9d6c42c6f720d3ef8152000a7cbea64dd0128f2d0c", "pointer": "/bibliography/4"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Stockman SSS* already has main911 pending
  responsibility. The new PNS/INS/DUAL* and existing ITERSSS* procedures do not absorb
  its defining scope.", "disposition": "existing_pending_owner", "existing_record_ids":
  ["AIMech:ITERSSSStar"], "group": "ijcai1985", "kind": "bibliography", "next_check":
  "Inspect original SSS* and coordinate1985/1986/1987 citation occurrences while retaining
  each source object.", "original": {"exact_original_object": {"authors_as_read":
  "G.C. Stockman", "exact_visual_source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png",
  "sha256": "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry6", "number": 6, "publication_reading": "Artificial Intelligence12,2
  (1979),179–196", "qualification": "Original not read in this task.", "source": {"path":
  "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256":
  "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection",
  "title_reading": "A minimax algorithm better than alpha-beta"}, "index": 5, "origin":
  {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "ecd814b8f6d7b9213b5eff343a93fea6ace56b8a8d0fbc1070050b20190e8114", "pointer": "/bibliography/5"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1983 minimax comparison is the same
  citation family as1987 reference6 but remains a separate uninspected source.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "bibliography",
  "next_check": "Read exact comparators, score/order assumptions and empirical setup
  before any cross-paper performance conclusion.", "original": {"exact_original_object":
  {"authors_as_read": "M. Campbell and T.A. Marsland", "exact_visual_source": {"path":
  "/private/tmp/aimech-ins-pns-1985-source-research-20261016/page-04.png", "sha256":
  "51b480d00441adbf8f56cd6ab8c528e1776a89f08e47f094ff476e1e102dc291"}, "locator":
  "p1043 References, entry7", "number": 7, "publication_reading": "Artificial Intelligence20
  (1983),347–367", "qualification": "Original not read in this task.", "source": {"path":
  "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf", "sha256":
  "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status": "pending_original_source_inspection",
  "title_reading": "A comparison of minimax tree search algorithms"}, "index": 6,
  "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "cd078500a8476c7bf2e2f0da2900f04b5151535d730df772bc3660b7fdf3a88d", "pointer": "/bibliography/6"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1985 near-root/subtree description and1987
  first-level wording are preserved as source/version scope. Full1985 reading does
  not determine an unspecified general fixed retention depth.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check":
  "Seek an explicit PNS listing or author clarification of near-root retention across
  subtrees and versions.", "original": {"exact_original_object": {"current_owner":
  null, "id": "PNS-RETENTION-DEPTH", "locator": "p1041 Section3;1987p190", "question":
  "Clarify near-root prove-best retention for each subtree versus1987 first-level
  wording; do not assume an unspecified fixed depth.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 0, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "194dd2c01e2f3e0837f5560510ae2d9ddc556d87c295d5e67180dd74e85acdc2", "pointer": "/additional_questions/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1985 appendix specifies INS, not a full
  PNS implementation. The new PNS record deliberately leaves PV/bound retention and
  cache policy incomplete.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Find a primary
  PNS listing or author implementation for PV updates, bound validity, eviction and
  lifetime.", "original": {"exact_original_object": {"current_owner": null, "id":
  "PNS-PV-AND-BOUND-INTERFACE", "locator": "p1041 Section3; p1043 Appendix", "question":
  "Find a full PNS listing or author implementation defining PV retention, update,
  bound validity, eviction and cache lifetime. The1985 appendix is INS only.", "source":
  {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 1, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "b77523e0805467596b6467d1afedd80301da6982c7f600bce381b75becfccf70", "pointer": "/additional_questions/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Both source displays have now been inspected:1985
  has the explicit i<w guard, while1987 expresses the last-successor exclusion in
  a comment and adds a kind assignment. This observed difference does not certify
  executable/version equivalence.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Preserve the
  exact two listings and inspect author implementation/version history before executable
  claims.", "original": {"exact_original_object": {"current_owner": null, "id": "INS-1985-1987-DISPLAY",
  "locator": "p1043 Appendix;1987Figure3p191", "question": "Retain explicit1985 i<w
  guard and1987 comment-only guard plus the additional kind assignment; assess implementation/version
  correspondence before executable claims.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 2, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "ee54367185a8749b4dbbbc08c39e4532045ec63e193f78844719adb3c62db478", "pointer": "/additional_questions/2"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Reading both sources leaves GetInfo/SaveInfo/Sort
  and initial merit population delegated or incomplete.", "disposition": "pending_inspection",
  "existing_record_ids": [], "group": "ijcai1985", "kind": "source_questions", "next_check":
  "Seek exact storage and cache-miss conventions; do not patch either source silently.",
  "original": {"exact_original_object": {"current_owner": null, "id": "INS-SCORE-STORAGE",
  "locator": "p1043 Appendix;1987pp190–191", "question": "Resolve delegated GetInfo/SaveInfo/Sort
  and invisible initial score population, including cache misses and lifetime, without
  patching either source silently.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 3, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "79d48bec3db245ab4c8170c581058c8ccb9045ee03dc678d9062bd2afccd135a", "pointer": "/additional_questions/3"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The exact storage summation remains limited
  by reconstructed artifact clarity; the native PNS record makes no exact total-memory
  guarantee from it.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Acquire a clearer
  original scan before asserting exponent/index bounds or total implementation memory.",
  "original": {"exact_original_object": {"current_owner": null, "id": "INS-STORAGE-FORMULA-ARTIFACT",
  "locator": "p1041 Section3", "question": "Acquire a clearer original scan for the
  p1041 storage summation before claiming its exact exponent, index bounds or a total-memory
  guarantee.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 4, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "f4059c75601202310b571d5d10e0884249f2bc465daf606e357b1751a644b272", "pointer": "/additional_questions/4"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1985 and1987 timing descriptions use
  different denominators/context; no numeric synthesis follows from their joint reading.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985",
  "kind": "source_questions", "next_check": "Trace original implementation and timing
  definitions before comparing or combining results.", "original": {"exact_original_object":
  {"current_owner": null, "id": "TIMING-VERSION-COST-MODEL", "locator": "p1042 Section4–5;1987p198",
  "question": "Trace the differing1985/1987 timing denominators and implementation
  cost models before any numeric performance synthesis.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 5, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "3253f5ef8a0b970b73b135bb94ebff099259e6033ee0325e143574812d54c543", "pointer": "/additional_questions/5"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The1981 Fishburn report and1984 book remain
  separate source-version questions.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "source_questions", "next_check": "Inspect both
  originals and establish relevant minimal-window lineage rather than equating matching
  titles.", "original": {"exact_original_object": {"current_owner": null, "id": "FISHBURN-REPORT-BOOK",
  "locator": "p1043 reference1;1987p199reference3", "question": "Inspect1981 Technical
  Report431 separately from the1984 book cited by1987; determine relevant minimal-window
  provenance.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 6, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "499e8b2a2058d6ca85eef32163d3c59ac7ef68689ae52deb3b3537b16589cd45", "pointer": "/additional_questions/6"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Ambiguous reconstruction in1985 references4/5
  remains a bibliographic verification question despite the1987 cross-reference context.",
  "disposition": "pending_inspection", "existing_record_ids": [], "group": "ijcai1985",
  "kind": "source_questions", "next_check": "Verify the exact originals/images and
  record any correction explicitly; retain the original extracted objects.", "original":
  {"exact_original_object": {"current_owner": null, "id": "BIBLIOGRAPHIC-RECONSTRUCTION",
  "locator": "p1043 References; PDFmetadata", "question": "Verify reference4/5 issue/page/title
  fields against original bibliographies because the selected official ABBYY artifact
  has ambiguous reconstructed characters.", "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 7, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "b7fd6acb8dbbf53f76545a1f142975665eb9366f8db4916e9795b7f99b310272", "pointer": "/additional_questions/7"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The requested current identity/owner comparison
  has been performed for this exact362 collection: no normalized candidate collision,
  all328 matching contents read and current native/AIO contexts compared. This is
  bounded current evidence, not global novelty or proof-number-search equivalence.",
  "disposition": "retained_context", "existing_record_ids": [], "group": "ijcai1985",
  "kind": "source_questions", "next_check": "Recheck identity at any changed write
  base; keep the independent proof-number and PNMCTS source questions pending.", "original":
  {"exact_original_object": {"current_owner": null, "id": "PNS-CURRENT-IDENTITY",
  "locator": "Current research recommendation only; no new search performed", "question":
  "Run future ignored-inclusive record/frontier/AIO reconciliation for source-specific
  Partially Informed NegaScout, distinguishing INS, NS/PVS and unrelated PNS expansions.",
  "source": {"path": "/private/tmp/aimech-ins-pns-1985-source-research-20261016/ijcai1985.pdf",
  "sha256": "0c1363cd3e91c2d53f096cbdc1e61c1e6f14ebe29a24b60d733a6989c464744a"}, "status":
  "pending_source_or_current_identity_inspection"}, "index": 8, "origin": {"path":
  "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "62b0f8a65706f023a4e4cf5be0344cae208e4d8fbb8816faf8f79974b8eac57a", "pointer": "/additional_questions/8"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "This is the same ICAPS04 URL/pointer as
  journal1987 incidental_retrieval_contexts[1], with a different historical wrapper.
  Both occurrences remain exact; source identity is unestablished.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "additional_context_questions",
  "next_check": "Coordinate one retrieval/primary-method inspection under main911
  and determine the actual PNS expansion before relation claims.", "original": {"exact_original_object":
  {"exact_url": "https://www.cs.unh.edu/~ruml/papers/icaps-04-ws-pns.pdf", "future_owner":
  null, "next_check": "Acquire exact author-hosted PDF, verify title/version and which
  expansion of pns it uses; compare current identities only after method reading.",
  "origin": {"pointer": "/source_catalog/pdf_links/87", "source": {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261011T054555Z-best-first-search.json",
  "sha256": "4d527783af0e0f75abe1179df198f3c219ac161d272bb0f5316a329e8e6dd122"}},
  "question_id": "PNS-IDX-ICAPS04", "status": "pending_original_retrieval"}, "index":
  0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json",
  "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256":
  "a8b26fae214ca33ed5e0bfc82a3cda932e6e976a8a0cdca2d59fa87234f327f9", "pointer": "/questions/0"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Allis–van der Meulen–van den Herik1994
  Proof-number search is an independent PNS expansion known here only from metadata.
  It is not Partially Informed NegaScout.", "disposition": "pending_inspection", "existing_record_ids":
  [], "group": "ijcai1985", "kind": "additional_context_questions", "next_check":
  "Preserve the publisher403 route and obtain accessible full primary text before
  method/identity curation.", "original": {"exact_original_object": {"authors": ["L.V.
  Allis", "M. van der Meulen", "H.J. van den Herik"], "future_owner": null, "next_check":
  "Find accessible primary full text and assess defining proof/disproof mechanism
  before any record or identity decision. Preserve publisher403 route.", "origin":
  {"path": "/private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json",
  "sha256": "da8749d9822c729ba4f738166200878ee5722b5ae3b9bb79e5e8dd647fecb701"}, "publication":
  "Artificial Intelligence66(1),91–124,1994", "question_id": "PNS-ACRONYM-PROOF1994",
  "status": "metadata_only_primary_fulltext_pending", "title": "Proof-number search"},
  "index": 1, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json",
  "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256":
  "9679f5c773397a0fcb424a2f9b73667f10a5ef6d2c19abf71adef6549903b279", "pointer": "/questions/1"},
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The2022 proof-number/MCTS hybrid is a separate
  abstract-level primary lead, not evidence for this1985 PNS mechanism.", "disposition":
  "pending_inspection", "existing_record_ids": [], "group": "ijcai1985", "kind": "additional_context_questions",
  "next_check": "Read the full primary method and bibliography before any new record
  or equivalence decision.", "original": {"exact_original_object": {"future_owner":
  null, "next_check": "Read full primary method and source bibliography if this distinct
  hybrid is considered for discovery. The present task uses only acronym evidence.",
  "origin": {"path": "/private/tmp/aimech-pns-identity-mapping-proposal-20261016/proof-number-acronym-context.json",
  "sha256": "da8749d9822c729ba4f738166200878ee5722b5ae3b9bb79e5e8dd647fecb701"}, "question_id":
  "PNS-ACRONYM-PNMCTS2022", "status": "abstract_only_primary_fulltext_pending", "title":
  "Combining Monte-Carlo Tree Search with Proof-Number Search", "version": "arXiv:2206.03965v1"},
  "index": 2, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/additional-context-questions.json",
  "sha256": "97b07dd327617dfc06ab1b6f7498b6444a8d22dbb6d473d0a1df47a3e59259e3"}, "original_object_sha256":
  "20239e6c1faec3ac4c0bea96920436390c299dd94b405eac067d844ce497dcb3", "pointer": "/questions/2"},
  "responsible_owner": {"family": "main", "index": 911}}'
- 'Historical responsibility link journal1987: {"added_record_ids": ["AIMech:InformedNegaScout",
  "AIMech:DUALStar"], "assessment": "The exact Low overhead alternatives to SSS* reference7
  inherited from the1989 MA*/MAO* bibliography is represented by two distinct source-scoped
  records: INS and DUAL*. The full15-page1987 reproduction has been read. Main911
  is the existing source responsibility, not a claim that these algorithms equal MA*/MAO*,
  ITERSSS* or each other.", "disposition": "represented_by_added_record", "existing_record_ids":
  [], "next_check": "Retain all16 bibliography,9 source questions and2 incidental
  retrieval objects, together with independent1985/version/helper/lineage scopes;
  no source-family exhaustion or issue closure.", "original": {"exact_original_object":
  {"authors": "T. A. Marsland; A. Reinefeld; J. Schaeffer", "future_owner": null,
  "next_check": "Game-tree restricted-memory variants; original not freshly acquired/read.",
  "publication": "Artificial Intelligence31,185–199,1987", "reference_number": 7,
  "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Low overhead alternatives to SSS*"}, "index": 0, "origin": {"path": "/private/tmp/aimech-ins-dual-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "7d7f1f2077e3fffe8d88a9c72fcc68898045b5e375629185cc62c5e16c8afc85"}, "original_object_sha256":
  "12cd5640826b81734e4485f8d19bee015282545f694ef2d6681326f3de45192f", "pointer": "/exact_original_pointer_object/exact_original_object"},
  "responsible_owner": {"family": "main", "index": 911}}'
- 'Historical responsibility link ijcai1985: {"added_record_ids": ["AIMech:PartiallyInformedNegaScout"],
  "assessment": "The exact PNS-1985 original-reading question, also retained once
  as a1987 source-question occurrence, is represented by the separately defined1985
  Partially Informed NegaScout record following full official-paper reading. This
  is source-specific representation, not complete implementation/version resolution
  or a proof-number-search alias.", "disposition": "represented_by_added_record",
  "existing_record_ids": [], "next_check": "Retain all7 bibliography,9 source questions
  and3 additional context objects, including retention-depth, storage, score, timing
  and acronym boundaries. Preserve historical pending status only inside the exact
  original object.", "original": {"exact_original_object": {"id": "PNS-1985", "question":
  "Read Information acquisition in minimal window search (IJCAI1985,1040–1043), compare
  full INS/PNS procedure and source versions before any PNS identity or split.", "reference_numbers":
  [9], "status": "pending_original_reading"}, "index": 0, "origin": {"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/original-source-question-continuity.json",
  "sha256": "37b6b557c63e73e3d8d575acaa02f66b748a006a121c7478c9ede4b2cde487d4"}, "original_object_sha256":
  "f0f7c946f02d85a86271faa8e4a6ee94984a5405f8de87f3451275296ae1a070", "pointer": "/original_PNS1985_question"},
  "responsible_owner": {"family": "main", "index": 911}}'
- The exact full actual361 projection remains recursively accessible once under predecessor_state/projection,
  including its165 original objects,3 later access questions and2 restored tracking
  questions. Earlier402/404/406,356/357/358/359 obligations and360 scan-manifest bytes/all100
  asset metadata objects remain inherited. No source exhaustion or issue closure is
  asserted here.
- 'Inherited predecessor_state: exact object SHA256 b5bf2ccc458a00299fcec5f2bd9818a36fd3cb4be7d026364c12b24f4bf07bf8;
  original references remain under predecessor_state/projection/predecessor_state.'
- 'Inherited predecessor_state_sha256: exact object SHA256 8c3a464bcd3931025ca1ba4143c43bd408da7812eb3c4bee3a3d0146746d0957;
  original references remain under predecessor_state/projection/predecessor_state_sha256.'
- 'Inherited source_accounting: exact object SHA256 3ccb5df1a0fbf065471fa12c35f8b16b8dbbb700b3ab99c7039a93dd691d9fbc;
  original references remain under predecessor_state/projection/source_accounting.'
- 'Inherited frontier_result: exact object SHA256 88dc2e869fa9dad355e204ef421f1bf74e7a65082c69cc6d323d3dff7066849d;
  original references remain under predecessor_state/projection/frontier_result.'
- 'Approved access-attribution correction (issue415 tracking; no research closure):
  {"accepted_root_ref": {"path": "/private/tmp/aimech-cohort362-wording-correction-20261016/root-accepted-correction.json",
  "sha256": "bda7c17e335fe6a5ae8b852e620076a0f01c4c973de707c3edf2311fc29111d9"}, "exact_accepted_correction":
  {"accepted": true, "after": "The paper’s PNS stores relevant upper bounds only at
  the first level, and its footnote discusses NegaScout/PVS lineage. Those descriptions
  do not by themselves establish PNS as this full INS procedure, global PVS aliases,
  or equivalence to all later implementations. The 1985 original has been read separately;
  its version differences and the other cited lineage questions remain separately
  tracked.", "assessment": "Root freshly read all three selected definitions,16 claims
  and28 limitations and identified a stale present-tense access claim. Sibling356
  independently confirmed the exact defect in conversation. The earlier complete1985
  paper reading remains attributed to the accepted PNS scientific/native lineage.
  This correction updates access attribution only, preserving the unresolved1985/1987
  version correspondence and other cited lineage questions. No source exhaustion or
  algorithm defect is asserted.", "before": "The paper’s PNS stores relevant upper
  bounds only at the first level, and its footnote discusses NegaScout/PVS lineage.
  Those descriptions do not by themselves establish PNS as this full INS procedure,
  global PVS aliases, or equivalence to all later implementations; the cited originals
  remain pending.", "evidence": [{"path": "/private/tmp/aimech-pns-native-data-preparation-20261016/root-native-data-acceptance.json",
  "sha256": "c1ff1a62918393a360054de311f191f0879b68efed2baaf659b3ee61a169de77"}, {"path":
  "/private/tmp/aimech-pns-native-preview-20261016/root-native-preview-readback.json",
  "sha256": "9c653872bbea06f7c5754085da863c43a4ad8382952e2480daa698034a223579"}],
  "field": "limitations", "historical_preview": {"path": "/private/tmp/aimech-ins-dual-native-preview-20261016/InformedNegaScout.native-preview.json",
  "sha256": "732d869fc587033b0b23ca9616c326433b9dde75ad08df3082c0e7b942443aaa"}, "index":
  7, "issue": "https://github.com/CultureBotAI/AIMech/issues/415", "path": "data/curated/InformedNegaScout.yaml",
  "record_id": "AIMech:InformedNegaScout", "recorded_at": "2026-10-16T06:03:07.166585Z",
  "scope": "Only this precise limitation string may change from the accepted historical
  scientific payload; separately required current identity_notes and actual curation
  time remain permitted."}}'
- 'Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "changed_main_indexes":
  [911], "changed_nested_indexes": [], "historical_source_responsibility_links": 2,
  "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_source_objects":
  46, "source_object_counts": {"ijcai1985": {"additional_context_questions": 3, "bibliography":
  7, "source_questions": 9}, "journal1987": {"bibliography": 16, "incidental_retrieval_contexts":
  2, "source_questions": 9}}}'
- 'Actual source accounting digest (sorted compact JSON UTF-8): 095ee33fb7187ebb148606e6dd5e71040816932d169efa926315819fd2bdcfdd'
- 'Actual historical/current identity changes: [{"id": "AIMech:InformedNegaScout",
  "field": "identity_notes", "historical": "This proposal selects the1987 recursively
  informed NegaScout procedure: retained ignore-left regions and successor upper bounds
  influence later re-search. It does not collapse PNS, baseline NegaScout, Principal
  Variation Search, generic alpha-beta or all later INS implementations. The1985 official
  paper is an additional version question under separate review. Bare INS is source-local
  and omitted from global aliases. At the historical04:51–04:52UTC branch360 snapshot,
  all1243 record identities (801native/442AIO;4927 field occurrences/3766 normalized
  values) were compared without an exact normalized candidate collision. Four ignored/hidden-inclusive
  roots supplied749 distinct matching contents. The reading covers747 full contents
  plus all matching leaves in two large wrappers. This is prospective historical evidence,
  not future current-state clearance.", "current": "Current prewrite comparison at
  merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f on 2026-10-16 compared 1,246
  records (804 native, 442 pinned AIO), 4,937 identity-field occurrences and 3,774
  normalized values. Candidate identity collisions were empty; ITERSSS* was the sole
  normalized context match. Four explicit roots were searched with ignored and hidden
  files included, using literal source/name probes and separate word-bounded INS/PNS
  context probes. The 328 distinct complete matching contents were semantically reviewed,
  and all 602 occurrence references were mechanically reconstructed; the successor
  collection preserved their exact line multisets. This record selects the 1987 complete-information
  NegaScout procedure with recursive retained bounds and ignore-left/prove-best control.
  It remains distinct from the separately defined 1985 partial-information policy,
  baseline NegaScout/PVS, DUAL*, SSS* and memory-controlled ITERSSS*. INS is source-local
  and is not a global alias. The 1985 source has now been read separately; its correspondence
  to the 1987 helper/storage/retention descriptions and the other original lineage
  sources remain tracked. Main911 carries the existing source responsibility while
  retaining all earlier records and unresolved questions. The pinned 30-target AIO
  no-match assessment is retained with its historical reading scope; current identity
  clearance is bounded to the inspected corpus and explicit search roots, not global
  novelty.", "root_decision": "records/AIMech:InformedNegaScout/identity_notes"},
  {"id": "AIMech:DUALStar", "field": "identity_notes", "historical": "This proposal
  selects the1987 MAX-rooted dual-of-SSS* procedure with LIVE/SOLVED descriptors,
  maximum merit, increasing OPEN order and dual MAX/MIN transitions. It is distinct
  from INS, SSS*, generic mathematical duality and Hamiltonian dual averaging. The
  earlier parallel dual-ss* citation is lineage to inspect, not an exact alias. Bare
  DUAL is omitted; the literal name keeps its star. At the historical04:51–04:52UTC
  branch360 snapshot, all1243 record identities (801native/442AIO;4927 field occurrences/3766
  normalized values) were compared without an exact normalized candidate collision.
  Four ignored/hidden-inclusive roots supplied749 distinct matching contents. The
  reading covers747 full contents plus all matching leaves in two large wrappers.
  This is prospective historical evidence, not future current-state clearance.", "current":
  "Current prewrite comparison at merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f
  on 2026-10-16 compared 1,246 records (804 native, 442 pinned AIO), 4,937 identity-field
  occurrences and 3,774 normalized values. Candidate identity collisions were empty;
  ITERSSS* was the sole normalized context match. Four explicit roots were searched
  with ignored and hidden files included, using literal source/name probes and separate
  word-bounded INS/PNS context probes. The 328 distinct complete matching contents
  were semantically reviewed, and all 602 occurrence references were mechanically
  reconstructed; the successor collection preserved their exact line multisets. This
  record selects the 1987 MAX-rooted application of the dual of SSS*, with LIVE/SOLVED
  descriptors, increasing ordered merit and dual MAX/MIN rules. It is distinct from
  INS/PNS, SSS*, ITERSSS*, generic duality, dual averaging and the uninspected parallel
  dual-ss* or RecDual* formulations. Bare DUAL is omitted from aliases. Source-specific
  node-kind, parity, purge and tie interfaces remain explicit; no hard byte budget
  or full correctness certification is inferred. Main911 carries source responsibility
  without merging any of these identities. The pinned 30-target AIO no-match assessment
  is retained with its historical reading scope; current identity clearance is bounded
  to the inspected corpus and explicit search roots, not global novelty.", "root_decision":
  "records/AIMech:DUALStar/identity_notes"}, {"id": "AIMech:PartiallyInformedNegaScout",
  "field": "identity_notes", "historical": "This record draft denotes the particular
  partial-information NegaScout policy described in the official 1985 paper: prove-best
  information near each subtree root and the principal variation from its initial
  search. It does not identify all partial NegaScout policies, the complete-information
  1987 INS procedure, baseline NegaScout, Principal Variation Search, DUAL* or proof-number
  search. The source-local abbreviation PNS is omitted from global aliases because
  a separate primary publication explicitly uses PNS for Proof-Number Search. The
  1985 near-root-plus-path description and the 1987 first-level upper-bound description
  remain an unresolved version question. Historical comparison at 05:11–05:12 UTC
  on 2026-10-16 covered 801 native and 442 pinned AIO records at HEAD add2c806f6729c8599f4d5cfd6d75c7decde006c,
  with four ignored- and hidden-inclusive search roots. A separate subsequent comparison
  read the newly added SVPG, Iterative Expansion and ITERSSS* records and current
  main 911 source context. That bounded supplement does not constitute a new complete
  inventory or assign PNS a source owner. Full source and evidence limitations remain
  explicit.", "current": "Current prewrite comparison at merged base b5db0b5d88c5fdc5bdc920dedcb26b9b35af6a4f
  on 2026-10-16 compared 1,246 records (804 native, 442 pinned AIO), 4,937 identity-field
  occurrences and 3,774 normalized values. Candidate identity collisions were empty;
  ITERSSS* was the sole normalized context match. Four explicit roots were searched
  with ignored and hidden files included, using literal source/name probes and separate
  word-bounded INS/PNS context probes. The 328 distinct complete matching contents
  were semantically reviewed, and all 602 occurrence references were mechanically
  reconstructed; the successor collection preserved their exact line multisets. This
  record denotes the particular 1985 partial-information NegaScout policy retaining
  near-root prove-best information and the initial principal variation. It is distinct
  from the complete-information 1987 INS, baseline NegaScout/PVS, DUAL*, all possible
  partial policies and proof-number search. PNS remains omitted from global aliases.
  The 1985 near-root-plus-path and 1987 first-level descriptions remain an unresolved
  version/interface question despite completed reading of both selected primary sources.
  Main911 carries this separate source responsibility; the proof-number/MCTS and ICAPS04
  retrieval questions remain pending. The pinned 30-target AIO no-match assessment
  is retained with its historical reading scope; current identity clearance is bounded
  to the inspected corpus and explicit search roots, not global novelty.", "root_decision":
  "records/AIMech:PartiallyInformedNegaScout/identity_notes"}]'
```
