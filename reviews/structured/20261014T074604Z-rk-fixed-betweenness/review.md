# Scientific author self-review of Riondato–Kornaropoulos fixed-sample betweenness approximation

- Review: 20261014T074604Z-rk-fixed-betweenness
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T07:30:42Z
- Finished UTC: 2026-10-14T07:46:04Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the RK all-node fixed-sample estimator as DRAFT with its explicit AIO no-match assessment and conditional confidence assumptions. No unsupported universal sample constant or benchmark claim is added.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:RiondatoKornaropoulosBetweennessSampling
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2593b07b341480f709596150ed3ed4ea993e17ce.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RiondatoKornaropoulosBetweennessSampling | data/curated/RiondatoKornaropoulosBetweennessSampling.yaml | maintained | Riondato–Kornaropoulos fixed-sample betweenness approximation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RiondatoKornaropoulosBetweennessSampling | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 308.83s (0:05:08)<br>Checked 442 record(s); 0 failed.<br>Checked 697 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 387 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 388,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RiondatoKornaropoulosBetweennessSampling | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RiondatoKornaropoulosBetweennessSampling | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RiondatoKornaropoulosBetweennessSampling | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:RiondatoKornaropoulosBetweennessSampling | {"weighted_three_node_graphs": 729, "ordered_pair_cases": 4374, "branching_path_probabilities": {"(0, 3, 5)": "1/3", "(0, 1, 4, 5)": "1/3", "(0, 2, 4, 5)": "1/3"}, "incorrect_uniform_predecessor_probabilities": {"(0, 3, 5)": "1/2", "(0, 1, 4, 5)": "1/4", "(0, 2, 4, 5)": "1/4"}, "disconnected_example": {"ordered_pairs": 12, "reachable_pairs": 3, "empty_mass": "3/4", "central_node_expectation": "1/12", "incorrect_reachable_only_expectation": "1/3"}, "weighted_example": {"vertex_diameter": 3, "weighted_distance_diameter": 2}, "triangle": {"edges": 3, "vertex_diameter": 2, "all_internal_scores_zero": true}, "formula_transcription_arithmetic": {"epsilon": 0.05, "delta": 0.1, "diameter_upper_bound": 4, "vc_upper_bound": 2, "experimental_c": 0.5, "equation3_ceiling": 861, "algorithm1_omitted_one_ceiling": 661, "confidence_certified": false}} |

## Scientific And Domain Assessments

### Riondato–Kornaropoulos fixed-sample betweenness approximation

identity: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Retain this distinct DRAFT algorithm.

Retain the all-node fixed-size path-indicator estimator separately from KADABRA adaptive stopping and its conditional sampler, ABRA pair-fraction estimators, exact Brandes and pivot-dependency sampling. Top-k, edge, bounded-distance and walk estimands remain separate leads.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

The explicit AIO mapping assessment is supported within its stated scope.

Retain a bounded no-match over eleven complete AIO contexts and seven native neighbors. The identity is a particular randomized graph procedure with VC-based sample allocation, not just the abstract centrality functional. Learning-theory support does not make it a neural architecture, clustering task, bias concept or data-preparation identity.

### domain-and-estimand

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Uniform distinct ordered-pair sampling plus conditional uniform shortest paths targets denominator n(n-1). Unreachable pairs remain zero draws; positive weights exclude shortest-path count cycles. At an independently fixed r, indicator averaging is unbiased; no optional-stopping claim is made.

### vc-based-fixed-count

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Corollary1 and Equation3 yield floor(log2(D_hat-2))+1 and an integer-ceiled fixed r when D_hat&gt;=3 is valid. The guarantee is expressly conditional on a sufficient uniform-convergence constant. The manuscript only estimates c approximately0.5; the record does not convert it into a certified constant.

### count-weighted-path-sampling

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Algorithm1 retains predecessor path counts. Multiplying sigma_sz/sigma_sx along backward steps telescopes to1/sigma_st. The independent finite simple-path oracle agrees on4374 ordered cases; unequal predecessor multiplicity exposes uniform-predecessor bias.

