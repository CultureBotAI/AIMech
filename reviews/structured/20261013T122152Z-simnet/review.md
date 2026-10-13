# Scientific author self-review of SimNet

- Review: 20261013T122152Z-simnet
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T12:10:28Z
- Finished UTC: 2026-10-13T12:21:52Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SimNet as a DRAFT architecture family with supported identity, mappings and all six claims. No actionable defect found in this adversarial author self-review. Kernel, initialization and evaluation conclusions remain limited to inspected source conditions; no author-code or benchmark replication.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:SimNet
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7790076626bda6cfbbe062064085c36db2632290.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SimNet | data/curated/SimNet.yaml | maintained | SimNet |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SimNet | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 149.21s (0:02:29)<br>Checked 442 record(s); 0 failed.<br>Checked 615 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 285 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 281,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SimNet | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SimNet | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SimNet | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:SimNet | {"different_parameter_nested": 2.0269476687206525, "equal_group_collapse": 2.798888091483922, "finite_relu_surrogate": -0.21907019637983863, "hard_majority_class": 0, "kernel_identity_lhs": -0.397653850676081, "kernel_identity_rhs": -0.39765385067608083, "mean_score_class": 1, "mex_max_approx": 2.998901387711332, "mex_min_approx": -0.9989013877113319, "mex_positive": 2.2279503525993607, "mex_zero_limit": 1.3333333333333333, "unequal_group_nested": 2.423407770337307} |

## Scientific And Domain Assessments

### SimNet

identity: supported. Targets: AIMech:SimNet.

Retain this distinct DRAFT architecture.

Retain Cohen and Shashua’s similarity/MEX neural architecture family. SimSiam, generated dynamic kernels and arbitrary Siamese or similarity-scoring networks are not equivalent. Original shallow evaluation and the abstract-only Deep SimNets followup do not justify a second identity or a deep-performance claim.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:SimNet.

The declared AIO mapping is supported.

ANN is broader than this neural family. DeepConvolutionalNetwork is related because the operator family generalizes convolutional configurations but is not confined to their image-specific scope. Conv, Kernel and Pooling layers are components; the pinned KernelLayer means a dot-product component rather than an RKHS kernel. Perceptron has a single binary linear threshold definition despite its feed-forward synonym. All six annotated AIO node/edge/generated contexts were inspected.

### similarity-and-template-sharing

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Section2 gives u^T phi with nonnegative coordinate weights, product or negative powered-distance matching and p&gt;0. Unit product weights recover the inner product; patch sharing yields convolution. The weighted sum can be negative and general p does not imply a metric or PSD kernel.

### mex-limits-and-collapse

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Equations1–2 use log-mean-exp divided by xi, mean at zero and max/min limits. Equal-size groups and common xi preserve normalization; constructed unequal groups or unequal parameters do not collapse. Finite MEX with zero is not exact ReLU; its recovery uses the positive infinite limit.

### kernel-interpretation-scope

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Sections3.1–3.2 require positive fixed xi, unit weights and either product or0&lt;p&lt;=2 distance similarity. Theorem1 rules out its stated universal weighted-distance kernel identity, not all approximation. The algebraic score representation supplies no equivalence to maximum-margin optimization. The chosen unweighted Gaussian example verifies one identity only.

### initialization-and-supervision

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Section5 page9 explicitly derives a component log-joint up to c_l from generalized Gaussian mixture parameters. It is not a normalized posterior. The experimental text initializes on unlabeled training patches and then optimizes supervised softmax loss; semantics after training are not guaranteed.

### patch-labeling-instantiation

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Figure3(a) and Section6 give six-by-six RGB patches, stride1, p1/2, first xi1 and final xi0 averaging, with regional offsets. Averaging real class scores can disagree with a hard majority of patch winners, as the constructed three-patch counterexample shows.

### evaluation-and-parameter-limits

evidence: supported. Targets: AIMech:SimNet.

Supported within the stated primary-source and mathematical scope.

Section6.1 explicitly calls Figures4–5 cross-validation accuracy. Pages12–13 give77.1percent/400 templates,76.2percent/6400 CNN and78.3percent/3200 triangle coding, differing preprocessing and optimization, and selected random-initialization losses. Parameter counts do not establish measured runtime. The body explicitly denies dataset state-of-the-art performance despite broader abstract wording; deeper evaluation is future work in this version.

