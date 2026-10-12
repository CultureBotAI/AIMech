# Scientific author self-review of two-stage adaptive-neighborhood sparse-spectrum regression

- Review: 20261012T224523Z-adaptive-neighborhood
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T22:41:33Z
- Finished UTC: 2026-10-12T22:45:23Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the distinct two-stage query-local variational regression algorithm with squared-mean weighting and full-training-set reselection. No actionable record defect was found; the record remains DRAFT.

## Scope And Provenance

All maintained fields and primary evidence of the exact two-stage neighborhood record.

Selection: Exact maintained ID: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 04c54876c7f14095346413d9461d3081e8968f50.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | data/curated/TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.yaml | maintained | Two-stage adaptive-neighborhood sparse-spectrum regression |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 117.72s (0:01:57)<br>Checked 442 record(s); 0 failed.<br>Checked 550 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 197 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 195,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | Exited 0 without output. |
| Exact neighborhood boundary arithmetic | passed | True | AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression | {"supplied_mean": ["1/10", "1"], "supplied_variance": ["100", "1/100"], "euclidean_squared_distances": {"A": "4", "B": "1"}, "squared_mean_distances": {"A": "1/25", "B": "1"}, "second_moment_distances": {"A": "10001/25", "B": "101/100"}, "one_neighbor_selections": {"first_stage_euclidean": "B", "prescribed_second_stage": "A", "second_moment_alternative": "B"}, "zero_weights_collapse_distinct_points": true, "sign_change_preserves_this_distance": true, "scope": "Exact arithmetic for the neighborhood rule at supplied parameters; no variational fit, model training or predictive benchmark."} |

## Scientific And Domain Assessments

### Query-local neighborhood algorithm

identity: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Retain a distinct algorithm record.

The descriptive name denotes the two-stage variational instantiation in Section 6. It differs from the generic finite-feature model, global variational fitting, prediction moment transforms, neighbor-response averaging and supervised representation-learning objectives. The original point-estimate SSGP comparator is explicitly contextual. There is no unsupported acronym alias or claim of an accepted upstream term.

### Task relationship and rejected neighbors

grounding: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

The related regression mapping is justified without an is-a assertion.

The regression task is directly applicable. K-nearest-neighbor classification voting and response averaging do not identify the local spectral fits. The pinned MetricLearning class is a deep neural network. LassoRegression, KernelLayer, ProbabilisticGraphicalModel and VariationalAutoEncoder do not establish equivalence or an appropriate hierarchical parent. AIO pin and mapping direction remain explicit.

### local-fitting-context

evidence: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Supported within the stated source and fitting assumptions.

For scalar responses y_i at inputs x_i in R^d, Tan et al. use m fixed standard-normal spectral draws s_r and paired features cos((s_r elementwise x_i)^T*lambda) and sin((s_r elementwise x_i)^T*lambda). The 2m coefficients have a conditional Gaussian prior and observations have Gaussian noise. A shared vector lambda controls all features; its Gaussian variational factor has mean mu_lambda and may have full covariance. The local models in Section 6 use the paper’s adaptive nonconjugate variational message-passing Algorithm 2. This is a specified approximate fitting routine, without a convergence or exact-posterior guarantee.

### two-stage-selection

evidence: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Supported within the stated source and fitting assumptions.

Given N finite training pairs D={(x_i,y_i)}, a fixed query x_star and an integer neighborhood size k with 1&lt;=k&lt;=N, select the k closest training inputs by Euclidean distance, forming index set N1. Fit local model M1 to the pairs indexed by N1. Let mu_lambda be the posterior-mean vector from M1 and define d_mu(x_star,x_i)=sqrt(sum_l mu_lambda_l^2*(x_star_l-x_i_l)^2). Select k nearest inputs from the entire original training set D using this weighted distance, forming N2; N2 is not restricted to N1. Fit a fresh local model M2 to the pairs indexed by N2 and use its variational posterior for prediction at x_star. These steps assume the local fits produce valid finite variational parameters; neighbor ties require a specified implementation convention.

### distance-interpretation

evidence: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Supported within the stated source and fitting assumptions.

