# Resolved scientific self-review of five beam-search concepts

- Review: 20261011T060751Z-beam-search-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T06:07:51Z
- Finished UTC: 2026-10-11T06:07:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five scoped algorithm identities and mechanisms are supported by inspected primary methods and explicit AIO no-match assessments. The minor BSS alias finding is resolved by removing the unsupported optional alias from the record and discovery entry, with exact predecessor lineage retained.

## Scope And Provenance

Full review of breadth-first beam search, global-cap best-first beam search, beam-stack search, DCBSS and BULB.

Selection: Exactly the five maintained IDs in the beam-search discovery ledger; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base fc0edca0452ab5d37d6d8411741daa4b61b68192.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BeamSearch | data/curated/BeamSearch.yaml | maintained | Breadth-first beam search |
| AIMech:GlobalFrontierBeamSearch | data/curated/GlobalFrontierBeamSearch.yaml | maintained | Best-first beam search with a global frontier cap |
| AIMech:BeamStackSearch | data/curated/BeamStackSearch.yaml | maintained | Beam-stack search |
| AIMech:DivideConquerBeamStackSearch | data/curated/DivideConquerBeamStackSearch.yaml | maintained | Divide-and-conquer beam-stack search |
| AIMech:BULB | data/curated/BULB.yaml | maintained | Beam search using limited discrepancy backtracking |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | Checked 135 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | Checked 28 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 28,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 64.82s (0:01:04)<br>Checked 442 record(s); 0 failed.<br>Checked 135 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 28 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 28,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Pruning scope, backtracking policy, resource assumptions and AIO no-match assessment

evidence: supported. Targets: AIMech:BeamSearch.

This record denotes the conventional breadth-first form of beam search. Wider historical uses of beam search also include global best-first frontier truncation and other heuristic pruning procedures. A width of one follows a single surviving continuation; it is not the unbounded global-frontier algorithm curated as greedy best-first search. No normalized identity match was found across the 442 AIO and 130 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations and search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing concept records.

Width pruning can discard every path to a solution or every optimal path, so basic beam search has no general completeness or optimality guarantee. A layer-width bound does not by itself bound all memory: stored predecessor information, retained earlier layers, generated successors and any global duplicate table must also be accounted for. Ranking, ties, goal stopping and duplicate handling are additional choices. Increasing the beam width does not guarantee an improvement in returned solution quality for every implementation and problem.

### Pruning scope, backtracking policy, resource assumptions and AIO no-match assessment

evidence: supported. Targets: AIMech:GlobalFrontierBeamSearch.

The qualified name identifies the global frontier truncation described in the 2005 and 2010 search papers. The unqualified phrase best-first beam search is intentionally not an identity alias: Meister, Vieira and Cotterell use that phrase in 2020 for a decoding procedure with a per-sequence-length path limit. A shared name does not equate those pruning rules. No normalized identity match was found across the 442 AIO and 130 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations and search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing concept records.

Global frontier pruning can permanently remove a needed path; the cap alone establishes neither completeness nor optimality. The cap applies to the open frontier, not automatically to closed tables, predecessor storage, generated successors or the total program memory. No equivalence to breadth-first beam output, monotonic quality with larger width, or universal runtime advantage is asserted.

### Pruning scope, backtracking policy, resource assumptions and AIO no-match assessment

evidence: supported. Targets: AIMech:BeamStackSearch.

Beam-stack search combines breadth-first beam expansion with chronological backtracking and an incumbent solution-cost bound. It is distinct from permanent beam pruning, limited-discrepancy beam backtracking, and the separately named iterative-deepening BSIDA-star variant. No normalized identity match was found across the 442 AIO and 130 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations and search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing concept records.

The paper’s termination and optimality argument assumes finite branching, a positive lower bound on operator cost and a finite initial upper bound supplied by an actual solution, together with admissible pruning. It is not a guarantee for arbitrary zero-cost cycles, an infinite bound or arbitrary duplicate policies. Ties require a consistent ordering, or enough beam capacity to retain the unbroken tie group; a bare numeric range with unresolved ties is insufficient. The baseline retains up to a beam of nodes per depth layer plus the beam stack. O(w*d) node storage does not mean a fixed total-memory cap independent of search depth. The initially supplied solution must remain available if no improvement is found. An upper-bound number alone is not a returned path; this record does not certify the displayed pseudocode as a complete implementation.

### Pruning scope, backtracking policy, resource assumptions and AIO no-match assessment

evidence: supported. Targets: AIMech:DivideConquerBeamStackSearch.

DCBSS is the divide-and-conquer implementation of beam-stack search described by Zhou and Hansen. Unlike divide-and-conquer beam search without backtracking, it retains beam-stack range information that permits previously discarded layers to be regenerated and searched further. No normalized identity match was found across the 442 AIO and 130 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations and search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing concept records.

Four retained node layers do not imply constant total storage: the beam stack still has depth-dependent entries, and path output, temporary successors and reconstruction state also require memory. Discarding layers trades storage for regeneration and reconstruction work; no universal runtime improvement is implied. The underlying beam-stack pruning, tie handling and bounded-search assumptions still matter. Layered duplicate detection must be matched to the graph setting; the paper distinguishes directed and undirected behavior. The paper summarizes recursive solution recovery and refers to earlier work for implementation details. This record supports the described mechanism, not a complete executable reconstruction implementation.

### Pruning scope, backtracking policy, resource assumptions and AIO no-match assessment

evidence: supported. Targets: AIMech:BULB.

