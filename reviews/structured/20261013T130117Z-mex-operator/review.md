# Scientific author self-review of MEX Operator

- Review: 20261013T130117Z-mex-operator
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T12:49:02Z
- Finished UTC: 2026-10-13T13:01:17Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain MEX Operator as a DRAFT mathematical-method concept, distinct from its layers and SimNet. All four claims and mappings are supported within explicit algebraic and source limits. No actionable defect found in adversarial author self-review; training and empirical replication excluded.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:MEXOperator
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d7487520d6fbc6e9c415d3aea32da0870966016d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MEXOperator | data/curated/MEXOperator.yaml | maintained | MEX Operator |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MEXOperator | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 136.59s (0:02:16)<br>Checked 442 record(s); 0 failed.<br>Checked 619 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 290 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 286,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MEXOperator | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:MEXOperator | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:MEXOperator | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:MEXOperator | {"equal_group_nested": 5.949350044000794, "finite_zero_augmented_value": -0.2190701963798386, "flattened": 5.949350044000794, "log_sum_exp_scaled": 4.015724071038566, "mixed_parameter_nested": 3.4822250666926555, "negative_limit_approx": -1.9998901387711332, "normalization_offset": 0.845086375898546, "normalized_input_gradient": [0.00040144448932702664, 0.019832340952673992, 0.9797662145579991], "numerical_gradient": [0.00040144452206902764, 0.019832340925063363, 0.9797662145372142], "positive_limit_approx": 3.9998901387711334, "unequal_group_nested": 5.6374663083356555, "value": 3.1706376951400195, "zero_limit": 1.0} |

## Scientific And Domain Assessments

### MEX Operator

identity: supported. Targets: AIMech:MEXOperator.

Retain this distinct DRAFT mathematical_method.

Retain the scalar operator separately from SimNet and a concrete MEX layer. MATLAB mex and identifier-prefix dependency matches are unrelated acronym meanings. The qualified MEX (SimNets) alias, mean normalization and real parameter distinguish the intended identity from probability-vector softmax or a particular loss.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:MEXOperator.

The declared AIO mapping is supported.

MathematicalFunction is broader. SoftmaxFunction is related through the input derivative and ReLUFunction through an additional-zero positive-infinite limit. Neither relation asserts equality of finite outputs. Complete ActivationLayer and spatial PoolingLayer targets do not subsume every use of the scalar operation. All five full annotated node/edge/generated contexts were inspected.

### normalized-scalar-and-limits

evidence: supported. Targets: AIMech:MEXOperator.

Supported within the stated primary-source and mathematical scope.

Equation1 includes1/N inside the logarithm. Algebra gives scaled log-sum-exp minus log(N)/xi and input derivative softmax(xi*c), for either nonzero sign of xi. Mean is the continuous zero extension; max/min require limits. A gradient probability vector is not the scalar output.

### nested-collapse-conditions

evidence: supported. Targets: AIMech:MEXOperator.

Supported within the stated primary-source and mathematical scope.

Equation2 uses the same xi and a rectangular collection with equal inner size m. Expanding exponentials preserves uniform weights only under that grouping; chosen unequal groups and different parameters provide counterexamples to stronger unconditional collapse. Permutation invariance and shift equivariance follow directly from Equation1.

### relu-and-layer-scope

evidence: supported. Targets: AIMech:MEXOperator.

Supported within the stated primary-source and mathematical scope.

Pages2–4 distinguish the operator from local-block MEX layers with shifts and optional constants. Max pooling is a limit, and ReLU uses a zero constant with zero offsets. The chosen finite aggregate of -.5 and0 is negative, unlike exact ReLU.

### combined-network-evidence-boundary

evidence: supported. Targets: AIMech:MEXOperator.

Supported within the stated primary-source and mathematical scope.

Section6 sets the evaluated first MEX parameter to1 and second to the mean limit. This is not the equal-parameter collapse case. Existing whole-network comparisons include similarity functions, preprocessing, initialization and optimizer changes, so no operator-only performance or hardware benefit is inferred.

### scalar versus probability-vector identity, mean normalization, nested collapse, limiting ReLU and full-network evidence scope

consistency: supported. Targets: AIMech:MEXOperator.