The weights in Equation 16 are squares of the first fit’s posterior means, (E_q[lambda_l])^2, rather than posterior second moments E_q[lambda_l^2]. The latter would add Var_q(lambda_l) and generally select different neighbors. Although the source calls lambda a lengthscale, Equation 1 uses exp(-0.5*sum_l lambda_l^2*h_l^2), so its magnitude is an inverse-lengthscale parameter. Larger magnitude makes a fixed input displacement farther in the adapted distance; a zero posterior mean removes that coordinate from this distance even if its posterior variance is large. This is a plug-in neighborhood rule, not Bayesian averaging of neighborhood memberships.

### query-specific-prediction

evidence: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Supported within the stated source and fitting assumptions.

Repeat the two local fits separately for each requested prediction location. The second fitted variational distribution, not the first fit or an average of neighboring responses, supplies the predictive inference. The source uses approximate integration of the Gaussian observation model under variational factors for coefficients, lambda and noise scale. Query-local fitting allows different neighborhoods and smoothing/noise estimates at different locations; the construction does not itself provide a single joint posterior covariance across all query locations.

### two-stage-boundary

evidence: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

Supported within the stated source and fitting assumptions.

The published neighborhood procedure stops after two fits. The authors advise against repeatedly adapting the neighborhood because expansion and contraction can cycle; there is no asserted fixed-point guarantee. Their experiments also apply the same neighborhood construction to point-estimate SSGP fits by replacing mu_lambda with fitted lambda estimates. That comparator does not possess the variational posterior over lambda and is distinguished from this record’s variational instantiation.

### Mean-square distance and full-data reselection

consistency: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

The critical neighborhood boundaries are preserved.

Equation 16 squares posterior means; it does not integrate squared inverse-lengthscales. At the supplied illustrative parameters, Euclidean selection chooses B, squared-mean selection chooses A, and second-moment selection chooses B. N2 can leave N1 because the source searches all training data. The calculation does not assert that these parameters arise from a one-observation fit. Zero-weight pseudometric degeneracy, sign invariance of this distance only, ties and valid-fit assumptions are explicit. Lambda is correctly interpreted as a signed inverse-lengthscale in the displayed kernel.

### Predictive and optimization limits

scope: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

No joint-posterior, calibration, convergence or total-cost guarantee is asserted.

Each query has two separate local fits. Integrating the second variational model gives a generally non-Gaussian predictive mixture; separate local fits do not define one joint posterior covariance across queries. Mean-only neighborhood adaptation omits lengthscale covariance even though that covariance participates in the local variational model. Algorithm 2 details and executable implementation remain pending; source index and feature-orientation inconsistencies are not silently adopted. No quantitative performance superiority is claimed.

### Complete maintained record and report mirror

provenance: supported. Targets: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.

All fields are assessed and the record remains DRAFT.