### diameter-and-transcription-boundaries

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Vertex count on weighted shortest paths is distinct from weighted length and minimum-hop paths. A largest weak-component size is a safe upper bound, and VD&lt;=2 has zero internal scores. The omitted+1 and integer rounding are explicit, as are the undirected restriction on the unique-path VC bound and the excluded diameter-sample reuse dependence.

### finite-law-and-normalization-checks

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Exact enumeration and unequal-branch construction support only the stated finite laws. The chain-plus-isolate has three reachable pairs of12, empty mass3/4 and central expectation1/12; removing unreachable draws gives1/3. Arithmetic sample sizes861 versus661 are explicitly not a confidence-coverage certification.

### identity-and-evaluation-scope

evidence: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Supported within the stated primary-source and mathematical scope.

Source experiments are bounded to the historical C/igraph implementation, five runs, selected networks and experimental c=0.5/delta0.1. They establish no universal speedup, current implementation validity or equivalence to fraction estimators. No numerical benchmark result is adopted.

### fixed-count versus stopped confidence, uniform complete-path laws, empty-path mass, positive-weight and vertex-diameter limits, sufficient constants and pseudocode transcription

consistency: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Constructed calculations support the stated distinctions.

Exact finite arithmetic checks count-weighted predecessor sampling against independent simple-path enumeration on729 small directed weighted graphs, unequal predecessor counts, empty-path mass and endpoint normalization. Separate arithmetic exposes vertex-count versus weighted-distance and omitted-+1 sample-size differences. It does not certify a universal VC constant, general probability guarantee, author code or benchmarks.

### All maintained fields

provenance: supported. Targets: AIMech:RiondatoKornaropoulosBetweennessSampling.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All maintained fields, six claims, precise locators, primary source/version limits and no-match assessment inspected. Source Equation3 supplies the maintained count rather than literal pseudocode. Independent main-stream selection, positive weights, aggregate unreachable mass and integer rounding are explicit. Complete current record read before capture and its byte-identical contents reassessed after the source rereading.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T072629Z-rk-fixed-betweenness.json | supports | Compared all 442 pinned AIO and 695 native identities; no normalized match. Ignored- and hidden-inclusive searches of three full checkouts returned 51,0,0 lines, all read as existing RK source URLs, leads or query strings. Semantic assessment covered 155 AIO and 540 native definitions: all155 prior AIO and539 prior native rows verified unchanged, and the newly added conditional KADABRA sampler row and full record read. Eleven complete AIO contexts and seven full native neighbors were assessed; corrected KADABRA contexts were reassessed. The maintained identity is all-node fixed-sample path-indicator averaging with a VC-based sample count, not KADABRA adaptive stopping, ABRA pair-fraction averaging, exact Brandes accumulation, pivot dependency sampling or a conditional path sampler. Top-k and other estimands require separate assessment. |
| mapping | sources/aio/aio.json | supports | Retain a bounded no-match over eleven complete AIO contexts and seven native neighbors. The identity is a particular randomized graph procedure with VC-based sample allocation, not just the abstract centrality functional. Learning-theory support does not make it a neural architecture, clustering task, bias concept or data-preparation identity. |
| riondatokornaropoulos2016author | https://www.rionda.to/papers/RiondatoKornaropoulos-BetweennessSampling-DMKD.pdf; Sections 4 and 5.1, Corollary 1, Equation 3 and Algorithm 1, PDF pp. 9 and 15–19; Section 3.1, PDF pp. 5–6; Section 5.1, pp. 15–19; Theorem 1 and following constant discussion, PDF p. 8; Corollary 1, p. 9; Section 5.1, Equation 3, p. 15; Section 5.1, PDF pp. 16–17 and Algorithm 1; curator weighted-path calculations in research/discovery/rk-path-boundaries.py; Definition 1, PDF p. 6; Corollary 1 and Lemma 2, pp. 9–10; directed counterexample, pp. 11–12; Equation 3, p. 15; Algorithm 1 and diameter approximation, pp. 17–18; Section 5.1, PDF pp. 15–19; explicit curator calculations in research/discovery/rk-path-boundaries.py; Sections 5.1–5.2, 6 and 7, PDF pp. 15–35; named-neighbor distinction assessed against the maintained KADABRA and ABRA records | supports | 37-page author-hosted manuscript with placeholder journal header and received/accepted dates; author catalog identifies DMKD30(2):438-475,2016. No publisher-byte equivalence. All37 pages and47references read as text, with rendered pages6,8,9,15,17 inspected. Other figures/tables and many proof displays remain text-only. The linked author catalog identifies the2016 journal article and2014 conference version; no version-specific publisher DOI or byte equivalence is asserted. |
| calculation | research/discovery/rk-path-boundaries.py | supports | Exact finite arithmetic checks count-weighted predecessor sampling against independent simple-path enumeration on729 small directed weighted graphs, unequal predecessor counts, empty-path mass and endpoint normalization. Separate arithmetic exposes vertex-count versus weighted-distance and omitted-+1 sample-size differences. It does not certify a universal VC constant, general probability guarantee, author code or benchmarks. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This round adds one DRAFT concept, reaching 696 native and 442 unchanged AIO records. The main frontier has 881 entries, including 472 pending and 58 partly addressed cohorts; nested leads remain.
- All37 author-manuscript pages and47references previously read. Rendered pages6,8,15,17 previously inspected; pages8,9,15,17 reread/inspected in this continuation. Additional text rereading covers5,6,16,18,19,27.
- Other figures/tables and many proof displays remain text-only. No author-code execution, general VC-theorem certification, exact universal c value, benchmark replication or publisher-byte equivalence.
- The fixed-sample RK all-node estimator is added. Relative top-k, edge, bounded-distance and walk variants, diameter-sample reuse, other centrality sources and the publication-catalog inventory retain separate assessments.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T074604Z-rk-fixed-betweenness
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Riondato–Kornaropoulos fixed-sample betweenness
  approximation
