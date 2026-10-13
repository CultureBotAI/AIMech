# Scientific author self-review of Key-Value Memory Network

- Review: 20261013T103505Z-key-value-memory-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T10:30:34Z
- Finished UTC: 2026-10-13T10:35:05Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain KV-MemNN as DRAFT with broad ANN and related attention-component mappings. Six claims preserve representation, retrieval, training and evaluation scope. Author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:KeyValueMemoryNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9a88043583bb9e5d215e4cd80bbd86f52886385d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:KeyValueMemoryNetwork | data/curated/KeyValueMemoryNetwork.yaml | maintained | Key-Value Memory Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:KeyValueMemoryNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 139.04s (0:02:19)<br>Checked 442 record(s); 0 failed.<br>Checked 605 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 269 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 266,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:KeyValueMemoryNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:KeyValueMemoryNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:KeyValueMemoryNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:KeyValueMemoryNetwork | {"read": 1.6666666666666665, "paired_permutation_equal": true, "unpaired_value_swap": 2.3333333333333335, "duplicate_slot_read": 1.4000000000000001, "later_query_restricted_read": 1.0, "later_query_full_read": 2.998048780487805, "transform_after_sum": 5.333333333333333, "transform_query_only": 3.6666666666666665, "limits": "Chosen one-dimensional examples; no hashing implementation, model fitting, author code or benchmark."} |

## Scientific And Domain Assessments

### Key-Value Memory Network

identity: supported. Targets: AIMech:KeyValueMemoryNetwork.

Retain this distinct DRAFT architecture.

Named KV-MemNN permits distinct supplied key/value content. It is a specific neural architecture, not ordinary key-value storage or an exact alias of every original MemN2N configuration.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:KeyValueMemoryNetwork.

The declared AIO mapping is supported.

Seven annotated AIO contexts support broad ANN and component-level related AttentionLayer. LLM, internal memory cell, NTM and Hopfield identities are unsupported; observed-time recurrence is not required by fixed-hop query updates.

### key-addressing-value-reading

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section3.1 uses shared embedding matrix A with different query/key/value feature maps and potentially distinct underlying key/value content. Dot-product softmax weights values rather than performing exact dictionary retrieval.

### query-hops-and-output

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

The update transforms the whole q+o sum with hop-specific R. Final candidate scores use B and cross-entropy training concerns scores/probabilities, not a gradient through the displayed selected-answer argmax.

### initial-hash-restriction

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

The source explicitly repeats addressing and reading but not hashing. The constructed changed-query example cannot restore a removed candidate, and slot duplication changes the normalized read. No empty-set implementation convention is invented.

### representation-variants

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section3.2 separates triple, sentence, window, center and title constructions. The reported key-equals-value recovery is qualified by compatible configuration rather than treated as universal parameter equivalence.

### wikimovies-evaluation-boundary

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Primary split, filtered-KB and hits-at-one descriptions bound the evaluation. Table2 test values and Table3 development ablations differ; one correct returned entity is not all-answer recall.

### wikiqa-is-a-separate-protocol

evidence: supported. Targets: AIMech:KeyValueMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

WikiQA uses preselected sentences, no hash, window keys/sentence values, pretrained embeddings and additional exact-match/dropout choices. MAP/MRR are separate from WikiMovies hits-at-one; the comparison does not isolate one design change.

### key/value roles, initial retrieval restriction, softmax slot effects and task-specific evaluation

consistency: supported. Targets: AIMech:KeyValueMemoryNetwork.

Constructed calculations support the stated distinctions.

Chosen soft reads preserve complete-pair permutation but change when values detach from keys or a slot is duplicated. Initial candidate removal prevents a later query from attending to that excluded memory. Query transform placement changes the next state. No trained model, author code or benchmark is implemented.

### All maintained fields

