# Scientific author self-review of End-to-End Memory Network

- Review: 20261013T101937Z-end-to-end-memory-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T10:15:12Z
- Finished UTC: 2026-10-13T10:19:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain MemN2N as a DRAFT neural architecture with broad ANN and related attention-component mappings. Six claims preserve mechanism, variant, supervision and finite-evaluation boundaries; author self-review resolved the source-locator finding through explicit predecessor links and corrected-input checks.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:EndToEndMemoryNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4b13f46070942eb9cc99296f28d42bf341801b5a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:EndToEndMemoryNetwork | data/curated/EndToEndMemoryNetwork.yaml | maintained | End-to-End Memory Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:EndToEndMemoryNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 137.48s (0:02:17)<br>Checked 442 record(s); 0 failed.<br>Checked 603 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 267 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 264,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:EndToEndMemoryNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:EndToEndMemoryNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:EndToEndMemoryNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:EndToEndMemoryNetwork | {"soft_weights": [0.6666666666666666, 0.3333333333333333], "read": 1.6666666666666665, "additive_next_query": 2.6666666666666665, "paired_permutation_invariant": true, "duplicated_slot_read": 1.4000000000000001, "zero_value_unmasked_slot_read": 1.25, "bow_reverse_equal": true, "position_encoded_forward": ["1/2", "1"], "position_encoded_reverse": ["1/2", "1/2"], "limits": "Chosen one-hop values only; temporal embeddings, training, full architecture and empirical results are not implemented."} |

## Scientific And Domain Assessments

### End-to-End Memory Network

identity: supported. Targets: AIMech:EndToEndMemoryNetwork.

Retain this distinct DRAFT architecture.

MemN2N is an explicitly named end-to-end architecture with soft memory reads, distinct from the general I/G/O/R family, supervised hard-retrieval MemNN, stack/list controllers and CommNet.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:EndToEndMemoryNetwork.

The declared AIO mapping is supported.

Seven complete annotated AIO contexts support ANN as broader and AttentionLayer as a related component. Memory-Augmented LLM is too narrow in task/model scope; a memory cell, NTM controller, symmetric Hopfield attractor and temporal RNN are not equivalent identities.

### soft-memory-read

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Equations1–3 separate A keys and C values, normalize query-key scores and sum weighted output embeddings before the answer softmax. The chosen read5/3 is neither of the two discrete stored values.

### hops-and-tying

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section2.2 distinguishes additive adjacent tying from layer-wise tying with H. Parameter identities, final W transpose and query initialization have precise roles; more hops do not require observed-time recurrence.

### word-and-memory-order

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

The deterministic positional coordinate weights distinguish a reversed two-word example even when bag-of-words sums agree. Permuting complete embedded pairs preserves a soft sum, while temporal encodings can change when memory positions change.

### supervision-and-training

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

The primary source contrasts answer-only MemN2N supervision with support-supervised MemNN. The linear-start training phase removes memory softmax before reintroduction; it is not silently identified with the ordinary normalized-read equations.

### finite-buffer-and-slot-boundaries

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Latest50sentence storage and null-word/temporal embedding details bound memory claims. Duplicating an unmasked slot or adding a zero-valued slot changes normalization and readout in the constructed examples. No author implementation masking convention is inferred.

### evaluation-and-output-scope

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Supported within the stated primary-source and mathematical scope.

QA and language-model input/query/tying/output rules differ; multiword QA answers are compound vocabulary entries. Table-level differences and rescaled heatmaps do not establish universal improvements, causal explanation or independent replication.

### key/value role separation, hop versus observation time, attention normalization, supplied-buffer limits and supervision/evaluation variants

consistency: supported. Targets: AIMech:EndToEndMemoryNetwork.

Constructed calculations support the stated distinctions.

Chosen keys log2 and0 with values1 and3 give a soft read5/3. Paired permutation preserves the read, duplicate or zero-valued unmasked slots change it, and explicit position encoding distinguishes word orders with equal bag-of-words sums. No full model, temporal embedding, fitting or benchmark is implemented.

### All maintained fields

provenance: supported. Targets: AIMech:EndToEndMemoryNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Complete corrected record and all mapping YAMLs reread after fresh capture. All primary method/evaluation pages specified in the initial reading were reread before locator-only corrections; the changed locator page was reread again after final capture. Scientific claims are unchanged. Constructed examples recomputed.

### Issue262 source-locator correction

evidence: supported. Targets: AIMech:EndToEndMemoryNetwork.

