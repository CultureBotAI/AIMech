# Scientific self-review of five point and set architectures

- Review: 20261011T042145Z-point-and-set-architectures
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:21:45Z
- Finished UTC: 2026-10-11T04:21:45Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All five architecture identities and mechanisms have inspected primary support and justified broader AIO mappings. Their base/variant distinctions, symmetry properties and numerical/implementation limitations are preserved. No actionable unresolved defect was identified in these five records.

## Scope And Provenance

Identity, definitions, mechanism evidence, source versions, limitations and AIO mappings for five point/set architecture additions.

Selection: Exactly the five entries in the point-and-set-architectures discovery report; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 03016c6a386cff3b9aefd6fc21e80d9d27e63896.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PointNet | data/curated/PointNet.yaml | maintained | PointNet |
| AIMech:SetTransformer | data/curated/SetTransformer.yaml | maintained | Set Transformer |
| AIMech:PointNetPlusPlus | data/curated/PointNetPlusPlus.yaml | maintained | PointNet++ |
| AIMech:DeepSetsPlusPlus | data/curated/DeepSetsPlusPlus.yaml | maintained | Deep Sets++ |
| AIMech:SetTransformerPlusPlus | data/curated/SetTransformerPlusPlus.yaml | maintained | Set Transformer++ |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | Checked 442 record(s); 0 failed. |
| python -m aimech validate-curated | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | Checked 82 curated concept record(s); 0 error(s). |
| python -m aimech seed --check | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python -m aimech validate-history --base HEAD | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | Checked 14 history record(s); 0 error(s). |
| python scripts/record_review.py check | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 12,<br>  "coverage": "declared_scopes_only"<br>} |
| PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 40.06s<br>Checked 442 record(s); 0 failed.<br>Checked 82 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 14 history record(s); 0 error(s).<br>topClass is deprecated - use top_class<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 12,<br>  "coverage": "declared_scopes_only"<br>}<br> |
| PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check | passed | True | AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus | bash scripts/check_vendored_sync.sh<br>OK: 22 governed artifacts match the pinned claw revision<br> |

## Scientific And Domain Assessments

### Architecture identity and primary-method support

evidence: supported. Targets: AIMech:PointNet.

This is the original PointNet architecture, including its classification and segmentation paths. It is distinct from PointNet++'s hierarchical local grouping and from a generic set-pooling model.

Permutation invariance of a global output and permutation equivariance of per-point predictions are different properties. Learned alignment modules do not establish exact invariance to every geometric transformation; no universal accuracy or robustness claim is curated.

### Architecture identity and primary-method support

evidence: supported. Targets: AIMech:SetTransformer.

The Set Transformer is a set-input architecture, not the AIO Transformer Language Model class, an individual multihead attention layer, or the later Set Transformer++ encoder revision.

The encoder is permutation equivariant; the pooled output is invariant to input ordering. Multiple seed outputs are not input-element labels. Linear scaling with input-set size concerns a fixed number of inducing points; ordinary self-attention blocks have quadratic interactions. No universal benchmark superiority is asserted.

### Architecture identity and primary-method support

evidence: supported. Targets: AIMech:PointNetPlusPlus.

PointNet++ adds hierarchical local set abstraction to PointNet. Multi-scale and multi-resolution grouping are distinct variants within this architecture; the paper also evaluates a single-scale ablation.

Neighborhood scale, sampling density and the selected grouping variant affect the representation; density-adaptive construction is not a guarantee for arbitrary missing data. The single-scale ablation, multi-scale grouping and multi-resolution grouping are not identical procedures. No universal benchmark advantage is curated.

### Architecture identity and primary-method support

evidence: supported. Targets: AIMech:DeepSetsPlusPlus.

Deep Sets++ is the encoder revision defined by Zhang and colleagues, not an alternate spelling of Deep Sets or a claim that every deeper set network uses this construction.

The written standardization assumes a nonzero denominator; this record does not specify numerical handling of degenerate or padded sets. The change concerns the encoder. Its construction does not guarantee improved training or accuracy for every task.

### Architecture identity and primary-method support

evidence: supported. Targets: AIMech:SetTransformerPlusPlus.

Set Transformer++ denotes the specific encoder revision and ISAB++ construction in Zhang and colleagues. It is distinct from the original Set Transformer and from Deep Sets++ despite their shared residual and normalization design principles.

