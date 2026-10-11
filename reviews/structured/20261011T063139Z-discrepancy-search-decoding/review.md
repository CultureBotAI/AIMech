# Scientific self-review of discrepancy search and beam-decoding policies

- Review: 20261011T063139Z-discrepancy-search-decoding
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T06:31:39Z
- Finished UTC: 2026-10-11T06:31:39Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five maintained identities, mechanisms and explicit AIO assessments are supported within the stated scopes. No actionable record finding remains. Source caveats and unresolved candidates are preserved without promoting DRAFT status.

## Scope And Provenance

Full review of two discrepancy-search procedures and three beam-decoding policies.

Selection: Exactly the five native IDs in the discrepancy-search-decoding discovery ledger; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 7386abd692a37826b5818c6cfb824b844c1b0969.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LimitedDiscrepancySearch | data/curated/LimitedDiscrepancySearch.yaml | maintained | Limited discrepancy search |
| AIMech:ImprovedLimitedDiscrepancySearch | data/curated/ImprovedLimitedDiscrepancySearch.yaml | maintained | Improved limited discrepancy search |
| AIMech:FCFSBeamDecoding | data/curated/FCFSBeamDecoding.yaml | maintained | First-come, first-served beam decoding |
| AIMech:PatienceControlledBeamDecoding | data/curated/PatienceControlledBeamDecoding.yaml | maintained | Patience-controlled FCFS beam decoding |
| AIMech:VanillaSequenceBeamDecoding | data/curated/VanillaSequenceBeamDecoding.yaml | maintained | Vanilla sequence beam decoding |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | Checked 146 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | Checked 30 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 30,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 54.76s<br>Checked 442 record(s); 0 failed.<br>Checked 146 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 30 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 30,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| DDS driver finite-tree illustration | passed | False | AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding | The literal driver misses LR; the curator variant finds it on this one tree. The saved trace informs candidate deferral, not certification of an author implementation. |

## Scientific And Domain Assessments

### Identity, discrepancy accounting, completed-output policy and AIO assessment

evidence: supported. Targets: AIMech:LimitedDiscrepancySearch.

The original LDS searches paths with at most k discrepancies in each pass. It differs from Korf’s improved LDS, which avoids revisiting leaves at the supplied maximum depth by allocating an exact discrepancy count there, and from depth-bounded discrepancy search, which bounds where deviations may occur. The original 1995 Figure 1 explores the nonpreferred child first when discrepancy budget remains; Korf’s 1996 presentation of original LDS uses the opposite within-pass order. The names do not establish identical visit sequences. No normalized identity match was found across the 442 AIO and 141 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads and incidental substrings such as builds in records, source text and dependencies, not existing concept records.

Completeness applies to exhaustive passes on a finite tree with a sufficient discrepancy/depth limit and adequate resources. A fixed early-pass cutoff is not a decision procedure for unsolvability. The first goal found is not generally a minimum-cost or shortest-path goal. Successor preference is a search-order heuristic, not an admissible cost bound. The curated original mechanism is binary. Counting any alternate child as one discrepancy and assigning rank-based discrepancy costs are distinct multiway extensions requiring an explicit policy. Repeated at-most-k passes revisit paths. The subsequent ILDS paper qualifies the original redundancy argument and supplies cases where discrepancy search has no advantage over ordinary DFS. The original paper references an LDS-BBS appendix that is not present in the inspected seven-page download. The bounded-backtracking hybrid is not asserted as part of this record.

### Identity, discrepancy accounting, completed-output policy and AIO assessment

evidence: supported. Targets: AIMech:ImprovedLimitedDiscrepancySearch.

ILDS is the 1996 improvement to LDS, not a generic label for any later discrepancy-search modification. Its exact-count guarantee concerns leaves at the specified maximum depth; shallower leaves and internal nodes can still be revisited. The supplied depth bound differs from a bound on the depths at which discrepancies are allowed. No normalized identity match was found across the 442 AIO and 141 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads and incidental substrings such as builds in records, source text and dependencies, not existing concept records.

A valid upper bound on maximum depth is an input. A loose bound or pruning that creates shallower leaves reduces the benefit because those leaves may be visited on several passes. Visiting each maximum-depth leaf once does not mean visiting every internal node once; repeated prefixes remain. The complete uniform-tree expansion analysis is conditional on that tree shape. It does not establish an unconditional wall-clock advantage on pruned trees or early-terminated searches. The procedure’s discrepancy priority does not guarantee that the first goal is shortest or globally minimum-cost. No universal superiority over DFS is asserted. The 1996 prose gives a depth-three original-LDS path count inconsistent with its own displayed counting formula and the original paper’s trace. No literal 19-path count is adopted.

### Identity, discrepancy accounting, completed-output policy and AIO assessment

evidence: supported. Targets: AIMech:FCFSBeamDecoding.

FCFS here names a sequence-decoding policy, not first-in-first-out queue scheduling. Completed sequences leave the active beam and remain in a separate set. This differs from the paper’s vanilla beam decoder, where finished and unfinished hypotheses compete for the same beam slots, and from score-prioritized per-length best-first beam search. The original policy is the patience-controlled family’s p=1 case. No normalized identity match was found across the 442 AIO and 141 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads and incidental substrings such as builds in records, source text and dependencies, not existing concept records.

The count-based stopping rule can discard unfinished candidates and is not a global optimality certificate or a guarantee of equality to vanilla beam decoding. The record identifies the paper’s specified procedure. Claims about particular library defaults are historical context, not assertions about current software versions. The simplified pseudocode assumes that candidate selection and completion return are defined. Exhausted candidate pools, absence of any EOS completion, ties and maximum-length handling require explicit implementation policies. The score and any length penalty affect candidate selection and comparison of completed outputs. A fixed beam width alone does not determine output quality. The paper’s favorable comparisons are task/model dependent; no numerical benchmark gain or universal generation-quality claim is curated.

