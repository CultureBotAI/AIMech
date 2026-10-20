# Scientific author self-review of FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations

- Review: 20261019T095430Z-flora-stacking-heterogeneous-federated-lora
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T09:54:00Z
- Finished UTC: 2026-10-19T09:54:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a11d83172617673b479642a24becacec747ea0aa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml | maintained | FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | Validated history sidecar files. |
| python3 flora-stacking-heterogeneous-federated-lora-boundaries.py | passed | True | AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation | FLoRA boundary verification passed: {'stacked_rank': 6, 'flora_err': 7.033790317987055e-17, 'fedit_zeropad_err': 0.691864, 'perm_err': 7.033790317987055e-17} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.

FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank Adaptations is a distinct concept.

Distinct from FFA-LoRA (AIMech:FfaLoraFederatedFreezeALowRankAdaptation; Sun et al., ICLR 2024), which eliminates aggregation cross-terms by freezing a homogeneous random projection matrix A_0 across all clients rather than training both A_k and B_k with heterogeneous client ranks r_k and stacking them on the server. Distinct from FedIT (Zhang et al., 2023) and zero-padded heterogeneous LoRA (HetLoRA; Cho et al., 2023), which average A_k and B_k separately and suffer from cross-client product noise (sum_k p_k B_k)(sum_k p_k A_k) != sum_k p_k B_k A_k. Also distinct from centralized memory-efficient low-rank gradient projection (Flora; Hao et al., 2024), which resamples random projection matrices on a single machine rather than stacking multi-client heterogeneous LoRA adapters in federated learning.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in flora-stacking-heterogeneous-federated-lora-boundaries.py passed with exit code 0: FLoRA boundary verification passed: {'stacked_rank': 6, 'flora_err': 7.033790317987055e-17, 'fedit_zeropad_err': 0.691864, 'perm_err': 7.033790317987055e-17}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T095400Z-flora-stacking-heterogeneous-federated-lora.json | supports | No normalized identity match for AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/flora-stacking-heterogeneous-federated-lora-boundaries.py | supports | All constructed boundary assertions in flora-stacking-heterogeneous-federated-lora-boundaries.py passed with exit code 0: FLoRA boundary verification passed: {'stacked_rank': 6, 'flora_err': 7.033790317987055e-17, 'fedit_zeropad_err': 0.691864, 'perm_err': 7.033790317987055e-17} |
| r511-primary-pdf | https://arxiv.org/pdf/2409.05976.pdf; Full-text PDF | supports | Full-text PDF (Advances in Neural Information Processing Systems 37 (NeurIPS 2024) (2024)) read and verified. |
| r511-arxiv-abs | https://arxiv.org/abs/2409.05976; arXiv abstract | supports | arXiv abstract read and verified. |
| r511-metadata-cr | https://dblp.org/rec/conf/nips/WangSHS0LL24; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation in Round 511.
- All pages of Advances in Neural Information Processing Systems 37 (NeurIPS 2024) (2024) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T095430Z-flora-stacking-heterogeneous-federated-lora
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of FLoRA: Stacking-Based Federated Fine-Tuning
  with Heterogeneous Low-Rank Adaptations'
started_at: '2026-10-19T09:54:00Z'
finished_at: '2026-10-19T09:54:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
    against existing AIMech and AIO records and verified all claims against Advances
    in Neural Information Processing Systems 37 (NeurIPS 2024) (2024) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank
  Adaptations as a distinct DRAFT algorithm. All three claims are supported by full-text
  primary evidence and pure-Python boundary verification.'
source:
  git_revision: a11d83172617673b479642a24becacec747ea0aa
  state: working_tree
  inputs:
  - path: data/aio/FederatedLearning.yaml
    sha256: 024eec559a32c34b180c7d16af94b58c22315d797ddf629f3f13f7f167b99938
    role: context
  - path: data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml
    sha256: 3775a69e22e203ec2874c6fd2fa5f975bc13bf080e82391268c77e66ce258832
    role: target
  - path: research/discovery/20261019T095400Z-flora-stacking-heterogeneous-federated-lora.json
    sha256: 82c765d8d87a5e354fe338c44fc718c1719239e02ad3d422b831d1c1e77ced7c
    role: context
  - path: research/discovery/flora-stacking-heterogeneous-federated-lora-boundaries.py
    sha256: 89c864dc79734099bf99b5dd70c0562d86ad90a53ccfa6d491d5879fd66870fa
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
- target_id: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  path: data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml
  label: 'FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank
    Adaptations'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml
    role: maintained
