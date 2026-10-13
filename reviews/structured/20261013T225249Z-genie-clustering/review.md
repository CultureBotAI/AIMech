# Scientific author self-review of Genie clustering

- Review: 20261013T225249Z-genie-clustering
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T22:47:46Z
- Finished UTC: 2026-10-13T22:52:49Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain original Genie clustering as a DRAFT native algorithm with related AIO task mappings. Author self-review supports the formal merge rule while preserving source-example, threshold, plotting-height, implementation and evaluation boundaries.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:GenieClustering
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 699a153ef5b22c4f5a80a0751fc73895d23858b5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GenieClustering | data/curated/GenieClustering.yaml | maintained | Genie clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GenieClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 139.68s (0:02:19)<br>Checked 442 record(s); 0 failed.<br>Checked 657 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 338 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 335,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GenieClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GenieClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GenieClustering | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:GenieClustering | {"distinct_weight_cases": 2880, "tied_weight_cases": 2916, "scope": "Four-point symmetric nonnegative dissimilarities: 720 edge permutations and 729 three-valued assignments, each at four thresholds. The MST choices satisfy the full eligible-pair minimum; distinct-weight traces agree exactly. Gini incremental updates agree with direct pair-sum recomputation. This is finite verification, not a universal proof.", "paper_example": {"points": [0, 1, 3, 6, 10], "threshold": "3/10", "trace": [{"edge": [0, 1], "distance": "1", "forced": false, "gini_before": "0", "gini_after": "1/5", "partition": [[0, 1], [2], [3], [4]]}, {"edge": [1, 2], "distance": "2", "forced": false, "gini_before": "1/5", "gini_after": "2/5", "partition": [[0, 1, 2], [3], [4]]}, {"edge": [2, 3], "distance": "3", "forced": true, "gini_before": "2/5", "gini_after": "3/5", "partition": [[0, 1, 2, 3], [4]]}, {"edge": [3, 4], "distance": "4", "forced": true, "gini_before": "3/5", "gini_after": null, "partition": [[0, 1, 2, 3, 4]]}], "assessment": "The printed OR eligibility rule and statically inspected Genie1.0.0 merge predicate choose distance3 at the third merge. The paper Example1 instead claims distance4 and partition {0,1,2}/{3,4}; that claim does not follow from its stated rule. No author program was executed."}, "inversion": {"points": [0, 1, 10, 12, 100], "threshold": "3/20", "trace": [{"edge": [0, 1], "distance": "1", "forced": false, "gini_before": "0", "gini_after": "1/5", "partition": [[0, 1], [2], [3], [4]]}, {"edge": [2, 3], "distance": "2", "forced": true, "gini_before": "1/5", "gini_after": "1/5", "partition": [[0, 1], [2, 3], [4]]}, {"edge": [3, 4], "distance": "88", "forced": true, "gini_before": "1/5", "gini_after": "1/5", "partition": [[0, 1], [2, 3, 4]]}, {"edge": [1, 2], "distance": "9", "forced": true, "gini_before": "1/5", "gini_after": null, "partition": [[0, 1, 2, 3, 4]]}]}, "limits": "Curator reference only. No author R/C++ execution, floating-point certification, benchmark reproduction, universal tie equivalence or outlier-recovery guarantee."} |

## Scientific And Domain Assessments

### Genie clustering

identity: supported. Targets: AIMech:GenieClustering.

Retain this distinct DRAFT algorithm.

Retain the original inequality-triggered single-link algorithm, distinct from fixed-linkage NN-chain, cached-bound search, Ward ESS, BIRCH compression and RS tree pruning. Later genieclust extensions are not silently equated with the original method.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:GenieClustering.

The declared AIO mapping is supported.

Related hierarchical and unsupervised clustering tasks are supported without algorithm/task equivalence. Nine full annotated AIO contexts and five native records were inspected. Neither neighbor voting, neural metric learning nor a scalar inequality function identifies the whole algorithm.

### inequality-triggered-merging

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

Section3.1 and the original merge predicate agree: when current Gini exceeds g, at least one endpoint must have globally minimum component size. This is an OR condition, not a demand that both clusters be smallest or that the next Gini fall below g. The finite calculations test that rule directly.

