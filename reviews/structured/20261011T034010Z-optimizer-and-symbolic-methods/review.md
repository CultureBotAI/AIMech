# Scientific self-review of four new algorithms and two optimizer evidence enrichments

- Review: 20261011T034010Z-optimizer-and-symbolic-methods
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T03:40:10Z
- Finished UTC: 2026-10-11T03:40:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The four added algorithms have supported, scoped mechanisms. Original Adafactor evidence and the conditional Adam counterexample are preserved without universal performance claims. Two symbolic algorithms use explicit no-match assessments rather than forced AIO links. No actionable unresolved finding was identified within this scope.

## Scope And Provenance

New identities, definitions/mechanisms and AIO mapping assessments for AMSGrad, AdamNC, A-star and STRIPS; changed primary-evidence support for existing Adam and Adafactor.

Selection: Exactly the six added/enriched records enumerated in the optimizer-and-symbolic-methods discovery report; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base a5ae79f2462d527b82879145519e7ca5d6fb012f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AMSGrad | data/curated/AMSGrad.yaml | maintained | AMSGrad |
| AIMech:AdamNC | data/curated/AdamNC.yaml | maintained | AdamNC |
| AIMech:AStarSearch | data/curated/AStarSearch.yaml | maintained | A-star search |
| AIMech:STRIPSPlanning | data/curated/STRIPSPlanning.yaml | maintained | STRIPS planning method |
| AIMech:Adafactor | data/curated/Adafactor.yaml | maintained | Adafactor |
| AIMech:Adam | data/curated/Adam.yaml | maintained | Adam |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | Checked 442 record(s); 0 failed. |
| python -m aimech seed --check | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-curated | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | Checked 60 curated concept record(s); 0 error(s). |
| python scripts/record_review.py check | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 4,<br>  "coverage": "declared_scopes_only"<br>} |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | 220 passed, 3 skipped; 442 AIO records valid and exactly reproducible; 60 native records, 9 history sidecars and 4 prior review bundles valid. |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | All 22 governed artifacts match the immutable public CLAW pin. |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 uv run --locked pytest tests/test_curated.py -q | passed | True | AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam | 30 focused validator tests passed, including no-match acceptance, contradictory/missing assessments, duplicate/invalid targets, identity/pin checks and abstract-only rejection. |

## Scientific And Domain Assessments

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:AMSGrad.

The historical maximum distinguishes AMSGrad from Adam and from weight-decay decoupling in AdamW. It can be combined with other optimizer choices without becoming identical to them.

The paper's convergence analysis imposes assumptions and schedules; no unconditional convergence or benchmark advantage is claimed here. The record describes the original formulation; implementation-specific bias correction and numerical stabilizers require separate comparison.

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:AdamNC.

AdamNC changes the moment schedules rather than taking AMSGrad's historical maximum. The named method is distinct from an arbitrary claim that any changing Adam hyperparameters ensures convergence.

The paper's guarantees require additional conditions on schedules, gradients and the feasible region; no guarantee is asserted for arbitrary schedules or nonconvex training. No performance comparison or experimental replication is curated.

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:AStarSearch.

This is the graph-search algorithm conventionally written A*, not a graph language model or a learned policy. Its heuristic estimate is distinct from the exact remaining path cost.

The original analysis assumes graph arc costs bounded below by a positive constant; its optimality arguments depend on heuristic and graph assumptions. This record curates the search mechanism, not a claim of fewest possible expansions or universal optimality. The 1972 correction and later optimal-efficiency analyses remain follow-up evidence.

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:STRIPSPlanning.

This record denotes the planning procedure described in the 1971 STRIPS paper, not a particular executable or every later STRIPS-style action representation.

The original paper's predicate-calculus world models and theorem-proving procedure should not be equated automatically with every later propositional STRIPS formalism. No completeness, runtime or robotic performance guarantee is curated.

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:Adafactor.

Same method identity as the existing native record; no duplicate created.

PyTorch documents differences from the original paper in learning-rate control and epsilon handling; the record does not equate their exact update equations. No measured memory reduction, benchmark superiority or convergence guarantee is asserted.

### New concept mechanism or changed primary-evidence support

evidence: supported. Targets: AIMech:Adam.

