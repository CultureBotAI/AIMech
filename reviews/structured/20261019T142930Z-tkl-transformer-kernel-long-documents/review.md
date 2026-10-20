# Scientific author self-review of TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval

- Review: 20261019T142930Z-tkl-transformer-kernel-long-documents
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:29:00Z
- Finished UTC: 2026-10-19T14:29:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/TKLTransformerKernelForLongDocuments.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:TKLTransformerKernelForLongDocuments
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 390b3aada81fdf47bfc5bcd2f2c6bf1d2a8de754.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TKLTransformerKernelForLongDocuments | data/curated/TKLTransformerKernelForLongDocuments.yaml | maintained | TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:TKLTransformerKernelForLongDocuments | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:TKLTransformerKernelForLongDocuments | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:TKLTransformerKernelForLongDocuments | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:TKLTransformerKernelForLongDocuments | Validated history sidecar files. |
| python3 tkl-transformer-kernel-long-documents-boundaries.py | passed | True | AIMech:TKLTransformerKernelForLongDocuments | TKL boundary verification passed:<br>  Packed non-padding windows: 2 (from 4 total chunks)<br>  Learned saturation values:  s(1)=0.000000, s(4)=0.043236, s(8)=0.065067<br>  Top-2 local maxima indices: [14, 3] |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:TKLTransformerKernelForLongDocuments.

TKL: Transformer-Kernel Model with Local Self-Attention for Long Document Retrieval is a distinct concept.