### MEX limits and normalization, kernel-identity assumptions, probabilistic interpretation, score aggregation and historical cross-validation comparisons

consistency: supported. Targets: AIMech:SimNet.

Constructed calculations support the stated distinctions.

Chosen log-mean-exp examples distinguish limits from finite operators, demonstrate the conditions of nested collapse, verify a restricted kernel identity and contrast real-score averaging with hard majority voting. No formal proof certification, author-code execution or benchmark replication.

### All maintained fields

provenance: supported. Targets: AIMech:SimNet.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Entire maintained YAML and selected AIO mapping YAMLs read after capture. Rechecked similarity/MEX definitions, collapse and ReLU conditions, the exact universal identity in Theorem1, mixture log-joint formula, Figure3 and cross-validation/parameter comparisons. The constructed calculations and exact synchronized report mirror were inspected. No actionable defect found in this declared scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T121013Z-simnet.json | supports | Compared all 442 pinned AIO and 614 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 7, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 30 AIO and 55 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 2 full native records were inspected. SimNet denotes Cohen and Shashua’s architecture family composed from similarity and MEX operators. It is not SimSiam similarity-based representation learning, a dynamic generated-kernel layer, a generic Siamese network or every network with a similarity score. The generic phrase similarity network was searched for ambiguity but is not asserted as an unqualified exact alias. |
| mapping | sources/aio/aio.json | supports | ANN is broader than this neural family. DeepConvolutionalNetwork is related because the operator family generalizes convolutional configurations but is not confined to their image-specific scope. Conv, Kernel and Pooling layers are components; the pinned KernelLayer means a dot-product component rather than an RKHS kernel. Perceptron has a single binary linear threshold definition despite its feed-forward synonym. All six annotated AIO node/edge/generated contexts were inspected. |
| cohen2014 | https://arxiv.org/pdf/1410.0781v3; Complete 19-page arXiv:1410.0781v3 including mathematical appendices inspected. No independent formal-proof certification, author implementation, later full-paper version, model fitting or empirical replication. | supports | arXiv:1410.0781v3, 7 December 2014, 19 PDF pages including Appendices A–B; all pages visually read. PDF/printed page numbers coincide. No journal acceptance, author implementation or empirical replication inferred. The later Deep SimNets paper was encountered as an abstract-only followup, not used as claim evidence. |
| calculation | research/discovery/simnet-boundaries.py | supports | Chosen log-mean-exp examples distinguish limits from finite operators, demonstrate the conditions of nested collapse, verify a restricted kernel identity and contrast real-score averaging with hard majority voting. No formal proof certification, author-code execution or benchmark replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 615 native and 442 unchanged generated records. The 799-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 19 PDF pages visually read, including figures, formulas, tables, references and any appendices. No author code, training or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T122152Z-simnet
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SimNet
started_at: '2026-10-13T12:10:28Z'
finished_at: '2026-10-13T12:21:52Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged MEX limits and normalization, kernel-identity
    assumptions, probabilistic interpretation, score aggregation and historical cross-validation
    comparisons. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SimNet as a DRAFT architecture family with supported identity, mappings
  and all six claims. No actionable defect found in this adversarial author self-review.
  Kernel, initialization and evaluation conclusions remain limited to inspected source
  conditions; no author-code or benchmark replication.
