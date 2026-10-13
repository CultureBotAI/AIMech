# Scientific author self-review of Batch reciprocal-nearest-neighbor agglomeration

- Review: 20261013T215940Z-batch-reciprocal-nearest-neighbor-clustering
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T21:54:09Z
- Finished UTC: 2026-10-13T21:59:40Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain batch reciprocal-nearest-neighbor agglomeration as a DRAFT algorithm with related AIO clustering mappings. Author self-review supports the batch procedure while preserving tie, criterion, output-order, repeated-scan, source-notation and historical-evaluation limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:BatchReciprocalNearestNeighborClustering
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base dd9bc520ed85889862052e3b49ca6ee08252354f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BatchReciprocalNearestNeighborClustering | data/curated/BatchReciprocalNearestNeighborClustering.yaml | maintained | Batch reciprocal-nearest-neighbor agglomeration |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:BatchReciprocalNearestNeighborClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 157.37s (0:02:37)<br>Checked 442 record(s); 0 failed.<br>Checked 654 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 335 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 332,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:BatchReciprocalNearestNeighborClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:BatchReciprocalNearestNeighborClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:BatchReciprocalNearestNeighborClustering | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:BatchReciprocalNearestNeighborClustering | {"matrix_cases": {"distinct_initial": 2880, "ties_allowed": 2916}, "overlapping_ties": [{"active": 3, "reciprocal_pairs": 3, "disjoint_merges": 1}, {"active": 2, "reciprocal_pairs": 1, "disjoint_merges": 1}], "equal_minima_counterexample": {"nearest_minimum": 1, "cross_pair_distance": 5}, "one_pair_per_pass": [{"active": 8, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 7, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 6, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 5, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 4, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 3, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 2, "reciprocal_pairs": 1, "disjoint_merges": 1}], "source_six_point_ward": {"raw": [{"left": [0], "right": [1], "height": "125"}, {"left": [2], "right": [3], "height": "250"}, {"left": [4], "right": [5], "height": "425/2"}, {"left": [0, 1], "right": [4, 5], "height": "5525/4"}, {"left": [0, 1, 4, 5], "right": [2, 3], "height": "19225/12"}], "sorted": [{"left": [0], "right": [1], "height": "125"}, {"left": [4], "right": [5], "height": "425/2"}, {"left": [2], "right": [3], "height": "250"}, {"left": [0, 1], "right": [4, 5], "height": "5525/4"}, {"left": [0, 1, 4, 5], "right": [2, 3], "height": "19225/12"}], "rounds": [{"active": 6, "reciprocal_pairs": 3, "disjoint_merges": 3}, {"active": 3, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 2, "reciprocal_pairs": 1, "disjoint_merges": 1}]}, "limits": "Finite rational checks of a curator implementation. Lexicographic disjoint matching is an explicit tie extension, not specified by deRham. No author code, timing or universal correctness proof."} |

## Scientific And Domain Assessments

### Batch reciprocal-nearest-neighbor agglomeration

identity: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Retain this distinct DRAFT algorithm.

Retain repeated global reciprocal-pair passes as a distinct merge-search procedure. It is not the Ward linkage criterion, the later reusable NN-chain, generic lower-bound recertification or nearest-neighbor label voting. Identity/context references are not assertions of algorithm equivalence.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

The declared AIO mapping is supported.

Related hierarchical and unsupervised clustering targets describe the task served without asserting algorithm/task equivalence. Nine full annotated AIO contexts and four native algorithm records were inspected; neighbor-voting classification and learned neural metric representations do not identify this procedure.

### reciprocal-batch-passes

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

The introduction and algorithm explicitly alternate reciprocal-pair search and batch merging. The record uses the correct mutual-membership definition; equal minima without attaining the pair distance fail in a four-point example. Logical batching does not assert a parallel implementation.

### matrix-distance-updates

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