Constructed calculations support the stated distinctions.

Chosen stable log-mean-exp calculations verify the log-sum-exp normalization term, softmax input derivative, shift equivariance, equal-size nested collapse and failures with unequal groups or parameters. Finite values differ from exact ReLU and max/min limits. These are constructed mathematical checks, not experimental replication.

### All maintained fields

provenance: supported. Targets: AIMech:MEXOperator.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all four claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Entire maintained YAML and selected mapping YAMLs read after capture. Rechecked Equation1 normalization and parameter limits, Equation2 group-size/common-parameter scope, MEX layer/ReLU construction and the evaluated two-stage parameter choices. Constructed derivative and collapse counterexamples were inspected. Exact record/report mirror and source/context hashes agree.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T124839Z-mex-operator.json | supports | Compared all 442 pinned AIO and 618 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 125, 0, 80 lines. All distinct match contents were inspected. Semantic matching covered 43 AIO and 31 native definitions, with every matched definition read. 5 full annotated AIO node/edge/generated contexts and 2 full native records were inspected. MEX denotes the scalar log-mean-exp operator used by Cohen and Shashua, separate from the complete SimNet architecture and a spatial MEX layer with offsets and sharing. The search also found MATLAB mex syntax and unrelated identifier-prefix registries in ignored dependencies; those are different meanings. The alias is qualified as MEX (SimNets). A softmax probability vector and the unnormalized log-sum-exp within lifted structured loss are related computations, not this operator identity. |
| mapping | sources/aio/aio.json | supports | MathematicalFunction is broader. SoftmaxFunction is related through the input derivative and ReLUFunction through an additional-zero positive-infinite limit. Neither relation asserts equality of finite outputs. Complete ActivationLayer and spatial PoolingLayer targets do not subsume every use of the scalar operation. All five full annotated node/edge/generated contexts were inspected. |
| cohen2014 | https://arxiv.org/pdf/1410.0781v3; Reused exact complete19page primary PDF with original download timestamp/hash. Other versions, later Deep SimNets full paper, author implementation, model fitting and empirical replication excluded. | supports | arXiv:1410.0781v3, 7 December 2014, 19 PDF pages. All pages visually read, including Appendices A and B; original download timestamp and hash reused. PDF and printed page numbers agree. No publication acceptance inferred; author implementation and later versions not inspected. |
| calculation | research/discovery/mex-operator-boundaries.py | supports | Chosen stable log-mean-exp calculations verify the log-sum-exp normalization term, softmax input derivative, shift equivariance, equal-size nested collapse and failures with unequal groups or parameters. Finite values differ from exact ReLU and max/min limits. These are constructed mathematical checks, not experimental replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 619 native and 442 unchanged generated records. The 803-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 19 PDF pages visually read, including figures, formulas, tables, references and any appendices. No author code, training or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T130117Z-mex-operator
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of MEX Operator
started_at: '2026-10-13T12:49:02Z'
finished_at: '2026-10-13T13:01:17Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged scalar versus probability-vector identity,
    mean normalization, nested collapse, limiting ReLU and full-network evidence scope.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain MEX Operator as a DRAFT mathematical-method concept, distinct from
  its layers and SimNet. All four claims and mappings are supported within explicit
  algebraic and source limits. No actionable defect found in adversarial author self-review;
  training and empirical replication excluded.