provenance: supported. Targets: AIMech:KeyValueMemoryNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Full maintained record and all seven mapping YAMLs reread after capture; primary methods, representation and evaluation pages reread. Constructed key/value and restriction examples recomputed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T102926Z-key-value-memory-network.json | supports | Compared all 442 pinned AIO and 603 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 6, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 65 AIO and 87 native definitions, with every matched definition read. 7 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. KV-MemNN separates supplied key and value content, not merely two embeddings of the same sentence. It differs from ordinary key-value storage, original hard-retrieval MemNN and the maintained MemN2N configurations. Shared memory terminology does not identify it with an LLM, internal memory cell or NTM read/write controller. |
| mapping | sources/aio/aio.json | supports | Seven annotated AIO contexts support broad ANN and component-level related AttentionLayer. LLM, internal memory cell, NTM and Hopfield identities are unsupported; observed-time recurrence is not required by fixed-hop query updates. |
| miller2016 | https://arxiv.org/pdf/1606.03126v2; All ten pages of arXiv1606.03126v2 visually read before curation; methods and evaluation reread after capture. Other versions, author code and training not inspected. | supports | arXiv 1606.03126v2, 10 October 2016, ten PDF pages. All pages visually read, including equations, figures, tables and references. Locators use PDF page order. Other versions and author code not inspected. |
| calculation | research/discovery/key-value-memory-boundaries.py | supports | Chosen soft reads preserve complete-pair permutation but change when values detach from keys or a slot is duplicated. Initial candidate removal prevents a later query from attending to that excluded memory. Query transform placement changes the next state. No trained model, author code or benchmark is implemented. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 604 native and 442 unchanged generated records. The 788-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All10primarypages visually inspected; no source code or other version inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T103505Z-key-value-memory-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Key-Value Memory Network
started_at: '2026-10-13T10:30:34Z'
finished_at: '2026-10-13T10:35:05Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged key/value roles, initial retrieval restriction,
    softmax slot effects and task-specific evaluation. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain KV-MemNN as DRAFT with broad ANN and related attention-component mappings.
  Six claims preserve representation, retrieval, training and evaluation scope. Author
  self-review found no actionable defect.
source:
  git_revision: 9a88043583bb9e5d215e4cd80bbd86f52886385d
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/AttentionLayer.yaml
    sha256: ace47f724bab8a1aec9f963f7d8121f148134e5bbcce7c23a3a1f62c9c83619b
    role: context
  - path: data/aio/HopfieldNetwork.yaml
    sha256: 042815574abb3502427a76bb970ab78fd1ef684fa5f807b41c948ddb62e63822
    role: context
  - path: data/aio/MemoryAugmentedLLM.yaml
    sha256: 8727073cb355b965f54a2f0e58997f862f6b734c9143511008c26f9d31a965fd
    role: context
  - path: data/aio/MemoryCellLayer.yaml
    sha256: 290f04d7838e185381b29b22e67f8765de74242d687d23b0ffae2dad9d3f7237
    role: context
  - path: data/aio/NeuralTuringMachineNetwork.yaml
    sha256: bb483a9f90d767bcae50856c6084f31fe855d510d352419a5130fa4fc036be79
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/CommunicationNeuralNetwork.yaml
    sha256: 6da13aca3d17822181f43ddfb796a62170d2cdbb28a2e01a5d541c9a1ff8d813
    role: context
  - path: data/curated/EndToEndMemoryNetwork.yaml
    sha256: 6c4806b22f49ed5ee492e207d08ed8665a62844b4dad44606d08d9e4b6cf69e6
    role: context
  - path: data/curated/KeyValueMemoryNetwork.yaml
    sha256: 7c1c576ad0b4626e66cdcafbba48877a7058c145b07c55fb2a9317d789ad2831
    role: target
  - path: data/curated/MemoryNetwork.yaml
    sha256: 46acd0a723a761c602f633b7fe4c2aea0924883a9d0b57dbb0cf411da19a8673
    role: context
  - path: research/discovery/20261013T102926Z-key-value-memory-network.json
    sha256: 70db0e29adc4105e53f4765660f4459d9014de67db18cf5dbc2efaba9d325a4c
    role: context
  - path: research/discovery/key-value-memory-boundaries.py
    sha256: eba62b22144b6efc31ff3405e1b13278caf7402fc83cb74961becdfb9db516c4
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
- target_id: AIMech:KeyValueMemoryNetwork
  path: data/curated/KeyValueMemoryNetwork.yaml
  label: Key-Value Memory Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KeyValueMemoryNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:KeyValueMemoryNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:KeyValueMemoryNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All ten pages of arXiv1606.03126v2 visually read before curation; methods
      and evaluation reread after capture. Other versions, author code and training
      not inspected.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 139.04s (0:02:19)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 605 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 269 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 266,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/key-value-memory-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"read": 1.6666666666666665, "paired_permutation_equal": true, "unpaired_value_swap":
    2.3333333333333335, "duplicate_slot_read": 1.4000000000000001, "later_query_restricted_read":
    1.0, "later_query_full_read": 2.998048780487805, "transform_after_sum": 5.333333333333333,
    "transform_query_only": 3.6666666666666665, "limits": "Chosen one-dimensional
    examples; no hashing implementation, model fitting, author code or benchmark."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T102926Z-key-value-memory-network.json
  accessed_at: '2026-10-13T10:30:34Z'
  support: supports
  summary: Compared all 442 pinned AIO and 603 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    6, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    65 AIO and 87 native definitions, with every matched definition read. 7 full annotated
    AIO node/edge/generated contexts and 3 full native records were inspected. KV-MemNN
    separates supplied key and value content, not merely two embeddings of the same
    sentence. It differs from ordinary key-value storage, original hard-retrieval
    MemNN and the maintained MemN2N configurations. Shared memory terminology does
    not identify it with an LLM, internal memory cell or NTM read/write controller.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T10:30:34Z'
  support: supports
  summary: Seven annotated AIO contexts support broad ANN and component-level related
    AttentionLayer. LLM, internal memory cell, NTM and Hopfield identities are unsupported;
    observed-time recurrence is not required by fixed-hop query updates.
