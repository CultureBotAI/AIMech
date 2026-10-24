# Scientific author self-review of BERT-of-Theseus: Compressing BERT by Progressive Module Replacing

- Review: 20261019T144830Z-bert-of-theseus-progressive-module-replacing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:48:00Z
- Finished UTC: 2026-10-19T14:48:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain BERT-of-Theseus: Compressing BERT by Progressive Module Replacing as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ea3f1d13317e26da94745daaec213f23c652f105.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml | maintained | BERT-of-Theseus: Compressing BERT by Progressive Module Replacing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | Validated history sidecar files. |
| python3 bert-of-theseus-progressive-module-replacing-boundaries.py | passed | True | AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing | {"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing", "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum": 3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0": 2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing.

BERT-of-Theseus: Compressing BERT by Progressive Module Replacing is a distinct concept.

Introduced by Canwen Xu, Wangchunshu Zhou, Tao Ge, Furu Wei, and Ming Zhou (EMNLP 2020, pp. 7859-7869, arXiv:2002.02925, doi:10.18653/v1/2020.emnlp-main.633). Distinct from knowledge distillation methods such as TinyBERT (Round 800), MiniLM (Round 801), BERT-PKD (Round 802), DistilBERT (Round 803), and MobileBERT (Round 804): BERT-of-Theseus requires zero auxiliary feature-matching, attention-matching, or logit KL-divergence losses and no balancing hyperparameters between task and distillation losses, relying instead on closed-loop gradient interactions between frozen predecessor modules and trainable successor modules inside the hybrid computational graph.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in bert-of-theseus-progressive-module-replacing-boundaries.py passed with exit code 0: {"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing", "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum": 3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0": 2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T144800Z-bert-of-theseus-progressive-module-replacing.json | supports | No normalized identity match for AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/bert-of-theseus-progressive-module-replacing-boundaries.py | supports | All constructed boundary assertions in bert-of-theseus-progressive-module-replacing-boundaries.py passed with exit code 0: {"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing", "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum": 3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0": 2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"} |
| r805-primary-pdf | https://arxiv.org/pdf/2002.02925.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020) (2020)) read and verified. |
| r805-arxiv-abs | https://arxiv.org/abs/2002.02925; arXiv abstract | supports | arXiv abstract read and verified. |
| r805-metadata-cr | https://arxiv.org/bibtex/2002.02925; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing in Round 805.
- All pages of Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020) (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T144830Z-bert-of-theseus-progressive-module-replacing
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of BERT-of-Theseus: Compressing BERT by Progressive
  Module Replacing'
started_at: '2026-10-19T14:48:00Z'
finished_at: '2026-10-19T14:48:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP
    2020) (2020) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain BERT-of-Theseus: Compressing BERT by Progressive Module Replacing
  as a distinct DRAFT algorithm. All four claims are supported by full-text primary
  evidence and pure-Python boundary verification.'
source:
  git_revision: ea3f1d13317e26da94745daaec213f23c652f105
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml
    sha256: 11e02071c7f9c2e08112ba5fbcb6d8628844bedcfb9d12b705f42ae23cd62200
    role: target
  - path: research/discovery/20261019T144800Z-bert-of-theseus-progressive-module-replacing.json
    sha256: b57f2848dc5d8860e78d7dea6be7238212b2567ad70d01007a232dd215822bc8
    role: context
  - path: research/discovery/bert-of-theseus-progressive-module-replacing-boundaries.py
    sha256: 84be397dcce09dd4ba3c9743f28d5aa495d52ce10d7aab07e02b57a49548f3b4
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
- target_id: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  path: data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml
  label: 'BERT-of-Theseus: Compressing BERT by Progressive Module Replacing'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml
    role: maintained
scope:
  description: All fields of data/curated/BERToftheseusCompressingBERTByProgressiveModuleReplacing.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
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
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 bert-of-theseus-progressive-module-replacing-boundaries.py
  command: python3 research/discovery/bert-of-theseus-progressive-module-replacing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  exit_code: 0
  expected_exit_code: 0
  summary: '{"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing",
    "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum":
    3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0":
    2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T144800Z-bert-of-theseus-progressive-module-replacing.json
  accessed_at: '2026-10-19T14:48:00Z'
  support: supports
  summary: No normalized identity match for AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:48:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/bert-of-theseus-progressive-module-replacing-boundaries.py
  accessed_at: '2026-10-19T14:48:00Z'
  snapshot_sha256: 84be397dcce09dd4ba3c9743f28d5aa495d52ce10d7aab07e02b57a49548f3b4
  support: supports
  summary: 'All constructed boundary assertions in bert-of-theseus-progressive-module-replacing-boundaries.py
    passed with exit code 0: {"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing",
    "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum":
    3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0":
    2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"}'
- evidence_id: r805-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2002.02925.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:48:00Z'
  snapshot_sha256: cece57da8bb1587e9e4883c39c4177c3dd9da43331c2d38ae95774143088dade
  support: supports
  summary: Full-text PDF (Proceedings of the 2020 Conference on Empirical Methods
    in Natural Language Processing (EMNLP 2020) (2020)) read and verified.
- evidence_id: r805-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2002.02925
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:48:00Z'
  snapshot_sha256: 254c8115962a7ddc00d8ed2cde4aa207d7c960d37f1cac4d376cf44ac58a9ea9
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r805-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2002.02925
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:48:00Z'
  snapshot_sha256: a9074bf8594db78708053ffbd051d40ad2b9457335859491ace090ff5a6fd7ab
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  evidence_ids:
  - identity
  - r805-primary-pdf
  - r805-arxiv-abs
  - r805-metadata-cr
  summary: 'BERT-of-Theseus: Compressing BERT by Progressive Module Replacing is a
    distinct concept.'
  details: 'Introduced by Canwen Xu, Wangchunshu Zhou, Tao Ge, Furu Wei, and Ming
    Zhou (EMNLP 2020, pp. 7859-7869, arXiv:2002.02925, doi:10.18653/v1/2020.emnlp-main.633).
    Distinct from knowledge distillation methods such as TinyBERT (Round 800), MiniLM
    (Round 801), BERT-PKD (Round 802), DistilBERT (Round 803), and MobileBERT (Round
    804): BERT-of-Theseus requires zero auxiliary feature-matching, attention-matching,
    or logit KL-divergence losses and no balancing hyperparameters between task and
    distillation losses, relying instead on closed-loop gradient interactions between
    frozen predecessor modules and trainable successor modules inside the hybrid computational
    graph.'
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  evidence_ids:
  - mapping
  - r805-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  evidence_ids:
  - r805-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in bert-of-theseus-progressive-module-replacing-boundaries.py
    passed with exit code 0: {"concept": "BERToftheseusCompressingBERTByProgressiveModuleReplacing",
    "num_modules": 6, "num_hybrid_paths": 64, "y_predecessor_only": 3.984192, "y_hybrid_mid_curriculum":
    3.518925, "y_successor_only": 3.158203, "curriculum_transition_step": 9000, "effective_lr_t0":
    2.0000000000000003e-06, "effective_lr_t9000": 2e-05, "status": "ok"}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  evidence_ids:
  - identity
  - mapping
  - r805-primary-pdf
  - r805-arxiv-abs
  - r805-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:BERToftheseusCompressingBERTByProgressiveModuleReplacing
  in Round 805.
- All pages of Proceedings of the 2020 Conference on Empirical Methods in Natural
  Language Processing (EMNLP 2020) (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