source:
  git_revision: d7487520d6fbc6e9c415d3aea32da0870966016d
  state: working_tree
  inputs:
  - path: data/aio/ActivationLayer.yaml
    sha256: 3b7d6dfd59e913373ceec1986f4210636d894f9ad3396d0d65284f5167bf2a1c
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/PoolingLayer.yaml
    sha256: 2a5cc182b52109a337a926a42bd715d5f1142e2a0876a8bfbc41890846e84246
    role: context
  - path: data/aio/ReLUFunction.yaml
    sha256: 815a5255ec7e87bb8bb123ea7121d024d46450ccfab164985e2014108b53d28c
    role: context
  - path: data/aio/SoftmaxFunction.yaml
    sha256: 150cf1f70d0a49c2515fc4569b451c6b835050346797db01b0536751b867e69f
    role: context
  - path: data/curated/LiftedStructuredEmbeddingLoss.yaml
    sha256: fbfa4bf9e8910269a90d0f4e866c2f9b8cf7be7512302e1a0debb21154838764
    role: context
  - path: data/curated/MEXOperator.yaml
    sha256: 6615393af74d901896efd73e152a22e48294f791350ede59cfe6a8bfc4911c5b
    role: target
  - path: data/curated/SimNet.yaml
    sha256: 9fb428e28a283c959c45f9245470db476c589d43c7f7dda909976e85a8d78f78
    role: context
  - path: research/discovery/20261013T124839Z-mex-operator.json
    sha256: 7a7cdb0959289abb7307fea667af1fefe2d112ae76476fb64cbf084774a2a29b
    role: context
  - path: research/discovery/mex-operator-boundaries.py
    sha256: af85a8cbb9de1117c963380e04a7960816828063ea1cdc3614605abf9b0a5ef5
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
- target_id: AIMech:MEXOperator
  path: data/curated/MEXOperator.yaml
  label: MEX Operator
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MEXOperator.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:MEXOperator'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:MEXOperator
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Reused exact complete19page primary PDF with original download timestamp/hash.
      Other versions, later Deep SimNets full paper, author implementation, model
      fitting and empirical replication excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MEXOperator
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 136.59s (0:02:16)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 619 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 290 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 286,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:MEXOperator
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
  - AIMech:MEXOperator
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
  - AIMech:MEXOperator
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/mex-operator-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MEXOperator
  exit_code: 0
  expected_exit_code: 0
  summary: '{"equal_group_nested": 5.949350044000794, "finite_zero_augmented_value":
    -0.2190701963798386, "flattened": 5.949350044000794, "log_sum_exp_scaled": 4.015724071038566,
    "mixed_parameter_nested": 3.4822250666926555, "negative_limit_approx": -1.9998901387711332,
    "normalization_offset": 0.845086375898546, "normalized_input_gradient": [0.00040144448932702664,
    0.019832340952673992, 0.9797662145579991], "numerical_gradient": [0.00040144452206902764,
    0.019832340925063363, 0.9797662145372142], "positive_limit_approx": 3.9998901387711334,
    "unequal_group_nested": 5.6374663083356555, "value": 3.1706376951400195, "zero_limit":
    1.0}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T124839Z-mex-operator.json
  accessed_at: '2026-10-13T12:49:02Z'
  support: supports
  summary: Compared all 442 pinned AIO and 618 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    125, 0, 80 lines. All distinct match contents were inspected. Semantic matching
    covered 43 AIO and 31 native definitions, with every matched definition read.
    5 full annotated AIO node/edge/generated contexts and 2 full native records were
    inspected. MEX denotes the scalar log-mean-exp operator used by Cohen and Shashua,
    separate from the complete SimNet architecture and a spatial MEX layer with offsets
    and sharing. The search also found MATLAB mex syntax and unrelated identifier-prefix
    registries in ignored dependencies; those are different meanings. The alias is
    qualified as MEX (SimNets). A softmax probability vector and the unnormalized
    log-sum-exp within lifted structured loss are related computations, not this operator
    identity.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T12:49:02Z'
  support: supports
  summary: MathematicalFunction is broader. SoftmaxFunction is related through the
    input derivative and ReLUFunction through an additional-zero positive-infinite
    limit. Neither relation asserts equality of finite outputs. Complete ActivationLayer
    and spatial PoolingLayer targets do not subsume every use of the scalar operation.
    All five full annotated node/edge/generated contexts were inspected.
- evidence_id: cohen2014
  kind: primary_source
  reference: https://arxiv.org/pdf/1410.0781v3
  locator: Reused exact complete19page primary PDF with original download timestamp/hash.
    Other versions, later Deep SimNets full paper, author implementation, model fitting
    and empirical replication excluded.
  accessed_at: '2026-10-13T11:58:05Z'
  snapshot_sha256: 91119773f55d79557a02212c71a3c49d491223229b5354b24610eb0d3e89de26
  support: supports
  summary: arXiv:1410.0781v3, 7 December 2014, 19 PDF pages. All pages visually read,
    including Appendices A and B; original download timestamp and hash reused. PDF
    and printed page numbers agree. No publication acceptance inferred; author implementation
    and later versions not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/mex-operator-boundaries.py
  accessed_at: '2026-10-13T12:54:14Z'
  snapshot_sha256: af85a8cbb9de1117c963380e04a7960816828063ea1cdc3614605abf9b0a5ef5
  support: supports
  summary: Chosen stable log-mean-exp calculations verify the log-sum-exp normalization
    term, softmax input derivative, shift equivariance, equal-size nested collapse
    and failures with unequal groups or parameters. Finite values differ from exact
    ReLU and max/min limits. These are constructed mathematical checks, not experimental
    replication.
