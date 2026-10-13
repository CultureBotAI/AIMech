# Scientific author self-review of Feature-wise Linear Modulation

- Review: 20261013T161809Z-feature-wise-linear-modulation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T16:13:09Z
- Finished UTC: 2026-10-13T16:18:09Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain FiLM as a DRAFT native neural layer with an explicit broad AIO Layer mapping. Every maintained field was assessed against complete primary evidence and constructed algebra checks. No actionable maintained-record defect identified; author self-review only.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:FeatureWiseLinearModulation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e6c27549594f9a37afea1d99852d8cd591365d64.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FeatureWiseLinearModulation | data/curated/FeatureWiseLinearModulation.yaml | maintained | Feature-wise Linear Modulation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FeatureWiseLinearModulation | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 140.50s (0:02:20)<br>Checked 442 record(s); 0 failed.<br>Checked 631 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 307 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 304,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FeatureWiseLinearModulation | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:FeatureWiseLinearModulation | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:FeatureWiseLinearModulation | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:FeatureWiseLinearModulation | {"beta_finite_difference": [0.5999999999950489, 1.7999999999962488], "beta_gradient": [0.6, 1.8], "coupled_input_total_derivative": 4.000000000026205, "frozen_condition_partial_derivative": 2.0, "gamma_finite_difference": [0.14999999999876223, 1.2600000000029254], "gamma_gradient": [0.15, 1.2600000000000002], "operation_counts": [{"coefficients": 4, "height": 14, "multiplies_plus_adds": 784, "width": 14}, {"coefficients": 4, "height": 28, "multiplies_plus_adds": 3136, "width": 28}], "output": [[0.3, 0.3], [0.30000000000000004, 1.5]], "partial_feature_gradient_fixed_condition": [[0.0, 0.0], [0.6000000000000001, 3.0]]} |

## Scientific And Domain Assessments

### Feature-wise Linear Modulation

identity: supported. Targets: AIMech:FeatureWiseLinearModulation.

Retain this distinct DRAFT layer.

Retain FiLM as the condition-generated feature-wise affine layer. The full visual reasoning architecture, fixed speaker adaptation, ordinary rescaling preprocessing and parameter-arithmetic inference procedure have distinct scopes. Unrelated film-library text is not an ontology identity.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:FeatureWiseLinearModulation.

The declared AIO mapping is supported.

The pinned AIO Layer class is broader than this neural conditioning layer. Five full AIO node/edge/YAML contexts and two full native neighbors were inspected. FiLM performs no intrinsic mean/variance standardization and is not equivalent to batch normalization or image preprocessing.

### conditional-feature-affine-rule

evidence: supported. Targets: AIMech:FeatureWiseLinearModulation.

Supported within the stated primary-source and mathematical scope.

The conditioning generator produces one scale and shift per channel in the demonstrated CNN formulation and broadcasts them spatially. The source permits same-input or other-modality conditioning. The record does not turn those into independently generated pixel coefficients.

### affine-and-gradient-boundaries

evidence: supported. Targets: AIMech:FeatureWiseLinearModulation.

Supported within the stated primary-source and mathematical scope.

The operation is affine in features only when conditioning is held fixed. Zero gamma leaves beta and can retain a gamma-generator gradient. Finite differences and an input-dependent scalar example substantiate the distinction without asserting global linearity.

### normalization-independence

evidence: supported. Targets: AIMech:FeatureWiseLinearModulation.

Supported within the stated primary-source and mathematical scope.

FiLM does not itself standardize feature statistics. The main architecture uses a separate batch-normalization operation with disabled affine parameters. Its finite insertion-point and normalization ablations do not guarantee equal quality for every architecture.

### coefficient-count-versus-application-cost

evidence: supported. Targets: AIMech:FeatureWiseLinearModulation.

Supported within the stated primary-source and mathematical scope.

Two generated values per channel are independent of spatial resolution, while applying them requires work proportional to the feature tensor size. Constructed counts distinguish these costs and qualify the source’s resolution-independent phrasing.

### architecture-and-evaluation-scope

evidence: supported. Targets: AIMech:FeatureWiseLinearModulation.

Supported within the stated primary-source and mathematical scope.

