# Balanced attention primary-source locator review

- Review: 20261013T090634Z-balanced-attention-locators-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T09:04:08Z
- Finished UTC: 2026-10-13T09:06:34Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed minor source-location finding; correct before final review.

## Scope And Provenance

Branch-equation and evaluation locator accuracy.

Selection: Exact maintained ID AIMech:BalancedAttentionMechanism
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 60c68a75f948fe44ff8d479de146f5fa3fe4d97d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BalancedAttentionMechanism | data/curated/BalancedAttentionMechanism.yaml | maintained | Balanced Attention Mechanism |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:BalancedAttentionMechanism | Pending correction; a gate on the preceding draft is still running and does not validate corrected inputs. |

## Scientific And Domain Assessments

### Source equation/page and heading accuracy

evidence: concern. Targets: AIMech:BalancedAttentionMechanism.

Correct source locators before publication.

The ACAM locator names Equations1–2, but its average pooling and learned branch are Equations1 and3 on PDFp3. The MSAM locator names Equations3–4 on p3, but its channel maximum is Equation2 on p3 and learned branch Equation4 on p4. Evaluation and runtime locators also use section labels not printed in this PDF. Correct the locator descriptions to actual equations, pages and headings; the mechanisms and scoped empirical claims remain supported.

## Findings

### F1: Correct balanced attention source locators

minor / open / confirmed; issue key: balanced-attention-primary-locators.

The ACAM locator names Equations1–2, but its average pooling and learned branch are Equations1 and3 on PDFp3. The MSAM locator names Equations3–4 on p3, but its channel maximum is Equation2 on p3 and learned branch Equation4 on p4. Evaluation and runtime locators also use section labels not printed in this PDF. Correct the locator descriptions to actual equations, pages and headings; the mechanisms and scoped empirical claims remain supported.

## Recommended Actions And Acceptance Checks

### A1

Correct locators, synchronize the discovery-report mirror and append EDIT history, then recapture and reassess.

- ACAM cites Equations1 and3 on p3; MSAM cites Equation2 on p3 and Equation4 on p4.
- Evaluation/runtime locators use the printed section headings.
- Fresh corrected-input review, rendered pages and required gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/BalancedAttentionMechanism.yaml | supports | Incorrect equation/page and section descriptions are present in the saved draft. |
| wang2021 | https://arxiv.org/pdf/2104.07566v3; All eight pages read; PDFpp2–5 and7 reread after capture. Equations1–3 on p3, Equation4 on p4; printed headings Datasets and metrics, Implementation details, Comparison experiments and Speed comparison. | supports | Primary paper supports the scoped content but supplies different precise locations. |

## Limits And Additional Notes

- Partial author self-review; no independent approval or status promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T090634Z-balanced-attention-locators-open
kind: record
repository: CultureBotAI/AIMech
title: Balanced attention primary-source locator review
started_at: '2026-10-13T09:04:08Z'
finished_at: '2026-10-13T09:06:34Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author checked the actual paper equations and headings during
    adversarial rereading; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed minor source-location finding; correct before final review.
source:
  git_revision: 60c68a75f948fe44ff8d479de146f5fa3fe4d97d
  state: working_tree
  inputs:
  - path: data/aio/AttentionLayer.yaml
    sha256: ace47f724bab8a1aec9f963f7d8121f148134e5bbcce7c23a3a1f62c9c83619b
    role: context
  - path: data/aio/Convolution2DLayer.yaml
    sha256: c8aa862ad114729498e9ff7c689d37fc58d286d8240e8f5d9afcb90dff26d5b0
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/GlobalAveragePooling2DLayer.yaml
    sha256: 092db3c9424ae2796082e850845716356673a157d37fbdf1cf8656a957b1c110
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
    role: context
  - path: data/aio/PReLULayer.yaml
    sha256: 3ced4948a6e188220efb364544cf6adfb418e8ff9df8912655eaf605d78d7d33
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
    role: context
  - path: data/curated/BalancedAttentionMechanism.yaml
    sha256: 40d5da7f012d2c6772b336bc0779189bcd11fe2c389032534ca86bc07c7d75d3
    role: target
  - path: data/curated/BottleneckAttentionModule.yaml
    sha256: 465518e5c03eba3a2922b8e5494ebfd5ad945e4dfdfb159f997dc120786500b9
    role: context
  - path: data/curated/ConvolutionalBlockAttentionModule.yaml
    sha256: ece8d0432112916c5f158b484b24e6f316a9c3edfe07233fefeae5b454a96b96
    role: context
  - path: data/curated/SqueezeAndExcitationBlock.yaml
    sha256: e91da402137dfbda2cc38257b36587771d8a9b924488690dfeeb5bf70625fac8
    role: context
  - path: research/discovery/20261013T090246Z-balanced-attention-mechanism.json
    sha256: a0ce8cfc93d40ca77509f8657cc20c0143bc1456d0ff465937af84df7720eaf0
    role: context
  - path: research/discovery/balanced-attention-boundaries.py
    sha256: d2d412f9c5f64d8810565ab909d19f8ff707fab79d533bc85f9798a4f5daee7c
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
- target_id: AIMech:BalancedAttentionMechanism
  path: data/curated/BalancedAttentionMechanism.yaml
  label: Balanced Attention Mechanism
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BalancedAttentionMechanism.yaml
    role: maintained