BULB denotes Furcy and Koenig’s Beam search Using Limited discrepancy Backtracking. A discrepancy selects a nonpreferred successor slice; it is not a numerical heuristic error or an action cost. The inspected algorithm is presented for unit-cost state-space search and seeks a path, not necessarily a shortest path. No normalized identity match was found across the 442 AIO and 130 prior native records; ignored-inclusive text hits in the main checkout were prior discovery leads, source citations and search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing concept records.

Completeness is conditional on enough memory to store a beam along a solution path. A fixed memory budget and arbitrary beam width do not guarantee solving every instance. The method need not return a shortest path. An anytime extension is discussed separately from the base procedure. The O(B*d) storage statement concerns retained slices along the active search; temporary successor generation, heuristic data and other implementation storage need separate accounting. The active hash table prevents cycles involving retained states and some transpositions, but it is not a permanent global closed list of every state ever visited. Figure 4 has an apparent depth-label inconsistency: nextSlice labels a successor with depth although the caller next probes depth+1. The prose describes a next-level slice. This record follows that described mechanism and does not certify the literal pseudocode as executable.

### Evidence for the short BSS alias

identity: supported. Targets: AIMech:BeamStackSearch.

The optional unsupported BSS alias is absent from both current alias lists; the supported full name and stable local ID remain.

The only saved same-key predecessor was verified across all hidden/ignored-inclusive bundles. Its affected target is retained. The resolution removes an unsubstantiated assertion without claiming that no outside source ever uses this abbreviation.

### Counterexamples to unconditional width, memory and completeness claims

scope: supported. Targets: AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB.

The records distinguish a layer cap from a whole-frontier cap and from NLP per-length counters, retain beam-stack incumbent/tie assumptions, do not turn four retained layers into constant total storage, and qualify BULB completeness by memory.

The BSS initial-incumbent obligation is explicit curator inference. BULB’s apparent printed depth-label inconsistency is documented rather than silently corrected. BSIDA-star is deferred because its short contour description leaves a progress boundary unresolved. No benchmark result or executable correctness certificate is asserted.

## Findings

### unsupported-short-alias: Remove the unsubstantiated BSS identity alias

minor / resolved / confirmed; issue key: aimech-beam-stack-unsubstantiated-alias.

The draft asserts BSS although the inspected sources only establish the full beam-stack name and DCBSS for the separate divide-and-conquer variant. Remove this optional unsupported alias. The finding does not claim the abbreviation is absent from all literature and does not dispute the core algorithm identity.