scope:
  description: All fields of data/curated/FloraStackingBasedFederatedHeterogeneousLowRankAdaptation.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
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
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 flora-stacking-heterogeneous-federated-lora-boundaries.py
  command: python3 research/discovery/flora-stacking-heterogeneous-federated-lora-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  exit_code: 0
  expected_exit_code: 0
  summary: 'FLoRA boundary verification passed: {''stacked_rank'': 6, ''flora_err'':
    7.033790317987055e-17, ''fedit_zeropad_err'': 0.691864, ''perm_err'': 7.033790317987055e-17}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T095400Z-flora-stacking-heterogeneous-federated-lora.json
  accessed_at: '2026-10-19T09:54:00Z'
  support: supports
  summary: No normalized identity match for AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T09:54:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/flora-stacking-heterogeneous-federated-lora-boundaries.py
  accessed_at: '2026-10-19T09:54:00Z'
  snapshot_sha256: 89c864dc79734099bf99b5dd70c0562d86ad90a53ccfa6d491d5879fd66870fa
  support: supports
  summary: 'All constructed boundary assertions in flora-stacking-heterogeneous-federated-lora-boundaries.py
    passed with exit code 0: FLoRA boundary verification passed: {''stacked_rank'':
    6, ''flora_err'': 7.033790317987055e-17, ''fedit_zeropad_err'': 0.691864, ''perm_err'':
    7.033790317987055e-17}'
- evidence_id: r511-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2409.05976.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T09:54:00Z'
  snapshot_sha256: bf2a952105e6c9db9fdc487ce89cc502296982189afce8cff4cfed861c0e29f3
  support: supports
  summary: Full-text PDF (Advances in Neural Information Processing Systems 37 (NeurIPS
    2024) (2024)) read and verified.
- evidence_id: r511-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2409.05976
  locator: arXiv abstract
  accessed_at: '2026-10-19T09:54:00Z'
  snapshot_sha256: 9d56705d958ed6a1ac21014a66b8d4c2d127a71b5e16fc721c355eb768fd9002
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r511-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/conf/nips/WangSHS0LL24
  locator: Crossref metadata
  accessed_at: '2026-10-19T09:54:00Z'
  snapshot_sha256: b108b3ff0768ad67acf7ba7881b84ff4fed8b4051c84f2438dae6b4a985b9ca2
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  evidence_ids:
  - identity
  - r511-primary-pdf
  - r511-arxiv-abs
  - r511-metadata-cr
  summary: 'FLoRA: Stacking-Based Federated Fine-Tuning with Heterogeneous Low-Rank
    Adaptations is a distinct concept.'
  details: Distinct from FFA-LoRA (AIMech:FfaLoraFederatedFreezeALowRankAdaptation;
    Sun et al., ICLR 2024), which eliminates aggregation cross-terms by freezing a
    homogeneous random projection matrix A_0 across all clients rather than training
    both A_k and B_k with heterogeneous client ranks r_k and stacking them on the
    server. Distinct from FedIT (Zhang et al., 2023) and zero-padded heterogeneous
    LoRA (HetLoRA; Cho et al., 2023), which average A_k and B_k separately and suffer
    from cross-client product noise (sum_k p_k B_k)(sum_k p_k A_k) != sum_k p_k B_k
    A_k. Also distinct from centralized memory-efficient low-rank gradient projection
    (Flora; Hao et al., 2024), which resamples random projection matrices on a single
    machine rather than stacking multi-client heterogeneous LoRA adapters in federated
    learning.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  evidence_ids:
  - mapping
  - r511-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  evidence_ids:
  - r511-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in flora-stacking-heterogeneous-federated-lora-boundaries.py
    passed with exit code 0: FLoRA boundary verification passed: {''stacked_rank'':
    6, ''flora_err'': 7.033790317987055e-17, ''fedit_zeropad_err'': 0.691864, ''perm_err'':
    7.033790317987055e-17}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  evidence_ids:
  - identity
  - mapping
  - r511-primary-pdf
  - r511-arxiv-abs
  - r511-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation
  in Round 511.
- All pages of Advances in Neural Information Processing Systems 37 (NeurIPS 2024)
  (2024) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
