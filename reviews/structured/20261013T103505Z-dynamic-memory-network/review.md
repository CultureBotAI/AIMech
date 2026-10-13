# Scientific author self-review of Dynamic Memory Network

- Review: 20261013T103505Z-dynamic-memory-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T10:30:36Z
- Finished UTC: 2026-10-13T10:35:05Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain original DMN as DRAFT with broad recurrent-network and related GRU mappings. Six claims preserve variant and supervision boundaries; source-version authorship discrepancy is explicit. Author self-review found no actionable defect.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:DynamicMemoryNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9a88043583bb9e5d215e4cd80bbd86f52886385d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DynamicMemoryNetwork | data/curated/DynamicMemoryNetwork.yaml | maintained | Dynamic Memory Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DynamicMemoryNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 139.04s (0:02:19)<br>Checked 442 record(s); 0 failed.<br>Checked 605 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 269 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 266,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DynamicMemoryNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:DynamicMemoryNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:DynamicMemoryNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:DynamicMemoryNetwork | {"independent_sigmoid_gate_sum": 1.5, "recurrent_episode_forward": 0.3853416835791875, "recurrent_episode_reverse": 0.38269116145784, "fixed_logit_softmax_pool": 1.5, "reset_after_projection": [0.75, 1.5], "reset_before_projection": [1.75, 1.5], "limits": "Chosen finite formulas only; no gate-label learning, stopping controller, trained DMN or empirical evaluation."} |

## Scientific And Domain Assessments

### Dynamic Memory Network

identity: supported. Targets: AIMech:DynamicMemoryNetwork.

Retain this distinct DRAFT architecture.

Original DMN has recurrent contextual facts and repeated gated episodic memory updates. The original I/G/O/R framework, MemN2N, KV-MemNN and later DMN+ remain distinct. The inherited DMN/DMN+ lead is only partly addressed.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:DynamicMemoryNetwork.

The declared AIO mapping is supported.

Eight complete annotated AIO contexts support a broader recurrent network and a related GRU component. ANN is a less informative broader abstraction. The source MLP/bilinear gate is not the pinned dot-product AttentionLayer identity; LLM, internal cell, NTM and Hopfield identities are not forced.

### input-question-and-memory-modules

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Sections2.1–2.3 define contextual EOS fact states, separate question recurrent encoder, shared word embeddings and question-initialized memory. GRU use and LSTM comparison are scoped to source experiments.

### episodic-gates-and-recurrent-scan

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Equations1–8 preserve the source old-state z convention and reset-after-projection placement. Independent sigmoid gates need not sum to one. Concrete GRU scan order matters; the episode and memory pass are different recurrent axes.

### qa-aggregation-and-supervision

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Sections2.5 and4.1 explicitly add support-label gate supervision despite the broad abstract wording. QA softmax over pre-sigmoid scores and weighted fact sum is kept separate from default gated GRU episodes.

### answer-and-stopping-variants

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section2.4 gives answer recurrence and per-word tagging changes. End-of-passes gating and finite maximum iterations are described without inventing uninspected discrete-feedback or dynamic-stopping implementation details.

### separate-task-evaluation

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section4 trains tasks independently. QA supporting facts, SST root evaluation and POS four-model ensemble are retained; no single multitask model, universal superiority or unsupported transfer claim is made.

### passes-and-attention-interpretation

evidence: supported. Targets: AIMech:DynamicMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Table4 sentiment two-pass52.1 exceeds three-pass50.1. Figure3 includes a wrong attention focus, and selected examples do not establish causal interpretation. Future multimodal/multitask extensions and later DMN+ are not attributed to original evidence.

### independent gates versus normalized pooling, ordered recurrence, GRU conventions, support labels and original-versus-DMN+ scope

consistency: supported. Targets: AIMech:DynamicMemoryNetwork.

Constructed calculations support the stated distinctions.

Chosen sigmoid gates need not sum to one; a concrete scalar GRU scan is order-sensitive while a fixed softmax-weighted fact sum is permutation invariant. A two-dimensional reset example distinguishes applying the reset before versus after recurrent projection. These are constructed formula checks, not trained-model behavior.

### All maintained fields