Existing Adam mechanism and identity remain unchanged; negative evidence is a scoped additional claim.

No universal convergence or benchmark superiority claim is curated. AdamW, AdaMax and other variants require their own identity assessment. The reported counterexample is an existence result for the analyzed Adam setting, not a statement that Adam fails on every training problem or that all later variants share the result. The analysis introduces projection and a decreasing step-size setting, omits debiasing for exposition, and states that its arguments extend to the debiased version; it does not analyze every implementation configuration.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AMSGrad, AIMech:AdamNC, AIMech:AStarSearch, AIMech:STRIPSPlanning, AIMech:Adafactor, AIMech:Adam. Retain historical-maximum AMSGrad, scheduled-moment AdamNC, the existing Adam/Adafactor identities, heuristic graph search and the original STRIPS planning procedure as distinct concepts. Evidence enrichment does not create a new identity; the STRIPS procedure does not denote every later action formalism.
- defer: AIMech:AStarSearch, AIMech:STRIPSPlanning. Defer positive AIO mappings: none of the inspected targets supplies a suitable counterpart. The explicit no-match records retain rejected candidates and bounded search scope for later source or taxonomy reassessment.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T033802Z-optimizer-and-symbolic-methods.json | supports | No duplicate native identity was found for the four additions; existing Adam and Adafactor were enriched without creating new identities. |
| mapping-assessments | sources/aio/aio.json; TrainingStrategy, GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask and MathematicalFunction definitions | supports | Optimizer related mappings retain abstraction differences. Shared graph or reasoning terms do not justify language-model mappings for A-star and STRIPS; their explicit no-match decisions are bounded to the inspected pin. |
| mapping-validator | src/aimech/curated.py; validate_curated_record and validate_curated; tests/test_curated.py | supports | Exactly one mapping representation is required. No-match assessments require nonempty scope/rationale and examined targets; target validity, source pin, identity and evidence checks still apply. Focused rejection cases passed. |
| amsgrad-evidence | https://arxiv.org/pdf/1904.09237v1; Section 4 and Algorithm 2, PDF/printed p. 5 | supports | The method keeps first- and second-moment accumulators and a nondecreasing coordinatewise maximum of the latter; its original constrained formulation projects the resulting adaptive step onto the feasible set. Selected rendered pages inspected: 5, 19. |
| adamnc-evidence | https://arxiv.org/pdf/1904.09237v1; Section 5.1, PDF/printed p. 8; Algorithm 3, PDF/printed p. 19 | supports | Both moment accumulators use iteration-indexed decay coefficients; the original method scales the first-moment step by the square root of the second moment and projects it onto the feasible set. Selected rendered pages inspected: 5, 19. |
| astarsearch-evidence | https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf; Section II.A–C, printed pp. 101–102 / PDF pp. 2–3; Search Algorithm A* and equation 2 | supports | The procedure expands a minimum-score open node, updates successor path estimates, reopens a closed successor when a better estimate is found, and terminates when a selected node is a goal. Selected rendered pages inspected: 1, 2, 3. |
| stripsplanning-evidence | https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf; Sections 2.1–2.2, printed pp. 191–193 / PDF pp. 3–5 | supports | Operators specify preconditions and additions/deletions to a logical world model. The search identifies operators relevant to an unmet goal, treats their preconditions as subgoals, applies an applicable operator and revisits the original goal. Selected rendered pages inspected: 4, 5. |
| adafactor-evidence | https://arxiv.org/pdf/1804.04235v1; Algorithms 4–6, PDF p. 8 | supports | Original matrix/vector updates support factorization, RMS clipping and parameter scaling. Retained documented differences in PyTorch learning-rate and epsilon handling. Selected rendered pages inspected: 8. |
| adam-evidence | https://arxiv.org/pdf/1904.09237v1; Section 2, PDF/printed pp. 2–3; Theorem 3 and scope discussion, PDF/printed p. 5 | supports | Preserved the existence of stochastic convex counterexamples in the analyzed setting, the fixed-coefficient condition and the projected/bounded setup. This does not assert failure on every task. Selected rendered pages inspected: 5, 19. |

## Limits And Additional Notes

