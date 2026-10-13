# Scientific author self-review of Complete Karmarkar–Karp

- Review: 20261013T075819Z-complete-karmarkar-karp
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T07:52:39Z
- Finished UTC: 2026-10-13T07:58:19Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two-way Complete Karmarkar–Karp as a DRAFT complete anytime algorithm with explicit AIO no-match assessment. All six claims are supported within exact-arithmetic, search-completion and historical-evaluation limits; author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CompleteKarmarkarKarp
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 056887d7fc59bb465711037151f4a208338908cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CompleteKarmarkarKarp | data/curated/CompleteKarmarkarKarp.yaml | maintained | Complete Karmarkar–Karp |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CompleteKarmarkarKarp | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 166.43s (0:02:46)<br>Checked 442 record(s); 0 failed.<br>Checked 589 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 248 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 247,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CompleteKarmarkarKarp | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CompleteKarmarkarKarp | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CompleteKarmarkarKarp | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CompleteKarmarkarKarp | {"scope": "Ten constructed fixtures, exhaustive sign enumeration, and one one-node-budget boundary; no timing or empirical replication.", "results": [{"values": [8, 7, 6, 5, 4], "initial_kk": 2, "residue": 0, "incumbent_history": [2, 0], "nodes": 5, "certified": true}, {"values": [73, 40, 30, 20, 13, 6, 3], "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes": 0, "certified": true}, {"values": [5, 5, 5, 5], "initial_kk": 0, "residue": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [0, 0, 0], "initial_kk": 0, "residue": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [9], "initial_kk": 9, "residue": 9, "incumbent_history": [9], "nodes": 1, "certified": true}, {"values": [10, 3, 2], "initial_kk": 5, "residue": 5, "incumbent_history": [5], "nodes": 1, "certified": true}, {"values": [3, 2, 2], "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes": 0, "certified": true}, {"values": [4, 3, 3, 2], "initial_kk": 0, "residue": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [13, 11, 9, 7, 5], "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes": 0, "certified": true}, {"values": [12, 9, 8, 7, 5, 4], "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes": 0, "certified": true}], "interrupted": {"initial_kk": 2, "residue": 2, "incumbent_history": [2], "nodes": 1, "certified": false}} |

## Scientific And Domain Assessments

### Complete Karmarkar–Karp

identity: supported. Targets: AIMech:CompleteKarmarkarKarp.

Retain this distinct DRAFT algorithm.

CKK searches relative subpartition orientations and can certify optimality, unlike the KK heuristic. It differs from generic DFS, discrepancy ordering and complete greedy raw-item assignment. The record explicitly scopes the two-way depth-first formulation.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CompleteKarmarkarKarp.

Explicit no-match assessment is supported.

All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence.

### difference-and-sum-branches

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Section3 and Figure4 explicitly branch on opposite/same orientations of the two largest residuals. Source Section11 explains relative assignments; reconstruction bookkeeping remains required and complete greedy is distinguished.

### dominance-and-parity

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Largest-minus-rest is both a nonnegative lower bound and attainable when dominant. Original integer parity is preserved by sum and difference. The record uses exact0/1 certification, not floating tolerance or a claim that odd inputs always have residue1.

### anytime-versus-optimal

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

A KK incumbent is available before further exploration; strict improvements are retained. The finite constructed counterexample and one-node interruption verify the distinction between feasible and certified, without asserting every search step improves.

### complexity-and-representation

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Worst-case exponential search remains. Linear-space organization is qualified by compact bookkeeping, not copied-list recursion; bit complexity is distinct. Sorted-array and small-state source optimizations are correctly experimental implementation details.

### subset-sum-reduction-scope

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

For c within[0,s], complementation makes c&gt;=s/2 and d=2c-s nonnegative. Augmented zero residue corresponds to an original target subset, with complementation back when needed. A positive incumbent only excludes a target if optimality is established; no nonzero-error equivalence is asserted.

### historical-evaluation-boundaries

evidence: supported. Targets: AIMech:CompleteKarmarkarKarp.

Supported within the stated primary-source and mathematical scope.

Source Sections4–6 limit timing and improvement results to sampled uniform integer distributions, precision and old hardware. Figure6 is100 trials of50 48-bit numbers; multiway and discrepancy variants are separate. No arbitrary-instance polynomial or runtime guarantee remains.

