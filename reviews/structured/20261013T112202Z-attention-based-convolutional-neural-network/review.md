# Scientific author self-review of Attention-Based Convolutional Neural Network

- Review: 20261013T112202Z-attention-based-convolutional-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T11:15:00Z
- Finished UTC: 2026-10-13T11:22:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

ABCNN is supported as a distinct DRAFT sentence-pair architecture. Both minor citation findings are resolved by the corrected mechanism claim and Table2 locator; training and evaluation limitations remain explicit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:AttentionBasedConvolutionalNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ddc81b074ce61455a789440a8b80097a95737f0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AttentionBasedConvolutionalNeuralNetwork | data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml | maintained | Attention-Based Convolutional Neural Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 122.43s (0:02:02)<br>Checked 442 record(s); 0 failed.<br>Checked 609 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 276 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 272,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | {"bilinear_tanh": [[0.0, 0.0], [0.0, 0.9640275800758169]], "conv_alignment_shape": [7, 9], "distance_affinity": [[1.0, 0.3333333333333333], [0.5, 0.5]], "duplicated_counterpart": [5.0, 8.933333333333334], "normalized_first_window": 1.5000000000000002, "pooled_lengths": [5, 7], "row_sums": [0.8333333333333333, 0.8333333333333333, 0.7], "weighted_window_sum": [2.5, 4.466666666666667]} |

## Scientific And Domain Assessments

### Attention-Based Convolutional Neural Network

identity: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Retain this distinct DRAFT architecture.

The sentence-pair ABCNN identity is distinct from Attentive Pooling, CBAM, PointNet and visual ABC-CNN. Numbered variants1/2/3 are scoped alternatives inside this family, not interchangeable aliases or separate trained-model records.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

The declared AIO mapping is supported.

ANN is broader than the complete sentence-pair architecture; convolutional layer is a related component. The pinned Luong dot-product attention definition does not match its distance affinity. Visual DeepConvolutionalNetwork, ordinary pooling layers and OrdinalLLM do not support additional is-a mappings.

### shared-sentence-convolution

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Section3 explicitly shares the sentence CNN weights, pads pairs to common maximum length and uses wide convolution with window/global pooling. Figure3 unequal lengths are illustrative; the record does not silently equate set permutation with sequence order.

### input-attention-variant

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Equation1 and the learned W projections support reciprocal-distance input attention. Footnote1 states shared W weights. The corrected claim removes the separate Attentive Pooling mechanism assertion, so its sole primary citation supports its remaining content.

### pool-attention-and-combined-variants

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

The displayed formula uses row/column sums and weighted window sums with no probability normalization. Figure3 dimensions are consistent with s+w-1 convolutions, unlike the printed s-by-s affinity label. Duplicating fixed counterpart columns doubles the chosen pooled sums; this is an algebraic test, not a new sentence-level experiment.

### staged-training-and-feature-heads

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Section5 freezes pretrained embeddings and previously trained blocks, then fits SVM/LR to multilevel features. Table2 on p7 is the hyperparameter table; the corrected locator replaces the unrelated Table1 notation citation.

### task-specific-comparison-boundaries

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Rechecked WikiQA filtering/truncation, MSRP swapped pairs and SICK ORIG/NONOVER. Footnotes4/6/7 report feature-removal drops and non-significant MSRP improvement; Table3 also refutes a uniformly monotonic depth benefit.

### attention-and-scope-limits

evidence: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Cross-sentence feature dependence and positive affinity sums do not produce independent embeddings or normalized one-to-one alignment. The single selected Figure4 heatmap supports illustration rather than causal or general coreference proof.

### variant identity, distance-affinity shape, unnormalized pooling, feature-dependent performance and claim-specific citations

consistency: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Constructed calculations support the stated distinctions.

Chosen affinity and pooling calculations distinguish distance affinities from bilinear-tanh interactions, show that row-sum weighted pooling is not normalized averaging and can scale with duplicated counterpart columns, and check convolution/pooling dimensions. No author code, fitted model or benchmark executed.