### Identity, discrepancy accounting, completed-output policy and AIO assessment

evidence: supported. Targets: AIMech:PatienceControlledBeamDecoding.

This is the algorithmic stopping-policy variant introduced by Kasai and colleagues, not a standalone model, learned parameter or generic training patience rule. Setting p=1 recovers their FCFS baseline; changing p separates its finished-output threshold from its continuing-beam width. No normalized identity match was found across the 442 AIO and 141 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads and incidental substrings such as builds in records, source text and dependencies, not existing concept records.

The finite maximum length can end decoding before the completion threshold is reached. Empty finished sets and exhausted candidate pools need an implementation-specific outcome. Increasing patience can expose more completions but does not guarantee better task quality, a globally optimal sequence, or equivalence to vanilla beam search. The parameter is a stopping threshold, not a score upper bound or a proof that no unfinished hypothesis can improve the incumbent. The source evaluates specific translation and news-summarization settings. English news summarization does not establish benefits for all languages, domains or tasks. No current library default, runtime gain, numerical quality improvement or trained-model execution is claimed.

### Identity, discrepancy accounting, completed-output policy and AIO assessment

evidence: supported. Targets: AIMech:VanillaSequenceBeamDecoding.

This is the vanilla sequence-decoding policy contrasted with FCFS by Kasai and colleagues. It specializes generic breadth-first beam search by specifying EOS retention and competition for active slots. Finished outputs are not accumulated in a separate permanent set, and the procedure is not the score-prioritized per-length best-first decoder. No normalized identity match was found across the 442 AIO and 141 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads and incidental substrings such as builds in records, source text and dependencies, not existing concept records.

A completed hypothesis can later fall off the beam because it competes with unfinished candidates. Its discovery alone does not reserve an output slot. Finite beam pruning is not exact global MAP decoding. Different tie, length-score and maximum-length policies can change outputs. At the length limit, an implementation must specify what to return if no retained hypothesis is EOS-complete; the simplified figures do not provide a universal failure policy. Figure 2 in the 2024 paper omits initialization/reset of its temporary H pool. The fresh-per-layer interpretation is supported by the layer-based prose and the explicit reset in Meister et al. 2020 Algorithm 1; the record does not certify the 2024 figure as executable code. The name identifies the source-defined policy, not a claim that all libraries or all uses of beam search implement it.

### Discrepancy budgets and beam completion accounting are separate algorithm choices

scope: supported. Targets: AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding.

The records distinguish at-most discrepancy passes from exact-count-at-maximum-depth passes, and persistent completed-output sets from EOS hypotheses competing inside a beam. The patience family explicitly contains the FCFS p=1 case.

No minimum-cost first-goal claim, universal runtime improvement, global sequence-optimality guarantee or current library default is inferred. The original and later LDS traversal orders are distinguished. ILDS can repeat internal nodes and shallow leaves. A parameterized method family and its historically defined baseline overlap without being identical concepts; this boundary is stated explicitly.

### Incomplete pseudocode and inconsistent printed claims

evidence: supported. Targets: AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding.

The record scopes preserve the LDS appendix access gap, the ILDS path-count inconsistency, the vanilla temporary-pool omission and the separate DDS driver concern.