started_at: '2026-10-14T07:30:42Z'
finished_at: '2026-10-14T07:46:04Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged fixed-count versus stopped confidence,
    uniform complete-path laws, empty-path mass, positive-weight and vertex-diameter
    limits, sufficient constants and pseudocode transcription. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the RK all-node fixed-sample estimator as DRAFT with its explicit
  AIO no-match assessment and conditional confidence assumptions. No unsupported universal
  sample constant or benchmark claim is added.
source:
  git_revision: 2593b07b341480f709596150ed3ed4ea993e17ce
  state: working_tree
  inputs:
  - path: data/aio/BidirectionalLayer.yaml
    sha256: e5a9046594e0cc0b0ddf152c6d84745d25b3a3246273babbd7a859f01d7270c8
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/DeepActiveLearning.yaml
    sha256: b04c9aa74728adbe1bd907cb3f0e15b263bda18ed29660babce092daeed2b4f9
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/RankingBias.yaml
    sha256: 3e931657e0ee2a47e36a7858dbb8f26f00b565040f4fedd138f55353551160b0
    role: context
  - path: data/aio/RepresentationBias.yaml
    sha256: 5ac7d1455814eb8305b1ab9d0934e61fc50c09fe3dfd7724da5fdb4a21f360b2
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/ABRASFixedSampleBetweenness.yaml
    sha256: 54cfede513b8c180857a7be3cdb1c6a330dd2471df8fd4b3cf0b277fa353ce92
    role: context
  - path: data/curated/ABRASProgressiveBetweenness.yaml
    sha256: 9b1d85ceb3a3305970c23930e67cda59be68985f8fd5da6b4ae3ec94c655a113
    role: context
  - path: data/curated/Apriori.yaml
    sha256: ecdb6f7857fe97ae313e2e6c95984852213e1647bc4b4ab81a30e81a989c71a6
    role: context
  - path: data/curated/BrandesBetweennessCentrality.yaml
    sha256: 2ff7051fa27a4e1150545d634b90599a335b909b1fe6956441260c5284830e21
    role: context
  - path: data/curated/BrandesPichPivotCentralityEstimation.yaml
    sha256: 7f8492fc3a881da6c35439412b535572f687215410b85b05439d2ca8d799b9c1
    role: context
  - path: data/curated/KADABRAAdaptiveBetweenness.yaml
    sha256: 8add303f8ebaa0330d3a2ffde947c7a5113fdb3abce5749e937cffb27fb9d8e3
    role: context
  - path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
    sha256: 8c1b7efb694d77cb27feb07be1b6a962af20f59312829909331ce77605b1b442
    role: context
  - path: data/curated/RiondatoKornaropoulosBetweennessSampling.yaml
    sha256: ea24a1a5cf5019380c36640508cc8a7458203f4491276551898d5477da07f6b8
    role: target
  - path: research/discovery/20261014T072629Z-rk-fixed-betweenness.json
    sha256: eaefcf440895241721011b501386970d52fdf969f7403b73f8da8dae110cd2c6
    role: context
  - path: research/discovery/rk-path-boundaries.py
    sha256: 8571513258fe3418f9af5c80e7afa1a54a7629a46807cc7bfc5d417f0af7c1b1
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
- target_id: AIMech:RiondatoKornaropoulosBetweennessSampling
  path: data/curated/RiondatoKornaropoulosBetweennessSampling.yaml
  label: Riondato–Kornaropoulos fixed-sample betweenness approximation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RiondatoKornaropoulosBetweennessSampling.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:RiondatoKornaropoulosBetweennessSampling'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: Complete author manuscript read as text; only selected mathematical displays
      and figures visually inspected. No general VC proof certification, universal
      c=0.5 guarantee, author-code execution, benchmark replication or publisher-byte
      equivalence.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 308.83s (0:05:08)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 697 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 387 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 388,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
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
  - AIMech:RiondatoKornaropoulosBetweennessSampling
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
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/rk-path-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  exit_code: 0
  expected_exit_code: 0
  summary: '{"weighted_three_node_graphs": 729, "ordered_pair_cases": 4374, "branching_path_probabilities":
    {"(0, 3, 5)": "1/3", "(0, 1, 4, 5)": "1/3", "(0, 2, 4, 5)": "1/3"}, "incorrect_uniform_predecessor_probabilities":
    {"(0, 3, 5)": "1/2", "(0, 1, 4, 5)": "1/4", "(0, 2, 4, 5)": "1/4"}, "disconnected_example":
    {"ordered_pairs": 12, "reachable_pairs": 3, "empty_mass": "3/4", "central_node_expectation":
    "1/12", "incorrect_reachable_only_expectation": "1/3"}, "weighted_example": {"vertex_diameter":
    3, "weighted_distance_diameter": 2}, "triangle": {"edges": 3, "vertex_diameter":
    2, "all_internal_scores_zero": true}, "formula_transcription_arithmetic": {"epsilon":
    0.05, "delta": 0.1, "diameter_upper_bound": 4, "vc_upper_bound": 2, "experimental_c":
    0.5, "equation3_ceiling": 861, "algorithm1_omitted_one_ceiling": 661, "confidence_certified":
    false}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T072629Z-rk-fixed-betweenness.json
  accessed_at: '2026-10-14T07:30:42Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 695 native identities; no normalized match.
    Ignored- and hidden-inclusive searches of three full checkouts returned 51,0,0
    lines, all read as existing RK source URLs, leads or query strings. Semantic assessment
    covered 155 AIO and 540 native definitions: all155 prior AIO and539 prior native
    rows verified unchanged, and the newly added conditional KADABRA sampler row and
    full record read. Eleven complete AIO contexts and seven full native neighbors
    were assessed; corrected KADABRA contexts were reassessed. The maintained identity
    is all-node fixed-sample path-indicator averaging with a VC-based sample count,
    not KADABRA adaptive stopping, ABRA pair-fraction averaging, exact Brandes accumulation,
    pivot dependency sampling or a conditional path sampler. Top-k and other estimands
    require separate assessment.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T07:30:42Z'
  support: supports
  summary: Retain a bounded no-match over eleven complete AIO contexts and seven native
    neighbors. The identity is a particular randomized graph procedure with VC-based
    sample allocation, not just the abstract centrality functional. Learning-theory
    support does not make it a neural architecture, clustering task, bias concept
    or data-preparation identity.
