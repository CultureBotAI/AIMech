# Scientific author self-review of HAC-ML network clustering

- Review: 20261014T011057Z-hacml
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T01:05:07Z
- Finished UTC: 2026-10-14T01:10:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HAC-ML as a DRAFT algorithm with related AIO clustering tasks. Author self-review supports the profile-likelihood mechanism and separate Bayesian selection while preserving a printed shorthand discrepancy, restricted-search qualifications and empirical evaluation limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:HACML
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f9030f612fbe81d829a98721437e1201d7ba0c9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HACML | data/curated/HACML.yaml | maintained | HAC-ML network clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HACML | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 154.85s (0:02:34)<br>Checked 442 record(s); 0 failed.<br>Checked 669 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 356 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 353,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HACML | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HACML | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HACML | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:HACML | {"single_mismatch_profile_ratio": "1/4", "printed_single_mismatch_expression": "1/2", "single_mismatch_integrated_ratio": "2/3", "matching_external_edges_profile_ratio": "1", "matching_external_edges_integrated_ratio": "4/3", "singleton_collapse_ratio": "1", "two_independent_mismatch_types_ratio": "1/16", "balanced_test_precision": "1/2", "precision_at_one_percent_prevalence": "1/100", "scope": "Exact source-formula and base-rate examples. No author code, full merge sequence, benchmark or universal optimality claim."} |

## Scientific And Domain Assessments

### HAC-ML network clustering

identity: supported. Targets: AIMech:HACML.

Retain this distinct DRAFT algorithm.

Retain the 2011 profile-likelihood network merge guide with separate integrated-probability model selection. HAC-E, HAC-ES and HAC-Q are different scoring rules; generic HAC, ROCK, graph degree linkage and CliXO do not identify this algorithm.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:HACML.

The explicit AIO mapping assessment is supported within its stated scope.

The related HierarchicalClustering and UnsupervisedClustering targets describe relevant tasks, not equivalent algorithm identities or asserted superclasses. The observed-interaction graph is not itself a conditional-dependence or causal graph.

### profile-likelihood-guide

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

Equations 1–5 distinguish the Bernoulli block model and profiled edge/hole probabilities from uniform-prior integrated factors. The selected external-group merge ratio guides a greedy hierarchy; no global optimum or posterior ensemble is asserted.

### bayesian-boundaries

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

Equations 7–8 separately select top-level stopping and terminal collapse, with the latter requiring both children already collapsed. The paper explicitly omits alternative merge/split multiplicities. The two-singleton collapse ratio is one under either possible internal edge.

### multiple-edge-types

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

The extension multiplies independent type likelihoods under shared group structure. The constructed two-type score is 1/16, rather than a score of an edge union. Table 3 has both small improvements and decreases, so no consistent joint-network benefit is claimed.

### printed-score-boundary

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

The one-mismatch profiled ratio is 1/4 under Equations 2 and 5, whereas the singleton prose shorthand yields 1/2. The integrated ratio is separately 2/3. This is a printed-formula comparison, with implementation consequences expressly unverified.

### complexity-and-search

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

The faster stated complexity depends on a priority queue, lazy evaluation, common-neighbor candidates and sparse-network assumptions. Candidate restriction and irrevocable greedy selection preclude reading this as exhaustive optimization.

### evaluation-scope

evidence: supported. Targets: AIMech:HACML.

Supported within the stated primary-source and mathematical scope.

Held-out edges are compared with an equal number of sampled holes; the source acknowledges the resulting optimistic practical interpretation on sparse graphs. The finite base-rate example changes precision from 1/2 to 1/100 with identical conditional rates. Degree filtering and common-vertex joint comparisons remain explicit.

### profile versus integrated scores, omitted partition multiplicities, restricted greedy search and evaluation prevalence

consistency: supported. Targets: AIMech:HACML.

Constructed calculations support the stated distinctions.

Exact profiled versus integrated block-score, collapse, independent-type and balanced-test base-rate checks. No full merge sequence or author-code behavior is asserted.

### All maintained fields

