# Scientific author self-review of HAC-ES network clustering

- Review: 20261014T012653Z-haces
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T01:21:01Z
- Finished UTC: 2026-10-14T01:26:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HAC-ES as a DRAFT algorithm with related AIO clustering tasks. Author self-review supports its density-plus-external-neighbor guide and preserves its non-probability score, undefined empty-union case and empirical limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:HACES
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f817323fed6cabf4a06a6754a0d86133d03aed9e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HACES | data/curated/HACES.yaml | maintained | HAC-ES network clustering |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HACES | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 183.28s (0:03:03)<br>Checked 442 record(s); 0 failed.<br>Checked 672 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 359 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 356,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HACES | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HACES | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HACES | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:HACES | {"pair_ab_edge_density": "1/2", "pair_ab_shared_vertex_jaccard": "1", "pair_ab_combined_score": "3/2", "pair_de_edge_density": "1", "pair_de_shared_vertex_jaccard": "0", "pair_de_combined_score": "1", "external_vertex_c_contribution": "1 despite two incident edges from group A", "single_edge_density": "1", "single_edge_shared_score": null, "scope": "Candidate-pair score reversal and undefined empty-union boundary only. The pairs are not claimed to be selected in a full run; no author convention for 0/0 is invented."} |

## Scientific And Domain Assessments

### HAC-ES network clustering

identity: supported. Targets: AIMech:HACES.

Retain this distinct DRAFT algorithm.

Retain the source-named HAC-ES variant: edge density plus Jaccard overlap of external neighboring vertices. ROCK uses cross-cluster shared-neighbor link counts and a different size normalization. HAC-ML uses profiled network likelihood, and neither HAC-E nor HAC-Q has this combined score.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:HACES.

The explicit AIO mapping assessment is supported within its stated scope.

Related HierarchicalClustering and UnsupervisedClustering mappings preserve the algorithm/task distinction. Neither a degree-based modularity score nor a shared-neighbor density creates a modular language model, probabilistic dependency diagram or causal model. Sixteen annotated contexts were assessed; the four listed generated YAMLs were reread after capture.

### combined-merge-guide

evidence: supported. Targets: AIMech:HACES.

Supported within the stated primary-source and mathematical scope.

Equations 9–10 and the accompanying text define edge density plus Boolean intersection-over-union of external neighboring vertices. The summation is over vertices outside the candidate groups, not current aggregate cluster labels or the number of connecting paths.

### ranking-and-probability-boundary

evidence: supported. Targets: AIMech:HACES.

Supported within the stated primary-source and mathematical scope.

The explicit graph realizes density1/2 plus shared-neighbor score1 for one pair, versus density1 plus overlap0 for another. It reverses their density-only ordering and yields a score above1. It does not assert that either pair is the global next merge.

### empty-neighborhood-boundary

evidence: supported. Targets: AIMech:HACES.

Supported within the stated primary-source and mathematical scope.

On an isolated two-vertex edge, the outside-neighbor union is empty and the literal Equation10 ratio is0/0. The calculator returns an explicit undefined marker, not an invented author implementation convention. Restricted candidate selection could avoid the case; no runtime bug is claimed.

### hierarchical-link-estimation

evidence: supported. Targets: AIMech:HACES.

Supported within the stated primary-source and mathematical scope.

The page5 protocol estimates link densities at tree joins for hierarchical methods. The shared-neighbor heuristic ranks merges but is not itself the later probability estimator or a proof of community identity.

### evaluation-scope

evidence: supported. Targets: AIMech:HACES.

Supported within the stated primary-source and mathematical scope.

Pages 4–6 define degree-filtered biological interaction graphs, equal held-out-edge and hole counts, ranked predictions and maximum F scores. Table 2 and Figure 1 compare the named variants with different outcomes across networks and settings. The record makes no universal ranking, calibrated-probability or direct biological-truth claim.

### external vertices versus neighbor-path multiplicity, density-only versus combined rankings and undefined empty-neighborhood ratio

consistency: supported. Targets: AIMech:HACES.

Constructed calculations support the stated distinctions.

Exact external-vertex Jaccard score reversal, Boolean neighbor counting and an isolated-edge empty-union boundary. No author convention or full merge sequence is asserted.

### All maintained fields

