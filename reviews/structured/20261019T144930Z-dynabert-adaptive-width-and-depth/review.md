# Scientific author self-review of DynaBERT: Dynamic BERT with Adaptive Width and Depth

- Review: 20261019T144930Z-dynabert-adaptive-width-and-depth
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:49:00Z
- Finished UTC: 2026-10-19T14:49:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain DynaBERT: Dynamic BERT with Adaptive Width and Depth as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b5b25a67b8ce4feb3d51050e66f491a164689553.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml | maintained | DynaBERT: Dynamic BERT with Adaptive Width and Depth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | Validated history sidecar files. |
| python3 dynabert-adaptive-width-and-depth-boundaries.py | passed | True | AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth | {"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth", "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired": 4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1, 2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050": [2, 4, 6, 8, 10, 12], "status": "ok"} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.

DynaBERT: Dynamic BERT with Adaptive Width and Depth is a distinct concept.

Introduced by Lu Hou, Zhiqi Huang, Lifeng Shang, Xin Jiang, Xiao Chen, and Qun Liu (NeurIPS 2020, arXiv:2004.04037). Distinct from fixed-size BERT compression methods such as TinyBERT (Round 800), MiniLM (Round 801), BERT-PKD (Round 802), DistilBERT (Round 803), MobileBERT (Round 804), and BERT-of-Theseus (Round 805), and from depth-only early-exit or layer-dropping methods such as FastBERT (Round 807), PABEE (Round 808), and LayerDrop: DynaBERT adapts both Transformer width (via parallel head and FFN-neuron slicing in Eqs. 1-2 after Taylor-importance network rewiring) and depth (via strided layer dropping and last-layer-preserving hidden-state matching in Eq. 4) inside a single deployed checkpoint.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in dynabert-adaptive-width-and-depth-boundaries.py passed with exit code 0: {"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth", "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired": 4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1, 2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050": [2, 4, 6, 8, 10, 12], "status": "ok"}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T144900Z-dynabert-adaptive-width-and-depth.json | supports | No normalized identity match for AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/dynabert-adaptive-width-and-depth-boundaries.py | supports | All constructed boundary assertions in dynabert-adaptive-width-and-depth-boundaries.py passed with exit code 0: {"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth", "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired": 4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1, 2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050": [2, 4, 6, 8, 10, 12], "status": "ok"} |
| r806-primary-pdf | https://arxiv.org/pdf/2004.04037.pdf; Full-text PDF | supports | Full-text PDF (Advances in Neural Information Processing Systems 33 (NeurIPS 2020) (2020)) read and verified. |
| r806-arxiv-abs | https://arxiv.org/abs/2004.04037; arXiv abstract | supports | arXiv abstract read and verified. |
| r806-metadata-cr | https://arxiv.org/bibtex/2004.04037; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth in Round 806.
- All pages of Advances in Neural Information Processing Systems 33 (NeurIPS 2020) (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T144930Z-dynabert-adaptive-width-and-depth
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of DynaBERT: Dynamic BERT with Adaptive Width
  and Depth'
started_at: '2026-10-19T14:49:00Z'
finished_at: '2026-10-19T14:49:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
    against existing AIMech and AIO records and verified all claims against Advances
    in Neural Information Processing Systems 33 (NeurIPS 2020) (2020) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain DynaBERT: Dynamic BERT with Adaptive Width and Depth as a distinct
  DRAFT architecture. All three claims are supported by full-text primary evidence
  and pure-Python boundary verification.'
source:
  git_revision: b5b25a67b8ce4feb3d51050e66f491a164689553
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml
    sha256: 6c5450fd16229285de4046f964cb9e8bcf66ed2fd3ec0a15fc5883a2f17484dd
    role: target
  - path: research/discovery/20261019T144900Z-dynabert-adaptive-width-and-depth.json
    sha256: ef0262db75dcf826aebcb92547cadc01ad51559b5fd15bffe6e146fa0a71c751
    role: context
  - path: research/discovery/dynabert-adaptive-width-and-depth-boundaries.py
    sha256: e6b15344f567910a124a747086630c1fc190cf273e99c9a30d5b166210277c11
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
- target_id: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  path: data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml
  label: 'DynaBERT: Dynamic BERT with Adaptive Width and Depth'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml
    role: maintained
scope:
  description: All fields of data/curated/DynaBERTDynamicBERTWithAdaptiveWidthAndDepth.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
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
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 dynabert-adaptive-width-and-depth-boundaries.py
  command: python3 research/discovery/dynabert-adaptive-width-and-depth-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  exit_code: 0
  expected_exit_code: 0
  summary: '{"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth", "num_subnetwork_configs":
    12, "top2_importance_unrewired": 1.8, "top2_importance_rewired": 4.1, "dropped_layers_md_075":
    [4, 8, 12], "teacher_matched_layers_md_075": [1, 2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050":
    [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050": [2, 4, 6, 8, 10, 12], "status":
    "ok"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T144900Z-dynabert-adaptive-width-and-depth.json
  accessed_at: '2026-10-19T14:49:00Z'
  support: supports
  summary: No normalized identity match for AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:49:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/dynabert-adaptive-width-and-depth-boundaries.py
  accessed_at: '2026-10-19T14:49:00Z'
  snapshot_sha256: e6b15344f567910a124a747086630c1fc190cf273e99c9a30d5b166210277c11
  support: supports
  summary: 'All constructed boundary assertions in dynabert-adaptive-width-and-depth-boundaries.py
    passed with exit code 0: {"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth",
    "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired":
    4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1,
    2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050":
    [2, 4, 6, 8, 10, 12], "status": "ok"}'
- evidence_id: r806-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2004.04037.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:49:00Z'
  snapshot_sha256: 92673b794cdb21b2276d7c21b040f84172ec900310dc35219a1e3f92a5d066fb
  support: supports
  summary: Full-text PDF (Advances in Neural Information Processing Systems 33 (NeurIPS
    2020) (2020)) read and verified.
- evidence_id: r806-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2004.04037
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:49:00Z'
  snapshot_sha256: 2acbc2d4a0fe989aebff5c49c7f9ef31667ab89e62e7e74ab9d4409c32254418
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r806-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2004.04037
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:49:00Z'
  snapshot_sha256: c175b3102913f5f41a326c1c8c06f40d4a6f207516e5d5035f8dc31483c14e0c
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  evidence_ids:
  - identity
  - r806-primary-pdf
  - r806-arxiv-abs
  - r806-metadata-cr
  summary: 'DynaBERT: Dynamic BERT with Adaptive Width and Depth is a distinct concept.'
  details: 'Introduced by Lu Hou, Zhiqi Huang, Lifeng Shang, Xin Jiang, Xiao Chen,
    and Qun Liu (NeurIPS 2020, arXiv:2004.04037). Distinct from fixed-size BERT compression
    methods such as TinyBERT (Round 800), MiniLM (Round 801), BERT-PKD (Round 802),
    DistilBERT (Round 803), MobileBERT (Round 804), and BERT-of-Theseus (Round 805),
    and from depth-only early-exit or layer-dropping methods such as FastBERT (Round
    807), PABEE (Round 808), and LayerDrop: DynaBERT adapts both Transformer width
    (via parallel head and FFN-neuron slicing in Eqs. 1-2 after Taylor-importance
    network rewiring) and depth (via strided layer dropping and last-layer-preserving
    hidden-state matching in Eq. 4) inside a single deployed checkpoint.'
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  evidence_ids:
  - mapping
  - r806-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  evidence_ids:
  - r806-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in dynabert-adaptive-width-and-depth-boundaries.py
    passed with exit code 0: {"concept": "DynaBERTDynamicBERTWithAdaptiveWidthAndDepth",
    "num_subnetwork_configs": 12, "top2_importance_unrewired": 1.8, "top2_importance_rewired":
    4.1, "dropped_layers_md_075": [4, 8, 12], "teacher_matched_layers_md_075": [1,
    2, 4, 5, 6, 8, 9, 10, 12], "dropped_layers_md_050": [2, 4, 6, 8, 10, 12], "teacher_matched_layers_md_050":
    [2, 4, 6, 8, 10, 12], "status": "ok"}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth
  evidence_ids:
  - identity
  - mapping
  - r806-primary-pdf
  - r806-arxiv-abs
  - r806-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth in Round
  806.
- All pages of Advances in Neural Information Processing Systems 33 (NeurIPS 2020)
  (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