The vanilla fresh-layer interpretation has an explicit primary citation to the 2020 Algorithm 1. The DDS example is a curator transcription on one finite tree; its successful modification is not an author-approved correction or a general proof. It remains outside this five-record cohort.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:LimitedDiscrepancySearch, AIMech:ImprovedLimitedDiscrepancySearch, AIMech:FCFSBeamDecoding, AIMech:PatienceControlledBeamDecoding, AIMech:VanillaSequenceBeamDecoding. Original at-most discrepancy passes and ILDS exact-at-depth passes have different repetition behavior. The vanilla decoder keeps completed hypotheses in its competitive beam; FCFS accumulates completions separately and stops at k; controlled patience generalizes that threshold to k*p. Preserve each explicit specialization without asserting disjointness, equivalence to a task, or equivalence to every use of beam search.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T062948Z-discrepancy-search-decoding.json | supports | No normalized identity match across all 442 pinned AIO labels/scoped synonyms and 141 preceding native IDs/names/aliases. Ignored and hidden files were included in both checkout text searches. The 22 worktree hits are prior discovery leads, source references and incidental builds substrings; 139 main-checkout hits include those plus dependency substrings such as builds, rebuilds and childs. No hit establishes an existing candidate record. Short LDS was included in normalized identity checking; a separate ignored-inclusive whole-word LDS/ILDS/FCFS search of data/aio, data/curated and docs/proposals returned no hits before writes. |
| mapping | sources/aio/aio.json; Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing, GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning | supports | Two tree-search procedures retain explicit no-match assessments after six exact AIO CLASS definitions, synonyms and edges were inspected: GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning. Three sequence decoders have related_match to the exact NaturalLanguageProcessing task CLASS because natural-language generation is their central source domain. This is not an is-a or equivalence mapping. The pinned ontology and semantic label/synonym scans are unchanged from the predecessor; no upstream refresh is implied. |
| limiteddiscrepancysearch-0 | https://www.ijcai.org/Proceedings/95-1/Papers/080.pdf; Section 3 and Figure 1, printed p. 608 / PDF p. 2; Section 5.5, printed p. 611 / PDF p. 5 | supports | A backtracking tree-search strategy that repeatedly explores paths under an increasing upper limit on deviations from a successor-ordering heuristic; in the original binary formulation, taking the nonpreferred child consumes one discrepancy. Version: IJCAI 1995; official seven-page PDF, printed pp. 607–613. Actually inspected rendered PDF pages: 2. |
| limiteddiscrepancysearch-1 | https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf; Printed pp. 286–287 / PDF pp. 1–2; Figures 2–3 | supports | Korf distinguishes original at-most-k passes from an exact-count-at-maximum-depth modification, and presents a left-child-first original probe. This differs from the right-child-first positive-budget probe printed in the 1995 paper; the two presentations share a budget principle, not necessarily a visit order. Version: AAAI 1996 proceedings, printed pp. 286–291; official six-page PDF. Actually inspected rendered PDF pages: 1, 2, 3. |
| limiteddiscrepancysearch-2 | https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf; A Simpler Algorithm and Negative Result and Conclusions, printed pp. 290–291 / PDF pp. 5–6 | supports | Discrepancy search depends on the successor heuristic and search-tree structure. The 1996 study includes negative results against DFS, so the original method is not characterized by universal runtime superiority. Version: AAAI 1996 proceedings, printed pp. 286–291; official six-page PDF. Actually inspected rendered PDF pages: 1, 2, 3. |
| improvedlimiteddiscrepancysearch-0 | https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf; Improved Limited Discrepancy Search and Figure 3, printed p. 287 / PDF p. 2; Interior Node Overhead of ILDS, printed p. 288 / PDF p. 3 | supports | Korf’s discrepancy-search variant that uses a supplied maximum search depth and remaining discrepancy count to generate each path to that depth in the pass corresponding to its exact number of nonpreferred choices, avoiding the original method’s repeated maximum-depth paths. Version: AAAI 1996 proceedings, printed pp. 286–291; official six-page PDF. Actually inspected rendered PDF pages: 1, 2, 3. |
| improvedlimiteddiscrepancysearch-1 | https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf; Printed pp. 287–288 and 290–291 / PDF pp. 2–3 and 5–6 | supports | Maximum-depth paths are generated once across discrepancy passes, but shorter leaves and internal nodes can recur. The paper’s uniform-tree overhead analysis and its negative number-partitioning results are distinct from a universal performance guarantee. Version: AAAI 1996 proceedings, printed pp. 286–291; official six-page PDF. Actually inspected rendered PDF pages: 1, 2, 3. |
| fcfsbeamdecoding-0 | https://aclanthology.org/2024.lrec-main.7.pdf; Figure 1 with p=1, printed p. 77 / PDF p. 1; Section 2 and Figures 2–3, printed pp. 78–79 / PDF pp. 2–3 | supports | The sequence beam-decoding procedure described by Kasai and colleagues that stores completed hypotheses separately from the continuing beam and stops when the accumulated number of completed hypotheses reaches the beam width, returning the highest-scoring stored completion. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3. |
| fcfsbeamdecoding-1 | https://aclanthology.org/2024.lrec-main.7.pdf; Section 2 and Figures 1–3, printed pp. 77–79 / PDF pp. 1–3 | supports | Finished hypotheses accumulate outside the k-wide continuing beam in FCFS. In the contrasted vanilla procedure, completed hypotheses remain among the beam candidates and can later fall out. These are different search policies despite a shared beam width. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3. |
| patiencecontrolledbeamdecoding-0 | https://aclanthology.org/2024.lrec-main.7.pdf; Figure 1 line 13, printed p. 77 / PDF p. 1; Patience Factor for FCFS, Section 2, printed p. 79 / PDF p. 3 | supports | A generalization of first-come, first-served sequence beam decoding that retains beam width k for continuing hypotheses but uses a positive patience factor p to stop when the accumulated completed-hypothesis count reaches at least k·p. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3. |
| patiencecontrolledbeamdecoding-1 | https://aclanthology.org/2024.lrec-main.7.pdf; Section 2, Section 3.3 and Limitations, printed pp. 79–81 / PDF pp. 3–5 | supports | The paper separates stopping depth from beam breadth and reports task-dependent behavior; its limitations explicitly restrict summarization evidence to English news. More extensive search and better generated-text quality are not equivalent claims. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3. |
| vanillasequencebeamdecoding-0 | https://aclanthology.org/2024.lrec-main.7.pdf; Section 2 and Figures 2–3, printed pp. 78–79 / PDF pp. 2–3 | supports | A layer-based sequence beam decoder in which completed and unfinished hypotheses compete for the same k beam slots: finished hypotheses are carried forward unchanged, unfinished hypotheses are extended, and the top-scoring candidates form the next beam. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3. |
| vanillasequencebeamdecoding-1 | https://aclanthology.org/2020.tacl-1.51.pdf; Algorithm 1 and footnotes, printed p. 797 / PDF p. 3 | supports | The standard sequence-beam algorithm initializes an empty candidate pool for each time step, carries EOS-complete hypotheses unchanged, extends unfinished hypotheses and selects the next top-k beam. This supplies an explicit layer-pool scope for the later vanilla-policy description. Version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8. |
| dds-driver-analysis | research/validation/20261011T062948Z-dds-driver-counterexample.json; Literal driver and curator variant traces; companion script research/validation/20261011T062948Z-dds-driver-counterexample.py | context_only | The printed driver overwrites the returned depth each iteration. On this finite unbalanced binary tree, it stops after visiting LL and R and misses goal LR. Retaining the maximum depth observed across passes finds LR in this example. This supports deferral of a separate candidate, not a claim about the correctness of the five added procedures. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval; all five records remain DRAFT.
- No unconditional completeness, optimality, runtime or decoding-quality claim is transferred between different procedures.
- The vanilla pool reset is supported by a second primary algorithm, while the later abbreviated figure remains explicitly incomplete.
- The DDS illustration is a curator transcription, not an author erratum, implementation audit or general proof.
- Repeated citations to different passages in the same paper are not independent studies.
- An initial vendored-check failed because the restricted environment could not resolve the public source host. The network-enabled rerun passed; this was an access failure, not a vendored artifact mismatch.
- The two cross-paper claim citations were tightened before this saved assessment. No unresolved corrective issue remains in this review scope.
- The source pin and generated records are unchanged. These five reviewed targets do not retire unrelated historical findings or establish discovery saturation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063139Z-discrepancy-search-decoding
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of discrepancy search and beam-decoding policies
started_at: '2026-10-11T06:31:39Z'
finished_at: '2026-10-11T06:31:39Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own five records
    and source assumptions. No independent reviewer or approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five maintained identities, mechanisms and explicit AIO assessments are
  supported within the stated scopes. No actionable record finding remains. Source
  caveats and unresolved candidates are preserved without promoting DRAFT status.
