# Scientific self-review of source-scoped HRSAT and TSAT

- Review: 20261015T234957Z-hrsat-tsat-and-search-pointer-restoration
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-15T23:37:14.984717Z
- Finished UTC: 2026-10-15T23:49:57.390789Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain source-scoped HRSAT and TSAT as distinct DRAFT algorithms. Ten claims and fourteen limitations preserve original-versus-implementation, specification, finite-search and empirical boundaries. The 12-target AIO union and partial 296 outcome are bounded. Two older pending search pointers repair 397/398 accounting only. Actual canonical/capture/page evidence and six checks are verified; prior corrections remain predecessor provenance, not repeated issue closure.

## Scope And Provenance

Complete explicitly selected two-record cohort in captured canonical state, plus two scoped historical-accounting repairs.

Selection: Exact AIMech:HRSAT and AIMech:TabuSearchForSAT drafts. The two historical search-pointer restorations concern accounting only.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 14e9168ee3496e914545ae5c449e3ee190f0294b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HRSAT | data/curated/HRSAT.yaml | maintained | HRSAT |
| AIMech:TabuSearchForSAT | data/curated/TabuSearchForSAT.yaml | maintained | Tabu search for SAT (TSAT) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |
| just vendored-check | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |
| uv run --locked aimech check-source | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |
| just render | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |
| just render-check | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |
| git diff --check | passed | True | AIMech:HRSAT, AIMech:TabuSearchForSAT | Actual successful command; exact output is retained. |

## Scientific And Domain Assessments

### Claim printed-gensat-search-context

evidence: supported. Targets: AIMech:HRSAT.

The source explicitly introduces HRSAT within GenSAT and supplies the random GSAT initial assignment, pre-flip test and budgets. No fully specified age initialization or terminal repair is added.

### Claim probability-controlled-candidate-set

evidence: supported. Targets: AIMech:HRSAT.

The printed select branches and Section 2 global-score rule support the two pools. The source’s separate only-when-no-improvement experiment prevents accidentally imposing a local-minimum trigger on the base composition.

### Claim literal-history-pick-composition

evidence: supported. Targets: AIMech:HRSAT.

The definition is deliberately literal and source-scoped. Deterministic pick follows select in Figure 1; the later generic random-picking prose remains unresolved rather than silently selecting an experimental implementation.

### Claim focused-moves-and-endpoints

evidence: supported. Targets: AIMech:HRSAT.

The score-decrease statement is explicit in the introduction. Endpoint behavior is hand substitution into the probability branch with identical outer/history conventions, not a convergence theorem or executed solver.

### Claim archived-hwsat-version-distinction

evidence: supported. Targets: AIMech:HRSAT.

The original paper and exact archived member independently support the contrast. The source row hashes the downloaded archive and separately identifies its inspected member. The comparison does not certify the delegated HSAT code or establish an HWSAT alias.

### Limitation 1

scope: supported. Targets: AIMech:HRSAT.

Preserve both printed composition and prose; scope appears in definition, identity and claim 3 as well as this limitation. Locator: 1995 PDF pp. 3–5 and 8

### Limitation 2

scope: supported. Targets: AIMech:HRSAT.

The static branch in hwsat.c is clause-first; the conditional hand example in research demonstrates that this distribution can differ. No observed implementation failure is claimed. Locator: UBCSAT 1.0 src/hwsat.c lines 56–77; 1995 PDF p. 3

### Limitation 3

scope: supported. Targets: AIMech:HRSAT.

No 1993 source rereading is attributed to this pass. Missing operational conventions remain explicit, and recency preference is not changed into a tabu exclusion. Locator: 1995 PDF pp. 3–5; scope of original-source reading ledger

### Limitation 4

scope: supported. Targets: AIMech:HRSAT.

This is a domain/representation qualification derived from the probability coin and need for a nonempty set. It does not assert that the authors encountered an empty candidate set. Locator: 1995 PDF pp. 1–3, CNF setting and Figure 1; UBCSAT 1.0 src/hwsat.c lines 60–67 for the clause-first representation contrast.

### Limitation 5

scope: supported. Targets: AIMech:HRSAT.

The single-unit-clause, one-flip conditional hand witness establishes the literal loop boundary. Source satisfiable-instance experiments do not provide an UNSAT certificate. Locator: 1995 PDF p. 3, Figure 1 and satisfiable-instance filtering

### Limitation 6

scope: supported. Targets: AIMech:HRSAT.

Full 1995 OCR reading includes Sections 4–7 and conclusion; no exact benchmark-table value or universal performance statement is curated. Locator: 1995 PDF pp. 4–12, parameter studies, structured problems and conclusion

### Limitation 7

scope: supported. Targets: AIMech:HRSAT.

The focused score-decrease example and selector-law distinction are hand reasoning. Generic pure-walk convergence assumptions are not supplied by deterministic oldest-picking, and p=0 is a boundary case only. Locator: 1995 PDF pp. 1–3, 5 and 12; separately attributed hand analyses

### Definition and concept granularity

identity: supported. Targets: AIMech:HRSAT.

Explicit source-scoped literal composition and ambiguity satisfy the root boundary; no universal experimental implementation is claimed.

### Historical identity and version boundaries

identity: supported. Targets: AIMech:HRSAT.

Retain the literal printed 1995 GenSAT HRSAT composition separately from ordinary HSAT and later clause-first HWSAT. The probability branch selects a pool and the source-scoped history pick follows; unresolved generic random-walk prose and experimental-executable identity remain explicit. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 296 has the current bounded disposition partially_addressed, with all prior IDs, discovery pointers and resolution objects retained.

### Bounded explicit AIO no-match

grounding: supported. Targets: AIMech:HRSAT.

The inspected AIO targets describe language models, machine-learning tasks or training, neural architectures/layers, or a stochastic network/model class. The source-scoped symbolic SAT selector does not require those mechanisms. A possible augmented-state stochastic representation and flip-age bookkeeping do not alone establish a suitable mapping. The 11 rejected targets and dated semantic scope remain explicit; current search scope requires the fresh actual collection. The actual no-match search_scope is the separately recorded current root assessment; its accepted rationale and examined-target rejections remain unchanged.

### Distinct source versions and reading scopes

evidence: supported. Targets: AIMech:HRSAT.

The primary paper supports the original scoped method; the versioned archive supports its explicitly labeled selector-comparison claim. Preserve exact member/archive hashes and all incomplete implementation, source-version and empirical boundaries. Original root research reading: {"primary_ocr_pages": [2, 3, 4, 5, 8], "primary_visual_pages": [3, 4], "author_1995_visual_pages": [3], "code": "Complete archived UBCSAT1.0 src/hwsat.c read, not delegated HSAT implementation or complete solver.", "context": "Complete research science, five proposed claims/seven limitations and hand witnesses; source ledger and identity/mapping assessments. All four distinct matching contents, five maintained definitions/mechanism statements and eleven exact AIO CLASS nodes with44 incident edges read. Whole unrelated frontier remains supporting-agent scope."}. Exact draft acceptance reading: Root read full data-only module, final inputs/support, all five claim and seven limitation assessments, eleven no-match reasons, sources, identity, source-context and time projection, and support refinement. Prior root primary reading remains as in research acceptance; agent full-source readings are not relabeled as root full-source readings. This review-DATA preparation read the accepted support and metadata but did not newly read primary pages or execute the algorithms.

### Algorithm and operational specification

scope: supported. Targets: AIMech:HRSAT.

The record denotes a source-scoped SAT-search algorithm over complete Boolean assignments, not an LLM, learned model, benchmark result or certified complete executable.

### Claim gsat-model-finding-context

evidence: supported. Targets: AIMech:TabuSearchForSAT.

The paper introduces TSAT in the GSAT complete-assignment, single-variable-flip model-finding setting, with random initial attempts and bounded flips/tries in the surrounding GSAT presentation. Figure 3 is the basic GSAT algorithm, not a fully specified TSAT pseudocode.

### Claim systematic-fifo-variable-exclusion

evidence: supported. Targets: AIMech:TabuSearchForSAT.

TSAT maintains a fixed-length chronologically ordered FIFO list of flipped variables and forbids a listed variable from being flipped again while it remains tabu. The list is updated after every flip.

### Claim no-aspiration-and-attribute-memory

evidence: supported. Targets: AIMech:TabuSearchForSAT.

The described basic TSAT uses no aspiration criterion, so a favorable score alone does not override tabu status. Its memory stores variables rather than complete forbidden truth assignments.

### Claim random-walk-branch-distinction

evidence: supported. Targets: AIMech:TabuSearchForSAT.

TSAT removes the extra RWS-GSAT random-walk branch in favor of systematic tabu restrictions. This is not a claim that its random initial assignments or every tie decision become deterministic. The text discusses basic GSAT random tie selection but does not restate a complete TSAT tie/reset specification.

### Claim versioned-gsat-tabu-selector

evidence: supported. Targets: AIMech:TabuSearchForSAT.

The inspected archived registration cites CP95. The unweighted selector filters by last-change cutoff, finds minimum cached score among admissible variables and breaks multiple best candidates uniformly. These static versioned details do not certify the 1997 experimental executable; the broader catalog naming sentence is not asserted by this claim.

### Limitation 1

scope: supported. Targets: AIMech:TabuSearchForSAT.

The 1997 presentation does not provide a complete dedicated TSAT pseudocode. Initialization/reset of tabu memory, ties, the discrete boundary of tenure and empty-admissible-set behavior need explicit operational conventions; they must not be silently filled from a later implementation. Locator: PDF pp. 2–3, GSAT setting/Figure 3 and TSAT prose.

### Limitation 2

scope: supported. Targets: AIMech:TabuSearchForSAT.

A nonnegative integer tenure and a nonempty variable universe require declared domains. T&lt;n is a simple sufficient admissibility condition for a distinct length-at-most-T FIFO; T≥n can forbid all variables. The paper states no general all-tabu fallback or aspiration escape. Locator: PDF p. 3, fixed-length variable FIFO; bounded cardinality argument in hand-analysis.json.

### Limitation 3

scope: supported. Targets: AIMech:TabuSearchForSAT.

Finite unsuccessful search is not an UNSAT certificate. Recent-variable exclusion neither proves global cycle freedom nor eventual success; the bounded two-variable cycle witness demonstrates the former limit. No generic random-walk reachability theorem is imported. Locator: PDF pp. 1–3, incomplete model finding and recency motivation; hand-analysis.json and peer cycle clarification.

### Limitation 4

scope: supported. Targets: AIMech:TabuSearchForSAT.

The best admissible flip need not improve the clause score, and a useful move can be tabu. No-aspiration TSAT differs from generic tabu configurations with aspiration, adaptive tenure or longer-term intensification/diversification. Locator: PDF p. 3, no aspiration/possibly-negative GSAT gain; PDF p. 4, constant-time circular-list access.

### Limitation 5

scope: supported. Targets: AIMech:TabuSearchForSAT.

The empirical linear formula for an optimal tabu-list length is a fit for inspected random K-SAT experiments, not a universal rule, theorem, integer rounding convention or guarantee for structured SAT. The source explicitly leaves dynamic lengths and structured examples to later work. Locator: PDF pp. 3–4, Figure 4, empirical fine-tuning and further-work discussion.

### Limitation 6

scope: supported. Targets: AIMech:TabuSearchForSAT.

Table 1 reports time/flip averages for solved instances; its solved percentages use an approximately 50% satisfiable denominator at the phase transition. The study does not establish universal speedups, complete solution rates or comparative performance outside its common C/Linux/Pentium platform and stated budgets. No empirical claim need be curated. Locator: PDF p. 4, Table 1 explanation and specified experimental setting.

### Limitation 7

scope: supported. Targets: AIMech:TabuSearchForSAT.

