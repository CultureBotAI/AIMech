# Scientific author self-review of Nearest-neighbor-chain clustering

- Review: 20261013T213043Z-nearest-neighbor-chain-clustering
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T21:25:23Z
- Finished UTC: 2026-10-13T21:30:43Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain nearest-neighbor-chain clustering as a DRAFT algorithm with related hierarchical and unsupervised clustering mappings. Resolve the confirmed major source-attribution error: Figure4 prints ≤3, consistent with the code. The corrected record and calculation preserve the separate update-law, tie, output, complexity and static-inspection limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:NearestNeighborChainClustering
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c1d7f442e06af850d7a450a55c958ac49760d35.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NearestNeighborChainClustering | data/curated/NearestNeighborChainClustering.yaml | maintained | Nearest-neighbor-chain clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NearestNeighborChainClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 153.88s (0:02:33)<br>Checked 442 record(s); 0 failed.<br>Checked 652 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 333 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 330,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NearestNeighborChainClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NearestNeighborChainClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NearestNeighborChainClustering | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:NearestNeighborChainClustering | {"matrix_cases": 11664, "ward_euclidean_cases": 324, "reordered_complete": {"raw": [{"left": [1], "right": [0], "height": "3"}, {"left": [3], "right": [2], "height": "1"}, {"left": [2, 3], "right": [0, 1], "height": "7"}, {"left": [4], "right": [0, 1, 2, 3], "height": "15"}], "stable_sorted": [{"left": [3], "right": [2], "height": "1"}, {"left": [1], "right": [0], "height": "3"}, {"left": [2, 3], "right": [0, 1], "height": "7"}, {"left": [4], "right": [0, 1, 2, 3], "height": "15"}]}, "reducibility_without_commutation": {"primitive": [{"left": [2], "right": [3], "height": "1"}, {"left": [0], "right": [1], "height": "3"}, {"left": [0, 1], "right": [2, 3], "height": "27"}, {"left": [0, 1, 2, 3], "right": [4], "height": "85"}], "chain_sorted": [{"left": [3], "right": [2], "height": "1"}, {"left": [1], "right": [0], "height": "3"}, {"left": [4], "right": [2, 3], "height": "28"}, {"left": [2, 3, 4], "right": [0, 1], "height": "87"}], "disjoint_pair_order_distances": ["29", "27"]}, "arbitrary_tie_cycle": [0, 1, 2, 0], "predecessor_tie_trace": [{"left": [1], "right": [0], "height": "1"}, {"left": [2], "right": [0, 1], "height": "1"}], "reversing_equal_height_dependencies_is_invalid": true, "actual_figure4_restart_boundaries": [{"length": 0, "action": "restart"}, {"length": 1, "action": "restart"}, {"length": 2, "action": "restart"}, {"length": 3, "action": "restart"}, {"length": 4, "action": "reuse"}, {"length": 5, "action": "reuse"}, {"length": 6, "action": "reuse"}, {"length": 7, "action": "reuse"}, {"length": 8, "action": "reuse"}], "equal_minima_not_reciprocal": {"minima": 1, "pair_distance": 5}, "limits": "Finite rational checks of a curator-written conceptual algorithm; no author program run, no universal proof, no timing or floating-point replication."} |

## Scientific And Domain Assessments

### Nearest-neighbor-chain clustering

identity: supported. Targets: AIMech:NearestNeighborChainClustering.

Retain this distinct DRAFT algorithm.

Retain the chain as an agglomerative merge-search procedure parameterized by linkage. It is distinct from Ward’s ESS criterion, k-means reassignment, CURE representatives, BIRCH compression, nearest-neighbor label voting and the earlier reciprocal-pair batch procedure. The NN-chain alias is qualified by clustering rather than a bare acronym.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:NearestNeighborChainClustering.

The declared AIO mapping is supported.

Related matches to HierarchicalClustering and UnsupervisedClustering describe the task served without asserting task/algorithm equivalence or subclass membership. Nine full annotated AIO contexts include the neighbor-voting classifier; its mechanism does not identify a reciprocal merge chain.

### reciprocal-chain

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

The original descriptions and CADENA listing support following nearest neighbors, predecessor tie preference, reciprocal termination, pair merging and prefix reuse. The current core uses strict improvement scans and an explicit &lt;=3 restart guard. The curator implementation safely drops the last reciprocal pair and rescans the retained endpoint.

