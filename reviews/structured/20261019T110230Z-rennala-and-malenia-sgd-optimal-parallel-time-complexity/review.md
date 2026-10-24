# Scientific author self-review of Rennala SGD and Malenia SGD

- Review: 20261019T110230Z-rennala-and-malenia-sgd-optimal-parallel-time-complexity
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T11:02:00Z
- Finished UTC: 2026-10-19T11:02:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Rennala SGD and Malenia SGD as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base abbe381f3d8d9bd1adc402a7293dd59ba60536e9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml | maintained | Rennala SGD and Malenia SGD |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | Validated history sidecar files. |
| python3 rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py | passed | True | AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization | [PASS] Round 579 Rennala &amp; Malenia SGD verified: t_rennala=4.80 &lt; t_async=15.50 &lt;&lt; t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39&gt;=1.00 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.

Rennala SGD and Malenia SGD is a distinct concept.

Distinct from classical Asynchronous SGD (which applies delayed gradients hat{nabla} f(x^{k - delta_k}) computed at stale iterates and suffers suboptimal wall-clock complexity when slow stragglers inject large delays) and from synchronous Minibatch SGD (which waits for the slowest worker tau_n at every batch). Rennala SGD and Malenia SGD run workers in an asynchronous loop but strictly filter for current-iterate gradients (k' = k), automatically excluding slow stragglers i &gt; m^* in the homogeneous regime and balancing harmonic sample sizes in the heterogeneous regime.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py passed with exit code 0: [PASS] Round 579 Rennala &amp; Malenia SGD verified: t_rennala=4.80 &lt; t_async=15.50 &lt;&lt; t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39&gt;=1.00

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T110200Z-rennala-and-malenia-sgd-optimal-parallel-time-complexity.json | supports | No normalized identity match for AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py | supports | All constructed boundary assertions in rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py passed with exit code 0: [PASS] Round 579 Rennala &amp; Malenia SGD verified: t_rennala=4.80 &lt; t_async=15.50 &lt;&lt; t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39&gt;=1.00 |
| r579-primary-pdf | https://arxiv.org/pdf/2305.12387; Full-text PDF | supports | Full-text PDF (Advances in Neural Information Processing Systems 36 (NeurIPS 2023) (2023)) read and verified. |
| r579-arxiv-abs | https://arxiv.org/abs/2305.12387; arXiv abstract | supports | arXiv abstract read and verified. |
| r579-metadata-cr | https://dblp.org/search/publ/api?q=Optimal+Time+Complexities+Parallel+Stochastic+Optimization+Tyurin+Richtarik&amp;format=json; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization in Round 579.
- All pages of Advances in Neural Information Processing Systems 36 (NeurIPS 2023) (2023) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T110230Z-rennala-and-malenia-sgd-optimal-parallel-time-complexity
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Rennala SGD and Malenia SGD
started_at: '2026-10-19T11:02:00Z'
finished_at: '2026-10-19T11:02:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
    against existing AIMech and AIO records and verified all claims against Advances
    in Neural Information Processing Systems 36 (NeurIPS 2023) (2023) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Rennala SGD and Malenia SGD as a distinct DRAFT algorithm. All four
  claims are supported by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: abbe381f3d8d9bd1adc402a7293dd59ba60536e9
  state: working_tree
  inputs:
  - path: data/aio/FederatedLearning.yaml
    sha256: 024eec559a32c34b180c7d16af94b58c22315d797ddf629f3f13f7f167b99938
    role: context
  - path: data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml
    sha256: 4953b3551a9b71a3bdac699b273af8917f8cb7c54f540cd63724df0219a8ee7e
    role: target
  - path: research/discovery/20261019T110200Z-rennala-and-malenia-sgd-optimal-parallel-time-complexity.json
    sha256: de16740ab91777f0ad0eb8aefb7933bf287786306e8a924dd31017c5e2142cf0
    role: context
  - path: research/discovery/rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
    sha256: 9b07ad4918c83b30bb49b1af4332e4c6aacd8317173c960de3bb6e414daab75e
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
- target_id: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  path: data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml
  label: Rennala SGD and Malenia SGD
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml
    role: maintained
scope:
  description: All fields of data/curated/RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
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
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
  command: python3 research/discovery/rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 579 Rennala & Malenia SGD verified: t_rennala=4.80 < t_async=15.50
    << t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39>=1.00'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T110200Z-rennala-and-malenia-sgd-optimal-parallel-time-complexity.json
  accessed_at: '2026-10-19T11:02:00Z'
  support: supports
  summary: No normalized identity match for AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T11:02:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
  accessed_at: '2026-10-19T11:02:00Z'
  snapshot_sha256: 9b07ad4918c83b30bb49b1af4332e4c6aacd8317173c960de3bb6e414daab75e
  support: supports
  summary: 'All constructed boundary assertions in rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
    passed with exit code 0: [PASS] Round 579 Rennala & Malenia SGD verified: t_rennala=4.80
    < t_async=15.50 << t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39>=1.00'
- evidence_id: r579-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2305.12387
  locator: Full-text PDF
  accessed_at: '2026-10-19T11:02:00Z'
  snapshot_sha256: 9147aec69519d81c6d8c5aba9435feb050e9df2cc925e17dfb32ffc242bc8347
  support: supports
  summary: Full-text PDF (Advances in Neural Information Processing Systems 36 (NeurIPS
    2023) (2023)) read and verified.
- evidence_id: r579-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2305.12387
  locator: arXiv abstract
  accessed_at: '2026-10-19T11:02:00Z'
  snapshot_sha256: 8fd764778b566d909aa5c95a1352c12877138c84acf11a9100604df48f0373f2
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r579-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Optimal+Time+Complexities+Parallel+Stochastic+Optimization+Tyurin+Richtarik&format=json
  locator: Crossref metadata
  accessed_at: '2026-10-19T11:02:00Z'
  snapshot_sha256: b9d7a66cae2aa69b3eedbfbbebb4c3e619af164564b2b41b49530e518040d480
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  evidence_ids:
  - identity
  - r579-primary-pdf
  - r579-arxiv-abs
  - r579-metadata-cr
  summary: Rennala SGD and Malenia SGD is a distinct concept.
  details: Distinct from classical Asynchronous SGD (which applies delayed gradients
    hat{nabla} f(x^{k - delta_k}) computed at stale iterates and suffers suboptimal
    wall-clock complexity when slow stragglers inject large delays) and from synchronous
    Minibatch SGD (which waits for the slowest worker tau_n at every batch). Rennala
    SGD and Malenia SGD run workers in an asynchronous loop but strictly filter for
    current-iterate gradients (k' = k), automatically excluding slow stragglers i
    > m^* in the homogeneous regime and balancing harmonic sample sizes in the heterogeneous
    regime.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  evidence_ids:
  - mapping
  - r579-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  evidence_ids:
  - r579-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in rennala-and-malenia-sgd-optimal-parallel-time-complexity-boundaries.py
    passed with exit code 0: [PASS] Round 579 Rennala & Malenia SGD verified: t_rennala=4.80
    < t_async=15.50 << t_mb=8200.00, counts=[6, 3, 2, 1, 0, 0, 0, 0], harm_B=12.39>=1.00'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  evidence_ids:
  - identity
  - mapping
  - r579-primary-pdf
  - r579-arxiv-abs
  - r579-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:RennalaSgdAndMaleniaSgdMinimaxOptimalParallelStochasticOptimization
  in Round 579.
- All pages of Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
  (2023) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
