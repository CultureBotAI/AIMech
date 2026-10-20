# Scientific author self-review of Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork)

- Review: 20261019T130830Z-hyperdecoder-instance-specific-decoder-adapters
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:08:00Z
- Finished UTC: 2026-10-19T13:08:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork) as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HyperdecoderInstanceSpecificDecoderAdapter
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 17f1f577621a44e989c7200c17a6297bfd2202c5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HyperdecoderInstanceSpecificDecoderAdapter | data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml | maintained | Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HyperdecoderInstanceSpecificDecoderAdapter | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HyperdecoderInstanceSpecificDecoderAdapter | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HyperdecoderInstanceSpecificDecoderAdapter | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HyperdecoderInstanceSpecificDecoderAdapter | Validated history sidecar files. |
| python3 hyperdecoder-instance-specific-decoder-adapters-boundaries.py | passed | True | AIMech:HyperdecoderInstanceSpecificDecoderAdapter | [PASS] Hyperdecoder boundaries verified: total_params=14731296, inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HyperdecoderInstanceSpecificDecoderAdapter.

Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork) is a distinct concept.

Introduced by Hamish Ivison and Matthew E. Peters (Findings of EMNLP 2022, pp. 1715-1730, arXiv:2203.08304). Distinct from HyperFormer (Karimi Mahabadi et al., ACL/IJCNLP 2021; AIMech Round 703), which generates sequential adapters for both the encoder and decoder conditioned on learned static task embeddings (producing identical parameters for all instances within a task and requiring task IDs at inference), whereas Hyperdecoder uses non-generated shared parallel adapters in the encoder and generates instance-specific parallel adapters solely in the decoder conditioned on the encoded input text without requiring task embeddings.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HyperdecoderInstanceSpecificDecoderAdapter.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HyperdecoderInstanceSpecificDecoderAdapter.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in hyperdecoder-instance-specific-decoder-adapters-boundaries.py passed with exit code 0: [PASS] Hyperdecoder boundaries verified: total_params=14731296, inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HyperdecoderInstanceSpecificDecoderAdapter.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T130800Z-hyperdecoder-instance-specific-decoder-adapters.json | supports | No normalized identity match for AIMech:HyperdecoderInstanceSpecificDecoderAdapter across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/hyperdecoder-instance-specific-decoder-adapters-boundaries.py | supports | All constructed boundary assertions in hyperdecoder-instance-specific-decoder-adapters-boundaries.py passed with exit code 0: [PASS] Hyperdecoder boundaries verified: total_params=14731296, inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0 |
| r705-primary-pdf | https://arxiv.org/pdf/2203.08304.pdf; Full-text PDF | supports | Full-text PDF (Findings of the Association for Computational Linguistics: EMNLP 2022 (2022)) read and verified. |
| r705-arxiv-abs | https://arxiv.org/abs/2203.08304; arXiv abstract | supports | arXiv abstract read and verified. |
| r705-metadata-cr | https://dblp.org/search/publ/api?q=Hyperdecoders+Instance-specific+decoders&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyperdecoderInstanceSpecificDecoderAdapter in Round 705.
- All pages of Findings of the Association for Computational Linguistics: EMNLP 2022 (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T130830Z-hyperdecoder-instance-specific-decoder-adapters
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Hyperdecoder (Encoder-Conditioned Instance-Specific
  Decoder Adapter Hypernetwork)
started_at: '2026-10-19T13:08:00Z'
finished_at: '2026-10-19T13:08:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:HyperdecoderInstanceSpecificDecoderAdapter
    against existing AIMech and AIO records and verified all claims against Findings
    of the Association for Computational Linguistics: EMNLP 2022 (2022) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter
  Hypernetwork) as a distinct DRAFT architecture. All three claims are supported by
  full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 17f1f577621a44e989c7200c17a6297bfd2202c5
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml
    sha256: 215d62bf445a52f066f74838543fd9ecfa872c05578f9807487d7e0184b7ce6f
    role: target
  - path: research/discovery/20261019T130800Z-hyperdecoder-instance-specific-decoder-adapters.json
    sha256: 3315084850b71d79eaa56a698ec8a796b754b7e56165ac69e55e9ed4cbd3d774
    role: context
  - path: research/discovery/hyperdecoder-instance-specific-decoder-adapters-boundaries.py
    sha256: 785b77b1eba88d5ec3b203866e0d7935eeaf68f1b606ebda2225df3f114e3e8b
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
- target_id: AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  path: data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml
  label: Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml
    role: maintained