CLEVR, CLEVR-Humans and CoGenT experiments use specified visual and language components and supervision. Pretrained image features have ImageNet supervision. Source failures, shifts and parameter-arithmetic applicability prevent universal compositional reasoning or superiority claims.

### conditional affine scope, zero-scale derivative paths, normalization separation and spatial application cost

consistency: supported. Targets: AIMech:FeatureWiseLinearModulation.

Constructed calculations support the stated distinctions.

Finite differences verify scale and shift derivatives for fixed conditioning. Examples show that a zero scale can retain a nonzero shift and scale gradient, input-dependent conditioning adds derivative paths, and spatial application cost grows while coefficient count stays fixed. These are constructed calculations, not author code or hardware benchmarks.

### All maintained fields

provenance: supported. Targets: AIMech:FeatureWiseLinearModulation.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed every maintained field, evidence locator and mapping direction. Challenged fixed-conditioning affine scope versus nonlinear conditional computation, broadcast coefficient count versus application work, zero-scale gradient paths, separate normalization and the limits of visual reasoning experiments.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T161259Z-feature-wise-linear-modulation.json | supports | Compared all 442 pinned AIO and 630 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 67, 0, 9 lines. All distinct match contents were inspected. Semantic matching covered 21 AIO and 90 native definitions, with every matched definition read. 5 full annotated AIO node/edge/generated contexts and 2 full native records were inspected. Retain the conditional feature-wise affine layer. The complete question/image reasoning architecture is a separate scope. A fixed learned speaker transform, input-dependent attention mechanism and generic preprocessing rescaling are not equivalent identities. The FiLM acronym is scoped to the Perez and colleagues conditioning method; unrelated film-library examples do not match. |
| mapping | sources/aio/aio.json | supports | The pinned AIO Layer class is broader than this neural conditioning layer. Five full AIO node/edge/YAML contexts and two full native neighbors were inspected. FiLM performs no intrinsic mean/variance standardization and is not equivalent to batch normalization or image preprocessing. |
| perez2017film | https://arxiv.org/pdf/1709.07871v2; Complete thirteen-page arXiv 1709.07871v2 visually inspected, including Equations 1–3, Tables 1–4, Figures 1–18, references and Appendix Sections 7.1–7.3. Other versions, author code, hardware measurements and empirical replication excluded. | supports | arXiv:1709.07871v2, 18 December 2017, thirteen PDF pages with AAAI 2018 copyright. All pages visually read, including Equations 1–3, Tables 1–4, Figures 1–18, references and Appendix Sections 7.1–7.3. Other versions and author implementation not inspected. |
| calculation | research/discovery/film-boundaries.py | supports | Finite differences verify scale and shift derivatives for fixed conditioning. Examples show that a zero scale can retain a nonzero shift and scale gradient, input-dependent conditioning adds derivative paths, and spatial application cost grows while coefficient count stays fixed. These are constructed calculations, not author code or hardware benchmarks. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 631 native and 442 unchanged generated records. The 816-entry main frontier retains 475 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- Complete thirteen-page primaryv2 visually inspected, including appendix, equations, tables, all18figures and references. No author implementation or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T161809Z-feature-wise-linear-modulation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Feature-wise Linear Modulation
started_at: '2026-10-13T16:13:09Z'
finished_at: '2026-10-13T16:18:09Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged conditional affine scope, zero-scale derivative
    paths, normalization separation and spatial application cost. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain FiLM as a DRAFT native neural layer with an explicit broad AIO Layer
  mapping. Every maintained field was assessed against complete primary evidence and
  constructed algebra checks. No actionable maintained-record defect identified; author
  self-review only.