Read the stable ID, descriptive name, empty aliases, algorithm kind, definition, identity notes, five claims and locators, source version/hash/access timestamp, pin, related mapping, six limitations and actual curation timestamps. The report entry equals the YAML. The journal landing page confirms bibliographic context but is not full journal-text inspection. The failed author-page access and bounded code-search scope remain explicit. No author implementation, model fit, training or empirical benchmark was run.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T224120Z-adaptive-neighborhood.json | supports | Compared all 442 pinned AIO IDs, names and scoped synonyms and 549 maintained IDs, names and aliases; no normalized match for this identity. Full-text fixed-string searches of the recovery, older discovery and original Documents checkouts included hidden and ignored files, with 6, 0 and 0 matched lines. All five distinct matched contents were read: source leads and source-reading context, not existing records. Assessed 40 semantic AIO rows, 155 maintained names/definitions, eight full annotated AIO CLASS nodes with incident edges and generated YAML, and six complete native context records. This query-specific neighborhood-selection and refitting algorithm differs from the generic GP and SSGP model families, Gal–Turner global spectral inference, neighbor-response averaging, and the NCA, LMNN and RCA representation-learning procedures. Its descriptive local name denotes the variational two-stage method in Tan et al. Section 6; the point-estimate SSGP adaptation is contextual. Absence is bounded to the searched pin and corpus. |
| mapping | sources/aio/aio.json | supports | Assessed 40 semantic AIO rows and 155 native names/definitions, eight full annotated AIO nodes with incident edges and generated records, and six complete native records. The algorithm/task related mapping and seven rejected mappings preserve abstraction boundaries. |
| tan2015 | https://arxiv.org/pdf/1306.1999v3; Sections 2–6, Equations 1, 4–5, 15–16, Algorithm 2 and two numbered neighborhood stages, PDF pp. 3–8; especially p. 8. | supports | arXiv:1306.1999v3, revised 26 January 2015. All 21 rendered PDF pages visually read: 20 numbered content pages plus a final graphic-only page, including eleven figures, Table 1, references and Appendices A–C. The related journal article appeared online 12 September 2015 and in Statistics and Computing 26:1243–1261 (2016), DOI 10.1007/s11222-015-9600-7. Mechanism locators refer to this inspected preprint, not an uninspected journal PDF. All 21 pages were read during preparation. After freezing the current record, PDF pp. 3, 4, 7 and 8 were visually reread against its complete YAML. |
| calculation | research/discovery/adaptive-neighborhood-boundaries.py | supports | Exact Fraction arithmetic at supplied illustrative parameters verifies that squared means and second moments can choose different neighbors, and that full-data reselection can move outside N1. Zero-weight degeneracy and distance sign invariance are checked. This is not a fitted posterior, training run or predictive benchmark. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue is manufactured for a clean record.
- Added one DRAFT native algorithm: 550 maintained records and 442 unchanged generated records. The 735-entry main frontier retains 485 pending and 56 partly addressed cohorts; discovery has not reached saturation.
- All preprint pages were read; the publisher page supplied bibliographic confirmation and a subscription preview, not the complete journal text. The author page returned HTTP 502. No author implementation was located in the bounded code-search queries, which is not an exhaustive absence claim. No author code, model fitting, training, paid access or benchmark was run. Exact finite curator arithmetic checks only the distance boundary at supplied illustrative parameters. The record remains DRAFT.
- Source-search title leads remain preserved separately with their actual access levels. They are not asserted concepts or a claim of complete frontier deduplication.
- Original-checkout synchronization and old round141 cleanup await explicit approval after automatic review rejection; this work uses only the isolated public recovery checkout.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T224523Z-adaptive-neighborhood
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of two-stage adaptive-neighborhood sparse-spectrum
  regression
started_at: '2026-10-12T22:41:33Z'
finished_at: '2026-10-12T22:45:23Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent challenged identity, distance semantics,
    neighborhood search population, predictive scope and optimization assumptions.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the distinct two-stage query-local variational regression algorithm
  with squared-mean weighting and full-training-set reselection. No actionable record
  defect was found; the record remains DRAFT.
source:
  git_revision: 04c54876c7f14095346413d9461d3081e8968f50
  state: working_tree
  inputs:
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/KnearestNeighborAlgorithm.yaml
    sha256: cdb4ab16dea60d54981c94dd2474ac427ffd0e35b728b6356e12cecf87b7a5c0
    role: context
  - path: data/aio/KnearestNeighborRegressionAlgorithm.yaml
    sha256: d601b4b9fe609add6e8f9fad5cd43c623bbae548ec8eb36b1b75515fa58d56d2
    role: context
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/LargeMarginNearestNeighbor.yaml
    sha256: f17ce62722a0b1aaf9629bbb196e67249c1853edd31d220bfff76019d3e3295e
    role: context
  - path: data/curated/NeighborhoodComponentsAnalysis.yaml
    sha256: 9aa5fa5229196181f23e7ba5910dba00623a60e558b97233e6cefc1f0fbbd577
    role: context
  - path: data/curated/RelevantComponentAnalysis.yaml
    sha256: b90fe3dd50da413f6f66c6ea26ecd2eb937b2aec43b4c1eb1f4635dc4609094f
    role: context
  - path: data/curated/SparseSpectrumGaussianProcessRegression.yaml
    sha256: d1680103fd8df79740d12629429a4009709f0b2e136140fc95c565852f63db44
    role: context
  - path: data/curated/TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.yaml
    sha256: a8ed8c144a7b82979d72594f54450e229b605de5a8712938ef03680019878da7
    role: target
  - path: data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml
    sha256: e508cdaea10654cf24a1b219887c88e4d3236cd440a2db4c2f9a8eee7742bba2
    role: context
  - path: research/discovery/20261012T224120Z-adaptive-neighborhood.json
    sha256: 2bb3ef063eac7b07960a4d31041a99ca629418d7ef1be88a0380b85712c25bbf
    role: context
  - path: research/discovery/adaptive-neighborhood-boundaries.py
    sha256: a9d4ee02e5ad9c94ed83292ab4607237d52ca8d9e93f276fca17f71a4a9c61be
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
- target_id: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  path: data/curated/TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.yaml
  label: Two-stage adaptive-neighborhood sparse-spectrum regression
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TwoStageAdaptiveNeighborhoodSparseSpectrumRegression.yaml
    role: maintained