### mst-and-conditional-edge-selection

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

Figure5 and the complete C++ merge code maintain tree edges with conditional eligibility. The reference compares 2880 distinct-weight traces exactly and validates 2916 tied cases against the full eligible-pair minimum. Skipped edges remain available; finite cases are not a universal proof.

### distance-and-storage-scope

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

The paper’s base dissimilarity assumptions are separated from triangle-inequality requirements for VP-tree pruning. The inspected Prim loop visits each unordered pair once and stores linear arrays. No universal VP-tree count or high-dimensional speedup is asserted.

### threshold-and-height-boundaries

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

Current Gini can exceed the threshold and can increase after a corrective merge. The five-point example has raw distances1,2,88,9. Code marks corrective distances with signs, while the R wrapper interpolates and applies trailing cumulative maxima. Plot heights are not claimed to be raw distances.

### worked-example-discrepancy

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

For paper points0,1,3,6,10 and g0.3, the formal rule and code admit the edge of length3 at step3 because its singleton endpoint has minimum size. The paper example instead chooses length4. The inconsistency is retained explicitly; author software was not executed.

### reported-evaluation

evidence: supported. Targets: AIMech:GenieClustering.

Supported within the stated primary-source and mathematical scope.

Tables1–3 report known-K cuts, FM medians over10 input permutations and selected29/21-dataset comparisons. Aggregate mean.850 and median.921 at g0.2 match Table2. The same benchmark collection compares thresholds; dataset selection and unequal-size failures prevent general superiority claims.

### Genie identity, threshold-triggered merge eligibility, MST equivalence, Gini update, source discrepancy and plotting/evaluation scope

consistency: supported. Targets: AIMech:GenieClustering.

Constructed calculations support the stated distinctions.

Exact curator checks cover2880 distinct-weight and2916 tied four-point inputs/thresholds; MST choices satisfy the full eligible-pair minimum and Gini recurrence matches direct pair sums. The paper example gives raw distances1,2,3,4 under the formal rule, while a separate five-point example gives1,2,88,9. These are reference calculations, not author execution or universal guarantees.

### All maintained fields