- evidence_id: riondatokornaropoulos2016author
  kind: primary_source
  reference: https://www.rionda.to/papers/RiondatoKornaropoulos-BetweennessSampling-DMKD.pdf
  locator: Sections 4 and 5.1, Corollary 1, Equation 3 and Algorithm 1, PDF pp. 9
    and 15–19; Section 3.1, PDF pp. 5–6; Section 5.1, pp. 15–19; Theorem 1 and following
    constant discussion, PDF p. 8; Corollary 1, p. 9; Section 5.1, Equation 3, p.
    15; Section 5.1, PDF pp. 16–17 and Algorithm 1; curator weighted-path calculations
    in research/discovery/rk-path-boundaries.py; Definition 1, PDF p. 6; Corollary
    1 and Lemma 2, pp. 9–10; directed counterexample, pp. 11–12; Equation 3, p. 15;
    Algorithm 1 and diameter approximation, pp. 17–18; Section 5.1, PDF pp. 15–19;
    explicit curator calculations in research/discovery/rk-path-boundaries.py; Sections
    5.1–5.2, 6 and 7, PDF pp. 15–35; named-neighbor distinction assessed against the
    maintained KADABRA and ABRA records
  accessed_at: '2026-10-14T06:07:46Z'
  snapshot_sha256: b783f401a0a6cc637fe6f6c56dfeeca093cf7a796b44b939012511ec86647653
  support: supports
  summary: 37-page author-hosted manuscript with placeholder journal header and received/accepted
    dates; author catalog identifies DMKD30(2):438-475,2016. No publisher-byte equivalence.
    All37 pages and47references read as text, with rendered pages6,8,9,15,17 inspected.
    Other figures/tables and many proof displays remain text-only. The linked author
    catalog identifies the2016 journal article and2014 conference version; no version-specific
    publisher DOI or byte equivalence is asserted.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/rk-path-boundaries.py
  accessed_at: '2026-10-14T07:33:16Z'
  snapshot_sha256: 8571513258fe3418f9af5c80e7afa1a54a7629a46807cc7bfc5d417f0af7c1b1
  support: supports
  summary: Exact finite arithmetic checks count-weighted predecessor sampling against
    independent simple-path enumeration on729 small directed weighted graphs, unequal
    predecessor counts, empty-path mass and endpoint normalization. Separate arithmetic
    exposes vertex-count versus weighted-distance and omitted-+1 sample-size differences.
    It does not certify a universal VC constant, general probability guarantee, author
    code or benchmarks.