This record covers the source's ISAB++ encoder construction, not all possible residual attention variants. Set standardization assumes a nonzero variance; no universal optimization or benchmark improvement is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus. Retain original pointwise/global PointNet, hierarchical PointNet++, attention-based Set Transformer and the separately defined DS++/ST++ encoder revisions. Shared set-input symmetry or normalization does not make these architectures equivalent.
- defer: AIMech:PointNet, AIMech:SetTransformer, AIMech:PointNetPlusPlus, AIMech:DeepSetsPlusPlus, AIMech:SetTransformerPlusPlus. Do not automatically turn every named layer or sampling component into a new architecture record. Resolve the independent identity and native layer representation of set norm, MAB/SAB/ISAB/PMA, ISAB++, grouping and alignment components before further additions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T041944Z-point-and-set-architectures.json | supports | All 442 AIO labels/scoped synonyms and 77 prior native identities were compared with the plus-preserving normalizer. Ignored-inclusive hits were prior leads, adjacent concepts, the new validator reproduction/tests and an incidental Git hook substring; no duplicate concept identity. |
| mapping | sources/aio/aio.json; ArtificialNeuralNetwork, TransformerLanguageModel and MultiHeadAttentionLayer | supports | Each addition is a specific learned neural architecture, with broad_match to ArtificialNeuralNetwork. TransformerLanguageModel is restricted to language modeling, and MultiHeadAttentionLayer denotes a component, so neither is an exact identity for the set architecture. |
| pointnet-method | https://openaccess.thecvf.com/content_cvpr_2017/papers/Qi_PointNet_Deep_Learning_CVPR_2017_paper.pdf; Section 4.2, Figure 2 and equations 1–2, PDF pp. 3–4 / printed pp. 654–655 | supports | Shared multilayer perceptrons encode points; max pooling aggregates their features. The segmentation path concatenates the global descriptor with point features before shared prediction layers. Learned input and feature transformations provide alignment modules. Rendered pages actually inspected: 3, 4. |
| settransformer-method | https://proceedings.mlr.press/v97/lee19d/lee19d.pdf; Sections 3.1–3.4, equations 6–16 and Figure 1, PDF pp. 3–4 | supports | Stack self-attention or induced-attention blocks without positional encoding, then pool encoded features by attention from learned seed vectors. The induced variant first attends from learned inducing points to the input and then from the input to the resulting summaries. Rendered pages actually inspected: 3, 4. |
| pointnetplusplus-method | https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf; Sections 3.2–3.3, Figures 2–3, PDF/printed pp. 3–5 | supports | Farthest-point sampling chooses centroids; neighborhood grouping and local-coordinate PointNet encoders produce features for successive abstraction levels. Multi-scale grouping concatenates features from different radii, while multi-resolution grouping combines lower-level summaries with directly encoded regional points. Rendered pages actually inspected: 3, 4, 5. |
| deepsetsplusplus-method | https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf; Section 4 opening and Sections 4.1–4.3, Figure 2 and the DS++ block equation, PDF pp. 4–6 | supports | Encoder blocks add an unmodified input to a transformed branch using learned linear maps, ReLU and set normalization. Set normalization uses a mean and variance over each set's elements and feature coordinates, followed by feature-specific scale and bias. Rendered pages actually inspected: 5, 6. |
| settransformerplusplus-method | https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf; Section 4 opening and Sections 4.1–4.2 and 4.4, Figure 2 and equations 21–26, PDF pp. 4–6 | supports | The revised encoder uses two successive attention blocks linking learned inducing points and input elements. Set normalization occurs on the transformed attention and feedforward branches, while each residual addition retains its unmodified query-side input. Rendered pages actually inspected: 5, 6. |
| implementation-scope | https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf; Section 3 footnote 2, PDF p. 3; Section 4, PDF pp. 4–6 | context_only | The later paper follows a Set Transformer implementation baseline that differs from the original MAB paper definition. The current records cite their own defining constructions without asserting identical code and paper variants. |

## Limits And Additional Notes

- Scientific self-review, not independent approval or experimental replication.
- PointNet alignment is learned, Set Transformer complexity depends on its block choice, and PointNet++ grouping variants remain distinct.
- Set norm assumes nonzero variance; no unsupported padding/degenerate-input implementation rule is inferred.
- Original-paper and later implementation-baseline scopes remain distinct. All five records remain DRAFT; discovery is ongoing.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T042145Z-point-and-set-architectures
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of five point and set architectures
started_at: '2026-10-11T04:21:45Z'
finished_at: '2026-10-11T04:21:45Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent researched, authored and reviewed these records;
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All five architecture identities and mechanisms have inspected primary support
  and justified broader AIO mappings. Their base/variant distinctions, symmetry properties
  and numerical/implementation limitations are preserved. No actionable unresolved
  defect was identified in these five records.