provenance: supported. Targets: AIMech:GenieClustering.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed ID/name/aliases/kind, definition and evidence, all six claims and locators, four source identities/versions/access/hashes, AIO mappings, formal OR eligibility, current-partition Gini normalization and threshold overshoot, MST conditional edge reuse, raw-height inversions versus wrapper presentation, source Example1 discrepancy, evaluation selection and actual curation provenance. DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T224735Z-genie-clustering.json | supports | Compared all 442 pinned AIO and 656 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 30, 0, 0 lines. All distinct match contents were read, including pending discovery entries and source-reading observations. Recovery hits concern pending Genie discovery notes and primary-source context; none identifies an existing standalone Genie record. Both other checkouts returned no matches including ignored and hidden files. Semantic matching covered 26 AIO and 173 native definitions, all read; unchanged definitions were byte-compared with the preceding full assessment. 9 full annotated AIO node/edge/generated contexts and 5 full native records were inspected. Retain the original inequality-triggered single-link merge rule. It differs from fixed linkage-preserving chains, global cached-bound search, Ward variance minimization, BIRCH compression and RS tree pruning. Genieclust names a later software package with extensions, not an exact alias for all original-method claims. |
| mapping | sources/aio/aio.json | supports | Related hierarchical and unsupervised clustering tasks are supported without algorithm/task equivalence. Nine full annotated AIO contexts and five native records were inspected. Neither neighbor voting, neural metric learning nor a scalar inequality function identifies the whole algorithm. |
| genie2016 | https://arxiv.org/pdf/2209.05757v1; Section3.1, PDF pp.7–8; Figure5, PDF p.15; Sections2.2–3.1, PDF pp.5–8, Equations1–2; Section4, Theorem1 and Figure5, PDF pp.14–17; Introduction, PDF p.2; Sections4.1–4.3, Figures6–7, PDF pp.17–22; Section3.1, PDF p.8; Section4.1, PDF pp.16–17; Section3.1, PDF pp.7–8; Figure5, PDF p.15; Example1, PDF p.16; Sections3.2–3.3, PDF pp.9–14, Tables1–3 | supports | arXiv2209.05757v1,13September2022 deposit citing Information Sciences363(2016),8–23. All30 pages visually read; journal typeset text not separately compared. |
| genie-merge | https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/src/hclust2_mstbased_gini.cpp; HClustMSTbasedGini::compute; HClustMSTbasedGini::compute, conditional edge exclusion; HClustMSTbasedGini::compute, pq_cache restoration; HClustMSTbasedGini::getMST; HClustMSTbasedGini::compute, signed res.link distance; HClustMSTbasedGini::compute, both-size-greater-than-minimum exclusion | supports | Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016; DESCRIPTION version1.0.0. Complete file statically read; not executed. |
| genie-wrapper | https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/R/hclust2.R; hclust2, final height adjustment | supports | Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016; DESCRIPTION version1.0.0. Complete file statically read; not executed. |
| genie-description | https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/DESCRIPTION; Package, Version and Date fields | supports | Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016; DESCRIPTION version1.0.0. Complete file statically read; not executed. |
| calculation | research/discovery/genie-clustering-boundaries.py | supports | Exact curator checks cover2880 distinct-weight and2916 tied four-point inputs/thresholds; MST choices satisfy the full eligible-pair minimum and Gini recurrence matches direct pair sums. The paper example gives raw distances1,2,3,4 under the formal rule, while a separate five-point example gives1,2,88,9. These are reference calculations, not author execution or universal guarantees. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 657 native and 442 unchanged generated records. The 842-entry main frontier retains 473 pending and 58 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All30 paper pages and all cited pinned implementation files read; eight original implementation files inspected in total. No author execution or benchmark replication.
- No author-code execution, training, paid service, hardware measurement or empirical replication. The complete cited primary and implementation sources were read; historical experiments and floating-point behavior were not reproduced. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T225249Z-genie-clustering
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Genie clustering
started_at: '2026-10-13T22:47:46Z'
finished_at: '2026-10-13T22:52:49Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged Genie identity, threshold-triggered merge
    eligibility, MST equivalence, Gini update, source discrepancy and plotting/evaluation
    scope. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain original Genie clustering as a DRAFT native algorithm with related
  AIO task mappings. Author self-review supports the formal merge rule while preserving
  source-example, threshold, plotting-height, implementation and evaluation boundaries.