source:
  git_revision: 7790076626bda6cfbbe062064085c36db2632290
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/DeepConvolutionalNetwork.yaml
    sha256: b2be73a895ae3890ca0ba464c1d0de55e41960f33ec53dcab4547abfe1159c62
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/Perceptron.yaml
    sha256: 6b1cc7cb96bfe03ed8720cca04490657976eea656fab6674d7ef685c34216915
    role: context
  - path: data/aio/PoolingLayer.yaml
    sha256: 2a5cc182b52109a337a926a42bd715d5f1142e2a0876a8bfbc41890846e84246
    role: context
  - path: data/curated/DynamicConvolutionalLayer.yaml
    sha256: 5cd632daf0ae4a1d9420d6b6989ce7775be966820eb60b3a84c1c08ef6b62190
    role: context
  - path: data/curated/SimNet.yaml
    sha256: 9fb428e28a283c959c45f9245470db476c589d43c7f7dda909976e85a8d78f78
    role: target
  - path: data/curated/SimSiam.yaml
    sha256: 283a7d1d5f9bbd6bff853294b71e26d5489a412568bfff0846bef831d9019fe3
    role: context
  - path: research/discovery/20261013T121013Z-simnet.json
    sha256: 4d1f05934275f33f1c7338eed51dd082756041dcc426c22ae9d42b7a8d0d65af
    role: context
  - path: research/discovery/simnet-boundaries.py
    sha256: c5cb6c50ec83f391c5e595b46daac04acf5c4a77be9bbf49267209e58b9e190a
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
- target_id: AIMech:SimNet
  path: data/curated/SimNet.yaml
  label: SimNet
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SimNet.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:SimNet'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SimNet
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete 19-page arXiv:1410.0781v3 including mathematical appendices inspected.
      No independent formal-proof certification, author implementation, later full-paper
      version, model fitting or empirical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SimNet
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 149.21s (0:02:29)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 615 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 285 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 281,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SimNet
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
  - AIMech:SimNet
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
  - AIMech:SimNet
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/simnet-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SimNet
  exit_code: 0
  expected_exit_code: 0
  summary: '{"different_parameter_nested": 2.0269476687206525, "equal_group_collapse":
    2.798888091483922, "finite_relu_surrogate": -0.21907019637983863, "hard_majority_class":
    0, "kernel_identity_lhs": -0.397653850676081, "kernel_identity_rhs": -0.39765385067608083,
    "mean_score_class": 1, "mex_max_approx": 2.998901387711332, "mex_min_approx":
    -0.9989013877113319, "mex_positive": 2.2279503525993607, "mex_zero_limit": 1.3333333333333333,
    "unequal_group_nested": 2.423407770337307}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T121013Z-simnet.json
  accessed_at: '2026-10-13T12:10:28Z'
  support: supports
  summary: Compared all 442 pinned AIO and 614 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    7, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    30 AIO and 55 native definitions, with every matched definition read. 6 full annotated
    AIO node/edge/generated contexts and 2 full native records were inspected. SimNet
    denotes Cohen and Shashua’s architecture family composed from similarity and MEX
    operators. It is not SimSiam similarity-based representation learning, a dynamic
    generated-kernel layer, a generic Siamese network or every network with a similarity
    score. The generic phrase similarity network was searched for ambiguity but is
    not asserted as an unqualified exact alias.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T12:10:28Z'
  support: supports
  summary: ANN is broader than this neural family. DeepConvolutionalNetwork is related
    because the operator family generalizes convolutional configurations but is not
    confined to their image-specific scope. Conv, Kernel and Pooling layers are components;
    the pinned KernelLayer means a dot-product component rather than an RKHS kernel.
    Perceptron has a single binary linear threshold definition despite its feed-forward
    synonym. All six annotated AIO node/edge/generated contexts were inspected.
- evidence_id: cohen2014
  kind: primary_source
  reference: https://arxiv.org/pdf/1410.0781v3
  locator: Complete 19-page arXiv:1410.0781v3 including mathematical appendices inspected.
    No independent formal-proof certification, author implementation, later full-paper
    version, model fitting or empirical replication.
  accessed_at: '2026-10-13T11:58:05Z'
  snapshot_sha256: 91119773f55d79557a02212c71a3c49d491223229b5354b24610eb0d3e89de26
  support: supports
  summary: arXiv:1410.0781v3, 7 December 2014, 19 PDF pages including Appendices A–B;
    all pages visually read. PDF/printed page numbers coincide. No journal acceptance,
    author implementation or empirical replication inferred. The later Deep SimNets
    paper was encountered as an abstract-only followup, not used as claim evidence.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/simnet-boundaries.py
  accessed_at: '2026-10-13T12:21:22Z'
  snapshot_sha256: c5cb6c50ec83f391c5e595b46daac04acf5c4a77be9bbf49267209e58b9e190a
  support: supports
  summary: Chosen log-mean-exp examples distinguish limits from finite operators,
    demonstrate the conditions of nested collapse, verify a restricted kernel identity
    and contrast real-score averaging with hard majority voting. No formal proof certification,
    author-code execution or benchmark replication.