scope:
  description: All maintained fields and primary evidence of the exact two-stage neighborhood
    record.
  selection: 'Exact maintained ID: AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  exclusions:
  - target: Detailed base and adaptive NCVMP fitting algorithms
    reason: Separate identities and unresolved implementation/notation questions retained
      for follow-up.
  - target: Author implementation, full journal version and empirical reproduction
    reason: Inspected complete preprint and bibliographic landing page; finite curator
      arithmetic only.
  - target: Existing native and AIO context records
    reason: Identity and mapping context rather than complete scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 117.72s (0:01:57)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 550 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 197 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 195,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
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
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
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
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Exact neighborhood boundary arithmetic
  command: python3 research/discovery/adaptive-neighborhood-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  exit_code: 0
  expected_exit_code: 0
  summary: '{"supplied_mean": ["1/10", "1"], "supplied_variance": ["100", "1/100"],
    "euclidean_squared_distances": {"A": "4", "B": "1"}, "squared_mean_distances":
    {"A": "1/25", "B": "1"}, "second_moment_distances": {"A": "10001/25", "B": "101/100"},
    "one_neighbor_selections": {"first_stage_euclidean": "B", "prescribed_second_stage":
    "A", "second_moment_alternative": "B"}, "zero_weights_collapse_distinct_points":
    true, "sign_change_preserves_this_distance": true, "scope": "Exact arithmetic
    for the neighborhood rule at supplied parameters; no variational fit, model training
    or predictive benchmark."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T224120Z-adaptive-neighborhood.json
  accessed_at: '2026-10-12T22:41:33Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, names and scoped synonyms and 549 maintained
    IDs, names and aliases; no normalized match for this identity. Full-text fixed-string
    searches of the recovery, older discovery and original Documents checkouts included
    hidden and ignored files, with 6, 0 and 0 matched lines. All five distinct matched
    contents were read: source leads and source-reading context, not existing records.
    Assessed 40 semantic AIO rows, 155 maintained names/definitions, eight full annotated
    AIO CLASS nodes with incident edges and generated YAML, and six complete native
    context records. This query-specific neighborhood-selection and refitting algorithm
    differs from the generic GP and SSGP model families, Gal–Turner global spectral
    inference, neighbor-response averaging, and the NCA, LMNN and RCA representation-learning
    procedures. Its descriptive local name denotes the variational two-stage method
    in Tan et al. Section 6; the point-estimate SSGP adaptation is contextual. Absence
    is bounded to the searched pin and corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T22:41:33Z'
  support: supports
  summary: Assessed 40 semantic AIO rows and 155 native names/definitions, eight full
    annotated AIO nodes with incident edges and generated records, and six complete
    native records. The algorithm/task related mapping and seven rejected mappings
    preserve abstraction boundaries.
- evidence_id: tan2015
  kind: primary_source
  reference: https://arxiv.org/pdf/1306.1999v3
  locator: Sections 2–6, Equations 1, 4–5, 15–16, Algorithm 2 and two numbered neighborhood
    stages, PDF pp. 3–8; especially p. 8.
  accessed_at: '2026-10-12T22:01:48Z'
  snapshot_sha256: 72feb4c72b26680c07c76b3f7632ef926b55384131cfa12456d29542ba03aad4
  support: supports
  summary: 'arXiv:1306.1999v3, revised 26 January 2015. All 21 rendered PDF pages
    visually read: 20 numbered content pages plus a final graphic-only page, including
    eleven figures, Table 1, references and Appendices A–C. The related journal article
    appeared online 12 September 2015 and in Statistics and Computing 26:1243–1261
    (2016), DOI 10.1007/s11222-015-9600-7. Mechanism locators refer to this inspected
    preprint, not an uninspected journal PDF. All 21 pages were read during preparation.
    After freezing the current record, PDF pp. 3, 4, 7 and 8 were visually reread
    against its complete YAML.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/adaptive-neighborhood-boundaries.py
  accessed_at: '2026-10-12T22:41:33Z'
  snapshot_sha256: a9d4ee02e5ad9c94ed83292ab4607237d52ca8d9e93f276fca17f71a4a9c61be
  support: supports
  summary: Exact Fraction arithmetic at supplied illustrative parameters verifies
    that squared means and second moments can choose different neighbors, and that
    full-data reselection can move outside N1. Zero-weight degeneracy and distance
    sign invariance are checked. This is not a fitted posterior, training run or predictive
    benchmark.
