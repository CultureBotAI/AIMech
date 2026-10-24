# Scientific author self-review of HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts)

- Review: 20261019T130930Z-hyperprompt-task-conditioned-attention-prompts
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:09:00Z
- Finished UTC: 2026-10-19T13:09:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts) as a distinct DRAFT architecture. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HyperPromptTaskConditionedAttentionPrompt
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d5a297a94c1012cecd618f219a28e331a0f44ec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HyperPromptTaskConditionedAttentionPrompt | data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml | maintained | HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HyperPromptTaskConditionedAttentionPrompt | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HyperPromptTaskConditionedAttentionPrompt | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HyperPromptTaskConditionedAttentionPrompt | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HyperPromptTaskConditionedAttentionPrompt | Validated history sidecar files. |
| python3 hyperprompt-task-conditioned-attention-prompts-boundaries.py | passed | True | AIMech:HyperPromptTaskConditionedAttentionPrompt | [PASS] HyperPrompt boundaries verified: params_global=4842752 &lt; params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4) |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HyperPromptTaskConditionedAttentionPrompt.

HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts) is a distinct concept.

Introduced by Yun He, Huaixiu Steven Zheng, Yi Tay, Jai Gupta, Yu Du, Vamsi Aribandi, Zhe Zhao, YaGuang Li, Zhao Chen, Donald Metzler, Heng-Tze Cheng, and Ed H. Chi (ICML 2022, PMLR 162:8678-8690, arXiv:2203.00759). Distinct from Prefix-Tuning (Li &amp; Liang, ACL 2021; AIMech:PrefixTuning), which optimizes single-task per-layer prefixes without cross-task hypernetworks or global-to-local bottleneck projections, and distinct from HyperFormer (Karimi Mahabadi et al., ACL 2021; AIMech Round 703), which generates post-FFN sequential adapter layers rather than self-attention key/value memory tokens. All three architectural variants (HyperPrompt-Share, HyperPrompt-Sep, and HyperPrompt-Global) are covered within this single record.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HyperPromptTaskConditionedAttentionPrompt.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HyperPromptTaskConditionedAttentionPrompt.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in hyperprompt-task-conditioned-attention-prompts-boundaries.py passed with exit code 0: [PASS] HyperPrompt boundaries verified: params_global=4842752 &lt; params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4)

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HyperPromptTaskConditionedAttentionPrompt.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T130900Z-hyperprompt-task-conditioned-attention-prompts.json | supports | No normalized identity match for AIMech:HyperPromptTaskConditionedAttentionPrompt across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/hyperprompt-task-conditioned-attention-prompts-boundaries.py | supports | All constructed boundary assertions in hyperprompt-task-conditioned-attention-prompts-boundaries.py passed with exit code 0: [PASS] HyperPrompt boundaries verified: params_global=4842752 &lt; params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4) |
| r706-primary-pdf | https://arxiv.org/pdf/2203.00759.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 39th International Conference on Machine Learning (ICML 2022), PMLR 162:8678-8690 (2022)) read and verified. |
| r706-arxiv-abs | https://arxiv.org/abs/2203.00759; arXiv abstract | supports | arXiv abstract read and verified. |
| r706-metadata-cr | https://dblp.org/search/publ/api?q=HyperPrompt+Prompt-based+Task-Conditioning&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyperPromptTaskConditionedAttentionPrompt in Round 706.
- All pages of Proceedings of the 39th International Conference on Machine Learning (ICML 2022), PMLR 162:8678-8690 (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T130930Z-hyperprompt-task-conditioned-attention-prompts
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of HyperPrompt (HyperNetwork-Generated Task-Conditioned
  Self-Attention Prompts)
started_at: '2026-10-19T13:09:00Z'
finished_at: '2026-10-19T13:09:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:HyperPromptTaskConditionedAttentionPrompt
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 39th International Conference on Machine Learning (ICML 2022), PMLR 162:8678-8690
    (2022) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention
  Prompts) as a distinct DRAFT architecture. All four claims are supported by full-text
  primary evidence and pure-Python boundary verification.