Later GSAT/TABU documentation, the CP95 reference and the 1997 primary paper are distinct versions. The inspected UBCSAT helper has no explicit zero-candidate branch before reading candidate index zero; infrastructure and runtime behavior were not audited, and no implementation defect or observed solver failure is asserted. WalkSAT/TABU and its null/NoNull variants remain separate residuals, as does the earlier timid TSAT acronym. Locator: PDF pp. 1,3,5, historical/source boundaries; src/gsat-tabu.c lines 34–38,75–105; retained identity comparison for timid TSAT and WalkSAT/TABU.

### Definition and concept granularity

identity: supported. Targets: AIMech:TabuSearchForSAT.

Source-scoped FIFO/no-aspiration method, without certifying unprinted implementation conventions.

### Historical identity and version boundaries

identity: supported. Targets: AIMech:TabuSearchForSAT.

Retain the 1997 fixed-FIFO, no-aspiration TSAT method separately from generic tabu configurations, HRSAT age preference, timid TSAT and clause-focused WalkSAT/TABU. Later UBCSAT unweighted selector details retain their own version and CP95 attribution. The actual captured identity notes implement the root current collection decisions; the original preview scope remains historical and is recorded in context_changes. Existing owner 296 has the current bounded disposition partially_addressed, with all prior IDs, discovery pointers and resolution objects retained.

### Bounded explicit AIO no-match

grounding: supported. Targets: AIMech:TabuSearchForSAT.

Symbolic SAT-specific search, with a fixed supplied objective and recency restrictions, is not a model or necessarily an ML training task. No mapping is forced from generic memory, score or stochastic vocabulary. The 9 rejected targets and dated semantic scope remain explicit; current search scope requires the fresh actual collection. The actual no-match search_scope is the separately recorded current root assessment; its accepted rationale and examined-target rejections remain unchanged.

### Distinct source versions and reading scopes

evidence: supported. Targets: AIMech:TabuSearchForSAT.

The primary paper supports the original scoped method; the versioned archive supports its explicitly labeled selector-comparison claim. Preserve exact member/archive hashes and all incomplete implementation, source-version and empirical boundaries. Original root research reading: "Root read all five primary text pages and page 3 visual in the preceding working context, page 1 visual now; full scientific assessment, hand analyses, source ledger, identity/mapping assessments, nine AIO node/definition/edge contexts, six neighboring definitions, six complete matched-content strings/dispositions, and the bounded supporting peer assessment. Matched occurrence provenance reconstruction and full neighboring-record reading remain attributed to the supporting researcher. Root inspected unweighted UBCSAT helper lines 1–115 without claiming a full runtime audit.". Exact draft acceptance reading: Root read the complete module, inputs, sources, identity notes, source context/time projection, and all five claim/seven limitation support assessments. The duplicated core was mechanically shown identical to the fully read module; all non-core support fields were recovered after a truncated combined display. Prior primary/code reading retains the exact research-acceptance scope. Nine no-match target reasons and source-version boundaries were inspected. This review-DATA preparation read the accepted support and metadata but did not newly read primary pages or execute the algorithms.

### Algorithm and operational specification

scope: supported. Targets: AIMech:TabuSearchForSAT.

The record denotes a source-scoped SAT-search algorithm over complete Boolean assignments, not an LLM, learned model, benchmark result or certified complete executable.

### Restore historical pending ownership: MREC, MA-star, SMA-star and iterative threshold search

ownership: supported. Targets: AIMech:HRSAT, AIMech:TabuSearchForSAT.

The exact older pending pointer is restored at current main index 911. Its candidate, URL, next-check and historical origin match the approved source projection. Fresh owner reconciliation is recorded, while the method itself remains pending inspection. This repairs 397/398 accounting only; earlier 352 restorations and LPGA corrections remain predecessor evidence.

### Restore historical pending ownership: Iterative expansion

ownership: supported. Targets: AIMech:HRSAT, AIMech:TabuSearchForSAT.

The exact older pending pointer is restored at current main index 912. Its candidate, URL, next-check and historical origin match the approved source projection. Fresh owner reconciliation is recorded, while the method itself remains pending inspection. This repairs 397/398 accounting only; earlier 352 restorations and LPGA corrections remain predecessor evidence.

### Actual records, owners, restoration, history, capture, pages and checks

provenance: supported. Targets: AIMech:HRSAT, AIMech:TabuSearchForSAT.

Both current DRAFT records equal accepted science and actual root context: ten claims, fourteen limitations, two defining papers and two versioned documentation rows sharing one archive. Five exclusive files include one CREATE history. Only 296 changed and remains partial; 298, 910 other main objects and 394 nested objects remain exact. Two older pending pointers repair 397/398 ownership accounting without accepting their methods. Current identity, 45 captured inputs, actual pages and six checks are bound. Prior 352 restoration and deferred findings remain exact; no independent approval or exhaustion is implied. Later source questions are separately retained in this review and the linked open issue; creation-stage search counts are not a full-paper exhaustion claim.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:HRSAT. Retain the literal printed 1995 GenSAT HRSAT composition separately from ordinary HSAT and later clause-first HWSAT. The probability branch selects a pool and the source-scoped history pick follows; unresolved generic random-walk prose and experimental-executable identity remain explicit.
- retain: AIMech:TabuSearchForSAT. Retain the 1997 fixed-FIFO, no-aspiration TSAT method separately from generic tabu configurations, HRSAT age preference, timid TSAT and clause-focused WalkSAT/TABU. Later UBCSAT unweighted selector details retain their own version and CP95 attribution.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| preview-hrsat | /private/tmp/aimech-hrsat-draft-preparation-20261015/native-preview.json | context_only | Actual accepted TEMP native preview; canonical correspondence remains a later event. |
| support-hrsat | /private/tmp/aimech-hrsat-draft-preparation-20261015/scientific-support.final.json | context_only | Accepted per-claim/per-limitation assessment; original reading and future-event statements retain their dates. |
| draft-acceptance-hrsat | /private/tmp/aimech-hrsat-draft-preparation-20261015/root-draft-acceptance.json | context_only | Actual exact root acceptance before TEMP native validation; this does not establish future identity clearance. |
| preview-validation-hrsat | /private/tmp/aimech-hrsat-draft-preparation-20261015/native-preview-validation.json | context_only | One passed TEMP native schema/claim-source validation after exact acceptance; no whole-collection gate implied. |
| root-research-hrsat | /private/tmp/aimech-hwsat-research-20261015/root-research-acceptance.json | context_only | Original root research reading: {"primary_ocr_pages": [2, 3, 4, 5, 8], "primary_visual_pages": [3, 4], "author_1995_visual_pages": [3], "code": "Complete archived UBCSAT1.0 src/hwsat.c read, not delegated HSAT implementation or complete solver.", "context": "Complete research science, five proposed claims/seven limitations and hand witnesses; source ledger and identity/mapping assessments. All four distinct matching contents, five maintained definitions/mechanism statements and eleven exact AIO CLASS nodes with44 incident edges read. Whole unrelated frontier remains supporting-agent scope."}. Exact draft acceptance reading: Root read full data-only module, final inputs/support, all five claim and seven limitation assessments, eleven no-match reasons, sources, identity, source-context and time projection, and support refinement. Prior root primary reading remains as in research acceptance; agent full-source readings are not relabeled as root full-source readings. This review-DATA preparation read the accepted support and metadata but did not newly read primary pages or execute the algorithms. |
| preparation-reading-hrsat | /private/tmp/aimech-hrsat-draft-preparation-20261015/reading.json | context_only | Original preparation reading; not a new354 primary-page assessment. |
| historical-identity-hrsat | /private/tmp/aimech-hwsat-research-20261015/identity-assessment.json | context_only | Dated783/442 ignored/hidden-inclusive identity assessment, not current354 clearance. |
| src-gent-walsh1995 | /private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf | supports | Thirteen-page archival author-layout version of the 1995 AISB paper in Hybrid Problems, Hybrid Solutions, pp. 73–85. Locators use physical PDF pages. The native text has malformed glyphs; all pages were read by OCR and defining pages were checked visually. The original printed select/pick composition and generic random-walk prose are kept distinct; no experimental executable is certified. Direct primary support for the source-scoped method. |
| src-ubcsat1-hwsat | /private/tmp/aimech-hwsat-research-20261015/ubcsat-1-0-0.tar.gz | supports | Official project-linked version 1.0.0 archive. The SHA-256 identifies the complete downloaded archive; inspected member src/hwsat.c has SHA-256 68eb445492935e76943c3429c9071c967087dba482030bbed9b6dbd61d6d89ec. The unweighted PickHWSat branch at lines 56–77 is read statically for its clause-first sampling. No build, execution or certification of the delegated HSAT helper, full solver or later releases is implied. Direct support for this archived selector comparison only; not original-method/executable equivalence. |
| preview-tsat | /private/tmp/aimech-tsat-draft-preparation-20261015/native-preview.json | context_only | Actual accepted TEMP native preview; canonical correspondence remains a later event. |
| support-tsat | /private/tmp/aimech-tsat-draft-preparation-20261015/scientific-support.json | context_only | Accepted per-claim/per-limitation assessment; original reading and future-event statements retain their dates. |
| draft-acceptance-tsat | /private/tmp/aimech-tsat-draft-preparation-20261015/root-draft-acceptance.json | context_only | Actual exact root acceptance before TEMP native validation; this does not establish future identity clearance. |
| preview-validation-tsat | /private/tmp/aimech-tsat-draft-preparation-20261015/native-preview-validation.json | context_only | One passed TEMP native schema/claim-source validation after exact acceptance; no whole-collection gate implied. |
| root-research-tsat | /private/tmp/aimech-gsat-tabu-research-20261015/root-research-acceptance.json | context_only | Original root research reading: "Root read all five primary text pages and page 3 visual in the preceding working context, page 1 visual now; full scientific assessment, hand analyses, source ledger, identity/mapping assessments, nine AIO node/definition/edge contexts, six neighboring definitions, six complete matched-content strings/dispositions, and the bounded supporting peer assessment. Matched occurrence provenance reconstruction and full neighboring-record reading remain attributed to the supporting researcher. Root inspected unweighted UBCSAT helper lines 1–115 without claiming a full runtime audit.". Exact draft acceptance reading: Root read the complete module, inputs, sources, identity notes, source context/time projection, and all five claim/seven limitation support assessments. The duplicated core was mechanically shown identical to the fully read module; all non-core support fields were recovered after a truncated combined display. Prior primary/code reading retains the exact research-acceptance scope. Nine no-match target reasons and source-version boundaries were inspected. This review-DATA preparation read the accepted support and metadata but did not newly read primary pages or execute the algorithms. |
| preparation-reading-tsat | /private/tmp/aimech-tsat-draft-preparation-20261015/reading.json | context_only | Original preparation reading; not a new354 primary-page assessment. |
| historical-identity-tsat | /private/tmp/aimech-gsat-tabu-research-20261015/identity-assessment.json | context_only | Dated783/442 ignored/hidden-inclusive identity assessment, not current354 clearance. |
| src-mazure1997 | /private/tmp/aimech-gsat-tabu-research-20261015/mazure1997.pdf | supports | Five-page publisher scan of AAAI-97 proceedings pp. 281–285. PDF locators are physical pages; Figure 3 is explicitly basic GSAT. The PDF creation/modification timestamps postdate publication and do not identify its publication date. All five native pages and visuals 1, 3 and 4 were read for this source-scoped assessment. Direct primary support for the source-scoped method. |
| src-ubcsat1-gsat-tabu | /private/tmp/aimech-hwsat-research-20261015/ubcsat-1-0-0.tar.gz | supports | Official project-linked version 1.0.0 archive. The SHA-256 identifies the complete download; inspected member src/gsat-tabu.c has SHA-256 6195d250d9725a6e90210afb6f070edbc94cdad8d6a03b70623756bdf5fbca37. The unweighted registration and selector at lines 30–106 were inspected statically. Its attribution is CP95, and its complete runtime/initialization machinery was not certified as the 1997 experimental executable. Direct support for this archived selector comparison only; not original-method/executable equivalence. |
| historical_restoration_proposal | /private/tmp/aimech-cohort352-context350-699-20261015/proposed-issues/ownership-proposal.json | context_only | Conditional accounting proposal only; no method acceptance. |
| issue_posting | /private/tmp/aimech-cohort352-historical-review-issue-posting.json | context_only | Actual397/398 posting only, not closure. |
| predecessor_narrative_findings | /private/tmp/aimech-cohort352-review-narrative-successor-20261015/findings.json | context_only | Retained352 review-only prose findings; not defects in this pair or claims of later resolution. |
| predecessor_narrative_successor | /private/tmp/aimech-cohort352-review-narrative-successor-20261015/handoff.json | context_only | Retained352 review DATA corrections, not new354 science. |
| predecessor_narrative_issue399 | /private/tmp/aimech-cohort352-review-narrative-issue-posting.json | context_only | Actual posting of issue399 for the two352 review-only source-fidelity corrections. This is predecessor provenance, not a354 defect or closure request. |
| predecessor_corrected_review_generator | /private/tmp/aimech-cohort352-prepare-review-corrected.py | context_only | Corrected352 review generator code binds the corrected LPGA narrative DATA and issue399 provenance. This file was inspected as code, not invoked by354 preparation; no future save or merge result is inferred. |
| actual-write | /private/tmp/aimech-hrsat-tsat-cohort354-write.json | context_only | Actual exclusive creation receipt: two records, report pair and one CREATE history. |
| captured-inputs | /private/tmp/aimech-cohort354-capture.json | context_only | Actual canonical inspection; every current input hash and maintained target was checked. |
| postcapture-reading | /private/tmp/aimech-cohort354-root-postcapture-reading.json | context_only | Historical root reading receipt, recorded 2026-10-15T23:41:07.351585Z: Root read both complete actual canonical YAML records after capture:10claims14limitations4source rows, all20individual no-match rejection rows. Read complete report Markdown and CREATE history, current report metadata/counts/limitations, complete owner296/298/909–912 and exact current restoration object. Current decision object was authored/read in full; inherited397/398 findings and402original objects were read this turn and verified exact in current mirrors. Other910main/394nested objects and1228prior record preservation are mechanical comparisons, not fresh semantic readings of every source. Fresh GenSAT source-followup questions are separately retained for issue/review linkage; this receipt does not declare global source accounting clean. Root read actual scientific and governance assessments and the24-row supporting scientific matrix, recovering its truncated middle as complete one-row prose. All primary source reading is attributed to the research and supporting scientist receipts. Issue404 independently retains6later source questions; its pending status is explicit and must survive the canonical review. Gates are still running at this reading time. Any future-event wording belongs to that earlier receipt; the later six check logs establish completion before this review was generated, while canonical save remains subsequent. |
| governance-assessment | /private/tmp/aimech-cohort354-governance-audit-20261015/assessment.json | context_only | Actual byte preservation, owner/frontier, history and parsed-page audit; no independent approval. |
| rendered-pages | /private/tmp/aimech-cohort354-governance-audit-20261015/rendered-pages.json | context_only | Actual generated page paths and bytes, with parsed-content correspondence; no browser/layout inspection. |
| actual-scientific-assessment | /private/tmp/aimech-cohort354-actual-scientific-audit-20261015/assessment.json | context_only | Same-author actual-record adversarial assessment with separately attributed primary reading. |
| current-identity-collection | /private/tmp/aimech-cohort354-identity-20261015/collection.json | context_only | Current four-root ignored- and hidden-inclusive identity collection; mechanical coverage is distinct from attributed semantic reading. |
| current-context-assessment | /private/tmp/aimech-cohort354-identity-20261015/collection-assessment.json | context_only | Actual supporting interpretation of retained matched contexts; root and supporting scopes remain separate. |
| root-decisions | /private/tmp/aimech-cohort354-identity-20261015/root-decisions.json | context_only | Actual root identity, partial owner 296 and two historical pending-pointer restoration decisions; owner 298 and all other old objects remain unchanged. |
| inherited-issue402-triage | /private/tmp/aimech-cohort353-identity-20261015/root-decisions.json | context_only | Exact actual353 deferred_bibliographic_triage: four historical source questions, two original reading objects and posting/assessment references; separately preserved from397/398 accounting, without new concept or closure claims. |
| scientific-support | /private/tmp/aimech-cohort354-review-helper-preparation-20261015/scientific-support.v3.prepared.json | context_only | Exact accepted claim and limitation support; historical and later source/math scopes remain separate. |
| discovery-report | /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.json | context_only | Current records and owner mirrors; prior restoration/deferred findings remain exact and two historical pending pointers are appended without method acceptance. |
| creation-history | /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/hrsat-tsat-and-restored-search-pointers/2026-10-15T233612Z-codex-fecb18.yaml | context_only | Actual CREATE report history covers two new records and the report; no old report or existing restoration row is edited. |
| record-hrsat | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/HRSAT.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| record-tsat | /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/TabuSearchForSAT.yaml | context_only | Complete current DRAFT record equals accepted science and actual root identity decisions. |
| check-gate | /private/tmp/aimech-cohort354-check-gate.json | context_only | Actual required command completed successfully before this review generation. |
| check-vendor | /private/tmp/aimech-cohort354-check-vendor.json | context_only | Actual required command completed successfully before this review generation. |
| check-check-source | /private/tmp/aimech-cohort354-check-check-source.json | context_only | Actual required command completed successfully before this review generation. |
| check-render | /private/tmp/aimech-cohort354-check-render.json | context_only | Actual required command completed successfully before this review generation. |
| check-render-check | /private/tmp/aimech-cohort354-check-render-check.json | context_only | Actual required command completed successfully before this review generation. |
| check-diff | /private/tmp/aimech-cohort354-check-diff.json | context_only | Actual required command completed successfully before this review generation. |
| later-source-followup-decision | /private/tmp/aimech-cohort354-source-residual-probe-20261015/root-followup-acceptance.json | context_only | Root decision retaining six later source questions as pending under https://github.com/CultureBotAI/AIMech/issues/404; no new concept, source-family exhaustion or candidate science defect asserted. |
| later-source-followup-ledger | /private/tmp/aimech-cohort354-source-residual-probe-20261015/followup-ledger.json | context_only | Five named GenSAT forms plus one restricted-walk policy question, with exact source locators and possible broader owners. |
| later-source-followup-posting | /private/tmp/aimech-cohort354-source-residual-probe-20261015/posting.json | context_only | Actual issue creation and open-state observation at posting time; no future issue-state assertion. |

