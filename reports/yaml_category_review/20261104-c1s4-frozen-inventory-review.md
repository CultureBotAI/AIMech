# YAML Category Review: AIMech Cycle 1 Stage 4 Frozen Inventory (1,929 Records)

- Repository: `CultureBotAI/AIMech`
- Category: `c1s4-frozen-inventory-review` (`data/aio/*.yaml` + `data/curated/*.yaml`)
- Selection Rule: All eligible scientific records (`442` generated `data/aio/*.yaml` + `1,487` maintained `data/curated/*.yaml` = `1,929` records) at frozen `source_revision: 7ad7d92709e8816ab33bc8979d7187dec109a1ab`
- Started UTC: `2026-11-04T11:20:00Z`
- Finished UTC: `2026-11-04T11:26:00Z`
- Verdict: `needs curation` (`pass_with_limitations` for generated `data/aio/*.yaml` via `20261104T112500Z-c1s4-aio-corpus-category-review`; `needs_curation` for the 38-record curated provenance/mapping subcohort via `20261104T112600Z-c1s4-curated-provenance-mapping-review`)

## Target Category

- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `1` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `7ad7d92709e8816ab33bc8979d7187dec109a1ab`
- **Total Eligible Scientific Records Reviewed**: `1929` (`442` generated `data/aio/*.yaml` + `1487` maintained `data/curated/*.yaml`)
- **Scientific Review Coverage**: `1929 / 1929` (`100.0%` full-category coverage across subcohorts)
- **Stage 4 Structured Review Bundles**:
  - `reviews/structured/20261104T112500Z-c1s4-aio-corpus-category-review/review.yaml` (`kind: category`, `verdict: pass_with_limitations`, `population_size: 442`)
  - `reviews/structured/20261104T112600Z-c1s4-curated-provenance-mapping-review/review.yaml` (`kind: category`, `verdict: needs_curation`, `population_size: 38`)