provenance: supported. Targets: AIMech:HACES.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All five claims and remaining fields were assessed. The denominator uses the union of outside neighboring vertices, each counted once. The constructed 3/2 versus1 ranking reversal and single-edge undefined overlap are bounded local checks. No repository defect was identified; DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T012034Z-haces.json | supports | Compared all 442 pinned AIO and 669 native IDs, names, aliases and scoped synonyms for the three candidates and publication identifiers; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 158, 0 and 5 lines. All 158 public matches were inspected and belong to source/discovery/review context and rendered existing records, not these maintained identities. The five original-checkout matches are unrelated Spanish hace text in ignored dependencies. Semantic assessment covered 46 AIO and 264 native definitions: 44 AIO and 260 native rows were unchanged from prior reading; two additional AIO and four additional native definitions were read. Sixteen complete annotated AIO node/edge/generated contexts and the candidate-specific native records were assessed. Retain the source-named HAC-ES variant: edge density plus Jaccard overlap of external neighboring vertices. ROCK uses cross-cluster shared-neighbor link counts and a different size normalization. HAC-ML uses profiled network likelihood, and neither HAC-E nor HAC-Q has this combined score. |
| mapping | sources/aio/aio.json | supports | Related HierarchicalClustering and UnsupervisedClustering mappings preserve the algorithm/task distinction. Neither a degree-based modularity score nor a shared-neighbor density creates a modular language model, probabilistic dependency diagram or causal model. Sixteen annotated contexts were assessed; the four listed generated YAMLs were reread after capture. |
| park2011 | https://link.springer.com/content/pdf/10.1186/1471-2105-12-S1-S44.pdf; Different merging scores, PDF p. 4, Equations 9–10 and named score substitutions; Different merging scores, PDF p. 4, Equations 9–10 and explanation of the summation; Different merging scores, PDF p. 4, Equations 9–10; curator-derived candidate comparison in research/discovery/haces-boundaries.py; Different merging scores, PDF p. 4, Equation 10; curator-derived empty-union boundary in research/discovery/haces-boundaries.py; Link prediction and Empirical evaluation, PDF p. 5; Table 2 and Figure 1, p. 6; Performance Evaluation and Link prediction, PDF pp. 4–5; Table 2 and Figure 1, p. 6 | supports | BMC Bioinformatics 12(Suppl 1):S44, 2011-02-15. All ten publisher-PDF pages, 36 references, Equations 1–11, pseudocode, four figures and three tables were read. Variant formulas on page 4 and evaluation on page 6 were visually reassessed in this batch. Supplementary author code remains uninspected. |
| calculation | research/discovery/haces-boundaries.py | supports | Exact external-vertex Jaccard score reversal, Boolean neighbor counting and an isolated-edge empty-union boundary. No author convention or full merge sequence is asserted. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- The initial sandboxed vendored-check could not resolve the public artifact host. The network-enabled rerun passed all22 pinned artifacts; no vendored bytes were changed.
- This cohort step adds one DRAFT record, reaching 671 native and 442 unchanged AIO records. The main frontier now has 856 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- All ten pages of the 2011 primary paper, all references, four figures, three tables and Equations 1–11 were already fully read during the HAC-ML batch. For this variant assessment, page 4 equations and page 6 table/figure were visually reread and the candidate-specific finite calculations were authored, read and executed.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T012653Z-haces
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of HAC-ES network clustering
started_at: '2026-10-14T01:21:01Z'
finished_at: '2026-10-14T01:26:53Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged external vertices versus neighbor-path
    multiplicity, density-only versus combined rankings and undefined empty-neighborhood
    ratio. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain HAC-ES as a DRAFT algorithm with related AIO clustering tasks. Author
  self-review supports its density-plus-external-neighbor guide and preserves its
  non-probability score, undefined empty-union case and empirical limits.