source:
  git_revision: e6c27549594f9a37afea1d99852d8cd591365d64
  state: working_tree
  inputs:
  - path: data/aio/BatchNormalizationLayer.yaml
    sha256: bd8652e8a4c948e562152d12d81d9e230a2e53355ae84152da9621d0d1468c0b
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/NormalizationLayer.yaml
    sha256: 34991f2f4946bb409ac2b4a22fb8436f8d25ac87e30089278f7ecf8bf00f83fb
    role: context
  - path: data/aio/RescalingLayer.yaml
    sha256: d819303cefc3a220baf09d788a6d39505e53d21b63242e5874b7abd5084ea6d8
    role: context
  - path: data/curated/BalancedAttentionMechanism.yaml
    sha256: 81a15c5f706655cd3a88a47b7a3b5a592b638350205f8db0d336669ffda4f513
    role: context
  - path: data/curated/FeatureWiseLinearModulation.yaml
    sha256: 04cdbed7b9a44ec4fc4c98b2dd6971a1fb6e4fc2c133926febe9411423836b63
    role: target
  - path: data/curated/LearningHiddenUnitContributions.yaml
    sha256: 6b1934004475e048e761316d27b4629080fec2e719154bca49dd7ab001f29f94
    role: context
  - path: research/discovery/20261013T161259Z-feature-wise-linear-modulation.json
    sha256: 9731ddc4e75fd16f7ea2c0dd989a5bd76db7329444c283cf25f2e5b544fe25b2
    role: context
  - path: research/discovery/film-boundaries.py
    sha256: be79e78492628b6bacbe55c8d20b07ccef61301874e1ae62cb652aa6f4cf7f1c
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
- target_id: AIMech:FeatureWiseLinearModulation
  path: data/curated/FeatureWiseLinearModulation.yaml
  label: Feature-wise Linear Modulation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FeatureWiseLinearModulation.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:FeatureWiseLinearModulation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FeatureWiseLinearModulation
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete thirteen-page arXiv 1709.07871v2 visually inspected, including
      Equations 1–3, Tables 1–4, Figures 1–18, references and Appendix Sections 7.1–7.3.
      Other versions, author code, hardware measurements and empirical replication
      excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 140.50s (0:02:20)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 631 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 307 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 304,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FeatureWiseLinearModulation
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
  - AIMech:FeatureWiseLinearModulation
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
  - AIMech:FeatureWiseLinearModulation
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/film-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  exit_code: 0
  expected_exit_code: 0
  summary: '{"beta_finite_difference": [0.5999999999950489, 1.7999999999962488], "beta_gradient":
    [0.6, 1.8], "coupled_input_total_derivative": 4.000000000026205, "frozen_condition_partial_derivative":
    2.0, "gamma_finite_difference": [0.14999999999876223, 1.2600000000029254], "gamma_gradient":
    [0.15, 1.2600000000000002], "operation_counts": [{"coefficients": 4, "height":
    14, "multiplies_plus_adds": 784, "width": 14}, {"coefficients": 4, "height": 28,
    "multiplies_plus_adds": 3136, "width": 28}], "output": [[0.3, 0.3], [0.30000000000000004,
    1.5]], "partial_feature_gradient_fixed_condition": [[0.0, 0.0], [0.6000000000000001,
    3.0]]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T161259Z-feature-wise-linear-modulation.json
  accessed_at: '2026-10-13T16:13:09Z'
  support: supports
  summary: Compared all 442 pinned AIO and 630 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    67, 0, 9 lines. All distinct match contents were inspected. Semantic matching
    covered 21 AIO and 90 native definitions, with every matched definition read.
    5 full annotated AIO node/edge/generated contexts and 2 full native records were
    inspected. Retain the conditional feature-wise affine layer. The complete question/image
    reasoning architecture is a separate scope. A fixed learned speaker transform,
    input-dependent attention mechanism and generic preprocessing rescaling are not
    equivalent identities. The FiLM acronym is scoped to the Perez and colleagues
    conditioning method; unrelated film-library examples do not match.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T16:13:09Z'
  support: supports
  summary: The pinned AIO Layer class is broader than this neural conditioning layer.
    Five full AIO node/edge/YAML contexts and two full native neighbors were inspected.
    FiLM performs no intrinsic mean/variance standardization and is not equivalent
    to batch normalization or image preprocessing.
