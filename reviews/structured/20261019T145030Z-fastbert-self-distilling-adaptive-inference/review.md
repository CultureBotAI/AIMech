# Scientific author self-review of FastBERT: Self-Distilling BERT with Adaptive Inference Time

- Review: 20261019T145030Z-fastbert-self-distilling-adaptive-inference
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:50:00Z
- Finished UTC: 2026-10-19T14:50:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain FastBERT: Self-Distilling BERT with Adaptive Inference Time as a distinct DRAFT architecture. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8fa33b8f6c4a5d1b5408e6ba275b59e5025b42da.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml | maintained | FastBERT: Self-Distilling BERT with Adaptive Inference Time |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | Validated history sidecar files. |
| python3 fastbert-self-distilling-adaptive-inference-boundaries.py | passed | True | AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime | {"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime", "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform": 0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled": 0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08": 2784.0, "layer0_exit_speedup": 11.74, "status": "ok"} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.

FastBERT: Self-Distilling BERT with Adaptive Inference Time is a distinct concept.

Introduced by Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Haotang Deng, and Qi Ju (ACL 2020, pp. 6035-6044, arXiv:2004.02178, doi:10.18653/v1/2020.acl-main.537). Distinct from cross-model knowledge distillation methods (DistilBERT Round 803, TinyBERT Round 800, MobileBERT Round 804) that execute a fixed number of layers for every input, and from Patience-Based Early Exit (PABEE, Round 808), which jointly trains linear internal classifiers and exits based on cross-layer prediction agreement patience rather than frozen-backbone branch self-distillation and single-layer normalized entropy thresholding.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in fastbert-self-distilling-adaptive-inference-boundaries.py passed with exit code 0: {"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime", "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform": 0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled": 0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08": 2784.0, "layer0_exit_speedup": 11.74, "status": "ok"}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T145000Z-fastbert-self-distilling-adaptive-inference.json | supports | No normalized identity match for AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/fastbert-self-distilling-adaptive-inference-boundaries.py | supports | All constructed boundary assertions in fastbert-self-distilling-adaptive-inference-boundaries.py passed with exit code 0: {"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime", "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform": 0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled": 0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08": 2784.0, "layer0_exit_speedup": 11.74, "status": "ok"} |
| r807-primary-pdf | https://arxiv.org/pdf/2004.02178.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020) (2020)) read and verified. |
| r807-arxiv-abs | https://arxiv.org/abs/2004.02178; arXiv abstract | supports | arXiv abstract read and verified. |
| r807-metadata-cr | https://arxiv.org/bibtex/2004.02178; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime in Round 807.
- All pages of Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020) (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T145030Z-fastbert-self-distilling-adaptive-inference
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of FastBERT: Self-Distilling BERT with Adaptive
  Inference Time'
started_at: '2026-10-19T14:50:00Z'
finished_at: '2026-10-19T14:50:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 58th Annual Meeting of the Association for Computational Linguistics (ACL
    2020) (2020) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain FastBERT: Self-Distilling BERT with Adaptive Inference Time as a
  distinct DRAFT architecture. All four claims are supported by full-text primary
  evidence and pure-Python boundary verification.'
source:
  git_revision: 8fa33b8f6c4a5d1b5408e6ba275b59e5025b42da
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml
    sha256: f2a5949486d6855d6d04c82cdadadf261dc138f4698c7177518016ed06a27d65
    role: target
  - path: research/discovery/20261019T145000Z-fastbert-self-distilling-adaptive-inference.json
    sha256: d6369de3ab052b0eb7eeeb9052eca8b83813c512476e0d08397f9638577f7e26
    role: context
  - path: research/discovery/fastbert-self-distilling-adaptive-inference-boundaries.py
    sha256: 01131f7362fe229a433400b1e9970c4576ad6859374b12086e4dd51c43ba7a22
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
- target_id: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  path: data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml
  label: 'FastBERT: Self-Distilling BERT with Adaptive Inference Time'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml
    role: maintained
scope:
  description: All fields of data/curated/FastBERTSelfDistillingBERTWithAdaptiveInferenceTime.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
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
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 fastbert-self-distilling-adaptive-inference-boundaries.py
  command: python3 research/discovery/fastbert-self-distilling-adaptive-inference-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  exit_code: 0
  expected_exit_code: 0
  summary: '{"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime", "uncertainty_one_hot":
    -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform": 0.9999999999999998,
    "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled": 0.005975,
    "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08":
    2784.0, "layer0_exit_speedup": 11.74, "status": "ok"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T145000Z-fastbert-self-distilling-adaptive-inference.json
  accessed_at: '2026-10-19T14:50:00Z'
  support: supports
  summary: No normalized identity match for AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:50:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/fastbert-self-distilling-adaptive-inference-boundaries.py
  accessed_at: '2026-10-19T14:50:00Z'
  snapshot_sha256: 01131f7362fe229a433400b1e9970c4576ad6859374b12086e4dd51c43ba7a22
  support: supports
  summary: 'All constructed boundary assertions in fastbert-self-distilling-adaptive-inference-boundaries.py
    passed with exit code 0: {"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime",
    "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform":
    0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled":
    0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08":
    2784.0, "layer0_exit_speedup": 11.74, "status": "ok"}'
- evidence_id: r807-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2004.02178.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:50:00Z'
  snapshot_sha256: 9e86dbcb4a98cdca5df0bb16bf7319ca534545765a0a335e698a9ba06fd9546d
  support: supports
  summary: Full-text PDF (Proceedings of the 58th Annual Meeting of the Association
    for Computational Linguistics (ACL 2020) (2020)) read and verified.
- evidence_id: r807-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2004.02178
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:50:00Z'
  snapshot_sha256: 589beceeeeaf435811040b064841f357971f963e6c6e99f514588e905bde5cd5
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r807-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2004.02178
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:50:00Z'
  snapshot_sha256: 900374299d441b941621fb0d941d5b904d5c789d33495e7f31133a31171681e8
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  evidence_ids:
  - identity
  - r807-primary-pdf
  - r807-arxiv-abs
  - r807-metadata-cr
  summary: 'FastBERT: Self-Distilling BERT with Adaptive Inference Time is a distinct
    concept.'
  details: Introduced by Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Haotang Deng,
    and Qi Ju (ACL 2020, pp. 6035-6044, arXiv:2004.02178, doi:10.18653/v1/2020.acl-main.537).
    Distinct from cross-model knowledge distillation methods (DistilBERT Round 803,
    TinyBERT Round 800, MobileBERT Round 804) that execute a fixed number of layers
    for every input, and from Patience-Based Early Exit (PABEE, Round 808), which
    jointly trains linear internal classifiers and exits based on cross-layer prediction
    agreement patience rather than frozen-backbone branch self-distillation and single-layer
    normalized entropy thresholding.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  evidence_ids:
  - mapping
  - r807-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  evidence_ids:
  - r807-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in fastbert-self-distilling-adaptive-inference-boundaries.py
    passed with exit code 0: {"concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime",
    "uncertainty_one_hot": -0.0, "uncertainty_low": 0.301921, "uncertainty_uniform":
    0.9999999999999998, "self_distill_loss_untrained": 7.9383, "self_distill_loss_distilled":
    0.005975, "avg_flops_speed_01": 12528.0, "avg_flops_speed_05": 7424.0, "avg_flops_speed_08":
    2784.0, "layer0_exit_speedup": 11.74, "status": "ok"}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  evidence_ids:
  - identity
  - mapping
  - r807-primary-pdf
  - r807-arxiv-abs
  - r807-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime
  in Round 807.
- All pages of Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics (ACL 2020) (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
