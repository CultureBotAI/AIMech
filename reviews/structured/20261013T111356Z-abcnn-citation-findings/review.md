# ABCNN claim citation findings

- Review: 20261013T111356Z-abcnn-citation-findings
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T11:12:12Z
- Finished UTC: 2026-10-13T11:13:56Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor citation defects require correction; no architecture-identity error found.

## Scope And Provenance

Confirmed claim-level citation defects in the ABCNN draft.

Selection: Exact maintained ID AIMech:AttentionBasedConvolutionalNeuralNetwork
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ddc81b074ce61455a789440a8b80097a95737f0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AttentionBasedConvolutionalNeuralNetwork | data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml | maintained | Attention-Based Convolutional Neural Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:AttentionBasedConvolutionalNeuralNetwork | Corrected inputs do not yet exist; the ongoing pre-correction gate is not evidence for them. |

## Scientific And Domain Assessments

### Claim and table citation accuracy

evidence: concern. Targets: AIMech:AttentionBasedConvolutionalNeuralNetwork.

Remove the uncited comparator clause and correct the training-table locator.

The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax Attentive Pooling Network, but its sole citation is the ABCNN paper, which does not substantiate the comparator mechanism. The comparison is supported by separately inspected native identity context, but it lacks a claim-level primary citation. Remove that unnecessary comparator sentence from the mechanism claim, retaining the independently audited identity distinction. The training claim cites Table 1, which is the notation table on PDFp4. Hyperparameters are in Table 2 on PDFp7. Correct the table locator; the section/page citations and training mechanism are otherwise supported.

## Findings

### F1: Correct ABCNN claim citation accuracy

minor / open / confirmed; issue key: abcnn-cross-method-evidence.

The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax Attentive Pooling Network, but its sole citation is the ABCNN paper, which does not substantiate the comparator mechanism. The comparison is supported by separately inspected native identity context, but it lacks a claim-level primary citation. Remove that unnecessary comparator sentence from the mechanism claim, retaining the independently audited identity distinction.

### F2: Correct ABCNN claim citation accuracy

minor / open / confirmed; issue key: abcnn-training-table-locator.

The training claim cites Table 1, which is the notation table on PDFp4. Hyperparameters are in Table 2 on PDFp7. Correct the table locator; the section/page citations and training mechanism are otherwise supported.

## Recommended Actions And Acceptance Checks

### A1

Remove the comparator sentence from the mechanism claim and change its training-table locator to Table2; synchronize report, append history, recapture and reassess.

- The mechanism claim only asserts what its cited ABCNN source supports.
- The training claim cites Table2 on PDFp7.
- Final gates and successor review assess the corrected record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml | supports | Complete maintained record read after capture; both affected statements and citation locators are present. |
| paper | https://arxiv.org/pdf/1512.05193v4; Sections 3–5, PDFpp3–7, Tables1–2 and Equation1; complete PDF was inspected. | supports | The paper supports ABCNN distance affinities, feature maps and training; it does not establish the Attentive Pooling comparator mechanism, and Table1 is notation rather than hyperparameters. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T111356Z-abcnn-citation-findings
kind: record
repository: CultureBotAI/AIMech
title: ABCNN claim citation findings
started_at: '2026-10-13T11:12:12Z'
finished_at: '2026-10-13T11:13:56Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author compared complete maintained fields with the inspected
    primary paper; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Two minor citation defects require correction; no architecture-identity error
  found.
source:
  git_revision: 1ddc81b074ce61455a789440a8b80097a95737f0
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/AttentionLayer.yaml
    sha256: ace47f724bab8a1aec9f963f7d8121f148134e5bbcce7c23a3a1f62c9c83619b
    role: context
  - path: data/aio/AveragePooling1DLayer.yaml
    sha256: 2c78ecf6ef4bf7c25befcde55b4df86d12082e39f84eeb5242a8c6278216659e
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/DeepConvolutionalNetwork.yaml
    sha256: b2be73a895ae3890ca0ba464c1d0de55e41960f33ec53dcab4547abfe1159c62
    role: context
  - path: data/aio/OrdinalLLM.yaml
    sha256: 2bbb482a7007dd95f6e644863e264f646f7cc40e3debc05273bdb7ac96160d4b
    role: context
  - path: data/aio/PoolingLayer.yaml
    sha256: 2a5cc182b52109a337a926a42bd715d5f1142e2a0876a8bfbc41890846e84246
    role: context
  - path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    sha256: 10574f3cc598db864593192eacf59f6c2dbdb4f26e68d11d582eb8855b972aa7
    role: target
  - path: data/curated/AttentivePoolingNetwork.yaml
    sha256: c2c9abe6d2c5f19926cca4cf6a06203bd6c3f285cf7558fd56983d278aded52d
    role: context
  - path: data/curated/ConvolutionalBlockAttentionModule.yaml
    sha256: ece8d0432112916c5f158b484b24e6f316a9c3edfe07233fefeae5b454a96b96
    role: context
  - path: data/curated/PointNet.yaml
    sha256: b2292a45d360ee989f143838b4ca9008033e69d63c5b578e7e2ab45fb6ee80dd
    role: context
  - path: research/discovery/20261013T111155Z-attention-based-convolutional-neural-network.json
    sha256: 98b7a11600ba49c020b6dbf96fe464bc6b01df23bd97beb79aaf1a45d976a533
    role: context
  - path: research/discovery/abcnn-boundaries.py
    sha256: 31e5f0296bb5e1110e0a23a56fa6f2509d6cda446b55a31c5a04ced5208f1987
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
- target_id: AIMech:AttentionBasedConvolutionalNeuralNetwork
  path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
  label: Attention-Based Convolutional Neural Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
