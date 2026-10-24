# Scientific author self-review of Dynamic Memory Network Plus

- Review: 20261013T110057Z-dynamic-memory-network-plus
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T10:54:12Z
- Finished UTC: 2026-10-13T11:00:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain DMN+ as DRAFT with broad RNN and related GRU mappings. Six claims preserve source-notation issues, architectural distinctions and experimental limits. Author self-review resolves its confirmed Issue265 finding, preserving the immutable initial observation.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:DynamicMemoryNetworkPlus
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5f5966223a21ece5924450317e72c926b42cdaed.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DynamicMemoryNetworkPlus | data/curated/DynamicMemoryNetworkPlus.yaml | maintained | Dynamic Memory Network Plus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DynamicMemoryNetworkPlus | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 233.45s (0:03:53)<br>Checked 442 record(s); 0 failed.<br>Checked 607 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 273 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 269,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DynamicMemoryNetworkPlus | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:DynamicMemoryNetworkPlus | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:DynamicMemoryNetworkPlus | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:DynamicMemoryNetworkPlus | {"replaced_update_gate": 0.5134618428048621, "gate_outside_full_gru": 0.4494232899634034, "ordered_scan": 0.6780378586752849, "reversed_scan": 0.6638781563696936, "old_weighted_convention": 0.406730921402431, "candidate_weighted_convention": 0.7269236856097242, "concatenated_input_width": 3, "output_width": 1, "rectified_update": 2.0, "limits": "Constructed finite formula checks only; no learned gates, recurrent fusion implementation, stopping controller or benchmark."} |

## Scientific And Domain Assessments

### Dynamic Memory Network Plus

identity: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Retain this distinct DRAFT architecture.

Final DMN+ is retained as a distinct successor combining input fusion, attention-based GRU and untied ReLU memory. Original DMN and intermediate ablations are not aliases.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

The declared AIO mapping is supported.

Eight annotated AIO contexts support broad RNN and related GRU component. The MLP gate is not the pinned dot-product AttentionLayer identity; LLM, memory cell, NTM and Hopfield mappings are not forced.

### fused-text-and-image-facts

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

Sections3.1–3.2 use position-weighted sentence embeddings with summed bidirectional GRU states, and projected visual regions with snake-order fusion. No arbitrary patch invariance or exact segmentation follows.

### normalized-attention-gru

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

The scalar attention gate replaces the GRU update gate, whereas original DMN gates an entire GRU output. Eq11 and the constructed formulas distinguish them. A fixed-vector weighted sum and the complete context encoder have different order properties.

### untied-memory-and-printed-notation

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

Eq13 concatenates three n_H vectors before a rectified affine map. Its printed square-matrix dimension is inconsistent; the required input width is explicitly labelled inference. Eq10 fact-count notation is likewise preserved as a source inconsistency.

### answer-supervised-finite-protocol

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

Sections5–6 distinguish answer-supervised bAbI10k training from original support-labelled QA, and retain finite passes, truncated inputs, early stopping and restart selection. Ablation rows are not treated as equivalent names.

### task-and-metric-boundaries

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

DAQUAR single-word filtering, VQA human agreement and bAbI errors are separate denominators. Corrected Table3 number scores are DMN+36.8, SAN36.6 and D-NMN37.4. The tables include weaker task/answer-type results; aggregate gains do not prove universal superiority.

### order-and-visualization-limits

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Supported within the stated primary-source and mathematical scope.

Recurrent scan order matters in a constructed example. Figure6 selected gate maps do not certify causal object localization; source counting limitations and patch boundaries remain.

### recurrent gate placement, normalized attention, inconsistent printed dimensions, support labels and bounded visual/text evaluation

consistency: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Constructed calculations support the stated distinctions.

Chosen formulas distinguish replacing a GRU update gate from gating an entire GRU, preserve recurrent order dependence and expose the matrix width required by concatenation. No learned model, author code or benchmark is executed.

### All maintained fields

provenance: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Full maintained record and eight mapping YAMLs reread after capture; primary methods, equations, evaluation tables and visualizations reread against initial captured bytes; corrected Table3 comparison reread after recapture. Constructed gate placement, convention, order and dimension checks recomputed.

### Issue265 evidence accuracy correction

evidence: supported. Targets: AIMech:DynamicMemoryNetworkPlus.

Confirmed evidence-accuracy finding resolved.

The affected benchmark comparison or equation locators now match the primary evidence, with explicit predecessor lineage.

## Findings

### F1: Correct Dynamic Memory Network Plus evidence accuracy

