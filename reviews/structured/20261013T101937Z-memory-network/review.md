# Scientific author self-review of Memory Network

- Review: 20261013T101937Z-memory-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T10:15:14Z
- Finished UTC: 2026-10-13T10:19:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the original Memory Network family as DRAFT with a broad Network mapping. Six claims distinguish general components from neural instantiation and preserve state, supervision, retrieval and evaluation limits; author self-review resolved the source-locator finding through explicit predecessor links and corrected-input checks.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:MemoryNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4b13f46070942eb9cc99296f28d42bf341801b5a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MemoryNetwork | data/curated/MemoryNetwork.yaml | maintained | Memory Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MemoryNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 137.48s (0:02:17)<br>Checked 442 record(s); 0 failed.<br>Checked 603 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 267 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 264,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MemoryNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:MemoryNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:MemoryNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:MemoryNetwork | {"single_slot_update": ["a", "b", "c"], "parameters_unchanged": true, "role_conditioned_score_ab": 3, "role_conditioned_score_ba": 8, "global_max": "b", "restricted_candidate_max": "c", "chosen_pairwise_winners": ["c", "b"], "limits": "Constructed generic examples only. The cyclic preferences are not claimed to be a fitted paper model; author code, training and empirical evaluation are not executed."} |

## Scientific And Domain Assessments

### Memory Network

identity: supported. Targets: AIMech:MemoryNetwork.

Retain this distinct DRAFT model_family.

The original Section2 framework allows non-neural modules. The neural MemNN example is explicitly scoped within the family, not an exact alias for every implementation. The later MemN2N soft-read architecture differs in mechanism and supervision.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:MemoryNetwork.

The declared AIO mapping is supported.

Eight annotated AIO contexts were inspected. The generic Network target includes connected computational entities and is broader than the memory/input/update/inference/response system. ANN and temporal RNN do not cover all permitted non-neural implementations. LLM, internal cell, attention layer, NTM and Hopfield identities are not forced.

### memory-and-four-components

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section2 explicitly defines I/G/O/R and permits SVMs or decision trees. Memory updating precedes output inference; neural implementation is not a framework requirement.

### state-update-versus-parameter-learning

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Equation1 writes one selected slot and preserves others. Test-time memory changes coexist with fixed learned parameters; forgetting is mentioned as unexamined. The constructed slot update does not alter its separate parameter fixture.

### neural-instantiation-is-specific

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Section3 gives hard one/two-support argmax and word scoring, with role-specific embeddings and separate O/R parameters. The positive-semidefinite shared inner metric does not force symmetry after distinct role maps; the chosen scores3 and8 demonstrate the distinction.

### support-supervision-boundary

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Training knows supporting sentences and uses margin losses against sampled negatives; word segmentation also uses support-derived labels. Unknown argmax differentiation or answer-only learning is not established by these experiments.

### retrieval-extensions-and-order

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Hashing changes the candidate set. AppendixC uses pairwise comparisons with relative write-order features and states scalar-max equivalence without those features. A generic cyclic comparator demonstrates possible tournament order dependence without asserting such a trained source model was observed.

### evaluation-is-instantiation-specific

evidence: supported. Targets: AIMech:MemoryNetwork.

Supported within the stated primary-source and mathematical scope.

Large-triple QA reranking, support-supervised simulation, presegmented alternatives and multiword semantic scoring are distinct protocols. Small simulated grammar and asymmetric supervision do not support framework-wide accuracy or general language understanding.

### non-neural framework scope, test-time memory versus parameters, role-conditioned scores, support labels and restricted retrieval

consistency: supported. Targets: AIMech:MemoryNetwork.

Constructed calculations support the stated distinctions.

Chosen examples distinguish a single-slot state write from parameter updates, role-specific embedding scores from symmetric raw metrics, restricted retrieval from global maximization and general pairwise tournament order dependence. These are not trained-model, hash-recall or author-code experiments.

### All maintained fields

provenance: supported. Targets: AIMech:MemoryNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Complete corrected record and all mapping YAMLs reread after fresh capture. All primary method/evaluation pages specified in the initial reading were reread before locator-only corrections; the changed locator page was reread again after final capture. Scientific claims are unchanged. Constructed examples recomputed.

### Issue262 source-locator correction

evidence: supported. Targets: AIMech:MemoryNetwork.