source:
  git_revision: 03016c6a386cff3b9aefd6fc21e80d9d27e63896
  state: working_tree
  inputs:
  - path: data/curated/DeepSetsPlusPlus.yaml
    sha256: e612b62bc0a9424615974a0ef89fd9f70d6c0b4e08aaea0ef2d30fc2d5de594b
    role: target
  - path: data/curated/PointNet.yaml
    sha256: b2292a45d360ee989f143838b4ca9008033e69d63c5b578e7e2ab45fb6ee80dd
    role: target
  - path: data/curated/PointNetPlusPlus.yaml
    sha256: 46c6a537105778b2cb776e30bb1e4c394d18333492752d1aaee38ab6b3e9696c
    role: target
  - path: data/curated/SetTransformer.yaml
    sha256: 8c20fa1dbeb0add989673a24a446bb55bc5ca94130bd95939cc1b16f959690bf
    role: target
  - path: data/curated/SetTransformerPlusPlus.yaml
    sha256: 902e4372ab7ff92da5911bdc1880c4ab116e1d0af88d398794d8b70225b543e0
    role: target
  - path: docs/curated-concepts.md
    sha256: 0b6f6aa0ffa770e8521b51b90e227ace92be8a8fff49f1e066d836cc11c11c2e
    role: context
  - path: research/discovery/20261011T041944Z-point-and-set-architectures.json
    sha256: c5b935290e036685cc694d9eb38b8ee795c090922f925e14de3c18e0daa0b0b8
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: dfcbacdcdeb7429bfa947d7c1c8431e5d0b886f593daaa359588273ba2a2c6e0
    role: context
targets:
- target_id: AIMech:PointNet
  path: data/curated/PointNet.yaml
  label: PointNet
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PointNet.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:SetTransformer
  path: data/curated/SetTransformer.yaml
  label: Set Transformer
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SetTransformer.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:PointNetPlusPlus
  path: data/curated/PointNetPlusPlus.yaml
  label: PointNet++
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PointNetPlusPlus.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:DeepSetsPlusPlus
  path: data/curated/DeepSetsPlusPlus.yaml
  label: Deep Sets++
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DeepSetsPlusPlus.yaml
    role: maintained concept and claim evidence/mapping
- target_id: AIMech:SetTransformerPlusPlus
  path: data/curated/SetTransformerPlusPlus.yaml
  label: Set Transformer++
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SetTransformerPlusPlus.yaml
    role: maintained concept and claim evidence/mapping
scope:
  description: Identity, definitions, mechanism evidence, source versions, limitations
    and AIO mappings for five point/set architecture additions.
  selection: Exactly the five entries in the point-and-set-architectures discovery
    report; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exclusions:
  - target: Identity-normalizer implementation finding
    reason: Reviewed separately with its exact issue key, initial finding and evidence-backed
      successor.
  - target: Universal performance, numerical implementation and all component-layer
      identities
    reason: Architecture support does not imply benchmark superiority or specify uninspected
      numerical behavior; component scope and native layer representation remain explicit
      leads.
checks:
- check_id: required-0
  name: python -m aimech check-source
  command: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
- check_id: required-1
  name: python -m aimech validate
  command: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
- check_id: required-2
  name: python -m aimech validate-curated
  command: python -m aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 82 curated concept record(s); 0 error(s).
- check_id: required-3
  name: python -m aimech seed --check
  command: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
- check_id: required-4
  name: python -m aimech validate-history --base HEAD
  command: python -m aimech validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 14 history record(s); 0 error(s).
- check_id: required-5
  name: python scripts/record_review.py check
  command: python scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 12,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}"
- check_id: required-6
  name: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: "uv run --locked --extra dev python scripts/check.py\nAll checks passed!\n\
    ........................................................................ [ 31%]\n\
    ........................................................................ [ 63%]\n\
    ........................................................................ [ 94%]\n\
    .........sss                                                             [100%]\n\
    225 passed, 3 skipped in 40.06s\nChecked 442 record(s); 0 failed.\nChecked 82\
    \ curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing, 0 changed,\
    \ 0 unexpected.\nChecked 14 history record(s); 0 error(s).\ntopClass is deprecated\
    \ - use top_class\n{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\"\
    : 12,\n  \"coverage\": \"declared_scopes_only\"\n}\n"
