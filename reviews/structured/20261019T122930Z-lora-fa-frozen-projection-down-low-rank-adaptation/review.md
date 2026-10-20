# Scientific author self-review of LoRA-FA

- Review: 20261019T122930Z-lora-fa-frozen-projection-down-low-rank-adaptation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T12:29:00Z
- Finished UTC: 2026-10-19T12:29:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain LoRA-FA as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/LoRAFA.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:LoRAFA
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c181edd913b55e8e79354c7bbeba853cb05947ba.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LoRAFA | data/curated/LoRAFA.yaml | maintained | LoRA-FA |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:LoRAFA | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:LoRAFA | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:LoRAFA | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:LoRAFA | Validated history sidecar files. |
| python3 lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py | passed | True | AIMech:LoRAFA | [PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0, err_opt=72.4186&lt;err_raw=56250.7211, dL=-0.2297&lt;0, act_savings=18.0GB |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:LoRAFA.

LoRA-FA is a distinct concept.

Distinct from AIMech:LowRankAdaptation (LoRA), which updates both A in R^{d_{in} x r} and B in R^{r x d_{out}} and must retain the full input activation tensor X in R^{b x s x d_{in}} in GPU memory to compute dL/dA = (alpha/r) X^T (dL/dY) B^T during backpropagation, and from AIMech:LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates (LoRA+), which still updates both A and B with asymmetric learning rates. LoRA-FA (Longteng Zhang, Lin Zhang, Shaohuai Shi, Xiaowen Chu, and Bo Li, arXiv:2308.03303) proves that stacked linear low-rank updates collapse to single-layer linear regression within the column space of A_0 (Theorem 3.1) and derives the closed-form gradient correction g^B = (r/alpha)^2 (A^T A)^{-1} g^B_{LoRA-FA} (Theorem 4.1) that minimizes the Frobenius norm discrepancy &#124;&#124;(alpha/r) A g^B - g&#124;&#124;_F^2 against the full-fine-tuning gradient g while guaranteeing dL &lt;= 0. Because A is frozen, only the r-dimensional intermediate activation X A in R^{b x s x r} (2bsr bytes instead of 2bsd + 2bsr bytes) is stored for backpropagation, and K = (A^T A)^{-1} in R^{r x r} is precomputed once at initialization.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:LoRAFA.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:LoRAFA.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py passed with exit code 0: [PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0, err_opt=72.4186&lt;err_raw=56250.7211, dL=-0.2297&lt;0, act_savings=18.0GB

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:LoRAFA.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T122900Z-lora-fa-frozen-projection-down-low-rank-adaptation.json | supports | No normalized identity match for AIMech:LoRAFA across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py | supports | All constructed boundary assertions in lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py passed with exit code 0: [PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0, err_opt=72.4186&lt;err_raw=56250.7211, dL=-0.2297&lt;0, act_savings=18.0GB |
| r666-primary-pdf | https://arxiv.org/pdf/2308.03303; Full-text PDF | supports | Full-text PDF (arXiv Computing Research Repository (CoRR) (2023)) read and verified. |
| r666-arxiv-abs | https://arxiv.org/abs/2308.03303; arXiv abstract | supports | arXiv abstract read and verified. |
| r666-metadata-cr | https://dblp.org/search/publ/api?q=LoRA-FA+Longteng+Zhang&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:LoRAFA in Round 666.
- All pages of arXiv Computing Research Repository (CoRR) (2023) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T122930Z-lora-fa-frozen-projection-down-low-rank-adaptation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of LoRA-FA
started_at: '2026-10-19T12:29:00Z'
finished_at: '2026-10-19T12:29:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:LoRAFA
    against existing AIMech and AIO records and verified all claims against arXiv
    Computing Research Repository (CoRR) (2023) and pure-Python boundary checks. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain LoRA-FA as a distinct DRAFT algorithm. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: c181edd913b55e8e79354c7bbeba853cb05947ba
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/LoRAFA.yaml
    sha256: 5bd0ec904b60a3cf36efe6ee20a5db7846e82c6e0f00740175104fc27911486f
    role: target
  - path: research/discovery/20261019T122900Z-lora-fa-frozen-projection-down-low-rank-adaptation.json
    sha256: 9cd6f4cf16869fecaecb60cff5b947d2e8909dde2c4a5e51b4a851e7ba43af43
    role: context
  - path: research/discovery/lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
    sha256: 224dd08ff1c289a69671c79b4c7d8c87e2eb6c9bd6454bcab88f1ac0597c8362
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
- target_id: AIMech:LoRAFA
  path: data/curated/LoRAFA.yaml
  label: LoRA-FA
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LoRAFA.yaml
    role: maintained
scope:
  description: All fields of data/curated/LoRAFA.yaml and its primary evidence.
  selection: 'Exact maintained ID: AIMech:LoRAFA'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:LoRAFA
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
  - AIMech:LoRAFA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:LoRAFA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:LoRAFA
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:LoRAFA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
  command: python3 research/discovery/lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LoRAFA
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0, err_opt=72.4186<err_raw=56250.7211,
    dL=-0.2297<0, act_savings=18.0GB'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T122900Z-lora-fa-frozen-projection-down-low-rank-adaptation.json
  accessed_at: '2026-10-19T12:29:00Z'
  support: supports
  summary: No normalized identity match for AIMech:LoRAFA across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T12:29:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
  accessed_at: '2026-10-19T12:29:00Z'
  snapshot_sha256: 224dd08ff1c289a69671c79b4c7d8c87e2eb6c9bd6454bcab88f1ac0597c8362
  support: supports
  summary: 'All constructed boundary assertions in lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
    passed with exit code 0: [PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0,
    err_opt=72.4186<err_raw=56250.7211, dL=-0.2297<0, act_savings=18.0GB'
- evidence_id: r666-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2308.03303
  locator: Full-text PDF
  accessed_at: '2026-10-19T12:29:00Z'
  snapshot_sha256: 92cbd65b03a4342835c497530b6dc1db58a11222c18a454eec28d9f62f51d55d
  support: supports
  summary: Full-text PDF (arXiv Computing Research Repository (CoRR) (2023)) read
    and verified.
- evidence_id: r666-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2308.03303
  locator: arXiv abstract
  accessed_at: '2026-10-19T12:29:00Z'
  snapshot_sha256: 71875b5a677febcea9b41509c28522a30930990444a74e19b72f3408fab420b5
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r666-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=LoRA-FA+Longteng+Zhang&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T12:29:00Z'
  snapshot_sha256: 7d58a9788804b6b609e147128479e1d6db43b80be6db2ecac3785de58f8dfb79
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:LoRAFA
  evidence_ids:
  - identity
  - r666-primary-pdf
  - r666-arxiv-abs
  - r666-metadata-cr
  summary: LoRA-FA is a distinct concept.
  details: Distinct from AIMech:LowRankAdaptation (LoRA), which updates both A in
    R^{d_{in} x r} and B in R^{r x d_{out}} and must retain the full input activation
    tensor X in R^{b x s x d_{in}} in GPU memory to compute dL/dA = (alpha/r) X^T
    (dL/dY) B^T during backpropagation, and from AIMech:LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates
    (LoRA+), which still updates both A and B with asymmetric learning rates. LoRA-FA
    (Longteng Zhang, Lin Zhang, Shaohuai Shi, Xiaowen Chu, and Bo Li, arXiv:2308.03303)
    proves that stacked linear low-rank updates collapse to single-layer linear regression
    within the column space of A_0 (Theorem 3.1) and derives the closed-form gradient
    correction g^B = (r/alpha)^2 (A^T A)^{-1} g^B_{LoRA-FA} (Theorem 4.1) that minimizes
    the Frobenius norm discrepancy ||(alpha/r) A g^B - g||_F^2 against the full-fine-tuning
    gradient g while guaranteeing dL <= 0. Because A is frozen, only the r-dimensional
    intermediate activation X A in R^{b x s x r} (2bsr bytes instead of 2bsd + 2bsr
    bytes) is stored for backpropagation, and K = (A^T A)^{-1} in R^{r x r} is precomputed
    once at initialization.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:LoRAFA
  evidence_ids:
  - mapping
  - r666-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:LoRAFA
  evidence_ids:
  - r666-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in lora-fa-frozen-projection-down-low-rank-adaptation-boundaries.py
    passed with exit code 0: [PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0,
    err_opt=72.4186<err_raw=56250.7211, dL=-0.2297<0, act_savings=18.0GB'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:LoRAFA
  evidence_ids:
  - identity
  - mapping
  - r666-primary-pdf
  - r666-arxiv-abs
  - r666-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:LoRAFA in Round 666.
- All pages of arXiv Computing Research Repository (CoRR) (2023) were read in full
  text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