### update-law-conditions

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

Theorem1 explicitly requires reducibility plus commutation of disjoint pair merges. Proposition2 covers the five named linkage rules. The sum3 counterexample reproduces primitive heights 1,3,27,85 versus invalid sorted chain 1,3,28,87; it refutes reducibility alone for history-dependent recurrences.

### stepwise-output-and-ties

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

The paper requires stable sorting and representative relabeling, and the pinned wrapper performs both with actual found union roots. A finite complete-link example discovers heights3,1,7,15, then gives a valid stepwise sequence1,3,7,15. Validation checks greedy admissibility rather than equality to one arbitrary tie order.

### matrix-complexity

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

Section4.1 explicitly separates the writable quadratic matrix from linear auxiliary memory and gives quadratic total time. Benzécri’s bound has a distance-formula constant; the record confines it to constant-time scalar updates and does not transfer it to arbitrary vector-distance computation.

### procedure-versus-linkage

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

The method is a candidate-selection algorithm across supported linkages. Ward is a criterion-specific specialization, while de Rham’s earlier method repeatedly finds batches of reciprocal pairs. AIO’s nearest-neighbor classifier predicts labels by voting. The cited result concerns valid hierarchical output, not unrestricted optimal partitions.

### implementation-boundaries

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Supported within the stated primary-source and mathematical scope.

Figure4 line6 and pinned core agree on ≤3 / &lt;=3. The corrected finite check restarts at lengths0–3 and safely accesses the retained prefix for lengths4–8. Static source inspection confirms saved premerge sizes, root-aware output unions, stable sorting, Ward scaling and separate matrix/vector dispatch. NEWS documents vector-chain removal. The earlier fabricated &lt;3 check and claimed source defect are rejected, not evidence against the method.

### chain identity, update-law conditions, tied nearest neighbors, valid stepwise output, memory accounting and printed-versus-implemented boundaries

consistency: supported. Targets: AIMech:NearestNeighborChainClustering.

Constructed calculations support the stated distinctions.

A curator-written rational chain is checked against greedy stepwise validity in 11,664 four-object dissimilarity/linkage/start cases and 324 finite Euclidean Ward/start cases. A complete-link example requires reordering 3,1,7,15 to 1,3,7,15. The source’s sum3 update counterexample gives primitive heights 1,3,27,85 but sorted chain 1,3,28,87. Other checks illustrate predecessor ties, the actual Figure4 ≤3 restart guard at lengths0–3 and safe retained-prefix indexing at lengths4–8 and equal minima without reciprocity. No author implementation or benchmark was executed.

### All maintained fields

provenance: supported. Targets: AIMech:NearestNeighborChainClustering.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all names, aliases and kind, definition and locators, six claims, seven source versions and hashes, related/rejected mappings, both update-law conditions, predecessor tie preference, sorted/relabelled output, matrix versus auxiliary memory, separation from Ward and batch procedures, literal pseudocode boundaries, pinned static-code scope and actual provenance. DRAFT remains. Corrected implementation-boundary claim, limitation3, actual guard calculation, report mirror and explicit rejected-observation log were reassessed after recapture. Prior Ward-report bytes and saved reviews remain unchanged; issue312 has exact finding lineage in this successor.

### Corrected source attribution

evidence: supported. Targets: AIMech:NearestNeighborChainClustering.

Issue312 source-attribution finding resolved.

The recaptured record explicitly uses ≤3, as confirmed in the original-resolution Figure4. The calculation now checks actual restart/safe reuse boundaries. The report mirrors the corrected record, rejects each erroneous preliminary observation and explicitly corrects the preceding Ward report without rewriting it. An actual EDIT history exists and corrected-input gates pass.

## Findings

### F1: Correct the false Figure4 restart-guard defect

major / resolved / confirmed; issue key: nn-chain-figure4-restart-guard-misattribution.

Figure 4 line 6, PDF p.13, actually prints length(chain) ≤3. The draft limitation misreads it as &lt;3 and alleges an out-of-range [-4] access at length3. The curator calculation deliberately uses &lt;3 and labels that fabricated variant as printed pseudocode. Current source notes/report mirror this error. Both the paper and pinned NN_chain_core use ≤3 / &lt;=3; the earlier Ward report contains the same preliminary suspicion and needs an explicit successor correction, not a rewrite.