- check_id: required-7
  name: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  exit_code: 0
  expected_exit_code: 0
  summary: 'bash scripts/check_vendored_sync.sh

    OK: 22 governed artifacts match the pinned claw revision

    '
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T041944Z-point-and-set-architectures.json
  accessed_at: '2026-10-11T04:21:45Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 77 prior native identities were
    compared with the plus-preserving normalizer. Ignored-inclusive hits were prior
    leads, adjacent concepts, the new validator reproduction/tests and an incidental
    Git hook substring; no duplicate concept identity.
  search_scope: All 442 AIO labels/scoped synonyms and 77 preceding native identities,
    with ignored-inclusive and hidden-inclusive text searches of both checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: ArtificialNeuralNetwork, TransformerLanguageModel and MultiHeadAttentionLayer
  accessed_at: '2026-10-11T04:21:45Z'
  support: supports
  summary: Each addition is a specific learned neural architecture, with broad_match
    to ArtificialNeuralNetwork. TransformerLanguageModel is restricted to language
    modeling, and MultiHeadAttentionLayer denotes a component, so neither is an exact
    identity for the set architecture.
- evidence_id: pointnet-method
  kind: primary_source
  reference: https://openaccess.thecvf.com/content_cvpr_2017/papers/Qi_PointNet_Deep_Learning_CVPR_2017_paper.pdf
  locator: Section 4.2, Figure 2 and equations 1–2, PDF pp. 3–4 / printed pp. 654–655
  accessed_at: '2026-10-11T04:11:09Z'
  snapshot_sha256: 7c4c69310de5130b079e80c5771322ed45ca8f032d592396303bc93b19bea3ec
  support: supports
  summary: 'Shared multilayer perceptrons encode points; max pooling aggregates their
    features. The segmentation path concatenates the global descriptor with point
    features before shared prediction layers. Learned input and feature transformations
    provide alignment modules. Rendered pages actually inspected: 3, 4.'
- evidence_id: settransformer-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/lee19d/lee19d.pdf
  locator: Sections 3.1–3.4, equations 6–16 and Figure 1, PDF pp. 3–4
  accessed_at: '2026-10-11T04:11:08Z'
  snapshot_sha256: 965aee34a80935c775156bf96c059e74a226282cbcaee69eb6f9cf6f2603525d
  support: supports
  summary: 'Stack self-attention or induced-attention blocks without positional encoding,
    then pool encoded features by attention from learned seed vectors. The induced
    variant first attends from learned inducing points to the input and then from
    the input to the resulting summaries. Rendered pages actually inspected: 3, 4.'
- evidence_id: pointnetplusplus-method
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf
  locator: Sections 3.2–3.3, Figures 2–3, PDF/printed pp. 3–5
  accessed_at: '2026-10-11T04:14:52Z'
  snapshot_sha256: 648c8a3951b89d3b27a7a5a85cacdee89673ec919da3d4aa2cbcebd03da0d811
  support: supports
  summary: 'Farthest-point sampling chooses centroids; neighborhood grouping and local-coordinate
    PointNet encoders produce features for successive abstraction levels. Multi-scale
    grouping concatenates features from different radii, while multi-resolution grouping
    combines lower-level summaries with directly encoded regional points. Rendered
    pages actually inspected: 3, 4, 5.'
- evidence_id: deepsetsplusplus-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf
  locator: Section 4 opening and Sections 4.1–4.3, Figure 2 and the DS++ block equation,
    PDF pp. 4–6
  accessed_at: '2026-10-11T04:14:52Z'
  snapshot_sha256: 9b302c6977e34aaba6dce3d6e4c173850c5a8e3ad7f381fa7c578d7c67d3a28d
  support: supports
  summary: 'Encoder blocks add an unmodified input to a transformed branch using learned
    linear maps, ReLU and set normalization. Set normalization uses a mean and variance
    over each set''s elements and feature coordinates, followed by feature-specific
    scale and bias. Rendered pages actually inspected: 5, 6.'
