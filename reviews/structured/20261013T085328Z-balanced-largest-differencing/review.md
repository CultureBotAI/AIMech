# Scientific author self-review of Balanced largest differencing method

- Review: 20261013T085328Z-balanced-largest-differencing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T08:46:23Z
- Finished UTC: 2026-10-13T08:53:28Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain balanced largest differencing as a DRAFT algorithm with explicit AIO no-match. Six claims preserve cardinality, heuristic and empirical boundaries; adversarial author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:BalancedLargestDifferencing
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 957d748fc2041b518126094f3a67806c620acd3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BalancedLargestDifferencing | data/curated/BalancedLargestDifferencing.yaml | maintained | Balanced largest differencing method |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:BalancedLargestDifferencing | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 194.05s (0:03:14)<br>Checked 442 record(s); 0 failed.<br>Checked 595 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 254 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 253,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:BalancedLargestDifferencing | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:BalancedLargestDifferencing | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:BalancedLargestDifferencing | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:BalancedLargestDifferencing | {"scope": "Eight fixed integer fixtures and positive scaling; no probabilistic or hardware replication.", "results": [{"values": [8, 7, 6, 5, 4], "balanced_optimum": 0, "residue": 2, "indices": [[4, 1, 3], [0, 2]], "loads": [16, 14], "cardinality_difference": 1, "first_round": [1, 1, 4], "trace": [[1, 1, 4], [1, 3], [2]]}, {"values": [200, 100, 90, 80, 70, 61, 50, 42], "balanced_optimum": 13, "residue": 73, "indices": [[0, 3, 5, 7], [1, 2, 4, 6]], "loads": [383, 310], "cardinality_difference": 0, "first_round": [100, 10, 9, 8], "trace": [[100, 10, 9, 8], [9, 8, 90], [8, 81], [73]]}, {"values": [100, 10, 9, 8], "balanced_optimum": 89, "residue": 89, "indices": [[0, 3], [1, 2]], "loads": [108, 19], "cardinality_difference": 0, "first_round": [90, 1], "trace": [[90, 1], [89]]}, {"values": [9, 8, 7, 6, 5, 4, 3], "balanced_optimum": 0, "residue": 0, "indices": [[4, 0, 2], [5, 6, 1, 3]], "loads": [21, 21], "cardinality_difference": 1, "first_round": [1, 1, 1, 3], "trace": [[1, 1, 1, 3], [1, 1, 2], [1, 1], [0]]}, {"values": [5, 5, 5, 5], "balanced_optimum": 0, "residue": 0, "indices": [[0, 3], [1, 2]], "loads": [10, 10], "cardinality_difference": 0, "first_round": [0, 0], "trace": [[0, 0], [0]]}, {"values": [0, 0, 0], "balanced_optimum": 0, "residue": 0, "indices": [[0], [1, 2]], "loads": [0, 0], "cardinality_difference": 1, "first_round": [0, 0], "trace": [[0, 0], [0]]}, {"values": [9], "balanced_optimum": 9, "residue": 9, "indices": [[0], []], "loads": [9, 0], "cardinality_difference": 1, "first_round": [9], "trace": [[9]]}, {"values": [7, 7], "balanced_optimum": 0, "residue": 0, "indices": [[0], [1]], "loads": [7, 7], "cardinality_difference": 0, "first_round": [0], "trace": [[0]]}], "paired_comparison": {"residue": 89, "indices": [[0, 3, 5, 6], [1, 2, 4, 7]], "loads": [391, 302], "cardinality_difference": 0, "first_round": [100, 10, 9, 8], "trace": [[100, 10, 9, 8], [90, 1], [89]]}} |

## Scientific And Domain Assessments

### Balanced largest differencing method

identity: supported. Targets: AIMech:BalancedLargestDifferencing.

Retain this distinct DRAFT algorithm.