Confirmed source-locator finding resolved.

Two affected claim locators now match inspected primary headings, with explicit predecessor lineage.

## Findings

### F1: Correct End-to-End Memory Network source locators

minor / resolved / confirmed; issue key: memn2n-training-buffer-locators.

MemN2N training and buffer-limit locators omit Section 4.2. Linear-start, restarts, latest50 memory and zero null embedding are in Section4.2 on PDFp5. Section4.1 supplies temporal encoding, not those training details.

Disposition: Corrected two claim source-section locators against the actual primary-paper headings. Scientific statements unchanged. Full corrected record, exact report mirror, EDIT history and corrected-input checks establish resolution.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T100955Z-end-to-end-memory-network.json | supports | Compared all 442 pinned AIO and 601 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 17, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 60 AIO and 65 native definitions, with every matched definition read. 7 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. MemN2N uses differentiable soft reads and answer supervision, unlike the original Memory Network framework and hard-retrieval MemNN instantiation. External stack/list operations and CommNet mean communication have distinct mechanisms. Generic external-memory wording is not LLM identity or a Neural Turing Machine equivalence. |
| mapping | sources/aio/aio.json | supports | Seven complete annotated AIO contexts support ANN as broader and AttentionLayer as a related component. Memory-Augmented LLM is too narrow in task/model scope; a memory cell, NTM controller, symmetric Hopfield attractor and temporal RNN are not equivalent identities. |
| sukhbaatar2015 | https://papers.neurips.cc/paper/5846-end-to-end-memory-networks.pdf; All nine primary proceedings pages visually read before curation. Selected method and evaluation pages reread after capture. Supplement, other versions and author code not inspected; no training or empirical replication. | supports | NIPS 2015 proceedings paper, volume 28, nine PDF pages. All pages, equations, figures, tables and references visually read; locators use PDF/printed page order. The arXiv identifier resolves the work; this evidence file is the primary proceedings PDF, not an asserted arXiv version. Supplement and author code not inspected. |
| calculation | research/discovery/end-to-end-memory-boundaries.py | supports | Chosen keys log2 and0 with values1 and3 give a soft read5/3. Paired permutation preserves the read, duplicate or zero-valued unmasked slots change it, and explicit position encoding distinguishes word orders with equal bag-of-words sums. No full model, temporal embedding, fitting or benchmark is implemented. |
| predecessor | reviews/structured/20261013T101336Z-memory-network-locator-findings/review.yaml | supports | Immutable initial review preserves both confirmed source-section locator findings. |
| corrected-record | data/curated/EndToEndMemoryNetwork.yaml | supports | Full corrected maintained record, synchronized report and EDIT history inspected. Primary headings confirm the corrected locators. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 602 native and 442 unchanged generated records. The 786-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All9pages visually read including formulas, figures, tables and references. Supplement, other versions and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T101937Z-end-to-end-memory-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of End-to-End Memory Network
started_at: '2026-10-13T10:15:12Z'
finished_at: '2026-10-13T10:19:37Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged key/value role separation, hop versus
    observation time, attention normalization, supplied-buffer limits and supervision/evaluation
    variants. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain MemN2N as a DRAFT neural architecture with broad ANN and related attention-component
  mappings. Six claims preserve mechanism, variant, supervision and finite-evaluation
  boundaries; author self-review resolved the source-locator finding through explicit
  predecessor links and corrected-input checks.
