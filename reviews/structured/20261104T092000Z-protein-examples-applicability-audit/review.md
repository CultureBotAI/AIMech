# Stage 3 applicability audit of biological UniProt protein examples across AIMech LinkML schemas and 1,929-record AI-concept corpus

- Review: 20261104T092000Z-protein-examples-applicability-audit
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-11-04T09:10:00Z
- Finished UTC: 2026-11-04T09:20:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Biological UniProt protein examples (protein_examples, uniprot_id, UniProtKB accessions, gene symbols, and molecular/enzymatic target annotations) remain not_applicable to AIMech's native AI-concept domain and LinkML schemas. A deterministic full-corpus and schema audit (research/validation/20261104T091000Z-protein-examples-applicability-audit.py and .json) across all three LinkML schema modules (src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml, src/aimech/schema/mech_shared.yaml) and all 1,929 YAML corpus records (442 generated data/aio/*.yaml records and 1,487 maintained data/curated/*.yaml records) confirms zero biological entity prefixes (UniProt, UniProtKB, HGNC, NCBIGene, GO, PR, PDB), zero protein-example or gene-example slots, and zero UniProt CURIEs/accessions across the entire corpus. Across all 442 generated AIO records, 0 records mention proteins or UniProt and only 3 mention biological to contrast artificial neural units with biological neurons or note time-to-event subjects. Across all 1,487 maintained curated AI-concept records, only 3 records (AIMech:BrandesPichPivotCentralityEstimation, AIMech:ZhouAttractorCommunityDetection, AIMech:ZhouRandomWalkDissimilarity) mention the token protein, and all 3 do so exclusively inside kind=limitation claims disclaiming biological-function prediction or causal biology from historical yeast protein-interaction network evaluations. All 95 curated records matching broad biological/bioinformatics/genomic/biomedical tokens are deterministically partitioned into four non-protein-instance categories: 62 negative-scope or benchmark disclaimers, 10 bio-inspired optimization/neural-learning metaphors, 3 acronym/homonym collisions, and 20 downstream biomedical/genomic/ontology evaluation dataset contexts.

## Scope And Provenance