The one-round paired initialization followed by largest-residual operations is the named BLDM heuristic. It differs from PDM repeated rounds and from complete search. Full identity searches include ignored and hidden files in three checkouts.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:BalancedLargestDifferencing.

Explicit no-match assessment is supported.

All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence.

### paired-initialization

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Section 2.1 explicitly applies one PDM phase before LDM. Odd input carries its unpaired item; later operations reorder residuals after each pair. The record does not repeatedly apply PDM rounds.

### cardinality-invariant

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Paired residuals carry signed count zero and at most one unpaired item carries a unit. Every later signed combination therefore preserves absolute final count n mod 2. Indexed zero and duplicate fixtures retain all original items.

### largest-phase-and-reconstruction

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Opposite orientation reconstructs signed sums correctly. The eight-item example gives initial residuals 100,10,9,8, then BLDM73 versus PDM89. Neither this example nor the source is used to assert universal dominance.

### not-an-optimality-certificate

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

The five-weight constructed BLDM result is balanced but has residue2 while exhaustive balanced assignments attain0. Fixed initial opposite-side choices omit feasible partitions; the heuristic provides no optimum certificate.

### resource-cost

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

The source states O(n log n) work and O(n) storage for differencing. The record identifies heap or ordered representation and a merge tree, limits arithmetic to unit cost, and does not use the illustrative copying implementation as a memory benchmark.

### empirical-evidence-scope

evidence: supported. Targets: AIMech:BalancedLargestDifferencing.

Supported within the stated primary-source and mathematical scope.

Figure4 uses 2n-bit uniform inputs scaled by 2^(2n), 1000 trials per point and a conjectural fit. The inaccessible Yakir proof is not used to assert an asymptotic theorem.

### one-round pairing, signed cardinality preservation, reconstruction, nonoptimality and empirical scaling limits

consistency: supported. Targets: AIMech:BalancedLargestDifferencing.

Constructed calculations support the stated distinctions.

Eight indexed exact-integer fixtures verify cardinality balance, original-index coverage and positive scaling. A five-weight example has residue2 versus balanced optimum0; an eight-weight example distinguishes BLDM residue73 from PDM residue89 without claiming universal dominance. No author implementation or statistical experiment.

### All maintained fields

provenance: supported. Targets: AIMech:BalancedLargestDifferencing.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read all maintained fields and six AIO target YAMLs after capture. Reread the paired initialization, signed-cardinality explanation, complete-method distinction and heuristic experiment. Indexed fixtures check original-item coverage, zero residuals, cardinality balance and nonoptimality.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T084439Z-balanced-largest-differencing.json | supports | Compared all 442 pinned AIO and 593 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 54, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 67 AIO and 100 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. BLDM fixes one initial round of adjacent sorted pairs, then uses largest-residual differencing. This differs from PDM whole rounds throughout, unconstrained LDM/KK, and complete balanced or unconstrained search. Existing text hits are prior records and pending leads, not an existing identity. The fully inspected AIO contexts have no suitable counterpart. |
| mapping | sources/aio/aio.json | supports | All six complete AIO nodes, edges and generated YAMLs were inspected. None denotes this nonlearning number-partitioning procedure. The explicit aio_no_match preserves each rejection rationale rather than asserting a function, task or language-model equivalence. |
| mertens1999 | https://arxiv.org/pdf/cs/9903011v1; All 12 Mertens preprint pages read before curation, selected pages reread after capture. Yakir publisher metadata and abstract read but its PDF returned HTTP403; no full asymptotic proof, author-code or statistical replication. | supports | All 12 pages of the arXiv cs/9903011v1 PDF read. The margin and primary abstract identify submission on 11 March 1999; the downloaded PDF footer says 26 November 2024. The footer is not treated as the original publication date. Locators are PDF/printed pages 1–12; no later journal version or author implementation inspected. |
| calculation | research/discovery/balanced-largest-differencing-boundaries.py | supports | Eight indexed exact-integer fixtures verify cardinality balance, original-index coverage and positive scaling. A five-weight example has residue2 versus balanced optimum0; an eight-weight example distinguishes BLDM residue73 from PDM residue89 without claiming universal dominance. No author implementation or statistical experiment. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 594 native and 442 unchanged generated records. The 778-entry main frontier retains 480 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 12 Mertens preprint pages visually read, including pseudocode, five figures, experiment details and references. Yakir primary metadata and abstract were inspected, but the public publisher PDF returned HTTP403; full proof and author implementations were not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T085328Z-balanced-largest-differencing
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Balanced largest differencing method
started_at: '2026-10-13T08:46:23Z'
finished_at: '2026-10-13T08:53:28Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged one-round pairing, signed cardinality
    preservation, reconstruction, nonoptimality and empirical scaling limits. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain balanced largest differencing as a DRAFT algorithm with explicit AIO
  no-match. Six claims preserve cardinality, heuristic and empirical boundaries; adversarial
  author self-review found no actionable defect.