## Limits And Additional Notes

- Historical research, root and supporting readings remain separately attributed. Review-DATA preparation added no fresh primary-page reading or algorithm execution.
- HRSAT denotes the literal printed 1995 select/pick composition. Generic random-walk prose remains an ambiguity; the later clause-first HWSAT implementation is not asserted as an exact alias or original executable.
- TSAT denotes the 1997 fixed-FIFO, no-aspiration method. Figure 3 is basic GSAT, and unprinted tie/reset/empty-set conventions are not filled from later code.
- Finite unsuccessful runs are not UNSAT certificates. History preference and finite tabu exclusion do not establish universal convergence, cycle freedom or performance.
- Two primary papers and two documentation rows represent three artifacts. The shared archive supports specific versioned selector comparisons, not certification of either original experiment or complete solver infrastructure.
- Both exact draft acceptances preceded the retained one-time TEMP native validations. Later actual canonical and whole-collection checks remain separately required.
- The two pending-pointer restorations repair accounting for 397/398 only. Prior 352 restorations, LPGA corrections and all old report/review bytes remain predecessor evidence; no old method acceptance or issue closure is repeated.
- Historical 783/442 identity evidence remains dated. Current root decisions supply actual identity/no-match scopes. Owner 296 remains partial and 298 unchanged. The restored historical methods remain pending inspection.
- Actual five creation outputs, one CREATE history, 6 generated pages and 45 capture inputs are bound through separate receipts. Six required checks passed; failed attempts remain explicit. Parsed HTML is not browser/layout inspection. Canonical save/check and publication remain subsequent.
- Later full-paper source review identified six pending followup questions retained individually in the notes and issue https://github.com/CultureBotAI/AIMech/issues/404. The creation-stage no-new-lead assertion was limited to its earlier query matches; the source family is not exhausted. No existing frontier owner assignment or method acceptance is inferred for these questions.
- Historical root reading receipt, recorded 2026-10-15T23:41:07.351585Z: Root read both complete actual canonical YAML records after capture:10claims14limitations4source rows, all20individual no-match rejection rows. Read complete report Markdown and CREATE history, current report metadata/counts/limitations, complete owner296/298/909–912 and exact current restoration object. Current decision object was authored/read in full; inherited397/398 findings and402original objects were read this turn and verified exact in current mirrors. Other910main/394nested objects and1228prior record preservation are mechanical comparisons, not fresh semantic readings of every source. Fresh GenSAT source-followup questions are separately retained for issue/review linkage; this receipt does not declare global source accounting clean. Root read actual scientific and governance assessments and the24-row supporting scientific matrix, recovering its truncated middle as complete one-row prose. All primary source reading is attributed to the research and supporting scientist receipts. Issue404 independently retains6later source questions; its pending status is explicit and must survive the canonical review. Gates are still running at this reading time. Later command logs establish check completion; save remains subsequent.
- Four original roots included ignored and hidden files; all1329distinct match contents/23381occurrences covered by attributed partitions, with full current1228identity inventory mechanical comparisons and18 contextual fields across10neighborprojections. Later six source questions use separate four-root ignored-inclusive lexical no-match evidence, not global semantic absence.
- The two defining primary papers, Gent/Walsh1995 and Mazure et al.1997, are kept distinct from the shared UBCSAT1.0.0 archive and later2004 catalog lineage. The printed HRSAT pool/history rule is not silently equated to HWSAT clause-first uniform choice;1997 TSAT does not consume earlier timid TSAT, nor every tabu SAT variant. Currentowner296 remains partial for WalkSAT/TABU, G2WSAT, adaptive Novelty, SAPS, PAWS, DDFW, RGSAT, SAMD and variable weighting, including implementation discrepancies. Existingowner301 retains the GWSAT sampling-version question;289 retains Gu;297 retains the preference-graph residual;298 retains GenSAT variants. No new unowned lead was established in these bounded matches. Historical MREC/MA*/SMA*/iterative-threshold and Russell iterative-expansion pointers are restored pending as397/398 accounting repairs, without method acceptance. Exact inherited402 four-item bibliography triage and both original reading objects remain frozen and open; current TEMP source research is separate.
- Both retained native validations occurred after their exact draft acceptance; direct support and acceptance references remain unchanged.
- Two primary papers support the original scoped methods. The documentation rows directly support only the labeled archived selector comparisons; one shared archive is not two distinct artifacts or original executable certification.
- Only 397/398 accounting is repaired here. Previous 392/393 restorations, LPGA record and review-narrative corrections, including issue399, remain immutable predecessor provenance; no old closure is repeated.
- Exact issue402 triage from actual353 remains separately preserved in the current report and generation receipt; no remote issue-state observation or closure is asserted. Its four bibliography questions are not established new concepts.
- Additional source-followup registry, recorded after the creation-stage identity decision: https://github.com/CultureBotAI/AIMech/issues/404. Five named forms and one trigger-policy question from Gent and Walsh (1995) remain pending source identity and owner reconciliation. These are six research questions, not six established concepts or defects in the two records. The source PDF is https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf (SHA-256 eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5). The creation receipt and its no-new-lead count retain their earlier bounded query scope; this saved review separately preserves the later full-paper findings. No source-family exhaustion or remote issue closure is asserted.
- H354-S1 — CRSAT source-defined cautious walk variant. Status: pending source identity and owner reconciliation. Physical PDF pages 3, 4, 5. Reconcile the cautious candidate rule and probability-controlled focused branch with original CSAT and other maintained SAT selectors; preserve select/pick ambiguity rather than assume a new distinct identity. Possible existing owners: 296, 298; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.
- H354-S2 — TRSAT source-defined timid walk variant. Status: pending source identity and owner reconciliation. Physical PDF pages 3, 4, 5. Reconcile the timid candidate rule and focused branch with original timid TSAT; do not confuse it with1997 tabu TSAT or assume the abbreviation proves identity. Possible existing owners: 296, 298; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.
- H354-S3 — DRSAT source-defined deterministic fair-pick walk variant. Status: pending source identity and owner reconciliation. Physical PDF pages 3, 4, 5. Inspect the deterministic fair picker and its composition with the focused branch against original DSAT; establish operational convention and identity before any addition. Possible existing owners: 296, 298; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.
- H354-S4 — CHRSAT cautious history-pick walk variant. Status: pending source identity and owner reconciliation. Physical PDF pages 8. Reconcile cautious hill-climbing plus the HRSAT picking method and the CHSAT no-walk comparison. Determine whether this is a separate concept, scoped variant or existing-owner sublead. Possible existing owners: 296, 298; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.
- H354-S5 — JumpSAT multiple-clause jump variant. Status: pending source identity and owner reconciliation. Physical PDF pages 8, 9. Inspect the one-variable-from-each-unsatisfied-clause jump and its selection/update semantics, including overlapping variables and the unrestricted versus improvement-gated versions; do not infer a full executable or universal success. Possible existing owners: 296, 298, 270; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.
- H354-S6 — Restricted-walk trigger policy in CHRSAT and JumpSAT. Status: pending source identity and owner reconciliation. Physical PDF pages 8, 9. Retain the explicit policy difference between allowing focused moves on every step and allowing them only without an improving move. Determine whether this is an internal variant dimension or a separately owned identity; it is not a sixth named algorithm. Possible existing owners: 296, 298; assignment is not yet established. This question remains in the discovery backlog even if no new record is ultimately needed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T234957Z-hrsat-tsat-and-search-pointer-restoration
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of source-scoped HRSAT and TSAT
started_at: '2026-10-15T23:37:14.984717Z'
finished_at: '2026-10-15T23:49:57.390789Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author self-review with separately attributed primary research,
    root reading and bounded supporting reasoning. Preparing this scaffold is not
    an independent scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain source-scoped HRSAT and TSAT as distinct DRAFT algorithms. Ten claims
  and fourteen limitations preserve original-versus-implementation, specification,
  finite-search and empirical boundaries. The 12-target AIO union and partial 296
  outcome are bounded. Two older pending search pointers repair 397/398 accounting
  only. Actual canonical/capture/page evidence and six checks are verified; prior
  corrections remain predecessor provenance, not repeated issue closure.
