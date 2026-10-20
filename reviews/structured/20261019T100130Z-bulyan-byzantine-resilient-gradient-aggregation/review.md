# Scientific author self-review of Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule)

- Review: 20261019T100130Z-bulyan-byzantine-resilient-gradient-aggregation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T10:01:00Z
- Finished UTC: 2026-10-19T10:01:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/BulyanByzantineResilientGradientAggregation.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:BulyanByzantineResilientGradientAggregation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b166c90c50edd184006b803f82d2dd9f782f502f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BulyanByzantineResilientGradientAggregation | data/curated/BulyanByzantineResilientGradientAggregation.yaml | maintained | Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:BulyanByzantineResilientGradientAggregation | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:BulyanByzantineResilientGradientAggregation | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:BulyanByzantineResilientGradientAggregation | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:BulyanByzantineResilientGradientAggregation | Validated history sidecar files. |
| python3 bulyan-byzantine-resilient-gradient-aggregation-boundaries.py | passed | True | AIMech:BulyanByzantineResilientGradientAggregation | [PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859&gt;&gt;bulyan_coord0_err=0.0237, bracketed_all_d=200 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:BulyanByzantineResilientGradientAggregation.

Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule) is a distinct concept.

Introduced by El Mahdi El Mhamdi, Rachid Guerraoui, and Sebastien Rouault in 'The Hidden Vulnerability of Distributed Learning in Byzantium' (ICML 2018, PMLR 80:3518-3527; arXiv:1802.07927). Distinct from Krum and Multi-Krum (Blanchard et al. NeurIPS 2017), which select and average whole vectors using Euclidean pairwise distance scores without coordinate-wise median trimming and thus remain vulnerable to single-coordinate O(sqrt(d)) poisoning; and distinct from Coordinate-Wise Median and Trimmed Mean (Yin et al. ICML 2018), which apply coordinate-wise order statistics directly to all n submitted vectors without a first-stage (alpha, f)-Byzantine-resilient vector selection quorum S.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:BulyanByzantineResilientGradientAggregation.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:BulyanByzantineResilientGradientAggregation.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in bulyan-byzantine-resilient-gradient-aggregation-boundaries.py passed with exit code 0: [PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859&gt;&gt;bulyan_coord0_err=0.0237, bracketed_all_d=200

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:BulyanByzantineResilientGradientAggregation.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T100100Z-bulyan-byzantine-resilient-gradient-aggregation.json | supports | No normalized identity match for AIMech:BulyanByzantineResilientGradientAggregation across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/bulyan-byzantine-resilient-gradient-aggregation-boundaries.py | supports | All constructed boundary assertions in bulyan-byzantine-resilient-gradient-aggregation-boundaries.py passed with exit code 0: [PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859&gt;&gt;bulyan_coord0_err=0.0237, bracketed_all_d=200 |
| r518-primary-pdf | https://arxiv.org/pdf/1802.07927.pdf; Full-text PDF | supports | Full-text PDF (ICML 2018 (2018)) read and verified. |
| r518-arxiv-abs | https://arxiv.org/abs/1802.07927; arXiv abstract | supports | arXiv abstract read and verified. |
| r518-metadata-cr | https://dblp.org/rec/conf/icml/MhamdiGR18; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:BulyanByzantineResilientGradientAggregation in Round 518.
- All pages of ICML 2018 (2018) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T100130Z-bulyan-byzantine-resilient-gradient-aggregation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Bulyan (Byzantine-Resilient Gradient Meta-Aggregation
  Rule)
started_at: '2026-10-19T10:01:00Z'
finished_at: '2026-10-19T10:01:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:BulyanByzantineResilientGradientAggregation
    against existing AIMech and AIO records and verified all claims against ICML 2018
    (2018) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule) as a distinct
  DRAFT algorithm. All three claims are supported by full-text primary evidence and
  pure-Python boundary verification.
source:
  git_revision: b166c90c50edd184006b803f82d2dd9f782f502f
  state: working_tree
  inputs:
  - path: data/aio/FederatedLearning.yaml
    sha256: 024eec559a32c34b180c7d16af94b58c22315d797ddf629f3f13f7f167b99938
    role: context
  - path: data/curated/BulyanByzantineResilientGradientAggregation.yaml
    sha256: 10053e2d1d2df9f700a42030a89c767e4a7c14749157c3a5516b60acc72bcf06
    role: target
  - path: research/discovery/20261019T100100Z-bulyan-byzantine-resilient-gradient-aggregation.json
    sha256: edb0f3061ab302218aebe89ce24aef836ed7b9ab68d98cbf6821c1e5ed697c38
    role: context
  - path: research/discovery/bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
    sha256: 4131fc51094c117ba77165565f43ad6cfc4e841d79641af3dc0ad4c848774e16
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
- target_id: AIMech:BulyanByzantineResilientGradientAggregation
  path: data/curated/BulyanByzantineResilientGradientAggregation.yaml
  label: Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BulyanByzantineResilientGradientAggregation.yaml
    role: maintained
scope:
  description: All fields of data/curated/BulyanByzantineResilientGradientAggregation.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:BulyanByzantineResilientGradientAggregation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
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
  - AIMech:BulyanByzantineResilientGradientAggregation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
  command: python3 research/discovery/bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859>>bulyan_coord0_err=0.0237,
    bracketed_all_d=200'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T100100Z-bulyan-byzantine-resilient-gradient-aggregation.json
  accessed_at: '2026-10-19T10:01:00Z'
  support: supports
  summary: No normalized identity match for AIMech:BulyanByzantineResilientGradientAggregation
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T10:01:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
  accessed_at: '2026-10-19T10:01:00Z'
  snapshot_sha256: 4131fc51094c117ba77165565f43ad6cfc4e841d79641af3dc0ad4c848774e16
  support: supports
  summary: 'All constructed boundary assertions in bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
    passed with exit code 0: [PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859>>bulyan_coord0_err=0.0237,
    bracketed_all_d=200'
- evidence_id: r518-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1802.07927.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T10:01:00Z'
  snapshot_sha256: 5234c45a295f7915d26f9bb60a4d5f0739d0fb19ad99f0622391dffb917c145d
  support: supports
  summary: Full-text PDF (ICML 2018 (2018)) read and verified.
- evidence_id: r518-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1802.07927
  locator: arXiv abstract
  accessed_at: '2026-10-19T10:01:00Z'
  snapshot_sha256: 54577000dfe2cb4aca5efdbbcd3cb8546200e12cfb42a1ae4113e432ea908c5c
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r518-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/conf/icml/MhamdiGR18
  locator: Crossref metadata
  accessed_at: '2026-10-19T10:01:00Z'
  snapshot_sha256: 72596d3756ca83f7a992ecc5fa84afffebdc58a9b0ca88f547969a0819108a9a
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  evidence_ids:
  - identity
  - r518-primary-pdf
  - r518-arxiv-abs
  - r518-metadata-cr
  summary: Bulyan (Byzantine-Resilient Gradient Meta-Aggregation Rule) is a distinct
    concept.
  details: Introduced by El Mahdi El Mhamdi, Rachid Guerraoui, and Sebastien Rouault
    in 'The Hidden Vulnerability of Distributed Learning in Byzantium' (ICML 2018,
    PMLR 80:3518-3527; arXiv:1802.07927). Distinct from Krum and Multi-Krum (Blanchard
    et al. NeurIPS 2017), which select and average whole vectors using Euclidean pairwise
    distance scores without coordinate-wise median trimming and thus remain vulnerable
    to single-coordinate O(sqrt(d)) poisoning; and distinct from Coordinate-Wise Median
    and Trimmed Mean (Yin et al. ICML 2018), which apply coordinate-wise order statistics
    directly to all n submitted vectors without a first-stage (alpha, f)-Byzantine-resilient
    vector selection quorum S.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  evidence_ids:
  - mapping
  - r518-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  evidence_ids:
  - r518-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in bulyan-byzantine-resilient-gradient-aggregation-boundaries.py
    passed with exit code 0: [PASS] Round 518 Bulyan (El Mhamdi et al. 2018): krum_coord0_err=2.859>>bulyan_coord0_err=0.0237,
    bracketed_all_d=200'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:BulyanByzantineResilientGradientAggregation
  evidence_ids:
  - identity
  - mapping
  - r518-primary-pdf
  - r518-arxiv-abs
  - r518-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:BulyanByzantineResilientGradientAggregation in Round
  518.
- All pages of ICML 2018 (2018) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
