# Causal Mechanism Graph Applicability Audit for AIMech (`mech-goal-sequence-20261019`, Cycle 1, Stage 2)

- **Audit ID:** `20261025T052500Z-causal-graph-applicability-audit`
- **Created At:** `2026-10-25T05:25:00Z`
- **Run / Cycle / Stage:** `mech-goal-sequence-20261019`, Cycle `1`, Stage `2` (`causal_graphs`)
- **Applicability Verdict:** `not_applicable`
- **Workflow Profile:** `workflow/mech-workflow.yaml` (SHA-256: `1f4575151090b50346fa5b8e75b9bfa0ef42b189350ba2d772516de6431671f8`)
- **Audit Script:** `research/validation/20261025T052500Z-causal-graph-applicability-audit.py` (SHA-256: `12b815009c3e567e9c5022b1999d57ae7e21853da8cca1443bb47589c0e09c25`)
- **Structured Audit Output:** `research/validation/20261025T052500Z-causal-graph-applicability-audit.json` (SHA-256: `ad8426af19ac80c8854681d2c2653b32ce5e6af74a0f426eb2363c8bd758f60c`)

## 1. Executive Summary

Stage 2 (`causal_graphs`) of the shared Mech workflow (`workflow/parent/mech-cycle.yaml`) is designed around biological knowledge bases (such as DisMech, CultureMech, MIM, CommunityMech, and TraitMech) where records curate biological pathways, upstream/downstream regulatory edges, and gene/protein instances (e.g., UniProt accessions).

In AIMech, `workflow/mech-workflow.yaml` explicitly overrides Stage 2 with `applicability: not_applicable`:

> Audit and document whether causal mechanism graphs apply to AIMech's native AI-concept domain and schema, using its local record-review skill and full corpus inventory. Preserve the ontology/causality distinction and report inapplicability with evidence; do not invent biological data or unsupported fields. If a real applicable representation is discovered, report it for review before replacing this applicability objective.

A deterministic audit of all three LinkML schema modules (`src/aimech/schema/aimech.yaml`, `src/aimech/schema/curated_concept.yaml`, and `src/aimech/schema/mech_shared.yaml`) and all **1,929 YAML records** in the AIMech corpus (**442** generated AIO projection records in `data/aio/*.yaml` and **1,487** maintained curated AI-concept records in `data/curated/*.yaml`) confirms:

1. **Zero causal-mechanism-graph classes, slots, or predicates exist** in AIMech's LinkML schemas (`aimech.yaml`, `curated_concept.yaml`, or `mech_shared.yaml`).
2. **Zero records (`0 / 1,929`)** across `data/aio/*.yaml` and `data/curated/*.yaml` carry causal-graph, pathway, regulatory, or gene/protein instance fields.
3. **AIMech's schema and documentation explicitly forbid conflating ontology axioms or vocabulary mappings with causal mechanism claims.**
4. **No biological data, UniProt protein examples, or unsupported causal-graph slots should be added to AIMech records.** Stage 2 (`causal_graphs`) remains `not_applicable` (`applicability: not_applicable`) in `workflow/mech-workflow.yaml`.

---

## 2. LinkML Schema Audit

The audit script (`research/validation/20261025T052500Z-causal-graph-applicability-audit.py`) inspected all classes, slots, and enums across all three LinkML schema files in `src/aimech/schema/` against candidate causal-graph/biological-mechanism slots (`causal_graph`, `causal_graphs`, `causal_edges`, `causal_mechanism`, `causal_mechanisms`, `mechanism_graph`, `pathways`, `biological_processes`, `upstream`, `downstream`, `regulates`, `positively_regulates`, `negatively_regulates`, `gene_examples`, `protein_examples`, `uniprot_id`).

