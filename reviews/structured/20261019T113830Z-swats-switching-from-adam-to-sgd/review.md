# Scientific author self-review of SWATS

- Review: 20261019T113830Z-swats-switching-from-adam-to-sgd
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T11:38:00Z
- Finished UTC: 2026-10-19T11:38:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SWATS as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SWATS.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SWATS
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6e280ae8cbcd51e4ed229b90295ad77536b55990.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SWATS | data/curated/SWATS.yaml | maintained | SWATS |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SWATS | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SWATS | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SWATS | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SWATS | Validated history sidecar files. |
| python3 swats-switching-from-adam-to-sgd-boundaries.py | passed | True | AIMech:SWATS | [PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16, orth_norm_gap=1.7611e-01&gt;0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16, adam_excess_norm=0.1030&gt;0 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SWATS.

SWATS is a distinct concept.

Distinct from AdaBound/AMSBound (AIMech:AdaBoundAndAMSBound, which smoothly pinches coordinate-wise step sizes via scheduled upper and lower bounds parameterized by gamma) and from Padam (AIMech:Padam, which maintains a constant partial-adaptivity power p in (0, 1/2] throughout training). SWATS executes a discrete phase switch from Adam to uniform-step-size SGD(M) where both the switchover iteration and the post-switch SGD learning rate Lambda are inferred automatically from the projection of -gamma_k g_k onto p_k.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SWATS.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SWATS.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in swats-switching-from-adam-to-sgd-boundaries.py passed with exit code 0: [PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16, orth_norm_gap=1.7611e-01&gt;0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16, adam_excess_norm=0.1030&gt;0

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SWATS.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T113800Z-swats-switching-from-adam-to-sgd.json | supports | No normalized identity match for AIMech:SWATS across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/swats-switching-from-adam-to-sgd-boundaries.py | supports | All constructed boundary assertions in swats-switching-from-adam-to-sgd-boundaries.py passed with exit code 0: [PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16, orth_norm_gap=1.7611e-01&gt;0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16, adam_excess_norm=0.1030&gt;0 |
| r615-primary-pdf | https://arxiv.org/pdf/1712.07628.pdf; Full-text PDF | supports | Full-text PDF (arXiv (2017)) read and verified. |
| r615-arxiv-abs | https://arxiv.org/abs/1712.07628; arXiv abstract | supports | arXiv abstract read and verified. |
| r615-metadata-cr | https://dblp.org/rec/journals/corr/abs-1712-07628.xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SWATS in Round 615.
- All pages of arXiv (2017) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T113830Z-swats-switching-from-adam-to-sgd
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SWATS
started_at: '2026-10-19T11:38:00Z'
finished_at: '2026-10-19T11:38:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SWATS
    against existing AIMech and AIO records and verified all claims against arXiv
    (2017) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SWATS as a distinct DRAFT algorithm. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 6e280ae8cbcd51e4ed229b90295ad77536b55990
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/SWATS.yaml
    sha256: 146f76e9a60357790b5eb8eed38308e569fe36d2975f1fc39360318fbeed879b
    role: target
  - path: research/discovery/20261019T113800Z-swats-switching-from-adam-to-sgd.json
    sha256: 4c1fee1978652c535045ad1ec5bc3b7bc626350131e874048d1138bc4fd19f86
    role: context
  - path: research/discovery/swats-switching-from-adam-to-sgd-boundaries.py
    sha256: b82733dd99ab2d3533199612a06b9d7cd629119bd6ed39850b301b88beece601
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
- target_id: AIMech:SWATS
  path: data/curated/SWATS.yaml
  label: SWATS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SWATS.yaml
    role: maintained
scope:
  description: All fields of data/curated/SWATS.yaml and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SWATS'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SWATS
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
  - AIMech:SWATS
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SWATS
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SWATS
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SWATS
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 swats-switching-from-adam-to-sgd-boundaries.py
  command: python3 research/discovery/swats-switching-from-adam-to-sgd-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SWATS
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16,
    orth_norm_gap=1.7611e-01>0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16,
    adam_excess_norm=0.1030>0'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T113800Z-swats-switching-from-adam-to-sgd.json
  accessed_at: '2026-10-19T11:38:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SWATS across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T11:38:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/swats-switching-from-adam-to-sgd-boundaries.py
  accessed_at: '2026-10-19T11:38:00Z'
  snapshot_sha256: b82733dd99ab2d3533199612a06b9d7cd629119bd6ed39850b301b88beece601
  support: supports
  summary: 'All constructed boundary assertions in swats-switching-from-adam-to-sgd-boundaries.py
    passed with exit code 0: [PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16,
    orth_norm_gap=1.7611e-01>0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16,
    adam_excess_norm=0.1030>0'
- evidence_id: r615-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1712.07628.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T11:38:00Z'
  snapshot_sha256: a5c0875c1c614755cc69a4b4fe4d970c7770574bfcc6e25ebe363837546e97d1
  support: supports
  summary: Full-text PDF (arXiv (2017)) read and verified.
- evidence_id: r615-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1712.07628
  locator: arXiv abstract
  accessed_at: '2026-10-19T11:38:00Z'
  snapshot_sha256: 9e92c3a4b805bb23f0b09595d42a93c5df700837113b99f1ac4c35745e0bfc68
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r615-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/journals/corr/abs-1712-07628.xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T11:38:00Z'
  snapshot_sha256: 7311fb071ea7490e66bc9edd149561ace1dbc8201dc09c6a24ed243ee8c92d51
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SWATS
  evidence_ids:
  - identity
  - r615-primary-pdf
  - r615-arxiv-abs
  - r615-metadata-cr
  summary: SWATS is a distinct concept.
  details: Distinct from AdaBound/AMSBound (AIMech:AdaBoundAndAMSBound, which smoothly
    pinches coordinate-wise step sizes via scheduled upper and lower bounds parameterized
    by gamma) and from Padam (AIMech:Padam, which maintains a constant partial-adaptivity
    power p in (0, 1/2] throughout training). SWATS executes a discrete phase switch
    from Adam to uniform-step-size SGD(M) where both the switchover iteration and
    the post-switch SGD learning rate Lambda are inferred automatically from the projection
    of -gamma_k g_k onto p_k.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SWATS
  evidence_ids:
  - mapping
  - r615-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SWATS
  evidence_ids:
  - r615-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in swats-switching-from-adam-to-sgd-boundaries.py
    passed with exit code 0: [PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16,
    orth_norm_gap=1.7611e-01>0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16,
    adam_excess_norm=0.1030>0'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SWATS
  evidence_ids:
  - identity
  - mapping
  - r615-primary-pdf
  - r615-arxiv-abs
  - r615-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SWATS in Round 615.
- All pages of arXiv (2017) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
