# AIMech Cycle 1 Stage 5 Issue Map and Finding Dispositions (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `2` (supersedes `revision-0001`)
- **Source Revision (`main`)**: `06fd3aac34a3001757944d865c0f2267271cdd9f`
- **Scope Frozen At**: `2026-11-04T13:33:00Z`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: 9747831b405b60f12fdfd22337058b1edae8002e053e6f20add750dfdb61f049`)
- **Initial Stage 5 Native Structured Review**: `reviews/structured/20261104T142000Z-c1s5-curated-remediation-review/review.yaml` (`sha256: 454c1e55a995f66e6bf5c6f2574901aa7be61d806e375b3b5cce1b9946ac6067`)
- **Post-Suite Linked Successor Structured Review**: `reviews/structured/20261104T145000Z-c1s5-curated-remediation-review/review.yaml` (`sha256: f0266f7877763e71040411c7d9183d64ba286e7642de79f4cf4eac2c0fdb7545`)

## 1. Deduplication Against Open GitHub Issues in `CultureBotAI/AIMech`

Before creating issues, all open issues in `CultureBotAI/AIMech` (`#10`–`#16`, `#383`, `#396`, `#397`, `#403`) were inspected:

- None of the existing open issues matched the 3 maintained-record provenance/grounding findings (`F-C1S4-001`..`F-C1S4-003`) or the 3 upstream AIO ontology findings (`F-C1S4-004`..`F-C1S4-006`) surfaced in Cycle 1 Stage 4.
- Four bounded GitHub issues (`#451`, `#452`, `#453`, `#454`) were created in `CultureBotAI/AIMech`, grouping the 6 carried-forward findings by shared root cause and repair ownership.

## 2. Finding Groups and GitHub Issue Mapping