provenance: supported. Targets: AIMech:DynamicMemoryNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Full maintained record and all eight mapping YAMLs reread after capture; primary title, methods, variants and evaluation pages reread. Constructed gate normalization, order and reset-placement examples recomputed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T103002Z-dynamic-memory-network.json | supports | Compared all 442 pinned AIO and 604 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 22, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 65 AIO and 88 native definitions, with every matched definition read. 8 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. The original DMN has contextual recurrent input facts, question-conditioned episodic gates, memory updates and an answer module. This is distinct from original Memory Networks, MemN2N soft key/value reads and KV-MemNN supplied key/value representations. DMN+ is a later successor requiring separate primary inspection; the inherited broad discovery lead remains partly addressed. |
| mapping | sources/aio/aio.json | supports | Eight complete annotated AIO contexts support a broader recurrent network and a related GRU component. ANN is a less informative broader abstraction. The source MLP/bilinear gate is not the pinned dot-product AttentionLayer identity; LLM, internal cell, NTM and Hopfield identities are not forced. |
| kumar2016 | https://arxiv.org/pdf/1506.07285v5; All ten pages of arXiv1506.07285v5 visually read before curation. Title and method/evaluation pages reread after capture. Official PMLR and current arXiv author metadata inspected; proceedings PDF, supplement, author code and training not inspected. | supports | arXiv 1506.07285v5, 5 March 2016, ten PDF pages, all visually read. Authors here transcribe this PDF title page: it omits Ozan Irsoy, who is included in the inspected current arXiv metadata and official PMLR48:kumar16 author list. Do not infer identical versions from the work title. Locators use PDF page order. Proceedings PDF, supplement and author code not inspected. |
| calculation | research/discovery/dynamic-memory-boundaries.py | supports | Chosen sigmoid gates need not sum to one; a concrete scalar GRU scan is order-sensitive while a fixed softmax-weighted fact sum is permutation invariant. A two-dimensional reset example distinguishes applying the reset before versus after recurrent projection. These are constructed formula checks, not trained-model behavior. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 605 native and 442 unchanged generated records. The 789-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All ten primary PDF pages visually inspected, including references. No source code or other version inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T103505Z-dynamic-memory-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Dynamic Memory Network
started_at: '2026-10-13T10:30:36Z'
finished_at: '2026-10-13T10:35:05Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged independent gates versus normalized pooling,
    ordered recurrence, GRU conventions, support labels and original-versus-DMN+ scope.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain original DMN as DRAFT with broad recurrent-network and related GRU
  mappings. Six claims preserve variant and supervision boundaries; source-version
  authorship discrepancy is explicit. Author self-review found no actionable defect.
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
  - path: data/aio/GatedRecurrentUnit.yaml
    sha256: 16e73da5012ad3e1d3de23bb30db0a0e18464b02b038acddd1c0f07f4fe82940
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
  - path: data/curated/DynamicMemoryNetwork.yaml
    sha256: 0affc6bdf4fd1c02c6d423d8560b53d357f5eca0ec8d93d29176375da25636fe
    role: target
  - path: data/curated/EndToEndMemoryNetwork.yaml
    sha256: 6c4806b22f49ed5ee492e207d08ed8665a62844b4dad44606d08d9e4b6cf69e6
    role: context
  - path: data/curated/KeyValueMemoryNetwork.yaml
    sha256: 7c1c576ad0b4626e66cdcafbba48877a7058c145b07c55fb2a9317d789ad2831
    role: context
  - path: data/curated/MemoryNetwork.yaml
    sha256: 46acd0a723a761c602f633b7fe4c2aea0924883a9d0b57dbb0cf411da19a8673
    role: context
  - path: research/discovery/20261013T103002Z-dynamic-memory-network.json
    sha256: 1f696a672d9f57e8b871e7732bfe2890fe866eea95a51c9ade6424097bdfae56
    role: context
  - path: research/discovery/dynamic-memory-boundaries.py
    sha256: f08282c9244e0a9d6203e031b377692915fe842d72f50bd28af1ff280c9f80b4
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
- target_id: AIMech:DynamicMemoryNetwork
  path: data/curated/DynamicMemoryNetwork.yaml
  label: Dynamic Memory Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DynamicMemoryNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:DynamicMemoryNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DynamicMemoryNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All ten pages of arXiv1506.07285v5 visually read before curation. Title
      and method/evaluation pages reread after capture. Official PMLR and current
      arXiv author metadata inspected; proceedings PDF, supplement, author code and
      training not inspected.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:DynamicMemoryNetwork
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
  - AIMech:DynamicMemoryNetwork
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
  - AIMech:DynamicMemoryNetwork
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
  - AIMech:DynamicMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/dynamic-memory-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DynamicMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"independent_sigmoid_gate_sum": 1.5, "recurrent_episode_forward": 0.3853416835791875,
    "recurrent_episode_reverse": 0.38269116145784, "fixed_logit_softmax_pool": 1.5,
    "reset_after_projection": [0.75, 1.5], "reset_before_projection": [1.75, 1.5],
    "limits": "Chosen finite formulas only; no gate-label learning, stopping controller,
    trained DMN or empirical evaluation."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T103002Z-dynamic-memory-network.json
  accessed_at: '2026-10-13T10:30:36Z'
  support: supports
  summary: Compared all 442 pinned AIO and 604 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    22, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 65 AIO and 88 native definitions, with every matched definition read.
    8 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. The original DMN has contextual recurrent input facts, question-conditioned
    episodic gates, memory updates and an answer module. This is distinct from original
    Memory Networks, MemN2N soft key/value reads and KV-MemNN supplied key/value representations.
    DMN+ is a later successor requiring separate primary inspection; the inherited
    broad discovery lead remains partly addressed.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T10:30:36Z'
  support: supports
  summary: Eight complete annotated AIO contexts support a broader recurrent network
    and a related GRU component. ANN is a less informative broader abstraction. The
    source MLP/bilinear gate is not the pinned dot-product AttentionLayer identity;
    LLM, internal cell, NTM and Hopfield identities are not forced.