| Schema Module | SHA-256 | Classes | Candidate Causal-Graph Slots Present | Domain Purpose & Explicit Boundary |
|---|---|---|---|---|
| `src/aimech/schema/aimech.yaml` | `5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852` | `AIConcept`, `ConceptRelationship`, `ConceptSynonym`, `CurationEvent`, `ImportProvenance` | `0` (`[]`) | Provenance-bearing projection of pinned Artificial Intelligence Ontology (AIO) classes. Schema description states: *"Ontology membership does not establish efficacy, benchmark performance, safety, or causal mechanism."* |
| `src/aimech/schema/curated_concept.yaml` | `3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f` | `CuratedAIConcept`, `ConceptClaim`, `EvaluationContext`, `EvidenceCitation`, `EvidenceSource`, `MappingSnapshot`, `AIOMapping`, `NoAIOMatch`, `AIOExaminedTarget`, `CurationProvenance` | `0` (`[]`) | Maintained AIMech-native AI concepts (`AIMech:*`) backed by primary literature (`EvidenceSource` + `EvidenceCitation`) and pinned AIO vocabulary alignment (`aio_mappings` or `aio_no_match`). |
| `src/aimech/schema/mech_shared.yaml` | `c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895` | `Discussion`, `ProposedExperiment`, `Dataset`, `CrossCorpusLink`, `SupportingReference` | `0` (`[]`) | Vendored cross-fleet shared LinkML module (imported by `aimech.yaml` for `AIConcept.discussions`). Although `Discussion.attaches_to` includes a cross-fleet docstring example (`e.g. causal_graphs#edge_x`), `mech_shared.yaml` defines no causal-graph class or slot. |

### Key Schema Slot Inventory

- **`AIConcept` (`src/aimech/schema/aimech.yaml`):**
  - Slots (`16`): `branches`, `comments`, `curation_history`, `definition`, `definition_sources`, `discussions`, `history_refs`, `id`, `name`, `ontology_iri`, `parents`, `provenance`, `relationships`, `review_status`, `subsets`, `synonyms`.
  - `ConceptRelationship`: `predicate` (`RelationshipPredicate`: only `BFO:0000051`) and `target`. The schema explicitly annotates `ConceptRelationship` as *"An exported named-class relationship, not an experimental causal claim."* and `BFO:0000051` as *"has part; exported ontology axiom, not evidence of causal effect."*
- **`CuratedAIConcept` (`src/aimech/schema/curated_concept.yaml`):**
  - Slots (`16`): `aio_mappings`, `aio_no_match`, `aio_snapshot`, `aliases`, `claims`, `concept_kind`, `curation`, `definition`, `definition_evidence`, `evidence_sources`, `history_refs`, `id`, `identity_notes`, `limitations`, `name`, `review_status`.
  - `ConceptKind` (`14` values): `algorithm`, `architecture`, `bias`, `computational_paradigm`, `coordination_mechanism`, `evaluation_criterion`, `evaluation_method`, `layer`, `learning_paradigm`, `mathematical_method`, `model_family`, `preprocessing_method`, `risk`, `task`.
  - `ClaimKind` (`5` values): `application`, `limitation`, `mechanism`, `performance`, `scope`.

---

## 3. Full Corpus Inventory (`1,929` Total Records)

### 3.1 Generated AIO Corpus (`data/aio/*.yaml` — `442` Records)

- **Total records inspected:** `442`
- **Records with causal-graph candidate slots:** `0`
- **Records with `discussions` populated:** `0`
- **Top-level key frequency across `442` records:**
  - `id`, `name`, `ontology_iri`, `definition`, `branches`, `parents`, `subsets`, `review_status`, `provenance`: `442 / 442` (`100%`)
  - `definition_sources`: `364 / 442`
  - `synonyms`: `233 / 442` (`446` total `ConceptSynonym` entries)
  - `comments`: `217 / 442`
  - `relationships`: `26 / 442` (`71` total `ConceptRelationship` edges, `100%` using predicate `BFO:0000051`)
- **AIO branch distribution (`442` total branch assignments):**
  - `Layer`: `168`
  - `Model`: `76`
  - `Bias`: `61`
  - `MachineLearningTask`: `57`
  - `Network`: `52`
  - `MathematicalFunction`: `14`
  - `Preprocessing`: `10`
  - `TrainingStrategy`: `4`

### 3.2 Maintained Curated AI-Concept Corpus (`data/curated/*.yaml` — `1,487` Records)

