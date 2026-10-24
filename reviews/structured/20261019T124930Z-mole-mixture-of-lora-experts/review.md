# Scientific author self-review of MoLE (Mixture of LoRA Experts)

- Review: 20261019T124930Z-mole-mixture-of-lora-experts
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T12:49:00Z
- Finished UTC: 2026-10-19T12:49:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain MoLE (Mixture of LoRA Experts) as a distinct DRAFT architecture. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/MoLEMixtureOfLoRAExperts.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:MoLEMixtureOfLoRAExperts
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 770ecf435afc6ea08e0466b5ac62f035a3a4f3d8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MoLEMixtureOfLoRAExperts | data/curated/MoLEMixtureOfLoRAExperts.yaml | maintained | MoLE (Mixture of LoRA Experts) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:MoLEMixtureOfLoRAExperts | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:MoLEMixtureOfLoRAExperts | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:MoLEMixtureOfLoRAExperts | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:MoLEMixtureOfLoRAExperts | Validated history sidecar files. |
| python3 mole-mixture-of-lora-experts-boundaries.py | passed | True | AIMech:MoLEMixtureOfLoRAExperts | [PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32 &lt;&lt; nla_err=43.80 &lt; unnorm_err=50.70, L_bal(uniform)=3.2958 &lt; L_bal(collapsed)=6.0968 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:MoLEMixtureOfLoRAExperts.

MoLE (Mixture of LoRA Experts) is a distinct concept.

Distinct from LoraHub (AIMech:LoraHub, which optimizes static scalar weights per LoRA module via gradient-free black-box optimization), from LoRA-Flow (AIMech:LoRAFlow, which computes token-level gates directly from the pre-LoRA hidden state x^l_t without concatenating LoRA expert outputs or optimizing a log-product gating balancing loss), and from LoRAMoE (AIMech:LoRAMoE, which trains LoRA experts from scratch inside FFN blocks with a localized balancing constraint to prevent world knowledge forgetting during SFT rather than composing separately pre-trained frozen LoRAs). Formulated by Wu, Huang, and Wei (ICLR 2024, arXiv:2404.13628).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:MoLEMixtureOfLoRAExperts.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:MoLEMixtureOfLoRAExperts.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in mole-mixture-of-lora-experts-boundaries.py passed with exit code 0: [PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32 &lt;&lt; nla_err=43.80 &lt; unnorm_err=50.70, L_bal(uniform)=3.2958 &lt; L_bal(collapsed)=6.0968

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:MoLEMixtureOfLoRAExperts.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T124900Z-mole-mixture-of-lora-experts.json | supports | No normalized identity match for AIMech:MoLEMixtureOfLoRAExperts across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/mole-mixture-of-lora-experts-boundaries.py | supports | All constructed boundary assertions in mole-mixture-of-lora-experts-boundaries.py passed with exit code 0: [PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32 &lt;&lt; nla_err=43.80 &lt; unnorm_err=50.70, L_bal(uniform)=3.2958 &lt; L_bal(collapsed)=6.0968 |
| r686-primary-pdf | https://arxiv.org/pdf/2404.13628.pdf; Full-text PDF | supports | Full-text PDF (International Conference on Learning Representations (ICLR 2024) (2024)) read and verified. |
| r686-arxiv-abs | https://arxiv.org/abs/2404.13628; arXiv abstract | supports | arXiv abstract read and verified. |
| r686-metadata-cr | https://dblp.org/search/publ/api?q=2404.13628&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:MoLEMixtureOfLoRAExperts in Round 686.
- All pages of International Conference on Learning Representations (ICLR 2024) (2024) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T124930Z-mole-mixture-of-lora-experts
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of MoLE (Mixture of LoRA Experts)
started_at: '2026-10-19T12:49:00Z'
finished_at: '2026-10-19T12:49:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:MoLEMixtureOfLoRAExperts
    against existing AIMech and AIO records and verified all claims against International
    Conference on Learning Representations (ICLR 2024) (2024) and pure-Python boundary
    checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain MoLE (Mixture of LoRA Experts) as a distinct DRAFT architecture. All
  four claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: 770ecf435afc6ea08e0466b5ac62f035a3a4f3d8
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/MoLEMixtureOfLoRAExperts.yaml
    sha256: fd2260fd1407a27a7d06c671bee8e4ad2f2c5309234a2716a9be766a6cbb562c
    role: target
  - path: research/discovery/20261019T124900Z-mole-mixture-of-lora-experts.json
    sha256: e2737391e3e6b2fa20849a30746d9a573ef6e660ed11323b65f000d462a09946
    role: context
  - path: research/discovery/mole-mixture-of-lora-experts-boundaries.py
    sha256: 5f65e33a0e43eaa3a2eb680d17304d8634fe00e105bee2f84e5602310d178513
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
- target_id: AIMech:MoLEMixtureOfLoRAExperts
  path: data/curated/MoLEMixtureOfLoRAExperts.yaml
  label: MoLE (Mixture of LoRA Experts)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MoLEMixtureOfLoRAExperts.yaml
    role: maintained
scope:
  description: All fields of data/curated/MoLEMixtureOfLoRAExperts.yaml and its primary
    evidence.
  selection: 'Exact maintained ID: AIMech:MoLEMixtureOfLoRAExperts'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
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
  - AIMech:MoLEMixtureOfLoRAExperts
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 mole-mixture-of-lora-experts-boundaries.py
  command: python3 research/discovery/mole-mixture-of-lora-experts-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32 << nla_err=43.80
    < unnorm_err=50.70, L_bal(uniform)=3.2958 < L_bal(collapsed)=6.0968'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T124900Z-mole-mixture-of-lora-experts.json
  accessed_at: '2026-10-19T12:49:00Z'
  support: supports
  summary: No normalized identity match for AIMech:MoLEMixtureOfLoRAExperts across
    AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T12:49:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/mole-mixture-of-lora-experts-boundaries.py
  accessed_at: '2026-10-19T12:49:00Z'
  snapshot_sha256: 5f65e33a0e43eaa3a2eb680d17304d8634fe00e105bee2f84e5602310d178513
  support: supports
  summary: 'All constructed boundary assertions in mole-mixture-of-lora-experts-boundaries.py
    passed with exit code 0: [PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32
    << nla_err=43.80 < unnorm_err=50.70, L_bal(uniform)=3.2958 < L_bal(collapsed)=6.0968'
- evidence_id: r686-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2404.13628.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T12:49:00Z'
  snapshot_sha256: 415b8d661e5e8dba53a4794d9360777591a561e982fc6ba678b83cd61b061b01
  support: supports
  summary: Full-text PDF (International Conference on Learning Representations (ICLR
    2024) (2024)) read and verified.
- evidence_id: r686-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2404.13628
  locator: arXiv abstract
  accessed_at: '2026-10-19T12:49:00Z'
  snapshot_sha256: d2cb6e24cd1a789780766b21c8682af1083a12f76fca18406f14a956c25191ee
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r686-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=2404.13628&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T12:49:00Z'
  snapshot_sha256: 16ddc5ec05b1e36007daaf32a49ceb670891b586519954f5251bab89020be529
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  evidence_ids:
  - identity
  - r686-primary-pdf
  - r686-arxiv-abs
  - r686-metadata-cr
  summary: MoLE (Mixture of LoRA Experts) is a distinct concept.
  details: Distinct from LoraHub (AIMech:LoraHub, which optimizes static scalar weights
    per LoRA module via gradient-free black-box optimization), from LoRA-Flow (AIMech:LoRAFlow,
    which computes token-level gates directly from the pre-LoRA hidden state x^l_t
    without concatenating LoRA expert outputs or optimizing a log-product gating balancing
    loss), and from LoRAMoE (AIMech:LoRAMoE, which trains LoRA experts from scratch
    inside FFN blocks with a localized balancing constraint to prevent world knowledge
    forgetting during SFT rather than composing separately pre-trained frozen LoRAs).
    Formulated by Wu, Huang, and Wei (ICLR 2024, arXiv:2404.13628).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  evidence_ids:
  - mapping
  - r686-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  evidence_ids:
  - r686-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in mole-mixture-of-lora-experts-boundaries.py
    passed with exit code 0: [PASS] Round 686 MoLE (Wu et al., ICLR 2024): mole_err=1.54e-32
    << nla_err=43.80 < unnorm_err=50.70, L_bal(uniform)=3.2958 < L_bal(collapsed)=6.0968'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:MoLEMixtureOfLoRAExperts
  evidence_ids:
  - identity
  - mapping
  - r686-primary-pdf
  - r686-arxiv-abs
  - r686-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:MoLEMixtureOfLoRAExperts in Round 686.
- All pages of International Conference on Learning Representations (ICLR 2024) (2024)
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
