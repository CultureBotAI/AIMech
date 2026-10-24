# Scientific author self-review of COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval

- Review: 20261019T135830Z-coco-dr-contrastive-distributionally-robust-dense-retrieval
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:58:00Z
- Finished UTC: 2026-10-19T13:58:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a97a59d0bb83fa44042d14f6e9c3cb26ef2cc5b4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml | maintained | COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | Validated history sidecar files. |
| python3 coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py | passed | True | AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning | Round 755 COCO-DR boundary verification passed. |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.

COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval is a distinct concept.

Distinct from coCondenser (Gao &amp; Callan, ACL 2022, AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining), which pre-trains on the source corpus (e.g., MS MARCO) and fine-tunes with uniform Empirical Risk Minimization without target-corpus adaptation or iDRO query-cluster reweighting; distinct from GPL (Wang et al., NAACL 2022, AIMech:GPLGenerativePseudoLabelingForDenseRetrieval), which generates synthetic queries and cross-encoder pseudo-labels to train a separate model per target task rather than a single unified zero-shot model; and distinct from GroupDRO (Sagawa et al., ICLR 2020, AIMech:GroupDistributionallyRobustOptimization), which weights groups solely by loss magnitude without the cross-cluster gradient dot-product similarity r_{ij}.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py passed with exit code 0: Round 755 COCO-DR boundary verification passed.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T135800Z-coco-dr-contrastive-distributionally-robust-dense-retrieval.json | supports | No normalized identity match for AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py | supports | All constructed boundary assertions in coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py passed with exit code 0: Round 755 COCO-DR boundary verification passed. |
| r755-primary-pdf | https://arxiv.org/pdf/2210.15212.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022), pp. 1462-1479 (2022)) read and verified. |
| r755-arxiv-abs | https://arxiv.org/abs/2210.15212; arXiv abstract | supports | arXiv abstract read and verified. |
| r755-metadata-cr | https://arxiv.org/bibtex/2210.15212; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning in Round 755.
- All pages of Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022), pp. 1462-1479 (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T135830Z-coco-dr-contrastive-distributionally-robust-dense-retrieval
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of COCO-DR Contrastive and Distributionally Robust
  Zero-Shot Dense Retrieval
started_at: '2026-10-19T13:58:00Z'
finished_at: '2026-10-19T13:58:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP
    2022), pp. 1462-1479 (2022) and pure-Python boundary checks. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval
  as a distinct DRAFT algorithm. All four claims are supported by full-text primary
  evidence and pure-Python boundary verification.
source:
  git_revision: a97a59d0bb83fa44042d14f6e9c3cb26ef2cc5b4
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml
    sha256: 2df22e94d92ca61c776ee9812c6d730343580ceb6bda9645d9d37ad29d96e4ee
    role: target
  - path: research/discovery/20261019T135800Z-coco-dr-contrastive-distributionally-robust-dense-retrieval.json
    sha256: a92204ac7b4caf5b978a866d460adb1abbe186a9b66c2db82cd48f108b9099c7
    role: context
  - path: research/discovery/coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
    sha256: 3ce9621dd18b946a6c195dbc0c82ead5f84cf74f0203e99879a1f5f95f47fd06
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
- target_id: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  path: data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml
  label: COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml
    role: maintained
scope:
  description: All fields of data/curated/COCODRDenseRetrievalDistributionallyRobustContrastiveLearning.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
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
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
  command: python3 research/discovery/coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Round 755 COCO-DR boundary verification passed.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T135800Z-coco-dr-contrastive-distributionally-robust-dense-retrieval.json
  accessed_at: '2026-10-19T13:58:00Z'
  support: supports
  summary: No normalized identity match for AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:58:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
  accessed_at: '2026-10-19T13:58:00Z'
  snapshot_sha256: 3ce9621dd18b946a6c195dbc0c82ead5f84cf74f0203e99879a1f5f95f47fd06
  support: supports
  summary: 'All constructed boundary assertions in coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
    passed with exit code 0: Round 755 COCO-DR boundary verification passed.'
- evidence_id: r755-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2210.15212.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:58:00Z'
  snapshot_sha256: 1343e4dc99eef4931b56f02fd3be5dad6621fe287cfe55c4ca382dfca04bc9b1
  support: supports
  summary: Full-text PDF (Proceedings of the 2022 Conference on Empirical Methods
    in Natural Language Processing (EMNLP 2022), pp. 1462-1479 (2022)) read and verified.
- evidence_id: r755-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2210.15212
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:58:00Z'
  snapshot_sha256: 263f6d44686a6a3d9f25362319916d7f9fec74d32fb4da2f227192e9a4d32c07
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r755-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2210.15212
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:58:00Z'
  snapshot_sha256: 270f788b3e3a5255ce2ad52baef997c656ea18c02824c9a978e27d17277c5e9a
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  evidence_ids:
  - identity
  - r755-primary-pdf
  - r755-arxiv-abs
  - r755-metadata-cr
  summary: COCO-DR Contrastive and Distributionally Robust Zero-Shot Dense Retrieval
    is a distinct concept.
  details: Distinct from coCondenser (Gao & Callan, ACL 2022, AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining),
    which pre-trains on the source corpus (e.g., MS MARCO) and fine-tunes with uniform
    Empirical Risk Minimization without target-corpus adaptation or iDRO query-cluster
    reweighting; distinct from GPL (Wang et al., NAACL 2022, AIMech:GPLGenerativePseudoLabelingForDenseRetrieval),
    which generates synthetic queries and cross-encoder pseudo-labels to train a separate
    model per target task rather than a single unified zero-shot model; and distinct
    from GroupDRO (Sagawa et al., ICLR 2020, AIMech:GroupDistributionallyRobustOptimization),
    which weights groups solely by loss magnitude without the cross-cluster gradient
    dot-product similarity r_{ij}.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  evidence_ids:
  - mapping
  - r755-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  evidence_ids:
  - r755-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in coco-dr-contrastive-distributionally-robust-dense-retrieval-boundaries.py
    passed with exit code 0: Round 755 COCO-DR boundary verification passed.'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  evidence_ids:
  - identity
  - mapping
  - r755-primary-pdf
  - r755-arxiv-abs
  - r755-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning
  in Round 755.
- All pages of Proceedings of the 2022 Conference on Empirical Methods in Natural
  Language Processing (EMNLP 2022), pp. 1462-1479 (2022) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