- evidence_id: perez2017film
  kind: primary_source
  reference: https://arxiv.org/pdf/1709.07871v2
  locator: Complete thirteen-page arXiv 1709.07871v2 visually inspected, including
    Equations 1–3, Tables 1–4, Figures 1–18, references and Appendix Sections 7.1–7.3.
    Other versions, author code, hardware measurements and empirical replication excluded.
  accessed_at: '2026-10-13T14:50:22Z'
  snapshot_sha256: 765acea6f2a78b1d76961392099cd0af49cb2e7d6f06d0b3d82f1dbe9cdcd363
  support: supports
  summary: arXiv:1709.07871v2, 18 December 2017, thirteen PDF pages with AAAI 2018
    copyright. All pages visually read, including Equations 1–3, Tables 1–4, Figures
    1–18, references and Appendix Sections 7.1–7.3. Other versions and author implementation
    not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/film-boundaries.py
  accessed_at: '2026-10-13T16:16:36Z'
  snapshot_sha256: be79e78492628b6bacbe55c8d20b07ccef61301874e1ae62cb652aa6f4cf7f1c
  support: supports
  summary: Finite differences verify scale and shift derivatives for fixed conditioning.
    Examples show that a zero scale can retain a nonzero shift and scale gradient,
    input-dependent conditioning adds derivative paths, and spatial application cost
    grows while coefficient count stays fixed. These are constructed calculations,
    not author code or hardware benchmarks.
assessments:
- assessment_id: identity
  area: identity
  topic: Feature-wise Linear Modulation
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - identity
  - perez2017film
  summary: Retain this distinct DRAFT layer.
  details: Retain FiLM as the condition-generated feature-wise affine layer. The full
    visual reasoning architecture, fixed speaker adaptation, ordinary rescaling preprocessing
    and parameter-arithmetic inference procedure have distinct scopes. Unrelated film-library
    text is not an ontology identity.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - mapping
  - perez2017film
  summary: The declared AIO mapping is supported.
  details: The pinned AIO Layer class is broader than this neural conditioning layer.
    Five full AIO node/edge/YAML contexts and two full native neighbors were inspected.
    FiLM performs no intrinsic mean/variance standardization and is not equivalent
    to batch normalization or image preprocessing.
- assessment_id: conditional-feature-affine-rule
  area: evidence
  topic: conditional-feature-affine-rule
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: The conditioning generator produces one scale and shift per channel in
    the demonstrated CNN formulation and broadcasts them spatially. The source permits
    same-input or other-modality conditioning. The record does not turn those into
    independently generated pixel coefficients.
- assessment_id: affine-and-gradient-boundaries
  area: evidence
  topic: affine-and-gradient-boundaries
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The operation is affine in features only when conditioning is held fixed.
    Zero gamma leaves beta and can retain a gamma-generator gradient. Finite differences
    and an input-dependent scalar example substantiate the distinction without asserting
    global linearity.
- assessment_id: normalization-independence
  area: evidence
  topic: normalization-independence
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: FiLM does not itself standardize feature statistics. The main architecture
    uses a separate batch-normalization operation with disabled affine parameters.
    Its finite insertion-point and normalization ablations do not guarantee equal
    quality for every architecture.
- assessment_id: coefficient-count-versus-application-cost
  area: evidence
  topic: coefficient-count-versus-application-cost
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Two generated values per channel are independent of spatial resolution,
    while applying them requires work proportional to the feature tensor size. Constructed
    counts distinguish these costs and qualify the source’s resolution-independent
    phrasing.
- assessment_id: architecture-and-evaluation-scope
  area: evidence
  topic: architecture-and-evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: CLEVR, CLEVR-Humans and CoGenT experiments use specified visual and language
    components and supervision. Pretrained image features have ImageNet supervision.
    Source failures, shifts and parameter-arithmetic applicability prevent universal
    compositional reasoning or superiority claims.
- assessment_id: constructed-boundaries
  area: consistency
  topic: conditional affine scope, zero-scale derivative paths, normalization separation
    and spatial application cost
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - perez2017film
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Finite differences verify scale and shift derivatives for fixed conditioning.
    Examples show that a zero scale can retain a nonzero shift and scale gradient,
    input-dependent conditioning adds derivative paths, and spatial application cost
    grows while coefficient count stays fixed. These are constructed calculations,
    not author code or hardware benchmarks.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:FeatureWiseLinearModulation
  evidence_ids:
  - identity
  - mapping
  - perez2017film
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed every maintained field, evidence locator and
    mapping direction. Challenged fixed-conditioning affine scope versus nonlinear
    conditional computation, broadcast coefficient count versus application work,
    zero-scale gradient paths, separate normalization and the limits of visual reasoning
    experiments.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 631 native and 442 unchanged generated records.
  The 816-entry main frontier retains 475 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- Complete thirteen-page primaryv2 visually inspected, including appendix, equations,
  tables, all18figures and references. No author implementation or empirical replication.
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