The original extends the linkage recurrence to two newly merged endpoint clusters. The exact rational reference sequentially updates disjoint pairs and validates stable-ordered output against all current pairs in5,796 four-object cases across four linkage rules; it does not claim literal execution of the source pseudocode.

### vector-realization

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

The source’s vector realization updates centroids and weights for its coordinate-compatible strategies and reports N(K+5) words of implementation storage. This is distinct from eliminating distance evaluations or claiming linear memory for all batch implementations.

### criterion-and-tie-scope

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

The source differentiates named monotone criteria from centroid heuristics. An all-equal three-object example yields three overlapping reciprocal pairs; the reference uses an explicit disjoint matching that is not attributed to the paper. General reducibility alone is not adopted as a universal history-dependent update guarantee.

### passes-and-output-boundaries

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

Benzecri identifies one-pair-per-pass behavior as a weakness of the predecessor batch method. An eight-object complete-link construction makes seven such passes. The six-point Ward source example also gives non-sorted first-batch heights; the finite check validates a stable ordered sequence and preserves the rounded-versus-exact distinction.

### historical-evaluation-scope

evidence: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Supported within the stated primary-source and mathematical scope.

The table uses32/64/128 two-variable synthetic hierarchies on a CDC6500, reporting milliseconds and words. Different strategy denominators for BASE/DIST and DONN prevent an unconditional ranking; no timing was reproduced.

### batch identity, reciprocal-pair definition, tied overlaps, finite merge admissibility, historical cost scales and repeated global scans

consistency: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Constructed calculations support the stated distinctions.

A curator reference checks2,880 four-object cases with distinct initial distances and2,916 with ties across four linkages, plus the source six-point Ward example. Explicit disjoint tie matching is a curator extension. Equal minima alone fail reciprocity; three equidistant points produce overlapping pairs. An eight-object complete-link example yields only one pair per pass. Exact source ESS heights are125,212.5,250,1381.25,19225/12. No author program, timing or universal proof.

### All maintained fields