Disposition: The recaptured record explicitly uses ≤3, as confirmed in the original-resolution Figure4. The calculation now checks actual restart/safe reuse boundaries. The report mirrors the corrected record, rejects each erroneous preliminary observation and explicitly corrects the preceding Ward report without rewriting it. An actual EDIT history exists and corrected-input gates pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T211701Z-nearest-neighbor-chain-clustering.json | supports | Compared all 442 pinned AIO and 651 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 21, 0, 0 lines. All distinct match contents were read, including generated index rows repeating the fully read Ward record. Recovery hits concern Ward implementation context, its saved review or pending discovery/source notes; none identifies an existing standalone chain record. Both other checkouts returned no matches including ignored and hidden files. Semantic matching covered 26 AIO and 168 native definitions, all read; unchanged definitions were byte-compared with the preceding full assessment. 9 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. The chain is an agglomerative merge-search procedure parameterized by linkage. It differs from the Ward ESS criterion, centroid reassignment in k-means, CURE representatives, BIRCH compression, nearest-neighbor label voting and batch reciprocal-neighbor passes. Retain the conditional stepwise-output identity rather than treating all nearest-neighbor algorithms or all fastcluster entrypoints as aliases. |
| mapping | sources/aio/aio.json | supports | Related matches to HierarchicalClustering and UnsupervisedClustering describe the task served without asserting task/algorithm equivalence or subclass membership. Nine full annotated AIO contexts include the neighbor-voting classifier; its mechanism does not identify a reciprocal merge chain. |
| mullner2011 | https://arxiv.org/pdf/1109.2378v1; Section3.2, Theorem 1 and Figure 4, PDF pp.11–16; Section3.2 and Figure 4, PDF pp.11–16; Section3.2, Equation1, Theorem 1, Proposition2 and footnote1, PDF pp.12–16; Section2.2 and Section3.2, Figures4–5, PDF pp.4–5,11–16; Section4.1, PDF p.20; Sections2 and3.2, PDF pp.3–8,11–16; Figure4, NN-CHAIN-CORE line6, PDFp13: length(chain) ≤3 | supports | arXiv1109.2378v1,12September2011; all29 PDF pages visually read. |
| benzecri1982 | https://www.numdam.org/item/CAD_1982__7_2_209_0.pdf; Sections1 and2.4–2.5, printed pp.209–210,213–214 / PDF pp.2–3,6–7; Sections2.2–2.5 and3, printed pp.211–218 / PDF pp.4–11; Section2.5, printed p.214 / PDF p.7; Section1, printed pp.209–210 / PDF pp.2–3 | supports | Les Cahiers de l’analyse des données7(2),1982,pp.209–218. Eleven scanned PDF pages including cover, all visually read. |
| juan1982 | https://www.numdam.org/article/CAD_1982__7_2_219_0.pdf; Sections1–2, printed pp.219–220 / PDF pp.2–3; CADENA listing, printed pp.223–224 / PDF pp.6–7 | supports | Les Cahiers de l’analyse des données7(2),1982,pp.219–225. Eight scanned PDF pages including cover, all visually read. |
| derham1980 | https://www.numdam.org/item/CAD_1980__5_2_135_0.pdf; Introduction and Sections3.2 and4.2, printed pp.135–136,140–142 / PDF pp.2–3,7–9 | supports | Les Cahiers de l’analyse des données5(2),1980,pp.135–144. Eleven scanned PDF pages including cover, all visually read. |
| fastcluster-core | https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/src/fastcluster.cpp; node comparator, lines225–232; union_find, lines366–403 at the pinned commit; NN_chain_core lines574–778; f_ward lines530–545; union_find lines366–403 | supports | Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Lines1–120,225–290,360–410,490–785 statically read, not compiled or executed. Later code is not assumed identical to the2011 benchmark implementation. |
| fastcluster-wrapper | https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/src/fastcluster_python.cpp; generate_SciPy_dendrogram, src/fastcluster_python.cpp lines108–145 at the pinned commit; Matrix dispatch/preprocessing/postprocessing lines290–353; vector dispatch lines1164–1193; dendrogram output lines108–145 | supports | Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Lines105–150,290–355,1160–1195 statically read, not compiled or executed. Later code is not assumed identical to the2011 benchmark implementation. |
| fastcluster-news | https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/NEWS.txt; Version1.1.2 entry dated 11 October 2011 | supports | Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Complete file statically read, not compiled or executed. Later code is not assumed identical to the2011 benchmark implementation. |
| calculation | research/discovery/nearest-neighbor-chain-clustering-boundaries.py | supports | A curator-written rational chain is checked against greedy stepwise validity in 11,664 four-object dissimilarity/linkage/start cases and 324 finite Euclidean Ward/start cases. A complete-link example requires reordering 3,1,7,15 to 1,3,7,15. The source’s sum3 update counterexample gives primitive heights 1,3,27,85 but sorted chain 1,3,28,87. Other checks illustrate predecessor ties, the actual Figure4 ≤3 restart guard at lengths0–3 and safe retained-prefix indexing at lengths4–8 and equal minima without reciprocity. No author implementation or benchmark was executed. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 652 native and 442 unchanged generated records. The 837-entry main frontier retains 473 pending and 58 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All59 pages of the four cited primary PDFs visually read; named C++ ranges plus complete README, NEWS and license statically read. No author software executed.
- No author-code execution, training, paid service, hardware measurement or empirical replication. The source listings and named pinned implementation ranges were statically read; historical experiments and floating-point behavior were not reproduced. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T213043Z-nearest-neighbor-chain-clustering
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Nearest-neighbor-chain clustering
started_at: '2026-10-13T21:25:23Z'
finished_at: '2026-10-13T21:30:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged chain identity, update-law conditions,
    tied nearest neighbors, valid stepwise output, memory accounting and printed-versus-implemented
    boundaries. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain nearest-neighbor-chain clustering as a DRAFT algorithm with related
  hierarchical and unsupervised clustering mappings. Resolve the confirmed major source-attribution
  error: Figure4 prints ≤3, consistent with the code. The corrected record and calculation
  preserve the separate update-law, tie, output, complexity and static-inspection
  limits.'