Full-corpus and LinkML schema applicability audit of Stage 3 (protein_examples) across src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml, src/aimech/schema/mech_shared.yaml, all 442 generated data/aio/*.yaml records, and all 1,487 maintained data/curated/*.yaml records.

Selection: All 3 AIMech LinkML schema modules plus the deterministic full-corpus (1,929 records) UniProt protein-example applicability audit bundle
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 692bc9e12d08ec5df65d7773fa613fccd6444090.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:schema-aimech | src/aimech/schema/aimech.yaml | maintained | AIMech generated AIO concept LinkML schema |
| AIMech:schema-curated-concept | src/aimech/schema/curated_concept.yaml | maintained | AIMech maintained curated AI concept LinkML schema |
| AIMech:schema-mech-shared | src/aimech/schema/mech_shared.yaml | maintained | Imported cross-Mech shared provenance LinkML schema |
| AIMech:protein-examples-applicability-audit | research/validation/20261104T091000Z-protein-examples-applicability-audit.json | maintained | Full-corpus (1,929 records) and schema UniProt protein-example applicability audit |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech corpus, curated, seed, and history validation suite | passed | True | AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:schema-mech-shared, AIMech:protein-examples-applicability-audit | Checked 442 record(s); 0 failed.<br>Checked 1487 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 1126 history record(s); 0 error(s).<br> |
| check_vendored_sync.py | passed | True | AIMech:schema-mech-shared, AIMech:protein-examples-applicability-audit | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:schema-aimech, AIMech:protein-examples-applicability-audit | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:schema-mech-shared, AIMech:protein-examples-applicability-audit | Exited 0 without output. |
| pytest tests/test_curated.py | passed | True | AIMech:schema-curated-concept, AIMech:protein-examples-applicability-audit | ..............................................                           [100%]<br>46 passed in 3.24s<br> |
| Deterministic full-corpus and schema UniProt protein-example applicability audit | passed | True | AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:schema-mech-shared, AIMech:protein-examples-applicability-audit | Audited 3 LinkML schema modules and 1,929 YAML corpus records (442 AIO + 1,487 curated); 0 biological prefixes or protein-example candidate slots in schemas, 0 records with protein-example slots or UniProt CURIEs, applicability=not_applicable. |
| post-save structured review corpus check | skipped | False | AIMech:protein-examples-applicability-audit | Skipped at the moment this review input YAML is serialized prior to &#96;record_review.py save&#96;; executed as a mandatory post-save gate immediately after &#96;record_review.py save&#96; writes &#96;reviews/structured/20261104T092000Z-protein-examples-applicability-audit/review.yaml&#96; and &#96;review.md&#96;. |

## Scientific And Domain Assessments

### Absence of biological entity prefixes and UniProt protein-example slots across AIMech LinkML schemas

schema: supported. Targets: AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:schema-mech-shared.

All three LinkML schema modules (src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml, and src/aimech/schema/mech_shared.yaml) declare zero biological entity prefixes (UniProt, UniProtKB, HGNC, NCBIGene, GO, PR, PDB) and zero protein-example or gene-example slots. In mech_shared.yaml, protein appears only in cross-fleet docstrings warning against treating shared proteins as biological mechanisms or record equivalence and in DatasetTypeEnum.PROTEOMICS (unreferenced by AIConcept and CuratedAIConcept).

### Preservation of the ontology, causality, and entity-boundary distinction across all 1,929 AIMech corpus records

representation: supported. Targets: AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:protein-examples-applicability-audit.

Across all 1,929 corpus records (442 generated AIO records and 1,487 maintained curated records), zero records contain protein-example fields or UniProt CURIEs/accessions. Zero AIO records mention proteins or UniProt, and the only 3 curated records mentioning the token protein (AIMech:BrandesPichPivotCentralityEstimation, AIMech:ZhouAttractorCommunityDetection, AIMech:ZhouRandomWalkDissimilarity) do so exclusively inside kind=limitation claims disclaiming biological-function prediction or causal biology from historical yeast protein-interaction network evaluations. All 95 curated records matching broad biological tokens partition cleanly into negative-scope/benchmark disclaimers (62), bio-inspired metaphors (10), acronym/homonym collisions (3), and downstream dataset contexts (20).

### Evaluation of AI-for-biology method curation vs biological UniProt protein examples and Stage 3 objective retention

scope: supported. Targets: AIMech:schema-aimech, AIMech:schema-curated-concept, AIMech:schema-mech-shared, AIMech:protein-examples-applicability-audit.

Biological UniProt protein examples do not apply to AIMech's AI-concept domain or schemas, and inventing biological data or unsupported fields would violate repository constraints. Even when AIMech curates AI methods used in computational biology (such as ontology construction/alignment algorithms like AIMech:CliXO and AIMech:NeXOOntologyConstruction or future protein language models), the curated record represents the computational method under CuratedAIConcept (with empirical datasets captured in EvaluationContext.dataset_and_split when performance claims are curated), never biological UniProt protein instances. Stage 3 (protein_examples) remains not_applicable in workflow/mech-workflow.yaml.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| schema-aimech-ev | src/aimech/schema/aimech.yaml; lines 1-146 (prefixes, AIConcept, ConceptRelationship, RelationshipPredicate) | supports | Defines prefixes (linkml, aimech, AIO), AIConcept (16 slots), and ConceptRelationship (predicate BFO:0000051 only) for generated AIO records. Declares zero biological prefixes (UniProt, UniProtKB, HGNC, NCBIGene, GO, PR, PDB) and zero protein-example or gene-example slots. |
| schema-curated-ev | src/aimech/schema/curated_concept.yaml; lines 1-185 (prefixes, CuratedAIConcept, ConceptClaim, EvaluationContext, ConceptKind, ClaimKind) | supports | Defines prefixes (linkml, AIMech), CuratedAIConcept (16 slots), ConceptKind (14 AI/ML/statistical methodological kinds), and EvaluationContext (task, dataset_and_split, model_and_version, metric_and_units, result, baseline, conditions, uncertainty). Declares zero biological prefixes and zero protein-example or gene-example slots. |
| schema-shared-ev | src/aimech/schema/mech_shared.yaml; lines 1-382 (description, prefixes, DatasetTypeEnum, CrossCorpusLink, Discussion) | supports | Vendored cross-fleet shared provenance schema imported by aimech.yaml for AIConcept.discussions. Mentions the word protein only in cross-fleet docstrings warning that sharing a protein supplies a curation lead rather than biological mechanism or record equivalence (lines 23 and 226) and in DatasetTypeEnum.PROTEOMICS (unreferenced by AIConcept or CuratedAIConcept). Declares zero biological prefixes and zero protein-example slots. |
| audit-script | research/validation/20261104T091000Z-protein-examples-applicability-audit.py; lines 1-489 (build_audit_report, audit_schema, audit_aio_corpus, audit_curated_corpus, classify_broad_biological_record) | supports | Deterministic Python audit script inspecting all 3 LinkML schema modules, all 442 generated data/aio/*.yaml records, and all 1,487 maintained data/curated/*.yaml records for candidate biological prefixes, protein-example slots, UniProt CURIEs, direct protein/proteomics tokens, and broad biological/genomic/bioinformatics terminology. |
| audit-json | research/validation/20261104T091000Z-protein-examples-applicability-audit.json; applicability_verdict, corpus_totals, aio_corpus_inventory, curated_corpus_inventory, ontology_and_entity_boundary_distinction | supports | Structured JSON output confirming 1,929 total records (442 AIO + 1,487 curated), 0 biological prefixes or protein-example slots in schemas or records, 0 UniProt CURIEs, 0 AIO records and 3 curated records matching direct protein terms (all 3 inside limitation claims disclaiming biological-function/causal-biology assertions), and an exact 4-category partition (62 + 10 + 3 + 20 = 95) of all 95 curated records matching broad biological tokens. |
| corpus-search | research/validation/20261104T091000Z-protein-examples-applicability-audit.md; Sections 2-5 | supports | Full-corpus slot, CURIE, and regex search across all 442 data/aio/*.yaml and 1,487 data/curated/*.yaml files (including representative records AIO:ArtificialNeuralNetwork, AIO:SpikingHiddenLayer, AIO:SurvivalAnalysis, AIMech:BrandesPichPivotCentralityEstimation, AIMech:ZhouAttractorCommunityDetection, AIMech:ZhouRandomWalkDissimilarity, AIMech:CliXO, AIMech:GeneticAlgorithm, AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations) confirming that biological/protein terms appear only as negative-scope disclaimers, bio-inspired metaphors, acronym homonyms, or downstream benchmark dataset contexts. |
| validation-suite | workflow/mech-workflow.yaml; stages[2] (stage 3 protein_examples, lines 39-52) | supports | All AIMech validation checks passed (442 AIO records, 1,487 curated records, 1,126 history records, 22 governed artifacts, 46 curated pytest tests) and workflow/mech-workflow.yaml validates cleanly with protein_examples applicability: not_applicable. |

## Limits And Additional Notes

- Author self-review of the Stage 3 full-corpus and schema UniProt protein-example applicability audit; independent adversarial PR review is required prior to merge.
- Full-corpus inventory inspects schema structure, prefixes, slot usage, CURIE patterns, and protein/biological terminology across all 1,929 records rather than re-verifying every individual primary-source paper locator across all 5,149 curated claims.
- Corroborates infrastructure task aimech-infra-0002 (https://github.com/CultureBotAI/AIMech/issues/431) across all 1,929 records (442 data/aio/*.yaml + 1,487 data/curated/*.yaml) at Cycle 1 Stage 3.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T092000Z-protein-examples-applicability-audit
kind: repository
repository: CultureBotAI/AIMech
title: Stage 3 applicability audit of biological UniProt protein examples across AIMech
  LinkML schemas and 1,929-record AI-concept corpus
started_at: '2026-11-04T09:10:00Z'
finished_at: '2026-11-04T09:20:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini 4 Argon
  independence: self_review
  independence_basis: Author self-review of the Stage 3 (protein_examples) full-corpus
    and LinkML schema applicability audit for run mech-goal-sequence-20261019, cycle
    1, stage 3; does not substitute for independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Biological UniProt protein examples (protein_examples, uniprot_id, UniProtKB
  accessions, gene symbols, and molecular/enzymatic target annotations) remain not_applicable
  to AIMech''s native AI-concept domain and LinkML schemas. A deterministic full-corpus
  and schema audit (research/validation/20261104T091000Z-protein-examples-applicability-audit.py
  and .json) across all three LinkML schema modules (src/aimech/schema/aimech.yaml,
  src/aimech/schema/curated_concept.yaml, src/aimech/schema/mech_shared.yaml) and
  all 1,929 YAML corpus records (442 generated data/aio/*.yaml records and 1,487 maintained
  data/curated/*.yaml records) confirms zero biological entity prefixes (UniProt,
  UniProtKB, HGNC, NCBIGene, GO, PR, PDB), zero protein-example or gene-example slots,
  and zero UniProt CURIEs/accessions across the entire corpus. Across all 442 generated
  AIO records, 0 records mention proteins or UniProt and only 3 mention biological
  to contrast artificial neural units with biological neurons or note time-to-event
  subjects. Across all 1,487 maintained curated AI-concept records, only 3 records
  (AIMech:BrandesPichPivotCentralityEstimation, AIMech:ZhouAttractorCommunityDetection,
  AIMech:ZhouRandomWalkDissimilarity) mention the token protein, and all 3 do so exclusively
  inside kind=limitation claims disclaiming biological-function prediction or causal
  biology from historical yeast protein-interaction network evaluations. All 95 curated
  records matching broad biological/bioinformatics/genomic/biomedical tokens are deterministically
  partitioned into four non-protein-instance categories: 62 negative-scope or benchmark
  disclaimers, 10 bio-inspired optimization/neural-learning metaphors, 3 acronym/homonym
  collisions, and 20 downstream biomedical/genomic/ontology evaluation dataset contexts.'
source:
  git_revision: 692bc9e12d08ec5df65d7773fa613fccd6444090
  state: working_tree
  inputs:
  - path: INFRA_TASKS.md
    sha256: b4db9fd977b90021262ca539f14394558bfd0b02dd91b6d7ba05224517cc4202
    role: context
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/SpikingHiddenLayer.yaml
    sha256: 4e15ae925a6de1ca58fa90c0bedb159dbb6c36a588816bec83df40a3899b5a65
    role: context
  - path: data/aio/SurvivalAnalysis.yaml
    sha256: 15110144a2f471cd0005fd8d3de7efdde478a51e5753c547e0cdbc6cd6eeb881
    role: context
  - path: data/curated/BrandesPichPivotCentralityEstimation.yaml
    sha256: 7f8492fc3a881da6c35439412b535572f687215410b85b05439d2ca8d799b9c1
    role: context
  - path: data/curated/CliXO.yaml
    sha256: 68a4f69aab547e5d7c0bded8104c312b719d3f5cad62941e8c44ed697fd61fa8
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/RegularizedNonlinearAccelerationOfFixedPointIterations.yaml
    sha256: 5bf7cbb5842ded4e74f9409269b6006f43f17e62ba6f10c3738cc02d15a4fbf7
    role: context
  - path: data/curated/ZhouAttractorCommunityDetection.yaml
    sha256: 5c9e1ef015d93e705d8091714a911c5c0df1a52cf51fb7904b2833cd85d85a15
    role: context
  - path: data/curated/ZhouRandomWalkDissimilarity.yaml
    sha256: 6f454bccc8f4836f493967732cc2bb1925a4fef13dad52880cda1332edf52497
    role: context
  - path: history/reports/protein-examples-applicability-audit/2026-11-04T091745Z-antigravity-95e968.yaml
    sha256: 51a71362288eb138b4ba041d852eb0ff848ee9274345946fbacc74b80e847102
    role: context
  - path: research/validation/20261104T091000Z-protein-examples-applicability-audit.json
    sha256: 4501738cdc176915b301d6b8e1e8f5560b0e68a2c7e85b5315b49500ea5c61b0
    role: target
  - path: research/validation/20261104T091000Z-protein-examples-applicability-audit.md
    sha256: 348911fc91e97951bf0d818d0a9e8f9a8a5a6c68124c7f4527b52db366a95a77
    role: context
  - path: research/validation/20261104T091000Z-protein-examples-applicability-audit.py
    sha256: 217b5344c0aaff7d4d871e072c4cf8dd0f8117f09d940c25d4b36bf0e0ec93ec
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/importer.py
    sha256: 7c2dd8e12f18b76cfb5ed4acc7e1901ae9a968b3a6c7a9d62cb260bc2f1ad3ab
    role: context
  - path: src/aimech/schema/aimech.yaml
    sha256: 5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852
    role: target
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: target
  - path: src/aimech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: target
  - path: workflow/mech-workflow.yaml
    sha256: 1f4575151090b50346fa5b8e75b9bfa0ef42b189350ba2d772516de6431671f8
    role: context
targets:
- target_id: AIMech:schema-aimech
  path: src/aimech/schema/aimech.yaml
  label: AIMech generated AIO concept LinkML schema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/schema/aimech.yaml
    role: maintained
- target_id: AIMech:schema-curated-concept
  path: src/aimech/schema/curated_concept.yaml
  label: AIMech maintained curated AI concept LinkML schema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/schema/curated_concept.yaml
    role: maintained
- target_id: AIMech:schema-mech-shared
  path: src/aimech/schema/mech_shared.yaml
  label: Imported cross-Mech shared provenance LinkML schema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: src/aimech/schema/mech_shared.yaml
    role: maintained
- target_id: AIMech:protein-examples-applicability-audit
  path: research/validation/20261104T091000Z-protein-examples-applicability-audit.json
  label: Full-corpus (1,929 records) and schema UniProt protein-example applicability
    audit
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: research/validation/20261104T091000Z-protein-examples-applicability-audit.py
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/validation/20261104T091000Z-protein-examples-applicability-audit.json
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/validation/20261104T091000Z-protein-examples-applicability-audit.md
    role: maintained
scope:
  description: Full-corpus and LinkML schema applicability audit of Stage 3 (protein_examples)
    across src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml,
    src/aimech/schema/mech_shared.yaml, all 442 generated data/aio/*.yaml records,
    and all 1,487 maintained data/curated/*.yaml records.
  selection: All 3 AIMech LinkML schema modules plus the deterministic full-corpus
    (1,929 records) UniProt protein-example applicability audit bundle
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  exclusions:
  - target: Record-by-record primary-literature line re-verification across all 1,487
      curated records
    reason: Stage 3 audits schema and full-corpus UniProt protein-example applicability
      and ontology/causality/entity boundaries rather than re-reviewing every individual
      paper locator across all 5,149 claims.
  - target: Hypothetical future curation of computational-biology AI methods
    reason: Assessed as conceptual domain scope only; any future AI-for-biology method
      records would be curated as AI architectures/algorithms under CuratedAIConcept
      rather than biological UniProt protein records.
checks:
- check_id: required-0
  name: aimech corpus, curated, seed, and history validation suite
  command: PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate && PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated && PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check && PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base origin/main
  status: passed
  required: true
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    Checked 1487 curated concept record(s); 0 error(s).

    AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    Checked 1126 history record(s); 0 error(s).

    '
  evidence_ids:
  - validation-suite
- check_id: required-1
  name: check_vendored_sync.py
  command: PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    scripts/check_vendored_sync.py
  status: passed
  required: true
  target_ids:
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    '
  evidence_ids:
  - validation-suite
- check_id: required-2
  name: aimech check-source
  command: PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:schema-aimech
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
  evidence_ids:
  - validation-suite
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
  evidence_ids:
  - validation-suite
- check_id: curated-pytest
  name: pytest tests/test_curated.py
  command: PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python
    -m pytest tests/test_curated.py -q
  status: passed
  required: true
  target_ids:
  - AIMech:schema-curated-concept
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: '..............................................                           [100%]

    46 passed in 3.24s

    '
  evidence_ids:
  - validation-suite
- check_id: protein-examples-audit-script
  name: Deterministic full-corpus and schema UniProt protein-example applicability
    audit
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python research/validation/20261104T091000Z-protein-examples-applicability-audit.py
    --output research/validation/20261104T091000Z-protein-examples-applicability-audit.json
  status: passed
  required: true
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  exit_code: 0
  expected_exit_code: 0
  summary: Audited 3 LinkML schema modules and 1,929 YAML corpus records (442 AIO
    + 1,487 curated); 0 biological prefixes or protein-example candidate slots in
    schemas, 0 records with protein-example slots or UniProt CURIEs, applicability=not_applicable.
  evidence_ids:
  - audit-json
  - audit-script
- check_id: post-save-review-check
  name: post-save structured review corpus check
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/AIMech/.venv/bin/python scripts/record_review.py
    --repo-root . --schema schema/record_review.yaml check --base origin/main
  status: skipped
  required: false
  target_ids:
  - AIMech:protein-examples-applicability-audit
  summary: Skipped at the moment this review input YAML is serialized prior to `record_review.py
    save`; executed as a mandatory post-save gate immediately after `record_review.py
    save` writes `reviews/structured/20261104T092000Z-protein-examples-applicability-audit/review.yaml`
    and `review.md`.
evidence:
- evidence_id: schema-aimech-ev
  kind: record_content
  reference: src/aimech/schema/aimech.yaml
  locator: lines 1-146 (prefixes, AIConcept, ConceptRelationship, RelationshipPredicate)
  accessed_at: '2026-11-04T09:15:00Z'
  snapshot_sha256: 5a54dafe2fc17bc027e14bc3a2829b265cbb34427ad58eef63fe99616e17b852
  support: supports
  summary: Defines prefixes (linkml, aimech, AIO), AIConcept (16 slots), and ConceptRelationship
    (predicate BFO:0000051 only) for generated AIO records. Declares zero biological
    prefixes (UniProt, UniProtKB, HGNC, NCBIGene, GO, PR, PDB) and zero protein-example
    or gene-example slots.
- evidence_id: schema-curated-ev
  kind: record_content
  reference: src/aimech/schema/curated_concept.yaml
  locator: lines 1-185 (prefixes, CuratedAIConcept, ConceptClaim, EvaluationContext,
    ConceptKind, ClaimKind)
  accessed_at: '2026-11-04T09:15:00Z'
  snapshot_sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
  support: supports
  summary: Defines prefixes (linkml, AIMech), CuratedAIConcept (16 slots), ConceptKind
    (14 AI/ML/statistical methodological kinds), and EvaluationContext (task, dataset_and_split,
    model_and_version, metric_and_units, result, baseline, conditions, uncertainty).
    Declares zero biological prefixes and zero protein-example or gene-example slots.
- evidence_id: schema-shared-ev
  kind: record_content
  reference: src/aimech/schema/mech_shared.yaml
  locator: lines 1-382 (description, prefixes, DatasetTypeEnum, CrossCorpusLink, Discussion)
  accessed_at: '2026-11-04T09:15:00Z'
  snapshot_sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
  support: supports
  summary: Vendored cross-fleet shared provenance schema imported by aimech.yaml for
    AIConcept.discussions. Mentions the word protein only in cross-fleet docstrings
    warning that sharing a protein supplies a curation lead rather than biological
    mechanism or record equivalence (lines 23 and 226) and in DatasetTypeEnum.PROTEOMICS
    (unreferenced by AIConcept or CuratedAIConcept). Declares zero biological prefixes
    and zero protein-example slots.
- evidence_id: audit-script
  kind: validation
  reference: research/validation/20261104T091000Z-protein-examples-applicability-audit.py
  locator: lines 1-489 (build_audit_report, audit_schema, audit_aio_corpus, audit_curated_corpus,
    classify_broad_biological_record)
  accessed_at: '2026-11-04T09:18:00Z'
  snapshot_sha256: 217b5344c0aaff7d4d871e072c4cf8dd0f8117f09d940c25d4b36bf0e0ec93ec
  support: supports
  summary: Deterministic Python audit script inspecting all 3 LinkML schema modules,
    all 442 generated data/aio/*.yaml records, and all 1,487 maintained data/curated/*.yaml
    records for candidate biological prefixes, protein-example slots, UniProt CURIEs,
    direct protein/proteomics tokens, and broad biological/genomic/bioinformatics
    terminology.
- evidence_id: audit-json
  kind: validation
  reference: research/validation/20261104T091000Z-protein-examples-applicability-audit.json
  locator: applicability_verdict, corpus_totals, aio_corpus_inventory, curated_corpus_inventory,
    ontology_and_entity_boundary_distinction
  accessed_at: '2026-11-04T09:18:00Z'
  snapshot_sha256: 4501738cdc176915b301d6b8e1e8f5560b0e68a2c7e85b5315b49500ea5c61b0
  support: supports
  summary: Structured JSON output confirming 1,929 total records (442 AIO + 1,487
    curated), 0 biological prefixes or protein-example slots in schemas or records,
    0 UniProt CURIEs, 0 AIO records and 3 curated records matching direct protein
    terms (all 3 inside limitation claims disclaiming biological-function/causal-biology
    assertions), and an exact 4-category partition (62 + 10 + 3 + 20 = 95) of all
    95 curated records matching broad biological tokens.
- evidence_id: corpus-search
  kind: search
  reference: research/validation/20261104T091000Z-protein-examples-applicability-audit.md
  locator: Sections 2-5
  accessed_at: '2026-11-04T09:18:00Z'
  snapshot_sha256: 348911fc91e97951bf0d818d0a9e8f9a8a5a6c68124c7f4527b52db366a95a77
  support: supports
  summary: Full-corpus slot, CURIE, and regex search across all 442 data/aio/*.yaml
    and 1,487 data/curated/*.yaml files (including representative records AIO:ArtificialNeuralNetwork,
    AIO:SpikingHiddenLayer, AIO:SurvivalAnalysis, AIMech:BrandesPichPivotCentralityEstimation,
    AIMech:ZhouAttractorCommunityDetection, AIMech:ZhouRandomWalkDissimilarity, AIMech:CliXO,
    AIMech:GeneticAlgorithm, AIMech:RegularizedNonlinearAccelerationOfFixedPointIterations)
    confirming that biological/protein terms appear only as negative-scope disclaimers,
    bio-inspired metaphors, acronym homonyms, or downstream benchmark dataset contexts.
  search_scope: All 3 LinkML schema files in src/aimech/schema/, all 442 generated
    YAML records in data/aio/, and all 1,487 maintained YAML records in data/curated/
    (tracked repository files; gitignored files excluded).
- evidence_id: validation-suite
  kind: validation
  reference: workflow/mech-workflow.yaml
  locator: stages[2] (stage 3 protein_examples, lines 39-52)
  accessed_at: '2026-11-04T09:18:00Z'
  snapshot_sha256: 1f4575151090b50346fa5b8e75b9bfa0ef42b189350ba2d772516de6431671f8
  support: supports
  summary: 'All AIMech validation checks passed (442 AIO records, 1,487 curated records,
    1,126 history records, 22 governed artifacts, 46 curated pytest tests) and workflow/mech-workflow.yaml
    validates cleanly with protein_examples applicability: not_applicable.'
assessments:
- assessment_id: schema-protein-examples-inapplicability
  area: schema
  topic: Absence of biological entity prefixes and UniProt protein-example slots across
    AIMech LinkML schemas
  outcome: supported
  summary: All three LinkML schema modules (src/aimech/schema/aimech.yaml, src/aimech/schema/curated_concept.yaml,
    and src/aimech/schema/mech_shared.yaml) declare zero biological entity prefixes
    (UniProt, UniProtKB, HGNC, NCBIGene, GO, PR, PDB) and zero protein-example or
    gene-example slots. In mech_shared.yaml, protein appears only in cross-fleet docstrings
    warning against treating shared proteins as biological mechanisms or record equivalence
    and in DatasetTypeEnum.PROTEOMICS (unreferenced by AIConcept and CuratedAIConcept).
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  evidence_ids:
  - schema-aimech-ev
  - schema-curated-ev
  - schema-shared-ev
  - audit-json
  metrics:
  - name: schema_protein_example_slots
    value: 0.0
    unit: count
    definition: Count of UniProt protein-example or biological gene/protein target
      slots declared across all 3 AIMech LinkML schemas.
    denominator: 3
    minimum: 0.0
    maximum: 3.0
  dimensions:
  - name: StageApplicability
    value: not_applicable
    definition: Configured Stage 3 (protein_examples) applicability status in workflow/mech-workflow.yaml.
    evidence_ids:
    - validation-suite
    - audit-json
- assessment_id: ontology-and-entity-boundary
  area: representation
  topic: Preservation of the ontology, causality, and entity-boundary distinction
    across all 1,929 AIMech corpus records
  outcome: supported
  summary: Across all 1,929 corpus records (442 generated AIO records and 1,487 maintained
    curated records), zero records contain protein-example fields or UniProt CURIEs/accessions.
    Zero AIO records mention proteins or UniProt, and the only 3 curated records mentioning
    the token protein (AIMech:BrandesPichPivotCentralityEstimation, AIMech:ZhouAttractorCommunityDetection,
    AIMech:ZhouRandomWalkDissimilarity) do so exclusively inside kind=limitation claims
    disclaiming biological-function prediction or causal biology from historical yeast
    protein-interaction network evaluations. All 95 curated records matching broad
    biological tokens partition cleanly into negative-scope/benchmark disclaimers
    (62), bio-inspired metaphors (10), acronym/homonym collisions (3), and downstream
    dataset contexts (20).
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:protein-examples-applicability-audit
  evidence_ids:
  - schema-aimech-ev
  - schema-curated-ev
  - audit-script
  - audit-json
  - corpus-search
  metrics:
  - name: corpus_records_inspected
    value: 1929.0
    unit: records
    definition: Total YAML records inspected across data/aio/*.yaml (442) and data/curated/*.yaml
      (1,487).
    denominator: 1929
    minimum: 0.0
    maximum: 1929.0
  - name: records_with_protein_example_slots
    value: 0.0
    unit: records
    definition: Count of AIMech corpus records containing UniProt protein-example
      slots or UniProt CURIEs/accessions.
    denominator: 1929
    minimum: 0.0
    maximum: 1929.0
  dimensions:
  - name: CorpusScope
    value: full_corpus_1929_records
    definition: Complete inventory of 442 generated AIO records and 1,487 maintained
      curated AI-concept records.
    evidence_ids:
    - audit-json
    - corpus-search
- assessment_id: candidate-native-representation-governance
  area: scope
  topic: Evaluation of AI-for-biology method curation vs biological UniProt protein
    examples and Stage 3 objective retention
  outcome: supported
  summary: Biological UniProt protein examples do not apply to AIMech's AI-concept
    domain or schemas, and inventing biological data or unsupported fields would violate
    repository constraints. Even when AIMech curates AI methods used in computational
    biology (such as ontology construction/alignment algorithms like AIMech:CliXO
    and AIMech:NeXOOntologyConstruction or future protein language models), the curated
    record represents the computational method under CuratedAIConcept (with empirical
    datasets captured in EvaluationContext.dataset_and_split when performance claims
    are curated), never biological UniProt protein instances. Stage 3 (protein_examples)
    remains not_applicable in workflow/mech-workflow.yaml.
  target_ids:
  - AIMech:schema-aimech
  - AIMech:schema-curated-concept
  - AIMech:schema-mech-shared
  - AIMech:protein-examples-applicability-audit
  evidence_ids:
  - audit-json
  - corpus-search
  - validation-suite
findings: []
actions: []
limitations:
- Author self-review of the Stage 3 full-corpus and schema UniProt protein-example
  applicability audit; independent adversarial PR review is required prior to merge.
- Full-corpus inventory inspects schema structure, prefixes, slot usage, CURIE patterns,
  and protein/biological terminology across all 1,929 records rather than re-verifying
  every individual primary-source paper locator across all 5,149 curated claims.
notes:
- Corroborates infrastructure task aimech-infra-0002 (https://github.com/CultureBotAI/AIMech/issues/431)
  across all 1,929 records (442 data/aio/*.yaml + 1,487 data/curated/*.yaml) at Cycle
  1 Stage 3.
links:
- https://github.com/CultureBotAI/AIMech/issues/431
tags:
- protein_examples
- uniprot
- applicability_audit
- schema_boundary
- stage_3
```