- evidence_id: kumar2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1506.07285v5
  locator: All ten pages of arXiv1506.07285v5 visually read before curation. Title
    and method/evaluation pages reread after capture. Official PMLR and current arXiv
    author metadata inspected; proceedings PDF, supplement, author code and training
    not inspected.
  accessed_at: '2026-10-13T10:02:14Z'
  snapshot_sha256: ff3ac481ffdc8cc136cc4a30052013c2b6c984d09f1fc6d12fe0d1b2c7ab3719
  support: supports
  summary: 'arXiv 1506.07285v5, 5 March 2016, ten PDF pages, all visually read. Authors
    here transcribe this PDF title page: it omits Ozan Irsoy, who is included in the
    inspected current arXiv metadata and official PMLR48:kumar16 author list. Do not
    infer identical versions from the work title. Locators use PDF page order. Proceedings
    PDF, supplement and author code not inspected.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/dynamic-memory-boundaries.py
  accessed_at: '2026-10-13T10:32:05Z'
  snapshot_sha256: f08282c9244e0a9d6203e031b377692915fe842d72f50bd28af1ff280c9f80b4
  support: supports
  summary: Chosen sigmoid gates need not sum to one; a concrete scalar GRU scan is
    order-sensitive while a fixed softmax-weighted fact sum is permutation invariant.
    A two-dimensional reset example distinguishes applying the reset before versus
    after recurrent projection. These are constructed formula checks, not trained-model
    behavior.
assessments:
- assessment_id: identity
  area: identity
  topic: Dynamic Memory Network
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - identity
  - kumar2016
  summary: Retain this distinct DRAFT architecture.
  details: Original DMN has recurrent contextual facts and repeated gated episodic
    memory updates. The original I/G/O/R framework, MemN2N, KV-MemNN and later DMN+
    remain distinct. The inherited DMN/DMN+ lead is only partly addressed.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - mapping
  - kumar2016
  summary: The declared AIO mapping is supported.
  details: Eight complete annotated AIO contexts support a broader recurrent network
    and a related GRU component. ANN is a less informative broader abstraction. The
    source MLP/bilinear gate is not the pinned dot-product AttentionLayer identity;
    LLM, internal cell, NTM and Hopfield identities are not forced.
- assessment_id: input-question-and-memory-modules
  area: evidence
  topic: input-question-and-memory-modules
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections2.1–2.3 define contextual EOS fact states, separate question recurrent
    encoder, shared word embeddings and question-initialized memory. GRU use and LSTM
    comparison are scoped to source experiments.
- assessment_id: episodic-gates-and-recurrent-scan
  area: evidence
  topic: episodic-gates-and-recurrent-scan
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations1–8 preserve the source old-state z convention and reset-after-projection
    placement. Independent sigmoid gates need not sum to one. Concrete GRU scan order
    matters; the episode and memory pass are different recurrent axes.
- assessment_id: qa-aggregation-and-supervision
  area: evidence
  topic: qa-aggregation-and-supervision
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections2.5 and4.1 explicitly add support-label gate supervision despite
    the broad abstract wording. QA softmax over pre-sigmoid scores and weighted fact
    sum is kept separate from default gated GRU episodes.
- assessment_id: answer-and-stopping-variants
  area: evidence
  topic: answer-and-stopping-variants
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2.4 gives answer recurrence and per-word tagging changes. End-of-passes
    gating and finite maximum iterations are described without inventing uninspected
    discrete-feedback or dynamic-stopping implementation details.
- assessment_id: separate-task-evaluation
  area: evidence
  topic: separate-task-evaluation
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section4 trains tasks independently. QA supporting facts, SST root evaluation
    and POS four-model ensemble are retained; no single multitask model, universal
    superiority or unsupported transfer claim is made.
- assessment_id: passes-and-attention-interpretation
  area: evidence
  topic: passes-and-attention-interpretation
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Table4 sentiment two-pass52.1 exceeds three-pass50.1. Figure3 includes
    a wrong attention focus, and selected examples do not establish causal interpretation.
    Future multimodal/multitask extensions and later DMN+ are not attributed to original
    evidence.
- assessment_id: constructed-boundaries
  area: consistency
  topic: independent gates versus normalized pooling, ordered recurrence, GRU conventions,
    support labels and original-versus-DMN+ scope
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - kumar2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen sigmoid gates need not sum to one; a concrete scalar GRU scan is
    order-sensitive while a fixed softmax-weighted fact sum is permutation invariant.
    A two-dimensional reset example distinguishes applying the reset before versus
    after recurrent projection. These are constructed formula checks, not trained-model
    behavior.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetwork
  evidence_ids:
  - identity
  - mapping
  - kumar2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Full maintained record and all eight mapping YAMLs
    reread after capture; primary title, methods, variants and evaluation pages reread.
    Constructed gate normalization, order and reset-placement examples recomputed.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 605 native and 442 unchanged generated records.
  The 789-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All ten primary PDF pages visually inspected, including references. No source code
  or other version inspected.
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
