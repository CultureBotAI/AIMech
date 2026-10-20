# Scientific author self-review of Instance-Dependent Prompt Generation

- Review: 20261019T131430Z-idpg-instance-dependent-prompt-generation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:14:00Z
- Finished UTC: 2026-10-19T13:14:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Instance-Dependent Prompt Generation as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/IDPGInstanceDependentPromptGeneration.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:IDPGInstanceDependentPromptGeneration
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b68acce0656bd87c76d7f20e4eb33046d216f85b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:IDPGInstanceDependentPromptGeneration | data/curated/IDPGInstanceDependentPromptGeneration.yaml | maintained | Instance-Dependent Prompt Generation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:IDPGInstanceDependentPromptGeneration | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:IDPGInstanceDependentPromptGeneration | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:IDPGInstanceDependentPromptGeneration | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:IDPGInstanceDependentPromptGeneration | Validated history sidecar files. |
| python3 idpg-instance-dependent-prompt-generation-boundaries.py | passed | True | AIMech:IDPGInstanceDependentPromptGeneration | [PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362&gt;0, diff_static=0.0e+00 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:IDPGInstanceDependentPromptGeneration.

Instance-Dependent Prompt Generation is a distinct concept.

Introduced by Zhuofeng Wu, Sinong Wang, Jiatao Gu, Rui Hou, Yuxiao Dong, V. G. Vinod Vydiswaran, and Hao Ma (NAACL 2022, arXiv:2204.04497) as Instance-Dependent Prompt Generation (IDPG / S-IDPG-PHM / M-IDPG-PHM). Distinct from static Prompt Tuning and SPoT (AIMech:SPoTSoftPromptTransfer), which use a fixed input-independent prompt per task (recovered as the degenerate case W = 0 in IDPG where only the second-layer bias is active); from ATTEMPT (AIMech:ATTEMPTAttentionalMixturesOfSoftPrompts), which interpolates pre-trained source-task prompts via sub-query attention rather than generating prompts through a PHM bottleneck MLP; and from Hyperdecoder (AIMech:HyperdecoderInstanceSpecificDecoderAdapter), which generates decoder adapter weights from encoder hidden states rather than layer-wise soft prompt tokens.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:IDPGInstanceDependentPromptGeneration.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:IDPGInstanceDependentPromptGeneration.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in idpg-instance-dependent-prompt-generation-boundaries.py passed with exit code 0: [PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362&gt;0, diff_static=0.0e+00

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:IDPGInstanceDependentPromptGeneration.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T131400Z-idpg-instance-dependent-prompt-generation.json | supports | No normalized identity match for AIMech:IDPGInstanceDependentPromptGeneration across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/idpg-instance-dependent-prompt-generation-boundaries.py | supports | All constructed boundary assertions in idpg-instance-dependent-prompt-generation-boundaries.py passed with exit code 0: [PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362&gt;0, diff_static=0.0e+00 |
| r711-primary-pdf | https://arxiv.org/pdf/2204.04497.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022)) read and verified. |
| r711-arxiv-abs | https://arxiv.org/abs/2204.04497; arXiv abstract | supports | arXiv abstract read and verified. |
| r711-metadata-cr | https://dblp.org/search/publ/api?q=IDPG+An+Instance-Dependent+Prompt+Generation+Method&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:IDPGInstanceDependentPromptGeneration in Round 711.
- All pages of Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T131430Z-idpg-instance-dependent-prompt-generation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Instance-Dependent Prompt Generation
started_at: '2026-10-19T13:14:00Z'
finished_at: '2026-10-19T13:14:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:IDPGInstanceDependentPromptGeneration
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2022 Conference of the North American Chapter of the Association for Computational
    Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Instance-Dependent Prompt Generation as a distinct DRAFT algorithm.
  All three claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: b68acce0656bd87c76d7f20e4eb33046d216f85b
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/IDPGInstanceDependentPromptGeneration.yaml
    sha256: 7cc765e20214dc20a47c33023b01774a31a7ff6316aca4282e0f35252f04476a
    role: target
  - path: research/discovery/20261019T131400Z-idpg-instance-dependent-prompt-generation.json
    sha256: 7b86b363c42a43c91adae38555f94a0fb352dc90e07e2a827b6cfd815a72471e
    role: context
  - path: research/discovery/idpg-instance-dependent-prompt-generation-boundaries.py
    sha256: e70f193db90394b1db6ce4b58f2cf4cf51caa326632a3cfb45c8ffcfd8ba0f52
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
- target_id: AIMech:IDPGInstanceDependentPromptGeneration
  path: data/curated/IDPGInstanceDependentPromptGeneration.yaml
  label: Instance-Dependent Prompt Generation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IDPGInstanceDependentPromptGeneration.yaml
    role: maintained
scope:
  description: All fields of data/curated/IDPGInstanceDependentPromptGeneration.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:IDPGInstanceDependentPromptGeneration'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
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
  - AIMech:IDPGInstanceDependentPromptGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 idpg-instance-dependent-prompt-generation-boundaries.py
  command: python3 research/discovery/idpg-instance-dependent-prompt-generation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs DNN=1541.2K, M-IDPG-PHM=134K,
    diff_inst=8.4362>0, diff_static=0.0e+00'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T131400Z-idpg-instance-dependent-prompt-generation.json
  accessed_at: '2026-10-19T13:14:00Z'
  support: supports
  summary: No normalized identity match for AIMech:IDPGInstanceDependentPromptGeneration
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:14:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/idpg-instance-dependent-prompt-generation-boundaries.py
  accessed_at: '2026-10-19T13:14:00Z'
  snapshot_sha256: e70f193db90394b1db6ce4b58f2cf4cf51caa326632a3cfb45c8ffcfd8ba0f52
  support: supports
  summary: 'All constructed boundary assertions in idpg-instance-dependent-prompt-generation-boundaries.py
    passed with exit code 0: [PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs
    DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362>0, diff_static=0.0e+00'
- evidence_id: r711-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2204.04497.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:14:00Z'
  snapshot_sha256: bc7419642a39683264bb873422fe707232972b73f7975d120e63da4ea7c3ddfa
  support: supports
  summary: 'Full-text PDF (Proceedings of the 2022 Conference of the North American
    Chapter of the Association for Computational Linguistics: Human Language Technologies
    (NAACL-HLT 2022) (2022)) read and verified.'
- evidence_id: r711-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2204.04497
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:14:00Z'
  snapshot_sha256: 0fe36615990405d389cf60fde0d02f509f9dbb82688a8e49a95f8d85216c5539
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r711-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=IDPG+An+Instance-Dependent+Prompt+Generation+Method&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:14:00Z'
  snapshot_sha256: 86944201b50982d32b84c5a48d30f5bec484acb5f72736a48ba02adb4dc3a4c1
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  evidence_ids:
  - identity
  - r711-primary-pdf
  - r711-arxiv-abs
  - r711-metadata-cr
  summary: Instance-Dependent Prompt Generation is a distinct concept.
  details: Introduced by Zhuofeng Wu, Sinong Wang, Jiatao Gu, Rui Hou, Yuxiao Dong,
    V. G. Vinod Vydiswaran, and Hao Ma (NAACL 2022, arXiv:2204.04497) as Instance-Dependent
    Prompt Generation (IDPG / S-IDPG-PHM / M-IDPG-PHM). Distinct from static Prompt
    Tuning and SPoT (AIMech:SPoTSoftPromptTransfer), which use a fixed input-independent
    prompt per task (recovered as the degenerate case W = 0 in IDPG where only the
    second-layer bias is active); from ATTEMPT (AIMech:ATTEMPTAttentionalMixturesOfSoftPrompts),
    which interpolates pre-trained source-task prompts via sub-query attention rather
    than generating prompts through a PHM bottleneck MLP; and from Hyperdecoder (AIMech:HyperdecoderInstanceSpecificDecoderAdapter),
    which generates decoder adapter weights from encoder hidden states rather than
    layer-wise soft prompt tokens.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  evidence_ids:
  - mapping
  - r711-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  evidence_ids:
  - r711-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in idpg-instance-dependent-prompt-generation-boundaries.py
    passed with exit code 0: [PASS] IDPG boundaries verified: S-IDPG-PHM=105.25K vs
    DNN=1541.2K, M-IDPG-PHM=134K, diff_inst=8.4362>0, diff_static=0.0e+00'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:IDPGInstanceDependentPromptGeneration
  evidence_ids:
  - identity
  - mapping
  - r711-primary-pdf
  - r711-arxiv-abs
  - r711-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:IDPGInstanceDependentPromptGeneration in Round 711.
- 'All pages of Proceedings of the 2022 Conference of the North American Chapter of
  the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT
  2022) (2022) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