- evidence_id: settransformerplusplus-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf
  locator: Section 4 opening and Sections 4.1–4.2 and 4.4, Figure 2 and equations
    21–26, PDF pp. 4–6
  accessed_at: '2026-10-11T04:14:52Z'
  snapshot_sha256: 9b302c6977e34aaba6dce3d6e4c173850c5a8e3ad7f381fa7c578d7c67d3a28d
  support: supports
  summary: 'The revised encoder uses two successive attention blocks linking learned
    inducing points and input elements. Set normalization occurs on the transformed
    attention and feedforward branches, while each residual addition retains its unmodified
    query-side input. Rendered pages actually inspected: 5, 6.'
- evidence_id: implementation-scope
  kind: primary_source
  reference: https://proceedings.mlr.press/v162/zhang22ac/zhang22ac.pdf
  locator: Section 3 footnote 2, PDF p. 3; Section 4, PDF pp. 4–6
  accessed_at: '2026-10-11T04:14:52Z'
  snapshot_sha256: 9b302c6977e34aaba6dce3d6e4c173850c5a8e3ad7f381fa7c578d7c67d3a28d
  support: context_only
  summary: The later paper follows a Set Transformer implementation baseline that
    differs from the original MAB paper definition. The current records cite their
    own defining constructions without asserting identical code and paper variants.
assessments:
- assessment_id: pointnet-method
  area: evidence
  topic: Architecture identity and primary-method support
  outcome: supported
  target_ids:
  - AIMech:PointNet
  evidence_ids:
  - pointnet-method
  - identity-search
  - mapping
  summary: This is the original PointNet architecture, including its classification
    and segmentation paths. It is distinct from PointNet++'s hierarchical local grouping
    and from a generic set-pooling model.
  details: Permutation invariance of a global output and permutation equivariance
    of per-point predictions are different properties. Learned alignment modules do
    not establish exact invariance to every geometric transformation; no universal
    accuracy or robustness claim is curated.
  dimensions:
  - name: access-level
    value: full_text with rendered method inspection
    definition: Read abstracts, relevant method definitions and limitations; checked
      listed diagrams/equations visually.
    evidence_ids:
    - pointnet-method
  - name: mapping-direction
    value: broad_match to ArtificialNeuralNetwork
    definition: Shared neural feature extractors, learned transforms and neural prediction
      paths make this a specific artificial neural architecture.
    evidence_ids:
    - pointnet-method
    - mapping
- assessment_id: settransformer-method
  area: evidence
  topic: Architecture identity and primary-method support
  outcome: supported
  target_ids:
  - AIMech:SetTransformer
  evidence_ids:
  - settransformer-method
  - identity-search
  - mapping
  summary: The Set Transformer is a set-input architecture, not the AIO Transformer
    Language Model class, an individual multihead attention layer, or the later Set
    Transformer++ encoder revision.
  details: The encoder is permutation equivariant; the pooled output is invariant
    to input ordering. Multiple seed outputs are not input-element labels. Linear
    scaling with input-set size concerns a fixed number of inducing points; ordinary
    self-attention blocks have quadratic interactions. No universal benchmark superiority
    is asserted.
  dimensions:
  - name: access-level
    value: full_text with rendered method inspection
    definition: Read abstracts, relevant method definitions and limitations; checked
      listed diagrams/equations visually.
    evidence_ids:
    - settransformer-method
  - name: mapping-direction
    value: broad_match to ArtificialNeuralNetwork
    definition: The source specifies a learned neural encoder, attention pooling and
      output network. ArtificialNeuralNetwork is broader without adding a language-model
      restriction.
    evidence_ids:
    - settransformer-method
    - mapping
- assessment_id: pointnetplusplus-method
  area: evidence
  topic: Architecture identity and primary-method support
  outcome: supported
  target_ids:
  - AIMech:PointNetPlusPlus
  evidence_ids:
  - pointnetplusplus-method
  - identity-search
  - mapping
  summary: PointNet++ adds hierarchical local set abstraction to PointNet. Multi-scale
    and multi-resolution grouping are distinct variants within this architecture;
    the paper also evaluates a single-scale ablation.
  details: Neighborhood scale, sampling density and the selected grouping variant
    affect the representation; density-adaptive construction is not a guarantee for
    arbitrary missing data. The single-scale ablation, multi-scale grouping and multi-resolution
    grouping are not identical procedures. No universal benchmark advantage is curated.
  dimensions:
  - name: access-level
    value: full_text with rendered method inspection
    definition: Read abstracts, relevant method definitions and limitations; checked
      listed diagrams/equations visually.
    evidence_ids:
    - pointnetplusplus-method
  - name: mapping-direction
    value: broad_match to ArtificialNeuralNetwork
    definition: Hierarchical learned PointNet modules and prediction layers form a
      specific artificial neural architecture.
    evidence_ids:
    - pointnetplusplus-method
    - mapping