provenance: supported. Targets: AIMech:BatchReciprocalNearestNeighborClustering.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all names, aliases, kind, definition/locators, six claims, three source identities/versions/access/hashes, related/rejected mappings, mutual-membership versus malformed shortcuts, disjoint tie interpretation, matrix/vector distinction, criterion scope, exact versus rounded example costs, repeated passes and historical workload differences. DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T215358Z-batch-reciprocal-nearest-neighbor-clustering.json | supports | Compared all 442 pinned AIO and 653 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 57, 0, 0 lines. All distinct match contents were read, including generated index rows repeating the fully read corrected nearest-neighbor-chain record. Recovery hits concern shared primary-source references, chain implementation context or pending batch-procedure discovery notes; none identifies an existing standalone batch record. Both other checkouts returned no matches including ignored and hidden files. Semantic matching covered 26 AIO and 170 native definitions, all read; unchanged definitions were byte-compared with the preceding full assessment. 9 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Retain the two-phase batch reciprocal-pair search from deRham1980. It differs from a linkage criterion, a reusable nearest-neighbor chain, globally certified cached-bound selection and nearest-neighbor label voting. The later RS pruning/representative method has a different procedure and remains a separate lead. |
| mapping | sources/aio/aio.json | supports | Related hierarchical and unsupervised clustering targets describe the task served without asserting algorithm/task equivalence. Nine full annotated AIO contexts and four native algorithm records were inspected; neighbor-voting classification and learned neural metric representations do not identify this procedure. |
| derham1980 | https://www.numdam.org/item/CAD_1980__5_2_135_0.pdf; Introduction and Sections2.3,3.2, printedpp135,137,140 / PDFpp2,4,7; Sections2.1,3.1–3.3, printedpp136,139–140 / PDFpp3,6–7; Sections4.1–4.2 and5, printedpp141–143 / PDFpp8–10; Introduction, Sections2.1,2.3,3.2 and4.1, printedpp135–137,140–141 / PDFpp2–4,7–8; Section3.3, printedp140 / PDFp7; Section5 and comparison table, printedp143 / PDFp10 | supports | Les Cahiers de l’analyse des données5(2),1980,pp.135–144. Eleven scanned PDF pages including cover, all visually read. |
| benzecri1982 | https://www.numdam.org/item/CAD_1982__7_2_209_0.pdf; Section1, printedpp209–210 / PDFpp2–3 | supports | Les Cahiers de l’analyse des données7(2),1982,pp.209–218. Eleven scanned PDF pages including cover, all visually read. |
| mullner2011 | https://arxiv.org/pdf/1109.2378v1; Section3.2, Theorem1 and footnote1, PDFpp12–16: limits of general reciprocal-pair arguments; Sections2.2 and3.2, PDFpp4–5,11–16 | supports | arXiv1109.2378v1,12September2011; all29 PDF pages visually read. |
| calculation | research/discovery/batch-reciprocal-neighbor-boundaries.py | supports | A curator reference checks2,880 four-object cases with distinct initial distances and2,916 with ties across four linkages, plus the source six-point Ward example. Explicit disjoint tie matching is a curator extension. Equal minima alone fail reciprocity; three equidistant points produce overlapping pairs. An eight-object complete-link example yields only one pair per pass. Exact source ESS heights are125,212.5,250,1381.25,19225/12. No author program, timing or universal proof. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 654 native and 442 unchanged generated records. The 839-entry main frontier retains 473 pending and 58 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All11 pages of deRham1980,11 of Benzecri1982 and29 of Mullner2011v1 visually read. Source boundary checks are curator-written, with no author execution.
- No author-code execution, training, paid service, hardware measurement or empirical replication. The complete cited printed sources were read; historical experiments and floating-point behavior were not reproduced. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T215940Z-batch-reciprocal-nearest-neighbor-clustering
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Batch reciprocal-nearest-neighbor agglomeration
started_at: '2026-10-13T21:54:09Z'
finished_at: '2026-10-13T21:59:40Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged batch identity, reciprocal-pair definition,
    tied overlaps, finite merge admissibility, historical cost scales and repeated
    global scans. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain batch reciprocal-nearest-neighbor agglomeration as a DRAFT algorithm
  with related AIO clustering mappings. Author self-review supports the batch procedure
  while preserving tie, criterion, output-order, repeated-scan, source-notation and
  historical-evaluation limits.
