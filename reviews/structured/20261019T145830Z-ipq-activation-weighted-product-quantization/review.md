# Scientific author self-review of Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ)

- Review: 20261019T145830Z-ipq-activation-weighted-product-quantization
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:58:00Z
- Finished UTC: 2026-10-19T14:58:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 59802cc35cfdf020d41943a7145550fd34c5a493.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml | maintained | Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | Validated history sidecar files. |
| python3 ipq-activation-weighted-product-quantization-boundaries.py | passed | True | AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks | iPQ verification passed: act_err_act=0.0558 &lt;&lt; act_err_std=13.1130, idx_bytes=16384, cb_bytes=4608 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.

Iterative Product Quantization for Neural Networks (And the Bit Goes Down / Activation-Weighted PQ) is a distinct concept.

Distinct from classical weight-space Product Quantization (Gong et al., 2014), which minimizes Frobenius weight error &#124;&#124;W - W_hat&#124;&#124;_2^2 (Eq. 1) and suffers catastrophic accuracy drift across deep layers, and distinct from Quant-Noise (AIMech:QuantNoiseTrainingWithQuantizationNoiseForExtremeCompression), which applies quantization noise to random weight blocks during training to preserve unbiased gradient flow.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in ipq-activation-weighted-product-quantization-boundaries.py passed with exit code 0: iPQ verification passed: act_err_act=0.0558 &lt;&lt; act_err_std=13.1130, idx_bytes=16384, cb_bytes=4608

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T145800Z-ipq-activation-weighted-product-quantization.json | supports | No normalized identity match for AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/ipq-activation-weighted-product-quantization-boundaries.py | supports | All constructed boundary assertions in ipq-activation-weighted-product-quantization-boundaries.py passed with exit code 0: iPQ verification passed: act_err_act=0.0558 &lt;&lt; act_err_std=13.1130, idx_bytes=16384, cb_bytes=4608 |
| r815-primary-pdf | https://arxiv.org/pdf/1907.05686; Full-text PDF | supports | Full-text PDF (ICLR 2020 (2020)) read and verified. |
| r815-arxiv-abs | https://arxiv.org/abs/1907.05686; arXiv abstract | supports | arXiv abstract read and verified. |
| r815-metadata-cr | https://arxiv.org/bibtex/1907.05686; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks in Round 815.
- All pages of ICLR 2020 (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T145830Z-ipq-activation-weighted-product-quantization
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Iterative Product Quantization for Neural
  Networks (And the Bit Goes Down / Activation-Weighted PQ)
started_at: '2026-10-19T14:58:00Z'
finished_at: '2026-10-19T14:58:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
    against existing AIMech and AIO records and verified all claims against ICLR 2020
    (2020) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Iterative Product Quantization for Neural Networks (And the Bit Goes
  Down / Activation-Weighted PQ) as a distinct DRAFT algorithm. All three claims are
  supported by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 59802cc35cfdf020d41943a7145550fd34c5a493
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml
    sha256: ef1d10320f5ed45da11aa7270c31787bc1cfe0f18a42050301eab8faf7a99b74
    role: target
  - path: research/discovery/20261019T145800Z-ipq-activation-weighted-product-quantization.json
    sha256: f73bb9b1bc060e61262093d8e2a3252791838dfdb6a3efc35cf6801806545213
    role: context
  - path: research/discovery/ipq-activation-weighted-product-quantization-boundaries.py
    sha256: 527bd3dbae74b4e7838cb71b7b0142be8e08a288a391b9303b990c43b35ffd88
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
- target_id: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  path: data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml
  label: Iterative Product Quantization for Neural Networks (And the Bit Goes Down
    / Activation-Weighted PQ)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml
    role: maintained
scope:
  description: All fields of data/curated/AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
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
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 ipq-activation-weighted-product-quantization-boundaries.py
  command: python3 research/discovery/ipq-activation-weighted-product-quantization-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  exit_code: 0
  expected_exit_code: 0
  summary: 'iPQ verification passed: act_err_act=0.0558 << act_err_std=13.1130, idx_bytes=16384,
    cb_bytes=4608'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T145800Z-ipq-activation-weighted-product-quantization.json
  accessed_at: '2026-10-19T14:58:00Z'
  support: supports
  summary: No normalized identity match for AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:58:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/ipq-activation-weighted-product-quantization-boundaries.py
  accessed_at: '2026-10-19T14:58:00Z'
  snapshot_sha256: 527bd3dbae74b4e7838cb71b7b0142be8e08a288a391b9303b990c43b35ffd88
  support: supports
  summary: 'All constructed boundary assertions in ipq-activation-weighted-product-quantization-boundaries.py
    passed with exit code 0: iPQ verification passed: act_err_act=0.0558 << act_err_std=13.1130,
    idx_bytes=16384, cb_bytes=4608'
- evidence_id: r815-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1907.05686
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:58:00Z'
  snapshot_sha256: 4e5462e5d02519de37dc4f019d0a68b4aeb01e0e3b8b40c0289702dccd568a1c
  support: supports
  summary: Full-text PDF (ICLR 2020 (2020)) read and verified.
- evidence_id: r815-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1907.05686
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:58:00Z'
  snapshot_sha256: 1c62969616244b29903fd900535cd7b92fbda6a649f585d08a599559cd933d57
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r815-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/1907.05686
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:58:00Z'
  snapshot_sha256: e3feb828eafea5f1e335b1be41de8afec3c850c4a8d1074b1d5722605122cb9d
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  evidence_ids:
  - identity
  - r815-primary-pdf
  - r815-arxiv-abs
  - r815-metadata-cr
  summary: Iterative Product Quantization for Neural Networks (And the Bit Goes Down
    / Activation-Weighted PQ) is a distinct concept.
  details: Distinct from classical weight-space Product Quantization (Gong et al.,
    2014), which minimizes Frobenius weight error ||W - W_hat||_2^2 (Eq. 1) and suffers
    catastrophic accuracy drift across deep layers, and distinct from Quant-Noise
    (AIMech:QuantNoiseTrainingWithQuantizationNoiseForExtremeCompression), which applies
    quantization noise to random weight blocks during training to preserve unbiased
    gradient flow.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  evidence_ids:
  - mapping
  - r815-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  evidence_ids:
  - r815-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in ipq-activation-weighted-product-quantization-boundaries.py
    passed with exit code 0: iPQ verification passed: act_err_act=0.0558 << act_err_std=13.1130,
    idx_bytes=16384, cb_bytes=4608'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  evidence_ids:
  - identity
  - mapping
  - r815-primary-pdf
  - r815-arxiv-abs
  - r815-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:AndTheBitGoesDownIterativeProductQuantizationForNeuralNetworks
  in Round 815.
- All pages of ICLR 2020 (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