- assessment_id: deepsetsplusplus-method
  area: evidence
  topic: Architecture identity and primary-method support
  outcome: supported
  target_ids:
  - AIMech:DeepSetsPlusPlus
  evidence_ids:
  - deepsetsplusplus-method
  - identity-search
  - mapping
  summary: Deep Sets++ is the encoder revision defined by Zhang and colleagues, not
    an alternate spelling of Deep Sets or a claim that every deeper set network uses
    this construction.
  details: The written standardization assumes a nonzero denominator; this record
    does not specify numerical handling of degenerate or padded sets. The change concerns
    the encoder. Its construction does not guarantee improved training or accuracy
    for every task.
  dimensions:
  - name: access-level
    value: full_text with rendered method inspection
    definition: Read abstracts, relevant method definitions and limitations; checked
      listed diagrams/equations visually.
    evidence_ids:
    - deepsetsplusplus-method
  - name: mapping-direction
    value: broad_match to ArtificialNeuralNetwork
    definition: The source modifies learned neural encoder blocks with residual paths
      and normalization; ArtificialNeuralNetwork is the broader architecture class.
    evidence_ids:
    - deepsetsplusplus-method
    - mapping
- assessment_id: settransformerplusplus-method
  area: evidence
  topic: Architecture identity and primary-method support
  outcome: supported
  target_ids:
  - AIMech:SetTransformerPlusPlus
  evidence_ids:
  - settransformerplusplus-method
  - identity-search
  - mapping
  summary: Set Transformer++ denotes the specific encoder revision and ISAB++ construction
    in Zhang and colleagues. It is distinct from the original Set Transformer and
    from Deep Sets++ despite their shared residual and normalization design principles.
  details: This record covers the source's ISAB++ encoder construction, not all possible
    residual attention variants. Set standardization assumes a nonzero variance; no
    universal optimization or benchmark improvement is asserted.
  dimensions:
  - name: access-level
    value: full_text with rendered method inspection
    definition: Read abstracts, relevant method definitions and limitations; checked
      listed diagrams/equations visually.
    evidence_ids:
    - settransformerplusplus-method
  - name: mapping-direction
    value: broad_match to ArtificialNeuralNetwork
    definition: The revised attention encoder is a learned neural architecture; the
      broader artificial-neural-network class does not equate it with a language model
      or its component attention operation.
    evidence_ids:
    - settransformerplusplus-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  evidence_ids:
  - identity-search
  - mapping
  - pointnet-method
  - settransformer-method
  - pointnetplusplus-method
  - deepsetsplusplus-method
  - settransformerplusplus-method
  - implementation-scope
  rationale: Retain original pointwise/global PointNet, hierarchical PointNet++, attention-based
    Set Transformer and the separately defined DS++/ST++ encoder revisions. Shared
    set-input symmetry or normalization does not make these architectures equivalent.
- action: defer
  target_ids:
  - AIMech:PointNet
  - AIMech:SetTransformer
  - AIMech:PointNetPlusPlus
  - AIMech:DeepSetsPlusPlus
  - AIMech:SetTransformerPlusPlus
  evidence_ids:
  - pointnet-method
  - settransformer-method
  - pointnetplusplus-method
  - deepsetsplusplus-method
  - settransformerplusplus-method
  - implementation-scope
  rationale: Do not automatically turn every named layer or sampling component into
    a new architecture record. Resolve the independent identity and native layer representation
    of set norm, MAB/SAB/ISAB/PMA, ISAB++, grouping and alignment components before
    further additions.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261011T042136Z-plus-identity-resolved
  relationship: Separate software resolution of the reproduced plus-sign identity
    collision; scientific review of the five additions is scoped here.
limitations:
- Scientific self-review, not independent approval or experimental replication.
- PointNet alignment is learned, Set Transformer complexity depends on its block choice,
  and PointNet++ grouping variants remain distinct.
- Set norm assumes nonzero variance; no unsupported padding/degenerate-input implementation
  rule is inferred.
- Original-paper and later implementation-baseline scopes remain distinct. All five
  records remain DRAFT; discovery is ongoing.
tags:
- native-concepts
- primary-papers
- point-and-set-architectures
- self-review
- discovery-ongoing
```