Disposition: Removed BSS from the record and mirrored discovery entry, re-read current bytes, reinspected hashes, passed the required final checks and verified the only saved predecessor and its full affected-target union across hidden and ignored files. Core identity and scientific claims remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:BeamSearch, AIMech:GlobalFrontierBeamSearch, AIMech:BeamStackSearch, AIMech:DivideConquerBeamStackSearch, AIMech:BULB. Layer-based pruning, global frontier truncation, chronological range backtracking, layer regeneration with relay reconstruction, and discrepancy-budget beam backtracking are different procedures. Shared names or beam terminology do not justify lumping them. The short alias defect is removable without changing concept boundaries.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T060240Z-beam-search.json | supports | No normalized match across all 442 AIO labels/scoped synonyms and 130 preceding native identities. Ignored-inclusive full-text searches found 16 worktree and 35 main lines: prior frontier leads, search-order contrasts and source references, plus 19 lightbulb/wet-bulb dependency substrings. None denotes an existing record for these five identities. The global-cap record has a qualified name and no unqualified best-first beam alias because the 2020 NLP paper defines a different per-length rule. |
| mapping | sources/aio/aio.json; Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning | supports | Exact CLASS nodes, synonyms and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning were inspected, alongside a beam/search/planning/heuristic/path/traversal/symbolic/reasoning/graph label scan. Each record uses aio_no_match with six target-specific rejections; a learned model, learning task or mathematical function does not denote these search procedures. |
| beamsearch-0 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Background: Beam search, PDF p. 1; breadth-first scope on PDF p. 2 | supports | A heuristic search procedure that advances by depth layers, retaining at most a chosen beam width of the best-ranked candidate nodes for each next layer and discarding the other candidates. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: 2. |
| beamsearch-1 | https://www.cs.unh.edu/~ruml/papers/beam-socs10.pdf; Beam Search and Closed Lists, PDF pp. 4–5; Incompleteness of Beam Search, PDF p. 5 | supports | The comparative study distinguishes layer-limited and whole-frontier beam policies, and shows why duplicate handling must be specified separately. Its non-unit-cost examples challenge a universal claim that widening a beam always improves the returned solution. Source version: SoCS 1(1), 129–136 (2010); author-hosted manuscript with unnumbered PDF pages. Rendered pages actually inspected: 4, 5. |
| globalfrontierbeamsearch-0 | https://www.cs.unh.edu/~ruml/papers/beam-socs10.pdf; Beam Search, PDF p. 4: best-first versus breadth-first beams | supports | A best-first search procedure that limits the entire open frontier to a fixed number of nodes by discarding the worst-ranked frontier nodes when that capacity is exceeded. Source version: SoCS 1(1), 129–136 (2010); author-hosted manuscript with unnumbered PDF pages. Rendered pages actually inspected: 4. |
| globalfrontierbeamsearch-1 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Background: Beam search, PDF p. 1, broader best-first use | supports | The beam-stack paper distinguishes its layer-based beam from the broader usage that truncates a best-first open list after adding successors. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: . |
| globalfrontierbeamsearch-2 | https://aclanthology.org/2020.tacl-1.51.pdf; Algorithm 2, printed p. 797 / PDF p. 3; Section 3.1 choice point 3 and Table 1, printed p. 798 / PDF p. 4 | supports | The later NLP paper controls how many paths of each sequence length are considered. That per-length counter is a different rule from limiting the total open frontier, so the same phrase does not identify the global-cap procedure without qualification. Source version: Transactions of the Association for Computational Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Rendered pages actually inspected: 3, 4. |
| beamstacksearch-0 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Beam-stack search, PDF pp. 2–3; Theorem 1, PDF pp. 3–4 | supports | A layer-based beam search augmented with a stack of admitted evaluation ranges so that backtracking systematically revisits successors previously discarded by beam-width pruning. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: 2, 3. |
| beamstacksearch-1 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Memory efficiency, PDF p. 4; Figure 1, PDF p. 5, initialization and return path; Beam-stack iterative-deepening A-star, PDF p. 6 | supports | The basic method starts from a bound corresponding to an actual solution, while the paper introduces a separate iterative-deepening version when such a bound is unavailable. As an implementation obligation inferred from the displayed initialization and return logic, a wrapper must preserve the initial incumbent when the improvement search finds no better path. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: 5, 6. |
| divideconquerbeamstacksearch-0 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Memory efficiency and Divide-and-conquer beam search, PDF p. 4; Divide-and-conquer beam-stack search and Figure 1, PDF p. 5; continuation on PDF p. 6 | supports | A beam-stack search implementation that retains a small set of search layers and relay information, regenerates missing layers for backtracking, and reconstructs a solution through recursive subproblems. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: 5, 6. |
| divideconquerbeamstacksearch-1 | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Using external memory, PDF p. 6 | supports | A separately described external-memory option stores old layers on disk instead of regenerating them. Restoring a layer also requires the previous layer for duplicate detection and repairing relay references; disk use is an optional implementation extension, not part of every DCBSS execution. Source version: ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages actually inspected: 6. |
| bulb-0 | https://www.ijcai.org/Proceedings/05/Papers/0596.pdf; Sections 2–3.3, PDF pp. 2–4; Figure 4 on PDF p. 3 | supports | A memory-bounded beam search that explores heuristic-ranked slices using increasing limited-discrepancy budgets and removes backtracked slices so that alternative beams can be examined. Source version: IJCAI 2005 proceedings; official conference PDF with unnumbered pages. Rendered pages actually inspected: 3, 4. |
| bulb-1 | https://www.ijcai.org/Proceedings/05/Papers/0596.pdf; Section 3.4, PDF p. 4; Conclusion, PDF p. 7 | supports | The paper qualifies completeness by the memory needed to retain a beam to a solution and describes the base method as approximate in solution length. Its conclusion discusses conversion to an anytime algorithm as an extension, not an automatic guarantee of the presented stopping rule. Source version: IJCAI 2005 proceedings; official conference PDF with unnumbered pages. Rendered pages actually inspected: 4, 7. |
| bulb-2 | https://www.ijcai.org/Proceedings/05/Papers/0596.pdf; Figure 4, PDF p. 3: recursive depth increment and nextSlice depth assignment; Section 3.3 prose, PDF p. 4 | supports | Visual inspection identifies an apparent inconsistency between the recursive depth increment and the depth label assigned to generated successors. The next-level interpretation comes from the adjacent prose; no corrected reference implementation or author erratum was established by this review. Source version: IJCAI 2005 proceedings; official conference PDF with unnumbered pages. Rendered pages actually inspected: 3, 4. |
| alias-evidence | https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf; Complete extracted PDF pp. 1–9; named algorithm descriptions on pp. 2–5 | supports | The inspected paper establishes the full beam-stack name and the DCBSS abbreviation; a whole-word search found no standalone BSS. The predecessor draft asserted BSS; the current record no longer does. This bounds the finding to missing inspected support, not universal absence of the abbreviation. |
| alias-resolution | data/curated/BeamStackSearch.yaml; aliases, name, id and curation.updated_at; discovery entry aliases and review_remediation | supports | Both current alias lists are empty; the full name and AIMech:BeamStackSearch remain unchanged. The discovery ledger records the actual correction time and issue 27. Hidden/ignored-inclusive saved-bundle traversal found exactly one open same-key head, 20261011T060506Z-beam-search-open/unsupported-short-alias, with the same affected target. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval; all five records remain DRAFT.
- BULB’s apparent depth-label inconsistency is a source caveat, not an asserted corrected implementation. Targeted searches did not establish a primary erratum.
- Preserving an initial beam-stack incumbent is explicit curator inference from the source initialization and return logic.
- For this cohort, 2020 NLP evidence is limited to PDF pp. 1–4 for name disambiguation. Subsequent proofs and scoring variants are being researched separately, without importing their guarantees into these records.
- Repeated source identifiers for different passages of the same paper do not represent independent studies.
- Memory statements distinguish node layers, depth-dependent metadata, temporary successors and other implementation storage.
- No puzzle solving, benchmark execution, complete proof certification or implementation audit was performed.
- All required structural checks passed; discovery remains ongoing with older and new pending candidates.
- The first unsaved predecessor draft failed schema validation because an external issue was represented numerically; the URL string was used before saving. No immutable review was overwritten.
- The alias correction is supported by inspected-source coverage, not proof that the abbreviation is never used in other literature. GitHub closure awaits the authorized PR merge.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T060751Z-beam-search-resolved
kind: category
repository: CultureBotAI/AIMech
title: Resolved scientific self-review of five beam-search concepts
started_at: '2026-10-11T06:07:51Z'
finished_at: '2026-10-11T06:07:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own records against
    inspected primary methods; no independent approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five scoped algorithm identities and mechanisms are supported by inspected
  primary methods and explicit AIO no-match assessments. The minor BSS alias finding
  is resolved by removing the unsupported optional alias from the record and discovery
  entry, with exact predecessor lineage retained.