source:
  git_revision: 4b13f46070942eb9cc99296f28d42bf341801b5a
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
    role: target
  - path: data/curated/ListAugmentedRecurrentNeuralNetwork.yaml
    sha256: d0ae4afbb09ca9e76259fc4d75d1025b2233f06ac529acb401d198deede309b8
    role: context
  - path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
    sha256: f544aaabf56c79e2d2a66c37c3e357854ee751d00e05f890a4324f366e52055d
    role: context
  - path: research/discovery/20261013T100955Z-end-to-end-memory-network.json
    sha256: cc04862ee99932af59b95de9ad707791fcd6b6a966186edc6993783989153546
    role: context
  - path: research/discovery/end-to-end-memory-boundaries.py
    sha256: 3d75ee4945fe5d8db5b9f09f418c5839d1538f5a62cdf94bcca104177002ea08
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
- target_id: AIMech:EndToEndMemoryNetwork
  path: data/curated/EndToEndMemoryNetwork.yaml
  label: End-to-End Memory Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EndToEndMemoryNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:EndToEndMemoryNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:EndToEndMemoryNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All nine primary proceedings pages visually read before curation. Selected
      method and evaluation pages reread after capture. Supplement, other versions
      and author code not inspected; no training or empirical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 137.48s (0:02:17)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 603 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 267 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 264,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:EndToEndMemoryNetwork
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
  - AIMech:EndToEndMemoryNetwork
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
  - AIMech:EndToEndMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/end-to-end-memory-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"soft_weights": [0.6666666666666666, 0.3333333333333333], "read": 1.6666666666666665,
    "additive_next_query": 2.6666666666666665, "paired_permutation_invariant": true,
    "duplicated_slot_read": 1.4000000000000001, "zero_value_unmasked_slot_read": 1.25,
    "bow_reverse_equal": true, "position_encoded_forward": ["1/2", "1"], "position_encoded_reverse":
    ["1/2", "1/2"], "limits": "Chosen one-hop values only; temporal embeddings, training,
    full architecture and empirical results are not implemented."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T100955Z-end-to-end-memory-network.json
  accessed_at: '2026-10-13T10:15:12Z'
  support: supports
  summary: Compared all 442 pinned AIO and 601 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    17, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 60 AIO and 65 native definitions, with every matched definition read.
    7 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. MemN2N uses differentiable soft reads and answer supervision, unlike
    the original Memory Network framework and hard-retrieval MemNN instantiation.
    External stack/list operations and CommNet mean communication have distinct mechanisms.
    Generic external-memory wording is not LLM identity or a Neural Turing Machine
    equivalence.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T10:15:12Z'
  support: supports
  summary: Seven complete annotated AIO contexts support ANN as broader and AttentionLayer
    as a related component. Memory-Augmented LLM is too narrow in task/model scope;
    a memory cell, NTM controller, symmetric Hopfield attractor and temporal RNN are
    not equivalent identities.
- evidence_id: sukhbaatar2015
  kind: primary_source
  reference: https://papers.neurips.cc/paper/5846-end-to-end-memory-networks.pdf
  locator: All nine primary proceedings pages visually read before curation. Selected
    method and evaluation pages reread after capture. Supplement, other versions and
    author code not inspected; no training or empirical replication.
  accessed_at: '2026-10-13T09:21:47Z'
  snapshot_sha256: b518b8b0bd13f6ba48f11a9d98f831bac2c69ea5aec808e1eadd469b38e9970b
  support: supports
  summary: NIPS 2015 proceedings paper, volume 28, nine PDF pages. All pages, equations,
    figures, tables and references visually read; locators use PDF/printed page order.
    The arXiv identifier resolves the work; this evidence file is the primary proceedings
    PDF, not an asserted arXiv version. Supplement and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/end-to-end-memory-boundaries.py
  accessed_at: '2026-10-13T10:15:56Z'
  snapshot_sha256: 3d75ee4945fe5d8db5b9f09f418c5839d1538f5a62cdf94bcca104177002ea08
  support: supports
  summary: Chosen keys log2 and0 with values1 and3 give a soft read5/3. Paired permutation
    preserves the read, duplicate or zero-valued unmasked slots change it, and explicit
    position encoding distinguishes word orders with equal bag-of-words sums. No full
    model, temporal embedding, fitting or benchmark is implemented.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T101336Z-memory-network-locator-findings/review.yaml
  accessed_at: '2026-10-13T10:15:56Z'
  snapshot_sha256: 6ed1e23771f1612eb9d3a1f03c626a7e8a716f647368a21ef9d3e7361146f4a2
  support: supports
  summary: Immutable initial review preserves both confirmed source-section locator
    findings.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/EndToEndMemoryNetwork.yaml
  accessed_at: '2026-10-13T10:15:56Z'
  snapshot_sha256: 6c4806b22f49ed5ee492e207d08ed8665a62844b4dad44606d08d9e4b6cf69e6
  support: supports
  summary: Full corrected maintained record, synchronized report and EDIT history
    inspected. Primary headings confirm the corrected locators.
assessments:
- assessment_id: identity
  area: identity
  topic: End-to-End Memory Network
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - identity
  - sukhbaatar2015
  summary: Retain this distinct DRAFT architecture.
  details: MemN2N is an explicitly named end-to-end architecture with soft memory
    reads, distinct from the general I/G/O/R family, supervised hard-retrieval MemNN,
    stack/list controllers and CommNet.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - mapping
  - sukhbaatar2015
  summary: The declared AIO mapping is supported.
  details: Seven complete annotated AIO contexts support ANN as broader and AttentionLayer
    as a related component. Memory-Augmented LLM is too narrow in task/model scope;
    a memory cell, NTM controller, symmetric Hopfield attractor and temporal RNN are
    not equivalent identities.