source:
  git_revision: 957d748fc2041b518126094f3a67806c620acd3b
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
  - path: data/curated/BalancedLargestDifferencing.yaml
    sha256: 06a914d365f65b2d26a4d9103a22f7f282441fa6478769e83986e352c2b5f607
    role: target
  - path: data/curated/CompleteGreedyNumberPartitioning.yaml
    sha256: 449aea6d4207da9e65e090c87cb49235af72c91d33deb0ac30525cdfdb7b3ebb
    role: context
  - path: data/curated/CompleteKarmarkarKarp.yaml
    sha256: 65431bae97ba1ebb9e38b2a17a9b59fcc156087167173faf88308b5f38fddcca
    role: context
  - path: data/curated/KarmarkarKarpDifferencing.yaml
    sha256: 3bfbfa6fc45fe53b3bda3c61ace7e2beb7d39b8dec3ee93b360d5cfe0d6afdfc
    role: context
  - path: data/curated/PairedDifferencing.yaml
    sha256: cf97c997c3654cf14d15b791faa92658e38b98a07751735e92f1de06aed035c0
    role: context
  - path: research/discovery/20261013T084439Z-balanced-largest-differencing.json
    sha256: c4e0ede7999aa025fbc93aded2eb5f543e73c49fd2b8035703b31584b2edcfd5
    role: context
  - path: research/discovery/balanced-largest-differencing-boundaries.py
    sha256: 4a17bd1b8f9fe2e27cf62cc7ed89d6306ee6552d0c4104cd8bd0f71757ee8d43
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
- target_id: AIMech:BalancedLargestDifferencing
  path: data/curated/BalancedLargestDifferencing.yaml
  label: Balanced largest differencing method
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BalancedLargestDifferencing.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:BalancedLargestDifferencing'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BalancedLargestDifferencing
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All 12 Mertens preprint pages read before curation, selected pages reread
      after capture. Yakir publisher metadata and abstract read but its PDF returned
      HTTP403; no full asymptotic proof, author-code or statistical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:BalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 194.05s (0:03:14)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 595 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 254 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 253,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:BalancedLargestDifferencing
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
  - AIMech:BalancedLargestDifferencing
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
  - AIMech:BalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/balanced-largest-differencing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:BalancedLargestDifferencing
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Eight fixed integer fixtures and positive scaling; no probabilistic
    or hardware replication.", "results": [{"values": [8, 7, 6, 5, 4], "balanced_optimum":
    0, "residue": 2, "indices": [[4, 1, 3], [0, 2]], "loads": [16, 14], "cardinality_difference":
    1, "first_round": [1, 1, 4], "trace": [[1, 1, 4], [1, 3], [2]]}, {"values": [200,
    100, 90, 80, 70, 61, 50, 42], "balanced_optimum": 13, "residue": 73, "indices":
    [[0, 3, 5, 7], [1, 2, 4, 6]], "loads": [383, 310], "cardinality_difference": 0,
    "first_round": [100, 10, 9, 8], "trace": [[100, 10, 9, 8], [9, 8, 90], [8, 81],
    [73]]}, {"values": [100, 10, 9, 8], "balanced_optimum": 89, "residue": 89, "indices":
    [[0, 3], [1, 2]], "loads": [108, 19], "cardinality_difference": 0, "first_round":
    [90, 1], "trace": [[90, 1], [89]]}, {"values": [9, 8, 7, 6, 5, 4, 3], "balanced_optimum":
    0, "residue": 0, "indices": [[4, 0, 2], [5, 6, 1, 3]], "loads": [21, 21], "cardinality_difference":
    1, "first_round": [1, 1, 1, 3], "trace": [[1, 1, 1, 3], [1, 1, 2], [1, 1], [0]]},
    {"values": [5, 5, 5, 5], "balanced_optimum": 0, "residue": 0, "indices": [[0,
    3], [1, 2]], "loads": [10, 10], "cardinality_difference": 0, "first_round": [0,
    0], "trace": [[0, 0], [0]]}, {"values": [0, 0, 0], "balanced_optimum": 0, "residue":
    0, "indices": [[0], [1, 2]], "loads": [0, 0], "cardinality_difference": 1, "first_round":
    [0, 0], "trace": [[0, 0], [0]]}, {"values": [9], "balanced_optimum": 9, "residue":
    9, "indices": [[0], []], "loads": [9, 0], "cardinality_difference": 1, "first_round":
    [9], "trace": [[9]]}, {"values": [7, 7], "balanced_optimum": 0, "residue": 0,
    "indices": [[0], [1]], "loads": [7, 7], "cardinality_difference": 0, "first_round":
    [0], "trace": [[0]]}], "paired_comparison": {"residue": 89, "indices": [[0, 3,
    5, 6], [1, 2, 4, 7]], "loads": [391, 302], "cardinality_difference": 0, "first_round":
    [100, 10, 9, 8], "trace": [[100, 10, 9, 8], [90, 1], [89]]}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T084439Z-balanced-largest-differencing.json
  accessed_at: '2026-10-13T08:46:23Z'
  support: supports
  summary: Compared all 442 pinned AIO and 593 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    54, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 67 AIO and 100 native definitions, with every matched definition read.
    6 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. BLDM fixes one initial round of adjacent sorted pairs, then uses largest-residual
    differencing. This differs from PDM whole rounds throughout, unconstrained LDM/KK,
    and complete balanced or unconstrained search. Existing text hits are prior records
    and pending leads, not an existing identity. The fully inspected AIO contexts
    have no suitable counterpart.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T08:46:23Z'
  support: supports
  summary: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- evidence_id: mertens1999
  kind: primary_source
  reference: https://arxiv.org/pdf/cs/9903011v1
  locator: All 12 Mertens preprint pages read before curation, selected pages reread
    after capture. Yakir publisher metadata and abstract read but its PDF returned
    HTTP403; no full asymptotic proof, author-code or statistical replication.
  accessed_at: '2026-10-13T08:05:53Z'
  snapshot_sha256: fe0bcf132782ff8d59c7888b6ea0a7aae195bc3df69dddc728cc842a8258ecd3
  support: supports
  summary: All 12 pages of the arXiv cs/9903011v1 PDF read. The margin and primary
    abstract identify submission on 11 March 1999; the downloaded PDF footer says
    26 November 2024. The footer is not treated as the original publication date.
    Locators are PDF/printed pages 1–12; no later journal version or author implementation
    inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/balanced-largest-differencing-boundaries.py
  accessed_at: '2026-10-13T08:47:02Z'
  snapshot_sha256: 4a17bd1b8f9fe2e27cf62cc7ed89d6306ee6552d0c4104cd8bd0f71757ee8d43
  support: supports
  summary: Eight indexed exact-integer fixtures verify cardinality balance, original-index
    coverage and positive scaling. A five-weight example has residue2 versus balanced
    optimum0; an eight-weight example distinguishes BLDM residue73 from PDM residue89
    without claiming universal dominance. No author implementation or statistical
    experiment.