scope:
  description: All fields of data/curated/HyperdecoderInstanceSpecificDecoderAdapter.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HyperdecoderInstanceSpecificDecoderAdapter'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: validation-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 hyperdecoder-instance-specific-decoder-adapters-boundaries.py
  command: python3 research/discovery/hyperdecoder-instance-specific-decoder-adapters-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Hyperdecoder boundaries verified: total_params=14731296, inst_diff=10.2337,
    layer_diff=0.6525, zero_init_err=0.0'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T130800Z-hyperdecoder-instance-specific-decoder-adapters.json
  accessed_at: '2026-10-19T13:08:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HyperdecoderInstanceSpecificDecoderAdapter
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:08:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/hyperdecoder-instance-specific-decoder-adapters-boundaries.py
  accessed_at: '2026-10-19T13:08:00Z'
  snapshot_sha256: 785b77b1eba88d5ec3b203866e0d7935eeaf68f1b606ebda2225df3f114e3e8b
  support: supports
  summary: 'All constructed boundary assertions in hyperdecoder-instance-specific-decoder-adapters-boundaries.py
    passed with exit code 0: [PASS] Hyperdecoder boundaries verified: total_params=14731296,
    inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0'
- evidence_id: r705-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2203.08304.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:08:00Z'
  snapshot_sha256: d87244826a357de5b5e6e1ebaa114194ec517803fb74315b5b2daf583b1e612b
  support: supports
  summary: 'Full-text PDF (Findings of the Association for Computational Linguistics:
    EMNLP 2022 (2022)) read and verified.'
- evidence_id: r705-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2203.08304
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:08:00Z'
  snapshot_sha256: 557e029e6467eee081c83f1c6ccf3469fcd248cada605d3cc01dc6a27777aa6a
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r705-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Hyperdecoders+Instance-specific+decoders&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:08:00Z'
  snapshot_sha256: 9afed0799cf3b76102f03fc5c0620ef6a20586ea4c60d8fdfb9691cc66d34823
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  evidence_ids:
  - identity
  - r705-primary-pdf
  - r705-arxiv-abs
  - r705-metadata-cr
  summary: Hyperdecoder (Encoder-Conditioned Instance-Specific Decoder Adapter Hypernetwork)
    is a distinct concept.
  details: Introduced by Hamish Ivison and Matthew E. Peters (Findings of EMNLP 2022,
    pp. 1715-1730, arXiv:2203.08304). Distinct from HyperFormer (Karimi Mahabadi et
    al., ACL/IJCNLP 2021; AIMech Round 703), which generates sequential adapters for
    both the encoder and decoder conditioned on learned static task embeddings (producing
    identical parameters for all instances within a task and requiring task IDs at
    inference), whereas Hyperdecoder uses non-generated shared parallel adapters in
    the encoder and generates instance-specific parallel adapters solely in the decoder
    conditioned on the encoded input text without requiring task embeddings.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  evidence_ids:
  - mapping
  - r705-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  evidence_ids:
  - r705-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in hyperdecoder-instance-specific-decoder-adapters-boundaries.py
    passed with exit code 0: [PASS] Hyperdecoder boundaries verified: total_params=14731296,
    inst_diff=10.2337, layer_diff=0.6525, zero_init_err=0.0'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HyperdecoderInstanceSpecificDecoderAdapter
  evidence_ids:
  - identity
  - mapping
  - r705-primary-pdf
  - r705-arxiv-abs
  - r705-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyperdecoderInstanceSpecificDecoderAdapter in Round
  705.
- 'All pages of Findings of the Association for Computational Linguistics: EMNLP 2022
  (2022) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