### All maintained fields

provenance: supported. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Reread the complete corrected record and all seven mapping YAMLs after corrected capture; unchanged wider primary assessment retained with explicit timing. Removed the comparator clause lacking claim-level primary support, corrected Table2, and verified report synchronization and append-only EDIT history. Checked reciprocal affinities, unnormalized window sums, shape caveat, frozen-block training, feature removals and non-significant MSRP comparison.

## Findings

### F1: Correct ABCNN claim citation accuracy

minor / resolved / confirmed; issue key: abcnn-cross-method-evidence.

The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax Attentive Pooling Network, but its sole citation is the ABCNN paper, which does not substantiate the comparator mechanism. The comparison is supported by separately inspected native identity context, but it lacks a claim-level primary citation. Remove that unnecessary comparator sentence from the mechanism claim, retaining the independently audited identity distinction.

Disposition: Equation1 and the learned W projections support reciprocal-distance input attention. Footnote1 states shared W weights. The corrected claim removes the separate Attentive Pooling mechanism assertion, so its sole primary citation supports its remaining content.

### F2: Correct ABCNN claim citation accuracy

minor / resolved / confirmed; issue key: abcnn-training-table-locator.

The training claim cites Table 1, which is the notation table on PDFp4. Hyperparameters are in Table 2 on PDFp7. Correct the table locator; the section/page citations and training mechanism are otherwise supported.

Disposition: Section5 freezes pretrained embeddings and previously trained blocks, then fits SVM/LR to multilevel features. Table2 on p7 is the hyperparameter table; the corrected locator replaces the unrelated Table1 notation citation.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T111155Z-attention-based-convolutional-neural-network.json | supports | Compared all 442 pinned AIO and 608 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 7, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 104 AIO and 66 native definitions, with every matched definition read. 7 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. This is Yin and colleagues’ named sentence-pair ABCNN, using reciprocal-distance affinities with input-feature and pooling attention variants. It is not the bilinear/max/softmax Attentive Pooling Network, CBAM channel/spatial refinement, PointNet set pooling, ABC-CNN visual QA or every later model reusing the acronym. ABCNN-1, -2 and -3 remain explicitly different variants. |
| mapping | sources/aio/aio.json | supports | ANN is broader than the complete sentence-pair architecture; convolutional layer is a related component. The pinned Luong dot-product attention definition does not match its distance affinity. Visual DeepConvolutionalNetwork, ordinary pooling layers and OrdinalLLM do not support additional is-a mappings. |
| yin2018 | https://arxiv.org/pdf/1512.05193v4; All fourteen pages of arXiv1512.05193v4 visually read; no other versions, author implementation, training or benchmark execution. | supports | arXiv1512.05193v4,25 June2018, fourteen PDF pages. All pages visually read, including equations, diagrams, tables, footnotes and references. Locators use PDF page order. Other versions and author code not inspected. |
| calculation | research/discovery/abcnn-boundaries.py | supports | Chosen affinity and pooling calculations distinguish distance affinities from bilinear-tanh interactions, show that row-sum weighted pooling is not normalized averaging and can scale with duplicated counterpart columns, and check convolution/pooling dimensions. No author code, fitted model or benchmark executed. |
| predecessor | reviews/structured/20261013T111356Z-abcnn-citation-findings/review.yaml | supports | Immutable initial review records both minor citation findings. |
| corrected-record | data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml | supports | Complete corrected record, synchronized report and EDIT history inspected; affected primary passages reread after recapture. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 609 native and 442 unchanged generated records. The 793-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All fourteen pages of arXiv1512.05193v4 visually inspected. Author code and other versions not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T112202Z-attention-based-convolutional-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Attention-Based Convolutional Neural Network
started_at: '2026-10-13T11:15:00Z'
finished_at: '2026-10-13T11:22:02Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged variant identity, distance-affinity shape,
    unnormalized pooling, feature-dependent performance and claim-specific citations.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: ABCNN is supported as a distinct DRAFT sentence-pair architecture. Both minor
  citation findings are resolved by the corrected mechanism claim and Table2 locator;
  training and evaluation limitations remain explicit.
