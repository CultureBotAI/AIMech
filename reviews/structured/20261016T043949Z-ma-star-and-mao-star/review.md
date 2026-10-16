# Scientific self-review of MA* and MAO*

- Review: 20261016T043949Z-ma-star-and-mao-star
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-16T04:39:40.362224Z
- Finished UTC: 2026-10-16T04:39:49.045663Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain MA* and MAO* as separate source-scoped DRAFT algorithms. Twelve claims and17 limitations preserve their different path/solution-graph mechanisms, memory measures, source control-flow questions and theorem scope. Exact current and inherited source responsibilities remain pending where appropriate; the canonical report durably binds the scan manifest and100 asset metadata objects.

## Scope And Provenance

Two exact current native records from accepted cohort360 creation; all selected claims and limitations assessed. Historical source and neighbor reading scopes remain separately attributed.

Selection: Exact AIMech:MAStar and AIMech:MAOStar.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 0da1b27de4ee552bc8fb16a083d0f91d2a093142.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MAStar | data/curated/MAStar.yaml | maintained | MA* |
| AIMech:MAOStar | data/curated/MAOStar.yaml | maintained | MAO* |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |
| just vendored-check | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |
| uv run --locked aimech check-source | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |
| just render | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |
| just render-check | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |
| git diff --check | passed | True | AIMech:MAStar, AIMech:MAOStar | Actual completed command exited0; exact output and timing retained. |

## Scientific And Domain Assessments

### MA*: separate-successor-bounds

evidence: supported. Targets: AIMech:MAStar.

The source distinguishes absent-successor versus all-successor minima explicitly. Do not collapse f and F or replace successor-specific estimates with SMA* single-node f.

For each node n, MA* stores g(n), depth d(n), and a remaining-cost estimate h(n,m) for each successor. It defines hf(n) as the minimum over successors absent from the explicit tree and hF(n) as the minimum over all successors; f(n)=g(n)+hf(n) is used for expansion selection and F(n)=g(n)+hF(n) for backed-up cost and pruning.

### MA*: selection-and-continuation

evidence: supported. Targets: AIMech:MAStar.

The displayed Select2 compares the new child against the savedGL and jumps directly to the goal test/expansion. This is stronger than merely saying minimum-f frontier search; it retains the exact phase order.

Select the OPEN node with minimum f, breaking ties toward greater depth, and save its value as GL. Generate its next most promising absent successor. If that child has f&lt;=GL, continue directly from it; otherwise perform bottom-up revision and the memory check before returning to global selection. A node with no ungenerated successors leaves OPEN for CLOSED.

### MA*: pathmax-and-branch-backup

evidence: supported. Targets: AIMech:MAStar.

The high-resolution diagnostic confirms h(m,q) in both sides of the assignment; the independent reviewer retracted its earlier index-reading error. This claim asserts the printed tree operations, not a general graph consistency theorem.

For a generated child m of n and q in S(m), pathmax raises h(m,q) to at least h(n,m)-c(n,m). Bottom-up revision increases a parent branch estimate h(q,p) to hF(p)+c(q,p) when that value is larger, recalculates the parent hF and F, and propagates the revision upward. Retained branch bounds carry information about subsequently pruned descendants.

### MA*: base-pruning-rule

evidence: supported. Targets: AIMech:MAStar.

The source maximum-F equality is the base stopping test. The added count&lt;=theta*MAX alternative belongs to the separate theta-pruning variant, so it is not imported here.

If count exceeds MAX after revision, repeatedly select the OPEN leaf with greatest F, breaking ties toward shallower depth. If its F equals the root F, stop pruning and return to selection; otherwise remove it, decrement count, reopen its parent from CLOSED if needed and recompute that parent’s hf and f. Base MA* does not stop pruning merely because count has fallen to MAX.

### MA*: source-memory-measure

evidence: supported. Targets: AIMech:MAStar.

The displayed count starts at zero with the root already present. The bound is retained as a source statement with its exact path-length definition, not independent certification or a portable allocator guarantee.

MAX denotes extra search storage. The paper states count&lt;=MAX+&#124;C*&#124;, with &#124;C*&#124; defined as the greatest length of a path whose f value is at most the optimal solution cost C*. This is a source-specific search-state count statement, conditional on the relevant quantity being finite, rather than a strict total-memory or byte cap.

### MA*: memory-endpoint-boundary

evidence: supported. Targets: AIMech:MAStar.

Both endpoint descriptions occur together with an explicit ordering distinction. This is identity/scope evidence, not a universal expansion-count or runtime improvement.

With sufficiently large MAX, pruning is avoided and the source describes A*-like operation with one successor generated at a time. With MAX=0 it describes an iterative-deepening-like procedure whose backed-up successor ordering differs from the cited IDA* comparator. These endpoint comparisons do not make the complete parameterized MA* procedure an alias of A* or IDA*.

### MA*: retained limitation 1

scope: supported. Targets: AIMech:MAStar.

MA-GRAPH-SCOPE: preserve the root-identified boundary. No constructed graph counterexample was executed or claimed.

The displayed MA* procedure is for trees. Its graph-extension paragraph asserts that pathmax removes CLOSED reopening, but a complete graph duplicate, cycle and improved-path update policy is not specified here; no general graph-search correctness guarantee is inferred from path-local monotonicity.

### MA*: retained limitation 2

scope: supported. Targets: AIMech:MAStar.

Q2: the retained geometric-cost reasoning example and independent bounded review challenge that inference without claiming failure on the finite puzzle experiments.

The source assumes admissible lower-bound heuristic estimates. Its infinite-graph termination argument uses finite positive individual arc costs, which alone do not exclude an infinite path with finite total cost. Unrestricted termination is not certified; finite relevant cost contours or suitable stronger premises would need a separate argument and are not attributed as printed assumptions.

### MA*: retained limitation 3

scope: supported. Targets: AIMech:MAStar.

Q3: distinguish source state-count convention from byte allocation; do not silently add missing root/bookkeeping terms to the author theorem.

MAX and count do not measure portable total machine memory. The root is present while count initializes to zero; successor estimates, node fields, OPEN/CLOSED structures and transient generation must be accounted for in an implementation. MAX=0 is not zero storage, and a finite MAX+&#124;C*&#124; statement requires a finite relevant &#124;C*&#124;.

### MA*: retained limitation 4

scope: supported. Targets: AIMech:MAStar.

The source explicitly attributes observed node-count differences to ordering and says IDA* can also be modified; that does not erase the full MA* identity.

MA* at its memory endpoints is not treated as exact algorithmic equivalence to maintained A* or IDA*. Different successor ordering, partial expansion and retained bounds can change its execution; no global duplicate-policy equivalence is asserted.

### MA*: retained limitation 5

scope: supported. Targets: AIMech:MAStar.

All five exact variant objects remain in the unchanged six-object source ledger; the sixth concerns MAO* refinements/endpoints.

MA*-PP, MA*-thetaP, MA*-phiP, MA*-MO and MA*-VO are retained named variant questions. Their admission, pruning, OPEN organization or secondary-storage choices are not silently included in the base procedure, asserted as aliases, or accepted as separate concepts.

### MA*: retained limitation 6

scope: supported. Targets: AIMech:MAStar.

The research receipt distinguishes ordinary Manhattan in the endpoint comparison from the modified estimates used for later comparisons. OCR/table limitations and full original visual reading remain attributed.

The reported experiments concern particular Fifteen Puzzle problems and heuristic settings. Later comparisons modify Manhattan estimates at nongoals, and node counts need not decrease monotonically with memory. No universal runtime, expansion-count improvement or benchmark replication is claimed.

### MA*: retained limitation 7

scope: supported. Targets: AIMech:MAStar.

Keep b and C* dependence and the simplified problem model; do not promote source O(MAX) wording to an unconditional complexity claim.

The worst-case savings analysis assumes a uniform b-ary unit-cost tree, zero heuristic and fixed solution depth. Its parameter-dependent node-generation calculation is not a graph-independent multivariate or wall-clock-runtime guarantee.

### MA*: retained limitation 8

scope: supported. Targets: AIMech:MAStar.

Q4: preserve actual artifact/version scope and all10 references, the conference question and two retrieval leads. A citation does not establish that its original was read.

Evidence is the inspected25-page third-party journal scan reproduction, not a publisher PDF. The1987 ELDECS conference paper was identified from author metadata but not acquired; its exact relationship to the journal version and the thesis/other referenced originals remains unresolved.

### MA*: retained limitation 9

scope: supported. Targets: AIMech:MAStar.

MA-PSEUDOCODE-INTERFACES: fresh200–201 visuals and197–201 text confirm that these guards/conventions are not explicit in the inspected display. This extends scope qualification only; the six positive MA* claims and original eight limitations remain unchanged.

The displayed pseudocode is not certified as a complete executable interface. Its upward revision queue has no explicit root-parent stopping guard, successor-minimum initialization for goals or dead ends is not fully spelled out, and no OPEN-empty failure return is displayed. These conventions remain source questions; no repair or general unsolvable-instance behavior is asserted.

### MA*: definition and concept kind

evidence: supported. Targets: AIMech:MAStar.

The definition identifies the source tree-search procedure through separate absent/all-successor bounds, expansion, branch revision and regeneration-aware pruning. It does not turn the subsequent graph-extension paragraph into a general duplicate-handling or reopening theorem, and it does not equate MAX with a hard total-memory cap.

A memory-controlled heuristic tree-search algorithm that stores separate lower bounds for absent and all successors, expands promising continuations, backs up successor costs, and prunes selected high-cost leaves while retaining bounds for regeneration.

### MA*: source identity and historical comparison

identity: supported. Targets: AIMech:MAStar.

Use literal MA* with no expanded-name or endpoint aliases. The selected tree procedure is distinguished from MREC, SMA*, ITS, A*, IDA* and RBFS-family search by its successor-specific f/F bookkeeping, saved-GL continuation and base pruning stop. The 797-native/442-AIO inventory and four-root ignored-inclusive searches are historical branch358 observations. The provisional ID and exact local spelling require a new current-state check before any addition.

This specific selection, f/F bookkeeping, continuation, backup and pruning procedure differs from maintained MREC, SMA*, ITS, A*, IDA* and RBFS-family methods. An endpoint resemblance or common best-first ancestry is not an exact identity. Use the literal source name. No expansion such as Memory-Available A* is asserted from an unverified source spelling; named variants and large/zero-memory endpoints are not aliases. This is a source-scoped prospective draft, with a provisional local ID only. The observed branch358 inventory contained797 native and442 pinned AIO records; candidate exact/local IDs, names, aliases and scoped synonyms were mechanically compared with no normalized collision. Ignored/hidden-inclusive searches covered four roots; fourteen selected native contexts and22 full AIO nodes/133 relations were read with exact scope in the bound proposal. This historical snapshot does not substitute for eventual fresh identity and owner review.

### MA*: bounded AIO no-match assessment

grounding: supported. Targets: AIMech:MAStar.

Retain the bounded aio_no_match proposal. In the inspected pinned snapshot, neural memory layers/LLMs, classification trees, training/task classes and mathematical min/max functions do not denote this resource-controlled tree-search procedure. Cost-bound revision alone does not establish learned-from-data or reinforcement-learning scope. All 22 target-specific rejection reasons remain exact; this is a curator assessment over the disclosed scope, not proof of global ontology absence.

Historical branch358 snapshot: pinned AIO commit397851c547d1c4d8f06ef184f63c1d40bc86937a, SHA256 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6. All442 CLASS identity/synonym fields mechanically compared and class labels read;22 selected full nodes and all133 incident relations inspected. Other definitions and external definition-source papers were not all reread. This is a bounded pinned-snapshot mapping proposal requiring reassessment at eventual curation.

### MA*: standalone boundary and unresolved source questions

scope: supported. Targets: AIMech:MAStar.

Retain MA* as a standalone source-defined procedure, separate from MAO* and from its own MA*-PP, thetaP, phiP, MO and VO questions. Large/zero-memory resemblances to A*/IDA* do not establish whole-procedure equivalence. The unchanged bibliography and variant ledger continues to carry the uninspected-original/version questions.

Retain proposal only; no source-owner closure, record allocation or ontology restructuring is performed.

### MAO*: marked-partial-solution-graph

evidence: supported. Targets: AIMech:MAOStar.

The source changes the objective from a least-cost path to a least-cost solution graph. Its explicit acyclic scope is retained; this does not import general cyclic AND/OR search.

MAO* operates on an acyclic structure of pure AND and OR nodes. It maintains a marked partial solution graph rooted at the start and expands a nonterminal tip of that marked structure. When the start is labelled SOLVED, the marked structure is returned as the solution graph.

### MAO*: single-or-all-and-generation

evidence: supported. Targets: AIMech:MAOStar.

This keeps A/N as per-arc/per-node space units, not two counters or a node-only cap. The original paper stores estimates for all immediate successors, including ungenerated ones.

Expansion generates the marked successor arc of an OR node, or all successor arcs of an AND node. Existing explicit nodes are reused and only missing nodes are created. Newly created nodes receive f=h; their successor-specific bounds start from their node f at OR nodes and zero at AND nodes. MEMORY increases by A per generated arc and N per new node, where A and N are the source’s storage costs.

### MAO*: monotone-cost-backup-with-source-gap

evidence: supported. Targets: AIMech:MAOStar.

Q1 is in the asserted claim itself: the intended prose/example backup is supported, while literal executable completeness is withheld. No new pseudocode line is supplied and no universal claim about implementations is made.

The source describes revising a successor-specific bound with the child f plus arc cost and raising node f only when the newly aggregated cost is greater. OR aggregation takes a minimum; AND aggregation uses the problem’s Phi operation, with sum and maximum given as examples. The displayed expansion includes the branch update, but the later parent-revision queue does not explicitly show every parent-arc refresh needed by the prose and worked trace.

### MAO*: marking-solved-and-parent-propagation

evidence: supported. Targets: AIMech:MAOStar.

These are the literal marking and queue guards. The separate parent-arc refresh gap remains binding; describing queued parents does not silently certify full cost propagation.

For an OR node, mark a minimum-bound successor, preferring a SOLVED child and then the currently marked child when ties remain; label the parent SOLVED when its marked child is present and SOLVED. At an AND node mark all successors and label it SOLVED when all are present and SOLVED. Cost revision processes descendants before ancestors and queues marked parents when a node’s f changes or it is labelled SOLVED.

### MAO*: unmarked-arc-and-orphan-pruning

evidence: supported. Targets: AIMech:MAOStar.

The initial choice is some eligible unmarked OR arc; later suggestions to choose the largest branch bound are not imported. The no-eligible-arc exit matters because protected solution storage can exceed MAX.

When memory exceeds MAX and the root is not SOLVED, choose an unmarked outgoing arc of an OR node for pruning. Remove that arc and recursively remove nodes and their outgoing arcs only when they become parentless; shared nodes with remaining parents are retained. Stop when no eligible arc exists or MEMORY&lt;=theta*MAX. This protects the marked partial solution structure.

### MAO*: solution-graph-memory-scope

evidence: supported. Targets: AIMech:MAOStar.

This preserves the author-defined units and formula as a stated result. The finiteness, bookkeeping and control-flow qualifications remain; no byte-level implementation bound or proof certification is supplied.

The paper states a bound MAX+&#124;C*&#124;, where &#124;C*&#124; is the maximum storage required by a partial solution graph of pathmax cost at most optimal solution cost C*. This solution-graph quantity differs from the path-length quantity used for MA*. The stated post-pruning bound is max(MAX,&#124;C*&#124;), not an unconditional hard MAX cap.

### MAO*: retained limitation 1

scope: supported. Targets: AIMech:MAOStar.

The source explicitly excludes ordinary graphs with loops for MAO*. Imported reference4 supplies additional setting details not freshly investigated here.

The inspected procedure is for acyclic AND/OR graphs with pure node types and a specified problem-cost aggregation. It is not a general cyclic-graph version of MA*, and the examples sum/max do not certify arbitrary aggregation operators or imported uninspected AO* assumptions.

### MAO*: retained limitation 2

scope: supported. Targets: AIMech:MAOStar.

Q1: the trace raises A-to-B from3 to5 when B rises from2 to4 with unit arc cost. The independent reviewer agrees with this bounded source fidelity issue.

The parent-arc refresh in cost propagation is not fully explicit in the printed pseudocode: updated child f values queue marked parents, whose aggregation reads stored successor-specific bounds. The prose and Figure2 require a refreshed parent branch bound. This omission/implicit-operation question is retained without silently repairing the algorithm or asserting that every implementation is wrong.

### MAO*: retained limitation 3

scope: supported. Targets: AIMech:MAOStar.

Q2: retain the independent geometric-cost reasoning boundary. This is not an execution or a new proof of the author’s finite-instance statements.

The source’s positive-individual-arc-cost argument does not by itself establish termination on arbitrary infinite graphs, because bounded-cost infinite paths can exist. Its finite zero-cost and game-tree statements are also not independently certified here. No missing uniform lower-bound or finite-contour premise is falsely attributed to the printed theorem.

### MAO*: retained limitation 4

scope: supported. Targets: AIMech:MAOStar.

Q3: source units differ from MA* count/path length. Preserve &#124;C*&#124; as maximal relevant partial-solution storage and require finiteness before interpreting it as a finite bound.

A and N represent per-arc and per-node storage in the source model. Marked solution structure can remain after pruning when no eligible unmarked arc exists, and expansion precedes the memory check. Successor estimates, data structures and transient allocations require implementation accounting; MAX=0 is not zero memory and MAX is not a strict total byte cap.

### MAO*: retained limitation 5

scope: supported. Targets: AIMech:MAOStar.

Keep the source’s uniform-tree/zero-heuristic comparison context and no theorem-certification boundary; source O(MAX) wording is not a standalone implementation guarantee.

Theorem3.6 states analogous node-generation savings for AND/OR trees using the preceding simplified MA* analysis. It does not establish a general runtime bound, unrestricted graph efficiency or a universal monotonic benefit from increasing memory.

### MAO*: retained limitation 6

scope: supported. Targets: AIMech:MAOStar.

Avoid transferring ordinary-search tables to the AND/OR algorithm. No author code or experiment was run.

The numerical Fifteen Puzzle study evaluates MA* and its pruning variants, not an empirical benchmark of MAO*. The article’s possible game-tree and alternative-pruning uses do not supply a measured general MAO* performance advantage.

### MAO*: retained limitation 7

scope: supported. Targets: AIMech:MAOStar.

Preserves the sixth named-variant/endpoints object plus relevant bibliography references, without changing future responsibility.

The MAX=0 iterative-deepening behavior, large-MAX AO*/MarkA-like cases, possible game-tree SSS* relationships and proposed alternate pruning policies remain scoped source questions. They are not aliases, accepted independent concepts or an inspection of the cited original algorithms.

### MAO*: retained limitation 8

scope: supported. Targets: AIMech:MAOStar.

Q4: the source manifest hash is explicit. All10 bibliography objects, six variant questions, two retrieval leads and conference question remain unchanged.

Evidence is the inspected25-page public third-party reproduction of the journal article. No publisher PDF byte identity is established; the1987 conference full text and thesis were not acquired, and the exact version relationship or potential primary clarification of the backup display remains unresolved.

### MAO*: definition and concept kind

evidence: supported. Targets: AIMech:MAOStar.

The definition retains acyclic pure AND/OR solution-graph search, a marked partial solution structure and unmarked-arc/orphan pruning. It describes the intended source mechanism while the explicit parent-arc refresh question remains in the claim and limitations; no complete executable implementation is certified.

A memory-controlled heuristic search algorithm for acyclic AND/OR graphs that expands a marked partial solution graph, revises lower-bound costs through OR selection and AND aggregation, and prunes unmarked OR arcs with newly orphaned descendants while preserving the marked structure.

### MAO*: source identity and historical comparison

identity: supported. Targets: AIMech:MAOStar.

Use literal MAO* with no alias to MA*, AO*, cyclic AND/OR algorithms, importance-sampling AOAS or later modified cutoff variants. Its objective and marking/arc-pruning state distinguish it from ordinary path search. The bound 797-native/442-AIO inventory is historical, not evidence of current absence. The provisional ID and its local spelling require a new current-state check before addition.

The marked AND/OR solution structure, successor-specific bounds, AND/OR generation and arc/orphan pruning differ from the ordinary-path MA* procedure and maintained importance-sampling AOAS. The source’s relation to AO* is a refinement context, not an established alias. Use the literal source name. Do not merge MAO* with MA*, AO*, cyclic AND/OR algorithms or the modified cutoff variant. This is a source-scoped prospective draft, with a provisional local ID only. The observed branch358 inventory contained797 native and442 pinned AIO records; candidate exact/local IDs, names, aliases and scoped synonyms were mechanically compared with no normalized collision. Ignored/hidden-inclusive searches covered four roots; fourteen selected native contexts and22 full AIO nodes/133 relations were read with exact scope in the bound proposal. This historical snapshot does not substitute for eventual fresh identity and owner review.

### MAO*: bounded AIO no-match assessment

grounding: supported. Targets: AIMech:MAOStar.

Retain the bounded aio_no_match proposal. An acyclic AND/OR decomposition with cost aggregation is not thereby a probabilistic graphical model, graph neural network, classifier, memory-augmented LLM or reinforcement-learning method. Data representations and component min/max operations do not identify the algorithm. All 22 rejection reasons remain exact and require reassessment at eventual curation.

Historical branch358 snapshot: pinned AIO commit397851c547d1c4d8f06ef184f63c1d40bc86937a, SHA256 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6. All442 CLASS identity/synonym fields mechanically compared and class labels read;22 selected full nodes and all133 incident relations inspected. Other definitions and external definition-source papers were not all reread. This is a bounded pinned-snapshot mapping proposal requiring reassessment at eventual curation.