source:
  git_revision: 699a153ef5b22c4f5a80a0751fc73895d23858b5
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
  - path: data/curated/BIRCH.yaml
    sha256: c1baee35bb4c6352d9060c5594cd62cb41100dbc929a8d58fa836928d1d70d83
    role: context
  - path: data/curated/GenericLazyNeighborAgglomerativeClustering.yaml
    sha256: b7497e08e16cdc9b30d8566c492f668dd76295fd7878dbf05b191317ba3926b9
    role: context
  - path: data/curated/GenieClustering.yaml
    sha256: 4bd69f9d4dbf5be9e97c4a5f8bba9d674fab7e240f1d49abc017e4d04dd58181
    role: target
  - path: data/curated/NearestNeighborChainClustering.yaml
    sha256: 29edd6535409cbf8a1fb3c806de4d52f0f33473d597439c40af4c895fa49746a
    role: context
  - path: data/curated/ReciprocalNearestNeighborsSupportedClustering.yaml
    sha256: e3bc2d88143b46989b642e695be1c94d11d090c67606f91c970bd1c4ece47738
    role: context
  - path: data/curated/WardMinimumVarianceClustering.yaml
    sha256: cd8fbbb8257329683eeafb2a453da362175e4df0371d393e699a887b06f95c4c
    role: context
  - path: research/discovery/20261013T224735Z-genie-clustering.json
    sha256: bed313a44c66e1e85ef73b394e32aa3625b26f9d8d8630475b5fe8e94f28b326
    role: context
  - path: research/discovery/genie-clustering-boundaries.py
    sha256: 4e937a5bfb228031f6f003b991fe86c4db66e735af6db4353687ae6e5f950789
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
- target_id: AIMech:GenieClustering
  path: data/curated/GenieClustering.yaml
  label: Genie clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GenieClustering.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:GenieClustering'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GenieClustering
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All30 primary pages and complete cited original implementation files read.
      Other implementation internals, later genieclust extensions, floating-point
      behavior, actual data and benchmarks were not executed or certified.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GenieClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 139.68s (0:02:19)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 657 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 338 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 335,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GenieClustering
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
  - AIMech:GenieClustering
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
  - AIMech:GenieClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/genie-clustering-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GenieClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"distinct_weight_cases": 2880, "tied_weight_cases": 2916, "scope": "Four-point
    symmetric nonnegative dissimilarities: 720 edge permutations and 729 three-valued
    assignments, each at four thresholds. The MST choices satisfy the full eligible-pair
    minimum; distinct-weight traces agree exactly. Gini incremental updates agree
    with direct pair-sum recomputation. This is finite verification, not a universal
    proof.", "paper_example": {"points": [0, 1, 3, 6, 10], "threshold": "3/10", "trace":
    [{"edge": [0, 1], "distance": "1", "forced": false, "gini_before": "0", "gini_after":
    "1/5", "partition": [[0, 1], [2], [3], [4]]}, {"edge": [1, 2], "distance": "2",
    "forced": false, "gini_before": "1/5", "gini_after": "2/5", "partition": [[0,
    1, 2], [3], [4]]}, {"edge": [2, 3], "distance": "3", "forced": true, "gini_before":
    "2/5", "gini_after": "3/5", "partition": [[0, 1, 2, 3], [4]]}, {"edge": [3, 4],
    "distance": "4", "forced": true, "gini_before": "3/5", "gini_after": null, "partition":
    [[0, 1, 2, 3, 4]]}], "assessment": "The printed OR eligibility rule and statically
    inspected Genie1.0.0 merge predicate choose distance3 at the third merge. The
    paper Example1 instead claims distance4 and partition {0,1,2}/{3,4}; that claim
    does not follow from its stated rule. No author program was executed."}, "inversion":
    {"points": [0, 1, 10, 12, 100], "threshold": "3/20", "trace": [{"edge": [0, 1],
    "distance": "1", "forced": false, "gini_before": "0", "gini_after": "1/5", "partition":
    [[0, 1], [2], [3], [4]]}, {"edge": [2, 3], "distance": "2", "forced": true, "gini_before":
    "1/5", "gini_after": "1/5", "partition": [[0, 1], [2, 3], [4]]}, {"edge": [3,
    4], "distance": "88", "forced": true, "gini_before": "1/5", "gini_after": "1/5",
    "partition": [[0, 1], [2, 3, 4]]}, {"edge": [1, 2], "distance": "9", "forced":
    true, "gini_before": "1/5", "gini_after": null, "partition": [[0, 1, 2, 3, 4]]}]},
    "limits": "Curator reference only. No author R/C++ execution, floating-point certification,
    benchmark reproduction, universal tie equivalence or outlier-recovery guarantee."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T224735Z-genie-clustering.json
  accessed_at: '2026-10-13T22:47:46Z'
  support: supports
  summary: Compared all 442 pinned AIO and 656 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    30, 0, 0 lines. All distinct match contents were read, including pending discovery
    entries and source-reading observations. Recovery hits concern pending Genie discovery
    notes and primary-source context; none identifies an existing standalone Genie
    record. Both other checkouts returned no matches including ignored and hidden
    files. Semantic matching covered 26 AIO and 173 native definitions, all read;
    unchanged definitions were byte-compared with the preceding full assessment. 9
    full annotated AIO node/edge/generated contexts and 5 full native records were
    inspected. Retain the original inequality-triggered single-link merge rule. It
    differs from fixed linkage-preserving chains, global cached-bound search, Ward
    variance minimization, BIRCH compression and RS tree pruning. Genieclust names
    a later software package with extensions, not an exact alias for all original-method
    claims.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T22:47:46Z'
  support: supports
  summary: Related hierarchical and unsupervised clustering tasks are supported without
    algorithm/task equivalence. Nine full annotated AIO contexts and five native records
    were inspected. Neither neighbor voting, neural metric learning nor a scalar inequality
    function identifies the whole algorithm.