- **Total records inspected:** `1,487`
- **Records with causal-graph candidate slots:** `0`
- **Top-level key frequency across `1,487` records:**
  - `id`, `name`, `concept_kind`, `definition`, `definition_evidence`, `claims`, `identity_notes`, `evidence_sources`, `aio_snapshot`, `limitations`, `review_status`, `curation`: `1,487 / 1,487` (`100%`)
  - `aliases`: `1,418 / 1,487`
  - `aio_mappings`: `1,338 / 1,487` (`1,822` total `AIOMapping` entries: `1,415` `related_match`, `325` `broad_match`, `82` `narrow_match`)
  - `aio_no_match`: `149 / 1,487` (`1,338 + 149 = 1,487` mutually exclusive and collectively exhaustive AIO alignment coverage)
- **`ConceptKind` distribution across `1,487` curated records:**
  - `algorithm`: `1,047`
  - `mathematical_method`: `175`
  - `architecture`: `121`
  - `model_family`: `91`
  - `layer`: `20`
  - `learning_paradigm`: `13`
  - `preprocessing_method`: `7`
  - `evaluation_criterion`: `5`
  - `evaluation_method`: `5`
  - `bias`: `1`
  - `computational_paradigm`: `1`
  - `coordination_mechanism`: `1`
- **`ConceptClaim` distribution (`5,149` total claims across `1,487` curated records):**
  - `mechanism`: `2,793`
  - `limitation`: `1,029`
  - `scope`: `845`
  - `application`: `477`
  - `performance`: `5`
- **`EvidenceSource` distribution (`3,269` total source entries across `1,487` curated records):**
  - By `source_type`: `primary_paper` (`3,004`), `official_documentation` (`190`), `author_technical_report` (`66`), `primary_monograph` (`9`)
  - By `access_level`: `full_text` (`1,778`), `abstract_only` (`1,301`), `documentation` (`190`)

---

## 4. Preserving the Ontology-vs-Causality Distinction

A central requirement of AIMech's design (`CLAUDE.md`, `src/aimech/schema/aimech.yaml`, `docs/record-review-profile.md`) is keeping ontological classification, structural partonomy, conceptual vocabulary alignment, and algorithmic operating mechanisms distinct from empirical or biological causal mechanism graphs:

1. **Taxonomic Class Subsumption (`parents` in `data/aio/*.yaml`):**
   - All `442` generated AIO records carry `parents` edges (`442` total edges) representing OWL/RDFS class subsumption (`rdfs:subClassOf` / `owl:Thing`). Subclass relationships (e.g., `AIO:CausalLLM` $\sqsubseteq$ `AIO:LargeLanguageModel`) classify conceptual types and do not represent causal state transitions.
2. **Mereological Ontology Axioms (`relationships` with `BFO:0000051` in `data/aio/*.yaml`):**
   - Exactly `26` generated AIO records carry `71` `ConceptRelationship` entries, all using `predicate: BFO:0000051` (`has part`), such as `AIO:ResidualNeuralNetwork` having parts `AIO:AdditionLayer`, `AIO:BatchNormalizationLayer`, `AIO:InputLayer`, `AIO:ReLULayer`, and `AIO:WeightedLayer`.
   - As enforced by `src/aimech/schema/aimech.yaml`, `BFO:0000051` is an exported structural partonomy axiom from `aio.owl`, not a directed dataflow graph or evidence of causal effect.
3. **Cross-Vocabulary Conceptual Alignment (`aio_mappings` / `aio_no_match` in `data/curated/*.yaml`):**
   - The `1,822` `AIOMapping` entries across `1,338` curated records use `broad_match` (`325`), `narrow_match` (`82`), and `related_match` (`1,415`) to situate fine-grained AI methods relative to pinned AIO classes (`commit: 397851c547d1c4d8f06ef184f63c1d40bc86937a`). These are vocabulary-alignment predicates, not causal relationships.
4. **Algorithmic and Mathematical Mechanism Prose Claims (`claims` with `kind: mechanism` in `data/curated/*.yaml`):**
   - Curated records contain `2,793` `ConceptClaim` items with `kind: mechanism`. In AIMech's native domain (`src/aimech/schema/curated_concept.yaml`), a `mechanism` claim states how an algorithm, mathematical method, layer, or architecture computes its output (e.g., an objective function, update rule, estimator formula, or architectural transformation), supported by explicit page/equation/section locators in primary papers. These claims are formal mathematical/computational specifications rather than biological causal pathways.