scope:
  description: Branch-equation and evaluation locator accuracy.
  selection: Exact maintained ID AIMech:BalancedAttentionMechanism
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:BalancedAttentionMechanism
  exclusions:
  - target: Corrected-input full scientific review and publication gates
    reason: Pending remediation; this partial review preserves the finding.
checks:
- check_id: publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:BalancedAttentionMechanism
  summary: Pending correction; a gate on the preceding draft is still running and
    does not validate corrected inputs.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/BalancedAttentionMechanism.yaml
  accessed_at: '2026-10-13T09:06:34Z'
  snapshot_sha256: 40d5da7f012d2c6772b336bc0779189bcd11fe2c389032534ca86bc07c7d75d3
  support: supports
  summary: Incorrect equation/page and section descriptions are present in the saved
    draft.
- evidence_id: wang2021
  kind: primary_source
  reference: https://arxiv.org/pdf/2104.07566v3
  accessed_at: '2026-10-13T08:37:17Z'
  snapshot_sha256: dcd27007bcb038d79cb625e2a8a35ca4b6a19814b137173ba786dd83c328ab79
  support: supports
  locator: All eight pages read; PDFpp2–5 and7 reread after capture. Equations1–3
    on p3, Equation4 on p4; printed headings Datasets and metrics, Implementation
    details, Comparison experiments and Speed comparison.
  summary: Primary paper supports the scoped content but supplies different precise
    locations.
assessments:
- assessment_id: locators
  area: evidence
  topic: Source equation/page and heading accuracy
  outcome: concern
  target_ids:
  - AIMech:BalancedAttentionMechanism
  evidence_ids:
  - record
  - wang2021
  summary: Correct source locators before publication.
  details: The ACAM locator names Equations1–2, but its average pooling and learned
    branch are Equations1 and3 on PDFp3. The MSAM locator names Equations3–4 on p3,
    but its channel maximum is Equation2 on p3 and learned branch Equation4 on p4.
    Evaluation and runtime locators also use section labels not printed in this PDF.
    Correct the locator descriptions to actual equations, pages and headings; the
    mechanisms and scoped empirical claims remain supported.
findings:
- finding_id: F1
  issue_key: balanced-attention-primary-locators
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct balanced attention source locators
  description: The ACAM locator names Equations1–2, but its average pooling and learned
    branch are Equations1 and3 on PDFp3. The MSAM locator names Equations3–4 on p3,
    but its channel maximum is Equation2 on p3 and learned branch Equation4 on p4.
    Evaluation and runtime locators also use section labels not printed in this PDF.
    Correct the locator descriptions to actual equations, pages and headings; the
    mechanisms and scoped empirical claims remain supported.
  target_ids:
  - AIMech:BalancedAttentionMechanism
  field_paths:
  - claims[claim_id=average-channel-branch].evidence
  - claims[claim_id=maximum-spatial-branch].evidence
  - claims[claim_id=evaluation-protocol].evidence
  - claims[claim_id=mixed-results-and-runtime].evidence
  evidence_ids:
  - record
  - wang2021
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BalancedAttentionMechanism.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct locators, synchronize the discovery-report mirror and append
    EDIT history, then recapture and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:BalancedAttentionMechanism
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BalancedAttentionMechanism.yaml
    role: maintained
  acceptance_checks:
  - ACAM cites Equations1 and3 on p3; MSAM cites Equation2 on p3 and Equation4 on
    p4.
  - Evaluation/runtime locators use the printed section headings.
  - Fresh corrected-input review, rendered pages and required gates pass.
limitations:
- Partial author self-review; no independent approval or status promotion.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- source-locators
```
