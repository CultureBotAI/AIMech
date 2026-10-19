# Scientific author self-review of FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)

- Review: 20261019T080930Z-fedbn-federated-learning-non-iid-features-local-bn
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T08:09:00Z
- Finished UTC: 2026-10-19T08:09:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain FedBN (Federated Learning on Non-IID Features via Local Batch Normalization) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3a8af9ff5eb9e25d72e97f77ca0e04178074afc2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml | maintained | FedBN (Federated Learning on Non-IID Features via Local Batch Normalization) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | Validated history sidecar files. |
| python3 fedbn-federated-learning-non-iid-features-local-bn-boundaries.py | passed | True | AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization | [PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366&gt;mu0=0.01559, rate_fedbn=0.5264&lt;rate_fedavg=0.8554, mse_fedbn=1.51e-31&lt;&lt;mse_fedavg_bn=12.7582 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.

FedBN (Federated Learning on Non-IID Features via Local Batch Normalization) is a distinct concept.

Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization) and SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning), which synchronize all model layers including Batch Normalization parameters and add proximal or control-variate corrections, and from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning, which keeps the top classification head h_i local to address heterogeneous label conditional distributions P_i(y&#124;x) rather than keeping internal Batch Normalization layers local to mitigate feature shift P_i(x)).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in fedbn-federated-learning-non-iid-features-local-bn-boundaries.py passed with exit code 0: [PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366&gt;mu0=0.01559, rate_fedbn=0.5264&lt;rate_fedavg=0.8554, mse_fedbn=1.51e-31&lt;&lt;mse_fedavg_bn=12.7582

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T080900Z-fedbn-federated-learning-non-iid-features-local-bn.json | supports | No normalized identity match for AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/fedbn-federated-learning-non-iid-features-local-bn-boundaries.py | supports | All constructed boundary assertions in fedbn-federated-learning-non-iid-features-local-bn-boundaries.py passed with exit code 0: [PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366&gt;mu0=0.01559, rate_fedbn=0.5264&lt;rate_fedavg=0.8554, mse_fedbn=1.51e-31&lt;&lt;mse_fedavg_bn=12.7582 |
| r406-primary-pdf | https://openreview.net/forum?id=6YEQUn0QICG; Full-text PDF | supports | Full-text PDF (International Conference on Learning Representations (ICLR 2021) (2021)) read and verified. |
| r406-arxiv-abs | https://arxiv.org/abs/2102.07623; arXiv abstract | supports | arXiv abstract read and verified. |
| r406-metadata-cr | https://openreview.net/forum?id=6YEQUn0QICG; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization in Round 406.
- All pages of International Conference on Learning Representations (ICLR 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T080930Z-fedbn-federated-learning-non-iid-features-local-bn
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of FedBN (Federated Learning on Non-IID Features
  via Local Batch Normalization)
started_at: '2026-10-19T08:09:00Z'
finished_at: '2026-10-19T08:09:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
    against existing AIMech and AIO records and verified all claims against International
    Conference on Learning Representations (ICLR 2021) (2021) and pure-Python boundary
    checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)
  as a distinct DRAFT algorithm. All three claims are supported by full-text primary
  evidence and pure-Python boundary verification.
source:
  git_revision: 3a8af9ff5eb9e25d72e97f77ca0e04178074afc2
  state: working_tree
  inputs:
  - path: data/aio/FederatedLearning.yaml
    sha256: 024eec559a32c34b180c7d16af94b58c22315d797ddf629f3f13f7f167b99938
    role: context
  - path: data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml
    sha256: 6b61181b3eda9048bec4fc6cce180d35e0c2532669d6e6b99a66ff621703d49b
    role: target
  - path: research/discovery/20261019T080900Z-fedbn-federated-learning-non-iid-features-local-bn.json
    sha256: aef927865f29a9bbe7f5c43f3ac32f19e24b823d9e7b1b4db11be13513af1e61
    role: context
  - path: research/discovery/fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
    sha256: 52f80e00c0eac51f79d0a67201f489814a7ea7b7ddab747a5dda440885b63440
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
- target_id: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  path: data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml
  label: FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml
    role: maintained
scope:
  description: All fields of data/curated/FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
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
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
  command: python3 research/discovery/fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366>mu0=0.01559,
    rate_fedbn=0.5264<rate_fedavg=0.8554, mse_fedbn=1.51e-31<<mse_fedavg_bn=12.7582'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T080900Z-fedbn-federated-learning-non-iid-features-local-bn.json
  accessed_at: '2026-10-19T08:09:00Z'
  support: supports
  summary: No normalized identity match for AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T08:09:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
  accessed_at: '2026-10-19T08:09:00Z'
  snapshot_sha256: 52f80e00c0eac51f79d0a67201f489814a7ea7b7ddab747a5dda440885b63440
  support: supports
  summary: 'All constructed boundary assertions in fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
    passed with exit code 0: [PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366>mu0=0.01559,
    rate_fedbn=0.5264<rate_fedavg=0.8554, mse_fedbn=1.51e-31<<mse_fedavg_bn=12.7582'
- evidence_id: r406-primary-pdf
  kind: primary_source
  reference: https://openreview.net/forum?id=6YEQUn0QICG
  locator: Full-text PDF
  accessed_at: '2026-10-19T08:09:00Z'
  snapshot_sha256: 47b20c25d7729a04b4a7245e3134e561948897df2e57fcf5a07d7bbeb4c8e6c4
  support: supports
  summary: Full-text PDF (International Conference on Learning Representations (ICLR
    2021) (2021)) read and verified.
- evidence_id: r406-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2102.07623
  locator: arXiv abstract
  accessed_at: '2026-10-19T08:09:00Z'
  snapshot_sha256: 17d7f818cc9d69ccefdde08b7b889b7d346c096308ba9d0cc11b94b3cd469507
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r406-metadata-cr
  kind: primary_source
  reference: https://openreview.net/forum?id=6YEQUn0QICG
  locator: Crossref metadata
  accessed_at: '2026-10-19T08:09:00Z'
  snapshot_sha256: 9cc870f1447c3ea813498d84cb409cb55b2bc15535262765f03d6e05ec166e77
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  evidence_ids:
  - identity
  - r406-primary-pdf
  - r406-arxiv-abs
  - r406-metadata-cr
  summary: FedBN (Federated Learning on Non-IID Features via Local Batch Normalization)
    is a distinct concept.
  details: Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization)
    and SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning),
    which synchronize all model layers including Batch Normalization parameters and
    add proximal or control-variate corrections, and from FedRep (AIMech:FedRepExploitingSharedRepresentationsForPersonalizedFederatedLearning,
    which keeps the top classification head h_i local to address heterogeneous label
    conditional distributions P_i(y|x) rather than keeping internal Batch Normalization
    layers local to mitigate feature shift P_i(x)).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  evidence_ids:
  - mapping
  - r406-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  evidence_ids:
  - r406-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in fedbn-federated-learning-non-iid-features-local-bn-boundaries.py
    passed with exit code 0: [PASS] Round 406 FedBN (Li et al. 2021): mu0_star=0.06366>mu0=0.01559,
    rate_fedbn=0.5264<rate_fedavg=0.8554, mse_fedbn=1.51e-31<<mse_fedavg_bn=12.7582'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  evidence_ids:
  - identity
  - mapping
  - r406-primary-pdf
  - r406-arxiv-abs
  - r406-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FedBnFederatedLearningOnNonIidFeaturesViaLocalBatchNormalization
  in Round 406.
- All pages of International Conference on Learning Representations (ICLR 2021) (2021)
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