assessments:
- assessment_id: identity
  area: identity
  topic: Balanced largest differencing method
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - identity
  - mertens1999
  summary: Retain this distinct DRAFT algorithm.
  details: The one-round paired initialization followed by largest-residual operations
    is the named BLDM heuristic. It differs from PDM repeated rounds and from complete
    search. Full identity searches include ignored and hidden files in three checkouts.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mapping
  - mertens1999
  summary: Explicit no-match assessment is supported.
  details: All six complete AIO nodes, edges and generated YAMLs were inspected. None
    denotes this nonlearning number-partitioning procedure. The explicit aio_no_match
    preserves each rejection rationale rather than asserting a function, task or language-model
    equivalence.
- assessment_id: paired-initialization
  area: evidence
  topic: paired-initialization
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section 2.1 explicitly applies one PDM phase before LDM. Odd input carries
    its unpaired item; later operations reorder residuals after each pair. The record
    does not repeatedly apply PDM rounds.
- assessment_id: cardinality-invariant
  area: evidence
  topic: cardinality-invariant
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Paired residuals carry signed count zero and at most one unpaired item
    carries a unit. Every later signed combination therefore preserves absolute final
    count n mod 2. Indexed zero and duplicate fixtures retain all original items.
- assessment_id: largest-phase-and-reconstruction
  area: evidence
  topic: largest-phase-and-reconstruction
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Opposite orientation reconstructs signed sums correctly. The eight-item
    example gives initial residuals 100,10,9,8, then BLDM73 versus PDM89. Neither
    this example nor the source is used to assert universal dominance.