source:
  git_revision: fc0edca0452ab5d37d6d8411741daa4b61b68192
  state: working_tree
  inputs:
  - path: data/curated/BULB.yaml
    sha256: daac190f8e4e5c66eb9ed6a4a32eee911fc756b8fc068b47522a34814ae6df50
    role: target
  - path: data/curated/BeamSearch.yaml
    sha256: aec9aab4ec700ecfc6aa4b71c98f33bdbb456d131748729a98480abef34875bc
    role: target
  - path: data/curated/BeamStackSearch.yaml
    sha256: 161a74d1afbe844b276989df5e068268ffa239e62799523221b56a626b4f4861
    role: target
  - path: data/curated/DivideConquerBeamStackSearch.yaml
    sha256: 98ac2b0108b54fa8fb833693f2b8f88531f9f84853c2c659c0acc89b4ab53cba
    role: target
  - path: data/curated/GlobalFrontierBeamSearch.yaml
    sha256: 9aab298f05ea47fadb17df3bc0cc536ea954777aa47f9ee1e231937c8443ea6b
    role: target
  - path: research/discovery/20261011T060240Z-beam-search.json
    sha256: a47234215de55ccec0d465e8c5beeee05dfbb649680ce54648764489b378f36c
    role: context
  - path: reviews/structured/20261011T060506Z-beam-search-open/review.yaml
    sha256: 3681d92ba0276fba68c3ac0c00cb644aec2161a27314f6006a347b08b777cff7
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
- target_id: AIMech:BeamSearch
  path: data/curated/BeamSearch.yaml
  label: Breadth-first beam search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BeamSearch.yaml
    role: maintained_record
- target_id: AIMech:GlobalFrontierBeamSearch
  path: data/curated/GlobalFrontierBeamSearch.yaml
  label: Best-first beam search with a global frontier cap
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GlobalFrontierBeamSearch.yaml
    role: maintained_record
- target_id: AIMech:BeamStackSearch
  path: data/curated/BeamStackSearch.yaml
  label: Beam-stack search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BeamStackSearch.yaml
    role: maintained_record
- target_id: AIMech:DivideConquerBeamStackSearch
  path: data/curated/DivideConquerBeamStackSearch.yaml
  label: Divide-and-conquer beam-stack search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DivideConquerBeamStackSearch.yaml
    role: maintained_record
- target_id: AIMech:BULB
  path: data/curated/BULB.yaml
  label: Beam search using limited discrepancy backtracking
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BULB.yaml
    role: maintained_record
scope:
  description: Full review of breadth-first beam search, global-cap best-first beam
    search, beam-stack search, DCBSS and BULB.
  selection: Exactly the five maintained IDs in the beam-search discovery ledger;
    no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exclusions:
  - target: Formal proof certification, reference implementation correctness and benchmark
      replication
    reason: The review assesses identities, cited mechanisms and limitations; source
      pseudocode inconsistencies are retained explicitly.
  - target: BSIDA-star, NLP beam variants, DCBS, LDS and other pending frontiers
    reason: Separate primary-method and identity work remains, with concrete next
      checks in the discovery ledger.
checks:
- check_id: final-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: final-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    '
- check_id: final-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 135 curated concept record(s); 0 error(s).

    '
- check_id: final-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    '
- check_id: final-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 28 history record(s); 0 error(s).

    '
- check_id: final-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 28,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: final-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 64.82s (0:01:04)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 135 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 28 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 28,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: final-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T060240Z-beam-search.json
  accessed_at: '2026-10-11T06:05:06Z'
  support: supports
  summary: 'No normalized match across all 442 AIO labels/scoped synonyms and 130
    preceding native identities. Ignored-inclusive full-text searches found 16 worktree
    and 35 main lines: prior frontier leads, search-order contrasts and source references,
    plus 19 lightbulb/wet-bulb dependency substrings. None denotes an existing record
    for these five identities. The global-cap record has a qualified name and no unqualified
    best-first beam alias because the 2020 NLP paper defines a different per-length
    rule.'
  search_scope: All 442 AIO labels/scoped synonyms, 130 prior native IDs/names/aliases,
    and both checkouts including hidden and ignored files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Exact CLASS nodes and edges for GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM,
    MachineLearningTask, MathematicalFunction and ReinforcementLearning
  accessed_at: '2026-10-11T06:05:06Z'
  support: supports
  summary: Exact CLASS nodes, synonyms and edges for GraphLanguageModel, ReasoningLLM,
    NeuroSymbolicLLM, MachineLearningTask, MathematicalFunction and ReinforcementLearning
    were inspected, alongside a beam/search/planning/heuristic/path/traversal/symbolic/reasoning/graph
    label scan. Each record uses aio_no_match with six target-specific rejections;
    a learned model, learning task or mathematical function does not denote these
    search procedures.
- evidence_id: beamsearch-0
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: 'Background: Beam search, PDF p. 1; breadth-first scope on PDF p. 2'
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'A heuristic search procedure that advances by depth layers, retaining
    at most a chosen beam width of the best-ranked candidate nodes for each next layer
    and discarding the other candidates. Source version: ICAPS 2005 proceedings, 90–98;
    official conference PDF with unnumbered pages. Rendered pages actually inspected:
    2.'