| Group ID | Finding IDs | Issue Key(s) | GitHub Issue | Repair Owner | Status | Summary |
| --- | --- | --- | --- | --- | --- | --- |
| `G-C1S5-001` | `F-C1S4-001` | `aimech-first-native-cohort-pdf-provenance` | [#451](https://github.com/CultureBotAI/AIMech/issues/451) | `data/curated/{ExpectationMaximization,MarkovDecisionProcess,PartiallyObservableMarkovDecisionProcess}.yaml` + `history/records/<slug>/` | `resolved` | Record verified primary PDF `sha256` digests, strip `#page=` viewer fragments from canonical URLs, and add `persistent_id: doi:10.1016/S0004-3702(98)00023-X` |
| `G-C1S5-002` | `F-C1S4-002` | `aimech-curated-documentation-missing-sha256` | [#452](https://github.com/CultureBotAI/AIMech/issues/452) | `data/curated/{Apriori,BarlowTwins,Eclat,GeneticAlgorithm,HiddenMarkovModel,VICReg}.yaml` + `history/records/<slug>/` | `resolved` | Populate verified `sha256` content digests on all 7 `access_level: documentation` evidence sources across 6 maintained records |
| `G-C1S5-003` | `F-C1S4-003` | `aimech-curated-identity-mapping-proposal-diary-carryover` | [#453](https://github.com/CultureBotAI/AIMech/issues/453) | `data/curated/{CLARANSClustering,GloVe,LargeMarginNearestNeighbor,MarkovRandomField,RelevantComponentAnalysis}.yaml` + `history/records/<slug>/` | `resolved` | Differentiate target-specific `aio_mappings[].rationale` in `GloVe.yaml` and remove candidate-proposal / batch-discovery diary text from `identity_notes` |
| `G-C1S5-004` | `F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006` | `aio-upstream-near-duplicate-class-boundaries`, `aio-upstream-genus-hierarchy-mismatch`, `aio-upstream-deep-feed-forward-synonym-typo` | [#454](https://github.com/CultureBotAI/AIMech/issues/454) | Upstream `berkeleybop/artificial-intelligence-ontology` (`sources/aio/aio.json` via `aimech-refresh-aio`) | `deferred` | Defer 3 upstream AIO ontology defects across 9 generated `data/aio/*.yaml` records to upstream ontology curation and future `aimech-refresh-aio` cycles |

## 3. Per-Finding Dispositions and Maintained Owner Artifacts

### `F-C1S4-001` (`resolved` — `G-C1S5-001`, [#451](https://github.com/CultureBotAI/AIMech/issues/451))
- **Issue Key**: `aimech-first-native-cohort-pdf-provenance`
- **Predecessor Occurrence**: `20261104T112600Z-c1s4-curated-provenance-mapping-review` (`F-C1S4-001`)
- **Successor Review Verification**: `20261104T145000Z-c1s5-curated-remediation-review` (superseding `20261104T142000Z-c1s5-curated-remediation-review`, `F-C1S4-001`, `status: resolved`, assessment `ASM-C1S5-PDF-PROVENANCE-RESOLVED`)
- **Remediation & History Sidecars**:
  - `data/curated/ExpectationMaximization.yaml` (`sha256: df46faf98d2b4dbcd5c9456e63e74658f65e6555b68115f07b9b6910a7df76a8`) + `history/records/ExpectationMaximization/2026-11-04T141532Z-antigravity-3be937.yaml`: inspected Bilmes (1998) TR-97-021 PDF (15 pages, 193,778 bytes), stripped `#page=3` from `evidence_sources[0].url`, and recorded `sha256: 7ccc87d9ba4abfe1f46c221e29a1c9ced4eb9731fd4d91c7a094b601cc02a024`.
  - `data/curated/MarkovDecisionProcess.yaml` (`sha256: 68e13acf60ac0fc76bd9763af5fc64716125b5dcd99798115dbbe528de76762c`) + `history/records/MarkovDecisionProcess/2026-11-04T141532Z-antigravity-ae9503.yaml`: inspected Kaelbling et al. (1998) *Artificial Intelligence* 101:99-134 PDF (36 pages, 426,460 bytes), stripped `#page=3` from `evidence_sources[0].url`, added `persistent_id: doi:10.1016/S0004-3702(98)00023-X`, and recorded `sha256: 71a6d1aee278e93c5fae8dd7d0c452c8b7b035af55d9dce2bc367d473bfc9645`.
  - `data/curated/PartiallyObservableMarkovDecisionProcess.yaml` (`sha256: db743bbf4823c6ac64d110cc3d32342dfd5818bcd38136a28de386ad01ea37bf`) + `history/records/PartiallyObservableMarkovDecisionProcess/2026-11-04T141532Z-antigravity-8f6851.yaml`: inspected Kaelbling et al. (1998) PDF, stripped `#page=7` from `evidence_sources[0].url`, added `persistent_id: doi:10.1016/S0004-3702(98)00023-X`, and recorded `sha256: 71a6d1aee278e93c5fae8dd7d0c452c8b7b035af55d9dce2bc367d473bfc9645`.

### `F-C1S4-002` (`resolved` — `G-C1S5-002`, [#452](https://github.com/CultureBotAI/AIMech/issues/452))
- **Issue Key**: `aimech-curated-documentation-missing-sha256`
- **Predecessor Occurrence**: `20261104T112600Z-c1s4-curated-provenance-mapping-review` (`F-C1S4-002`)
- **Successor Review Verification**: `20261104T145000Z-c1s5-curated-remediation-review` (superseding `20261104T142000Z-c1s5-curated-remediation-review`, `F-C1S4-002`, `status: resolved`, assessment `ASM-C1S5-DOC-SHA256-RESOLVED`)
- **Remediation & History Sidecars**:
  - `data/curated/Apriori.yaml` (`sha256: 5d3b0bbb849a8cc11bfdbc235a861d7b35f36969b07a7d46281d0bac14f99987`) + `history/records/Apriori/2026-11-04T141532Z-antigravity-f2157d.yaml` (`evidence_sources[0].sha256 = 53ebb565d1913dd8d4f240fc5b0e17842c04f01a23f35fdb766efdaf97c12544`)
  - `data/curated/Eclat.yaml` (`sha256: 0ecebf216f2d0c8c12cfeca21a2f85f7689299808506209153857a02fd365a5f`) + `history/records/Eclat/2026-11-04T141532Z-antigravity-147095.yaml` (`evidence_sources[0].sha256 = b1b85b34f34853842ebb85a6ac497a0bdd5452e9865956b6e1e1e1ae2e3bb835`)
  - `data/curated/GeneticAlgorithm.yaml` (`sha256: fad7091726036606a8fb8c34232f2f2dd53d08b0608f2e97acdcfad769404ad9`) + `history/records/GeneticAlgorithm/2026-11-04T141532Z-antigravity-a79adb.yaml` (`evidence_sources[0].sha256 = c12c835bb781cf8e1018c9cee786c549a10a653a6efa4c852afd20b969a1c1e8`)
  - `data/curated/HiddenMarkovModel.yaml` (`sha256: 12e18fdb093233e0d0ecb5cf7698fc94dd03b6adbbf0dace436d82ae63b167de`) + `history/records/HiddenMarkovModel/2026-11-04T141532Z-antigravity-c9c131.yaml` (`evidence_sources[0].sha256 = c33b67d7f77543da50e5c436c1b19644ef74f8f13a3e340866466cff25734188`)
  - `data/curated/BarlowTwins.yaml` (`sha256: 68c763b31eb58ed2fe4b637675e1fe283f109ee9a38ef02dc24eb2f0fc298496`) + `history/records/BarlowTwins/2026-11-04T141532Z-antigravity-9ac5b6.yaml` (`evidence_sources[2].sha256 = 2e2dfa7111415f7dd47ac8487fe58fd7b223a67f91c374494768206c70779bf5`)
  - `data/curated/VICReg.yaml` (`sha256: bb5e751b5bc06d74a77b7f0cdcb24108873b54df74357634a0e7e2038ed0c9f0`) + `history/records/VICReg/2026-11-04T141532Z-antigravity-7923b0.yaml` (`evidence_sources[2].sha256 = 4704f2227121b5f921af7ddeea110d2bf1e98f99f98dd5bef3c6bab478f087af`, `evidence_sources[3].sha256 = 2b09e329187a5713f8f9dd78db1180f06c7386ec5996870d21a76f91c5388694`)

### `F-C1S4-003` (`resolved` — `G-C1S5-003`, [#453](https://github.com/CultureBotAI/AIMech/issues/453))
- **Issue Key**: `aimech-curated-identity-mapping-proposal-diary-carryover`
- **Predecessor Occurrence**: `20261104T112600Z-c1s4-curated-provenance-mapping-review` (`F-C1S4-003`)
- **Successor Review Verification**: `20261104T145000Z-c1s5-curated-remediation-review` (superseding `20261104T142000Z-c1s5-curated-remediation-review`, `F-C1S4-003`, `status: resolved`, assessment `ASM-C1S5-GROUNDING-AND-IDENTITY-NOTES-RESOLVED`)
- **Remediation & History Sidecars**:
  - `data/curated/GloVe.yaml` (`sha256: efad5a877f905f1b0f9e85b2b453189e3d2537e1c2fb5181b577a47ac8b1c08a`) + `history/records/GloVe/2026-11-04T141532Z-antigravity-53d435.yaml`: differentiated `aio_mappings[0..2].rationale` for `AIO:RepresentationLearning` (`broad`), `AIO:word2vecCBOW` (`related`), and `AIO:word2vecSkipGram` (`related`).
  - `data/curated/MarkovRandomField.yaml` (`sha256: 4f42ed2a995837d69b0a755e940b12986ca069130bb6b87087ccabed290ae94e`) + `history/records/MarkovRandomField/2026-11-04T141532Z-antigravity-f01fa7.yaml`: replaced candidate-proposal phrasing in `identity_notes` and `aio_mappings[0].rationale`.
  - `data/curated/CLARANSClustering.yaml` (`sha256: aa1c9743e8d375a861cdbfe9d0cf14428f6e1be5c52220cf7cf37aa25d26de98`) + `history/records/CLARANSClustering/2026-11-04T141532Z-antigravity-b03a64.yaml`: removed batch-discovery diary tail from `identity_notes`.
  - `data/curated/LargeMarginNearestNeighbor.yaml` (`sha256: 68b84c06c14399ef34f534fdd12f72045e567390c6f10c26b7c22b399f7e3f97`) + `history/records/LargeMarginNearestNeighbor/2026-11-04T141532Z-antigravity-9cb40e.yaml`: removed batch-discovery diary tail from `identity_notes`.
  - `data/curated/RelevantComponentAnalysis.yaml` (`sha256: 119aa77d1b1d0529f9e9ba5c7142a963ce540122cc7b16a748509f99f4fdfa59`) + `history/records/RelevantComponentAnalysis/2026-11-04T141532Z-antigravity-2da229.yaml`: removed batch-discovery diary tail from `identity_notes`.

### `F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006` (`deferred` — `G-C1S5-004`, [#454](https://github.com/CultureBotAI/AIMech/issues/454))
- **Issue Keys**: `aio-upstream-near-duplicate-class-boundaries` (`F-C1S4-004`), `aio-upstream-genus-hierarchy-mismatch` (`F-C1S4-005`), `aio-upstream-deep-feed-forward-synonym-typo` (`F-C1S4-006`)
- **Predecessor Occurrence**: `20261104T112500Z-c1s4-aio-corpus-category-review` (`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006`)
- **Successor Review Verification**: `20261104T145000Z-c1s5-curated-remediation-review` (superseding `20261104T142000Z-c1s5-curated-remediation-review`, `F-C1S4-004`..`F-C1S4-006`, `status: deferred`, assessments `ASM-C1S5-AIO-GENERATED-PROJECTION-SUPPORTED` and `ASM-C1S5-AIO-UPSTREAM-DEFERRED`)
- **Disposition**: Explicit deferral preserved (`carry_forward_ids: [F-C1S4-004, F-C1S4-005, F-C1S4-006]`). Per `AGENTS.md`, `data/aio/*.yaml` is generated from pinned `sources/aio/aio.json` (release `2026-07-22`) and must not rewrite upstream identifiers or alter generated records locally; tracked in [#454](https://github.com/CultureBotAI/AIMech/issues/454) for upstream `berkeleybop/artificial-intelligence-ontology` curation and future `aimech-refresh-aio` evaluation.