### complementary branch completeness, exact optimality certificates, interrupted incumbents, subset-sum reduction and distribution-specific evaluation

consistency: supported. Targets: AIMech:CompleteKarmarkarKarp.

Constructed calculations support the stated distinctions.

Ten small exact-integer fixtures compare a constructed CKK-style search against exhaustive sign enumeration. The counterexample improves2→0, dominance cases attain their bounds, and a search interrupted before exploring children retains an uncertified residue2. This is not author-code or performance replication.

### All maintained fields

provenance: supported. Targets: AIMech:CompleteKarmarkarKarp.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read the entire maintained record and six examined-target YAMLs after capture. Reread source pruning, complete difference/sum search, implementation/evaluation, anytime improvement and subset-sum reduction pages. All31 manuscript pages were read before curation. Checked complementary orientation, admissible bounds, integer parity, interrupted-incumbent status and the feasible-target restriction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T075226Z-complete-karmarkar-karp.json | supports | Compared all 442 pinned AIO and 588 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 204, 120, 119 lines. All distinct match contents were inspected. Semantic matching covered 67 AIO and 95 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. The combined frontier entry and new KK heuristic are related prior work, not an existing CKK identity. This two-way complete anytime algorithm searches relative subpartition orientations by differencing and summing the largest residuals. It is distinct from the irreversible KK heuristic, complete greedy item assignment, generic DFS and discrepancy-order search. Multiway extensions remain separate leads. No suitable counterpart was found in the inspected pinned AIO graph. |
| mapping | sources/aio/aio.json | supports | All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence. |
| korf1997 | https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf; Complete31-page27June1997 manuscript read, with selected mechanism/evaluation/reduction pages reread after capture. Later publisher metadata identifies the1998 DOI; final journal full text and author implementation not inspected. No empirical replication. | supports | University-hosted31-page manuscript dated27June1997, read in full. DOI identifies the later1998 Artificial Intelligence106(2):181–203 publication; its final typeset text was not inspected. Locators refer to manuscript PDF/printed pages1–31. |
| calculation | research/discovery/complete-karmarkar-karp-boundaries.py | supports | Ten small exact-integer fixtures compare a constructed CKK-style search against exhaustive sign enumeration. The counterexample improves2→0, dominance cases attain their bounds, and a search interrupted before exploring children retains an uncertified residue2. This is not author-code or performance replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 589 native and 442 unchanged generated records. The 773-entry main frontier retains 480 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All31 pages of the dated1997 Korf manuscript visually read; final1998 publisher metadata corroborated separately, not the final full text. No author code or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T075819Z-complete-karmarkar-karp
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Complete Karmarkar–Karp
started_at: '2026-10-13T07:52:39Z'
finished_at: '2026-10-13T07:58:19Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged complementary branch completeness, exact
    optimality certificates, interrupted incumbents, subset-sum reduction and distribution-specific
    evaluation. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain two-way Complete Karmarkar–Karp as a DRAFT complete anytime algorithm
  with explicit AIO no-match assessment. All six claims are supported within exact-arithmetic,
  search-completion and historical-evaluation limits; author self-review found no
  actionable defect.