Confirmed source-locator finding resolved.

Two affected claim locators now match inspected primary headings, with explicit predecessor lineage.

## Findings

### F2: Correct Memory Network source locators

minor / resolved / confirmed; issue key: memory-network-training-locators.

Basic neural training and Equations6–8 are in Section3.1 on PDFp4; Section3.2 concerns segmentation and Equation9. The response alternative is also Section3.1, pp3–4. Correct the current Section3.2-only training reference and related neural-instantiation locator.

Disposition: Corrected two claim source-section locators against the actual primary-paper headings. Scientific statements unchanged. Full corrected record, exact report mirror, EDIT history and corrected-input checks establish resolution.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T101028Z-memory-network.json | supports | Compared all 442 pinned AIO and 602 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 108, 12, 12 lines. All distinct match contents were inspected. Semantic matching covered 65 AIO and 86 native definitions, with every matched definition read. 8 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. The Section2 I/G/O/R framework explicitly permits non-neural components, while Section3 MemNN is a particular strongly supervised hard-retrieval neural implementation. The record denotes the original general family and carefully scopes that implementation. MemNN is searched as context, not asserted as an exact family-wide alias. MemN2N, external stack/list controllers and LLM memory systems have distinct identities. |
| mapping | sources/aio/aio.json | supports | Eight annotated AIO contexts were inspected. The generic Network target includes connected computational entities and is broader than the memory/input/update/inference/response system. ANN and temporal RNN do not cover all permitted non-neural implementations. LLM, internal cell, attention layer, NTM and Hopfield identities are not forced. |
| weston2015 | https://arxiv.org/pdf/1410.3916v11; All15pages of arXiv1410.3916v11 visually read before curation; selected method, evaluation and appendix pages reread after capture. Other versions and author code not inspected; no training or empirical replication. | supports | arXiv1410.3916v11,29November2015, with ICLR2015 publication header. All15PDFpages visually read, including AppendicesA–F. Locators use PDF/printed page order. Other versions and author code not inspected. |
| calculation | research/discovery/memory-network-boundaries.py | supports | Chosen examples distinguish a single-slot state write from parameter updates, role-specific embedding scores from symmetric raw metrics, restricted retrieval from global maximization and general pairwise tournament order dependence. These are not trained-model, hash-recall or author-code experiments. |
| predecessor | reviews/structured/20261013T101336Z-memory-network-locator-findings/review.yaml | supports | Immutable initial review preserves both confirmed source-section locator findings. |
| corrected-record | data/curated/MemoryNetwork.yaml | supports | Full corrected maintained record, synchronized report and EDIT history inspected. Primary headings confirm the corrected locators. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 603 native and 442 unchanged generated records. The 787-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All15pages of arXiv1410.3916v11 visually read, including all figures, tables, formulas and AppendicesA–F. Other versions and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T101937Z-memory-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Memory Network
started_at: '2026-10-13T10:15:14Z'
finished_at: '2026-10-13T10:19:37Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged non-neural framework scope, test-time
    memory versus parameters, role-conditioned scores, support labels and restricted
    retrieval. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the original Memory Network family as DRAFT with a broad Network mapping.
  Six claims distinguish general components from neural instantiation and preserve
  state, supervision, retrieval and evaluation limits; author self-review resolved
  the source-locator finding through explicit predecessor links and corrected-input
  checks.
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
  - path: data/aio/Network.yaml
    sha256: ec24eb397241fe903137b2d8c8f4081d0f9d246c296c247864f199e160a3ee30
    role: context
  - path: data/aio/NeuralTuringMachineNetwork.yaml
    sha256: bb483a9f90d767bcae50856c6084f31fe855d510d352419a5130fa4fc036be79
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/EndToEndMemoryNetwork.yaml
    sha256: 6c4806b22f49ed5ee492e207d08ed8665a62844b4dad44606d08d9e4b6cf69e6
    role: context
  - path: data/curated/ListAugmentedRecurrentNeuralNetwork.yaml
    sha256: d0ae4afbb09ca9e76259fc4d75d1025b2233f06ac529acb401d198deede309b8
    role: context
  - path: data/curated/MemoryNetwork.yaml
    sha256: 46acd0a723a761c602f633b7fe4c2aea0924883a9d0b57dbb0cf411da19a8673
    role: target
  - path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
    sha256: f544aaabf56c79e2d2a66c37c3e357854ee751d00e05f890a4324f366e52055d
    role: context
  - path: research/discovery/20261013T101028Z-memory-network.json
    sha256: 2ada5844e775b2c784664a2a8d1cb3bd10b307cfc4493499c6d7a73b579289b4
    role: context
  - path: research/discovery/memory-network-boundaries.py
    sha256: ff3b68d0ec762fe0afee8daa46ba1afa8ca702c41cecf778804fd4b918bf8e6a
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
- target_id: AIMech:MemoryNetwork
  path: data/curated/MemoryNetwork.yaml
  label: Memory Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MemoryNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:MemoryNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:MemoryNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All15pages of arXiv1410.3916v11 visually read before curation; selected
      method, evaluation and appendix pages reread after capture. Other versions and
      author code not inspected; no training or empirical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MemoryNetwork
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
  - AIMech:MemoryNetwork
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
  - AIMech:MemoryNetwork
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
  - AIMech:MemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/memory-network-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MemoryNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"single_slot_update": ["a", "b", "c"], "parameters_unchanged": true,
    "role_conditioned_score_ab": 3, "role_conditioned_score_ba": 8, "global_max":
    "b", "restricted_candidate_max": "c", "chosen_pairwise_winners": ["c", "b"], "limits":
    "Constructed generic examples only. The cyclic preferences are not claimed to
    be a fitted paper model; author code, training and empirical evaluation are not
    executed."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T101028Z-memory-network.json
  accessed_at: '2026-10-13T10:15:14Z'
  support: supports
  summary: Compared all 442 pinned AIO and 602 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    108, 12, 12 lines. All distinct match contents were inspected. Semantic matching
    covered 65 AIO and 86 native definitions, with every matched definition read.
    8 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. The Section2 I/G/O/R framework explicitly permits non-neural components,
    while Section3 MemNN is a particular strongly supervised hard-retrieval neural
    implementation. The record denotes the original general family and carefully scopes
    that implementation. MemNN is searched as context, not asserted as an exact family-wide
    alias. MemN2N, external stack/list controllers and LLM memory systems have distinct
    identities.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T10:15:14Z'
  support: supports
  summary: Eight annotated AIO contexts were inspected. The generic Network target
    includes connected computational entities and is broader than the memory/input/update/inference/response
    system. ANN and temporal RNN do not cover all permitted non-neural implementations.
    LLM, internal cell, attention layer, NTM and Hopfield identities are not forced.