source:
  git_revision: 9c1d7f442e06af850d7a450a55c958ac49760d35
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
  - path: data/curated/CUREClustering.yaml
    sha256: ab437b2bd33b77ed821e8695bc15ba90de4fc216d4cafff09da7e48060d42cba
    role: context
  - path: data/curated/KMeans.yaml
    sha256: 50fc1d8d18403a8f314636f68b6812ffd15fec2dfaaf4c32aaad423dfa7ffa03
    role: context
  - path: data/curated/NearestNeighborChainClustering.yaml
    sha256: 29edd6535409cbf8a1fb3c806de4d52f0f33473d597439c40af4c895fa49746a
    role: target
  - path: data/curated/WardMinimumVarianceClustering.yaml
    sha256: cd8fbbb8257329683eeafb2a453da362175e4df0371d393e699a887b06f95c4c
    role: context
  - path: research/discovery/20261013T211701Z-nearest-neighbor-chain-clustering.json
    sha256: 8824d0321d610676e31316a624035f02cf15bff9a3afa548f77e8ded519a9ef9
    role: context
  - path: research/discovery/nearest-neighbor-chain-clustering-boundaries.py
    sha256: 9be518f85c442a72f5ff4f193d381aab46b508b5b279d98e56f1bbf8dd632abf
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
- target_id: AIMech:NearestNeighborChainClustering
  path: data/curated/NearestNeighborChainClustering.yaml
  label: Nearest-neighbor-chain clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NearestNeighborChainClustering.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:NearestNeighborChainClustering'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:NearestNeighborChainClustering
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All 59 pages of four primary PDFs visually read; specified static source
      ranges and complete NEWS read at commit 9d0e48609283edaae90593a6967d3f2217786d2d.
      No author software executed or historical benchmark reproduced; no complete-program
      or floating-point correctness certification.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborChainClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 153.88s (0:02:33)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 652 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 333 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 330,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborChainClustering
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
  - AIMech:NearestNeighborChainClustering
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
  - AIMech:NearestNeighborChainClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/nearest-neighbor-chain-clustering-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NearestNeighborChainClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"matrix_cases": 11664, "ward_euclidean_cases": 324, "reordered_complete":
    {"raw": [{"left": [1], "right": [0], "height": "3"}, {"left": [3], "right": [2],
    "height": "1"}, {"left": [2, 3], "right": [0, 1], "height": "7"}, {"left": [4],
    "right": [0, 1, 2, 3], "height": "15"}], "stable_sorted": [{"left": [3], "right":
    [2], "height": "1"}, {"left": [1], "right": [0], "height": "3"}, {"left": [2,
    3], "right": [0, 1], "height": "7"}, {"left": [4], "right": [0, 1, 2, 3], "height":
    "15"}]}, "reducibility_without_commutation": {"primitive": [{"left": [2], "right":
    [3], "height": "1"}, {"left": [0], "right": [1], "height": "3"}, {"left": [0,
    1], "right": [2, 3], "height": "27"}, {"left": [0, 1, 2, 3], "right": [4], "height":
    "85"}], "chain_sorted": [{"left": [3], "right": [2], "height": "1"}, {"left":
    [1], "right": [0], "height": "3"}, {"left": [4], "right": [2, 3], "height": "28"},
    {"left": [2, 3, 4], "right": [0, 1], "height": "87"}], "disjoint_pair_order_distances":
    ["29", "27"]}, "arbitrary_tie_cycle": [0, 1, 2, 0], "predecessor_tie_trace": [{"left":
    [1], "right": [0], "height": "1"}, {"left": [2], "right": [0, 1], "height": "1"}],
    "reversing_equal_height_dependencies_is_invalid": true, "actual_figure4_restart_boundaries":
    [{"length": 0, "action": "restart"}, {"length": 1, "action": "restart"}, {"length":
    2, "action": "restart"}, {"length": 3, "action": "restart"}, {"length": 4, "action":
    "reuse"}, {"length": 5, "action": "reuse"}, {"length": 6, "action": "reuse"},
    {"length": 7, "action": "reuse"}, {"length": 8, "action": "reuse"}], "equal_minima_not_reciprocal":
    {"minima": 1, "pair_distance": 5}, "limits": "Finite rational checks of a curator-written
    conceptual algorithm; no author program run, no universal proof, no timing or
    floating-point replication."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T211701Z-nearest-neighbor-chain-clustering.json
  accessed_at: '2026-10-13T21:25:23Z'
  support: supports
  summary: Compared all 442 pinned AIO and 651 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    21, 0, 0 lines. All distinct match contents were read, including generated index
    rows repeating the fully read Ward record. Recovery hits concern Ward implementation
    context, its saved review or pending discovery/source notes; none identifies an
    existing standalone chain record. Both other checkouts returned no matches including
    ignored and hidden files. Semantic matching covered 26 AIO and 168 native definitions,
    all read; unchanged definitions were byte-compared with the preceding full assessment.
    9 full annotated AIO node/edge/generated contexts and 4 full native records were
    inspected. The chain is an agglomerative merge-search procedure parameterized
    by linkage. It differs from the Ward ESS criterion, centroid reassignment in k-means,
    CURE representatives, BIRCH compression, nearest-neighbor label voting and batch
    reciprocal-neighbor passes. Retain the conditional stepwise-output identity rather
    than treating all nearest-neighbor algorithms or all fastcluster entrypoints as
    aliases.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T21:25:23Z'
  support: supports
  summary: Related matches to HierarchicalClustering and UnsupervisedClustering describe
    the task served without asserting task/algorithm equivalence or subclass membership.
    Nine full annotated AIO contexts include the neighbor-voting classifier; its mechanism
    does not identify a reciprocal merge chain.