source:
  git_revision: d5a297a94c1012cecd618f219a28e331a0f44ec0
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml
    sha256: 7b10d6d5eec1e2350182bc2566e96986f0aae2f80f6ebf566193df3460496d57
    role: target
  - path: research/discovery/20261019T130900Z-hyperprompt-task-conditioned-attention-prompts.json
    sha256: f6e9cc00a2eea871463fa215815063a90f478340b87f25d3eaa2da8b47a05e35
    role: context
  - path: research/discovery/hyperprompt-task-conditioned-attention-prompts-boundaries.py
    sha256: 77e408698fd7ed7641a1727f2a667690caaef1893f134d091d27f25d13167efc
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
- target_id: AIMech:HyperPromptTaskConditionedAttentionPrompt
  path: data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml
  label: HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml
    role: maintained
scope:
  description: All fields of data/curated/HyperPromptTaskConditionedAttentionPrompt.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HyperPromptTaskConditionedAttentionPrompt'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
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
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 hyperprompt-task-conditioned-attention-prompts-boundaries.py
  command: python3 research/discovery/hyperprompt-task-conditioned-attention-prompts-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] HyperPrompt boundaries verified: params_global=4842752 < params_sep=7176192,
    rel_increase_2xT=0.0204, out_shape=(3, 4)'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T130900Z-hyperprompt-task-conditioned-attention-prompts.json
  accessed_at: '2026-10-19T13:09:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HyperPromptTaskConditionedAttentionPrompt
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:09:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/hyperprompt-task-conditioned-attention-prompts-boundaries.py
  accessed_at: '2026-10-19T13:09:00Z'
  snapshot_sha256: 77e408698fd7ed7641a1727f2a667690caaef1893f134d091d27f25d13167efc
  support: supports
  summary: 'All constructed boundary assertions in hyperprompt-task-conditioned-attention-prompts-boundaries.py
    passed with exit code 0: [PASS] HyperPrompt boundaries verified: params_global=4842752
    < params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4)'
- evidence_id: r706-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2203.00759.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:09:00Z'
  snapshot_sha256: 29269d6e22d4575f6565ef2f86b28a49ddcb1ea31ddaf420ed67abac5d47371c
  support: supports
  summary: Full-text PDF (Proceedings of the 39th International Conference on Machine
    Learning (ICML 2022), PMLR 162:8678-8690 (2022)) read and verified.
- evidence_id: r706-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2203.00759
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:09:00Z'
  snapshot_sha256: 7a2f0307fe1ca7ebb6bd967ef347384e1c271d70bc68902378c3b1043946d914
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r706-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=HyperPrompt+Prompt-based+Task-Conditioning&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:09:00Z'
  snapshot_sha256: 07e4d71c57a2f92f43ceaf2144425737d9471fe295220646f5b3c2afae40e9b8
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  evidence_ids:
  - identity
  - r706-primary-pdf
  - r706-arxiv-abs
  - r706-metadata-cr
  summary: HyperPrompt (HyperNetwork-Generated Task-Conditioned Self-Attention Prompts)
    is a distinct concept.
  details: Introduced by Yun He, Huaixiu Steven Zheng, Yi Tay, Jai Gupta, Yu Du, Vamsi
    Aribandi, Zhe Zhao, YaGuang Li, Zhao Chen, Donald Metzler, Heng-Tze Cheng, and
    Ed H. Chi (ICML 2022, PMLR 162:8678-8690, arXiv:2203.00759). Distinct from Prefix-Tuning
    (Li & Liang, ACL 2021; AIMech:PrefixTuning), which optimizes single-task per-layer
    prefixes without cross-task hypernetworks or global-to-local bottleneck projections,
    and distinct from HyperFormer (Karimi Mahabadi et al., ACL 2021; AIMech Round
    703), which generates post-FFN sequential adapter layers rather than self-attention
    key/value memory tokens. All three architectural variants (HyperPrompt-Share,
    HyperPrompt-Sep, and HyperPrompt-Global) are covered within this single record.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  evidence_ids:
  - mapping
  - r706-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  evidence_ids:
  - r706-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in hyperprompt-task-conditioned-attention-prompts-boundaries.py
    passed with exit code 0: [PASS] HyperPrompt boundaries verified: params_global=4842752
    < params_sep=7176192, rel_increase_2xT=0.0204, out_shape=(3, 4)'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HyperPromptTaskConditionedAttentionPrompt
  evidence_ids:
  - identity
  - mapping
  - r706-primary-pdf
  - r706-arxiv-abs
  - r706-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyperPromptTaskConditionedAttentionPrompt in Round 706.
- All pages of Proceedings of the 39th International Conference on Machine Learning
  (ICML 2022), PMLR 162:8678-8690 (2022) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