source:
  git_revision: 7386abd692a37826b5818c6cfb824b844c1b0969
  state: working_tree
  inputs:
  - path: data/curated/FCFSBeamDecoding.yaml
    sha256: 1f21d30b556ee6e9165607c1f08219ce7d6823a64a855f5470102174de40e813
    role: target
  - path: data/curated/ImprovedLimitedDiscrepancySearch.yaml
    sha256: 93689aa911171cdd85f4c0e8b9517414532037295fe7e084189d51d4e174a6ad
    role: target
  - path: data/curated/LimitedDiscrepancySearch.yaml
    sha256: 144d2daed4c13fdca8e6b1251fa64c4c486354ac6d80c2c5e51b828b0cabbee1
    role: target
  - path: data/curated/PatienceControlledBeamDecoding.yaml
    sha256: f1bd32ef7d1652ad43ad3fb92539e27ed9b3261ce92b26760967dac9162775ab
    role: target
  - path: data/curated/VanillaSequenceBeamDecoding.yaml
    sha256: f10fab4f3575f098ce6c978158ec15954fe20cbda03cbe63aecea23ff23e6356
    role: target
  - path: research/discovery/20261011T062948Z-discrepancy-search-decoding.json
    sha256: 065dbee0d23af9fc95db2fd6c44cbb4ad0b27830ccb7407671eefb0ceddc040d
    role: context
  - path: research/validation/20261011T062948Z-dds-driver-counterexample.json
    sha256: 621ac3f24b866d8928cf7b7c24ee6e2bec3f2ee8aa5762a960d2fe2287c7e0fa
    role: context
  - path: research/validation/20261011T062948Z-dds-driver-counterexample.py
    sha256: 201c453e0bb30ef829665be04375e2951fc6ee8c097fd546098b9bd602621c50
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
- target_id: AIMech:LimitedDiscrepancySearch
  path: data/curated/LimitedDiscrepancySearch.yaml
  label: Limited discrepancy search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LimitedDiscrepancySearch.yaml
    role: maintained_record
- target_id: AIMech:ImprovedLimitedDiscrepancySearch
  path: data/curated/ImprovedLimitedDiscrepancySearch.yaml
  label: Improved limited discrepancy search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ImprovedLimitedDiscrepancySearch.yaml
    role: maintained_record
- target_id: AIMech:FCFSBeamDecoding
  path: data/curated/FCFSBeamDecoding.yaml
  label: First-come, first-served beam decoding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FCFSBeamDecoding.yaml
    role: maintained_record
- target_id: AIMech:PatienceControlledBeamDecoding
  path: data/curated/PatienceControlledBeamDecoding.yaml
  label: Patience-controlled FCFS beam decoding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PatienceControlledBeamDecoding.yaml
    role: maintained_record
- target_id: AIMech:VanillaSequenceBeamDecoding
  path: data/curated/VanillaSequenceBeamDecoding.yaml
  label: Vanilla sequence beam decoding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VanillaSequenceBeamDecoding.yaml
    role: maintained_record
scope:
  description: Full review of two discrepancy-search procedures and three beam-decoding
    policies.
  selection: Exactly the five native IDs in the discrepancy-search-decoding discovery
    ledger; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exclusions:
  - target: DDS, bounded-backtracking hybrids and other pending frontier groups
    reason: Their unresolved driver rules, source-access gaps or uninspected primary
      methods are retained in the discovery ledger.
  - target: Numerical benchmark replication and formal correctness certification
    reason: No author code, model or benchmark was executed. The curator driver illustration
      is limited to its stated finite tree.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
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
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
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
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 146 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
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
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 30 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 30,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 54.76s\nChecked 442 record(s); 0 failed.\n\
    Checked 146 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 30 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 30,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: curator-illustration
  name: DDS driver finite-tree illustration
  command: python3 research/validation/20261011T062948Z-dds-driver-counterexample.py
  status: passed
  required: false
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  exit_code: 0
  expected_exit_code: 0
  summary: The literal driver misses LR; the curator variant finds it on this one
    tree. The saved trace informs candidate deferral, not certification of an author
    implementation.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T062948Z-discrepancy-search-decoding.json
  accessed_at: '2026-10-11T06:31:39Z'
  support: supports
  summary: No normalized identity match across all 442 pinned AIO labels/scoped synonyms
    and 141 preceding native IDs/names/aliases. Ignored and hidden files were included
    in both checkout text searches. The 22 worktree hits are prior discovery leads,
    source references and incidental builds substrings; 139 main-checkout hits include
    those plus dependency substrings such as builds, rebuilds and childs. No hit establishes
    an existing candidate record. Short LDS was included in normalized identity checking;
    a separate ignored-inclusive whole-word LDS/ILDS/FCFS search of data/aio, data/curated
    and docs/proposals returned no hits before writes.
  search_scope: All 442 AIO labels/scoped synonyms and 141 preceding native IDs/names/aliases;
    both updated checkouts with ignored and hidden files included.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact CLASS definitions, synonyms and incident edges for NaturalLanguageProcessing,
    GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction
    and ReinforcementLearning
  accessed_at: '2026-10-11T06:31:39Z'
  support: supports
  summary: 'Two tree-search procedures retain explicit no-match assessments after
    six exact AIO CLASS definitions, synonyms and edges were inspected: GraphLanguageModel,
    ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and
    ReinforcementLearning. Three sequence decoders have related_match to the exact
    NaturalLanguageProcessing task CLASS because natural-language generation is their
    central source domain. This is not an is-a or equivalence mapping. The pinned
    ontology and semantic label/synonym scans are unchanged from the predecessor;
    no upstream refresh is implied.'