- evidence_id: beamsearch-1
  kind: primary_source
  reference: https://www.cs.unh.edu/~ruml/papers/beam-socs10.pdf
  locator: Beam Search and Closed Lists, PDF pp. 4–5; Incompleteness of Beam Search,
    PDF p. 5
  accessed_at: '2026-10-11T05:39:45Z'
  snapshot_sha256: cfc3cf8f422bdd0c52caef1c858775b92bfca74c3187965248c4cbf7825f0d45
  support: supports
  summary: 'The comparative study distinguishes layer-limited and whole-frontier beam
    policies, and shows why duplicate handling must be specified separately. Its non-unit-cost
    examples challenge a universal claim that widening a beam always improves the
    returned solution. Source version: SoCS 1(1), 129–136 (2010); author-hosted manuscript
    with unnumbered PDF pages. Rendered pages actually inspected: 4, 5.'
- evidence_id: globalfrontierbeamsearch-0
  kind: primary_source
  reference: https://www.cs.unh.edu/~ruml/papers/beam-socs10.pdf
  locator: 'Beam Search, PDF p. 4: best-first versus breadth-first beams'
  accessed_at: '2026-10-11T05:39:45Z'
  snapshot_sha256: cfc3cf8f422bdd0c52caef1c858775b92bfca74c3187965248c4cbf7825f0d45
  support: supports
  summary: 'A best-first search procedure that limits the entire open frontier to
    a fixed number of nodes by discarding the worst-ranked frontier nodes when that
    capacity is exceeded. Source version: SoCS 1(1), 129–136 (2010); author-hosted
    manuscript with unnumbered PDF pages. Rendered pages actually inspected: 4.'
- evidence_id: globalfrontierbeamsearch-1
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: 'Background: Beam search, PDF p. 1, broader best-first use'
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'The beam-stack paper distinguishes its layer-based beam from the broader
    usage that truncates a best-first open list after adding successors. Source version:
    ICAPS 2005 proceedings, 90–98; official conference PDF with unnumbered pages.
    Rendered pages actually inspected: .'
- evidence_id: globalfrontierbeamsearch-2
  kind: primary_source
  reference: https://aclanthology.org/2020.tacl-1.51.pdf
  locator: Algorithm 2, printed p. 797 / PDF p. 3; Section 3.1 choice point 3 and
    Table 1, printed p. 798 / PDF p. 4
  accessed_at: '2026-10-11T05:59:59Z'
  snapshot_sha256: 46728395bd4f2e7eb8abea7c42f9e3260e28ba8958bde3b7e77414db617352d4
  support: supports
  summary: 'The later NLP paper controls how many paths of each sequence length are
    considered. That per-length counter is a different rule from limiting the total
    open frontier, so the same phrase does not identify the global-cap procedure without
    qualification. Source version: Transactions of the Association for Computational
    Linguistics 8, 795–809 (2020); ACL Anthology published PDF. Rendered pages actually
    inspected: 3, 4.'
- evidence_id: beamstacksearch-0
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: Beam-stack search, PDF pp. 2–3; Theorem 1, PDF pp. 3–4
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'A layer-based beam search augmented with a stack of admitted evaluation
    ranges so that backtracking systematically revisits successors previously discarded
    by beam-width pruning. Source version: ICAPS 2005 proceedings, 90–98; official
    conference PDF with unnumbered pages. Rendered pages actually inspected: 2, 3.'
- evidence_id: beamstacksearch-1
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: Memory efficiency, PDF p. 4; Figure 1, PDF p. 5, initialization and return
    path; Beam-stack iterative-deepening A-star, PDF p. 6
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'The basic method starts from a bound corresponding to an actual solution,
    while the paper introduces a separate iterative-deepening version when such a
    bound is unavailable. As an implementation obligation inferred from the displayed
    initialization and return logic, a wrapper must preserve the initial incumbent
    when the improvement search finds no better path. Source version: ICAPS 2005 proceedings,
    90–98; official conference PDF with unnumbered pages. Rendered pages actually
    inspected: 5, 6.'
- evidence_id: divideconquerbeamstacksearch-0
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: Memory efficiency and Divide-and-conquer beam search, PDF p. 4; Divide-and-conquer
    beam-stack search and Figure 1, PDF p. 5; continuation on PDF p. 6
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'A beam-stack search implementation that retains a small set of search
    layers and relay information, regenerates missing layers for backtracking, and
    reconstructs a solution through recursive subproblems. Source version: ICAPS 2005
    proceedings, 90–98; official conference PDF with unnumbered pages. Rendered pages
    actually inspected: 5, 6.'
- evidence_id: divideconquerbeamstacksearch-1
  kind: primary_source
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: Using external memory, PDF p. 6
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: 'A separately described external-memory option stores old layers on disk
    instead of regenerating them. Restoring a layer also requires the previous layer
    for duplicate detection and repairing relay references; disk use is an optional
    implementation extension, not part of every DCBSS execution. Source version: ICAPS
    2005 proceedings, 90–98; official conference PDF with unnumbered pages. Rendered
    pages actually inspected: 6.'
- evidence_id: bulb-0
  kind: primary_source
  reference: https://www.ijcai.org/Proceedings/05/Papers/0596.pdf
  locator: Sections 2–3.3, PDF pp. 2–4; Figure 4 on PDF p. 3
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: 25fa7ecf4d94bf2975c39e1c2c4180d2564a721acdaa258b9eceebaa03241172
  support: supports
  summary: 'A memory-bounded beam search that explores heuristic-ranked slices using
    increasing limited-discrepancy budgets and removes backtracked slices so that
    alternative beams can be examined. Source version: IJCAI 2005 proceedings; official
    conference PDF with unnumbered pages. Rendered pages actually inspected: 3, 4.'