- assessment_id: not-an-optimality-certificate
  area: evidence
  topic: not-an-optimality-certificate
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The five-weight constructed BLDM result is balanced but has residue2 while
    exhaustive balanced assignments attain0. Fixed initial opposite-side choices omit
    feasible partitions; the heuristic provides no optimum certificate.
- assessment_id: resource-cost
  area: evidence
  topic: resource-cost
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source states O(n log n) work and O(n) storage for differencing. The
    record identifies heap or ordered representation and a merge tree, limits arithmetic
    to unit cost, and does not use the illustrative copying implementation as a memory
    benchmark.
- assessment_id: empirical-evidence-scope
  area: evidence
  topic: empirical-evidence-scope
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure4 uses 2n-bit uniform inputs scaled by 2^(2n), 1000 trials per point
    and a conjectural fit. The inaccessible Yakir proof is not used to assert an asymptotic
    theorem.
- assessment_id: constructed-boundaries
  area: consistency
  topic: one-round pairing, signed cardinality preservation, reconstruction, nonoptimality
    and empirical scaling limits
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - mertens1999
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Eight indexed exact-integer fixtures verify cardinality balance, original-index
    coverage and positive scaling. A five-weight example has residue2 versus balanced
    optimum0; an eight-weight example distinguishes BLDM residue73 from PDM residue89
    without claiming universal dominance. No author implementation or statistical
    experiment.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:BalancedLargestDifferencing
  evidence_ids:
  - identity
  - mapping
  - mertens1999
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read all maintained fields and six AIO target YAMLs
    after capture. Reread the paired initialization, signed-cardinality explanation,
    complete-method distinction and heuristic experiment. Indexed fixtures check original-item
    coverage, zero residuals, cardinality balance and nonoptimality.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 594 native and 442 unchanged generated records.
  The 778-entry main frontier retains 480 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All 12 Mertens preprint pages visually read, including pseudocode, five figures,
  experiment details and references. Yakir primary metadata and abstract were inspected,
  but the public publisher PDF returned HTTP403; full proof and author implementations
  were not inspected.
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