source:
  git_revision: 056887d7fc59bb465711037151f4a208338908cd
  state: working_tree
  inputs:
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/curated/CompleteKarmarkarKarp.yaml
    sha256: 65431bae97ba1ebb9e38b2a17a9b59fcc156087167173faf88308b5f38fddcca
    role: target
  - path: data/curated/DepthFirstSearch.yaml
    sha256: 060134862e6bb35089311a0fc2b1c7cd91f408556660f856d11e8bc4762ab6a6
    role: context
  - path: data/curated/ImprovedLimitedDiscrepancySearch.yaml
    sha256: 93689aa911171cdd85f4c0e8b9517414532037295fe7e084189d51d4e174a6ad
    role: context
  - path: data/curated/KarmarkarKarpDifferencing.yaml
    sha256: 3bfbfa6fc45fe53b3bda3c61ace7e2beb7d39b8dec3ee93b360d5cfe0d6afdfc
    role: context
  - path: data/curated/LimitedDiscrepancySearch.yaml
    sha256: 144d2daed4c13fdca8e6b1251fa64c4c486354ac6d80c2c5e51b828b0cabbee1
    role: context
  - path: research/discovery/20261013T075226Z-complete-karmarkar-karp.json
    sha256: 83e723d3b9ba0082f303c949f0a65ba7ec4d9cd25bf0d1de5733dea455e1c01b
    role: context
  - path: research/discovery/complete-karmarkar-karp-boundaries.py
    sha256: 8fd9a0baaa330ba58372532d0c54308fd4bdb203cf25f1c8fa455b197adad2d3
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
- target_id: AIMech:CompleteKarmarkarKarp
  path: data/curated/CompleteKarmarkarKarp.yaml
  label: Complete Karmarkar–Karp
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CompleteKarmarkarKarp.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CompleteKarmarkarKarp'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CompleteKarmarkarKarp
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete31-page27June1997 manuscript read, with selected mechanism/evaluation/reduction
      pages reread after capture. Later publisher metadata identifies the1998 DOI;
      final journal full text and author implementation not inspected. No empirical
      replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 166.43s (0:02:46)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 589 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 248 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 247,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteKarmarkarKarp
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
  - AIMech:CompleteKarmarkarKarp
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
  - AIMech:CompleteKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/complete-karmarkar-karp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Ten constructed fixtures, exhaustive sign enumeration, and
    one one-node-budget boundary; no timing or empirical replication.", "results":
    [{"values": [8, 7, 6, 5, 4], "initial_kk": 2, "residue": 0, "incumbent_history":
    [2, 0], "nodes": 5, "certified": true}, {"values": [73, 40, 30, 20, 13, 6, 3],
    "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes": 0, "certified":
    true}, {"values": [5, 5, 5, 5], "initial_kk": 0, "residue": 0, "incumbent_history":
    [0], "nodes": 0, "certified": true}, {"values": [0, 0, 0], "initial_kk": 0, "residue":
    0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values": [9], "initial_kk":
    9, "residue": 9, "incumbent_history": [9], "nodes": 1, "certified": true}, {"values":
    [10, 3, 2], "initial_kk": 5, "residue": 5, "incumbent_history": [5], "nodes":
    1, "certified": true}, {"values": [3, 2, 2], "initial_kk": 1, "residue": 1, "incumbent_history":
    [1], "nodes": 0, "certified": true}, {"values": [4, 3, 3, 2], "initial_kk": 0,
    "residue": 0, "incumbent_history": [0], "nodes": 0, "certified": true}, {"values":
    [13, 11, 9, 7, 5], "initial_kk": 1, "residue": 1, "incumbent_history": [1], "nodes":
    0, "certified": true}, {"values": [12, 9, 8, 7, 5, 4], "initial_kk": 1, "residue":
    1, "incumbent_history": [1], "nodes": 0, "certified": true}], "interrupted": {"initial_kk":
    2, "residue": 2, "incumbent_history": [2], "nodes": 1, "certified": false}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T075226Z-complete-karmarkar-karp.json
  accessed_at: '2026-10-13T07:52:39Z'
  support: supports
  summary: Compared all 442 pinned AIO and 588 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    204, 120, 119 lines. All distinct match contents were inspected. Semantic matching
    covered 67 AIO and 95 native definitions, with every matched definition read.
    6 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. The combined frontier entry and new KK heuristic are related prior
    work, not an existing CKK identity. This two-way complete anytime algorithm searches
    relative subpartition orientations by differencing and summing the largest residuals.
    It is distinct from the irreversible KK heuristic, complete greedy item assignment,
    generic DFS and discrepancy-order search. Multiway extensions remain separate
    leads. No suitable counterpart was found in the inspected pinned AIO graph.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T07:52:39Z'
  support: supports
  summary: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- evidence_id: korf1997
  kind: primary_source
  reference: https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf
  locator: Complete31-page27June1997 manuscript read, with selected mechanism/evaluation/reduction
    pages reread after capture. Later publisher metadata identifies the1998 DOI; final
    journal full text and author implementation not inspected. No empirical replication.
  accessed_at: '2026-10-13T07:27:28Z'
  snapshot_sha256: 00751dfacfb610eaca973274764704476ecef22865526b9528eb88e07dc09074
  support: supports
  summary: University-hosted31-page manuscript dated27June1997, read in full. DOI
    identifies the later1998 Artificial Intelligence106(2):181–203 publication; its
    final typeset text was not inspected. Locators refer to manuscript PDF/printed
    pages1–31.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/complete-karmarkar-karp-boundaries.py
  accessed_at: '2026-10-13T07:54:42Z'
  snapshot_sha256: 8fd9a0baaa330ba58372532d0c54308fd4bdb203cf25f1c8fa455b197adad2d3
  support: supports
  summary: Ten small exact-integer fixtures compare a constructed CKK-style search
    against exhaustive sign enumeration. The counterexample improves2→0, dominance
    cases attain their bounds, and a search interrupted before exploring children
    retains an uncertified residue2. This is not author-code or performance replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Complete Karmarkar–Karp
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - identity
  - korf1997
  summary: Retain this distinct DRAFT algorithm.
  details: CKK searches relative subpartition orientations and can certify optimality,
    unlike the KK heuristic. It differs from generic DFS, discrepancy ordering and
    complete greedy raw-item assignment. The record explicitly scopes the two-way
    depth-first formulation.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - mapping
  - korf1997
  summary: Explicit no-match assessment is supported.
  details: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- assessment_id: difference-and-sum-branches
  area: evidence
  topic: difference-and-sum-branches
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3 and Figure4 explicitly branch on opposite/same orientations of
    the two largest residuals. Source Section11 explains relative assignments; reconstruction
    bookkeeping remains required and complete greedy is distinguished.