- evidence_id: bulb-1
  kind: primary_source
  reference: https://www.ijcai.org/Proceedings/05/Papers/0596.pdf
  locator: Section 3.4, PDF p. 4; Conclusion, PDF p. 7
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: 25fa7ecf4d94bf2975c39e1c2c4180d2564a721acdaa258b9eceebaa03241172
  support: supports
  summary: 'The paper qualifies completeness by the memory needed to retain a beam
    to a solution and describes the base method as approximate in solution length.
    Its conclusion discusses conversion to an anytime algorithm as an extension, not
    an automatic guarantee of the presented stopping rule. Source version: IJCAI 2005
    proceedings; official conference PDF with unnumbered pages. Rendered pages actually
    inspected: 4, 7.'
- evidence_id: bulb-2
  kind: primary_source
  reference: https://www.ijcai.org/Proceedings/05/Papers/0596.pdf
  locator: 'Figure 4, PDF p. 3: recursive depth increment and nextSlice depth assignment;
    Section 3.3 prose, PDF p. 4'
  accessed_at: '2026-10-11T05:47:52Z'
  snapshot_sha256: 25fa7ecf4d94bf2975c39e1c2c4180d2564a721acdaa258b9eceebaa03241172
  support: supports
  summary: 'Visual inspection identifies an apparent inconsistency between the recursive
    depth increment and the depth label assigned to generated successors. The next-level
    interpretation comes from the adjacent prose; no corrected reference implementation
    or author erratum was established by this review. Source version: IJCAI 2005 proceedings;
    official conference PDF with unnumbered pages. Rendered pages actually inspected:
    3, 4.'
- evidence_id: alias-evidence
  kind: search
  reference: https://cdn.aaai.org/ICAPS/2005/ICAPS05-010.pdf
  locator: Complete extracted PDF pp. 1–9; named algorithm descriptions on pp. 2–5
  accessed_at: '2026-10-11T06:05:06Z'
  snapshot_sha256: eb2ac12fea9da9d376764a1959dbdbd14929962cf5b34c28e4dd20771b8d90b9
  support: supports
  summary: The inspected paper establishes the full beam-stack name and the DCBSS
    abbreviation; a whole-word search found no standalone BSS. The predecessor draft
    asserted BSS; the current record no longer does. This bounds the finding to missing
    inspected support, not universal absence of the abbreviation.
  search_scope: rg --no-ignore --hidden -n -w BSS|DCBSS over the complete locally
    extracted primary PDF text; relevant rendered algorithm pages inspected.
- evidence_id: alias-resolution
  kind: record_content
  reference: data/curated/BeamStackSearch.yaml
  locator: aliases, name, id and curation.updated_at; discovery entry aliases and
    review_remediation
  accessed_at: '2026-10-11T06:07:51Z'
  support: supports
  summary: Both current alias lists are empty; the full name and AIMech:BeamStackSearch
    remain unchanged. The discovery ledger records the actual correction time and
    issue 27. Hidden/ignored-inclusive saved-bundle traversal found exactly one open
    same-key head, 20261011T060506Z-beam-search-open/unsupported-short-alias, with
    the same affected target.
assessments:
- assessment_id: beamsearch
  area: evidence
  topic: Pruning scope, backtracking policy, resource assumptions and AIO no-match
    assessment
  outcome: supported
  target_ids:
  - AIMech:BeamSearch
  evidence_ids:
  - identity
  - mapping
  - beamsearch-0
  - beamsearch-1
  summary: This record denotes the conventional breadth-first form of beam search.
    Wider historical uses of beam search also include global best-first frontier truncation
    and other heuristic pruning procedures. A width of one follows a single surviving
    continuation; it is not the unbounded global-frontier algorithm curated as greedy
    best-first search. No normalized identity match was found across the 442 AIO and
    130 prior native records; ignored-inclusive text hits in the main checkout were
    prior discovery leads, source citations and search-order contrasts, plus incidental
    lightbulb and wet-bulb dependency substrings, not existing concept records.
  details: 'Width pruning can discard every path to a solution or every optimal path,
    so basic beam search has no general completeness or optimality guarantee. A layer-width
    bound does not by itself bound all memory: stored predecessor information, retained
    earlier layers, generated successors and any global duplicate table must also
    be accounted for. Ranking, ties, goal stopping and duplicate handling are additional
    choices. Increasing the beam width does not guarantee an improvement in returned
    solution quality for every implementation and problem.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined search procedure, not a trained checkpoint, task or benchmark
      score.
    evidence_ids:
    - beamsearch-0
    - beamsearch-1
  - name: aio-mapping
    value: explicit no-match
    definition: Six exact AIO targets were examined and rejected for scope mismatches
      in the pinned snapshot.
    evidence_ids:
    - mapping
    - identity
- assessment_id: globalfrontierbeamsearch
  area: evidence
  topic: Pruning scope, backtracking policy, resource assumptions and AIO no-match
    assessment
  outcome: supported
  target_ids:
  - AIMech:GlobalFrontierBeamSearch
  evidence_ids:
  - identity
  - mapping
  - globalfrontierbeamsearch-0
  - globalfrontierbeamsearch-1
  - globalfrontierbeamsearch-2
  summary: 'The qualified name identifies the global frontier truncation described
    in the 2005 and 2010 search papers. The unqualified phrase best-first beam search
    is intentionally not an identity alias: Meister, Vieira and Cotterell use that
    phrase in 2020 for a decoding procedure with a per-sequence-length path limit.
    A shared name does not equate those pruning rules. No normalized identity match
    was found across the 442 AIO and 130 prior native records; ignored-inclusive text
    hits in the main checkout were prior discovery leads, source citations and search-order
    contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing
    concept records.'
  details: Global frontier pruning can permanently remove a needed path; the cap alone
    establishes neither completeness nor optimality. The cap applies to the open frontier,
    not automatically to closed tables, predecessor storage, generated successors
    or the total program memory. No equivalence to breadth-first beam output, monotonic
    quality with larger width, or universal runtime advantage is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined search procedure, not a trained checkpoint, task or benchmark
      score.
    evidence_ids:
    - globalfrontierbeamsearch-0
    - globalfrontierbeamsearch-1
    - globalfrontierbeamsearch-2
  - name: aio-mapping
    value: explicit no-match
    definition: Six exact AIO targets were examined and rejected for scope mismatches
      in the pinned snapshot.
    evidence_ids:
    - mapping
    - identity