source:
  git_revision: f817323fed6cabf4a06a6754a0d86133d03aed9e
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
  - path: data/aio/ModularLLM.yaml
    sha256: 73d7e14187388642a79ea7756f9c4fdd9958e0882e8292b3addf4ab6167a3613
    role: context
  - path: data/aio/ModularLanguageModel.yaml
    sha256: d5de5d9786239ade0804aaa751ff93ef75b782bf61208789772bf4ad83e6595c
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/GraphDegreeLinkage.yaml
    sha256: 0bd60481926261ff2fb8d69f0404a5d0132f3de4f0c915758bfaffa77fd62f8f
    role: context
  - path: data/curated/HACES.yaml
    sha256: 9744802e7708270aecb44a9cb0b9c39600d5629f25a3b008490353bf1d9f7d83
    role: target
  - path: data/curated/HACML.yaml
    sha256: 06a6b1b83616ce816b112084bfcfb2f29cd061a2fa0d07c3b66c6e2cfcbaae4a
    role: context
  - path: data/curated/ROCKClustering.yaml
    sha256: 5be4a00f39b229a245cd86e01d80e2b39cf2f09bb26487d7b911ca9d95625bec
    role: context
  - path: research/discovery/20261014T012034Z-haces.json
    sha256: 516d2a3c28d26551582d0ab356c4c0f64b36111739c6f26969b111a548dac136
    role: context
  - path: research/discovery/haces-boundaries.py
    sha256: fe08d8ff503e8d98fcf243484ecc155de6f2f4b6f8aabe77381be06091b0e496
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
- target_id: AIMech:HACES
  path: data/curated/HACES.yaml
  label: HAC-ES network clustering
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HACES.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:HACES'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HACES
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: The full primary paper was read; author implementations, data and supplements
      were not inspected or executed. Variant-specific candidate restrictions, tie
      policies, top stopping and terminal-collapse behavior remain unverified. Newer
      HSBM abstract and thesis search excerpts are follow-up context, not evidence
      for this record.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HACES
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 183.28s (0:03:03)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 672 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 359 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 356,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HACES
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
  - AIMech:HACES
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
  - AIMech:HACES
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/haces-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HACES
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pair_ab_edge_density": "1/2", "pair_ab_shared_vertex_jaccard": "1",
    "pair_ab_combined_score": "3/2", "pair_de_edge_density": "1", "pair_de_shared_vertex_jaccard":
    "0", "pair_de_combined_score": "1", "external_vertex_c_contribution": "1 despite
    two incident edges from group A", "single_edge_density": "1", "single_edge_shared_score":
    null, "scope": "Candidate-pair score reversal and undefined empty-union boundary
    only. The pairs are not claimed to be selected in a full run; no author convention
    for 0/0 is invented."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T012034Z-haces.json
  accessed_at: '2026-10-14T01:21:01Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 669 native IDs, names, aliases and scoped
    synonyms for the three candidates and publication identifiers; no normalized identity
    match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older
    discovery and original Documents checkouts returned 158, 0 and 5 lines. All 158
    public matches were inspected and belong to source/discovery/review context and
    rendered existing records, not these maintained identities. The five original-checkout
    matches are unrelated Spanish hace text in ignored dependencies. Semantic assessment
    covered 46 AIO and 264 native definitions: 44 AIO and 260 native rows were unchanged
    from prior reading; two additional AIO and four additional native definitions
    were read. Sixteen complete annotated AIO node/edge/generated contexts and the
    candidate-specific native records were assessed. Retain the source-named HAC-ES
    variant: edge density plus Jaccard overlap of external neighboring vertices. ROCK
    uses cross-cluster shared-neighbor link counts and a different size normalization.
    HAC-ML uses profiled network likelihood, and neither HAC-E nor HAC-Q has this
    combined score.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T01:21:01Z'
  support: supports
  summary: Related HierarchicalClustering and UnsupervisedClustering mappings preserve
    the algorithm/task distinction. Neither a degree-based modularity score nor a
    shared-neighbor density creates a modular language model, probabilistic dependency
    diagram or causal model. Sixteen annotated contexts were assessed; the four listed
    generated YAMLs were reread after capture.
- evidence_id: park2011
  kind: primary_source
  reference: https://link.springer.com/content/pdf/10.1186/1471-2105-12-S1-S44.pdf
  locator: Different merging scores, PDF p. 4, Equations 9–10 and named score substitutions;
    Different merging scores, PDF p. 4, Equations 9–10 and explanation of the summation;
    Different merging scores, PDF p. 4, Equations 9–10; curator-derived candidate
    comparison in research/discovery/haces-boundaries.py; Different merging scores,
    PDF p. 4, Equation 10; curator-derived empty-union boundary in research/discovery/haces-boundaries.py;
    Link prediction and Empirical evaluation, PDF p. 5; Table 2 and Figure 1, p. 6;
    Performance Evaluation and Link prediction, PDF pp. 4–5; Table 2 and Figure 1,
    p. 6
  accessed_at: '2026-10-14T00:38:22Z'
  snapshot_sha256: e930abd762f0f7c51d7671b3f605bc1fd2a35cdc230b668515c7778ffcb73b60
  support: supports
  summary: BMC Bioinformatics 12(Suppl 1):S44, 2011-02-15. All ten publisher-PDF pages,
    36 references, Equations 1–11, pseudocode, four figures and three tables were
    read. Variant formulas on page 4 and evaluation on page 6 were visually reassessed
    in this batch. Supplementary author code remains uninspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/haces-boundaries.py
  accessed_at: '2026-10-14T01:22:42Z'
  snapshot_sha256: fe08d8ff503e8d98fcf243484ecc155de6f2f4b6f8aabe77381be06091b0e496
  support: supports
  summary: Exact external-vertex Jaccard score reversal, Boolean neighbor counting
    and an isolated-edge empty-union boundary. No author convention or full merge
    sequence is asserted.