- evidence_id: limiteddiscrepancysearch-0
  kind: primary_source
  reference: https://www.ijcai.org/Proceedings/95-1/Papers/080.pdf
  locator: Section 3 and Figure 1, printed p. 608 / PDF p. 2; Section 5.5, printed
    p. 611 / PDF p. 5
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: aa484ed1115a53ab9098d3509407bc50b3951f58cea96df46c108a68350bf1db
  support: supports
  summary: 'A backtracking tree-search strategy that repeatedly explores paths under
    an increasing upper limit on deviations from a successor-ordering heuristic; in
    the original binary formulation, taking the nonpreferred child consumes one discrepancy.
    Version: IJCAI 1995; official seven-page PDF, printed pp. 607–613. Actually inspected
    rendered PDF pages: 2.'
- evidence_id: limiteddiscrepancysearch-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf
  locator: Printed pp. 286–287 / PDF pp. 1–2; Figures 2–3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 55b3305027e77ddf84ad13dd4b1114a0a1630d4c066562aa8c64d6c376ab18aa
  support: supports
  summary: 'Korf distinguishes original at-most-k passes from an exact-count-at-maximum-depth
    modification, and presents a left-child-first original probe. This differs from
    the right-child-first positive-budget probe printed in the 1995 paper; the two
    presentations share a budget principle, not necessarily a visit order. Version:
    AAAI 1996 proceedings, printed pp. 286–291; official six-page PDF. Actually inspected
    rendered PDF pages: 1, 2, 3.'
- evidence_id: limiteddiscrepancysearch-2
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf
  locator: A Simpler Algorithm and Negative Result and Conclusions, printed pp. 290–291
    / PDF pp. 5–6
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 55b3305027e77ddf84ad13dd4b1114a0a1630d4c066562aa8c64d6c376ab18aa
  support: supports
  summary: 'Discrepancy search depends on the successor heuristic and search-tree
    structure. The 1996 study includes negative results against DFS, so the original
    method is not characterized by universal runtime superiority. Version: AAAI 1996
    proceedings, printed pp. 286–291; official six-page PDF. Actually inspected rendered
    PDF pages: 1, 2, 3.'
- evidence_id: improvedlimiteddiscrepancysearch-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf
  locator: Improved Limited Discrepancy Search and Figure 3, printed p. 287 / PDF
    p. 2; Interior Node Overhead of ILDS, printed p. 288 / PDF p. 3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 55b3305027e77ddf84ad13dd4b1114a0a1630d4c066562aa8c64d6c376ab18aa
  support: supports
  summary: 'Korf’s discrepancy-search variant that uses a supplied maximum search
    depth and remaining discrepancy count to generate each path to that depth in the
    pass corresponding to its exact number of nonpreferred choices, avoiding the original
    method’s repeated maximum-depth paths. Version: AAAI 1996 proceedings, printed
    pp. 286–291; official six-page PDF. Actually inspected rendered PDF pages: 1,
    2, 3.'
- evidence_id: improvedlimiteddiscrepancysearch-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1996/AAAI96-043.pdf
  locator: Printed pp. 287–288 and 290–291 / PDF pp. 2–3 and 5–6
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 55b3305027e77ddf84ad13dd4b1114a0a1630d4c066562aa8c64d6c376ab18aa
  support: supports
  summary: 'Maximum-depth paths are generated once across discrepancy passes, but
    shorter leaves and internal nodes can recur. The paper’s uniform-tree overhead
    analysis and its negative number-partitioning results are distinct from a universal
    performance guarantee. Version: AAAI 1996 proceedings, printed pp. 286–291; official
    six-page PDF. Actually inspected rendered PDF pages: 1, 2, 3.'
- evidence_id: fcfsbeamdecoding-0
  kind: primary_source
  reference: https://aclanthology.org/2024.lrec-main.7.pdf
  locator: Figure 1 with p=1, printed p. 77 / PDF p. 1; Section 2 and Figures 2–3,
    printed pp. 78–79 / PDF pp. 2–3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 7d090ee35511ac9fdcdb52ca92cad5d2e96075635de73ada84abd042362a9fec
  support: supports
  summary: 'The sequence beam-decoding procedure described by Kasai and colleagues
    that stores completed hypotheses separately from the continuing beam and stops
    when the accumulated number of completed hypotheses reaches the beam width, returning
    the highest-scoring stored completion. Version: LREC-COLING 2024, 77–90; published
    ACL Anthology PDF (distinct from the 2022 arXiv version). Actually inspected rendered
    PDF pages: 1, 2, 3.'
