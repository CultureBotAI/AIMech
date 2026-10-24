# Scientific author self-review of Compacter (Low-Rank Hypercomplex Adapter Layers)

- Review: 20261019T122230Z-compacter-low-rank-hypercomplex-adapter-layers
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T12:22:00Z
- Finished UTC: 2026-10-19T12:22:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Compacter (Low-Rank Hypercomplex Adapter Layers) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:CompacterLowRankHypercomplexAdapterLayers
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6b8e7538c2d2940cfff668f83987fc7ef0e7b66f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CompacterLowRankHypercomplexAdapterLayers | data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml | maintained | Compacter (Low-Rank Hypercomplex Adapter Layers) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:CompacterLowRankHypercomplexAdapterLayers | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:CompacterLowRankHypercomplexAdapterLayers | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:CompacterLowRankHypercomplexAdapterLayers | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:CompacterLowRankHypercomplexAdapterLayers | Validated history sidecar files. |
| python3 compacter-low-rank-hypercomplex-adapter-layers-boundaries.py | passed | True | AIMech:CompacterLowRankHypercomplexAdapterLayers | [PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): params_adapter=884736 &gt; params_phm=224256 &gt; params_compacter=38080 &gt; params_compacter++=19072, max_diff=4.86e-17, &#124;&#124;W1-W2&#124;&#124;_F=0.7716 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:CompacterLowRankHypercomplexAdapterLayers.

Compacter (Low-Rank Hypercomplex Adapter Layers) is a distinct concept.

Distinct from standard bottleneck adapters (Houlsby et al., 2019), which parameterize U^l and D^l as unconstrained dense matrices costing 4 L k d parameters across L encoder-decoder layers, and from PHM-Adapter, which does not share A_i across layers or factorize B_i into rank-one outer products (costing 4 L (k d / n + n^3) parameters). Also distinct from LoRA (Hu et al., 2022), which adds parallel low-rank updates directly to frozen attention weights without a nonlinear GeLU bottleneck or Kronecker hypercomplex multiplication.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:CompacterLowRankHypercomplexAdapterLayers.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:CompacterLowRankHypercomplexAdapterLayers.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in compacter-low-rank-hypercomplex-adapter-layers-boundaries.py passed with exit code 0: [PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): params_adapter=884736 &gt; params_phm=224256 &gt; params_compacter=38080 &gt; params_compacter++=19072, max_diff=4.86e-17, &#124;&#124;W1-W2&#124;&#124;_F=0.7716

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:CompacterLowRankHypercomplexAdapterLayers.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T122200Z-compacter-low-rank-hypercomplex-adapter-layers.json | supports | No normalized identity match for AIMech:CompacterLowRankHypercomplexAdapterLayers across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/compacter-low-rank-hypercomplex-adapter-layers-boundaries.py | supports | All constructed boundary assertions in compacter-low-rank-hypercomplex-adapter-layers-boundaries.py passed with exit code 0: [PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): params_adapter=884736 &gt; params_phm=224256 &gt; params_compacter=38080 &gt; params_compacter++=19072, max_diff=4.86e-17, &#124;&#124;W1-W2&#124;&#124;_F=0.7716 |
| r659-primary-pdf | https://arxiv.org/pdf/2106.04647.pdf; Full-text PDF | supports | Full-text PDF (Advances in Neural Information Processing Systems 34 (NeurIPS 2021) (2021)) read and verified. |
| r659-arxiv-abs | https://arxiv.org/abs/2106.04647; arXiv abstract | supports | arXiv abstract read and verified. |
| r659-metadata-cr | https://dblp.org/rec/conf/nips/MahabadiHR21.html; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:CompacterLowRankHypercomplexAdapterLayers in Round 659.
- All pages of Advances in Neural Information Processing Systems 34 (NeurIPS 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T122230Z-compacter-low-rank-hypercomplex-adapter-layers
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Compacter (Low-Rank Hypercomplex Adapter Layers)
started_at: '2026-10-19T12:22:00Z'
finished_at: '2026-10-19T12:22:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:CompacterLowRankHypercomplexAdapterLayers
    against existing AIMech and AIO records and verified all claims against Advances
    in Neural Information Processing Systems 34 (NeurIPS 2021) (2021) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Compacter (Low-Rank Hypercomplex Adapter Layers) as a distinct DRAFT
  algorithm. All three claims are supported by full-text primary evidence and pure-Python
  boundary verification.
source:
  git_revision: 6b8e7538c2d2940cfff668f83987fc7ef0e7b66f
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml
    sha256: 1b6d6ddc6dd58f0001ec0b5351d493d9141aa5b728520481041bfaf601154ee1
    role: target
  - path: research/discovery/20261019T122200Z-compacter-low-rank-hypercomplex-adapter-layers.json
    sha256: 139f802ee246ee0e56f9a64ad2d6e20063e7453e19cc6846f4c24fe95b016188
    role: context
  - path: research/discovery/compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
    sha256: 73f8e994287a6beb2af4aeaad54be6528b6a300e44b662d60ae88a0955aef808
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
- target_id: AIMech:CompacterLowRankHypercomplexAdapterLayers
  path: data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml
  label: Compacter (Low-Rank Hypercomplex Adapter Layers)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml
    role: maintained
scope:
  description: All fields of data/curated/CompacterLowRankHypercomplexAdapterLayers.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:CompacterLowRankHypercomplexAdapterLayers'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
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
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
  command: python3 research/discovery/compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021): params_adapter=884736
    > params_phm=224256 > params_compacter=38080 > params_compacter++=19072, max_diff=4.86e-17,
    ||W1-W2||_F=0.7716'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T122200Z-compacter-low-rank-hypercomplex-adapter-layers.json
  accessed_at: '2026-10-19T12:22:00Z'
  support: supports
  summary: No normalized identity match for AIMech:CompacterLowRankHypercomplexAdapterLayers
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T12:22:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
  accessed_at: '2026-10-19T12:22:00Z'
  snapshot_sha256: 73f8e994287a6beb2af4aeaad54be6528b6a300e44b662d60ae88a0955aef808
  support: supports
  summary: 'All constructed boundary assertions in compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
    passed with exit code 0: [PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021):
    params_adapter=884736 > params_phm=224256 > params_compacter=38080 > params_compacter++=19072,
    max_diff=4.86e-17, ||W1-W2||_F=0.7716'