source:
  git_revision: 14e9168ee3496e914545ae5c449e3ee190f0294b
  state: working_tree
  inputs:
  - path: .claude/skills/review-category/SKILL.md
    sha256: 553c3870c1dfc127f90f196b7b212b644706d4c26e2a578ab615ccce588070d7
    role: context
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/HopfieldNetwork.yaml
    sha256: 042815574abb3502427a76bb970ab78fd1ef684fa5f807b41c948ddb62e63822
    role: context
  - path: data/aio/LongShortTermMemory.yaml
    sha256: c78f9d7cd7fa61ec26d6964fbdd8dd17302480984df521b1a1c2b336f9768093
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MemoryAugmentedLLM.yaml
    sha256: 8727073cb355b965f54a2f0e58997f862f6b734c9143511008c26f9d31a965fd
    role: context
  - path: data/aio/MemoryCellLayer.yaml
    sha256: 290f04d7838e185381b29b22e67f8765de74242d687d23b0ffae2dad9d3f7237
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
  - path: data/curated/BULB.yaml
    sha256: daac190f8e4e5c66eb9ed6a4a32eee911fc756b8fc068b47522a34814ae6df50
    role: context
  - path: data/curated/BreadthFirstIDAStar.yaml
    sha256: 6a769cf81b4b128f652ba6b7340563a855a12e73f9a689e5f3d83d6baae0b20c
    role: context
  - path: data/curated/GSAT.yaml
    sha256: cfad196dde77b2b47bb3cbc2f1cce46bafe138025d937d744fd5404c5bcaeb80
    role: context
  - path: data/curated/GSATWithRandomWalk.yaml
    sha256: 5d63a89898da6fa4b60fd75387c72505f9390a3bba23aa423a7e2de3f6eed27b
    role: context
  - path: data/curated/HRSAT.yaml
    sha256: 823d962f64df9237f5f8eef8f557e0f642b9faeddec015540a68dd29b979a724
    role: target
  - path: data/curated/HSAT.yaml
    sha256: 9593d9a6fdebaada6f45ae32fa136bc5c7ad08ebbd546d9e2a82f0c8e2354045
    role: context
  - path: data/curated/IHSAT.yaml
    sha256: 2763ce1104880118f9e5edcade6fc49919860caad813352a7f5c7ab0a00f41ef
    role: context
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/RecursiveBestFirstSearch.yaml
    sha256: 8ec921263592df64c798eed093ffc2b454c5e1c79c915edcb154bef63dbae6ab
    role: context
  - path: data/curated/SimpleRecursiveBestFirstSearch.yaml
    sha256: ed513766e81bbf1801453eb8053bf999bc91666bcbae5bb7fd48f20bc2052c19
    role: context
  - path: data/curated/StochasticLocalSearch.yaml
    sha256: f4ae6fc7e1599ac08d77a99b2adcb54498cc41f9c184b13bf0e8c9a0297a789e
    role: context
  - path: data/curated/TabuSearch.yaml
    sha256: 6dae782f4d0c0b2a7195f471b7f73acb38fa036fb43ec15bacfa8f9a0264b844
    role: context
  - path: data/curated/TabuSearchForSAT.yaml
    sha256: 2197a5ca589fa859fff095447e12348fd496c2f1d7c5836cae1d482834deaf07
    role: target
  - path: data/curated/WalkSAT.yaml
    sha256: 7f28176fc24fe30c94bfd14a74304cae1021787abf87ebcfdbde6b19bc11fd23
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
  - path: history/reports/hrsat-tsat-and-restored-search-pointers/2026-10-15T233612Z-codex-fecb18.yaml
    sha256: d3a2a0fe4c350174f82503cf43a8eed98d8e00b83973c85c300823ce23c4517a
    role: context
  - path: justfile
    sha256: 2d9c1b68c1c80d53aa44a6b8b5e916efe8b493650ff59a3fc7479a42be37f400
    role: context
  - path: research/discovery/20261011T053332Z-foundational-search.json
    sha256: 59f36ac0138b557643ee5368a129b73ceeb064c974192812da38faaaa051ee5f
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
  description: Complete explicitly selected two-record cohort in captured canonical
    state, plus two scoped historical-accounting repairs.
  selection: Exact AIMech:HRSAT and AIMech:TabuSearchForSAT drafts. The two historical
    search-pointer restorations concern accounting only.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  exclusions:
  - target: HWSAT equivalence, original experimental executables, other UBCSAT variants
      and timid TSAT
    reason: Version distinctions and owner 296 residuals remain explicit; owner 298
      is untouched.
  - target: Original methods behind memory-bounded search and Iterative expansion
      pointers
    reason: Restoring pending ownership does not inspect or accept those methods.
  - target: Previous 392/393 restorations and LPGA record/review corrections
    reason: Predecessor evidence is preserved and not reopened or re-closed by this
      cohort.
checks:
- check_id: check-gate
  name: just check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-gate
- check_id: check-vendor
  name: just vendored-check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-vendor
- check_id: check-check-source
  name: uv run --locked aimech check-source
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: uv run --locked aimech check-source
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-source
- check_id: check-render
  name: just render
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: just render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render
- check_id: check-render-check
  name: just render-check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-render-check
- check_id: check-diff
  name: git diff --check
  status: passed
  required: true
  summary: Actual successful command; exact output is retained.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-diff
findings: []
actions: []
limitations:
- Historical research, root and supporting readings remain separately attributed.
  Review-DATA preparation added no fresh primary-page reading or algorithm execution.
- HRSAT denotes the literal printed 1995 select/pick composition. Generic random-walk
  prose remains an ambiguity; the later clause-first HWSAT implementation is not asserted
  as an exact alias or original executable.
- TSAT denotes the 1997 fixed-FIFO, no-aspiration method. Figure 3 is basic GSAT,
  and unprinted tie/reset/empty-set conventions are not filled from later code.
- Finite unsuccessful runs are not UNSAT certificates. History preference and finite
  tabu exclusion do not establish universal convergence, cycle freedom or performance.
- Two primary papers and two documentation rows represent three artifacts. The shared
  archive supports specific versioned selector comparisons, not certification of either
  original experiment or complete solver infrastructure.
- Both exact draft acceptances preceded the retained one-time TEMP native validations.
  Later actual canonical and whole-collection checks remain separately required.
- The two pending-pointer restorations repair accounting for 397/398 only. Prior 352
  restorations, LPGA corrections and all old report/review bytes remain predecessor
  evidence; no old method acceptance or issue closure is repeated.
- Historical 783/442 identity evidence remains dated. Current root decisions supply
  actual identity/no-match scopes. Owner 296 remains partial and 298 unchanged. The
  restored historical methods remain pending inspection.
- Actual five creation outputs, one CREATE history, 6 generated pages and 45 capture
  inputs are bound through separate receipts. Six required checks passed; failed attempts
  remain explicit. Parsed HTML is not browser/layout inspection. Canonical save/check
  and publication remain subsequent.
- Later full-paper source review identified six pending followup questions retained
  individually in the notes and issue https://github.com/CultureBotAI/AIMech/issues/404.
  The creation-stage no-new-lead assertion was limited to its earlier query matches;
  the source family is not exhausted. No existing frontier owner assignment or method
  acceptance is inferred for these questions.
tags:
- scientific-review
- self-review
- source-scoped
- satisfiability
- historical-frontier-accounting
notes:
- 'Historical root reading receipt, recorded 2026-10-15T23:41:07.351585Z: Root read
  both complete actual canonical YAML records after capture:10claims14limitations4source
  rows, all20individual no-match rejection rows. Read complete report Markdown and
  CREATE history, current report metadata/counts/limitations, complete owner296/298/909–912
  and exact current restoration object. Current decision object was authored/read
  in full; inherited397/398 findings and402original objects were read this turn and
  verified exact in current mirrors. Other910main/394nested objects and1228prior record
  preservation are mechanical comparisons, not fresh semantic readings of every source.
  Fresh GenSAT source-followup questions are separately retained for issue/review
  linkage; this receipt does not declare global source accounting clean. Root read
  actual scientific and governance assessments and the24-row supporting scientific
  matrix, recovering its truncated middle as complete one-row prose. All primary source
  reading is attributed to the research and supporting scientist receipts. Issue404
  independently retains6later source questions; its pending status is explicit and
  must survive the canonical review. Gates are still running at this reading time.
  Later command logs establish check completion; save remains subsequent.'
- Four original roots included ignored and hidden files; all1329distinct match contents/23381occurrences
  covered by attributed partitions, with full current1228identity inventory mechanical
  comparisons and18 contextual fields across10neighborprojections. Later six source
  questions use separate four-root ignored-inclusive lexical no-match evidence, not
  global semantic absence.
- The two defining primary papers, Gent/Walsh1995 and Mazure et al.1997, are kept
  distinct from the shared UBCSAT1.0.0 archive and later2004 catalog lineage. The
  printed HRSAT pool/history rule is not silently equated to HWSAT clause-first uniform
  choice;1997 TSAT does not consume earlier timid TSAT, nor every tabu SAT variant.
  Currentowner296 remains partial for WalkSAT/TABU, G2WSAT, adaptive Novelty, SAPS,
  PAWS, DDFW, RGSAT, SAMD and variable weighting, including implementation discrepancies.
  Existingowner301 retains the GWSAT sampling-version question;289 retains Gu;297
  retains the preference-graph residual;298 retains GenSAT variants. No new unowned
  lead was established in these bounded matches. Historical MREC/MA*/SMA*/iterative-threshold
  and Russell iterative-expansion pointers are restored pending as397/398 accounting
  repairs, without method acceptance. Exact inherited402 four-item bibliography triage
  and both original reading objects remain frozen and open; current TEMP source research
  is separate.