provenance: supported. Targets: AIMech:HACML.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All six claims and remaining maintained fields are supported within their recorded scope. The profile/integrated distinction, source shorthand discrepancy, omitted model multiplicities, restricted search and balanced-negative evaluation remain explicit. No repository correction was identified; DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T010443Z-hacml.json | supports | Compared all 442 pinned AIO and 666 native IDs, names, aliases and scoped synonyms for the three candidates and their publication identifiers; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 26, 0, 0 lines. All matches were read and are prior source/discovery context, with no existing maintained identity. Semantic assessment covered 44 AIO and 260 native definitions: 41 AIO and 228 native rows were unchanged from earlier reading; three additional AIO and 32 additional native definitions were read. Fourteen complete annotated AIO node/edge/generated contexts and the candidate-specific native records were inspected. Retain the 2011 profiled network-likelihood merge guide with separate Bayesian top/terminal selection. ROCK counts shared neighbors with a size normalization, graph degree linkage multiplies directed degree averages, and CliXO selects persistent informative cliques. Generic HAC, a fitted interactome and the HAC-E/ES/Q score variants are distinct scopes. |
| mapping | sources/aio/aio.json | supports | The related HierarchicalClustering and UnsupervisedClustering targets describe relevant tasks, not equivalent algorithm identities or asserted superclasses. The observed-interaction graph is not itself a conditional-dependence or causal graph. |
| park2011 | https://link.springer.com/content/pdf/10.1186/1471-2105-12-S1-S44.pdf; Methods, Preliminary definitions and Agglomerative clustering, PDF pp. 2–4, Equations 1–8 and pseudocode; Methods, PDF pp. 2–3, Equations 1–5 and greedy pseudocode; Conclusions, p. 9; Methods, PDF pp. 2–4, Equations 2, 7–8 and model-selection qualifications; Extension to multiple edge types, PDF p. 4; Synergy in mixed networks, pp. 8–9 and Table 3; Methods, PDF pp. 2–3, Equations 2 and 5 and singleton-mismatch paragraph; curator calculation in research/discovery/hacml-boundaries.py; Greedy agglomerative algorithm, PDF pp. 3–4; Conclusions, p. 9; Performance Evaluation and Results, PDF pp. 4–8, Tables 1–3 and Figures 1–4 | supports | BMC Bioinformatics12(Suppl1):S44,2011-02-15; all10 publisher PDF pages and36references read, including Equations1–11, pseudocode, four figures and three tables. Supplementary author code not inspected. |
| calculation | research/discovery/hacml-boundaries.py | supports | Exact profiled versus integrated block-score, collapse, independent-type and balanced-test base-rate checks. No full merge sequence or author-code behavior is asserted. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This cohort step adds one DRAFT record, reaching 667 native and 442 unchanged AIO records. The main frontier now has 852 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- All10 pages each of the NeXO2013 and HACML2011 primary papers were read, with references and every figure, table and method equation inspected. This record cites only its listed evidence sources. Full193-line extracted-text diff read; all differences are publication headers, pagination and copyright lines. Advance-copy page10 rendered and read; both PDFs show the same reciprocal bootstrap equation. Other advance-copy pages were not separately visually read.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T011057Z-hacml
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of HAC-ML network clustering
started_at: '2026-10-14T01:05:07Z'
finished_at: '2026-10-14T01:10:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged profile versus integrated scores, omitted
    partition multiplicities, restricted greedy search and evaluation prevalence.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain HAC-ML as a DRAFT algorithm with related AIO clustering tasks. Author
  self-review supports the profile-likelihood mechanism and separate Bayesian selection
  while preserving a printed shorthand discrepancy, restricted-search qualifications
  and empirical evaluation limits.