source:
  git_revision: dd9bc520ed85889862052e3b49ca6ee08252354f
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/BatchReciprocalNearestNeighborClustering.yaml
    sha256: aa195a0676822c921f7e0d8a130797180c6df6a38c21ebea2c551b064956ad49
    role: target
  - path: data/curated/GenericLazyNeighborAgglomerativeClustering.yaml
    sha256: b7497e08e16cdc9b30d8566c492f668dd76295fd7878dbf05b191317ba3926b9
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/NearestNeighborChainClustering.yaml
    sha256: 29edd6535409cbf8a1fb3c806de4d52f0f33473d597439c40af4c895fa49746a
    role: context
  - path: data/curated/WardMinimumVarianceClustering.yaml
    sha256: cd8fbbb8257329683eeafb2a453da362175e4df0371d393e699a887b06f95c4c
    role: context
  - path: research/discovery/20261013T215358Z-batch-reciprocal-nearest-neighbor-clustering.json
    sha256: 592c62dcd8b8aa4875184b1c7ea8aee2419b0ed683f4da46710ed5c1324a9589
    role: context
  - path: research/discovery/batch-reciprocal-neighbor-boundaries.py
    sha256: 043607807a94667b34ce893b044ec976118636d8184527683ebcc8144147291d
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
- target_id: AIMech:BatchReciprocalNearestNeighborClustering
  path: data/curated/BatchReciprocalNearestNeighborClustering.yaml
  label: Batch reciprocal-nearest-neighbor agglomeration
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BatchReciprocalNearestNeighborClustering.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:BatchReciprocalNearestNeighborClustering'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete cited primary texts visually read; finite curator calculations
      only. No historical author program, modern implementation, benchmark or floating-point
      audit. Curator disjoint matching is an explicit tie extension; finite admissibility
      checks do not establish all linkages or all inputs.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 157.37s (0:02:37)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 654 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 335 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 332,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
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
  - AIMech:BatchReciprocalNearestNeighborClustering
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
  - AIMech:BatchReciprocalNearestNeighborClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/batch-reciprocal-neighbor-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"matrix_cases": {"distinct_initial": 2880, "ties_allowed": 2916}, "overlapping_ties":
    [{"active": 3, "reciprocal_pairs": 3, "disjoint_merges": 1}, {"active": 2, "reciprocal_pairs":
    1, "disjoint_merges": 1}], "equal_minima_counterexample": {"nearest_minimum":
    1, "cross_pair_distance": 5}, "one_pair_per_pass": [{"active": 8, "reciprocal_pairs":
    1, "disjoint_merges": 1}, {"active": 7, "reciprocal_pairs": 1, "disjoint_merges":
    1}, {"active": 6, "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 5,
    "reciprocal_pairs": 1, "disjoint_merges": 1}, {"active": 4, "reciprocal_pairs":
    1, "disjoint_merges": 1}, {"active": 3, "reciprocal_pairs": 1, "disjoint_merges":
    1}, {"active": 2, "reciprocal_pairs": 1, "disjoint_merges": 1}], "source_six_point_ward":
    {"raw": [{"left": [0], "right": [1], "height": "125"}, {"left": [2], "right":
    [3], "height": "250"}, {"left": [4], "right": [5], "height": "425/2"}, {"left":
    [0, 1], "right": [4, 5], "height": "5525/4"}, {"left": [0, 1, 4, 5], "right":
    [2, 3], "height": "19225/12"}], "sorted": [{"left": [0], "right": [1], "height":
    "125"}, {"left": [4], "right": [5], "height": "425/2"}, {"left": [2], "right":
    [3], "height": "250"}, {"left": [0, 1], "right": [4, 5], "height": "5525/4"},
    {"left": [0, 1, 4, 5], "right": [2, 3], "height": "19225/12"}], "rounds": [{"active":
    6, "reciprocal_pairs": 3, "disjoint_merges": 3}, {"active": 3, "reciprocal_pairs":
    1, "disjoint_merges": 1}, {"active": 2, "reciprocal_pairs": 1, "disjoint_merges":
    1}]}, "limits": "Finite rational checks of a curator implementation. Lexicographic
    disjoint matching is an explicit tie extension, not specified by deRham. No author
    code, timing or universal correctness proof."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T215358Z-batch-reciprocal-nearest-neighbor-clustering.json
  accessed_at: '2026-10-13T21:54:09Z'
  support: supports
  summary: Compared all 442 pinned AIO and 653 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    57, 0, 0 lines. All distinct match contents were read, including generated index
    rows repeating the fully read corrected nearest-neighbor-chain record. Recovery
    hits concern shared primary-source references, chain implementation context or
    pending batch-procedure discovery notes; none identifies an existing standalone
    batch record. Both other checkouts returned no matches including ignored and hidden
    files. Semantic matching covered 26 AIO and 170 native definitions, all read;
    unchanged definitions were byte-compared with the preceding full assessment. 9
    full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. Retain the two-phase batch reciprocal-pair search from deRham1980.
    It differs from a linkage criterion, a reusable nearest-neighbor chain, globally
    certified cached-bound selection and nearest-neighbor label voting. The later
    RS pruning/representative method has a different procedure and remains a separate
    lead.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T21:54:09Z'
  support: supports
  summary: Related hierarchical and unsupervised clustering targets describe the task
    served without asserting algorithm/task equivalence. Nine full annotated AIO contexts
    and four native algorithm records were inspected; neighbor-voting classification
    and learned neural metric representations do not identify this procedure.
