# UniProt Protein-Example Applicability Audit for AIMech (`mech-goal-sequence-20261019`, Cycle 1, Stage 3)

- **Audit ID:** `20261104T091000Z-protein-examples-applicability-audit`
- **Created At:** `2026-11-04T09:10:00Z`
- **Run / Cycle / Stage:** `mech-goal-sequence-20261019`, Cycle `1`, Stage `3` (`protein_examples`)
- **Applicability Verdict:** `not_applicable`
- **Workflow Profile:** `workflow/mech-workflow.yaml` (SHA-256: `1f4575151090b50346fa5b8e75b9bfa0ef42b189350ba2d772516de6431671f8`)
- **Audit Script:** `research/validation/20261104T091000Z-protein-examples-applicability-audit.py` (SHA-256: `217b5344c0aaff7d4d871e072c4cf8dd0f8117f09d940c25d4b36bf0e0ec93ec`)
- **Structured Audit Output:** `research/validation/20261104T091000Z-protein-examples-applicability-audit.json` (SHA-256: `4501738cdc176915b301d6b8e1e8f5560b0e68a2c7e85b5315b49500ea5c61b0`)

## 1. Executive Summary

Stage 3 (`protein_examples`) of the shared Mech workflow (`workflow/parent/mech-cycle.yaml`) is designed around biological knowledge bases (such as DisMech, CultureMech, MIM, CommunityMech, and TraitMech) where records curate biological UniProt protein examples (`UniProtKB:...` accessions, gene symbols, enzymatic activities, or molecular targets).

In AIMech, `workflow/mech-workflow.yaml` explicitly overrides Stage 3 with `applicability: not_applicable`:

> Audit and document whether biological UniProt protein examples apply to AIMech's native AI-concept domain and schema, using its local record-review skill and full corpus inventory. Preserve the ontology/causality distinction and report inapplicability with evidence; do not invent biological data or unsupported fields. If a real applicable representation is discovered, report it for review before replacing this applicability objective.

A deterministic audit of all three LinkML schema modules (`src/aimech/schema/aimech.yaml`, `src/aimech/schema/curated_concept.yaml`, and `src/aimech/schema/mech_shared.yaml`) and all **1,929 YAML records** in the AIMech corpus (**442** generated AIO projection records in `data/aio/*.yaml` and **1,487** maintained curated AI-concept records in `data/curated/*.yaml`) confirms:

1. **Zero biological entity prefixes (`UniProt`, `UniProtKB`, `HGNC`, `NCBIGene`, `GO`, `PR`, `PDB`) and zero protein-example or gene-example slots exist** in AIMech's LinkML schemas (`aimech.yaml`, `curated_concept.yaml`, or `mech_shared.yaml`).
2. **Zero records (`0 / 1,929`)** across `data/aio/*.yaml` and `data/curated/*.yaml` carry protein-example fields or UniProt CURIEs/accessions (`UniProt:...`, `UniProtKB:...`, `Swiss-Prot`, `TrEMBL`).
3. **Across all `442` generated AIO records (`data/aio/*.yaml`), `0` records mention proteins or UniProt**, and only `3` records (`AIO:ArtificialNeuralNetwork`, `AIO:SpikingHiddenLayer`, `AIO:SurvivalAnalysis`) mention the word `biological` to contrast artificial neural units with biological neurons or note time-to-event subjects.
4. **Across all `1,487` maintained curated AI-concept records (`data/curated/*.yaml`), only `3` records (`AIMech:BrandesPichPivotCentralityEstimation`, `AIMech:ZhouAttractorCommunityDetection`, `AIMech:ZhouRandomWalkDissimilarity`) mention the word `protein`**, and in all `3` records the token appears exclusively inside `kind: limitation` claims noting that historical benchmark evaluations on yeast protein-interaction networks do **not** establish biological-function prediction, protein transport/essentiality mechanisms, or causal biology.
5. **No biological UniProt protein examples or unsupported protein-instance fields should be added to AIMech records.** Stage 3 (`protein_examples`) remains `not_applicable` (`applicability: not_applicable`) in `workflow/mech-workflow.yaml`.

---

## 2. LinkML Schema Audit

