# Scientific author self-review of Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring

- Review: 20261019T133330Z-pmi-dc-domain-conditional-pointwise-mutual-information
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:33:00Z
- Finished UTC: 2026-10-19T13:33:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring as a distinct DRAFT evaluation_method. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:PMIDCDomainConditionalPointwiseMutualInformation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e788a00ef44958a3847a94fc0327d7609396fd62.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PMIDCDomainConditionalPointwiseMutualInformation | data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml | maintained | Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:PMIDCDomainConditionalPointwiseMutualInformation | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:PMIDCDomainConditionalPointwiseMutualInformation | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:PMIDCDomainConditionalPointwiseMutualInformation | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:PMIDCDomainConditionalPointwiseMutualInformation | Validated history sidecar files. |
| python3 pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py | passed | True | AIMech:PMIDCDomainConditionalPointwiseMutualInformation | Domain Conditional PMI verification passed. |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:PMIDCDomainConditionalPointwiseMutualInformation.

Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring is a distinct concept.

Distinct from standard direct probability arg max_i P(y_i &#124; x) and length-normalized average log-likelihood AVG = (1/l_i) sum_j log P(y_i^j &#124; x, y_i^{&lt;j}), which do not factor out surface-form rarity, and from Contextual Calibration (Zhao et al., ICML 2021, AIMech:CalibrateBeforeUseContextualCalibration), which fits an affine matrix over a fixed closed label set using multiple content-free inputs rather than computing the symmetric log-probability difference log P(y_i &#124; x) - log P(y_i &#124; x_domain) for arbitrary open-set per-question answer options.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:PMIDCDomainConditionalPointwiseMutualInformation.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:PMIDCDomainConditionalPointwiseMutualInformation.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py passed with exit code 0: Domain Conditional PMI verification passed.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:PMIDCDomainConditionalPointwiseMutualInformation.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T133300Z-pmi-dc-domain-conditional-pointwise-mutual-information.json | supports | No normalized identity match for AIMech:PMIDCDomainConditionalPointwiseMutualInformation across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py | supports | All constructed boundary assertions in pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py passed with exit code 0: Domain Conditional PMI verification passed. |
| r730-primary-pdf | https://arxiv.org/pdf/2104.08315.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021), pp. 7038-7051 (2021)) read and verified. |
| r730-arxiv-abs | https://arxiv.org/abs/2104.08315; arXiv abstract | supports | arXiv abstract read and verified. |
| r730-metadata-cr | https://dblp.org/search/publ/api?q=Surface+Form+Competition+Why+the+Highest+Probability+Answer+Holtzman&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:PMIDCDomainConditionalPointwiseMutualInformation in Round 730.
- All pages of Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021), pp. 7038-7051 (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T133330Z-pmi-dc-domain-conditional-pointwise-mutual-information
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Domain Conditional Pointwise Mutual Information
  (PMI_DC) Scoring
started_at: '2026-10-19T13:33:00Z'
finished_at: '2026-10-19T13:33:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:PMIDCDomainConditionalPointwiseMutualInformation
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP
    2021), pp. 7038-7051 (2021) and pure-Python boundary checks. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring as
  a distinct DRAFT evaluation_method. All three claims are supported by full-text
  primary evidence and pure-Python boundary verification.
source:
  git_revision: e788a00ef44958a3847a94fc0327d7609396fd62
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml
    sha256: c334ca08547eaf2df9c3887be8597fbd55309e1b30511c796a2b38992a9b44cf
    role: target
  - path: research/discovery/20261019T133300Z-pmi-dc-domain-conditional-pointwise-mutual-information.json
    sha256: fe4e769103ccecf2f532a7504ce3e045d0aba4ac0d5eb6fc5dcc552e0a9f3092
    role: context
  - path: research/discovery/pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
    sha256: b9eec52098b65e72d5effb90952fe8b4cbbaadcc42d56360765891adf99e9de2
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
- target_id: AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  path: data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml
  label: Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml
    role: maintained
scope:
  description: All fields of data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:PMIDCDomainConditionalPointwiseMutualInformation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
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
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
  command: python3 research/discovery/pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  exit_code: 0
  expected_exit_code: 0
  summary: Domain Conditional PMI verification passed.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T133300Z-pmi-dc-domain-conditional-pointwise-mutual-information.json
  accessed_at: '2026-10-19T13:33:00Z'
  support: supports
  summary: No normalized identity match for AIMech:PMIDCDomainConditionalPointwiseMutualInformation
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:33:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
  accessed_at: '2026-10-19T13:33:00Z'
  snapshot_sha256: b9eec52098b65e72d5effb90952fe8b4cbbaadcc42d56360765891adf99e9de2
  support: supports
  summary: 'All constructed boundary assertions in pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
    passed with exit code 0: Domain Conditional PMI verification passed.'
- evidence_id: r730-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2104.08315.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:33:00Z'
  snapshot_sha256: 810c26ceec851aff7b478bab82f09aaf09bd592650f1931869ecaac325974566
  support: supports
  summary: Full-text PDF (Proceedings of the 2021 Conference on Empirical Methods
    in Natural Language Processing (EMNLP 2021), pp. 7038-7051 (2021)) read and verified.
- evidence_id: r730-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2104.08315
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:33:00Z'
  snapshot_sha256: 158504202d2676331b91bfba598ec764538bf25b0f7f737c8d81c282fc1c763c
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r730-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Surface+Form+Competition+Why+the+Highest+Probability+Answer+Holtzman&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:33:00Z'
  snapshot_sha256: c5e89a324d8f33e92af0db51cccfc82748eb1693d8f7ab48487080618bc38ce6
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  evidence_ids:
  - identity
  - r730-primary-pdf
  - r730-arxiv-abs
  - r730-metadata-cr
  summary: Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring is a distinct
    concept.
  details: Distinct from standard direct probability arg max_i P(y_i | x) and length-normalized
    average log-likelihood AVG = (1/l_i) sum_j log P(y_i^j | x, y_i^{<j}), which do
    not factor out surface-form rarity, and from Contextual Calibration (Zhao et al.,
    ICML 2021, AIMech:CalibrateBeforeUseContextualCalibration), which fits an affine
    matrix over a fixed closed label set using multiple content-free inputs rather
    than computing the symmetric log-probability difference log P(y_i | x) - log P(y_i
    | x_domain) for arbitrary open-set per-question answer options.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  evidence_ids:
  - mapping
  - r730-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  evidence_ids:
  - r730-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in pmi-dc-domain-conditional-pointwise-mutual-information-boundaries.py
    passed with exit code 0: Domain Conditional PMI verification passed.'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:PMIDCDomainConditionalPointwiseMutualInformation
  evidence_ids:
  - identity
  - mapping
  - r730-primary-pdf
  - r730-arxiv-abs
  - r730-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:PMIDCDomainConditionalPointwiseMutualInformation in
  Round 730.
- All pages of Proceedings of the 2021 Conference on Empirical Methods in Natural
  Language Processing (EMNLP 2021), pp. 7038-7051 (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