- Both retained native validations occurred after their exact draft acceptance; direct
  support and acceptance references remain unchanged.
- Two primary papers support the original scoped methods. The documentation rows directly
  support only the labeled archived selector comparisons; one shared archive is not
  two distinct artifacts or original executable certification.
- Only 397/398 accounting is repaired here. Previous 392/393 restorations, LPGA record
  and review-narrative corrections, including issue399, remain immutable predecessor
  provenance; no old closure is repeated.
- Exact issue402 triage from actual353 remains separately preserved in the current
  report and generation receipt; no remote issue-state observation or closure is asserted.
  Its four bibliography questions are not established new concepts.
- 'Additional source-followup registry, recorded after the creation-stage identity
  decision: https://github.com/CultureBotAI/AIMech/issues/404. Five named forms and
  one trigger-policy question from Gent and Walsh (1995) remain pending source identity
  and owner reconciliation. These are six research questions, not six established
  concepts or defects in the two records. The source PDF is https://cs.uwaterloo.ca/~dtompkin/archive/ubcsat/algorithms/GenWal95.pdf
  (SHA-256 eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5). The
  creation receipt and its no-new-lead count retain their earlier bounded query scope;
  this saved review separately preserves the later full-paper findings. No source-family
  exhaustion or remote issue closure is asserted.'
- 'H354-S1 — CRSAT source-defined cautious walk variant. Status: pending source identity
  and owner reconciliation. Physical PDF pages 3, 4, 5. Reconcile the cautious candidate
  rule and probability-controlled focused branch with original CSAT and other maintained
  SAT selectors; preserve select/pick ambiguity rather than assume a new distinct
  identity. Possible existing owners: 296, 298; assignment is not yet established.
  This question remains in the discovery backlog even if no new record is ultimately
  needed.'
- 'H354-S2 — TRSAT source-defined timid walk variant. Status: pending source identity
  and owner reconciliation. Physical PDF pages 3, 4, 5. Reconcile the timid candidate
  rule and focused branch with original timid TSAT; do not confuse it with1997 tabu
  TSAT or assume the abbreviation proves identity. Possible existing owners: 296,
  298; assignment is not yet established. This question remains in the discovery backlog
  even if no new record is ultimately needed.'
- 'H354-S3 — DRSAT source-defined deterministic fair-pick walk variant. Status: pending
  source identity and owner reconciliation. Physical PDF pages 3, 4, 5. Inspect the
  deterministic fair picker and its composition with the focused branch against original
  DSAT; establish operational convention and identity before any addition. Possible
  existing owners: 296, 298; assignment is not yet established. This question remains
  in the discovery backlog even if no new record is ultimately needed.'
- 'H354-S4 — CHRSAT cautious history-pick walk variant. Status: pending source identity
  and owner reconciliation. Physical PDF pages 8. Reconcile cautious hill-climbing
  plus the HRSAT picking method and the CHSAT no-walk comparison. Determine whether
  this is a separate concept, scoped variant or existing-owner sublead. Possible existing
  owners: 296, 298; assignment is not yet established. This question remains in the
  discovery backlog even if no new record is ultimately needed.'
- 'H354-S5 — JumpSAT multiple-clause jump variant. Status: pending source identity
  and owner reconciliation. Physical PDF pages 8, 9. Inspect the one-variable-from-each-unsatisfied-clause
  jump and its selection/update semantics, including overlapping variables and the
  unrestricted versus improvement-gated versions; do not infer a full executable or
  universal success. Possible existing owners: 296, 298, 270; assignment is not yet
  established. This question remains in the discovery backlog even if no new record
  is ultimately needed.'
- 'H354-S6 — Restricted-walk trigger policy in CHRSAT and JumpSAT. Status: pending
  source identity and owner reconciliation. Physical PDF pages 8, 9. Retain the explicit
  policy difference between allowing focused moves on every step and allowing them
  only without an improving move. Determine whether this is an internal variant dimension
  or a separately owned identity; it is not a sixth named algorithm. Possible existing
  owners: 296, 298; assignment is not yet established. This question remains in the
  discovery backlog even if no new record is ultimately needed.'
targets:
- target_id: AIMech:HRSAT
  label: HRSAT
  path: data/curated/HRSAT.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HRSAT.yaml
    role: maintained native concept record
- target_id: AIMech:TabuSearchForSAT
  label: Tabu search for SAT (TSAT)
  path: data/curated/TabuSearchForSAT.yaml
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TabuSearchForSAT.yaml
    role: maintained native concept record
evidence:
- evidence_id: preview-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hrsat-draft-preparation-20261015/native-preview.json
  snapshot_sha256: d392561f29b5fab6357b83b84ff1de86afde9a9eb04d9f169d18c3b08f4b3879
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Actual accepted TEMP native preview; canonical correspondence remains a
    later event.
- evidence_id: support-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hrsat-draft-preparation-20261015/scientific-support.final.json
  snapshot_sha256: 4889843d5e707e6fbdccd6f42b167d1d8e8a84102bb9a6f4ceb4daf998f48de5
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Accepted per-claim/per-limitation assessment; original reading and future-event
    statements retain their dates.
- evidence_id: draft-acceptance-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hrsat-draft-preparation-20261015/root-draft-acceptance.json
  snapshot_sha256: c1eb915f3189520b217b59bf3d54f8049d4d08f3a648fa456d34049666bd5f2b
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Actual exact root acceptance before TEMP native validation; this does not
    establish future identity clearance.
- evidence_id: preview-validation-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hrsat-draft-preparation-20261015/native-preview-validation.json
  snapshot_sha256: 9b9725962939583da93dcf578ca05aca06dd910c770099061389b874c4ce9c9b
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: One passed TEMP native schema/claim-source validation after exact acceptance;
    no whole-collection gate implied.
- evidence_id: root-research-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hwsat-research-20261015/root-research-acceptance.json
  snapshot_sha256: e380089d5391a0d1fd1e0edee582747bd8abc67d6acb54fdd02763027c63d860
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: 'Original root research reading: {"primary_ocr_pages": [2, 3, 4, 5, 8],
    "primary_visual_pages": [3, 4], "author_1995_visual_pages": [3], "code": "Complete
    archived UBCSAT1.0 src/hwsat.c read, not delegated HSAT implementation or complete
    solver.", "context": "Complete research science, five proposed claims/seven limitations
    and hand witnesses; source ledger and identity/mapping assessments. All four distinct
    matching contents, five maintained definitions/mechanism statements and eleven
    exact AIO CLASS nodes with44 incident edges read. Whole unrelated frontier remains
    supporting-agent scope."}. Exact draft acceptance reading: Root read full data-only
    module, final inputs/support, all five claim and seven limitation assessments,
    eleven no-match reasons, sources, identity, source-context and time projection,
    and support refinement. Prior root primary reading remains as in research acceptance;
    agent full-source readings are not relabeled as root full-source readings. This
    review-DATA preparation read the accepted support and metadata but did not newly
    read primary pages or execute the algorithms.'
- evidence_id: preparation-reading-hrsat
  kind: record_content
  reference: /private/tmp/aimech-hrsat-draft-preparation-20261015/reading.json
  snapshot_sha256: d9398e88c40be78c5626b7066d51d21fea387f255c703074032cc94753d89785
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Original preparation reading; not a new354 primary-page assessment.
- evidence_id: historical-identity-hrsat
  kind: search
  reference: /private/tmp/aimech-hwsat-research-20261015/identity-assessment.json
  snapshot_sha256: b3d4b2dac8c0d7405c96cbc753291a9227232bd904af8ce04f7d78253eaefc8a
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Dated783/442 ignored/hidden-inclusive identity assessment, not current354
    clearance.
  search_scope: Dated research snapshot of 783 native and 442 AIO identities; four
    full-checkout searches including ignored and hidden files; all four unique matching
    contents and current owner 296 context; eleven exact AIO CLASS nodes with 44 incident
    edges and five full native neighboring records. Absence is bounded to the inspected
    snapshot and semantic neighborhood.
- evidence_id: src-gent-walsh1995
  kind: primary_source
  reference: /private/tmp/aimech-hwsat-research-20261015/gent-walsh1995.pdf
  snapshot_sha256: eaa23fc5c52ed9a73646f05ed892622d3c06a22a99d049c6e572e50a039c15e5
  accessed_at: '2026-10-15T21:23:41Z'
  support: supports
  summary: Thirteen-page archival author-layout version of the 1995 AISB paper in
    Hybrid Problems, Hybrid Solutions, pp. 73–85. Locators use physical PDF pages.
    The native text has malformed glyphs; all pages were read by OCR and defining
    pages were checked visually. The original printed select/pick composition and
    generic random-walk prose are kept distinct; no experimental executable is certified.
    Direct primary support for the source-scoped method.
- evidence_id: src-ubcsat1-hwsat
  kind: primary_source
  reference: /private/tmp/aimech-hwsat-research-20261015/ubcsat-1-0-0.tar.gz
  snapshot_sha256: 62a15f14ea22246ece58de7fb430f96493da0c91af54dafbd11157a1c3ffee62
  accessed_at: '2026-10-15T21:29:18Z'
  support: supports
  summary: Official project-linked version 1.0.0 archive. The SHA-256 identifies the
    complete downloaded archive; inspected member src/hwsat.c has SHA-256 68eb445492935e76943c3429c9071c967087dba482030bbed9b6dbd61d6d89ec.
    The unweighted PickHWSat branch at lines 56–77 is read statically for its clause-first
    sampling. No build, execution or certification of the delegated HSAT helper, full
    solver or later releases is implied. Direct support for this archived selector
    comparison only; not original-method/executable equivalence.
- evidence_id: preview-tsat
  kind: record_content
  reference: /private/tmp/aimech-tsat-draft-preparation-20261015/native-preview.json
  snapshot_sha256: 6900f0c428c571bc0faf2449a8f9159ce6845bfd928835786cb573fc2eb4000d
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Actual accepted TEMP native preview; canonical correspondence remains a
    later event.
- evidence_id: support-tsat
  kind: record_content
  reference: /private/tmp/aimech-tsat-draft-preparation-20261015/scientific-support.json
  snapshot_sha256: 3d9fefa0f86072fc9d4e8082fdb981e548ffea1a1ecd4ac0535f9812b9908036
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Accepted per-claim/per-limitation assessment; original reading and future-event
    statements retain their dates.
- evidence_id: draft-acceptance-tsat
  kind: record_content
  reference: /private/tmp/aimech-tsat-draft-preparation-20261015/root-draft-acceptance.json
  snapshot_sha256: 77929ae3f73ba0677d1764dd84cf7bc480249ccaefb0684a4f91c1db71ea54ce
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Actual exact root acceptance before TEMP native validation; this does not
    establish future identity clearance.
- evidence_id: preview-validation-tsat
  kind: record_content
  reference: /private/tmp/aimech-tsat-draft-preparation-20261015/native-preview-validation.json
  snapshot_sha256: 1af26d78d2beb340279e72c95f457c9cae404774b1ab3aa20ea4052c73c810d8
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: One passed TEMP native schema/claim-source validation after exact acceptance;
    no whole-collection gate implied.
- evidence_id: root-research-tsat
  kind: record_content
  reference: /private/tmp/aimech-gsat-tabu-research-20261015/root-research-acceptance.json
  snapshot_sha256: 5f6613a83a79746d656d21f3323d235a5575219aec5474a49cacd10c6d986623
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: 'Original root research reading: "Root read all five primary text pages
    and page 3 visual in the preceding working context, page 1 visual now; full scientific
    assessment, hand analyses, source ledger, identity/mapping assessments, nine AIO
    node/definition/edge contexts, six neighboring definitions, six complete matched-content
    strings/dispositions, and the bounded supporting peer assessment. Matched occurrence
    provenance reconstruction and full neighboring-record reading remain attributed
    to the supporting researcher. Root inspected unweighted UBCSAT helper lines 1–115
    without claiming a full runtime audit.". Exact draft acceptance reading: Root
    read the complete module, inputs, sources, identity notes, source context/time
    projection, and all five claim/seven limitation support assessments. The duplicated
    core was mechanically shown identical to the fully read module; all non-core support
    fields were recovered after a truncated combined display. Prior primary/code reading
    retains the exact research-acceptance scope. Nine no-match target reasons and
    source-version boundaries were inspected. This review-DATA preparation read the
    accepted support and metadata but did not newly read primary pages or execute
    the algorithms.'