- **Parent Workflow Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`

## Selection and Membership

- **Included Member Paths (`1,929` records)**:
  - `data/aio/*.yaml` (`442` `AIConcept` files generated from `sources/aio/aio.json` release `2026-07-22`).
  - `data/curated/*.yaml` (`1,487` `CuratedAIConcept` files maintained in-repo). Every included record path, SHA-256 digest, corpus, `record_class`, branch/kind, primary structured review ID, boundary decision, and finding assignment is enumerated in `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_coverage.tsv` and `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json`.
- **Excluded Non-Record Paths**:
  - `reviews/**`, `reports/**`, `history/**`, `research/**`, `sources/**`, and `src/aimech/schema/**` are governance, provenance, upstream snapshot, or schema artifacts rather than scientific concept records.

### Generated AIO Subcohorts (`data/aio/*.yaml` — 442 records)

| AIO Top-Level Branch | Record Count | Retain | Defer (Upstream AIO) | Structured Review Bundle |
| --- | ---: | ---: | ---: | --- |
| `Bias` | 61 | 61 | 0 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `Layer` | 168 | 166 | 2 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `MachineLearningTask` | 57 | 57 | 0 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `MathematicalFunction` | 14 | 14 | 0 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `Model` | 76 | 73 | 3 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `Network` | 52 | 49 | 3 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `Preprocessing` | 10 | 10 | 0 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| `TrainingStrategy` | 4 | 3 | 1 | `20261104T112500Z-c1s4-aio-corpus-category-review` |
| **Total (`data/aio/*.yaml`)** | **442** | **433** | **9** | `20261104T112500Z-c1s4-aio-corpus-category-review` |

### Maintained Curated Subcohorts (`data/curated/*.yaml` — 1,487 records)

| Curated `ConceptKind` | Record Count | Retain | Open Findings (Stage 5) | Review Coverage |
| --- | ---: | ---: | ---: | --- |
| `algorithm` | 1047 | 1047 | 10 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `architecture` | 121 | 121 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `bias` | 1 | 1 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `computational_paradigm` | 1 | 1 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `coordination_mechanism` | 1 | 1 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `evaluation_criterion` | 5 | 5 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `evaluation_method` | 5 | 5 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `layer` | 20 | 20 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `learning_paradigm` | 13 | 13 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `mathematical_method` | 175 | 175 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `model_family` | 91 | 91 | 4 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| `preprocessing_method` | 7 | 7 | 0 | Prior cohort/record reviews + `20261104T112600Z-c1s4-curated-provenance-mapping-review` |
| **Total (`data/curated/*.yaml`)** | **1487** | **1487** | **14** | **100.0% (`1,487 / 1,487`)** |

## Validation

- `python research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`: Passed (`1,929` records audited: `442` AIO + `1,487` curated; `100.0%` scientific review coverage).
- `python scripts/record_review.py check --require-reviews --base main`: Passed (`224` structured review bundles validated).
- `just vendored-check`: Passed (`verify_vendored.py` verified immutable CLAW files).
- `just check`: Passed (`1,929` records validated: `442` AIO, `1,487` curated, `224` history events, `224` structured reviews; `315 passed, 3 skipped` in pytest).

## Lump and Split Review

- **`retain` (`1,920` records)**:
  - `433` generated `data/aio/*.yaml` classes have distinct ontology IRIs, labels, definitions, and parent subtrees in pinned AIO release `2026-07-22` (`sources/aio/aio.json`).
  - All `1,487` maintained `data/curated/*.yaml` records have distinct `AIMech:` identifiers, explicit AIO mapping assessments (`exact_match: 0`, `close_match: 1`, `broad_match: 917`, `narrow_match: 32`, `related_match: 641`), and primary-publication or versioned-documentation evidence.
- **`defer` (`9` generated `data/aio/*.yaml` records)**:
  - Deferred to upstream `berkeleybop/artificial-intelligence-ontology` (`src/ontology/aio-src.csv`) because `data/aio/*.yaml` is a generated projection (`python -m aimech seed --check`) and upstream identifiers/definitions must not be rewritten locally (`AGENTS.md`):
    - Near-duplicate upstream class pairs (`F-C1S4-004`): `AIO:AddLayer` / `AIO:AdditionLayer`, `AIO:TransformerLLM` / `AIO:TransformerLanguageModel`, and `AIO:ZeroShotLearningLLM` / `AIO:ZeroshotLearning`.
    - Upstream genus-to-hierarchy mismatches (`F-C1S4-005`): `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, and `AIO:TrainingStrategy`.
    - Upstream exact-synonym typo (`F-C1S4-006`): `AIO:DeepFeedForwardNetwork` (`"Multilayer Perceptoron"`).
- **`lump` (`0` local merges executed)**: No maintained `AIMech:` records duplicate an existing `AIMech:` or `AIO:` concept.
- **`split` (`0` record splits required)**: Existing records denote single coherent AI concepts; the frozen 1,929-record inventory was partitioned into reviewable branch and `ConceptKind` subcohorts for audit execution.

## Identity and Grounding

- **Generated AIO Corpus (`data/aio/*.yaml`, `442` records)**: All `442` records conform to `AIConcept`, carry `AIO:` CURIEs matching `sources/aio/aio.json` (`2026-07-22`), and preserve `status: generated`.
- **Maintained Curated Corpus (`data/curated/*.yaml`, `1,487` records)**: All `1,487` records conform to `CuratedAIConcept`, use unique `AIMech:<PascalCase>` identifiers, resolve all `related_concepts` and `aio_mappings.target_id` references against `data/aio/*.yaml` and `data/curated/*.yaml`, and carry explicit `aio_mapping_status` (`mapped_partial: 1,452`, `unmapped_missing_in_aio: 35`).
- **Identity Notes and Multi-Target Mapping Hygiene (`F-C1S4-003`)**: `AIMech:GloVe` is the only multi-mapped curated record (`3` `aio_mappings` targets: `AIO:RepresentationLearning`, `AIO:word2vecCBOW`, `AIO:word2vecSkipGram`) that repeats one undifferentiated `identity_notes` string verbatim across all `3` `aio_mappings[].rationale` entries; `AIMech:MarkovRandomField` retains candidate-proposal phrasing (`"this candidate specifically uses an undirected graph"`) in `identity_notes` and `aio_mappings[0].rationale`; and `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, and `AIMech:RelevantComponentAnalysis` retain batch-discovery process diary text in `identity_notes`.

## Evidence Patterns

- **Generated AIO Corpus (`data/aio/*.yaml`)**: Grounded strictly to `sources/aio/aio.json` (`version: 2026-07-22`) with zero fabricated scientific claims or model evaluation metadata.
- **Maintained Curated Corpus (`data/curated/*.yaml`)**: Grounded to primary publications and versioned implementation documentation with supporting snippets.
- **Missing `sha256` Digests on Inspected Artifacts (`F-C1S4-001`, `F-C1S4-002`)**:
  - `3` curated records from the 2026-10-11 first native cohort (`AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess`) declare `access_level: full_text` on PDF primary sources without `evidence_sources[0].sha256` or `pdf_reading` entries in `research/discovery/20261011T030803Z-first-native-cohort.json`, embed single-page `#page=` viewer fragment anchors in `evidence_sources[0].url`, and omit `persistent_id` (`doi:10.1016/S0004-3702(98)00023-X`) on `MarkovDecisionProcess.yaml` and `PartiallyObservableMarkovDecisionProcess.yaml` (`F-C1S4-001`).
  - `6` curated records (`AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg`; `7` documentation entries total) declare `access_level: documentation` without `sha256` content digests (`F-C1S4-002`).

## Completeness Patterns

- **Generated AIO Corpus (`data/aio/*.yaml`)**: Complete with respect to the pinned `sources/aio/aio.json` snapshot (`442 / 442` classes).
- **Maintained Curated Corpus (`data/curated/*.yaml`)**: All `1,487` curated records populate `id`, `name`, `record_class`, `status`, `concept_kind`, `definition`, `mechanism_summary`, `aio_mapping_status`, `evidence_sources`, `claims`, and `last_reviewed_utc`. The `4` curated records using `access_level: full_text` with explicit version qualification (`AIMech:AdaBoost`, `AIMech:Bagging`, `AIMech:HierarchicalAgglomerativeClustering`, `AIMech:VariationalInference`) explicitly document in `evidence_sources[1].version` that no local PDF checksum was retained and are not defective.

## Findings

| Finding ID | Status | Severity | Category | Structured Review | Target Records | Summary |
| --- | --- | --- | --- | --- | --- | --- |
| `F-C1S4-001` | `open` | `minor` | `provenance` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess` | Three maintained records from the 2026-10-11T03:01:34Z first native cohort (AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess) cite PDF primary sources with access_level=full_text (Bilmes 1998 TR-97-021 and Kaelbling, Littman & Cassandra 1998 Artificial Intelligence 101:99-134) while omitting evidence_sources[0].sha256 and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json, embedding single-page #page= viewer fragment anchors in evidence_sources[0].url (even where the locator spans multiple pages), and omitting persistent_id (doi:10.1016/S0004-3702(98)00023-X) on MarkovDecisionProcess.yaml and PartiallyObservableMarkovDecisionProcess.yaml. |
| `F-C1S4-002` | `open` | `minor` | `provenance` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg` | Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm, AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation source entries total) are the only curated records whose access_level=documentation evidence_sources omit sha256 content digests (borgelt.net/apriori.html, borgelt.net/eclat.html, deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, hmmlearn.readthedocs.io/en/0.3.3/tutorial.html, and the secondary PyTorch 2.14 documentation entries in BarlowTwins.yaml and VICReg.yaml). |
| `F-C1S4-003` | `open` | `minor` | `grounding` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:GloVe`, `AIMech:MarkovRandomField`, `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, `AIMech:RelevantComponentAnalysis` | AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record in data/curated/*.yaml that repeats one undifferentiated identity_notes sentence verbatim across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning, AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField (data/curated/MarkovRandomField.yaml) retains candidate-proposal phrasing ('this candidate specifically uses an undirected graph') in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain batch-discovery diary text ('No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record... with 79 worktree and 79 main-checkout matching lines...') inside identity_notes. |
| `F-C1S4-004` | `deferred` | `minor` | `scope` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:AddLayer`, `AIO:AdditionLayer`, `AIO:TransformerLLM`, `AIO:TransformerLanguageModel`, `AIO:ZeroShotLearningLLM`, `AIO:ZeroshotLearning` | Pinned upstream AIO release 2026-07-22 (sources/aio/aio.json) contains three pairs of distinct class IRIs with overlapping definitions, parent chains, or cross-linked synonyms: (1) AIO:AddLayer (branches: [Layer], parents: [AIO:MergingLayer], definition: 'A merging layer that adds a list of inputs taking as input a list of tensors all of the same shape.') and AIO:AdditionLayer (branches: [Layer], parents: [AIO:Layer], definition: 'A layer that adds inputs from one or more other layers to cells or neurons of a target layer.'); (2) AIO:TransformerLLM (branches: [Model], parents: [AIO:TransformerLanguageModel], exact synonym 'Transformer Large Language Model') and AIO:TransformerLanguageModel (branches: [Model], parents: [AIO:LanguageModel], exact synonym 'Transformer LM'), whose definitions share the identical relative clause 'that uses the transformer architecture based on multi-head attention mechanisms allowing it to contextualize tokens within a context window for effective language understanding and generation'; and (3) AIO:ZeroShotLearningLLM (branches: [Model], parents: [AIO:LargeLanguageModel], exact synonym 'Zero-Shot LLM', related synonym 'zero-shot learning') and AIO:ZeroshotLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], exact synonym 'ZSL'). Because data/aio/*.yaml is generated and upstream identifiers must not be locally rewritten or merged without upstream curation, these boundary overlaps are deferred to berkeleybop/artificial-intelligence-ontology. |
| `F-C1S4-005` | `deferred` | `minor` | `consistency` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, `AIO:TrainingStrategy` | In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), AIO:RepresentationLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], definition: 'A deep neural network that discovers representations required for feature detection or classification from raw data.') and AIO:ZeroshotLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], definition: 'A deep neural network that predicts classes at test time from classes not observed during training.') are placed under AIO:DeepNeuralNetwork with definitions beginning 'A deep neural network that...' despite denoting learning paradigms/tasks, and top-level branch AIO:TrainingStrategy (branches: [TrainingStrategy], parents: [owl:Thing]) defines itself with the genus 'A preprocessing used to train machine learning models...' while AIO:Preprocessing is a sibling top-level branch. Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated from the pinned ontology snapshot. |
| `F-C1S4-006` | `deferred` | `minor` | `nomenclature` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:DeepFeedForwardNetwork` | In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), class AIO:DeepFeedForwardNetwork (data/aio/DeepFeedForwardNetwork.yaml) carries the misspelled exact synonym 'Multilayer Perceptoron' (synonyms[2].value) alongside exact synonyms 'DFF' (synonyms[0].value) and 'MLP' (synonyms[1].value). Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated and must reproduce sources/aio/aio.json byte-for-byte under python -m aimech seed --check. |

## Recommended Edits

1. **`F-C1S4-001` (`status: open`, `severity: minor`, `3` curated records: `AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess`)**: In Stage 5 (`resolve_review_findings`), record verified 64-hex `sha256` PDF digests, canonical URLs without single-page `#page=` viewer fragments, and `persistent_id` (`doi:10.1016/S0004-3702(98)00023-X`) on `data/curated/{ExpectationMaximization,MarkovDecisionProcess,PartiallyObservableMarkovDecisionProcess}.yaml`, recording append-only curation history via `just new-history`.
2. **`F-C1S4-002` (`status: open`, `severity: minor`, `6` curated records: `AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg`)**: In Stage 5 (`resolve_review_findings`), record verified 64-hex `sha256` content digests or explicit version qualifications on the `7` `access_level: documentation` entries across those `6` records (`evidence_sources[0].sha256` on `Apriori`, `Eclat`, `GeneticAlgorithm`, `HiddenMarkovModel`; `evidence_sources[2].sha256` on `BarlowTwins`; `evidence_sources[2].sha256` and `evidence_sources[3].sha256` on `VICReg`), recording append-only curation history via `just new-history`.
3. **`F-C1S4-003` (`status: open`, `severity: minor`, `5` curated records: `AIMech:GloVe`, `AIMech:MarkovRandomField`, `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, `AIMech:RelevantComponentAnalysis`)**: In Stage 5 (`resolve_review_findings`), differentiate target-specific `aio_mappings[0..2].rationale` strings on `data/curated/GloVe.yaml` and replace candidate-proposal / batch-discovery diary text in `identity_notes` (and `aio_mappings[0].rationale` on `MarkovRandomField.yaml`), recording append-only curation history via `just new-history`.
4. **`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006` (`status: deferred`, `9` generated records in `data/aio/*.yaml`)**: Do not hand-edit `data/aio/*.yaml`; preserve these findings as upstream ontology proposals/deferrals owned by `sources/aio/aio.json` (`berkeleybop/artificial-intelligence-ontology` `src/ontology/aio-src.csv`), `sources/aio/source.yaml`, and `src/aimech/importer.py`.

## Follow-up Checks

- `python research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`
- `python scripts/record_review.py check --require-reviews --base main`
- `just vendored-check`
- `just check`

## Additional Notes

- **Stage 4 Non-Mutation Gate**: Zero scientific records (`data/aio/*.yaml` or `data/curated/*.yaml`) were modified during Stage 4 (`record_review`); all actionable curated fixes (`F-C1S4-001`, `F-C1S4-002`, `F-C1S4-003`) and upstream AIO deferrals (`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006`) are preserved in `carry_forward_ids` for Stage 5 (`resolve_review_findings`).
- **Reproducible Audit Script**: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`.
- **Reproducible Audit JSON**: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json`.