- evidence_id: r659-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2106.04647.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T12:22:00Z'
  snapshot_sha256: ef87e29bf8fadae8d40cb12d1436835142eab0c25bdb0bd3757147c67b193fe4
  support: supports
  summary: Full-text PDF (Advances in Neural Information Processing Systems 34 (NeurIPS
    2021) (2021)) read and verified.
- evidence_id: r659-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2106.04647
  locator: arXiv abstract
  accessed_at: '2026-10-19T12:22:00Z'
  snapshot_sha256: 7588d8592cb38ee2fade0c7cb10e8b29fd6af0ba9581c03fa8feba4a32b0e7c7
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r659-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/conf/nips/MahabadiHR21.html
  locator: Crossref metadata
  accessed_at: '2026-10-19T12:22:00Z'
  snapshot_sha256: 339bb4474dad810e63a69952067735c8a6a4ca6440e795b3d455062834e9b770
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  evidence_ids:
  - identity
  - r659-primary-pdf
  - r659-arxiv-abs
  - r659-metadata-cr
  summary: Compacter (Low-Rank Hypercomplex Adapter Layers) is a distinct concept.
  details: Distinct from standard bottleneck adapters (Houlsby et al., 2019), which
    parameterize U^l and D^l as unconstrained dense matrices costing 4 L k d parameters
    across L encoder-decoder layers, and from PHM-Adapter, which does not share A_i
    across layers or factorize B_i into rank-one outer products (costing 4 L (k d
    / n + n^3) parameters). Also distinct from LoRA (Hu et al., 2022), which adds
    parallel low-rank updates directly to frozen attention weights without a nonlinear
    GeLU bottleneck or Kronecker hypercomplex multiplication.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  evidence_ids:
  - mapping
  - r659-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  evidence_ids:
  - r659-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in compacter-low-rank-hypercomplex-adapter-layers-boundaries.py
    passed with exit code 0: [PASS] Round 659 Compacter (Karimi Mahabadi et al. 2021):
    params_adapter=884736 > params_phm=224256 > params_compacter=38080 > params_compacter++=19072,
    max_diff=4.86e-17, ||W1-W2||_F=0.7716'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:CompacterLowRankHypercomplexAdapterLayers
  evidence_ids:
  - identity
  - mapping
  - r659-primary-pdf
  - r659-arxiv-abs
  - r659-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:CompacterLowRankHypercomplexAdapterLayers in Round 659.
- All pages of Advances in Neural Information Processing Systems 34 (NeurIPS 2021)
  (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