- evidence_id: fcfsbeamdecoding-1
  kind: primary_source
  reference: https://aclanthology.org/2024.lrec-main.7.pdf
  locator: Section 2 and Figures 1–3, printed pp. 77–79 / PDF pp. 1–3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 7d090ee35511ac9fdcdb52ca92cad5d2e96075635de73ada84abd042362a9fec
  support: supports
  summary: 'Finished hypotheses accumulate outside the k-wide continuing beam in FCFS.
    In the contrasted vanilla procedure, completed hypotheses remain among the beam
    candidates and can later fall out. These are different search policies despite
    a shared beam width. Version: LREC-COLING 2024, 77–90; published ACL Anthology
    PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages:
    1, 2, 3.'
- evidence_id: patiencecontrolledbeamdecoding-0
  kind: primary_source
  reference: https://aclanthology.org/2024.lrec-main.7.pdf
  locator: Figure 1 line 13, printed p. 77 / PDF p. 1; Patience Factor for FCFS, Section
    2, printed p. 79 / PDF p. 3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 7d090ee35511ac9fdcdb52ca92cad5d2e96075635de73ada84abd042362a9fec
  support: supports
  summary: 'A generalization of first-come, first-served sequence beam decoding that
    retains beam width k for continuing hypotheses but uses a positive patience factor
    p to stop when the accumulated completed-hypothesis count reaches at least k·p.
    Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct from the
    2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3.'
- evidence_id: patiencecontrolledbeamdecoding-1
  kind: primary_source
  reference: https://aclanthology.org/2024.lrec-main.7.pdf
  locator: Section 2, Section 3.3 and Limitations, printed pp. 79–81 / PDF pp. 3–5
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 7d090ee35511ac9fdcdb52ca92cad5d2e96075635de73ada84abd042362a9fec
  support: supports
  summary: 'The paper separates stopping depth from beam breadth and reports task-dependent
    behavior; its limitations explicitly restrict summarization evidence to English
    news. More extensive search and better generated-text quality are not equivalent
    claims. Version: LREC-COLING 2024, 77–90; published ACL Anthology PDF (distinct
    from the 2022 arXiv version). Actually inspected rendered PDF pages: 1, 2, 3.'
- evidence_id: vanillasequencebeamdecoding-0
  kind: primary_source
  reference: https://aclanthology.org/2024.lrec-main.7.pdf
  locator: Section 2 and Figures 2–3, printed pp. 78–79 / PDF pp. 2–3
  accessed_at: '2026-10-11T06:19:44Z'
  snapshot_sha256: 7d090ee35511ac9fdcdb52ca92cad5d2e96075635de73ada84abd042362a9fec
  support: supports
  summary: 'A layer-based sequence beam decoder in which completed and unfinished
    hypotheses compete for the same k beam slots: finished hypotheses are carried
    forward unchanged, unfinished hypotheses are extended, and the top-scoring candidates
    form the next beam. Version: LREC-COLING 2024, 77–90; published ACL Anthology
    PDF (distinct from the 2022 arXiv version). Actually inspected rendered PDF pages:
    1, 2, 3.'
- evidence_id: vanillasequencebeamdecoding-1
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Algorithm 1 and footnotes, printed p. 797 / PDF p. 3
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The standard sequence-beam algorithm initializes an empty candidate pool
    for each time step, carries EOS-complete hypotheses unchanged, extends unfinished
    hypotheses and selects the next top-k beam. This supplies an explicit layer-pool
    scope for the later vanilla-policy description. Version: Transactions of the Association
    for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF.
    Actually inspected rendered PDF pages: 3, 4, 5, 6, 7, 8.'
- evidence_id: dds-driver-analysis
  kind: record_content
  reference: research/validation/20261011T062948Z-dds-driver-counterexample.json
  locator: Literal driver and curator variant traces; companion script research/validation/20261011T062948Z-dds-driver-counterexample.py
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: 621ac3f24b866d8928cf7b7c24ee6e2bec3f2ee8aa5762a960d2fe2287c7e0fa
  support: context_only
  summary: The printed driver overwrites the returned depth each iteration. On this
    finite unbalanced binary tree, it stops after visiting LL and R and misses goal
    LR. Retaining the maximum depth observed across passes finds LR in this example.
    This supports deferral of a separate candidate, not a claim about the correctness
    of the five added procedures.