source:
  git_revision: 0f9030f612fbe81d829a98721437e1201d7ba0c9
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/EthicalLLM.yaml
    sha256: cd35ce670508ad59d04c55392e04f481415e2245c36f87185700b83bf14636f6
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
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
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
  - path: data/curated/CliXO.yaml
    sha256: 68a4f69aab547e5d7c0bded8104c312b719d3f5cad62941e8c44ed697fd61fa8
    role: context
  - path: data/curated/GraphDegreeLinkage.yaml
    sha256: 0bd60481926261ff2fb8d69f0404a5d0132f3de4f0c915758bfaffa77fd62f8f
    role: context
  - path: data/curated/HACML.yaml
    sha256: 06a6b1b83616ce816b112084bfcfb2f29cd061a2fa0d07c3b66c6e2cfcbaae4a
    role: target
  - path: data/curated/ROCKClustering.yaml
    sha256: 5be4a00f39b229a245cd86e01d80e2b39cf2f09bb26487d7b911ca9d95625bec
    role: context
  - path: research/discovery/20261014T010443Z-hacml.json
    sha256: 55e6b0f102f830852e721b203229e4e1fc32cc565db73e3b0ec14a638180d7aa
    role: context
  - path: research/discovery/hacml-boundaries.py
    sha256: 7c5ddd7d5bd445a17645625ddb3dea955d3335501e77bce1c50ad41b5ae8324e
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
- target_id: AIMech:HACML
  path: data/curated/HACML.yaml
  label: HAC-ML network clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HACML.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:HACML'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HACML
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: The published main papers were read completely. Author code, experimental
      data and supplements were not audited or executed. The NeXO advance copy was
      compared by extracted text and visually on page 10 only; this is not a second
      full visual audit. Constructed checks do not replicate a benchmark or certify
      a complete algorithm.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HACML
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 154.85s (0:02:34)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 669 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 356 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 353,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HACML
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
  - AIMech:HACML
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
  - AIMech:HACML
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/hacml-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HACML
  exit_code: 0
  expected_exit_code: 0
  summary: '{"single_mismatch_profile_ratio": "1/4", "printed_single_mismatch_expression":
    "1/2", "single_mismatch_integrated_ratio": "2/3", "matching_external_edges_profile_ratio":
    "1", "matching_external_edges_integrated_ratio": "4/3", "singleton_collapse_ratio":
    "1", "two_independent_mismatch_types_ratio": "1/16", "balanced_test_precision":
    "1/2", "precision_at_one_percent_prevalence": "1/100", "scope": "Exact source-formula
    and base-rate examples. No author code, full merge sequence, benchmark or universal
    optimality claim."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T010443Z-hacml.json
  accessed_at: '2026-10-14T01:05:07Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 666 native IDs, names, aliases and scoped
    synonyms for the three candidates and their publication identifiers; no normalized
    identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery,
    older discovery and original Documents checkouts returned 26, 0, 0 lines. All
    matches were read and are prior source/discovery context, with no existing maintained
    identity. Semantic assessment covered 44 AIO and 260 native definitions: 41 AIO
    and 228 native rows were unchanged from earlier reading; three additional AIO
    and 32 additional native definitions were read. Fourteen complete annotated AIO
    node/edge/generated contexts and the candidate-specific native records were inspected.
    Retain the 2011 profiled network-likelihood merge guide with separate Bayesian
    top/terminal selection. ROCK counts shared neighbors with a size normalization,
    graph degree linkage multiplies directed degree averages, and CliXO selects persistent
    informative cliques. Generic HAC, a fitted interactome and the HAC-E/ES/Q score
    variants are distinct scopes.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T01:05:07Z'
  support: supports
  summary: The related HierarchicalClustering and UnsupervisedClustering targets describe
    relevant tasks, not equivalent algorithm identities or asserted superclasses.
    The observed-interaction graph is not itself a conditional-dependence or causal
    graph.
- evidence_id: park2011
  kind: primary_source
  reference: https://link.springer.com/content/pdf/10.1186/1471-2105-12-S1-S44.pdf
  locator: Methods, Preliminary definitions and Agglomerative clustering, PDF pp.
    2–4, Equations 1–8 and pseudocode; Methods, PDF pp. 2–3, Equations 1–5 and greedy
    pseudocode; Conclusions, p. 9; Methods, PDF pp. 2–4, Equations 2, 7–8 and model-selection
    qualifications; Extension to multiple edge types, PDF p. 4; Synergy in mixed networks,
    pp. 8–9 and Table 3; Methods, PDF pp. 2–3, Equations 2 and 5 and singleton-mismatch
    paragraph; curator calculation in research/discovery/hacml-boundaries.py; Greedy
    agglomerative algorithm, PDF pp. 3–4; Conclusions, p. 9; Performance Evaluation
    and Results, PDF pp. 4–8, Tables 1–3 and Figures 1–4
  accessed_at: '2026-10-14T00:38:22Z'
  snapshot_sha256: e930abd762f0f7c51d7671b3f605bc1fd2a35cdc230b668515c7778ffcb73b60
  support: supports
  summary: BMC Bioinformatics12(Suppl1):S44,2011-02-15; all10 publisher PDF pages
    and36references read, including Equations1–11, pseudocode, four figures and three
    tables. Supplementary author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/hacml-boundaries.py
  accessed_at: '2026-10-14T01:10:50Z'
  snapshot_sha256: 7c5ddd7d5bd445a17645625ddb3dea955d3335501e77bce1c50ad41b5ae8324e
  support: supports
  summary: Exact profiled versus integrated block-score, collapse, independent-type
    and balanced-test base-rate checks. No full merge sequence or author-code behavior
    is asserted.