- Scientific self-review of selected mechanisms and changed evidence; not independent peer review, proof verification or experiment replication.
- The review timestamps record post-inspection assessment; the dated discovery report records earlier retrieval, reading and curation.
- A-star optimal-efficiency corrections and later STRIPS representations remain follow-up leads; no broad guarantee or identity conflation is asserted.
- No-match decisions are bounded to the current pin and inspected definitions, not all possible ontologies or interpretations.
- All records remain DRAFT. Four new concepts were found and the broader discovery frontier remains nonempty.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T034010Z-optimizer-and-symbolic-methods
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of four new algorithms and two optimizer evidence enrichments
started_at: '2026-10-11T03:40:10Z'
finished_at: '2026-10-11T03:40:10Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent researched, curated and reviewed these records
    and schema changes; this is not independent review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The four added algorithms have supported, scoped mechanisms. Original Adafactor
  evidence and the conditional Adam counterexample are preserved without universal
  performance claims. Two symbolic algorithms use explicit no-match assessments rather
  than forced AIO links. No actionable unresolved finding was identified within this
  scope.
source:
  git_revision: a5ae79f2462d527b82879145519e7ca5d6fb012f
  state: working_tree
  inputs:
  - path: data/curated/AMSGrad.yaml
    sha256: cea17d1eed28932058c4a0c194673d3500cff0344cc3ca4ee4b282386bce4d95
    role: target
  - path: data/curated/AStarSearch.yaml
    sha256: 685cfd5d6b4eaf0811d597e93e117ad065857d5707f0040420d3e6885f520b8d
    role: target
  - path: data/curated/Adafactor.yaml
    sha256: c247b6b34b342fa3d8e87696462dbfd1812b65030371f9cb2d58349429e05721
    role: target
  - path: data/curated/Adam.yaml
    sha256: b28d5f93f73b80005b3ef7b98d306b5b548f3d2aa77362592c497404e0ea944a
    role: target
  - path: data/curated/AdamNC.yaml
    sha256: 634d64a1a4806ea801415d3594fb9ab7048eee29d8195f380f9e74cccbccf902
    role: target
  - path: data/curated/STRIPSPlanning.yaml
    sha256: 6b4e884b76dd3049bb7f3c8103738eafddfd8ed492587ca35adf9c846f49317d
    role: target
  - path: research/discovery/20261011T033802Z-optimizer-and-symbolic-methods.json
    sha256: 91b8ab35230b47e29120c9519c3db4ccb57f9118c7636ead5ea196a571c6eb95
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: b9a87f14341119f89fffac2cfb29fab222d0fcc9ac999990650e349e06d9cfc3
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: dfcbacdcdeb7429bfa947d7c1c8431e5d0b886f593daaa359588273ba2a2c6e0
    role: context
  - path: tests/test_curated.py
    sha256: 8dd0902901be8a7c1da61fb80c5ffd8c9e131293d0d805ff35d4c26b04a4a664
    role: context
targets:
- target_id: AIMech:AMSGrad
  path: data/curated/AMSGrad.yaml
  label: AMSGrad
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AMSGrad.yaml
    role: maintained concept and evidence/mapping assessment
- target_id: AIMech:AdamNC
  path: data/curated/AdamNC.yaml
  label: AdamNC
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdamNC.yaml
    role: maintained concept and evidence/mapping assessment
- target_id: AIMech:AStarSearch
  path: data/curated/AStarSearch.yaml
  label: A-star search
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AStarSearch.yaml
    role: maintained concept and evidence/mapping assessment
- target_id: AIMech:STRIPSPlanning
  path: data/curated/STRIPSPlanning.yaml
  label: STRIPS planning method
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/STRIPSPlanning.yaml
    role: maintained concept and evidence/mapping assessment
- target_id: AIMech:Adafactor
  path: data/curated/Adafactor.yaml
  label: Adafactor
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adafactor.yaml
    role: maintained concept and evidence/mapping assessment
- target_id: AIMech:Adam
  path: data/curated/Adam.yaml
  label: Adam
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adam.yaml
    role: maintained concept and evidence/mapping assessment
