# Cycle 1 Stage 4 (`record_review`) Findings Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `1` / Stage `4` / Revision `1`
- **Frozen Source Revision**: `7ad7d92709e8816ab33bc8979d7187dec109a1ab`
- **Carry-Forward Finding IDs (`6`)**: `F-C1S4-001, F-C1S4-002, F-C1S4-003, F-C1S4-004, F-C1S4-005, F-C1S4-006`

## `F-C1S4-001` — Record PDF content digests, canonical URLs, and DOI metadata for the three full-text PDF concepts in the first native cohort

- **Issue Key**: `aimech-first-native-cohort-pdf-provenance`
- **Status**: `open`
- **Severity**: `minor`
- **Category**: `provenance`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112600Z-c1s4-curated-provenance-mapping-review/review.yaml`
- **Target Records (`3`)**: `AIMech:ExpectationMaximization`, `AIMech:MarkovDecisionProcess`, `AIMech:PartiallyObservableMarkovDecisionProcess`
- **Owner Paths**: `data/curated/ExpectationMaximization.yaml`, `data/curated/MarkovDecisionProcess.yaml`, `data/curated/PartiallyObservableMarkovDecisionProcess.yaml`
- **Summary**: Three maintained records from the 2026-10-11T03:01:34Z first native cohort (AIMech:ExpectationMaximization, AIMech:MarkovDecisionProcess, AIMech:PartiallyObservableMarkovDecisionProcess) cite PDF primary sources with access_level=full_text (Bilmes 1998 TR-97-021 and Kaelbling, Littman & Cassandra 1998 Artificial Intelligence 101:99-134) while omitting evidence_sources[0].sha256 and pdf_reading entries in research/discovery/20261011T030803Z-first-native-cohort.json, embedding single-page #page= viewer fragment anchors in evidence_sources[0].url (even where the locator spans multiple pages), and omitting persistent_id (doi:10.1016/S0004-3702(98)00023-X) on MarkovDecisionProcess.yaml and PartiallyObservableMarkovDecisionProcess.yaml.

## `F-C1S4-002` — Populate or explicitly qualify missing sha256 content digests on seven curated documentation evidence sources across six maintained records

- **Issue Key**: `aimech-curated-documentation-missing-sha256`
- **Status**: `open`
- **Severity**: `minor`
- **Category**: `provenance`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112600Z-c1s4-curated-provenance-mapping-review/review.yaml`
- **Target Records (`6`)**: `AIMech:Apriori`, `AIMech:Eclat`, `AIMech:GeneticAlgorithm`, `AIMech:HiddenMarkovModel`, `AIMech:BarlowTwins`, `AIMech:VICReg`
- **Owner Paths**: `data/curated/Apriori.yaml`, `data/curated/Eclat.yaml`, `data/curated/GeneticAlgorithm.yaml`, `data/curated/HiddenMarkovModel.yaml`, `data/curated/BarlowTwins.yaml`, `data/curated/VICReg.yaml`
- **Summary**: Six maintained curated records (AIMech:Apriori, AIMech:Eclat, AIMech:GeneticAlgorithm, AIMech:HiddenMarkovModel, AIMech:BarlowTwins, AIMech:VICReg; seven documentation source entries total) are the only curated records whose access_level=documentation evidence_sources omit sha256 content digests (borgelt.net/apriori.html, borgelt.net/eclat.html, deap.readthedocs.io/en/stable/api/algo.html#deap.algorithms.eaSimple, hmmlearn.readthedocs.io/en/0.3.3/tutorial.html, and the secondary PyTorch 2.14 documentation entries in BarlowTwins.yaml and VICReg.yaml).

## `F-C1S4-003` — Differentiate target-specific AIO mapping rationales in GloVe.yaml and remove candidate-proposal / batch-discovery diary text from MarkovRandomField, CLARANSClustering, LargeMarginNearestNeighbor, and RelevantComponentAnalysis

- **Issue Key**: `aimech-curated-identity-mapping-proposal-diary-carryover`
- **Status**: `open`
- **Severity**: `minor`
- **Category**: `grounding`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112600Z-c1s4-curated-provenance-mapping-review/review.yaml`
- **Target Records (`5`)**: `AIMech:GloVe`, `AIMech:MarkovRandomField`, `AIMech:CLARANSClustering`, `AIMech:LargeMarginNearestNeighbor`, `AIMech:RelevantComponentAnalysis`
- **Owner Paths**: `data/curated/GloVe.yaml`, `data/curated/MarkovRandomField.yaml`, `data/curated/CLARANSClustering.yaml`, `data/curated/LargeMarginNearestNeighbor.yaml`, `data/curated/RelevantComponentAnalysis.yaml`
- **Summary**: AIMech:GloVe (data/curated/GloVe.yaml) is the only multi-mapping record in data/curated/*.yaml that repeats one undifferentiated identity_notes sentence verbatim across all three distinct aio_mappings[].rationale targets (AIO:RepresentationLearning, AIO:word2vecCBOW, AIO:word2vecSkipGram); AIMech:MarkovRandomField (data/curated/MarkovRandomField.yaml) retains candidate-proposal phrasing ('this candidate specifically uses an undirected graph') in identity_notes and aio_mappings[0].rationale; and AIMech:CLARANSClustering, AIMech:LargeMarginNearestNeighbor, and AIMech:RelevantComponentAnalysis retain batch-discovery diary text ('No normalized identity match for this candidate was found across all 442 pinned AIO labels/scoped synonyms and 227 preceding native IDs/names/aliases. The same search identified BIRCH as an existing native record... with 79 worktree and 79 main-checkout matching lines...') inside identity_notes.

## `F-C1S4-004` — Defer three upstream AIO near-duplicate class pairs (AddLayer/AdditionLayer, TransformerLLM/TransformerLanguageModel, ZeroShotLearningLLM/ZeroshotLearning) to upstream ontology curation

- **Issue Key**: `aio-upstream-near-duplicate-class-boundaries`
- **Status**: `deferred`
- **Severity**: `minor`
- **Category**: `scope`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112500Z-c1s4-aio-corpus-category-review/review.yaml`
- **Target Records (`6`)**: `AIO:AddLayer`, `AIO:AdditionLayer`, `AIO:TransformerLLM`, `AIO:TransformerLanguageModel`, `AIO:ZeroShotLearningLLM`, `AIO:ZeroshotLearning`
- **Owner Paths**: `sources/aio/aio.json`, `sources/aio/source.yaml`, `src/aimech/importer.py`
- **Summary**: Pinned upstream AIO release 2026-07-22 (sources/aio/aio.json) contains three pairs of distinct class IRIs with overlapping definitions, parent chains, or cross-linked synonyms: (1) AIO:AddLayer (branches: [Layer], parents: [AIO:MergingLayer], definition: 'A merging layer that adds a list of inputs taking as input a list of tensors all of the same shape.') and AIO:AdditionLayer (branches: [Layer], parents: [AIO:Layer], definition: 'A layer that adds inputs from one or more other layers to cells or neurons of a target layer.'); (2) AIO:TransformerLLM (branches: [Model], parents: [AIO:TransformerLanguageModel], exact synonym 'Transformer Large Language Model') and AIO:TransformerLanguageModel (branches: [Model], parents: [AIO:LanguageModel], exact synonym 'Transformer LM'), whose definitions share the identical relative clause 'that uses the transformer architecture based on multi-head attention mechanisms allowing it to contextualize tokens within a context window for effective language understanding and generation'; and (3) AIO:ZeroShotLearningLLM (branches: [Model], parents: [AIO:LargeLanguageModel], exact synonym 'Zero-Shot LLM', related synonym 'zero-shot learning') and AIO:ZeroshotLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], exact synonym 'ZSL'). Because data/aio/*.yaml is generated and upstream identifiers must not be locally rewritten or merged without upstream curation, these boundary overlaps are deferred to berkeleybop/artificial-intelligence-ontology.
- **Disposition**: Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); generated data/aio/*.yaml files must remain exact projections of the pinned AIO release (AGENTS.md).

## `F-C1S4-005` — Defer upstream AIO genus-to-hierarchy mismatches on RepresentationLearning, ZeroshotLearning, and TrainingStrategy to upstream ontology curation

- **Issue Key**: `aio-upstream-genus-hierarchy-mismatch`
- **Status**: `deferred`
- **Severity**: `minor`
- **Category**: `consistency`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112500Z-c1s4-aio-corpus-category-review/review.yaml`
- **Target Records (`3`)**: `AIO:RepresentationLearning`, `AIO:ZeroshotLearning`, `AIO:TrainingStrategy`
- **Owner Paths**: `sources/aio/aio.json`, `sources/aio/source.yaml`, `src/aimech/importer.py`
- **Summary**: In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), AIO:RepresentationLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], definition: 'A deep neural network that discovers representations required for feature detection or classification from raw data.') and AIO:ZeroshotLearning (branches: [Network], parents: [AIO:DeepNeuralNetwork], definition: 'A deep neural network that predicts classes at test time from classes not observed during training.') are placed under AIO:DeepNeuralNetwork with definitions beginning 'A deep neural network that...' despite denoting learning paradigms/tasks, and top-level branch AIO:TrainingStrategy (branches: [TrainingStrategy], parents: [owl:Thing]) defines itself with the genus 'A preprocessing used to train machine learning models...' while AIO:Preprocessing is a sibling top-level branch. Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated from the pinned ontology snapshot.
- **Disposition**: Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); maintained curated records already document these upstream placement caveats in aio_mappings[].rationale and identity_notes without mutating generated data/aio/*.yaml.

## `F-C1S4-006` — Defer upstream AIO exact-synonym typo ('Multilayer Perceptoron') on AIO:DeepFeedForwardNetwork to upstream ontology curation

- **Issue Key**: `aio-upstream-deep-feed-forward-synonym-typo`
- **Status**: `deferred`
- **Severity**: `minor`
- **Category**: `nomenclature`
- **Certainty**: `confirmed`
- **Native Structured Review Bundle**: `reviews/structured/20261104T112500Z-c1s4-aio-corpus-category-review/review.yaml`
- **Target Records (`1`)**: `AIO:DeepFeedForwardNetwork`
- **Owner Paths**: `sources/aio/aio.json`, `sources/aio/source.yaml`, `src/aimech/importer.py`
- **Summary**: In pinned upstream AIO release 2026-07-22 (sources/aio/aio.json), class AIO:DeepFeedForwardNetwork (data/aio/DeepFeedForwardNetwork.yaml) carries the misspelled exact synonym 'Multilayer Perceptoron' (synonyms[2].value) alongside exact synonyms 'DFF' (synonyms[0].value) and 'MLP' (synonyms[1].value). Deferred to upstream berkeleybop/artificial-intelligence-ontology because data/aio/*.yaml is generated and must reproduce sources/aio/aio.json byte-for-byte under python -m aimech seed --check.
- **Disposition**: Deferred to upstream berkeleybop/artificial-intelligence-ontology (src/ontology/aio-src.csv); generated data/aio/DeepFeedForwardNetwork.yaml must remain faithful to the pinned upstream snapshot.