source:
  git_revision: 1ddc81b074ce61455a789440a8b80097a95737f0
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/AttentionLayer.yaml
    sha256: ace47f724bab8a1aec9f963f7d8121f148134e5bbcce7c23a3a1f62c9c83619b
    role: context
  - path: data/aio/AveragePooling1DLayer.yaml
    sha256: 2c78ecf6ef4bf7c25befcde55b4df86d12082e39f84eeb5242a8c6278216659e
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/DeepConvolutionalNetwork.yaml
    sha256: b2be73a895ae3890ca0ba464c1d0de55e41960f33ec53dcab4547abfe1159c62
    role: context
  - path: data/aio/OrdinalLLM.yaml
    sha256: 2bbb482a7007dd95f6e644863e264f646f7cc40e3debc05273bdb7ac96160d4b
    role: context
  - path: data/aio/PoolingLayer.yaml
    sha256: 2a5cc182b52109a337a926a42bd715d5f1142e2a0876a8bfbc41890846e84246
    role: context
  - path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    sha256: 115dae9f922226484a13491b1428c066ae6e996c1dc1b1f16025d6438fcf4ebe
    role: target
  - path: data/curated/AttentivePoolingNetwork.yaml
    sha256: c2c9abe6d2c5f19926cca4cf6a06203bd6c3f285cf7558fd56983d278aded52d
    role: context
  - path: data/curated/ConvolutionalBlockAttentionModule.yaml
    sha256: ece8d0432112916c5f158b484b24e6f316a9c3edfe07233fefeae5b454a96b96
    role: context
  - path: data/curated/PointNet.yaml
    sha256: b2292a45d360ee989f143838b4ca9008033e69d63c5b578e7e2ab45fb6ee80dd
    role: context
  - path: research/discovery/20261013T111155Z-attention-based-convolutional-neural-network.json
    sha256: 113b877a7a4ffae7466f6e374053144405ae39d0778c22fcef5ea63361fe1a19
    role: context
  - path: research/discovery/abcnn-boundaries.py
    sha256: 31e5f0296bb5e1110e0a23a56fa6f2509d6cda446b55a31c5a04ced5208f1987
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
- target_id: AIMech:AttentionBasedConvolutionalNeuralNetwork
  path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
  label: Attention-Based Convolutional Neural Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:AttentionBasedConvolutionalNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All fourteen pages of arXiv1512.05193v4 visually read; no other versions,
      author implementation, training or benchmark execution.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 122.43s (0:02:02)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 609 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 276 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 272,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
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
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
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
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/abcnn-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"bilinear_tanh": [[0.0, 0.0], [0.0, 0.9640275800758169]], "conv_alignment_shape":
    [7, 9], "distance_affinity": [[1.0, 0.3333333333333333], [0.5, 0.5]], "duplicated_counterpart":
    [5.0, 8.933333333333334], "normalized_first_window": 1.5000000000000002, "pooled_lengths":
    [5, 7], "row_sums": [0.8333333333333333, 0.8333333333333333, 0.7], "weighted_window_sum":
    [2.5, 4.466666666666667]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T111155Z-attention-based-convolutional-neural-network.json
  accessed_at: '2026-10-13T11:15:00Z'
  support: supports
  summary: Compared all 442 pinned AIO and 608 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    7, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    104 AIO and 66 native definitions, with every matched definition read. 7 full
    annotated AIO node/edge/generated contexts and 3 full native records were inspected.
    This is Yin and colleagues’ named sentence-pair ABCNN, using reciprocal-distance
    affinities with input-feature and pooling attention variants. It is not the bilinear/max/softmax
    Attentive Pooling Network, CBAM channel/spatial refinement, PointNet set pooling,
    ABC-CNN visual QA or every later model reusing the acronym. ABCNN-1, -2 and -3
    remain explicitly different variants.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T11:15:00Z'
  support: supports
  summary: ANN is broader than the complete sentence-pair architecture; convolutional
    layer is a related component. The pinned Luong dot-product attention definition
    does not match its distance affinity. Visual DeepConvolutionalNetwork, ordinary
    pooling layers and OrdinalLLM do not support additional is-a mappings.
