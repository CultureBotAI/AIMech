# Scientific author self-review of HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images

- Review: 20261019T094430Z-harmofl-amplitude-normalization-weight-perturbation-fl
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T09:44:00Z
- Finished UTC: 2026-10-19T09:44:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 382c5e9a587399de494dcbe983f985b80f7a0882.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml | maintained | HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | Validated history sidecar files. |
| python3 harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py | passed | True | AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning | [PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00 -&gt; harmo_diff=3.55e-29, gamma_raw=0.18317 -&gt; gamma_harmo=0.04344, g_unpert=0.0235 vs g_pert=-0.7158 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.

HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images is a distinct concept.

Distinct from FedDG / ELCFS (AIMech:FedDgEpisodicLearningInContinuousFrequencySpaceForFederatedDomainGeneralization; Liu et al., CVPR 2021), which shares per-client frequency amplitude banks for episodic continuous interpolation and boundary-oriented meta-learning; HarmoFL maintains a single server-averaged moving-average amplitude template A_bar^t without sharing individual image amplitude banks and couples frequency harmonization with SAM-style local Euclidean weight perturbation delta_k = alpha * g / &#124;&#124;g&#124;&#124;_2. Distinct from FedBN (Li et al., ICLR 2021), which keeps Batch Normalization parameters local without frequency-space amplitude harmonization or local weight perturbation.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py passed with exit code 0: [PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00 -&gt; harmo_diff=3.55e-29, gamma_raw=0.18317 -&gt; gamma_harmo=0.04344, g_unpert=0.0235 vs g_pert=-0.7158

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T094400Z-harmofl-amplitude-normalization-weight-perturbation-fl.json | supports | No normalized identity match for AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py | supports | All constructed boundary assertions in harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py passed with exit code 0: [PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00 -&gt; harmo_diff=3.55e-29, gamma_raw=0.18317 -&gt; gamma_harmo=0.04344, g_unpert=0.0235 vs g_pert=-0.7158 |
| r501-primary-pdf | https://arxiv.org/pdf/2112.10775.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2022), Vol. 36, No. 1, pp. 1087-1095 (2022)) read and verified. |
| r501-arxiv-abs | https://arxiv.org/abs/2112.10775; arXiv abstract | supports | arXiv abstract read and verified. |
| r501-metadata-cr | https://doi.org/10.1609/aaai.v36i1.19993; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning in Round 501.
- All pages of Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2022), Vol. 36, No. 1, pp. 1087-1095 (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T094430Z-harmofl-amplitude-normalization-weight-perturbation-fl
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of HarmoFL: Harmonizing Local and Global Drifts
  in Federated Learning on Heterogeneous Medical Images'
started_at: '2026-10-19T09:44:00Z'
finished_at: '2026-10-19T09:44:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the AAAI Conference on Artificial Intelligence (AAAI 2022), Vol. 36, No. 1,
    pp. 1087-1095 (2022) and pure-Python boundary checks. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain HarmoFL: Harmonizing Local and Global Drifts in Federated Learning
  on Heterogeneous Medical Images as a distinct DRAFT algorithm. All four claims are
  supported by full-text primary evidence and pure-Python boundary verification.'
source:
  git_revision: 382c5e9a587399de494dcbe983f985b80f7a0882
  state: working_tree
  inputs:
  - path: data/aio/FederatedLearning.yaml
    sha256: 024eec559a32c34b180c7d16af94b58c22315d797ddf629f3f13f7f167b99938
    role: context
  - path: data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml
    sha256: cb2e244ee5c1df8ef51288821c9b3b114fec214ce0067174a2bb57f13b589370
    role: target
  - path: research/discovery/20261019T094400Z-harmofl-amplitude-normalization-weight-perturbation-fl.json
    sha256: 1b4532d5e62e6140e2767b7a347a884ff91d1e64cd8470a114eec1b2c1f12712
    role: context
  - path: research/discovery/harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
    sha256: a3c5727ac6510328a444b46ccc12a5da87ffc3dd8fdb643b3c1ca6627e47a6dd
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
- target_id: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  path: data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml
  label: 'HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous
    Medical Images'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml
    role: maintained
scope:
  description: All fields of data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
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
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
  command: python3 research/discovery/harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00 ->
    harmo_diff=3.55e-29, gamma_raw=0.18317 -> gamma_harmo=0.04344, g_unpert=0.0235
    vs g_pert=-0.7158'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T094400Z-harmofl-amplitude-normalization-weight-perturbation-fl.json
  accessed_at: '2026-10-19T09:44:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T09:44:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
  accessed_at: '2026-10-19T09:44:00Z'
  snapshot_sha256: a3c5727ac6510328a444b46ccc12a5da87ffc3dd8fdb643b3c1ca6627e47a6dd
  support: supports
  summary: 'All constructed boundary assertions in harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
    passed with exit code 0: [PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00
    -> harmo_diff=3.55e-29, gamma_raw=0.18317 -> gamma_harmo=0.04344, g_unpert=0.0235
    vs g_pert=-0.7158'
- evidence_id: r501-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2112.10775.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T09:44:00Z'
  snapshot_sha256: 116b5072a1653df161fbe762fd7db648d0db928a7414aa6493fff3f37b0442db
  support: supports
  summary: Full-text PDF (Proceedings of the AAAI Conference on Artificial Intelligence
    (AAAI 2022), Vol. 36, No. 1, pp. 1087-1095 (2022)) read and verified.
- evidence_id: r501-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2112.10775
  locator: arXiv abstract
  accessed_at: '2026-10-19T09:44:00Z'
  snapshot_sha256: 1426048d7e76e573295d98909ea8e7bc46ef9ef4e658c5c82805b034e65f08ca
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r501-metadata-cr
  kind: primary_source
  reference: https://doi.org/10.1609/aaai.v36i1.19993
  locator: Crossref metadata
  accessed_at: '2026-10-19T09:44:00Z'
  snapshot_sha256: bce74fe7f1f03e93a9c9e2cb71c1f375ee052f890fe1ca7736210b31b6e5804f
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  evidence_ids:
  - identity
  - r501-primary-pdf
  - r501-arxiv-abs
  - r501-metadata-cr
  summary: 'HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on
    Heterogeneous Medical Images is a distinct concept.'
  details: Distinct from FedDG / ELCFS (AIMech:FedDgEpisodicLearningInContinuousFrequencySpaceForFederatedDomainGeneralization;
    Liu et al., CVPR 2021), which shares per-client frequency amplitude banks for
    episodic continuous interpolation and boundary-oriented meta-learning; HarmoFL
    maintains a single server-averaged moving-average amplitude template A_bar^t without
    sharing individual image amplitude banks and couples frequency harmonization with
    SAM-style local Euclidean weight perturbation delta_k = alpha * g / ||g||_2. Distinct
    from FedBN (Li et al., ICLR 2021), which keeps Batch Normalization parameters
    local without frequency-space amplitude harmonization or local weight perturbation.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  evidence_ids:
  - mapping
  - r501-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  evidence_ids:
  - r501-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in harmofl-amplitude-normalization-weight-perturbation-fl-boundaries.py
    passed with exit code 0: [PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00
    -> harmo_diff=3.55e-29, gamma_raw=0.18317 -> gamma_harmo=0.04344, g_unpert=0.0235
    vs g_pert=-0.7158'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  evidence_ids:
  - identity
  - mapping
  - r501-primary-pdf
  - r501-arxiv-abs
  - r501-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning
  in Round 501.
- All pages of Proceedings of the AAAI Conference on Artificial Intelligence (AAAI
  2022), Vol. 36, No. 1, pp. 1087-1095 (2022) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