scope:
  description: Confirmed claim-level citation defects in the ABCNN draft.
  selection: Exact maintained ID AIMech:AttentionBasedConvolutionalNeuralNetwork
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  exclusions:
  - target: Corrected-input complete scientific review
    reason: Pending correction and final gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  summary: Corrected inputs do not yet exist; the ongoing pre-correction gate is not
    evidence for them.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
  accessed_at: '2026-10-13T11:13:56Z'
  snapshot_sha256: 10574f3cc598db864593192eacf59f6c2dbdb4f26e68d11d582eb8855b972aa7
  support: supports
  summary: Complete maintained record read after capture; both affected statements
    and citation locators are present.
- evidence_id: paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1512.05193v4
  accessed_at: '2026-10-13T10:40:35Z'
  snapshot_sha256: 46b9425267ae1c454af3708c0c52837aeadb341e1cbfc8fc39315febd5f43e3d
  support: supports
  locator: Sections 3–5, PDFpp3–7, Tables1–2 and Equation1; complete PDF was inspected.
  summary: The paper supports ABCNN distance affinities, feature maps and training;
    it does not establish the Attentive Pooling comparator mechanism, and Table1 is
    notation rather than hyperparameters.
assessments:
- assessment_id: citations
  area: evidence
  topic: Claim and table citation accuracy
  outcome: concern
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  evidence_ids:
  - record
  - paper
  summary: Remove the uncited comparator clause and correct the training-table locator.
  details: The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax
    Attentive Pooling Network, but its sole citation is the ABCNN paper, which does
    not substantiate the comparator mechanism. The comparison is supported by separately
    inspected native identity context, but it lacks a claim-level primary citation.
    Remove that unnecessary comparator sentence from the mechanism claim, retaining
    the independently audited identity distinction. The training claim cites Table
    1, which is the notation table on PDFp4. Hyperparameters are in Table 2 on PDFp7.
    Correct the table locator; the section/page citations and training mechanism are
    otherwise supported.
findings:
- finding_id: F1
  issue_key: abcnn-cross-method-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct ABCNN claim citation accuracy
  description: The input-attention claim compares ABCNN with the bilinear-tanh/max-softmax
    Attentive Pooling Network, but its sole citation is the ABCNN paper, which does
    not substantiate the comparator mechanism. The comparison is supported by separately
    inspected native identity context, but it lacks a claim-level primary citation.
    Remove that unnecessary comparator sentence from the mechanism claim, retaining
    the independently audited identity distinction.
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  field_paths:
  - claims[claim_id=input-attention-variant].statement
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
- finding_id: F2
  issue_key: abcnn-training-table-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct ABCNN claim citation accuracy
  description: The training claim cites Table 1, which is the notation table on PDFp4.
    Hyperparameters are in Table 2 on PDFp7. Correct the table locator; the section/page
    citations and training mechanism are otherwise supported.
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  field_paths:
  - claims[claim_id=staged-training-and-feature-heads].evidence
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
actions:
- action_id: A1
  description: Remove the comparator sentence from the mechanism claim and change
    its training-table locator to Table2; synchronize report, append history, recapture
    and reassess.
  finding_ids:
  - F1
  - F2
  target_ids:
  - AIMech:AttentionBasedConvolutionalNeuralNetwork
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AttentionBasedConvolutionalNeuralNetwork.yaml
    role: maintained
  acceptance_checks:
  - The mechanism claim only asserts what its cited ABCNN source supports.
  - The training claim cites Table2 on PDFp7.
  - Final gates and successor review assess the corrected record.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- source-locators
```
