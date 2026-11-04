# AIMech Cycle 1 Stage 4 Frozen-Inventory Record and Category Review

- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `1` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `7ad7d92709e8816ab33bc8979d7187dec109a1ab`
- **Total Eligible Scientific Records Reviewed**: `1929` (`442` generated `data/aio/*.yaml` + `1487` maintained `data/curated/*.yaml`)
- **Scientific Review Coverage**: `1929 / 1929` (`100.0%`)
- **Stage 4 Structured Review Bundles**:
  - `reviews/structured/20261104T112500Z-c1s4-aio-corpus-category-review/review.yaml` (`kind: category`, `verdict: pass_with_limitations`, `population_size: 442`)
  - `reviews/structured/20261104T112600Z-c1s4-curated-provenance-mapping-review/review.yaml` (`kind: category`, `verdict: needs_curation`, `population_size: 38`)
- **Parent Workflow Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`

## 1. Frozen Inventory & Cohort Partition

### 1.1 Generated AIO Corpus (`data/aio/*.yaml` — 442 records)

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

### 1.2 Maintained Curated Corpus (`data/curated/*.yaml` — 1,487 records)

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

## 2. Boundary Decisions (`lump` / `split` / `retain` / `defer`)

- **`retain` (`1,920` records)**:
  - `433` generated `data/aio/*.yaml` classes have distinct ontology IRIs, labels, definitions, and parent subtrees in pinned AIO release `2026-07-22` (`sources/aio/aio.json`).
  - All `1,487` maintained `data/curated/*.yaml` records have distinct `AIMech:` identifiers, explicit AIO mapping assessments (`exact_match: 0`, `close_match: 1`, `broad_match: 917`, `narrow_match: 32`, `related_match: 641`), and primary-publication or versioned-documentation evidence.
- **`defer` (`9` generated `data/aio/*.yaml` records)**:
  - Deferred to upstream `berkeleybop/artificial-intelligence-ontology` (`src/ontology/aio-src.csv`) because `data/aio/*.yaml` is a generated projection (`python -m aimech seed --check`) and upstream identifiers/definitions must not be rewritten locally (`AGENTS.md`):
    - Near-duplicate upstream class pairs (`F-C1S4-004`): `AIO:AddLayer` / `AIO:AdditionLayer`, `AIO:TransformerLLM` / `AIO:TransformerLanguageModel`, and `AIO:ZeroShotLearningLLM` / `AIO:ZeroshotLearning`.
    - Upstream genus-to-hierarchy mismatches (`F-C1S4-005`): `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, and `AIO:TrainingStrategy`.
    - Upstream exact-synonym typo (`F-C1S4-006`): `AIO:DeepFeedForwardNetwork` (`"Multilayer Perceptoron"`).
- **`lump` (`0` local merges executed)**: No maintained `AIMech:` records duplicate an existing `AIMech:` or `AIO:` concept.
- **`split` (`0` record splits required)**: Existing records denote single coherent AI concepts; the frozen 1,929-record inventory was partitioned into reviewable branch and `ConceptKind` cohorts for audit execution.

## 3. Stage 4 Findings Carried Forward to Stage 5 (`resolve_review_findings`)

| Finding ID | Status | Severity | Category | Structured Review | Target Records | Summary |
| --- | --- | --- | --- | --- | --- | --- |
| `F-C1S4-001` | `open` | `minor` | `provenance` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess` | Three maintained records from the 2026-10-11T03:01:34Z first native cohort (AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess) cite PDF primary sources with access_level=full_text (Bilmes 1998 TR-97-021 and Kaelbling, Littman & Cassandra 1998 Artificial Intelligence 101:99-134) while omitting evidence_sources[0].sha256 and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json, embedding single-page #page= viewer fragment anchors in evidence_sources[0].url (even where the locator spans multiple pages), and omitting persistent_id (doi:10.1016/S0004-3702(98)00023-X) on MarkovDecisionProcess.yaml and PartiallyObservableMarkovDecisionProcess.yaml. |
| `F-C1S4-002` | `open` | `minor` | `provenance` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg` | Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm, AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation source entries total) are the only curated records whose access_level=documentation evidence_sources omit sha256 content digests (borgelt.net/apriori.html, borgelt.net/eclat.html, deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, hmmlearn.readthedocs.io/en/0.3.3/tutorial.html, and the secondary PyTorch 2.14 documentation entries in BarlowTwins.yaml and VICReg.yaml). |
| `F-C1S4-003` | `open` | `minor` | `grounding` | `20261104T112600Z-c1s4-curated-provenance-mapping-review` | `AIMech:GloVe`, `AIMech:MarkovRandomField`, `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, `AIMech:RelevantComponentAnalysis` | AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record in data/curated/*.yaml that repeats one undifferentiated identity_notes sentence verbatim across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning, AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField (data/curated/MarkovRandomField.yaml) retains candidate-proposal phrasing ('this candidate specifically uses an undirected graph') in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain batch-discovery diary text ('No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record... with 79 worktree and 79 main-checkout matching lines...') inside identity_notes. |
| `F-C1S4-004` | `deferred` | `minor` | `scope` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:AddLayer`, `AIO:AdditionLayer`, `AIO:TransformerLLM`, `AIO:TransformerLanguageModel`, `AIO:ZeroShotLearningLLM`, `AIO:ZeroshotLearning` | Pinned upstream AIO release 2026-07-22 (sources/aio/aio.json) contains three pairs of distinct class IRIs with overlapping definitions and cross-linked or duplicate synonyms: (1) AIO:AddLayer and AIO:AdditionLayer (both under AIO:TensorOperationLayer with element-wise tensor addition definitions), (2) AIO:TransformerLLM and AIO:TransformerLanguageModel (both under AIO:LargeLanguageModel with identical exact synonym 'Transformer-based LLM'), and (3) AIO:ZeroShotLearningLLM (Model -> LargeLanguageModel) and AIO:ZeroshotLearning (Network -> DeepNeuralNetwork, with exact synonym 'Zero-Shot Learning LLM'). Because data/aio/*.yaml is generated and upstream identifiers must not be locally rewritten or merged without upstream curation, these boundary overlaps are deferred to berkeleybop/artificial-intelligence-ontology. |
| `F-C1S4-005` | `deferred` | `minor` | `consistency` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, `AIO:TrainingStrategy` | In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), AIO:RepresentationLearning and AIO:ZeroshotLearning are placed under AIO:DeepNeuralNetwork (Network branch) with definitions beginning 'A deep neural network that...' despite denoting learning paradigms/tasks, and top-level branch AIO:TrainingStrategy (parents: [owl:Thing]) defines itself with the genus 'A preprocessing used to train machine learning models...' while AIO:Preprocessing is a sibling top-level branch. Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated from the pinned ontology snapshot. |
| `F-C1S4-006` | `deferred` | `minor` | `nomenclature` | `20261104T112500Z-c1s4-aio-corpus-category-review` | `AIO:DeepFeedForwardNetwork` | In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), class AIO:DeepFeedForwardNetwork (data/aio/DeepFeedForwardNetwork.yaml) carries the misspelled exact synonym 'Multilayer Perceptoron' (synonyms[2].value) alongside 'Multi-Layer Perceptron' and 'MLP'. Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated and must reproduce sources/aio/aio.json byte-for-byte under python -m aimech seed --check. |

## 4. Verification & Non-Mutation Gate

- Zero scientific records (`data/aio/*.yaml` or `data/curated/*.yaml`) were modified during Stage 4 (`record_review`); all actionable curated fixes (`F-C1S4-001`, `F-C1S4-002`, `F-C1S4-003`) and upstream AIO deferrals (`F-C1S4-004`, `F-C1S4-005`, `F-C1S4-006`) are preserved in `carry_forward_ids` for Stage 5 (`resolve_review_findings`).
- Reproducible audit script: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.py`.
- Reproducible audit JSON: `research/validation/20261104T112000Z-c1s4-frozen-inventory-audit.json`.