assessments:
- assessment_id: identity
  area: identity
  topic: HAC-ML network clustering
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - identity
  - park2011
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the 2011 profile-likelihood network merge guide with separate integrated-probability
    model selection. HAC-E, HAC-ES and HAC-Q are different scoring rules; generic
    HAC, ROCK, graph degree linkage and CliXO do not identify this algorithm.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - mapping
  - park2011
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: The related HierarchicalClustering and UnsupervisedClustering targets describe
    relevant tasks, not equivalent algorithm identities or asserted superclasses.
    The observed-interaction graph is not itself a conditional-dependence or causal
    graph.
- assessment_id: profile-likelihood-guide
  area: evidence
  topic: profile-likelihood-guide
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations 1–5 distinguish the Bernoulli block model and profiled edge/hole
    probabilities from uniform-prior integrated factors. The selected external-group
    merge ratio guides a greedy hierarchy; no global optimum or posterior ensemble
    is asserted.
- assessment_id: bayesian-boundaries
  area: evidence
  topic: bayesian-boundaries
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations 7–8 separately select top-level stopping and terminal collapse,
    with the latter requiring both children already collapsed. The paper explicitly
    omits alternative merge/split multiplicities. The two-singleton collapse ratio
    is one under either possible internal edge.
- assessment_id: multiple-edge-types
  area: evidence
  topic: multiple-edge-types
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The extension multiplies independent type likelihoods under shared group
    structure. The constructed two-type score is 1/16, rather than a score of an edge
    union. Table 3 has both small improvements and decreases, so no consistent joint-network
    benefit is claimed.
- assessment_id: printed-score-boundary
  area: evidence
  topic: printed-score-boundary
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The one-mismatch profiled ratio is 1/4 under Equations 2 and 5, whereas
    the singleton prose shorthand yields 1/2. The integrated ratio is separately 2/3.
    This is a printed-formula comparison, with implementation consequences expressly
    unverified.
- assessment_id: complexity-and-search
  area: evidence
  topic: complexity-and-search
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  summary: Supported within the stated primary-source and mathematical scope.
  details: The faster stated complexity depends on a priority queue, lazy evaluation,
    common-neighbor candidates and sparse-network assumptions. Candidate restriction
    and irrevocable greedy selection preclude reading this as exhaustive optimization.
- assessment_id: evaluation-scope
  area: evidence
  topic: evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Held-out edges are compared with an equal number of sampled holes; the
    source acknowledges the resulting optimistic practical interpretation on sparse
    graphs. The finite base-rate example changes precision from 1/2 to 1/100 with
    identical conditional rates. Degree filtering and common-vertex joint comparisons
    remain explicit.
- assessment_id: constructed-boundaries
  area: consistency
  topic: profile versus integrated scores, omitted partition multiplicities, restricted
    greedy search and evaluation prevalence
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - park2011
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact profiled versus integrated block-score, collapse, independent-type
    and balanced-test base-rate checks. No full merge sequence or author-code behavior
    is asserted.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:HACML
  evidence_ids:
  - identity
  - mapping
  - park2011
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All six claims and remaining maintained fields are
    supported within their recorded scope. The profile/integrated distinction, source
    shorthand discrepancy, omitted model multiplicities, restricted search and balanced-negative
    evaluation remain explicit. No repository correction was identified; DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This cohort step adds one DRAFT record, reaching 667 native and 442 unchanged AIO
  records. The main frontier now has 852 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- All10 pages each of the NeXO2013 and HACML2011 primary papers were read, with references
  and every figure, table and method equation inspected. This record cites only its
  listed evidence sources. Full193-line extracted-text diff read; all differences
  are publication headers, pagination and copyright lines. Advance-copy page10 rendered
  and read; both PDFs show the same reciprocal bootstrap equation. Other advance-copy
  pages were not separately visually read.
- Primary methods were read; no author-code execution, model fitting, paid service,
  data upload, hardware benchmark or formal theorem certification. Constructed arithmetic
  examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved
  after automatic-review rejection; only the isolated recovery checkout is changed.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