- evidence_id: mullner2011
  kind: primary_source
  reference: https://arxiv.org/pdf/1109.2378v1
  locator: 'Section3.2, Theorem 1 and Figure 4, PDF pp.11–16; Section3.2 and Figure
    4, PDF pp.11–16; Section3.2, Equation1, Theorem 1, Proposition2 and footnote1,
    PDF pp.12–16; Section2.2 and Section3.2, Figures4–5, PDF pp.4–5,11–16; Section4.1,
    PDF p.20; Sections2 and3.2, PDF pp.3–8,11–16; Figure4, NN-CHAIN-CORE line6, PDFp13:
    length(chain) ≤3'
  accessed_at: '2026-10-13T20:51:04Z'
  snapshot_sha256: 3d8ea802c328a9dfada44e1c7a4c4824086c1210b45a4b99b5b9801435934dae
  support: supports
  summary: arXiv1109.2378v1,12September2011; all29 PDF pages visually read.
- evidence_id: benzecri1982
  kind: primary_source
  reference: https://www.numdam.org/item/CAD_1982__7_2_209_0.pdf
  locator: Sections1 and2.4–2.5, printed pp.209–210,213–214 / PDF pp.2–3,6–7; Sections2.2–2.5
    and3, printed pp.211–218 / PDF pp.4–11; Section2.5, printed p.214 / PDF p.7; Section1,
    printed pp.209–210 / PDF pp.2–3
  accessed_at: '2026-10-13T20:51:05Z'
  snapshot_sha256: 2569b4b21a2e3ed5d20f7b50e5164fd37ba02be5ea90d683d711246adea98b58
  support: supports
  summary: Les Cahiers de l’analyse des données7(2),1982,pp.209–218. Eleven scanned
    PDF pages including cover, all visually read.