Distinct from the short-text TK model (AIMech:TKTransformerKernelModelForReRanking, which applies full self-attention over the first ~200 tokens and uses fixed log saturation over the entire document). TKL introduces overlapping local self-attention windows with minibatch padding-chunk skipping, a learned non-linear power saturation function conditioned on query-term salience e_i and region token count c_len, and two-stage local/global topography pooling via top-local-max_{t,f}.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:TKLTransformerKernelForLongDocuments.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:TKLTransformerKernelForLongDocuments.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in tkl-transformer-kernel-long-documents-boundaries.py passed with exit code 0: TKL boundary verification passed:
  Packed non-padding windows: 2 (from 4 total chunks)
  Learned saturation values:  s(1)=0.000000, s(4)=0.043236, s(8)=0.065067
  Top-2 local maxima indices: [14, 3]

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:TKLTransformerKernelForLongDocuments.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T142900Z-tkl-transformer-kernel-long-documents.json | supports | No normalized identity match for AIMech:TKLTransformerKernelForLongDocuments across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/tkl-transformer-kernel-long-documents-boundaries.py | supports | All constructed boundary assertions in tkl-transformer-kernel-long-documents-boundaries.py passed with exit code 0: TKL boundary verification passed:<br>  Packed non-padding windows: 2 (from 4 total chunks)<br>  Learned saturation values:  s(1)=0.000000, s(4)=0.043236, s(8)=0.065067<br>  Top-2 local maxima indices: [14, 3] |
| r786-primary-pdf | https://arxiv.org/pdf/2005.04908.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2020) (2020)) read and verified. |
| r786-arxiv-abs | https://arxiv.org/abs/2005.04908; arXiv abstract | supports | arXiv abstract read and verified. |
| r786-metadata-cr | https://arxiv.org/bibtex/2005.04908; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:TKLTransformerKernelForLongDocuments in Round 786.
- All pages of Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2020) (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T142930Z-tkl-transformer-kernel-long-documents
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of TKL: Transformer-Kernel Model with Local
  Self-Attention for Long Document Retrieval'
started_at: '2026-10-19T14:29:00Z'
finished_at: '2026-10-19T14:29:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:TKLTransformerKernelForLongDocuments
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 43rd International ACM SIGIR Conference on Research and Development in
    Information Retrieval (SIGIR 2020) (2020) and pure-Python boundary checks. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain TKL: Transformer-Kernel Model with Local Self-Attention for Long
  Document Retrieval as a distinct DRAFT architecture. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.'
source:
  git_revision: 390b3aada81fdf47bfc5bcd2f2c6bf1d2a8de754
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/TKLTransformerKernelForLongDocuments.yaml
    sha256: b5114fbf97d01c956eef1f842acee627b54b7c346bfdec83143f7957c9eec3df
    role: target
  - path: research/discovery/20261019T142900Z-tkl-transformer-kernel-long-documents.json
    sha256: 9609cb941d9cdae07e2665606c48dd9c9322782090b7ae5781ed79a86fa511c0
    role: context
  - path: research/discovery/tkl-transformer-kernel-long-documents-boundaries.py
    sha256: 1ab4e1cdfa8c221d8d452d54f234cfe5f1cbec2e26623e57ed73b911eec8f51a
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
- target_id: AIMech:TKLTransformerKernelForLongDocuments
  path: data/curated/TKLTransformerKernelForLongDocuments.yaml
  label: 'TKL: Transformer-Kernel Model with Local Self-Attention for Long Document
    Retrieval'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TKLTransformerKernelForLongDocuments.yaml
    role: maintained
scope:
  description: All fields of data/curated/TKLTransformerKernelForLongDocuments.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:TKLTransformerKernelForLongDocuments'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
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
  - AIMech:TKLTransformerKernelForLongDocuments
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 tkl-transformer-kernel-long-documents-boundaries.py
  command: python3 research/discovery/tkl-transformer-kernel-long-documents-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  exit_code: 0
  expected_exit_code: 0
  summary: "TKL boundary verification passed:\n  Packed non-padding windows: 2 (from\
    \ 4 total chunks)\n  Learned saturation values:  s(1)=0.000000, s(4)=0.043236,\
    \ s(8)=0.065067\n  Top-2 local maxima indices: [14, 3]"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T142900Z-tkl-transformer-kernel-long-documents.json
  accessed_at: '2026-10-19T14:29:00Z'
  support: supports
  summary: No normalized identity match for AIMech:TKLTransformerKernelForLongDocuments
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:29:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/tkl-transformer-kernel-long-documents-boundaries.py
  accessed_at: '2026-10-19T14:29:00Z'
  snapshot_sha256: 1ab4e1cdfa8c221d8d452d54f234cfe5f1cbec2e26623e57ed73b911eec8f51a
  support: supports
  summary: "All constructed boundary assertions in tkl-transformer-kernel-long-documents-boundaries.py\
    \ passed with exit code 0: TKL boundary verification passed:\n  Packed non-padding\
    \ windows: 2 (from 4 total chunks)\n  Learned saturation values:  s(1)=0.000000,\
    \ s(4)=0.043236, s(8)=0.065067\n  Top-2 local maxima indices: [14, 3]"
- evidence_id: r786-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2005.04908.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:29:00Z'
  snapshot_sha256: e79f78c1a5cf90d2fbc9bac4410a6f5681a28c66989c01cad56fa44d050612c4
  support: supports
  summary: Full-text PDF (Proceedings of the 43rd International ACM SIGIR Conference
    on Research and Development in Information Retrieval (SIGIR 2020) (2020)) read
    and verified.
- evidence_id: r786-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2005.04908
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:29:00Z'
  snapshot_sha256: dbc02e6249bbb0bfe923a2571b89fe4c231d109efa238164b7c83c0721f3bcaf
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r786-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2005.04908
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:29:00Z'
  snapshot_sha256: 2727573b00c92dcbfa8beb03a7db76f2d79021e268353d00cc433d1e28a688aa
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  evidence_ids:
  - identity
  - r786-primary-pdf
  - r786-arxiv-abs
  - r786-metadata-cr
  summary: 'TKL: Transformer-Kernel Model with Local Self-Attention for Long Document
    Retrieval is a distinct concept.'
  details: Distinct from the short-text TK model (AIMech:TKTransformerKernelModelForReRanking,
    which applies full self-attention over the first ~200 tokens and uses fixed log
    saturation over the entire document). TKL introduces overlapping local self-attention
    windows with minibatch padding-chunk skipping, a learned non-linear power saturation
    function conditioned on query-term salience e_i and region token count c_len,
    and two-stage local/global topography pooling via top-local-max_{t,f}.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  evidence_ids:
  - mapping
  - r786-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  evidence_ids:
  - r786-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: "All constructed boundary assertions in tkl-transformer-kernel-long-documents-boundaries.py\
    \ passed with exit code 0: TKL boundary verification passed:\n  Packed non-padding\
    \ windows: 2 (from 4 total chunks)\n  Learned saturation values:  s(1)=0.000000,\
    \ s(4)=0.043236, s(8)=0.065067\n  Top-2 local maxima indices: [14, 3]"
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:TKLTransformerKernelForLongDocuments
  evidence_ids:
  - identity
  - mapping
  - r786-primary-pdf
  - r786-arxiv-abs
  - r786-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:TKLTransformerKernelForLongDocuments in Round 786.
- All pages of Proceedings of the 43rd International ACM SIGIR Conference on Research
  and Development in Information Retrieval (SIGIR 2020) (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