- evidence_id: genie2016
  kind: primary_source
  reference: https://arxiv.org/pdf/2209.05757v1
  locator: Section3.1, PDF pp.7–8; Figure5, PDF p.15; Sections2.2–3.1, PDF pp.5–8,
    Equations1–2; Section4, Theorem1 and Figure5, PDF pp.14–17; Introduction, PDF
    p.2; Sections4.1–4.3, Figures6–7, PDF pp.17–22; Section3.1, PDF p.8; Section4.1,
    PDF pp.16–17; Section3.1, PDF pp.7–8; Figure5, PDF p.15; Example1, PDF p.16; Sections3.2–3.3,
    PDF pp.9–14, Tables1–3
  accessed_at: '2026-10-13T21:57:12Z'
  snapshot_sha256: 173888c1207996b3eca871bdf1e10728735f3265d65ebfdd846e021ae4882564
  support: supports
  summary: arXiv2209.05757v1,13September2022 deposit citing Information Sciences363(2016),8–23.
    All30 pages visually read; journal typeset text not separately compared.
- evidence_id: genie-merge
  kind: primary_source
  reference: https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/src/hclust2_mstbased_gini.cpp
  locator: HClustMSTbasedGini::compute; HClustMSTbasedGini::compute, conditional edge
    exclusion; HClustMSTbasedGini::compute, pq_cache restoration; HClustMSTbasedGini::getMST;
    HClustMSTbasedGini::compute, signed res.link distance; HClustMSTbasedGini::compute,
    both-size-greater-than-minimum exclusion
  accessed_at: '2026-10-13T22:20:37Z'
  snapshot_sha256: 5af3cf1e3d2fb11e8a31370d04a12fcdd3077fd536612dd4831d331cb30b09d5
  support: supports
  summary: Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016;
    DESCRIPTION version1.0.0. Complete file statically read; not executed.
- evidence_id: genie-wrapper
  kind: primary_source
  reference: https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/R/hclust2.R
  locator: hclust2, final height adjustment
  accessed_at: '2026-10-13T22:20:36Z'
  snapshot_sha256: 8330e818daaece08d8ed139093c6a1d1968848ea59b72e370ba6a61d228a2fe9
  support: supports
  summary: Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016;
    DESCRIPTION version1.0.0. Complete file statically read; not executed.
- evidence_id: genie-description
  kind: primary_source
  reference: https://raw.githubusercontent.com/gagolews/genie/67ea675abba113560608173ac34cafc1e66b3b1c/DESCRIPTION
  locator: Package, Version and Date fields
  accessed_at: '2026-10-13T22:20:35Z'
  snapshot_sha256: b84da1dc41bd2b7c378b4a8ef8fd3afddeed824fb70d038dd57a1d9b22faeaf5
  support: supports
  summary: Author repository commit67ea675abba113560608173ac34cafc1e66b3b1c,7March2016;
    DESCRIPTION version1.0.0. Complete file statically read; not executed.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/genie-clustering-boundaries.py
  accessed_at: '2026-10-13T22:48:22Z'
  snapshot_sha256: 4e937a5bfb228031f6f003b991fe86c4db66e735af6db4353687ae6e5f950789
  support: supports
  summary: Exact curator checks cover2880 distinct-weight and2916 tied four-point
    inputs/thresholds; MST choices satisfy the full eligible-pair minimum and Gini
    recurrence matches direct pair sums. The paper example gives raw distances1,2,3,4
    under the formal rule, while a separate five-point example gives1,2,88,9. These
    are reference calculations, not author execution or universal guarantees.
assessments:
- assessment_id: identity
  area: identity
  topic: Genie clustering
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - identity
  - genie2016
  - genie-merge
  - genie-wrapper
  - genie-description
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the original inequality-triggered single-link algorithm, distinct
    from fixed-linkage NN-chain, cached-bound search, Ward ESS, BIRCH compression
    and RS tree pruning. Later genieclust extensions are not silently equated with
    the original method.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - mapping
  - genie2016
  - genie-merge
  - genie-wrapper
  - genie-description
  summary: The declared AIO mapping is supported.
  details: Related hierarchical and unsupervised clustering tasks are supported without
    algorithm/task equivalence. Nine full annotated AIO contexts and five native records
    were inspected. Neither neighbor voting, neural metric learning nor a scalar inequality
    function identifies the whole algorithm.