assessments:
- assessment_id: limiteddiscrepancysearch
  area: evidence
  topic: Identity, discrepancy accounting, completed-output policy and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  evidence_ids:
  - identity
  - mapping
  - limiteddiscrepancysearch-0
  - limiteddiscrepancysearch-1
  - limiteddiscrepancysearch-2
  summary: The original LDS searches paths with at most k discrepancies in each pass.
    It differs from Korf’s improved LDS, which avoids revisiting leaves at the supplied
    maximum depth by allocating an exact discrepancy count there, and from depth-bounded
    discrepancy search, which bounds where deviations may occur. The original 1995
    Figure 1 explores the nonpreferred child first when discrepancy budget remains;
    Korf’s 1996 presentation of original LDS uses the opposite within-pass order.
    The names do not establish identical visit sequences. No normalized identity match
    was found across the 442 AIO and 141 prior native records; ignored-inclusive text
    hits in the main checkout were prior discovery leads and incidental substrings
    such as builds in records, source text and dependencies, not existing concept
    records.
  details: Completeness applies to exhaustive passes on a finite tree with a sufficient
    discrepancy/depth limit and adequate resources. A fixed early-pass cutoff is not
    a decision procedure for unsolvability. The first goal found is not generally
    a minimum-cost or shortest-path goal. Successor preference is a search-order heuristic,
    not an admissible cost bound. The curated original mechanism is binary. Counting
    any alternate child as one discrepancy and assigning rank-based discrepancy costs
    are distinct multiway extensions requiring an explicit policy. Repeated at-most-k
    passes revisit paths. The subsequent ILDS paper qualifies the original redundancy
    argument and supplies cases where discrepancy search has no advantage over ordinary
    DFS. The original paper references an LDS-BBS appendix that is not present in
    the inspected seven-page download. The bounded-backtracking hybrid is not asserted
    as part of this record.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - limiteddiscrepancysearch-0
    - limiteddiscrepancysearch-1
    - limiteddiscrepancysearch-2
  - name: aio-assessment
    value: explicit no-match
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: improvedlimiteddiscrepancysearch
  area: evidence
  topic: Identity, discrepancy accounting, completed-output policy and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:ImprovedLimitedDiscrepancySearch
  evidence_ids:
  - identity
  - mapping
  - improvedlimiteddiscrepancysearch-0
  - improvedlimiteddiscrepancysearch-1
  summary: ILDS is the 1996 improvement to LDS, not a generic label for any later
    discrepancy-search modification. Its exact-count guarantee concerns leaves at
    the specified maximum depth; shallower leaves and internal nodes can still be
    revisited. The supplied depth bound differs from a bound on the depths at which
    discrepancies are allowed. No normalized identity match was found across the 442
    AIO and 141 prior native records; ignored-inclusive text hits in the main checkout
    were prior discovery leads and incidental substrings such as builds in records,
    source text and dependencies, not existing concept records.
  details: A valid upper bound on maximum depth is an input. A loose bound or pruning
    that creates shallower leaves reduces the benefit because those leaves may be
    visited on several passes. Visiting each maximum-depth leaf once does not mean
    visiting every internal node once; repeated prefixes remain. The complete uniform-tree
    expansion analysis is conditional on that tree shape. It does not establish an
    unconditional wall-clock advantage on pruned trees or early-terminated searches.
    The procedure’s discrepancy priority does not guarantee that the first goal is
    shortest or globally minimum-cost. No universal superiority over DFS is asserted.
    The 1996 prose gives a depth-three original-LDS path count inconsistent with its
    own displayed counting formula and the original paper’s trace. No literal 19-path
    count is adopted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - improvedlimiteddiscrepancysearch-0
    - improvedlimiteddiscrepancysearch-1
  - name: aio-assessment
    value: explicit no-match
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: fcfsbeamdecoding
  area: evidence
  topic: Identity, discrepancy accounting, completed-output policy and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:FCFSBeamDecoding
  evidence_ids:
  - identity
  - mapping
  - fcfsbeamdecoding-0
  - fcfsbeamdecoding-1
  summary: FCFS here names a sequence-decoding policy, not first-in-first-out queue
    scheduling. Completed sequences leave the active beam and remain in a separate
    set. This differs from the paper’s vanilla beam decoder, where finished and unfinished
    hypotheses compete for the same beam slots, and from score-prioritized per-length
    best-first beam search. The original policy is the patience-controlled family’s
    p=1 case. No normalized identity match was found across the 442 AIO and 141 prior
    native records; ignored-inclusive text hits in the main checkout were prior discovery
    leads and incidental substrings such as builds in records, source text and dependencies,
    not existing concept records.
  details: The count-based stopping rule can discard unfinished candidates and is
    not a global optimality certificate or a guarantee of equality to vanilla beam
    decoding. The record identifies the paper’s specified procedure. Claims about
    particular library defaults are historical context, not assertions about current
    software versions. The simplified pseudocode assumes that candidate selection
    and completion return are defined. Exhausted candidate pools, absence of any EOS
    completion, ties and maximum-length handling require explicit implementation policies.
    The score and any length penalty affect candidate selection and comparison of
    completed outputs. A fixed beam width alone does not determine output quality.
    The paper’s favorable comparisons are task/model dependent; no numerical benchmark
    gain or universal generation-quality claim is curated.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - fcfsbeamdecoding-0
    - fcfsbeamdecoding-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: patiencecontrolledbeamdecoding
  area: evidence
  topic: Identity, discrepancy accounting, completed-output policy and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:PatienceControlledBeamDecoding
  evidence_ids:
  - identity
  - mapping
  - patiencecontrolledbeamdecoding-0
  - patiencecontrolledbeamdecoding-1
  summary: This is the algorithmic stopping-policy variant introduced by Kasai and
    colleagues, not a standalone model, learned parameter or generic training patience
    rule. Setting p=1 recovers their FCFS baseline; changing p separates its finished-output
    threshold from its continuing-beam width. No normalized identity match was found
    across the 442 AIO and 141 prior native records; ignored-inclusive text hits in
    the main checkout were prior discovery leads and incidental substrings such as
    builds in records, source text and dependencies, not existing concept records.
  details: The finite maximum length can end decoding before the completion threshold
    is reached. Empty finished sets and exhausted candidate pools need an implementation-specific
    outcome. Increasing patience can expose more completions but does not guarantee
    better task quality, a globally optimal sequence, or equivalence to vanilla beam
    search. The parameter is a stopping threshold, not a score upper bound or a proof
    that no unfinished hypothesis can improve the incumbent. The source evaluates
    specific translation and news-summarization settings. English news summarization
    does not establish benefits for all languages, domains or tasks. No current library
    default, runtime gain, numerical quality improvement or trained-model execution
    is claimed.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - patiencecontrolledbeamdecoding-0
    - patiencecontrolledbeamdecoding-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: vanillasequencebeamdecoding
  area: evidence
  topic: Identity, discrepancy accounting, completed-output policy and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:VanillaSequenceBeamDecoding
  evidence_ids:
  - identity
  - mapping
  - vanillasequencebeamdecoding-0
  - vanillasequencebeamdecoding-1
  summary: This is the vanilla sequence-decoding policy contrasted with FCFS by Kasai
    and colleagues. It specializes generic breadth-first beam search by specifying
    EOS retention and competition for active slots. Finished outputs are not accumulated
    in a separate permanent set, and the procedure is not the score-prioritized per-length
    best-first decoder. No normalized identity match was found across the 442 AIO
    and 141 prior native records; ignored-inclusive text hits in the main checkout
    were prior discovery leads and incidental substrings such as builds in records,
    source text and dependencies, not existing concept records.
  details: A completed hypothesis can later fall off the beam because it competes
    with unfinished candidates. Its discovery alone does not reserve an output slot.
    Finite beam pruning is not exact global MAP decoding. Different tie, length-score
    and maximum-length policies can change outputs. At the length limit, an implementation
    must specify what to return if no retained hypothesis is EOS-complete; the simplified
    figures do not provide a universal failure policy. Figure 2 in the 2024 paper
    omits initialization/reset of its temporary H pool. The fresh-per-layer interpretation
    is supported by the layer-based prose and the explicit reset in Meister et al.
    2020 Algorithm 1; the record does not certify the 2024 figure as executable code.
    The name identifies the source-defined policy, not a claim that all libraries
    or all uses of beam search implement it.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A specified search or decoding procedure rather than a trained model,
      a benchmark result or a task.
    evidence_ids:
    - vanillasequencebeamdecoding-0
    - vanillasequencebeamdecoding-1
  - name: aio-assessment
    value: 'related_match: NaturalLanguageProcessing'
    definition: NLP mappings are non-hierarchical method-to-domain relationships supported
      by central source scope; graph-search no-match decisions reject six exact targets
      in the pin.
    evidence_ids:
    - mapping
    - identity