assessments:
- assessment_id: identity
  area: identity
  topic: Riondato–Kornaropoulos fixed-sample betweenness approximation
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - identity
  - riondatokornaropoulos2016author
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the all-node fixed-size path-indicator estimator separately from
    KADABRA adaptive stopping and its conditional sampler, ABRA pair-fraction estimators,
    exact Brandes and pivot-dependency sampling. Top-k, edge, bounded-distance and
    walk estimands remain separate leads.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - mapping
  - riondatokornaropoulos2016author
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Retain a bounded no-match over eleven complete AIO contexts and seven native
    neighbors. The identity is a particular randomized graph procedure with VC-based
    sample allocation, not just the abstract centrality functional. Learning-theory
    support does not make it a neural architecture, clustering task, bias concept
    or data-preparation identity.
- assessment_id: domain-and-estimand
  area: evidence
  topic: domain-and-estimand
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Uniform distinct ordered-pair sampling plus conditional uniform shortest
    paths targets denominator n(n-1). Unreachable pairs remain zero draws; positive
    weights exclude shortest-path count cycles. At an independently fixed r, indicator
    averaging is unbiased; no optional-stopping claim is made.
- assessment_id: vc-based-fixed-count
  area: evidence
  topic: vc-based-fixed-count
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  summary: Supported within the stated primary-source and mathematical scope.
  details: Corollary1 and Equation3 yield floor(log2(D_hat-2))+1 and an integer-ceiled
    fixed r when D_hat>=3 is valid. The guarantee is expressly conditional on a sufficient
    uniform-convergence constant. The manuscript only estimates c approximately0.5;
    the record does not convert it into a certified constant.