scope:
  description: New identities, definitions/mechanisms and AIO mapping assessments
    for AMSGrad, AdamNC, A-star and STRIPS; changed primary-evidence support for existing
    Adam and Adafactor.
  selection: Exactly the six added/enriched records enumerated in the optimizer-and-symbolic-methods
    discovery report; no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exclusions:
  - target: Other native concepts and generated AIO claims
    reason: Used as identity and mapping context; no new claim-by-claim fleet review.
  - target: Independent proof checking, benchmark replication and uncurated optimal-efficiency
      claims
    reason: The review assesses source support and bounded interpretation, not mathematical
      peer review or experiments.
checks:
- check_id: required-0
  name: python -m aimech check-source
  command: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
- check_id: required-1
  name: python -m aimech validate
  command: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
- check_id: required-2
  name: python -m aimech seed --check
  command: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
- check_id: required-3
  name: python -m aimech validate-curated
  command: python -m aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 60 curated concept record(s); 0 error(s).
- check_id: required-4
  name: python scripts/record_review.py check
  command: python scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 4,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}"
- check_id: quality
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: 220 passed, 3 skipped; 442 AIO records valid and exactly reproducible;
    60 native records, 9 history sidecars and 4 prior review bundles valid.
- check_id: governance
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: All 22 governed artifacts match the immutable public CLAW pin.
- check_id: focused
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 uv run --locked pytest
    tests/test_curated.py -q
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 uv run --locked pytest
    tests/test_curated.py -q
  status: passed
  required: true
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  exit_code: 0
  expected_exit_code: 0
  summary: 30 focused validator tests passed, including no-match acceptance, contradictory/missing
    assessments, duplicate/invalid targets, identity/pin checks and abstract-only
    rejection.
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T033802Z-optimizer-and-symbolic-methods.json
  accessed_at: '2026-10-11T03:40:10Z'
  support: supports
  summary: No duplicate native identity was found for the four additions; existing
    Adam and Adafactor were enriched without creating new identities.
  search_scope: Ignored-inclusive and hidden-inclusive searches of both checkouts,
    plus normalized comparison of all 442 AIO labels/scoped synonyms and the 56 preceding
    native records. Semantic target definitions were inspected as declared in the
    two no-match assessments.
- evidence_id: mapping-assessments
  kind: record_content
  reference: sources/aio/aio.json
  locator: TrainingStrategy, GraphLanguageModel, ReasoningLLM, NeuroSymbolicLLM, MachineLearningTask
    and MathematicalFunction definitions
  accessed_at: '2026-10-11T03:40:10Z'
  support: supports
  summary: Optimizer related mappings retain abstraction differences. Shared graph
    or reasoning terms do not justify language-model mappings for A-star and STRIPS;
    their explicit no-match decisions are bounded to the inspected pin.
- evidence_id: mapping-validator
  kind: record_content
  reference: src/aimech/curated.py
  locator: validate_curated_record and validate_curated; tests/test_curated.py
  accessed_at: '2026-10-11T03:40:10Z'
  support: supports
  summary: Exactly one mapping representation is required. No-match assessments require
    nonempty scope/rationale and examined targets; target validity, source pin, identity
    and evidence checks still apply. Focused rejection cases passed.
- evidence_id: amsgrad-evidence
  kind: primary_source
  reference: https://arxiv.org/pdf/1904.09237v1
  locator: Section 4 and Algorithm 2, PDF/printed p. 5
  accessed_at: '2026-10-11T03:27:02Z'
  snapshot_sha256: 75a949b0751e81c490e7eee76efadd1eb8868c64f44275d8d1542a8f42cb7c01
  support: supports
  summary: 'The method keeps first- and second-moment accumulators and a nondecreasing
    coordinatewise maximum of the latter; its original constrained formulation projects
    the resulting adaptive step onto the feasible set. Selected rendered pages inspected:
    5, 19.'
- evidence_id: adamnc-evidence
  kind: primary_source
  reference: https://arxiv.org/pdf/1904.09237v1
  locator: Section 5.1, PDF/printed p. 8; Algorithm 3, PDF/printed p. 19
  accessed_at: '2026-10-11T03:27:02Z'
  snapshot_sha256: 75a949b0751e81c490e7eee76efadd1eb8868c64f44275d8d1542a8f42cb7c01
  support: supports
  summary: 'Both moment accumulators use iteration-indexed decay coefficients; the
    original method scales the first-moment step by the square root of the second
    moment and projects it onto the feasible set. Selected rendered pages inspected:
    5, 19.'