- evidence_id: preparation-reading-tsat
  kind: record_content
  reference: /private/tmp/aimech-tsat-draft-preparation-20261015/reading.json
  snapshot_sha256: a86c58b337c47b83e8de2a4ccbea846922d3f9afca5eec242fa7a067c75d0d21
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Original preparation reading; not a new354 primary-page assessment.
- evidence_id: historical-identity-tsat
  kind: search
  reference: /private/tmp/aimech-gsat-tabu-research-20261015/identity-assessment.json
  snapshot_sha256: 2fac9a908cfeeeaba5837cd00301bab1495af5813bc9bb6adcdb81ea9d31236d
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Dated783/442 ignored/hidden-inclusive identity assessment, not current354
    clearance.
  search_scope: Dated 783-native and 442-AIO research inventory; four full-checkout
    searches including ignored and hidden files; six complete matching contents and
    selected frontier context; nine exact AIO CLASS nodes with 39 incident-edge occurrences
    and six complete native neighbors. Absence is bounded to that snapshot and semantic
    neighborhood.
- evidence_id: src-mazure1997
  kind: primary_source
  reference: /private/tmp/aimech-gsat-tabu-research-20261015/mazure1997.pdf
  snapshot_sha256: d5593e3e1a1efd01bffb9bf36649d2dadd3cfddef660ff4880b8e9f96f31eb93
  accessed_at: '2026-10-15T21:45:45Z'
  support: supports
  summary: Five-page publisher scan of AAAI-97 proceedings pp. 281–285. PDF locators
    are physical pages; Figure 3 is explicitly basic GSAT. The PDF creation/modification
    timestamps postdate publication and do not identify its publication date. All
    five native pages and visuals 1, 3 and 4 were read for this source-scoped assessment.
    Direct primary support for the source-scoped method.
- evidence_id: src-ubcsat1-gsat-tabu
  kind: primary_source
  reference: /private/tmp/aimech-hwsat-research-20261015/ubcsat-1-0-0.tar.gz
  snapshot_sha256: 62a15f14ea22246ece58de7fb430f96493da0c91af54dafbd11157a1c3ffee62
  accessed_at: '2026-10-15T21:29:18Z'
  support: supports
  summary: Official project-linked version 1.0.0 archive. The SHA-256 identifies the
    complete download; inspected member src/gsat-tabu.c has SHA-256 6195d250d9725a6e90210afb6f070edbc94cdad8d6a03b70623756bdf5fbca37.
    The unweighted registration and selector at lines 30–106 were inspected statically.
    Its attribution is CP95, and its complete runtime/initialization machinery was
    not certified as the 1997 experimental executable. Direct support for this archived
    selector comparison only; not original-method/executable equivalence.
- evidence_id: historical_restoration_proposal
  kind: record_content
  reference: /private/tmp/aimech-cohort352-context350-699-20261015/proposed-issues/ownership-proposal.json
  snapshot_sha256: 95f8bd103247731dbd745dbb0e688571dd4b64151c9e3fd50fcd229a1bcb6b34
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Conditional accounting proposal only; no method acceptance.
- evidence_id: issue_posting
  kind: record_content
  reference: /private/tmp/aimech-cohort352-historical-review-issue-posting.json
  snapshot_sha256: 727a0c8b879509173c87cad98655a025deb9e9109dd8e4e29166abc29cd65224
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Actual397/398 posting only, not closure.
- evidence_id: predecessor_narrative_findings
  kind: record_content
  reference: /private/tmp/aimech-cohort352-review-narrative-successor-20261015/findings.json
  snapshot_sha256: cc974d28d74f2d1c532eb2ed7e9fed2383175e167d00885434662d00d1fe2c8b
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Retained352 review-only prose findings; not defects in this pair or claims
    of later resolution.
- evidence_id: predecessor_narrative_successor
  kind: record_content
  reference: /private/tmp/aimech-cohort352-review-narrative-successor-20261015/handoff.json
  snapshot_sha256: bacfc77419b747891924ea1929fdaef38f23d587d63657c748eb34e1e22e8b9c
  accessed_at: '2026-10-15T22:21:18.487150Z'
  support: context_only
  summary: Retained352 review DATA corrections, not new354 science.
- evidence_id: predecessor_narrative_issue399
  kind: record_content
  reference: /private/tmp/aimech-cohort352-review-narrative-issue-posting.json
  snapshot_sha256: dffa7a0c306120cfbcd572dab5fc5c1f20b81e28f2c82686587e1602851e3028
  accessed_at: '2026-10-15T22:24:26.075126Z'
  support: context_only
  summary: Actual posting of issue399 for the two352 review-only source-fidelity corrections.
    This is predecessor provenance, not a354 defect or closure request.
- evidence_id: predecessor_corrected_review_generator
  kind: record_content
  reference: /private/tmp/aimech-cohort352-prepare-review-corrected.py
  snapshot_sha256: 4c814f9c1bb8eefad9157a5d488007e08124e74437ba10e3635b484e0e4a5f40
  accessed_at: '2026-10-15T22:24:26.075126Z'
  support: context_only
  summary: Corrected352 review generator code binds the corrected LPGA narrative DATA
    and issue399 provenance. This file was inspected as code, not invoked by354 preparation;
    no future save or merge result is inferred.
- evidence_id: actual-write
  kind: record_content
  reference: /private/tmp/aimech-hrsat-tsat-cohort354-write.json
  snapshot_sha256: 5b4674e1952696b8887a64b818a64f00b21149dad10a78baa50ae76ea493e45b
  accessed_at: '2026-10-15T23:49:57.379465Z'
  support: context_only
  summary: 'Actual exclusive creation receipt: two records, report pair and one CREATE
    history.'
- evidence_id: captured-inputs
  kind: record_content
  reference: /private/tmp/aimech-cohort354-capture.json
  snapshot_sha256: 3f50ea27acf53a3341c84adf8a25498db1f01f1dfd909a2ea008fd8eef623c1b
  accessed_at: '2026-10-15T23:49:57.379504Z'
  support: context_only
  summary: Actual canonical inspection; every current input hash and maintained target
    was checked.
- evidence_id: postcapture-reading
  kind: record_content
  reference: /private/tmp/aimech-cohort354-root-postcapture-reading.json
  snapshot_sha256: 3ccebcb4235c9778c1521aaadea4eb1c6d4415bbefcb53feb57ab7fb0016d463
  accessed_at: '2026-10-15T23:49:57.379519Z'
  support: context_only
  summary: 'Historical root reading receipt, recorded 2026-10-15T23:41:07.351585Z:
    Root read both complete actual canonical YAML records after capture:10claims14limitations4source
    rows, all20individual no-match rejection rows. Read complete report Markdown and
    CREATE history, current report metadata/counts/limitations, complete owner296/298/909–912
    and exact current restoration object. Current decision object was authored/read
    in full; inherited397/398 findings and402original objects were read this turn
    and verified exact in current mirrors. Other910main/394nested objects and1228prior
    record preservation are mechanical comparisons, not fresh semantic readings of
    every source. Fresh GenSAT source-followup questions are separately retained for
    issue/review linkage; this receipt does not declare global source accounting clean.
    Root read actual scientific and governance assessments and the24-row supporting
    scientific matrix, recovering its truncated middle as complete one-row prose.
    All primary source reading is attributed to the research and supporting scientist
    receipts. Issue404 independently retains6later source questions; its pending status
    is explicit and must survive the canonical review. Gates are still running at
    this reading time. Any future-event wording belongs to that earlier receipt; the
    later six check logs establish completion before this review was generated, while
    canonical save remains subsequent.'
- evidence_id: governance-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort354-governance-audit-20261015/assessment.json
  snapshot_sha256: 01374b1cfeee9cae8efbde290498061ed550f47c1a22178632162e740798a515
  accessed_at: '2026-10-15T23:49:57.379533Z'
  support: context_only
  summary: Actual byte preservation, owner/frontier, history and parsed-page audit;
    no independent approval.
- evidence_id: rendered-pages
  kind: record_content
  reference: /private/tmp/aimech-cohort354-governance-audit-20261015/rendered-pages.json
  snapshot_sha256: 77ae75ed9ef39f708d8a5a62cff23dd062b2d81be8f70aaf0d938db1331e2760
  accessed_at: '2026-10-15T23:49:57.379546Z'
  support: context_only
  summary: Actual generated page paths and bytes, with parsed-content correspondence;
    no browser/layout inspection.
- evidence_id: actual-scientific-assessment
  kind: record_content
  reference: /private/tmp/aimech-cohort354-actual-scientific-audit-20261015/assessment.json
  snapshot_sha256: 649f3a922c491d4e019242b25445e132da0600871ffee79040b153fb2c5ff917
  accessed_at: '2026-10-15T23:49:57.379558Z'
  support: context_only
  summary: Same-author actual-record adversarial assessment with separately attributed
    primary reading.
- evidence_id: current-identity-collection
  kind: search
  reference: /private/tmp/aimech-cohort354-identity-20261015/collection.json
  snapshot_sha256: 862c0ac766d58541b6fd3a7f70332ca01db26d090fa8aa2acc60b482c30bdf53
  accessed_at: '2026-10-15T23:49:57.379665Z'
  support: context_only
  summary: Current four-root ignored- and hidden-inclusive identity collection; mechanical
    coverage is distinct from attributed semantic reading.
  search_scope: Four original roots included ignored and hidden files; all1329distinct
    match contents/23381occurrences covered by attributed partitions, with full current1228identity
    inventory mechanical comparisons and18 contextual fields across10neighborprojections.
    Later six source questions use separate four-root ignored-inclusive lexical no-match
    evidence, not global semantic absence.
- evidence_id: current-context-assessment
  kind: search
  reference: /private/tmp/aimech-cohort354-identity-20261015/collection-assessment.json
  snapshot_sha256: b8e6474046d3891b65bd5f5c1723df008fbb40f467ef5385116c550aefc72817
  accessed_at: '2026-10-15T23:49:57.379702Z'
  support: context_only
  summary: Actual supporting interpretation of retained matched contexts; root and
    supporting scopes remain separate.
  search_scope: Four original roots included ignored and hidden files; all1329distinct
    match contents/23381occurrences covered by attributed partitions, with full current1228identity
    inventory mechanical comparisons and18 contextual fields across10neighborprojections.
    Later six source questions use separate four-root ignored-inclusive lexical no-match
    evidence, not global semantic absence.
- evidence_id: root-decisions
  kind: record_content
  reference: /private/tmp/aimech-cohort354-identity-20261015/root-decisions.json
  snapshot_sha256: bb1cded9afb2b520c74de7c6fb71ada24beec8a158a5e961dcd06b06468d700d
  accessed_at: '2026-10-15T23:49:57.379715Z'
  support: context_only
  summary: Actual root identity, partial owner 296 and two historical pending-pointer
    restoration decisions; owner 298 and all other old objects remain unchanged.
- evidence_id: inherited-issue402-triage
  kind: record_content
  reference: /private/tmp/aimech-cohort353-identity-20261015/root-decisions.json
  snapshot_sha256: d8bc3a508f980fc6a541561ecd0346bfa892c64cfc91061aba06208e9ec1ff46
  accessed_at: '2026-10-15T23:49:57.380432Z'
  support: context_only
  summary: 'Exact actual353 deferred_bibliographic_triage: four historical source
    questions, two original reading objects and posting/assessment references; separately
    preserved from397/398 accounting, without new concept or closure claims.'