assessments:
- assessment_id: identity
  area: identity
  topic: MEX Operator
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - identity
  - cohen2014
  summary: Retain this distinct DRAFT mathematical_method.
  details: Retain the scalar operator separately from SimNet and a concrete MEX layer.
    MATLAB mex and identifier-prefix dependency matches are unrelated acronym meanings.
    The qualified MEX (SimNets) alias, mean normalization and real parameter distinguish
    the intended identity from probability-vector softmax or a particular loss.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - mapping
  - cohen2014
  summary: The declared AIO mapping is supported.
  details: MathematicalFunction is broader. SoftmaxFunction is related through the
    input derivative and ReLUFunction through an additional-zero positive-infinite
    limit. Neither relation asserts equality of finite outputs. Complete ActivationLayer
    and spatial PoolingLayer targets do not subsume every use of the scalar operation.
    All five full annotated node/edge/generated contexts were inspected.
- assessment_id: normalized-scalar-and-limits
  area: evidence
  topic: normalized-scalar-and-limits
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation1 includes1/N inside the logarithm. Algebra gives scaled log-sum-exp
    minus log(N)/xi and input derivative softmax(xi*c), for either nonzero sign of
    xi. Mean is the continuous zero extension; max/min require limits. A gradient
    probability vector is not the scalar output.
- assessment_id: nested-collapse-conditions
  area: evidence
  topic: nested-collapse-conditions
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation2 uses the same xi and a rectangular collection with equal inner
    size m. Expanding exponentials preserves uniform weights only under that grouping;
    chosen unequal groups and different parameters provide counterexamples to stronger
    unconditional collapse. Permutation invariance and shift equivariance follow directly
    from Equation1.
- assessment_id: relu-and-layer-scope
  area: evidence
  topic: relu-and-layer-scope
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pages2–4 distinguish the operator from local-block MEX layers with shifts
    and optional constants. Max pooling is a limit, and ReLU uses a zero constant
    with zero offsets. The chosen finite aggregate of -.5 and0 is negative, unlike
    exact ReLU.
- assessment_id: combined-network-evidence-boundary
  area: evidence
  topic: combined-network-evidence-boundary
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - cohen2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section6 sets the evaluated first MEX parameter to1 and second to the mean
    limit. This is not the equal-parameter collapse case. Existing whole-network comparisons
    include similarity functions, preprocessing, initialization and optimizer changes,
    so no operator-only performance or hardware benefit is inferred.
- assessment_id: constructed-boundaries
  area: consistency
  topic: scalar versus probability-vector identity, mean normalization, nested collapse,
    limiting ReLU and full-network evidence scope
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - cohen2014
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen stable log-mean-exp calculations verify the log-sum-exp normalization
    term, softmax input derivative, shift equivariance, equal-size nested collapse
    and failures with unequal groups or parameters. Finite values differ from exact
    ReLU and max/min limits. These are constructed mathematical checks, not experimental
    replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:MEXOperator
  evidence_ids:
  - identity
  - mapping
  - cohen2014
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all four claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Entire maintained YAML and selected mapping YAMLs
    read after capture. Rechecked Equation1 normalization and parameter limits, Equation2
    group-size/common-parameter scope, MEX layer/ReLU construction and the evaluated
    two-stage parameter choices. Constructed derivative and collapse counterexamples
    were inspected. Exact record/report mirror and source/context hashes agree.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 619 native and 442 unchanged generated records.
  The 803-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All 19 PDF pages visually read, including figures, formulas, tables, references
  and any appendices. No author code, training or empirical replication.
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