5. **AI & Statistical Causal-Inference Subject Matter (`6` AIO records and `80` Curated records):**
   - Full-text regex scanning across all `1,929` records identified `6` generated AIO records (`AIO:BayesianNetwork`, `AIO:CausalGraphicalModel`, `AIO:CausalLLM`, `AIO:GenerativeCommonsenseLLM`, `AIO:ProbabilisticGraphicalModel`, `AIO:ProbabilisticTopicModel`) and `80` maintained curated records whose names, definitions, identity notes, or claim statements match causal or graphical terminology.
   - Across those `80` curated records, every occurrence falls into one of four methodological categories:
     1. **Statistical causal inference, instrumental-variable estimation, and counterfactual fairness criteria** (e.g., `AIMech:CounterfactualFairness`, `AIMech:BivariateCounterfactualFairnessSensitivity`, `AIMech:FairLearning`, `AIMech:MaxCFU`, `AIMech:AdaptiveLassoAndMedianOfRatiosConsistentInvalidInstrumentSelectionInLinearInstrumentalVariablesModels`, `AIMech:SomeInvalidSomeValidInstrumentalVariablesEstimatorAndMajorityRuleIdentifiability`, `AIMech:TSHTTwoStageHardThresholdingWithPluralityVotingForInvalidInstruments`);
     2. **Probabilistic graphical models and Bayesian-network inference/conflict diagnostics** (e.g., `AIMech:ContinuousTimeBayesianNetwork`, `AIMech:VariationalMessagePassing`, `AIMech:MixtureApproximationNodeSplittingDiagnostic`, `AIMech:SequentialScoreDiscrepancyConflictDiagnostic`, `AIMech:PachinkoAllocationModel`);
     3. **Causal (autoregressive / non-anticipative) operators and algorithmic DAGs** (e.g., `AIMech:RetNet`, `AIMech:HammersteinModel`, `AIMech:WienerModel`, `AIMech:BrandesBetweennessCentrality` shortest-path DAGs);
     4. **Explicit negative-scope disclaimers in limitation claims** (e.g., `AIMech:ZhouRandomWalkDissimilarity` and `AIMech:ZhouAttractorCommunityDetection`, which explicitly note that benchmark network examples do not establish causal biology).
   - In all cases, causal or graphical models are the *mathematical/algorithmic subject matter* of the AI concept being defined, not a record-level biological causal mechanism graph.

---

## 5. Assessment of Candidate Native Analogues & Governance Recommendation

Stage 2's goal prompt asks:
> *"If a real applicable representation is discovered, report it for review before replacing this applicability objective."*

### Evaluation of Candidate Representations

- **Biological causal mechanism graphs / UniProt protein examples:** **Inapplicable (`not_applicable`).** AIMech curates artificial intelligence, machine learning, and statistical methodologies rather than biological pathways, diseases, or microbial traits. Inventing biological entities or unsupported causal-graph slots would violate AIMech's schema and domain boundaries.
- **Computational operator-composition or mathematical dependency graphs:** While neural architectures and algorithms can in principle be analyzed in terms of formal computational dataflow or operator composition, AIMech's current schemas (`src/aimech/schema/aimech.yaml` and `src/aimech/schema/curated_concept.yaml`) intentionally represent:
  - generated AIO partonomy via `BFO:0000051` (`relationships`) and taxonomy via `parents`, and
  - curated mathematical/algorithmic mechanisms via literature-backed `ConceptClaim` (`kind: mechanism`) prose statements with exact primary-source locators.
- **Conclusion:** No applicable causal-mechanism-graph representation exists in AIMech's current schema or corpus. Any hypothetical future addition of structured computational/operator dependency graphs would represent *formal computational composition* rather than *empirical causal mechanism* and would require a separate, explicitly reviewed LinkML schema proposal before altering Stage 2's `not_applicable` configuration in `workflow/mech-workflow.yaml`.