- assessment_id: count-weighted-path-sampling
  area: evidence
  topic: count-weighted-path-sampling
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Algorithm1 retains predecessor path counts. Multiplying sigma_sz/sigma_sx
    along backward steps telescopes to1/sigma_st. The independent finite simple-path
    oracle agrees on4374 ordered cases; unequal predecessor multiplicity exposes uniform-predecessor
    bias.
- assessment_id: diameter-and-transcription-boundaries
  area: evidence
  topic: diameter-and-transcription-boundaries
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Vertex count on weighted shortest paths is distinct from weighted length
    and minimum-hop paths. A largest weak-component size is a safe upper bound, and
    VD<=2 has zero internal scores. The omitted+1 and integer rounding are explicit,
    as are the undirected restriction on the unique-path VC bound and the excluded
    diameter-sample reuse dependence.
- assessment_id: finite-law-and-normalization-checks
  area: evidence
  topic: finite-law-and-normalization-checks
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exact enumeration and unequal-branch construction support only the stated
    finite laws. The chain-plus-isolate has three reachable pairs of12, empty mass3/4
    and central expectation1/12; removing unreachable draws gives1/3. Arithmetic sample
    sizes861 versus661 are explicitly not a confidence-coverage certification.
- assessment_id: identity-and-evaluation-scope
  area: evidence
  topic: identity-and-evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  summary: Supported within the stated primary-source and mathematical scope.
  details: Source experiments are bounded to the historical C/igraph implementation,
    five runs, selected networks and experimental c=0.5/delta0.1. They establish no
    universal speedup, current implementation validity or equivalence to fraction
    estimators. No numerical benchmark result is adopted.
- assessment_id: constructed-boundaries
  area: consistency
  topic: fixed-count versus stopped confidence, uniform complete-path laws, empty-path
    mass, positive-weight and vertex-diameter limits, sufficient constants and pseudocode
    transcription
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - riondatokornaropoulos2016author
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact finite arithmetic checks count-weighted predecessor sampling against
    independent simple-path enumeration on729 small directed weighted graphs, unequal
    predecessor counts, empty-path mass and endpoint normalization. Separate arithmetic
    exposes vertex-count versus weighted-distance and omitted-+1 sample-size differences.
    It does not certify a universal VC constant, general probability guarantee, author
    code or benchmarks.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:RiondatoKornaropoulosBetweennessSampling
  evidence_ids:
  - identity
  - mapping
  - riondatokornaropoulos2016author
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All maintained fields, six claims, precise locators,
    primary source/version limits and no-match assessment inspected. Source Equation3
    supplies the maintained count rather than literal pseudocode. Independent main-stream
    selection, positive weights, aggregate unreachable mass and integer rounding are
    explicit. Complete current record read before capture and its byte-identical contents
    reassessed after the source rereading.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This round adds one DRAFT concept, reaching 696 native and 442 unchanged AIO records.
  The main frontier has 881 entries, including 472 pending and 58 partly addressed
  cohorts; nested leads remain.
- All37 author-manuscript pages and47references previously read. Rendered pages6,8,15,17
  previously inspected; pages8,9,15,17 reread/inspected in this continuation. Additional
  text rereading covers5,6,16,18,19,27.
- Other figures/tables and many proof displays remain text-only. No author-code execution,
  general VC-theorem certification, exact universal c value, benchmark replication
  or publisher-byte equivalence.
- The fixed-sample RK all-node estimator is added. Relative top-k, edge, bounded-distance
  and walk variants, diameter-sample reuse, other centrality sources and the publication-catalog
  inventory retain separate assessments.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