- evidence_id: scientific-support
  kind: record_content
  reference: /private/tmp/aimech-cohort354-review-helper-preparation-20261015/scientific-support.v3.prepared.json
  snapshot_sha256: 53f89b4ac8ae51fd855c7838f9c0b0f38168b6a25c25d3c1ee638db27722a750
  accessed_at: '2026-10-15T23:49:57.380451Z'
  support: context_only
  summary: Exact accepted claim and limitation support; historical and later source/math
    scopes remain separate.
- evidence_id: discovery-report
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/research/discovery/20261015T233554Z-hrsat-tsat-and-restored-search-pointers.json
  snapshot_sha256: cfb1da2d42702cf571b4b3594c8f408f33392a02bc7dd8b79c50a9b09adb279f
  accessed_at: '2026-10-15T23:49:57.383027Z'
  support: context_only
  summary: Current records and owner mirrors; prior restoration/deferred findings
    remain exact and two historical pending pointers are appended without method acceptance.
- evidence_id: creation-history
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/history/reports/hrsat-tsat-and-restored-search-pointers/2026-10-15T233612Z-codex-fecb18.yaml
  snapshot_sha256: d3a2a0fe4c350174f82503cf43a8eed98d8e00b83973c85c300823ce23c4517a
  accessed_at: '2026-10-15T23:49:57.383195Z'
  support: context_only
  summary: Actual CREATE report history covers two new records and the report; no
    old report or existing restoration row is edited.
- evidence_id: record-hrsat
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/HRSAT.yaml
  snapshot_sha256: 823d962f64df9237f5f8eef8f557e0f642b9faeddec015540a68dd29b979a724
  accessed_at: '2026-10-15T23:49:57.383350Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: record-tsat
  kind: record_content
  reference: /private/tmp/aimech-discovery-recovery-worktree-20261012/data/curated/TabuSearchForSAT.yaml
  snapshot_sha256: 2197a5ca589fa859fff095447e12348fd496c2f1d7c5836cae1d482834deaf07
  accessed_at: '2026-10-15T23:49:57.383532Z'
  support: context_only
  summary: Complete current DRAFT record equals accepted science and actual root identity
    decisions.
- evidence_id: check-gate
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-gate.json
  snapshot_sha256: 5bfc20bc60a6df33f4e7ede24c4bde6f6970c4221dae6157a452abf0e84afd1e
  accessed_at: '2026-10-15T23:49:22.647249Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-vendor
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-vendor.json
  snapshot_sha256: 4ec4eb6e37d12b74b2490c811c8512112a0ad6494650f3e00e4ba9d8bd60ad94
  accessed_at: '2026-10-15T23:49:26.438703Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-check-source
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-check-source.json
  snapshot_sha256: ede83a7f55292115f1ffd998d9faac62e41e570b0ec5bd3a68730c0285ec4744
  accessed_at: '2026-10-15T23:49:28.592975Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-render.json
  snapshot_sha256: 66795f573755da5cccd54bb3b15cfb1d634a1cdd3fbf96969e2b7f4226009ece
  accessed_at: '2026-10-15T23:36:57.861376Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-render-check
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-render-check.json
  snapshot_sha256: 37f7894ce65c56e1efeafe62e1e97ee56df41db8c2cb83dc1788b3ba13adca6a
  accessed_at: '2026-10-15T23:49:42.547078Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: check-diff
  kind: validation
  reference: /private/tmp/aimech-cohort354-check-diff.json
  snapshot_sha256: 8c61e90cfaef9a8d8fbc9630940d26a907f4c344e14a375b14fe1600b9721f40
  accessed_at: '2026-10-15T23:49:42.763512Z'
  support: context_only
  summary: Actual required command completed successfully before this review generation.
- evidence_id: later-source-followup-decision
  kind: record_content
  reference: /private/tmp/aimech-cohort354-source-residual-probe-20261015/root-followup-acceptance.json
  snapshot_sha256: 81c81677950a9c9e0f9477d8c35bc9bd04a9e68820ab797d31278b0429c2e626
  accessed_at: '2026-10-15T23:49:57.390742Z'
  support: context_only
  summary: Root decision retaining six later source questions as pending under https://github.com/CultureBotAI/AIMech/issues/404;
    no new concept, source-family exhaustion or candidate science defect asserted.
- evidence_id: later-source-followup-ledger
  kind: record_content
  reference: /private/tmp/aimech-cohort354-source-residual-probe-20261015/followup-ledger.json
  snapshot_sha256: 5df0bf4ee84ade54e310b5d8ce12817f7b6e46580db23f038e4ecf8380f8d55a
  accessed_at: '2026-10-15T23:49:57.390767Z'
  support: context_only
  summary: Five named GenSAT forms plus one restricted-walk policy question, with
    exact source locators and possible broader owners.
- evidence_id: later-source-followup-posting
  kind: record_content
  reference: /private/tmp/aimech-cohort354-source-residual-probe-20261015/posting.json
  snapshot_sha256: b2e666a95b8dd98e7237c04ea6a7ca7e5904054a11f0fd63a14d691b8e3ec9ba
  accessed_at: '2026-10-15T23:49:57.390778Z'
  support: context_only
  summary: Actual issue creation and open-state observation at posting time; no future
    issue-state assertion.