- evidence_id: yin2018
  kind: primary_source
  reference: https://arxiv.org/pdf/1512.05193v4
  locator: All fourteen pages of arXiv1512.05193v4 visually read; no other versions,
    author implementation, training or benchmark execution.
  accessed_at: '2026-10-13T10:40:35Z'
  snapshot_sha256: 46b9425267ae1c454af3708c0c52837aeadb341e1cbfc8fc39315febd5f43e3d
  support: supports
  summary: arXiv1512.05193v4,25 June2018, fourteen PDF pages. All pages visually read,
    including equations, diagrams, tables, footnotes and references. Locators use
    PDF page order. Other versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/abcnn-boundaries.py
  accessed_at: '2026-10-13T11:16:53Z'
  snapshot_sha256: 31e5f0296bb5e1110e0a23a56fa6f2509d6cda446b55a31c5a04ced5208f1987
  support: supports
  summary: Chosen affinity and pooling calculations distinguish distance affinities
    from bilinear-tanh interactions, show that row-sum weighted pooling is not normalized
    averaging and can scale with duplicated counterpart columns, and check convolution/pooling
    dimensions. No author code, fitted model or benchmark executed.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T111356Z-abcnn-citation-findings/review.yaml
  accessed_at: '2026-10-13T11:16:53Z'
  support: supports
  summary: Immutable initial review records both minor citation findings.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
  accessed_at: '2026-10-13T11:16:53Z'
  snapshot_sha256: 115dae9f922226484a13491b1428c066ae6e996c1dc1b1f16025d6438fcf4ebe
  support: supports
  summary: Complete corrected record, synchronized report and EDIT history inspected;
    affected primary passages reread after recapture.
assessments:
- assessment_id: identity
  area: identity
  topic: Attention-Based Convolutional Neural Network
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - identity
  - yin2018
  summary: Retain this distinct DRAFT architecture.
  details: The sentence-pair ABCNN identity is distinct from Attentive Pooling, CBAM,
    PointNet and visual ABC-CNN. Numbered variants1/2/3 are scoped alternatives inside
    this family, not interchangeable aliases or separate trained-model records.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - mapping
  - yin2018
  summary: The declared AIO mapping is supported.
  details: ANN is broader than the complete sentence-pair architecture; convolutional
    layer is a related component. The pinned Luong dot-product attention definition
    does not match its distance affinity. Visual DeepConvolutionalNetwork, ordinary
    pooling layers and OrdinalLLM do not support additional is-a mappings.
- assessment_id: shared-sentence-convolution
  area: evidence
  topic: shared-sentence-convolution
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3 explicitly shares the sentence CNN weights, pads pairs to common
    maximum length and uses wide convolution with window/global pooling. Figure3 unequal
    lengths are illustrative; the record does not silently equate set permutation
    with sequence order.
- assessment_id: input-attention-variant
  area: evidence
  topic: input-attention-variant
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation1 and the learned W projections support reciprocal-distance input
    attention. Footnote1 states shared W weights. The corrected claim removes the
    separate Attentive Pooling mechanism assertion, so its sole primary citation supports
    its remaining content.
- assessment_id: pool-attention-and-combined-variants
  area: evidence
  topic: pool-attention-and-combined-variants
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The displayed formula uses row/column sums and weighted window sums with
    no probability normalization. Figure3 dimensions are consistent with s+w-1 convolutions,
    unlike the printed s-by-s affinity label. Duplicating fixed counterpart columns
    doubles the chosen pooled sums; this is an algebraic test, not a new sentence-level
    experiment.