major / resolved / confirmed; issue key: dmn-plus-vqa-number-comparator.

The draft states that the DMN+ VQA number score is below SAN. Table3 on PDFp8 instead reports DMN+36.8 and SAN36.6. Other listed systems exceed DMN+ on numbers, including D-NMN37.4. Correct the named comparison and retain the bounded aggregate-performance conclusion.

Disposition: Corrected the DMN+ VQA-number comparator or the three Attentive Pooling equation ranges, as applicable. Full corrected record, exact report mirror, EDIT history and corrected-input checks establish resolution.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T104420Z-dynamic-memory-network-plus.json | supports | Compared all 442 pinned AIO and 605 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 39, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 65 AIO and 89 native definitions, with every matched definition read. 8 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. DMN+ is the named successor with bidirectional fact fusion, scalar attention replacing the GRU update gate, and untied ReLU memory updates. It is not an alias of the original DMN, the intermediate DMN2/DMN3 ablations, KV-MemNN or CommNet. Existing incidental DMN+ benchmark mentions are not a maintained identity. |
| mapping | sources/aio/aio.json | supports | Eight annotated AIO contexts support broad RNN and related GRU component. The MLP gate is not the pinned dot-product AttentionLayer identity; LLM, memory cell, NTM and Hopfield mappings are not forced. |
| xiong2016 | https://arxiv.org/pdf/1603.01417v1; All ten pages of arXiv1603.01417v1 visually read before curation; pages2–9 reread after the initial capture; the correction evidence reread after the corrected capture. Other versions, author code, training and empirical replication not inspected. | supports | arXiv 1603.01417v1, 4 March 2016, ten PDF pages. All pages visually read, including equations, diagrams, tables and references. Locators use PDF page order. Other versions and author code not inspected. |
| calculation | research/discovery/dynamic-memory-plus-boundaries.py | supports | Chosen formulas distinguish replacing a GRU update gate from gating an entire GRU, preserve recurrent order dependence and expose the matrix width required by concatenation. No learned model, author code or benchmark is executed. |
| predecessor | reviews/structured/20261013T105057Z-dmn-plus-attentive-pooling-findings/review.yaml | supports | Immutable initial review preserves the confirmed DMN+ benchmark comparison and Attentive Pooling locator findings. |
| corrected-record | data/curated/DynamicMemoryNetworkPlus.yaml | supports | Full corrected maintained record, synchronized report and EDIT history inspected. Table3 confirms the corrected comparison; Section3 ends at Equation18. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 606 native and 442 unchanged generated records. The 790-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All ten primary pages visually inspected; no author code or other version inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T110057Z-dynamic-memory-network-plus
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Dynamic Memory Network Plus
started_at: '2026-10-13T10:54:12Z'
finished_at: '2026-10-13T11:00:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged recurrent gate placement, normalized attention,
    inconsistent printed dimensions, support labels and bounded visual/text evaluation.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain DMN+ as DRAFT with broad RNN and related GRU mappings. Six claims
  preserve source-notation issues, architectural distinctions and experimental limits.
  Author self-review resolves its confirmed Issue265 finding, preserving the immutable
  initial observation.
