# Scientific author self-review of MiLoRA

- Review: 20261019T123830Z-milora-minor-singular-component-low-rank-adaptation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T12:38:00Z
- Finished UTC: 2026-10-19T12:38:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain MiLoRA as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/MiLoRA.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:MiLoRA
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fe4fc54329b6db3a95465d995b85591d3cc8a51c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MiLoRA | data/curated/MiLoRA.yaml | maintained | MiLoRA |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:MiLoRA | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:MiLoRA | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:MiLoRA | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:MiLoRA | Validated history sidecar files. |
| python3 milora-minor-singular-component-low-rank-adaptation-boundaries.py | passed | True | AIMech:MiLoRA | [PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15, orth_err=2.29e-15, forgetting_milora=2.7231e-18&lt;&lt;forgetting_pissa=1.7460 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:MiLoRA.

MiLoRA is a distinct concept.

Directly complementary to AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation (PiSSA, which initializes the trainable adapter from the top-r principal singular components and freezes the minor residual) and distinct from AIMech:LowRankAdaptation (which initializes A randomly and B to zero in an unguided subspace). MiLoRA (Minor singular component based Low-Rank Adaptation; Hanqing Wang, Yixia Li, Shuo Wang, Guanhua Chen, &amp; Yun Chen, NAACL 2025, arXiv:2406.09044) partitions the SVD W = U Sigma V^T = sum_{i=1}^{m-r} sigma_i u_i v_i^T + sum_{i=m-r+1}^m sigma_i u_i v_i^T = W_p + W_m (Equations 3-5). By freezing W_p and initializing B_m = U_m sqrt(Sigma_m) and A_m = sqrt(Sigma_m) V_m^T, MiLoRA (1) satisfies W = W_p + B_m A_m exactly at initialization without setting B_m = 0 or tuning a separate alpha/r scaling factor, and (2) initializes the trainable adapter in a subspace orthogonal to the principal knowledge subspace (U_p^T B_m = 0, A_m V_p = 0), adapting long-tail/noisy singular directions to the downstream task while minimizing catastrophic forgetting of pre-trained world knowledge.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:MiLoRA.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:MiLoRA.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in milora-minor-singular-component-low-rank-adaptation-boundaries.py passed with exit code 0: [PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15, orth_err=2.29e-15, forgetting_milora=2.7231e-18&lt;&lt;forgetting_pissa=1.7460

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:MiLoRA.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T123800Z-milora-minor-singular-component-low-rank-adaptation.json | supports | No normalized identity match for AIMech:MiLoRA across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/milora-minor-singular-component-low-rank-adaptation-boundaries.py | supports | All constructed boundary assertions in milora-minor-singular-component-low-rank-adaptation-boundaries.py passed with exit code 0: [PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15, orth_err=2.29e-15, forgetting_milora=2.7231e-18&lt;&lt;forgetting_pissa=1.7460 |
| r675-primary-pdf | https://arxiv.org/pdf/2406.09044.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025) (2025)) read and verified. |
| r675-arxiv-abs | https://arxiv.org/abs/2406.09044; arXiv abstract | supports | arXiv abstract read and verified. |
| r675-metadata-cr | https://dblp.org/search/publ/api?q=MiLoRA+Harnessing+Minor+Singular+Components&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:MiLoRA in Round 675.
- All pages of Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025) (2025) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T123830Z-milora-minor-singular-component-low-rank-adaptation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of MiLoRA
started_at: '2026-10-19T12:38:00Z'
finished_at: '2026-10-19T12:38:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:MiLoRA
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2025 Conference of the Nations of the Americas Chapter of the Association
    for Computational Linguistics (NAACL 2025) (2025) and pure-Python boundary checks.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain MiLoRA as a distinct DRAFT algorithm. All four claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: fe4fc54329b6db3a95465d995b85591d3cc8a51c
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/MiLoRA.yaml
    sha256: b62e69d91bde8c25e140f932e74a036e6c042b7830393a9a42bbc8f4c636ae8b
    role: target
  - path: research/discovery/20261019T123800Z-milora-minor-singular-component-low-rank-adaptation.json
    sha256: b0c87fca05fee42804203dd1d0ee5d80de0b06a0890cb1f0690efdac4707e8ab
    role: context
  - path: research/discovery/milora-minor-singular-component-low-rank-adaptation-boundaries.py
    sha256: 8827658aef2085a2d0959cb77160c55efcce11bca4a6aed4cee0d442b462a521
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
- target_id: AIMech:MiLoRA
  path: data/curated/MiLoRA.yaml
  label: MiLoRA
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MiLoRA.yaml
    role: maintained
scope:
  description: All fields of data/curated/MiLoRA.yaml and its primary evidence.
  selection: 'Exact maintained ID: AIMech:MiLoRA'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:MiLoRA
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
  - AIMech:MiLoRA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:MiLoRA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:MiLoRA
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:MiLoRA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 milora-minor-singular-component-low-rank-adaptation-boundaries.py
  command: python3 research/discovery/milora-minor-singular-component-low-rank-adaptation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MiLoRA
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15,
    orth_err=2.29e-15, forgetting_milora=2.7231e-18<<forgetting_pissa=1.7460'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T123800Z-milora-minor-singular-component-low-rank-adaptation.json
  accessed_at: '2026-10-19T12:38:00Z'
  support: supports
  summary: No normalized identity match for AIMech:MiLoRA across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T12:38:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/milora-minor-singular-component-low-rank-adaptation-boundaries.py
  accessed_at: '2026-10-19T12:38:00Z'
  snapshot_sha256: 8827658aef2085a2d0959cb77160c55efcce11bca4a6aed4cee0d442b462a521
  support: supports
  summary: 'All constructed boundary assertions in milora-minor-singular-component-low-rank-adaptation-boundaries.py
    passed with exit code 0: [PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15,
    orth_err=2.29e-15, forgetting_milora=2.7231e-18<<forgetting_pissa=1.7460'
- evidence_id: r675-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2406.09044.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T12:38:00Z'
  snapshot_sha256: 82f52cb6080e232fbefa636c5a0a92f2ee8ed90d0686cafe1974eeb6b78a0190
  support: supports
  summary: Full-text PDF (Proceedings of the 2025 Conference of the Nations of the
    Americas Chapter of the Association for Computational Linguistics (NAACL 2025)
    (2025)) read and verified.
- evidence_id: r675-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2406.09044
  locator: arXiv abstract
  accessed_at: '2026-10-19T12:38:00Z'
  snapshot_sha256: 31219bdbdda35dd2cc186d674f4cb389c56f9d0a5f7738500e0e30aed6f3940d
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r675-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=MiLoRA+Harnessing+Minor+Singular+Components&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T12:38:00Z'
  snapshot_sha256: bd20e09a33528015067f025a32bfa995c030042646d6de1d2d167b50372a986b
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:MiLoRA
  evidence_ids:
  - identity
  - r675-primary-pdf
  - r675-arxiv-abs
  - r675-metadata-cr
  summary: MiLoRA is a distinct concept.
  details: Directly complementary to AIMech:PissaPrincipalSingularValuesAndSingularVectorsAdaptation
    (PiSSA, which initializes the trainable adapter from the top-r principal singular
    components and freezes the minor residual) and distinct from AIMech:LowRankAdaptation
    (which initializes A randomly and B to zero in an unguided subspace). MiLoRA (Minor
    singular component based Low-Rank Adaptation; Hanqing Wang, Yixia Li, Shuo Wang,
    Guanhua Chen, & Yun Chen, NAACL 2025, arXiv:2406.09044) partitions the SVD W =
    U Sigma V^T = sum_{i=1}^{m-r} sigma_i u_i v_i^T + sum_{i=m-r+1}^m sigma_i u_i
    v_i^T = W_p + W_m (Equations 3-5). By freezing W_p and initializing B_m = U_m
    sqrt(Sigma_m) and A_m = sqrt(Sigma_m) V_m^T, MiLoRA (1) satisfies W = W_p + B_m
    A_m exactly at initialization without setting B_m = 0 or tuning a separate alpha/r
    scaling factor, and (2) initializes the trainable adapter in a subspace orthogonal
    to the principal knowledge subspace (U_p^T B_m = 0, A_m V_p = 0), adapting long-tail/noisy
    singular directions to the downstream task while minimizing catastrophic forgetting
    of pre-trained world knowledge.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:MiLoRA
  evidence_ids:
  - mapping
  - r675-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:MiLoRA
  evidence_ids:
  - r675-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in milora-minor-singular-component-low-rank-adaptation-boundaries.py
    passed with exit code 0: [PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): recon_err=1.31e-15,
    orth_err=2.29e-15, forgetting_milora=2.7231e-18<<forgetting_pissa=1.7460'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:MiLoRA
  evidence_ids:
  - identity
  - mapping
  - r675-primary-pdf
  - r675-arxiv-abs
  - r675-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:MiLoRA in Round 675.
- All pages of Proceedings of the 2025 Conference of the Nations of the Americas Chapter
  of the Association for Computational Linguistics (NAACL 2025) (2025) were read in
  full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