assessments:
- assessment_id: identity
  area: identity
  topic: Query-local neighborhood algorithm
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - identity
  - tan2015
  summary: Retain a distinct algorithm record.
  details: The descriptive name denotes the two-stage variational instantiation in
    Section 6. It differs from the generic finite-feature model, global variational
    fitting, prediction moment transforms, neighbor-response averaging and supervised
    representation-learning objectives. The original point-estimate SSGP comparator
    is explicitly contextual. There is no unsupported acronym alias or claim of an
    accepted upstream term.
- assessment_id: mapping
  area: grounding
  topic: Task relationship and rejected neighbors
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - mapping
  - tan2015
  summary: The related regression mapping is justified without an is-a assertion.
  details: The regression task is directly applicable. K-nearest-neighbor classification
    voting and response averaging do not identify the local spectral fits. The pinned
    MetricLearning class is a deep neural network. LassoRegression, KernelLayer, ProbabilisticGraphicalModel
    and VariationalAutoEncoder do not establish equivalence or an appropriate hierarchical
    parent. AIO pin and mapping direction remain explicit.
- assessment_id: local-fitting-context
  area: evidence
  topic: local-fitting-context
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  summary: Supported within the stated source and fitting assumptions.
  details: For scalar responses y_i at inputs x_i in R^d, Tan et al. use m fixed standard-normal
    spectral draws s_r and paired features cos((s_r elementwise x_i)^T*lambda) and
    sin((s_r elementwise x_i)^T*lambda). The 2m coefficients have a conditional Gaussian
    prior and observations have Gaussian noise. A shared vector lambda controls all
    features; its Gaussian variational factor has mean mu_lambda and may have full
    covariance. The local models in Section 6 use the paper’s adaptive nonconjugate
    variational message-passing Algorithm 2. This is a specified approximate fitting
    routine, without a convergence or exact-posterior guarantee.
- assessment_id: two-stage-selection
  area: evidence
  topic: two-stage-selection
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  - calculation
  summary: Supported within the stated source and fitting assumptions.
  details: Given N finite training pairs D={(x_i,y_i)}, a fixed query x_star and an
    integer neighborhood size k with 1<=k<=N, select the k closest training inputs
    by Euclidean distance, forming index set N1. Fit local model M1 to the pairs indexed
    by N1. Let mu_lambda be the posterior-mean vector from M1 and define d_mu(x_star,x_i)=sqrt(sum_l
    mu_lambda_l^2*(x_star_l-x_i_l)^2). Select k nearest inputs from the entire original
    training set D using this weighted distance, forming N2; N2 is not restricted
    to N1. Fit a fresh local model M2 to the pairs indexed by N2 and use its variational
    posterior for prediction at x_star. These steps assume the local fits produce
    valid finite variational parameters; neighbor ties require a specified implementation
    convention.
- assessment_id: distance-interpretation
  area: evidence
  topic: distance-interpretation
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  - calculation
  summary: Supported within the stated source and fitting assumptions.
  details: The weights in Equation 16 are squares of the first fit’s posterior means,
    (E_q[lambda_l])^2, rather than posterior second moments E_q[lambda_l^2]. The latter
    would add Var_q(lambda_l) and generally select different neighbors. Although the
    source calls lambda a lengthscale, Equation 1 uses exp(-0.5*sum_l lambda_l^2*h_l^2),
    so its magnitude is an inverse-lengthscale parameter. Larger magnitude makes a
    fixed input displacement farther in the adapted distance; a zero posterior mean
    removes that coordinate from this distance even if its posterior variance is large.
    This is a plug-in neighborhood rule, not Bayesian averaging of neighborhood memberships.