- evidence_id: miller2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1606.03126v2
  locator: All ten pages of arXiv1606.03126v2 visually read before curation; methods
    and evaluation reread after capture. Other versions, author code and training
    not inspected.
  accessed_at: '2026-10-13T10:02:13Z'
  snapshot_sha256: 466043a5722431ced489c44027372d1cf28f4ef35352409b6723f89ae4c23cb8
  support: supports
  summary: arXiv 1606.03126v2, 10 October 2016, ten PDF pages. All pages visually
    read, including equations, figures, tables and references. Locators use PDF page
    order. Other versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/key-value-memory-boundaries.py
  accessed_at: '2026-10-13T10:32:05Z'
  snapshot_sha256: eba62b22144b6efc31ff3405e1b13278caf7402fc83cb74961becdfb9db516c4
  support: supports
  summary: Chosen soft reads preserve complete-pair permutation but change when values
    detach from keys or a slot is duplicated. Initial candidate removal prevents a
    later query from attending to that excluded memory. Query transform placement
    changes the next state. No trained model, author code or benchmark is implemented.
assessments:
- assessment_id: identity
  area: identity
  topic: Key-Value Memory Network
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - identity
  - miller2016
  summary: Retain this distinct DRAFT architecture.
  details: Named KV-MemNN permits distinct supplied key/value content. It is a specific
    neural architecture, not ordinary key-value storage or an exact alias of every
    original MemN2N configuration.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - mapping
  - miller2016
  summary: The declared AIO mapping is supported.
  details: Seven annotated AIO contexts support broad ANN and component-level related
    AttentionLayer. LLM, internal memory cell, NTM and Hopfield identities are unsupported;
    observed-time recurrence is not required by fixed-hop query updates.
- assessment_id: key-addressing-value-reading
  area: evidence
  topic: key-addressing-value-reading
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3.1 uses shared embedding matrix A with different query/key/value
    feature maps and potentially distinct underlying key/value content. Dot-product
    softmax weights values rather than performing exact dictionary retrieval.
- assessment_id: query-hops-and-output
  area: evidence
  topic: query-hops-and-output
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The update transforms the whole q+o sum with hop-specific R. Final candidate
    scores use B and cross-entropy training concerns scores/probabilities, not a gradient
    through the displayed selected-answer argmax.
- assessment_id: initial-hash-restriction
  area: evidence
  topic: initial-hash-restriction
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source explicitly repeats addressing and reading but not hashing. The
    constructed changed-query example cannot restore a removed candidate, and slot
    duplication changes the normalized read. No empty-set implementation convention
    is invented.
- assessment_id: representation-variants
  area: evidence
  topic: representation-variants
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3.2 separates triple, sentence, window, center and title constructions.
    The reported key-equals-value recovery is qualified by compatible configuration
    rather than treated as universal parameter equivalence.
- assessment_id: wikimovies-evaluation-boundary
  area: evidence
  topic: wikimovies-evaluation-boundary
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Primary split, filtered-KB and hits-at-one descriptions bound the evaluation.
    Table2 test values and Table3 development ablations differ; one correct returned
    entity is not all-answer recall.
- assessment_id: wikiqa-is-a-separate-protocol
  area: evidence
  topic: wikiqa-is-a-separate-protocol
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: WikiQA uses preselected sentences, no hash, window keys/sentence values,
    pretrained embeddings and additional exact-match/dropout choices. MAP/MRR are
    separate from WikiMovies hits-at-one; the comparison does not isolate one design
    change.
- assessment_id: constructed-boundaries
  area: consistency
  topic: key/value roles, initial retrieval restriction, softmax slot effects and
    task-specific evaluation
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - miller2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen soft reads preserve complete-pair permutation but change when values
    detach from keys or a slot is duplicated. Initial candidate removal prevents a
    later query from attending to that excluded memory. Query transform placement
    changes the next state. No trained model, author code or benchmark is implemented.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:KeyValueMemoryNetwork
  evidence_ids:
  - identity
  - mapping
  - miller2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Full maintained record and all seven mapping YAMLs
    reread after capture; primary methods, representation and evaluation pages reread.
    Constructed key/value and restriction examples recomputed.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 604 native and 442 unchanged generated records.
  The 788-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All10primarypages visually inspected; no source code or other version inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