- assessment_id: inequality-triggered-merging
  area: evidence
  topic: inequality-triggered-merging
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: 'Section3.1 and the original merge predicate agree: when current Gini exceeds
    g, at least one endpoint must have globally minimum component size. This is an
    OR condition, not a demand that both clusters be smallest or that the next Gini
    fall below g. The finite calculations test that rule directly.'
- assessment_id: mst-and-conditional-edge-selection
  area: evidence
  topic: mst-and-conditional-edge-selection
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure5 and the complete C++ merge code maintain tree edges with conditional
    eligibility. The reference compares 2880 distinct-weight traces exactly and validates
    2916 tied cases against the full eligible-pair minimum. Skipped edges remain available;
    finite cases are not a universal proof.
- assessment_id: distance-and-storage-scope
  area: evidence
  topic: distance-and-storage-scope
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  summary: Supported within the stated primary-source and mathematical scope.
  details: The paper’s base dissimilarity assumptions are separated from triangle-inequality
    requirements for VP-tree pruning. The inspected Prim loop visits each unordered
    pair once and stores linear arrays. No universal VP-tree count or high-dimensional
    speedup is asserted.
- assessment_id: threshold-and-height-boundaries
  area: evidence
  topic: threshold-and-height-boundaries
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  - genie-wrapper
  - genie-description
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Current Gini can exceed the threshold and can increase after a corrective
    merge. The five-point example has raw distances1,2,88,9. Code marks corrective
    distances with signs, while the R wrapper interpolates and applies trailing cumulative
    maxima. Plot heights are not claimed to be raw distances.
- assessment_id: worked-example-discrepancy
  area: evidence
  topic: worked-example-discrepancy
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: For paper points0,1,3,6,10 and g0.3, the formal rule and code admit the
    edge of length3 at step3 because its singleton endpoint has minimum size. The
    paper example instead chooses length4. The inconsistency is retained explicitly;
    author software was not executed.
- assessment_id: reported-evaluation
  area: evidence
  topic: reported-evaluation
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Tables1–3 report known-K cuts, FM medians over10 input permutations and
    selected29/21-dataset comparisons. Aggregate mean.850 and median.921 at g0.2 match
    Table2. The same benchmark collection compares thresholds; dataset selection and
    unequal-size failures prevent general superiority claims.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Genie identity, threshold-triggered merge eligibility, MST equivalence, Gini
    update, source discrepancy and plotting/evaluation scope
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - genie2016
  - genie-merge
  - genie-wrapper
  - genie-description
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact curator checks cover2880 distinct-weight and2916 tied four-point
    inputs/thresholds; MST choices satisfy the full eligible-pair minimum and Gini
    recurrence matches direct pair sums. The paper example gives raw distances1,2,3,4
    under the formal rule, while a separate five-point example gives1,2,88,9. These
    are reference calculations, not author execution or universal guarantees.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:GenieClustering
  evidence_ids:
  - identity
  - mapping
  - genie2016
  - genie-merge
  - genie-wrapper
  - genie-description
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed ID/name/aliases/kind, definition and evidence,
    all six claims and locators, four source identities/versions/access/hashes, AIO
    mappings, formal OR eligibility, current-partition Gini normalization and threshold
    overshoot, MST conditional edge reuse, raw-height inversions versus wrapper presentation,
    source Example1 discrepancy, evaluation selection and actual curation provenance.
    DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 657 native and 442 unchanged generated records.
  The 842-entry main frontier retains 473 pending and 58 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All30 paper pages and all cited pinned implementation files read; eight original
  implementation files inspected in total. No author execution or benchmark replication.
- No author-code execution, training, paid service, hardware measurement or empirical
  replication. The complete cited primary and implementation sources were read; historical
  experiments and floating-point behavior were not reproduced. Constructed checks
  test stated boundaries only.
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