- assessment_id: beamstacksearch
  area: evidence
  topic: Pruning scope, backtracking policy, resource assumptions and AIO no-match
    assessment
  outcome: supported
  target_ids:
  - AIMech:BeamStackSearch
  evidence_ids:
  - identity
  - mapping
  - beamstacksearch-0
  - beamstacksearch-1
  summary: Beam-stack search combines breadth-first beam expansion with chronological
    backtracking and an incumbent solution-cost bound. It is distinct from permanent
    beam pruning, limited-discrepancy beam backtracking, and the separately named
    iterative-deepening BSIDA-star variant. No normalized identity match was found
    across the 442 AIO and 130 prior native records; ignored-inclusive text hits in
    the main checkout were prior discovery leads, source citations and search-order
    contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing
    concept records.
  details: The paper’s termination and optimality argument assumes finite branching,
    a positive lower bound on operator cost and a finite initial upper bound supplied
    by an actual solution, together with admissible pruning. It is not a guarantee
    for arbitrary zero-cost cycles, an infinite bound or arbitrary duplicate policies.
    Ties require a consistent ordering, or enough beam capacity to retain the unbroken
    tie group; a bare numeric range with unresolved ties is insufficient. The baseline
    retains up to a beam of nodes per depth layer plus the beam stack. O(w*d) node
    storage does not mean a fixed total-memory cap independent of search depth. The
    initially supplied solution must remain available if no improvement is found.
    An upper-bound number alone is not a returned path; this record does not certify
    the displayed pseudocode as a complete implementation.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined search procedure, not a trained checkpoint, task or benchmark
      score.
    evidence_ids:
    - beamstacksearch-0
    - beamstacksearch-1
  - name: aio-mapping
    value: explicit no-match
    definition: Six exact AIO targets were examined and rejected for scope mismatches
      in the pinned snapshot.
    evidence_ids:
    - mapping
    - identity
- assessment_id: divideconquerbeamstacksearch
  area: evidence
  topic: Pruning scope, backtracking policy, resource assumptions and AIO no-match
    assessment
  outcome: supported
  target_ids:
  - AIMech:DivideConquerBeamStackSearch
  evidence_ids:
  - identity
  - mapping
  - divideconquerbeamstacksearch-0
  - divideconquerbeamstacksearch-1
  summary: DCBSS is the divide-and-conquer implementation of beam-stack search described
    by Zhou and Hansen. Unlike divide-and-conquer beam search without backtracking,
    it retains beam-stack range information that permits previously discarded layers
    to be regenerated and searched further. No normalized identity match was found
    across the 442 AIO and 130 prior native records; ignored-inclusive text hits in
    the main checkout were prior discovery leads, source citations and search-order
    contrasts, plus incidental lightbulb and wet-bulb dependency substrings, not existing
    concept records.
  details: 'Four retained node layers do not imply constant total storage: the beam
    stack still has depth-dependent entries, and path output, temporary successors
    and reconstruction state also require memory. Discarding layers trades storage
    for regeneration and reconstruction work; no universal runtime improvement is
    implied. The underlying beam-stack pruning, tie handling and bounded-search assumptions
    still matter. Layered duplicate detection must be matched to the graph setting;
    the paper distinguishes directed and undirected behavior. The paper summarizes
    recursive solution recovery and refers to earlier work for implementation details.
    This record supports the described mechanism, not a complete executable reconstruction
    implementation.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined search procedure, not a trained checkpoint, task or benchmark
      score.
    evidence_ids:
    - divideconquerbeamstacksearch-0
    - divideconquerbeamstacksearch-1
  - name: aio-mapping
    value: explicit no-match
    definition: Six exact AIO targets were examined and rejected for scope mismatches
      in the pinned snapshot.
    evidence_ids:
    - mapping
    - identity
- assessment_id: bulb
  area: evidence
  topic: Pruning scope, backtracking policy, resource assumptions and AIO no-match
    assessment
  outcome: supported
  target_ids:
  - AIMech:BULB
  evidence_ids:
  - identity
  - mapping
  - bulb-0
  - bulb-1
  - bulb-2
  summary: BULB denotes Furcy and Koenig’s Beam search Using Limited discrepancy Backtracking.
    A discrepancy selects a nonpreferred successor slice; it is not a numerical heuristic
    error or an action cost. The inspected algorithm is presented for unit-cost state-space
    search and seeks a path, not necessarily a shortest path. No normalized identity
    match was found across the 442 AIO and 130 prior native records; ignored-inclusive
    text hits in the main checkout were prior discovery leads, source citations and
    search-order contrasts, plus incidental lightbulb and wet-bulb dependency substrings,
    not existing concept records.
  details: 'Completeness is conditional on enough memory to store a beam along a solution
    path. A fixed memory budget and arbitrary beam width do not guarantee solving
    every instance. The method need not return a shortest path. An anytime extension
    is discussed separately from the base procedure. The O(B*d) storage statement
    concerns retained slices along the active search; temporary successor generation,
    heuristic data and other implementation storage need separate accounting. The
    active hash table prevents cycles involving retained states and some transpositions,
    but it is not a permanent global closed list of every state ever visited. Figure
    4 has an apparent depth-label inconsistency: nextSlice labels a successor with
    depth although the caller next probes depth+1. The prose describes a next-level
    slice. This record follows that described mechanism and does not certify the literal
    pseudocode as executable.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined search procedure, not a trained checkpoint, task or benchmark
      score.
    evidence_ids:
    - bulb-0
    - bulb-1
    - bulb-2
  - name: aio-mapping
    value: explicit no-match
    definition: Six exact AIO targets were examined and rejected for scope mismatches
      in the pinned snapshot.
    evidence_ids:
    - mapping
    - identity