- evidence_id: juan1982
  kind: primary_source
  reference: https://www.numdam.org/article/CAD_1982__7_2_219_0.pdf
  locator: Sections1–2, printed pp.219–220 / PDF pp.2–3; CADENA listing, printed pp.223–224
    / PDF pp.6–7
  accessed_at: '2026-10-13T20:51:05Z'
  snapshot_sha256: 3710466686c46c0eee10119cc00d2c61145836bd6030ca61103bebada0e57140
  support: supports
  summary: Les Cahiers de l’analyse des données7(2),1982,pp.219–225. Eight scanned
    PDF pages including cover, all visually read.
- evidence_id: derham1980
  kind: primary_source
  reference: https://www.numdam.org/item/CAD_1980__5_2_135_0.pdf
  locator: Introduction and Sections3.2 and4.2, printed pp.135–136,140–142 / PDF pp.2–3,7–9
  accessed_at: '2026-10-13T20:51:05Z'
  snapshot_sha256: c62314df59e7eb3f64e36d7cf141711233493b241ac8939f272d708fa045d0b3
  support: supports
  summary: Les Cahiers de l’analyse des données5(2),1980,pp.135–144. Eleven scanned
    PDF pages including cover, all visually read.
- evidence_id: fastcluster-core
  kind: primary_source
  reference: https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/src/fastcluster.cpp
  locator: node comparator, lines225–232; union_find, lines366–403 at the pinned commit;
    NN_chain_core lines574–778; f_ward lines530–545; union_find lines366–403
  accessed_at: '2026-10-13T21:01:45Z'
  snapshot_sha256: 9ba52420e3732bb87cd3ee502323d2707bb6ce610c06c274a377b7b0ea195d4c
  support: supports
  summary: Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Lines1–120,225–290,360–410,490–785
    statically read, not compiled or executed. Later code is not assumed identical
    to the2011 benchmark implementation.
- evidence_id: fastcluster-wrapper
  kind: primary_source
  reference: https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/src/fastcluster_python.cpp
  locator: generate_SciPy_dendrogram, src/fastcluster_python.cpp lines108–145 at the
    pinned commit; Matrix dispatch/preprocessing/postprocessing lines290–353; vector
    dispatch lines1164–1193; dendrogram output lines108–145
  accessed_at: '2026-10-13T21:01:45Z'
  snapshot_sha256: b7fc7d732572e77556c9a3eed52390971ba212b81d612b296820e3d13e4d5e89
  support: supports
  summary: Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Lines105–150,290–355,1160–1195
    statically read, not compiled or executed. Later code is not assumed identical
    to the2011 benchmark implementation.
- evidence_id: fastcluster-news
  kind: primary_source
  reference: https://raw.githubusercontent.com/fastcluster/fastcluster/9d0e48609283edaae90593a6967d3f2217786d2d/NEWS.txt
  locator: Version1.1.2 entry dated 11 October 2011
  accessed_at: '2026-10-13T21:01:45Z'
  snapshot_sha256: 087eb9c9afaba169a5ef466a1e525efde4f9febb67c80217e5ec37792d5360d5
  support: supports
  summary: Git commit 9d0e48609283edaae90593a6967d3f2217786d2d dated2026-09-15; Complete
    file statically read, not compiled or executed. Later code is not assumed identical
    to the2011 benchmark implementation.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/nearest-neighbor-chain-clustering-boundaries.py
  accessed_at: '2026-10-13T21:26:10Z'
  snapshot_sha256: 9be518f85c442a72f5ff4f193d381aab46b508b5b279d98e56f1bbf8dd632abf
  support: supports
  summary: A curator-written rational chain is checked against greedy stepwise validity
    in 11,664 four-object dissimilarity/linkage/start cases and 324 finite Euclidean
    Ward/start cases. A complete-link example requires reordering 3,1,7,15 to 1,3,7,15.
    The source’s sum3 update counterexample gives primitive heights 1,3,27,85 but
    sorted chain 1,3,28,87. Other checks illustrate predecessor ties, the actual Figure4
    ≤3 restart guard at lengths0–3 and safe retained-prefix indexing at lengths4–8
    and equal minima without reciprocity. No author implementation or benchmark was
    executed.
