# Scientific self-review of SAT random-walk extensions and IHSAT

- Review: 20261011T160058Z-sat-walk-extension
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T15:57:48Z
- Finished UTC: 2026-10-11T16:00:58Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Novelty+, the1999 R-Novelty+ and IHSAT as distinct DRAFT concepts with bounded AIO no-match assessments. The records preserve per-step random-walk conditions, the absence of the old periodic override, source-version boundaries and indifferent candidate selection. No actionable curation finding remains in the declared scope.

## Scope And Provenance

All fields of three maintained random-walk-extension and indifferent-history SAT concepts.

Selection: Exact three IDs in the saved ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 4144970eaf42142f7b7efe209f85025999563c2d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NoveltyPlus | data/curated/NoveltyPlus.yaml | maintained | Novelty+ SAT heuristic |
| AIMech:RNoveltyPlus | data/curated/RNoveltyPlus.yaml | maintained | R-Novelty+ SAT heuristic |
| AIMech:IHSAT | data/curated/IHSAT.yaml | maintained | IHSAT |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 110.25s (0:01:50)<br>Checked 442 record(s); 0 failed.<br>Checked 328 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 89 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 87,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT | Command exited0 with no output. |
| Finite sat-walk-extension boundary examples | passed | True | AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT | {"ihsat_nondecreasing_choice": "b", "hsat_best_choice": "a", "ihsat_all_negative_choice": "b", "declared_walk_probability": "1/100", "first_step_y_probability": "1/300", "three_random_step_monotone_path_probability": "1/12000000", "conservative_five_step_success_lower_bound": "1/18895680000000000", "interpretation": "The three-step probability counts only the two monotone all-random paths through y,z1,z2 to the known F2 model; other algorithm trajectories are omitted. The five-step value is the theorem\u2019s conservative bound, not measured success or expected runtime. A per-step walk branch can expose y immediately, unlike the previously declared periodic phase. IHSAT can prefer a neutral or more-worsening older candidate."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:NoveltyPlus.

This is Hoos’s 1999 Novelty+ random-walk extension. The plus sign identifies an additional per-step random-walk branch, distinct from Novelty’s conditional noise parameter and from later adaptive, diversification or look-ahead variants. It does not require a periodic schedule or an SKC zero-break priority. The theorem concerns asymptotic model finding on satisfiable formulas, not probably-approximately-correct learning or a finite UNSAT decision. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 90 and 90 lines respectively. All 64 unique hit contents were inspected: neighboring variant and source references, saved reviews and candidate leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a complete truth assignment and variable flip timestamps. If the formula is not satisfied, randomly choose an unsatisfied clause. With fixed probability w in [0,1], choose a variable uniformly from that clause and flip it. Otherwise rank clause variables by the global post-flip violation count, breaking score ties in favor of the least recently flipped variable. If the best is not the most recently flipped variable in the clause, select it; otherwise select second-best with probability p and best with probability 1−p, where p is in [0,1]. Update the flipped variable’s timestamp and continue under the declared stopping policy. The walk branch is available regardless of scores, recency or zero-break candidates. With w=1 this is the pure clause-first random walk; with w=0 it is the underlying Novelty selector. Any fixed w&gt;0 satisfies the source’s random-walk premise once all remaining move cases are well-defined. For a finite satisfiable CNF and a well-defined remaining move policy, a fixed positive lower bound on the probability of a uniform random-clause/random-variable step at every search step gives success probability approaching one as the number of steps tends to infinity. Hoos1999 Theorem 2 establishes this via a positive probability of a sequence reducing Hamming distance to a model. The conclusion does not give a polynomial or practically small runtime, a finite-run guarantee, or an UNSAT certificate. Limits: The asymptotic guarantee requires a strictly positive walk probability at every step, bounded below independently of elapsed search history. A scheduled-only override or a probability that tends to zero does not automatically satisfy that premise. At w=0 the random-walk argument no longer applies. The guarantee concerns finding a model on a finite satisfiable formula in the limit of continued search. A finite budget can miss an existing model and cannot certify UNSAT. The source’s lower bound can be extremely small; no polynomial or practical runtime follows. The walk probability w is separate from the inner selector’s noise parameter p. The reported experimental w=0.01 is not a defining or universally optimal constant. Optional outer restarts and cutoffs must be specified separately. Empty clauses, unit clauses lacking a second candidate, initial age ties, duplicate literals and timestamp/reset conventions require a well-defined implementation. The general random-walk proof does not certify undocumented choices in the short selector description. No author solver or benchmark was executed.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:RNoveltyPlus.

The record is scoped to Hoos’s 1999 R-Novelty+ definition. It removes the original every-100-step override, rather than adding a random-walk branch while silently retaining that schedule. The 2004 competition report uses Rnovelty+ for a periodic configuration; that differently specified variant is not the present identity. At zero walk probability this method reduces to the core R-Novelty selector without the 1997 periodic escape, not the entire original 1997 strategy. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 90 and 90 lines respectively. All 64 unique hit contents were inspected: neighboring variant and source references, saved reviews and candidate leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Randomly select an unsatisfied clause. With fixed walk probability w in [0,1], choose a variable uniformly from that clause and flip it. Otherwise apply the core R-Novelty selector: rank candidates by global post-flip violation count with oldest-variable tie breaks. Choose the best if it is not the most recently flipped variable in the clause. If it is most recent, let d be the second-best count minus the best count, with d&gt;=1 under the stated age/score assumptions, and use inner noise p in [0,1]. For p&lt;0.5 choose second-best with probability 2p when d=1 and with probability zero when d&gt;1. For p&gt;=0.5 choose second-best with probability one when d=1 and with probability 2(p−0.5) when d&gt;1. Choose best otherwise. Update the timestamp of the flipped variable. Omit the periodic every-100-step override: the new walk coin is evaluated at each step. A fixed w&gt;0 supports the source’s asymptotic result; w=1 gives pure clause-first random walk and w=0 retains only the core selector. For a finite satisfiable CNF and a well-defined remaining move policy, a fixed positive lower bound on the probability of a uniform random-clause/random-variable step at every search step gives success probability approaching one as the number of steps tends to infinity. Hoos1999 Theorem 2 establishes this via a positive probability of a sequence reducing Hamming distance to a model. The conclusion does not give a polynomial or practically small runtime, a finite-run guarantee, or an UNSAT certificate. Hoos1999 explicitly removes the periodic escape when defining R-Novelty+, while the 2004 competition report calls an every-100-step configuration Rnovelty+. This record follows the former definition and does not treat the latter’s cycling-prevention statement as its theorem. Limits: The asymptotic guarantee requires a strictly positive walk probability at every step, bounded below independently of elapsed search history. A scheduled-only override or a probability that tends to zero does not automatically satisfy that premise. At w=0 the random-walk argument no longer applies. The guarantee concerns finding a model on a finite satisfiable formula in the limit of continued search. A finite budget can miss an existing model and cannot certify UNSAT. The source’s lower bound can be extremely small; no polynomial or practical runtime follows. The walk probability w is separate from the inner selector’s noise parameter p. The reported experimental w=0.01 is not a defining or universally optimal constant. Optional outer restarts and cutoffs must be specified separately. Empty clauses, unit clauses lacking a second candidate, initial age ties, duplicate literals and timestamp/reset conventions require a well-defined implementation. The general random-walk proof does not certify undocumented choices in the short selector description. No author solver or benchmark was executed. The asymptotic guarantee for the 1999 per-step extension must not be transferred to the 2004 periodic configuration merely because both use a plus label. The previously proved trapping example shows why scheduled random steps can miss an essential variable.

### Identity, definition, mechanism, limitations, provenance and explicit AIO assessment

evidence: supported. Targets: AIMech:IHSAT.

IHSAT combines ISAT’s indifferent candidate-set rule with HSAT’s history-based picking rule in Gent and Walsh’s 1993 paper. It is not merely another name for greedy HSAT: a neutral old candidate can be selected while a positive-gain candidate exists, and when every move worsens the score, age selection can choose a move worse than the least-decreasing alternative. Memory is scoped to the current attempt and does not impose a tabu prohibition. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 90 and 90 lines respectively. All 64 unique hit contents were inspected: neighboring variant and source references, saved reviews and candidate leads, not existing candidate records. Exact checkout counts and differences are retained in the ledger. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and five full native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Begin a GSAT/GenSAT attempt with a random complete assignment and fresh attempt-local flip history. If the formula is not satisfied, compute each variable’s gain in satisfied-clause count if flipped. If any gain is nonnegative, make every variable with gain at least zero a candidate, without favoring a larger improvement over a neutral flip. If all gains are negative, make every variable a candidate. From this pool choose the one whose last flip in the current attempt was longest ago; treat never-flipped variables as oldest and break their ties with a fixed arbitrary ordering, as in HSAT. Flip it, update its timestamp and repeat within the selected attempt budget. New attempts retain the GSAT initialization behavior and reset the current-attempt history. Limits: The fallback pool when all gains are negative contains all variables; it is not restricted to least-worsening moves. Replacing the nonnegative pool with only maximum-gain candidates yields a different rule. The oldest-variable selector is deterministic once the current attempt and fixed ordering are specified, but initialization remains randomized. A rule excluding recent moves for a tenure would introduce tabu behavior not required by IHSAT. The 1993 evidence is empirical. No completeness, polynomial runtime or universal superiority is established by the inspected method description, and no numerical benchmark claim is curated. The GenSAT loop checks satisfaction before each flip; exact final-flip return handling and budget boundaries must be declared in an implementation. Finite failure is not an UNSAT certificate. No author solver was executed.

### Per-step walk coin and conditional Novelty selector

consistency: supported. Targets: AIMech:NoveltyPlus.

Retain the plus extension with separate walk and selector parameters.

The1999 method makes the random clause-variable branch available at every step, irrespective of the best candidate’s recency or score. Its w parameter differs from the inner Novelty p coin. At w=0 the original selector remains; at w=1 the pure clause-first walk remains. Fixed w&gt;0 gives the source’s asymptotic guarantee under well-defined move rules, not a finite success or practical runtime guarantee.

### Removing the periodic override and retaining the core score-gap rule

consistency: supported. Targets: AIMech:RNoveltyPlus.

Retain the1999 definition and keep the2004 plus convention distinct.

The1999 paper explicitly omits the every100-step escape when defining R-Novelty+. The nonwalk branch uses the complete1997 four-case score-gap rule; w=0 therefore yields only that core, not the whole original periodic strategy. The2004 report labels a periodic configuration with the plus name, so its naming and cycling claim are not adopted. Finite F2 path calculations show positive per-step escape possibilities without pretending to benchmark the full solver.

### Indifferent candidate pool followed by age-based picking

consistency: supported. Targets: AIMech:IHSAT.

Retain IHSAT as distinct from greedy HSAT.

ISAT offers every nonnegative-gain variable, falling back to all variables when none qualify. IHSAT uses HSAT’s oldest-in-current-try pick rule on that pool. The finite examples select a neutral variable despite an improving alternative and select a more-worsening variable when all moves worsen. Neither maximum-gain filtering nor tabu exclusion is silently imposed. Random starts, attempt-local history and finite-failure limits remain explicit.

### SAT random exploration and history versus neural or learned models

grounding: supported. Targets: AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT.

Retain three native concepts with bounded no-match assessments.

Nine exact AIO CLASS nodes were read in the preceding batch and recaptured unchanged with definitions, scoped synonyms/comments and outgoing edges. The same bounded SAT/search/memory neighborhood applies: random-walk exploration and age bookkeeping do not make neural memory, a language model, a training strategy or a learned action-value method. Three native concepts receive bounded no-match assessments. Five complete neighbors distinguish HSAT’s greedy candidate set, original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie priority; their older mapping dispositions remain context rather than a new approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NoveltyPlus, AIMech:RNoveltyPlus, AIMech:IHSAT. Novelty+ and R-Novelty+ retain different nonwalk selectors, while IHSAT changes its global candidate pool and selects by age. The plus methods share a per-step walk extension but are not identical algorithms; the1999 and2004 plus conventions remain separate.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T155702Z-sat-walk-extension.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases; no normalized identity match. Both full-checkout text searches included ignored and hidden files, and every unique hit content was inspected. Matches were neighboring variant/source references, saved reviews and candidate leads, not existing candidate records. Exact per-checkout counts, paths and output hashes are preserved. Nine exact AIO nodes and five complete native neighbors were inspected; absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Nine exact CLASS nodes with scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Nine exact AIO CLASS nodes were read in the preceding batch and recaptured unchanged with definitions, scoped synonyms/comments and outgoing edges. The same bounded SAT/search/memory neighborhood applies: random-walk exploration and age bookkeeping do not make neural memory, a language model, a training strategy or a learned action-value method. Three native concepts receive bounded no-match assessments. Five complete neighbors distinguish HSAT’s greedy candidate set, original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie priority; their older mapping dispositions remain context rather than a new approval. |
| neighbors | research/discovery/20261011T155702Z-sat-walk-extension.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Full HSAT, Novelty, RNovelty, GSATWithRandomWalk and WalkSAT records distinguish greedy candidate sets, original recency/gap selectors, focused GSAT noise and SKC break/freebie priority. Their prior mappings are contextual, not newly approved. |
| finite-conventions | research/discovery/sat-walk-extension-boundaries.py; calculate(): IHSAT nonnegative/all-negative candidate pools, monotone random paths in F2 and a conservative theorem-bound substitution | supports | Original finite substitutions show IHSAT choosing a neutral old candidate over an improving alternative and its all-negative fallback choosing a more-worsening move. On Hoos1999’s published F2, two monotone all-random paths reach the model with positive probability under a per-step walk coin. The conservative theorem-bound substitution is not measured success, a complete solver implementation or a general complexity proof. |
| noveltyplus-source-0 | https://cdn.aaai.org/AAAI/1999/AAAI99-094.pdf; PDF3, Definition 2 and no-restart scope; PDF3–4, Lemma 1 and Theorem 2; PDF5–6, application to the plus extensions; PDF5–6, Improving SLS Performance, per-step random-walk extension and naming; PDF2, WalkSAT/Novelty context; PDF3–4, asymptotic scope and Theorem 2 | supports | On the Run-time Behaviour of Stochastic Local Search Algorithms for SAT. Six-page AAAI-99 publisher PDF with proceedings banner and 1999 copyright. The pages have no printed proceedings numbers; locators use PDF pages. This file differs in bytes from the UBCSAT archive copy, and all six publisher page images were inspected directly. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| noveltyplus-source-1 | https://cdn.aaai.org/AAAI/1997/AAAI97-050.pdf; PDF2 / printed322, Novelty and R-Novelty selector definitions; PDF3 / printed323, original periodic R-Novelty override | supports | Evidence for Invariants in Local Search. Six-page AAAI-97 proceedings scan from the publisher, pp.321–326. The 1997 R-Novelty description includes a periodic random clause-variable flip every 100 moves. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| rnoveltyplus-source-0 | https://cdn.aaai.org/AAAI/1999/AAAI99-094.pdf; PDF3, Definition 2 and no-restart scope; PDF3–4, Lemma 1 and Theorem 2; PDF5–6, application to the plus extensions; PDF5–6, per-step walk and omission of periodic override; PDF5–6, random-walk extension and explicit removal of R-Novelty’s periodic override; PDF3–4, asymptotic scope and Theorem 2; PDF4–5, periodic strategy incompleteness | supports | On the Run-time Behaviour of Stochastic Local Search Algorithms for SAT. Six-page AAAI-99 publisher PDF with proceedings banner and 1999 copyright. The pages have no printed proceedings numbers; locators use PDF pages. This file differs in bytes from the UBCSAT archive copy, and all six publisher page images were inspected directly. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| rnoveltyplus-source-1 | https://cdn.aaai.org/AAAI/1997/AAAI97-050.pdf; PDF2 / printed322, Novelty and R-Novelty selector definitions; PDF3 / printed323, original periodic R-Novelty override | supports | Evidence for Invariants in Local Search. Six-page AAAI-97 proceedings scan from the publisher, pp.321–326. The 1997 R-Novelty description includes a periodic random clause-variable flip every 100 moves. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| rnoveltyplus-source-2 | https://www.cs.virginia.edu/~rmw7my/papers/walksat.pdf; PDF/printed2, periodic configuration and plus naming | supports | Walksat in the 2004 SAT Competition. Two-page author-hosted SAT Competition 2004 solver description, printed/PDF pp.1–2. Defines the SKC rule and distinguishes AutoWalksat and Rnovelty+; this is not documentation for every later software version. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |
| ihsat-source-0 | https://cdn.aaai.org/AAAI/1993/AAAI93-005.pdf; PDF2 / printed29, ISAT candidate-set definition; PDF4 / printed31, IHSAT combining indifferent hill-climbing with HSAT picking; PDF1 / printed28, GenSAT outer loop | supports | Towards an Understanding of Hill-climbing Procedures for SAT. Six-page AAAI-93 proceedings scan from the publisher, pp.28–33. This is distinct from the fourteen-page draft hosted in the UBCSAT archive; printed and PDF page locators refer to this publisher version. Actual paper and HTML reading scopes are declared in source_analysis; extraction, rendering and a full-text access label do not establish that every page was read. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- Asymptotic model finding requires the declared fixed positive per-step random-walk premise and well-defined move rules. It is not a finite UNSAT test, a polynomial bound or a practical runtime guarantee.
- The1999 R-Novelty+ removes the old periodic override; the2004 plus convention remains distinct. Unit clauses and initial age/reset conventions are not silently invented.
- All six pages of the1999 publisher PDF were visually inspected; the1993,1997 and2004 sources retain their declared prior page scopes. No author implementation or numerical benchmark was executed.
- There are 186 pending inspection leads plus unresolved dispositions; discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T160058Z-sat-walk-extension
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of SAT random-walk extensions and IHSAT
started_at: '2026-10-11T15:57:48Z'
finished_at: '2026-10-11T16:00:58Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all new fields against
    primary method sections, critical PDF images, nine exact AIO nodes, five full
    neighboring records and original finite counterexamples. Separate walk/selector
    parameters, the uniform positive random-walk premise, removal of the old periodic
    schedule and IHSAT candidate-pool boundaries were preserved before record creation.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Novelty+, the1999 R-Novelty+ and IHSAT as distinct DRAFT concepts
  with bounded AIO no-match assessments. The records preserve per-step random-walk
  conditions, the absence of the old periodic override, source-version boundaries
  and indifferent candidate selection. No actionable curation finding remains in the
  declared scope.
source:
  git_revision: 4144970eaf42142f7b7efe209f85025999563c2d
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
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
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/GSATWithRandomWalk.yaml
    sha256: 5d63a89898da6fa4b60fd75387c72505f9390a3bba23aa423a7e2de3f6eed27b
    role: context
  - path: data/curated/HSAT.yaml
    sha256: 9593d9a6fdebaada6f45ae32fa136bc5c7ad08ebbd546d9e2a82f0c8e2354045
    role: context
  - path: data/curated/IHSAT.yaml
    sha256: 2763ce1104880118f9e5edcade6fc49919860caad813352a7f5c7ab0a00f41ef
    role: target
  - path: data/curated/Novelty.yaml
    sha256: 6a85c443510cb4ecee4dbe2f4a5b43e87c53c8e0f3c11142dc81a6419a6feee5
    role: context
  - path: data/curated/NoveltyPlus.yaml
    sha256: a019ef5bec6faf42ce64e3cbc2f7d3388832c103505e9635f213ccfd1a4f5a75
    role: target
  - path: data/curated/RNovelty.yaml
    sha256: ae6b7c18041ad345bf7db44d26a350e7d64d99164b98ac730262490b5c88ba98
    role: context
  - path: data/curated/RNoveltyPlus.yaml
    sha256: c6130d848787664b24ec75a07270c548a644ec7c9ec77b375bde2b0d269e7c03
    role: target
  - path: data/curated/WalkSAT.yaml
    sha256: 7f28176fc24fe30c94bfd14a74304cae1021787abf87ebcfdbde6b19bc11fd23
    role: context
  - path: research/discovery/20261011T155702Z-sat-walk-extension.json
    sha256: 5c964dc121ba49ed43e34c978700ce143113aff1e460d267488b9a7458f44a27
    role: context
  - path: research/discovery/sat-walk-extension-boundaries.py
    sha256: 6afe77c9bb01a4e84d7d2ffd96b073cceb61563b58e920eaafa3402b626f55c0
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
- target_id: AIMech:NoveltyPlus
  path: data/curated/NoveltyPlus.yaml
  label: Novelty+ SAT heuristic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NoveltyPlus.yaml
    role: maintained
- target_id: AIMech:RNoveltyPlus
  path: data/curated/RNoveltyPlus.yaml
  label: R-Novelty+ SAT heuristic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RNoveltyPlus.yaml
    role: maintained
- target_id: AIMech:IHSAT
  path: data/curated/IHSAT.yaml
  label: IHSAT
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IHSAT.yaml
    role: maintained
scope:
  description: All fields of three maintained random-walk-extension and indifferent-history
    SAT concepts.
  selection: Exact three IDs in the saved ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  exclusions:
  - target: Uninspected frontier leads and complete executable implementations
    reason: The batch does not exhaust SAT search or execute original solvers. Other
      GenSAT and UBCSAT variants, tuning invariants and GWSAT source reconciliation
      remain frontier leads.
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
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 110.25s (0:01:50)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 328 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 89 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 87,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
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
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
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
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Finite sat-walk-extension boundary examples
  command: python3 research/discovery/sat-walk-extension-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  exit_code: 0
  expected_exit_code: 0
  summary: '{"ihsat_nondecreasing_choice": "b", "hsat_best_choice": "a", "ihsat_all_negative_choice":
    "b", "declared_walk_probability": "1/100", "first_step_y_probability": "1/300",
    "three_random_step_monotone_path_probability": "1/12000000", "conservative_five_step_success_lower_bound":
    "1/18895680000000000", "interpretation": "The three-step probability counts only
    the two monotone all-random paths through y,z1,z2 to the known F2 model; other
    algorithm trajectories are omitted. The five-step value is the theorem\u2019s
    conservative bound, not measured success or expected runtime. A per-step walk
    branch can expose y immediately, unlike the previously declared periodic phase.
    IHSAT can prefer a neutral or more-worsening older candidate."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T155702Z-sat-walk-extension.json
  accessed_at: '2026-10-11T15:57:48Z'
  support: supports
  summary: Compared all 442 pinned AIO labels/scoped synonyms and 325 preceding native
    IDs/names/aliases; no normalized identity match. Both full-checkout text searches
    included ignored and hidden files, and every unique hit content was inspected.
    Matches were neighboring variant/source references, saved reviews and candidate
    leads, not existing candidate records. Exact per-checkout counts, paths and output
    hashes are preserved. Nine exact AIO nodes and five complete native neighbors
    were inspected; absence is bounded to this snapshot and semantic neighborhood.
  search_scope: All 442 pinned AIO labels/scoped synonyms and 325 preceding maintained
    IDs/names/aliases; both full checkouts including ignored and hidden files. Every
    unique hit content inspected; matches were neighboring variant/source references,
    saved reviews and candidate leads. Exact counts, paths and differences remain
    in the ledger.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Nine exact CLASS nodes with scoped synonyms/comments/outgoing edges in
    source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T15:57:48Z'
  support: supports
  summary: 'Nine exact AIO CLASS nodes were read in the preceding batch and recaptured
    unchanged with definitions, scoped synonyms/comments and outgoing edges. The same
    bounded SAT/search/memory neighborhood applies: random-walk exploration and age
    bookkeeping do not make neural memory, a language model, a training strategy or
    a learned action-value method. Three native concepts receive bounded no-match
    assessments. Five complete neighbors distinguish HSAT’s greedy candidate set,
    original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie
    priority; their older mapping dispositions remain context rather than a new approval.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T155702Z-sat-walk-extension.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T15:57:48Z'
  support: supports
  summary: Full HSAT, Novelty, RNovelty, GSATWithRandomWalk and WalkSAT records distinguish
    greedy candidate sets, original recency/gap selectors, focused GSAT noise and
    SKC break/freebie priority. Their prior mappings are contextual, not newly approved.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/sat-walk-extension-boundaries.py
  locator: 'calculate(): IHSAT nonnegative/all-negative candidate pools, monotone
    random paths in F2 and a conservative theorem-bound substitution'
  accessed_at: '2026-10-11T15:57:48Z'
  snapshot_sha256: 6afe77c9bb01a4e84d7d2ffd96b073cceb61563b58e920eaafa3402b626f55c0
  support: supports
  summary: Original finite substitutions show IHSAT choosing a neutral old candidate
    over an improving alternative and its all-negative fallback choosing a more-worsening
    move. On Hoos1999’s published F2, two monotone all-random paths reach the model
    with positive probability under a per-step walk coin. The conservative theorem-bound
    substitution is not measured success, a complete solver implementation or a general
    complexity proof.
- evidence_id: noveltyplus-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1999/AAAI99-094.pdf
  locator: PDF3, Definition 2 and no-restart scope; PDF3–4, Lemma 1 and Theorem 2;
    PDF5–6, application to the plus extensions; PDF5–6, Improving SLS Performance,
    per-step random-walk extension and naming; PDF2, WalkSAT/Novelty context; PDF3–4,
    asymptotic scope and Theorem 2
  accessed_at: '2026-10-11T15:47:53Z'
  snapshot_sha256: 6afd11724464cf043880c221fd14f2110176c9e3bdc97cbb0b200ad3de789eb6
  support: supports
  summary: On the Run-time Behaviour of Stochastic Local Search Algorithms for SAT.
    Six-page AAAI-99 publisher PDF with proceedings banner and 1999 copyright. The
    pages have no printed proceedings numbers; locators use PDF pages. This file differs
    in bytes from the UBCSAT archive copy, and all six publisher page images were
    inspected directly. Actual paper and HTML reading scopes are declared in source_analysis;
    extraction, rendering and a full-text access label do not establish that every
    page was read.
- evidence_id: noveltyplus-source-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1997/AAAI97-050.pdf
  locator: PDF2 / printed322, Novelty and R-Novelty selector definitions; PDF3 / printed323,
    original periodic R-Novelty override
  accessed_at: '2026-10-11T15:35:13Z'
  snapshot_sha256: 79821a112c8ca937583164161be118c3ebb9795e5cfa494a55536881233852a8
  support: supports
  summary: Evidence for Invariants in Local Search. Six-page AAAI-97 proceedings scan
    from the publisher, pp.321–326. The 1997 R-Novelty description includes a periodic
    random clause-variable flip every 100 moves. Actual paper and HTML reading scopes
    are declared in source_analysis; extraction, rendering and a full-text access
    label do not establish that every page was read.
- evidence_id: rnoveltyplus-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1999/AAAI99-094.pdf
  locator: PDF3, Definition 2 and no-restart scope; PDF3–4, Lemma 1 and Theorem 2;
    PDF5–6, application to the plus extensions; PDF5–6, per-step walk and omission
    of periodic override; PDF5–6, random-walk extension and explicit removal of R-Novelty’s
    periodic override; PDF3–4, asymptotic scope and Theorem 2; PDF4–5, periodic strategy
    incompleteness
  accessed_at: '2026-10-11T15:47:53Z'
  snapshot_sha256: 6afd11724464cf043880c221fd14f2110176c9e3bdc97cbb0b200ad3de789eb6
  support: supports
  summary: On the Run-time Behaviour of Stochastic Local Search Algorithms for SAT.
    Six-page AAAI-99 publisher PDF with proceedings banner and 1999 copyright. The
    pages have no printed proceedings numbers; locators use PDF pages. This file differs
    in bytes from the UBCSAT archive copy, and all six publisher page images were
    inspected directly. Actual paper and HTML reading scopes are declared in source_analysis;
    extraction, rendering and a full-text access label do not establish that every
    page was read.
- evidence_id: rnoveltyplus-source-1
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1997/AAAI97-050.pdf
  locator: PDF2 / printed322, Novelty and R-Novelty selector definitions; PDF3 / printed323,
    original periodic R-Novelty override
  accessed_at: '2026-10-11T15:35:13Z'
  snapshot_sha256: 79821a112c8ca937583164161be118c3ebb9795e5cfa494a55536881233852a8
  support: supports
  summary: Evidence for Invariants in Local Search. Six-page AAAI-97 proceedings scan
    from the publisher, pp.321–326. The 1997 R-Novelty description includes a periodic
    random clause-variable flip every 100 moves. Actual paper and HTML reading scopes
    are declared in source_analysis; extraction, rendering and a full-text access
    label do not establish that every page was read.
- evidence_id: rnoveltyplus-source-2
  kind: primary_source
  reference: https://www.cs.virginia.edu/~rmw7my/papers/walksat.pdf
  locator: PDF/printed2, periodic configuration and plus naming
  accessed_at: '2026-10-11T15:10:47Z'
  snapshot_sha256: 525f46d2f9fd9d32cc46daee6b15a0ece5fcef17af614e74d6143643ed2cf74f
  support: supports
  summary: Walksat in the 2004 SAT Competition. Two-page author-hosted SAT Competition
    2004 solver description, printed/PDF pp.1–2. Defines the SKC rule and distinguishes
    AutoWalksat and Rnovelty+; this is not documentation for every later software
    version. Actual paper and HTML reading scopes are declared in source_analysis;
    extraction, rendering and a full-text access label do not establish that every
    page was read.
- evidence_id: ihsat-source-0
  kind: primary_source
  reference: https://cdn.aaai.org/AAAI/1993/AAAI93-005.pdf
  locator: PDF2 / printed29, ISAT candidate-set definition; PDF4 / printed31, IHSAT
    combining indifferent hill-climbing with HSAT picking; PDF1 / printed28, GenSAT
    outer loop
  accessed_at: '2026-10-11T15:35:13Z'
  snapshot_sha256: 26ae9ce8d185fd098dceaac939e9eda345c7ae311165d7a8fc014e447a7aff58
  support: supports
  summary: Towards an Understanding of Hill-climbing Procedures for SAT. Six-page
    AAAI-93 proceedings scan from the publisher, pp.28–33. This is distinct from the
    fourteen-page draft hosted in the UBCSAT archive; printed and PDF page locators
    refer to this publisher version. Actual paper and HTML reading scopes are declared
    in source_analysis; extraction, rendering and a full-text access label do not
    establish that every page was read.
assessments:
- assessment_id: noveltyplus
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:NoveltyPlus
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - noveltyplus-source-0
  - noveltyplus-source-1
  summary: 'This is Hoos’s 1999 Novelty+ random-walk extension. The plus sign identifies
    an additional per-step random-walk branch, distinct from Novelty’s conditional
    noise parameter and from later adaptive, diversification or look-ahead variants.
    It does not require a periodic schedule or an SKC zero-break priority. The theorem
    concerns asymptotic model finding on satisfiable formulas, not probably-approximately-correct
    learning or a finite UNSAT decision. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 90 and 90 lines respectively. All 64 unique hit contents were
    inspected: neighboring variant and source references, saved reviews and candidate
    leads, not existing candidate records. Exact checkout counts and differences are
    retained in the ledger. Nine exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and five full native neighboring records were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.'
  details: 'Maintain a complete truth assignment and variable flip timestamps. If
    the formula is not satisfied, randomly choose an unsatisfied clause. With fixed
    probability w in [0,1], choose a variable uniformly from that clause and flip
    it. Otherwise rank clause variables by the global post-flip violation count, breaking
    score ties in favor of the least recently flipped variable. If the best is not
    the most recently flipped variable in the clause, select it; otherwise select
    second-best with probability p and best with probability 1−p, where p is in [0,1].
    Update the flipped variable’s timestamp and continue under the declared stopping
    policy. The walk branch is available regardless of scores, recency or zero-break
    candidates. With w=1 this is the pure clause-first random walk; with w=0 it is
    the underlying Novelty selector. Any fixed w>0 satisfies the source’s random-walk
    premise once all remaining move cases are well-defined. For a finite satisfiable
    CNF and a well-defined remaining move policy, a fixed positive lower bound on
    the probability of a uniform random-clause/random-variable step at every search
    step gives success probability approaching one as the number of steps tends to
    infinity. Hoos1999 Theorem 2 establishes this via a positive probability of a
    sequence reducing Hamming distance to a model. The conclusion does not give a
    polynomial or practically small runtime, a finite-run guarantee, or an UNSAT certificate.
    Limits: The asymptotic guarantee requires a strictly positive walk probability
    at every step, bounded below independently of elapsed search history. A scheduled-only
    override or a probability that tends to zero does not automatically satisfy that
    premise. At w=0 the random-walk argument no longer applies. The guarantee concerns
    finding a model on a finite satisfiable formula in the limit of continued search.
    A finite budget can miss an existing model and cannot certify UNSAT. The source’s
    lower bound can be extremely small; no polynomial or practical runtime follows.
    The walk probability w is separate from the inner selector’s noise parameter p.
    The reported experimental w=0.01 is not a defining or universally optimal constant.
    Optional outer restarts and cutoffs must be specified separately. Empty clauses,
    unit clauses lacking a second candidate, initial age ties, duplicate literals
    and timestamp/reset conventions require a well-defined implementation. The general
    random-walk proof does not certify undocumented choices in the short selector
    description. No author solver or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - noveltyplus-source-0
    - noveltyplus-source-1
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Nine exact AIO CLASS nodes were read in the preceding batch and recaptured
      unchanged with definitions, scoped synonyms/comments and outgoing edges. The
      same bounded SAT/search/memory neighborhood applies: random-walk exploration
      and age bookkeeping do not make neural memory, a language model, a training
      strategy or a learned action-value method. Three native concepts receive bounded
      no-match assessments. Five complete neighbors distinguish HSAT’s greedy candidate
      set, original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie
      priority; their older mapping dispositions remain context rather than a new
      approval.'
    evidence_ids:
    - mapping
- assessment_id: rnoveltyplus
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:RNoveltyPlus
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - rnoveltyplus-source-0
  - rnoveltyplus-source-1
  - rnoveltyplus-source-2
  summary: 'The record is scoped to Hoos’s 1999 R-Novelty+ definition. It removes
    the original every-100-step override, rather than adding a random-walk branch
    while silently retaining that schedule. The 2004 competition report uses Rnovelty+
    for a periodic configuration; that differently specified variant is not the present
    identity. At zero walk probability this method reduces to the core R-Novelty selector
    without the 1997 periodic escape, not the entire original 1997 strategy. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    325 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in worktree and main, returning 90 and 90 lines respectively.
    All 64 unique hit contents were inspected: neighboring variant and source references,
    saved reviews and candidate leads, not existing candidate records. Exact checkout
    counts and differences are retained in the ledger. Nine exact AIO CLASS nodes
    with scoped synonyms/comments and outgoing edges and five full native neighboring
    records were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  details: 'Randomly select an unsatisfied clause. With fixed walk probability w in
    [0,1], choose a variable uniformly from that clause and flip it. Otherwise apply
    the core R-Novelty selector: rank candidates by global post-flip violation count
    with oldest-variable tie breaks. Choose the best if it is not the most recently
    flipped variable in the clause. If it is most recent, let d be the second-best
    count minus the best count, with d>=1 under the stated age/score assumptions,
    and use inner noise p in [0,1]. For p<0.5 choose second-best with probability
    2p when d=1 and with probability zero when d>1. For p>=0.5 choose second-best
    with probability one when d=1 and with probability 2(p−0.5) when d>1. Choose best
    otherwise. Update the timestamp of the flipped variable. Omit the periodic every-100-step
    override: the new walk coin is evaluated at each step. A fixed w>0 supports the
    source’s asymptotic result; w=1 gives pure clause-first random walk and w=0 retains
    only the core selector. For a finite satisfiable CNF and a well-defined remaining
    move policy, a fixed positive lower bound on the probability of a uniform random-clause/random-variable
    step at every search step gives success probability approaching one as the number
    of steps tends to infinity. Hoos1999 Theorem 2 establishes this via a positive
    probability of a sequence reducing Hamming distance to a model. The conclusion
    does not give a polynomial or practically small runtime, a finite-run guarantee,
    or an UNSAT certificate. Hoos1999 explicitly removes the periodic escape when
    defining R-Novelty+, while the 2004 competition report calls an every-100-step
    configuration Rnovelty+. This record follows the former definition and does not
    treat the latter’s cycling-prevention statement as its theorem. Limits: The asymptotic
    guarantee requires a strictly positive walk probability at every step, bounded
    below independently of elapsed search history. A scheduled-only override or a
    probability that tends to zero does not automatically satisfy that premise. At
    w=0 the random-walk argument no longer applies. The guarantee concerns finding
    a model on a finite satisfiable formula in the limit of continued search. A finite
    budget can miss an existing model and cannot certify UNSAT. The source’s lower
    bound can be extremely small; no polynomial or practical runtime follows. The
    walk probability w is separate from the inner selector’s noise parameter p. The
    reported experimental w=0.01 is not a defining or universally optimal constant.
    Optional outer restarts and cutoffs must be specified separately. Empty clauses,
    unit clauses lacking a second candidate, initial age ties, duplicate literals
    and timestamp/reset conventions require a well-defined implementation. The general
    random-walk proof does not certify undocumented choices in the short selector
    description. No author solver or benchmark was executed. The asymptotic guarantee
    for the 1999 per-step extension must not be transferred to the 2004 periodic configuration
    merely because both use a plus label. The previously proved trapping example shows
    why scheduled random steps can miss an essential variable.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - rnoveltyplus-source-0
    - rnoveltyplus-source-1
    - rnoveltyplus-source-2
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Nine exact AIO CLASS nodes were read in the preceding batch and recaptured
      unchanged with definitions, scoped synonyms/comments and outgoing edges. The
      same bounded SAT/search/memory neighborhood applies: random-walk exploration
      and age bookkeeping do not make neural memory, a language model, a training
      strategy or a learned action-value method. Three native concepts receive bounded
      no-match assessments. Five complete neighbors distinguish HSAT’s greedy candidate
      set, original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie
      priority; their older mapping dispositions remain context rather than a new
      approval.'
    evidence_ids:
    - mapping
- assessment_id: ihsat
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and explicit AIO
    assessment
  outcome: supported
  target_ids:
  - AIMech:IHSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - ihsat-source-0
  summary: 'IHSAT combines ISAT’s indifferent candidate-set rule with HSAT’s history-based
    picking rule in Gent and Walsh’s 1993 paper. It is not merely another name for
    greedy HSAT: a neutral old candidate can be selected while a positive-gain candidate
    exists, and when every move worsens the score, age selection can choose a move
    worse than the least-decreasing alternative. Memory is scoped to the current attempt
    and does not impose a tabu prohibition. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 325 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 90 and 90 lines respectively. All 64 unique hit contents were
    inspected: neighboring variant and source references, saved reviews and candidate
    leads, not existing candidate records. Exact checkout counts and differences are
    retained in the ledger. Nine exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and five full native neighboring records were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.'
  details: 'Begin a GSAT/GenSAT attempt with a random complete assignment and fresh
    attempt-local flip history. If the formula is not satisfied, compute each variable’s
    gain in satisfied-clause count if flipped. If any gain is nonnegative, make every
    variable with gain at least zero a candidate, without favoring a larger improvement
    over a neutral flip. If all gains are negative, make every variable a candidate.
    From this pool choose the one whose last flip in the current attempt was longest
    ago; treat never-flipped variables as oldest and break their ties with a fixed
    arbitrary ordering, as in HSAT. Flip it, update its timestamp and repeat within
    the selected attempt budget. New attempts retain the GSAT initialization behavior
    and reset the current-attempt history. Limits: The fallback pool when all gains
    are negative contains all variables; it is not restricted to least-worsening moves.
    Replacing the nonnegative pool with only maximum-gain candidates yields a different
    rule. The oldest-variable selector is deterministic once the current attempt and
    fixed ordering are specified, but initialization remains randomized. A rule excluding
    recent moves for a tenure would introduce tabu behavior not required by IHSAT.
    The 1993 evidence is empirical. No completeness, polynomial runtime or universal
    superiority is established by the inspected method description, and no numerical
    benchmark claim is curated. The GenSAT loop checks satisfaction before each flip;
    exact final-flip return handling and budget boundaries must be declared in an
    implementation. Finite failure is not an UNSAT certificate. No author solver was
    executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable architecture or search procedure, not a trained model instance
      or benchmark outcome.
    evidence_ids:
    - ihsat-source-0
  - name: aio-assessment
    value: bounded_no_match
    definition: 'Nine exact AIO CLASS nodes were read in the preceding batch and recaptured
      unchanged with definitions, scoped synonyms/comments and outgoing edges. The
      same bounded SAT/search/memory neighborhood applies: random-walk exploration
      and age bookkeeping do not make neural memory, a language model, a training
      strategy or a learned action-value method. Three native concepts receive bounded
      no-match assessments. Five complete neighbors distinguish HSAT’s greedy candidate
      set, original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie
      priority; their older mapping dispositions remain context rather than a new
      approval.'
    evidence_ids:
    - mapping
- assessment_id: noveltyplus-boundaries
  area: consistency
  topic: Per-step walk coin and conditional Novelty selector
  outcome: supported
  target_ids:
  - AIMech:NoveltyPlus
  evidence_ids:
  - noveltyplus-source-0
  - noveltyplus-source-1
  - finite-conventions
  summary: Retain the plus extension with separate walk and selector parameters.
  details: The1999 method makes the random clause-variable branch available at every
    step, irrespective of the best candidate’s recency or score. Its w parameter differs
    from the inner Novelty p coin. At w=0 the original selector remains; at w=1 the
    pure clause-first walk remains. Fixed w>0 gives the source’s asymptotic guarantee
    under well-defined move rules, not a finite success or practical runtime guarantee.
- assessment_id: rnoveltyplus-boundaries
  area: consistency
  topic: Removing the periodic override and retaining the core score-gap rule
  outcome: supported
  target_ids:
  - AIMech:RNoveltyPlus
  evidence_ids:
  - rnoveltyplus-source-0
  - rnoveltyplus-source-1
  - rnoveltyplus-source-2
  - finite-conventions
  summary: Retain the1999 definition and keep the2004 plus convention distinct.
  details: The1999 paper explicitly omits the every100-step escape when defining R-Novelty+.
    The nonwalk branch uses the complete1997 four-case score-gap rule; w=0 therefore
    yields only that core, not the whole original periodic strategy. The2004 report
    labels a periodic configuration with the plus name, so its naming and cycling
    claim are not adopted. Finite F2 path calculations show positive per-step escape
    possibilities without pretending to benchmark the full solver.
- assessment_id: ihsat-boundaries
  area: consistency
  topic: Indifferent candidate pool followed by age-based picking
  outcome: supported
  target_ids:
  - AIMech:IHSAT
  evidence_ids:
  - ihsat-source-0
  - finite-conventions
  summary: Retain IHSAT as distinct from greedy HSAT.
  details: ISAT offers every nonnegative-gain variable, falling back to all variables
    when none qualify. IHSAT uses HSAT’s oldest-in-current-try pick rule on that pool.
    The finite examples select a neutral variable despite an improving alternative
    and select a more-worsening variable when all moves worsen. Neither maximum-gain
    filtering nor tabu exclusion is silently imposed. Random starts, attempt-local
    history and finite-failure limits remain explicit.
- assessment_id: mapping-boundaries
  area: grounding
  topic: SAT random exploration and history versus neural or learned models
  outcome: supported
  target_ids:
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three native concepts with bounded no-match assessments.
  details: 'Nine exact AIO CLASS nodes were read in the preceding batch and recaptured
    unchanged with definitions, scoped synonyms/comments and outgoing edges. The same
    bounded SAT/search/memory neighborhood applies: random-walk exploration and age
    bookkeeping do not make neural memory, a language model, a training strategy or
    a learned action-value method. Three native concepts receive bounded no-match
    assessments. Five complete neighbors distinguish HSAT’s greedy candidate set,
    original Novelty/R-Novelty selectors, focused GSAT noise and SKC break/freebie
    priority; their older mapping dispositions remain context rather than a new approval.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NoveltyPlus
  - AIMech:RNoveltyPlus
  - AIMech:IHSAT
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - noveltyplus-source-0
  - noveltyplus-source-1
  - rnoveltyplus-source-0
  - rnoveltyplus-source-1
  - rnoveltyplus-source-2
  - ihsat-source-0
  rationale: Novelty+ and R-Novelty+ retain different nonwalk selectors, while IHSAT
    changes its global candidate pool and selects by age. The plus methods share a
    per-step walk extension but are not identical algorithms; the1999 and2004 plus
    conventions remain separate.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- Asymptotic model finding requires the declared fixed positive per-step random-walk
  premise and well-defined move rules. It is not a finite UNSAT test, a polynomial
  bound or a practical runtime guarantee.
- The1999 R-Novelty+ removes the old periodic override; the2004 plus convention remains
  distinct. Unit clauses and initial age/reset conventions are not silently invented.
- All six pages of the1999 publisher PDF were visually inspected; the1993,1997 and2004
  sources retain their declared prior page scopes. No author implementation or numerical
  benchmark was executed.
- There are 186 pending inspection leads plus unresolved dispositions; discovery remains
  active.
links: []
tags:
- native-concepts
- sat-search
- self-review
- discovery-ongoing
```
