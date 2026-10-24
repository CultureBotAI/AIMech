# Scientific author self-review of Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport

- Review: 20261019T064630Z-iterative-bregman-projections-dykstra-regularized-ot
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T06:46:00Z
- Finished UTC: 2026-10-19T06:46:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3dd7fd98c635bcb063790629eec92f0ec83193d8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml | maintained | Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | Validated history sidecar files. |
| python3 iterative-bregman-projections-dykstra-regularized-ot-boundaries.py | passed | True | AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport | {"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport", "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15, "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17, "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.

Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport is a distinct concept.

Distinct from standard pairwise Sinkhorn matrix scaling (&#96;AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport&#96;) and dual subgradient Wasserstein barycenters (&#96;AIMech:FastWassersteinBarycentersAndSmoothedDualSubgradientDescent&#96;). Specifically captures the Benamou et al. (2015) unified KL Bregman projection formulation over intersections of affine and non-affine convex sets (Section 2, Equations 2-4), the Proposition 2 geometric-mean IBP Wasserstein barycenter algorithm (which eliminates inner Sinkhorn loops and line-search step sizes), and the Bregman-Dykstra algorithm with multiplicative memory variables for partial, capacity-constrained, and martingale transport (Sections 5.1-5.3, Propositions 4-5, Equations 20-26).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in iterative-bregman-projections-dykstra-regularized-ot-boundaries.py passed with exit code 0: {"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport", "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15, "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17, "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T064600Z-iterative-bregman-projections-dykstra-regularized-ot.json | supports | No normalized identity match for AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/iterative-bregman-projections-dykstra-regularized-ot-boundaries.py | supports | All constructed boundary assertions in iterative-bregman-projections-dykstra-regularized-ot-boundaries.py passed with exit code 0: {"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport", "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15, "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17, "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"} |
| r327-primary-pdf | https://arxiv.org/pdf/1412.5154v1; Full-text PDF | supports | Full-text PDF (SIAM Journal on Scientific Computing 37(2):A1111-A1138 (2015)) read and verified. |
| r327-arxiv-abs | https://arxiv.org/abs/1412.5154v1; arXiv abstract | supports | arXiv abstract read and verified. |
| r327-metadata-cr | https://api.crossref.org/works/10.1137/141000439; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport in Round 327.
- All pages of SIAM Journal on Scientific Computing 37(2):A1111-A1138 (2015) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T064630Z-iterative-bregman-projections-dykstra-regularized-ot
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Iterative Bregman Projections and Bregman-Dykstra
  Regularized Optimal Transport
started_at: '2026-10-19T06:46:00Z'
finished_at: '2026-10-19T06:46:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
    against existing AIMech and AIO records and verified all claims against SIAM Journal
    on Scientific Computing 37(2):A1111-A1138 (2015) and pure-Python boundary checks.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal
  Transport as a distinct DRAFT algorithm. All three claims are supported by full-text
  primary evidence and pure-Python boundary verification.
source:
  git_revision: 3dd7fd98c635bcb063790629eec92f0ec83193d8
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml
    sha256: 625d5b3fa2081ac080846fb84f4d7838b8b5c198791bff33c16530cc081302f7
    role: target
  - path: research/discovery/20261019T064600Z-iterative-bregman-projections-dykstra-regularized-ot.json
    sha256: 1b9f8ab9ef5e1042d4ce0b2882017deee941ff45517f75add56ba421e5eb8e3b
    role: context
  - path: research/discovery/iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
    sha256: 1b415ef756566f75aaa9920da2367ee9cca88e1e85557ba988adac206e4019f1
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
- target_id: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  path: data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml
  label: Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml
    role: maintained
scope:
  description: All fields of data/curated/IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
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
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
  command: python3 research/discovery/iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  exit_code: 0
  expected_exit_code: 0
  summary: '{"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport",
    "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15,
    "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17,
    "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T064600Z-iterative-bregman-projections-dykstra-regularized-ot.json
  accessed_at: '2026-10-19T06:46:00Z'
  support: supports
  summary: No normalized identity match for AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T06:46:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
  accessed_at: '2026-10-19T06:46:00Z'
  snapshot_sha256: 1b415ef756566f75aaa9920da2367ee9cca88e1e85557ba988adac206e4019f1
  support: supports
  summary: 'All constructed boundary assertions in iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
    passed with exit code 0: {"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport",
    "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15,
    "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17,
    "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"}'
- evidence_id: r327-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1412.5154v1
  locator: Full-text PDF
  accessed_at: '2026-10-19T06:46:00Z'
  snapshot_sha256: fd5f2b5137e2775ff7e3597dcbda20bd77c3009126b89e8cb915536817e61eae
  support: supports
  summary: Full-text PDF (SIAM Journal on Scientific Computing 37(2):A1111-A1138 (2015))
    read and verified.
- evidence_id: r327-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1412.5154v1
  locator: arXiv abstract
  accessed_at: '2026-10-19T06:46:00Z'
  snapshot_sha256: 28938b44634c3f46092a755ca2dd9f63de0bc7398e11fb933eeca1d726742c2c
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r327-metadata-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1137/141000439
  locator: Crossref metadata
  accessed_at: '2026-10-19T06:46:00Z'
  snapshot_sha256: 8f97b1bc4edf7b88cab562da62358d45e7bf467e3b1f3ce535880ccad2e18e97
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  evidence_ids:
  - identity
  - r327-primary-pdf
  - r327-arxiv-abs
  - r327-metadata-cr
  summary: Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport
    is a distinct concept.
  details: Distinct from standard pairwise Sinkhorn matrix scaling (`AIMech:SinkhornDistancesAndEntropicRegularizedOptimalTransport`)
    and dual subgradient Wasserstein barycenters (`AIMech:FastWassersteinBarycentersAndSmoothedDualSubgradientDescent`).
    Specifically captures the Benamou et al. (2015) unified KL Bregman projection
    formulation over intersections of affine and non-affine convex sets (Section 2,
    Equations 2-4), the Proposition 2 geometric-mean IBP Wasserstein barycenter algorithm
    (which eliminates inner Sinkhorn loops and line-search step sizes), and the Bregman-Dykstra
    algorithm with multiplicative memory variables for partial, capacity-constrained,
    and martingale transport (Sections 5.1-5.3, Propositions 4-5, Equations 20-26).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  evidence_ids:
  - mapping
  - r327-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  evidence_ids:
  - r327-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in iterative-bregman-projections-dykstra-regularized-ot-boundaries.py
    passed with exit code 0: {"concept": "IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport",
    "dykstra_feasibility_err": 3.3306690738754696e-16, "dykstra_kkt_cycle_err": 1.7763568394002505e-15,
    "naive_vs_dykstra_l1_gap": 0.333333, "prop1_sinkhorn_ibp_diff": 5.551115123125783e-17,
    "prop2_barycenter_midpoint_mass": 0.613453, "status": "VERIFIED"}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  evidence_ids:
  - identity
  - mapping
  - r327-primary-pdf
  - r327-arxiv-abs
  - r327-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport
  in Round 327.
- All pages of SIAM Journal on Scientific Computing 37(2):A1111-A1138 (2015) were
  read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