- evidence_id: astarsearch-evidence
  kind: primary_source
  reference: https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf
  locator: Section II.A–C, printed pp. 101–102 / PDF pp. 2–3; Search Algorithm A*
    and equation 2
  accessed_at: '2026-10-11T03:27:02Z'
  snapshot_sha256: ed435399010be2e9ee70006a8cd0865ecbff367f6b312ab5f87bd2f34db41eac
  support: supports
  summary: 'The procedure expands a minimum-score open node, updates successor path
    estimates, reopens a closed successor when a better estimate is found, and terminates
    when a selected node is a goal. Selected rendered pages inspected: 1, 2, 3.'
- evidence_id: stripsplanning-evidence
  kind: primary_source
  reference: https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf
  locator: Sections 2.1–2.2, printed pp. 191–193 / PDF pp. 3–5
  accessed_at: '2026-10-11T03:27:03Z'
  snapshot_sha256: a6813d187806c1785bebe701b5baf5a891ecaef7fc606bc8ace13a6270d8b7a6
  support: supports
  summary: 'Operators specify preconditions and additions/deletions to a logical world
    model. The search identifies operators relevant to an unmet goal, treats their
    preconditions as subgoals, applies an applicable operator and revisits the original
    goal. Selected rendered pages inspected: 4, 5.'
- evidence_id: adafactor-evidence
  kind: primary_source
  reference: https://arxiv.org/pdf/1804.04235v1
  locator: Algorithms 4–6, PDF p. 8
  accessed_at: '2026-10-11T03:27:02Z'
  snapshot_sha256: 893ccde9ab41deba45282caa1007847d2bd586811e1f0aaa421fc8b3d3f13085
  support: supports
  summary: 'Original matrix/vector updates support factorization, RMS clipping and
    parameter scaling. Retained documented differences in PyTorch learning-rate and
    epsilon handling. Selected rendered pages inspected: 8.'
- evidence_id: adam-evidence
  kind: primary_source
  reference: https://arxiv.org/pdf/1904.09237v1
  locator: Section 2, PDF/printed pp. 2–3; Theorem 3 and scope discussion, PDF/printed
    p. 5
  accessed_at: '2026-10-11T03:27:02Z'
  snapshot_sha256: 75a949b0751e81c490e7eee76efadd1eb8868c64f44275d8d1542a8f42cb7c01
  support: supports
  summary: 'Preserved the existence of stochastic convex counterexamples in the analyzed
    setting, the fixed-coefficient condition and the projected/bounded setup. This
    does not assert failure on every task. Selected rendered pages inspected: 5, 19.'