- evidence_id: weston2015
  kind: primary_source
  reference: https://arxiv.org/pdf/1410.3916v11
  locator: All15pages of arXiv1410.3916v11 visually read before curation; selected
    method, evaluation and appendix pages reread after capture. Other versions and
    author code not inspected; no training or empirical replication.
  accessed_at: '2026-10-13T09:41:47Z'
  snapshot_sha256: 978ecaac3081beb72db3a4c40ca6264eb542008d2ab6dfb7766e1456e2312e99
  support: supports
  summary: arXiv1410.3916v11,29November2015, with ICLR2015 publication header. All15PDFpages
    visually read, including AppendicesA–F. Locators use PDF/printed page order. Other
    versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/memory-network-boundaries.py
  accessed_at: '2026-10-13T10:15:56Z'
  snapshot_sha256: ff3b68d0ec762fe0afee8daa46ba1afa8ca702c41cecf778804fd4b918bf8e6a
  support: supports
  summary: Chosen examples distinguish a single-slot state write from parameter updates,
    role-specific embedding scores from symmetric raw metrics, restricted retrieval
    from global maximization and general pairwise tournament order dependence. These
    are not trained-model, hash-recall or author-code experiments.
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
  reference: data/curated/MemoryNetwork.yaml
  accessed_at: '2026-10-13T10:15:56Z'
  snapshot_sha256: 46acd0a723a761c602f633b7fe4c2aea0924883a9d0b57dbb0cf411da19a8673
  support: supports
  summary: Full corrected maintained record, synchronized report and EDIT history
    inspected. Primary headings confirm the corrected locators.