- assessment_id: query-specific-prediction
  area: evidence
  topic: query-specific-prediction
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  summary: Supported within the stated source and fitting assumptions.
  details: Repeat the two local fits separately for each requested prediction location.
    The second fitted variational distribution, not the first fit or an average of
    neighboring responses, supplies the predictive inference. The source uses approximate
    integration of the Gaussian observation model under variational factors for coefficients,
    lambda and noise scale. Query-local fitting allows different neighborhoods and
    smoothing/noise estimates at different locations; the construction does not itself
    provide a single joint posterior covariance across all query locations.
- assessment_id: two-stage-boundary
  area: evidence
  topic: two-stage-boundary
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  summary: Supported within the stated source and fitting assumptions.
  details: The published neighborhood procedure stops after two fits. The authors
    advise against repeatedly adapting the neighborhood because expansion and contraction
    can cycle; there is no asserted fixed-point guarantee. Their experiments also
    apply the same neighborhood construction to point-estimate SSGP fits by replacing
    mu_lambda with fitted lambda estimates. That comparator does not possess the variational
    posterior over lambda and is distinguished from this record’s variational instantiation.
- assessment_id: boundaries
  area: consistency
  topic: Mean-square distance and full-data reselection
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  - calculation
  summary: The critical neighborhood boundaries are preserved.
  details: Equation 16 squares posterior means; it does not integrate squared inverse-lengthscales.
    At the supplied illustrative parameters, Euclidean selection chooses B, squared-mean
    selection chooses A, and second-moment selection chooses B. N2 can leave N1 because
    the source searches all training data. The calculation does not assert that these
    parameters arise from a one-observation fit. Zero-weight pseudometric degeneracy,
    sign invariance of this distance only, ties and valid-fit assumptions are explicit.
    Lambda is correctly interpreted as a signed inverse-lengthscale in the displayed
    kernel.
- assessment_id: limits
  area: scope
  topic: Predictive and optimization limits
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - tan2015
  summary: No joint-posterior, calibration, convergence or total-cost guarantee is
    asserted.
  details: Each query has two separate local fits. Integrating the second variational
    model gives a generally non-Gaussian predictive mixture; separate local fits do
    not define one joint posterior covariance across queries. Mean-only neighborhood
    adaptation omits lengthscale covariance even though that covariance participates
    in the local variational model. Algorithm 2 details and executable implementation
    remain pending; source index and feature-orientation inconsistencies are not silently
    adopted. No quantitative performance superiority is claimed.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record and report mirror
  outcome: supported
  target_ids:
  - AIMech:TwoStageAdaptiveNeighborhoodSparseSpectrumRegression
  evidence_ids:
  - identity
  - mapping
  - tan2015
  - calculation
  summary: All fields are assessed and the record remains DRAFT.
  details: Read the stable ID, descriptive name, empty aliases, algorithm kind, definition,
    identity notes, five claims and locators, source version/hash/access timestamp,
    pin, related mapping, six limitations and actual curation timestamps. The report
    entry equals the YAML. The journal landing page confirms bibliographic context
    but is not full journal-text inspection. The failed author-page access and bounded
    code-search scope remain explicit. No author implementation, model fit, training
    or empirical benchmark was run.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue is
  manufactured for a clean record.
- 'Added one DRAFT native algorithm: 550 maintained records and 442 unchanged generated
  records. The 735-entry main frontier retains 485 pending and 56 partly addressed
  cohorts; discovery has not reached saturation.'
- All preprint pages were read; the publisher page supplied bibliographic confirmation
  and a subscription preview, not the complete journal text. The author page returned
  HTTP 502. No author implementation was located in the bounded code-search queries,
  which is not an exhaustive absence claim. No author code, model fitting, training,
  paid access or benchmark was run. Exact finite curator arithmetic checks only the
  distance boundary at supplied illustrative parameters. The record remains DRAFT.
- Source-search title leads remain preserved separately with their actual access levels.
  They are not asserted concepts or a claim of complete frontier deduplication.
- Original-checkout synchronization and old round141 cleanup await explicit approval
  after automatic review rejection; this work uses only the isolated public recovery
  checkout.
related_reviews: []
links: []
tags:
- native-concepts
- gaussian-processes
- neighborhood-selection
- self-review
- discovery-ongoing
```