assessments:
- assessment_id: amsgrad-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:AMSGrad
  evidence_ids:
  - amsgrad-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: The historical maximum distinguishes AMSGrad from Adam and from weight-decay
    decoupling in AdamW. It can be combined with other optimizer choices without becoming
    identical to them.
  details: The paper's convergence analysis imposes assumptions and schedules; no
    unconditional convergence or benchmark advantage is claimed here. The record describes
    the original formulation; implementation-specific bias correction and numerical
    stabilizers require separate comparison.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - amsgrad-evidence
  - name: aio-disposition
    value: 'related_match: AIO:TrainingStrategy'
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
- assessment_id: adamnc-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:AdamNC
  evidence_ids:
  - adamnc-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: AdamNC changes the moment schedules rather than taking AMSGrad's historical
    maximum. The named method is distinct from an arbitrary claim that any changing
    Adam hyperparameters ensures convergence.
  details: The paper's guarantees require additional conditions on schedules, gradients
    and the feasible region; no guarantee is asserted for arbitrary schedules or nonconvex
    training. No performance comparison or experimental replication is curated.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - adamnc-evidence
  - name: aio-disposition
    value: 'related_match: AIO:TrainingStrategy'
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
- assessment_id: astarsearch-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:AStarSearch
  evidence_ids:
  - astarsearch-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: This is the graph-search algorithm conventionally written A*, not a graph
    language model or a learned policy. Its heuristic estimate is distinct from the
    exact remaining path cost.
  details: The original analysis assumes graph arc costs bounded below by a positive
    constant; its optimality arguments depend on heuristic and graph assumptions.
    This record curates the search mechanism, not a claim of fewest possible expansions
    or universal optimality. The 1972 correction and later optimal-efficiency analyses
    remain follow-up evidence.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - astarsearch-evidence
  - name: aio-disposition
    value: no_suitable_match
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
- assessment_id: stripsplanning-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:STRIPSPlanning
  evidence_ids:
  - stripsplanning-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: This record denotes the planning procedure described in the 1971 STRIPS
    paper, not a particular executable or every later STRIPS-style action representation.
  details: The original paper's predicate-calculus world models and theorem-proving
    procedure should not be equated automatically with every later propositional STRIPS
    formalism. No completeness, runtime or robotic performance guarantee is curated.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - stripsplanning-evidence
  - name: aio-disposition
    value: no_suitable_match
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
- assessment_id: adafactor-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:Adafactor
  evidence_ids:
  - adafactor-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: Same method identity as the existing native record; no duplicate created.
  details: PyTorch documents differences from the original paper in learning-rate
    control and epsilon handling; the record does not equate their exact update equations.
    No measured memory reduction, benchmark superiority or convergence guarantee is
    asserted.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - adafactor-evidence
  - name: aio-disposition
    value: existing related mapping retained
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
- assessment_id: adam-evidence
  area: evidence
  topic: New concept mechanism or changed primary-evidence support
  outcome: supported
  target_ids:
  - AIMech:Adam
  evidence_ids:
  - adam-evidence
  - identity-search
  - mapping-assessments
  - mapping-validator
  summary: Existing Adam mechanism and identity remain unchanged; negative evidence
    is a scoped additional claim.
  details: No universal convergence or benchmark superiority claim is curated. AdamW,
    AdaMax and other variants require their own identity assessment. The reported
    counterexample is an existence result for the analyzed Adam setting, not a statement
    that Adam fails on every training problem or that all later variants share the
    result. The analysis introduces projection and a decreasing step-size setting,
    omits debiasing for exposition, and states that its arguments extend to the debiased
    version; it does not analyze every implementation configuration.
  dimensions:
  - name: evidence-access
    value: full_text with rendered-page inspection
    definition: Full method passages were read and the listed equations/search descriptions
      visually checked; A-star additionally required OCR of a scan.
    evidence_ids:
    - adam-evidence
  - name: aio-disposition
    value: existing related mapping retained
    definition: Mapping assessment of the pinned AIO snapshot; no-match does not assert
      a positive ontology edge.
    evidence_ids:
    - mapping-assessments
    - mapping-validator
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AMSGrad
  - AIMech:AdamNC
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  - AIMech:Adafactor
  - AIMech:Adam
  evidence_ids:
  - identity-search
  - mapping-assessments
  - mapping-validator
  - amsgrad-evidence
  - adamnc-evidence
  - astarsearch-evidence
  - stripsplanning-evidence
  - adafactor-evidence
  - adam-evidence
  rationale: Retain historical-maximum AMSGrad, scheduled-moment AdamNC, the existing
    Adam/Adafactor identities, heuristic graph search and the original STRIPS planning
    procedure as distinct concepts. Evidence enrichment does not create a new identity;
    the STRIPS procedure does not denote every later action formalism.
- action: defer
  target_ids:
  - AIMech:AStarSearch
  - AIMech:STRIPSPlanning
  evidence_ids:
  - identity-search
  - mapping-assessments
  rationale: 'Defer positive AIO mappings: none of the inspected targets supplies
    a suitable counterpart. The explicit no-match records retain rejected candidates
    and bounded search scope for later source or taxonomy reassessment.'
limitations:
- Scientific self-review of selected mechanisms and changed evidence; not independent
  peer review, proof verification or experiment replication.
- The review timestamps record post-inspection assessment; the dated discovery report
  records earlier retrieval, reading and curation.
- A-star optimal-efficiency corrections and later STRIPS representations remain follow-up
  leads; no broad guarantee or identity conflation is asserted.
- No-match decisions are bounded to the current pin and inspected definitions, not
  all possible ontologies or interpretations.
- All records remain DRAFT. Four new concepts were found and the broader discovery
  frontier remains nonempty.
tags:
- native-concepts
- primary-papers
- symbolic-ai
- optimizers
- aio-no-match
- self-review
- discovery-ongoing
```