source:
  git_revision: 5f5966223a21ece5924450317e72c926b42cdaed
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
  - path: data/curated/CommunicationNeuralNetwork.yaml
    sha256: 6da13aca3d17822181f43ddfb796a62170d2cdbb28a2e01a5d541c9a1ff8d813
    role: context
  - path: data/curated/DynamicMemoryNetwork.yaml
    sha256: 0affc6bdf4fd1c02c6d423d8560b53d357f5eca0ec8d93d29176375da25636fe
    role: context
  - path: data/curated/DynamicMemoryNetworkPlus.yaml
    sha256: a7360c19312b2db3e79fdebcf74908537e3d1582488646b164c9a97a6c6568d6
    role: target
  - path: data/curated/KeyValueMemoryNetwork.yaml
    sha256: 7c1c576ad0b4626e66cdcafbba48877a7058c145b07c55fb2a9317d789ad2831
    role: context
  - path: research/discovery/20261013T104420Z-dynamic-memory-network-plus.json
    sha256: 07c00ab1cb5ad9e01c42f7a773e0f248bbfc853e24fb37f05f705a1bfbed3e5d
    role: context
  - path: research/discovery/dynamic-memory-plus-boundaries.py
    sha256: 10920e3c1900743ca04452fc6d0d2f3096a2237d9bc32559d0a20892e4987dd5
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
- target_id: AIMech:DynamicMemoryNetworkPlus
  path: data/curated/DynamicMemoryNetworkPlus.yaml
  label: Dynamic Memory Network Plus
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DynamicMemoryNetworkPlus.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:DynamicMemoryNetworkPlus'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All ten pages of arXiv1603.01417v1 visually read before curation; pages2–9
      reread after the initial capture; the correction evidence reread after the corrected
      capture. Other versions, author code, training and empirical replication not
      inspected.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 233.45s (0:03:53)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 607 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 273 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 269,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
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
  - AIMech:DynamicMemoryNetworkPlus
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
  - AIMech:DynamicMemoryNetworkPlus
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/dynamic-memory-plus-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  exit_code: 0
  expected_exit_code: 0
  summary: '{"replaced_update_gate": 0.5134618428048621, "gate_outside_full_gru":
    0.4494232899634034, "ordered_scan": 0.6780378586752849, "reversed_scan": 0.6638781563696936,
    "old_weighted_convention": 0.406730921402431, "candidate_weighted_convention":
    0.7269236856097242, "concatenated_input_width": 3, "output_width": 1, "rectified_update":
    2.0, "limits": "Constructed finite formula checks only; no learned gates, recurrent
    fusion implementation, stopping controller or benchmark."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T104420Z-dynamic-memory-network-plus.json
  accessed_at: '2026-10-13T10:54:12Z'
  support: supports
  summary: Compared all 442 pinned AIO and 605 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    39, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 65 AIO and 89 native definitions, with every matched definition read.
    8 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. DMN+ is the named successor with bidirectional fact fusion, scalar
    attention replacing the GRU update gate, and untied ReLU memory updates. It is
    not an alias of the original DMN, the intermediate DMN2/DMN3 ablations, KV-MemNN
    or CommNet. Existing incidental DMN+ benchmark mentions are not a maintained identity.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T10:54:12Z'
  support: supports
  summary: Eight annotated AIO contexts support broad RNN and related GRU component.
    The MLP gate is not the pinned dot-product AttentionLayer identity; LLM, memory
    cell, NTM and Hopfield mappings are not forced.
- evidence_id: xiong2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1603.01417v1
  locator: All ten pages of arXiv1603.01417v1 visually read before curation; pages2–9
    reread after the initial capture; the correction evidence reread after the corrected
    capture. Other versions, author code, training and empirical replication not inspected.
  accessed_at: '2026-10-13T10:22:19Z'
  snapshot_sha256: ce961743dc7bc5ebd00a86dd7209476d4dc0e4f24dcf2cb36054bb50bda0f2ab
  support: supports
  summary: arXiv 1603.01417v1, 4 March 2016, ten PDF pages. All pages visually read,
    including equations, diagrams, tables and references. Locators use PDF page order.
    Other versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/dynamic-memory-plus-boundaries.py
  accessed_at: '2026-10-13T10:55:24Z'
  snapshot_sha256: 10920e3c1900743ca04452fc6d0d2f3096a2237d9bc32559d0a20892e4987dd5
  support: supports
  summary: Chosen formulas distinguish replacing a GRU update gate from gating an
    entire GRU, preserve recurrent order dependence and expose the matrix width required
    by concatenation. No learned model, author code or benchmark is executed.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T105057Z-dmn-plus-attentive-pooling-findings/review.yaml
  accessed_at: '2026-10-13T10:55:24Z'
  snapshot_sha256: 8fcc472e17c5e34087a2693393b74f52d2fa03ed32e1ac53c8759f029a39af99
  support: supports
  summary: Immutable initial review preserves the confirmed DMN+ benchmark comparison
    and Attentive Pooling locator findings.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/DynamicMemoryNetworkPlus.yaml
  accessed_at: '2026-10-13T10:55:24Z'
  snapshot_sha256: a7360c19312b2db3e79fdebcf74908537e3d1582488646b164c9a97a6c6568d6
  support: supports
  summary: Full corrected maintained record, synchronized report and EDIT history
    inspected. Table3 confirms the corrected comparison; Section3 ends at Equation18.
assessments:
- assessment_id: identity
  area: identity
  topic: Dynamic Memory Network Plus
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - identity
  - xiong2016
  summary: Retain this distinct DRAFT architecture.
  details: Final DMN+ is retained as a distinct successor combining input fusion,
    attention-based GRU and untied ReLU memory. Original DMN and intermediate ablations
    are not aliases.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - mapping
  - xiong2016
  summary: The declared AIO mapping is supported.
  details: Eight annotated AIO contexts support broad RNN and related GRU component.
    The MLP gate is not the pinned dot-product AttentionLayer identity; LLM, memory
    cell, NTM and Hopfield mappings are not forced.