assessments:
- assessment_id: identity
  area: identity
  topic: Nearest-neighbor-chain clustering
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - identity
  - mullner2011
  - benzecri1982
  - juan1982
  - derham1980
  - fastcluster-core
  - fastcluster-wrapper
  - fastcluster-news
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the chain as an agglomerative merge-search procedure parameterized
    by linkage. It is distinct from Ward’s ESS criterion, k-means reassignment, CURE
    representatives, BIRCH compression, nearest-neighbor label voting and the earlier
    reciprocal-pair batch procedure. The NN-chain alias is qualified by clustering
    rather than a bare acronym.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mapping
  - mullner2011
  - benzecri1982
  - juan1982
  - derham1980
  - fastcluster-core
  - fastcluster-wrapper
  - fastcluster-news
  summary: The declared AIO mapping is supported.
  details: Related matches to HierarchicalClustering and UnsupervisedClustering describe
    the task served without asserting task/algorithm equivalence or subclass membership.
    Nine full annotated AIO contexts include the neighbor-voting classifier; its mechanism
    does not identify a reciprocal merge chain.
- assessment_id: reciprocal-chain
  area: evidence
  topic: reciprocal-chain
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - benzecri1982
  - juan1982
  - mullner2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The original descriptions and CADENA listing support following nearest
    neighbors, predecessor tie preference, reciprocal termination, pair merging and
    prefix reuse. The current core uses strict improvement scans and an explicit <=3
    restart guard. The curator implementation safely drops the last reciprocal pair
    and rescans the retained endpoint.
- assessment_id: update-law-conditions
  area: evidence
  topic: update-law-conditions
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Theorem1 explicitly requires reducibility plus commutation of disjoint
    pair merges. Proposition2 covers the five named linkage rules. The sum3 counterexample
    reproduces primitive heights 1,3,27,85 versus invalid sorted chain 1,3,28,87;
    it refutes reducibility alone for history-dependent recurrences.
- assessment_id: stepwise-output-and-ties
  area: evidence
  topic: stepwise-output-and-ties
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - fastcluster-wrapper
  - fastcluster-core
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The paper requires stable sorting and representative relabeling, and the
    pinned wrapper performs both with actual found union roots. A finite complete-link
    example discovers heights3,1,7,15, then gives a valid stepwise sequence1,3,7,15.
    Validation checks greedy admissibility rather than equality to one arbitrary tie
    order.
- assessment_id: matrix-complexity
  area: evidence
  topic: matrix-complexity
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - benzecri1982
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section4.1 explicitly separates the writable quadratic matrix from linear
    auxiliary memory and gives quadratic total time. Benzécri’s bound has a distance-formula
    constant; the record confines it to constant-time scalar updates and does not
    transfer it to arbitrary vector-distance computation.
- assessment_id: procedure-versus-linkage
  area: evidence
  topic: procedure-versus-linkage
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - benzecri1982
  - derham1980
  summary: Supported within the stated primary-source and mathematical scope.
  details: The method is a candidate-selection algorithm across supported linkages.
    Ward is a criterion-specific specialization, while de Rham’s earlier method repeatedly
    finds batches of reciprocal pairs. AIO’s nearest-neighbor classifier predicts
    labels by voting. The cited result concerns valid hierarchical output, not unrestricted
    optimal partitions.
- assessment_id: implementation-boundaries
  area: evidence
  topic: implementation-boundaries
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - fastcluster-core
  - fastcluster-wrapper
  - fastcluster-news
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure4 line6 and pinned core agree on ≤3 / <=3. The corrected finite check
    restarts at lengths0–3 and safely accesses the retained prefix for lengths4–8.
    Static source inspection confirms saved premerge sizes, root-aware output unions,
    stable sorting, Ward scaling and separate matrix/vector dispatch. NEWS documents
    vector-chain removal. The earlier fabricated <3 check and claimed source defect
    are rejected, not evidence against the method.