- assessment_id: staged-training-and-feature-heads
  area: evidence
  topic: staged-training-and-feature-heads
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section5 freezes pretrained embeddings and previously trained blocks, then
    fits SVM/LR to multilevel features. Table2 on p7 is the hyperparameter table;
    the corrected locator replaces the unrelated Table1 notation citation.
- assessment_id: task-specific-comparison-boundaries
  area: evidence
  topic: task-specific-comparison-boundaries
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rechecked WikiQA filtering/truncation, MSRP swapped pairs and SICK ORIG/NONOVER.
    Footnotes4/6/7 report feature-removal drops and non-significant MSRP improvement;
    Table3 also refutes a uniformly monotonic depth benefit.
- assessment_id: attention-and-scope-limits
  area: evidence
  topic: attention-and-scope-limits
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Cross-sentence feature dependence and positive affinity sums do not produce
    independent embeddings or normalized one-to-one alignment. The single selected
    Figure4 heatmap supports illustration rather than causal or general coreference
    proof.
- assessment_id: constructed-boundaries
  area: consistency
  topic: variant identity, distance-affinity shape, unnormalized pooling, feature-dependent
    performance and claim-specific citations
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - yin2018
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen affinity and pooling calculations distinguish distance affinities
    from bilinear-tanh interactions, show that row-sum weighted pooling is not normalized
    averaging and can scale with duplicated counterpart columns, and check convolution/pooling
    dimensions. No author code, fitted model or benchmark executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - yin2018
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Reread the complete corrected record and all seven
    mapping YAMLs after corrected capture; unchanged wider primary assessment retained
    with explicit timing. Removed the comparator clause lacking claim-level primary
    support, corrected Table2, and verified report synchronization and append-only
    EDIT history. Checked reciprocal affinities, unnormalized window sums, shape caveat,
    frozen-block training, feature removals and non-significant MSRP comparison.
findings:
- finding_id: F1
  issue_key: abcnn-cross-method-evidence
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct ABCNN claim citation accuracy
  description: The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax
    Attentive Pooling Network, but its sole citation is the ABCNN paper, which does
    not substantiate the comparator mechanism. The comparison is supported by separately
    inspected native identity context, but it lacks a claim-level primary citation.
    Remove that unnecessary comparator sentence from the mechanism claim, retaining
    the independently audited identity distinction.
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  field_paths:
  - claims[claim_id=input-attention-variant].statement
  evidence_ids:
  - yin2018
  - corrected-record
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/267
  disposition_reason: Equation1 and the learned W projections support reciprocal-distance
    input attention. Footnote1 states shared W weights. The corrected claim removes
    the separate Attentive Pooling mechanism assertion, so its sole primary citation
    supports its remaining content.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T111356Z-abcnn-citation-findings
    finding_id: F1
- finding_id: F2
  issue_key: abcnn-training-table-locator
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct ABCNN claim citation accuracy
  description: The training claim cites Table 1, which is the notation table on PDFp4.
    Hyperparameters are in Table 2 on PDFp7. Correct the table locator; the section/page
    citations and training mechanism are otherwise supported.
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  field_paths:
  - claims[claim_id=staged-training-and-feature-heads].evidence
  evidence_ids:
  - yin2018
  - corrected-record
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/267
  disposition_reason: Section5 freezes pretrained embeddings and previously trained
    blocks, then fits SVM/LR to multilevel features. Table2 on p7 is the hyperparameter
    table; the corrected locator replaces the unrelated Table1 notation citation.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T111356Z-abcnn-citation-findings
    finding_id: F2
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 609 native and 442 unchanged generated records.
  The 793-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All fourteen pages of arXiv1512.05193v4 visually inspected. Author code and other
  versions not inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T111356Z-abcnn-citation-findings
  relationship: Resolves both explicitly linked citation findings for this record.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