The audit script (`research/validation/20261104T091000Z-protein-examples-applicability-audit.py`) inspected all prefixes, classes, slots, and enums across all three LinkML schema files in `src/aimech/schema/` against candidate biological prefixes (`UniProt`, `UniProtKB`, `uniprot`, `HGNC`, `NCBIGene`, `PR`, `GO`, `PDB`, `ENSEMBL`, `REFSEQ`) and candidate protein/gene/causal-graph slots (`protein_examples`, `protein_example`, `proteins`, `uniprot`, `uniprot_id`, `uniprot_ids`, `uniprot_accession`, `uniprot_kb`, `gene_examples`, `gene_symbol`, `gene_id`, `ncbi_gene_id`, `hgnc_id`, `protein_targets`, `enzymes`, `substrates`, `products`, `sequence`, `amino_acid_sequence`, `pdb_id`, `causal_graph`, `causal_graphs`, `pathways`, `biological_processes`).

| Schema Module | SHA-256 | Declared Prefixes | Candidate Biological Prefixes | Candidate Protein-Example Slots Present | Domain Purpose & Explicit Boundary |
|---|---|---|---|---|---|
| `src/aimech/schema/aimech.yaml` | `5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852` | `AIO`, `aimech`, `linkml` | `0` (`[]`) | `0` (`[]`) | Provenance-bearing projection of pinned Artificial Intelligence Ontology (AIO) classes (`AIConcept`). Schema description states: *"Ontology membership does not establish efficacy, benchmark performance, safety, or causal mechanism."* |
| `src/aimech/schema/curated_concept.yaml` | `3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f` | `AIMech`, `linkml` | `0` (`[]`) | `0` (`[]`) | Maintained AIMech-native AI concepts (`CuratedAIConcept`) backed by primary literature (`EvidenceSource` + `EvidenceCitation`) and pinned AIO vocabulary alignment (`aio_mappings` or `aio_no_match`). |
| `src/aimech/schema/mech_shared.yaml` | `c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895` | `linkml`, `mech_shared` | `0` (`[]`) | `0` (`[]`) | Vendored cross-fleet shared LinkML module (imported by `aimech.yaml` for `AIConcept.discussions`). Mentions `protein` only in cross-fleet docstrings warning that *"Sharing a protein or a reaction supplies a curation lead, not an assertion of record equivalence or biological mechanism"* (`description` line 23; `CrossCorpusLink.basis` line 226) and in `DatasetTypeEnum.PROTEOMICS` / `DatasetRepositoryEnum.PRIDE` (unreferenced by `AIConcept` and `CuratedAIConcept`). |

---

## 3. Full Corpus Inventory (`1,929` Total Records)

### 3.1 Generated AIO Corpus (`data/aio/*.yaml` — `442` Records)

- **Total records inspected:** `442`
- **Records with protein-example candidate slots:** `0`
- **Records with UniProt CURIEs/accessions (`UniProt:...`, `UniProtKB:...`):** `0`
- **Records matching direct protein/UniProt/proteomics terms (`uniprot`, `swiss-prot`, `trembl`, `protein`, `proteins`, `proteome`, `proteomics`, `peptide`, `amino acid`, `alphafold`, `esmfold`, `rosettafold`, `pdb`):** `0`
- **Records matching broader biological terminology (`biological`):** `3 / 442`
  1. `AIO:ArtificialNeuralNetwork` (`data/aio/ArtificialNeuralNetwork.yaml`, branch `Network`): *"A network based on a collection of connected units called artificial neurons modeled after biological neurons."*
  2. `AIO:SpikingHiddenLayer` (`data/aio/SpikingHiddenLayer.yaml`, branch `Layer`): *"A hidden layer that makes connections to an additional, heterogeneous hidden layer; modeled after biological neural networks."*
  3. `AIO:SurvivalAnalysis` (`data/aio/SurvivalAnalysis.yaml`, branch `MachineLearningTask`): *"A machine learning task focused on methods for analyzing the expected duration of time until one or more events occur such as death in biological organisms or failure in mechanical systems."*

### 3.2 Maintained Curated AI-Concept Corpus (`data/curated/*.yaml` — `1,487` Records)