assessments:
- assessment_id: identity
  area: identity
  topic: Memory Network
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - identity
  - weston2015
  summary: Retain this distinct DRAFT model_family.
  details: The original Section2 framework allows non-neural modules. The neural MemNN
    example is explicitly scoped within the family, not an exact alias for every implementation.
    The later MemN2N soft-read architecture differs in mechanism and supervision.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - mapping
  - weston2015
  summary: The declared AIO mapping is supported.
  details: Eight annotated AIO contexts were inspected. The generic Network target
    includes connected computational entities and is broader than the memory/input/update/inference/response
    system. ANN and temporal RNN do not cover all permitted non-neural implementations.
    LLM, internal cell, attention layer, NTM and Hopfield identities are not forced.
- assessment_id: memory-and-four-components
  area: evidence
  topic: memory-and-four-components
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2 explicitly defines I/G/O/R and permits SVMs or decision trees.
    Memory updating precedes output inference; neural implementation is not a framework
    requirement.
- assessment_id: state-update-versus-parameter-learning
  area: evidence
  topic: state-update-versus-parameter-learning
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation1 writes one selected slot and preserves others. Test-time memory
    changes coexist with fixed learned parameters; forgetting is mentioned as unexamined.
    The constructed slot update does not alter its separate parameter fixture.
- assessment_id: neural-instantiation-is-specific
  area: evidence
  topic: neural-instantiation-is-specific
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3 gives hard one/two-support argmax and word scoring, with role-specific
    embeddings and separate O/R parameters. The positive-semidefinite shared inner
    metric does not force symmetry after distinct role maps; the chosen scores3 and8
    demonstrate the distinction.
- assessment_id: support-supervision-boundary
  area: evidence
  topic: support-supervision-boundary
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: Training knows supporting sentences and uses margin losses against sampled
    negatives; word segmentation also uses support-derived labels. Unknown argmax
    differentiation or answer-only learning is not established by these experiments.
- assessment_id: retrieval-extensions-and-order
  area: evidence
  topic: retrieval-extensions-and-order
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Hashing changes the candidate set. AppendixC uses pairwise comparisons
    with relative write-order features and states scalar-max equivalence without those
    features. A generic cyclic comparator demonstrates possible tournament order dependence
    without asserting such a trained source model was observed.
- assessment_id: evaluation-is-instantiation-specific
  area: evidence
  topic: evaluation-is-instantiation-specific
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  summary: Supported within the stated primary-source and mathematical scope.
  details: Large-triple QA reranking, support-supervised simulation, presegmented
    alternatives and multiword semantic scoring are distinct protocols. Small simulated
    grammar and asymmetric supervision do not support framework-wide accuracy or general
    language understanding.
- assessment_id: constructed-boundaries
  area: consistency
  topic: non-neural framework scope, test-time memory versus parameters, role-conditioned
    scores, support labels and restricted retrieval
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - weston2015
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen examples distinguish a single-slot state write from parameter updates,
    role-specific embedding scores from symmetric raw metrics, restricted retrieval
    from global maximization and general pairwise tournament order dependence. These
    are not trained-model, hash-recall or author-code experiments.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:MemoryNetwork
  evidence_ids:
  - identity
  - mapping
  - weston2015
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
  - AIMech:MemoryNetwork
  evidence_ids:
  - predecessor
  - corrected-record
  - weston2015
  summary: Confirmed source-locator finding resolved.
  details: Two affected claim locators now match inspected primary headings, with
    explicit predecessor lineage.
findings:
- finding_id: F2
  issue_key: memory-network-training-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct Memory Network source locators
  description: Basic neural training and Equations6–8 are in Section3.1 on PDFp4;
    Section3.2 concerns segmentation and Equation9. The response alternative is also
    Section3.1, pp3–4. Correct the current Section3.2-only training reference and
    related neural-instantiation locator.
  target_ids:
  - AIMech:MemoryNetwork
  field_paths:
  - claims[claim_id=neural-instantiation-is-specific].evidence
  - claims[claim_id=support-supervision-boundary].evidence
  evidence_ids:
  - predecessor
  - corrected-record
  - weston2015
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MemoryNetwork.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T101336Z-memory-network-locator-findings
    finding_id: F2
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
- One new DRAFT concept, yielding 603 native and 442 unchanged generated records.
  The 787-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All15pages of arXiv1410.3916v11 visually read, including all figures, tables, formulas
  and AppendicesA–F. Other versions and author code not inspected.
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