- assessment_id: alias-provenance
  area: identity
  topic: Evidence for the short BSS alias
  outcome: supported
  target_ids:
  - AIMech:BeamStackSearch
  evidence_ids:
  - alias-evidence
  - alias-resolution
  - beamstacksearch-0
  summary: The optional unsupported BSS alias is absent from both current alias lists;
    the supported full name and stable local ID remain.
  details: The only saved same-key predecessor was verified across all hidden/ignored-inclusive
    bundles. Its affected target is retained. The resolution removes an unsubstantiated
    assertion without claiming that no outside source ever uses this abbreviation.
- assessment_id: adversarial-scope
  area: scope
  topic: Counterexamples to unconditional width, memory and completeness claims
  outcome: supported
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  evidence_ids:
  - beamsearch-1
  - globalfrontierbeamsearch-2
  - beamstacksearch-0
  - beamstacksearch-1
  - divideconquerbeamstacksearch-0
  - bulb-1
  - bulb-2
  summary: The records distinguish a layer cap from a whole-frontier cap and from
    NLP per-length counters, retain beam-stack incumbent/tie assumptions, do not turn
    four retained layers into constant total storage, and qualify BULB completeness
    by memory.
  details: The BSS initial-incumbent obligation is explicit curator inference. BULB’s
    apparent printed depth-label inconsistency is documented rather than silently
    corrected. BSIDA-star is deferred because its short contour description leaves
    a progress boundary unresolved. No benchmark result or executable correctness
    certificate is asserted.
findings:
- finding_id: unsupported-short-alias
  issue_key: aimech-beam-stack-unsubstantiated-alias
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  target_ids:
  - AIMech:BeamStackSearch
  field_paths:
  - aliases
  - entries[id=AIMech:BeamStackSearch].aliases
  evidence_ids:
  - alias-evidence
  - beamstacksearch-0
  - alias-resolution
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BeamStackSearch.yaml
    role: maintained_record
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261011T060240Z-beam-search.json
    role: discovery_report
  title: Remove the unsubstantiated BSS identity alias
  description: The draft asserts BSS although the inspected sources only establish
    the full beam-stack name and DCBSS for the separate divide-and-conquer variant.
    Remove this optional unsupported alias. The finding does not claim the abbreviation
    is absent from all literature and does not dispute the core algorithm identity.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/27
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261011T060506Z-beam-search-open
    finding_id: unsupported-short-alias
  disposition_reason: Removed BSS from the record and mirrored discovery entry, re-read
    current bytes, reinspected hashes, passed the required final checks and verified
    the only saved predecessor and its full affected-target union across hidden and
    ignored files. Core identity and scientific claims remain unchanged.
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:BeamSearch
  - AIMech:GlobalFrontierBeamSearch
  - AIMech:BeamStackSearch
  - AIMech:DivideConquerBeamStackSearch
  - AIMech:BULB
  evidence_ids:
  - identity
  - mapping
  - beamsearch-0
  - beamsearch-1
  - globalfrontierbeamsearch-0
  - globalfrontierbeamsearch-1
  - globalfrontierbeamsearch-2
  - beamstacksearch-0
  - beamstacksearch-1
  - divideconquerbeamstacksearch-0
  - divideconquerbeamstacksearch-1
  - bulb-0
  - bulb-1
  - bulb-2
  - alias-evidence
  rationale: Layer-based pruning, global frontier truncation, chronological range
    backtracking, layer regeneration with relay reconstruction, and discrepancy-budget
    beam backtracking are different procedures. Shared names or beam terminology do
    not justify lumping them. The short alias defect is removable without changing
    concept boundaries.
limitations:
- Adversarial author self-review, not independent approval; all five records remain
  DRAFT.
- BULB’s apparent depth-label inconsistency is a source caveat, not an asserted corrected
  implementation. Targeted searches did not establish a primary erratum.
- Preserving an initial beam-stack incumbent is explicit curator inference from the
  source initialization and return logic.
- For this cohort, 2020 NLP evidence is limited to PDF pp. 1–4 for name disambiguation.
  Subsequent proofs and scoring variants are being researched separately, without
  importing their guarantees into these records.
- Repeated source identifiers for different passages of the same paper do not represent
  independent studies.
- Memory statements distinguish node layers, depth-dependent metadata, temporary successors
  and other implementation storage.
- No puzzle solving, benchmark execution, complete proof certification or implementation
  audit was performed.
- All required structural checks passed; discovery remains ongoing with older and
  new pending candidates.
- The first unsaved predecessor draft failed schema validation because an external
  issue was represented numerically; the URL string was used before saving. No immutable
  review was overwritten.
- The alias correction is supported by inspected-source coverage, not proof that the
  abbreviation is never used in other literature. GitHub closure awaits the authorized
  PR merge.
tags:
- native-concepts
- beam-search
- self-review
- primary-papers
- discovery-ongoing
```