### MAO*: standalone boundary and unresolved source questions

scope: supported. Targets: AIMech:MAOStar.

Retain MAO* separately from MA* because marked AND/OR solution graphs, per-arc/per-node accounting and orphan-aware arc pruning change both objective and state. AO*/MarkA-like endpoints, game-tree SSS* relations and alternate pruning policies remain scoped questions. Do not transfer MA* Fifteen Puzzle results as empirical evidence for MAO*.

Retain proposal only; no source-owner closure, record allocation or ontology restructuring is performed.

### Actual canonical correspondence, current ownership and durable source preservation

provenance: supported. Targets: AIMech:MAStar, AIMech:MAOStar.

Actual records retain12 claims and17 limitations, two source rows and one shared defining JSON scan-manifest artifact. Five exclusive creation outputs and one CREATE event are bound. Exact38592-byte manifest recovery and all100 asset metadata/hash/provenance objects are verified from the canonical report. Current dynamic owner changes and additions exactly follow the accepted plan: {"additional_source_question_count": 0, "bibliography_occurrences": 10, "changed_main_indexes": [911], "changed_nested_indexes": [], "conference_version_questions": 1, "historical_source_responsibilities": 2, "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_variant_questions": 6, "retrieval_questions": 2, "source_qualifications": 6}. Ten bibliography, six variant, two retrieval, one1987 version, two historical responsibility and six source-qualification objects remain distinct. The complete actual359 predecessor projection preserves original402/404/406 and356/357/358/359 source responsibilities. 68 unique captured inputs, actual parsed generated pages and six successful required checks are bound. No source exhaustion, independent approval, issue closure or publication result is implied.

Actual canonical records, source questions, inherited source responsibilities, exact manifest bytes, all100 asset metadata entries and capture/check receipts were assessed at their recorded times. Historical source reading remains separately attributed. Review save, exact-head review, publication and merge are subsequent steps.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:MAStar. Retain MA* as a standalone source-defined procedure, separate from MAO* and from its own MA*-PP, thetaP, phiP, MO and VO questions. Large/zero-memory resemblances to A*/IDA* do not establish whole-procedure equivalence. The unchanged bibliography and variant ledger continues to carry the uninspected-original/version questions.
- retain: AIMech:MAOStar. Retain MAO* separately from MA* because marked AND/OR solution graphs, per-arc/per-node accounting and orphan-aware arc pruning change both objective and state. AO*/MarkA-like endpoints, game-tree SSS* relations and alternate pruning policies remain scoped questions. Do not transfer MA* Fifteen Puzzle results as empirical evidence for MAO*.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ma-mao-primary-scan | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Journal printed pp.197–221; public reader pp.1–25 | supports | Shared defining journal article inspected through 25 original public-reader scan images. The hash identifies the exact JSON bundle manifest, not a publisher PDF. Source reading is inherited with explicit attribution. |
| ma-mao-source-durability | /private/tmp/aimech-ma-mao-review-fragments-20261016/source-durability.fragment.json; canonical_report_payload and future_acceptance_requirements | context_only | Prepared durable-source payload and requirements only. No canonical persistence or completed source verification is asserted. |
| ma-mao-accepted-support | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json; records, source_qualification_objects and reading_attribution | context_only | Accepted scientific support for the 12 claims and 17 limitations. This fragment assembly is by an earlier author, not a new independent primary-source review. |
| ma-mao-root-preview-readback | /private/tmp/aimech-ma-mao-native-preview-20261016/root-preview-readback.json; records and limitations | context_only | Actual prior TEMP preview readback. Validation establishes representation correspondence only, not current identity, ownership or source durability. |
| ma-mao-source-questions | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/source-question-continuity.json; original_objects, added_boundary | context_only | Exact original ten citations, six named variant questions, two retrieval leads, conference relationship question and graph boundary remain pending by their retained objects. New research does not rewrite these historical objects. |
| ma-mao-interface-question | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json; complete source interface qualification | context_only | Root-parent termination, successor-minimum initialization and OPEN-empty failure conventions remain qualified; the display is not certified as executable code. |
| ma-mao-identity-mapping | /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/handoff.final.json; source-scoped historical identity and no-match proposal | context_only | Prior ignored/hidden-inclusive four-root search and bounded native/AIO comparison, not a current absence conclusion. |
| ma-mao-root-identity-mapping | /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/root-prospective-identity-mapping-reading.json; scope and prospective drafting acceptance | context_only | Root prospective mapping/name reading; it explicitly withholds future current-state identity, ownership and canonical approval. |
| reading-researcher-prior-full25-scan-and-ocr | /private/tmp/aimech-ma-mao-original-source-research-20261016/manual-reading.json; exact declared reading and limits | context_only | Inherited reading receipt; its original actor and fresh-versus-prior scope remain controlling. No new full-paper reading is asserted during this DATA assembly. |
| reading-independent-bounded-controlflow-math | /private/tmp/aimech-ma-mao-independent-controlflow-audit-20261016/assessment.v2.json; exact declared reading and limits | context_only | Inherited reading receipt; its original actor and fresh-versus-prior scope remain controlling. No new full-paper reading is asserted during this DATA assembly. |
| reading-root-bounded-science | /private/tmp/aimech-ma-mao-original-source-research-20261016/root-bounded-scientific-reading.json; exact declared reading and limits | context_only | Inherited reading receipt; its original actor and fresh-versus-prior scope remain controlling. No new full-paper reading is asserted during this DATA assembly. |
| reading-identity-mapping-researcher | /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/manual-reading.json; exact declared reading and limits | context_only | Inherited reading receipt; its original actor and fresh-versus-prior scope remain controlling. No new full-paper reading is asserted during this DATA assembly. |
| reading-additional-fresh-interface-check | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json; exact declared reading and limits | context_only | Inherited reading receipt; its original actor and fresh-versus-prior scope remain controlling. No new full-paper reading is asserted during this DATA assembly. |
| ma-accepted-preview | /private/tmp/aimech-ma-mao-native-preview-20261016/MAStar.preview.json; complete scientific fields; curation is prior TEMP-only provenance | context_only | Exact accepted native preview with provisional source-scoped identity. Future current identity/owner, curation time and canonical correspondence remain unset. |
| ma-claim-1-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section2.2, Definition2.2, printed p.199 / reader p.3; Algorithm MA* initialization on p.200 / reader p.4 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-claim-2-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section2.2 and Algorithm MA*, printed pp.199–201 / reader pp.3–5, steps2–7 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-claim-3-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.199–201 / reader pp.3–5, pathmax display and step6 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-claim-4-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Algorithm MA*, printed p.201 / reader p.5, steps7–8; theta variant on p.205 / reader p.9 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-claim-5-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.198–200,204 / reader pp.2–4,8; definition of &#124;C*&#124;, initialization and Theorem2.10 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-claim-6-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section2.3.1, printed p.205 / reader p.9 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| ma-limitation-1-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed p.201 / reader p.5, paragraph following Algorithm MA* | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-2-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Assumption2.1 on p.199 / reader p.3; Theorem2.7 and proof on pp.202–203 / reader pp.6–7 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-3-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.199–200,204 / reader pp.3–4,8 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-4-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section2.3.1, printed p.205 / reader p.9 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-5-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.204–205,210–211,220–221 / reader pp.8–9,14–15,24–25 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-6-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section2.3.2–2.4 and Tables1–4, printed pp.205–210 / reader pp.9–14 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-7-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.205–207 / reader pp.9–11, worst-case analysis and Theorem2.12 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-8-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Journal pp.197–221 / reader pp.1–25; received/revised dates on p.221; author bibliography conference entry | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-limitation-9-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.198–201 / reader pp.2–5; successor minima, initialization/selection and step6 parent queue | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| ma-definition-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Sections2.1–2.2, printed pp.198–201 / reader pp.2–5 | supports | Prior primary-source reading supports the selected procedural definition with the retained limitations. |
| mao-accepted-preview | /private/tmp/aimech-ma-mao-native-preview-20261016/MAOStar.preview.json; complete scientific fields; curation is prior TEMP-only provenance | context_only | Exact accepted native preview with provisional source-scoped identity. Future current identity/owner, curation time and canonical correspondence remain unset. |
| mao-claim-1-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section3–3.1, printed pp.211–213 / reader pp.15–17, initialization, termination and step3.1 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-claim-2-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Algorithm MAO*, printed pp.212–213 / reader pp.16–17, steps1 and3.2 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-claim-3-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Section3.1 prose on p.212; steps3.2(vi),4.2 on pp.213–214; Figure2(f)–(g) on p.216 / reader pp.16–18,20 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-claim-4-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Algorithm MAO*, printed pp.213–214 / reader pp.17–18, steps4.2.1–4.2.3 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-claim-5-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Algorithm MAO*, printed p.214 / reader p.18, steps5–6 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-claim-6-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Theorem3.5 and proof, printed p.219 / reader p.23; game-tree discussion on p.220 / reader p.24 | supports | Prior inspected scan passages support this source-specific claim; retain all associated scope qualifications. |
| mao-limitation-1-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.211–212,214,219 / reader pp.15–16,18,23 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-2-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.212–214,216 / reader pp.16–18,20, Section3.1, steps3.2(vi)/4.2 and Figure2(f)–(g) | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-3-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Theorem3.4 and proof, printed pp.218–219 / reader pp.22–23 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-4-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.212–214,219 / reader pp.16–18,23 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-5-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.205–207,219 / reader pp.9–11,23 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-6-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.205–210,219–220 / reader pp.9–14,23–24 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-7-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Printed pp.219–220 / reader pp.23–24 | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-limitation-8-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Journal pp.197–221 / reader pp.1–25; author bibliography and source-acquisition receipts | supports | Source passage and attributed bounded reasoning establish the need to retain this limitation; this is not a new canonical defect finding. |
| mao-definition-source | /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json; Sections3–3.1, printed pp.211–214 / reader pp.15–18 | supports | Prior primary-source reading supports the selected procedural definition with the retained limitations. |
| actual-write | /private/tmp/aimech-cohort360-write.json | context_only | Actual exclusive creation of two native records, report pair and CREATE history. |
| captured-inputs | /private/tmp/aimech-cohort360-postwrite-20261016/actual-capture.json | context_only | Actual canonical input-byte and maintained-target capture. |
| postcapture-reading | /private/tmp/aimech-cohort360-postwrite-20261016/root-generation-reading.json | context_only | Actual root reading of source-scoped canonical records, metadata and all retained question objects; historical source reading stays separately attributed. |
| governance-assessment | /private/tmp/aimech-cohort360-governance-20261016/assessment.json | context_only | Actual byte preservation, dynamic owner-plan reconstruction, inherited metadata and parsed-page audit. |
| rendered-pages | /private/tmp/aimech-cohort360-governance-20261016/rendered-pages.json | context_only | Actual generated-page bytes and parsed content; no visual/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort360-actual-adversarial-review-20261016/assessment.preliminary.json | context_only | Actual record scientific assessment with its own attributed source-reading scope. |
| current-identity-collection | /private/tmp/aimech-cohort360-current-collection-20261016/collection.json | context_only | Actual scoped ignored-inclusive identity collection; mechanical capture is distinct from human semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort360-current-identity-audit-20261016/assessment.json | context_only | Actual attributed current identity and source-question assessment. |
| root-decisions | /private/tmp/aimech-cohort360-final-inputs-20261016/decisions.json | context_only | Exact current record identity decisions, dynamic accepted ownership and retained source questions. |
| ownership-plan | /private/tmp/aimech-cohort360-current-ownership-proposal-20261016/ownership-plan.proposed.json | context_only | Exact shared-source responsibilities:10 bibliography,6 variants,2 retrieval questions,1 conference-version object,2 historical responsibilities and6 source qualifications; current additional questions remain explicit. |
| ownership-plan-acceptance | /private/tmp/aimech-cohort360-final-inputs-20261016/ownership-acceptance.json | context_only | Actual root acceptance of current source responsibility; no whole-issue closure. |
| current-discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T042347Z-ma-star-and-mao-star.json | context_only | Canonical durable report containing the exact recursively queryable predecessor_state bundle and separate current pair source responsibilities. |
| durable-source-manifest | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T042347Z-ma-star-and-mao-star.json | context_only | Actual canonical source_durability embeds the reconstructible exact JSON manifest and all100 original asset metadata/provenance objects. SHA-256 does not identify a publisher PDF. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/ma-star-and-mao-star/2026-10-16T042411Z-codex-a6f975.yaml | context_only | Actual single CREATE event for the report. |
| review-support | /private/tmp/aimech-cohort360-consumer-preparation-20261016/review-support.prepared.json | context_only | Exact historical per-claim and per-limitation narrative support. |
| check-gate | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-gate.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-vendor | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-vendor.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-check-source | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-check-source.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-render.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-render-check | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-render-check.json | context_only | Actual completed required command, exit0; scope is its recorded output. |
| check-diff | /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-diff.json | context_only | Actual completed required command, exit0; scope is its recorded output. |

## Limits And Additional Notes