- assessment_id: constructed-boundaries
  area: consistency
  topic: chain identity, update-law conditions, tied nearest neighbors, valid stepwise
    output, memory accounting and printed-versus-implemented boundaries
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - benzecri1982
  - juan1982
  - derham1980
  - fastcluster-core
  - fastcluster-wrapper
  - fastcluster-news
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: A curator-written rational chain is checked against greedy stepwise validity
    in 11,664 four-object dissimilarity/linkage/start cases and 324 finite Euclidean
    Ward/start cases. A complete-link example requires reordering 3,1,7,15 to 1,3,7,15.
    The source’s sum3 update counterexample gives primitive heights 1,3,27,85 but
    sorted chain 1,3,28,87. Other checks illustrate predecessor ties, the actual Figure4
    ≤3 restart guard at lengths0–3 and safe retained-prefix indexing at lengths4–8
    and equal minima without reciprocity. No author implementation or benchmark was
    executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - identity
  - mapping
  - mullner2011
  - benzecri1982
  - juan1982
  - derham1980
  - fastcluster-core
  - fastcluster-wrapper
  - fastcluster-news
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all names, aliases and kind, definition and
    locators, six claims, seven source versions and hashes, related/rejected mappings,
    both update-law conditions, predecessor tie preference, sorted/relabelled output,
    matrix versus auxiliary memory, separation from Ward and batch procedures, literal
    pseudocode boundaries, pinned static-code scope and actual provenance. DRAFT remains.
    Corrected implementation-boundary claim, limitation3, actual guard calculation,
    report mirror and explicit rejected-observation log were reassessed after recapture.
    Prior Ward-report bytes and saved reviews remain unchanged; issue312 has exact
    finding lineage in this successor.
- assessment_id: figure4-correction
  area: evidence
  topic: Corrected source attribution
  outcome: supported
  target_ids:
  - AIMech:NearestNeighborChainClustering
  evidence_ids:
  - mullner2011
  - fastcluster-core
  - calculation
  summary: Issue312 source-attribution finding resolved.
  details: The recaptured record explicitly uses ≤3, as confirmed in the original-resolution
    Figure4. The calculation now checks actual restart/safe reuse boundaries. The
    report mirrors the corrected record, rejects each erroneous preliminary observation
    and explicitly corrects the preceding Ward report without rewriting it. An actual
    EDIT history exists and corrected-input gates pass.
findings:
- finding_id: F1
  issue_key: nn-chain-figure4-restart-guard-misattribution
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct the false Figure4 restart-guard defect
  description: Figure 4 line 6, PDF p.13, actually prints length(chain) ≤3. The draft
    limitation misreads it as <3 and alleges an out-of-range [-4] access at length3.
    The curator calculation deliberately uses <3 and labels that fabricated variant
    as printed pseudocode. Current source notes/report mirror this error. Both the
    paper and pinned NN_chain_core use ≤3 / <=3; the earlier Ward report contains
    the same preliminary suspicion and needs an explicit successor correction, not
    a rewrite.
  target_ids:
  - AIMech:NearestNeighborChainClustering
  field_paths:
  - limitations[2]
  - claims[implementation-boundaries].statement
  - curator_calculation
  - source_analysis.reading
  evidence_ids:
  - mullner2011
  - fastcluster-core
  - calculation
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NearestNeighborChainClustering.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261013T211701Z-nearest-neighbor-chain-clustering.json
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/nearest-neighbor-chain-clustering-boundaries.py
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/312
  disposition_reason: The recaptured record explicitly uses ≤3, as confirmed in the
    original-resolution Figure4. The calculation now checks actual restart/safe reuse
    boundaries. The report mirrors the corrected record, rejects each erroneous preliminary
    observation and explicitly corrects the preceding Ward report without rewriting
    it. An actual EDIT history exists and corrected-input gates pass.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T212339Z-nn-chain-figure4-guard
    finding_id: F1
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 652 native and 442 unchanged generated records.
  The 837-entry main frontier retains 473 pending and 58 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All59 pages of the four cited primary PDFs visually read; named C++ ranges plus
  complete README, NEWS and license statically read. No author software executed.
- No author-code execution, training, paid service, hardware measurement or empirical
  replication. The source listings and named pinned implementation ranges were statically
  read; historical experiments and floating-point behavior were not reproduced. Constructed
  checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T212339Z-nn-chain-figure4-guard
  relationship: Resolves the same source-attribution finding after correction and
    recapture.
links:
- https://github.com/CultureBotAI/AIMech/issues/312
tags:
- native-concepts
- self-review
- discovery-ongoing
```