assessments:
- assessment_id: identity
  area: identity
  topic: HAC-ES network clustering
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - identity
  - park2011
  summary: Retain this distinct DRAFT algorithm.
  details: 'Retain the source-named HAC-ES variant: edge density plus Jaccard overlap
    of external neighboring vertices. ROCK uses cross-cluster shared-neighbor link
    counts and a different size normalization. HAC-ML uses profiled network likelihood,
    and neither HAC-E nor HAC-Q has this combined score.'
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - mapping
  - park2011
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related HierarchicalClustering and UnsupervisedClustering mappings preserve
    the algorithm/task distinction. Neither a degree-based modularity score nor a
    shared-neighbor density creates a modular language model, probabilistic dependency
    diagram or causal model. Sixteen annotated contexts were assessed; the four listed
    generated YAMLs were reread after capture.
- assessment_id: combined-merge-guide
  area: evidence
  topic: combined-merge-guide
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations 9–10 and the accompanying text define edge density plus Boolean
    intersection-over-union of external neighboring vertices. The summation is over
    vertices outside the candidate groups, not current aggregate cluster labels or
    the number of connecting paths.
- assessment_id: ranking-and-probability-boundary
  area: evidence
  topic: ranking-and-probability-boundary
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The explicit graph realizes density1/2 plus shared-neighbor score1 for
    one pair, versus density1 plus overlap0 for another. It reverses their density-only
    ordering and yields a score above1. It does not assert that either pair is the
    global next merge.
- assessment_id: empty-neighborhood-boundary
  area: evidence
  topic: empty-neighborhood-boundary
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: On an isolated two-vertex edge, the outside-neighbor union is empty and
    the literal Equation10 ratio is0/0. The calculator returns an explicit undefined
    marker, not an invented author implementation convention. Restricted candidate
    selection could avoid the case; no runtime bug is claimed.
- assessment_id: hierarchical-link-estimation
  area: evidence
  topic: hierarchical-link-estimation
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  summary: Supported within the stated primary-source and mathematical scope.
  details: The page5 protocol estimates link densities at tree joins for hierarchical
    methods. The shared-neighbor heuristic ranks merges but is not itself the later
    probability estimator or a proof of community identity.
- assessment_id: evaluation-scope
  area: evidence
  topic: evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pages 4–6 define degree-filtered biological interaction graphs, equal held-out-edge
    and hole counts, ranked predictions and maximum F scores. Table 2 and Figure 1
    compare the named variants with different outcomes across networks and settings.
    The record makes no universal ranking, calibrated-probability or direct biological-truth
    claim.
- assessment_id: constructed-boundaries
  area: consistency
  topic: external vertices versus neighbor-path multiplicity, density-only versus
    combined rankings and undefined empty-neighborhood ratio
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - park2011
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact external-vertex Jaccard score reversal, Boolean neighbor counting
    and an isolated-edge empty-union boundary. No author convention or full merge
    sequence is asserted.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:HACES
  evidence_ids:
  - identity
  - mapping
  - park2011
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All five claims and remaining fields were assessed.
    The denominator uses the union of outside neighboring vertices, each counted once.
    The constructed 3/2 versus1 ranking reversal and single-edge undefined overlap
    are bounded local checks. No repository defect was identified; DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- The initial sandboxed vendored-check could not resolve the public artifact host.
  The network-enabled rerun passed all22 pinned artifacts; no vendored bytes were
  changed.
- This cohort step adds one DRAFT record, reaching 671 native and 442 unchanged AIO
  records. The main frontier now has 856 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- All ten pages of the 2011 primary paper, all references, four figures, three tables
  and Equations 1–11 were already fully read during the HAC-ML batch. For this variant
  assessment, page 4 equations and page 6 table/figure were visually reread and the
  candidate-specific finite calculations were authored, read and executed.
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