- assessment_id: fused-text-and-image-facts
  area: evidence
  topic: fused-text-and-image-facts
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections3.1–3.2 use position-weighted sentence embeddings with summed bidirectional
    GRU states, and projected visual regions with snake-order fusion. No arbitrary
    patch invariance or exact segmentation follows.
- assessment_id: normalized-attention-gru
  area: evidence
  topic: normalized-attention-gru
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The scalar attention gate replaces the GRU update gate, whereas original
    DMN gates an entire GRU output. Eq11 and the constructed formulas distinguish
    them. A fixed-vector weighted sum and the complete context encoder have different
    order properties.
- assessment_id: untied-memory-and-printed-notation
  area: evidence
  topic: untied-memory-and-printed-notation
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Eq13 concatenates three n_H vectors before a rectified affine map. Its
    printed square-matrix dimension is inconsistent; the required input width is explicitly
    labelled inference. Eq10 fact-count notation is likewise preserved as a source
    inconsistency.
- assessment_id: answer-supervised-finite-protocol
  area: evidence
  topic: answer-supervised-finite-protocol
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections5–6 distinguish answer-supervised bAbI10k training from original
    support-labelled QA, and retain finite passes, truncated inputs, early stopping
    and restart selection. Ablation rows are not treated as equivalent names.
- assessment_id: task-and-metric-boundaries
  area: evidence
  topic: task-and-metric-boundaries
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: DAQUAR single-word filtering, VQA human agreement and bAbI errors are separate
    denominators. Corrected Table3 number scores are DMN+36.8, SAN36.6 and D-NMN37.4.
    The tables include weaker task/answer-type results; aggregate gains do not prove
    universal superiority.
- assessment_id: order-and-visualization-limits
  area: evidence
  topic: order-and-visualization-limits
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Recurrent scan order matters in a constructed example. Figure6 selected
    gate maps do not certify causal object localization; source counting limitations
    and patch boundaries remain.
- assessment_id: constructed-boundaries
  area: consistency
  topic: recurrent gate placement, normalized attention, inconsistent printed dimensions,
    support labels and bounded visual/text evaluation
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - xiong2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen formulas distinguish replacing a GRU update gate from gating an
    entire GRU, preserve recurrent order dependence and expose the matrix width required
    by concatenation. No learned model, author code or benchmark is executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - identity
  - mapping
  - xiong2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Full maintained record and eight mapping YAMLs
    reread after capture; primary methods, equations, evaluation tables and visualizations
    reread against initial captured bytes; corrected Table3 comparison reread after
    recapture. Constructed gate placement, convention, order and dimension checks
    recomputed.
- assessment_id: review-remediation
  area: evidence
  topic: Issue265 evidence accuracy correction
  outcome: supported
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  evidence_ids:
  - predecessor
  - corrected-record
  - xiong2016
  summary: Confirmed evidence-accuracy finding resolved.
  details: The affected benchmark comparison or equation locators now match the primary
    evidence, with explicit predecessor lineage.
findings:
- finding_id: F1
  issue_key: dmn-plus-vqa-number-comparator
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct Dynamic Memory Network Plus evidence accuracy
  description: The draft states that the DMN+ VQA number score is below SAN. Table3
    on PDFp8 instead reports DMN+36.8 and SAN36.6. Other listed systems exceed DMN+
    on numbers, including D-NMN37.4. Correct the named comparison and retain the bounded
    aggregate-performance conclusion.
  target_ids:
  - AIMech:DynamicMemoryNetworkPlus
  field_paths:
  - claims[claim_id=task-and-metric-boundaries].statement
  evidence_ids:
  - predecessor
  - corrected-record
  - xiong2016
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DynamicMemoryNetworkPlus.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T105057Z-dmn-plus-attentive-pooling-findings
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/265
  disposition_reason: Corrected the DMN+ VQA-number comparator or the three Attentive
    Pooling equation ranges, as applicable. Full corrected record, exact report mirror,
    EDIT history and corrected-input checks establish resolution.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 606 native and 442 unchanged generated records.
  The 790-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All ten primary pages visually inspected; no author code or other version inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T105057Z-dmn-plus-attentive-pooling-findings
  relationship: Resolves only the explicitly linked evidence-accuracy finding for
    this record; companion review addresses the other record.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