- evidence_id: derham1980
  kind: primary_source
  reference: https://www.numdam.org/item/CAD_1980__5_2_135_0.pdf
  locator: Introduction and Sections2.3,3.2, printedpp135,137,140 / PDFpp2,4,7; Sections2.1,3.1–3.3,
    printedpp136,139–140 / PDFpp3,6–7; Sections4.1–4.2 and5, printedpp141–143 / PDFpp8–10;
    Introduction, Sections2.1,2.3,3.2 and4.1, printedpp135–137,140–141 / PDFpp2–4,7–8;
    Section3.3, printedp140 / PDFp7; Section5 and comparison table, printedp143 /
    PDFp10
  accessed_at: '2026-10-13T20:51:05Z'
  snapshot_sha256: c62314df59e7eb3f64e36d7cf141711233493b241ac8939f272d708fa045d0b3
  support: supports
  summary: Les Cahiers de l’analyse des données5(2),1980,pp.135–144. Eleven scanned
    PDF pages including cover, all visually read.
- evidence_id: benzecri1982
  kind: primary_source
  reference: https://www.numdam.org/item/CAD_1982__7_2_209_0.pdf
  locator: Section1, printedpp209–210 / PDFpp2–3
  accessed_at: '2026-10-13T20:51:05Z'
  snapshot_sha256: 2569b4b21a2e3ed5d20f7b50e5164fd37ba02be5ea90d683d711246adea98b58
  support: supports
  summary: Les Cahiers de l’analyse des données7(2),1982,pp.209–218. Eleven scanned
    PDF pages including cover, all visually read.
- evidence_id: mullner2011
  kind: primary_source
  reference: https://arxiv.org/pdf/1109.2378v1
  locator: 'Section3.2, Theorem1 and footnote1, PDFpp12–16: limits of general reciprocal-pair
    arguments; Sections2.2 and3.2, PDFpp4–5,11–16'
  accessed_at: '2026-10-13T20:51:04Z'
  snapshot_sha256: 3d8ea802c328a9dfada44e1c7a4c4824086c1210b45a4b99b5b9801435934dae
  support: supports
  summary: arXiv1109.2378v1,12September2011; all29 PDF pages visually read.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/batch-reciprocal-neighbor-boundaries.py
  accessed_at: '2026-10-13T21:54:36Z'
  snapshot_sha256: 043607807a94667b34ce893b044ec976118636d8184527683ebcc8144147291d
  support: supports
  summary: A curator reference checks2,880 four-object cases with distinct initial
    distances and2,916 with ties across four linkages, plus the source six-point Ward
    example. Explicit disjoint tie matching is a curator extension. Equal minima alone
    fail reciprocity; three equidistant points produce overlapping pairs. An eight-object
    complete-link example yields only one pair per pass. Exact source ESS heights
    are125,212.5,250,1381.25,19225/12. No author program, timing or universal proof.
assessments:
- assessment_id: identity
  area: identity
  topic: Batch reciprocal-nearest-neighbor agglomeration
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - identity
  - derham1980
  - benzecri1982
  - mullner2011
  summary: Retain this distinct DRAFT algorithm.
  details: Retain repeated global reciprocal-pair passes as a distinct merge-search
    procedure. It is not the Ward linkage criterion, the later reusable NN-chain,
    generic lower-bound recertification or nearest-neighbor label voting. Identity/context
    references are not assertions of algorithm equivalence.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - mapping
  - derham1980
  - benzecri1982
  - mullner2011
  summary: The declared AIO mapping is supported.
  details: Related hierarchical and unsupervised clustering targets describe the task
    served without asserting algorithm/task equivalence. Nine full annotated AIO contexts
    and four native algorithm records were inspected; neighbor-voting classification
    and learned neural metric representations do not identify this procedure.