- Scientific transfer uses exact accepted previews and attributed source/control-flow/mathematical reading. No new full25-page visual reading or native validation is claimed by this preparation.
- MA* tree/graph and executable-interface boundaries, MAO* parent-arc propagation question, positive-individual-cost theorem limits and distinct memory units remain explicit.
- Evidence is one exact JSON manifest of25 third-party scan pages. No publisher PDF byte identity or inspected1987 conference full text is asserted.
- Ten bibliography entries, six variants, two retrieval leads and the1987 version question remain separate from two historical responsibilities and six source qualifications; source questions are not automatically concepts.
- The complete actual359 projection retains prior issue/source scopes recursively. Additional current questions must be explicitly retained.
- Actual five creation outputs, one CREATE history, 68 capture inputs and 6 parsed generated pages are bound. Six required commands passed; earlier failed attempts remain explicit. Canonical review save/check and publication are subsequent operations.
- The37 scientific assessments and46 evidence templates retain accepted static-fragment content. The38th assessment now records actual current governance supported by the bound receipts.
- Local evidence access instants are filled from the actual attributed postcapture reading. Primary acquisition times preserve their historical instants and are normalized to UTC Z. References to preparation in the retained scientific limitations describe the historical fragment scope.
- The source manifest exact bytes and all100 asset metadata/provenance objects must be reconstructed from the canonical report and verified at capture, save and exact-head stages.
- Original source question objects and all Q1–Q4/graph/interface boundaries remain queryable; no issue closure or discovery exhaustion is asserted.
- One shared journal source retains ten bibliography entries, six named variant questions, two retrieval leads and one 1987 version question. Two historical responsibility objects and six source qualifications remain separate; no count asserts new concepts.
- {"added_record_ids": [], "assessment": "The 1985 Bagchi–Mahanti article supplies the C, PropC and MarkA comparison/theory question. It is retained under the current memory-search source umbrella; neither the MA*/MAO* pair nor a shared best-first vocabulary establishes those source identities.", "disposition": "pending_inspection", "exact_original_object": {"authors": "A. Bagchi; A. Mahanti", "future_owner": null, "next_check": "C,PropC,MarkA comparison/theory; resolve exact definitions from original if needed.", "publication": "JACM32,1–27,1985", "reference_number": 1, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Three approaches to heuristic search in networks"}, "existing_record_ids": [], "group": "journal1989", "index": 0, "kind": "bibliography", "next_check": "Read the exact 1985 original and compare C, PropC and MarkA definitions, inherited bounds and assumptions; reconcile any narrower current owner before further curation.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "bac149ea23ebbaf47bbb94b9f73f3469cd6d72aa310765b08b4a90b362e7071f", "pointer": "/references/0", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The AAAI1986 game-tree article remains a separate ITERSSS* source responsibility. A prospective TEMP draft/native preview is not a maintained record in this captured 1241-record inventory and does not authorize an ownership resolution here.", "disposition": "pending_inspection", "exact_original_object": {"authors": "S. Bhattacharyya; A. Bagchi", "future_owner": null, "next_check": "ITERSSS* source question; inspect defining paper before identity or relation decision.", "publication": "AAAI1986,163–167", "reference_number": 2, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Making the best use of available memory when searching game trees"}, "existing_record_ids": [], "group": "journal1989", "index": 1, "kind": "bibliography", "next_check": "Keep the exact historical reference and compare any later accepted ITERSSS* evidence with current identity/ownership in its own authorized addition; do not identify it with ordinary-tree MA* or AND/OR MAO*.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "02fae9f8e3daa3cf432043822f1a63d13a2121a683fc75d6e43731f80750c3d6", "pointer": "/references/1", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The 1988 thesis is an exact primary-source follow-up for multiple OPEN lists, parallel MA*-MO and MAO* backup details. Reading the journal scan does not supply the unacquired thesis.", "disposition": "pending_inspection", "exact_original_object": {"authors": "P. P. Chakrabarti", "future_owner": null, "next_check": "Potential primary clarification of MA*-MO parallel version and MAO* backup; full thesis not acquired.", "publication": "PhD thesis,IIT Kharagpur,1988", "reference_number": 3, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Some studies in heuristic search theory and algorithms"}, "existing_record_ids": [], "group": "journal1989", "index": 2, "kind": "bibliography", "next_check": "Seek the thesis legitimately; inspect the relevant original algorithm and version passages before settling parallelization or implicit backup operations.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "b4b7515f66b4e57c8d15bc8c4d1d94015fcaa9924bff941790e4732fca9aa27c", "pointer": "/references/2", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The 1988 AO* overestimation paper remains the imported AND/OR admissibility/pathmax/WAO* source question. Current WeightedAStar is fixed-weight ordinary best-first search and provides a contrast only, not this AO* identity or theorem.", "disposition": "pending_inspection", "exact_original_object": {"authors": "P. P. Chakrabarti; S. Ghose; S. C. de Sarkar", "future_owner": null, "next_check": "Explicit imported AND/OR/pathmax/solution-graph assumptions and WAO* reference; inspect original before stronger theorem/weighting statements.", "publication": "Artificial Intelligence34,97–113,1988", "reference_number": 4, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Admissibility of AO* when heuristics overestimate"}, "existing_record_ids": ["AIMech:WeightedAStar"], "group": "journal1989", "index": 3, "kind": "bibliography", "next_check": "Read the original 1988 theorem and algorithm, including solution-graph and weighting assumptions; do not transfer Weighted A* guarantees to AO*.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "4ee673d6924a66bdfd557bcb67203164f7a9d52950ea3afb15d9df6b11a626dd", "pointer": "/references/3", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Depth_m is a separately cited restricted-memory branch-and-bound comparator. Current BreadthFirstBranchAndBound is a layered unit-edge-cost procedure and does not resolve Ibaraki’s 1978 method.", "disposition": "pending_inspection", "exact_original_object": {"authors": "T. Ibaraki", "future_owner": null, "next_check": "Restricted-memory comparator source; no new-concept assertion.", "publication": "International Journal of Computer and Information Sciences7,315–343,1978", "reference_number": 5, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Depth_m search in branch and bound algorithms"}, "existing_record_ids": ["AIMech:BreadthFirstBranchAndBound"], "group": "journal1989", "index": 4, "kind": "bibliography", "next_check": "Acquire and inspect the exact 1978 Depth_m source, its memory parameter and branch-and-bound schedule before any equivalence or record decision.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "b9e296846a2f7e700e960934dff5a6b011c6277e3100703790a38263ecd2fb4f", "pointer": "/references/4", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The exact Korf1985 paper is already an evidence source of the current IDA* and DFID records. Their cost-threshold versus depth-threshold identities are explicit; the historical source’s erratum/access and theorem qualifications remain, so this citation is context rather than a new concept.", "disposition": "existing_record_context", "exact_original_object": {"authors": "R. E. Korf", "future_owner": null, "next_check": "Existing IDA* comparison context; no current ownership reconciliation in this dossier.", "publication": "Artificial Intelligence27,97–109,1985", "reference_number": 6, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Depth-first iterative-deepening: An optimal admissible tree search"}, "existing_record_ids": ["AIMech:IterativeDeepeningAStar", "AIMech:DepthFirstIterativeDeepening"], "group": "journal1989", "index": 5, "kind": "bibliography", "next_check": "Retain the maintained IDA*/DFID source scopes and their 1986 erratum residual; inspect any source-specific stronger comparison before extending the present records.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "31726a729d8fd82ffb6aae4550c4bcb83555f085ed7229a9a6f4cf7d9bda7a94", "pointer": "/references/5", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The 1987 low-overhead alternatives to SSS* paper is a game-tree restricted-memory source question. The accepted MAO* scan comparison does not constitute a fresh full reading or identify all SSS* alternatives.", "disposition": "pending_inspection", "exact_original_object": {"authors": "T. A. Marsland; A. Reinefeld; J. Schaeffer", "future_owner": null, "next_check": "Game-tree restricted-memory variants; original not freshly acquired/read.", "publication": "Artificial Intelligence31,185–199,1987", "reference_number": 7, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Low overhead alternatives to SSS*"}, "existing_record_ids": [], "group": "journal1989", "index": 6, "kind": "bibliography", "next_check": "Read the original algorithms and their game-tree/space assumptions, then compare any current game-tree owners; retain each alternative’s scope without an alias assertion.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "12cd5640826b81734e4485f8d19bee015282545f694ef2d6681326f3de45192f", "pointer": "/references/6", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The 1984 general branch-and-bound SPLIT/PRUNE framework remains an original-source relationship question. Current AStarSearch and BreadthFirstBranchAndBound give concrete comparison contexts but do not represent the entire framework or its AO* relation.", "disposition": "pending_inspection", "exact_original_object": {"authors": "D. S. Nau; V. Kumar; L. N. Kanal", "future_owner": null, "next_check": "General SPLIT/PRUNE framework relation; no automatic exact mapping.", "publication": "Artificial Intelligence23,29–58,1984", "reference_number": 8, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "General branch and bound, and its relation to A* and AO*"}, "existing_record_ids": ["AIMech:AStarSearch", "AIMech:BreadthFirstBranchAndBound"], "group": "journal1989", "index": 7, "kind": "bibliography", "next_check": "Inspect the original SPLIT/PRUNE formulation and its stated A*/AO* correspondences; preserve framework-versus-specific-algorithm granularity.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "9fb521b7a1628872f9b545d9f692081c130a6857ac02d21584b5721a1d93294b", "pointer": "/references/7", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Nilsson’s 1980 book is retained for imported A*/AO* graph and admissibility premises. Current AStarSearch has a separate 1968 primary source; its presence does not imply a full reading of this book or representation of AO*.", "disposition": "pending_inspection", "exact_original_object": {"authors": "N. J. Nilsson", "future_owner": null, "next_check": "Imported A*/AO* graph and admissibility premises; no full book reading in this dossier.", "publication": "Tioga,Palo Alto,1980", "reference_number": 9, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Principles of Artificial Intelligence"}, "existing_record_ids": ["AIMech:AStarSearch"], "group": "journal1989", "index": 8, "kind": "bibliography", "next_check": "Read the cited book passages when needed for an exact imported premise; retain the distinction between current A* context and unresolved AO* assumptions.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "acd720c28ba7e58b910663708ef8846b2431970abe645c55506716b9ee11d01b", "pointer": "/references/8", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Pearl’s 1984 Heuristics is retained for search theory and A_epsilon* context. Current AStarSearch and BestFirstSearch provide neighboring strategy definitions, not a read or accepted identity for every book method.", "disposition": "pending_inspection", "exact_original_object": {"authors": "J. Pearl", "future_owner": null, "next_check": "Search theory/A_epsilon* context; no full book reading in this dossier.", "publication": "Addison-Wesley,Reading,1984", "reference_number": 10, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question", "title": "Heuristics"}, "existing_record_ids": ["AIMech:AStarSearch", "AIMech:BestFirstSearch"], "group": "journal1989", "index": 9, "kind": "bibliography", "next_check": "Inspect the specific book passages and A_epsilon* definition before any identity or bound claim; do not replace a restricted-candidate policy with generic best-first selection.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "7325a4e3d95733bc98f90c4321c9c6bb79647ad5b34fdadc5fcfb81c70dd5bb4", "pointer": "/references/9", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Pre-emptive admission is a named MA* policy with the retained source condition f(child)&lt;=GL. The base MA* record does not decide standalone identity for MA*-PP.", "disposition": "pending_inspection", "exact_original_object": {"label": "MA*-PP", "locator": "p.204", "question": "Does pre-emptive admission deserve a standalone identity or remain a named MA* policy? Retain exact acceptance condition f(child)&lt;=GL."}, "existing_record_ids": [], "group": "journal1989", "index": 0, "kind": "named_variants", "next_check": "Compare the complete admission/pruning control flow and decide policy-versus-concept granularity only after current identity review.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "2bc4c16b5674f58f4f32e4f76dbde04c0c74eb2dabd31f7aa5b8834b82109293", "pointer": "/named_variant_questions/0", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The source-defined fractional-pruning policy keeps theta in [0,1]. It remains a variant question rather than a second resolved record or an alias of every pruning policy.", "disposition": "pending_inspection", "exact_original_object": {"label": "MA*-thetaP", "locator": "p.205", "question": "Retain fractional pruning as a source-defined policy, with theta in[0,1]; identity granularity undecided."}, "existing_record_ids": [], "group": "journal1989", "index": 1, "kind": "named_variants", "next_check": "Retain the exact theta parameter range and inspect whether any proposed standalone identity changes the base algorithm beyond a policy choice.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "f29f026f525fb32c01717a550af134246b3c2f589132697193099329cf738e6c", "pointer": "/named_variant_questions/1", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Depth-sensitive MA*-phiP preserves the scan’s uppercase F equality. Neither a spelling normalization nor theta-pruning similarity settles this policy’s identity.", "disposition": "pending_inspection", "exact_original_object": {"label": "MA*-phiP", "locator": "p.210", "question": "Retain depth-sensitive pruning and uppercase F equality from scan; no alias with theta pruning."}, "existing_record_ids": [], "group": "journal1989", "index": 2, "kind": "named_variants", "next_check": "Compare the source’s exact depth-sensitive rule and uppercase F with theta pruning before any policy identity decision.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "22083158a6cd1ebc6fba064d0dac0e41a106f9795ff6953d1ea5e7dbf5b1984b", "pointer": "/named_variant_questions/2", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Multiple OPEN-list organization and the thesis’s parallel extension remain separate source and implementation-granularity questions. The journal-based MA* record does not certify the uninspected thesis extension.", "disposition": "pending_inspection", "exact_original_object": {"label": "MA*-MO", "locator": "p.211", "question": "Multiple OPEN-list organization and source thesis parallel extension; distinct implementation policy versus concept remains open."}, "existing_record_ids": [], "group": "journal1989", "index": 3, "kind": "named_variants", "next_check": "Inspect the cited thesis and exact OPEN-list selection/parallel coordination before standalone curation.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "5d0d1d51a436c3fb0e2c9ab9b82acaa946c3976819d320f66cd527835bab2992", "pointer": "/named_variant_questions/3", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "Virtual OPEN and optional secondary storage are retained as source-specific organization choices; no strict RAM or I/O bound or standalone identity follows from the base record.", "disposition": "pending_inspection", "exact_original_object": {"label": "MA*-VO", "locator": "pp.211,220–221", "question": "Virtual OPEN and optional secondary-storage organization; source variant retained without automatic standalone concept."}, "existing_record_ids": [], "group": "journal1989", "index": 4, "kind": "named_variants", "next_check": "Compare virtual OPEN/secondary-storage mechanics and accounting before deciding whether a separate implementation policy merits a record.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "86030d600d3b284c2b8149f1165f6d31d75d321c06f54fc80a6dcbc5cb324e4b", "pointer": "/named_variant_questions/4", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "MAX=0, large-MAX and game-tree endpoints are qualified source relationships. Existing IDA* and DFID are useful endpoint contrasts, not aliases of MAO*, AO*, MarkA or SSS*.", "disposition": "pending_inspection", "exact_original_object": {"label": "MAO* refinements and endpoints", "locator": "pp.219–220", "question": "Retain MAX=0 iterative-deepening endpoint, large-MAX AO*/MarkA-like cases, game-tree SSS* relationship and proposed alternate unmarked-arc pruning; do not silently turn these into aliases or separate algorithms."}, "existing_record_ids": ["AIMech:IterativeDeepeningAStar", "AIMech:DepthFirstIterativeDeepening"], "group": "journal1989", "index": 5, "kind": "named_variants", "next_check": "Inspect each endpoint’s complete control flow, memory convention and game-tree/AND-OR assumptions; keep alternate unmarked-arc pruning proposed rather than silently implemented.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "d4d0ac49b104eb94e029a37f41f7095396aee127c4018d810a60885e30dc5548", "pointer": "/named_variant_questions/5", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The exact speculative-search/SB&amp;B/SIDA* URL remains search-only. Existing IDA* is a comparison context; neither its name nor the retained source title supplies an inspected speculative algorithm.", "disposition": "pending_inspection", "exact_original_object": {"label": "Speculative search / SB&amp;B / SIDA* comparison", "next_check": "If comparison is needed, inspect its definition and node-count convention; a search snippet is not algorithm evidence.", "status": "search-only; not acquired or read", "url": "https://wah.cse.cuhk.edu.hk/wah/Wah/papers/C063/C63.pdf"}, "existing_record_ids": ["AIMech:IterativeDeepeningAStar"], "group": "journal1989", "index": 0, "kind": "retrieval_only", "next_check": "Retrieve https://wah.cse.cuhk.edu.hk/wah/Wah/papers/C063/C63.pdf and inspect definitions and node-count convention before identity or comparison claims.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "8f0d39eb4bf38645d2f593efc84f12cf3e1ee55dbce51009377a42691ab86828", "pointer": "/additional_bounded_retrieval_questions/0", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "This 1992 effective-memory publication is already retained in current inherited memory_search_source_accounting/search_only_reconciliation/4 under main7. Preserve that responsibility and the exact newly retained publisher route and IDA*_CRM/IDA*_CRAM spellings. The current IDA* context does not resolve the 1991 IDA-CR/CRA versus 1992 retained-memory relationship.", "disposition": "existing_pending_owner", "exact_original_object": {"label": "Effective use of memory in iterative deepening search / IDA*_CRM / IDA*_CRAM", "next_check": "Preserve retrieved spelling variants for later original-source reconciliation; no alias decision.", "status": "search-only; existing358 source pointer continuity retained separately", "url": "https://www.sciencedirect.com/science/article/abs/pii/002001909290131E"}, "existing_record_ids": ["AIMech:IterativeDeepeningAStar"], "group": "journal1989", "index": 1, "kind": "retrieval_only", "next_check": "Obtain the exact 1992 original at https://www.sciencedirect.com/science/article/abs/pii/002001909290131E; compare its retained-memory mechanism, spellings and publication relationship with main7’s 1991 source without collapsing names.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json", "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256": "1ff781a04b21fa3cbc270694bcaba49692cfada2a849d3fe239c532d23c56305", "pointer": "/additional_bounded_retrieval_questions/1", "responsible_owner": {"family": "main", "index": 7}}
- {"added_record_ids": [], "assessment": "The exact 1987 ELDECS source-version object is already under main911 and remains pending. The 25-page 1989 journal scan does not establish conference-to-journal equivalence, first introduction or publisher-byte identity.", "disposition": "existing_pending_owner", "exact_original_object": {"object": {"assessment": "The 1987 conference-to-1989 MA*/MAO* journal relationship is an explicit unresolved source-version question under 911. It is not an additional algorithm merely because a separate publication is cited.", "disposition": "existing_pending_owner", "exact_original_object": {"candidate": "Tree searching in restricted memory", "discovery": "Institutional primary-author bibliography.", "disposition": "pending_publication_relationship", "next_check": "Resolve conference-to-journal relationship with the1989 MA*/MAO* source; a predecessor publication is not automatically a new concept.", "publication": "Chakrabarti, Ghose, Acharya and De Sarkar, ELDECS1987,518–520, author bibliography", "source": "https://cse.iitkgp.ac.in/~ppchak/publications.html"}, "existing_record_ids": [], "index": 5, "next_check": "Resolve conference-to-journal relationship with the1989 MA*/MAO* source; a predecessor publication is not automatically a new concept.", "original_object_sha256": "0e98a8ebf4b7207f512dfd1902d703b0b3325d08474d9333f1b5683f479028f2", "responsible_owner": {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/search_only_reconciliation/5"}, "existing_record_ids": [], "group": "journal1989", "index": 0, "kind": "conference_version", "next_check": "Acquire an author/library copy of the ELDECS1987 pp.518–520 paper and compare its actual content with the retained 1989 scan; preserve the institutional bibliography URL.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json", "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256": "fe29abe85605da32ff69ffb6e7209f8e331df028e9bbbf3521cbbf709103233c", "pointer": "/source_objects/1", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "assessment": "This historical Chakrabarti1989 citation responsibility is proposed to be represented by the two distinct accepted source-scoped records: displayed-tree MA* and acyclic AND/OR MAO*. Original old full_text_read=false and next_check values remain verbatim provenance. The accepted current source is the exact JSON scan manifest and 100 asset objects, not a publisher PDF; all six source qualifications and 1987 version question remain unresolved. Historical PhilPapers https://philpapers.org/rec/CHAHSI-4 and OUCI https://ouci.dntb.gov.ua/en/works/45XORXv7/ are same-title retrieval metadata, not further methods or newly inspected originals.", "disposition": "represented_by_added_record", "exact_original_object": {"object": {"assessment": "This is the explicit unresolved MA*/MAO* source in current memory-search owner 911. Adding SMA* does not substitute Russell's approximate MA* sketch for the unavailable original, nor settle ordinary-graph versus AND/OR scope.", "disposition": "existing_pending_owner", "exact_original_object": {"authors": "P.P. Chakrabarti, S. Ghose, A. Acharya and S.C. de Sarkar", "candidate": "Heuristic search in restricted memory", "citation_key": "chakrabarti1989", "disposition": "retained_source_question", "full_text_read_in_this_dossier": false, "next_check": "Acquire and fully read MA*/MAO* original, retaining the minimum-memory qualification and source-specific variants.", "owner_links": [], "publication": "Artificial Intelligence41(2),197–221,1989", "source_occurrences": [{"pdf_page": 6, "reference_label": "Chakrabarti et al., 1989", "source_id": "mrec1989"}, {"pdf_page": 5, "reference_label": "2", "source_id": "sma1992"}, {"pdf_page": 6, "reference_label": "1", "source_id": "its1994"}], "source_title_matches": []}, "existing_record_ids": [], "index": 1, "next_check": "Acquire and fully read MA*/MAO* original, retaining the minimum-memory qualification and source-specific variants.", "original_object_sha256": "cca4cb705b6d0445f46f635ca69767b7193a82e6ad62cfefc1865d3df652732a", "responsible_owner": {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/bibliography_reconciliation/1"}, "existing_record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"], "group": "journal1989", "index": 0, "kind": "historical_source_responsibilities", "next_check": "After authorized addition, retain variants, imported references, source-control-flow qualifications and author/publisher version comparison; never rewrite the earlier access-gap receipt as if full text had then been available.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json", "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256": "4547654d21f5b616e8775020e013704852f81f8f698152eddaa6c74754de3dd2", "pointer": "/source_objects/0", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "assessment": "The historical combined MA*/MAO* full-text/identity residual is proposed to be represented at base-procedure scope by the two distinct records supported by the subsequently acquired 25-page public scan. The older source object, failed access and empty read_pages stay exact. Current source boundaries include displayed-tree MA*, acyclic AND/OR MAO*, qualified memory units and uncompleted pseudocode interfaces; the umbrella remains partial.", "disposition": "represented_by_added_record", "exact_original_object": {"object": {"assessment": "The original MA*/MAO* full text is still unavailable in the accepted dossier. Current owner 911 remains partial after the three separate procedures; ordinary versus AND/OR graph scope, minimum memory and exact operations remain open.", "disposition": "existing_pending_owner", "exact_original_object": {"candidate": "MA* and MAO*", "disposition": "pending_original_full_text_and_identity_reconciliation", "next_check": "Acquire and read the original Chakrabarti et al. 1989 article, distinguish ordinary-graph MA* from AND/OR MAO*, then compare precise quantities, pruning, backup and memory premises with SMA*, MREC and maintained neighboring records. Russell’s explicit approximate sketch is not a substitute.", "source": {"access_gap": "Publisher search result provides abstract and access options. Direct web open failed with internal error. Searches found no acquired legitimate original full-text copy. Other papers’ sketches are explicitly secondary for MA*.", "access_level": "publisher metadata and abstract; author institutional bibliography", "author_metadata": "https://cse.iitkgp.ac.in/~ppchak/publications.html", "authors": ["P. P. Chakrabarti", "S. Ghose", "A. Acharya", "S. C. de Sarkar"], "doi": "10.1016/0004-3702(89)90010-6", "primary_pdf": null, "publication": "Artificial Intelligence 41(2), 197–221, December 1989", "read_pages": [], "role": "defining primary source identified; full text not obtained", "supported_abstract_scope": "The publisher abstract distinguishes MA* for ordinary graphs from MAO* for AND/OR graphs and conditions its memory/admissibility statement on a minimum memory requirement. No unseen algorithms, proofs or parameter choices are reconstructed.", "title": "Heuristic Search in Restricted Memory", "url": "https://www.sciencedirect.com/science/article/pii/0004370289900106", "visual_pages": []}}, "existing_record_ids": [], "index": 0, "next_check": "Acquire and read the original Chakrabarti et al. 1989 article, distinguish ordinary-graph MA* from AND/OR MAO*, then compare precise quantities, pruning, backup and memory premises with SMA*, MREC and maintained neighboring records. Russell’s explicit approximate sketch is not a substitute.", "original_object_sha256": "47e4ec6dbb124db6c44b27d251e52c24b3415da980e3022f9899720eae3c97fc", "responsible_owner": {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/residual_reconciliation/0"}, "existing_record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"], "group": "journal1989", "index": 1, "kind": "historical_source_responsibilities", "next_check": "Keep all variant/version/theorem/interface questions pending under main911 and preserve the existing22 bibliography/28occurrence plus6lead accounting and separate IE owner912. No family exhaustion or issue closure follows.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json", "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256": "22200a181af6870bd9f28857c09b648b985e5190e4260dec49bc1b82ba9a737a", "pointer": "/source_objects/2", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The source-local MAO* parent-arc refresh omission remains an explicit interface qualification. The prose, printed backup and Figure2 are retained together; the base record does not insert an algorithm line.", "disposition": "existing_pending_owner", "exact_original_object": {"consequence": "A literal transcription lacks the explicit parent-arc refresh needed for the depicted propagation. This is an original-source pseudocode omission/implicit-operation question, not an OCR error and not a claim that every implementation is incorrect. Preserve both prose and pseudocode; do not silently invent an algorithm line.", "id": "Q1", "kind": "source_control_flow_qualification", "locator": "p.212 Section3.1; pp.213–214 steps3.2(vi),4.2.1–4.2.3; p.216 Fig.2(f)–(g)", "next_check": "Independent control-flow review, then compare author thesis/errata or another primary version if accessible.", "observation": "The prose explicitly describes successor-specific backup. The printed expansion assigns f(n,n′)=max(f(n,n′),f(n′)+c(n,n′)); cost revision subsequently aggregates stored f(m,m′), increases f(m), and queues marked parents, but does not explicitly refresh each parent f(p,m) there. The worked figure raises A’s retained branch estimate from3 to5 when B rises from2 to4 with unit arc cost."}, "existing_record_ids": [], "group": "journal1989", "index": 0, "kind": "source_qualifications", "next_check": "Compare the author thesis, errata or another primary version for the explicit successor-specific parent-arc update; retain the distinction between source omission and a proven implementation failure.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json", "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256": "e1b9cac943fd14de11278c2774ea42ef8347e6a2acd436454a1e2dc268512047", "pointer": "/source_qualification_objects/0", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The positive-but-summable infinite-path counterexample remains a mathematical scope qualification. Independent review does not turn individual positive arc costs into a uniform lower bound or certify termination on every infinite graph.", "disposition": "existing_pending_owner", "exact_original_object": {"consequence": "Do not universalize the source theorem to arbitrary infinite graphs. Finite relevant cost contours or suitable finite-branching/positive-lower-bound conditions can be stated only as additional reasoning conditions, never falsely attributed as printed premises.", "id": "Q2", "kind": "source_theorem_scope_qualification", "locator": "p.202 Theorem2.7 proof; p.219 Theorem3.4 proof", "manual_counterexample": "Take a root with a goal edge of cost2 and an infinite alternative chain with successive costs1/2,1/4,1/8,...; h=0. Every chain prefix costs less than1, and each edge is finite and positive. Optional edges of cost2 from each chain node to a goal ensure finite goal-reaching continuations without changing the cheaper-prefix obstruction. An infinite family of prefixes stays below the root goal cost. This is a reasoning example, not an executed algorithm or a claim about the finite Fifteen Puzzle experiments.", "next_check": "Independent mathematical review and source-version clarification.", "observation": "The proofs state termination for infinite graphs with finite positive individual arc costs. Individual positivity alone does not rule out an infinite path of finite total cost."}, "existing_record_ids": [], "group": "journal1989", "index": 1, "kind": "source_qualifications", "next_check": "Seek primary-version clarification of termination premises; preserve the finite-contour/additional-condition reasoning as independent qualification rather than printed theorem text.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json", "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256": "6a124bd01e110438baedb37806329b6c299b2d245d1dabb2c66958619e90d42b", "pointer": "/source_qualification_objects/1", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The original memory counters, protected marked storage and expansion-before-pruning convention remain scoped to the source. Base records do not certify a strict allocator cap, identical MA*/MAO* units or zero storage at MAX=0.", "disposition": "existing_pending_owner", "exact_original_object": {"consequence": "Retain the author-defined memory measures and stated theorem rather than promising a strict allocator cap, zero-memory execution at MAX=0, or equality of MA*/MAO* memory units. No exact machine-memory or transient-allocation guarantee was verified.", "id": "Q3", "kind": "memory_accounting_scope", "locator": "p.200 count initialized0 while root stored; pp.204,212–214,219", "next_check": "If future curation includes a precise implementation bound, audit root/per-successor/transient accounting separately.", "observation": "MA* counts generated successors starting at0 with root already stored; MAO* explicitly counts nodes and arcs. Expansion occurs before pruning and marked path/solution storage is protected."}, "existing_record_ids": [], "group": "journal1989", "index": 2, "kind": "source_qualifications", "next_check": "If a future implementation-level bound is requested, audit root, generated successors, arcs, stack and transient allocation separately.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json", "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256": "1e2bbf4ae5c6bb82fdac4849dfc604715e2b6d69b53377989b9386ba23ddcc18", "pointer": "/source_qualification_objects/2", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The public scan’s third-party provenance and missing conference/publisher original remain unchanged access boundaries. The accepted scan supports source reading without proving publisher-byte identity or conference equivalence.", "disposition": "existing_pending_owner", "exact_original_object": {"consequence": "No conference-to-journal equivalence or first-introduction attribution beyond the verified citations. The public scan remains explicitly third-party provenance.", "id": "Q4", "kind": "version_access", "locator": "author bibliography entry101; journalp.221 received/revised dates", "next_check": "Seek an author/library primary copy of the conference proceedings and publisher/author journal text; compare bytes/content rather than retroactively changing historical access receipts.", "observation": "1987 ELDECS original full text was not acquired; publisher journal PDF also not acquired, although all25 public scan pages were read."}, "existing_record_ids": [], "group": "journal1989", "index": 3, "kind": "source_qualifications", "next_check": "Seek an author/library conference copy and publisher/author journal text, compare content and bytes, and retain all historical failed access receipts.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json", "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256": "a84046c181a03fb33f5c5bd071fa2c832a9ccd4632b6adf82d8976dfcb5a9107", "pointer": "/source_qualification_objects/3", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The displayed MA* algorithm remains a tree procedure. The graph paragraph’s pathmax/no-reopening assertion does not settle transpositions, cycles or improved-path handling, and no general graph guarantee is inferred.", "disposition": "existing_pending_owner", "exact_original_object": {"assessment": "Path-local monotonicity alone is not a full general graph duplicate-handling or consistency proof. Preserve the exact tree procedure; leave graph transpositions, cycle handling, path-cost improvements and reopening behavior as an explicit unresolved extension question. This is a scope qualification, not a demonstrated counterexample or a silent algorithm repair.", "changes_to_original_source_questions": false, "id": "MA-GRAPH-SCOPE", "image": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-05.jpg", "sha256": "3388a75a92404905eff06b5231b2bddaa9d7bf2da113d89a560ecb7873dbb703"}, "locator": "Printed p.201, paragraph following Algorithm MA*; public reader page5", "ocr": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-05.txt", "sha256": "3146bf08e89c43fb2fef4034889045d1fc2159f5d5cdc6c14fc70243d361c3e0"}, "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/root-bounded-scientific-reading.json", "sha256": "84e4cfec9200a89c080ebd39ce2b249da3be31d4aa4ea71250930a273145a935"}, "proposed_limitation": "The displayed MA* procedure is for trees. Its graph-extension paragraph asserts that pathmax removes CLOSED reopening, but a complete graph duplicate, cycle and improved-path update policy is not specified here; no general graph-search correctness guarantee is inferred from path-local monotonicity.", "source_statement_summary": "The displayed algorithm is for trees; subsequent prose proposes checking OPEN/CLOSED when extending to graphs and asserts that maintained pathmax removes the need for CLOSED reopening.", "status": "retained_curation_boundary_and_pending_source_question"}, "existing_record_ids": [], "group": "journal1989", "index": 4, "kind": "source_qualifications", "next_check": "Inspect the original graph-extension specification or later primary clarification of duplicate detection, path-cost improvements and CLOSED reopening before any extension claim.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/source-question-continuity.json", "sha256": "1d0e6b4cf08506e81957cc7144602594285d197ae4fb6cbe33d7ebd14d43ee0f"}, "original_sha256": "776f24921046ea76465724a302379bb5609b33e7cfab1c213afab039297e1d6b", "pointer": "/added_boundary", "responsible_owner": {"family": "main", "index": 911}}
- {"added_record_ids": [], "assessment": "The missing displayed parent-root guard, empty-successor conventions and OPEN-empty failure return remain executable-interface questions. The accepted record retains those limitations and does not silently repair the printed procedure.", "disposition": "existing_pending_owner", "exact_original_object": {"assessment": "No completing guard or convention was located in the inspected notation/algorithm text. Prior complete source reading provides context, but this bounded fresh inspection does not claim a search of every cited original. Retain as a qualification of executable completeness, not a repaired algorithm or new positive claim.", "fresh_reading": {"page_images": [{"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-04.jpg", "sha256": "cd98b81df25308273337c650ae6e352d02aff39e97cb09370f4f983a56370149"}, {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-05.jpg", "sha256": "3388a75a92404905eff06b5231b2bddaa9d7bf2da113d89a560ecb7873dbb703"}], "text": [{"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-01.txt", "sha256": "a67f14b3b6a53c358ca1ceca413eb919d6d8524f49bb7301e648015cfd5ecb1b"}, {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-02.txt", "sha256": "d991e96a972533c41f046edd676fed82a805ba152d299307fac8b53deeb1050a"}, {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-03.txt", "sha256": "706483915acbd256a3e76ddbfe4f5c0163e98df38c90b22de175a02254256eb0"}, {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-04.txt", "sha256": "0115471d43d51b3a6e84005ac8389c2854c15de40a2aad7f726186014267c41a"}, {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-05.txt", "sha256": "3146bf08e89c43fb2fef4034889045d1fc2159f5d5cdc6c14fc70243d361c3e0"}], "text_printed_pages": [197, 198, 199, 200, 201], "visual_printed_pages": [200, 201]}, "id": "MA-PSEUDOCODE-INTERFACES", "observations": [{"locator": "Printed201, step6(ii)(a)–(b)", "observation": "A removed p is assigned parentq; an increased parent bound causesq to be put intoZ. The display has no explicit root-stop guard before a subsequent parent lookup.", "scope": "This is a missing displayed interface convention, not proof that the author implementation dereferences a nonexistent parent."}, {"locator": "Printed198–200, notation, Definition2.2 and initialization/expansion/termination", "observation": "The source defines successor minima and tests the selected node for a goal, but the displayed procedure does not fully state goal/dead-end empty-successor initialization conventions.", "scope": "A complete implementation needs conventions; no convention is silently inserted or attributed to the source."}, {"locator": "Printed200, Select1 and Termination", "observation": "Select1 chooses a node fromOPEN; no explicit OPEN-empty failure return is displayed.", "scope": "Do not certify a general unsolvable-instance interface from the literal pseudocode."}], "original_dossier_unchanged": true, "recorded_at": "2026-10-16T03:19:26.504883Z", "root_origin": {"path": "/private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/root-prospective-identity-mapping-reading.json", "sha256": "d6cae02242bb5745889c85eb73caa45c96f0d69db1aeda4d7e438ca5a6a0f534"}, "status": "scope_boundary_not_proven_algorithm_failure"}, "existing_record_ids": [], "group": "journal1989", "index": 5, "kind": "source_qualifications", "next_check": "Locate author implementation, thesis or primary clarification for root stopping, goal/dead-end initialization and unsolvable-instance return conventions; no fabricated algorithm line or demonstrated-failure claim.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json", "sha256": "5daf989d86b1a22a4c7126f4b4fe234bdfdc909808cda10f04e9c454b1a9f8b7"}, "original_sha256": "26999fec925c8358a3ed960336a98c2cb33defd3cc42fa9072153d9076f30990", "pointer": "", "responsible_owner": {"family": "main", "index": 911}}
- The canonical source_durability object embeds the exact 38,592-byte JSON manifest as base64 and all 100 asset metadata/provenance objects for 25 third-party public-reader scan pages. This is not a publisher PDF or publisher-byte equivalence.
- Exact inherited source scopes are recursively retained under predecessor_state/projection; actual 359 report {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json", "sha256": "5aaa5f8a608224430161ccddacc1cc2cbd7ecedba79e8cec86b52ee81ec4056d"}. No original 402/404/406 closure or family exhaustion is asserted.
- Inherited predecessor_state: exact object SHA256 a435620b7452df3a201584e1166dfdf12137a3fa28ee81394fddb075b12a6a9b; original source references remain inside predecessor_state/projection/predecessor_state.
- Inherited predecessor_state_sha256: exact object SHA256 2912acd1d631adda13c03fd77e8469cbf11881ef183c539dd85189345b762876; original source references remain inside predecessor_state/projection/predecessor_state_sha256.
- Inherited pair_source_accounting: exact object SHA256 421cbcd6778c6a1e998d7e143c32f9c60ffd8132b255edf1c402017d702d50c4; original source references remain inside predecessor_state/projection/pair_source_accounting.
- Inherited frontier_result: exact object SHA256 64027f21b60509db51861e16ead984787c10d5b6bd2bcfbd5d926a04e01bfc36; original source references remain inside predecessor_state/projection/frontier_result.
- Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "bibliography_occurrences": 10, "changed_main_indexes": [911], "changed_nested_indexes": [], "conference_version_questions": 1, "historical_source_responsibilities": 2, "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_variant_questions": 6, "retrieval_questions": 2, "source_qualifications": 6}
- Actual source accounting digest (sorted compact JSON UTF-8): 785039b1312b403f5135840b972e08898dae00b745eb9316f9067ef30b04266f
- Actual historical/current identity changes: [{"id": "AIMech:MAStar", "field": "identity_notes", "historical": "This specific selection, f/F bookkeeping, continuation, backup and pruning procedure differs from maintained MREC, SMA*, ITS, A*, IDA* and RBFS-family methods. An endpoint resemblance or common best-first ancestry is not an exact identity. Use the literal source name. No expansion such as Memory-Available A* is asserted from an unverified source spelling; named variants and large/zero-memory endpoints are not aliases. This is a source-scoped prospective draft, with a provisional local ID only. The observed branch358 inventory contained797 native and442 pinned AIO records; candidate exact/local IDs, names, aliases and scoped synonyms were mechanically compared with no normalized collision. Ignored/hidden-inclusive searches covered four roots; fourteen selected native contexts and22 full AIO nodes/133 relations were read with exact scope in the bound proposal. This historical snapshot does not substitute for eventual fresh identity and owner review.", "current": "Current ignored-inclusive identity review on 2026-10-16 at base 0da1b27de4ee552bc8fb16a083d0f91d2a093142 examined1241 records,4921 identity occurrences and3760 normalized values, plus945 exact search occurrences in215 distinct content groups across four recorded roots. No candidate or context normalized collision was found for the recorded probes. MA* is curated as displayed ordinary-tree OPEN/CLOSED search with successor lower bounds and F-driven pruning; it remains distinct from the other member of this pair, MREC, SMA*, ITS, RBFS, RTAA* and amortized SVGD. Full current neighbor and inherited search-context readings are explicitly attributed in the discovery report; this is bounded absence evidence, not global novelty. Shared current source responsibility is main911, which remains partial; all27 original source items and separate main7/main912 responsibilities survive.", "root_decision": "records/AIMech:MAStar/identity_notes"}, {"id": "AIMech:MAOStar", "field": "identity_notes", "historical": "The marked AND/OR solution structure, successor-specific bounds, AND/OR generation and arc/orphan pruning differ from the ordinary-path MA* procedure and maintained importance-sampling AOAS. The source’s relation to AO* is a refinement context, not an established alias. Use the literal source name. Do not merge MAO* with MA*, AO*, cyclic AND/OR algorithms or the modified cutoff variant. This is a source-scoped prospective draft, with a provisional local ID only. The observed branch358 inventory contained797 native and442 pinned AIO records; candidate exact/local IDs, names, aliases and scoped synonyms were mechanically compared with no normalized collision. Ignored/hidden-inclusive searches covered four roots; fourteen selected native contexts and22 full AIO nodes/133 relations were read with exact scope in the bound proposal. This historical snapshot does not substitute for eventual fresh identity and owner review.", "current": "Current ignored-inclusive identity review on 2026-10-16 at base 0da1b27de4ee552bc8fb16a083d0f91d2a093142 examined1241 records,4921 identity occurrences and3760 normalized values, plus945 exact search occurrences in215 distinct content groups across four recorded roots. No candidate or context normalized collision was found for the recorded probes. MAO* is curated as acyclic pure-AND/OR marked partial solution-graph search with successor-specific backups and orphan-aware pruning; it remains distinct from the other member of this pair, MREC, SMA*, ITS, RBFS, RTAA* and amortized SVGD. Full current neighbor and inherited search-context readings are explicitly attributed in the discovery report; this is bounded absence evidence, not global novelty. Shared current source responsibility is main911, which remains partial; all27 original source items and separate main7/main912 responsibilities survive.", "root_decision": "records/AIMech:MAOStar/identity_notes"}]

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T043949Z-ma-star-and-mao-star
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of MA* and MAO*
started_at: '2026-10-16T04:39:40.362224Z'
finished_at: '2026-10-16T04:39:49.045663Z'
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
summary: Retain MA* and MAO* as separate source-scoped DRAFT algorithms. Twelve claims
  and17 limitations preserve their different path/solution-graph mechanisms, memory
  measures, source control-flow questions and theorem scope. Exact current and inherited
  source responsibilities remain pending where appropriate; the canonical report durably
  binds the scan manifest and100 asset metadata objects.
source:
  git_revision: 0da1b27de4ee552bc8fb16a083d0f91d2a093142
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/GraphConvolutionalNetwork.yaml
    sha256: 644b6187436c10693cb547dbaa809b8c00c97ad198db201342e5bc0780c78d44
    role: context
  - path: data/aio/GraphConvolutionalPolicyNetwork.yaml
    sha256: c8a6e283e5d6c5ebc59e1db234d174dc3be79dd0f4a30cdb74e6494e65507d79
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
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
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
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
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
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
  - path: data/curated/BeamSearch.yaml
    sha256: aec9aab4ec700ecfc6aa4b71c98f33bdbb456d131748729a98480abef34875bc
    role: context
  - path: data/curated/BeamStackSearch.yaml
    sha256: 161a74d1afbe844b276989df5e068268ffa239e62799523221b56a626b4f4861
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/BreadthFirstBranchAndBound.yaml
    sha256: f81b9d69d5cab18ce6584b1fc61be1e25a51b7a12ba3822628a8fe3793bcbfd0
    role: context
  - path: data/curated/DepthFirstIterativeDeepening.yaml
    sha256: 2e01d2da093397d74a7647e624015b8b0f54d14c7420e00d3ded18a576ce605d
    role: context
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/IterativeThresholdSearch.yaml
    sha256: bd24d2cd8bf58105833b7fde36a5ba43da19e1bb8425ccff2bc8aefe68cc62ac
    role: context
  - path: data/curated/MAOStar.yaml
    sha256: 8856d812fbfad12e40bd79f321cc935ed2166d60dc044bf164cb24328c1f9477
    role: target
  - path: data/curated/MAStar.yaml
    sha256: b92ce9ec4eed5198b58a24d1d256c7287c734a47219c4922dde36aa05640b66c
    role: target
  - path: data/curated/MREC.yaml
    sha256: 0a6b229e7b98ddc60d52843f82f1d344374136f2ff4e870238358dd51e2f785b
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
  - path: history/reports/ma-star-and-mao-star/2026-10-16T042411Z-codex-a6f975.yaml
    sha256: cd3dc113fdcf98dc8782e27e936480d5a59240972b8a5f263d4abda289154300
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
  - path: research/discovery/20261016T042347Z-ma-star-and-mao-star.md
    sha256: 663132f9655b2779f0dc9034b5f578e87078654e75397ebf98c844baa3ae1bf2
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
  description: Two exact current native records from accepted cohort360 creation;
    all selected claims and limitations assessed. Historical source and neighbor reading
    scopes remain separately attributed.
  selection: Exact AIMech:MAStar and AIMech:MAOStar.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:MAStar
  - AIMech:MAOStar
  exclusions:
  - target: MA*-PP,thetaP,phiP,MO,VO and MAO* refinements/endpoints
    reason: Exact named-policy questions retained without automatic alias or concept
      decisions.
  - target: 1987 conference, thesis and other referenced originals
    reason: Actual acquisition/reading limitations remain exact; citations do not
      establish source inspection.
  - target: Inherited402/404/406 and356/357/358/359 source responsibilities
    reason: Full recursively queryable predecessor scope is preserved; whole issues
      and source families are not closed.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual completed command exited0; exact output and timing retained.
  target_ids:
  - AIMech:MAStar
  - AIMech:MAOStar
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
  - AIMech:MAStar
  - AIMech:MAOStar
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
  - AIMech:MAStar
  - AIMech:MAOStar
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
  - AIMech:MAStar
  - AIMech:MAOStar
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
  - AIMech:MAStar
  - AIMech:MAOStar
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
  - AIMech:MAStar
  - AIMech:MAOStar
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - check-diff
evidence:
- evidence_id: ma-mao-primary-scan
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Journal printed pp.197–221; public reader pp.1–25
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Shared defining journal article inspected through 25 original public-reader
    scan images. The hash identifies the exact JSON bundle manifest, not a publisher
    PDF. Source reading is inherited with explicit attribution.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-mao-source-durability
  kind: record_content
  reference: /private/tmp/aimech-ma-mao-review-fragments-20261016/source-durability.fragment.json
  locator: canonical_report_payload and future_acceptance_requirements
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Prepared durable-source payload and requirements only. No canonical persistence
    or completed source verification is asserted.
  snapshot_sha256: daa1e61ded84220be35a4be048167107e33c10125438e94de18160b3848e77c7
- evidence_id: ma-mao-accepted-support
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json
  locator: records, source_qualification_objects and reading_attribution
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Accepted scientific support for the 12 claims and 17 limitations. This
    fragment assembly is by an earlier author, not a new independent primary-source
    review.
  snapshot_sha256: a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753
- evidence_id: ma-mao-root-preview-readback
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-native-preview-20261016/root-preview-readback.json
  locator: records and limitations
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Actual prior TEMP preview readback. Validation establishes representation
    correspondence only, not current identity, ownership or source durability.
  snapshot_sha256: 0f19af363c7ed2ccb3212d5955f1578a9f4ae469da20058bf338ae8345973808
- evidence_id: ma-mao-source-questions
  kind: record_content
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/source-question-continuity.json
  locator: original_objects, added_boundary
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Exact original ten citations, six named variant questions, two retrieval
    leads, conference relationship question and graph boundary remain pending by their
    retained objects. New research does not rewrite these historical objects.
  snapshot_sha256: 1d0e6b4cf08506e81957cc7144602594285d197ae4fb6cbe33d7ebd14d43ee0f
- evidence_id: ma-mao-interface-question
  kind: record_content
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json
  locator: complete source interface qualification
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Root-parent termination, successor-minimum initialization and OPEN-empty
    failure conventions remain qualified; the display is not certified as executable
    code.
  snapshot_sha256: 5daf989d86b1a22a4c7126f4b4fe234bdfdc909808cda10f04e9c454b1a9f8b7
- evidence_id: ma-mao-identity-mapping
  kind: search
  reference: /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/handoff.final.json
  locator: source-scoped historical identity and no-match proposal
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Prior ignored/hidden-inclusive four-root search and bounded native/AIO
    comparison, not a current absence conclusion.
  snapshot_sha256: b2395748fb5da9a0d022697b501cdbd76055ed225e781678566e03d3babdf6b6
  search_scope: 'Historical branch358 snapshot: pinned AIO commit397851c547d1c4d8f06ef184f63c1d40bc86937a,
    SHA256 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6. All442
    CLASS identity/synonym fields mechanically compared and class labels read;22 selected
    full nodes and all133 incident relations inspected. Other definitions and external
    definition-source papers were not all reread. This is a bounded pinned-snapshot
    mapping proposal requiring reassessment at eventual curation.'
- evidence_id: ma-mao-root-identity-mapping
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/root-prospective-identity-mapping-reading.json
  locator: scope and prospective drafting acceptance
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Root prospective mapping/name reading; it explicitly withholds future current-state
    identity, ownership and canonical approval.
  snapshot_sha256: d6cae02242bb5745889c85eb73caa45c96f0d69db1aeda4d7e438ca5a6a0f534
- evidence_id: reading-researcher-prior-full25-scan-and-ocr
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-original-source-research-20261016/manual-reading.json
  locator: exact declared reading and limits
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Inherited reading receipt; its original actor and fresh-versus-prior scope
    remain controlling. No new full-paper reading is asserted during this DATA assembly.
  snapshot_sha256: b6d37ee0d0fefacf5c1c221abba4f27c7c1cc57af07142d9ced365c7dcc813fb
- evidence_id: reading-independent-bounded-controlflow-math
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-independent-controlflow-audit-20261016/assessment.v2.json
  locator: exact declared reading and limits
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Inherited reading receipt; its original actor and fresh-versus-prior scope
    remain controlling. No new full-paper reading is asserted during this DATA assembly.
  snapshot_sha256: 278bf5fa4194b691974ad5f4c1464ab60e8610ab3911d1f3da2ce6843a49f972
- evidence_id: reading-root-bounded-science
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-original-source-research-20261016/root-bounded-scientific-reading.json
  locator: exact declared reading and limits
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Inherited reading receipt; its original actor and fresh-versus-prior scope
    remain controlling. No new full-paper reading is asserted during this DATA assembly.
  snapshot_sha256: 84e4cfec9200a89c080ebd39ce2b249da3be31d4aa4ea71250930a273145a935
- evidence_id: reading-identity-mapping-researcher
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/manual-reading.json
  locator: exact declared reading and limits
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Inherited reading receipt; its original actor and fresh-versus-prior scope
    remain controlling. No new full-paper reading is asserted during this DATA assembly.
  snapshot_sha256: 468a7e265f1b70ffc4ad9a93b2a453d03a54760c20172325c209383a714a8a66
- evidence_id: reading-additional-fresh-interface-check
  kind: prior_review
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json
  locator: exact declared reading and limits
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Inherited reading receipt; its original actor and fresh-versus-prior scope
    remain controlling. No new full-paper reading is asserted during this DATA assembly.
  snapshot_sha256: 5daf989d86b1a22a4c7126f4b4fe234bdfdc909808cda10f04e9c454b1a9f8b7
- evidence_id: ma-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-ma-mao-native-preview-20261016/MAStar.preview.json
  locator: complete scientific fields; curation is prior TEMP-only provenance
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Exact accepted native preview with provisional source-scoped identity.
    Future current identity/owner, curation time and canonical correspondence remain
    unset.
  snapshot_sha256: 6975fb1ea00bed939aee3df57085ad5fe7017a4e1b20a40febe767d60c6cf5c3
- evidence_id: ma-claim-1-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section2.2, Definition2.2, printed p.199 / reader p.3; Algorithm MA* initialization
    on p.200 / reader p.4
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-claim-2-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section2.2 and Algorithm MA*, printed pp.199–201 / reader pp.3–5, steps2–7
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-claim-3-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.199–201 / reader pp.3–5, pathmax display and step6
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-claim-4-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Algorithm MA*, printed p.201 / reader p.5, steps7–8; theta variant on p.205
    / reader p.9
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-claim-5-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.198–200,204 / reader pp.2–4,8; definition of |C*|, initialization
    and Theorem2.10
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-claim-6-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section2.3.1, printed p.205 / reader p.9
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-1-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed p.201 / reader p.5, paragraph following Algorithm MA*
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-2-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Assumption2.1 on p.199 / reader p.3; Theorem2.7 and proof on pp.202–203
    / reader pp.6–7
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-3-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.199–200,204 / reader pp.3–4,8
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-4-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section2.3.1, printed p.205 / reader p.9
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-5-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.204–205,210–211,220–221 / reader pp.8–9,14–15,24–25
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-6-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section2.3.2–2.4 and Tables1–4, printed pp.205–210 / reader pp.9–14
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-7-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.205–207 / reader pp.9–11, worst-case analysis and Theorem2.12
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-8-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Journal pp.197–221 / reader pp.1–25; received/revised dates on p.221; author
    bibliography conference entry
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-limitation-9-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.198–201 / reader pp.2–5; successor minima, initialization/selection
    and step6 parent queue
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: ma-definition-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Sections2.1–2.2, printed pp.198–201 / reader pp.2–5
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior primary-source reading supports the selected procedural definition
    with the retained limitations.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-accepted-preview
  kind: record_content
  reference: /private/tmp/aimech-ma-mao-native-preview-20261016/MAOStar.preview.json
  locator: complete scientific fields; curation is prior TEMP-only provenance
  accessed_at: '2026-10-16T04:29:46.871214Z'
  support: context_only
  summary: Exact accepted native preview with provisional source-scoped identity.
    Future current identity/owner, curation time and canonical correspondence remain
    unset.
  snapshot_sha256: c5df5caef85bc9cf6029f311b84ff198769ca7bc50fb3b640a56f6c692c016bf
- evidence_id: mao-claim-1-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section3–3.1, printed pp.211–213 / reader pp.15–17, initialization, termination
    and step3.1
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-claim-2-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Algorithm MAO*, printed pp.212–213 / reader pp.16–17, steps1 and3.2
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-claim-3-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Section3.1 prose on p.212; steps3.2(vi),4.2 on pp.213–214; Figure2(f)–(g)
    on p.216 / reader pp.16–18,20
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-claim-4-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Algorithm MAO*, printed pp.213–214 / reader pp.17–18, steps4.2.1–4.2.3
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-claim-5-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Algorithm MAO*, printed p.214 / reader p.18, steps5–6
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-claim-6-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Theorem3.5 and proof, printed p.219 / reader p.23; game-tree discussion
    on p.220 / reader p.24
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior inspected scan passages support this source-specific claim; retain
    all associated scope qualifications.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-1-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.211–212,214,219 / reader pp.15–16,18,23
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-2-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.212–214,216 / reader pp.16–18,20, Section3.1, steps3.2(vi)/4.2
    and Figure2(f)–(g)
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-3-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Theorem3.4 and proof, printed pp.218–219 / reader pp.22–23
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-4-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.212–214,219 / reader pp.16–18,23
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-5-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.205–207,219 / reader pp.9–11,23
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-6-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.205–210,219–220 / reader pp.9–14,23–24
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-7-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Printed pp.219–220 / reader pp.23–24
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-limitation-8-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Journal pp.197–221 / reader pp.1–25; author bibliography and source-acquisition
    receipts
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Source passage and attributed bounded reasoning establish the need to retain
    this limitation; this is not a new canonical defect finding.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: mao-definition-source
  kind: primary_source
  reference: /private/tmp/aimech-ma-mao-scientific-data-draft-20261016/public-reader-scan-bundle.json
  locator: Sections3–3.1, printed pp.211–214 / reader pp.15–18
  accessed_at: '2026-10-16T02:59:32Z'
  support: supports
  summary: Prior primary-source reading supports the selected procedural definition
    with the retained limitations.
  snapshot_sha256: 199bddda69540c8c68cf7e2e72ac33cfbf1df8c9a3d2e97e2e5c8e98931fa17c
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-cohort360-write.json
  snapshot_sha256: 64659bb7370e42f947a1b3aa19fb5e4b8feca46921e81aa9c94f50db486a2328
  accessed_at: '2026-10-16T04:39:48.985756Z'
  support: context_only
  summary: Actual exclusive creation of two native records, report pair and CREATE
    history.
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-capture.json
  snapshot_sha256: bd33ae1600db120a9e99740bcdb7de879b8f4f1d20cd6e7fac31368702fd2476
  accessed_at: '2026-10-16T04:39:48.985939Z'
  support: context_only
  summary: Actual canonical input-byte and maintained-target capture.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/root-generation-reading.json
  snapshot_sha256: f1d74801b291b1e4c71104fec9fd2fa5a6dd9476efd2af5cd9971052dc075a06
  accessed_at: '2026-10-16T04:39:48.986094Z'
  support: context_only
  summary: Actual root reading of source-scoped canonical records, metadata and all
    retained question objects; historical source reading stays separately attributed.
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort360-governance-20261016/assessment.json
  snapshot_sha256: d8c4c54d3e18dc005c175212de16b875f64fcd9a45a5d25f42b2853d81a8da0e
  accessed_at: '2026-10-16T04:39:48.989113Z'
  support: context_only
  summary: Actual byte preservation, dynamic owner-plan reconstruction, inherited
    metadata and parsed-page audit.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort360-governance-20261016/rendered-pages.json
  snapshot_sha256: b2d67bae3dc5eacc4997e5c12dea27aab7c42ac38b8d17f04e9e696ff7e72703
  accessed_at: '2026-10-16T04:39:48.989266Z'
  support: context_only
  summary: Actual generated-page bytes and parsed content; no visual/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort360-actual-adversarial-review-20261016/assessment.preliminary.json
  snapshot_sha256: 31b8227a882046a597a70523e0900321975675e0b397f10fd6ed99edcad3193f
  accessed_at: '2026-10-16T04:39:48.989460Z'
  support: context_only
  summary: Actual record scientific assessment with its own attributed source-reading
    scope.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort360-current-collection-20261016/collection.json
  snapshot_sha256: 3081d71c9ae6b0285d536e7eb7c010e9ca505e7dc84a7a7b8580e29b70518946
  accessed_at: '2026-10-16T04:39:48.992852Z'
  support: context_only
  summary: Actual scoped ignored-inclusive identity collection; mechanical capture
    is distinct from human semantic reading.
  search_scope: Four recorded roots, ignored andhidden included,945occurrences215groups,1241identity
    records; complete current absence only for recordedcandidate/context probes. Full
    current context is attributed to the identity receipt, not broader all-literature
    absence.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort360-current-identity-audit-20261016/assessment.json
  snapshot_sha256: 2261c117781ed7353a31413f597423a6312894e052989e3e237f034eef3c5a2c
  accessed_at: '2026-10-16T04:39:48.993013Z'
  support: context_only
  summary: Actual attributed current identity and source-question assessment.
  search_scope: Four recorded roots, ignored andhidden included,945occurrences215groups,1241identity
    records; complete current absence only for recordedcandidate/context probes. Full
    current context is attributed to the identity receipt, not broader all-literature
    absence.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort360-final-inputs-20261016/decisions.json
  snapshot_sha256: 4ded714c62d8a3461431aba09b3a2dc2098d64e364a5037d544f7f499274fd8e
  accessed_at: '2026-10-16T04:39:48.993347Z'
  support: context_only
  summary: Exact current record identity decisions, dynamic accepted ownership and
    retained source questions.
- evidence_id: ownership-plan
  kind: record_content
  reference: /private/tmp/aimech-cohort360-current-ownership-proposal-20261016/ownership-plan.proposed.json
  snapshot_sha256: 3d9d9aaeb1d1f99de2f1a1c09de4d15cc8dac24f7b5a6fc60e72df0eff072369
  accessed_at: '2026-10-16T04:39:48.993611Z'
  support: context_only
  summary: Exact shared-source responsibilities:10 bibliography,6 variants,2 retrieval
    questions,1 conference-version object,2 historical responsibilities and6 source
    qualifications; current additional questions remain explicit.
- evidence_id: ownership-plan-acceptance
  kind: record_content
  reference: /private/tmp/aimech-cohort360-final-inputs-20261016/ownership-acceptance.json
  snapshot_sha256: 84e6dc4c9c03fc02463e4b460d26dff64ffaaaa91158b87ab0b4b6a2791904b6
  accessed_at: '2026-10-16T04:39:48.993808Z'
  support: context_only
  summary: Actual root acceptance of current source responsibility; no whole-issue
    closure.
- evidence_id: current-discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T042347Z-ma-star-and-mao-star.json
  snapshot_sha256: 4575b88d2f6496e13bfa1772ea3ec12371289f8ffa8e25afa07a8f250eda818c
  accessed_at: '2026-10-16T04:39:49.004924Z'
  support: context_only
  summary: Canonical durable report containing the exact recursively queryable predecessor_state
    bundle and separate current pair source responsibilities.
- evidence_id: durable-source-manifest
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T042347Z-ma-star-and-mao-star.json
  snapshot_sha256: 4575b88d2f6496e13bfa1772ea3ec12371289f8ffa8e25afa07a8f250eda818c
  accessed_at: '2026-10-16T04:39:49.014902Z'
  support: context_only
  summary: Actual canonical source_durability embeds the reconstructible exact JSON
    manifest and all100 original asset metadata/provenance objects. SHA-256 does not
    identify a publisher PDF.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/ma-star-and-mao-star/2026-10-16T042411Z-codex-a6f975.yaml
  snapshot_sha256: cd3dc113fdcf98dc8782e27e936480d5a59240972b8a5f263d4abda289154300
  accessed_at: '2026-10-16T04:39:49.015117Z'
  support: context_only
  summary: Actual single CREATE event for the report.
- evidence_id: review-support
  kind: record_content
  reference: /private/tmp/aimech-cohort360-consumer-preparation-20261016/review-support.prepared.json
  snapshot_sha256: 14186eb8b9134722f646caf98a6fb6fb4cea80f6dd790d973ad40b20ddc65a4f
  accessed_at: '2026-10-16T04:39:49.015554Z'
  support: context_only
  summary: Exact historical per-claim and per-limitation narrative support.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-gate.json
  snapshot_sha256: bdb257324e4b7a496036c8976674187264fc19f1ba934eb3574403139b689ed0
  accessed_at: '2026-10-16T04:32:53.425141Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-vendor.json
  snapshot_sha256: de1437d5701c860469fd0c2474fd52e59497b90cf3370c5be0d577746c20db3a
  accessed_at: '2026-10-16T04:32:54.692423Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-check-source.json
  snapshot_sha256: a504b179039e339c639298c3256e345990de2c5fafef87dc6060e6a332dde29f
  accessed_at: '2026-10-16T04:32:56.604156Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-render.json
  snapshot_sha256: b50c934127456f2f01d625533394d67e62f025834fb12d47179169eed24eaa0a
  accessed_at: '2026-10-16T04:24:38.663441Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-render-check.json
  snapshot_sha256: 911d88857bea4953eab39125d4976d7d8cc26eed1850aed233c8f8524727f713
  accessed_at: '2026-10-16T04:33:06.767372Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort360-postwrite-20261016/actual-check-diff.json
  snapshot_sha256: 6d9d6cfde604715f068b59681dfb9ead1f050cc01e03431d7b2e7f709f3cf5b4
  accessed_at: '2026-10-16T04:33:06.900449Z'
  support: context_only
  summary: Actual completed required command, exit0; scope is its recorded output.
assessments:
- assessment_id: ma-claim-separate-successor-bounds
  area: evidence
  topic: 'MA*: separate-successor-bounds'
  outcome: supported
  summary: The source distinguishes absent-successor versus all-successor minima explicitly.
    Do not collapse f and F or replace successor-specific estimates with SMA* single-node
    f.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-1-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: For each node n, MA* stores g(n), depth d(n), and a remaining-cost estimate
    h(n,m) for each successor. It defines hf(n) as the minimum over successors absent
    from the explicit tree and hF(n) as the minimum over all successors; f(n)=g(n)+hf(n)
    is used for expansion selection and F(n)=g(n)+hF(n) for backed-up cost and pruning.
- assessment_id: ma-claim-selection-and-continuation
  area: evidence
  topic: 'MA*: selection-and-continuation'
  outcome: supported
  summary: The displayed Select2 compares the new child against the savedGL and jumps
    directly to the goal test/expansion. This is stronger than merely saying minimum-f
    frontier search; it retains the exact phase order.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-2-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Select the OPEN node with minimum f, breaking ties toward greater depth,
    and save its value as GL. Generate its next most promising absent successor. If
    that child has f<=GL, continue directly from it; otherwise perform bottom-up revision
    and the memory check before returning to global selection. A node with no ungenerated
    successors leaves OPEN for CLOSED.
- assessment_id: ma-claim-pathmax-and-branch-backup
  area: evidence
  topic: 'MA*: pathmax-and-branch-backup'
  outcome: supported
  summary: The high-resolution diagnostic confirms h(m,q) in both sides of the assignment;
    the independent reviewer retracted its earlier index-reading error. This claim
    asserts the printed tree operations, not a general graph consistency theorem.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-3-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: For a generated child m of n and q in S(m), pathmax raises h(m,q) to at
    least h(n,m)-c(n,m). Bottom-up revision increases a parent branch estimate h(q,p)
    to hF(p)+c(q,p) when that value is larger, recalculates the parent hF and F, and
    propagates the revision upward. Retained branch bounds carry information about
    subsequently pruned descendants.
- assessment_id: ma-claim-base-pruning-rule
  area: evidence
  topic: 'MA*: base-pruning-rule'
  outcome: supported
  summary: The source maximum-F equality is the base stopping test. The added count<=theta*MAX
    alternative belongs to the separate theta-pruning variant, so it is not imported
    here.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-4-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: If count exceeds MAX after revision, repeatedly select the OPEN leaf with
    greatest F, breaking ties toward shallower depth. If its F equals the root F,
    stop pruning and return to selection; otherwise remove it, decrement count, reopen
    its parent from CLOSED if needed and recompute that parent’s hf and f. Base MA*
    does not stop pruning merely because count has fallen to MAX.
- assessment_id: ma-claim-source-memory-measure
  area: evidence
  topic: 'MA*: source-memory-measure'
  outcome: supported
  summary: The displayed count starts at zero with the root already present. The bound
    is retained as a source statement with its exact path-length definition, not independent
    certification or a portable allocator guarantee.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-5-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: MAX denotes extra search storage. The paper states count<=MAX+|C*|, with
    |C*| defined as the greatest length of a path whose f value is at most the optimal
    solution cost C*. This is a source-specific search-state count statement, conditional
    on the relevant quantity being finite, rather than a strict total-memory or byte
    cap.
- assessment_id: ma-claim-memory-endpoint-boundary
  area: evidence
  topic: 'MA*: memory-endpoint-boundary'
  outcome: supported
  summary: Both endpoint descriptions occur together with an explicit ordering distinction.
    This is identity/scope evidence, not a universal expansion-count or runtime improvement.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-claim-6-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: With sufficiently large MAX, pruning is avoided and the source describes
    A*-like operation with one successor generated at a time. With MAX=0 it describes
    an iterative-deepening-like procedure whose backed-up successor ordering differs
    from the cited IDA* comparator. These endpoint comparisons do not make the complete
    parameterized MA* procedure an alias of A* or IDA*.
- assessment_id: ma-limitation-1
  area: scope
  topic: 'MA*: retained limitation 1'
  outcome: supported
  summary: 'MA-GRAPH-SCOPE: preserve the root-identified boundary. No constructed
    graph counterexample was executed or claimed.'
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-1-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed MA* procedure is for trees. Its graph-extension paragraph
    asserts that pathmax removes CLOSED reopening, but a complete graph duplicate,
    cycle and improved-path update policy is not specified here; no general graph-search
    correctness guarantee is inferred from path-local monotonicity.
- assessment_id: ma-limitation-2
  area: scope
  topic: 'MA*: retained limitation 2'
  outcome: supported
  summary: 'Q2: the retained geometric-cost reasoning example and independent bounded
    review challenge that inference without claiming failure on the finite puzzle
    experiments.'
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-2-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source assumes admissible lower-bound heuristic estimates. Its infinite-graph
    termination argument uses finite positive individual arc costs, which alone do
    not exclude an infinite path with finite total cost. Unrestricted termination
    is not certified; finite relevant cost contours or suitable stronger premises
    would need a separate argument and are not attributed as printed assumptions.
- assessment_id: ma-limitation-3
  area: scope
  topic: 'MA*: retained limitation 3'
  outcome: supported
  summary: 'Q3: distinguish source state-count convention from byte allocation; do
    not silently add missing root/bookkeeping terms to the author theorem.'
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-3-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: MAX and count do not measure portable total machine memory. The root is
    present while count initializes to zero; successor estimates, node fields, OPEN/CLOSED
    structures and transient generation must be accounted for in an implementation.
    MAX=0 is not zero storage, and a finite MAX+|C*| statement requires a finite relevant
    |C*|.
- assessment_id: ma-limitation-4
  area: scope
  topic: 'MA*: retained limitation 4'
  outcome: supported
  summary: The source explicitly attributes observed node-count differences to ordering
    and says IDA* can also be modified; that does not erase the full MA* identity.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-4-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: MA* at its memory endpoints is not treated as exact algorithmic equivalence
    to maintained A* or IDA*. Different successor ordering, partial expansion and
    retained bounds can change its execution; no global duplicate-policy equivalence
    is asserted.
- assessment_id: ma-limitation-5
  area: scope
  topic: 'MA*: retained limitation 5'
  outcome: supported
  summary: All five exact variant objects remain in the unchanged six-object source
    ledger; the sixth concerns MAO* refinements/endpoints.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-5-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: MA*-PP, MA*-thetaP, MA*-phiP, MA*-MO and MA*-VO are retained named variant
    questions. Their admission, pruning, OPEN organization or secondary-storage choices
    are not silently included in the base procedure, asserted as aliases, or accepted
    as separate concepts.
- assessment_id: ma-limitation-6
  area: scope
  topic: 'MA*: retained limitation 6'
  outcome: supported
  summary: The research receipt distinguishes ordinary Manhattan in the endpoint comparison
    from the modified estimates used for later comparisons. OCR/table limitations
    and full original visual reading remain attributed.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-6-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The reported experiments concern particular Fifteen Puzzle problems and
    heuristic settings. Later comparisons modify Manhattan estimates at nongoals,
    and node counts need not decrease monotonically with memory. No universal runtime,
    expansion-count improvement or benchmark replication is claimed.
- assessment_id: ma-limitation-7
  area: scope
  topic: 'MA*: retained limitation 7'
  outcome: supported
  summary: Keep b and C* dependence and the simplified problem model; do not promote
    source O(MAX) wording to an unconditional complexity claim.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-7-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The worst-case savings analysis assumes a uniform b-ary unit-cost tree,
    zero heuristic and fixed solution depth. Its parameter-dependent node-generation
    calculation is not a graph-independent multivariate or wall-clock-runtime guarantee.
- assessment_id: ma-limitation-8
  area: scope
  topic: 'MA*: retained limitation 8'
  outcome: supported
  summary: 'Q4: preserve actual artifact/version scope and all10 references, the conference
    question and two retrieval leads. A citation does not establish that its original
    was read.'
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-8-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Evidence is the inspected25-page third-party journal scan reproduction,
    not a publisher PDF. The1987 ELDECS conference paper was identified from author
    metadata but not acquired; its exact relationship to the journal version and the
    thesis/other referenced originals remains unresolved.
- assessment_id: ma-limitation-9
  area: scope
  topic: 'MA*: retained limitation 9'
  outcome: supported
  summary: 'MA-PSEUDOCODE-INTERFACES: fresh200–201 visuals and197–201 text confirm
    that these guards/conventions are not explicit in the inspected display. This
    extends scope qualification only; the six positive MA* claims and original eight
    limitations remain unchanged.'
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-limitation-9-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The displayed pseudocode is not certified as a complete executable interface.
    Its upward revision queue has no explicit root-parent stopping guard, successor-minimum
    initialization for goals or dead ends is not fully spelled out, and no OPEN-empty
    failure return is displayed. These conventions remain source questions; no repair
    or general unsolvable-instance behavior is asserted.
- assessment_id: ma-definition
  area: evidence
  topic: 'MA*: definition and concept kind'
  outcome: supported
  summary: The definition identifies the source tree-search procedure through separate
    absent/all-successor bounds, expansion, branch revision and regeneration-aware
    pruning. It does not turn the subsequent graph-extension paragraph into a general
    duplicate-handling or reopening theorem, and it does not equate MAX with a hard
    total-memory cap.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-definition-source
  - ma-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: A memory-controlled heuristic tree-search algorithm that stores separate
    lower bounds for absent and all successors, expands promising continuations, backs
    up successor costs, and prunes selected high-cost leaves while retaining bounds
    for regeneration.
- assessment_id: ma-historical-identity
  area: identity
  topic: 'MA*: source identity and historical comparison'
  outcome: supported
  summary: Use literal MA* with no expanded-name or endpoint aliases. The selected
    tree procedure is distinguished from MREC, SMA*, ITS, A*, IDA* and RBFS-family
    search by its successor-specific f/F bookkeeping, saved-GL continuation and base
    pruning stop. The 797-native/442-AIO inventory and four-root ignored-inclusive
    searches are historical branch358 observations. The provisional ID and exact local
    spelling require a new current-state check before any addition.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-accepted-preview
  - ma-mao-identity-mapping
  - ma-mao-root-identity-mapping
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: This specific selection, f/F bookkeeping, continuation, backup and pruning
    procedure differs from maintained MREC, SMA*, ITS, A*, IDA* and RBFS-family methods.
    An endpoint resemblance or common best-first ancestry is not an exact identity.
    Use the literal source name. No expansion such as Memory-Available A* is asserted
    from an unverified source spelling; named variants and large/zero-memory endpoints
    are not aliases. This is a source-scoped prospective draft, with a provisional
    local ID only. The observed branch358 inventory contained797 native and442 pinned
    AIO records; candidate exact/local IDs, names, aliases and scoped synonyms were
    mechanically compared with no normalized collision. Ignored/hidden-inclusive searches
    covered four roots; fourteen selected native contexts and22 full AIO nodes/133
    relations were read with exact scope in the bound proposal. This historical snapshot
    does not substitute for eventual fresh identity and owner review.
- assessment_id: ma-aio-no-match
  area: grounding
  topic: 'MA*: bounded AIO no-match assessment'
  outcome: supported
  summary: Retain the bounded aio_no_match proposal. In the inspected pinned snapshot,
    neural memory layers/LLMs, classification trees, training/task classes and mathematical
    min/max functions do not denote this resource-controlled tree-search procedure.
    Cost-bound revision alone does not establish learned-from-data or reinforcement-learning
    scope. All 22 target-specific rejection reasons remain exact; this is a curator
    assessment over the disclosed scope, not proof of global ontology absence.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-accepted-preview
  - ma-mao-identity-mapping
  - ma-mao-root-identity-mapping
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'Historical branch358 snapshot: pinned AIO commit397851c547d1c4d8f06ef184f63c1d40bc86937a,
    SHA256 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6. All442
    CLASS identity/synonym fields mechanically compared and class labels read;22 selected
    full nodes and all133 incident relations inspected. Other definitions and external
    definition-source papers were not all reread. This is a bounded pinned-snapshot
    mapping proposal requiring reassessment at eventual curation.'
- assessment_id: ma-boundary
  area: scope
  topic: 'MA*: standalone boundary and unresolved source questions'
  outcome: supported
  summary: Retain MA* as a standalone source-defined procedure, separate from MAO*
    and from its own MA*-PP, thetaP, phiP, MO and VO questions. Large/zero-memory
    resemblances to A*/IDA* do not establish whole-procedure equivalence. The unchanged
    bibliography and variant ledger continues to carry the uninspected-original/version
    questions.
  target_ids:
  - AIMech:MAStar
  evidence_ids:
  - ma-mao-primary-scan
  - ma-accepted-preview
  - ma-mao-source-questions
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Retain proposal only; no source-owner closure, record allocation or ontology
    restructuring is performed.
- assessment_id: mao-claim-marked-partial-solution-graph
  area: evidence
  topic: 'MAO*: marked-partial-solution-graph'
  outcome: supported
  summary: The source changes the objective from a least-cost path to a least-cost
    solution graph. Its explicit acyclic scope is retained; this does not import general
    cyclic AND/OR search.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-1-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: MAO* operates on an acyclic structure of pure AND and OR nodes. It maintains
    a marked partial solution graph rooted at the start and expands a nonterminal
    tip of that marked structure. When the start is labelled SOLVED, the marked structure
    is returned as the solution graph.
- assessment_id: mao-claim-single-or-all-and-generation
  area: evidence
  topic: 'MAO*: single-or-all-and-generation'
  outcome: supported
  summary: This keeps A/N as per-arc/per-node space units, not two counters or a node-only
    cap. The original paper stores estimates for all immediate successors, including
    ungenerated ones.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-2-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Expansion generates the marked successor arc of an OR node, or all successor
    arcs of an AND node. Existing explicit nodes are reused and only missing nodes
    are created. Newly created nodes receive f=h; their successor-specific bounds
    start from their node f at OR nodes and zero at AND nodes. MEMORY increases by
    A per generated arc and N per new node, where A and N are the source’s storage
    costs.
- assessment_id: mao-claim-monotone-cost-backup-with-source-gap
  area: evidence
  topic: 'MAO*: monotone-cost-backup-with-source-gap'
  outcome: supported
  summary: 'Q1 is in the asserted claim itself: the intended prose/example backup
    is supported, while literal executable completeness is withheld. No new pseudocode
    line is supplied and no universal claim about implementations is made.'
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-3-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source describes revising a successor-specific bound with the child
    f plus arc cost and raising node f only when the newly aggregated cost is greater.
    OR aggregation takes a minimum; AND aggregation uses the problem’s Phi operation,
    with sum and maximum given as examples. The displayed expansion includes the branch
    update, but the later parent-revision queue does not explicitly show every parent-arc
    refresh needed by the prose and worked trace.
- assessment_id: mao-claim-marking-solved-and-parent-propagation
  area: evidence
  topic: 'MAO*: marking-solved-and-parent-propagation'
  outcome: supported
  summary: These are the literal marking and queue guards. The separate parent-arc
    refresh gap remains binding; describing queued parents does not silently certify
    full cost propagation.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-4-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: For an OR node, mark a minimum-bound successor, preferring a SOLVED child
    and then the currently marked child when ties remain; label the parent SOLVED
    when its marked child is present and SOLVED. At an AND node mark all successors
    and label it SOLVED when all are present and SOLVED. Cost revision processes descendants
    before ancestors and queues marked parents when a node’s f changes or it is labelled
    SOLVED.
- assessment_id: mao-claim-unmarked-arc-and-orphan-pruning
  area: evidence
  topic: 'MAO*: unmarked-arc-and-orphan-pruning'
  outcome: supported
  summary: The initial choice is some eligible unmarked OR arc; later suggestions
    to choose the largest branch bound are not imported. The no-eligible-arc exit
    matters because protected solution storage can exceed MAX.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-5-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: When memory exceeds MAX and the root is not SOLVED, choose an unmarked
    outgoing arc of an OR node for pruning. Remove that arc and recursively remove
    nodes and their outgoing arcs only when they become parentless; shared nodes with
    remaining parents are retained. Stop when no eligible arc exists or MEMORY<=theta*MAX.
    This protects the marked partial solution structure.
- assessment_id: mao-claim-solution-graph-memory-scope
  area: evidence
  topic: 'MAO*: solution-graph-memory-scope'
  outcome: supported
  summary: This preserves the author-defined units and formula as a stated result.
    The finiteness, bookkeeping and control-flow qualifications remain; no byte-level
    implementation bound or proof certification is supplied.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-claim-6-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The paper states a bound MAX+|C*|, where |C*| is the maximum storage required
    by a partial solution graph of pathmax cost at most optimal solution cost C*.
    This solution-graph quantity differs from the path-length quantity used for MA*.
    The stated post-pruning bound is max(MAX,|C*|), not an unconditional hard MAX
    cap.
- assessment_id: mao-limitation-1
  area: scope
  topic: 'MAO*: retained limitation 1'
  outcome: supported
  summary: The source explicitly excludes ordinary graphs with loops for MAO*. Imported
    reference4 supplies additional setting details not freshly investigated here.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-1-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The inspected procedure is for acyclic AND/OR graphs with pure node types
    and a specified problem-cost aggregation. It is not a general cyclic-graph version
    of MA*, and the examples sum/max do not certify arbitrary aggregation operators
    or imported uninspected AO* assumptions.
- assessment_id: mao-limitation-2
  area: scope
  topic: 'MAO*: retained limitation 2'
  outcome: supported
  summary: 'Q1: the trace raises A-to-B from3 to5 when B rises from2 to4 with unit
    arc cost. The independent reviewer agrees with this bounded source fidelity issue.'
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-2-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'The parent-arc refresh in cost propagation is not fully explicit in the
    printed pseudocode: updated child f values queue marked parents, whose aggregation
    reads stored successor-specific bounds. The prose and Figure2 require a refreshed
    parent branch bound. This omission/implicit-operation question is retained without
    silently repairing the algorithm or asserting that every implementation is wrong.'
- assessment_id: mao-limitation-3
  area: scope
  topic: 'MAO*: retained limitation 3'
  outcome: supported
  summary: 'Q2: retain the independent geometric-cost reasoning boundary. This is
    not an execution or a new proof of the author’s finite-instance statements.'
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-3-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The source’s positive-individual-arc-cost argument does not by itself establish
    termination on arbitrary infinite graphs, because bounded-cost infinite paths
    can exist. Its finite zero-cost and game-tree statements are also not independently
    certified here. No missing uniform lower-bound or finite-contour premise is falsely
    attributed to the printed theorem.
- assessment_id: mao-limitation-4
  area: scope
  topic: 'MAO*: retained limitation 4'
  outcome: supported
  summary: 'Q3: source units differ from MA* count/path length. Preserve |C*| as maximal
    relevant partial-solution storage and require finiteness before interpreting it
    as a finite bound.'
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-4-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: A and N represent per-arc and per-node storage in the source model. Marked
    solution structure can remain after pruning when no eligible unmarked arc exists,
    and expansion precedes the memory check. Successor estimates, data structures
    and transient allocations require implementation accounting; MAX=0 is not zero
    memory and MAX is not a strict total byte cap.
- assessment_id: mao-limitation-5
  area: scope
  topic: 'MAO*: retained limitation 5'
  outcome: supported
  summary: Keep the source’s uniform-tree/zero-heuristic comparison context and no
    theorem-certification boundary; source O(MAX) wording is not a standalone implementation
    guarantee.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-5-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Theorem3.6 states analogous node-generation savings for AND/OR trees using
    the preceding simplified MA* analysis. It does not establish a general runtime
    bound, unrestricted graph efficiency or a universal monotonic benefit from increasing
    memory.
- assessment_id: mao-limitation-6
  area: scope
  topic: 'MAO*: retained limitation 6'
  outcome: supported
  summary: Avoid transferring ordinary-search tables to the AND/OR algorithm. No author
    code or experiment was run.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-6-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The numerical Fifteen Puzzle study evaluates MA* and its pruning variants,
    not an empirical benchmark of MAO*. The article’s possible game-tree and alternative-pruning
    uses do not supply a measured general MAO* performance advantage.
- assessment_id: mao-limitation-7
  area: scope
  topic: 'MAO*: retained limitation 7'
  outcome: supported
  summary: Preserves the sixth named-variant/endpoints object plus relevant bibliography
    references, without changing future responsibility.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-7-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The MAX=0 iterative-deepening behavior, large-MAX AO*/MarkA-like cases,
    possible game-tree SSS* relationships and proposed alternate pruning policies
    remain scoped source questions. They are not aliases, accepted independent concepts
    or an inspection of the cited original algorithms.
- assessment_id: mao-limitation-8
  area: scope
  topic: 'MAO*: retained limitation 8'
  outcome: supported
  summary: 'Q4: the source manifest hash is explicit. All10 bibliography objects,
    six variant questions, two retrieval leads and conference question remain unchanged.'
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-limitation-8-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - ma-mao-source-questions
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Evidence is the inspected25-page public third-party reproduction of the
    journal article. No publisher PDF byte identity is established; the1987 conference
    full text and thesis were not acquired, and the exact version relationship or
    potential primary clarification of the backup display remains unresolved.
- assessment_id: mao-definition
  area: evidence
  topic: 'MAO*: definition and concept kind'
  outcome: supported
  summary: The definition retains acyclic pure AND/OR solution-graph search, a marked
    partial solution structure and unmarked-arc/orphan pruning. It describes the intended
    source mechanism while the explicit parent-arc refresh question remains in the
    claim and limitations; no complete executable implementation is certified.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-definition-source
  - mao-accepted-preview
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: A memory-controlled heuristic search algorithm for acyclic AND/OR graphs
    that expands a marked partial solution graph, revises lower-bound costs through
    OR selection and AND aggregation, and prunes unmarked OR arcs with newly orphaned
    descendants while preserving the marked structure.
- assessment_id: mao-historical-identity
  area: identity
  topic: 'MAO*: source identity and historical comparison'
  outcome: supported
  summary: Use literal MAO* with no alias to MA*, AO*, cyclic AND/OR algorithms, importance-sampling
    AOAS or later modified cutoff variants. Its objective and marking/arc-pruning
    state distinguish it from ordinary path search. The bound 797-native/442-AIO inventory
    is historical, not evidence of current absence. The provisional ID and its local
    spelling require a new current-state check before addition.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-accepted-preview
  - ma-mao-identity-mapping
  - ma-mao-root-identity-mapping
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: The marked AND/OR solution structure, successor-specific bounds, AND/OR
    generation and arc/orphan pruning differ from the ordinary-path MA* procedure
    and maintained importance-sampling AOAS. The source’s relation to AO* is a refinement
    context, not an established alias. Use the literal source name. Do not merge MAO*
    with MA*, AO*, cyclic AND/OR algorithms or the modified cutoff variant. This is
    a source-scoped prospective draft, with a provisional local ID only. The observed
    branch358 inventory contained797 native and442 pinned AIO records; candidate exact/local
    IDs, names, aliases and scoped synonyms were mechanically compared with no normalized
    collision. Ignored/hidden-inclusive searches covered four roots; fourteen selected
    native contexts and22 full AIO nodes/133 relations were read with exact scope
    in the bound proposal. This historical snapshot does not substitute for eventual
    fresh identity and owner review.
- assessment_id: mao-aio-no-match
  area: grounding
  topic: 'MAO*: bounded AIO no-match assessment'
  outcome: supported
  summary: Retain the bounded aio_no_match proposal. An acyclic AND/OR decomposition
    with cost aggregation is not thereby a probabilistic graphical model, graph neural
    network, classifier, memory-augmented LLM or reinforcement-learning method. Data
    representations and component min/max operations do not identify the algorithm.
    All 22 rejection reasons remain exact and require reassessment at eventual curation.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - mao-accepted-preview
  - ma-mao-identity-mapping
  - ma-mao-root-identity-mapping
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: 'Historical branch358 snapshot: pinned AIO commit397851c547d1c4d8f06ef184f63c1d40bc86937a,
    SHA256 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6. All442
    CLASS identity/synonym fields mechanically compared and class labels read;22 selected
    full nodes and all133 incident relations inspected. Other definitions and external
    definition-source papers were not all reread. This is a bounded pinned-snapshot
    mapping proposal requiring reassessment at eventual curation.'
- assessment_id: mao-boundary
  area: scope
  topic: 'MAO*: standalone boundary and unresolved source questions'
  outcome: supported
  summary: Retain MAO* separately from MA* because marked AND/OR solution graphs,
    per-arc/per-node accounting and orphan-aware arc pruning change both objective
    and state. AO*/MarkA-like endpoints, game-tree SSS* relations and alternate pruning
    policies remain scoped questions. Do not transfer MA* Fifteen Puzzle results as
    empirical evidence for MAO*.
  target_ids:
  - AIMech:MAOStar
  evidence_ids:
  - ma-mao-primary-scan
  - mao-accepted-preview
  - ma-mao-source-questions
  - ma-mao-accepted-support
  - actual-write
  - postcapture-reading
  - actual-scientific-assessment
  details: Retain proposal only; no source-owner closure, record allocation or ontology
    restructuring is performed.
- assessment_id: ma-mao-future-governance
  area: provenance
  topic: Actual canonical correspondence, current ownership and durable source preservation
  outcome: supported
  summary: 'Actual records retain12 claims and17 limitations, two source rows and
    one shared defining JSON scan-manifest artifact. Five exclusive creation outputs
    and one CREATE event are bound. Exact38592-byte manifest recovery and all100 asset
    metadata/hash/provenance objects are verified from the canonical report. Current
    dynamic owner changes and additions exactly follow the accepted plan: {"additional_source_question_count":
    0, "bibliography_occurrences": 10, "changed_main_indexes": [911], "changed_nested_indexes":
    [], "conference_version_questions": 1, "historical_source_responsibilities": 2,
    "main": 914, "nested": 394, "new_main_rows": 0, "new_nested_rows": 0, "retained_variant_questions":
    6, "retrieval_questions": 2, "source_qualifications": 6}. Ten bibliography, six
    variant, two retrieval, one1987 version, two historical responsibility and six
    source-qualification objects remain distinct. The complete actual359 predecessor
    projection preserves original402/404/406 and356/357/358/359 source responsibilities.
    68 unique captured inputs, actual parsed generated pages and six successful required
    checks are bound. No source exhaustion, independent approval, issue closure or
    publication result is implied.'
  target_ids:
  - AIMech:MAStar
  - AIMech:MAOStar
  evidence_ids:
  - actual-write
  - captured-inputs
  - postcapture-reading
  - governance-assessment
  - rendered-pages
  - actual-scientific-assessment
  - creation-history
  - current-discovery-report
  - durable-source-manifest
  - root-decisions
  - ownership-plan
  - ownership-plan-acceptance
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
  details: Actual canonical records, source questions, inherited source responsibilities,
    exact manifest bytes, all100 asset metadata entries and capture/check receipts
    were assessed at their recorded times. Historical source reading remains separately
    attributed. Review save, exact-head review, publication and merge are subsequent
    steps.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:MAStar
  rationale: Retain MA* as a standalone source-defined procedure, separate from MAO*
    and from its own MA*-PP, thetaP, phiP, MO and VO questions. Large/zero-memory
    resemblances to A*/IDA* do not establish whole-procedure equivalence. The unchanged
    bibliography and variant ledger continues to carry the uninspected-original/version
    questions.
  evidence_ids:
  - ma-mao-primary-scan
  - ma-accepted-preview
  - ma-mao-source-questions
  - ma-mao-accepted-support
  - actual-write
  - root-decisions
  - postcapture-reading
- action: retain
  target_ids:
  - AIMech:MAOStar
  rationale: Retain MAO* separately from MA* because marked AND/OR solution graphs,
    per-arc/per-node accounting and orphan-aware arc pruning change both objective
    and state. AO*/MarkA-like endpoints, game-tree SSS* relations and alternate pruning
    policies remain scoped questions. Do not transfer MA* Fifteen Puzzle results as
    empirical evidence for MAO*.
  evidence_ids:
  - ma-mao-primary-scan
  - mao-accepted-preview
  - ma-mao-source-questions
  - ma-mao-accepted-support
  - actual-write
  - root-decisions
  - postcapture-reading
targets:
- target_id: AIMech:MAStar
  label: MA*
  path: data/curated/MAStar.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MAStar.yaml
    role: maintained native concept record
- target_id: AIMech:MAOStar
  label: MAO*
  path: data/curated/MAOStar.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MAOStar.yaml
    role: maintained native concept record
limitations:
- Scientific transfer uses exact accepted previews and attributed source/control-flow/mathematical
  reading. No new full25-page visual reading or native validation is claimed by this
  preparation.
- MA* tree/graph and executable-interface boundaries, MAO* parent-arc propagation
  question, positive-individual-cost theorem limits and distinct memory units remain
  explicit.
- Evidence is one exact JSON manifest of25 third-party scan pages. No publisher PDF
  byte identity or inspected1987 conference full text is asserted.
- Ten bibliography entries, six variants, two retrieval leads and the1987 version
  question remain separate from two historical responsibilities and six source qualifications;
  source questions are not automatically concepts.
- The complete actual359 projection retains prior issue/source scopes recursively.
  Additional current questions must be explicitly retained.
- Actual five creation outputs, one CREATE history, 68 capture inputs and 6 parsed
  generated pages are bound. Six required commands passed; earlier failed attempts
  remain explicit. Canonical review save/check and publication are subsequent operations.
tags:
- source-scoped
- memory-bounded-search
- MA-star
- MAO-star
notes:
- The37 scientific assessments and46 evidence templates retain accepted static-fragment
  content. The38th assessment now records actual current governance supported by the
  bound receipts.
- Local evidence access instants are filled from the actual attributed postcapture
  reading. Primary acquisition times preserve their historical instants and are normalized
  to UTC Z. References to preparation in the retained scientific limitations describe
  the historical fragment scope.
- The source manifest exact bytes and all100 asset metadata/provenance objects must
  be reconstructed from the canonical report and verified at capture, save and exact-head
  stages.
- Original source question objects and all Q1–Q4/graph/interface boundaries remain
  queryable; no issue closure or discovery exhaustion is asserted.
- One shared journal source retains ten bibliography entries, six named variant questions,
  two retrieval leads and one 1987 version question. Two historical responsibility
  objects and six source qualifications remain separate; no count asserts new concepts.
- '{"added_record_ids": [], "assessment": "The 1985 Bagchi–Mahanti article supplies
  the C, PropC and MarkA comparison/theory question. It is retained under the current
  memory-search source umbrella; neither the MA*/MAO* pair nor a shared best-first
  vocabulary establishes those source identities.", "disposition": "pending_inspection",
  "exact_original_object": {"authors": "A. Bagchi; A. Mahanti", "future_owner": null,
  "next_check": "C,PropC,MarkA comparison/theory; resolve exact definitions from original
  if needed.", "publication": "JACM32,1–27,1985", "reference_number": 1, "source_locator":
  "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Three approaches to heuristic search in networks"}, "existing_record_ids":
  [], "group": "journal1989", "index": 0, "kind": "bibliography", "next_check": "Read
  the exact 1985 original and compare C, PropC and MarkA definitions, inherited bounds
  and assumptions; reconcile any narrower current owner before further curation.",
  "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "bac149ea23ebbaf47bbb94b9f73f3469cd6d72aa310765b08b4a90b362e7071f", "pointer": "/references/0",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The AAAI1986 game-tree article remains
  a separate ITERSSS* source responsibility. A prospective TEMP draft/native preview
  is not a maintained record in this captured 1241-record inventory and does not authorize
  an ownership resolution here.", "disposition": "pending_inspection", "exact_original_object":
  {"authors": "S. Bhattacharyya; A. Bagchi", "future_owner": null, "next_check": "ITERSSS*
  source question; inspect defining paper before identity or relation decision.",
  "publication": "AAAI1986,163–167", "reference_number": 2, "source_locator": "journalp.221
  / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Making the best use of available memory when searching game trees"}, "existing_record_ids":
  [], "group": "journal1989", "index": 1, "kind": "bibliography", "next_check": "Keep
  the exact historical reference and compare any later accepted ITERSSS* evidence
  with current identity/ownership in its own authorized addition; do not identify
  it with ordinary-tree MA* or AND/OR MAO*.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "02fae9f8e3daa3cf432043822f1a63d13a2121a683fc75d6e43731f80750c3d6", "pointer": "/references/1",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The 1988 thesis is an exact primary-source
  follow-up for multiple OPEN lists, parallel MA*-MO and MAO* backup details. Reading
  the journal scan does not supply the unacquired thesis.", "disposition": "pending_inspection",
  "exact_original_object": {"authors": "P. P. Chakrabarti", "future_owner": null,
  "next_check": "Potential primary clarification of MA*-MO parallel version and MAO*
  backup; full thesis not acquired.", "publication": "PhD thesis,IIT Kharagpur,1988",
  "reference_number": 3, "source_locator": "journalp.221 / readerpage25", "status":
  "retained_bibliographic_context_or_source_question", "title": "Some studies in heuristic
  search theory and algorithms"}, "existing_record_ids": [], "group": "journal1989",
  "index": 2, "kind": "bibliography", "next_check": "Seek the thesis legitimately;
  inspect the relevant original algorithm and version passages before settling parallelization
  or implicit backup operations.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "b4b7515f66b4e57c8d15bc8c4d1d94015fcaa9924bff941790e4732fca9aa27c", "pointer": "/references/2",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The 1988 AO* overestimation paper remains
  the imported AND/OR admissibility/pathmax/WAO* source question. Current WeightedAStar
  is fixed-weight ordinary best-first search and provides a contrast only, not this
  AO* identity or theorem.", "disposition": "pending_inspection", "exact_original_object":
  {"authors": "P. P. Chakrabarti; S. Ghose; S. C. de Sarkar", "future_owner": null,
  "next_check": "Explicit imported AND/OR/pathmax/solution-graph assumptions and WAO*
  reference; inspect original before stronger theorem/weighting statements.", "publication":
  "Artificial Intelligence34,97–113,1988", "reference_number": 4, "source_locator":
  "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Admissibility of AO* when heuristics overestimate"}, "existing_record_ids":
  ["AIMech:WeightedAStar"], "group": "journal1989", "index": 3, "kind": "bibliography",
  "next_check": "Read the original 1988 theorem and algorithm, including solution-graph
  and weighting assumptions; do not transfer Weighted A* guarantees to AO*.", "origin":
  {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "4ee673d6924a66bdfd557bcb67203164f7a9d52950ea3afb15d9df6b11a626dd", "pointer": "/references/3",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Depth_m is a separately cited restricted-memory
  branch-and-bound comparator. Current BreadthFirstBranchAndBound is a layered unit-edge-cost
  procedure and does not resolve Ibaraki’s 1978 method.", "disposition": "pending_inspection",
  "exact_original_object": {"authors": "T. Ibaraki", "future_owner": null, "next_check":
  "Restricted-memory comparator source; no new-concept assertion.", "publication":
  "International Journal of Computer and Information Sciences7,315–343,1978", "reference_number":
  5, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Depth_m search in branch and bound algorithms"}, "existing_record_ids":
  ["AIMech:BreadthFirstBranchAndBound"], "group": "journal1989", "index": 4, "kind":
  "bibliography", "next_check": "Acquire and inspect the exact 1978 Depth_m source,
  its memory parameter and branch-and-bound schedule before any equivalence or record
  decision.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "b9e296846a2f7e700e960934dff5a6b011c6277e3100703790a38263ecd2fb4f", "pointer": "/references/4",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The exact Korf1985 paper is already an
  evidence source of the current IDA* and DFID records. Their cost-threshold versus
  depth-threshold identities are explicit; the historical source’s erratum/access
  and theorem qualifications remain, so this citation is context rather than a new
  concept.", "disposition": "existing_record_context", "exact_original_object": {"authors":
  "R. E. Korf", "future_owner": null, "next_check": "Existing IDA* comparison context;
  no current ownership reconciliation in this dossier.", "publication": "Artificial
  Intelligence27,97–109,1985", "reference_number": 6, "source_locator": "journalp.221
  / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "Depth-first iterative-deepening: An optimal admissible tree search"},
  "existing_record_ids": ["AIMech:IterativeDeepeningAStar", "AIMech:DepthFirstIterativeDeepening"],
  "group": "journal1989", "index": 5, "kind": "bibliography", "next_check": "Retain
  the maintained IDA*/DFID source scopes and their 1986 erratum residual; inspect
  any source-specific stronger comparison before extending the present records.",
  "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "31726a729d8fd82ffb6aae4550c4bcb83555f085ed7229a9a6f4cf7d9bda7a94", "pointer": "/references/5",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The 1987 low-overhead alternatives to SSS*
  paper is a game-tree restricted-memory source question. The accepted MAO* scan comparison
  does not constitute a fresh full reading or identify all SSS* alternatives.", "disposition":
  "pending_inspection", "exact_original_object": {"authors": "T. A. Marsland; A. Reinefeld;
  J. Schaeffer", "future_owner": null, "next_check": "Game-tree restricted-memory
  variants; original not freshly acquired/read.", "publication": "Artificial Intelligence31,185–199,1987",
  "reference_number": 7, "source_locator": "journalp.221 / readerpage25", "status":
  "retained_bibliographic_context_or_source_question", "title": "Low overhead alternatives
  to SSS*"}, "existing_record_ids": [], "group": "journal1989", "index": 6, "kind":
  "bibliography", "next_check": "Read the original algorithms and their game-tree/space
  assumptions, then compare any current game-tree owners; retain each alternative’s
  scope without an alias assertion.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "12cd5640826b81734e4485f8d19bee015282545f694ef2d6681326f3de45192f", "pointer": "/references/6",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The 1984 general branch-and-bound SPLIT/PRUNE
  framework remains an original-source relationship question. Current AStarSearch
  and BreadthFirstBranchAndBound give concrete comparison contexts but do not represent
  the entire framework or its AO* relation.", "disposition": "pending_inspection",
  "exact_original_object": {"authors": "D. S. Nau; V. Kumar; L. N. Kanal", "future_owner":
  null, "next_check": "General SPLIT/PRUNE framework relation; no automatic exact
  mapping.", "publication": "Artificial Intelligence23,29–58,1984", "reference_number":
  8, "source_locator": "journalp.221 / readerpage25", "status": "retained_bibliographic_context_or_source_question",
  "title": "General branch and bound, and its relation to A* and AO*"}, "existing_record_ids":
  ["AIMech:AStarSearch", "AIMech:BreadthFirstBranchAndBound"], "group": "journal1989",
  "index": 7, "kind": "bibliography", "next_check": "Inspect the original SPLIT/PRUNE
  formulation and its stated A*/AO* correspondences; preserve framework-versus-specific-algorithm
  granularity.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "9fb521b7a1628872f9b545d9f692081c130a6857ac02d21584b5721a1d93294b", "pointer": "/references/7",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Nilsson’s 1980 book is retained for imported
  A*/AO* graph and admissibility premises. Current AStarSearch has a separate 1968
  primary source; its presence does not imply a full reading of this book or representation
  of AO*.", "disposition": "pending_inspection", "exact_original_object": {"authors":
  "N. J. Nilsson", "future_owner": null, "next_check": "Imported A*/AO* graph and
  admissibility premises; no full book reading in this dossier.", "publication": "Tioga,Palo
  Alto,1980", "reference_number": 9, "source_locator": "journalp.221 / readerpage25",
  "status": "retained_bibliographic_context_or_source_question", "title": "Principles
  of Artificial Intelligence"}, "existing_record_ids": ["AIMech:AStarSearch"], "group":
  "journal1989", "index": 8, "kind": "bibliography", "next_check": "Read the cited
  book passages when needed for an exact imported premise; retain the distinction
  between current A* context and unresolved AO* assumptions.", "origin": {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "acd720c28ba7e58b910663708ef8846b2431970abe645c55506716b9ee11d01b", "pointer": "/references/8",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Pearl’s 1984 Heuristics is retained for
  search theory and A_epsilon* context. Current AStarSearch and BestFirstSearch provide
  neighboring strategy definitions, not a read or accepted identity for every book
  method.", "disposition": "pending_inspection", "exact_original_object": {"authors":
  "J. Pearl", "future_owner": null, "next_check": "Search theory/A_epsilon* context;
  no full book reading in this dossier.", "publication": "Addison-Wesley,Reading,1984",
  "reference_number": 10, "source_locator": "journalp.221 / readerpage25", "status":
  "retained_bibliographic_context_or_source_question", "title": "Heuristics"}, "existing_record_ids":
  ["AIMech:AStarSearch", "AIMech:BestFirstSearch"], "group": "journal1989", "index":
  9, "kind": "bibliography", "next_check": "Inspect the specific book passages and
  A_epsilon* definition before any identity or bound claim; do not replace a restricted-candidate
  policy with generic best-first selection.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "7325a4e3d95733bc98f90c4321c9c6bb79647ad5b34fdadc5fcfb81c70dd5bb4", "pointer": "/references/9",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Pre-emptive admission is a named MA* policy
  with the retained source condition f(child)<=GL. The base MA* record does not decide
  standalone identity for MA*-PP.", "disposition": "pending_inspection", "exact_original_object":
  {"label": "MA*-PP", "locator": "p.204", "question": "Does pre-emptive admission
  deserve a standalone identity or remain a named MA* policy? Retain exact acceptance
  condition f(child)<=GL."}, "existing_record_ids": [], "group": "journal1989", "index":
  0, "kind": "named_variants", "next_check": "Compare the complete admission/pruning
  control flow and decide policy-versus-concept granularity only after current identity
  review.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "2bc4c16b5674f58f4f32e4f76dbde04c0c74eb2dabd31f7aa5b8834b82109293", "pointer": "/named_variant_questions/0",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The source-defined fractional-pruning policy
  keeps theta in [0,1]. It remains a variant question rather than a second resolved
  record or an alias of every pruning policy.", "disposition": "pending_inspection",
  "exact_original_object": {"label": "MA*-thetaP", "locator": "p.205", "question":
  "Retain fractional pruning as a source-defined policy, with theta in[0,1]; identity
  granularity undecided."}, "existing_record_ids": [], "group": "journal1989", "index":
  1, "kind": "named_variants", "next_check": "Retain the exact theta parameter range
  and inspect whether any proposed standalone identity changes the base algorithm
  beyond a policy choice.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "f29f026f525fb32c01717a550af134246b3c2f589132697193099329cf738e6c", "pointer": "/named_variant_questions/1",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Depth-sensitive MA*-phiP preserves the
  scan’s uppercase F equality. Neither a spelling normalization nor theta-pruning
  similarity settles this policy’s identity.", "disposition": "pending_inspection",
  "exact_original_object": {"label": "MA*-phiP", "locator": "p.210", "question": "Retain
  depth-sensitive pruning and uppercase F equality from scan; no alias with theta
  pruning."}, "existing_record_ids": [], "group": "journal1989", "index": 2, "kind":
  "named_variants", "next_check": "Compare the source’s exact depth-sensitive rule
  and uppercase F with theta pruning before any policy identity decision.", "origin":
  {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "22083158a6cd1ebc6fba064d0dac0e41a106f9795ff6953d1ea5e7dbf5b1984b", "pointer": "/named_variant_questions/2",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Multiple OPEN-list organization and the
  thesis’s parallel extension remain separate source and implementation-granularity
  questions. The journal-based MA* record does not certify the uninspected thesis
  extension.", "disposition": "pending_inspection", "exact_original_object": {"label":
  "MA*-MO", "locator": "p.211", "question": "Multiple OPEN-list organization and source
  thesis parallel extension; distinct implementation policy versus concept remains
  open."}, "existing_record_ids": [], "group": "journal1989", "index": 3, "kind":
  "named_variants", "next_check": "Inspect the cited thesis and exact OPEN-list selection/parallel
  coordination before standalone curation.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "5d0d1d51a436c3fb0e2c9ab9b82acaa946c3976819d320f66cd527835bab2992", "pointer": "/named_variant_questions/3",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "Virtual OPEN and optional secondary storage
  are retained as source-specific organization choices; no strict RAM or I/O bound
  or standalone identity follows from the base record.", "disposition": "pending_inspection",
  "exact_original_object": {"label": "MA*-VO", "locator": "pp.211,220–221", "question":
  "Virtual OPEN and optional secondary-storage organization; source variant retained
  without automatic standalone concept."}, "existing_record_ids": [], "group": "journal1989",
  "index": 4, "kind": "named_variants", "next_check": "Compare virtual OPEN/secondary-storage
  mechanics and accounting before deciding whether a separate implementation policy
  merits a record.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "86030d600d3b284c2b8149f1165f6d31d75d321c06f54fc80a6dcbc5cb324e4b", "pointer": "/named_variant_questions/4",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "MAX=0, large-MAX and game-tree endpoints
  are qualified source relationships. Existing IDA* and DFID are useful endpoint contrasts,
  not aliases of MAO*, AO*, MarkA or SSS*.", "disposition": "pending_inspection",
  "exact_original_object": {"label": "MAO* refinements and endpoints", "locator":
  "pp.219–220", "question": "Retain MAX=0 iterative-deepening endpoint, large-MAX
  AO*/MarkA-like cases, game-tree SSS* relationship and proposed alternate unmarked-arc
  pruning; do not silently turn these into aliases or separate algorithms."}, "existing_record_ids":
  ["AIMech:IterativeDeepeningAStar", "AIMech:DepthFirstIterativeDeepening"], "group":
  "journal1989", "index": 5, "kind": "named_variants", "next_check": "Inspect each
  endpoint’s complete control flow, memory convention and game-tree/AND-OR assumptions;
  keep alternate unmarked-arc pruning proposed rather than silently implemented.",
  "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "d4d0ac49b104eb94e029a37f41f7095396aee127c4018d810a60885e30dc5548", "pointer": "/named_variant_questions/5",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The exact speculative-search/SB&B/SIDA*
  URL remains search-only. Existing IDA* is a comparison context; neither its name
  nor the retained source title supplies an inspected speculative algorithm.", "disposition":
  "pending_inspection", "exact_original_object": {"label": "Speculative search / SB&B
  / SIDA* comparison", "next_check": "If comparison is needed, inspect its definition
  and node-count convention; a search snippet is not algorithm evidence.", "status":
  "search-only; not acquired or read", "url": "https://wah.cse.cuhk.edu.hk/wah/Wah/papers/C063/C63.pdf"},
  "existing_record_ids": ["AIMech:IterativeDeepeningAStar"], "group": "journal1989",
  "index": 0, "kind": "retrieval_only", "next_check": "Retrieve https://wah.cse.cuhk.edu.hk/wah/Wah/papers/C063/C63.pdf
  and inspect definitions and node-count convention before identity or comparison
  claims.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "8f0d39eb4bf38645d2f593efc84f12cf3e1ee55dbce51009377a42691ab86828", "pointer": "/additional_bounded_retrieval_questions/0",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "This 1992 effective-memory publication
  is already retained in current inherited memory_search_source_accounting/search_only_reconciliation/4
  under main7. Preserve that responsibility and the exact newly retained publisher
  route and IDA*_CRM/IDA*_CRAM spellings. The current IDA* context does not resolve
  the 1991 IDA-CR/CRA versus 1992 retained-memory relationship.", "disposition": "existing_pending_owner",
  "exact_original_object": {"label": "Effective use of memory in iterative deepening
  search / IDA*_CRM / IDA*_CRAM", "next_check": "Preserve retrieved spelling variants
  for later original-source reconciliation; no alias decision.", "status": "search-only;
  existing358 source pointer continuity retained separately", "url": "https://www.sciencedirect.com/science/article/abs/pii/002001909290131E"},
  "existing_record_ids": ["AIMech:IterativeDeepeningAStar"], "group": "journal1989",
  "index": 1, "kind": "retrieval_only", "next_check": "Obtain the exact 1992 original
  at https://www.sciencedirect.com/science/article/abs/pii/002001909290131E; compare
  its retained-memory mechanism, spellings and publication relationship with main7’s
  1991 source without collapsing names.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/bibliography-and-followups.json",
  "sha256": "fe374322f5b363133ef0ee6e254da80bf54ec6726824f3f003e1c5f784dc4c46"}, "original_sha256":
  "1ff781a04b21fa3cbc270694bcaba49692cfada2a849d3fe239c532d23c56305", "pointer": "/additional_bounded_retrieval_questions/1",
  "responsible_owner": {"family": "main", "index": 7}}'
- '{"added_record_ids": [], "assessment": "The exact 1987 ELDECS source-version object
  is already under main911 and remains pending. The 25-page 1989 journal scan does
  not establish conference-to-journal equivalence, first introduction or publisher-byte
  identity.", "disposition": "existing_pending_owner", "exact_original_object": {"object":
  {"assessment": "The 1987 conference-to-1989 MA*/MAO* journal relationship is an
  explicit unresolved source-version question under 911. It is not an additional algorithm
  merely because a separate publication is cited.", "disposition": "existing_pending_owner",
  "exact_original_object": {"candidate": "Tree searching in restricted memory", "discovery":
  "Institutional primary-author bibliography.", "disposition": "pending_publication_relationship",
  "next_check": "Resolve conference-to-journal relationship with the1989 MA*/MAO*
  source; a predecessor publication is not automatically a new concept.", "publication":
  "Chakrabarti, Ghose, Acharya and De Sarkar, ELDECS1987,518–520, author bibliography",
  "source": "https://cse.iitkgp.ac.in/~ppchak/publications.html"}, "existing_record_ids":
  [], "index": 5, "next_check": "Resolve conference-to-journal relationship with the1989
  MA*/MAO* source; a predecessor publication is not automatically a new concept.",
  "original_object_sha256": "0e98a8ebf4b7207f512dfd1902d703b0b3325d08474d9333f1b5683f479028f2",
  "responsible_owner": {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/search_only_reconciliation/5"},
  "existing_record_ids": [], "group": "journal1989", "index": 0, "kind": "conference_version",
  "next_check": "Acquire an author/library copy of the ELDECS1987 pp.518–520 paper
  and compare its actual content with the retained 1989 scan; preserve the institutional
  bibliography URL.", "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json",
  "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256":
  "fe29abe85605da32ff69ffb6e7209f8e331df028e9bbbf3521cbbf709103233c", "pointer": "/source_objects/1",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "assessment": "This historical
  Chakrabarti1989 citation responsibility is proposed to be represented by the two
  distinct accepted source-scoped records: displayed-tree MA* and acyclic AND/OR MAO*.
  Original old full_text_read=false and next_check values remain verbatim provenance.
  The accepted current source is the exact JSON scan manifest and 100 asset objects,
  not a publisher PDF; all six source qualifications and 1987 version question remain
  unresolved. Historical PhilPapers https://philpapers.org/rec/CHAHSI-4 and OUCI https://ouci.dntb.gov.ua/en/works/45XORXv7/
  are same-title retrieval metadata, not further methods or newly inspected originals.",
  "disposition": "represented_by_added_record", "exact_original_object": {"object":
  {"assessment": "This is the explicit unresolved MA*/MAO* source in current memory-search
  owner 911. Adding SMA* does not substitute Russell''s approximate MA* sketch for
  the unavailable original, nor settle ordinary-graph versus AND/OR scope.", "disposition":
  "existing_pending_owner", "exact_original_object": {"authors": "P.P. Chakrabarti,
  S. Ghose, A. Acharya and S.C. de Sarkar", "candidate": "Heuristic search in restricted
  memory", "citation_key": "chakrabarti1989", "disposition": "retained_source_question",
  "full_text_read_in_this_dossier": false, "next_check": "Acquire and fully read MA*/MAO*
  original, retaining the minimum-memory qualification and source-specific variants.",
  "owner_links": [], "publication": "Artificial Intelligence41(2),197–221,1989", "source_occurrences":
  [{"pdf_page": 6, "reference_label": "Chakrabarti et al., 1989", "source_id": "mrec1989"},
  {"pdf_page": 5, "reference_label": "2", "source_id": "sma1992"}, {"pdf_page": 6,
  "reference_label": "1", "source_id": "its1994"}], "source_title_matches": []}, "existing_record_ids":
  [], "index": 1, "next_check": "Acquire and fully read MA*/MAO* original, retaining
  the minimum-memory qualification and source-specific variants.", "original_object_sha256":
  "cca4cb705b6d0445f46f635ca69767b7193a82e6ad62cfefc1865d3df652732a", "responsible_owner":
  {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/bibliography_reconciliation/1"},
  "existing_record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"],
  "group": "journal1989", "index": 0, "kind": "historical_source_responsibilities",
  "next_check": "After authorized addition, retain variants, imported references,
  source-control-flow qualifications and author/publisher version comparison; never
  rewrite the earlier access-gap receipt as if full text had then been available.",
  "origin": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json",
  "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256":
  "4547654d21f5b616e8775020e013704852f81f8f698152eddaa6c74754de3dd2", "pointer": "/source_objects/0",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": ["AIMech:MAStar", "AIMech:MAOStar"], "assessment": "The historical
  combined MA*/MAO* full-text/identity residual is proposed to be represented at base-procedure
  scope by the two distinct records supported by the subsequently acquired 25-page
  public scan. The older source object, failed access and empty read_pages stay exact.
  Current source boundaries include displayed-tree MA*, acyclic AND/OR MAO*, qualified
  memory units and uncompleted pseudocode interfaces; the umbrella remains partial.",
  "disposition": "represented_by_added_record", "exact_original_object": {"object":
  {"assessment": "The original MA*/MAO* full text is still unavailable in the accepted
  dossier. Current owner 911 remains partial after the three separate procedures;
  ordinary versus AND/OR graph scope, minimum memory and exact operations remain open.",
  "disposition": "existing_pending_owner", "exact_original_object": {"candidate":
  "MA* and MAO*", "disposition": "pending_original_full_text_and_identity_reconciliation",
  "next_check": "Acquire and read the original Chakrabarti et al. 1989 article, distinguish
  ordinary-graph MA* from AND/OR MAO*, then compare precise quantities, pruning, backup
  and memory premises with SMA*, MREC and maintained neighboring records. Russell’s
  explicit approximate sketch is not a substitute.", "source": {"access_gap": "Publisher
  search result provides abstract and access options. Direct web open failed with
  internal error. Searches found no acquired legitimate original full-text copy. Other
  papers’ sketches are explicitly secondary for MA*.", "access_level": "publisher
  metadata and abstract; author institutional bibliography", "author_metadata": "https://cse.iitkgp.ac.in/~ppchak/publications.html",
  "authors": ["P. P. Chakrabarti", "S. Ghose", "A. Acharya", "S. C. de Sarkar"], "doi":
  "10.1016/0004-3702(89)90010-6", "primary_pdf": null, "publication": "Artificial
  Intelligence 41(2), 197–221, December 1989", "read_pages": [], "role": "defining
  primary source identified; full text not obtained", "supported_abstract_scope":
  "The publisher abstract distinguishes MA* for ordinary graphs from MAO* for AND/OR
  graphs and conditions its memory/admissibility statement on a minimum memory requirement.
  No unseen algorithms, proofs or parameter choices are reconstructed.", "title":
  "Heuristic Search in Restricted Memory", "url": "https://www.sciencedirect.com/science/article/pii/0004370289900106",
  "visual_pages": []}}, "existing_record_ids": [], "index": 0, "next_check": "Acquire
  and read the original Chakrabarti et al. 1989 article, distinguish ordinary-graph
  MA* from AND/OR MAO*, then compare precise quantities, pruning, backup and memory
  premises with SMA*, MREC and maintained neighboring records. Russell’s explicit
  approximate sketch is not a substitute.", "original_object_sha256": "47e4ec6dbb124db6c44b27d251e52c24b3415da980e3022f9899720eae3c97fc",
  "responsible_owner": {"family": "main", "index": 911}}, "pointer": "/memory_search_source_accounting/residual_reconciliation/0"},
  "existing_record_ids": ["AIMech:MREC", "AIMech:SimplifiedMemoryBoundedAStar", "AIMech:IterativeThresholdSearch"],
  "group": "journal1989", "index": 1, "kind": "historical_source_responsibilities",
  "next_check": "Keep all variant/version/theorem/interface questions pending under
  main911 and preserve the existing22 bibliography/28occurrence plus6lead accounting
  and separate IE owner912. No family exhaustion or issue closure follows.", "origin":
  {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/retained-current-context.json",
  "sha256": "d21e0e25d9101dc5b430f22207473593c729b5d9d5c12da7a86fed635a176248"}, "original_sha256":
  "22200a181af6870bd9f28857c09b648b985e5190e4260dec49bc1b82ba9a737a", "pointer": "/source_objects/2",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The source-local MAO* parent-arc refresh
  omission remains an explicit interface qualification. The prose, printed backup
  and Figure2 are retained together; the base record does not insert an algorithm
  line.", "disposition": "existing_pending_owner", "exact_original_object": {"consequence":
  "A literal transcription lacks the explicit parent-arc refresh needed for the depicted
  propagation. This is an original-source pseudocode omission/implicit-operation question,
  not an OCR error and not a claim that every implementation is incorrect. Preserve
  both prose and pseudocode; do not silently invent an algorithm line.", "id": "Q1",
  "kind": "source_control_flow_qualification", "locator": "p.212 Section3.1; pp.213–214
  steps3.2(vi),4.2.1–4.2.3; p.216 Fig.2(f)–(g)", "next_check": "Independent control-flow
  review, then compare author thesis/errata or another primary version if accessible.",
  "observation": "The prose explicitly describes successor-specific backup. The printed
  expansion assigns f(n,n′)=max(f(n,n′),f(n′)+c(n,n′)); cost revision subsequently
  aggregates stored f(m,m′), increases f(m), and queues marked parents, but does not
  explicitly refresh each parent f(p,m) there. The worked figure raises A’s retained
  branch estimate from3 to5 when B rises from2 to4 with unit arc cost."}, "existing_record_ids":
  [], "group": "journal1989", "index": 0, "kind": "source_qualifications", "next_check":
  "Compare the author thesis, errata or another primary version for the explicit successor-specific
  parent-arc update; retain the distinction between source omission and a proven implementation
  failure.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json",
  "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256":
  "e1b9cac943fd14de11278c2774ea42ef8347e6a2acd436454a1e2dc268512047", "pointer": "/source_qualification_objects/0",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The positive-but-summable infinite-path
  counterexample remains a mathematical scope qualification. Independent review does
  not turn individual positive arc costs into a uniform lower bound or certify termination
  on every infinite graph.", "disposition": "existing_pending_owner", "exact_original_object":
  {"consequence": "Do not universalize the source theorem to arbitrary infinite graphs.
  Finite relevant cost contours or suitable finite-branching/positive-lower-bound
  conditions can be stated only as additional reasoning conditions, never falsely
  attributed as printed premises.", "id": "Q2", "kind": "source_theorem_scope_qualification",
  "locator": "p.202 Theorem2.7 proof; p.219 Theorem3.4 proof", "manual_counterexample":
  "Take a root with a goal edge of cost2 and an infinite alternative chain with successive
  costs1/2,1/4,1/8,...; h=0. Every chain prefix costs less than1, and each edge is
  finite and positive. Optional edges of cost2 from each chain node to a goal ensure
  finite goal-reaching continuations without changing the cheaper-prefix obstruction.
  An infinite family of prefixes stays below the root goal cost. This is a reasoning
  example, not an executed algorithm or a claim about the finite Fifteen Puzzle experiments.",
  "next_check": "Independent mathematical review and source-version clarification.",
  "observation": "The proofs state termination for infinite graphs with finite positive
  individual arc costs. Individual positivity alone does not rule out an infinite
  path of finite total cost."}, "existing_record_ids": [], "group": "journal1989",
  "index": 1, "kind": "source_qualifications", "next_check": "Seek primary-version
  clarification of termination premises; preserve the finite-contour/additional-condition
  reasoning as independent qualification rather than printed theorem text.", "origin":
  {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json",
  "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256":
  "6a124bd01e110438baedb37806329b6c299b2d245d1dabb2c66958619e90d42b", "pointer": "/source_qualification_objects/1",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The original memory counters, protected
  marked storage and expansion-before-pruning convention remain scoped to the source.
  Base records do not certify a strict allocator cap, identical MA*/MAO* units or
  zero storage at MAX=0.", "disposition": "existing_pending_owner", "exact_original_object":
  {"consequence": "Retain the author-defined memory measures and stated theorem rather
  than promising a strict allocator cap, zero-memory execution at MAX=0, or equality
  of MA*/MAO* memory units. No exact machine-memory or transient-allocation guarantee
  was verified.", "id": "Q3", "kind": "memory_accounting_scope", "locator": "p.200
  count initialized0 while root stored; pp.204,212–214,219", "next_check": "If future
  curation includes a precise implementation bound, audit root/per-successor/transient
  accounting separately.", "observation": "MA* counts generated successors starting
  at0 with root already stored; MAO* explicitly counts nodes and arcs. Expansion occurs
  before pruning and marked path/solution storage is protected."}, "existing_record_ids":
  [], "group": "journal1989", "index": 2, "kind": "source_qualifications", "next_check":
  "If a future implementation-level bound is requested, audit root, generated successors,
  arcs, stack and transient allocation separately.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json",
  "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256":
  "1e2bbf4ae5c6bb82fdac4849dfc604715e2b6d69b53377989b9386ba23ddcc18", "pointer": "/source_qualification_objects/2",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The public scan’s third-party provenance
  and missing conference/publisher original remain unchanged access boundaries. The
  accepted scan supports source reading without proving publisher-byte identity or
  conference equivalence.", "disposition": "existing_pending_owner", "exact_original_object":
  {"consequence": "No conference-to-journal equivalence or first-introduction attribution
  beyond the verified citations. The public scan remains explicitly third-party provenance.",
  "id": "Q4", "kind": "version_access", "locator": "author bibliography entry101;
  journalp.221 received/revised dates", "next_check": "Seek an author/library primary
  copy of the conference proceedings and publisher/author journal text; compare bytes/content
  rather than retroactively changing historical access receipts.", "observation":
  "1987 ELDECS original full text was not acquired; publisher journal PDF also not
  acquired, although all25 public scan pages were read."}, "existing_record_ids":
  [], "group": "journal1989", "index": 3, "kind": "source_qualifications", "next_check":
  "Seek an author/library conference copy and publisher/author journal text, compare
  content and bytes, and retain all historical failed access receipts.", "origin":
  {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/scientific-support.v2.json",
  "sha256": "a5a5c42f4b1983b8e1fdc8e9b24dff305fbcf207f9e60de1ec0b2c4093e49753"}, "original_sha256":
  "a84046c181a03fb33f5c5bd071fa2c832a9ccd4632b6adf82d8976dfcb5a9107", "pointer": "/source_qualification_objects/3",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The displayed MA* algorithm remains a tree
  procedure. The graph paragraph’s pathmax/no-reopening assertion does not settle
  transpositions, cycles or improved-path handling, and no general graph guarantee
  is inferred.", "disposition": "existing_pending_owner", "exact_original_object":
  {"assessment": "Path-local monotonicity alone is not a full general graph duplicate-handling
  or consistency proof. Preserve the exact tree procedure; leave graph transpositions,
  cycle handling, path-cost improvements and reopening behavior as an explicit unresolved
  extension question. This is a scope qualification, not a demonstrated counterexample
  or a silent algorithm repair.", "changes_to_original_source_questions": false, "id":
  "MA-GRAPH-SCOPE", "image": {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-05.jpg",
  "sha256": "3388a75a92404905eff06b5231b2bddaa9d7bf2da113d89a560ecb7873dbb703"}, "locator":
  "Printed p.201, paragraph following Algorithm MA*; public reader page5", "ocr":
  {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-05.txt",
  "sha256": "3146bf08e89c43fb2fef4034889045d1fc2159f5d5cdc6c14fc70243d361c3e0"}, "origin":
  {"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/root-bounded-scientific-reading.json",
  "sha256": "84e4cfec9200a89c080ebd39ce2b249da3be31d4aa4ea71250930a273145a935"}, "proposed_limitation":
  "The displayed MA* procedure is for trees. Its graph-extension paragraph asserts
  that pathmax removes CLOSED reopening, but a complete graph duplicate, cycle and
  improved-path update policy is not specified here; no general graph-search correctness
  guarantee is inferred from path-local monotonicity.", "source_statement_summary":
  "The displayed algorithm is for trees; subsequent prose proposes checking OPEN/CLOSED
  when extending to graphs and asserts that maintained pathmax removes the need for
  CLOSED reopening.", "status": "retained_curation_boundary_and_pending_source_question"},
  "existing_record_ids": [], "group": "journal1989", "index": 4, "kind": "source_qualifications",
  "next_check": "Inspect the original graph-extension specification or later primary
  clarification of duplicate detection, path-cost improvements and CLOSED reopening
  before any extension claim.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/source-question-continuity.json",
  "sha256": "1d0e6b4cf08506e81957cc7144602594285d197ae4fb6cbe33d7ebd14d43ee0f"}, "original_sha256":
  "776f24921046ea76465724a302379bb5609b33e7cfab1c213afab039297e1d6b", "pointer": "/added_boundary",
  "responsible_owner": {"family": "main", "index": 911}}'
- '{"added_record_ids": [], "assessment": "The missing displayed parent-root guard,
  empty-successor conventions and OPEN-empty failure return remain executable-interface
  questions. The accepted record retains those limitations and does not silently repair
  the printed procedure.", "disposition": "existing_pending_owner", "exact_original_object":
  {"assessment": "No completing guard or convention was located in the inspected notation/algorithm
  text. Prior complete source reading provides context, but this bounded fresh inspection
  does not claim a search of every cited original. Retain as a qualification of executable
  completeness, not a repaired algorithm or new positive claim.", "fresh_reading":
  {"page_images": [{"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-04.jpg",
  "sha256": "cd98b81df25308273337c650ae6e352d02aff39e97cb09370f4f983a56370149"}, {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-page-05.jpg",
  "sha256": "3388a75a92404905eff06b5231b2bddaa9d7bf2da113d89a560ecb7873dbb703"}],
  "text": [{"path": "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-01.txt",
  "sha256": "a67f14b3b6a53c358ca1ceca413eb919d6d8524f49bb7301e648015cfd5ecb1b"}, {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-02.txt",
  "sha256": "d991e96a972533c41f046edd676fed82a805ba152d299307fac8b53deeb1050a"}, {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-03.txt",
  "sha256": "706483915acbd256a3e76ddbfe4f5c0163e98df38c90b22de175a02254256eb0"}, {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-04.txt",
  "sha256": "0115471d43d51b3a6e84005ac8389c2854c15de40a2aad7f726186014267c41a"}, {"path":
  "/private/tmp/aimech-ma-mao-original-source-research-20261016/article-ocr-page-05.txt",
  "sha256": "3146bf08e89c43fb2fef4034889045d1fc2159f5d5cdc6c14fc70243d361c3e0"}],
  "text_printed_pages": [197, 198, 199, 200, 201], "visual_printed_pages": [200, 201]},
  "id": "MA-PSEUDOCODE-INTERFACES", "observations": [{"locator": "Printed201, step6(ii)(a)–(b)",
  "observation": "A removed p is assigned parentq; an increased parent bound causesq
  to be put intoZ. The display has no explicit root-stop guard before a subsequent
  parent lookup.", "scope": "This is a missing displayed interface convention, not
  proof that the author implementation dereferences a nonexistent parent."}, {"locator":
  "Printed198–200, notation, Definition2.2 and initialization/expansion/termination",
  "observation": "The source defines successor minima and tests the selected node
  for a goal, but the displayed procedure does not fully state goal/dead-end empty-successor
  initialization conventions.", "scope": "A complete implementation needs conventions;
  no convention is silently inserted or attributed to the source."}, {"locator": "Printed200,
  Select1 and Termination", "observation": "Select1 chooses a node fromOPEN; no explicit
  OPEN-empty failure return is displayed.", "scope": "Do not certify a general unsolvable-instance
  interface from the literal pseudocode."}], "original_dossier_unchanged": true, "recorded_at":
  "2026-10-16T03:19:26.504883Z", "root_origin": {"path": "/private/tmp/aimech-ma-mao-identity-mapping-proposal-20261016/root-prospective-identity-mapping-reading.json",
  "sha256": "d6cae02242bb5745889c85eb73caa45c96f0d69db1aeda4d7e438ca5a6a0f534"}, "status":
  "scope_boundary_not_proven_algorithm_failure"}, "existing_record_ids": [], "group":
  "journal1989", "index": 5, "kind": "source_qualifications", "next_check": "Locate
  author implementation, thesis or primary clarification for root stopping, goal/dead-end
  initialization and unsolvable-instance return conventions; no fabricated algorithm
  line or demonstrated-failure claim.", "origin": {"path": "/private/tmp/aimech-ma-mao-scientific-data-draft-20261016/additional-interface-boundary.json",
  "sha256": "5daf989d86b1a22a4c7126f4b4fe234bdfdc909808cda10f04e9c454b1a9f8b7"}, "original_sha256":
  "26999fec925c8358a3ed960336a98c2cb33defd3cc42fa9072153d9076f30990", "pointer": "",
  "responsible_owner": {"family": "main", "index": 911}}'
- The canonical source_durability object embeds the exact 38,592-byte JSON manifest
  as base64 and all 100 asset metadata/provenance objects for 25 third-party public-reader
  scan pages. This is not a publisher PDF or publisher-byte equivalence.
- 'Exact inherited source scopes are recursively retained under predecessor_state/projection;
  actual 359 report {"path": "/private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261016T034316Z-amortized-svgd-and-real-time-adaptive-a-star.json",
  "sha256": "5aaa5f8a608224430161ccddacc1cc2cbd7ecedba79e8cec86b52ee81ec4056d"}. No
  original 402/404/406 closure or family exhaustion is asserted.'
- 'Inherited predecessor_state: exact object SHA256 a435620b7452df3a201584e1166dfdf12137a3fa28ee81394fddb075b12a6a9b;
  original source references remain inside predecessor_state/projection/predecessor_state.'
- 'Inherited predecessor_state_sha256: exact object SHA256 2912acd1d631adda13c03fd77e8469cbf11881ef183c539dd85189345b762876;
  original source references remain inside predecessor_state/projection/predecessor_state_sha256.'
- 'Inherited pair_source_accounting: exact object SHA256 421cbcd6778c6a1e998d7e143c32f9c60ffd8132b255edf1c402017d702d50c4;
  original source references remain inside predecessor_state/projection/pair_source_accounting.'
- 'Inherited frontier_result: exact object SHA256 64027f21b60509db51861e16ead984787c10d5b6bd2bcfbd5d926a04e01bfc36;
  original source references remain inside predecessor_state/projection/frontier_result.'
- 'Actual owner-plan/frontier outcome: {"additional_source_question_count": 0, "bibliography_occurrences":
  10, "changed_main_indexes": [911], "changed_nested_indexes": [], "conference_version_questions":
  1, "historical_source_responsibilities": 2, "main": 914, "nested": 394, "new_main_rows":
  0, "new_nested_rows": 0, "retained_variant_questions": 6, "retrieval_questions":
  2, "source_qualifications": 6}'
- 'Actual source accounting digest (sorted compact JSON UTF-8): 785039b1312b403f5135840b972e08898dae00b745eb9316f9067ef30b04266f'
- 'Actual historical/current identity changes: [{"id": "AIMech:MAStar", "field": "identity_notes",
  "historical": "This specific selection, f/F bookkeeping, continuation, backup and
  pruning procedure differs from maintained MREC, SMA*, ITS, A*, IDA* and RBFS-family
  methods. An endpoint resemblance or common best-first ancestry is not an exact identity.
  Use the literal source name. No expansion such as Memory-Available A* is asserted
  from an unverified source spelling; named variants and large/zero-memory endpoints
  are not aliases. This is a source-scoped prospective draft, with a provisional local
  ID only. The observed branch358 inventory contained797 native and442 pinned AIO
  records; candidate exact/local IDs, names, aliases and scoped synonyms were mechanically
  compared with no normalized collision. Ignored/hidden-inclusive searches covered
  four roots; fourteen selected native contexts and22 full AIO nodes/133 relations
  were read with exact scope in the bound proposal. This historical snapshot does
  not substitute for eventual fresh identity and owner review.", "current": "Current
  ignored-inclusive identity review on 2026-10-16 at base 0da1b27de4ee552bc8fb16a083d0f91d2a093142
  examined1241 records,4921 identity occurrences and3760 normalized values, plus945
  exact search occurrences in215 distinct content groups across four recorded roots.
  No candidate or context normalized collision was found for the recorded probes.
  MA* is curated as displayed ordinary-tree OPEN/CLOSED search with successor lower
  bounds and F-driven pruning; it remains distinct from the other member of this pair,
  MREC, SMA*, ITS, RBFS, RTAA* and amortized SVGD. Full current neighbor and inherited
  search-context readings are explicitly attributed in the discovery report; this
  is bounded absence evidence, not global novelty. Shared current source responsibility
  is main911, which remains partial; all27 original source items and separate main7/main912
  responsibilities survive.", "root_decision": "records/AIMech:MAStar/identity_notes"},
  {"id": "AIMech:MAOStar", "field": "identity_notes", "historical": "The marked AND/OR
  solution structure, successor-specific bounds, AND/OR generation and arc/orphan
  pruning differ from the ordinary-path MA* procedure and maintained importance-sampling
  AOAS. The source’s relation to AO* is a refinement context, not an established alias.
  Use the literal source name. Do not merge MAO* with MA*, AO*, cyclic AND/OR algorithms
  or the modified cutoff variant. This is a source-scoped prospective draft, with
  a provisional local ID only. The observed branch358 inventory contained797 native
  and442 pinned AIO records; candidate exact/local IDs, names, aliases and scoped
  synonyms were mechanically compared with no normalized collision. Ignored/hidden-inclusive
  searches covered four roots; fourteen selected native contexts and22 full AIO nodes/133
  relations were read with exact scope in the bound proposal. This historical snapshot
  does not substitute for eventual fresh identity and owner review.", "current": "Current
  ignored-inclusive identity review on 2026-10-16 at base 0da1b27de4ee552bc8fb16a083d0f91d2a093142
  examined1241 records,4921 identity occurrences and3760 normalized values, plus945
  exact search occurrences in215 distinct content groups across four recorded roots.
  No candidate or context normalized collision was found for the recorded probes.
  MAO* is curated as acyclic pure-AND/OR marked partial solution-graph search with
  successor-specific backups and orphan-aware pruning; it remains distinct from the
  other member of this pair, MREC, SMA*, ITS, RBFS, RTAA* and amortized SVGD. Full
  current neighbor and inherited search-context readings are explicitly attributed
  in the discovery report; this is bounded absence evidence, not global novelty. Shared
  current source responsibility is main911, which remains partial; all27 original
  source items and separate main7/main912 responsibilities survive.", "root_decision":
  "records/AIMech:MAOStar/identity_notes"}]'
```