- **Total records inspected:** `1,487` (`5,149` `ConceptClaim` items; `3,269` `EvidenceSource` entries; `1,338` records with `1,822` `aio_mappings` + `149` records with `aio_no_match`)
- **Records with protein-example candidate slots:** `0`
- **Records with UniProt CURIEs/accessions (`UniProt:...`, `UniProtKB:...`):** `0`
- **Records matching direct protein/UniProt/proteomics terms:** `3 / 1,487` (matching token `protein` only; `0` matches for `uniprot`, `swiss-prot`, `trembl`, `proteome`, `proteomics`, `peptide`, `amino acid`, `alphafold`, `esmfold`, `rosettafold`, `pdb`):
  1. `AIMech:BrandesPichPivotCentralityEstimation` (`data/curated/BrandesPichPivotCentralityEstimation.yaml`, `concept_kind: algorithm`): matches inside `claim_id: evaluation-and-application-scope` (`kind: limitation`), noting that the source paper evaluates pivot strategies on *"protein-interaction, needle-exchange and ticker-text networks"* and explicitly concluding: *"No unified numeric benchmark denominator, unreported weighting rule, universal strategy superiority or biological-function prediction is asserted."*
  2. `AIMech:ZhouAttractorCommunityDetection` (`data/curated/ZhouAttractorCommunityDetection.yaml`, `concept_kind: algorithm`): matches inside `claim_id: evaluation-and-extension-limits` (`kind: limitation`), noting application to *"a historical yeast protein-interaction component"* and explicitly concluding: *"Protein transport, essentiality and functional explanations remain hypotheses rather than causal evidence."*
  3. `AIMech:ZhouRandomWalkDissimilarity` (`data/curated/ZhouRandomWalkDissimilarity.yaml`, `concept_kind: mathematical_method`): matches inside `claim_id: interpretation-and-version-limits` (`kind: limitation`), noting historical *"yeast-network clustering examples"* and explicitly concluding: *"Its performance and protein-function hypotheses concern the full hierarchy pipeline and specific data, not independent validation of this pairwise functional or causal biology."*

---

## 4. Preserving the Ontology, Causality, and Entity-Boundary Distinction

Across all `1,929` AIMech records, ontological axioms, conceptual vocabulary mappings, mathematical/algorithmic mechanism claims, and benchmark dataset contexts are kept strictly distinct from biological UniProt protein instances and causal biology:

1. **Ontology Axioms & Vocabulary Mappings (`data/aio/*.yaml` and `data/curated/*.yaml`):**
   - Generated AIO records carry `442` taxonomic `parents` edges (`rdfs:subClassOf` / `owl:Thing`) and `71` mereological `BFO:0000051` (`has part`) relationships across `26` records (`src/aimech/schema/aimech.yaml`: *"has part; exported ontology axiom, not evidence of causal effect"*).
   - Maintained curated records carry `1,822` `AIOMapping` entries (`1,415` `related_match`, `325` `broad_match`, `82` `narrow_match`) across `1,338` records plus `149` `aio_no_match` records. None reference biological entity ontologies or UniProt accessions.
2. **Prose Algorithmic/Mathematical Mechanism Claims (`2,793` `kind: mechanism` claims):**
   - In `src/aimech/schema/curated_concept.yaml`, `ConceptClaim` items with `kind: mechanism` (`2,793 / 5,149` claims) specify formal mathematical or computational transformations backed by primary literature locators, not molecular or enzymatic mechanisms of UniProt proteins.