assessments:
- assessment_id: hrsat-claim-printed-gensat-search-context
  area: evidence
  topic: Claim printed-gensat-search-context
  outcome: supported
  summary: The source explicitly introduces HRSAT within GenSAT and supplies the random
    GSAT initial assignment, pre-flip test and budgets. No fully specified age initialization
    or terminal repair is added.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-claim-probability-controlled-candidate-set
  area: evidence
  topic: Claim probability-controlled-candidate-set
  outcome: supported
  summary: The printed select branches and Section 2 global-score rule support the
    two pools. The source’s separate only-when-no-improvement experiment prevents
    accidentally imposing a local-minimum trigger on the base composition.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-claim-literal-history-pick-composition
  area: evidence
  topic: Claim literal-history-pick-composition
  outcome: supported
  summary: The definition is deliberately literal and source-scoped. Deterministic
    pick follows select in Figure 1; the later generic random-picking prose remains
    unresolved rather than silently selecting an experimental implementation.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-claim-focused-moves-and-endpoints
  area: evidence
  topic: Claim focused-moves-and-endpoints
  outcome: supported
  summary: The score-decrease statement is explicit in the introduction. Endpoint
    behavior is hand substitution into the probability branch with identical outer/history
    conventions, not a convergence theorem or executed solver.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-claim-archived-hwsat-version-distinction
  area: evidence
  topic: Claim archived-hwsat-version-distinction
  outcome: supported
  summary: The original paper and exact archived member independently support the
    contrast. The source row hashes the downloaded archive and separately identifies
    its inspected member. The comparison does not certify the delegated HSAT code
    or establish an HWSAT alias.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-ubcsat1-hwsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: 'Preserve both printed composition and prose; scope appears in definition,
    identity and claim 3 as well as this limitation. Locator: 1995 PDF pp. 3–5 and
    8'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: 'The static branch in hwsat.c is clause-first; the conditional hand example
    in research demonstrates that this distribution can differ. No observed implementation
    failure is claimed. Locator: UBCSAT 1.0 src/hwsat.c lines 56–77; 1995 PDF p. 3'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: 'No 1993 source rereading is attributed to this pass. Missing operational
    conventions remain explicit, and recency preference is not changed into a tabu
    exclusion. Locator: 1995 PDF pp. 3–5; scope of original-source reading ledger'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: 'This is a domain/representation qualification derived from the probability
    coin and need for a nonempty set. It does not assert that the authors encountered
    an empty candidate set. Locator: 1995 PDF pp. 1–3, CNF setting and Figure 1; UBCSAT
    1.0 src/hwsat.c lines 60–67 for the clause-first representation contrast.'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: 'The single-unit-clause, one-flip conditional hand witness establishes
    the literal loop boundary. Source satisfiable-instance experiments do not provide
    an UNSAT certificate. Locator: 1995 PDF p. 3, Figure 1 and satisfiable-instance
    filtering'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: 'Full 1995 OCR reading includes Sections 4–7 and conclusion; no exact benchmark-table
    value or universal performance statement is curated. Locator: 1995 PDF pp. 4–12,
    parameter studies, structured problems and conclusion'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: 'The focused score-decrease example and selector-law distinction are hand
    reasoning. Generic pure-walk convergence assumptions are not supplied by deterministic
    oldest-picking, and p=0 is a boundary case only. Locator: 1995 PDF pp. 1–3, 5
    and 12; separately attributed hand analyses'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-definition-assessment
  area: identity
  topic: Definition and concept granularity
  outcome: supported
  summary: Explicit source-scoped literal composition and ambiguity satisfy the root
    boundary; no universal experimental implementation is claimed.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-identity-assessment
  area: identity
  topic: Historical identity and version boundaries
  outcome: supported
  summary: Retain the literal printed 1995 GenSAT HRSAT composition separately from
    ordinary HSAT and later clause-first HWSAT. The probability branch selects a pool
    and the source-scoped history pick follows; unresolved generic random-walk prose
    and experimental-executable identity remain explicit. The actual captured identity
    notes implement the root current collection decisions; the original preview scope
    remains historical and is recorded in context_changes. Existing owner 296 has
    the current bounded disposition partially_addressed, with all prior IDs, discovery
    pointers and resolution objects retained.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - historical-identity-hrsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: hrsat-mapping-assessment
  area: grounding
  topic: Bounded explicit AIO no-match
  outcome: supported
  summary: The inspected AIO targets describe language models, machine-learning tasks
    or training, neural architectures/layers, or a stochastic network/model class.
    The source-scoped symbolic SAT selector does not require those mechanisms. A possible
    augmented-state stochastic representation and flip-age bookkeeping do not alone
    establish a suitable mapping. The 11 rejected targets and dated semantic scope
    remain explicit; current search scope requires the fresh actual collection. The
    actual no-match search_scope is the separately recorded current root assessment;
    its accepted rationale and examined-target rejections remain unchanged.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - historical-identity-hrsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: hrsat-source-assessment
  area: evidence
  topic: Distinct source versions and reading scopes
  outcome: supported
  summary: 'The primary paper supports the original scoped method; the versioned archive
    supports its explicitly labeled selector-comparison claim. Preserve exact member/archive
    hashes and all incomplete implementation, source-version and empirical boundaries.
    Original root research reading: {"primary_ocr_pages": [2, 3, 4, 5, 8], "primary_visual_pages":
    [3, 4], "author_1995_visual_pages": [3], "code": "Complete archived UBCSAT1.0
    src/hwsat.c read, not delegated HSAT implementation or complete solver.", "context":
    "Complete research science, five proposed claims/seven limitations and hand witnesses;
    source ledger and identity/mapping assessments. All four distinct matching contents,
    five maintained definitions/mechanism statements and eleven exact AIO CLASS nodes
    with44 incident edges read. Whole unrelated frontier remains supporting-agent
    scope."}. Exact draft acceptance reading: Root read full data-only module, final
    inputs/support, all five claim and seven limitation assessments, eleven no-match
    reasons, sources, identity, source-context and time projection, and support refinement.
    Prior root primary reading remains as in research acceptance; agent full-source
    readings are not relabeled as root full-source readings. This review-DATA preparation
    read the accepted support and metadata but did not newly read primary pages or
    execute the algorithms.'
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: hrsat-kind-assessment
  area: scope
  topic: Algorithm and operational specification
  outcome: supported
  summary: The record denotes a source-scoped SAT-search algorithm over complete Boolean
    assignments, not an LLM, learned model, benchmark result or certified complete
    executable.
  target_ids:
  - AIMech:HRSAT
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - record-hrsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-claim-gsat-model-finding-context
  area: evidence
  topic: Claim gsat-model-finding-context
  outcome: supported
  summary: The paper introduces TSAT in the GSAT complete-assignment, single-variable-flip
    model-finding setting, with random initial attempts and bounded flips/tries in
    the surrounding GSAT presentation. Figure 3 is the basic GSAT algorithm, not a
    fully specified TSAT pseudocode.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-claim-systematic-fifo-variable-exclusion
  area: evidence
  topic: Claim systematic-fifo-variable-exclusion
  outcome: supported
  summary: TSAT maintains a fixed-length chronologically ordered FIFO list of flipped
    variables and forbids a listed variable from being flipped again while it remains
    tabu. The list is updated after every flip.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-claim-no-aspiration-and-attribute-memory
  area: evidence
  topic: Claim no-aspiration-and-attribute-memory
  outcome: supported
  summary: The described basic TSAT uses no aspiration criterion, so a favorable score
    alone does not override tabu status. Its memory stores variables rather than complete
    forbidden truth assignments.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-claim-random-walk-branch-distinction
  area: evidence
  topic: Claim random-walk-branch-distinction
  outcome: supported
  summary: TSAT removes the extra RWS-GSAT random-walk branch in favor of systematic
    tabu restrictions. This is not a claim that its random initial assignments or
    every tie decision become deterministic. The text discusses basic GSAT random
    tie selection but does not restate a complete TSAT tie/reset specification.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-claim-versioned-gsat-tabu-selector
  area: evidence
  topic: Claim versioned-gsat-tabu-selector
  outcome: supported
  summary: The inspected archived registration cites CP95. The unweighted selector
    filters by last-change cutoff, finds minimum cached score among admissible variables
    and breaks multiple best candidates uniformly. These static versioned details
    do not certify the 1997 experimental executable; the broader catalog naming sentence
    is not asserted by this claim.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-ubcsat1-gsat-tabu
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-1
  area: scope
  topic: Limitation 1
  outcome: supported
  summary: 'The 1997 presentation does not provide a complete dedicated TSAT pseudocode.
    Initialization/reset of tabu memory, ties, the discrete boundary of tenure and
    empty-admissible-set behavior need explicit operational conventions; they must
    not be silently filled from a later implementation. Locator: PDF pp. 2–3, GSAT
    setting/Figure 3 and TSAT prose.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-2
  area: scope
  topic: Limitation 2
  outcome: supported
  summary: 'A nonnegative integer tenure and a nonempty variable universe require
    declared domains. T<n is a simple sufficient admissibility condition for a distinct
    length-at-most-T FIFO; T≥n can forbid all variables. The paper states no general
    all-tabu fallback or aspiration escape. Locator: PDF p. 3, fixed-length variable
    FIFO; bounded cardinality argument in hand-analysis.json.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-3
  area: scope
  topic: Limitation 3
  outcome: supported
  summary: 'Finite unsuccessful search is not an UNSAT certificate. Recent-variable
    exclusion neither proves global cycle freedom nor eventual success; the bounded
    two-variable cycle witness demonstrates the former limit. No generic random-walk
    reachability theorem is imported. Locator: PDF pp. 1–3, incomplete model finding
    and recency motivation; hand-analysis.json and peer cycle clarification.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-4
  area: scope
  topic: Limitation 4
  outcome: supported
  summary: 'The best admissible flip need not improve the clause score, and a useful
    move can be tabu. No-aspiration TSAT differs from generic tabu configurations
    with aspiration, adaptive tenure or longer-term intensification/diversification.
    Locator: PDF p. 3, no aspiration/possibly-negative GSAT gain; PDF p. 4, constant-time
    circular-list access.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-5
  area: scope
  topic: Limitation 5
  outcome: supported
  summary: 'The empirical linear formula for an optimal tabu-list length is a fit
    for inspected random K-SAT experiments, not a universal rule, theorem, integer
    rounding convention or guarantee for structured SAT. The source explicitly leaves
    dynamic lengths and structured examples to later work. Locator: PDF pp. 3–4, Figure
    4, empirical fine-tuning and further-work discussion.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-6
  area: scope
  topic: Limitation 6
  outcome: supported
  summary: 'Table 1 reports time/flip averages for solved instances; its solved percentages
    use an approximately 50% satisfiable denominator at the phase transition. The
    study does not establish universal speedups, complete solution rates or comparative
    performance outside its common C/Linux/Pentium platform and stated budgets. No
    empirical claim need be curated. Locator: PDF p. 4, Table 1 explanation and specified
    experimental setting.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-limitation-7
  area: scope
  topic: Limitation 7
  outcome: supported
  summary: 'Later GSAT/TABU documentation, the CP95 reference and the 1997 primary
    paper are distinct versions. The inspected UBCSAT helper has no explicit zero-candidate
    branch before reading candidate index zero; infrastructure and runtime behavior
    were not audited, and no implementation defect or observed solver failure is asserted.
    WalkSAT/TABU and its null/NoNull variants remain separate residuals, as does the
    earlier timid TSAT acronym. Locator: PDF pp. 1,3,5, historical/source boundaries;
    src/gsat-tabu.c lines 34–38,75–105; retained identity comparison for timid TSAT
    and WalkSAT/TABU.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-definition-assessment
  area: identity
  topic: Definition and concept granularity
  outcome: supported
  summary: Source-scoped FIFO/no-aspiration method, without certifying unprinted implementation
    conventions.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-identity-assessment
  area: identity
  topic: Historical identity and version boundaries
  outcome: supported
  summary: Retain the 1997 fixed-FIFO, no-aspiration TSAT method separately from generic
    tabu configurations, HRSAT age preference, timid TSAT and clause-focused WalkSAT/TABU.
    Later UBCSAT unweighted selector details retain their own version and CP95 attribution.
    The actual captured identity notes implement the root current collection decisions;
    the original preview scope remains historical and is recorded in context_changes.
    Existing owner 296 has the current bounded disposition partially_addressed, with
    all prior IDs, discovery pointers and resolution objects retained.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - historical-identity-tsat
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: tsat-mapping-assessment
  area: grounding
  topic: Bounded explicit AIO no-match
  outcome: supported
  summary: Symbolic SAT-specific search, with a fixed supplied objective and recency
    restrictions, is not a model or necessarily an ML training task. No mapping is
    forced from generic memory, score or stochastic vocabulary. The 9 rejected targets
    and dated semantic scope remain explicit; current search scope requires the fresh
    actual collection. The actual no-match search_scope is the separately recorded
    current root assessment; its accepted rationale and examined-target rejections
    remain unchanged.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - historical-identity-tsat
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
  - current-identity-collection
  - current-context-assessment
  - root-decisions
- assessment_id: tsat-source-assessment
  area: evidence
  topic: Distinct source versions and reading scopes
  outcome: supported
  summary: 'The primary paper supports the original scoped method; the versioned archive
    supports its explicitly labeled selector-comparison claim. Preserve exact member/archive
    hashes and all incomplete implementation, source-version and empirical boundaries.
    Original root research reading: "Root read all five primary text pages and page
    3 visual in the preceding working context, page 1 visual now; full scientific
    assessment, hand analyses, source ledger, identity/mapping assessments, nine AIO
    node/definition/edge contexts, six neighboring definitions, six complete matched-content
    strings/dispositions, and the bounded supporting peer assessment. Matched occurrence
    provenance reconstruction and full neighboring-record reading remain attributed
    to the supporting researcher. Root inspected unweighted UBCSAT helper lines 1–115
    without claiming a full runtime audit.". Exact draft acceptance reading: Root
    read the complete module, inputs, sources, identity notes, source context/time
    projection, and all five claim/seven limitation support assessments. The duplicated
    core was mechanically shown identical to the fully read module; all non-core support
    fields were recovered after a truncated combined display. Prior primary/code reading
    retains the exact research-acceptance scope. Nine no-match target reasons and
    source-version boundaries were inspected. This review-DATA preparation read the
    accepted support and metadata but did not newly read primary pages or execute
    the algorithms.'
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: tsat-kind-assessment
  area: scope
  topic: Algorithm and operational specification
  outcome: supported
  summary: The record denotes a source-scoped SAT-search algorithm over complete Boolean
    assignments, not an LLM, learned model, benchmark result or certified complete
    executable.
  target_ids:
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - record-tsat
  - postcapture-reading
  - actual-scientific-assessment
- assessment_id: restore-memory-bounded-search
  area: ownership
  topic: 'Restore historical pending ownership: MREC, MA-star, SMA-star and iterative
    threshold search'
  outcome: supported
  summary: The exact older pending pointer is restored at current main index 911.
    Its candidate, URL, next-check and historical origin match the approved source
    projection. Fresh owner reconciliation is recorded, while the method itself remains
    pending inspection. This repairs 397/398 accounting only; earlier 352 restorations
    and LPGA corrections remain predecessor evidence.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - historical_restoration_proposal
  - issue_posting
  - root-decisions
  - discovery-report
  - governance-assessment
  - actual-scientific-assessment
- assessment_id: restore-iterative-expansion
  area: ownership
  topic: 'Restore historical pending ownership: Iterative expansion'
  outcome: supported
  summary: The exact older pending pointer is restored at current main index 912.
    Its candidate, URL, next-check and historical origin match the approved source
    projection. Fresh owner reconciliation is recorded, while the method itself remains
    pending inspection. This repairs 397/398 accounting only; earlier 352 restorations
    and LPGA corrections remain predecessor evidence.
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - historical_restoration_proposal
  - issue_posting
  - root-decisions
  - discovery-report
  - governance-assessment
  - actual-scientific-assessment
- assessment_id: actual-correspondence
  area: provenance
  topic: Actual records, owners, restoration, history, capture, pages and checks
  outcome: supported
  summary: 'Both current DRAFT records equal accepted science and actual root context:
    ten claims, fourteen limitations, two defining papers and two versioned documentation
    rows sharing one archive. Five exclusive files include one CREATE history. Only
    296 changed and remains partial; 298, 910 other main objects and 394 nested objects
    remain exact. Two older pending pointers repair 397/398 ownership accounting without
    accepting their methods. Current identity, 45 captured inputs, actual pages and
    six checks are bound. Prior 352 restoration and deferred findings remain exact;
    no independent approval or exhaustion is implied. Later source questions are separately
    retained in this review and the linked open issue; creation-stage search counts
    are not a full-paper exhaustion claim.'
  target_ids:
  - AIMech:HRSAT
  - AIMech:TabuSearchForSAT
  evidence_ids:
  - actual-write
  - captured-inputs
  - postcapture-reading
  - governance-assessment
  - rendered-pages
  - actual-scientific-assessment
  - creation-history
  - root-decisions
  - historical_restoration_proposal
  - issue_posting
  - inherited-issue402-triage
  - check-gate
  - check-vendor
  - check-check-source
  - check-render
  - check-render-check
  - check-diff
  - later-source-followup-decision
  - later-source-followup-ledger
  - later-source-followup-posting
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:HRSAT
  rationale: Retain the literal printed 1995 GenSAT HRSAT composition separately from
    ordinary HSAT and later clause-first HWSAT. The probability branch selects a pool
    and the source-scoped history pick follows; unresolved generic random-walk prose
    and experimental-executable identity remain explicit.
  evidence_ids:
  - preview-hrsat
  - support-hrsat
  - draft-acceptance-hrsat
  - preview-validation-hrsat
  - root-research-hrsat
  - preparation-reading-hrsat
  - historical-identity-hrsat
  - src-gent-walsh1995
  - src-ubcsat1-hwsat
  - root-decisions
  - current-identity-collection
- action: retain
  target_ids:
  - AIMech:TabuSearchForSAT
  rationale: Retain the 1997 fixed-FIFO, no-aspiration TSAT method separately from
    generic tabu configurations, HRSAT age preference, timid TSAT and clause-focused
    WalkSAT/TABU. Later UBCSAT unweighted selector details retain their own version
    and CP95 attribution.
  evidence_ids:
  - preview-tsat
  - support-tsat
  - draft-acceptance-tsat
  - preview-validation-tsat
  - root-research-tsat
  - preparation-reading-tsat
  - historical-identity-tsat
  - src-mazure1997
  - src-ubcsat1-gsat-tabu
  - root-decisions
  - current-identity-collection
```