- assessment_id: reciprocal-batch-passes
  area: evidence
  topic: reciprocal-batch-passes
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The introduction and algorithm explicitly alternate reciprocal-pair search
    and batch merging. The record uses the correct mutual-membership definition; equal
    minima without attaining the pair distance fail in a four-point example. Logical
    batching does not assert a parallel implementation.
- assessment_id: matrix-distance-updates
  area: evidence
  topic: matrix-distance-updates
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The original extends the linkage recurrence to two newly merged endpoint
    clusters. The exact rational reference sequentially updates disjoint pairs and
    validates stable-ordered output against all current pairs in5,796 four-object
    cases across four linkage rules; it does not claim literal execution of the source
    pseudocode.
- assessment_id: vector-realization
  area: evidence
  topic: vector-realization
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source’s vector realization updates centroids and weights for its coordinate-compatible
    strategies and reports N(K+5) words of implementation storage. This is distinct
    from eliminating distance evaluations or claiming linear memory for all batch
    implementations.
- assessment_id: criterion-and-tie-scope
  area: evidence
  topic: criterion-and-tie-scope
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  - mullner2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source differentiates named monotone criteria from centroid heuristics.
    An all-equal three-object example yields three overlapping reciprocal pairs; the
    reference uses an explicit disjoint matching that is not attributed to the paper.
    General reducibility alone is not adopted as a universal history-dependent update
    guarantee.
- assessment_id: passes-and-output-boundaries
  area: evidence
  topic: passes-and-output-boundaries
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - benzecri1982
  - derham1980
  - mullner2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Benzecri identifies one-pair-per-pass behavior as a weakness of the predecessor
    batch method. An eight-object complete-link construction makes seven such passes.
    The six-point Ward source example also gives non-sorted first-batch heights; the
    finite check validates a stable ordered sequence and preserves the rounded-versus-exact
    distinction.
- assessment_id: historical-evaluation-scope
  area: evidence
  topic: historical-evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  summary: Supported within the stated primary-source and mathematical scope.
  details: The table uses32/64/128 two-variable synthetic hierarchies on a CDC6500,
    reporting milliseconds and words. Different strategy denominators for BASE/DIST
    and DONN prevent an unconditional ranking; no timing was reproduced.
- assessment_id: constructed-boundaries
  area: consistency
  topic: batch identity, reciprocal-pair definition, tied overlaps, finite merge admissibility,
    historical cost scales and repeated global scans
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - derham1980
  - benzecri1982
  - mullner2011
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: A curator reference checks2,880 four-object cases with distinct initial
    distances and2,916 with ties across four linkages, plus the source six-point Ward
    example. Explicit disjoint tie matching is a curator extension. Equal minima alone
    fail reciprocity; three equidistant points produce overlapping pairs. An eight-object
    complete-link example yields only one pair per pass. Exact source ESS heights
    are125,212.5,250,1381.25,19225/12. No author program, timing or universal proof.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:BatchReciprocalNearestNeighborClustering
  evidence_ids:
  - identity
  - mapping
  - derham1980
  - benzecri1982
  - mullner2011
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all names, aliases, kind, definition/locators,
    six claims, three source identities/versions/access/hashes, related/rejected mappings,
    mutual-membership versus malformed shortcuts, disjoint tie interpretation, matrix/vector
    distinction, criterion scope, exact versus rounded example costs, repeated passes
    and historical workload differences. DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 654 native and 442 unchanged generated records.
  The 839-entry main frontier retains 473 pending and 58 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All11 pages of deRham1980,11 of Benzecri1982 and29 of Mullner2011v1 visually read.
  Source boundary checks are curator-written, with no author execution.
- No author-code execution, training, paid service, hardware measurement or empirical
  replication. The complete cited printed sources were read; historical experiments
  and floating-point behavior were not reproduced. Constructed checks test stated
  boundaries only.
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