3. **Complete Classification of All `95` Curated Records Matching Broader Biological Tokens:**
   - Scanning all `1,487` curated records for any broad biological/bioinformatics/genomic/biomedical token (`uniprot`, `protein`, `gene`, `genes`, `genome`, `genomic`, `genomics`, `dna`, `rna`, `enzyme`, `metabolic`, `bioinformatics`, `biological`, `biomedical`) returns `95` records partitioned into four mutually exclusive non-protein-instance categories:
     1. **Explicit negative-scope or benchmark disclaimers in `limitations` or `claims` (`62` records):** Records whose `limitations` or `kind: limitation` claims explicitly state that the curated AI/graph/statistical method does not establish biological causality, biological function, or experimental biological implementation (including `AIMech:BrandesPichPivotCentralityEstimation`, `AIMech:ZhouAttractorCommunityDetection`, `AIMech:ZhouRandomWalkDissimilarity`, `AIMech:GirvanNewmanCommunityDetection`, `AIMech:AdaBoost`, `AIMech:HelmholtzMachine`, `AIMech:InfomaxICA`, `AIMech:TopographicICA`, `AIMech:WakeSleepAlgorithm`, etc.).
     2. **Bio-inspired optimization and neural-learning metaphors (`10` records):** Evolutionary algorithms, swarm heuristics, and biologically inspired learning rules (`AIMech:AntColonyOptimization`, `AIMech:EstimationOfDistributionAlgorithms`, `AIMech:GeneticAlgorithm`, `AIMech:GuidedGeneticAlgorithm`, `AIMech:OjaLearningRule`, `AIMech:ParticleSwarmOptimization`, `AIMech:RegularizedEvolution`, `AIMech:Stigmergy`, `AIMech:SwarmIntelligence`, `AIMech:UnivariateMarginalDistributionAlgorithm`) where "genes" or "biological" refer to candidate parameter encodings or heuristic metaphors.
     3. **Acronym and homonym collisions (`3` records):** `AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations` and `AIMech:LSvrgAndLKatyushaLooplessVarianceReducedGradientMethods` (where `RNA` abbreviates *Regularized Nonlinear Acceleration*) and `AIMech:GENET` (a constraint-satisfaction neural network architecture explicitly disclaimed as *"not a biological genetic network"*).
     4. **Downstream biomedical, genomic, or ontology evaluation dataset contexts (`20` records):** General-purpose ontology-construction/alignment algorithms, statistical multiple-testing procedures, graphical models, clustering algorithms, and NLP/federated-learning methods (`AIMech:AutoPoissonMarkovRandomField`, `AIMech:BayesOptimalPValueWeightingUnderGaussianPrior`, `AIMech:CliXO`, `AIMech:CovariatePoweredCrossWeightedMultipleTesting`, `AIMech:DARTDifferentiablePromptFewShotTuning`, `AIMech:ExactPoClustering`, `AIMech:FedKdCommunicationEfficientFederatedLearningViaKnowledgeDistillation`, `AIMech:HACE`, `AIMech:HACES`, `AIMech:HACQ`, `AIMech:HiddenMarkovModelWithAuxiliaryMemory`, `AIMech:INLAGroupNodeConflictDiagnostic`, `AIMech:LeftTruncatedCauchyCombinationTest`, `AIMech:MoRA`, `AIMech:NeXOOntologyAlignment`, `AIMech:NeXOOntologyConstruction`, `AIMech:OptimalSpjotvollAndSieveGroupedPValueWeighting`, `AIMech:PARADEPassageRepresentationAggregationForDocumentReranking`, `AIMech:RandomizedLatentScoreConflictDiagnostic`, `AIMech:SupervisedPrincipalComponents`) whose primary papers evaluate or motivate the method on gene-ontology, genomic, RNA secondary-structure, or biomedical text datasets without curating individual UniProt protein instances.

---

## 5. Assessment of Candidate Native Analogues & Governance Recommendation

Stage 3's goal prompt asks:
> *"If a real applicable representation is discovered, report it for review before replacing this applicability objective."*

### Evaluation of Candidate Representations

- **Biological UniProt protein examples (`protein_examples`, `uniprot_id`):** **Inapplicable (`not_applicable`).** AIMech curates artificial intelligence, machine learning, and statistical concepts (`AIConcept` and `CuratedAIConcept`) rather than biological genes, proteins, microbial traits, or clinical pathways. Inventing UniProt accessions or unsupported biological fields would violate AIMech's schema and domain boundaries.
- **AI methods applied to computational biology / protein modeling:** Even when AIMech curates AI architectures or algorithms used in computational biology (e.g., ontology extraction such as `AIMech:CliXO` / `AIMech:NeXOOntologyConstruction` or future protein language models / equivariant structure-prediction architectures), the curated entity in AIMech is the **computational method, architecture, or model family** (`CuratedAIConcept`), and any empirical benchmark dataset belongs in `EvaluationContext.dataset_and_split` attached to a `performance` claim rather than a biological `protein_examples` slot.
- **Conclusion:** No applicable biological UniProt protein-example representation exists in AIMech's schemas or corpus. Stage 3 (`protein_examples`) should remain `not_applicable` (`applicability: not_applicable`) in `workflow/mech-workflow.yaml`.