- assessment_id: adversarial-boundaries
  area: scope
  topic: Discrepancy budgets and beam completion accounting are separate algorithm
    choices
  outcome: supported
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  evidence_ids:
  - limiteddiscrepancysearch-0
  - limiteddiscrepancysearch-1
  - improvedlimiteddiscrepancysearch-0
  - fcfsbeamdecoding-0
  - patiencecontrolledbeamdecoding-0
  - vanillasequencebeamdecoding-0
  - vanillasequencebeamdecoding-1
  summary: The records distinguish at-most discrepancy passes from exact-count-at-maximum-depth
    passes, and persistent completed-output sets from EOS hypotheses competing inside
    a beam. The patience family explicitly contains the FCFS p=1 case.
  details: No minimum-cost first-goal claim, universal runtime improvement, global
    sequence-optimality guarantee or current library default is inferred. The original
    and later LDS traversal orders are distinguished. ILDS can repeat internal nodes
    and shallow leaves. A parameterized method family and its historically defined
    baseline overlap without being identical concepts; this boundary is stated explicitly.
- assessment_id: source-caveats
  area: evidence
  topic: Incomplete pseudocode and inconsistent printed claims
  outcome: supported
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  evidence_ids:
  - limiteddiscrepancysearch-0
  - improvedlimiteddiscrepancysearch-0
  - vanillasequencebeamdecoding-1
  - dds-driver-analysis
  summary: The record scopes preserve the LDS appendix access gap, the ILDS path-count
    inconsistency, the vanilla temporary-pool omission and the separate DDS driver
    concern.
  details: The vanilla fresh-layer interpretation has an explicit primary citation
    to the 2020 Algorithm 1. The DDS example is a curator transcription on one finite
    tree; its successful modification is not an author-approved correction or a general
    proof. It remains outside this five-record cohort.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:LimitedDiscrepancySearch
  - AIMech:ImprovedLimitedDiscrepancySearch
  - AIMech:FCFSBeamDecoding
  - AIMech:PatienceControlledBeamDecoding
  - AIMech:VanillaSequenceBeamDecoding
  evidence_ids:
  - identity
  - mapping
  - limiteddiscrepancysearch-0
  - limiteddiscrepancysearch-1
  - limiteddiscrepancysearch-2
  - improvedlimiteddiscrepancysearch-0
  - improvedlimiteddiscrepancysearch-1
  - fcfsbeamdecoding-0
  - fcfsbeamdecoding-1
  - patiencecontrolledbeamdecoding-0
  - patiencecontrolledbeamdecoding-1
  - vanillasequencebeamdecoding-0
  - vanillasequencebeamdecoding-1
  rationale: Original at-most discrepancy passes and ILDS exact-at-depth passes have
    different repetition behavior. The vanilla decoder keeps completed hypotheses
    in its competitive beam; FCFS accumulates completions separately and stops at
    k; controlled patience generalizes that threshold to k*p. Preserve each explicit
    specialization without asserting disjointness, equivalence to a task, or equivalence
    to every use of beam search.
limitations:
- Adversarial author self-review, not independent approval; all five records remain
  DRAFT.
- No unconditional completeness, optimality, runtime or decoding-quality claim is
  transferred between different procedures.
- The vanilla pool reset is supported by a second primary algorithm, while the later
  abbreviated figure remains explicitly incomplete.
- The DDS illustration is a curator transcription, not an author erratum, implementation
  audit or general proof.
- Repeated citations to different passages in the same paper are not independent studies.
- An initial vendored-check failed because the restricted environment could not resolve
  the public source host. The network-enabled rerun passed; this was an access failure,
  not a vendored artifact mismatch.
- The two cross-paper claim citations were tightened before this saved assessment.
  No unresolved corrective issue remains in this review scope.
- The source pin and generated records are unchanged. These five reviewed targets
  do not retire unrelated historical findings or establish discovery saturation.
tags:
- native-concepts
- discrepancy-search
- sequence-decoding
- primary-papers
- self-review
- discovery-ongoing
```