- assessment_id: soft-memory-read
  area: evidence
  topic: soft-memory-read
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations1–3 separate A keys and C values, normalize query-key scores and
    sum weighted output embeddings before the answer softmax. The chosen read5/3 is
    neither of the two discrete stored values.
- assessment_id: hops-and-tying
  area: evidence
  topic: hops-and-tying
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2.2 distinguishes additive adjacent tying from layer-wise tying
    with H. Parameter identities, final W transpose and query initialization have
    precise roles; more hops do not require observed-time recurrence.
- assessment_id: word-and-memory-order
  area: evidence
  topic: word-and-memory-order
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The deterministic positional coordinate weights distinguish a reversed
    two-word example even when bag-of-words sums agree. Permuting complete embedded
    pairs preserves a soft sum, while temporal encodings can change when memory positions
    change.
- assessment_id: supervision-and-training
  area: evidence
  topic: supervision-and-training
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: The primary source contrasts answer-only MemN2N supervision with support-supervised
    MemNN. The linear-start training phase removes memory softmax before reintroduction;
    it is not silently identified with the ordinary normalized-read equations.
- assessment_id: finite-buffer-and-slot-boundaries
  area: evidence
  topic: finite-buffer-and-slot-boundaries
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Latest50sentence storage and null-word/temporal embedding details bound
    memory claims. Duplicating an unmasked slot or adding a zero-valued slot changes
    normalization and readout in the constructed examples. No author implementation
    masking convention is inferred.
- assessment_id: evaluation-and-output-scope
  area: evidence
  topic: evaluation-and-output-scope
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: QA and language-model input/query/tying/output rules differ; multiword
    QA answers are compound vocabulary entries. Table-level differences and rescaled
    heatmaps do not establish universal improvements, causal explanation or independent
    replication.
- assessment_id: constructed-boundaries
  area: consistency
  topic: key/value role separation, hop versus observation time, attention normalization,
    supplied-buffer limits and supervision/evaluation variants
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - sukhbaatar2015
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen keys log2 and0 with values1 and3 give a soft read5/3. Paired permutation
    preserves the read, duplicate or zero-valued unmasked slots change it, and explicit
    position encoding distinguishes word orders with equal bag-of-words sums. No full
    model, temporal embedding, fitting or benchmark is implemented.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - identity
  - mapping
  - sukhbaatar2015
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Complete corrected record and all mapping YAMLs
    reread after fresh capture. All primary method/evaluation pages specified in the
    initial reading were reread before locator-only corrections; the changed locator
    page was reread again after final capture. Scientific claims are unchanged. Constructed
    examples recomputed.
- assessment_id: review-remediation
  area: evidence
  topic: Issue262 source-locator correction
  outcome: supported
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  evidence_ids:
  - predecessor
  - corrected-record
  - sukhbaatar2015
  summary: Confirmed source-locator finding resolved.
  details: Two affected claim locators now match inspected primary headings, with
    explicit predecessor lineage.
findings:
- finding_id: F1
  issue_key: memn2n-training-buffer-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct End-to-End Memory Network source locators
  description: MemN2N training and buffer-limit locators omit Section 4.2. Linear-start,
    restarts, latest50 memory and zero null embedding are in Section4.2 on PDFp5.
    Section4.1 supplies temporal encoding, not those training details.
  target_ids:
  - AIMech:EndToEndMemoryNetwork
  field_paths:
  - claims[claim_id=supervision-and-training].evidence
  - claims[claim_id=finite-buffer-and-slot-boundaries].evidence
  evidence_ids:
  - predecessor
  - corrected-record
  - sukhbaatar2015
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EndToEndMemoryNetwork.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T101336Z-memory-network-locator-findings
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/262
  disposition_reason: Corrected two claim source-section locators against the actual
    primary-paper headings. Scientific statements unchanged. Full corrected record,
    exact report mirror, EDIT history and corrected-input checks establish resolution.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 602 native and 442 unchanged generated records.
  The 786-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All9pages visually read including formulas, figures, tables and references. Supplement,
  other versions and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T101336Z-memory-network-locator-findings
  relationship: Resolves only the explicitly linked locator finding for this record;
    companion review addresses the other record.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
