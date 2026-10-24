# Scientific author self-review of SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis)

- Review: 20261019T111230Z-soap-shampoo-with-adam-in-preconditioner-eigenbasis
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T11:12:00Z
- Finished UTC: 2026-10-19T11:12:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis) as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 884fd58b5588c54e765ca4ebbad26f17c5f089bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml | maintained | SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | Validated history sidecar files. |
| python3 soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py | passed | True | AIMech:SoapShampooWithAdamInPreconditionerEigenbasis | [PASS] Round 589 SOAP verified: claim1_diff=8.88e-16, loss_soap=2.2020e-05&lt;loss_sh=1.0655e-04, space=(10485760&lt;12582912&lt;48234496) |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis.

SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis) is a distinct concept.

Distinct from Shampoo in that SOAP establishes an exact equivalence between idealized Shampoo (with exponent 1/2 and trace scaling) and idealized Adafactor in Shampoo's eigenbasis (Claim 1), and replaces rank-1 Adafactor with full coordinatewise Adam second-moment tracking V updated at every step inside the rotated eigenbasis (Q_L, Q_R), preventing stale-preconditioner degradation when Q_L and Q_R are recomputed infrequently every f steps. Distinct from GaLore in that SOAP maintains exponential moving averages of G G^T and G^T G on both sides of a 2D layer and stores first-moment momentum M in the original parameter space before projecting into the updated eigenbasis.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py passed with exit code 0: [PASS] Round 589 SOAP verified: claim1_diff=8.88e-16, loss_soap=2.2020e-05&lt;loss_sh=1.0655e-04, space=(10485760&lt;12582912&lt;48234496)

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T111200Z-soap-shampoo-with-adam-in-preconditioner-eigenbasis.json | supports | No normalized identity match for AIMech:SoapShampooWithAdamInPreconditionerEigenbasis across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py | supports | All constructed boundary assertions in soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py passed with exit code 0: [PASS] Round 589 SOAP verified: claim1_diff=8.88e-16, loss_soap=2.2020e-05&lt;loss_sh=1.0655e-04, space=(10485760&lt;12582912&lt;48234496) |
| r589-primary-pdf | https://arxiv.org/pdf/2409.11321.pdf; Full-text PDF | supports | Full-text PDF (International Conference on Learning Representations (ICLR 2025) (2025)) read and verified. |
| r589-arxiv-abs | https://arxiv.org/abs/2409.11321; arXiv abstract | supports | arXiv abstract read and verified. |
| r589-metadata-cr | https://dblp.org/rec/conf/iclr/0001MZSBJK25; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SoapShampooWithAdamInPreconditionerEigenbasis in Round 589.
- All pages of International Conference on Learning Representations (ICLR 2025) (2025) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T111230Z-soap-shampoo-with-adam-in-preconditioner-eigenbasis
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SOAP (ShampoO with Adam in the Preconditioner's
  Eigenbasis)
started_at: '2026-10-19T11:12:00Z'
finished_at: '2026-10-19T11:12:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
    against existing AIMech and AIO records and verified all claims against International
    Conference on Learning Representations (ICLR 2025) (2025) and pure-Python boundary
    checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis) as a distinct
  DRAFT algorithm. All four claims are supported by full-text primary evidence and
  pure-Python boundary verification.
source:
  git_revision: 884fd58b5588c54e765ca4ebbad26f17c5f089bf
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml
    sha256: 44cac9fdec0c73aeb4380639eb8e1e1c43f6dd87662bf607adc2547e206b4947
    role: target
  - path: research/discovery/20261019T111200Z-soap-shampoo-with-adam-in-preconditioner-eigenbasis.json
    sha256: 9bf846b3a829f6d57153af290034eddca2be5ef1235720a5366f76bd427353d7
    role: context
  - path: research/discovery/soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
    sha256: 346974c9cf4e595c679971e56b7f0c41df3a8b55c8afb004aed8f2212550f39e
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
- target_id: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  path: data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml
  label: SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml
    role: maintained
scope:
  description: All fields of data/curated/SoapShampooWithAdamInPreconditionerEigenbasis.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SoapShampooWithAdamInPreconditionerEigenbasis'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
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
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
  command: python3 research/discovery/soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 589 SOAP verified: claim1_diff=8.88e-16, loss_soap=2.2020e-05<loss_sh=1.0655e-04,
    space=(10485760<12582912<48234496)'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T111200Z-soap-shampoo-with-adam-in-preconditioner-eigenbasis.json
  accessed_at: '2026-10-19T11:12:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T11:12:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
  accessed_at: '2026-10-19T11:12:00Z'
  snapshot_sha256: 346974c9cf4e595c679971e56b7f0c41df3a8b55c8afb004aed8f2212550f39e
  support: supports
  summary: 'All constructed boundary assertions in soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
    passed with exit code 0: [PASS] Round 589 SOAP verified: claim1_diff=8.88e-16,
    loss_soap=2.2020e-05<loss_sh=1.0655e-04, space=(10485760<12582912<48234496)'
- evidence_id: r589-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2409.11321.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T11:12:00Z'
  snapshot_sha256: d6f33bb71eab0f046d911b60800846fd3332f1dcf5f2f1434ab444ab89d0b22a
  support: supports
  summary: Full-text PDF (International Conference on Learning Representations (ICLR
    2025) (2025)) read and verified.
- evidence_id: r589-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2409.11321
  locator: arXiv abstract
  accessed_at: '2026-10-19T11:12:00Z'
  snapshot_sha256: 6b90ff5efde8274b1f5c8140bfed1203f1b25ecb69d1f77519459d0cd3e75257
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r589-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/conf/iclr/0001MZSBJK25
  locator: Crossref metadata
  accessed_at: '2026-10-19T11:12:00Z'
  snapshot_sha256: 8ccbc2ce42e0582ce719ea790ce4d4bb40b804fc1159eacd9585431be35a4b5e
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  evidence_ids:
  - identity
  - r589-primary-pdf
  - r589-arxiv-abs
  - r589-metadata-cr
  summary: SOAP (ShampoO with Adam in the Preconditioner's Eigenbasis) is a distinct
    concept.
  details: Distinct from Shampoo in that SOAP establishes an exact equivalence between
    idealized Shampoo (with exponent 1/2 and trace scaling) and idealized Adafactor
    in Shampoo's eigenbasis (Claim 1), and replaces rank-1 Adafactor with full coordinatewise
    Adam second-moment tracking V updated at every step inside the rotated eigenbasis
    (Q_L, Q_R), preventing stale-preconditioner degradation when Q_L and Q_R are recomputed
    infrequently every f steps. Distinct from GaLore in that SOAP maintains exponential
    moving averages of G G^T and G^T G on both sides of a 2D layer and stores first-moment
    momentum M in the original parameter space before projecting into the updated
    eigenbasis.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  evidence_ids:
  - mapping
  - r589-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  evidence_ids:
  - r589-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in soap-shampoo-with-adam-in-preconditioner-eigenbasis-boundaries.py
    passed with exit code 0: [PASS] Round 589 SOAP verified: claim1_diff=8.88e-16,
    loss_soap=2.2020e-05<loss_sh=1.0655e-04, space=(10485760<12582912<48234496)'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SoapShampooWithAdamInPreconditionerEigenbasis
  evidence_ids:
  - identity
  - mapping
  - r589-primary-pdf
  - r589-arxiv-abs
  - r589-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SoapShampooWithAdamInPreconditionerEigenbasis in Round
  589.
- All pages of International Conference on Learning Representations (ICLR 2025) (2025)
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