assessments:
- assessment_id: identity
  area: identity
  topic: SimNet
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - identity
  - cohen2014
  summary: Retain this distinct DRAFT architecture.
  details: Retain Cohen and Shashua’s similarity/MEX neural architecture family. SimSiam,
    generated dynamic kernels and arbitrary Siamese or similarity-scoring networks
    are not equivalent. Original shallow evaluation and the abstract-only Deep SimNets
    followup do not justify a second identity or a deep-performance claim.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - mapping
  - cohen2014
  summary: The declared AIO mapping is supported.
  details: ANN is broader than this neural family. DeepConvolutionalNetwork is related
    because the operator family generalizes convolutional configurations but is not
    confined to their image-specific scope. Conv, Kernel and Pooling layers are components;
    the pinned KernelLayer means a dot-product component rather than an RKHS kernel.
    Perceptron has a single binary linear threshold definition despite its feed-forward
    synonym. All six annotated AIO node/edge/generated contexts were inspected.
- assessment_id: similarity-and-template-sharing
  area: evidence
  topic: similarity-and-template-sharing
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2 gives u^T phi with nonnegative coordinate weights, product or
    negative powered-distance matching and p>0. Unit product weights recover the inner
    product; patch sharing yields convolution. The weighted sum can be negative and
    general p does not imply a metric or PSD kernel.
- assessment_id: mex-limits-and-collapse
  area: evidence
  topic: mex-limits-and-collapse
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations1–2 use log-mean-exp divided by xi, mean at zero and max/min limits.
    Equal-size groups and common xi preserve normalization; constructed unequal groups
    or unequal parameters do not collapse. Finite MEX with zero is not exact ReLU;
    its recovery uses the positive infinite limit.
- assessment_id: kernel-interpretation-scope
  area: evidence
  topic: kernel-interpretation-scope
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections3.1–3.2 require positive fixed xi, unit weights and either product
    or0<p<=2 distance similarity. Theorem1 rules out its stated universal weighted-distance
    kernel identity, not all approximation. The algebraic score representation supplies
    no equivalence to maximum-margin optimization. The chosen unweighted Gaussian
    example verifies one identity only.
- assessment_id: initialization-and-supervision
  area: evidence
  topic: initialization-and-supervision
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section5 page9 explicitly derives a component log-joint up to c_l from
    generalized Gaussian mixture parameters. It is not a normalized posterior. The
    experimental text initializes on unlabeled training patches and then optimizes
    supervised softmax loss; semantics after training are not guaranteed.
- assessment_id: patch-labeling-instantiation
  area: evidence
  topic: patch-labeling-instantiation
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure3(a) and Section6 give six-by-six RGB patches, stride1, p1/2, first
    xi1 and final xi0 averaging, with regional offsets. Averaging real class scores
    can disagree with a hard majority of patch winners, as the constructed three-patch
    counterexample shows.
- assessment_id: evaluation-and-parameter-limits
  area: evidence
  topic: evaluation-and-parameter-limits
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section6.1 explicitly calls Figures4–5 cross-validation accuracy. Pages12–13
    give77.1percent/400 templates,76.2percent/6400 CNN and78.3percent/3200 triangle
    coding, differing preprocessing and optimization, and selected random-initialization
    losses. Parameter counts do not establish measured runtime. The body explicitly
    denies dataset state-of-the-art performance despite broader abstract wording;
    deeper evaluation is future work in this version.
- assessment_id: constructed-boundaries
  area: consistency
  topic: MEX limits and normalization, kernel-identity assumptions, probabilistic
    interpretation, score aggregation and historical cross-validation comparisons
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - cohen2014
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen log-mean-exp examples distinguish limits from finite operators,
    demonstrate the conditions of nested collapse, verify a restricted kernel identity
    and contrast real-score averaging with hard majority voting. No formal proof certification,
    author-code execution or benchmark replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:SimNet
  evidence_ids:
  - identity
  - mapping
  - cohen2014
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Entire maintained YAML and selected AIO mapping
    YAMLs read after capture. Rechecked similarity/MEX definitions, collapse and ReLU
    conditions, the exact universal identity in Theorem1, mixture log-joint formula,
    Figure3 and cross-validation/parameter comparisons. The constructed calculations
    and exact synchronized report mirror were inspected. No actionable defect found
    in this declared scope.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 615 native and 442 unchanged generated records.
  The 799-entry main frontier retains 477 pending and 57 partly addressed cohorts,
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