- assessment_id: dominance-and-parity
  area: evidence
  topic: dominance-and-parity
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Largest-minus-rest is both a nonnegative lower bound and attainable when
    dominant. Original integer parity is preserved by sum and difference. The record
    uses exact0/1 certification, not floating tolerance or a claim that odd inputs
    always have residue1.
- assessment_id: anytime-versus-optimal
  area: evidence
  topic: anytime-versus-optimal
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: A KK incumbent is available before further exploration; strict improvements
    are retained. The finite constructed counterexample and one-node interruption
    verify the distinction between feasible and certified, without asserting every
    search step improves.
- assessment_id: complexity-and-representation
  area: evidence
  topic: complexity-and-representation
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: Worst-case exponential search remains. Linear-space organization is qualified
    by compact bookkeeping, not copied-list recursion; bit complexity is distinct.
    Sorted-array and small-state source optimizations are correctly experimental implementation
    details.
- assessment_id: subset-sum-reduction-scope
  area: evidence
  topic: subset-sum-reduction-scope
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: For c within[0,s], complementation makes c>=s/2 and d=2c-s nonnegative.
    Augmented zero residue corresponds to an original target subset, with complementation
    back when needed. A positive incumbent only excludes a target if optimality is
    established; no nonzero-error equivalence is asserted.
- assessment_id: historical-evaluation-boundaries
  area: evidence
  topic: historical-evaluation-boundaries
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  summary: Supported within the stated primary-source and mathematical scope.
  details: Source Sections4–6 limit timing and improvement results to sampled uniform
    integer distributions, precision and old hardware. Figure6 is100 trials of50 48-bit
    numbers; multiway and discrepancy variants are separate. No arbitrary-instance
    polynomial or runtime guarantee remains.
- assessment_id: constructed-boundaries
  area: consistency
  topic: complementary branch completeness, exact optimality certificates, interrupted
    incumbents, subset-sum reduction and distribution-specific evaluation
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - korf1997
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Ten small exact-integer fixtures compare a constructed CKK-style search
    against exhaustive sign enumeration. The counterexample improves2→0, dominance
    cases attain their bounds, and a search interrupted before exploring children
    retains an uncertified residue2. This is not author-code or performance replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CompleteKarmarkarKarp
  evidence_ids:
  - identity
  - mapping
  - korf1997
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read the entire maintained record and six examined-target
    YAMLs after capture. Reread source pruning, complete difference/sum search, implementation/evaluation,
    anytime improvement and subset-sum reduction pages. All31 manuscript pages were
    read before curation. Checked complementary orientation, admissible bounds, integer
    parity, interrupted-incumbent status and the feasible-target restriction.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 589 native and 442 unchanged generated records.
  The 773-entry main frontier retains 480 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All31 pages of the dated1997 Korf manuscript visually read; final1998 publisher
  metadata corroborated separately, not the final full text. No author code or empirical
  replication.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
